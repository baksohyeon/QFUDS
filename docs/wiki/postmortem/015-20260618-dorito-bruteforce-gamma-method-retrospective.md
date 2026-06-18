---
doc_id: postmortem-015-bruteforce-gamma-method-retrospective
id: postmortem-015-bruteforce-gamma-method-retrospective
seq: 15
title: "brute-force Gamma 접근 회고"
doc_type: postmortem
type: postmortem
stage: reference
status: reference
wiki_status: active
evidence_role: provenance
depends_on:
  - roadmap
  - result_001_gamma_scan
  - result_001_5_phase_transfer_physicality
  - result_004_p1_model_family_positioning
  - result_005_timing_prior_usefulness
  - result_006_literature_timing_support_audit
  - audit_2026_06_18_academic_derivation_bridge_ko
  - plan_2026_06_18_candidate_equation_proposal_template
next_gate: use this as method-retrospective guardrail before any future candidate fit
date: 2026-06-18
context: retained Gamma(a)를 학계 IV/IDE formalism으로 번역한 뒤, brute-force trend fitting에 가까웠던 연구 방법을 회고
audience: 주니어 개발자
length: 작업 단계별 풀어쓰기
created_at: 2026-06-18
created_by: dorito
updated_at: 2026-06-18
updated_by: dorito
last_updated: 2026-06-18
last_verified_at: 2026-06-18
last_verified_by: dorito
audit_log:
  - action: created
    at: 2026-06-18
    by: dorito
    note: "Created after 055 academic derivation bridge clarified that retained Gamma(a) is a phenomenological IV/IDE comparator, not physical QFUDS."
tags: [postmortem, retrospective, gamma, brute-force, methodology, qfuds]
relations:
  - docs/05_next_steps/000_roadmap.md
  - docs/04_results/010_result_001_gamma_scan.md
  - docs/04_results/015_result_001_5_phase_transfer_physicality.md
  - docs/04_results/030_result_004_p1_model_family_positioning.md
  - docs/04_results/030_result_005_timing_prior_usefulness.md
  - docs/04_results/030_result_006_literature_timing_support_audit.md
  - docs/wiki/research/investigations/source_x/conclusions/055_academic_derivation_bridge_ko.md
  - docs/wiki/research/investigations/baseline_reference/plans/010_candidate_equation_proposal_template.md
code_refs:
  - file: docs/04_results/010_result_001_gamma_scan.md
    note: "Records the original Gamma-law scan and the early lesson that free Gamma(a) reduces to interacting dark energy."
  - file: docs/04_results/030_result_004_p1_model_family_positioning.md
    note: "Classifies retained P1 as an exact interacting-vacuum instance and time-dependent IDE subset."
  - file: docs/wiki/research/investigations/source_x/conclusions/055_academic_derivation_bridge_ko.md
    note: "Translates retained Gamma(a) into the academic IV/IDE source-term chain."
  - file: docs/wiki/research/investigations/baseline_reference/plans/010_candidate_equation_proposal_template.md
    note: "Defines the future guardrail: fill source, stress tensor, transfer law, perturbations, and known-model escape before fitting."
---

# brute-force Gamma 접근 회고

## 사건 한 줄 요약

retained `Gamma(a)` 접근은 처음부터 엄밀한 물리 유도라기보다 경향성을 보고
맞는 모양을 찾아가는 brute-force 탐색에 가까웠다. 탐색 자체는 쓸모가
있었지만, 그 결과를 물리 source처럼 읽기 시작한 순간부터 순서가 뒤집혔다.

이 문서의 목적은 자책이 아니다.

```text
무엇을 놓쳤는지,
어떤 순서로 했으면 덜 순환적이었는지,
다음 speculative idea를 어떻게 다뤄야 하는지
```

를 기록하는 것이다.

## 0. 사전 지식

| 용어 | 이 회고에서의 의미 |
| --- | --- |
| brute-force scan | 여러 `Gamma(a)` 모양과 파라미터를 돌려 background/growth 경향을 보는 탐색 |
| trend fitting | 관측 또는 원하는 현상과 닮은 경향을 찾고 그 뒤에 해석을 붙이는 접근 |
| derivation | source variable, stress tensor, pressure, transfer law, perturbation response가 한 mechanism에서 나오는 것 |
| null model | 비교 기준. 여기서는 LCDM, interacting vacuum, IDE, effective `w(a)`, unified dark fluid 같은 알려진 모델 |
| holdout constraint | fit에 쓰지 않고 마지막에만 확인하는 관측 문턱 |
| candidate equation template | future branch가 관측값을 보기 전에 `X`, `T_mu_nu`, `Q^nu`, `delta Q`, known-model escape를 채우게 하는 양식 |

핵심 구분:

```text
brute force = exploratory tool로는 가능
brute force + 사후 물리 해석 = circularity risk
```

