---
doc_id: audit_2026_06_11_chen_figure5_numeric_digitization_execution_plan
title: "2026-06-11 Chen Figure 5 Numeric Digitization Execution Plan"
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
  - asset_chen_2026_merger_entropy_history_recovery_extract
  - asset_chen_2026_merger_entropy_budget
  - roadmap
next_gate: approved 046 numeric digitization only
last_updated: 2026-06-11
---

# 2026-06-11 Chen Figure 5 Numeric Digitization Execution Plan

## Purpose

This plan follows the
[2026-06-11 Numeric Digitization Planning Audit](044_numeric_digitization_planning_audit.md).

The `044` audit selected Chen Figure 5 as the first numeric digitization target.
This `045` document defines how a future `046` task should digitize that figure.

This document does not digitize the figure, extract numeric values, create a
CSV, create a structured product, modify asset files, or change roadmap status.

## Status Boundary

The current blocker remains:

```text
data_product_blocked
```

The lane remains `data_product_blocked` until a future `046` task creates and
validates a numeric product.

Roadmap status remains unchanged.

Physical-QFUDS Level 2B remains blocked.

`Gamma(a)` remains a prototype phenomenological transfer profile.

No `Q^nu` is derived here.

No `delta Q` is derived here.

No candidate `X` is created here.

No QFUDS support claim is made here.

## Authorities

Authority order:

1. [Black-Hole Data Product Audit](../conclusions/040_black_hole_data_product_audit.md)
2. [Product-Recovery Candidate Selection Plan](041_product_recovery_candidate_selection_plan.md)
3. [Product-Recovery Execution Plan](042_product_recovery_execution_plan.md)
4. [Product-Recovery Extraction Result](../conclusions/043_product_recovery_extraction_result.md)
5. [Numeric Digitization Planning Audit](044_numeric_digitization_planning_audit.md)

If these records conflict, earlier records in this list win.

Do not infer new requirements beyond this authority chain.

## Source Figure

Future `046` source image:

```text
docs/wiki/research/assets/chen_2026_merger_entropy_budget/figures/extracted/growth_entropy_gwtc4_only.png
```

Source support:
[Chen merger entropy history recovery extract](../../../assets/chen_2026_merger_entropy_budget/digitization/chen_2026_merger_entropy_history_recovery_extract.md).

Future `046` output path:

```text
docs/wiki/research/assets/chen_2026_merger_entropy_budget/digitization/chen_figure5_numeric_digitization.csv
```

This `045` plan names the future output path but does not create it.

## Target Curves

Future `046` must treat the blue and red curves as separate products.

| Curve | Quantity | Axis | Unit | Role |
| --- | --- | --- | --- | --- |
| blue central curve | `S_BH(a)` source-history candidate | left y-axis only | `k` | primary first recovery target |
| blue lower uncertainty band | lower uncertainty trace for `S_BH(a)` | left y-axis only | `k` | uncertainty boundary |
| blue upper uncertainty band | upper uncertainty trace for `S_BH(a)` | left y-axis only | `k` | uncertainty boundary |
| red central curve | entropy-density history candidate | right y-axis only | `k m^-3` | secondary separate curve |
| red lower uncertainty band | lower uncertainty trace for entropy density | right y-axis only | `k m^-3` | uncertainty boundary |
| red upper uncertainty band | upper uncertainty trace for entropy density | right y-axis only | `k m^-3` | uncertainty boundary |

Blue and red y-axis values must never be mixed.

## Axis Mapping Rules

Primary x-axis:
redshift `z` from the bottom axis of Figure 5.

Do not use the top lookback-time axis as the primary independent variable.

Future `046` must record the x-axis mapping method, including whether it uses
manual calibration points, a digitization tool calibration, or another recorded
image-coordinate mapping.

Derived columns:

```text
a = 1 / (1 + z)
ln_a = ln(a)
```

`ln_a` is optional only if the future CSV schema explicitly records why it was
omitted. If `ln_a` is present, it must be computed from `a`, not read from the
figure.

## Future 046 CSV Schema

Future `046` must create the CSV only if digitization is approved. The required
minimum columns are:

