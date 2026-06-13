---
doc_id: postmortem-012-qfuds-math-doc-audit
id: postmortem-012-qfuds-math-doc-audit
seq: 12
title: "QFUDS 수식 검산과 문서 정합성 감사 회고"
doc_type: postmortem
type: postmortem
stage: reference
status: reference
wiki_status: active
evidence_role: provenance
depends_on:
  - roadmap
  - qfuds_lineage_rough_tanh_numerical_sketch_ko
  - qfuds_lineage_rough_tanh_thesis_report_ko
next_gate: provenance only; roadmap이 상태 권위; CLASS/hi_class와 실제 likelihood는 여전히 미수행
date: 2026-06-13
context: main 브랜치에서 QFUDS Python 수식, lineage/assets/004_rough_tanh 산출물, README/qfuds_ko/lineage 문서 값을 함께 검산한 마무리 작업
audience: 주니어 개발자
length: 작업 단계별 풀어쓰기
created_at: 2026-06-13
created_by: dorito
updated_at: 2026-06-13
updated_by: dorito
last_updated: 2026-06-13
last_verified_at: 2026-06-13
last_verified_by: dorito
audit_log:
  - action: created
    at: 2026-06-13
    by: dorito
    note: "Python 수식 검산, lineage PNG/CSV 재생성, README/qfuds_ko/lineage 문서 정합성 수정을 마친 직후 작성"
tags: [postmortem, qfuds, math-audit, docs, lineage, reproducibility]
relations:
  - docs/wiki/lineage/003_research_flow_plain_language_ko.md
  - docs/wiki/lineage/004_rough_tanh_numerical_sketch_ko.md
  - docs/wiki/lineage/005_rough_tanh_thesis_report_ko.md
  - docs/05_next_steps/000_roadmap.md
  - .agent/workflows/research-investigation-result-routing-workflow.md
  - .agent/workflows/wiki-maintenance-workflow.md
code_refs:
  - file: qfuds/background.py
    note: "현재 밀도 합을 flat하게 맞춰 H(a=1)=H0가 되도록 omega_bfoam0 보정"
  - file: qfuds/perturbations.py
    note: "phase-B 밀도 양수성 게이트, P2 source denominator, 보존 residual 상태 처리를 보정"
  - file: qfuds/positioning.py
    note: "background viability failure를 먼저 분류하고 실패 perturbation 산출물을 남기지 않도록 보정"
  - file: docs/wiki/lineage/assets/004_rough_tanh/cp15_viscosity.py
    note: "점성 proxy의 k-shape 해석을 high-k onset이 아니라 ratio shape로 보정"
  - file: docs/wiki/lineage/assets/004_rough_tanh/cp16_growth_index.py
    note: "redshift 값으로 scale-factor grid를 보간하던 CP16 그림 버그 수정"
  - file: scripts/validate_docs.py
    note: "active-stage 문서의 local PNG 링크 존재 검증 추가"
  - file: tests/test_lineage_rough_tanh_assets.py
    note: "lineage 자산 수식의 flat closure, w_Q 극한, density background, CP16 scale band 테스트 추가"
---

# QFUDS 수식 검산과 문서 정합성 감사 회고

## 사건 한 줄 요약

QFUDS Python 수식과 lineage 자산을 검산하던 중, 배경 정규화, phase-B 음수 밀도 처리,
P2 perturbation failure 기록, CP15/CP16 그림 해석, CP5/CP7의 `c_eff²` 값 설명이 서로
완전히 같은 언어로 닫혀 있지 않다는 것을 확인했다. 코드는 보수적으로 실패를 먼저
드러내도록 고쳤고, 문서는 "무엇이 계산됐고 무엇이 아직 proxy인지"가 섞이지 않게
수정했다.

## 0. 사전 지식

