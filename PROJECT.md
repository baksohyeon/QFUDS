# QFUDS Project Documentation Control

Date: 2026-06-08

This file is the entry point for maintaining the QFUDS research record.

QFUDS is not a confirmed theory. The repository is a staged attempt to turn a speculative dark-sector idea into equations, reproducible tests, hostile reviews, and decisions.

## Execution Order

Repository level terminology and validation-order meanings live in
[repository_levels.md](docs/wiki/glossary/repository_levels.md). This file
controls documentation structure, not level definitions.

The current stop line — which level is active, what is complete, and what is
blocked — is **not** restated here. It lives in the single source of truth:
[docs/05_next_steps/000_roadmap.md](docs/05_next_steps/000_roadmap.md). Read
the roadmap for current status before acting.

## Status, Decisions, And Evidence

[PROJECT.md](PROJECT.md) controls documentation structure, not project status. To avoid
drift, status is maintained in exactly one place and is not duplicated here:

- **Current status, current level, active branch, and blockers** —
  [docs/05_next_steps/000_roadmap.md](docs/05_next_steps/000_roadmap.md)
  (single source of truth).
- **Why decisions were made** —
  [docs/00_project/decision_log.md](docs/00_project/decision_log.md).
- **Experiment evidence** — [docs/03_experiments/](docs/03_experiments/) and
  [docs/04_results/](docs/04_results/).

If anything in this file appears to assert project status, the roadmap wins and
this file must be corrected.

## Documentation Tree

Canonical active documents:

- [PROJECT.md](PROJECT.md)
- [AGENTS.md](AGENTS.md)
- [README.md](README.md)
- [docs/00_project/overview.md](docs/00_project/overview.md)
- [docs/00_project/decision_log.md](docs/00_project/decision_log.md)
- [docs/00_project/verification_guide.md](docs/00_project/verification_guide.md)
- [docs/00_project/frontmatter_convention.md](docs/00_project/frontmatter_convention.md)
- [docs/00_project/experiment_record_convention.md](docs/00_project/experiment_record_convention.md)
- [docs/02_theory/000_qfuds_v0_1_conceptual_origin.md](docs/02_theory/000_qfuds_v0_1_conceptual_origin.md)
- [docs/02_theory/000_qfuds_v0_2_two_phase_background.md](docs/02_theory/000_qfuds_v0_2_two_phase_background.md)
- [docs/02_theory/010_qfuds_v0_3_gamma_laws.md](docs/02_theory/010_qfuds_v0_3_gamma_laws.md)
- [docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md](docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md)
- [docs/02_theory/030_qfuds_phenomenological_perturbations.md](docs/02_theory/030_qfuds_phenomenological_perturbations.md)
- [docs/03_experiments/000_exp_000_lcdm_baseline.md](docs/03_experiments/000_exp_000_lcdm_baseline.md)
- [docs/03_experiments/010_exp_001_gamma_scan.md](docs/03_experiments/010_exp_001_gamma_scan.md)
- [docs/03_experiments/015_exp_001_5_phase_transfer_physicality.md](docs/03_experiments/015_exp_001_5_phase_transfer_physicality.md)
- [docs/03_experiments/020_exp_002_entropy_information_gate.md](docs/03_experiments/020_exp_002_entropy_information_gate.md)
- [docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md](docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md)
- [docs/04_results/000_result_000_lcdm_baseline.md](docs/04_results/000_result_000_lcdm_baseline.md)
- [docs/04_results/000_experiment_summary.md](docs/04_results/000_experiment_summary.md)
- [docs/04_results/010_result_001_gamma_scan.md](docs/04_results/010_result_001_gamma_scan.md)
- [docs/04_results/015_result_001_5_phase_transfer_physicality.md](docs/04_results/015_result_001_5_phase_transfer_physicality.md)
- [docs/04_results/020_result_002_entropy_information_gate.md](docs/04_results/020_result_002_entropy_information_gate.md)
- [docs/04_results/030_result_003_phenomenological_perturbation_closure.md](docs/04_results/030_result_003_phenomenological_perturbation_closure.md)
- [docs/05_next_steps/000_roadmap.md](docs/05_next_steps/000_roadmap.md)
- [docs/05_next_steps/010_perturbation_gate.md](docs/05_next_steps/010_perturbation_gate.md)

Historical/provenance documents:

