---
doc_id: audit_2026_06_18_iv_ide_formalism_study_map_ko
title: "2026-06-18 IV/IDE Formalism Study Map"
doc_type: guide
stage: reference
status: completed
evidence_role: audit
depends_on:
  - audit_2026_06_18_academic_derivation_bridge_ko
  - postmortem-015-bruteforce-gamma-method-retrospective
  - result_004_p1_model_family_positioning
  - result_005_timing_prior_usefulness
  - result_006_literature_timing_support_audit
  - plan_2026_06_18_candidate_equation_proposal_template
  - roadmap
next_gate: learn IV/IDE formalism before any future QFUDS candidate fit
last_updated: 2026-06-18
---

# 2026-06-18 IV/IDE Formalism Study Map

## Purpose

이 문서는 QFUDS를 다시 살리려는 문서가 아니다.

목적은 다음 질문에 답하는 실행 지도다.

```text
만약 brute-force Gamma 접근을 다시 하지 않고,
학계가 실제로 모델을 세우는 순서대로 따라가면 무엇을 먼저 봐야 하는가?
```

결론부터 말하면, 이 경로는 해볼 만하다. 다만 성공 기준은 "QFUDS가
맞는다"가 아니다.

```text
성공 = 내가 만든 Gamma(a)가 IV/IDE formalism의 어느 단계에서 멈췄는지
정확히 이해한다.
```

## Workflow Boundary

This study map follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md)
only to preserve source-state boundaries.

No new external source, PDF, table, posterior product, cache, digitization, or
availability claim is introduced here. Source states are inherited from the
owning records:

- retained P1 positioning and timing records: repository result records;
- Escamilla 2023 and Martinelli 2019 literature records:
  `literature_record_cached`, with raw assets `asset_available_not_downloaded`;
- Exp006 table-level timing audit: table-level products only;
- baseline-reference guardrails: cached constraints remain baseline
  constraints only, not QFUDS evidence.

This document does not use NASA/LAMBDA, BAO, CMB, LSS, or survey thresholds to
choose `Gamma(a)`, amplitude, width, transition redshift, or source scale.

## Not Too Much?

이건 뻘짓이 아니다. 단, 위치를 정확히 잡아야 한다.

| Wrong framing | Safer framing |
| --- | --- |
| QFUDS를 다시 밀어 본다 | IV/IDE formalism을 공부하면서 QFUDS가 어디서 멈췄는지 본다 |
| README에 새 연구 방향으로 크게 올린다 | README에는 학습 경로로 한 줄만 둔다 |
| `Gamma(a)`를 source로 복구한다 | `Gamma(a)`를 phenomenological interaction history로 둔다 |
| 관측값으로 다시 맞춘다 | 먼저 equations, frame, perturbations, null models를 배운다 |

## Study Path

### 1. Model Taxonomy

먼저 이름표를 붙인다.

```text
LCDM
effective w(a)
unified dark fluid
interacting vacuum
interacting dark energy
coupled quintessence
running vacuum / HDE
modified gravity / backreaction
```

목표는 QFUDS의 자리를 찾는 것이다. 현재 retained P1의 자리는 이미:

```text
interacting vacuum / time-dependent IDE subset
```

이다.

### 2. Background Source Term

그 다음 학계 표기와 QFUDS 표기를 맞춘다.

```math
Q = H \Gamma(a)\rho_A.
```

여기서 할 일은 fitting이 아니다.

```text
Q의 sign convention
Q가 rho_c에 비례하는지 rho_de에 비례하는지
dimensionless coupling을 무엇으로 정의하는지
```

를 정리하는 것이다.

### 3. Covariant Transfer Vector

background `Q` 다음은 `Q^mu`다.

```math
\nabla_\mu T_A^{\mu\nu}=-Q^\nu,
\qquad
\nabla_\mu T_B^{\mu\nu}=+Q^\nu.
```

여기서 가장 먼저 봐야 할 선택지는:

```text
Q^mu parallel to dark matter velocity
Q^mu parallel to dark energy velocity
Q^mu parallel to total dark-sector velocity
another covariant vector
```

이다.

QFUDS P1은 phase-A frame을 골랐다. 하지만 그 선택은 물리 유도가 아니라
Level 2A closure였다.

### 4. Perturbation Closure

그 다음은 perturbation이다.

최소 질문:

```text
gauge =
delta Q =
delta Gamma =
momentum transfer =
phase-B perturbation =
sound speed =
initial conditions =
stability criterion =
```

이 단계에서 QFUDS는 P1/P2를 시험했다.

```text
P1 = stable only as interacting-vacuum phenomenology
P2 = failed at retained amplitude
```

따라서 다음 공부는 "P1을 더 QFUDS답게 포장"하는 것이 아니라, IV/IDE
논문들이 이 closure 문제를 어떻게 다루는지 보는 것이다.

### 5. Stability And Known Failures

IDE는 background가 그럴듯해도 perturbation에서 죽을 수 있다.

따라서 볼 질문:

```text
early-time large-scale instability는 언제 생기는가?
which couplings are stable?
PPF 같은 안정화 formalism은 무엇을 대신 넣는가?
안정화가 물리 유도인가, phenomenological prescription인가?
```

QFUDS에서 배운 교훈은 그대로 적용된다.

```text
stable closure != physical source
```

### 6. Boltzmann And Likelihood Layer

마지막은 CLASS/CAMB 또는 equivalent likelihood layer다.

하지만 이건 지금 바로 할 일이 아니다. Roadmap에서 Level 4는 CMB comparison이고,
현재는 막혀 있다.

현재 허용되는 것은:

```text
어떤 equations가 Boltzmann solver에 들어가야 하는지 공부한다.
```

금지되는 것은:

```text
QFUDS CMB viability를 주장한다.
```

## Re-Run Rule

만약 이 경로로 다시 실행한다면 순서는 이렇게 고정한다.

| Step | Output | Stop condition |
| --- | --- | --- |
| 1. model taxonomy | known-model sink table | retained branch is already fully absorbed |
| 2. background `Q` map | sign/convention map | `Gamma(a)` remains arbitrary timing curve |
| 3. `Q^mu` map | frame-choice matrix | no physical frame rule |
| 4. perturbation closure | `delta Q`, gauge, sound-speed checklist | closure copied only for stability |
| 5. stability literature map | known instability and PPF fallback ledger | only phenomenological stabilization exists |
| 6. likelihood readiness | required data/code/product checklist | no Boltzmann-ready equation set |

이 표를 통과하지 못하면 NASA/BAO/CMB/LSS로 가지 않는다.

## What Would Be A Useful Result?

유용한 결과는 세 가지 중 하나다.

1. **Translation success**
   - QFUDS `Gamma(a)`가 IV/IDE notation으로 완전히 번역된다.
   - 결론은 "known-model comparator"다.
2. **Blocker localization**
   - 정확히 어느 단계에서 물리 유도가 없는지 분리된다.
   - 예: `Q^mu` frame rule, phase-B pressure, `delta Q`.
3. **Candidate rejection**
   - future candidate가 template를 못 채워서 빠르게 rejected/blocked 된다.

유용하지 않은 결과:

```text
곡선이 비슷하니 QFUDS가 그럴듯하다.
```

## Minimum Next Executable Task

다음 작업은 새 fit이 아니다.

```text
Create a compact IV/IDE formalism notes ledger:
Q convention, Q^mu frame choice, perturbation closure, instability condition,
and which part retained Gamma(a) can or cannot fill.
```

그 문서는 literature study/audit여야 한다. Physical-QFUDS 결과 문서가 아니고,
README에는 "학습 경로"로만 남겨야 한다.

## Status Boundary

```text
QFUDS support = no
physical derivation = no
Level 2B = closed
Level 4 CMB = no
README role = learning path link only
next honest work = IV/IDE formalism study ledger
```
