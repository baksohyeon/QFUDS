---
doc_id: docs_index
title: QFUDS Documentation Index
doc_type: index
stage: "1.5"
status: in_progress
evidence_role: ssot
depends_on:
  - project_overview
  - roadmap
next_gate: keep Level 2B blocked; no CMB or matter-power claims
last_updated: 2026-06-09
---

# QFUDS Documentation Index

This directory is organized by research workflow stage.

## Conventions

- Every maintained Markdown document in `docs/` starts with YAML frontmatter.
- The H1 must match the frontmatter `title`.
- `doc_id` is the stable machine-readable identity; the title is the reader-facing label.
- Active stage files in `02_theory`, `03_experiments`, `04_results`, and `05_next_steps` keep sortable numeric prefixes.
- Background-only documents must not imply perturbation, CMB, matter-power, or survey-likelihood viability.
- Provenance documents must use `status: provenance` or `evidence_role: provenance`.

Run the documentation validator with:

```bash
python3 scripts/validate_docs.py
```

Run the full documentation-integrity checks with:

```bash
python3 scripts/research_consistency.py
python3 scripts/preflight_exp004.py
```

## 00 Project

Project-level status, decisions, roadmap framing, and Korean overview.

- [overview.md](00_project/overview.md)
- [research_program.md](00_project/research_program.md)
- [decision_log.md](00_project/decision_log.md)
- [verification_guide.md](00_project/verification_guide.md)
- [qfuds_ko.md](00_project/qfuds_ko.md)
- [frontmatter_convention.md](00_project/frontmatter_convention.md) - canonical YAML frontmatter schema (SSOT for `scripts/validate_docs.py`)
- [experiment_record_convention.md](00_project/experiment_record_convention.md) - required experiment/result sections, summary policy, and postmortem policy
- [traceability_matrix.md](00_project/traceability_matrix.md) - bidirectional claim/evidence traceability index

## 01 Origin

Provenance and idea-history documents. These are not evidence that QFUDS is correct.

- [concept_origin.md](01_origin/concept_origin.md)

## 02 Theory

Theory notes, literature positioning, and model-version definitions.

- [010_qfuds_v0_1.md](02_theory/010_qfuds_v0_1.md)
- [015_qfuds_v0_15_phase_transfer_physics.md](02_theory/015_qfuds_v0_15_phase_transfer_physics.md) - QFUDS v0.15 / Level 1.5 phase-transfer physicality audit
- [020_qfuds_v0_2.md](02_theory/020_qfuds_v0_2.md)
- [030_qfuds_v0_3.md](02_theory/030_qfuds_v0_3.md)
- [040_qfuds_phenomenological_perturbations.md](02_theory/040_qfuds_phenomenological_perturbations.md)
- [900_qfuds_research_report.md](02_theory/900_qfuds_research_report.md)

## 03 Experiments

Reproducible experiment definitions.

- [000_exp_000_lcdm_baseline.md](03_experiments/000_exp_000_lcdm_baseline.md)
- [010_exp_001_gamma_scan.md](03_experiments/010_exp_001_gamma_scan.md)
- [015_exp_001_5_phase_transfer_physicality.md](03_experiments/015_exp_001_5_phase_transfer_physicality.md)
- [020_exp_002_entropy_information_gate.md](03_experiments/020_exp_002_entropy_information_gate.md)
- [030_exp_003_phenomenological_perturbation_closure.md](03_experiments/030_exp_003_phenomenological_perturbation_closure.md)

## 04 Results

Experiment reports, diagnostic results, and hostile-referee conclusions.

- [000_experiment_summary.md](04_results/000_experiment_summary.md) - lightweight per-experiment summary and postmortem coverage
- [000_result_000_lcdm_baseline.md](04_results/000_result_000_lcdm_baseline.md)
- [010_result_001_gamma_scan.md](04_results/010_result_001_gamma_scan.md)
- [015_result_001_5_phase_transfer_physicality.md](04_results/015_result_001_5_phase_transfer_physicality.md)
- [020_result_002_entropy_information_gate.md](04_results/020_result_002_entropy_information_gate.md)
- [030_result_003_phenomenological_perturbation_closure.md](04_results/030_result_003_phenomenological_perturbation_closure.md)

## 05 Next Steps

Current validation roadmap and blockers.

- [000_roadmap.md](05_next_steps/000_roadmap.md)
- [010_perturbation_gate.md](05_next_steps/010_perturbation_gate.md)
- [015_level_1_5_resolution_gate.md](05_next_steps/015_level_1_5_resolution_gate.md) - evidence criteria for Level 1.5 pass, fail, or demotion
- [020_exp004_preflight_gate.md](05_next_steps/020_exp004_preflight_gate.md) - repository consistency gate that must pass before exp_004
- [900_roadmap_overview_ko.md](05_next_steps/900_roadmap_overview_ko.md) - Korean guide to roadmap trajectory and branch outcomes