| 용어 | 뜻 | 이 사건에서 중요한 이유 |
| --- | --- | --- |
| `LCDM` / `ΛCDM` | 표준 우주론 기준선 | `gamma0=0`일 때 이 기준선을 정확히 회복해야 한다. |
| `rho_B` / phase-B density | 진공압처럼 행동하는 B상 밀도 | `rho_B <= 0`이면 perturbation 계산보다 먼저 배경 물리성 실패다. |
| P1 | B상을 매끈한 interacting vacuum처럼 두는 closure | 안정하더라도 새 QFUDS 물리가 아니라 IV/IDE 현상학이다. |
| P2 | B상도 near-vacuum fluid로 세워 perturbation을 적분하는 closure | retained amplitude에서 불안정하고, 더 큰 stress case는 배경부터 탈락한다. |
| `c_eff²` | 암흑 유체의 유효 음속 제곱 | CP5 단일 `S8=0.76` 교차값과 CP7 coarse best-fit 값이 다르므로 문서에서 분리해야 한다. |
| proxy | 정밀 Boltzmann code가 아니라 거친 근사 | `CLASS/hi_class`와 실제 likelihood가 없으면 강한 관측 생존 주장이 아니다. |

## 1. 증상

사용자 요청은 단순한 문서 정리가 아니라 "파이썬 계산 수식이 과학적/수학적으로 옳은지,
부동소수점까지 고려해 검산하고, 결과가 달라지면 문서·관련 데이터·PNG까지 갱신하라"는
감사였다.

검토 중 확인된 증상은 네 묶음이었다.

1. `qfuds/background.py`의 현재 밀도 합이 정확히 1이 아니어서 `H(a=1)=H0`가 엄밀히
   닫히지 않았다.
2. `qfuds/perturbations.py`의 P2 source가 `abs(rho_B)`로 음수 밀도를 숨길 수 있었고,
   conservation residual도 계산하지 않았는데 0처럼 보일 수 있었다.
3. lineage `cp16_growth_index.py`의 scale-dependence band가 scale factor grid를
   redshift 값으로 보간하고 있었다.
4. 문서에서는 CP5의 단일 `S8=0.76` 교차값 `c_eff²≈2.92e-5`와 CP7의 coarse best-fit
   `c_eff²=4.6e-6`, `S8≈0.778`이 한 문장 안에서 같은 "fit value"처럼 읽힐 수 있었다.

## 2. 첫 의문 + 가설

| 가설 | 왜 그럴 수 있는지 | 어떻게 확인할지 |
| --- | --- | --- |
| H1 | 현재 밀도 파라미터가 flat closure를 정확히 만족하지 않을 수 있다. | `pytest`에서 `E(a=1)=1`, `omega` 합, LCDM limit 회귀 테스트를 추가한다. |
| H2 | P2가 음수 `rho_B`를 수치 regularization으로 숨기고 있을 수 있다. | P2 denominator와 background grid를 확인하고, `rho_B <= 0`이면 적분 전 실패시키는 테스트를 둔다. |
| H3 | lineage 그림/CSV 중 하나가 grid 변수 또는 해석 라벨을 잘못 쓰고 있을 수 있다. | `docs/wiki/lineage/assets/004_rough_tanh/*.py`를 직접 실행하고, CP15/CP16 수식을 독립 테스트로 검산한다. |
| H4 | 문서가 최신 산출값과 달라 reader가 CP5/CP7 값을 혼동할 수 있다. | README, `qfuds_ko.md`, lineage 003/004/005를 `rg`로 교차 검색하고 숫자·판정 문장을 맞춘다. |
| H5 | PNG 경로 또는 생성 결과가 깨졌을 수 있다. | 문서 local link 검사와 PNG nonblank 검사를 따로 돌린다. |

## 3. 진단: 실제 상태 확인

### 3.1 수치 테스트와 회귀 테스트

명령:

```bash
/private/tmp/qfuds-review-venv/bin/python -m pytest -q
```

출력:

```text
.................                                              [100%]
17 passed, 10 subtests passed in 16.92s
```

해석:

- H1 지지: flat closure와 `H(a=1)=H0`가 테스트로 고정됐다.
- H2 지지: P2는 background density gate를 통과해야만 적분된다.
- H3 일부 지지: lineage 자산 테스트가 CP16 scale band와 density background 극한을 잡는다.

### 3.2 문서 frontmatter와 roadmap 정합성

명령:

```bash
/private/tmp/qfuds-review-venv/bin/python scripts/validate_docs.py
```

출력:

```text
docs validation passed
```

명령:

```bash
/private/tmp/qfuds-review-venv/bin/python scripts/research_consistency.py
```

출력:

```text
CONSISTENCY PASSED: roadmap is the single source of truth; no drift detected
```

해석:

- H4 지지: README와 overview 계열 문서는 roadmap을 상태 권위로 유지한다.
- 문서 수정은 roadmap status를 바꾸지 않는다. 이번 작업은 "새 실험 성공"이 아니라
  기존 증거와 산출물의 엄밀성 보정이다.

### 3.3 PNG와 local link 검사

명령:

```bash
/private/tmp/qfuds-review-venv/bin/python - <<'PY'
from pathlib import Path
from PIL import Image
root = Path('docs/wiki/lineage/assets/004_rough_tanh')
paths = sorted(root.glob('*.png'))
blank = []
for path in paths:
    im = Image.open(path).convert('L')
    lo, hi = im.getextrema()
    if lo == hi:
        blank.append(str(path))
print(f'checked {len(paths)} lineage PNGs; blank={len(blank)}')
if blank:
    print('\n'.join(blank))
    raise SystemExit(1)
PY
```

출력:

```text
checked 27 lineage PNGs; blank=0
```

명령:

```bash
/private/tmp/qfuds-review-venv/bin/python - <<'PY'
from pathlib import Path
import re
files = [
    Path('docs/wiki/lineage/003_research_flow_plain_language_ko.md'),
    Path('docs/wiki/lineage/004_rough_tanh_numerical_sketch_ko.md'),
    Path('docs/wiki/lineage/005_rough_tanh_thesis_report_ko.md'),
    Path('README.md'),
    Path('docs/00_project/qfuds_ko.md'),
]
pat = re.compile(r'!??\[[^\]]*\]\(([^)]+)\)')
missing = []
checked = 0
for f in files:
    text = f.read_text(encoding='utf-8')
    for raw in pat.findall(text):
        target = raw.split()[0].strip('<>')
        if target.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        if target.startswith('../') or target.startswith('./') or not target.startswith('/'):
            path = (f.parent / target).resolve()
            checked += 1
            if not path.exists():
                missing.append((str(f), target, str(path)))
print(f'checked local markdown links/images: {checked}; missing={len(missing)}')
for item in missing:
    print('MISSING', item)
raise SystemExit(1 if missing else 0)
PY
```

출력:

```text
checked local markdown links/images: 371; missing=0
```

해석:

- H5 반증: PNG는 존재하고 blank가 아니다.
- local Markdown/image link도 지정 문서 기준으로 깨지지 않았다.

### 3.4 diff hygiene

명령:

```bash
git diff --check
```

출력은 비어 있었다. 즉 trailing whitespace나 conflict marker는 없었다.

중간에 CP5 SVG를 재생성한 뒤에는 `git diff --check`가 matplotlib SVG의 trailing
whitespace를 다수 보고했다. 이는 수식 오류가 아니라 산출물 포맷 문제였고, SVG의
행 끝 공백만 제거한 뒤 다시 통과했다.

## 4. 추가 확인

lineage 자산은 단순 문서가 아니라 실행 가능한 연구 기록이므로 따로 확인했다.

- `docs/wiki/lineage/assets/004_rough_tanh/cp5_sound_speed.py`를 재실행해
  `S8 = 0.76` 교차값이 `2.916341353442478e-05`임을 확인했다.
- `cp7_brute_fit.py`는 coarse grid에서 `z*=6.0`, `Omega_m0=0.29`,
  `c_eff²=4.641589e-06`, `S8=0.7780`, `AIC=16.049`를 유지했다.
- `cp15_viscosity.py`는 `c_vis²=0`에서 CP11을 최대 상대 residual `4.20e-08`로
  재현했고, 점성 ratio shape가 단순 high-k onset 설명과 다르다는 점을 문서에 반영했다.
- `cp16_growth_index.py`는 `gamma_eff_scale_curves()`를 추가해 scale factor grid를
  redshift 값으로 보간하던 그림 버그를 막았다.

검증하지 않은 것:

- `CLASS/hi_class` Boltzmann code likelihood는 돌리지 않았다.
- 실제 DESI/Euclid likelihood와 공분산 비교는 하지 않았다.
- 외부 웹에서 future release 일정은 재검증하지 않았다. 그래서 문서는 "this October" 같은
  상대 일정 표현을 제거하고 "후속 자료가 다음 외부 검산"으로 보수화했다.

