---
doc_id: asset_li_2025_desi_dr2_sign_reversal_ide_equation_extract_20260618
title: Li 2025 IV/IDE Equation Extraction
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - asset_li_2025_desi_dr2_sign_reversal_ide
  - lit_li_2025_desi_dr2_sign_reversal_ide
next_gate: use only through the Source-X 059 extraction result
last_updated: 2026-06-18
---

# Li 2025 IV/IDE Equation Extraction

## Workflow State

This extraction follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).

This is a manual structured extract from the cached arXiv source TeX:

```text
docs/wiki/research/assets/li_2025_desi_dr2_sign_reversal_ide/source/extracted/idenpr.tex
```

Workflow state:

```text
asset_cached
asset_extracted_not_digitized
source_text_parse
manual_structured_extract
```

This file is not numerical digitization, posterior extraction, covariance
extraction, PCA-array extraction, or QFUDS evidence.

## Extracted Fields

| Field | Extracted value | Source location |
| --- | --- | --- |
| `model_class` | interacting vacuum / IDE with `w=-1` vacuum energy interacting with CDM | `idenpr.tex:65-75` |
| `background_equations` | `rho_de' + 3 Hc (1+w) rho_de = a Q`; `rho_c' + 3 Hc rho_c = -a Q` | `idenpr.tex:66-71` |
| `background_Q` | `Q = beta(a) H rho_de` | `idenpr.tex:71-75` |
| `time_derivative_variable` | conformal time for the density equations; `H` in the transfer-rate definition | `idenpr.tex:66-75` |
| `density_factor` | `rho_de` | `idenpr.tex:71-75` |
| `coupling_variable` | `beta(a)` / `beta(z)` | `idenpr.tex:72-79` |
| `coupling_dimension` | dimensionless | `idenpr.tex:75` |
| `time_dependence` | binned/piecewise in scale factor; also discussed as redshift history | `idenpr.tex:77-83`, `idenpr.tex:137-138` |
| `early_boundary_condition` | `beta(a)=0` at `a<a_1`, with `a_1=0.0001` | `idenpr.tex:83` |
| `Q_mu_defined` | yes | `idenpr.tex:97` |
| `Q_mu_direction` | parallel to CDM/dark-matter four-velocity | `idenpr.tex:97` |
| `momentum_transfer_frame` | DM frame; momentum transfer rate vanishes in the dark-matter rest frame | `idenpr.tex:97` |
| `perturbation_route` | dark-energy perturbation handled with ePPF | `idenpr.tex:97` |
| `stability_route` | ePPF is used to avoid possible large-scale instability in standard linear perturbation theory | `idenpr.tex:97` |
| `ePPF_mapping` | for the `beta(a)` model, `C_1=D_2=Q` and `C_2=C_3=D_1=0` | `idenpr.tex:97` |
| `solver_route` | IDECAMB implementation in CAMB; sampling through Cobaya/PolyChord | `idenpr.tex:137-138` |
| `product_boundary` | source contains paper text and figures, but not machine-readable `beta(z)`, covariance, posterior chains, or PCA arrays | asset README |

## Translation Hazards

- `beta(a)` multiplies `rho_de`, not QFUDS `rho_A`.
- The local QFUDS retained convention uses `Q = Hc Gamma(a) rho_A`.
- Positive early-time `beta(z)` is interpreted in the source as CDM-to-DE
  transfer, while late-time negative `beta(z)` reverses the flow.
- The source uses a sign-changing reconstructed coupling; retained `Gamma(a)`
  is not a signed sign-reversal model.
- ePPF is a stability prescription for this IDE implementation. It is not a
  QFUDS physical source derivation.

## Stop Status

```text
continue_to_perturbation_extract
```

Reason: the cached source gives background `Q`, `Q_mu`/frame, and ePPF route.
The extraction is still not enough for QFUDS physical admission, timing fitting,
or observational-constraint use.