## 1. 증상

초기 접근은 대략 이렇게 흘렀다.

```text
직관: black-hole information / quantum foam / dark sector가 연결될 수 있나?
-> 구현: phase A와 phase B를 두고 Gamma(a)로 에너지 전달을 넣음
-> 탐색: 여러 Gamma law를 스캔해 배경과 성장 경향을 확인
-> retained shape: 구조 형성기 근처 z ~= 2 peak가 남음
-> 해석 시도: 이 timing이 foam, entropy, black-hole information에서 왔는지 찾음
```

이 흐름에서 가장 약한 고리는 마지막이다.

```text
맞아 보이는 Gamma(a)를 먼저 얻고,
그 뒤에 source story를 찾아 붙였다.
```

이것은 과학적으로 바로 금지되는 것은 아니다. Exploratory data analysis로
라벨링하면 쓸 수 있다. 문제는 그 다음이다.

```text
탐색 결과를 derivation처럼 말하면 안 된다.
```

## 2. 첫 의문 + 가설

| 가설 | 왜 그럴 수 있는지 | 어떻게 확인할지 |
| --- | --- | --- |
| H1. 놓친 핵심은 물리 지식 부족보다 순서 문제다 | background scan을 먼저 하고 source equation을 나중에 찾았다 | result 001, 001.5, 004, 055의 결론을 대조한다 |
| H2. retained `Gamma(a)`는 완전히 쓸모없지는 않다 | IV/IDE comparator와 timing fingerprint로는 기능한다 | result 004-006과 055 bridge를 확인한다 |
| H3. physical QFUDS로는 현재 막힌다 | `X`, `Q^nu`, phase-B pressure, `delta Q`, known-model distinction이 없다 | candidate equation template와 roadmap blocker를 확인한다 |
| H4. 다음번에는 brute force 자체를 금지할 필요는 없다 | brute force는 가설 생성에는 유용하다 | 단, preregistration, null model, holdout constraint를 먼저 둔다 |

## 3. 진단: 실제 상태 확인

### 3.1 `Gamma(a)` scan은 탐색으로는 유효했다

[Result 001](../../04_results/010_result_001_gamma_scan.md)은 여러 transfer law를
돌려 다음을 확인했다.

- `Gamma(a)=0`은 LCDM null limit다.
- free 또는 early-active transfer는 쉽게 known IDE behavior 또는 background
  failure로 간다.
- low-redshift gated shape가 상대적으로 안전하다.

이 단계는 나쁘지 않았다. 문제는 이 결과가 말할 수 있는 범위다.

```text
말할 수 있는 것:
이런 timing shape가 background/growth proxy에서 덜 깨진다.

말할 수 없는 것:
이 timing shape가 quantum foam이나 black-hole information에서 유도된다.
```

### 3.2 physicality audit에서 바로 막혔다

[Result 001.5](../../04_results/015_result_001_5_phase_transfer_physicality.md)는
retained branch가 physical Level 1.5 promotion을 통과하지 못했다고 기록한다.

막힌 항목은 단순했다.

```text
source variable X 없음
physical threshold 없음
conversion efficiency 없음
stress-energy accounting 없음
phase-B vacuum pressure rationale 없음
```

즉 `Gamma(a)`는 curve로는 있었지만 source로는 없었다.

### 3.3 retained P1은 학계 모델 안으로 들어갔다

[Result 004](../../04_results/030_result_004_p1_model_family_positioning.md)는
retained P1을 다음처럼 분류했다.

```text
exact interacting-vacuum instance
generic time-dependent IDE subset under xi(a) = Gamma(a)
```

이건 실패만은 아니다. 내 직관이 완전히 엉뚱한 계산이 아니라, 실제 학계의
interacting dark sector 언어에 들어갈 수 있다는 뜻이다.

하지만 동시에 novelty는 사라진다.

```text
새 이론이 아니라 알려진 formalism의 한 parameterization으로 읽힌다.
```

### 3.4 055 bridge가 최종 번역을 했다

[Academic Derivation Bridge](../research/investigations/source_x/conclusions/055_academic_derivation_bridge_ko.md)는
retained `Gamma(a)`를 이렇게 번역한다.

```text
Gamma(a) intuition
-> Q = H Gamma(a) rho_A
-> Q^mu, transfer frame, delta Q, pressure closure가 필요
```

즉 실제 학계 논문은 "Gamma가 예쁘다"에서 시작하지 않는다. 보통은 다음
순서가 먼저다.

```text
stress-energy conservation
-> Q^mu definition
-> frame choice
-> perturbation closure
-> stability
-> likelihood constraint
```

QFUDS는 이 중 일부를 사후에 맞췄고, first-principles source는 아직 없다.

## 4. 무엇을 놓쳤나

