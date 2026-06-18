---
doc_id: audit_2026_06_18_academic_derivation_bridge_ko
title: "2026-06-18 Academic Derivation Bridge"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - result_004_p1_model_family_positioning
  - result_005_timing_prior_usefulness
  - result_006_literature_timing_support_audit
  - qfuds_phenomenological_perturbations
  - qfuds_qnu_necessity_formulation_audit
  - audit_2026_06_18_candidate_equation_template_attempts_ko
  - roadmap
next_gate: learn IV/IDE formalism from the Gamma bridge; do not reopen Level 2B
last_updated: 2026-06-18
---

# 2026-06-18 Academic Derivation Bridge

## Purpose

이 문서는 QFUDS를 독립 이론으로 보존하려는 문서가 아니다.

목적은 더 좁다.

```text
내가 직관적으로 만든 Gamma(a)가 학계의 interacting vacuum /
interacting dark energy formalism에서 어디에 해당하는지 번역한다.
```

현재 결론은 그대로 유지한다.

- retained `Gamma(a)`는 물리 QFUDS가 아니다.
- retained `Gamma(a)`는 phenomenological IV/IDE comparator다.
- `Gamma(a)`는 아직 `Q^nu`, pressure, perturbations, novelty를
  first-principles에서 유도하지 못했다.
- 이 문서는 Level 2B를 열지 않는다.

## Workflow Boundary

This bridge follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md)
only to preserve source-state boundaries.

No new external paper, PDF, table, figure, posterior product, cache, or
digitization claim is introduced here. Source states are inherited from the
owning records:

- retained P1 positioning and perturbation records: repository result records;
- Escamilla 2023 IV/IDE kernel record: `literature_record_cached`, with raw
  assets `asset_available_not_downloaded`;
- Martinelli 2019 interacting-vacuum record: `literature_record_cached`, with
  raw assets `asset_available_not_downloaded`;
- Exp006 inspected table products: table-level products only, no posterior
  product promotion.

NASA/LAMBDA, BAO, CMB, LSS, and survey products are not used here to choose
`Gamma(a)`, amplitude, transition redshift, transition width, or source scale.

## Short Answer

이 작업은 Phase 4가 아니다.

Roadmap에서 Level 4는 CMB comparison이며, CLASS/CAMB 구현 이후에나 의미가
있다. 이 문서는 observer mode 안의 reference/audit bridge다. 즉:

```text
QFUDS Gamma intuition -> academic IV/IDE source-term language
```

로 번역하는 문서일 뿐이다.

## Where Gamma(a) Stopped

QFUDS의 현재 two-phase background는 다음 모양에서 멈췄다.

```math
{d\rho_A\over d\ln a}+3\rho_A=-\Gamma(a)\rho_A,
```

```math
{d\rho_B\over d\ln a}=\Gamma(a)\rho_A.
```

여기까지는 직관적으로 말하면:

```text
phase A가 줄고, phase B가 늘어나는 시간 프로파일을 Gamma(a)로 둔다.
```

학계 언어로 쓰면 이것은 바로 background-level energy transfer다.

```math
Q = H\Gamma(a)\rho_A
```

또는 conformal-time convention에서는:

```math
Q = {\mathcal H}\Gamma(a)\rho_A.
```

따라서 retained `Gamma(a)`의 현 위치는:

```text
physical source = no
phenomenological interaction history = yes
```

이다.

## Academic Starting Point

실제 IV/IDE 논문은 보통 `Gamma(a)`라는 이름에서 시작하지 않는다. 먼저
stress-energy bookkeeping에서 시작한다.

총 dark-sector stress tensor는 보존되어야 한다.

```math
\nabla_\mu T_{\rm dark}^{\mu\nu}=0.
```

dark sector를 두 성분으로 쪼개면:

```math
T_{\rm dark}^{\mu\nu}=T_A^{\mu\nu}+T_B^{\mu\nu}.
```

두 성분 사이에 에너지-운동량이 이동한다면 표준적인 표현은:

```math
\nabla_\mu T_A^{\mu\nu}=-Q^\nu,
\qquad
\nabla_\mu T_B^{\mu\nu}=+Q^\nu.
```

여기서 학계가 묻는 질문은 `Gamma(a)`가 예쁜가가 아니다.

```text
Q^nu가 무엇인가?
어느 frame에 평행한가?
background Q는 무엇인가?
perturbation delta Q는 어떻게 정해지는가?
dark-energy pressure와 sound speed는 무엇인가?
```

이다.

## Translation Table

| QFUDS intuition | Academic IV/IDE object | Current status |
| --- | --- | --- |
| phase A | CDM-like interacting component | implemented as pressureless effective component |
| phase B | vacuum-like or DE-like interacting component | P1 only as interacting vacuum; P2 near-vacuum fluid failed retained amplitude |
| `Gamma(a)` | dimensionless time-dependent interaction history | phenomenological comparator |
| `Q = H Gamma rho_A` | background transfer scalar | writable, not derived |
| retained peak near `z ~= 2` | timing fingerprint for IV/IDE coupling support | allowed but not informative at table level |
| `Q_A^mu = -Q u_A^mu` | phase-A-frame transfer choice | Level 2A closure only |
| `deltaQ = Q delta_A` | perturbation closure ansatz | gauge-fixed phenomenological choice |
| black-hole / foam / information language | possible motivation or provenance | not a source derivation |

