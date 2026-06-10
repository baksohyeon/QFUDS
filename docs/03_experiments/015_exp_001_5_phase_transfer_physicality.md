---
doc_id: exp_001_5_phase_transfer_physicality
title: "Experiment 001.5: Phase Transfer Physicality Gate"
doc_type: experiment
stage: "1.5"
status: completed
evidence_role: audit
depends_on:
  - exp_002_entropy_information_gate
  - result_002_entropy_information_gate
  - qfuds_level_1_5_transfer_four_vector_derivation_attempt
next_gate: retained branch demoted; no physical Level 2B without a new admitted physical branch
last_updated: 2026-06-09
---

# Experiment 001.5: Phase Transfer Physicality Gate

Date: 2026-06-08

## Objective

Audit whether the retained collapse/information-production transfer shape has a
physical phase-transfer interpretation before any physical perturbation claim is
made.

This is a [Level 1.5](../wiki/glossary/repository_levels.md) gate document. It is not a numerical perturbation
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

This hypothesis must not be promoted to physical Level 2B unless the missing
physical inputs are fixed or the branch is explicitly demoted to a
phenomenological interacting-vacuum model.

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

## Outputs

This audit produces a classification result rather than a new numerical output
grid. Required evidence artifacts are:

- [docs/04_results/015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md);
- cited implementation evidence in `qfuds/gamma_laws.py` and `qfuds/growth.py`;
- roadmap and decision-log updates recording whether the branch remains physical
  QFUDS, is demoted to phenomenology, or is rejected.

## Result Document

The corresponding result is:

```text
docs/04_results/015_result_001_5_phase_transfer_physicality.md
```

## Decision

The retained collapse/information-production `Gamma(a)` branch fails physical
Level 1.5 promotion and is demoted to phenomenological interacting-vacuum
status. This does not falsify the broader DM-to-DE phase-transition hypothesis;
it rejects only the current retained source relation as a physical derivation.

Do not treat `exp_003` as physical QFUDS evidence. It may proceed only as a
Level 2A phenomenological closure audit. Do not open physical Level 2B for this
retained branch.

## Future-Branch Admission Rule

No new physical-QFUDS branch should be opened unless it provides, at minimum:

- `X =`
- `Q^nu =`
- `why phase B has w ~= -1 =`
- `delta Q route =`
- `known-model distinction =`
