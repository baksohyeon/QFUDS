---
doc_id: asset_wang_2015_dark_matter_vacuum_interaction_equation_extract_20260618
title: Wang 2015 Dark Matter Vacuum Interaction Equation Extraction
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - asset_wang_2015_dark_matter_vacuum_interaction
  - lit_wang_2015_dark_matter_vacuum_interaction
next_gate: use only through the Source-X 059 Wang extraction result
last_updated: 2026-06-18
---

# Wang 2015 Dark Matter Vacuum Interaction Equation Extraction

## Workflow State

This extraction follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).

This is a manual structured extract from the cached arXiv source TeX:

```text
docs/wiki/research/assets/wang_2015_dark_matter_vacuum_interaction/source/extracted/Recon_Inter-resubmit_2.tex
```

Workflow state:

```text
asset_cached
asset_extracted_not_digitized
source_text_parse
manual_structured_extract
```

This file is not PDF parsing, numerical digitization, posterior extraction,
covariance extraction, curve digitization, or QFUDS evidence.

## Extracted Fields

| Field | Extracted value | Source location |
| --- | --- | --- |
| `model_class` | interacting vacuum / dark matter-vacuum energy interaction | `Recon_Inter-resubmit_2.tex:85-106` |
| `vacuum_variable` | vacuum energy density `V` with `w=-1`; `V` varies by interaction with DM | `Recon_Inter-resubmit_2.tex:85` |
| `covariant_vacuum_relation` | `nabla_mu V = -Q_mu` | `Recon_Inter-resubmit_2.tex:85` |
| `background_equations_raw_Q` | `dot rho_dm + 3H rho_dm = -Q`; `dot V = Q` | `Recon_Inter-resubmit_2.tex:89-95` |
| `raw_Q_direction` | raw `Q>0` transfers DM energy into vacuum energy | `Recon_Inter-resubmit_2.tex:89-95` |
| `Q_mu_defined` | yes | `Recon_Inter-resubmit_2.tex:97-102` |
| `Q_mu_direction` | `Q^mu = Q u^mu_dm`, parallel to DM four-velocity | `Recon_Inter-resubmit_2.tex:97-102` |
| `momentum_transfer_frame` | DM comoving-orthogonal frame; no momentum transfer in that frame | `Recon_Inter-resubmit_2.tex:97-102` |
| `geodesic_condition` | DM particles follow geodesics as in LCDM under the chosen covariant form | `Recon_Inter-resubmit_2.tex:97-102` |
| `vacuum_perturbation_frame` | choose frame with spatially homogeneous vacuum, `delta V = 0`; coincides with geodesic-DM comoving-orthogonal frame | `Recon_Inter-resubmit_2.tex:97-102` |
| `irrotational_condition` | energy transfer is potential flow `Q^mu = -nabla^mu V`; DM velocity must be irrotational | `Recon_Inter-resubmit_2.tex:97-102` |
| `delta_dm_equation` | `dot delta_dm = -vartheta + Q(a_i) delta_dm / rho_dm` | `Recon_Inter-resubmit_2.tex:99-102` |
| `gauge` | comoving-synchronous gauge, with `vartheta = dot h / 2` | `Recon_Inter-resubmit_2.tex:99-102` |
| `background_Q_parameterization` | `Q = 3 alpha H rho_dm V / (rho_dm + V)` | `Recon_Inter-resubmit_2.tex:104` |
| `coupling_variable` | `alpha(a)` / binned `alpha_i` | `Recon_Inter-resubmit_2.tex:104-112` |
| `coupling_dimension` | dimensionless | `Recon_Inter-resubmit_2.tex:104` |
| `related_q_parameter` | Salvatelli-related `q = -3 alpha rho_dm / (rho_dm + V)` noted in footnote | `Recon_Inter-resubmit_2.tex:104` |
| `positive_alpha_direction` | positive `alpha` corresponds to positive raw `Q`, i.e. DM-to-vacuum transfer | `Recon_Inter-resubmit_2.tex:104`, `Recon_Inter-resubmit_2.tex:160-164` |
| `negative_alpha_direction` | negative `alpha` corresponds to vacuum decay into DM | `Recon_Inter-resubmit_2.tex:160-164`, `Recon_Inter-resubmit_2.tex:204-206` |
| `background_degeneracy` | can reproduce general background cosmologies and is degenerate with quintessence at background level | `Recon_Inter-resubmit_2.tex:95`, `Recon_Inter-resubmit_2.tex:106` |
| `perturbation_distinction` | perturbations have vanishing sound speed with nonzero energy transfer determined by background cosmology | `Recon_Inter-resubmit_2.tex:106` |
| `correlation_prior` | CPZ prior on binned `alpha(a)` with covariance from bin-integrated correlation function | `Recon_Inter-resubmit_2.tex:110-123` |
| `N_eff_rule` | `N_eff ~= (a_max - a_min) / a_c`; reconstruction independent of `N` when `N > N_eff` | `Recon_Inter-resubmit_2.tex:121-123` |
| `chosen_prior_parameters` | `sigma_bar_alpha = 0.04`; `a_c = 0.06` | `Recon_Inter-resubmit_2.tex:121-123` |
| `data_used` | Planck/WMAP CMB, JLA SNe, 6dFGRS/SDSS/BOSS/LyaF BAO, and RSD data combinations | `Recon_Inter-resubmit_2.tex:135` |
| `RSD_growth_observable` | `f_i = f_dm - Q(a_i)/(H rho_dm)` and weighted `f_vartheta`; RSD measures `f_vartheta sigma_8` in this model | `Recon_Inter-resubmit_2.tex:137-146` |
| `bin_definition` | 40 bins uniform in scale factor over `[0.001, 1]` | `Recon_Inter-resubmit_2.tex:150` |
| `solver_route` | modified CosmoMC MCMC reconstruction | `Recon_Inter-resubmit_2.tex:150` |
| `sign_change_result` | with LyaF included, best-fit `alpha(a)` is positive at `z >= about 2.1`, negative at `0.6 <= z <= about 2.1`, and consistent with LCDM at `z <= about 0.6` | `Recon_Inter-resubmit_2.tex:160-164` |
| `Bayes_factor_boundary` | fit improvement does not compensate for increased parameter volume; model not preferred over LCDM | `Recon_Inter-resubmit_2.tex:164-165` |
| `PCA_route` | Fisher matrix/eigenmodes of `alpha` bins after marginalizing over cosmological parameters | `Recon_Inter-resubmit_2.tex:173-177` |
| `PCA_result` | three data eigenmodes not affected by the prior; remaining modes prior-dominated | `Recon_Inter-resubmit_2.tex:175-177` |
| `mode_coefficients` | first three `beta_i` coefficients table exists in source | `Recon_Inter-resubmit_2.tex:180-202` |
| `conclusion_boundary` | mildly favored only with BOSS LyaF; LyaF BAO systematic caveat stated; not Bayesian-preferred over LCDM | `Recon_Inter-resubmit_2.tex:204-206` |
| `product_boundary` | cached source includes paper text and EPS figures; this extraction does not create machine-readable posterior chains, covariance matrices, or numerical `alpha(a)` products | asset README |

