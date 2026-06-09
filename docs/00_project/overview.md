---
doc_id: project_overview
title: QFUDS Project Overview
doc_type: overview
stage: "1.5"
status: in_progress
evidence_role: ssot
depends_on:
  - decision_log
  - roadmap
next_gate: keep Level 2B blocked; no CMB or matter-power claims
last_updated: 2026-06-09
---

# QFUDS Project Overview

Date: 2026-06-09

## Project Goals

Quantum Foam Unified Dark Sector (QFUDS) is a speculative research program that asks whether the observed dark sector can be modeled as two effective macroscopic phases of one underlying quantum-spacetime foam sector:

- phase A: a clustering, nearly pressureless component with `w_A ~= 0` and `c_s,A^2 ~= 0`;
- phase B: a smooth vacuum-pressure component with `w_B ~= -1`;
- optional defects/remnants: subdominant black/white-hole-like information-storage candidates, not the main dark-sector explanation.

The scientific goal is not to defend the idea as correct. The goal is to make the idea precise enough to compare with LCDM, unified dark fluids, k-essence, interacting dark energy, scalar-field dark matter, and compact-remnant scenarios.

The working standard is:

```text
Can this version be made precise enough to fail?
```

## Current Status

The current per-level status — completed, in progress, or blocked — and the list
of completed experiments are maintained only in the roadmap (single source of
truth): [docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md), with the reasoning trail in
[docs/00_project/decision_log.md](decision_log.md). This overview does not restate them, so it
cannot drift from the roadmap.

Current implementation anchors:

- `qfuds/background.py`: two-phase background integration.
- `qfuds/gamma_laws.py`: candidate `Gamma(a)` transfer laws.
- `qfuds/growth.py`: scale-independent growth proxy under smooth phase-B assumptions.
- `qfuds/diagnostics.py`: LCDM comparison and minimal viability flags.
- `scripts/run_minimal_model.py`: reproducible CLI runner.
- `outputs/`: generated CSV and PNG files for the baseline and background validation experiments.

## Known Limitations

QFUDS is not yet a complete physical theory.

1. No covariant microscopic foam action has been derived.
2. The phase split is phenomenological.
3. `Gamma(a)` laws in experiment 001 are toy prescriptions or empirical proxies.
4. The experiment 002 information-production branch is provenance, not current physical evidence.
5. Background-level viability does not imply CMB viability.
6. Physical perturbation closure is blocked until a new admitted physical branch supplies a transfer derivation.
7. A single adiabatic unified fluid with late `w -> -1` can fail structure formation through an excessive sound speed.
8. Compact black/white-hole remnants are optional and must remain subdominant unless their abundance and mass function are derived.
9. Existing data already strongly constrain deviations from LCDM.

## Roadmap

The immediate research path is:

1. Preserve the version history and experiment decisions in docs.
2. Keep experiments 001 and 002 as background-only diagnostic results.
3. Keep the retained `dF_coll/dln(a)` branch closed as a failed physical Level 1.5 promotion.
4. Interpret the Level 2A result as phenomenological interacting vacuum only; see the roadmap for its status.
5. Open no physical Level 2B or Boltzmann-code work until a new physical branch passes the roadmap admission rule.
6. Compare against CMB and matter power only after the relevant upstream perturbation and implementation gates exist.

The maintained roadmap is [docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md).

## Model Genealogy

```text
Concept origin
  Landauer/information-cost prompt
  -> black-hole information and Hawking-radiation questions
  -> reverse-channel and white-hole-like remnant speculation
  -> quantum foam as possible medium
  -> dark matter as clustering foam mode
  -> dark energy as residual foam pressure

qfuds_v0_1
  Conceptual unified-foam hypothesis.
  No validated equations. White-hole-universe image pruned out of the core claim.

qfuds_v0_2
  Minimal two-phase effective dark sector in unmodified GR.
  Gamma = 0 reproduces LCDM.
  Free Gamma(a) reduces to interacting dark energy.

qfuds_v0_3 / exp_001
  Background diagnostic scan over physically labeled Gamma(a) laws.
  Constant and ungated growth-driven transfer fail immediately.
  Low-redshift collapse, black-hole-entropy, and star-formation proxies survive
  only as toy targets for later audit, not as perturbation evidence.

exp_002
  Entropy/information-source diagnostic scan.
  Broad entropy language is rejected as a general explanation.
  The scan is retained as provenance, not as physical evidence.
  Collapse/information production is kept only as a Level 1.5 question.

Level 1.5
  Phase-transfer physicality audit.
  Current retained-branch verdict: Gamma(a) is a phenomenological
  coarse-grained transfer law with a physically motivated source shape, not a
  derived microscopic law.

Level 2A
  Phenomenological perturbation closure.
  Completed only as a gauge-declared interacting-dark-sector audit.
  P2 failed; P1 survives only as phenomenological interacting vacuum.
```

## Primary Source Documents

Maintained documentation:

- [docs/README.md](../README.md)
- [docs/00_project/overview.md](overview.md)
- [docs/00_project/decision_log.md](decision_log.md)
- [docs/00_project/verification_guide.md](verification_guide.md)
- [docs/02_theory/000_qfuds_v0_1_conceptual_origin.md](../02_theory/000_qfuds_v0_1_conceptual_origin.md)
- [docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md](../02_theory/015_qfuds_v0_15_phase_transfer_physics.md)
- [docs/02_theory/000_qfuds_v0_2_two_phase_background.md](../02_theory/000_qfuds_v0_2_two_phase_background.md)
- [docs/02_theory/010_qfuds_v0_3_gamma_laws.md](../02_theory/010_qfuds_v0_3_gamma_laws.md)
- [docs/02_theory/030_qfuds_phenomenological_perturbations.md](../02_theory/030_qfuds_phenomenological_perturbations.md)
- [docs/03_experiments/000_exp_000_lcdm_baseline.md](../03_experiments/000_exp_000_lcdm_baseline.md)
- [docs/03_experiments/010_exp_001_gamma_scan.md](../03_experiments/010_exp_001_gamma_scan.md)
- [docs/03_experiments/015_exp_001_5_phase_transfer_physicality.md](../03_experiments/015_exp_001_5_phase_transfer_physicality.md)
- [docs/03_experiments/020_exp_002_entropy_information_gate.md](../03_experiments/020_exp_002_entropy_information_gate.md)
- [docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md](../03_experiments/030_exp_003_phenomenological_perturbation_closure.md)
- [docs/04_results/000_result_000_lcdm_baseline.md](../04_results/000_result_000_lcdm_baseline.md)
- [docs/04_results/010_result_001_gamma_scan.md](../04_results/010_result_001_gamma_scan.md)
- [docs/04_results/015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md)
- [docs/04_results/020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md)
- [docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md)

Historical/source notes retained for provenance:

- [docs/01_origin/concept_origin.md](../01_origin/concept_origin.md)
- [docs/00_project/research_program.md](research_program.md)
- [docs/02_theory/900_qfuds_research_report.md](../02_theory/900_qfuds_research_report.md)
- [docs/00_project/qfuds_ko.md](qfuds_ko.md)
