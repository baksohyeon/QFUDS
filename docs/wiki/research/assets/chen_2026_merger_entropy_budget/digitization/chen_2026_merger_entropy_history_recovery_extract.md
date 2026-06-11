---
doc_id: asset_chen_2026_merger_entropy_history_recovery_extract
title: Chen 2026 Merger Entropy History Recovery Extract
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_black_hole_data_product_audit
  - audit_2026_06_11_product_recovery_candidate_selection_plan
  - audit_2026_06_11_product_recovery_execution_plan
  - asset_chen_2026_merger_entropy_budget
next_gate: no derivation; remains data_product_blocked unless candidate X and missing fields are supplied later
last_updated: 2026-06-11
---

# Chen 2026 Merger Entropy History Recovery Extract

## Boundary

This is the Lane B `043` manual structured extraction from the Chen, Jani, and
Kephart 2026 asset chain selected by `041` and scoped by `042`.

Recovered target:

```text
S_BH(a)
dS_BH / dln(a)
```

No `Q^nu` is derived here.

No `delta Q` is derived here.

No candidate `X` is derived here.

No entropy-to-energy conversion law is introduced here.

No Physical-QFUDS Level 2B branch is opened here.

No roadmap status is modified here.

No QFUDS support claim is made here.

This extract records merger-entropy source-history and comparator products only.
It does not turn Chen 2026 into QFUDS-ready evidence.

## Source Files Inspected

| Source type | Source file | Inspection status |
| --- | --- | --- |
| Source PDF | [paper_arxiv_2601.13621.pdf](../source/paper_arxiv_2601.13621.pdf) | File present; direct PDF text extraction unavailable in this environment. |
| PageIndex Markdown | [paper_arxiv_2601.13621.md](paper_arxiv_2601.13621.md) | Used for page, table, equation, figure, and caption locations. |
| TeX source | [sample631.tex](../source/extracted/sample631.tex) | Used to verify table row, equation labels, source conventions, and figure source paths. |
| Figure 5 PNG | [growth_entropy_gwtc4_only.png](../figures/extracted/growth_entropy_gwtc4_only.png) | Inspected as source figure path; not digitized. |
| Figure 6 PNG | [cumulative_ent_den_gwtc4_only.png](../figures/extracted/cumulative_ent_den_gwtc4_only.png) | Inspected as source figure path; not digitized. |
| Figure 7 PNG | [cumulative_tot_ent_gwtc4_pbh.png](../figures/extracted/cumulative_tot_ent_gwtc4_pbh.png) | Inspected as source figure path; not digitized. |

## Extraction Method

Quality state:
`manual_structured_extract`.

Extraction method:
manual extraction from PageIndex Markdown and TeX source, with source figure
paths recorded but no pixel-level digitization.

No figure values were digitized. Figure entries below record values only when
they are stated in the PageIndex Markdown or TeX source text.

## Structured Extract

