---
doc_id: postmortem-004-source-x-data-product-audit
id: postmortem-004-source-x-data-product-audit
seq: 4
title: "Source-X 데이터 제품 감사 회고"
doc_type: postmortem
type: postmortem
stage: reference
status: reference
wiki_status: active
evidence_role: reference
depends_on:
  - audit_2026_06_10_black_hole_data_product_audit_plan
  - audit_2026_06_10_black_hole_data_product_audit
  - source_x_audit_index
  - research_audit_index
  - repository_levels_glossary
next_gate: no roadmap change; use this as the postmortem for the Source-X black-hole data-product interlock
date: 2026-06-10
context: Source-X black-hole data-product audit plan and result after Phase 3 data_product_blocked finding
audience: 주니어 개발자
length: 작업 단계별 풀어쓰기
created_at: 2026-06-10
created_by: dorito
updated_at: 2026-06-10
updated_by: dorito
last_updated: 2026-06-10
last_verified_at: 2026-06-10
last_verified_by: dorito
audit_log:
  - action: created
    at: 2026-06-10
    by: dorito
    note: "Created after reviewing the 2026-06-10 Source-X data-product audit commits, chat prompts, source_x audit chain, and repository levels glossary."
tags: [postmortem, source-x, data-products, level-2b, qfuds]
relations:
  - docs/wiki/research/audits/source_x/plans/040_black_hole_data_product_audit_plan.md
  - docs/wiki/research/audits/source_x/conclusions/040_black_hole_data_product_audit.md
  - docs/wiki/research/audits/source_x/README.md
  - docs/wiki/research/audits/README.md
  - docs/wiki/glossary/repository_levels.md
code_refs:
  - file: docs/wiki/research/audits/source_x/plans/040_black_hole_data_product_audit_plan.md
    note: "Approved plan: defines the data-product interlock, product-state taxonomy, Lane A/B search axes, and no-Level-2B boundary."
  - file: docs/wiki/research/audits/source_x/conclusions/040_black_hole_data_product_audit.md
    note: "Executed audit result: records Lane A/B product search trace, candidate matrix, products not found, and no-derivation confirmation."
  - file: docs/wiki/research/audits/source_x/README.md
    note: "Source-X read order updated to include the 040 plan/result and reserve 041 for future delta-Q work."
  - file: docs/wiki/glossary/repository_levels.md
    note: "Glossary authority for why Level 2B remains blocked until a physical branch supplies X, Q^nu, phase-B rationale, delta Q, and known-model distinction."
---

# Source-X 데이터 제품 감사 회고

## 사건 한 줄 요약

오늘 Source-X 작업은 black-hole lane을 Physical-QFUDS Level 2B로 올리려는
작업이 아니었다. Phase 3에서 나온 `data_product_blocked` 상태를 더 잘게
쪼개서, 실제로 `rho_BH(a)`, `d rho_BH / dln(a)`, `S_BH(a)`,
`dS_BH / dln(a)`에 쓸 수 있는 data product가 있는지 확인하는
interlock을 만들고 실행한 작업이었다.

결론은 보수적이다.

```text
인접 문헌과 공개 제품은 있다.
하지만 QFUDS-usable data product는 확인되지 않았다.
따라서 black-hole lanes remain data_product_blocked, not physics_blocked.
Physical-QFUDS Level 2B remains blocked.
Roadmap unchanged.
```

## 0. 사전 지식

