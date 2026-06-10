---
doc_id: audit_2026_06_10_phase3_qnu_derivation_attempt
title: "2026-06-10 Phase 3 Q^nu Derivation Attempt"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_phase3_qnu_derivation_attempt_plan
  - audit_2026_06_10_phase2_candidate_selection_closeout
  - audit_2026_06_10_black_hole_coupled_source_audit
  - audit_2026_06_10_black_hole_coupled_literature_search
  - audit_2026_06_10_structure_era_activation_literature
  - roadmap
  - repository_levels_glossary
  - missing_physics_map
  - blocked_admission_rule_checkpoint
next_gate: no physical branch; Phase 3 is data-product blocked and no candidate supplies Q^nu
last_updated: 2026-06-10
---

# 2026-06-10 Phase 3 Q^nu Derivation Attempt

## Purpose

This document executes the approved
[2026-06-10 Phase 3 Q^nu Derivation Attempt Plan](../plans/030_phase3_qnu_derivation_attempt_plan.md).

It asks whether the retained Phase 2 candidate quantities can support a
physically meaningful covariant transfer vector `Q^nu`.

The only evaluated candidate lanes are:

- Lane A: black-hole mass growth history.
- Lane B: `dS_BH / dln(a)`.

This is a feasibility audit result. It is not a derivation.

## Status Boundary

Current retained-branch classification:
Phenomenological IV/IDE; Not Yet A Physical Model.

This classification applies to the current retained branch only.

Gamma(a) remains a prototype phenomenological transfer profile.

This audit determines whether a physically meaningful Q^nu can exist from the
checked repository evidence.

It does not assume that one already exists.

This audit does not:

- open Physical-QFUDS [Level 2B](../../../../glossary/repository_levels.md);
- modify roadmap status;
- claim black holes explain `Gamma(a)`;
- treat `Gamma(a)` as proven;
- introduce a new primary Source-X candidate;
- treat a conservation-compatible ansatz as physical admission.

## Evidence Scanned

- [2026-06-10 Phase 2 Candidate Selection Closeout](029_phase2_candidate_selection_closeout.md)
- [2026-06-10 Black-Hole-Coupled Source Audit](021_phase2_black_hole_coupled_source_audit.md)
- [2026-06-10 Black-Hole-Coupled Literature Search Audit](../coverage/022_phase2_black_hole_coupled_literature_search_audit.md)
- [2026-06-10 Structure-Era Activation Literature Audit](../coverage/024_phase2_structure_era_activation_literature_audit.md)
- [2026-06-10 Source-X Audit](011_phase1_source_x_audit.md)
- [Missing Physics Map](../../../../checkpoints/missing_physics_map.md)
- [Blocked Admission Rule](../../../../checkpoints/blocked-admission-rule.md)
- [Repository Levels](../../../../glossary/repository_levels.md)
- [Roadmap](../../../../../05_next_steps/000_roadmap.md)

## Lane A: Black-Hole Mass Growth History

| Requirement | Result |
| --- | --- |
| source quantity definition | Partial only. The candidate could be `rho_BH(a)` or `d rho_BH / dln(a)`, but the repository has no selected QFUDS-ready product or source convention. |
| units | Possible units are mass density, energy density, or density per `dln(a)`. The audit cannot fix units because no source product or transfer convention is selected. |
| normalization requirements | Failed. No repository rule fixes amplitude, reference density, sign convention, or redshift range before comparison to retained `Gamma(a)`. |
| background transfer requirements | Failed. Existing records say mass growth can be a timing replacement or constraint only; the repository does not derive retained `Gamma(a)` from mass growth. |
| stress-energy conservation requirements | Failed. No source-derived split of `nabla_mu T_A^{mu nu} = -Q^nu` and `nabla_mu T_B^{mu nu} = Q^nu` exists for this lane. |
| frame choice requirements | Failed. No phase-A, phase-B, total-fluid, or black-hole-population transfer frame is declared. |
| four-velocity assumptions | Failed. No repository evidence identifies whether `u^nu` should be phase A, phase B, total matter, or black-hole population flow. |
| perturbation requirements | Failed. No local mass-growth perturbation, gauge choice, or stability route is defined. |
| `delta Q` implications | Failed. Without local source perturbations and a declared transfer frame, `delta Q` is unknown. |
| known-model reduction risks | Very high. If mass growth sources dark energy, the lane reduces toward cosmologically coupled black-hole dark energy or black-hole-coupled DE unless QFUDS adds a distinct equation or observable. |

