---
doc_id: exp_005_timing_prior_usefulness
title: "Experiment 005: Timing-Prior Usefulness and Redundancy Audit"
doc_type: experiment
stage: "2"
status: completed
evidence_role: audit
depends_on:
  - result_004_p1_model_family_positioning
  - qfuds_positioning
  - qfuds_success_criteria
next_gate: use retained timing only as IV/IDE timing-prior compression target unless stronger evidence appears
last_updated: 2026-06-09
---

# Experiment 005: Timing-Prior Usefulness and Redundancy Audit

Date: 2026-06-09

## Objective

Test whether the retained structure-era `Gamma(a)` shape is scientifically
useful as a timing prior inside interacting-vacuum or interacting-dark-energy
phenomenology.

The question is not whether the retained profile is physically correct. The
question is:

```text
Can the retained structure-timed coupling history provide a useful
low-dimensional timing prior between rigid coupling families and flexible
tomographic or nonparametric reconstruction?
```

## Hypothesis

The retained timing profile may be useful if it compresses a flexible
structure-era transfer history into a small number of interpretable timing
features:

- peak redshift;
- width in `ln(a)`;
- half-max support;
- skew;
- early leakage;
- late tail.

This hypothesis is phenomenological only. It does not reopen Level 1.5 and does
not assert a physical source for `Gamma(a)`.

## Scope

This experiment compares normalized timing shapes only. It may establish:

- whether retained timing is too rigid, redundant, or useful as a compression
  target;
- whether standard compact timing families reproduce the retained shape;
- whether flexible binned or reconstruction-style families reproduce the shape;
- whether the retained profile preserves low early leakage and interpretable
  support.

It does not establish:

- a physical QFUDS source;
- a new `Q^nu`;
- physical Level 2B readiness;
- CMB, matter-power, BAO, supernova, DESI, Euclid, Roman, or likelihood
  viability;
- novelty of QFUDS as a physical theory.

## Method

Use the retained `information_production` branch with the existing retained
parameters:

```text
gamma_model = information_production
gamma0 = 0.02
collapse_a = 0.35
collapse_nu = 5.0
```

Normalize every timing family to `max(shape)=1`. Do not compare amplitudes.

Compare retained timing against:

- constant coupling;
- power-law coupling;
- cumulative logistic transition;
- logistic transition-rate pulse;
- Gaussian pulse in `ln(a)`;
- three-bin tomographic approximation;
- five-bin tomographic approximation;
- eight-knot piecewise-linear reconstruction proxy.

## Diagnostics

Report:

- normalized shape RMS error over retained support;
- normalized shape max error over retained support;
- parameter count;
- peak redshift;
- weighted mean redshift, computed from weighted mean `ln(a)`;
- half-max support;
- width in `ln(a)`;
- skew in `ln(a)`;
- `z > 1100` leakage fraction;
- `z > 10` leakage fraction;
- `z < 1` and `z < 0.5` fractions.

Approximate timing equivalence requires:

```text
shape RMS error <= 0.05
shape max error <= 0.15
```

## Failure Criteria

The experiment fails if:

1. amplitudes are compared instead of timing shape;
2. a timing prior is described as a physical source;
3. compact, tomographic, and reconstruction families are mixed without
   separating parameter count;
4. retained timing is described as novel when a standard timing family matches
   it;
5. the result implies roadmap or Level 1.5 status changes.

If these occur, the correct classification is `unresolved`.

## Outputs

Execution command:

```bash
python3 scripts/run_minimal_model.py --exp-005-timing-prior-audit --outdir outputs
```

Required outputs:

```text
outputs/exp005_timing_prior_summary.json
outputs/exp005_timing_family_comparison.csv
outputs/exp005_timing_fingerprint.csv
outputs/exp005_timing_prior_criteria.csv
outputs/figures/exp005_timing_family_shapes.png
outputs/figures/exp005_timing_family_shapes.svg
outputs/figures/exp005_timing_family_errors.png
outputs/figures/exp005_timing_family_errors.svg
```

Code paths:

```text
scripts/run_minimal_model.py
qfuds/timing_prior.py
qfuds/background.py
qfuds/gamma_laws.py
```

## Decision

Allowed classifications:

| Classification | Meaning |
| --- | --- |
| `redundant_as_unique_shape_but_useful_as_interpretable_prior` | A compact standard family matches the profile; retained timing is not unique but may still be a named prior. |
| `potentially_useful_compression_target` | Flexible timing reconstructions match better than compact families; retained timing may be useful if future reconstructions prefer similar support. |
| `not_supported_as_timing_prior` | Neither compact nor flexible families match well enough to justify retaining the timing prior. |
| `unresolved` | Diagnostics are insufficient or violate scope. |

The decision must remain phenomenological. It must not update roadmap status or
physical-QFUDS claims.
