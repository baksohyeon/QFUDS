---
doc_id: asset_chen_2026_figure5_numeric_digitization_provenance
title: Chen 2026 Figure 5 Numeric Digitization Provenance
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_11_chen_figure5_numeric_digitization_execution_plan
  - asset_chen_2026_merger_entropy_history_recovery_extract
  - asset_chen_2026_merger_entropy_budget
next_gate: Source-X result closeout before any physical use
last_updated: 2026-06-11
---

# Chen 2026 Figure 5 Numeric Digitization Provenance

## Boundary

This note documents the `046` numeric digitization of Chen Figure 5:

- [chen_figure5_numeric_digitization.csv](chen_figure5_numeric_digitization.csv)
- [growth_entropy_gwtc4_only.png](../figures/extracted/growth_entropy_gwtc4_only.png)

This is a `numeric_digitized` source-history candidate product only.

It does not derive `Q^nu`.

It does not derive `delta Q`.

It does not define candidate `X`.

It does not open Physical-QFUDS Level 2B.

It does not modify roadmap status.

It does not claim QFUDS support.

## Method

The CSV was generated from the cached Figure 5 PNG using color-segmented PNG
digitization with manual axis calibration.

Recovered curve groups:

| Curve group | Quantity | Axis | Unit | Rows |
| --- | --- | --- | --- | ---: |
| `chen_fig5_blue_entropy_central` | `S_BH(a)` | left y-axis | `k` | 72 |
| `chen_fig5_blue_entropy_lower` | `S_BH(a)` | left y-axis | `k` | 72 |
| `chen_fig5_blue_entropy_upper` | `S_BH(a)` | left y-axis | `k` | 72 |
| `chen_fig5_red_entropy_density_central` | `entropy_density(a)` | right y-axis | `k m^-3` | 72 |
| `chen_fig5_red_entropy_density_lower` | `entropy_density(a)` | right y-axis | `k m^-3` | 72 |
| `chen_fig5_red_entropy_density_upper` | `entropy_density(a)` | right y-axis | `k m^-3` | 72 |

Blue and red curves were calibrated against separate y-axes. They must not be
merged or compared as the same quantity.

## Calibration

Image dimensions:

```text
2036 x 1764 px
```

The bottom redshift axis is the primary x-axis. The top lookback-time axis was
not used as the primary independent variable.

Axis calibration:

| Axis | Calibration |
| --- | --- |
| x-axis | logarithmic redshift axis; `x = 279 px` at `z = 0.01`; `448 px` per decade |
| blue left y-axis | `y = 177 px` at `10^91 k`; `y = 1559 px` at `10^83 k` |
| red right y-axis | `y = 260 px` at `10^13 k m^-3`; `y = 1411 px` at `10^7 k m^-3` |

For each row, `a` was computed from:

```text
a = 1 / (1 + z)
```

`ln_a` was computed from:

```text
ln_a = ln(a)
```

## Landmark Checks

The digitized blue central curve peaks near the Figure 5 manual landmark
recorded in the `043` extract:

| Check | `043` manual landmark | Digitized CSV check | Status |
| --- | --- | --- | --- |
| blue `S_BH(a)` peak | approximately `z = 4.55`, `S = 1.43e90 k` | approximately `z = 4.32`, `S = 1.51e90 k` | consistent within visual digitization limits |
| red entropy-density peak redshift | approximately `z = 2.79`; value missing in `043` | approximately `z = 2.54`; value digitized from right y-axis | limited; no source-text scalar value exists |

The low-redshift power-law and intermediate/high-redshift slope statements from
`043` remain qualitative cross-checks. This digitization does not fit new power
laws.

## Missing Fields

The CSV records these missing fields in the `limitations` column:

- covariance;
- source-code reproduction route;
- entropy-to-energy conversion law;
- QFUDS normalization route;
- candidate `X` boundary.

Uncertainty-band rows are visible band-edge digitizations. They are not
posterior covariance, and they do not define a reusable statistical model.

## Product State

This output advances the Chen Figure 5 asset state to:

```text
numeric_digitized
```

It does not advance the Source-X physical-admission state.

The black-hole lane remains:

```text
data_product_blocked
```