| product_id | quantity | value | value_unit | z | a | ln_a | source_location | extraction_method | quality_state | qfuds_role |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `chen_2026_table1_bbh_merger_delta_s_entropy_density` | `S_BH(a)` | `7.1e12` | `k m^-3` | present inventory; redshift not specified | missing | missing | Page 5, Table 1, row `BBH mergers Delta S`; TeX `tab:budget` row | manual table extraction from PageIndex and TeX | `manual_structured_extract` | normalization check |
| `chen_2026_table1_bbh_merger_delta_s_entropy` | `S_BH(a)` | `1.1e93` | `k` | present inventory; redshift not specified | missing | missing | Page 5, Table 1, row `BBH mergers Delta S`; TeX `tab:budget` row | manual table extraction from PageIndex and TeX | `manual_structured_extract` | normalization check |
| `chen_2026_fig5_total_entropy_peak` | `S_BH(a)` | `1.43e90` | `k` | approximately `4.55` | approximately `0.180` | approximately `-1.714` | Page 8, Figure 5 text and caption; file `figures/extracted/growth_entropy_gwtc4_only.png` | manual figure-text extraction | `manual_structured_extract` | source-history candidate |
| `chen_2026_fig5_entropy_density_peak_redshift_only` | `S_BH(a)` | missing | `k m^-3` expected for entropy density, value not stated in text | approximately `2.79` | approximately `0.264` | approximately `-1.333` | Page 8, Figure 5 text and caption; file `figures/extracted/growth_entropy_gwtc4_only.png` | manual figure-text extraction | `manual_structured_extract` | source-history candidate |
| `chen_2026_fig5_low_z_growth_power_law` | `S_BH(a)` | `S_growth = 1.46e88 * z^2.37` | `k` | `z <= 0.5` | `a >= 0.667` | `ln_a >= -0.405` | Page 8, Figure 5 text; Figure 5 caption | manual figure-text extraction | `manual_structured_extract` | source-history candidate |
| `chen_2026_fig5_intermediate_high_z_slopes` | `S_BH(a)` | `S proportional to z^3.07` before peak; `S proportional to z^-4.82` beyond peak | proportionality only | approximately `0.5 < z < 4.5`, then beyond peak | not tabulated | not tabulated | Page 8, Figure 5 text; Figure 5 caption | manual figure-text extraction | `manual_structured_extract` | source-history candidate |
| `chen_2026_fig6_cmb_crossover_redshift` | `S_BH(a)` | crossover event; no scalar entropy value stated | redshift event, not entropy unit | `12.6` | approximately `0.0735` | approximately `-2.610` | Page 9-10, Section 4.1, Figure 6 caption; file `figures/extracted/cumulative_ent_den_gwtc4_only.png` | manual figure-text extraction | `manual_structured_extract` | comparator |
| `chen_2026_fig6_pbh_stellar_crossover_redshift` | `S_BH(a)` | crossover event; no scalar entropy value stated | redshift event, not entropy unit | `9.17` | approximately `0.0983` | approximately `-2.319` | Page 10, Figure 6 text and caption; file `figures/extracted/cumulative_ent_den_gwtc4_only.png` | manual figure-text extraction | `manual_structured_extract` | comparator |
| `chen_2026_fig7_retrospective_entropy_density_peak` | `S_BH(a)` | `4.17e12` | `k m^-3` | `4.33` | approximately `0.188` | approximately `-1.673` | Page 11-12, Equation 16 and Figure 7 text/caption; file `figures/extracted/cumulative_tot_ent_gwtc4_pbh.png` | manual figure-text extraction | `manual_structured_extract` | source-history candidate |
| `chen_2026_eq16_retrospective_entropy_density_definition` | `S_BH(a)` | equation structure only; no new numeric extraction | density definition | integration over `z in [0.01,20]` per Figure 7 caption | coverage `0.0476 to 0.990` | coverage `-3.045 to -0.010` | Page 11, Equation 16; Page 12 Figure 7 caption | manual equation-structure extraction | `manual_structured_extract` | source-history candidate |

## Field-Level Checks