```text
row_id
curve_id
curve_color
quantity
value
value_unit
z
a
ln_a
x_axis_source
y_axis_side
band_role
pixel_x
pixel_y
source_image
source_location
extraction_method
quality_state
qfuds_role
provenance_note
limitations
```

Controlled `curve_id` values:

```text
chen_fig5_blue_entropy_central
chen_fig5_blue_entropy_lower
chen_fig5_blue_entropy_upper
chen_fig5_red_entropy_density_central
chen_fig5_red_entropy_density_lower
chen_fig5_red_entropy_density_upper
```

Controlled `curve_color` values:

```text
blue
red
```

Controlled `quantity` values:

```text
S_BH(a)
entropy_density(a)
```

Controlled `value_unit` values:

```text
k
k m^-3
```

Controlled `x_axis_source` value:

```text
Figure 5 bottom redshift axis
```

Controlled `y_axis_side` values:

```text
left
right
```

Controlled `band_role` values:

```text
central
lower_uncertainty
upper_uncertainty
```

Controlled `source_location` values:

```text
Figure 5 blue central curve
Figure 5 blue lower uncertainty band
Figure 5 blue upper uncertainty band
Figure 5 red central curve
Figure 5 red lower uncertainty band
Figure 5 red upper uncertainty band
```

`source_location` must be curve-level. A generic `Figure 5` value is
insufficient.

Controlled `quality_state` value:

```text
numeric_digitized
```

Allowed `qfuds_role` values:

```text
source-history candidate
normalization check
```

Do not use a `qfuds_role` that implies QFUDS support.

## Uncertainty Handling

Future `046` should digitize central, lower, and upper traces separately only
where the band is visually separable.

If uncertainty-band boundaries cannot be separated from central curves or from
overlapping plot elements, future `046` must record that limitation instead of
inventing lower or upper values.

Visible uncertainty bands do not provide covariance. The future CSV and any
accompanying note must record covariance as missing unless a later approved
source-code or posterior product is recovered.

## Manual Landmark Cross-Checks

Future `046` must compare the digitized output against the manual landmarks
already recorded in the `043` Chen extraction record.

Required cross-check records:

- `chen_2026_fig5_total_entropy_peak`;
- `chen_2026_fig5_entropy_density_peak_redshift_only`;
- `chen_2026_fig5_low_z_growth_power_law`;
- `chen_2026_fig5_intermediate_high_z_slopes`.

These landmarks are cross-checks only. This `045` plan does not restate their
values as new extraction output.

Future `046` must fail or mark the product limited if the digitized curve is
inconsistent with the applicable `043` landmark records and no source-level
reason explains the difference.

## Required Missing-Field Record

Future `046` must explicitly record these missing fields unless recovered from
an approved source:

- covariance;
- source-code reproduction route;
- entropy-to-energy conversion law;
- QFUDS normalization route;
- candidate `X` boundary.

Missing fields must not be estimated, inferred, or backfilled from QFUDS needs.

## Failure Criteria

Future `046` must fail the product or mark it unusable if:

- blue and red y-axes are mixed;
- `source_location` is not curve-level;
- the log redshift axis mapping cannot be calibrated;
- uncertainty bands cannot be separated from central curves but are recorded as
  if they were separated;
- extracted points lack `pixel_x`, `pixel_y`, `source_image`, or provenance;
- required unit, axis, curve identity, or limitation fields are missing;
- the output cannot be checked against the `043` manual landmark records;
- the output is used to claim `Q^nu`, `delta Q`, candidate `X`, QFUDS support,
  or Level 2B admission.

## Future 046 Validation Steps

Future `046` must, at minimum:

1. Confirm the source image path exists.
2. Record image dimensions and digitization tool or method.
3. Calibrate the bottom redshift axis and each y-axis separately.
4. Digitize blue and red central curves as separate curve IDs.
5. Digitize visible uncertainty-band boundaries only when separable.
6. Compute `a = 1 / (1 + z)` and optional `ln_a = ln(a)`.
7. Check the digitized output against the `043` manual landmark records.
8. Record all missing fields and limitations.
9. Run repository documentation validation after writing the future product.

## Final Decision

This `045` document authorizes no digitization by itself.

It only defines the execution requirements for a future approved `046` task.

The black-hole lane remains:

```text
data_product_blocked
```