## 5. 결론 / 해결

| 결정 | 고른 것 | 안 고른 대안 | 근거 |
| --- | --- | --- | --- |
| background normalization | `omega_bfoam0=0.685708`로 flat sum을 맞춤 | 현재값을 "작은 오차"로 방치 | `H(a=1)=H0`는 baseline invariant라 부동소수점 tolerance 안에서 고정해야 한다. |
| P2 음수 밀도 | `rho_B <= 0`이면 perturbation 적분 전 실패 | `abs(rho_B)`로 denominator만 안정화 | 음수 density는 perturbation 문제가 아니라 배경 물리성 실패다. |
| conservation residual | 계산하지 못한 값은 `NaN`과 status로 기록 | 0으로 채움 | 0은 보존이 검증됐다는 뜻으로 오해된다. |
| CP15 해석 | 점성 ratio shape로 설명 | high-k onset/free-streaming으로 단순화 | 실제 ratio는 저-k부터 눌렸다가 `k≈1.2`에서 0.95로 회복한다. |
| CP16 그림 | scale factor 기준 보간 helper 추가 | redshift 배열을 그대로 `np.interp`에 사용 | 성장지수는 scale factor grid에서 계산되므로 보간 변수도 scale factor여야 한다. |
| CP5/CP7 문서 | CP5 `2.92e-5`, CP7 `4.6e-6`을 분리 | 둘 다 "fit value"로 뭉뚱그림 | 서로 다른 목적 함수와 스캔 조건에서 나온 값이다. |
| README/qfuds_ko 톤 | "자랑스럽게 말해도 될 수렴"으로 표현 | "정확히 학계 값과 일치" 또는 지나치게 건조한 표현 | 자부심은 보존하되, 검증/novelty claim으로 읽히지 않게 해야 한다. |

최종 판단:

- 로드맵 수준에서 새 레벨을 열거나 닫을 사안은 아니다.
- 하지만 기존 결과의 엄밀성에는 critical했다. 특히 음수 `rho_B`를 `abs()`로 숨기지 않는
  것과, 계산하지 않은 residual을 0으로 두지 않는 것은 증거 관리의 핵심이다.
- 문서는 현재 "계산됨", "프록시", "미수행", "blocked"의 경계가 더 명확해졌다.

## 6. 재발 방지 / 운영 메모

- 배경량 invariant는 코드 테스트로 먼저 고정한다. 예: flat sum, `E(1)=1`, LCDM limit.
- 물리성 실패는 numerical regularization보다 먼저 분류한다.
- 계산하지 않은 진단값은 0이 아니라 `NaN` 또는 explicit status를 쓴다.
- 그림/CSV를 재생성하면 `git diff --check`와 PNG nonblank 검사를 같이 돌린다.
- 문서에서 값이 여러 실험 조건에서 나온 경우, "무엇의 fit인가"를 값 옆에 붙인다.
- external release 일정처럼 시간이 흐르면 바뀌는 문장은 절대 날짜 또는 "후속 자료"로 쓴다.

## 7. 타임라인

- 2026-06-13: 사용자가 Python 수식과 lineage asset까지 과학적으로 검산해 달라고 요청.
- 2026-06-13: `qfuds/background.py` flat closure와 `H(a=1)=H0` 오차를 확인하고 보정.
- 2026-06-13: `qfuds/perturbations.py`에서 P2 음수 density gate, denominator, residual status를 보정.
- 2026-06-13: exp003/exp004/exp005 output과 figure를 재생성하고 문서를 최신 산출값으로 갱신.
- 2026-06-13: lineage CP15/CP16 수식과 그림을 검산하고 CP15/CP16 PNG/SVG를 재생성.
- 2026-06-13: README, `qfuds_ko.md`, lineage 003/004/005의 값과 판정 문장을 교차 수정.
- 2026-06-13: `pytest`, `validate_docs.py`, `research_consistency.py`, `git diff --check`, PNG/link 검사를 통과.
- 2026-06-13: 이 postmortem을 작성해 사건의 원인, 검증, tradeoff를 보존.

## 부록 A — 디버깅 명령어 모음

### 전체 테스트