| 용어 | 이 문서에서의 의미 |
| --- | --- |
| Source-X | QFUDS에서 `Gamma(a)` 같은 retained timing을 물리 source로 올릴 수 있는지 압박하는 audit chain |
| Lane A | black-hole mass-density 또는 growth-history product. 후보는 `rho_BH(a)` 또는 `d rho_BH / dln(a)` |
| Lane B | black-hole entropy 또는 entropy-growth product. 후보는 `S_BH(a)` 또는 `dS_BH / dln(a)` |
| literature hit | 관련 논문이나 모델은 찾았지만 extractable product는 아직 확인되지 않은 상태 |
| data-product hit | figure, table, code, sample, downloadable asset 등 product 자체는 확인된 상태 |
| reproducibility hit | public data/code 또는 numeric table로 재구성이 가능한 상태 |
| QFUDS-usable hit | units, redshift coverage, uncertainty, normalization route, provenance가 있고 `X`를 정의할 수 있는 상태 |
| Level 2B | physical perturbation closure. [Repository Levels Glossary](../glossary/repository_levels.md)에 따르면 현재 blocked이며, 새 physical branch가 `X`, `Q^nu`, phase-B vacuum-pressure rationale, `delta Q`, known-model distinction을 먼저 제공해야 한다 |

중요한 함정이 있다. "data product가 있다"는 말은 "`Q^nu`를 만들 수
있다"는 말이 아니다. 이번 작업은 그 차이를 문서 구조로 고정하는
작업이었다.

## 1. 증상

Phase 3 결과는 두 retained black-hole lane을 `data_product_blocked`로
분류했다. 이때 바로 물리 derivation으로 가면 안 되는 이유가 있었다.

```text
Q^nu =
why phase B has w ~= -1 =
delta Q route =
known-model distinction =
```

이 네 가지가 아직 비어 있기 때문이다.

사용자 프롬프트도 같은 boundary를 반복해서 걸었다. 복원 가능한 원문
핵심은 다음과 같다.

```text
# Black-Hole Data Product Audit Plan

Create `docs/wiki/research/audits/source_x/plans/040_black_hole_data_product_audit_plan.md`
as a docs-only audit plan for the current `data_product_blocked` state after Phase 3.
The plan will not derive `Q^nu`, will not open Physical-QFUDS Level 2B,
and will not modify roadmap status.
```

이후 구현 요청에서도 같은 제약이 유지됐다.

```text
PLEASE IMPLEMENT THIS PLAN:
...
Do not modify `docs/05_next_steps/000_roadmap.md`.
```

그리고 실행 요청에서는 계획을 바꾸지 말라는 제약이 명시됐다.

```text
Execute the approved plan.

Authority:

[040_black_hole_data_product_audit_plan.md](docs/wiki/research/audits/source_x/plans/040_black_hole_data_product_audit_plan.md)

Follow the plan exactly.

Do not redesign the plan.
Do not expand scope.
Do not modify roadmap status.
Do not open Physical-QFUDS Level 2B.
```

즉 증상은 "데이터 제품을 찾을 수도 있을 것 같다"가 아니라, "데이터
제품을 찾는 행위가 곧 물리 branch admission으로 오해될 수 있다"였다.

## 2. 첫 의문 + 가설

| 가설 | 왜 그럴 수 있는지 | 어떻게 확인할지 |
| --- | --- | --- |
| H1. `040`은 derivation이 아니라 data-product interlock이어야 한다 | 사용자 프롬프트가 `Do not derive Q^nu`, `Do not open Physical-QFUDS Level 2B`를 반복했다 | `040_black_hole_data_product_audit_plan.md`의 Status Boundary와 Reporting Requirements를 확인한다 |
| H2. 실행 결과 문서는 product hit와 QFUDS-usable hit를 분리해야 한다 | LVK/GWTC 같은 public product가 있어도 QFUDS `X -> Q^nu`로 바로 이어지지 않는다 | `040_black_hole_data_product_audit.md`의 search trace와 candidate matrix를 확인한다 |
| H3. Source-X index는 `040` 충돌을 해결해야 한다 | 기존 `040-049`는 Phase 4 `delta Q` 예약이었고, 사용자는 `040`을 data-product interlock으로 쓰라고 했다 | `source_x/README.md`의 filename convention과 read order를 확인한다 |
| H4. Roadmap과 Level 2B status는 바뀌면 안 된다 | 새 evidence가 physical admission-rule items를 채우지 못했다 | `repository_levels.md`, roadmap diff, validation command를 확인한다 |
| H5. 이번 결과는 "문헌이 없다"가 아니라 "QFUDS-usable product가 없다"여야 한다 | Farrah, Croker, Lacy, Amendola, LVK/GWTC, entropy-budget hit는 실제로 존재한다 | audit result의 Lane A/B conclusion과 Products Not Found를 대조한다 |

