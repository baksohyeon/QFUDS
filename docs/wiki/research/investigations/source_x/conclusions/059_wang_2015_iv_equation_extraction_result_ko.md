---
doc_id: audit_2026_06_18_wang_2015_iv_equation_extraction_result_ko
title: "2026-06-18 Wang 2015 IV Equation Extraction Result"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - plan_2026_06_18_paper_by_paper_iv_ide_equation_extraction_ko
  - audit_2026_06_18_martinelli_hogg_iv_geodesic_cdm_same_family_comparison_note_ko
  - asset_wang_2015_dark_matter_vacuum_interaction
  - asset_wang_2015_dark_matter_vacuum_interaction_equation_extract_20260618
  - lit_wang_2015_dark_matter_vacuum_interaction
  - roadmap
next_gate: compare Wang 2015 against the Martinelli/Hogg geodesic-CDM family before any retained timing fit
last_updated: 2026-06-18
---

# 2026-06-18 Wang 2015 IV Equation Extraction Result

## Purpose

이 문서는 [058 paper-by-paper IV/IDE extraction plan](../plans/058_paper_by_paper_iv_ide_equation_extraction_plan_ko.md)의
다섯 번째 Tier 1 실행 결과다.

대상은 Wang et al. 2015 dark matter-vacuum interaction paper다. 목적은
retained `Gamma(a)`를 맞추는 것이 아니라, `alpha(a)` reconstruction이
어떤 `Q`, `Q^mu`, perturbation equation, RSD observable, prior/PCA, and
Bayesian evidence boundary를 요구하는지 확인하는 것이다.

## Workflow Boundary

This result follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).

No new external source, posterior product, covariance product, chain, numerical
`alpha(a)` product, or product-absence claim is introduced here. The extraction
uses the already cached Wang 2015 arXiv source:

```text
docs/wiki/research/assets/wang_2015_dark_matter_vacuum_interaction/source/extracted/Recon_Inter-resubmit_2.tex
```

A manual structured extract was added at:

```text
docs/wiki/research/assets/wang_2015_dark_matter_vacuum_interaction/digitization/equation_extraction_20260618.md
```

Workflow states:

```text
asset_cached
asset_extracted_not_digitized
source_text_parse
manual_structured_extract
```

This is not PDF parsing, numerical digitization, or QFUDS evidence.

## Short Result

Wang 2015 passes the equation extraction gate as:

```text
stop_status = continue_to_perturbation_extract
```

Reason: the cached source gives background `Q`, covariant `Q^mu`, the DM-frame
geodesic condition, homogeneous-vacuum frame, perturbation equation, modified
RSD observable, 40-bin CPZ-prior reconstruction, PCA prior/data separation,
Bayesian evidence boundary, and modified CosmoMC route.

It does not provide:

```text
QFUDS physical source X
QFUDS-derived Q^mu[X, ...]
phase-B pressure derivation from a foam sector
retained Gamma(a) equivalence
machine-readable alpha(a) posterior history
```

## Structured Extraction Row

