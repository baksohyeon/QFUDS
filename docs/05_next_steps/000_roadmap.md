---
doc_id: roadmap
title: QFUDS Research Roadmap
doc_type: roadmap
stage: "1.5"
status: in_progress
evidence_role: ssot
depends_on:
  - result_001_5_phase_transfer_physicality
  - result_005_timing_prior_usefulness
  - qfuds_level_1_5_equivalence_source_perturbation_audit
  - qfuds_level_1_5_transfer_four_vector_derivation_attempt
  - qfuds_strong_gravity_source_mechanism_audit
next_gate: retained branch demoted; future physical-QFUDS branches must pass the admission rule before Level 2B
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
| 1.5 | retained phase-transfer physicality | completed for retained branch | [docs/02_theory/015_qfuds_level_1_5_equivalence_source_perturbation_audit.md](../02_theory/015_qfuds_level_1_5_equivalence_source_perturbation_audit.md), [docs/02_theory/015_qfuds_level_1_5_transfer_four_vector_derivation_attempt.md](../02_theory/015_qfuds_level_1_5_transfer_four_vector_derivation_attempt.md), [docs/04_results/015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md), `qfuds/gamma_laws.py` | Retained branch demoted to phenomenological interacting vacuum; future physical branches must pass the admission rule before reopening Level 1.5 or Level 2B |
| 2A | phenomenological perturbation closure | completed | [docs/02_theory/030_qfuds_phenomenological_perturbations.md](../02_theory/030_qfuds_phenomenological_perturbations.md), [docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md](../03_experiments/030_exp_003_phenomenological_perturbation_closure.md), [docs/04_results/030_result_003_phenomenological_perturbation_closure.md](../04_results/030_result_003_phenomenological_perturbation_closure.md), `outputs/exp003_stability_diagnostics.csv` | P2 failed at retained amplitude; P1 survives only as phenomenological interacting vacuum |
| 2B | physical perturbation closure | blocked | retained branch failed Level 1.5 physical promotion | Requires a new physical-QFUDS branch that first provides `X`, `Q^nu`, phase-B vacuum-pressure rationale, `delta Q`, and known-model distinction |
| 3 | CLASS integration | blocked | none | Requires a stable Level 2A closure at minimum; physical claims require Level 2B |
| 4 | CMB comparison | blocked | none | Requires CLASS/CAMB implementation |
| 5 | matter power spectrum | blocked | growth proxy only | Requires perturbation solver or Boltzmann output |
| 6 | DESI/Euclid comparison | blocked | no likelihood pipeline | Requires validated background plus perturbation predictions |

## Immediate Work

1. Treat the retained collapse/information-production `Gamma(a)` branch as demoted to phenomenological interacting-vacuum status.
2. Do not interpret that demotion as falsifying the broader DM-to-DE phase-transition hypothesis or all future physical QFUDS variants.
3. Treat the P2 regularized-fluid closure as failed at the retained amplitude.
4. Treat the P1 interacting-vacuum closure as Level 2A phenomenology only.
5. Do not open a new physical-QFUDS branch unless it satisfies the future-branch admission rule below.
6. Do not advance to physical Level 2B without a physical transfer derivation.
7. If continuing the phenomenological IV/IDE track, treat retained
   structure-era timing only as a possible prior-compression target and compare
   it against actual reconstructed or tomographic IV/IDE coupling histories
   before using it as a prior.

Do not treat Level 2A as derived QFUDS physics. Do not start Level 2B, CLASS/CAMB,
CMB, matter-power, or survey-likelihood claims until the relevant upstream gate
is satisfied.

## Completed Background Validations

| Experiment | Purpose | Result |
| --- | --- | --- |
| `exp_000` | zero-transfer LCDM baseline | control passed; not novel |
| `exp_001` | Gamma-law background scan | constant and ungated growth-driven laws rejected |
| `exp_002` | entropy/information-source gate | demoted to provenance; retained shape failed Level 1.5 physical promotion and remains phenomenological |
| `exp_005` | timing-prior usefulness audit | retained timing is a possible IV/IDE prior-compression target, not a physical source or new model family |

## Blockers

1. The retained `Gamma(a) proportional to dF_coll/dln a` source relation failed physical Level 1.5 promotion.
2. The broader DM-to-DE phase-transition hypothesis remains open but has no accepted physical transfer law in the repository.
3. No future physical branch has supplied the required `X`, `Q^nu`, phase-B vacuum-pressure rationale, `delta Q`, or known-model distinction.
4. No physical Level 2B perturbation closure relation exists.
5. No Boltzmann-code interface exists.
6. No likelihood comparison against CMB, BAO, SN, or matter power data exists.

## Rule For New Ideas

New speculative mechanisms should not be added to the main model unless they produce at least one of:

1. a new equation;
2. a new falsifiable observable;
3. a changed viability decision;
4. a reproducible experiment with code and outputs.

## Future-Branch Admission Rule

No new physical-QFUDS branch should be opened unless it provides, at minimum:

- `X =`
- `Q^nu =`
- `why phase B has w ~= -1 =`
- `delta Q route =`
- `known-model distinction =`
