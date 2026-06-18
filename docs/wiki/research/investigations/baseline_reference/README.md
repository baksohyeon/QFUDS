---
doc_id: baseline_reference_investigation_index
title: Baseline Reference Investigations
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - research_investigations_index
next_gate: baseline-reference chain closed until a future candidate fills upstream escape-equation templates
last_updated: 2026-06-18
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
5. [Foam State Variable Definition Plan](plans/005_foam_state_variable_definition_plan.md):
   define the required fields for a plan-only `X(x,a)` or `f_B(x,a)` definition
   audit before any model-facing baseline use.
6. [Foam State Variable Definition Audit](conclusions/005_foam_state_variable_definition_audit.md):
   execute the `X(x,a)` / `f_B(x,a)` definition audit and keep both below
   physical admission.
7. [f_B Stress-Energy Definition Audit](conclusions/006_fB_stress_energy_definition_audit.md):
   test whether the remaining `f_B` bookkeeping route can supply `rho_A`,
   `rho_B`, `p_A`, `p_B`, `Q^nu`, and `delta Q` before any model-facing
   baseline use.
8. [f_B Known-Model Reduction Checklist](conclusions/007_fB_known_model_reduction_checklist.md):
   close where the `f_B` route is first absorbed by effective `w(a)`, unified
   dark fluid, IV/IDE, running vacuum/HDE, EFTofLSS, backreaction, or screened
   modified gravity.
9. [Known-Model Escape Equation Templates](conclusions/008_known_model_escape_equation_templates.md):
   define the minimum equations required before any future `f_B`, `X`, or `xi`
   route can claim it escapes a known-model sink.
10. [NASA + BAO Baseline Constraint Map](conclusions/003_nasa_bao_baseline_constraint_map.md):
   list observational kill thresholds only after the non-circularity ledger,
   definition audits, known-model checklist, and escape-equation templates are
   frozen.
11. [Baseline Reference Chain Closure](conclusions/009_baseline_reference_chain_closure.md):
   final read-order and stop-rule summary for this chain.
12. [Candidate Equation Proposal Template](plans/010_candidate_equation_proposal_template.md):
   use this before accepting any future `Y`, `X`, `f_B`, `xi`, stress-tensor,
   or transfer-law proposal.
13. [Candidate Equation Triage Closeout](conclusions/010_candidate_equation_triage_closeout.md):
   apply the template to current lanes and record that no current candidate
   passes physical-branch admission.

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

The chain order matters. The assumption ledger, state-variable/placement
matrix, state-variable definition plan, definition audit, `f_B` stress-energy
audit, `f_B` known-model reduction checklist, and escape-equation templates
must come before model-facing use of the baseline constraint map. The closure
summary records this chain as closed until new candidate equations exist, so
observations cannot back-drive the effective foam scale.

## Candidate Re-Entry

The chain can re-enter only through the
[Candidate Equation Proposal Template](plans/010_candidate_equation_proposal_template.md).
If a candidate cannot fill that template, reject it before NASA/LAMBDA, BAO,
LSS, CMB, matter-power, or likelihood comparison.

The 2026-06-18
[Candidate Equation Triage Closeout](conclusions/010_candidate_equation_triage_closeout.md)
records that the current candidate set does not pass this re-entry rule.