Lane A outcome: `data_product_blocked`.

Reason: the lane might become testable only after a selected `rho_BH(a)` or
`d rho_BH/dln(a)` product, normalization, and source-to-transfer equation exist.
Current repository evidence does not supply a physically meaningful `Q^nu`.

## Lane B: `dS_BH / dln(a)`

| Requirement | Result |
| --- | --- |
| source quantity definition | Partial only. The candidate could be `X = dS_BH/dln(a)` after a real cosmic `S_BH(a)` is computed. The repository has no accepted `S_BH(a)` product. |
| units | Entropy per logarithmic scale factor. This is not an energy-transfer quantity unless a conversion law is supplied. |
| normalization requirements | Failed. A dimensionful entropy derivative still needs a physical coupling constant or conversion law. No such normalization exists in the repository. |
| background transfer requirements | Failed. `S_BH` and `dS_BH/dln(a)` can supply timing language only; the repository has no entropy-to-background-transfer equation. |
| stress-energy conservation requirements | Failed. Entropy accounting is not a covariant stress-energy transfer relation in the checked evidence. |
| frame choice requirements | Failed. No entropy-production transfer frame is declared. |
| four-velocity assumptions | Failed. No repository evidence identifies whether the entropy source is local, averaged, tied to black-hole worldlines, or tied to a phase four-velocity. |
| perturbation requirements | Failed. No entropy perturbation, smoothing scale, gauge choice, or stability route is defined. |
| `delta Q` implications | Failed. `delta Q` would require perturbations of `S_BH` and a gauge/frame prescription, neither of which exists. |
| known-model reduction risks | Very high. A fitted `dS_BH/dln(a)` coupling is generic IV/IDE; an entropy/topology route risks becoming a known black-hole entropy/topological dark-energy model without QFUDS distinction. |

Lane B outcome: `data_product_blocked`.

Reason: black-hole entropy is real thermodynamics, but the repository lacks
`S_BH(a)`, `dn_BH/dM`, accretion, merger, seed-history inputs, conversion law,
and perturbation prescription. Current repository evidence does not supply a
physically meaningful `Q^nu`.

## Required Equations Check

The approved plan required each lane to supply:

```text
X =
[X] =
normalization =
Q^nu[X,...] =
nabla_mu T_A^{mu nu} = -Q^nu
nabla_mu T_B^{mu nu} = Q^nu
background limit =
frame choice =
momentum-transfer declaration =
```

Current result:

| Required item | Lane A | Lane B |
| --- | --- | --- |
| `X =` | partial name only: `rho_BH(a)` or `d rho_BH/dln(a)` | partial name only: `dS_BH/dln(a)` after `S_BH(a)` exists |
| `[X] =` | unresolved because source convention is not selected | entropy per `dln(a)`, but not energy-transfer units |
| `normalization =` | missing | missing |
| `Q^nu[X,...] =` | missing | missing |
| `nabla_mu T_A^{mu nu} = -Q^nu` | not derived | not derived |
| `nabla_mu T_B^{mu nu} = Q^nu` | not derived | not derived |
| `background limit =` | not established without circular fitting | not established without conversion law |
| `frame choice =` | missing | missing |
| `momentum-transfer declaration =` | missing | missing |

Neither lane passes the required equation check.

## Required Conservation Tests

| Conservation test | Lane A | Lane B |
| --- | --- | --- |
| identify split stress-energy tensors | failed | failed |
| state total conservation | not enough; only a possible future split is named | not enough; entropy accounting is not stress-energy conservation |
| define transfer sign | missing | missing |
| dimensional consistency of `Q^nu` | missing because normalization and units are not fixed | missing because entropy-to-energy conversion is not fixed |
| recover background continuity equations | not derived | not derived |
| declare momentum transfer | missing | missing |
| keep phase B smooth and vacuum-pressure-like | not supplied | not supplied |

