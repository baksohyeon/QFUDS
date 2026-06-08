---
doc_id: project_status_entrypoint
title: QFUDS Project Overview
doc_type: overview
stage: "1.5"
status: in_progress
evidence_role: ssot
depends_on:
  - project_overview
  - roadmap
next_gate: keep Level 2B blocked; no CMB or matter-power claims
last_updated: 2026-06-08
---

# QFUDS Project Overview

Date: 2026-06-08

This is the project-level overview entry point requested by the documentation plan.

The maintained detailed overview is `docs/00_project/overview.md`. This file keeps the top-level status in one place and points to the canonical supporting documents.

## Project Goals

QFUDS asks whether dark matter and dark energy can be modeled as two effective macroscopic phases of one underlying quantum-spacetime foam sector.

The goal is not to prove QFUDS correct. The goal is to determine whether each version survives progressively stronger tests or must be rejected, narrowed, or classified as a known model.

## Current Status

```text
Level 0: literature position                    completed
Level 1: background toy model                   completed
QFUDS v0.15 / Level 1.5: phase transfer physicality    in progress
Level 2A: phenomenological perturbation closure completed
Level 2B: physical perturbation equations       blocked
Level 3: CLASS/CAMB integration                 blocked
Level 4: CMB comparison                         blocked
Level 5: matter power comparison                blocked
Level 6: DESI/Euclid/Roman constraints          blocked
```

The project remains at QFUDS v0.15 / Level 1.5 for physical interpretation.
The surviving `Gamma(a) proportional to dF_coll/dln(a)` branch is not yet a
derived physical phase-transfer law. A separate Level 2A phenomenological
perturbation-closure audit may proceed.

Level 1 contains three completed background validations:

```text
exp_000: zero-transfer LCDM baseline
exp_001: Gamma-law background scan
exp_002: entropy / information-source gate
```

## Known Limitations

- No microphysical foam action has been derived.
- The phase split remains phenomenological.
- The surviving transfer law has passed only background-level checks and is
  currently classified as phenomenological.
- The `dF_coll/dln(a)` source still depends on LCDM-style growth approximations.
- No tested transfer perturbation model exists.
- No CLASS/CAMB implementation exists.
- No CMB, matter-power, or survey-likelihood comparison exists.
- Background-level growth proxies are not matter-power predictions.

## Roadmap

The maintained roadmap is `docs/05_next_steps/000_roadmap.md`.

The required order is:

```text
literature position
-> background toy model
-> background transfer-law filters
-> Level 1.5 phase-transfer physicality gate for physical claims
-> Level 2A phenomenological perturbation closure
-> Level 2B physical perturbation closure
-> CLASS/CAMB integration
-> CMB comparison
-> matter power comparison
-> survey constraints
```

## Model Genealogy

```text
v0.1
  Conceptual unified-foam hypothesis.
  White-hole-universe image rejected as the central testable claim.

v0.2
  Minimal two-phase effective dark sector.
  Gamma = 0 gives the LCDM limit.
  Free Gamma(a) reduces to interacting dark energy.

qfuds_v0_3 / exp_001
  Background Gamma-law scan.
  Constant and ungated growth-driven transfer fail.
  Low-redshift proxies survive only as candidate shapes for later scrutiny.
  Later audit inserts QFUDS v0.15 / Level 1.5 before physical perturbation claims.

exp_002
  Entropy/information-source background gate.
  Broad entropy language mostly fails or reduces to known model classes.
  Demoted to provenance because it was run before the physical transfer
  mechanism, fixed mass threshold, and self-consistent QFUDS growth source were
  defined.
  Press-Schechter information production is retained only as the narrow Level
  1.5 question.

QFUDS v0.15 / Level 1.5
  Phase-transfer physicality gate.
  Current verdict: Gamma(a) is a phenomenological coarse-grained transfer law
  with a physically motivated source shape, not a derived microscopic law.

Level 2A next
  Phenomenological perturbation equations for phase A, phase B, and transfer perturbations.
  Physical Level 2B remains blocked.
```

## Primary Documents

- `PROJECT.md`: documentation control and validation order.
- `AGENTS.md`: agent constitution and research rules.
- `docs/00_project/overview.md`: detailed project overview.
- `docs/00_project/decision_log.md`: chronological decisions.
- `docs/00_project/verification_guide.md`: how to rerun and read current checks.
- `docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md`: QFUDS v0.15 / Level 1.5 audit.
- `docs/02_theory/040_qfuds_phenomenological_perturbations.md`: Level 2A closure audit.
- `docs/05_next_steps/000_roadmap.md`: current levels and blockers.
