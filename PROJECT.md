# QFUDS Project Documentation Control

Date: 2026-06-08

This file is the entry point for maintaining the QFUDS research record.

QFUDS is not a confirmed theory. The repository is a staged attempt to turn a speculative dark-sector idea into equations, reproducible tests, hostile reviews, and decisions.

## Execution Order

The validation order is sequential:

```text
Level 0: literature position
Level 1: background toy model
QFUDS v0.15 / Level 1.5: phase transfer physicality
Level 2A: phenomenological perturbation closure
Level 2B: physical perturbation equations
Level 3: CLASS or CAMB integration
Level 4: CMB comparison
Level 5: matter power comparison
Level 6: DESI / Euclid / Roman constraints
```

Level 1 contains three background validations:

```text
exp_000: zero-transfer LCDM baseline
exp_001: Gamma-law background scan
exp_002: entropy / information-source background gate
```

These are not observational successes. They are filters before QFUDS v0.15 / Level 1.5 because several candidate transfer laws needed to be killed before asking whether the surviving transfer law is physical enough for perturbation work.

Current stop line:

```text
QFUDS v0.15 / Level 1.5 phase-transfer physicality is not complete.
Level 2A phenomenological perturbation closure is complete (exp_003):
  P2 failed at the retained amplitude; P1 survives only as a non-novel
  phenomenological interacting vacuum.
Level 2B physical perturbation theory is blocked.
No CLASS/CAMB implementation exists.
No CMB spectrum exists.
No matter-power spectrum exists.
No survey likelihood exists.
```

## Current Status

Completed:

- Level 0 literature positioning at draft level.
- Level 1 background validation:
  - `exp_000` zero-transfer LCDM baseline;
  - `exp_001` Gamma-law background scan;
  - `exp_002` entropy/information-source background gate.
- Level 2A phenomenological perturbation closure (`exp_003`): P2 failed at the
  retained amplitude; P1 survives only as a non-novel phenomenological
  interacting vacuum. This is not physical QFUDS perturbation evidence.

In progress:

- QFUDS v0.15 / Level 1.5 phase-transfer physicality.

Blocked:

- Level 2B physical perturbation equations.
- CLASS/CAMB integration.
- CMB comparison.
- matter-power comparison.
- DESI/Euclid/Roman constraints.

## Documentation Tree

Canonical active documents:

```text
PROJECT.md
AGENTS.md
README.md
docs/00_project_overview.md
docs/00_project/overview.md
docs/00_project/decision_log.md
docs/00_project/verification_guide.md
docs/00_project/frontmatter_convention.md
docs/02_theory/010_qfuds_v0_1.md
docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md
docs/02_theory/020_qfuds_v0_2.md
docs/02_theory/030_qfuds_v0_3.md
docs/02_theory/040_qfuds_phenomenological_perturbations.md
docs/03_experiments/000_exp_000_lcdm_baseline.md
docs/03_experiments/010_exp_001_gamma_scan.md
docs/03_experiments/015_exp_001_5_phase_transfer_physicality.md
docs/03_experiments/020_exp_002_entropy_information_gate.md
docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md
docs/04_results/000_result_000_lcdm_baseline.md
docs/04_results/010_result_001_gamma_scan.md
docs/04_results/015_result_001_5_phase_transfer_physicality.md
docs/04_results/020_result_002_entropy_information_gate.md
docs/04_results/030_result_003_phenomenological_perturbation_closure.md
docs/05_next_steps/000_roadmap.md
docs/05_next_steps/010_perturbation_gate.md
```

Historical/provenance documents:

```text
docs/01_origin/concept_origin.md
docs/00_project/research_program.md
docs/00_project/qfuds_ko.md
docs/02_theory/900_qfuds_research_report.md
```

## Naming Convention

Use this convention:

```text
docs/02_theory/:      010_qfuds_v0_1, 015_qfuds_v0_15_*, 020_qfuds_v0_2, 030_qfuds_v0_3, 900_*
docs/03_experiments/: 000_exp_000_*, 010_exp_001_*, 015_exp_001_5_*, 020_exp_002_*
docs/04_results/:     000_result_000_*, 010_result_001_*, 015_result_001_5_*, 020_result_002_*
docs/05_next_steps/:  000_roadmap.md, 010_perturbation_gate.md
```

