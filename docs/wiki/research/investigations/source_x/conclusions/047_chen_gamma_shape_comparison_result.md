---
doc_id: audit_2026_06_11_chen_gamma_shape_comparison_result
title: "2026-06-11 Chen-Gamma Shape Comparison Result"
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
  - audit_2026_06_11_chen_figure5_numeric_digitization_result
  - audit_2026_06_11_chen_gamma_shape_comparison_plan
  - asset_chen_2026_figure5_numeric_digitization_provenance
  - roadmap
next_gate: no physical use; product remains data_product_blocked unless candidate X and physical-admission items are supplied later
last_updated: 2026-06-11
---

# 2026-06-11 Chen-Gamma Shape Comparison Result

## Purpose

This document closes out the approved `047` Chen-Gamma shape comparison audit
defined by the
[Chen-Gamma Shape Comparison Plan](../plans/047_chen_gamma_shape_comparison_plan.md).

The comparison is qualitative only. It checks timing-shape features of the
digitized Chen Figure 5 products against the retained repository
phenomenological `Gamma(a)` profile.

This result does not fit a curve.

This result does not derive `Q^nu`.

This result does not derive `delta Q`.

This result does not define candidate `X`.

This result does not claim QFUDS support.

This result does not modify roadmap status.

This result does not open Physical-QFUDS Level 2B.

## Status Boundary

The Chen Figure 5 asset has a `numeric_digitized` source-history candidate.

The black-hole lane remains `data_product_blocked`.

No physical source is admitted.

`Gamma(a)` remains a prototype phenomenological transfer profile.

The roadmap remains unchanged.

Physical-QFUDS Level 2B remains blocked.

Shape resemblance, where present, is recorded only as a timing-shape
observation. It is not physical evidence for QFUDS.

## Inputs

Chen digitization input:

- [chen_figure5_numeric_digitization.csv](../../../assets/chen_2026_merger_entropy_budget/digitization/chen_figure5_numeric_digitization.csv)
- [chen_figure5_numeric_digitization_provenance.md](../../../assets/chen_2026_merger_entropy_budget/digitization/chen_figure5_numeric_digitization_provenance.md)

Gamma implementation and retained context:

- [qfuds/gamma_laws.py](../../../../../../qfuds/gamma_laws.py)
- [QFUDS Level 2A Phenomenological Perturbations](../../../../../../docs/02_theory/030_qfuds_phenomenological_perturbations.md)
- [Experiment 003 phenomenological perturbation closure](../../../../../../docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md)

Gamma source and parameters used:

| Field | Value |
| --- | --- |
| implementation | `qfuds.gamma_laws.gamma_information_production` |
| model label | retained `information_production` phenomenological profile |
| `gamma0` | `0.02` |
| `collapse_a` | `0.35` |
| `collapse_nu` | `5.0` |
| cosmology parameters | repository default `CosmologyParams` |
| status | prototype phenomenological transfer profile only |

No Chen parameter was tuned to `Gamma(a)`.

No `Gamma(a)` parameter was tuned to Chen Figure 5.

## Compared Curve Groups

Actually compared:

| Curve group | Quantity | Use in this result |
| --- | --- | --- |
| `chen_fig5_blue_entropy_central` | `S_BH(a)` | primary Chen shape candidate |
| `chen_fig5_red_entropy_density_central` | `entropy_density(a)` | secondary comparator |

Used only as robustness context:

| Curve group | Quantity | Use in this result |
| --- | --- | --- |
| `chen_fig5_blue_entropy_lower` | `S_BH(a)` lower band | visual robustness bound only |
| `chen_fig5_blue_entropy_upper` | `S_BH(a)` upper band | visual robustness bound only |
| `chen_fig5_red_entropy_density_lower` | entropy-density lower band | visual robustness bound only |
| `chen_fig5_red_entropy_density_upper` | entropy-density upper band | visual robustness bound only |

Uncertainty bands were not treated as covariance.

The blue left-axis entropy product and red right-axis entropy-density product
were kept separate.

## Transformations And Normalization

The comparison used the CSV columns `z`, `a`, `ln_a`, `value`, `curve_id`, and
`band_role`.

