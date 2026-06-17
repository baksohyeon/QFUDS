---
doc_id: baseline_reference_investigation_index
title: Baseline Reference Investigations
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - research_investigations_index
next_gate: define one candidate foam-sector state variable before model-facing NASA or BAO interpretation
last_updated: 2026-06-17
---

# Baseline Reference Investigations

This chain stores plans and closeouts for external baseline-reference caches and
constraint-mapping checkpoints that improve standard cosmology, data-source, or
citation coverage without changing QFUDS status.

This chain uses the
[Research Asset and Product Workflow](../../../../../.agent/workflows/research-asset-product-workflow.md).

Workflow states represented here include `asset_cached`,
`manual_structured_extract`, `asset_extracted_not_digitized`, and
`direct_table`.

Do not use this chain for model support, physical-admission claims, or roadmap
changes.

## Read Order

1. [NASA LAMBDA Graphic History Cache Closeout](conclusions/001_nasa_lambda_graphic_history_cache_closeout.md):
   confirm the page-family cache and data-reference matrix as baseline
   provenance, not likelihood evidence.
2. [Effective Foam Assumption Ledger Preflight Plan](plans/002_effective_foam_assumption_ledger_preflight_plan.md):
   set the plan-only boundary before any model-facing claim.
3. [Effective Foam Assumption Ledger Result](conclusions/002_effective_foam_assumption_ledger_result.md):
   decide whether `xi ~= 10 Mpc`, transition width, and amplitude are
   independent assumptions or post-hoc fitted choices.
4. [Foam State Variable and Placement Selection Matrix](conclusions/004_foam_state_variable_placement_selection_matrix.md):
   propose and reject candidate foam-sector state variables and equation-side
   placements before model-facing use of baseline constraints.
5. [NASA + BAO Baseline Constraint Map](conclusions/003_nasa_bao_baseline_constraint_map.md):
   list observational kill thresholds only after the non-circularity ledger is
   frozen.

## Use Boundary

Allowed use:

- baseline source provenance;
- non-circularity audit inputs;
- future observational kill-map thresholds.

Forbidden use:

- QFUDS support or validation language;
- Physical-QFUDS Level 2B admission;
- choosing `xi`, transition width, transition redshift, or amplitude after
  seeing NASA/LAMBDA, DESI, eBOSS, BAO, LSS, or retained-timing targets;
- treating retained `Gamma(a)` as a physical foam-sector source.

The chain order matters. The assumption ledger and state-variable/placement
matrix must come before model-facing use of the baseline constraint map so
observations cannot back-drive the effective foam scale.
