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
  - result_006_literature_timing_support_audit
  - qfuds_level_1_5_equivalence_source_perturbation_audit
  - qfuds_level_1_5_transfer_four_vector_derivation_attempt
  - qfuds_strong_gravity_source_mechanism_audit
  - audit_2026_06_12_foam_sector_to_gamma_derivation_feasibility_result
  - audit_2026_06_18_candidate_equation_triage_closeout
  - plan_2026_06_18_public_bridge_lineage_ko
next_gate: observer mode; retained branch demoted; public bridge is provenance-only; no Level 2B without all five admission-rule items
last_updated: 2026-06-18
---

# QFUDS Research Roadmap

Date: 2026-06-09

## Status Key

- `completed`: implemented or documented at the current required level.
- `in progress`: partially implemented or drafted, but not sufficient for the next validation gate.
- `blocked`: cannot proceed responsibly until an upstream assumption or implementation is defined.

## Current Posture: Observer Mode

As of 2026-06-11 the project is in observer mode.

The retained `Gamma(a)` branch is demoted to phenomenological interacting
vacuum, Physical-QFUDS Level 2B is blocked, and the Source-X black-hole entropy
/ Chen-Gamma lane was found ineligible for Level 2B because all five
admission-rule items remain unsatisfied. See the Source-X
[Level 2B admission eligibility review](../wiki/research/investigations/source_x/conclusions/049_level2b_eligibility_review_and_observer_mode.md).
The later
[foam-sector-to-Gamma feasibility result](../wiki/research/investigations/source_x/conclusions/050_foam_sector_to_gamma_derivation_feasibility_result.md)
made the original forward foam-sector route explicit and found it not ready for
derivation because the minimum mathematical objects are still missing.

In observer mode:

- No new physical-QFUDS branch is opened and no Level 2B work is performed.
- Retained `Gamma(a)` is not rescued by wording.
- The surviving falsifiable hook is the dark-energy timing signature (`w0 ~= -1`,
  `|wa| > 0`, retained timing peak near `z ~= 2`). It is tracked against external
  observations, not derived in-repository.
- Watchlist: DESI DR3, Euclid, Roman, Rubin/LSST, the CCBH debate, and entropic
  or IV/IDE reconstruction products.

Observer mode is exited only when the future-branch admission rule is satisfied,
or when new data isolate a `z ~= 2` dark-sector interaction feature that known
families cannot absorb. This posture is recorded as audit success, not model
success or failure: the structure-era timing intuition is retained, its
explanatory candidates already exist in the literature, and current evidence
cannot select among them or assert new physics.

As of 2026-06-18, a galaxy/cosmic-web coarse-grained spacetime hypothesis may
be tracked only as a future candidate lane. In that lane, `xi_gal` must be
declared before model-facing use of NASA/LAMBDA, BAO, LSS, CMB, or retained
timing targets. Until a candidate supplies the admission-rule items below,
`xi_gal` is a preregistered effective coarse-graining input, not a derived
foam scale, physical source, or roadmap upgrade.

Workflow boundary: this roadmap applies the
[Research Asset and Product Workflow](../../.agent/workflows/research-asset-product-workflow.md)
only to preserve source-state boundaries. No new external asset, table, PDF,
or product claim is introduced here. Existing baseline states remain
`asset_cached`, `manual_structured_extract`, `asset_extracted_not_digitized`,
and `direct_table` as recorded in the baseline-reference chain.

## Levels

| Level | Topic | Status | Current Evidence | Next Gate |
| --- | --- | --- | --- | --- |
| 0 | literature position | completed | [docs/02_theory/900_qfuds_research_report.md](../02_theory/900_qfuds_research_report.md) | Keep comparison current as model changes |
| 1 | background validation | completed | [docs/04_results/000_result_000_lcdm_baseline.md](../04_results/000_result_000_lcdm_baseline.md), [docs/04_results/010_result_001_gamma_scan.md](../04_results/010_result_001_gamma_scan.md), [docs/04_results/020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md), `outputs/`, `tests/test_gamma_v03.py` | Treat experiment 002 as provenance; audit only the retained collapse/information-production shape |
| 1.5 | retained phase-transfer physicality | completed for retained branch | [docs/02_theory/015_qfuds_level_1_5_equivalence_source_perturbation_audit.md](../02_theory/015_qfuds_level_1_5_equivalence_source_perturbation_audit.md), [docs/02_theory/015_qfuds_level_1_5_transfer_four_vector_derivation_attempt.md](../02_theory/015_qfuds_level_1_5_transfer_four_vector_derivation_attempt.md), [docs/04_results/015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md), `qfuds/gamma_laws.py` | Retained branch demoted to phenomenological interacting vacuum; future physical branches must pass the admission rule before reopening [Level 1.5](../wiki/glossary/repository_levels.md) or Level 2B |
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
7. If continuing the phenomenological IV/IDE track, do not use retained
   structure-era timing as an informative prior from the current table-level
   literature audit alone. Experiment 006 found it allowed by Escamilla 2023
   table products but not informative; stronger posterior products,
   digitization with uncertainty, or a likelihood-level prior test would be
   required.
8. If exploring the galaxy/cosmic-web coarse-grained spacetime hypothesis,
   treat `xi_gal` as a preregistered input and run the
   candidate-equation template first. Do not treat galaxy-scale language as
   `X`, `Q^nu`, phase-B pressure, `delta Q`, or known-model distinction.
9. If producing public-facing black-hole information bridge material, route it
   through [020_public_bridge_lineage_plan_ko.md](020_public_bridge_lineage_plan_ko.md)
   and keep it as provenance only. Do not turn black-hole evaporation,
   remnant, or information-preservation language into a physical source claim
   without the admission-rule items.

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
| `exp_006` | literature timing-support audit | retained timing is allowed by Escamilla 2023 table-level products but not informative enough for prior use |

## Blockers

1. The retained `Gamma(a) proportional to dF_coll/dln a` source relation failed physical Level 1.5 promotion.
2. The broader DM-to-DE phase-transition hypothesis remains open but has no accepted physical transfer law in the repository.
3. The forward foam-sector-to-`Gamma(a)` route is blocked at the minimum-object
   level: no non-circular foam-sector state variable, calculable phase
   definitions, replacement transition object, or foam-sector equation set has
   been supplied.
4. No future physical branch has supplied the required `X`, `Q^nu`, phase-B vacuum-pressure rationale, `delta Q`, or known-model distinction.
5. No physical Level 2B perturbation closure relation exists.
6. No Boltzmann-code interface exists.
7. No likelihood comparison against CMB, BAO, SN, or matter power data exists.
8. No posterior-product, digitized-uncertainty, or likelihood-level evidence
   currently supports retained timing as an informative IV/IDE prior.
9. The galaxy/cosmic-web scale hypothesis has not supplied an effective
   stress tensor, geometry correction, averaging equation, conservation rule,
   perturbation route, or escape observable beyond known coarse-graining,
   EFTofLSS, halo-model, backreaction, or modified-gravity sinks.

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

For the galaxy/cosmic-web coarse-grained spacetime hypothesis, the first
allowed re-entry is a template-filled candidate that states:

- `xi_gal =` with units and whether it is an input, derived output,
  calibrated input, or unknown;
- whether the correction lives on the geometry side or stress-energy side;
- the effective equation, stress tensor, or averaging relation produced after
  coarse-graining;
- why the route does not reduce first to LCDM+EFTofLSS, halo modeling,
  backreaction, screened modified gravity, effective `w(a)`, or IV/IDE.
