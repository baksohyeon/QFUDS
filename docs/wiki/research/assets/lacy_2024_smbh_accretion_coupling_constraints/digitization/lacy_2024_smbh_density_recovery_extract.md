---
doc_id: asset_lacy_2024_smbh_density_recovery_extract
title: Lacy 2024 SMBH Density Recovery Extract
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_black_hole_data_product_audit
  - audit_2026_06_11_product_recovery_candidate_selection_plan
  - audit_2026_06_11_product_recovery_execution_plan
  - asset_lacy_2024_smbh_accretion_coupling_constraints
next_gate: no derivation; remains data_product_blocked unless candidate X and missing fields are supplied later
last_updated: 2026-06-17
---

# Lacy 2024 SMBH Density Recovery Extract

## Boundary

This is the Lane A `043` manual structured extraction from the Lacy 2024 asset
chain selected by `041` and scoped by `042`.

Recovered target:

```text
rho_BH(a)
d rho_BH / dln(a)
```

No `Q^nu` is derived here.

No `delta Q` is derived here.

No candidate `X` is derived here.

No Physical-QFUDS Level 2B branch is opened here.

No roadmap status is modified here.

No QFUDS support claim is made here.

This extract records source-history and comparator products only. It does not
turn Lacy 2024 into QFUDS-ready evidence.

## Source Files Inspected

