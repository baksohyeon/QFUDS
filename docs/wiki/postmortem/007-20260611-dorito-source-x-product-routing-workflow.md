---
doc_id: postmortem-007-source-x-product-routing-workflow
id: postmortem-007-source-x-product-routing-workflow
seq: 7
title: "Source-X product routing 혼선 포스트모템"
doc_type: postmortem
type: postmortem
stage: reference
status: reference
wiki_status: active
evidence_role: provenance
depends_on:
  - source_x_investigation_index
  - workflow-research-investigation-result-routing
  - audit_2026_06_11_product_recovery_extraction_result
  - audit_2026_06_11_chen_figure5_numeric_digitization_result
  - audit_2026_06_11_chen_gamma_shape_comparison_result
next_gate: use the result-routing workflow before any future asset product execution is treated as complete
date: 2026-06-11
context: Source-X product-recovery extraction, Chen Figure 5 digitization, and Chen-Gamma shape-comparison audit routing
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
    note: "Recorded after the Source-X asset product routing confusion was resolved with a result-routing workflow and 043/046/047 conclusion closeouts."
tags: [postmortem, source-x, research-assets, digitization, routing]
relations:
  - .agent/workflows/research-investigation-result-routing-workflow.md
  - .agent/workflows/research-asset-product-workflow.md
  - docs/wiki/research/investigations/source_x/README.md
  - docs/wiki/research/investigations/source_x/conclusions/043_product_recovery_extraction_result.md
  - docs/wiki/research/investigations/source_x/conclusions/046_chen_figure5_numeric_digitization_result.md
  - docs/wiki/research/investigations/source_x/conclusions/047_chen_gamma_shape_comparison_result.md
code_refs:
  - file: .agent/workflows/research-investigation-result-routing-workflow.md
    note: "New operational rule: derived asset products stay under assets, but their interpretation requires a Source-X conclusion closeout."
  - file: docs/wiki/research/investigations/source_x/README.md
    note: "Read-order index now shows plan/result pairs for 043, 046, and 047."
  - file: docs/wiki/research/investigations/source_x/conclusions/043_product_recovery_extraction_result.md
    note: "Closeout for manual structured extracts created under paper-level asset directories."
  - file: docs/wiki/research/investigations/source_x/conclusions/046_chen_figure5_numeric_digitization_result.md
    note: "Closeout for Chen Figure 5 numeric digitization CSV and provenance."
  - file: docs/wiki/research/investigations/source_x/conclusions/047_chen_gamma_shape_comparison_result.md
    note: "Closeout for qualitative Chen-Gamma timing-shape comparison."
---

# Source-X product routing 혼선 포스트모템

## 사건 한 줄 요약

이번 사건은 Chen/Lacy extraction과 Chen Figure 5 digitization 자체가
틀어졌다기보다, `assets/`에 생긴 derived product를 Source-X investigation
chain이 어떻게 판정해야 하는지 늦게 명문화된 사건이다.

최종 정리는 단순하다.

```text
asset product는 paper-level assets 아래에 둔다.
그 product가 무엇을 바꿨는지는 Source-X conclusions 아래에 closeout으로 닫는다.
plan-only task는 plans에 둔다.
```

이 정리 후에도 프로젝트 상태는 바뀌지 않았다. black-hole lane은
`data_product_blocked`이고, Physical-QFUDS Level 2B는 blocked이며,
roadmap은 unchanged다.

## 0. 사전 지식

| 용어 | 이 사건에서의 의미 |
| --- | --- |
| `assets/` | 논문·릴리스 단위 source PDF, TeX, figure, digitization CSV/Markdown, provenance를 보관하는 paper-level product cache |
| `plans/` | candidate selection, extraction plan, digitization plan, comparison plan처럼 아직 결과를 만들지 않는 실행 명세 |
| `conclusions/` | 실행 뒤에 무엇이 회수됐고 무엇이 아직 막혔는지 판정하는 Source-X closeout |
| `manual_structured_extract` | 논문에서 source location, units, equation, figure, table, missing fields를 수동 구조화한 상태 |
| `numeric_digitized` | figure에서 좌표, axis mapping, units, provenance를 갖춘 numeric CSV를 만든 상태 |
| `data_product_blocked` | usable product가 아직 physical-admission requirements를 만족하지 못한 상태 |
| `qfuds_usable_numeric_product` | candidate `X`, normalization, covariance/uncertainty route, `Q^nu`/`delta Q` route 등 admission boundary가 충족된 상태. 이번 사건에서는 존재하지 않는다 |

중요한 구분은 이것이다.

```text
asset product state != physical admission state
```

