---
doc_id: audit_2026_06_18_hogg_2020_iv_geodesic_cdm_equation_extraction_result_ko
title: "2026-06-18 Hogg 2020 IV/Geodesic-CDM Equation Extraction Result"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - plan_2026_06_18_paper_by_paper_iv_ide_equation_extraction_ko
  - audit_2026_06_18_martinelli_2019_iv_geodesic_cdm_equation_extraction_result_ko
  - asset_hogg_2020_vacuum_geodesic_cdm_interaction
  - asset_hogg_2020_vacuum_geodesic_cdm_interaction_equation_extract_20260618
  - lit_hogg_2020_vacuum_geodesic_cdm_interaction
  - roadmap
next_gate: compare Martinelli 2019 and Hogg 2020 as same-family IV/geodesic-CDM formalism before any retained timing fit
last_updated: 2026-06-18
---

# 2026-06-18 Hogg 2020 IV/Geodesic-CDM Equation Extraction Result

## Purpose

이 문서는 [058 paper-by-paper IV/IDE extraction plan](../plans/058_paper_by_paper_iv_ide_equation_extraction_plan_ko.md)의
네 번째 Tier 1 실행 결과다.

대상은 Hogg et al. 2020 vacuum-geodesic CDM interaction paper다. 목적은
retained `Gamma(a)`를 맞추는 것이 아니라, Martinelli 2019와 같은 계열의
interacting-vacuum 문헌이 `q(z)`를 더 높은 차원의 reconstruction 문제로
다룰 때 어떤 prior, binning, perturbation boundary, solver route, and
model-selection boundary를 두는지 확인하는 것이다.

## Workflow Boundary

This result follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).

No new external source, posterior product, covariance product, chain, numerical
`q(z)` product, or product-absence claim is introduced here. The extraction uses
the already cached Hogg 2020 arXiv source:

```text
docs/wiki/research/assets/hogg_2020_vacuum_geodesic_cdm_interaction/source/extracted/17bins.tex
```

A manual structured extract was added at:

```text
docs/wiki/research/assets/hogg_2020_vacuum_geodesic_cdm_interaction/digitization/equation_extraction_20260618.md
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

Hogg 2020 passes the same-family equation extraction gate as:

```text
stop_status = continue_to_perturbation_extract
```

Reason: the cached source gives the background transfer, `Q^mu`/frame summary,
geodesic-CDM closure, modified CAMB/CosmoMC route, RSD observable adjustment,
17-bin correlation-prior reconstruction, PCA prior-dominance check, and
Bayesian evidence boundary.

It does not provide:

```text
QFUDS physical source X
QFUDS-derived Q^mu[X, ...]
phase-B pressure derivation from a foam sector
retained Gamma(a) equivalence
machine-readable q(z) posterior history
```

## Structured Extraction Row

| Field | Extracted value |
| --- | --- |
| `paper_id` | `lit_hogg_2020_vacuum_geodesic_cdm_interaction` |
| `record_path` | [Hogg 2020 literature record](../../../literature/hogg_2020_vacuum_geodesic_cdm_interaction.md) |
| `source_state` | `asset_cached`; source TeX extracted; `manual_structured_extract` added |
| `equation_status` | `exact_in_cached_record` for background `Q`, `Q^mu`/frame summary, bin/prior/PCA/evidence; perturbation details inherited from Martinelli/Wands |
| `model_class` | interacting vacuum / geodesic CDM |
| `background_Q_raw` | `dot rho_c + 3H rho_c = -Q`; `dot V = Q` |
| `background_Q_parameterized` | `Q = -q H V` |
| `background_q_equations` | `dot rho_c + 3H rho_c = q H V`; `dot V = -q H V` |
| `time_derivative_variable` | cosmic time for dot equations; scale factor / redshift for `q(a)` and `q(z)` reconstruction |
| `hubble_factor_in_Q` | `H` in FLRW |
| `sign_convention_raw` | raw `Q>0` means CDM-to-vacuum; dimensionless `q>0` means vacuum-to-CDM |
| `positive_coupling_direction` | positive `q` transfers vacuum energy into CDM |
| `density_factor` | vacuum density `V` |
| `coupling_variable` | `q(a)` / `q(z)` |
| `coupling_dimension` | dimensionless |
| `time_dependence` | 17 redshift/scale-factor bins plus spline and Gaussian-process reconstructions |
| `Q_mu_defined` | yes, as a summary of the vacuum-geodesic CDM setup |
| `Q_mu_direction` | parallel to CDM four-velocity after setting momentum exchange to zero |
| `momentum_transfer_frame` | CDM frame / geodesic CDM frame |
| `gauge` | synchronous gauge comoving with CDM |
| `delta_Q` | interaction is stated as unperturbed in the selected gauge; detailed equation inherited from Martinelli/Wands |
| `delta_coupling` | no independent perturbation of `q` extracted |
| `pressure_perturbation` | not independently restated; vacuum-geodesic CDM closure inherited from cited theory papers |
| `sound_speed` | not restated as a standalone parameter; geodesic-CDM setup chosen to avoid extra CDM acceleration |
| `anisotropic_stress` | not extracted as a standalone field |
| `initial_conditions` | not restated as a standalone field; analysis uses modified CAMB/CosmoMC |
| `stability_rule` | direct geodesic-CDM perturbation route by reference, not PPF/ePPF |
| `PPF_or_ePPF_rule` | not used |
| `solver_route` | modified CAMB plus CosmoMC; GetDist covariance/PCA; MCEvidence Bayesian evidence |
| `posterior_covariance_PCA_products` | PCA method stated; no machine-readable product created by this extraction |
| `retained_Gamma_mapping` | comparator only; no direct equivalence |
| `translation_hazards` | raw `Q` vs `q` sign flip, vacuum-density factor, CDM-frame closure, inherited perturbation equations, redshift-bin/correlation-prior tuning risk |
| `stop_status` | `continue_to_perturbation_extract` |

## Reconstruction Boundary

Hogg 2020 is useful because it shows how an academic IV/geodesic-CDM paper
prevents an arbitrary binned interaction history from becoming pure visual
overfitting:

| Object | Hogg 2020 treatment | QFUDS boundary |
| --- | --- | --- |
| `q_i` bins | 17 bins in scale factor, with one wide high-redshift bin | not a foam scale or transition width |
| correlation prior | CPZ prior with `a_c = 0.06`, `N_eff = 16.7`, `N=17`, and `sigma_q = 0.6` | not a physical source derivation |
| reconstruction | spline and GP from posterior means and errors | not retained `Gamma(a)` matching |
| prior check | prior-only versus prior-plus-data PCA eigenvalues | useful audit pattern for non-circularity |
| evidence | fixed fiducial weakly favors LCDM; mean fiducial is not worth more than a bare mention | no validation language |
| tension outcome | does not solve `H_0`; apparent `sigma_8` relaxation is contour broadening | baseline constraint only |

## Translation Boundary

The repo-local retained convention is:

```math
Q = \mathcal{H}\Gamma(a)\rho_A.
```

Hogg 2020 uses:

```math
Q = -qHV.
```

Therefore a valid translation would need:

```text
raw Q vs q sign mapping
vacuum-density V vs retained rho_A conversion
H vs conformal-Hubble convention conversion
CDM-frame geodesic closure decision
gauge-specific delta Q and delta V boundary inherited from Martinelli/Wands
bin/prior/reconstruction mapping
```

The paper is strong as a formalism-learning target because it shows the
reconstruction safeguards that the retained brute-force `Gamma(a)` work lacked:
explicit bin priors, prior-dominance checks, solver route, and model-selection
language. It still does not derive a physical QFUDS source.

## Decision

| Question | Decision |
| --- | --- |
| Can Hogg 2020 be used as an IV/geodesic-CDM formalism teaching target? | Yes, especially together with Martinelli 2019. |
| Can `q(z)` be treated as direct QFUDS evidence? | No. |
| Can retained `Gamma(a)` be translated directly into Hogg `q(z)`? | No; sign, density, Hubble, frame, gauge, and prior conventions differ. |
| Does this open QFUDS Level 2B? | No. |
| Does this allow NASA/BAO/CMB/LSS model comparison now? | No. |
| What is the next safe step? | Compare Martinelli 2019 and Hogg 2020 as one same-family IV/geodesic-CDM lane, then decide whether Wang 2015 should be cached/extracted as the next historical convention target. |

## Next Executable Instruction

Create a same-family comparison note for Martinelli 2019 and Hogg 2020. The
note should separate shared physical setup (`Q`, `Q^mu`, CDM-frame closure,
solver route) from Hogg-specific reconstruction safeguards (17 bins, CPZ prior,
PCA, Bayes factor). Do not fit retained `Gamma(a)` and do not use NASA/BAO/CMB
as QFUDS evidence.