검증 순서는 cheap / high-signal 우선이었다. 먼저 git commit과 파일
구조로 실제 변경 범위를 확인하고, 그 다음 `040` plan/result의 boundary
문장을 확인했다. 마지막으로 validator와 roadmap diff로 상태 drift를
확인했다.

## 3. 진단: 실제 상태 확인

### 3.1 오늘 Source-X 커밋 범위 확인

사용한 명령:

```bash
rtk proxy git log --all --format='%h %ad %an %s' --date=iso --since='2026-06-10 00:00' -- docs/wiki/research/audits/source_x docs/wiki/research/audits/README.md
```

핵심 출력:

```text
d2072b0 2026-06-10 18:34:44 +0900 Dorito audit(conslusions): physical-QFUDS Level 2B remains blocked
cd756a2 2026-06-10 18:32:36 +0900 Dorito plan(audit): black hole data product audit
cfea252 2026-06-10 18:16:13 +0900 Dorito audit(Phase 3): Q^nu를 만들기 전에 필요한 데이터가 부족한 상태
483131a 2026-06-10 18:03:04 +0900 Dorito plan: phase3 qnu derivation attempt planning
240d438 2026-06-10 17:44:17 +0900 Dorito docs: summary 추가
48809d8 2026-06-10 17:34:31 +0900 Dorito refactor: audits 구조 및 파일 컨벤션 개편
363be9a 2026-06-10 16:09:28 +0900 Dorito docs: audit for black hole coupled source
f30760c 2026-06-10 16:07:25 +0900 Dorito chore: audit 구조 개편
```

해석:

- `source_x`는 하루 동안 구조 개편, Phase 3 plan/result, `040`
  data-product plan/result 순서로 쌓였다.
- 이 postmortem의 직접 대상은 `cd756a2`와 `d2072b0`이다.
- 앞선 `cfea252`, `483131a`는 왜 `040` interlock이 필요한지 설명하는
  선행 맥락이다.

H1과 H3은 지지된다. `040`은 갑자기 생긴 파일이 아니라 Phase 3
`data_product_blocked` 결과 뒤에 붙은 interlock이다.

### 3.2 실제 커밋 파일 확인

사용한 명령:

```bash
rtk proxy git show --name-status --oneline cd756a2 d2072b0
```

핵심 출력:

```text
cd756a2 plan(audit): black hole data product audit
M	docs/wiki/research/audits/README.md
M	docs/wiki/research/audits/source_x/README.md
A	docs/wiki/research/audits/source_x/plans/040_black_hole_data_product_audit_plan.md

d2072b0 audit(conslusions): physical-QFUDS Level 2B remains blocked
M	docs/wiki/research/audits/README.md
M	docs/wiki/research/audits/source_x/README.md
A	docs/wiki/research/audits/source_x/conclusions/040_black_hole_data_product_audit.md
```

해석:

- plan commit은 plan 문서 하나와 index 두 개만 바꿨다.
- result commit도 result 문서 하나와 index 두 개만 바꿨다.
- roadmap, decision log, theory docs, experiment/result docs는 바꾸지
  않았다.

H4는 지지된다. 변경 범위가 audit chain 내부에 갇혀 있다.

### 3.3 Source-X 파일 구조 확인

사용한 명령:

```bash
rtk rg --files docs/wiki/research/audits/source_x | sort
```

핵심 출력:

