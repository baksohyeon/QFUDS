---
doc_id: audit_2026_06_11_chen_gamma_shape_comparison_plan
title: "2026-06-11 Chen-Gamma Shape Comparison Plan"
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
  - asset_chen_2026_figure5_numeric_digitization_provenance
  - roadmap
next_gate: approved 047 shape comparison execution only
last_updated: 2026-06-11
---

# 2026-06-11 Chen-Gamma Shape Comparison Plan

## Purpose

This plan follows the
[Research Investigation Result Routing Workflow](../../../../../.agent/workflows/research-investigation-result-routing-workflow.md)
and the Source-X investigation routing conventions.

The purpose is to determine how a future audit should compare the shape of the
digitized Chen Figure 5 entropy-history products against the current retained
phenomenological `Gamma(a)` profile.

This is a planning audit only.

Do not perform the comparison.

Do not fit any curve.

Do not derive `Q^nu`.

Do not derive `delta Q`.

Do not define candidate `X`.

Do not claim QFUDS support.

Do not modify roadmap status.

Do not open Physical-QFUDS Level 2B.

## Status Boundary

The current lane remains `data_product_blocked`.

Numeric digitization exists for Chen Figure 5.

No physical source is admitted.

`Gamma(a)` remains a prototype phenomenological transfer profile.

Roadmap status remains unchanged.

Physical-QFUDS Level 2B remains blocked.

The future comparison may only ask whether timing shapes are qualitatively
similar or mismatched. It must not convert shape resemblance into physical
support.

## Authorities

Authority order:

1. [Black-Hole Data Product Audit](../conclusions/040_black_hole_data_product_audit.md)
2. [Product-Recovery Candidate Selection Plan](041_product_recovery_candidate_selection_plan.md)
3. [Product-Recovery Execution Plan](042_product_recovery_execution_plan.md)
4. [Product-Recovery Extraction Result](../conclusions/043_product_recovery_extraction_result.md)
5. [Numeric Digitization Planning Audit](044_numeric_digitization_planning_audit.md)
6. [Chen Figure 5 Numeric Digitization Execution Plan](045_chen_figure5_numeric_digitization_execution_plan.md)
7. [Numeric Digitization Execution Plan](046_numeric_digitization_execution_plan.md)
8. [Chen Figure 5 Numeric Digitization Result](../conclusions/046_chen_figure5_numeric_digitization_result.md)
9. [Chen Figure 5 numeric digitization provenance](../../../assets/chen_2026_merger_entropy_budget/digitization/chen_figure5_numeric_digitization_provenance.md)

If these records conflict, earlier records in this list win.

Do not infer new requirements beyond this authority chain.

## Inputs For A Future Comparison

Chen digitization input:

```text
docs/wiki/research/assets/chen_2026_merger_entropy_budget/digitization/chen_figure5_numeric_digitization.csv
```

Gamma implementation source:

- [qfuds/gamma_laws.py](../../../../../../qfuds/gamma_laws.py)
- [QFUDS Level 2A Phenomenological Perturbations](../../../../../../docs/02_theory/030_qfuds_phenomenological_perturbations.md)
- [Experiment 003 phenomenological perturbation closure](../../../../../../docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md)

The future audit must treat the retained `Gamma(a)` profile as an already
implemented phenomenological timing profile, not as a derived physical source.

## Eligible Chen Products

Eligible for future shape comparison:

| Curve group | Quantity | Use |
| --- | --- | --- |
| `chen_fig5_blue_entropy_central` | `S_BH(a)` | primary Chen shape candidate |
| `chen_fig5_blue_entropy_lower` | `S_BH(a)` uncertainty lower band | robustness bound only |
| `chen_fig5_blue_entropy_upper` | `S_BH(a)` uncertainty upper band | robustness bound only |
| `chen_fig5_red_entropy_density_central` | `entropy_density(a)` | secondary comparator |
| `chen_fig5_red_entropy_density_lower` | entropy-density uncertainty lower band | robustness bound only |
| `chen_fig5_red_entropy_density_upper` | entropy-density uncertainty upper band | robustness bound only |

