# QFUDS Research Roadmap

Date: 2026-06-08

## Status Key

- `completed`: implemented or documented at the current required level.
- `in progress`: partially implemented or drafted, but not sufficient for the next validation gate.
- `blocked`: cannot proceed responsibly until an upstream assumption or implementation is defined.

## Levels

| Level | Topic | Status | Current Evidence | Next Gate |
| --- | --- | --- | --- | --- |
| 0 | literature position | completed | `docs/02_theory/qfuds_research_report.md` | Keep comparison current as model changes |
| 1 | background validation | completed | `docs/04_results/result_000_lcdm_baseline.md`, `docs/04_results/result_001_gamma_scan.md`, `docs/04_results/result_002_entropy_information_gate.md`, `outputs/`, `tests/test_gamma_v03.py` | Continue only the collapse/information-production branch |
| 2 | perturbation equations | in progress | assumptions noted in `qfuds/growth.py` and theory docs | Specify phase-A, phase-B, and transfer perturbations |
| 3 | CLASS integration | blocked | none | Requires Level 2 equations |
| 4 | CMB comparison | blocked | none | Requires CLASS/CAMB implementation |
| 5 | matter power spectrum | blocked | growth proxy only | Requires perturbation solver or Boltzmann output |
| 6 | DESI/Euclid comparison | blocked | no likelihood pipeline | Requires validated background plus perturbation predictions |

## Immediate Work

1. Follow `docs/05_next_steps/perturbation_gate.md`.
2. Recompute `dF_coll/dln a` using self-consistent QFUDS growth `D(a)`.
3. Fix the collapse mass threshold `M` from a physical criterion.
4. Define phase-A, phase-B, and transfer perturbations.
5. Test the redshift-ratio relation between `w(a)` and `f sigma8(a)`.
6. Kill the branch if the relation fails or perturbations are unstable.

## Completed Background Validations

| Experiment | Purpose | Result |
| --- | --- | --- |
| `exp_000` | zero-transfer LCDM baseline | control passed; not novel |
| `exp_001` | Gamma-law background scan | constant and ungated growth-driven laws rejected |
| `exp_002` | entropy/information-source gate | only collapse/information production promoted to Level 2 |

## Blockers

1. No microphysical action or fixed collapse mass threshold.
2. No perturbation closure relation.
3. No Boltzmann-code interface.
4. No likelihood comparison against CMB, BAO, SN, or matter power data.

## Rule For New Ideas

New speculative mechanisms should not be added to the main model unless they produce at least one of:

1. a new equation;
2. a new falsifiable observable;
3. a changed viability decision;
4. a reproducible experiment with code and outputs.
