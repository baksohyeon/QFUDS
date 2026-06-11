---
doc_id: qfuds_branch_graph
title: QFUDS Branch Dependency Graph
doc_type: summary
stage: "2"
status: completed
evidence_role: audit
depends_on:
  - roadmap
  - concept_survival_audit
  - safe_future_branch_candidates
  - wiki_governance_001_physical_branch_summary
next_gate: use graph for routing only; do not open physical Level 2B without admission-rule items
last_updated: 2026-06-11
---

# QFUDS Branch Dependency Graph

## Status Boundary

This file maps branch relationships for handoff and routing. It is not the
roadmap and does not change project status. Current project status remains
governed by [docs/05_next_steps/000_roadmap.md](../../05_next_steps/000_roadmap.md).

Physical [Level 2B](../glossary/repository_levels.md) remains blocked. This graph cannot admit a branch into Level
2B.

## Current Retained-Branch Classification

Current retained-branch classification: Phenomenological IV/IDE; Not Yet A
Physical Model.

This classification applies to the current retained branch only. It does not
define the entire QFUDS research program.

P1 survives only as Level 2A phenomenological interacting-vacuum closure. P2
failed at retained amplitude. Physical Level 2B remains blocked.

## Graph Reading Rules

- `status` records current repository classification, not truth outside the
  repository.
- `evidence anchor` points to existing source docs and should not be expanded
  into a duplicate literature summary.
- `kill reason` is used only where a lane was rejected or failed under a stated
  test.
- `demotion reason` is used where a lane remains useful but lost stronger
  physical status.
- `surviving descendant` names the narrower lane that can still be used.

## Branch Dependency Table

