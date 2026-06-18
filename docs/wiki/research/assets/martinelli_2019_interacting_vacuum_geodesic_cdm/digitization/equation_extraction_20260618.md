---
doc_id: asset_martinelli_2019_interacting_vacuum_geodesic_cdm_equation_extract_20260618
title: Martinelli 2019 IV/Geodesic-CDM Equation Extraction
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - asset_martinelli_2019_interacting_vacuum_geodesic_cdm
  - lit_martinelli_2019_interacting_vacuum_geodesic_cdm
next_gate: use only through the Source-X 059 Martinelli extraction result
last_updated: 2026-06-18
---

# Martinelli 2019 IV/Geodesic-CDM Equation Extraction

## Workflow State

This extraction follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).

This is a manual structured extract from the cached arXiv source TeX:

```text
docs/wiki/research/assets/martinelli_2019_interacting_vacuum_geodesic_cdm/source/extracted/void.tex
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
| `model_class` | interacting vacuum / geodesic CDM | `void.tex:130`, `void.tex:140-183` |
| `vacuum_stress_energy` | `Tcheck^mu_nu = -V g^mu_nu`; vacuum has `w=-1` and no defined vacuum four-velocity | `void.tex:152-156` |
| `CDM_stress_energy` | `T^mu_nu = rho_c u^mu u_nu` | `void.tex:158-161` |
| `covariant_split` | `nabla_mu T^mu_nu = -Q_nu`; `nabla_mu Tcheck^mu_nu = -nabla_nu V = Q_nu` | `void.tex:162-167` |
| `Q_mu_defined` | yes | `void.tex:171-177` |
| `Q_mu_decomposition` | `Q^mu = Q u^mu + f^mu` | `void.tex:171-175` |
| `momentum_transfer_frame` | CDM frame / geodesic CDM frame | `void.tex:177-181` |
| `Q_mu_direction` | `Q^mu = Q u^mu` after setting `f^mu = 0` | `void.tex:177-181` |
| `geodesic_condition` | `f^mu = 0` implies CDM four-acceleration `a^mu = 0` | `void.tex:177-181` |
| `background_equations_raw_Q` | `dot rho_c + 3H rho_c = -Q`; `dot V = Q` | `void.tex:185-191` |
| `background_Q_parameterization` | `Q = -q_V Theta V / 3`; in FLRW, `Q(z) = -q_V(z) H(z) V(z)` | `void.tex:258-268` |
| `background_equations_qV` | `dot rho_c + 3H rho_c = q_V H V`; `dot V = -q_V H V` | `void.tex:269-273` |
| `positive_qV_direction` | positive `q_V` means vacuum decays into CDM in the paper convention | `void.tex:269-273`, `void.tex:335-337`, `void.tex:560` |
| `negative_qV_direction` | negative `q_V` means CDM decays into vacuum | `void.tex:335-337` |
| `time_derivative_variable` | cosmic time for dot equations; redshift for reconstructed coupling function | `void.tex:185-191`, `void.tex:258-283` |
| `hubble_factor_in_Q` | `H` in FLRW; `Theta/3` covariantly | `void.tex:258-268` |
| `density_factor` | vacuum density `V` | `void.tex:258-273` |
| `coupling_variable` | `q_V(z)` | `void.tex:258-268` |
| `coupling_dimension` | dimensionless | `void.tex:258-263` |
| `time_dependence` | constant, transition-redshift, seeded-vacuum, and four-bin redshift reconstructions | `void.tex:130-134`, `void.tex:277-289`, `void.tex:393-399` |
| `bin_definition` | four low-redshift bins with `z_i in {0.3, 0.9, 2.5, 10}` | `void.tex:393-399` |
| `perturbation_equations` | CDM/vacuum perturbed energy and momentum equations are stated | `void.tex:193-214` |
| `gauge` | synchronous gauge comoving with CDM, with `phi = v = B = 0` | `void.tex:215-220` |
| `delta_V` | `delta V = 0` in the CDM-comoving slicing/gauge | `void.tex:217-220` |
| `delta_Q` | `delta Q = 0` in the same gauge | `void.tex:219-220` |
| `density_contrast_equation` | `dot delta_c = (Q/rho_c) delta_c + 3 dot psi - nabla^2 dot E` | `void.tex:221-225` |
| `growth_observable_adjustment` | `f_i = f - Q/(H rho_c)` for interacting-vacuum RSD interpretation | `void.tex:240-248` |
| `PPF_or_ePPF_rule` | not used; perturbations are treated directly in the geodesic-CDM setup | `void.tex:207-227`, `void.tex:383-390` |
| `solver_route` | modified CAMB for background densities and CDM perturbation source term; CosmoMC for sampling | `void.tex:383-391` |
| `initial_conditions` | present-day `rho_c^0 = 3H_0^2 Omega_c`; `V_0 = 3H_0^2 Omega_Lambda`; evolved backward in time | `void.tex:383-389` |
| `product_boundary` | cached source includes paper text and figure PDFs; no curve-level numeric history was created by this extraction | asset README |

## Translation Hazards

- The paper has two related sign variables: raw `Q` and dimensionless `q_V`.
  The FLRW parameterization is `Q = -q_V H V`.
- Positive `q_V` means vacuum-to-CDM transfer, which is opposite to the
  retained `Gamma(a)` positive transfer direction.
- The density factor is vacuum density `V`, not retained `rho_A` and not
  Escamilla's `rho_c,0`.
- The perturbation closure is tied to geodesic CDM, CDM-comoving synchronous
  gauge, `delta V = 0`, and `delta Q = 0`. It cannot be copied into QFUDS as a
  physical source derivation.
- The four-bin redshift choices and transition redshifts are reconstruction
  parameters, not physical QFUDS scales.

## Stop Status

```text
continue_to_perturbation_extract
```

Reason: the cached source gives background `Q`, covariant `Q^mu`, the
CDM-frame/geodesic condition, perturbation equations, gauge/frame closure, RSD
growth adjustment, and a CAMB/CosmoMC solver route. It is still not QFUDS
physical admission because the source object is academic interacting vacuum,
not a derived QFUDS foam sector.
