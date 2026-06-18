---
doc_id: audit_2026_06_18_baseline_reference_chain_closure
title: "2026-06-18 Baseline Reference Chain Closure"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - baseline_reference_investigation_index
  - baseline_reference_conclusions_index
  - audit_2026_06_17_effective_foam_assumption_ledger_result
  - audit_2026_06_18_known_model_escape_equation_templates
  - audit_2026_06_17_nasa_bao_baseline_constraint_map
  - roadmap
next_gate: no model-facing NASA or BAO use until a future candidate fills the escape-equation templates before observing the kill-map targets
last_updated: 2026-06-18
---

# 2026-06-18 Baseline Reference Chain Closure

## Purpose

This document closes the baseline-reference investigation chain as a
read-order and stop-rule summary.

It does not create a new model, result, likelihood, or physical branch. It does
not change roadmap status and does not open Physical-QFUDS Level 2B.

## Workflow Application

This closure uses the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md)
only to preserve source-state boundaries.

Referenced source states remain:

- NASA/LAMBDA Graphic History: `asset_cached`;
- NASA/LAMBDA data-reference matrix: `manual_structured_extract`;
- DESI DR2 Ly-alpha BAO: `asset_extracted_not_digitized` with `direct_table`
  products;
- eBOSS DR16 Ly-alpha BAO: `asset_cached` with `direct_table` products.

These are baseline-source states. They are not QFUDS evidence.

## Final Read Order

Read the chain in this order:

1. [NASA LAMBDA Graphic History Cache Closeout](001_nasa_lambda_graphic_history_cache_closeout.md)
   for source provenance and cache state.
2. [Effective Foam Assumption Ledger Result](002_effective_foam_assumption_ledger_result.md)
   for the non-circularity ledger.
3. [Foam State Variable and Placement Selection Matrix](004_foam_state_variable_placement_selection_matrix.md)
   for candidate state-variable and equation-side placement risks.
4. [Foam State Variable Definition Audit](005_foam_state_variable_definition_audit.md)
   for the rejection of current `X(x,a)` and bookkeeping-only `f_B(x,a)`.
5. [f_B Stress-Energy Definition Audit](006_fB_stress_energy_definition_audit.md)
   for the missing `p_B`, `T_mu_nu`, `Q^nu`, and `delta Q` route.
6. [f_B Known-Model Reduction Checklist](007_fB_known_model_reduction_checklist.md)
   for the reduction path into effective `w(a)`, unified dark fluid, and
   IV/IDE.
7. [Known-Model Escape Equation Templates](008_known_model_escape_equation_templates.md)
   for the preregistration templates a future candidate must fill.
8. [NASA + BAO Baseline Constraint Map](003_nasa_bao_baseline_constraint_map.md)
   only as the observational kill-map after the upstream templates are filled.

## Closure Summary

| Question | Chain answer |
| --- | --- |
| Is `xi ~= 10 Mpc` derived? | No. It is not a state variable and remains undefined as input/output. |
| Is `X(x,a)` defined? | No. The current repository lacks `rho_F[X]`, `p_F[X]`, and an evolution equation. |
| Is `f_B(x,a)` physical? | No. It is allowed as bookkeeping only. |
| Does `f_B` supply phase-B pressure? | No. `p_B ~= -rho_B` is inserted if used. |
| Does the route supply `T_mu_nu`? | No. |
| Does the route supply `Q^nu`? | No. |
| Does the route supply `delta Q`? | No. |
| Does current `f_B` escape known models? | No. It reduces first to effective `w(a)`, unified dark fluid, or IV/IDE. |
| Are escape-equation templates filled? | No. |
| Is NASA/BAO model-facing interpretation allowed? | No. NASA/LAMBDA and BAO remain observational kill-map sources only. |

## Stop Rule

Stop any route that does this:

```text
read NASA/LAMBDA, DESI/eBOSS BAO, LSS, or retained timing targets
-> choose xi, transition width, transition redshift, or amplitude
-> call the chosen quantity a foam source
```

That is circular reasoning.

## Allowed Next Work

Allowed work must stay in one of these lanes:

- propose a future candidate that fills the
  [escape-equation templates](008_known_model_escape_equation_templates.md)
  before observing kill-map targets;
- use the [NASA + BAO Baseline Constraint Map](003_nasa_bao_baseline_constraint_map.md)
  only after the candidate computes observables without retuning to those
  targets;
- keep retained timing near `z ~= 2` as a phenomenological IV/IDE comparator
  only.

## Forbidden Next Work

Do not use this chain to claim:

- QFUDS support;
- candidate `X`;
- physical `f_B`;
- derived `xi`;
- `Q^nu`;
- `delta Q`;
- known-model distinction;
- CMB, matter-power, BAO, DESI, Euclid, Roman, or likelihood viability;
- roadmap advancement;
- Physical-QFUDS Level 2B admission.

## Decision

The baseline-reference chain is closed for now:

```text
baseline_reference_chain = closed_until_new_candidate_equations
NASA_LAMBDA = baseline_source_only
BAO = observational_kill_map_only
f_B = bookkeeping_only
xi = undefined
escape_equations = not_supplied
model_facing_interpretation = blocked
```

## Status Boundary Closeout

QFUDS support: no.

Known-model distinction: no.

Roadmap status change: no.

Physical-QFUDS Level 2B change: no.

NASA/LAMBDA or BAO model-facing interpretation: no.
