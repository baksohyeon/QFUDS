---
doc_id: plan_2026_06_18_source_object_x_definition_preflight_ko
title: Source Object X Definition Preflight Plan
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_18_retained_gamma_iv_non_equivalence_worksheet_ko
  - audit_2026_06_18_foam_sector_to_gamma_derivation_feasibility_result
  - audit_2026_06_17_foam_state_variable_literature_question_result
  - roadmap
next_gate: execute source-object X definition audit before any retained timing or observational comparison
last_updated: 2026-06-18
---

# Source Object X Definition Preflight Plan

## Purpose

This is a plan-only checkpoint for the next missing object:

```text
X
```

The goal is not to invent a new QFUDS mechanism by naming one. The goal is to
define the minimum conditions under which something may count as a source
object `X` at all.

No retained `Gamma(a)` fit, `q_V(a)` fit, NASA/BAO/CMB/LSS interpretation, or
Level 2B admission is allowed in this plan.

## Workflow Boundary

This plan introduces no new external source, web result, PDF, cache, numerical
product, or product-absence claim.

External-source handling remains governed by
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).
If a later execution pass uses literature or web sources, it must record the
asset state before making any source/product/absence claim.

Inherited upstream workflow states from the records this plan depends on:

```text
asset_cached
asset_extracted_not_digitized
source_text_parse
manual_structured_extract
```

This plan is not QFUDS support, validation, novelty, or Physical-QFUDS Level 2B
admission.

## Definition Rule

`X` may be considered a candidate source object only if it is specified before
data-facing comparison and answers all of the following:

| Required field | Meaning |
| --- | --- |
| `object_type` | scalar, vector, tensor, density, phase fraction, geometry scalar, stochastic variable, or effective field |
| `units` | physical units or dimensionless normalization |
| `equation_side` | geometry side, stress-energy side, or interaction/source side |
| `evolution_equation` | equation that evolves `X` before fitting timing data |
| `rho_A_route` | how phase A density is computed from `X` |
| `phase_B_pressure_route` | how `w_B ~= -1` or equivalent vacuum pressure follows from `X` |
| `Qmu_route` | how `Q^mu[X]` is derived or why it cannot be derived |
| `delta_Q_route` | perturbation prescription or explicit blocked status |
| `known_model_sink` | closest existing model family that absorbs the candidate first |
| `kill_condition` | observation or equation-level condition that rejects the candidate before tuning |

If any row is missing, the candidate remains `unknown`, not physical QFUDS.

## Candidate Slots To Audit

The execution audit may test these slots, but must not tune them to retained
timing:

| Candidate slot | First risk | Required pre-data answer |
| --- | --- | --- |
| `f_B(a)` phase fraction | effective `w(a)` / unified dark fluid | What equation determines `f_B` before fitting? |
| foam correlation variable | spacetime-foam or stochastic-vacuum speculation | What stress tensor and pressure does it generate? |
| coarse-graining scale `xi` | EFTofLSS cutoff or averaging-domain bookkeeping | Is it physical, or only a smoothing/domain choice? |
| backreaction domain scalar | Buchert/backreaction sink | Does it give source transfer or only averaged geometry? |
| running-vacuum scalar | RVM/HDE sink | What makes it QFUDS rather than `rho_vac(H, dot H)`? |
| remnant/black-hole inventory | compact-object/PBH/remnant constraints | How does it become smooth vacuum pressure rather than matter/radiation? |
| entropy/information proxy | analogy-as-source failure | What conservation law converts it into `Q^mu`? |

## Non-Circularity Rules

The execution audit fails immediately if:

- `X` is defined as "whatever produces the retained `Gamma(a)` shape";
- `xi`, transition redshift, width, or amplitude are selected from the same
  observations later used as support;
- `phase B` is called vacuum-like without a pressure or stress-energy route;
- `Q^mu` is chosen from a known IV/IDE family without deriving why QFUDS selects
  that frame;
- a known-model sink is renamed as QFUDS without a new equation or observable;
- NASA/BAO/CMB/LSS constraints are used before `X`, `Q^mu[X]`, phase-B pressure,
  and perturbation route are defined.

## Output Required From Execution

The matching execution record should be a compact table:

| Column | Required content |
| --- | --- |
| `candidate_X` | the proposed object |
| `status` | `defined`, `assumed`, `unknown`, `rejected`, or `circular_if_fitted` |
| `equation_side` | geometry, stress-energy, interaction, or unassigned |
| `evolution_equation` | equation or explicit absence |
| `rho_A_route` | route or absence |
| `phase_B_pressure_route` | route or absence |
| `Qmu_route` | route or absence |
| `delta_Q_route` | route or absence |
| `known_model_sink` | nearest absorber |
| `kill_condition` | predeclared failure condition |
| `decision` | ask deeper, use as comparator, block, or reject |

## Stop Boundary

This plan keeps the lane in observer mode.

It changes no physical-admission item:

```text
candidate X: not yet
Q^mu: not yet
phase-B pressure: not yet
delta Q: not yet
known-model distinction: not yet
Level 2B: no
```

## Next Executable Instruction

Execute the source-object `X` definition audit. Do not browse unless a specific
candidate slot requires external confirmation. Start with repo-local candidates
and mark each slot as `defined`, `assumed`, `unknown`, `rejected`, or
`circular_if_fitted`.
