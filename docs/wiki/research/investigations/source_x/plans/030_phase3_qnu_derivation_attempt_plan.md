---
doc_id: audit_2026_06_10_phase3_qnu_derivation_attempt_plan
title: "2026-06-10 Phase 3 Q^nu Derivation Attempt Plan"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_phase2_candidate_selection_closeout
  - audit_2026_06_10_black_hole_coupled_source_audit
  - audit_2026_06_10_black_hole_coupled_literature_search
  - audit_2026_06_10_structure_era_activation_literature
  - roadmap
  - repository_levels_glossary
  - wiki_governance_004_missing_physics_map
  - wiki_governance_003_blocked_admission_rule_gate
next_gate: no derivation; execute only as a feasibility audit with failure criteria first
last_updated: 2026-06-11
---

# 2026-06-10 Phase 3 Q^nu Derivation Attempt Plan

## Purpose

Plan a feasibility audit for whether the retained Phase 2 candidate quantities
can support a physically meaningful covariant transfer vector `Q^nu`.

This is not a derivation. This is a feasibility audit plan.

The plan evaluates two candidate lanes:

- Lane A: black-hole mass growth history.
- Lane B: `dS_BH / dln(a)`.

## Status Boundary

Current retained-branch classification:
Phenomenological IV/IDE; Not Yet A Physical Model.

This classification applies to the current retained branch only.

Gamma(a) remains a prototype phenomenological transfer profile.

The Phase 3 plan must determine whether a physically meaningful Q^nu can exist.

It must not assume that one already exists.

This plan does not:

- execute a derivation;
- open Physical-QFUDS [Level 2B](../../../../glossary/repository_levels.md);
- modify roadmap status;
- claim black holes explain `Gamma(a)`;
- treat `Gamma(a)` as proven;
- treat a conservation-compatible ansatz as physical admission.

## Candidate Lanes

| Requirement | Lane A: black-hole mass growth history | Lane B: `dS_BH / dln(a)` |
| --- | --- | --- |
| source quantity definition | Candidate `X` must be a black-hole mass-density history or derivative, such as `rho_BH(a)` or `d rho_BH / dln(a)`, with a declared population and source convention. | Candidate `X` must be a cosmic black-hole entropy-growth history, `dS_BH / dln(a)`, derived from an explicit black-hole mass function and growth history. |
| units | Must state whether `X` is mass density, energy density, or density per `dln(a)`. Units must be compatible with the proposed background transfer. | Entropy per logarithmic scale factor. The plan must require a conversion law before using entropy change as energy transfer. |
| normalization requirements | Must fix amplitude, reference density, sign convention, and redshift range before comparing to retained `Gamma(a)`. | Must fix entropy normalization, black-hole population assumptions, conversion constant if any, and redshift range before comparing to retained `Gamma(a)`. |
| background transfer requirements | Must define how mass growth changes phase-A and phase-B background densities without circularly fitting retained `Gamma(a)`. | Must define how entropy growth changes phase-A and phase-B background densities, not merely track timing. |
| stress-energy conservation requirements | Must support a split `nabla_mu T_A^{mu nu} = -Q^nu`, `nabla_mu T_B^{mu nu} = Q^nu` with signs, dimensions, and receiver/source components declared. | Must support the same conservation split and state how entropy change enters stress-energy rather than remaining thermodynamic bookkeeping. |
| frame choice requirements | Must choose a transfer frame, such as phase-A rest frame, phase-B rest frame, total-fluid frame, or source-population frame, and explain the momentum-transfer consequence. | Must choose a transfer frame for entropy production and state whether entropy perturbations move with phase A, phase B, black-hole population flow, or another declared frame. |
| four-velocity assumptions | Must declare the four-velocity used in any form like `Q^nu = Q u^nu` and justify whether black holes, phase A, phase B, or total matter define `u^nu`. | Must declare the four-velocity used for entropy-transfer flow and justify whether the entropy source is local, averaged, or tied to black-hole worldlines. |
| perturbation requirements | Must define how local mass-growth perturbations produce `delta Q` or `delta Q^nu`, including gauge and stability implications. | Must define how entropy-history perturbations produce `delta Q` or `delta Q^nu`, including gauge, smoothing scale, and stability implications. |
| `delta Q` implications | Fails if it cannot produce perturbation-level source fluctuations beyond a background timing function. | Fails if entropy growth cannot be perturbed in a controlled way or only gives a background scalar. |
| known-model reduction risks | Very high risk of reducing to cosmologically coupled black-hole dark energy, black-hole-coupled DE, or IV/IDE with a chosen coupling history. | Very high risk of reducing to black-hole entropy/topological dark energy, HDE-like reasoning, or IV/IDE with an entropy-shaped coupling history. |

## Required Equations

The Phase 3 audit must require equations, but must not assume their existence.

For each lane, the audit must require:

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

The audit must fail any proposal that only rewrites the retained background as:

```text
Q = H Gamma(a) rho_A
```

without deriving the transfer from the candidate source quantity.

## Required Conservation Tests

The Phase 3 audit must test whether each lane can state a conservation-law
split rather than only a scalar timing history.