| product_id | units | redshift coverage | uncertainty route | normalization route | provenance | candidate X boundary |
| --- | --- | --- | --- | --- | --- | --- |
| `chen_2026_table1_bbh_merger_delta_s_entropy_density` | verified against PageIndex and TeX as `k m^-3`; source PDF not directly text-checked | present inventory only; no redshift | `-3.5e12`, `+9.2e12` from Table 1 | entropy density computed by dividing by `V_obs`; TeX records `V_obs = 3.52e80 m^3` with uncertainty | PageIndex page 5 Table 1; TeX `tab:budget` | missing |
| `chen_2026_table1_bbh_merger_delta_s_entropy` | verified against PageIndex and TeX as `k`; source PDF not directly text-checked | present inventory only; no redshift | `-0.6e93`, `+1.5e93` from Table 1 | observable-universe entropy inventory | PageIndex page 5 Table 1; TeX `tab:budget` | missing |
| `chen_2026_fig5_total_entropy_peak` | source text states `k` | Figure 5 covers `z in [0.01,20]`; this row is peak at `z ~= 4.55` | `-0.71e90`, `+1.91e90` stated in Figure 5 text | merger-generated entropy in comoving frame; population/model convention not fully reusable without source code | PageIndex page 8 Figure 5 text/caption; PNG path recorded | missing |
| `chen_2026_fig5_entropy_density_peak_redshift_only` | unit available as entropy density, value missing | Figure 5 covers `z in [0.01,20]`; peak redshift only at `z ~= 2.79` | missing for value because value is not stated in text | merger-generated entropy density in comoving frame | PageIndex page 8 Figure 5 text/caption; PNG path recorded | missing |
| `chen_2026_fig5_low_z_growth_power_law` | source text states `k` for `S_growth` | low-redshift approximation only, `z <= 0.5` | missing | source fit from Figure 5 discussion; no covariance or residuals | PageIndex page 8 Figure 5 text | missing |
| `chen_2026_fig5_intermediate_high_z_slopes` | proportionality only; normalized values missing | intermediate and high-redshift regimes around the Figure 5 peak | missing | Figure 5 slope description only | PageIndex page 8 Figure 5 text | missing |
| `chen_2026_fig6_cmb_crossover_redshift` | not an entropy scalar | crossover redshift `12.6`; Figure 6 covers `z in [0.01,20]` | `-3.5`, `+1.5` in redshift | cumulative entropy compared with CMB photon entropy | PageIndex page 9-10 Section 4.1 and Figure 6 caption | missing |
| `chen_2026_fig6_pbh_stellar_crossover_redshift` | not an entropy scalar | crossover redshift `9.17`; Figure 6 covers `z in [0.01,20]` | `-1.01`, `+1.31` in redshift | PBH fraction comparator, not a QFUDS route | PageIndex page 10 Figure 6 text/caption | missing |
| `chen_2026_fig7_retrospective_entropy_density_peak` | source text states `k m^-3` | peak at `z=4.33`; Figure 7 integrates over `z in [0.01,20]` | `-2.00e12`, `+5.35e12` | retrospective entropy density normalized by comoving volume | PageIndex page 11-12 Equation 16 and Figure 7 text/caption | missing |
| `chen_2026_eq16_retrospective_entropy_density_definition` | equation-level density definition only | integration over `z in [0.01,20]` | missing | cumulative entropy divided by enclosed comoving volume | PageIndex page 11 Equation 16 and PageIndex page 12 Figure 7 caption | missing |

## Lane B Outcome

Lane B recovers present-inventory entropy values, redshift-history landmarks,
source power-law/proportionality structure, and retrospective entropy-density
structure for merger-generated black-hole entropy.

It does not recover a standalone machine-readable `S_BH(a)` curve, does not
recover `dS_BH / dln(a)`, and does not supply a candidate `X` boundary.

Units are partly verified. Table 1 entropy and entropy-density rows match
PageIndex and TeX source. Source-PDF direct text checking was unavailable in
this environment.

Uncertainty route is partial. Table 1 uncertainties, peak/crossover redshift
uncertainties, and selected figure-text uncertainties are recorded. No
standalone covariance, posterior product, or reproducible code route is
recovered here.

Normalization route is partial. Observable-universe entropy inventory,
comoving-frame merger entropy, and retrospective entropy-density conventions are
recorded. No entropy-to-energy conversion law or QFUDS normalization route
exists.

Redshift coverage is partial. Figure 5-7 records cover `z in [0.01,20]` where
stated, but some extracted rows are present inventory, peak-only, crossover-only,
or proportionality-only records.

Candidate `X` boundary:
missing.

Lane status:
`data_product_blocked`.
