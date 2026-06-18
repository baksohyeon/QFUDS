---
doc_id: audit_2026_06_18_foam_state_variable_definition_audit
title: "2026-06-18 Foam State Variable Definition Audit"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - audit_2026_06_17_foam_state_variable_definition_plan
  - audit_2026_06_17_foam_state_variable_placement_selection_matrix
  - audit_2026_06_17_effective_foam_assumption_ledger_result
  - wiki_governance_004_missing_physics_map
  - roadmap
next_gate: do not use NASA or BAO for model-facing interpretation; a future theory note would need a stress tensor or equation of state before Level 2B can be reconsidered
last_updated: 2026-06-18
---

# 2026-06-18 Foam State Variable Definition Audit

## Purpose

This document executes the
[Foam State Variable Definition Plan](../plans/005_foam_state_variable_definition_plan.md).

It asks whether either `X(x,a)` or `f_B(x,a)` can be defined well enough to act
as the next non-circular foam-sector state variable before NASA/LAMBDA or BAO
baseline constraints are used for model-facing interpretation.

This is a definition audit only.

It is not a physical derivation.

It is not an experiment result.

It does not claim QFUDS support.

It does not open Physical-QFUDS Level 2B.

It does not use NASA/LAMBDA, DESI, eBOSS, BAO, LSS, or retained timing targets
to choose `xi`, transition width, transition redshift, amplitude, `X`, or
`f_B`.

## Workflow Application

This audit uses the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md)
only to preserve the external baseline-source boundary.

Referenced source states remain:

- NASA/LAMBDA Graphic History: `asset_cached`;
- DESI DR2 Ly-alpha BAO: `asset_extracted_not_digitized` with `direct_table`
  products;
- eBOSS DR16 Ly-alpha BAO: `asset_cached` with `direct_table` products.

These states are baseline-source states only. They are not evidence for any
candidate state variable.

## Selected Candidate

The audit tests two definitions and selects no physical candidate.

| Candidate | Audit role | Result |
| --- | --- | --- |
| `X(x,a)` | General scalar order/phase variable | Too underdefined. It has no independent evolution equation and no `rho_F[X]` or `p_F[X]` mapping. |
| `f_B(x,a)` | Phase-B fraction bookkeeping variable | Usable only as bookkeeping. It exposes the missing phase-B pressure and stress tensor but does not derive them. |

The least-bad next notation is `f_B(x,a)` because QFUDS already uses phase A/B
language. That is a notation choice, not a physical success.

## Definition Table

| Field | `X(x,a)` route | `f_B(x,a)` route | Audit verdict |
| --- | --- | --- | --- |
| `symbol` | `X(x,a)` | `f_B(x,a)` | `f_B` is clearer for phase bookkeeping. |
| `plain_meaning` | Coarse-grained foam order variable. | Fraction of effective foam sector in phase B. | Both are definitions by declaration, not derivations. |
| `domain` | Coarse-grained spacetime or background limit `X(a)`. | Coarse-grained spacetime or background limit `f_B(a)`. | Background-only use would still not supply perturbations. |
| `units` | Unknown unless declared dimensionless. | Dimensionless. | `X` fails clarity; `f_B` passes bookkeeping. |
| `range` | Unknown. | `0 <= f_B <= 1`. | `f_B` passes bookkeeping. |
| `normalization` | Missing. | `f_B = 0` all phase A; `f_B = 1` all phase B. | `f_B` passes bookkeeping. |
| `equation_side` | Unclear; could be stress-energy or geometry. | Stress-energy side by default. | Stress-energy placement is the only bounded next route. |
| `rho_mapping` | Missing. | Formal split only: `rho_A = (1 - f_B) rho_F`, `rho_B = f_B rho_F`. | Bookkeeping only; `rho_F(a)` still needs an equation. |
| `p_mapping` | Missing. | Would require `p_A ~= 0` and `p_B ~= -rho_B` or another equation of state. | Fails as physics; phase-B pressure is assumed, not derived. |
| `conservation_rule` | Missing. | Total conservation can be imposed as bookkeeping; transfer `Q^nu` is not derived. | Fails physical admission. |
| `xi_role` | Not defined. | Absent at definition stage; may later become a derived correlation length or declared smoothing scale. | Pass only if `xi` stays downstream. |
| `Gamma_boundary` | Must not reproduce retained `Gamma(a)`. | Must not tune `df_B/dln(a)` to retained `Gamma(a)`. | Hard stop if violated. |
| `known_model_sink` | Scalar-field DE, unified dark fluid, running vacuum. | Unified dark fluid, IV/IDE, effective `w(a)`. | High known-model risk for both. |
| `kill_condition` | Reject if no `rho_F[X]`, `p_F[X]`, or evolution law. | Reject if `w_B ~= -1` is assumed without stress tensor or equation of state. | Both fail current physical definition. |