| 놓친 것 | 실제로 한 일 | 왜 문제였나 | 어떻게 했어야 했나 |
| --- | --- | --- | --- |
| motivation과 mechanism 분리 | black-hole/foam/information story에서 `Gamma(a)` 의미를 찾음 | 좋은 출발 질문이 source equation으로 승격될 위험이 있었다 | origin story는 lineage/provenance에 두고, mechanism은 별도 candidate equation으로만 인정 |
| source variable 선등록 | `Gamma(a)` shape를 먼저 얻고 `X`를 나중에 찾음 | 사후 source 찾기는 순환논리로 흐른다 | `X`, units, domain, equation을 관측 비교 전에 고정 |
| known-model null 우선순위 | QFUDS 이름으로 먼저 스캔 | 나중에 IV/IDE와 동치임을 확인했다 | LCDM, IV/IDE, effective `w(a)`, unified fluid를 먼저 null model로 둠 |
| phase-B pressure | `rho_B` 증가와 dark energy behavior를 같이 상상 | `rho_B`가 는다고 `p_B ~= -rho_B`가 유도되지는 않는다 | `p_B`, `T_B^{mu nu}`, equation of state를 먼저 요구 |
| covariant transfer | background `Q`만으로 충분해 보였음 | perturbation/CMB/LSS에서는 `Q^mu`, frame, `delta Q`가 필요하다 | background scan 전에 최소 transfer-frame 후보를 선언 |
| held-out constraint | 맞는 경향을 본 뒤 해석을 붙임 | 같은 관측에서 parameter와 해석을 동시에 고르면 과적합이다 | fit/selection용 constraint와 kill/holdout constraint를 분리 |
| amplitude/width/redshift freeze | `Gamma(a)` 모양을 보며 좋은 timing을 찾음 | peak, width, amplitude가 관측에서 역추론되면 source가 아니다 | parameter를 preregister하거나 fit status를 명시 |
| novelty check | 나중에 known-model distinction을 했다 | 이미 알려진 모델을 새 이름으로 부를 수 있다 | 모델 작성 직후 first known-model sink부터 표시 |
| data-product boundary | literature overlap을 support처럼 느끼기 쉬웠음 | table-level overlap은 physical support가 아니다 | source-state token과 product level을 먼저 기록 |
| language boundary | "survived"가 물리 survival처럼 들릴 수 있음 | Level 2A phenomenology survival이 physical QFUDS survival로 오해된다 | survived 뒤에 항상 scope를 붙임 |

## 5. 어떻게 했으면 좋았나

이상적인 순서는 이랬어야 한다.

### 5.1 먼저 질문을 세 갈래로 나눴어야 한다

```text
1. public origin question:
   왜 이 생각이 나왔는가?

2. phenomenological comparator:
   어떤 effective Gamma(a)가 IV/IDE에서 비교 가능한가?

3. physical candidate:
   어떤 source X가 T_mu_nu, Q^nu, pressure, delta Q를 만든다고 주장하는가?
```

초기에는 이 세 갈래가 섞였다. 그래서 동기, fitting, derivation이 서로
강도를 빌려 갔다.

### 5.2 그 다음 known-model sink를 먼저 열었어야 한다

QFUDS를 쓰기 전에 먼저 물었어야 하는 질문:

```text
이건 그냥 LCDM인가?
이건 그냥 IV/IDE인가?
이건 effective w(a)인가?
이건 unified dark fluid인가?
이건 running vacuum/HDE인가?
이건 backreaction/MG인가?
```

이 과정을 먼저 했으면 retained P1이 IV/IDE에 들어간다는 사실을 더 빨리
알았을 것이다.

### 5.3 candidate equation template가 먼저였어야 한다

다음 빈칸을 먼저 채우지 못하면, 관측 비교로 가면 안 됐다.

```text
X =
rho_A[X] =
rho_B[X] =
p_A[X] =
p_B[X] =
T_A^{mu nu}[X] =
T_B^{mu nu}[X] =
Q^nu[X,...] =
delta Q^nu[X,...] =
known_model_sink =
escape_equation =
kill_condition =
```

이 템플릿 없이 `Gamma(a)`를 먼저 맞추면, 나중에 source story를 끼워 넣기
쉬워진다.

### 5.4 brute force는 "탐색"으로만 허용했어야 한다

brute force 자체는 금지할 필요가 없다. 하지만 label이 중요했다.

```text
allowed:
exploratory scan found a shape worth comparing.

forbidden:
scan found a shape, therefore source is plausible.
```

앞으로 brute force를 쓰려면 최소 조건은 다음이다.

1. target observable을 보기 전에 parameter family를 적는다.
2. amplitude, width, peak redshift가 fitted인지 preregistered인지 표시한다.
3. fitting에 쓴 관측과 kill condition에 쓸 관측을 분리한다.
4. null models와 같은 데이터에서 비교한다.
5. 결과는 `hypothesis_generator`로만 승격한다.

