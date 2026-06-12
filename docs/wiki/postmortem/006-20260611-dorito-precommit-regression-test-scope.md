---
doc_id: postmortem-006-precommit-regression-test-scope
id: postmortem-006-precommit-regression-test-scope
seq: 6
title: "느린 pre-commit 훅, 범인은 preflight가 아니라 회귀 테스트였다"
doc_type: postmortem
type: postmortem
stage: reference
status: reference
wiki_status: active
evidence_role: provenance
depends_on:
  - postmortem-003-qfuds-scope-demotion-retrospective
next_gate: none; process history only — does not change roadmap status or promote evidence
date: 2026-06-11
context: 커밋할 때마다 pre-commit 훅이 느리다는 체감에서 출발 — preflight_exp004.py 제거 검토 중 실제 병목 측정
audience: 주니어 개발자
length: 작업 단계별 풀어쓰기
created_at: 2026-06-11
created_by: dorito
updated_at: 2026-06-11
updated_by: dorito
last_updated: 2026-06-11
last_verified_at: 2026-06-11
last_verified_by: dorito
audit_log:
  - action: created
    at: 2026-06-11
    by: dorito
    note: "pre-commit 훅 속도 진단 직후, 회귀 테스트 조건부 실행으로 고친 뒤 작성"
tags: [postmortem, git-hooks, pre-commit, performance, testing]
relations:
  - AGENTS.md
  - docs/05_next_steps/000_roadmap.md
code_refs:
  - file: scripts/git-hooks/pre-commit
    note: "정본 훅 — 회귀 스위트를 qfuds//tests/ 변경 시에만 실행하도록 조건부화"
  - file: .git/hooks/pre-commit
    note: "설치본 — 정본과 동일하게 반영 (추적되지 않으므로 따로 수정 필요)"
---

# 느린 pre-commit 훅, 범인은 preflight가 아니라 회귀 테스트였다

## 사건 한 줄 요약

커밋이 느려서 `scripts/preflight_exp004.py`를 의심해 빼려 했지만, 실제
측정 결과 그 스크립트는 0.08초였고 느림의 95%는 마지막 단계인 수치 회귀
테스트(4.2초)였다. 엉뚱한 파일을 째려던 것을, 측정으로 바로잡고 회귀
테스트를 "실험 코드가 바뀐 커밋에서만" 돌도록 조건부화했다.

---

## 0. 사전 지식

읽기 전에 알아야 할 것만.

| 용어 | 뜻 |
| --- | --- |
| pre-commit 훅 | `git commit` 실행 직전에 자동으로 도는 스크립트. 0이 아닌 종료코드를 내면 커밋이 막힌다. |
| 정본 vs 설치본 | 이 repo는 훅 원본을 `scripts/git-hooks/pre-commit`에 추적해 두고, 실제 동작하는 복사본은 추적되지 않는 `.git/hooks/pre-commit`에 둔다. **둘은 자동 동기화되지 않는다.** |
| 회귀 테스트(regression test) | 코드가 바뀌었을 때 *예전에 맞던 결과가 깨지지 않았나*를 확인하는 테스트. 이 repo에선 실험 스위트(`qfuds/`)를 다시 돌려 기록된 outputs와 맞는지 검사한다. |
| `unittest discover` | `tests/` 아래 `test_*.py`를 모두 찾아 한 프로세스에서 실행하는 파이썬 표준 러너. |

핵심 함정 하나: **"느리다"는 체감은 어느 단계가 느린지 말해주지 않는다.**
훅은 6단계를 순서대로 도는데, 그중 눈에 띄는(=가장 최근에 추가한) 파일을
범인으로 지목하기 쉽다. 측정 없이 지목하면 틀린다.

---

## 1. 증상

- 체감: "커밋할 때마다 pre-commit 훅이 너무 느리다."
- 지목된 용의자: `scripts/preflight_exp004.py` (exp_003 기록 일관성 게이트).
  이름이 거창하고 문서 전체를 훑는 스크립트라 느려 보였다.
- 요청: "걍 뺄까?"

당시 pre-commit 훅(`.git/hooks/pre-commit`)은 이랬다:

```sh
python3 scripts/update_frontmatter_last_updated.py --staged
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/preflight_exp004.py
git diff --check
python3 -m unittest discover -s tests -p 'test_*.py'
```