`manual_structured_extract`나 `numeric_digitized`가 생겨도, 그것만으로
QFUDS support, candidate `X`, `Q^nu`, `delta Q`, Level 2B admission이
생기지는 않는다.

## 1. 증상

작업 중 사용자가 계속 같은 구조적 질문을 던졌다.

```text
research/assets 에서 문서가 작성됨.
원래 investigations 폴더 안에서 정리되어야하는거아님?
research 는 딱 논문 자료들 관리하는 곳이잖아.
```

이 질문은 맞았다. 다만 답은 "assets가 틀렸다"가 아니라 "assets만
있으면 부족하다"였다.

이후에도 같은 혼선이 반복됐다.

```text
source_x 에서 result 에 들어가야하는거아니여? 아닌가 ?
```

그리고 최종적으로 사용자는 구조 역할 정의와 workflow를 요구했다.

```text
@docs/wiki/research/ 구조 역할 정의 명확히하고. 관련 워크플로우 만들어 @.agent/ 에다가.
digitization 도 맞는거같긴한데 그래도 최소한 conclusion 이런 곳에 요약이나 결론이나 결과보고서라도 적던가.
```

즉 증상은 파일 위치 하나의 문제가 아니었다.

- extraction record와 digitized CSV는 `assets/.../digitization/`에 있는 게 맞다.
- 하지만 그 산출물이 Source-X 상태를 어떻게 바꿨는지는 `conclusions/`에 있어야 한다.
- plan-only 문서는 `plans/`에 있어야 하고, result closeout은 `conclusions/`에 있어야 한다.
- workflow가 없으면 agent가 매번 사용자 프롬프트로 routing을 다시 배운다.

## 2. 첫 의문 + 가설

| 가설 | 왜 그럴 수 있는지 | 어떻게 확인할지 |
| --- | --- | --- |
| H1. extraction/digitization 파일이 `assets/.../digitization/`에 있는 것은 맞다 | source PDF, TeX, figures, derived CSV/Markdown은 paper-level asset product다 | [research-investigation-result-routing-workflow.md](../../../.agent/workflows/research-investigation-result-routing-workflow.md)의 folder role table을 확인한다 |
| H2. asset product만 있으면 Source-X chain이 끊긴다 | product interpretation이 assets 안에만 있으면 investigation decision을 읽기 어렵다 | workflow의 "Do not leave product interpretation only inside assets" rule을 확인한다 |
| H3. 043/046 같은 실행 결과에는 conclusion closeout이 필요하다 | manual extract나 numeric CSV가 만들어졌기 때문이다 | 043/046 result closeout이 created asset path, method, missing fields, blocked status를 기록하는지 확인한다 |
| H4. 044/045 같은 plan-only 문서는 conclusions에 없어도 된다 | 아직 execution이나 judgment가 없기 때문이다 | plans/README와 source_x read order에서 plan/result split을 확인한다 |
| H5. 047 comparison result도 conclusions에 있어야 한다 | 실제 qualitative comparison judgment를 수행했기 때문이다 | 047 result가 compared curves, Gamma parameters, missing fields, final boundary를 기록하는지 확인한다 |
| H6. 이 정리는 roadmap이나 Level 2B status를 바꾸지 않는다 | workflow는 routing process이고 physical evidence가 아니다 | validation과 roadmap diff를 확인한다 |

확인 순서는 "가장 싼 증거"부터 잡았다. 먼저 workflow와 Source-X index를
확인하고, 그 다음 043/046/047 result closeout의 body가 실제로
asset product interpretation을 담는지 봤다.

## 3. 진단: 실제 상태 확인

### 3.1 postmortem 번호와 작성자 확인

먼저 새 문서 번호와 작성자를 확인했다.

```bash
rtk ls docs/wiki/postmortem
```

출력:

```text
001-20260609-dorito-li-2025-data-cache.md  36.3K
002-20260609-dorito-iv-ide-timing-checkpoint.md  29.4K
003-20260610-dorito-qfuds-scope-demotion-retrospective.md  17.4K
004-20260610-dorito-source-x-data-product-audit.md  24.2K
005-20260611-dorito-research-asset-digitization-automation.md  50.0K
006-20260611-dorito-precommit-regression-test-scope.md  13.9K
README.md  1.0K
```

따라서 이번 문서는 `007`이다.

```bash
rtk git config user.name
rtk git config user.email
```

출력:

```text
Dorito
bori12370@gmail.com
```

frontmatter에는 기존 convention에 맞춰 lowercase `dorito`를 썼다.

### 3.2 workflow가 핵심 rule을 표현하는지 확인