| parent idea                             | derived branch                                                | status                                     | evidence anchor                                                                                                                                                                                                                                                 | kill reason, if rejected                                | demotion reason, if demoted                                                            | surviving descendant, if any                                     |
| --------------------------------------- | ------------------------------------------------------------- | ------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | -------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Landauer / information motivation       | information-cost origin trail                                 | provenance                                 | [concept_origin.md](../../01_origin/concept_origin.md), [concept_survival_audit.md](../../00_project/concept_survival_audit.md)                                                                                                                                 | none                                                    | does not derive a cosmological source, transfer law, or phase-B pressure               | information-flow motivation                                      |
| black-hole information motivation       | strong-gravity source audit                                   | candidate source audit only                | [015_qfuds_strong_gravity_source_mechanism_audit.md](../../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md)                                                                                                                                        | none                                                    | black-hole entropy or growth does not yet define stress-energy transfer                | black-hole-coupled source audit lane                             |
| white-hole / remnant motivation         | remnant-sector audit                                          | DM-only or defect-sector audit             | [concept_survival_audit.md](../../00_project/concept_survival_audit.md), [015_qfuds_strong_gravity_source_mechanism_audit.md](../../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md)                                                               | rejected as current DE source                           | produces no accepted smooth `w ~= -1` phase-B transfer                                 | remnant-sector DM-only lane                                      |
| quantum foam motivation                 | unified foam dark-sector question                             | open but unsupported                       | [research_program.md](../../00_project/research_program.md), [concept_survival_audit.md](../../00_project/concept_survival_audit.md)                                                                                                                            | none                                                    | no microscopic degree of freedom, action, stress tensor, or perturbation route         | future physical branch only if admission rule is met             |
| two-phase dark sector background        | phase A plus phase B bookkeeping                              | retained as model language                 | [000_qfuds_v0_2_two_phase_background.md](../../02_theory/000_qfuds_v0_2_two_phase_background.md)                                                                                                                                                                | none                                                    | free `Gamma(a)` reduces toward known interacting dark-sector phenomenology             | phenomenological IV/IDE branch                                   |
| `Gamma(a)` transfer prototype           | retained source-shaped timing profile                         | prototype phenomenology                    | [015_result_001_5_phase_transfer_physicality.md](../../04_results/015_result_001_5_phase_transfer_physicality.md), [030_result_005_timing_prior_usefulness.md](../../04_results/030_result_005_timing_prior_usefulness.md)                                      | not killed as timing                                    | failed as physical source derivation                                                   | IV/IDE timing-prior lane                                         |
| collapse / information-production proxy | `dF_coll/dln(a)` shaped transfer                              | provenance plus timing feature             | [015_qfuds_level_1_5_equivalence_source_perturbation_audit.md](../../02_theory/015_qfuds_level_1_5_equivalence_source_perturbation_audit.md), [015_result_001_5_phase_transfer_physicality.md](../../04_results/015_result_001_5_phase_transfer_physicality.md) | failed physical Level 1.5 promotion                     | supplies timing, not a physical source                                                 | retained timing feature                                          |
| phenomenological IV/IDE retained branch | P1 interacting-vacuum closure                                 | retained Level 2A phenomenology            | [030_result_003_phenomenological_perturbation_closure.md](../../04_results/030_result_003_phenomenological_perturbation_closure.md), [030_result_004_p1_model_family_positioning.md](../../04_results/030_result_004_p1_model_family_positioning.md)            | none                                                    | not independent physical QFUDS                                                         | IV/IDE phenomenology                                             |
| P1 perturbation closure                 | phase-A-comoving interacting vacuum with `deltaQ = Q delta_A` | survives Level 2A only                     | [030_qfuds_phenomenological_perturbations.md](../../02_theory/030_qfuds_phenomenological_perturbations.md), [030_result_003_phenomenological_perturbation_closure.md](../../04_results/030_result_003_phenomenological_perturbation_closure.md)                 | none                                                    | microphysics and Level 2B still absent                                                 | stable phenomenological closure                                  |
| P2 regularized-fluid closure            | near-vacuum phase-B fluid                                     | failed at retained amplitude               | [030_result_003_phenomenological_perturbation_closure.md](../../04_results/030_result_003_phenomenological_perturbation_closure.md)                                                                                                                             | unstable at retained amplitude for all tested `k` modes | none                                                                                   | none for retained branch                                         |
| IV/IDE timing-prior lane                | retained structure-era timing comparison                      | allowed but not informative at table level | [030_result_005_timing_prior_usefulness.md](../../04_results/030_result_005_timing_prior_usefulness.md), [030_result_006_literature_timing_support_audit.md](../../04_results/030_result_006_literature_timing_support_audit.md)                                | none                                                    | current table products do not support informative prior use                            | stronger posterior, digitization, or likelihood-level prior test |
| black-hole-coupled source audit lane    | black-hole production or mass-growth source candidate         | safe audit lane                            | [015_qfuds_strong_gravity_source_mechanism_audit.md](../../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md), [010_safe_future_branch_candidates.md](../../05_next_steps/010_safe_future_branch_candidates.md)                                      | none                                                    | not admitted without full `X`, `Q^nu`, phase-B, `delta Q`, and known-model distinction | candidate source audit                                           |
| HDE reduction-test lane                 | horizon-scale or holographic route                            | safe reduction-test lane                   | [015_qfuds_strong_gravity_source_mechanism_audit.md](../../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md), [010_safe_future_branch_candidates.md](../../05_next_steps/010_safe_future_branch_candidates.md)                                      | none                                                    | likely known-model behavior unless distinction is derived                              | HDE / interacting-vacuum comparison                              |
| remnant-sector DM-only lane             | compact remnant or defect sector                              | safe DM-only audit lane                    | [015_qfuds_strong_gravity_source_mechanism_audit.md](../../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md), [010_safe_future_branch_candidates.md](../../05_next_steps/010_safe_future_branch_candidates.md)                                      | rejected as current DE source                           | no smooth vacuum-pressure phase derived                                                | optional remnant/defect audit                                    |
| causal-set Lambda comparison lane       | stochastic or causal-set Lambda comparison                    | separate DE comparison                     | [010_safe_future_branch_candidates.md](../../05_next_steps/010_safe_future_branch_candidates.md)                                                                                                                                                                | none                                                    | not a DM-to-DE phase-transfer branch by itself                                         | adjacent DE comparison                                           |

## Landauer / Information Motivation Lane

Parent idea: Landauer made information physical in the origin trail.

Derived branch: information-cost and conservation motivation.

Status: provenance and conceptual constraint.
It motivates treating information as a physically meaningful quantity.
However, it does not by itself derive X, Q^nu, phase-B pressure, delta Q, or a known-model distinction.

## Black-Hole Information Motivation Lane

Parent idea: black holes are extreme information-processing systems.

Derived branch: strong-gravity source audits using black-hole entropy, mass
growth, or coupled-vacuum histories.

Status: safe audit lane only. It must not become a physical branch unless the
source defines stress-energy transfer and perturbations.

## White-Hole / Remnant Motivation Lane

Parent idea: delayed-release, tunneling, or remnant pictures from the
black-hole information trail.

Derived branch: remnant or defect-sector candidates.

Status: DM-only or provenance unless smooth vacuum-pressure phase-B behavior is
derived. This lane is not a current dark-energy source.

## Quantum Foam Motivation Lane

Parent idea: quantum spacetime foam as the possible common medium.

Derived branch: DM and DE as two effective macroscopic phases.

Status: open but unsupported. No current document derives a microscopic foam
degree of freedom, action, stress tensor, or physical perturbation closure.

## Two-Phase Dark Sector Background Lane

Parent idea: split the dark sector into phase A and phase B.

Derived branch: runnable background equations with an LCDM null limit.

