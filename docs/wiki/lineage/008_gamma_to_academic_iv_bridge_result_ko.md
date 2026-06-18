---
doc_id: qfuds_lineage_gamma_to_academic_iv_bridge_result_ko
title: "감마에서 멈춘 곳"
doc_type: summary
stage: reference
status: provenance
evidence_role: provenance
depends_on:
  - roadmap
  - qfuds_lineage_black_hole_information_public_bridge_ko
  - audit_2026_06_18_academic_derivation_bridge_ko
  - audit_2026_06_18_tier1_iv_extraction_pass_closeout_ko
next_gate: provenance only; use Source-X records for formal extraction and do not open Level 2B
last_updated: 2026-06-18
---

# 감마에서 멈춘 곳

## 먼저 읽을 것

이 문서는 QFUDS가 맞았다는 문서가 아니다.

이 문서는 "비전공자가 때려 넣은 `Gamma(a)` 직관이 실제 학계 언어로는 어디까지
번역되고, 어디서 멈추는가"를 남기는 lineage 결과 문서다.

현재 프로젝트 상태는
[QFUDS Research Roadmap](../../05_next_steps/000_roadmap.md)이 정한다.
이 문서는 roadmap을 대신하지 않는다.

## Workflow Boundary

This lineage result does not introduce a new external web, PDF, table, product,
cache, digitization, or availability claim. It summarizes existing Source-X
records only.

External-source handling remains governed by
[Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md).
Inherited workflow states include:

```text
asset_cached
asset_extracted_not_digitized
source_text_parse
manual_structured_extract
```

This note is not QFUDS support, validation, roadmap advancement,
known-model distinction, or Physical-QFUDS Level 2B admission.

## 한 줄 결론

`Gamma(a)`는 완전히 뻘짓은 아니었다.

하지만 물리 이론도 아니었다.

지금 남은 정직한 해석은 이것이다.

```text
retained Gamma(a)
= IV/IDE 쪽으로 들어가기 위한 phenomenological timing comparator
!= QFUDS에서 유도된 source term
```

즉, `Gamma(a)`는 "내 직관이 기존 학계의 어떤 문법을 건드렸는가"를 보여 주는
입구다. `Q^mu`, pressure, perturbations, novelty를 직접 주지는 않는다.

## 내가 실제로 한 일

처음 접근은 대충 이런 형태였다.

```text
dark matter와 dark energy가 같은 sector의 두 상태라면
어떤 시점에 에너지가 넘어가는 함수가 있지 않을까?
그 전환 타이밍이 z ~= 2 근처에서 보이면 뭔가 있지 않을까?
```

그래서 `Gamma(a)`를 만들고, 여러 shape를 brute-force로 돌렸다.

이 방식은 직관을 찾는 데는 도움이 됐다. 하지만 과학적으로는 바로 위험해진다.

```text
관측 경향을 먼저 보고
전환 위치, 폭, 세기를 나중에 고른 뒤
그걸 source physics라고 부르면 순환논리다.
```

이게 지금까지 QFUDS audit harness가 계속 막아 온 핵심 위험이다.

## 실제 학계 문법은 어디서 시작하는가

Tier 1 IV/IDE 추출 결과, 실제 논문들은 보통 `Gamma(a)` 같은 감각에서 시작하지
않는다. 최소한 다음 물건들을 함께 둔다.

| 필요한 것 | 학계 IV/IDE에서 하는 일 | QFUDS 현재 상태 |
| --- | --- | --- |
| background source | `Q`를 continuity equation에 넣는다. | `Gamma(a)`로 background timing만 있음. |
| covariant transfer | `Q^mu`와 transfer frame을 정한다. | `Q^mu[X]` 유도 없음. |
| frame choice | CDM frame, DE frame, geodesic condition 등을 명시한다. | QFUDS source가 frame을 고르지 못함. |
| perturbations | `delta Q`, pressure perturbation, gauge/closure를 둔다. | placeholder나 comparator 수준. |
| stability | instability를 피하는 closure 또는 PPF/ePPF를 둔다. | source 기반 안정성 없음. |
| solver route | CAMB/CLASS/CosmoMC 같은 경로로 constraints를 건다. | physical branch가 아니라 아직 observer mode. |
| evidence language | prior, PCA, Bayes factor, likelihood boundary를 분리한다. | NASA/BAO/CMB/LSS는 evidence가 아니라 kill-map/context. |

