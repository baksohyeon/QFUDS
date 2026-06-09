---
doc_id: roadmap
title: QFUDS Research Roadmap
doc_type: roadmap
stage: "1.5"
status: in_progress
evidence_role: ssot
depends_on:
  - result_001_5_phase_transfer_physicality
next_gate: keep Level 2B blocked; classify P1 continuation as phenomenological interacting vacuum
last_updated: 2026-06-09
---

# QFUDS Research Roadmap

Date: 2026-06-09

## Status Key

- `completed`: implemented or documented at the current required level.
- `in progress`: partially implemented or drafted, but not sufficient for the next validation gate.
- `blocked`: cannot proceed responsibly until an upstream assumption or implementation is defined.

## Levels

| Level | Topic | Status | Current Evidence | Next Gate |
| --- | --- | --- | --- | --- |
| 0 | literature position | completed | [docs/02_theory/900_qfuds_research_report.md](../02_theory/900_qfuds_research_report.md) | Keep comparison current as model changes |
| 1 | background validation | completed | [docs/04_results/000_result_000_lcdm_baseline.md](../04_results/000_result_000_lcdm_baseline.md), [docs/04_results/010_result_001_gamma_scan.md](../04_results/010_result_001_gamma_scan.md), [docs/04_results/020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md), `outputs/`, `tests/test_gamma_v03.py` | Treat experiment 002 as provenance; audit only the retained collapse/information-production shape |
| 1.5 | phase transfer physicality | in progress | [docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md](../02_theory/015_qfuds_v0_15_phase_transfer_physics.md), [docs/04_results/015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md), [docs/04_results/020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md), `qfuds/gamma_laws.py` | Resolve the evidence gate in [docs/05_next_steps/015_level_1_5_resolution_gate.md](015_level_1_5_resolution_gate.md); required for physical Level 2B claims |
| 2A | phenomenological perturbation closure | completed | [docs/02_theory/040_qfuds_phenomenological_perturbations.md](../02_theory/040_qfuds_phenomenological_perturbations.md), [docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md](../03_experiments/030_exp_003_phenomenological_perturbation_closure.md), [docs/04_results/030_result_003_phenomenological_perturbation_closure.md](../04_results/030_result_003_phenomenological_perturbation_closure.md), `outputs/exp003_stability_diagnostics.csv` | P2 failed at retained amplitude; P1 survives only as phenomenological interacting vacuum |
| 2B | physical perturbation closure | blocked | Level 1.5 audit docs | Requires derived or explicitly justified transfer physics |
| 3 | CLASS integration | blocked | none | Requires a stable Level 2A closure at minimum; physical claims require Level 2B |
| 4 | CMB comparison | blocked | none | Requires CLASS/CAMB implementation |
| 5 | matter power spectrum | blocked | growth proxy only | Requires perturbation solver or Boltzmann output |
| 6 | DESI/Euclid comparison | blocked | no likelihood pipeline | Requires validated background plus perturbation predictions |

## Immediate Work

1. Continue QFUDS v0.15 / Level 1.5 using [docs/05_next_steps/015_level_1_5_resolution_gate.md](015_level_1_5_resolution_gate.md) as the pass/fail gate.
2. Treat `Gamma(a)` as phenomenological unless the Level 1.5 audit derives or fixes its physical source.
3. Treat the P2 regularized-fluid closure as failed at the retained amplitude.
4. Treat the P1 interacting-vacuum closure as Level 2A phenomenology only.
5. Replace the implicit `collapse_a` threshold with an explicit physical mass threshold `M`, or document why that cannot yet be done.
6. Recompute `dF_coll/dln a` using self-consistent QFUDS growth only after the required growth ingredients exist.
7. Do not advance to physical Level 2B without a physical transfer derivation.

Do not treat Level 2A as derived QFUDS physics. Do not start Level 2B, CLASS/CAMB,
CMB, matter-power, or survey-likelihood claims until the relevant upstream gate
is satisfied.

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
4. No tested perturbation closure relation.
5. No Boltzmann-code interface.
6. No likelihood comparison against CMB, BAO, SN, or matter power data.

## Rule For New Ideas

New speculative mechanisms should not be added to the main model unless they produce at least one of:

1. a new equation;
2. a new falsifiable observable;
3. a changed viability decision;
4. a reproducible experiment with code and outputs.