---

## 2. 첫 의문 + 가설

> "preflight를 빼면 빨라질까? 아니면 애초에 다른 단계가 느린 걸까?"

| id | 가설 | 왜 그럴 수 있는지 | 어떻게 확인할지 |
| --- | --- | --- | --- |
| H1 | preflight_exp004.py가 느리다 | 문서 전체를 `rglob`로 두 번 훑는다 (192개 md) | 그 스크립트 단독 실행 시간 측정 |
| H2 | 진짜 병목은 다른 단계다 | 훅엔 6단계가 있고 마지막은 테스트 스위트다 | 각 단계를 따로 시간 측정해 비교 |
| H3 | 병목은 수치 테스트의 실제 계산이다 | 실험 스위트는 적분/수치계산 + 디스크 쓰기를 한다 | 테스트를 모듈별로 쪼개 측정 |

검증 순서는 가장 싸고 신호가 큰 것부터: **H1을 먼저** (단독 실행 한 번이면
끝), 그다음 H2(단계별), 마지막 H3(모듈별).

---

## 3. 진단: 실제 상태 확인

### 3-1. H1: preflight 단독 측정

```
$ time python3 scripts/preflight_exp004.py >/dev/null 2>&1
python3 scripts/preflight_exp004.py > /dev/null 2>&1  0.07s user 0.02s system 95% cpu 0.088 total
```

→ **0.088초.** H1 **기각.** preflight를 빼봐야 0.08초 절약이고, 체감
느림과 무관하다. 용의자 오인이 확정됐다.

### 3-2. 훅이 실제로 무엇을 부르는지 확인

```
$ cat .git/hooks/pre-commit
...
python3 scripts/preflight_exp004.py
git diff --check
python3 -m unittest discover -s tests -p 'test_*.py'
```

마지막 줄에 테스트 스위트가 있다. 여기를 의심.

### 3-3. H2: 단계별 측정

```
update_frontmatter_last_updated.py   0.028s
validate_docs.py                     0.110s
research_consistency.py              0.024s
preflight_exp004.py                  0.079s
unittest suite                       4.204s
```

→ 문서 스크립트 4종 합계 ≈ 0.24초, **`unittest` 스위트 4.20초.**
전체의 약 95%. H2 **지지**, H3로 좁혀 들어간다.

### 3-4. H3: 모듈별 측정 (여기서 함정에 빠질 뻔했다)

처음엔 repo 루트에서 이렇게 쟀다:

```
$ python3 -m unittest test_exp003_perturbations   # (repo 루트에서)
test_exp003_perturbations   0.035 total
test_exp004_positioning     0.030 total
test_exp005_timing_prior    0.026 total
test_gamma_v03              0.025 total
```

전부 0.03초? `discover`는 4.2초인데 합이 0.1초? **모순.** 이때 숫자를
믿고 "테스트도 빠르네" 하고 넘어갔으면 진단이 통째로 틀렸을 것이다.

모순을 그냥 두지 않고 `-v`로 확인:

```
$ python3 -m unittest discover -s tests -p 'test_*.py' -v
...
Ran 12 tests in 4.081s
OK
```

`discover`는 12개를 진짜로 돌렸다. 그렇다면 위의 "0.03초"들은 **0개를
돌린 것**이다. 원인: `tests/`가 `sys.path`에 없어서 모듈명 `test_exp003_...`
import가 조용히 실패하고 0개 실행 → 빠를 수밖에. (관찰 → 해석: *빠른 게
아니라 아무것도 안 한 것이다*.)

`tests/` 디렉터리 안에서 다시 측정:

```
$ cd tests
$ python3 -m unittest test_exp003_perturbations
test_exp003_perturbations   Ran 3 tests   1.345 total
test_exp004_positioning     Ran 2 tests   1.153 total
test_exp005_timing_prior    Ran 3 tests   2.063 total
test_gamma_v03              Ran 4 tests   0.232 total
```

→ H3 **지지.** 무거운 건 실험 스위트의 실제 수치 계산이다:
- `test_exp005_timing_prior` 2.06초
- `test_exp003_perturbations` 1.35초
- `test_exp004_positioning` 1.15초
- `test_gamma_v03` 0.23초 (사실상 numpy import 오버헤드뿐)