새 workflow의 core rule을 확인했다.

```bash
rtk sed -n '1,120p' .agent/workflows/research-investigation-result-routing-workflow.md
```

핵심 출력:

```text
Use this workflow whenever a research investigation creates, changes, judges, or
routes an asset-level product under `docs/wiki/research/`.
...
Do not leave product interpretation only inside `assets/`.
```

folder role table도 같은 결론을 준다.

```text
`docs/wiki/research/assets/<paper_or_release_key>/digitization/`
  Markdown conversions, manual extracts, digitized CSV/JSON, asset provenance
  Do not use for: Source-X decision closeouts

`docs/wiki/research/investigations/<chain>/plans/`
  candidate selection, execution plans, digitization plans, prompt/scope records
  Do not use for: result claims

`docs/wiki/research/investigations/<chain>/conclusions/`
  result closeouts, decision summaries, blocker judgments
  Do not use for: raw assets or numeric tables
```

판정:

- H1 지지. `assets/.../digitization/` 자체는 맞는 위치다.
- H2 지지. asset product 해석을 assets에만 두면 chain이 끊긴다.

### 3.3 Source-X read order가 plan/result split을 보여주는지 확인

Source-X index를 확인했다.

```bash
rtk sed -n '45,125p' docs/wiki/research/investigations/source_x/README.md
```

핵심 출력:

```text
| 043 | Product-Recovery Extraction Plan | product-recovery extraction execution scope |
| 043 | Product-Recovery Extraction Result | product-recovery extraction closeout |
| 044 | Numeric Digitization Planning Audit | numeric digitization target selection |
| 045 | Chen Figure 5 Numeric Digitization Execution Plan | Chen Figure 5 digitization execution specification |
| 046 | Numeric Digitization Execution Plan | approved Chen Figure 5 numeric digitization scope |
| 046 | Chen Figure 5 Numeric Digitization Result | Chen Figure 5 numeric digitization closeout |
| 047 | Chen-Gamma Shape Comparison Plan | plan-only qualitative shape comparison scope |
| 047 | Chen-Gamma Shape Comparison Result | qualitative Chen-Gamma shape comparison closeout |
```

그리고 short interpretation에는 다음 boundary가 있다.

```text
`043` records both the extraction plan and the extraction-result closeout.
...
`046` also includes a result closeout that records the product-state advance
to `numeric_digitized` while preserving the `data_product_blocked` physical
admission boundary.
...
`047` also includes a result closeout that records limited qualitative
timing-shape resemblance and material peak/tail mismatch. It preserves the
`data_product_blocked` boundary and makes no QFUDS support claim.
```

판정:

- H3 지지. 043/046은 execution 결과이므로 conclusions closeout이 필요했다.
- H4 지지. 044/045는 plan-only라 conclusions에 없어도 된다.
- H5 지지. 047은 comparison judgment를 수행했기 때문에 result closeout이 필요했다.

### 3.4 043 result가 asset extract를 Source-X closeout으로 판정하는지 확인

`043_product_recovery_extraction_result.md`는 asset-level extract가 어디에
있고, Source-X decision은 무엇인지 분리한다.

```bash
rtk sed -n '1,120p' docs/wiki/research/investigations/source_x/conclusions/043_product_recovery_extraction_result.md
```

핵심 출력:

```text
The source extraction records remain under the paper-level asset directories:

- Lacy 2024 SMBH density recovery extract
- Chen 2026 merger entropy history recovery extract

Those files are asset-level extraction records. This file is the Source-X
conclusion record that states what the extraction changed and what remains
blocked.
```

status boundary도 직접 적혀 있다.

```text
manual_structured_extract records now exist.
qfuds_usable_numeric_product does not exist.
Candidate X boundary is missing.
...
The black-hole lane remains:

data_product_blocked
```

판정:

- 043은 "assets가 틀렸다"가 아니라 "assets 산출물에 대한 Source-X
  closeout이 필요하다"는 해법을 정확히 따른다.

### 3.5 046 result가 numeric digitization을 과장하지 않는지 확인

`046_chen_figure5_numeric_digitization_result.md`는 Chen Figure 5 CSV를
asset product로 인정하되 physical admission으로 올리지 않는다.

```bash
rtk sed -n '1,150p' docs/wiki/research/investigations/source_x/conclusions/046_chen_figure5_numeric_digitization_result.md
```

핵심 출력:

```text
The Chen Figure 5 asset now has a `numeric_digitized` source-history candidate.

The black-hole lane remains `data_product_blocked`, not physics_blocked.

qfuds_usable_numeric_product does not exist.
Candidate X boundary is missing.
```

