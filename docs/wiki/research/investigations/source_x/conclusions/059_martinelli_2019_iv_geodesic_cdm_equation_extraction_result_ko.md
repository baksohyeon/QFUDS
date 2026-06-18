---
doc_id: audit_2026_06_18_martinelli_2019_iv_geodesic_cdm_equation_extraction_result_ko
title: "2026-06-18 Martinelli 2019 IV/Geodesic-CDM Equation Extraction Result"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - plan_2026_06_18_paper_by_paper_iv_ide_equation_extraction_ko
  - audit_2026_06_18_li_escamilla_iv_ide_convention_comparison_note_ko
  - asset_martinelli_2019_interacting_vacuum_geodesic_cdm
  - asset_martinelli_2019_interacting_vacuum_geodesic_cdm_equation_extract_20260618
  - lit_martinelli_2019_interacting_vacuum_geodesic_cdm
  - roadmap
next_gate: cache/source-extract Hogg 2020 for same-family IV/geodesic-CDM comparison
last_updated: 2026-06-18
---

# 2026-06-18 Martinelli 2019 IV/Geodesic-CDM Equation Extraction Result

## Purpose

이 문서는 [058 paper-by-paper IV/IDE extraction plan](../plans/058_paper_by_paper_iv_ide_equation_extraction_plan_ko.md)의
세 번째 Tier 1 실행 결과다.

대상은 Martinelli et al. 2019 interacting vacuum / geodesic CDM paper다.
목적은 retained `Gamma(a)`를 맞추는 것이 아니라, 실제 interacting-vacuum
문헌이 background `Q`, covariant `Q^mu`, transfer frame, perturbation
closure, and solver route를 어떻게 한 묶음으로 세우는지 확인하는 것이다.

## Workflow Boundary

This result follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).

No new external source, posterior product, covariance product, chain, numerical
`q_V(z)` product, or product-absence claim is introduced here. The extraction
uses the already cached Martinelli 2019 arXiv source:

```text
docs/wiki/research/assets/martinelli_2019_interacting_vacuum_geodesic_cdm/source/extracted/void.tex
```

A manual structured extract was added at:

```text
docs/wiki/research/assets/martinelli_2019_interacting_vacuum_geodesic_cdm/digitization/equation_extraction_20260618.md
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

Martinelli 2019 passes the exact equation extraction gate as:

```text
stop_status = continue_to_perturbation_extract
```

Reason: the cached source gives the background transfer, covariant `Q^mu`,
CDM-frame pure energy exchange, geodesic condition, perturbation equations,
synchronous CDM-comoving gauge closure, modified growth/RSD interpretation, and
modified CAMB/CosmoMC route.

It does not provide:

```text
QFUDS physical source X
QFUDS-derived Q^mu[X, ...]
phase-B pressure derivation from a foam sector
retained Gamma(a) equivalence
machine-readable q_V(z) posterior history
```

## Structured Extraction Row

| Field | Extracted value |
| --- | --- |
| `paper_id` | `lit_martinelli_2019_interacting_vacuum_geodesic_cdm` |
| `record_path` | [Martinelli 2019 literature record](../../../literature/martinelli_2019_interacting_vacuum_geodesic_cdm.md) |
| `source_state` | `asset_cached`; source TeX extracted; `manual_structured_extract` added |
| `equation_status` | `exact_in_cached_record` for background `Q`, covariant `Q^mu`, frame, perturbations, and solver route |
| `model_class` | interacting vacuum / geodesic CDM |
| `background_Q_raw` | `dot rho_c + 3H rho_c = -Q`; `dot V = Q` |
| `background_Q_parameterized` | `Q = -q_V Theta V / 3`; FLRW `Q(z) = -q_V(z) H(z) V(z)` |
| `background_qV_equations` | `dot rho_c + 3H rho_c = q_V H V`; `dot V = -q_V H V` |
| `time_derivative_variable` | cosmic time for dot equations; redshift for `q_V(z)` reconstruction |
| `hubble_factor_in_Q` | `H` in FLRW; covariant `Theta/3` |
| `sign_convention_raw` | raw `Q>0` means CDM-to-vacuum; dimensionless `q_V>0` means vacuum-to-CDM |
| `positive_coupling_direction` | positive `q_V` transfers vacuum energy into CDM |
| `density_factor` | vacuum density `V` |
| `coupling_variable` | `q_V(z)` |
| `coupling_dimension` | dimensionless |
| `time_dependence` | constant, transition redshift, seeded-vacuum, and four-bin redshift reconstructions |
| `Q_mu_defined` | yes |
| `Q_mu_direction` | parallel to CDM four-velocity after setting `f^mu=0` |
| `momentum_transfer_frame` | CDM frame / geodesic CDM frame |
| `gauge` | synchronous gauge comoving with CDM |
| `delta_Q` | `delta Q = 0` in the selected gauge |
| `delta_coupling` | no independent `delta q_V` extracted; closure uses homogeneous interaction in CDM-comoving gauge |
| `pressure_perturbation` | vacuum perturbation homogeneous in selected gauge: `delta V = 0` |
| `sound_speed` | geodesic CDM condition implies zero effective sound speed for matter perturbations in the stated setup |
| `anisotropic_stress` | not extracted as a standalone field |
| `initial_conditions` | present-day `rho_c^0` and `V_0`; backward integration |
| `stability_rule` | direct perturbation closure under geodesic-CDM/synchronous-comoving assumptions; no PPF/ePPF fallback |
| `PPF_or_ePPF_rule` | not used |
| `solver_route` | modified CAMB plus CosmoMC |
| `posterior_covariance_PCA_products` | not re-audited here; no new product-absence claim |
| `retained_Gamma_mapping` | comparator only; no direct equivalence |
| `translation_hazards` | raw `Q` vs `q_V` sign flip, vacuum-density factor, CDM-frame closure, gauge-specific `delta Q=0`, redshift-bin tuning risk |
| `stop_status` | `continue_to_perturbation_extract` |

## Translation Boundary

The repo-local retained convention is:

```math
Q = \mathcal{H}\Gamma(a)\rho_A.
```

Martinelli 2019 uses:

```math
Q = -q_{\rm V}\frac{\Theta}{3}V,
\qquad
Q(z) = -q_{\rm V}(z)H(z)V(z).
```

Therefore a valid translation would need:

```text
raw Q vs q_V sign mapping
vacuum-density V vs retained rho_A conversion
H vs conformal-Hubble convention conversion
CDM-frame geodesic closure decision
gauge-specific delta Q and delta V boundary
redshift-bin/transition-redshift mapping
```

The result is stronger than Escamilla for formalism learning because it reaches
`Q^mu`, frame, perturbations, and CAMB. It still does not derive a physical
QFUDS source.

## Decision

| Question | Decision |
| --- | --- |
| Can Martinelli 2019 be used as an IV/geodesic-CDM formalism teaching target? | Yes. |
| Can `q_V(z)` be treated as direct QFUDS evidence? | No. |
| Can retained `Gamma(a)` be translated directly into `q_V(z)`? | No; sign, density, Hubble, frame, and gauge conventions differ. |
| Does this open QFUDS Level 2B? | No. |
| Does this allow NASA/BAO/CMB/LSS model comparison now? | No. |
| What is the next safe step? | Cache/source-extract Hogg 2020, then compare it against Martinelli 2019 as same-family IV/geodesic-CDM work. |

## Next Executable Instruction

Create the next source-cache task for Hogg 2020. Apply the Research Asset and
Product Workflow first, cache the PDF/source if available, then extract only
the exact background `Q`, `Q^mu`/frame, perturbation route, sign/density/Hubble
conventions, and product-state boundary. Do not fit retained `Gamma(a)`.