Conservation result: failed for both lanes.

## Required Perturbation Tests

| Perturbation test | Lane A | Lane B |
| --- | --- | --- |
| define `delta X` | missing | missing |
| define `delta Q` or `delta Q^nu` | missing | missing |
| specify gauge or covariant variables | missing | missing |
| specify perturbation transfer frame | missing | missing |
| state source clustering/smoothing behavior | missing | missing |
| identify stability risks | only generic risk known; no model-specific test exists | only generic risk known; no model-specific test exists |
| identify first distinct observable | missing | missing |

Perturbation result: failed for both lanes.

## Known-Model Reduction Tests

| Comparator | Lane A | Lane B |
| --- | --- | --- |
| cosmologically coupled black-hole dark energy | very high reduction risk | indirect risk if entropy is tied to black-hole DE density |
| black-hole-coupled dark energy | very high reduction risk | high risk if entropy source is promoted to DE without QFUDS transfer |
| black-hole entropy or topological dark energy | secondary risk | very high reduction risk |
| remnant dark matter | not the main lane, but compact-object bookkeeping remains a risk | not the main lane, but remnant/defect routing remains a risk |
| interacting vacuum / IDE | high risk if mass-growth timing is fitted as `Gamma(a)` | high risk if entropy timing is fitted as `Gamma(a)` |
| HDE or horizon thermodynamics | lower than entropy lane, but possible if horizon language enters | high risk if entropy reasoning becomes horizon/HDE-like |

Reduction result: neither lane supplies a distinct QFUDS observable before
fitting. Both remain reduction-risk comparators, not physical QFUDS branches.

## Failure Criteria Results

| Failure criterion | Lane A | Lane B |
| --- | --- | --- |
| only supplies `X(a)` | fails; at most partial source naming exists | fails; at most partial source naming exists |
| only supplies `Gamma(a)` | fails if used as timing; no prediction exists | fails if used as timing; no prediction exists |
| reproduces background but not `Q^nu` | fails; no `Q^nu` exists | fails; no `Q^nu` exists |
| lacks conservation-law split | fails | fails |
| lacks perturbation route | fails | fails |
| reduces to known black-hole-coupled DE without distinct observable | high risk; no distinction supplied | high entropy/topological/HDE/IV-IDE reduction risk; no distinction supplied |
| requires fitting `Gamma(a)` instead of predicting it | fails if used now; no predictive normalization exists | fails if used now; no predictive normalization exists |

Both lanes fail the approved Phase 3 feasibility criteria in the current
repository state.

## Feasibility Outcome

Overall outcome: `data_product_blocked`.

Interpretation:

- Lane A is blocked by the absence of a selected black-hole mass-growth source
  product, fixed normalization, source-to-transfer equation, transfer frame,
  and perturbation route.
- Lane B is blocked by the absence of a computable cosmic `S_BH(a)` product,
  entropy-to-energy conversion law, transfer frame, and perturbation route.
- Both lanes also carry high known-model reduction risk.
- Neither lane can currently support a physically meaningful covariant
  `Q^nu`.

This is a negative feasibility result for the current repository evidence. It
is not a claim that no future black-hole source could ever work.

## What Would Change The Result

Future progress would require one retained lane to supply, before fitting:

- a selected source product with units and redshift range;
- a non-circular normalization;
- a source-derived `Q^nu`;
- a declared conservation-law split;
- a frame and momentum-transfer prescription;
- a phase-B `w ~= -1` rationale;
- a perturbation route for `delta Q`;
- a distinct observable against CCBH, black-hole-coupled DE, entropy/topological
  DE, HDE, remnant DM, and generic IV/IDE.

Until then, the lanes remain audit material.

## Level 2B Blocked Confirmation

Physical-QFUDS Level 2B remains blocked.

No Phase 3 result opens Level 2B because no retained lane supplies all
admission-rule items together:

```text
X =
Q^nu =
why phase B has w ~= -1 =
delta Q route =
known-model distinction =
```

## No-Roadmap-Upgrade Confirmation

Roadmap unchanged.

This audit result does not modify roadmap status, roadmap level, or current
retained branch classification. The roadmap remains the status authority.