## Placement Decision

Default placement remains:

```text
stress-energy side first
```

Reason:

- geometry-side language needs a modified field equation and
  Bianchi-compatible consistency statement, which the repository does not have;
- interaction-source language needs `Q^nu[X,...]`, which would be premature
  without a state variable;
- stress-energy placement forces the missing objects into the open:
  `T_mu_nu`, `rho`, `p`, equation of state, sound speed, and perturbation
  route.

This does not mean stress-energy placement is accepted. It means it is the
least ambiguous place to make the next failure explicit.

## Known-Model Sink

| Route | First known-model sink | Why |
| --- | --- | --- |
| `X(x,a)` with energy density and pressure | scalar-field dark energy or unified dark fluid | A scalar order variable with `rho[X]` and `p[X]` is not novel by itself. |
| `X(a)` affecting vacuum density | running vacuum / HDE | A background-only vacuum-like function can be absorbed into known running-vacuum or effective-DE language. |
| `f_B(a)` phase fraction with transfer | IV/IDE or effective `w(a)` | A time-varying phase fraction becomes a coupling or equation-of-state reconstruction unless independently derived. |
| `df_B/dln(a)` matched to retained timing | IV/IDE fit | This is retained `Gamma(a)` in another variable. |
| `xi` derived from correlation of `X` | EFTofLSS or halo-model coarse graining risk | Correlation length alone can be absorbed into smoothing/cutoff language unless it predicts a fixed observable. |

## Rejection Conditions

The current definition attempt fails physical admission for these reasons:

1. `X(x,a)` has no evolution equation, units, normalization, or density/pressure
   mapping.
2. `f_B(x,a)` supplies only a phase-fraction bookkeeping variable.
3. `f_B` does not explain why phase B has `w ~= -1`.
4. Neither route supplies an effective `T_mu_nu`.
5. Neither route supplies `Q^nu` or `delta Q^nu`.
6. Neither route supplies a perturbation prescription or sound speed.
7. Neither route distinguishes QFUDS from unified dark fluid, IV/IDE, running
   vacuum, scalar-field DE, or effective `w(a)`.

## NASA/BAO Boundary

NASA/LAMBDA and BAO remain blocked from model-facing interpretation.

Allowed:

- use NASA/LAMBDA and BAO as baseline-source provenance;
- keep the NASA + BAO baseline map as an observational kill-map;
- ask what a future model would have to compute.

Forbidden:

- choose `xi`, width, redshift, amplitude, `X`, or `f_B` from NASA/LAMBDA or
  BAO and then call the result a foam source;
- treat retained timing near `z ~= 2` as evidence for `f_B`;
- compute no `D_M/r_d` or `D_H/r_d` but imply BAO viability.

## Decision

The audit returns:

```text
X(x,a) = reject_current_definition
f_B(x,a) = bookkeeping_only
placement = stress_energy_side_for_next_failure_test
physical_QFUDS_admission = no
NASA_BAO_model_interpretation = blocked
```

The next useful checkpoint is not NASA/BAO interpretation. It is a narrow
theory-definition note asking whether a stress-energy-side `f_B` bookkeeping
variable can be promoted to a real `T_mu_nu` with:

- `rho_A`, `rho_B`;
- `p_A`, `p_B`;
- phase-B equation-of-state rationale;
- conservation or transfer law;
- perturbation requirement;
- known-model reduction test.

If that note cannot supply those objects, the `f_B` route should be rejected as
only an effective `w(a)` / IV/IDE rewriting.

## Status Boundary Closeout

Candidate `X`: no physical candidate supplied.

`f_B`: bookkeeping-only notation, not physical source.

`Q^nu`: no.

Phase-B `w ~= -1` rationale: no.

`delta Q`: no.

Known-model distinction: no.

QFUDS support: no.

Roadmap status change: no.

Physical-QFUDS Level 2B change: no.