또한 recovered curves는 정확히 asset product로 제한된다.

```text
chen_fig5_blue_entropy_central
chen_fig5_blue_entropy_lower
chen_fig5_blue_entropy_upper
chen_fig5_red_entropy_density_central
chen_fig5_red_entropy_density_lower
chen_fig5_red_entropy_density_upper
```

판정:

- `numeric_digitized`는 실제 진전이다.
- 하지만 missing fields가 남아 있으므로 `qfuds_usable_numeric_product`가
  아니다.

### 3.6 047 result가 comparison을 physical claim으로 바꾸지 않는지 확인

`047_chen_gamma_shape_comparison_result.md`는 실행된 comparison result다.
따라서 conclusions에 있는 것이 맞다.

```bash
rtk sed -n '1,220p' docs/wiki/research/investigations/source_x/conclusions/047_chen_gamma_shape_comparison_result.md
```

핵심 boundary:

```text
The comparison is qualitative only.
...
This result does not fit a curve.
This result does not derive Q^nu.
This result does not derive delta Q.
This result does not define candidate X.
This result does not claim QFUDS support.
```

핵심 decision:

```text
It records that Chen red entropy density is the closer qualitative timing
comparator than Chen blue total entropy, but neither curve supplies the missing
physical-admission items.

data_product_blocked
```

판정:

- 047 result는 conclusions에 있어야 한다.
- 044/045와 달리 047은 plan-only가 아니다. 실제 qualitative comparison
  judgment가 들어 있기 때문이다.

### 3.7 현재 worktree 상태 확인

현재 작업 전후 uncommitted state도 확인했다.

```bash
rtk git status --short
```

출력:

```text
 M docs/wiki/research/investigations/source_x/README.md
 M docs/wiki/research/investigations/source_x/conclusions/README.md
?? docs/wiki/research/investigations/source_x/conclusions/047_chen_gamma_shape_comparison_result.md
```

이 상태는 직전 `047` 작업의 산출물이다. 이번 postmortem은 그 위에
새 파일 하나를 추가한다. 기존 변경을 되돌리거나 재해석하지 않는다.

## 4. 추가 확인

이번 사건에서 확인하지 않은 것도 명시한다.

- `043`, `046`, `047` 문서가 아직 commit된 상태인지는 확인하지 않았다.
- GitHub PR 번호나 CI run URL은 확인하지 않았다.
- Chen Figure 5 numeric digitization 값 자체의 scientific 재검증은 이
  postmortem 범위가 아니다.
- roadmap status를 바꾸는 작업은 수행하지 않았다.

## 5. 결론 / 해결

이번 사건의 결론은 routing rule 하나로 정리된다.

```text
assets = product storage
plans = future execution scope
conclusions = executed result judgment
```

실제 해결은 세 단계였다.

| 결정 | 고른 것 | 안 고른 대안 | 근거 |
| --- | --- | --- | --- |
| asset extract 위치 | `assets/<paper>/digitization/` 유지 | extracts를 investigations로 이동 | extract 자체는 paper-level derived asset이다 |
| result 판정 위치 | `investigations/source_x/conclusions/` closeout 생성 | asset README에 상태 판정만 적기 | Source-X decision은 investigation chain에서 읽혀야 한다 |
| plan-only 위치 | `plans/` 유지 | 모든 numbered record를 conclusions에 복사 | plan-only task는 아직 result claim이 없다 |
| workflow 위치 | [research-investigation-result-routing-workflow.md](../../../.agent/workflows/research-investigation-result-routing-workflow.md) | chat prompt나 개별 README에만 설명 | agent가 반복 실행할 routing rule은 workflow가 SSOT여야 한다 |
| status 처리 | `data_product_blocked` 유지 | numeric product를 QFUDS support로 해석 | candidate `X`, QFUDS normalization, `Q^nu`, `delta Q`가 없다 |

현재 chain은 이렇게 닫힌다.

```text
043 plan -> asset manual extracts -> 043 conclusion closeout
044 plan-only digitization planning -> no conclusion needed
045 plan-only Chen Figure 5 execution spec -> no conclusion needed
046 execution plan -> asset CSV/provenance -> 046 conclusion closeout
047 comparison plan -> qualitative comparison result -> 047 conclusion closeout
```

## 6. 재발 방지 / 운영 메모

다음부터 agent는 research product 작업 전후에 이 체크리스트를 써야 한다.