| Source type | Source file | Inspection status |
| --- | --- | --- |
| Source PDF | [paper_arxiv_2312.12344.pdf](../source/paper_arxiv_2312.12344.pdf) | File present; direct PDF text extraction unavailable in this environment. |
| [PageIndex](https://github.com/VectifyAI/PageIndex) Markdown | [paper_arxiv_2312.12344.md](paper_arxiv_2312.12344.md) | Used for page, section, equation, figure, and caption locations. |
| TeX source | [AGN_BHgrowth.tex](../source/extracted/AGN_BHgrowth.tex) | Used to verify equation labels, figure labels, and selected density units. |
| Figure 1 PNG | [scenario1_revised.png](../figures/extracted/scenario1_revised.png) | Inspected as source figure path; not digitized. |
| Figure 2 PNG | [Salpeter_plot_revised.png](../figures/extracted/Salpeter_plot_revised.png) | Inspected as source figure path; not digitized. |

## Extraction Method

Quality state:
`manual_structured_extract`.

Extraction method:
manual extraction from [PageIndex](https://github.com/VectifyAI/PageIndex) Markdown and TeX source, with source figure
paths recorded but no pixel-level digitization.

No figure values were digitized. Figure entries below record recoverable source
structure and provenance only.

## Structured Extract

| product_id | quantity | value | value_unit | z | a | ln_a | source_location | extraction_method | quality_state | qfuds_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `lacy_2024_gd07_local_smbh_density_range` | `rho_BH(a)` | `4.4e5 to 5.9e5` | `M_sun Mpc^-3` | `0` | `1` | `0` | Page 3, Section 3.1; TeX `sec:bhdensity`, GD07 local SMBH density discussion | manual text/table-value extraction | `manual_structured_extract` | normalization check |
| `lacy_2024_kormendy_ho_thanjavur_local_smbh_density` | `rho_BH(a)` | `1.0e6` | `M_sun Mpc^-3` | `0` | `1` | `0` | Page 3, Section 3.1; TeX `sec:bhdensity`, Thanjavur spheroid mass function plus Kormendy-Ho relation | manual text extraction | `manual_structured_extract` | normalization check |
| `lacy_2024_adopted_local_smbh_density_range_with_unit_conflict` | `rho_BH(a)` | `3e5 to 1.6e6`; log range `6.0 +0.2 -0.5` | inconsistent: surrounding density convention is `M_sun Mpc^-3`, but extracted text/TeX range uses `Mpc^-1` | `0` | `1` | `0` | Page 4, Section 3.1; TeX `sec:bhdensity`, adopted range after systematic discussion | manual text extraction with unit conflict recorded | `manual_structured_extract` | normalization check |
| `lacy_2024_gwb_based_local_smbh_density` | `rho_BH(a)` | `7.4e6` | `M_sun Mpc^-3` | `0` | `1` | `0` | Page 4, Section 3.1; TeX `sec:bhdensity`, GWB posterior discussion | manual text extraction | `manual_structured_extract` | comparator |
| `lacy_2024_generalized_soltan_density_integral` | `rho_BH(a)` | equation structure only; no numeric curve extracted | equation-level density convention | `z` as integration endpoint; Figure 1 application uses `z=6` to `z=0` | `a = 1 / (1 + z)`; coverage `0.142857 to 1` for the Figure 1 application | `ln_a = -1.946 to 0` for the Figure 1 application | Page 3, Equation 9; TeX `eqn:generalSoltan`; Page 4-5 text and Figure 1 caption | manual equation-structure extraction | `manual_structured_extract` | source-history candidate |
| `lacy_2024_figure1_accretion_history_curve_target` | `rho_BH(a)` | not digitized | missing for curve values | Figure 1 application integrates `z=6` to `z=0` | coverage `0.142857 to 1` | coverage `-1.946 to 0` | Page 5, Figure 1 caption; TeX `fig:scenario1`; file `figures/extracted/scenario1_revised.png` | figure provenance extraction only | `manual_structured_extract` | source-history candidate |
| `lacy_2024_figure2_high_z_constraint_target` | `d rho_BH / dln(a)` | not digitized | missing for curve/region values | high-redshift constraint around `z=4` | approximately `0.2` | approximately `-1.609` | Page 6, Figure 2 caption; TeX `fig:salpeter`; file `figures/extracted/Salpeter_plot_revised.png` | figure provenance extraction only | `manual_structured_extract` | comparator |

## Field-Level Checks

| product_id | units | redshift coverage | uncertainty route | normalization route | provenance | candidate X boundary |
| --- | --- | --- | --- | --- | --- | --- |
| `lacy_2024_gd07_local_smbh_density_range` | verified in [PageIndex](https://github.com/VectifyAI/PageIndex) and TeX as `M_sun Mpc^-3`; source PDF not directly text-checked | local only, `z=0` | literature compilation range only; no covariance | GD07 adjusted to common `H0 = 70 km s^-1 Mpc^-1` | [PageIndex](https://github.com/VectifyAI/PageIndex) page 3 and TeX `sec:bhdensity` | missing |
| `lacy_2024_kormendy_ho_thanjavur_local_smbh_density` | verified in [PageIndex](https://github.com/VectifyAI/PageIndex) and TeX as `M_sun Mpc^-3`; source PDF not directly text-checked | local only, `z=0` | systematic discussion but no covariance | Thanjavur spheroid mass function plus Kormendy-Ho relation | [PageIndex](https://github.com/VectifyAI/PageIndex) page 3 and TeX `sec:bhdensity` | missing |
| `lacy_2024_adopted_local_smbh_density_range_with_unit_conflict` | inconsistent; do not reuse numerically until source PDF check resolves `Mpc^-1` vs `Mpc^-3` | local only, `z=0` | asymmetric log range and systematic discussion | adopted local density range based on bulge relation discussion | [PageIndex](https://github.com/VectifyAI/PageIndex) page 4 and TeX `sec:bhdensity` | missing |
| `lacy_2024_gwb_based_local_smbh_density` | verified in [PageIndex](https://github.com/VectifyAI/PageIndex) and TeX as `M_sun Mpc^-3`; source PDF not directly text-checked | local only, `z=0` | `95 percent` posterior range `2e6 to 1400e6`; average about `1e8` | GWB posterior assumptions from Agazie et al. as reported by Lacy 2024 | [PageIndex](https://github.com/VectifyAI/PageIndex) page 4 and TeX `sec:bhdensity` | missing |
| `lacy_2024_generalized_soltan_density_integral` | equation-level density convention only | equation endpoint is redshift; Figure 1 application uses `z=6` to `z=0` | depends on AGN luminosity density, `eta`, `lambda`, and local density assumptions; no covariance product recovered | source cosmology `H0 = 70`, `Omega_M = 0.3`, `Omega_Lambda = 0.7`; Shen et al. global fit B luminosity function | [PageIndex](https://github.com/VectifyAI/PageIndex) page 3, Equation 9; TeX `eqn:generalSoltan`; [PageIndex](https://github.com/VectifyAI/PageIndex) page 5 Figure 1 caption | missing |
| `lacy_2024_figure1_accretion_history_curve_target` | missing for curve values because no digitization was performed | figure application covers `z=6` to `z=0` | shaded Shen et al. luminosity-function uncertainty is described; no numeric uncertainty extracted | Shen et al. luminosity function, fixed `eta=0.1` and `eta=0.3`, and local density comparators | [PageIndex](https://github.com/VectifyAI/PageIndex) page 5 Figure 1 caption; TeX `fig:scenario1`; PNG path recorded | missing |
| `lacy_2024_figure2_high_z_constraint_target` | missing for figure-region values because no digitization was performed | high-redshift constraint around `z=4` only, not a full history | parameter-space exclusions from `eta`, `lambda`, and Salpeter time; no numeric region digitized | GD07, Lacy adopted density, and GWB density panels | [PageIndex](https://github.com/VectifyAI/PageIndex) page 6 Figure 2 caption; TeX `fig:salpeter`; PNG path recorded | missing |

## Lane A Outcome

Lane A recovers local SMBH density normalization records and a source-history
equation/figure route for `rho_BH(a)`. It does not recover a standalone
machine-readable `rho_BH(a)` curve, does not recover `d rho_BH / dln(a)`, and
does not supply a candidate `X` boundary.

Units are partly verified. The main local density values have TeX/[PageIndex](https://github.com/VectifyAI/PageIndex)
support for `M_sun Mpc^-3`, but the adopted log-range text carries a recorded
`Mpc^-1` inconsistency and requires source-PDF resolution before numerical
reuse.

Uncertainty route is partial. Local density ranges and GWB posterior ranges are
recorded, but no covariance or reusable posterior product is recovered.

Normalization route is partial. Source cosmology, local-density normalization
routes, and Shen et al. luminosity-function dependence are recorded, but no
QFUDS normalization route exists.

Redshift coverage is partial. Local density products are `z=0` only. Equation 9
and Figure 1 provide a source-history route over `z=6` to `z=0`, but no curve
values were digitized.

Candidate `X` boundary:
missing.

Lane status:
`data_product_blocked`.
