---
doc_id: roadmap
title: QFUDS Research Roadmap
doc_type: roadmap
stage: "1.5"
status: in_progress
evidence_role: ssot
depends_on:
  - result_001_5_phase_transfer_physicality
next_gate: resolve Level 1.5 before Level 2
last_updated: 2026-06-08
---

# QFUDS Research Roadmap

Date: 2026-06-08

## Status Key

- `completed`: implemented or documented at the current required level.
- `in progress`: partially implemented or drafted, but not sufficient for the next validation gate.
- `blocked`: cannot proceed responsibly until an upstream assumption or implementation is defined.

## Levels

| Level | Topic | Status | Current Evidence | Next Gate |
| --- | --- | --- | --- | --- |
| 0 | literature position | completed | `docs/02_theory/900_qfuds_research_report.md` | Keep comparison current as model changes |
| 1 | background validation | completed | `docs/04_results/000_result_000_lcdm_baseline.md`, `docs/04_results/010_result_001_gamma_scan.md`, `docs/04_results/020_result_002_entropy_information_gate.md`, `outputs/`, `tests/test_gamma_v03.py` | Treat experiment 002 as provenance; audit only the retained collapse/information-production shape |
| 1.5 | phase transfer physicality | in progress | `docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md`, `docs/04_results/015_result_001_5_phase_transfer_physicality.md`, `docs/04_results/020_result_002_entropy_information_gate.md`, `qfuds/gamma_laws.py` | Decide whether `Gamma(a)` is derived physics or only a phenomenological interacting-vacuum law |
| 2 | perturbation equations | blocked | assumptions noted in `qfuds/growth.py` and theory docs | Requires Level 1.5 closure first |
| 3 | CLASS integration | blocked | none | Requires Level 2 equations |
| 4 | CMB comparison | blocked | none | Requires CLASS/CAMB implementation |
| 5 | matter power spectrum | blocked | growth proxy only | Requires perturbation solver or Boltzmann output |
| 6 | DESI/Euclid comparison | blocked | no likelihood pipeline | Requires validated background plus perturbation predictions |

## Immediate Work

1. Complete QFUDS v0.15 / Level 1.5 in `docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md`.
2. Decide whether the surviving branch is a physical phase-transfer hypothesis or only a phenomenological transfer law.
3. Replace the implicit `collapse_a` threshold with an explicit physical mass threshold `M`, or document why that cannot yet be done.
4. Recompute `dF_coll/dln a` using self-consistent QFUDS growth only after the required growth ingredients exist.
5. Follow `docs/05_next_steps/010_perturbation_gate.md` only after the Level 1.5 gate is satisfied.
6. Kill or demote the branch if it remains ordinary interacting vacuum with a tuned source shape.

Do not create `exp_003` as a perturbation experiment until Level 1.5 is resolved.

## Completed Background Validations

| Experiment | Purpose | Result |
| --- | --- | --- |
| `exp_000` | zero-transfer LCDM baseline | control passed; not novel |
| `exp_001` | Gamma-law background scan | constant and ungated growth-driven laws rejected |
| `exp_002` | entropy/information-source gate | demoted to provenance; retained shape goes to Level 1.5 audit, not evidence |

## Blockers

1. `Gamma(a)` is not derived from microphysics.
2. The surviving `dF_coll/dln a` source currently uses LCDM growth approximations.
3. No fixed physical collapse mass threshold `M`.
4. No perturbation closure relation.
5. No Boltzmann-code interface.
6. No likelihood comparison against CMB, BAO, SN, or matter power data.

## Rule For New Ideas

New speculative mechanisms should not be added to the main model unless they produce at least one of:

1. a new equation;
2. a new falsifiable observable;
3. a changed viability decision;
4. a reproducible experiment with code and outputs.
