# QFUDS Research Roadmap

Date: 2026-06-08

## Status Key

- `completed`: implemented or documented at the current required level.
- `in progress`: partially implemented or drafted, but not sufficient for the next validation gate.
- `blocked`: cannot proceed responsibly until an upstream assumption or implementation is defined.

## Levels

| Level | Topic | Status | Current Evidence | Next Gate |
| --- | --- | --- | --- | --- |
| 0 | literature position | completed | `docs/qfuds_research_report.md` | Keep comparison current as model changes |
| 1 | background toy model | completed | `qfuds/background.py`, `scripts/run_minimal_model.py`, `outputs/qfuds_gamma0_beta0.csv` | Use as baseline only |
| 1.5 | Gamma-law background scan | completed | `docs/qfuds_v0_3_gamma_laws.md`, `outputs/`, `tests/test_gamma_v03.py` | Promote only surviving laws to perturbation tests |
| 2 | perturbation equations | in progress | assumptions noted in `qfuds/growth.py` and theory docs | Specify phase-A, phase-B, and transfer perturbations |
| 3 | CLASS integration | blocked | none | Requires Level 2 equations |
| 4 | CMB comparison | blocked | none | Requires CLASS/CAMB implementation |
| 5 | matter power spectrum | blocked | growth proxy only | Requires perturbation solver or Boltzmann output |
| 6 | DESI/Euclid comparison | blocked | no likelihood pipeline | Requires validated background plus perturbation predictions |

## Immediate Work

1. Write perturbation equations in a new theory note.
2. Define whether phase B is exactly smooth or weakly perturbed.
3. Define the transfer perturbation variable `delta_Q`.
4. Choose one surviving v0.3 proxy as the first perturbation target.
5. Add tests that prevent background-only results from being described as CMB-safe.

## Blockers

1. No microphysical action or derived `Gamma(a)`.
2. No perturbation closure relation.
3. No Boltzmann-code interface.
4. No likelihood comparison against CMB, BAO, SN, or matter power data.

## Rule For New Ideas

New speculative mechanisms should not be added to the main model unless they produce at least one of:

1. a new equation;
2. a new falsifiable observable;
3. a changed viability decision;
4. a reproducible experiment with code and outputs.
