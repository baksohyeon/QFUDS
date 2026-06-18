---
doc_id: asset_hogg_2020_vacuum_geodesic_cdm_interaction_equation_extract_20260618
title: Hogg 2020 Vacuum Geodesic CDM Interaction Equation Extraction
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - asset_hogg_2020_vacuum_geodesic_cdm_interaction
  - lit_hogg_2020_vacuum_geodesic_cdm_interaction
  - asset_martinelli_2019_interacting_vacuum_geodesic_cdm_equation_extract_20260618
next_gate: use only through the Source-X 059 Hogg extraction result
last_updated: 2026-06-18
---

# Hogg 2020 Vacuum Geodesic CDM Interaction Equation Extraction

## Workflow State

This extraction follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).

This is a manual structured extract from the cached arXiv source TeX:

```text
docs/wiki/research/assets/hogg_2020_vacuum_geodesic_cdm_interaction/source/extracted/17bins.tex
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
| `model_class` | interacting vacuum / geodesic CDM | `17bins.tex:128`, `17bins.tex:134-139` |
| `covariant_Q_mu_summary` | `Q^mu = Q u^mu + f^mu`; `f^mu` is momentum exchange | `17bins.tex:134-139` |
| `momentum_transfer_frame` | CDM frame / geodesic CDM frame | `17bins.tex:134-139` |
| `Q_mu_direction` | parallel to CDM four-velocity after setting `f^mu = 0` | `17bins.tex:134-139` |
| `geodesic_condition` | `f^mu = 0` implies `a^mu = 0` and no extra acceleration on CDM particles | `17bins.tex:134-139` |
| `perturbation_closure_summary` | in synchronous CDM-comoving gauge, the interaction is unperturbed and encoded in background `Q` | `17bins.tex:134-139` |
| `detailed_perturbation_equations` | not restated; paper points to Wands 2012 and Martinelli 2019 for the covariant and perturbation treatment | `17bins.tex:139` |
| `background_equations_raw_Q` | `dot rho_c + 3H rho_c = -Q`; `dot V = Q` | `17bins.tex:141-146` |
| `background_Q_parameterization` | `Q = -q H V` | `17bins.tex:148-157` |
| `background_equations_q` | `dot rho_c + 3H rho_c = q H V`; `dot V = -q H V` | `17bins.tex:152-157` |
| `positive_q_direction` | positive `q` means vacuum decays and dark matter grows | `17bins.tex:157` |
| `negative_q_direction` | negative `q` means dark matter decays and vacuum grows | `17bins.tex:157` |
| `coupling_variable` | `q(a)` / `q(z)`; dimensionless coupling strength | `17bins.tex:157`, `17bins.tex:163-165` |
| `time_derivative_variable` | cosmic time for dot equations; scale factor or redshift for the reconstructed coupling | `17bins.tex:141-157`, `17bins.tex:163-165` |
| `hubble_factor_in_Q` | `H` in FLRW | `17bins.tex:148-157` |
| `density_factor` | vacuum density `V` | `17bins.tex:141-157` |
| `bin_definition` | 17 bins: 16 uniform in scale factor from `a=1.0` to `a=0.14`, plus one wide high-redshift bin to `a approx 0.0001` | `17bins.tex:163-165` |
| `sampled_parameters` | `q_i`, `Omega_b h^2`, `Omega_c h^2`, `A_s`, `n_s`, and `H_0` | `17bins.tex:163-165` |
| `q_prior_range` | `q_i in [-6.0, 3.0]` | `17bins.tex:167-181` |
| `correlation_prior_role` | suppress rapid oscillations and reduce reconstruction bias from binning | `17bins.tex:184-189` |
| `correlation_function` | `xi(|a-a'|) = <[q(a)-bar q(a)][q(a')-bar q(a')]>`; covariance from double bin integral | `17bins.tex:191-197` |
| `CPZ_prior` | `xi(|a-a'|) = xi(0) / [1 + (|a-a'|/a_c)^2]` | `17bins.tex:199-203` |
| `N_eff_rule` | require `N > N_eff`, with `N_eff = (a_max - a_min) / a_c` | `17bins.tex:203-212` |
| `chosen_correlation_length` | `a_c = 0.06`, giving `N_eff = 16.7`, hence `N=17` | `17bins.tex:212` |
| `prior_strength` | uses variance of mean with `sigma_q = 0.6` | `17bins.tex:214` |
| `data_used` | Planck 2018 CMB temperature/polarization, 6dF BAO, SDSS DR12 BAO+RSD, Pantheon SNe Ia | `17bins.tex:216-219` |
| `BAO_boundary` | BAO included; paper states late-time Hubble-tension relief becomes disfavored when BAO and SNe are used together | `17bins.tex:219` |
| `RSD_growth_observable` | `f_i = f - Q / (H rho_c)` rather than direct LCDM growth factor `f` | `17bins.tex:221-225` |
| `solver_route` | modified CAMB and CosmoMC; GetDist for covariance/PCA; MCEvidence for Bayesian evidence | `17bins.tex:162-165`, `17bins.tex:314`, `17bins.tex:362` |
| `reconstruction_route` | cubic spline and Gaussian process using posterior means and 1-sigma errors of `q_i` | `17bins.tex:286-295` |
| `GP_kernel` | squared exponential kernel with optimized hyperparameters | `17bins.tex:278-286` |
| `PCA_route` | Fisher matrix eigenmodes from covariance of `q_i` after marginalizing over other parameters | `17bins.tex:312-328` |
| `prior_dominance_check` | prior-only MCMC chain compared to prior-plus-data eigenvalues | `17bins.tex:326-328` |
| `posterior_result_summary` | `q=0` / LCDM is within 1 sigma in every bin; Ockham preference for LCDM | `17bins.tex:235-243` |
| `tension_result_summary` | does not resolve `H_0`; apparent `sigma_8` relaxation comes from larger contours and should not be treated as true resolution | `17bins.tex:245-251` |
| `model_selection_result` | fixed fiducial weakly prefers LCDM; mean fiducial is not worth more than a bare mention; `Delta chi^2` improvement not significant | `17bins.tex:395-401` |
| `high_redshift_watch` | features near `z around 1` and `z around 3` are suggested as future enquiry targets, with Lyman-alpha forest weak lensing and SKA 21cm as possible probes | `17bins.tex:291-297` |
| `product_boundary` | cached source includes text and figure assets; this extraction does not create machine-readable posterior chains, covariance matrices, or numerical `q(z)` products | asset README and literature record |

## Translation Hazards

- Hogg 2020 uses the same vacuum-geodesic CDM family as Martinelli 2019, but
  writes the FLRW parameterization as `Q = -q H V` rather than the longer
  `q_V Theta V / 3` covariant notation.
- Positive `q` means vacuum-to-CDM transfer. This is opposite to the retained
  positive `Gamma(a)` direction in the repo-local convention.
- The density factor is vacuum density `V`, not retained `rho_A`.
- The perturbation closure is a geodesic-CDM, CDM-comoving synchronous-gauge
  closure inherited from the Martinelli/Wands treatment, not a new QFUDS
  derivation.
- The 17-bin reconstruction, correlation length, prior strength, spline, and GP
  choices are inference machinery. They must not be reinterpreted as foam
  transition scale, transition width, or physical source amplitude.
- The apparent high-redshift trough/feature is a watch target only. It is not
  retained `Gamma(a)` evidence without a separate, non-circular mapping and
  product audit.

## Stop Status

```text
continue_to_perturbation_extract
```

Reason: the cached source gives background `Q`, `Q^mu`/frame summary,
geodesic-CDM closure, modified CAMB/CosmoMC route, RSD observable adjustment,
and PCA/evidence checks. Detailed perturbation equations are inherited by
reference rather than restated, so Hogg should be used together with the
Martinelli 2019 extraction before any same-family comparison.
