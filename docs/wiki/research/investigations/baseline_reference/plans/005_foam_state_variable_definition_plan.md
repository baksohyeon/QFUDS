---
doc_id: audit_2026_06_17_foam_state_variable_definition_plan
title: "2026-06-17 Foam State Variable Definition Plan"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_17_foam_state_variable_placement_selection_matrix
  - audit_2026_06_17_effective_foam_assumption_ledger_result
  - wiki_governance_004_missing_physics_map
  - roadmap
next_gate: execute only as a definition audit; no NASA or BAO model-facing interpretation until one state variable and placement are fixed
last_updated: 2026-06-17
---

# 2026-06-17 Foam State Variable Definition Plan

## Purpose

This is a plan-only checkpoint for defining the minimum candidate foam-sector
state variable before any model-facing NASA/LAMBDA or BAO interpretation.

It follows the
[Foam State Variable and Placement Selection Matrix](../conclusions/004_foam_state_variable_placement_selection_matrix.md).

This plan does not derive a model.

It does not create an experiment result.

It does not claim QFUDS support.

It does not open Physical-QFUDS Level 2B.

It does not use NASA/LAMBDA, DESI, eBOSS, BAO, LSS, or retained timing targets
to choose `xi`, transition width, transition redshift, or amplitude.

## Workflow Application

This plan uses the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md)
only to preserve the external baseline-source boundary.

Referenced source states remain:

- NASA/LAMBDA Graphic History: `asset_cached`;
- DESI DR2 Ly-alpha BAO: `asset_extracted_not_digitized` with `direct_table`
  products;
- eBOSS DR16 Ly-alpha BAO: `asset_cached` with `direct_table` products.

These states are baseline-source states only. They are not evidence for any
candidate state variable.

## Target Scope

The next executable audit should define, then immediately stress-test, one of
these two least-bad stress-energy-side candidates:

| Candidate | Minimal meaning | Why it is considered | Immediate risk |
| --- | --- | --- | --- |
| `X(x,a)` | A coarse-grained scalar foam order or phase-density variable. | It is broad enough to support a later equation but concrete enough to demand units and normalization. | Can collapse into scalar-field DE, unified dark fluid, or running vacuum. |
| `f_B(x,a)` | The local or coarse-grained fraction of the effective foam sector in phase B. | It directly targets the missing A/B phase-transfer language. | Can collapse into IV/IDE or effective `w(a)` if it is only fitted timing. |

The audit should not define `xi ~= 10 Mpc` as the state variable. `xi` may only
appear downstream as a correlation length, smoothing scale, cutoff, or derived
property after `X` or `f_B` exists.

## Required Definition Fields

The executed definition audit must fill this table before any calculation or
observational comparison.

| Field | Required content |
| --- | --- |
| `symbol` | `X(x,a)` or `f_B(x,a)`. |
| `plain_meaning` | One sentence saying what the variable measures. |
| `domain` | Background-only `X(a)`/`f_B(a)` or spacetime/coarse-grained `X(x,a)`/`f_B(x,a)`. |
| `units` | Physical units or explicitly dimensionless. |
| `range` | Allowed range, positivity, boundedness, or sign. |
| `normalization` | What sets zero, one, or the reference value. |
| `equation_side` | Stress-energy side by default; geometry side only if a field equation is supplied. |
| `rho_mapping` | How the variable maps to density or phase fraction. |
| `p_mapping` | How it maps to pressure or phase-B equation of state. |
| `conservation_rule` | Whether total `T_mu_nu` is conserved or whether `Q^nu` is introduced later. |
| `xi_role` | Whether `xi` is absent, input smoothing scale, derived correlation length, or unknown. |
| `Gamma_boundary` | Explicit statement that retained `Gamma(a)` is not the source. |
| `known_model_sink` | First known framework that would absorb the definition. |
| `kill_condition` | One condition that ends this candidate before tuning. |

## Candidate Definition Tests

### Test A: `X(x,a)` order-variable route

Minimum acceptable plan output:

```text
X =
units =
range =
rho_F[X] =
p_F[X] =
conservation rule =
xi role =
known-model sink =
kill condition =
```

Reject the route if `X` is only a name for foam, if `rho_F[X]` and `p_F[X]`
cannot be stated even symbolically, or if `X` is chosen to reproduce retained
`Gamma(a)`.

### Test B: `f_B(x,a)` phase-fraction route

Minimum acceptable plan output:

```text
f_B =
range =
rho_A[f_B], rho_B[f_B] =
p_B[f_B] or w_B[f_B] =
phase-transfer rule boundary =
xi role =
known-model sink =
kill condition =
```

Reject the route if `f_B` is only a renamed dark-energy fraction, if phase B is
called `w ~= -1` without an equation-of-state rationale, or if the phase
fraction is tuned to match NASA/BAO/LSS or retained timing targets.

## Placement Rule

Default placement for this plan:

```text
stress-energy side first
```

The reason is procedural, not evidential. Stress-energy placement forces the
audit to ask for `T_mu_nu`, `rho`, `p`, equation of state, sound speed, and
conservation before any observational comparison.

Geometry-side placement is deferred unless the audit can supply:

- a modified field equation;
- Bianchi-compatible consistency;
- a lensing/growth consequence;
- a known-model comparison against backreaction and screened modified gravity.

Interaction-source placement is downstream only. It cannot be the first
definition because it invites reusing retained `Gamma(a)`.

## Non-Circularity Gates

Stop before execution if any item is true:

1. The plan chooses `xi`, transition width, transition redshift, or amplitude
   from NASA/LAMBDA, DESI, eBOSS, BAO, LSS, or retained timing.
2. The plan treats retained `Gamma(a)` as the physical source.
3. The plan treats `xi ~= 10 Mpc` as the state variable.
4. The plan uses phase-B `w ~= -1` as a label without an equation-of-state or
   stress-tensor route.
5. The plan does not name the closest known-model sink before novelty language.

## Output Format For The Execution Audit

The execution audit should create one conclusion document, not an experiment
result. Suggested filename:

```text
docs/wiki/research/investigations/baseline_reference/conclusions/005_foam_state_variable_definition_audit.md
```

Required sections:

- Purpose;
- Workflow Application;
- Selected Candidate;
- Definition Table;
- Placement Decision;
- Known-Model Sink;
- Rejection Conditions;
- NASA/BAO Boundary;
- Decision;
- Status Boundary Closeout.

## Decision

The next checkpoint may execute a definition audit for `X(x,a)` or `f_B(x,a)`,
with stress-energy-side placement as the default starting point.

No observational baseline map may be used for model-facing interpretation until
that audit either defines a candidate non-circularly or rejects the route.

## Status Boundary Closeout

Candidate `X`: plan target only, not supplied.

`Q^nu`: no.

Phase-B `w ~= -1` rationale: no.

`delta Q`: no.

Known-model distinction: no.

QFUDS support: no.

Roadmap status change: no.

Physical-QFUDS Level 2B change: no.
