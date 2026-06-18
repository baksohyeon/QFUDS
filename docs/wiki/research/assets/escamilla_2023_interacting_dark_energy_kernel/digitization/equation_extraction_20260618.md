---
doc_id: asset_escamilla_2023_interacting_dark_energy_kernel_equation_extract_20260618
title: Escamilla 2023 IV/IDE Kernel Equation Extraction
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - asset_escamilla_2023_interacting_dark_energy_kernel
  - lit_escamilla_2023_interacting_dark_energy_kernel
next_gate: use only through the Source-X 059 Escamilla extraction result
last_updated: 2026-06-18
---

# Escamilla 2023 IV/IDE Kernel Equation Extraction

## Workflow State

This extraction follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).

This is a manual structured extract from the cached arXiv source TeX:

```text
docs/wiki/research/assets/escamilla_2023_interacting_dark_energy_kernel/source/extracted/main.tex
```

Workflow state:

```text
asset_cached
asset_extracted_not_digitized
source_text_parse
manual_structured_extract
```

This file is not numerical digitization, posterior extraction, covariance
extraction, curve digitization, or QFUDS evidence.

## Extracted Fields

| Field | Extracted value | Source location |
| --- | --- | --- |
| `model_class` | interacting dark energy / dark matter background reconstruction | `main.tex:280-293` |
| `background_equations` | `dot rho_DM + 3H rho_DM = Q`; `dot rho_DE + 3H rho_DE(1+w_DE) = -Q` | `main.tex:280-283` |
| `time_derivative_variable` | cosmic time for dot equations; redshift derivatives after chain-rule rewrite | `main.tex:258`, `main.tex:340-350` |
| `Hubble_factor_in_Q` | `H` appears in the dimensionless normalizations | `main.tex:314-323`, `main.tex:372-376` |
| `sign_convention_raw` | `Q>0` means DE-to-DM transfer; `Q<0` means DM-to-DE transfer | `main.tex:285-289` |
| `positive_coupling_direction` | DE-to-DM in this paper convention | `main.tex:285-289` |
| `density_factor` | normalized against present critical density `rho_c,0`, not against `rho_DM` or `rho_DE` alone | `main.tex:321-323` |
| `coupling_variable` | `Pi_DE(z)` / `Pi_DM(z)` and visualization function `I_Q(z)` | `main.tex:321-323`, `main.tex:372-376` |
| `coupling_dimension` | dimensionless for `Pi_DE`, `Pi_DM`, and `I_Q` | `main.tex:321-323`, `main.tex:372-376` |
| `Pi_definition` | `Pi_DM = -Q/(3H rho_c,0) = -Pi_DE`, therefore `Pi_DE = Q/(3H rho_c,0)` | `main.tex:319-323` |
| `I_Q_definition` | `I_Q(z) = Q(z)/(rho_c,0 H(z)(1+z)^3)` | `main.tex:372-376` |
| `redshift_continuity_DM` | `d(rho_DM/rho_c,0)/dz = 3/(1+z)(rho_DM/rho_c,0 + Pi_DM)` | `main.tex:340-348` |
| `redshift_continuity_DE` | `d(rho_DE/rho_c,0)/dz = 3/(1+z)((1+w_DE)rho_DE/rho_c,0 + Pi_DE)` | `main.tex:347-350` |
| `reconstruction_nodes` | five amplitudes across `0 <= z <= 3`; GP nodes at `[0.0, 0.75, 1.5, 2.25, 3.0]` | `main.tex:447-454` |
| `bin_smoothing` | step-function interpolation smoothness parameter `xi = 0.15` | `main.tex:390-395` |
| `Q_mu_defined` | no covariant `Q^mu` extraction found in this pass | `main.tex:280-289`, `main.tex:328` |
| `momentum_transfer_frame` | not defined in the extracted source section | `main.tex:328` |
| `delta_Q` | not defined as an independent perturbation formula in this pass | `main.tex:328` |
| `perturbation_route` | deferred; paper states the proof-of-concept focus is background data | `main.tex:328` |
| `solver_route` | background expansion and distance inference with modified SimpleMC plus dynesty nested sampling | `main.tex:515-526` |
| `dataset_route` | cosmic chronometers, Pantheon+, and BAO | `main.tex:464-477` |
| `product_boundary` | cached source includes paper text and figure PDFs; no curve-level numeric history was created by this extraction | asset README |

## Translation Hazards

- This paper's positive `Q` convention means DE-to-DM transfer. That differs
  from the Li 2025 convention already extracted in Source-X 059.
- `Pi_DE` is normalized by `3H rho_c,0`; retained `Gamma(a)` uses a density
  factor tied to the retained comparator convention.
- The paper reconstructs a background kernel and explicitly defers full
  perturbation analysis. It cannot supply `Q^mu`, frame, `delta Q`, or
  perturbation closure for QFUDS.
- The redshift bins/nodes are reconstruction choices. They must not be reused
  as a QFUDS transition scale, width, or amplitude.

## Stop Status

```text
background_only_stop
```

Reason: the cached source gives a useful background IV/IDE kernel convention,
but does not provide the covariant transfer vector, momentum-transfer frame,
source perturbation route, or physical QFUDS source object needed for a
model-level comparison.
