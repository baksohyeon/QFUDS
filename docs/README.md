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
next_gate: retained branch demoted; keep Level 2B blocked
last_updated: 2026-06-10
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
python3 scripts/generate_result_figures.py
python3 scripts/research_consistency.py
python3 scripts/preflight_exp004.py
```

## 00 Project

Project-level status, decisions, roadmap framing, and Korean overview.

- [overview.md](00_project/overview.md)
- [research_program.md](00_project/research_program.md)
- [project_identity.md](00_project/project_identity.md) - current project identity, scope, non-goals, retained-branch classification, and lessons learned
- [qfuds_positioning.md](00_project/qfuds_positioning.md) - QFUDS ideas mapped against existing cosmology model families
- [concept_survival_audit.md](00_project/concept_survival_audit.md) - original intuition mapped against current evidence, demotions, and open candidates
- [success_criteria.md](00_project/success_criteria.md) - minimum, moderate, and strong success criteria plus physical-branch admission rule
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

- [000_qfuds_v0_1_conceptual_origin.md](02_theory/000_qfuds_v0_1_conceptual_origin.md)
- [000_qfuds_v0_2_two_phase_background.md](02_theory/000_qfuds_v0_2_two_phase_background.md)
- [010_qfuds_v0_3_gamma_laws.md](02_theory/010_qfuds_v0_3_gamma_laws.md)
- [015_qfuds_v0_15_phase_transfer_physics.md](02_theory/015_qfuds_v0_15_phase_transfer_physics.md) - QFUDS v0.15 / [Level 1.5](wiki/glossary/repository_levels.md) retained-branch demotion audit
- [015_qfuds_level_1_5_equivalence_source_perturbation_audit.md](02_theory/015_qfuds_level_1_5_equivalence_source_perturbation_audit.md) - completed Level 1.5 equivalence, source, and perturbation-readiness audit
- [015_qfuds_qnu_necessity_formulation_audit.md](02_theory/015_qfuds_qnu_necessity_formulation_audit.md) - audit of whether QFUDS needs an explicit transfer four-vector
- [015_qfuds_level_1_5_transfer_four_vector_derivation_attempt.md](02_theory/015_qfuds_level_1_5_transfer_four_vector_derivation_attempt.md) - failed Level 1.5 derivation attempt for a transfer four-vector
- [015_qfuds_strong_gravity_source_mechanism_audit.md](02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md) - strong-gravity source-mechanism audit for the broader DM-to-DE phase-transition hypothesis
- [030_qfuds_phenomenological_perturbations.md](02_theory/030_qfuds_phenomenological_perturbations.md)
- [900_qfuds_research_report.md](02_theory/900_qfuds_research_report.md)

## 03 Experiments

Reproducible experiment definitions.

- [000_exp_000_lcdm_baseline.md](03_experiments/000_exp_000_lcdm_baseline.md)
- [010_exp_001_gamma_scan.md](03_experiments/010_exp_001_gamma_scan.md)
- [015_exp_001_5_phase_transfer_physicality.md](03_experiments/015_exp_001_5_phase_transfer_physicality.md)
- [020_exp_002_entropy_information_gate.md](03_experiments/020_exp_002_entropy_information_gate.md)
- [030_exp_003_phenomenological_perturbation_closure.md](03_experiments/030_exp_003_phenomenological_perturbation_closure.md)
- [030_exp_004_p1_model_family_positioning.md](03_experiments/030_exp_004_p1_model_family_positioning.md)
- [030_exp_005_timing_prior_usefulness.md](03_experiments/030_exp_005_timing_prior_usefulness.md)
- [030_exp_006_literature_timing_support_audit.md](03_experiments/030_exp_006_literature_timing_support_audit.md)

## 04 Results

Experiment reports, diagnostic results, and hostile-referee conclusions.

- [000_experiment_summary.md](04_results/000_experiment_summary.md) - lightweight per-experiment summary and postmortem coverage
- [000_result_000_lcdm_baseline.md](04_results/000_result_000_lcdm_baseline.md)
- [010_result_001_gamma_scan.md](04_results/010_result_001_gamma_scan.md)
- [015_result_001_5_phase_transfer_physicality.md](04_results/015_result_001_5_phase_transfer_physicality.md)
- [020_result_002_entropy_information_gate.md](04_results/020_result_002_entropy_information_gate.md)
- [030_result_003_phenomenological_perturbation_closure.md](04_results/030_result_003_phenomenological_perturbation_closure.md)
- [030_result_004_p1_model_family_positioning.md](04_results/030_result_004_p1_model_family_positioning.md)
- [030_result_005_timing_prior_usefulness.md](04_results/030_result_005_timing_prior_usefulness.md)
- [030_result_006_literature_timing_support_audit.md](04_results/030_result_006_literature_timing_support_audit.md)

## 05 Next Steps

Current validation roadmap and blockers.

- [000_roadmap.md](05_next_steps/000_roadmap.md)
- [010_safe_future_branch_candidates.md](05_next_steps/010_safe_future_branch_candidates.md) - allowed non-Level-2B follow-up branches after the accepted physical-branch audit
- [010_perturbation_gate.md](05_next_steps/010_perturbation_gate.md)
- [015_level_1_5_resolution_gate.md](05_next_steps/015_level_1_5_resolution_gate.md) - evidence criteria for Level 1.5 pass, fail, demotion, and future branch admission
- [015_retained_branch_source_closure_plan_provenance.md](05_next_steps/015_retained_branch_source_closure_plan_provenance.md) - provenance planning gate superseded by the retained-branch demotion
- [030_exp003_record_consistency_gate.md](05_next_steps/030_exp003_record_consistency_gate.md) - exp_003 record consistency gate
- [900_roadmap_overview_ko.md](05_next_steps/900_roadmap_overview_ko.md) - Korean guide to roadmap trajectory and branch outcomes

## Research Cache

Raw literature records and dated availability audits. These are reference
records only, not experiment conclusions.

- [Research Cache](research/README.md)

## Wiki Audits And Checkpoints

Accepted audit summaries and handoff checkpoints. These are not roadmap status
authorities.

- [Physical Branch Audit Summary](wiki/audits/004-physical-branch-audit-summary.md)
- [Blocked Admission Rule Checkpoint](wiki/checkpoints/blocked-admission-rule.md)