## Translation Hazards

- Wang 2015 uses `Q = 3 alpha H rho_dm V / (rho_dm + V)`, not a simple
  one-density proportional transfer.
- Raw `Q>0` and `alpha>0` mean DM-to-vacuum transfer, matching the retained
  positive `Gamma(a)` direction more closely than Martinelli/Hogg `q>0`, but
  the density factor and perturbation closure still differ.
- The density factor is nonlinear in `rho_dm` and `V`, not retained `rho_A`.
- The perturbation route depends on DM-frame geodesic closure, homogeneous
  vacuum slicing, and the modified RSD observable `f_vartheta sigma_8`.
- The apparent sign change is tied to 2015 BOSS LyaF BAO and RSD tension. It
  must be treated as historical baseline/context, not as QFUDS evidence.
- CPZ prior parameters, 40 bins, PCA modes, and Bayes-factor behavior are
  inference safeguards, not a physical foam scale or source derivation.

## Stop Status

```text
continue_to_perturbation_extract
```

Reason: the cached source gives background `Q`, covariant `Q^mu`, the DM-frame
geodesic condition, perturbation equation, RSD observable adjustment, binned
correlation-prior reconstruction, PCA, Bayesian evidence boundary, and
modified CosmoMC route. It is still not QFUDS physical admission because the
source object is an academic interacting-vacuum ansatz, not a derived QFUDS
foam sector.