| Field | Extracted value |
| --- | --- |
| `paper_id` | `lit_wang_2015_dark_matter_vacuum_interaction` |
| `record_path` | [Wang 2015 literature record](../../../literature/wang_2015_dark_sector_interaction_reconstruction.md) |
| `source_state` | `asset_cached`; source TeX extracted; `manual_structured_extract` added |
| `equation_status` | `exact_in_cached_record` for background `Q`, `Q^mu`, frame, perturbation equation, RSD observable, prior/PCA/evidence, and solver route |
| `model_class` | interacting vacuum / dark matter-vacuum energy interaction |
| `background_Q_raw` | `dot rho_dm + 3H rho_dm = -Q`; `dot V = Q` |
| `background_Q_parameterized` | `Q = 3 alpha H rho_dm V / (rho_dm + V)` |
| `time_derivative_variable` | cosmic time for dot equations; scale factor for `alpha(a)` reconstruction |
| `hubble_factor_in_Q` | physical `H` |
| `sign_convention_raw` | raw `Q>0` means DM-to-vacuum transfer |
| `positive_coupling_direction` | positive `alpha` transfers DM energy into vacuum |
| `negative_coupling_direction` | negative `alpha` corresponds to vacuum decay |
| `density_factor` | nonlinear product/ratio `rho_dm V / (rho_dm + V)` |
| `coupling_variable` | `alpha(a)` / binned `alpha_i` |
| `coupling_dimension` | dimensionless |
| `time_dependence` | 40 scale-factor bins over `[0.001, 1]` |
| `Q_mu_defined` | yes |
| `Q_mu_direction` | parallel to DM four-velocity |
| `momentum_transfer_frame` | DM comoving-orthogonal frame; no momentum transfer in that frame |
| `gauge` | comoving-synchronous gauge for the stated perturbation equation |
| `delta_Q` | not extracted as independent perturbation; background-bin `Q(a_i)` enters the `delta_dm` equation |
| `delta_coupling` | no independent `delta alpha` extracted |
| `pressure_perturbation` | vacuum can be homogeneous in the selected frame: `delta V = 0` |
| `sound_speed` | perturbations described as restricted form with vanishing sound speed |
| `anisotropic_stress` | not extracted as a standalone field |
| `initial_conditions` | not extracted as a standalone field |
| `stability_rule` | direct geodesic-DM / homogeneous-vacuum perturbation route; no PPF/ePPF fallback |
| `PPF_or_ePPF_rule` | not used |
| `solver_route` | modified CosmoMC MCMC reconstruction |
| `posterior_covariance_PCA_products` | PCA method and mode table stated; no machine-readable product created by this extraction |
| `retained_Gamma_mapping` | comparator only; no direct equivalence |
| `translation_hazards` | nonlinear density factor, raw `Q` sign, DM-frame closure, homogeneous-vacuum slicing, RSD observable replacement, LyaF-era tension dependence |
| `stop_status` | `continue_to_perturbation_extract` |

## Boundary Versus Martinelli/Hogg

| Object | Wang 2015 | Martinelli/Hogg | QFUDS implication |
| --- | --- | --- | --- |
| coupling variable | `alpha(a)` | `q_V(z)` / `q(z)` | no symbol-level mapping |
| parameterized `Q` | `3 alpha H rho_dm V / (rho_dm + V)` | `-q H V` | density factor differs materially |
| positive dimensionless sign | DM-to-vacuum | vacuum-to-DM | sign flips across families |
| frame | DM comoving-orthogonal / geodesic | CDM-frame geodesic | close family, not identical notation |
| perturbation object | explicit `delta_dm` equation and RSD replacement | Martinelli gives detailed equations; Hogg inherits | perturbation route exists, but not QFUDS-derived |
| reconstruction | 40 bins in scale factor | Martinelli 4 bins; Hogg 17 bins | binning is inference machinery |
| PCA/evidence | three data-informed modes; not Bayesian-preferred over LCDM | Hogg also uses PCA/evidence boundary | useful anti-overfit pattern |

## Decision

| Question | Decision |
| --- | --- |
| Can Wang 2015 be used as a historical IV formalism teaching target? | Yes. |
| Is `alpha(a)` closer to retained positive `Gamma(a)` sign than Hogg/Martinelli `q(z)`? | Sign direction is closer, but density factor and perturbation closure still block direct mapping. |
| Can the `z around 2` sign-change region be used as QFUDS evidence? | No; it is tied to 2015 LyaF/RSD tensions and Bayesian evidence does not prefer the model over LCDM. |
| Does this open QFUDS Level 2B? | No. |
| Does this allow NASA/BAO/CMB/LSS model comparison now? | No. |
| What is the next safe step? | Compare Wang 2015 against the Martinelli/Hogg geodesic-CDM family before any retained timing fit. |

## Next Executable Instruction

Create a convention comparison note for Wang 2015 versus the Martinelli/Hogg
geodesic-CDM family. Freeze the sign, density-factor, `Q^mu` frame,
perturbation, RSD-observable, prior/PCA, and evidence differences before any
retained `Gamma(a)` fit or observational baseline interpretation.
