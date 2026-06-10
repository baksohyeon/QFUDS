---
doc_id: qfuds_success_criteria
title: QFUDS Success Criteria
doc_type: guide
stage: reference
status: reference
evidence_role: reference
depends_on:
  - qfuds_project_identity
  - qfuds_positioning
  - experiment_summary
  - roadmap
next_gate: use these criteria before choosing phenomenology, new branch, or stop
last_updated: 2026-06-09
---

# QFUDS Success Criteria

## Purpose

This guide defines what success means for QFUDS at different strengths. It is not
the roadmap and does not set current level status. Current status lives in
[docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md).

The criteria separate three outcomes:

1. a reproducible design-space exploration;
2. a useful phenomenological interacting-vacuum model;
3. a physical DM-to-DE phase-transition theory.

## Minimum Success

Definition:

QFUDS reaches minimum success if it becomes a reproducible, falsification-first
research program that turns the original intuition into explicit model classes,
tests, failures, evidence records, and future admission rules.

Evidence already achieved:

- the LCDM null limit is implemented and tested;
- constant and ungated growth-driven transfer laws were rejected at tested
  amplitudes;
- experiment 002 was preserved as provenance after stronger audits;
- [Level 1.5](../wiki/glossary/repository_levels.md) closed the retained physical branch without erasing it;
- Level 2A recorded the boundary of a phenomenological perturbation closure;
- documentation now preserves roadmap, decision, evidence, and traceability
  records.

Missing requirements:

- none required to claim minimum success as a design-space audit;
- future work should keep the success criteria explicit so status and value do
  not get confused.

Roadmap implications:

- minimum success does not authorize physical Level 2B;
- it supports a decision to continue, pause, or stop from a clearer evidence
  position.

## Moderate Success

Definition:

QFUDS reaches moderate success if the retained or future phenomenological track
becomes a useful constrained interacting-vacuum or interacting-dark-energy model
that can be tested observationally without being described as physical QFUDS.

Evidence already achieved:

- the retained `Gamma(a)` shape is constrained by a source-like timing proxy;
- the P1 interacting-vacuum perturbation closure is numerically stable under the
  declared Level 2A audit;
- P2 regularized phase-B fluid behavior failed at the retained amplitude;
- the closest known model class is now explicit.

Missing requirements:

- comparison against standard interacting-vacuum and interacting-dark-energy
  parameterizations;
- broader parameter studies;
- perturbation tests that cover known IDE instability modes;
- eventual Boltzmann-code or equivalent observational comparison if the
  phenomenology remains worth testing.

Roadmap implications:

- future work may continue as phenomenology, but every result must stay labeled
  as phenomenological interacting-vacuum or interacting-dark-energy work;
- phenomenological success does not imply physical QFUDS success.

## Strong Success

Definition:

QFUDS reaches strong success only if a physical DM-to-DE phase-transition
mechanism is derived or otherwise fixed enough to distinguish QFUDS from known
cosmology model families.

Evidence already achieved:

- none for the retained branch as a physical derivation;
- the retained branch failed physical Level 1.5 promotion;
- the broader DM-to-DE phase-transition hypothesis remains open.

Missing requirements:

- a physical source `X`;
- a stress-energy transfer relation `Q^nu`;
- a reason phase B has `w ~= -1`;
- a perturbation route for `delta Q`;
- a distinction from LCDM, unified dark fluids, interacting dark energy,
  interacting vacuum, holographic dark energy, and remnant dark matter.

Roadmap implications:

- strong success requires a new admitted physical branch before physical Level
  2B can begin;
- Level 3+ physical claims require Level 2B-quality perturbation equations and
  solver-ready implementation.

## Future Physical Branch Admission

No new physical-QFUDS branch should be opened unless it provides, at minimum:

```text
X =
Q^nu =
why phase B has w ~= -1 =
delta Q route =
known-model distinction =
```

No equation -> no branch.

The admission rule is intentionally stricter than ordinary brainstorming. A new
idea may be recorded as provenance or speculation, but it should not become a
physical branch until it creates at least one equation, falsifiable observable,
changed viability decision, or reproducible experiment plan.

## How To Use These Criteria

Before starting new work, classify it as one of three tracks:

1. **design-space documentation**: improves clarity, traceability, or failure
   boundaries;
2. **phenomenology**: tests a declared model without physical-QFUDS claims;
3. **physical branch**: supplies the admission-rule ingredients before Level 2B.

If a proposed task does not fit one of those tracks, it should remain a note or
be rejected as premature.