이 차이가 전부다.

`Gamma(a)`는 "어떤 모양의 상호작용이 있으면 좋겠다"에 가깝고, 실제 논문은
"그 상호작용이 어떤 방정식과 perturbation system 안에서 의미가 있는가"부터
묻는다.

## Martinelli/Hogg를 보면 멈춤 지점이 보인다

가장 좋은 학습 표적은 Martinelli/Hogg의 interacting-vacuum geodesic-CDM
계열이다.

그 계열은 이런 식으로 간다.

```text
dot rho_c + 3H rho_c = -Q
dot V = Q
Q = -q_V H V
```

그리고 여기서 끝나지 않는다.

```text
Q^mu placement
CDM-frame / geodesic condition
perturbation closure
solver route
prior and evidence boundary
```

반면 repo-local retained convention은:

```text
Q_retained = H_conf Gamma(a) rho_A
```

겉보기에는 이렇게 바꿔 쓸 수 있어 보인다.

```text
q_V(a) ~= - (H_conf / H) Gamma(a) rho_A / V
```

하지만 이건 derivation이 아니다.

이건 사후 번역 worksheet다.

왜냐하면 `rho_A = rho_c`인지, phase B가 `V`인지, 왜 `Q^mu`가 CDM
four-velocity 방향인지, 왜 momentum transfer가 없는지, 왜 vacuum perturbation
boundary가 맞는지 QFUDS가 아직 말하지 못하기 때문이다.

## 내가 놓친 것

놓친 것은 "전환 함수" 하나가 아니었다.

놓친 것은 함수가 들어갈 전체 구조였다.

1. `Q`는 그냥 예쁜 곡선이 아니라 continuity equation 안의 source다.
2. background `Q`만 있으면 부족하다. `Q^mu`가 있어야 한다.
3. `Q^mu`만 있어도 부족하다. frame, gauge, perturbations가 있어야 한다.
4. perturbations가 있어도 부족하다. stability와 solver route가 있어야 한다.
5. solver route가 있어도 부족하다. 기존 IV/IDE와 다른 점이 있어야 한다.

이걸 모른 상태에서 `Gamma(a)` shape를 먼저 만든 것이 brute-force의 한계였다.

그래도 이 작업이 완전히 헛되지는 않은 이유는, 그 shape가 기존 학계의
interacting dark sector 문법으로 들어가는 문을 찾게 해 줬기 때문이다.

## 지금 남은 가치

남은 가치는 QFUDS를 지키는 데 있지 않다.

남은 가치는 이것이다.

```text
SF적 직관
-> toy Gamma(a)
-> IV/IDE formalism
-> known-model sink와 circularity를 거르는 audit harness
```

이 흐름은 과학적으로 겸손하다. 하지만 쓸모는 있다.

`Gamma(a)`는 물리 기원이 아니라 "실제 논문을 읽기 위한 번역 손잡이"다.
이 손잡이를 통해 `Q`, `Q^mu`, perturbation closure, PPF/ePPF, solver route,
likelihood boundary를 배울 수 있다.

## 앞으로의 정직한 작업

다음 작업은 QFUDS를 증명하는 일이 아니다.

다음 작업은 retained `Gamma(a)`가 학계 IV/IDE 언어로 어디까지 번역되고,
어디서 반드시 `unknown` 또는 `circular_if_fitted`가 되는지 표로 박는 일이다.

특히 다음 변환을 조심해야 한다.

```text
Q_retained = H_conf Gamma(a) rho_A
Q_IV = -q_V H V
```

이 두 줄 사이의 모든 변환은 다음 네 상태 중 하나로 표시해야 한다.

```text
defined
assumed
unknown
circular_if_fitted
```

`defined`가 아닌 칸이 남으면, 그건 derivation이 아니다.

## 다음 실행 지시

Create a retained-Gamma non-equivalence worksheet. Compare
`Q_retained = H_conf Gamma(a) rho_A` against the Martinelli/Hogg
`Q_IV = -q_V H V` family, and mark each conversion as `defined`, `assumed`,
`unknown`, or `circular_if_fitted`. Do not fit `Gamma(a)`, do not use
NASA/BAO/CMB/LSS as evidence, and do not open Level 2B.
