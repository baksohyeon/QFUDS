---
doc_id: traceability_matrix
title: QFUDS Traceability Matrix
doc_type: summary
stage: "2"
status: in_progress
evidence_role: audit
depends_on:
  - roadmap
  - decision_log
  - experiment_summary
next_gate: keep synchronized with every new experiment/result decision
last_updated: 2026-06-09
---

# QFUDS Traceability Matrix

Date: 2026-06-09

This matrix lets a reader start from a roadmap-level conclusion and trace it
back to assumptions, experiment definitions, code paths, outputs, results, and
decisions. It is an evidence index, not the current status authority. Current
status remains in [docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md).

## Canonical Reading Path

For a new reader:

- [README.md](../../README.md)
- [docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md)
- [docs/04_results/000_experiment_summary.md](../04_results/000_experiment_summary.md)
- [docs/00_project/traceability_matrix.md](traceability_matrix.md)
- relevant theory note
- relevant experiment definition
- relevant result document
- [docs/00_project/decision_log.md](decision_log.md)
- [docs/00_project/verification_guide.md](verification_guide.md)

This path answers:

```text
hypothesis -> experiment -> result -> decision -> roadmap status
```

## Claim To Evidence

| Roadmap conclusion | Theory assumptions | Experiment definition | Code path | Outputs | Result | Decision record |
| --- | --- | --- | --- | --- | --- | --- |
| LCDM null limit exists | [docs/02_theory/020_qfuds_v0_2.md](../02_theory/020_qfuds_v0_2.md) | [docs/03_experiments/000_exp_000_lcdm_baseline.md](../03_experiments/000_exp_000_lcdm_baseline.md) | `scripts/run_minimal_model.py`, `qfuds/background.py`, `tests/test_gamma_v03.py` | `outputs/qfuds_gamma0_beta0.csv`, `outputs/qfuds_gamma0_beta0.png` | [docs/04_results/000_result_000_lcdm_baseline.md](../04_results/000_result_000_lcdm_baseline.md) | [docs/00_project/decision_log.md](decision_log.md) entry: keep zero-transfer run as LCDM regression baseline |
| early or ungated transfer laws fail background checks | [docs/02_theory/030_qfuds_v0_3.md](../02_theory/030_qfuds_v0_3.md) | [docs/03_experiments/010_exp_001_gamma_scan.md](../03_experiments/010_exp_001_gamma_scan.md) | `scripts/run_minimal_model.py`, `qfuds/gamma_laws.py`, `qfuds/background.py` | `outputs/qfuds_constant_gamma0.01_beta0.csv`, `outputs/qfuds_growth_driven_gamma0.01_beta0.csv`, related PNGs | [docs/04_results/010_result_001_gamma_scan.md](../04_results/010_result_001_gamma_scan.md) | decision-log entries rejecting constant and ungated growth-driven transfer |
| exp_002 is provenance, not physical evidence | [docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md](../02_theory/015_qfuds_v0_15_phase_transfer_physics.md) | [docs/03_experiments/020_exp_002_entropy_information_gate.md](../03_experiments/020_exp_002_entropy_information_gate.md) | `scripts/run_minimal_model.py`, `qfuds/gamma_laws.py`, `qfuds/growth.py` | `outputs/qfuds_information_production_gamma0.02_beta0.csv`, `outputs/qfuds_gravitational_entropy_gamma0.003_beta0.csv`, `outputs/qfuds_horizon_information_gamma0.03_beta0.csv` | [docs/04_results/020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md), [docs/04_results/015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md) | decision-log entry: demote experiment 002 from evidence to provenance |
| Level 1.5 physical transfer remains unresolved | [docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md](../02_theory/015_qfuds_v0_15_phase_transfer_physics.md) | [docs/03_experiments/015_exp_001_5_phase_transfer_physicality.md](../03_experiments/015_exp_001_5_phase_transfer_physicality.md) | `qfuds/gamma_laws.py`, `qfuds/growth.py` | classification audit, not a new output grid | [docs/04_results/015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md) | decision-log entry inserting Level 1.5 and demoting exp_002 |
| Level 2A P2 fails and P1 survives only phenomenologically | [docs/02_theory/040_qfuds_phenomenological_perturbations.md](../02_theory/040_qfuds_phenomenological_perturbations.md) | [docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md](../03_experiments/030_exp_003_phenomenological_perturbation_closure.md) | `scripts/run_minimal_model.py`, `qfuds/perturbations.py` | `outputs/exp003_stability_diagnostics.csv`, `outputs/exp003_phenomenological_perturbation_summary.json`, mode CSVs | [docs/04_results/030_result_003_phenomenological_perturbation_closure.md](../04_results/030_result_003_phenomenological_perturbation_closure.md) | decision-log entries for exp_003 verdict and friction-bug correction |