```text
docs/wiki/research/audits/source_x/README.md
docs/wiki/research/audits/source_x/conclusions/011_phase1_source_x_audit.md
docs/wiki/research/audits/source_x/conclusions/021_phase2_black_hole_coupled_source_audit.md
docs/wiki/research/audits/source_x/conclusions/029_phase2_candidate_selection_closeout.md
docs/wiki/research/audits/source_x/conclusions/031_phase3_qnu_derivation_attempt.md
docs/wiki/research/audits/source_x/conclusions/040_black_hole_data_product_audit.md
docs/wiki/research/audits/source_x/coverage/022_phase2_black_hole_coupled_literature_search_audit.md
docs/wiki/research/audits/source_x/coverage/023_phase2_compact_object_transient_source_literature_audit.md
docs/wiki/research/audits/source_x/coverage/024_phase2_structure_era_activation_literature_audit.md
docs/wiki/research/audits/source_x/plans/010_phase1_source_x_audit_plan.md
docs/wiki/research/audits/source_x/plans/020_phase2_black_hole_coupled_source_audit_plan.md
docs/wiki/research/audits/source_x/plans/030_phase3_qnu_derivation_attempt_plan.md
docs/wiki/research/audits/source_x/plans/040_black_hole_data_product_audit_plan.md
```

해석:

- `040` plan/result가 같은 route number를 공유한다.
- Phase 4 `delta Q`는 `041`로 밀렸다.
- `040`은 "결론을 내는 physical admission"이 아니라 "Phase 4로 넘어가기
  전에 data product가 있는지 확인하는 gate"다.

### 3.4 Plan boundary 확인

사용한 명령:

```bash
rtk rg -n "data_product_blocked|not physics_blocked|Do not derive Q\\^nu|Physical-QFUDS Level 2B|Roadmap unchanged" docs/wiki/research/audits/source_x/plans/040_black_hole_data_product_audit_plan.md
```

핵심 출력:

```text
29:Current Phase 3 state: `data_product_blocked`.
42:This interlock is `data_product_blocked`, not physics_blocked.
49:- `not physics_blocked` means this audit has not proven that no physical
53:Do not derive Q^nu.
55:Do not open Physical-QFUDS Level 2B.
323:Physical-QFUDS Level 2B remains blocked.
325:Roadmap unchanged.
```

해석:

- plan은 "물리적으로 불가능"이라고 결론내리지 않는다.
- plan은 "현재 필요한 data product가 없어서 다음 단계가 막혔다"로
  제한한다.
- 이 제한이 없으면 `LVK/GWTC products found` 같은 문장을 `Q^nu` 가능성으로
  과대해석하기 쉽다.

H1은 지지된다.

### 3.5 Result 문서의 실제 검증 내용 확인

사용한 명령:

```bash
rtk rg -n "Lane A remains|Lane B remains|Products Not Found|No-Derivation Confirmation|Physical-QFUDS Level 2B remains blocked|Roadmap unchanged" docs/wiki/research/audits/source_x/conclusions/040_black_hole_data_product_audit.md
```

핵심 출력:

```text
155:Lane A remains `data_product_blocked`.
180:Lane B remains `data_product_blocked`.
201:## Products Not Found
242:## No-Derivation Confirmation
258:Physical-QFUDS Level 2B remains blocked.
260:Roadmap unchanged.
```

result 문서의 핵심 내용은 다음과 같다.

```text
Lane A:
- Farrah 2023, Croker 2024, Lacy 2024, Amendola 2024, LVK/GWTC products 확인
- CCBH figure/table/code-route/product hit는 있음
- 하지만 QFUDS-usable rho_BH(a) 또는 d rho_BH / dln(a)는 없음

Lane B:
- entropy inventory, cosmic entropy budget, merger entropy history hit는 있음
- Chen/Jani/Kephart 2026 같은 product-shaped hit는 있음
- 하지만 QFUDS-usable S_BH(a) 또는 dS_BH / dln(a)는 없음
```

해석:

- H2는 지지된다. 제품은 일부 찾았지만 QFUDS-usable 조건을 통과하지
  않았다.
- H5도 지지된다. "문헌 없음"이 아니라 "문헌과 일부 product는 있지만
  QFUDS admission에 필요한 product는 없음"이다.