Uncertainty bands must not be treated as covariance.

The future audit must keep the blue left-axis product and red right-axis product
separate. It must not merge entropy and entropy density into one curve.

## Required Transformations

Use the existing CSV columns:

```text
z
a
ln_a
value
value_unit
curve_id
band_role
```

If `a` or `ln_a` are recomputed, enforce:

```text
a = 1 / (1 + z)
ln_a = ln(a)
```

Allowed shape normalization:

- max-normalization over the overlapping support;
- area-normalization over the overlapping support;
- no normalization if the future audit only compares feature locations.

The selected normalization must be recorded in the future result. Normalization
is only for dimensionless shape comparison. It must not be used as a physical
amplitude calibration or QFUDS normalization.

Scale alignment:

- compare only over overlapping `a` or `ln_a` support;
- record the support range used;
- do not extrapolate Chen curves beyond their digitized support;
- do not extrapolate `Gamma(a)` to force overlap.

## Gamma(a) Target

The future audit may use the current repository phenomenological Gamma profile
implemented in [qfuds/gamma_laws.py](../../../../../../qfuds/gamma_laws.py).

The retained context is the Level 2A/Exp003 phenomenological transfer profile.
The future audit should name the exact model and parameters it uses, including
whether the profile is the retained `information_production` configuration from
the Level 2A/Exp003 context.

Forbidden:

- tuning Chen data to `Gamma(a)`;
- tuning `Gamma(a)` to Chen data;
- fitting a new Gamma family;
- treating `Gamma(a)` as a physical law.

## Permitted Shape Checks

Evaluate only:

- turn-on epoch;
- peak location;
- peak width;
- saturation behavior;
- monotonicity;
- sign changes;
- qualitative similarity;
- qualitative mismatch.

These checks are qualitative timing-shape checks. They do not establish a
source term, transfer law, or physical mechanism.

## Forbidden Shape Checks

Do not perform or claim:

- parameter fitting;
- physical interpretation;
- causal claims;
- candidate `X` claims;
- `Q^nu` claims;
- `delta Q` claims;
- QFUDS support claims;
- Level 2B admission claims.

Do not compute a best-fit coupling, amplitude, efficiency, entropy-to-energy
conversion, or transfer normalization.

## Future Result Document

After a future approved execution, create:

```text
docs/wiki/research/investigations/source_x/conclusions/047_chen_gamma_shape_comparison_result.md
```

That result must follow the
[Research Investigation Result Routing Workflow](../../../../../.agent/workflows/research-investigation-result-routing-workflow.md).

The result must report:

- which Chen curve groups were actually compared;
- which `Gamma(a)` source and parameters were used;
- transformation and normalization choices;
- overlapping support range;
- qualitative match or mismatch for each permitted metric;
- missing fields, especially entropy-to-energy conversion, covariance, QFUDS
  normalization, candidate `X`, `Q^nu`, and `delta Q`;
- whether the comparison changes the Source-X decision.

The required status boundary for the result is:

```text
data_product_blocked
```

unless a later authority explicitly supplies the missing physical-admission
items. A shape comparison alone cannot do that.

## Failure Criteria

The future audit must fail or mark the comparison unusable if:

- blue entropy and red entropy density are mixed;
- uncertainty bands are treated as covariance;
- Chen curves are extrapolated beyond digitized support;
- `Gamma(a)` is tuned to improve agreement;
- parameter fitting is performed;
- a qualitative resemblance is reported as physical support;
- candidate `X`, `Q^nu`, `delta Q`, or Level 2B admission is claimed.

## Final Decision

This plan authorizes no comparison by itself.

It only defines the execution requirements for a future approved shape
comparison audit.

The black-hole lane remains:

```text
data_product_blocked
```