Status: retained as bookkeeping and test scaffolding. Background viability does
not establish physical QFUDS or Level 2B.

## Gamma(a) Transfer Prototype Lane

Parent idea: make phase transfer explicit through `Gamma(a)`.

Derived branch: retained source-shaped timing prototype.

Status: prototype phenomenology. It exposed timing constraints but is not a
derived physical law.

## Collapse / Information-Production Proxy Lane

Parent idea: structure formation or information production might shape transfer
timing.

Derived branch: retained `dF_coll/dln(a)` timing profile.

Status: demoted. It supplies a timing fingerprint, not a physical source
derivation.

## Phenomenological IV/IDE Retained Branch

Parent idea: retained P1 can be mapped to interacting vacuum /
time-dependent IDE.

Derived branch: Level 2A phenomenological closure and model-family positioning.

Status: retained as phenomenology only. It is not independent physical QFUDS.

## P1 Perturbation Closure Lane

Parent idea: choose a declared transfer frame and `deltaQ` closure.

Derived branch: phase-A-comoving interacting vacuum with `deltaQ = Q delta_A`.

Status: stable in the Level 2A audit only. This is not microphysics, novelty,
CMB viability, or matter-power viability.

## P2 Regularized-Fluid Closure Lane

Parent idea: regularize phase B as a near-vacuum fluid.

Derived branch: P2 with `w_B=-0.999` and fluid perturbations.

Status: failed at retained amplitude. The retained branch has no surviving P2
descendant.

## IV/IDE Timing-Prior Lane

Parent idea: retained timing may be useful as an interpretable IV/IDE timing
prior.

Derived branch: Exp005/Exp006 timing-prior and literature-support audits.

Status: possible but weak. Exp006 says allowed but not informative at table
level; stronger posterior products, digitization with uncertainty, or
likelihood-level tests are required.

## Black-Hole-Coupled Source Audit Lane

Parent idea: black-hole production, mass growth, or coupled vacuum could define
a candidate `X`.

Derived branch: source audit only.

Status: safe if it stays an audit. It cannot open Level 2B unless it supplies
all admission-rule items.

## HDE Reduction-Test Lane

Parent idea: horizon or holographic energy relations might explain phase B.

Derived branch: known-model reduction test.

Status: safe as comparison. It must test whether QFUDS reduces to known HDE or
interacting vacuum instead of assuming novelty.

## Remnant-Sector DM-Only Lane

Parent idea: remnants or defects may contribute to dark matter-like behavior.

Derived branch: compact remnant or defect-sector audit.

Status: safe as DM-only audit. It must not be used as a dark-energy source
without smooth vacuum-pressure stress-energy.

## Causal-Set Lambda Comparison Lane

Parent idea: stochastic or causal-set Lambda behavior may be an adjacent DE
comparison.

Derived branch: separate DE comparison.

Status: safe comparison only. It is not a DM-to-DE phase-transfer branch by
itself.

## Safe Routing Summary

Allowed next work must stay in one of these lanes:

- phenomenological IV/IDE timing-prior tests;
- black-hole-coupled source audits;
- HDE reduction tests;
- remnant-sector audits as DM-only, not DE;
- causal-set Lambda comparisons as separate DE comparisons.

No safe lane changes roadmap status by itself.

## Source Documents

- [docs/05_next_steps/000_roadmap.md](../../05_next_steps/000_roadmap.md)
- [docs/05_next_steps/010_safe_future_branch_candidates.md](../../05_next_steps/010_safe_future_branch_candidates.md)
- [docs/00_project/concept_survival_audit.md](../../00_project/concept_survival_audit.md)
- [docs/02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md](../../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md)
- [docs/02_theory/030_qfuds_phenomenological_perturbations.md](../../02_theory/030_qfuds_phenomenological_perturbations.md)
- [docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md](../../03_experiments/030_exp_003_phenomenological_perturbation_closure.md)
- [docs/04_results/030_result_003_phenomenological_perturbation_closure.md](../../04_results/030_result_003_phenomenological_perturbation_closure.md)
- [docs/04_results/030_result_004_p1_model_family_positioning.md](../../04_results/030_result_004_p1_model_family_positioning.md)
- [docs/wiki/governance/001_physical_branch_admission_summary.md](../governance/001_physical_branch_admission_summary.md)
- [docs/wiki/governance/003_blocked_admission_rule_gate.md](../governance/003_blocked_admission_rule_gate.md)
- [docs/wiki/research/literature/README.md](../research/literature/README.md)
- [docs/wiki/research/literature/index.csv](../research/literature/index.csv)

## No-Roadmap-Upgrade Confirmation

This graph is a routing map, not a status authority. It does not change roadmap
status, does not upgrade retained `Gamma(a)`, does not create a physical branch,
and cannot admit any branch into Physical-QFUDS Level 2B.