The numeric prefix is a sort key. It must keep file trees readable in ordinary
alphabetical or natural-sort file explorers. Do not create unprefixed active
stage files in `docs/02_theory/` through `docs/05_next_steps/`.

The semantic ID remains in the filename after the prefix. Do not rename
experiments as theory versions or theory notes as experiments.

## Frontmatter Convention

The canonical schema, allowed values, and enforced rules live in
`docs/00_project/frontmatter_convention.md` (SSOT) and are checked by
`scripts/validate_docs.py`. The block below is a convenience copy; if it drifts
from the convention document or the validator, those win.

Every maintained Markdown document under `docs/` must start with YAML
frontmatter. Active stage documents in `docs/02_theory/`,
`docs/03_experiments/`, `docs/04_results/`, and `docs/05_next_steps/` must also
keep their sortable filename prefix.

```yaml
---
doc_id: string
title: string
doc_type: overview | decision_log | guide | theory_note | experiment | result | roadmap | gate | index | reference
stage: "0" | "1" | "1.5" | "2" | "reference"
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

`docs/04_results/020_result_002_entropy_information_gate.md` is not a perturbation result.

It is a background-level entropy/information-source scan. It asks whether the phase-transfer shape can be tied to a concrete source such as horizon information, HBM/KL gravitational entropy, black-hole entropy, or Press-Schechter information production.

Experiment 002 is retained as provenance, not as physical evidence. It keeps
only the collapse/information-production shape as the QFUDS v0.15 / Level 1.5
physicality question.

## What Level 1.5 Must Decide

`docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md` asks whether the surviving branch is
a physical phase-transfer hypothesis or only a phenomenological transfer law.

Current Level 1.5 verdict:

```text
Gamma(a) is a phenomenological coarse-grained transfer law with a physically
motivated source shape. It is not yet derived physics.
```

## What Level 2 Produced And Still Must Produce

Level 2A phenomenological perturbation closure has been completed as `exp_003`.
It was permitted to proceed without Level 1.5 because it is an explicitly
phenomenological, gauge-declared closure audit, not a physical derivation. Its
verdict: the P2 regularized phase-B fluid closure failed at the retained
amplitude, and the P1 interacting-vacuum closure survives only as a non-novel
phenomenological interacting vacuum.

Physical Level 2B must not start until Level 1.5 is resolved. Once unblocked,
Level 2B must produce new theory and experiment documents before any CLASS/CAMB
work starts.

Required Level 2B outputs:

- self-consistent `dF_coll/dln a` using QFUDS growth `D(a)`;
- physically fixed collapse mass threshold `M`;
- perturbation literature review;
- equations for `delta_A`, `theta_A`, `delta_B`, `theta_B`;
- explicit transfer perturbation prescription;
- gauge assumptions;
- stability analysis;
- numerical perturbation evolution;
- LCDM and `w(a)` / `f sigma8(a)` redshift-ratio comparison;
- hostile review classification.

No Level 2 experiment is complete until it has:

- a document in `docs/03_experiments/`;
- a result in `docs/04_results/`;
- a decision-log update;
- a roadmap update.

`exp_003` satisfied all four for Level 2A.

## Files Already Produced And Still Needed

The Level 2A phenomenological closure files exist and are current:

```text
docs/02_theory/040_qfuds_phenomenological_perturbations.md
docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md
docs/04_results/030_result_003_phenomenological_perturbation_closure.md
docs/05_next_steps/010_perturbation_gate.md
```

Physical Level 2B files do not exist yet because Level 1.5 is not resolved and a
physical phase-transfer derivation has not been done. Names will be assigned when
Level 2B is unblocked.

## Refactoring Rule

Do not rewrite history to hide failed branches. The repository should preserve that `exp_001` and `exp_002` were background-level filters.

Do make active documents explicit about the sequence:

```text
background filters -> Level 1.5 phase-transfer physicality -> perturbation equations -> Boltzmann code -> observables
```

## README Update Rule

The README should remain a reader-facing overview. It should point to:

- `PROJECT.md` for documentation control and validation order;
- `docs/00_project_overview.md` for project status;
- `docs/00_project/verification_guide.md` for reproducible checks;
- `docs/05_next_steps/000_roadmap.md` for current blockers.
