---
doc_id: plan_2026_06_18_candidate_equation_proposal_template
title: "2026-06-18 Candidate Equation Proposal Template"
doc_type: guide
stage: reference
status: completed
evidence_role: audit
depends_on:
  - audit_2026_06_18_baseline_reference_chain_closure
  - audit_2026_06_18_known_model_escape_equation_templates
  - wiki_governance_004_missing_physics_map
  - roadmap
next_gate: reject any future candidate that cannot fill the template before NASA, BAO, LSS, or retained timing comparison
last_updated: 2026-06-18
---

# 2026-06-18 Candidate Equation Proposal Template

## Purpose

This guide defines the minimum form of a future candidate equation proposal
after the baseline-reference chain closure.

It is not a new model proposal.

It is not an experiment result.

It does not claim QFUDS support.

It does not open Physical-QFUDS Level 2B.

## Workflow Application

This guide uses the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md)
only to preserve the external-source boundary.

Referenced baseline source states remain:

- NASA/LAMBDA Graphic History: `asset_cached`;
- NASA/LAMBDA data-reference matrix: `manual_structured_extract`;
- DESI DR2 Ly-alpha BAO: `asset_extracted_not_digitized` with `direct_table`
  products;
- eBOSS DR16 Ly-alpha BAO: `asset_cached` with `direct_table` products.

These are not evidence for QFUDS, `f_B`, `xi`, retained timing, or known-model
distinction.

## Current Outlook

Near-term physical-QFUDS outlook is low.

Reason: every current route still overlaps known academic model families before
it supplies the missing equations:

- effective `w(a)`;
- unified dark fluid;
- interacting vacuum / IV/IDE;
- running vacuum / HDE;
- LCDM+EFTofLSS or halo-model coarse graining;
- backreaction;
- screened modified gravity;
- scalar-field DE / k-essence.

The outlook is not mathematically zero, but it is conditional:

```text
nonzero_only_if_new_equations
```

The only useful next move is not another fit. It is a candidate that fills the
template below before looking at NASA/LAMBDA, BAO, LSS, or retained timing
targets.

## Submission Template

Every future candidate must fill this block.

```text
candidate_name =
candidate_object =
object_type = state_variable | source_scalar | action | stress_tensor | geometry_term | scale_rule
units =
domain = background | perturbation | covariant | coarse_grained
input_or_derived = input | derived_output | calibrated_input | unknown

rho_A[...] =
rho_B[...] =
p_A[...] =
p_B[...] =
T_A^{mu nu}[...] =
T_B^{mu nu}[...] =

equation_of_motion_or_constraint =
conservation_or_transfer_law =
Q^nu[...] =
delta Q^nu[...] =
transfer_frame =
covariant_clock =

xi_definition =
xi_status = input | derived_output | calibrated_input | unknown
pre_observation_fixed_parameters =

known_model_sink =
escape_equation =
observable_not_absorbed_by_sink =
kill_condition =
```

Blank lines are failures, not TODOs.

## Minimum Pass Conditions

| Field group | Minimum requirement | Fail if |
| --- | --- | --- |
| candidate object | Names a variable or equation with units, domain, and role. | It is only `f_B = rho_B/(rho_A + rho_B)`, `xi ~= 10 Mpc`, or retained `Gamma(a)`. |
| density/pressure map | Supplies `rho_A`, `rho_B`, `p_A`, and `p_B`. | `p_B ~= -rho_B` is inserted as a label. |
| stress tensor | Supplies or derives `T_A^{mu nu}` and `T_B^{mu nu}`. | The proposal only reconstructs background `w(a)`. |
| conservation/transfer | Supplies conservation law or `Q^nu` with transfer frame. | `Q^nu` is copied from phenomenological IV/IDE without source derivation. |
| perturbation route | Supplies `delta Q^nu`, gauge/frame handling, and stability-relevant variables. | The route stops at background equations. |
| scale rule | Declares whether `xi` is input, derived output, calibrated input, or unknown. | `xi`, width, redshift, or amplitude are chosen after seeing target observations. |
| known-model distinction | Names the first known-model sink and a concrete escape equation. | The proposal claims novelty by naming foam language. |
| observable | Defines an observable that the known-model sink cannot absorb. | The observable is only a distance or expansion reconstruction. |

## Rejection Defaults

Reject the proposal immediately if it does any of the following:

1. Uses NASA/LAMBDA, BAO, LSS, or retained timing to choose `xi`, transition
   width, transition redshift, or amplitude.
2. Calls retained timing near `z ~= 2` a physical source.
3. Treats `f_B` bookkeeping as a physical state variable.
4. Inserts phase-B vacuum pressure without a stress-energy or equation-of-state
   derivation.
5. Reuses IV/IDE `Q^nu` as QFUDS microphysics.
6. Leaves `delta Q` undefined while making CMB, matter-power, or LSS claims.
7. Claims known-model distinction without comparing the first sink.

## Known-Model Sink Checklist

Before any optimistic interpretation, mark the first sink:

| If the candidate mainly does this | First sink |
| --- | --- |
| Fits background expansion through pressure history | effective `w(a)` |
| Writes one total dark-sector fluid | unified dark fluid |
| Transfers energy between CDM-like and vacuum-like sectors | interacting vacuum / IV/IDE |
| Evolves vacuum density with `H`, curvature, horizon, or cutoff | running vacuum / HDE |
| Uses `xi` as smoothing/cutoff/counterterm scale | LCDM+EFTofLSS or halo model |
| Averages cosmic-web geometry into expansion | backreaction |
| Changes force law, lensing slip, or screening | screened modified gravity |
| Introduces scalar action/order parameter | scalar-field DE / k-essence |

## Outlook Verdict

Current prospect:

```text
physical_QFUDS_near_term = low
phenomenological_comparator_value = moderate
known_model_overlap_risk = high
next_useful_work = candidate_equation_or_reject
```

Interpretation:

- The current branch is useful as an audit harness and phenomenological
  comparator.
- It should not be described as a promising physical theory yet.
- Most intuitive versions do overlap academic routes that are already known,
  constrained, or previously problematic.
- The only credible upside is a genuinely new constrained object that fills
  `T_mu_nu`, `p_B`, `Q^nu`, `delta Q`, `xi` rule, and an escape observable
  before seeing the observational kill-map.

## Next Executable Instruction

When a future candidate is proposed, fill this template first. If the template
cannot be filled, write a rejection note instead of moving to NASA/BAO, CMB,
matter-power, or likelihood comparisons.