### 3.6 Level 2B glossary 확인

사용한 명령:

```bash
rtk sed -n '378,456p' docs/wiki/glossary/repository_levels.md
```

핵심 출력:

```text
| 2B | physical perturbation closure | blocked | retained branch failed Level 1.5 physical promotion | Requires a new physical-QFUDS branch that first provides `X`, `Q^nu`, phase-B vacuum-pressure rationale, `delta Q`, and known-model distinction |
```

그리고 glossary는 promotion criteria를 다시 적는다.

```text
Requires a new physical-QFUDS branch that first provides `X`, `Q^nu`, phase-B vacuum-pressure rationale, `delta Q`, and known-model distinction
```

해석:

- `040` audit가 product hit를 찾더라도 Level 2B를 열 수 없다.
- Level 2B는 data availability 문제가 아니라 physical branch admission
  문제다.
- 이번 result가 "not physics_blocked"라고 한 이유도 이 때문이다. 아직
  물리적으로 죽인 게 아니라, admission에 필요한 data product가 부족한
  상태로 분류했다.

H4는 지지된다.

### 3.7 검증 명령 확인

작업 중 실행한 검증 명령:

```bash
rtk python3 scripts/validate_docs.py
rtk python3 scripts/research_consistency.py
rtk git diff --check -- docs/wiki/research/audits/source_x docs/wiki/research/audits/README.md
rtk git diff -- docs/05_next_steps/000_roadmap.md
```

핵심 출력:

```text
docs validation passed
```

```text
CONSISTENCY PASSED: roadmap is the single source of truth; no drift detected
```

`git diff --check`와 roadmap diff는 출력이 없었다. 여기서 출력 없음은
각각 whitespace error 없음, roadmap 변경 없음으로 읽었다.

해석:

- frontmatter, H1/title, crosslink, status drift check를 통과했다.
- roadmap은 실제로 수정되지 않았다.

## 4. 추가 확인: 실제로 확인하지 않은 것

이번 audit가 하지 않은 것도 명시해야 한다.

| 하지 않은 것 | 왜 하지 않았나 |
| --- | --- |
| External code 실행 | plan은 product coverage audit이지 reproducibility rerun이 아니었다 |
| LVK/GWTC product 다운로드 | plan/result 모두 "no assets downloaded" boundary를 유지했다 |
| Chen/Jani/Kephart 2026 수치 재구성 | result는 externally found gap 기록까지만 했다 |
| Literature cache 신규 파일 생성 | 외부 hit를 audit coverage로 기록했을 뿐 cache promotion은 하지 않았다 |
| Roadmap / decision log 수정 | 새 physical evidence가 아니므로 status authority를 건드리지 않았다 |
| Physical-QFUDS Level 2B 작업 | glossary 기준 admission-rule items가 없었다 |

이 부분이 중요하다. "외부 source를 봤다"와 "외부 source를 repo evidence로
캐시했다"는 다르다. 이번 결과는 후자까지 가지 않았다.

## 5. 결론 / 해결

오늘 선택한 해결은 다음과 같다.

| 결정 | 고른 것 | 안 고른 대안 | 근거 |
| --- | --- | --- | --- |
| `040` 번호 사용 | `040`을 data-product interlock으로 사용 | 기존 예약대로 `040_phase4_delta_q...` 유지 | 사용자 요청이 filename을 명시했고, Phase 4 derivation 전에 product gate가 필요했다 |
| Phase 4 번호 | future delta-Q를 `041`로 이동 | `040` 충돌 방치 | Source-X read order가 한 route에서 plan/result와 future derivation을 구분해야 했다 |
| Result 문서 위치 | `source_x/conclusions/040_black_hole_data_product_audit.md` | `plans/` 아래에 실행 결과 추가 | 실행 결과는 plan이 아니라 conclusion/result 성격이므로 기존 Source-X 패턴을 따랐다 |
| External hits 처리 | result 문서에 `externally_found_not_cached` / `recorded_gap_only`로 기록 | literature cache와 assets를 바로 추가 | plan은 scope-limited product coverage audit이고, 다운로드/추출을 요구하지 않았다 |
| Status 처리 | `data_product_blocked`, `not physics_blocked` 유지 | `physics_blocked`, Level 2B open, roadmap update | glossary와 user prompt 모두 physical admission을 금지했다 |