- [docs/01_origin/concept_origin.md](docs/01_origin/concept_origin.md)
- [docs/00_project/research_program.md](docs/00_project/research_program.md)
- [docs/00_project/qfuds_ko.md](docs/00_project/qfuds_ko.md)
- [docs/02_theory/900_qfuds_research_report.md](docs/02_theory/900_qfuds_research_report.md)

## Naming Convention

Use this convention:

```text
000_ baseline/control
010_ Level 1 / experiment 001
015_ QFUDS v0.15 / Level 1.5 gate
020_ experiment 002 entropy/information provenance sequence
030_ Level 2A / experiment 003 phenomenological perturbation sequence
040_ future Level 2B+ physical perturbation, interface, or downstream theory work
900_ broad reference or report
```

The numeric prefix is a sort key. It must keep file trees readable in ordinary
alphabetical or natural-sort file explorers. Do not create unprefixed active
stage files in `docs/02_theory/` through `docs/05_next_steps/`.

The semantic ID remains in the filename after the prefix. Do not rename
experiments as theory versions or theory notes as experiments.

## Frontmatter Convention

The canonical schema, allowed values, and enforced rules live in
[docs/00_project/frontmatter_convention.md](docs/00_project/frontmatter_convention.md)
(SSOT) and are checked by
`scripts/validate_docs.py`. The block below is a convenience copy; if it drifts
from the convention document or the validator, those win.

Every maintained Markdown document under [docs/](docs/) must start with YAML
frontmatter. Active stage documents in [docs/02_theory/](docs/02_theory/),
[docs/03_experiments/](docs/03_experiments/),
[docs/04_results/](docs/04_results/), and
[docs/05_next_steps/](docs/05_next_steps/) must also
keep their sortable filename prefix.

```yaml
---
doc_id: string
title: string
doc_type: overview | decision_log | guide | theory_note | experiment | result | summary | postmortem | roadmap | gate | index | reference
stage: "0" | "1" | "1.5" | "2" | "3" | "4" | "5" | "6" | "reference"
status: draft | completed | in_progress | blocked | provenance | reference
evidence_role: control | hypothesis | proxy_scan | provenance | audit | ssot | reference
depends_on: []
next_gate: string
last_updated: YYYY-MM-DD
---
```

Agents should read frontmatter first, then body text. If frontmatter and body
conflict, update the active document rather than guessing.

The H1 must match `title`. Use `doc_id` for machine-readable identity and the
H1/title for human-readable labels.

## What Experiment 002 Is

[docs/04_results/020_result_002_entropy_information_gate.md](docs/04_results/020_result_002_entropy_information_gate.md)
is not a perturbation result.

It is a background-level entropy/information-source scan. It asks whether the phase-transfer shape can be tied to a concrete source such as horizon information, HBM/KL gravitational entropy, black-hole entropy, or Press-Schechter information production.

Experiment 002 is retained as provenance, not as physical evidence. It keeps
only the collapse/information-production shape as the QFUDS v0.15 / Level 1.5
physicality question.

## Level Terminology

Use [repository_levels.md](docs/wiki/glossary/repository_levels.md) for level
definitions and [docs/05_next_steps/000_roadmap.md](docs/05_next_steps/000_roadmap.md)
for current status. Do not duplicate those definitions here.

No experiment is complete until it has:

- a document in [docs/03_experiments/](docs/03_experiments/);
- a result in [docs/04_results/](docs/04_results/);
- a decision-log update;
- a roadmap update;
- an experiment-summary update in
  [docs/04_results/000_experiment_summary.md](docs/04_results/000_experiment_summary.md).

`exp_003` satisfied all four for its documented scope.

## Refactoring Rule

Do not rewrite history to hide failed branches. The repository should preserve that `exp_001` and `exp_002` were background-level filters.

Do make active documents explicit about the sequence:

```text
background filters -> Level 1.5 phase-transfer physicality -> perturbation equations -> Boltzmann code -> observables
```

## README Update Rule

The README should remain a reader-facing overview. It should point to:

- [PROJECT.md](PROJECT.md) for documentation control and validation order;
- [docs/05_next_steps/000_roadmap.md](docs/05_next_steps/000_roadmap.md) for
  current status, level, and blockers (single source of truth);
- [docs/00_project/decision_log.md](docs/00_project/decision_log.md) for
  research history and decisions;
- [docs/00_project/verification_guide.md](docs/00_project/verification_guide.md)
  for reproducible checks.