## What Standard Formalism Requires

### 1. A source term

The first academic object is not a story. It is a source term:

```math
Q^\nu.
```

At background level, one projection becomes the scalar `Q`. But a background
scalar is not enough for perturbations or CMB/LSS work.

### 2. A transfer frame

One must choose whether the transfer is parallel to:

- the dark-matter four-velocity;
- the dark-energy four-velocity;
- the total dark-sector four-velocity;
- another covariantly defined vector.

The current QFUDS P1 closure chose the phase-A frame:

```math
Q_A^\mu=-Q u_A^\mu,
\qquad
Q_B^\mu=+Q u_A^\mu.
```

That made a Level 2A audit possible. It did not make the choice physical.

### 3. A pressure prescription

For phase B, the model must decide whether it is:

- exact interacting vacuum;
- near-vacuum fluid;
- scalar-field dark energy;
- unified fluid;
- modified-gravity effective component.

QFUDS currently keeps only the first option as a stable phenomenological
closure. The regularized fluid option was tested and failed at the retained
amplitude.

### 4. Perturbations

The formalism must specify:

```text
gauge
transfer frame
delta Q
delta Gamma or no delta Gamma
pressure perturbation
sound speed
anisotropic stress
initial conditions
stability criteria
```

The QFUDS Level 2A closure supplied these as a declared ansatz. It did not
derive them from foam, black holes, information, or a field action.

### 5. Known-model comparison

After all of the above, the model must still answer:

```text
Is this merely LCDM with Gamma = 0?
Is this ordinary interacting vacuum?
Is this ordinary time-dependent IDE?
Is this a unified dark fluid or scalar-field model in disguise?
```

For the retained P1 branch, the answer is already known:

```text
P1 is an exact interacting-vacuum instance with xi(a) = Gamma(a).
```

That is useful for learning and comparison. It is not novelty.

## Where Real Papers Begin

The practical academic entry point is therefore:

1. Choose an interaction convention, for example `Q = H xi(a) rho_c`,
   `Q = H xi(a) rho_de`, or a reconstructed kernel.
2. Specify the covariant transfer vector `Q^mu`.
3. Specify the momentum-transfer frame.
4. Specify the perturbation closure.
5. Run stability checks.
6. Implement or map into a Boltzmann solver.
7. Compare to CMB, BAO, SN, RSD, weak lensing, or combined likelihoods.
8. Interpret the result as a constraint on the interaction model, not as proof
   of a microscopic origin.

QFUDS reached only a subset of steps 1, 4, and 5:

- step 1: `Q = H Gamma(a) rho_A` was writable;
- step 4: P1 supplied a declared Level 2A closure;
- step 5: P1 survived the local stability audit, while P2 failed.

It did not reach:

- a derived `Q^nu`;
- a physical phase-B pressure derivation;
- a source-side `delta Q`;
- Boltzmann-code viability;
- likelihood comparison;
- novelty.

## Honest Boundary

The honest interpretation is:

```text
QFUDS did not derive a new dark-sector theory.
QFUDS rediscovered the entrance to interacting dark-sector modeling through a
specific phenomenological Gamma(a) intuition.
```

That is still useful, because it tells the next learning path:

```text
Study IV/IDE by asking how Q, Q^mu, frame choice, perturbation stability, and
observational constraints are normally built.
```

But it also kills the stronger claim:

```text
Gamma(a) is not a foam source unless a source equation derives it.
```

## Missing Items

| Missing item | Why it matters | Current status |
| --- | --- | --- |
| `X` | source variable that produces the interaction | missing |
| `Q^nu[X,...]` | covariant transfer law | missing |
| phase-B pressure derivation | reason B behaves like `w ~= -1` | missing |
| `delta Q` from same source | perturbation-level source response | missing |
| transfer frame from physics | prevents arbitrary closure choice | missing |
| known-model escape equation | separates from IV/IDE, UDF, scalar-field, MG | missing |
| likelihood comparison | asks whether data prefer this shape | not run |

## Decision

Classify `055` as:

```text
academic_derivation_bridge = yes
physical_QFUDS_derivation = no
Level_2B = closed
roadmap_level_4 = no
retained_Gamma_role = phenomenological_IV_IDE_comparator
```

## Next Executable Instruction

Do not try to rescue QFUDS as an independent physical branch from retained
`Gamma(a)`.

Use this bridge as the reading and derivation path into academic IV/IDE:
reconstruct the standard chain from `Q` to `Q^mu`, transfer frame,
perturbation closure, stability, Boltzmann implementation, and likelihood
constraints. Only after that chain is understood should a future candidate ask
whether QFUDS can supply a first-principles `X` and `Q^nu` that the standard
formalism does not already absorb.