The digitized CSV already records:

```text
a = 1 / (1 + z)
ln_a = ln(a)
```

Shape comparison used max-normalization over the overlapping digitized support.
The normalization is dimensionless and only supports qualitative timing-shape
inspection. It is not a QFUDS normalization.

No area normalization was used.

No extrapolation was used.

Overlapping support:

| Coordinate | Range |
| --- | --- |
| `a` | `0.04997111` to `0.98979209` |
| `z` | `19.01156449` to `0.01031319` |
| `ln_a` | `-2.99631033` to `-0.01026037` |

## Qualitative Shape Checks

Only the metrics authorized by the `047` plan were evaluated.

| Metric | Chen blue `S_BH(a)` | Chen red `entropy_density(a)` | retained `Gamma(a)` | Decision |
| --- | --- | --- | --- | --- |
| turn-on epoch | 10% level near `a = 0.09033044`, `z = 10.07046553` | 10% level near `a = 0.10931147`, `z = 8.14817055` | 10% level near `a = 0.13170352`, `z = 6.59281173` | Chen turns on earlier than `Gamma(a)` |
| peak location | peak near `a = 0.18810772`, `z = 4.31610301` | peak near `a = 0.26139591`, `z = 2.82561461` | peak near `a = 0.32717157`, `z = 2.05650028` | red is closer than blue, but both peak earlier than `Gamma(a)` |
| peak width | half-maximum support near `a = 0.12005740` to `0.28235312` | half-maximum support near `a = 0.15786948` to `0.40052325` | half-maximum support near `a = 0.18810772` to `0.78435406` | `Gamma(a)` is broader and extends later |
| saturation behavior | normalized late-time tail near `2.65e-7` at largest `a` | normalized late-time tail near `3.17e-2` at largest `a` | normalized late-time tail near `3.58e-1` at largest `a` | late-time behavior mismatches, especially for blue entropy |
| monotonicity | rises and falls once | rises and falls once | rises and falls once | qualitative similarity only |
| sign changes | no value-sign change observed | no value-sign change observed | no value-sign change observed | qualitative similarity only |
| qualitative similarity | single-peaked, nonnegative timing profile | single-peaked, nonnegative timing profile; closer peak timing than blue | single-peaked, nonnegative timing profile | shape class similarity exists |
| qualitative mismatch | earlier, narrower, no comparable late tail | earlier and narrower, with smaller late tail | later, broader, stronger late tail | timing and saturation mismatch remain |

## Interpretation Boundary

The comparison finds a limited qualitative resemblance: all compared central
profiles are nonnegative, single-peaked timing profiles over the digitized
support.

The comparison also finds material mismatch:

- Chen blue `S_BH(a)` peaks too early and is much narrower than the retained
  `Gamma(a)` profile.
- Chen red entropy density is the closer timing comparator, but still peaks
  earlier and falls off faster than `Gamma(a)`.
- The retained `Gamma(a)` profile has a broader late-time tail than either Chen
  central curve.

This is not a physical match claim.

This is not a source-term derivation.

This is not evidence that entropy history generates the retained `Gamma(a)`.

## Missing Fields

Still missing:

- entropy-to-energy conversion;
- covariance;
- source-code reproduction route for Chen Figure 5;
- QFUDS normalization;
- candidate `X`;
- `Q^nu`;
- `delta Q`;
- physical mapping from entropy history to a QFUDS source term;
- known-model distinction for any proposed physical branch.

The uncertainty bands are visual digitization bounds only. They are not
covariance and were not used for statistical confidence claims.

## Source-X Decision

The `047` comparison changes no Source-X admission decision.

It records that Chen red entropy density is the closer qualitative timing
comparator than Chen blue total entropy, but neither curve supplies the missing
physical-admission items.

The current state remains:

```text
data_product_blocked
```

The result is usable only as a qualitative comparator record for future audit
planning.

## Final Decision

`047` executes the approved qualitative shape comparison.

The comparison is valid as a bounded Source-X audit result.

The comparison does not create a QFUDS-usable physical source.

Roadmap status remains unchanged.

Physical-QFUDS Level 2B remains blocked.