## Evidence To Claim

| Evidence artifact | Supports or constrains claim | Where the final decision is recorded |
| --- | --- | --- |
| `outputs/qfuds_gamma0_beta0.csv` | zero-transfer path is the LCDM control baseline | [docs/04_results/000_result_000_lcdm_baseline.md](../04_results/000_result_000_lcdm_baseline.md), [docs/00_project/decision_log.md](decision_log.md) |
| `outputs/qfuds_constant_gamma0.01_beta0.csv` | constant transfer fails the tested background viability criteria | [docs/04_results/010_result_001_gamma_scan.md](../04_results/010_result_001_gamma_scan.md), [docs/00_project/decision_log.md](decision_log.md) |
| `outputs/qfuds_growth_driven_gamma0.01_beta0.csv` | ungated growth-driven transfer fails the tested background viability criteria | [docs/04_results/010_result_001_gamma_scan.md](../04_results/010_result_001_gamma_scan.md), [docs/00_project/decision_log.md](decision_log.md) |
| `outputs/qfuds_information_production_gamma0.02_beta0.csv` | collapse/information-production shape had acceptable background timing, but only as a proxy shape | [docs/04_results/020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md), [docs/04_results/015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md) |
| [docs/04_results/015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md) | retained transfer law is not yet physical QFUDS; physical Level 2B remains blocked | [docs/00_project/decision_log.md](decision_log.md), [docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md) |
| [docs/05_next_steps/015_level_1_5_resolution_gate.md](../05_next_steps/015_level_1_5_resolution_gate.md) | defines the evidence needed for Level 1.5 pass, fail, or demotion | future Level 1.5 result and decision-log entry |
| `outputs/exp003_stability_diagnostics.csv` | P2 fails at retained amplitude; P1 is stable only under the declared phenomenological closure | [docs/04_results/030_result_003_phenomenological_perturbation_closure.md](../04_results/030_result_003_phenomenological_perturbation_closure.md), [docs/00_project/decision_log.md](decision_log.md) |
| [outputs/postmortem/exp003_friction_bug/README.md](../../outputs/postmortem/exp003_friction_bug/README.md) | original exp_003 diagnostics were superseded after the Euler-friction correction | [docs/04_results/030_result_003_phenomenological_perturbation_closure.md](../04_results/030_result_003_phenomenological_perturbation_closure.md), [docs/00_project/decision_log.md](decision_log.md) |

## Exp 002 Reclassification

Experiment 002 originally scanned entropy and information-source shapes at
background level. It is now explicitly demoted because it was run before these
physical ingredients existed:

- derived phase-transfer mechanism;
- fixed physical mass threshold `M`;
- self-consistent QFUDS growth source;
- transfer perturbation prescription.

The retained collapse/information-production shape is therefore only a question
for Level 1.5:

```text
Can dF_coll/dln(a) be made into a physical transfer source?
```

It is not evidence that QFUDS is physical, novel, perturbatively stable, or
observationally viable.

## Integrity Commands

Run:

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/preflight_exp004.py
```

These commands check schema, section coverage, status authority, experiment/result
pairs, referenced outputs, exp_003 postmortem coverage, and premature
CLASS/CMB/matter-power claims.