최종 상태:

```text
Lane A remains data_product_blocked.
Lane B remains data_product_blocked.
Physical-QFUDS Level 2B remains blocked.
Roadmap unchanged.
```

이것은 실패가 아니라 좋은 audit 결과다. 다음 단계로 가기 전에 무엇이
부족한지 더 정확해졌기 때문이다.

## 6. 재발 방지 / 운영 메모

- Source-X chain에서 product availability와 physical derivation을 섞지 않는다.
- `literature hit`, `data-product hit`, `reproducibility hit`,
  `QFUDS-usable hit`를 같은 말로 쓰지 않는다.
- `Q^nu`라는 문자열이 등장하면 항상 "derived인가, admission condition인가,
  future gate인가"를 구분한다.
- Level 2B를 언급할 때는 첫 substantive mention에
  [Repository Levels Glossary](../glossary/repository_levels.md)를 붙인다.
- External product를 실제로 다운로드하거나 추출하면 그때만
  `docs/wiki/research/assets/` README와 cache update를 만든다.
- Roadmap은 새 physical evidence가 생긴 경우에만 바꾼다.

## 7. 타임라인

- 2026-06-10 16:07 KST: Source-X audit 구조 개편 커밋.
- 2026-06-10 16:09 KST: black-hole-coupled source audit 커밋.
- 2026-06-10 17:34 KST: audit 구조와 파일 컨벤션 개편 커밋.
- 2026-06-10 18:03 KST: Phase 3 `Q^nu` derivation attempt plan 커밋.
- 2026-06-10 18:16 KST: Phase 3 result에서 `Q^nu` 이전 data 부족 상태 기록.
- 2026-06-10 18:32 KST: `040_black_hole_data_product_audit_plan.md` 추가.
- 2026-06-10 18:34 KST: `040_black_hole_data_product_audit.md` 추가.
- 2026-06-10 이후: 이 postmortem에서 오늘 source_x 작업과 채팅 프롬프트
  trail을 회고 문서로 고정.

## 부록 A - 디버깅 명령어 모음

### 오늘 source_x 관련 커밋 보기

```bash
rtk proxy git log --all --format='%h %ad %an %s' --date=iso --since='2026-06-10 00:00' -- docs/wiki/research/audits/source_x docs/wiki/research/audits/README.md
```

일반적으로 `git log -- <path>`는 특정 path에 영향을 준 commit만 본다.
이번 사건에서는 "오늘 source_x에서 실제로 어떤 순서로 일이 진행됐나"를
확인하는 데 썼다.

### 특정 커밋의 파일 변경 목록 보기

```bash
rtk proxy git show --name-status --oneline cd756a2 d2072b0
```

`git show --name-status`는 commit이 어떤 파일을 추가, 수정, 삭제했는지
보여준다. 이번 사건에서는 plan commit과 result commit이 audit 문서와
index만 바꿨고 roadmap은 건드리지 않았음을 확인했다.

### Source-X 파일 구조 보기

```bash
rtk rg --files docs/wiki/research/audits/source_x | sort
```

`rg --files`는 저장소 파일 목록을 빠르게 출력한다. 이번 사건에서는
`plans/040...`과 `conclusions/040...`이 둘 다 존재하고, Source-X chain이
phase별로 정리되어 있음을 확인했다.

### Boundary 문장 확인하기

```bash
rtk rg -n "data_product_blocked|not physics_blocked|Do not derive Q\\^nu|Physical-QFUDS Level 2B|Roadmap unchanged" docs/wiki/research/audits/source_x/plans/040_black_hole_data_product_audit_plan.md
```

