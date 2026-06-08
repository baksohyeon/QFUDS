---
doc_id: exp_001_5_phase_transfer_physicality
title: "Experiment 001.5: Phase Transfer Physicality Gate"
doc_type: experiment
stage: "1.5"
status: in_progress
evidence_role: audit
depends_on:
  - exp_002_entropy_information_gate
  - result_002_entropy_information_gate
next_gate: do not create exp_003 until this gate is resolved
last_updated: 2026-06-08
---

# Experiment 001.5: Phase Transfer Physicality Gate

Date: 2026-06-08

## Objective

Audit whether the retained collapse/information-production transfer shape has a
physical phase-transfer interpretation before any perturbation experiment is
created.

This is a Level 1.5 gate document. It is not a numerical perturbation
experiment.

## Trigger

Experiment 002 retained the shape:

```math
\Gamma(a) \propto {dF_{\rm coll}(>M,a)\over d\ln a}.
```

The later audit found that experiment 002 was run before these prerequisites
were defined:

- physical phase-transfer mechanism;
- fixed mass threshold `M`;
- self-consistent QFUDS growth source;
- transfer perturbation prescription.

Therefore experiment 002 is retained as provenance, not physical evidence.

## Hypothesis Under Audit

The most conservative hypothesis is:

```text
Gamma(a) is an effective coarse-grained phase-conversion rate whose shape is
motivated by nonlinear collapse or information production.
```

This hypothesis must not be promoted to Level 2 unless the missing physical
inputs are fixed or the branch is explicitly demoted to a phenomenological
interacting-vacuum model.

## Scope

This gate evaluates interpretation, parameter classification, and
self-consistency.

It does not implement:

- `delta_A`, `theta_A`, `delta_B`, or `theta_B`;
- transfer perturbations;
- CLASS/CAMB;
- CMB spectra;
- matter power;
- survey likelihoods.

## Failure Criteria

The retained branch fails or is demoted if:

- `Gamma(a)` remains only a useful fitted shape;
- `gamma0` remains an unconstrained efficiency;
- `M` remains an implicit `collapse_a` tuning knob;
- `F_coll` cannot be computed from QFUDS growth;
- the branch is indistinguishable from known interacting vacuum models;
- entropy or information language is used without a stress-energy derivation.

## Result Document

The corresponding result is:

```text
docs/04_results/015_result_001_5_phase_transfer_physicality.md
```

## Decision

Remain at QFUDS v0.15 / Level 1.5.

Do not create `exp_003` until this gate is resolved.