이들은 `*_suite_writes_outputs` 류 테스트로, 커밋마다 실험 전체를 다시
돌려 outputs를 쓴다. `tests/`가 `from qfuds import ...`로 실험 소스에
의존함도 확인했다.

---

## 4. 추가 확인: 정본/설치본 이원화

훅을 고치기 전에 "이 훅이 어디서 오는가"를 확인했다.

```
$ git config core.hooksPath
(no custom hooksPath)
$ grep -rl "unittest discover|pre-commit" scripts/ ...
scripts/git-hooks/pre-commit
```

→ 추적되는 정본은 `scripts/git-hooks/pre-commit`. `.git/hooks/`만 고치면
재설치 시 날아간다. **두 곳 모두** 고쳐야 변경이 영구히 남는다.

---

## 5. 결론 / 해결

### 무엇을 했나

회귀 테스트를 **항상 돌리는 대신, 스테이징에 `qfuds/` 또는 `tests/`
변경이 있을 때만** 돌리도록 조건부화했다. 문서만 고친 커밋(최근 커밋
대부분)은 스위트를 통째로 스킵한다. `RUN_TESTS=1`로 강제 실행도 가능.

```sh
git diff --check

# 회귀 테스트는 실험 코드/테스트가 바뀐 커밋에서만 의미가 있다.
# 문서만 고친 커밋은 스킵해 빠르게 유지한다. RUN_TESTS=1로 강제.
staged=$(git diff --cached --name-only --diff-filter=ACMR)
if [ "${RUN_TESTS:-0}" = "1" ] || printf '%s\n' "$staged" | grep -qE '^(qfuds/|tests/)'; then
  echo "pre-commit: experiment code changed -> running regression suite"
  python3 -m unittest discover -s tests -p 'test_*.py'
else
  echo "pre-commit: no qfuds/ or tests/ changes -> skipping regression suite (RUN_TESTS=1 to force)"
fi
```

`scripts/git-hooks/pre-commit`(정본) + `.git/hooks/pre-commit`(설치본)
양쪽에 동일 반영.

### 왜 이 선택인가 (고른 것 / 안 고른 대안 / 근거)

| 선택지 | 했나 | 근거 |
| --- | --- | --- |
| preflight_exp004.py 제거 | ✗ | 병목이 아니다(0.08s). 빼도 체감 0, 기록 일관성 가드만 잃는다. |
| 무거운 테스트를 pre-push로 이동 | ✗ (후순위) | 가능하나, push 전까진 회귀가 로컬에 남는다. 경로 조건부가 더 정밀. |
| 실험 스위트에 저해상도 테스트 모드 추가 | ✗ | 코드 침습적. 지금 문제(잘못된 트리거 시점)엔 과한 처방. |
| **경로 기반 조건부 실행** | ✓ | 회귀 안전망 유지 + 문서 커밋은 약 0.3s. 변경 최소, 가역적. |

핵심 통찰: 회귀 테스트의 목적은 "실험 코드가 바뀌었는데 기록된 결과가
깨졌나"를 잡는 것이다. 실험 코드를 건드리지 않은 커밋엔 돌릴 이유가 없다.

### 검증

```
$ echo '> test' >> docs/README.md && git add docs/README.md
$ .git/hooks/pre-commit
...
pre-commit: no qfuds/ or tests/ changes -> skipping regression suite (RUN_TESTS=1 to force)
pre-commit: all checks passed
```

문서만 스테이징한 커밋이 회귀 스위트를 스킵하고 통과. `qfuds/`·`tests/`
경로는 grep 매칭으로 실행 분기됨을 확인.

### 트레이드오프 / 검증 안 한 것

- `qfuds/`를 import하지만 별도 디렉터리에 있는 코드(예: `scripts/` 내
  실험 호출)가 바뀐 경우는 트리거되지 않는다. 현재 테스트는 `qfuds/`와
  `tests/`만 의존하므로 충분하지만, 의존 구조가 바뀌면 조건도 갱신해야 한다.
- `--diff-filter=ACMR`은 추가/복사/수정/이름변경만 본다. 삭제(D)만 있는
  커밋은 스킵되는데, 실험 파일 삭제는 별도로 드물어 의도된 동작으로 둔다.

---

## 6. 재발 방지 / 운영 메모