Required checks:

- identify which stress-energy tensors are being split;
- state whether total stress-energy is conserved;
- define the sign of transfer from phase A to phase B;
- show dimensional consistency of `Q^nu`;
- state the background continuity equations recovered from `Q^nu`;
- state whether the transfer includes momentum transfer;
- identify whether phase B remains smooth and vacuum-pressure-like under the
  proposed split.

The lane fails if it reproduces background evolution but cannot state a
covariant `Q^nu`.

## Required Perturbation Tests

The Phase 3 audit must require a perturbation route before any physical
promotion can be considered.

Required checks:

- define `delta X` or an equivalent local source perturbation;
- define `delta Q` or `delta Q^nu`;
- specify gauge or covariant variable choices;
- specify the transfer frame used for perturbations;
- state whether source perturbations cluster, smooth, or follow the black-hole
  population;
- state stability risks for density, pressure, and velocity perturbations;
- identify the first observable that would change relative to known models.

Reusing a Level 2A phenomenological closure is not a derivation.

## Known-Model Reduction Tests

Each lane must be tested against the closest known model families before any
claim of QFUDS progress:

| Comparator | Reduction test |
| --- | --- |
| cosmologically coupled black-hole dark energy | Fails as QFUDS if the lane only imports black-hole mass growth as dark energy without a distinct QFUDS equation or observable. |
| black-hole-coupled dark energy | Fails as QFUDS if the source-to-DE relation is the same model under QFUDS labels. |
| black-hole entropy or topological dark energy | Fails as QFUDS if entropy/topology supplies the dark-energy mechanism without a distinct phase-transfer law. |
| remnant dark matter | Fails as phase-B source if the result behaves as compact matter, remnants, defects, or radiation. |
| interacting vacuum / IDE | Fails as physical QFUDS if the lane only chooses a time-dependent coupling history. |
| HDE or horizon thermodynamics | Fails as black-hole source if the actual mechanism becomes a standard horizon/IR-cutoff model. |

The required distinct observable must be stated before fitting.

## Failure Criteria

The lane automatically fails if:

1. It only supplies `X(a)`.
2. It only supplies `Gamma(a)`.
3. It reproduces background evolution but not `Q^nu`.
4. It lacks a conservation-law split.
5. It lacks a perturbation route.
6. It reduces directly to known black-hole-coupled DE without a distinct observable.
7. It requires fitting `Gamma(a)` instead of predicting it.

Additional automatic failures:

- it lacks normalization fixed before comparison;
- it cannot explain why phase B has `w ~= -1`;
- it cannot define `delta Q`;
- it treats timing overlap as proof;
- it opens Level 2B by naming a source instead of supplying the admission-rule
  items.

## Evidence Files to Scan

The Phase 3 audit must scan these authority and evidence files before any
derivation attempt:

- [2026-06-10 Phase 2 Candidate Selection Closeout](../conclusions/029_phase2_candidate_selection_closeout.md)
- [2026-06-10 Black-Hole-Coupled Source Audit](../conclusions/021_phase2_black_hole_coupled_source_audit.md)
- [2026-06-10 Black-Hole-Coupled Literature Search Audit](../coverage/022_phase2_black_hole_coupled_literature_search_audit.md)
- [2026-06-10 Structure-Era Activation Literature Audit](../coverage/024_phase2_structure_era_activation_literature_audit.md)
- [2026-06-10 Source-X Audit](../conclusions/011_phase1_source_x_audit.md)
- [Missing Physics Map](../../../../governance/004_missing_physics_map.md)
- [Blocked Admission Rule](../../../../governance/003_blocked_admission_rule_gate.md)
- [Repository Levels](../../../../glossary/repository_levels.md)
- [Roadmap](../../../../../05_next_steps/000_roadmap.md)

The audit may also scan repaired black-hole literature cache notes if it needs
paper-level comparator details. Cache records remain paper-fact anchors, not
QFUDS admission evidence.

## Success Criteria

The Phase 3 audit succeeds as a feasibility audit if it returns one of these
bounded outcomes:

- `feasible_to_attempt_derivation`: one lane supplies a credible route to
  candidate `Q^nu` equations and perturbation tests, but is not yet admitted;
- `not_feasible`: neither lane can define the required transfer structure;
- `known_model_reduction`: a lane can define a transfer only by reducing to a
  known model family;
- `data_product_blocked`: a lane might be testable, but required source
  histories, normalizations, or uncertainty products are missing.

The audit does not succeed by proving QFUDS. It succeeds by making the next
failure mode explicit.

## Level 2B Blocked Confirmation

Physical-QFUDS Level 2B remains blocked.

No Phase 3 plan or future Phase 3 audit may open Level 2B unless one mechanism
supplies all admission-rule items together:

```text
X =
Q^nu =
why phase B has w ~= -1 =
delta Q route =
known-model distinction =
```

## No-Roadmap-Upgrade Confirmation

Roadmap unchanged.

This plan does not modify roadmap status, roadmap level, or current retained
branch classification. The roadmap remains the status authority.
