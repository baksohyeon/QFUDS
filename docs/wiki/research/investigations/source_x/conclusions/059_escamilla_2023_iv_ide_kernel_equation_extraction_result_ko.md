---
doc_id: audit_2026_06_18_escamilla_2023_iv_ide_kernel_equation_extraction_result_ko
title: "2026-06-18 Escamilla 2023 IV/IDE Kernel Equation Extraction Result"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - plan_2026_06_18_paper_by_paper_iv_ide_equation_extraction_ko
  - audit_2026_06_18_li_2025_iv_ide_equation_extraction_result_ko
  - asset_escamilla_2023_interacting_dark_energy_kernel
  - asset_escamilla_2023_interacting_dark_energy_kernel_equation_extract_20260618
  - lit_escamilla_2023_interacting_dark_energy_kernel
  - roadmap
next_gate: compare Li 2025 and Escamilla 2023 conventions before caching the next IV/IDE formalism target
last_updated: 2026-06-18
---

# 2026-06-18 Escamilla 2023 IV/IDE Kernel Equation Extraction Result

## Purpose

이 문서는 [058 paper-by-paper IV/IDE extraction plan](../plans/058_paper_by_paper_iv_ide_equation_extraction_plan_ko.md)의
두 번째 실행 결과다.

대상은 Escamilla et al. 2023 interacting dark energy kernel paper다. 목적은
retained `Gamma(a)`를 맞추는 것이 아니라, 실제 IV/IDE 문헌이 background
interaction kernel을 어떤 부호, 정규화, 시간 변수, perturbation 경계로
다루는지 Li 2025와 비교 가능한 형태로 고정하는 것이다.

## Workflow Boundary

This result follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).

No new external source, posterior product, covariance product, chain, numerical
`Pi_DE(z)` product, or product-absence claim is introduced here. The extraction
uses the already cached Escamilla 2023 arXiv source:

```text
docs/wiki/research/assets/escamilla_2023_interacting_dark_energy_kernel/source/extracted/main.tex
```

A manual structured extract was added at:

```text
docs/wiki/research/assets/escamilla_2023_interacting_dark_energy_kernel/digitization/equation_extraction_20260618.md
```

Workflow states:

```text
asset_cached
asset_extracted_not_digitized
source_text_parse
manual_structured_extract
```

This is not numerical digitization and not QFUDS evidence.

## Short Result

Escamilla 2023 passes the source-cache and background-kernel extraction step,
but stops at:

```text
stop_status = background_only_stop
```

Reason: the cached source gives a background `Q`, `Pi_DE`, `Pi_DM`, `I_Q`, sign
convention, and reconstruction-node convention. It explicitly leaves full
perturbation analysis to future work and does not define a covariant `Q^mu`,
momentum-transfer frame, `delta Q`, or perturbation closure.

## Structured Extraction Row

| Field | Extracted value |
| --- | --- |
| `paper_id` | `lit_escamilla_2023_interacting_dark_energy_kernel` |
| `record_path` | [Escamilla 2023 literature record](../../../literature/escamilla_2023_interacting_dark_energy_kernel.md) |
| `source_state` | `asset_cached`; source TeX extracted; `manual_structured_extract` added |
| `equation_status` | `exact_in_cached_record` for background equations, `Pi_DE`, `Pi_DM`, `I_Q`, and reconstruction nodes |
| `model_class` | interacting dark energy / dark matter background reconstruction |
| `background_Q` | `dot rho_DM + 3H rho_DM = Q`; `dot rho_DE + 3H rho_DE(1+w_DE) = -Q` |
| `time_derivative_variable` | cosmic time for dot equations; redshift after chain-rule rewrite |
| `hubble_factor_in_Q` | `H` in `Pi` and `I_Q` normalizations |
| `sign_convention_raw` | `Q>0` is DE-to-DM; `Q<0` is DM-to-DE |
| `positive_coupling_direction` | DE-to-DM in this paper convention |
| `density_factor` | present critical density `rho_c,0` in `Pi_DE = Q/(3H rho_c,0)` |
| `coupling_variable` | `Pi_DE(z)`, `Pi_DM(z)`, and visualization function `I_Q(z)` |
| `coupling_dimension` | dimensionless |
| `time_dependence` | five amplitudes across `0 <= z <= 3`; GP nodes `[0.0, 0.75, 1.5, 2.25, 3.0]`; binned smoothness `xi = 0.15` |
| `Q_mu_defined` | no |
| `momentum_transfer_frame` | not defined |
| `gauge` | not defined |
| `delta_Q` | not defined |
| `delta_coupling` | not defined |
| `pressure_perturbation` | not defined; perturbation analysis deferred |
| `sound_speed` | not extracted as a standalone field |
| `anisotropic_stress` | not extracted as a standalone field |
| `stability_rule` | background prior guidance only; no perturbation closure |
| `solver_route` | modified SimpleMC with dynesty nested sampling for expansion/distance background inference |
| `posterior_covariance_PCA_products` | not re-audited here; no new product-absence claim |
| `retained_Gamma_mapping` | comparator only; no direct equivalence |
| `translation_hazards` | opposite sign direction relative to Li 2025, critical-density normalization, background-only status, reconstruction-node tuning risk |
| `stop_status` | `background_only_stop` |

## Translation Boundary

The repo-local retained convention is:

```math
Q = \mathcal{H}\Gamma(a)\rho_A.
```

Escamilla 2023 gives:

```math
\Pi_{\rm DE} = \frac{Q}{3H\rho_{c,0}},
\qquad
I_Q(z)=\frac{Q(z)}{\rho_{c,0}H(z)(1+z)^3}.
```

Therefore a valid translation would need:

```text
critical-density normalization conversion
H vs conformal-Hubble convention conversion
sign convention mapping
redshift-node/bin mapping
explicit decision that reconstruction nodes are not QFUDS physical scales
```

The paper's `xi = 0.15` is an interpolation smoothness parameter in redshift,
not the QFUDS `xi_gal` scale. Reusing it as a physical transition width would
be circular.

## What This Teaches

Escamilla 2023 is useful precisely because it shows a boundary case: real
academic work can reconstruct a model-independent background interaction
kernel while still stopping before perturbation-level closure.

That is close to where retained `Gamma(a)` currently lives. It can be compared
as a phenomenological timing/background shape, but it still lacks the objects
that Li 2025 supplies for model evolution: `Q^mu`, frame choice, perturbation
route, and solver-readiness.

## Decision

| Question | Decision |
| --- | --- |
| Can Escamilla 2023 be used as an IV/IDE background-kernel teaching target? | Yes. |
| Can `Pi_DE(z)` be treated as direct QFUDS evidence? | No. |
| Can retained `Gamma(a)` be translated directly into `Pi_DE(z)`? | No; sign, density, Hubble, and redshift-node conventions differ. |
| Does this open QFUDS Level 2B? | No. |
| Does this allow NASA/BAO/CMB/LSS model comparison now? | No. |
| What is the next safe step? | Compare Li 2025 and Escamilla 2023 conventions as formalism examples before caching the next IV/IDE target. |

## Next Executable Instruction

Create a short convention-comparison note for Li 2025 versus Escamilla 2023.
The note should compare background `Q`, sign direction, density factor, Hubble
factor, time variable, `Q^mu`/frame availability, perturbation route, and stop
status. Do not fit retained `Gamma(a)`, do not use NASA/BAO/CMB/LSS as model
evidence, and do not treat either paper as QFUDS physical admission.
