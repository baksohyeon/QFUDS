# QFUDS Project Documentation Control

Date: 2026-06-08

This file is the entry point for maintaining the QFUDS research record.

QFUDS is not a confirmed theory. The repository is a staged attempt to turn a speculative dark-sector idea into equations, reproducible tests, hostile reviews, and decisions.

## Execution Order

The validation order is sequential:

```text
Level 0: literature position
Level 1: background toy model
Level 2: perturbation equations
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

These are not separate theory versions and not observational successes. They are filters before Level 2 because several candidate transfer laws needed to be killed before perturbation work.

Current stop line:

```text
Level 2 perturbation theory is not complete.
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

In progress:

- Level 2 perturbation equations.

Blocked:

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
docs/02_theory/qfuds_v0_1.md
docs/02_theory/qfuds_v0_2.md
docs/02_theory/qfuds_v0_3.md
docs/03_experiments/exp_000_lcdm_baseline.md
docs/03_experiments/exp_001_gamma_scan.md
docs/03_experiments/exp_002_entropy_information_gate.md
docs/04_results/result_000_lcdm_baseline.md
docs/04_results/result_001_gamma_scan.md
docs/04_results/result_002_entropy_information_gate.md
docs/05_next_steps/roadmap.md
docs/05_next_steps/perturbation_gate.md
```

Historical/provenance documents:

```text
docs/01_origin/concept_origin.md
docs/00_project/research_program.md
docs/00_project/qfuds_ko.md
docs/02_theory/qfuds_research_report.md
```

## Naming Convention

Use this convention:

```text
theory version: qfuds_v0_1, qfuds_v0_2, qfuds_v0_3
experiment: exp_000, exp_001, exp_002
result: result_000, result_001, result_002
```

Do not name experiments as new `v0.x` theory versions.

## What Experiment 002 Is

`docs/04_results/result_002_entropy_information_gate.md` is not a perturbation result.

It is a background-level entropy/information-source scan. It asks whether the phase-transfer shape can be tied to a concrete source such as horizon information, HBM/KL gravitational entropy, black-hole entropy, or Press-Schechter information production.

Experiment 002 keeps only the collapse/information-production branch as a Level 2 perturbation target.

## What Level 2 Must Produce

Level 2 must produce new theory and experiment documents before any CLASS/CAMB work starts.

Required Level 2 outputs:

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

## Files Still Needed

For the next phase:

```text
docs/02_theory/qfuds_perturbations.md
docs/03_experiments/exp_003_perturbation_prescriptions.md
docs/04_results/result_003_perturbation_prescriptions.md
```

These files do not exist yet because the perturbation work has not been done.

## Refactoring Rule

Do not rewrite history to hide failed branches. The repository should preserve that `exp_001` and `exp_002` were background-level filters.

Do make active documents explicit about the sequence:

```text
background filters -> perturbation equations -> Boltzmann code -> observables
```

## README Update Rule

The README should remain a reader-facing overview. It should point to:

- `PROJECT.md` for documentation control and validation order;
- `docs/00_project_overview.md` for project status;
- `docs/00_project/verification_guide.md` for reproducible checks;
- `docs/05_next_steps/roadmap.md` for current blockers.