- 새 파일이 raw source, rendered figure, converted Markdown, CSV, provenance라면 `assets/<paper_or_release_key>/...` 아래에 둔다.
- 새 파일이 "무엇을 할지"만 정하는 문서라면 `investigations/<chain>/plans/`에 둔다.
- 새 파일이 "무엇이 나왔고 무엇이 아직 막혔는지" 판단한다면 `investigations/<chain>/conclusions/`에 둔다.
- `manual_structured_extract` 또는 `numeric_digitized`가 생기면 matching conclusion closeout이 필요한지 확인한다.
- conclusion closeout에는 최소한 created asset paths, method, quality state, recovered quantities, missing fields, candidate `X`, `Q^nu`, `delta Q`, roadmap, Level 2B status를 쓴다.
- plan-only task에는 matching conclusion을 만들지 않는다.
- asset README는 product inventory에 가깝게 유지하고, Source-X decision을 대신하게 하지 않는다.

운영 rule:

```text
Do not leave product interpretation only inside assets.
```

이 한 줄이 이번 사건의 핵심 재발방지 문장이다.

## 7. 타임라인

- 041: Lacy/Chen을 product-recovery candidate로 선택했다.
- 042: future 043 extraction이 무엇을 봐야 하는지 execution plan을 작성했다.
- 043: Lacy/Chen manual structured extracts가 asset 아래에 생겼고, 이후 Source-X conclusion closeout이 필요하다는 점이 드러났다.
- 044: Chen Figure 5를 first numeric digitization target으로 고른 plan-only audit을 작성했다.
- 045: Chen Figure 5 digitization execution spec을 작성했다.
- 046: Chen Figure 5 CSV/provenance가 asset 아래에 생겼고, Source-X conclusion closeout으로 product-state advance와 remaining blockers를 기록했다.
- workflow: [research-investigation-result-routing-workflow.md](../../../.agent/workflows/research-investigation-result-routing-workflow.md)를 만들어 asset product와 investigation result routing을 분리했다.
- 047: Chen-Gamma qualitative comparison을 실행했고, result는 conclusions에 기록했다.
- postmortem 007: 이 routing 혼선을 재발방지 문서로 남겼다.

## 부록 A -- 디버깅 명령어 모음

### 기존 postmortem 번호 확인

```bash
rtk ls docs/wiki/postmortem
```

일반적으로 특정 폴더의 파일 목록을 본다. 이 사건에서는 마지막 번호가
`006`인지 확인해서 새 파일을 `007`로 잡는 데 썼다.

### git author 확인

```bash
rtk git config user.name
rtk git config user.email
```

일반적으로 현재 repository에서 git commit author 정보를 확인한다. 이
사건에서는 frontmatter의 `created_by`, `updated_by`, `last_verified_by`
값을 기존 convention과 맞추기 위해 사용했다.

### workflow 핵심 rule 확인

```bash
rtk sed -n '1,120p' .agent/workflows/research-investigation-result-routing-workflow.md
```

`sed -n 'A,Bp'`는 파일의 A번째 줄부터 B번째 줄까지 출력한다. 이
사건에서는 workflow의 core rule과 folder role table을 확인했다.

### Source-X read order 확인

```bash
rtk sed -n '45,125p' docs/wiki/research/investigations/source_x/README.md
```

일반적으로 index 문서의 특정 구간만 읽을 때 쓴다. 이 사건에서는
043/046/047의 plan/result pair가 read order에 들어갔는지 확인했다.

### conclusion closeout 확인

```bash
rtk sed -n '1,120p' docs/wiki/research/investigations/source_x/conclusions/043_product_recovery_extraction_result.md
rtk sed -n '1,150p' docs/wiki/research/investigations/source_x/conclusions/046_chen_figure5_numeric_digitization_result.md
rtk sed -n '1,220p' docs/wiki/research/investigations/source_x/conclusions/047_chen_gamma_shape_comparison_result.md
```

일반적으로 새 conclusion 문서가 실제로 required boundary를 쓰는지 볼 때
쓴다. 이 사건에서는 세 문서가 각각 `manual_structured_extract`,
`numeric_digitized`, qualitative comparison result를 과장하지 않고
`data_product_blocked`로 닫는지 확인했다.

### 현재 변경 범위 확인

```bash
rtk git status --short
```

일반적으로 현재 worktree에 어떤 파일이 modified/untracked인지 본다. 이
사건에서는 직전 047 작업의 uncommitted files가 남아 있음을 확인했고,
이번 postmortem은 그 위에 새 파일 하나를 추가한다는 점을 분리했다.

이런 부류의 문제는 보통 이 순서로 푼다: 폴더 역할 문서 확인 -> index
read order 확인 -> result closeout 확인 -> status boundary 확인 -> git
status로 변경 범위 확인.
