---
doc_id: audit_2026_06_11_chen_figure5_numeric_digitization_result
title: "2026-06-11 Chen Figure 5 Numeric Digitization Result"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_black_hole_data_product_audit
  - audit_2026_06_11_product_recovery_candidate_selection_plan
  - audit_2026_06_11_product_recovery_execution_plan
  - audit_2026_06_11_product_recovery_extraction_result
  - audit_2026_06_11_numeric_digitization_planning_audit
  - audit_2026_06_11_chen_figure5_numeric_digitization_execution_plan
  - audit_2026_06_11_numeric_digitization_execution_plan
  - asset_chen_2026_figure5_numeric_digitization_provenance
  - roadmap
next_gate: judge whether a separate product-state audit is needed before any physical use
last_updated: 2026-06-11
---

# 2026-06-11 Chen Figure 5 Numeric Digitization Result

## Purpose

This document closes out the `046` Chen Figure 5 numeric digitization execution
for the Source-X chain.

The digitized asset products remain under the paper-level asset directory:

- [Chen Figure 5 numeric digitization CSV](../../../assets/chen_2026_merger_entropy_budget/digitization/chen_figure5_numeric_digitization.csv)
- [Chen Figure 5 numeric digitization provenance](../../../assets/chen_2026_merger_entropy_budget/digitization/chen_figure5_numeric_digitization_provenance.md)

Those files are asset-level products. This file is the Source-X conclusion
record that states what the digitization changed and what remains blocked.

## Status Boundary

The Chen Figure 5 asset now has a `numeric_digitized` source-history candidate.

The black-hole lane remains `data_product_blocked`, not physics_blocked.

`qfuds_usable_numeric_product` does not exist.

Candidate `X` boundary is missing.

No `Q^nu` is derived here.

No `delta Q` is derived here.

No Physical-QFUDS Level 2B branch is opened here.

Roadmap status is unchanged.

No QFUDS support claim is made here.

## Result Summary

| Item | Result |
| --- | --- |
| Source image | `docs/wiki/research/assets/chen_2026_merger_entropy_budget/figures/extracted/growth_entropy_gwtc4_only.png` |
| Output CSV | [chen_figure5_numeric_digitization.csv](../../../assets/chen_2026_merger_entropy_budget/digitization/chen_figure5_numeric_digitization.csv) |
| Provenance note | [chen_figure5_numeric_digitization_provenance.md](../../../assets/chen_2026_merger_entropy_budget/digitization/chen_figure5_numeric_digitization_provenance.md) |
| Method | color-segmented PNG digitization with manual axis calibration |
| Rows | 432 |
| Quality state | `numeric_digitized` |
| QFUDS role | `source-history candidate` |

Recovered curve groups:

| Curve group | Quantity | Axis | Unit | Rows |
| --- | --- | --- | --- | ---: |
| `chen_fig5_blue_entropy_central` | `S_BH(a)` | left y-axis | `k` | 72 |
| `chen_fig5_blue_entropy_lower` | `S_BH(a)` | left y-axis | `k` | 72 |
| `chen_fig5_blue_entropy_upper` | `S_BH(a)` | left y-axis | `k` | 72 |
| `chen_fig5_red_entropy_density_central` | `entropy_density(a)` | right y-axis | `k m^-3` | 72 |
| `chen_fig5_red_entropy_density_lower` | `entropy_density(a)` | right y-axis | `k m^-3` | 72 |
| `chen_fig5_red_entropy_density_upper` | `entropy_density(a)` | right y-axis | `k m^-3` | 72 |

## Calibration Decision

The digitization used the bottom redshift axis as the primary x-axis. The top
lookback-time axis was not used as the primary independent variable.

The blue curve was calibrated only against the left y-axis.

The red curve was calibrated only against the right y-axis.

The CSV records `z`, `a = 1 / (1 + z)`, `ln_a`, pixel coordinates,
curve-level `source_location`, and provenance notes for every row.

## Landmark Checks

The digitized blue central curve is consistent with the `043` manual landmark
within visual digitization limits:

| Check | `043` manual landmark | Digitized CSV check | Decision |
| --- | --- | --- | --- |
| blue `S_BH(a)` peak | approximately `z = 4.55`, `S = 1.43e90 k` | approximately `z = 4.32`, `S = 1.51e90 k` | usable as visual digitization |
| red entropy-density peak redshift | approximately `z = 2.79`; value missing in `043` | approximately `z = 2.54`; value digitized from right y-axis | limited because no source-text scalar value exists |

The digitization does not fit new power laws and does not recover covariance.

## Missing Fields

Still missing:

- covariance;
- source-code reproduction route;
- entropy-to-energy conversion law;
- QFUDS normalization route;
- candidate `X` boundary;
- `dS_BH / dln(a)` product;
- physical mapping from entropy history to a QFUDS source term.

Uncertainty-band rows are visible band-edge digitizations only. They are not a
posterior product and must not be treated as covariance.

## Product-State Decision

The asset product state has advanced from:

```text
manual_structured_extract
```

to:

```text
numeric_digitized
```

for Chen Figure 5 only.

The Source-X physical-admission state has not advanced.

The digitization is useful as a source-history candidate and comparator. It is
not a QFUDS-usable physical source product because it lacks candidate `X`,
normalization, entropy-to-energy conversion, covariance, and a `Q^nu` or
`delta Q` route.

## Final Decision

The `046` digitization is valid as a numeric asset product.

It is not QFUDS evidence.

It is not a physical derivation.

It is not a Level 2B admission result.

The black-hole lane remains:

```text
data_product_blocked
```
