---
doc_id: retained_branch_source_closure_plan_provenance
title: Retained Branch Source Closure Plan Provenance
doc_type: gate
stage: "1.5"
status: provenance
evidence_role: provenance
depends_on:
  - level_1_5_resolution_gate
  - result_001_5_phase_transfer_physicality
  - result_003_phenomenological_perturbation_closure
  - exp003_record_consistency_gate
next_gate: no retained-branch source-closure experiment; future physical branches must pass the admission rule
last_updated: 2026-06-09
---

# Retained Branch Source Closure Plan Provenance

Date: 2026-06-09

This gate previously turned the Level 1.5 blocker into a possible next research
step. It did not start physical Level 2B, change project status, or treat
`Gamma(a)` as derived physics.

Outcome: the retained branch has now been demoted, so this planning gate is
provenance rather than an active plan. Current status remains in
[000_roadmap.md](000_roadmap.md). The Level 1.5 pass/fail criteria remain in
[015_level_1_5_resolution_gate.md](015_level_1_5_resolution_gate.md).

## Question

Can the retained collapse/information-production shape

```math
\Gamma(a) \propto {dF_{\rm coll}(>M,a)\over d\ln a}
```

be promoted from a phenomenological interacting-vacuum transfer shape to a
physically justified phase-transfer model?

## Superseded Recommended Artifact

The next experiment was considered but is not opened for the retained branch.

Superseded experiment name:

```text
exp_004_phase_transfer_source_closure
```

Superseded future experiment document:

```text
docs/03_experiments/030_exp_004_phase_transfer_source_closure.md
```

Superseded future result document:

```text
docs/04_results/030_result_004_phase_transfer_source_closure.md
```

Do not create this experiment/result pair for the retained branch. The branch
failed physical Level 1.5 promotion before the experiment was opened.

## Hypothesis To Test

The only hypothesis worth testing next is narrow:

```text
The transfer source can be written as a fixed coarse-grained conservation law
or stress-energy exchange relation, where nonlinear collapse or information
production defines a real source scalar and not only a timing function.
```

This hypothesis is allowed to use collapse or information language only if it
assigns that language a mathematical role in the transfer model.

## Minimum Inputs Before Any Future Physical Branch

Before any future physical-QFUDS source-closure branch can be opened, the
repository needs all of the following:

1. A candidate transfer equation, for example a stress-energy exchange term
   `Q^\nu` or a coarse-grained conservation law, stating what phase A loses and
   what phase B gains.
2. A source scalar `X(a)` or `X[a, fields]` with units and normalization stated.
   `X = dF_coll/dln(a)` is allowed only if the physical threshold is explicit.
3. Replacement of implicit `collapse_a` with a fixed mass threshold `M`, or a
   documented decision that no physical threshold is currently available.
4. Classification of `gamma0` as derived, externally fixed, independently
   bounded, fitted, or phenomenological.
5. A non-circular source-computation plan explaining how `Gamma(a)` depends on
   growth while growth depends on `Gamma(a)`.
6. A perturbation-readiness sketch: transfer frame, gauge assumptions, `delta Q`,
   and phase-A/phase-B response.
7. A known-model comparison against LCDM, unified dark fluid, and interacting
   vacuum.

## PASS

Level 1.5 can pass only if a future physical branch produces evidence that satisfies
[015_level_1_5_resolution_gate.md](015_level_1_5_resolution_gate.md) and the
result can honestly state:

```text
The retained transfer law is fixed enough to define physical Level 2B
perturbation equations without adding new assumptions there.
```

That requires a fixed source, fixed or bounded parameters, a perturbation-ready
transfer prescription, and a distinct falsifiable relation. A good-looking
background curve is not a pass.

## FAIL

The branch should be rejected as physical QFUDS if the proposed source equation
is mathematically inconsistent, violates the stated density/energy conditions,
cannot define a transfer perturbation, or reduces to a label with no
stress-energy role.

A failed branch should remain in the record as provenance.

## DEMOTION

The branch should be explicitly demoted to phenomenological interacting vacuum
if any of these remain true after the audit:

- `Gamma(a)` is still a selected or fitted source shape.
- `collapse_a` remains the operational threshold.
- `dF_coll/dln(a)` still imports LCDM growth while claiming QFUDS
  self-consistency.
- `gamma0` remains an unconstrained efficiency.
- The construction is equivalent to interacting vacuum without a new fixed
  source relation or observable.
- collapse, information, entropy, foam, or black-hole language has no
  mathematical role in `Q^\nu`, `X(a)`, or the stress-energy accounting.

Demotion would leave Level 2B blocked. A phenomenological continuation may
still be useful, but it must not be called physical QFUDS.

## Future-Branch Admission Rule

No new physical-QFUDS branch should be opened unless it provides, at minimum:

- `X =`
- `Q^nu =`
- `why phase B has w ~= -1 =`
- `delta Q route =`
- `known-model distinction =`

## Required Artifacts After A Real Future Source-Closure Experiment

If a future source-closure experiment is executed, completion requires:

- theory assumptions or derivation update;
- experiment document with predeclared failure criteria;
- code path or analytic derivation;
- output artifacts or derivation record;
- result document;
- [decision_log.md](../00_project/decision_log.md) entry;
- [000_experiment_summary.md](../04_results/000_experiment_summary.md) row;
- [000_roadmap.md](000_roadmap.md) update;
- [traceability_matrix.md](../00_project/traceability_matrix.md) update.

Do not update those decision documents before the evidence changes.