- [ ] 훅을 고칠 땐 **정본(`scripts/git-hooks/`)과 설치본(`.git/hooks/`)
      양쪽**을 함께 수정한다. 한쪽만 고치면 재설치/clone 시 어긋난다.
- [ ] 성능 체감 문제는 **지목 전에 단계별로 측정**한다. "최근에 추가한
      파일 = 범인"은 자주 틀린다.
- [ ] `python -m unittest <module>`이 `Ran 0 tests`를 내면 빠른 게 아니라
      **아무것도 안 돈 것**이다. 항상 "Ran N tests"의 N을 확인한다.
- 후속(선택): 테스트가 더 느려지면 그때 pre-push 분리 또는 저해상도
      테스트 모드를 검토. 지금은 불필요(YAGNI).

---

## 7. 타임라인

- 사용자: "preflight_exp004.py 때문에 훅이 느리다, 뺄까?"
- preflight 단독 측정 → 0.088초. 용의자 오인 확인.
- 단계별 측정 → `unittest` 스위트 4.2초가 95%.
- 모듈별 측정 1차(루트) → 전부 0.03초라는 모순 발견.
- `-v`로 교차검증 → `discover`는 12개 실행. 루트 측정은 0개 no-op이었음.
- `tests/`에서 재측정 → exp005 2.06s / exp003 1.35s / exp004 1.15s.
- 사용자: "문서 커밋마다 실험 테스트 돌릴 필요 없잖아."
- 정본+설치본 훅에 경로 기반 조건부 실행 반영.
- docs-only 커밋으로 스킵 동작 검증, 통과.

---

## 부록 X: 디버깅 명령어 모음 (cheat sheet)

성능 병목을 "지목"이 아니라 "측정"으로 좁힐 때 이 순서로 쓴다.

```sh
# 1) 용의자 단독 측정 — 가장 싼 검증부터
time python3 scripts/preflight_exp004.py >/dev/null 2>&1
#   time: 명령 한 줄의 실제(real)/user/sys 시간을 잰다.
#   이 사건: 지목된 스크립트가 0.088s임을 보고 H1을 즉시 기각.

# 2) 파이프라인 단계별 측정 — 어느 단계가 무거운지
{ TIMEFORMAT='%R'; time python3 -m unittest discover -s tests -p 'test_*.py' >/dev/null 2>&1; } 2>&1
#   각 단계를 따로 time으로 감싸 비교. 합이 전체와 맞는지 본다.
#   이 사건: 문서 4종 0.24s vs 테스트 4.2s — 병목을 마지막 단계로 확정.

# 3) 테스트를 모듈별로 쪼개되, "몇 개 돌았는지" 반드시 확인
cd tests && python3 -m unittest test_exp005_timing_prior   # 'Ran N tests' 확인
#   -m unittest <module>은 sys.path에 모듈이 없으면 0개 돌고 조용히 끝난다.
#   이 사건: 루트에서 0개(=가짜 빠름) → tests/에서 실제 N개 측정으로 정정.

# 4) 의심되면 verbose로 교차검증
python3 -m unittest discover -s tests -p 'test_*.py' -v   # 마지막 'Ran 12 tests'
#   이 사건: 측정 모순(0.03s vs 4.2s)을 -v로 깨고 진실 확인.

# 5) 훅이 추적본인지 확인 — 어디를 고쳐야 영구히 남나
git config core.hooksPath          # 커스텀 경로 쓰는지
ls -la .git/hooks/pre-commit       # 설치본(추적 안 됨)
git ls-files scripts/git-hooks/    # 정본(추적됨)

# 6) 조건부 트리거 로직 단위 검증 — 훅 전체를 돌리지 않고 grep만
printf '%s\n' "qfuds/growth.py" "docs/README.md" | grep -qE '^(qfuds/|tests/)' && echo RUN || echo SKIP
#   git diff --cached --name-only가 낼 목록을 흉내내 분기를 확인.
```

응용 팁: **"느리다"류 문제는 거의 항상 "지목된 것 ≠ 진짜 병목"이다.**
싼 단독 측정 → 단계별 분해 → 모듈별 분해 순으로 좁히고, 측정값이
모순되면(특히 "너무 빠름") 그 자리에서 `-v`/카운트로 깨라. 빠른 0초는
대개 "안 돌았다"는 신호다.