`rg -n`은 match된 line number를 같이 보여준다. 이번 사건에서는 plan이
정말로 no-derivation, no-roadmap-change, no-Level-2B-open boundary를
문서 안에 갖고 있는지 확인했다.

### Result 결론 확인하기

```bash
rtk rg -n "Lane A remains|Lane B remains|Products Not Found|No-Derivation Confirmation|Physical-QFUDS Level 2B remains blocked|Roadmap unchanged" docs/wiki/research/audits/source_x/conclusions/040_black_hole_data_product_audit.md
```

이 명령은 result 문서가 plan의 acceptance criteria를 실제로 반영했는지
확인하는 데 썼다.

### Glossary에서 Level 2B 정의 확인하기

```bash
rtk sed -n '378,456p' docs/wiki/glossary/repository_levels.md
```

`sed -n 'A,Bp'`는 파일의 특정 line range만 출력한다. 이번 사건에서는
Level 2B가 왜 blocked이고, 어떤 admission-rule items가 필요한지 확인했다.

### 문서 validator 실행하기

```bash
rtk python3 scripts/validate_docs.py
```

이 command는 frontmatter, H1/title, duplicate `doc_id`, active-doc 규칙을
검사한다. 이번 사건에서는 `docs validation passed`로 통과했다.

### Research consistency 확인하기

```bash
rtk python3 scripts/research_consistency.py
```

이 command는 roadmap status drift와 experiment/result consistency를
확인한다. 이번 사건에서는 `CONSISTENCY PASSED: roadmap is the single source
of truth; no drift detected`로 통과했다.

### Whitespace와 roadmap diff 확인하기

```bash
rtk git diff --check -- docs/wiki/research/audits/source_x docs/wiki/research/audits/README.md
rtk git diff -- docs/05_next_steps/000_roadmap.md
```

둘 다 출력이 없으면 각각 whitespace error 없음, roadmap 변경 없음으로
읽을 수 있다.

이런 부류의 문제는 보통 이 순서로 푼다.

```text
commit 범위 확인
-> 변경 파일 확인
-> boundary 문장 확인
-> glossary/status authority 확인
-> validator와 roadmap diff로 drift 확인
```

## 부록 B - 도메인 개념 완전 해설

### 왜 product hit가 QFUDS success가 아닌가

LVK/GWTC처럼 좋은 공개 product가 있어도 그 product는 보통 자기 분야의
질문에 맞춰 만들어져 있다. 예를 들어 compact-binary population release는
merger population, mass distribution, redshift evolution을 재현하는 데
좋다.

하지만 QFUDS가 원하는 것은 더 좁다.

```text
X =
Q^nu =
phase-B vacuum-pressure rationale =
delta Q =
known-model distinction =
```

즉 "public data가 있다"는 말은 아직 "QFUDS physical source가 있다"가
아니다. 중간에 적어도 세 개의 변환이 더 필요하다.

```text
external product
-> QFUDS candidate X
-> covariant transfer Q^nu
-> perturbation route delta Q
```

이번 audit는 첫 화살표도 아직 통과하지 못했다고 본다. 일부 product는
있지만 `rho_BH(a)`, `d rho_BH / dln(a)`, `S_BH(a)`, `dS_BH / dln(a)`로
정리된 QFUDS-usable product가 아니기 때문이다.

### 왜 `not physics_blocked`라고 썼나

`physics_blocked`라고 쓰면 "블랙홀 lane은 물리적으로 불가능하다고
판정했다"는 뜻으로 읽힐 수 있다. 이번 작업은 그렇게 강한 결론을 내리지
않았다.

이번 결론은 더 좁다.

```text
현재 확인한 source들 안에서는 QFUDS-usable data product가 없다.
그래서 다음 physical derivation으로 갈 수 없다.
하지만 이것만으로 모든 black-hole route를 물리적으로 반증한 것은 아니다.
```

그래서 상태는 `data_product_blocked`, not `physics_blocked`다.