```bash
/private/tmp/qfuds-review-venv/bin/python -m pytest -q
```

일반적으로 Python test suite를 실행한다. 이 사건에서는 flat closure, perturbation gate,
lineage asset 수식 테스트가 모두 통과하는지 봤다. 출력의 `17 passed, 10 subtests passed`
가 회귀 테스트 통과 신호였다.

### 문서 frontmatter와 roadmap 정합성

```bash
/private/tmp/qfuds-review-venv/bin/python scripts/validate_docs.py
```

문서 frontmatter, active-stage 파일명, local PNG 링크 등을 검사한다. 이 사건에서는 문서
수정이 schema와 PNG 링크를 깨지 않았는지 확인했다.

```bash
/private/tmp/qfuds-review-venv/bin/python scripts/research_consistency.py
```

roadmap이 SSOT(single source of truth)인지, 실험/결과/decision log 연결이 유지되는지
본다. 이 사건에서는 "문서 수정이 로드맵 상태를 암묵적으로 바꾸지 않았다"는 확인에 썼다.

### 텍스트 검색

```bash
rg -n "3e-5|2.92|4.6e-6|CP15|CP16" README.md docs/00_project/qfuds_ko.md docs/wiki/lineage/*.md
```

`rg`는 빠른 ripgrep 검색 도구다. 이 사건에서는 오래된 CP5 값, CP7 값, CP15/CP16 해석
문장이 여러 문서에 남아 있는지 찾는 데 썼다.

### PNG nonblank 검사

```bash
/private/tmp/qfuds-review-venv/bin/python - <<'PY'
from pathlib import Path
from PIL import Image
root = Path('docs/wiki/lineage/assets/004_rough_tanh')
paths = sorted(root.glob('*.png'))
blank = []
for path in paths:
    im = Image.open(path).convert('L')
    lo, hi = im.getextrema()
    if lo == hi:
        blank.append(str(path))
print(f'checked {len(paths)} lineage PNGs; blank={len(blank)}')
if blank:
    print('\n'.join(blank))
    raise SystemExit(1)
PY
```

Pillow로 PNG를 열고 grayscale extrema가 같은지 본다. `lo == hi`면 모든 픽셀이 같은
blank 이미지일 가능성이 높다. 이 사건에서는 lineage PNG 27개가 모두 nonblank였다.

### Local link 검사

```bash
/private/tmp/qfuds-review-venv/bin/python - <<'PY'
from pathlib import Path
import re
files = [
    Path('docs/wiki/lineage/003_research_flow_plain_language_ko.md'),
    Path('docs/wiki/lineage/004_rough_tanh_numerical_sketch_ko.md'),
    Path('docs/wiki/lineage/005_rough_tanh_thesis_report_ko.md'),
    Path('README.md'),
    Path('docs/00_project/qfuds_ko.md'),
]
pat = re.compile(r'!??\[[^\]]*\]\(([^)]+)\)')
missing = []
checked = 0
for f in files:
    text = f.read_text(encoding='utf-8')
    for raw in pat.findall(text):
        target = raw.split()[0].strip('<>')
        if target.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        if target.startswith('../') or target.startswith('./') or not target.startswith('/'):
            path = (f.parent / target).resolve()
            checked += 1
            if not path.exists():
                missing.append((str(f), target, str(path)))
print(f'checked local markdown links/images: {checked}; missing={len(missing)}')
for item in missing:
    print('MISSING', item)
raise SystemExit(1 if missing else 0)
PY
```

Markdown의 local link와 image link가 실제 파일을 가리키는지 확인한다. 이 사건에서는
지정된 5개 문서의 371개 local reference가 모두 존재했다.

### diff hygiene

```bash
git diff --check
```

Git이 trailing whitespace와 conflict marker를 검사한다. matplotlib SVG를 재생성한 뒤
이 검사가 실패할 수 있으므로, 그림 산출물까지 commit할 때 마지막에 꼭 돌린다.

응용 팁: 이런 부류의 문제는 `rg`로 증상 범위를 잡고, 작은 invariant 테스트를 추가한 뒤,
산출물 재생성, 문서 숫자 대조, link/PNG 검증, `git diff --check` 순서로 닫으면 누락이
가장 적다.