### 5.5 학계 경로를 먼저 따라갔어야 한다

retained `Gamma(a)`가 궁금했다면, 가장 빠른 학습 경로는 QFUDS를 더 미는
것이 아니라 IV/IDE 논문의 표준 chain을 따라가는 것이었다.

```text
Q
-> Q^mu
-> transfer frame
-> perturbation equations
-> stability conditions
-> Boltzmann implementation
-> likelihood constraints
```

이 경로를 먼저 따라가면, QFUDS가 어느 빈칸에서 멈추는지 더 빨리 보인다.

## 6. 그래도 뻘짓이 아니었던 부분

이 접근이 전부 무의미했던 것은 아니다.

| 남은 가치 | 이유 |
| --- | --- |
| `Gamma(a)`가 IV/IDE entry point를 찾게 했다 | naive transfer intuition이 학계 formalism의 `Q` 언어로 번역됐다 |
| negative result가 빠르게 쌓였다 | constant/ungated laws, broad entropy source, P2 fluid closure가 탈락했다 |
| `z ~= 2` timing question이 분리됐다 | source는 죽었지만 timing fingerprint는 comparator로 남았다 |
| audit harness가 굳어졌다 | workflow, cache, guard, hostile review가 overclaim을 줄였다 |
| future guardrail이 생겼다 | candidate equation template와 non-circularity rule이 생겼다 |

즉 결과는:

```text
QFUDS physical derivation = no
methodological learning = yes
IV/IDE learning bridge = yes
```

## 7. 결론 / 해결

이번 회고의 결론은 보수적이다.

```text
내가 놓친 것은 "정답 논문" 하나가 아니라,
학계가 모델을 세우는 순서였다.
```

내 접근은:

```text
직관 -> Gamma scan -> 맞는 경향 -> source story 찾기
```

에 가까웠다.

더 나은 순서는:

```text
문헌/model taxonomy
-> known-model nulls
-> candidate equation
-> preregistered parameters
-> exploratory scan
-> holdout kill-map
-> IV/IDE or physical-QFUDS classification
```

이었다.

## 8. 재발 방지 / 운영 메모

다음 speculative branch에는 이 규칙을 적용한다.

1. Fit을 하기 전에 `candidate equation template`를 채운다.
2. 빈칸이 있으면 `physical candidate`가 아니라 `exploratory prompt`로 둔다.
3. Brute-force scan 결과에는 `hypothesis_generator` 라벨을 붙인다.
4. Observational threshold는 source parameter를 고른 뒤에만 사용한다.
5. `Gamma(a)`와 같은 effective curve는 source가 아니라 comparator로 시작한다.
6. `supports QFUDS`라는 문장을 쓰기 전에 known-model sink를 먼저 적는다.
7. 새 문헌을 쓰면 Research Asset and Product Workflow state token을 기록한다.

## 9. 타임라인

- 2026-06-08: `Gamma(a)` background scan과 entropy/information source trial이 시작됐다.
- 2026-06-09: retained branch가 physical Level 1.5 promotion에 실패하고 IV/IDE phenomenology로 강등됐다.
- 2026-06-13: P1/P2 perturbation closure와 model-family positioning이 정리됐다.
- 2026-06-18: candidate equation template, five-route template attempts, 055 academic derivation bridge가 만들어졌다.
- 2026-06-18: 이 회고에서 brute-force trend fitting과 physical derivation의 경계를 명시했다.

## 부록 A — 다음번에 먼저 물을 질문

1. 지금 하는 말은 origin story인가, phenomenological comparator인가, physical
   candidate인가?
2. `X`는 무엇이고 units는 무엇인가?
3. `X`가 `rho`, `p`, `T_mu_nu`를 만드는 식이 있는가?
4. `Q^nu`는 어느 frame에 평행한가?
5. `delta Q`는 같은 source에서 나오는가?
6. phase B의 `w ~= -1`은 유도인가, 삽입인가?
7. 가장 가까운 known-model sink는 무엇인가?
8. 어떤 observation을 보고 parameter를 골랐는가?
9. 어떤 observation은 holdout kill condition으로 남겨뒀는가?
10. 이 결과를 "탐색" 이상으로 승격할 근거가 있는가?

## Workflow Boundary

This postmortem follows the
[Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md)
only to preserve source-state boundaries.

No new external source, PDF, table, product, cache, digitization, or
availability claim is introduced here. Literature and product states are
inherited from the owning records, including `literature_record_cached`,
`asset_available_not_downloaded`, `asset_cached`,
`asset_extracted_not_digitized`, `manual_structured_extract`, and
`direct_table`.

This postmortem is not QFUDS support, validation, novelty, roadmap advancement,
Physical-QFUDS Level 2B admission, or Level 4 CMB work.
