---
doc_id: audit_2026_06_18_candidate_equation_triage_closeout
title: "2026-06-18 Candidate Equation Triage Closeout"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - plan_2026_06_18_candidate_equation_proposal_template
  - audit_2026_06_18_baseline_reference_chain_closure
  - wiki_governance_004_missing_physics_map
  - roadmap
next_gate: no physical-QFUDS branch unless a new candidate fills the admission template before baseline constraints are used
last_updated: 2026-06-18
---

# 2026-06-18 Candidate Equation Triage Closeout

## Purpose

This closeout applies the
[Candidate Equation Proposal Template](../plans/010_candidate_equation_proposal_template.md)
to the currently available QFUDS candidate lanes.

It is not a new theory proposal.

It is not an experiment result.

It does not claim QFUDS support.

It does not open Physical-QFUDS Level 2B.

## Workflow Application

This closeout uses the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md)
only to preserve the external-source boundary.

No new web, literature, PDF, table, product, cache, or digitization claim is
introduced here. Existing baseline source states remain inherited from the
baseline-reference chain:

- NASA/LAMBDA Graphic History: `asset_cached`;
- NASA/LAMBDA data-reference matrix: `manual_structured_extract`;
- DESI DR2 Ly-alpha BAO: `asset_extracted_not_digitized` with `direct_table`
  products;
- eBOSS DR16 Ly-alpha BAO: `asset_cached` with `direct_table` products.

These states remain baseline constraints only. They are not QFUDS evidence and
are not used below to choose `xi`, transition width, transition redshift, or
amplitude.

## Triage Rule

A candidate is admitted only if it fills all five physical-branch admission
items before observational baseline constraints are used:

```text
X =
Q^nu =
why phase B has w ~= -1 =
delta Q route =
known-model distinction =
```

Partial answers are failures for physical admission. They can remain as audit
material or comparison targets, but not as Physical-QFUDS branches.

## Candidate Triage Matrix

| Candidate lane | Candidate object attempted | X | Q^nu | phase-B w ~= -1 rationale | delta Q route | Known-model distinction | Triage verdict |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Retained `Gamma(a)` lift | Treat retained timing as the source object | no; retained timing is a phenomenological fingerprint, not a source scalar | no; only IV/IDE-like background transfer can be written | no | no; Level 2A P1 closure is phenomenological | no; first sink is IV/IDE | Reject as physical QFUDS; retain only as IV/IDE comparator. |
| `f_B(x,a)` phase fraction | Treat phase-B fraction as state variable | no; bookkeeping fraction without dynamics | no | no; `p_B ~= -rho_B` would be inserted | no | no; first sinks are effective `w(a)`, unified dark fluid, and IV/IDE | Reject as physical QFUDS; keep as bookkeeping only. |
| `xi ~= 10 Mpc` scale | Treat effective galaxy/cosmic-web scale as foam object | no; scale is not a state variable | no | no | no | no; first sinks are LCDM+EFTofLSS, halo model, or coarse-graining | Reject as physical QFUDS; keep as candidate scale label only. |
| Black-hole / Source-X route | Treat compact-object or strong-gravity history as source | not currently normalized into a source scalar | no | no; smooth vacuum pressure is not derived from compact objects, heat, radiation, or remnants | no | no; first sinks include black-hole-coupled DE, remnant DM, or HDE-like routes | Blocked; a future version must supply stress-energy and pressure before re-entry. |
| Horizon / HDE / running-vacuum route | Treat horizon or cutoff relation as dark-energy source | possible only by adopting a known route first | no QFUDS-specific transfer supplied | only if inherited from HDE/running-vacuum assumptions | no | no; first sink is HDE or running vacuum | Reject as QFUDS physical branch; allowed only as known-model comparison. |
| Geometry / backreaction route | Put foam effect on geometry side | no state variable or averaging object supplied | not applicable unless moved to source side | no | no perturbation prescription | no; first sinks are backreaction or modified gravity | Blocked until a field equation, Bianchi-compatible conservation rule, and perturbations exist. |
| Effective action / order-parameter route | Derive both phases from an action or field | not supplied | not supplied | not supplied | not supplied | not supplied; first sink would likely be scalar-field DE, k-essence, unified fluid, or IV/IDE | Not a current candidate; this is the only credible re-entry shape if equations are later supplied. |

## Admission Result

No current candidate fills the admission template.

```text
physical_QFUDS_candidate_admitted = no
observer_mode = unchanged
Level_2B = blocked
retained_timing_use = phenomenological_IV_IDE_comparator_only
NASA_LAMBDA = baseline_constraint_only
BAO = observational_kill_map_only
next_physical_work = blocked_until_new_equations
```

## What This Means

The current repository has a useful audit harness, but it does not currently
have a physical QFUDS model candidate.

That is a negative scientific result for the physical-theory branch, not a
roadmap upgrade.

The retained timing signal remains useful only as a phenomenological comparator
because it can still ask whether a class of IV/IDE timing histories deserves
external comparison. It does not explain its own source.

## Stop Conditions

Stop immediately if a future route does any of the following:

1. Uses NASA/LAMBDA, BAO, LSS, CMB, or retained timing targets to choose `xi`,
   transition width, transition redshift, or amplitude.
2. Calls retained `Gamma(a)` or the `z ~= 2` timing fingerprint a foam source.
3. Treats `f_B` as a physical state variable without `rho`, `p`, `T_mu_nu`,
   `Q^nu`, and `delta Q`.
4. Moves to a baseline constraint map before the candidate equation template is
   filled.
5. Claims known-model distinction without first naming the closest known-model
   sink and the equation that escapes it.

## Next Executable Instruction

Do not run another NASA/BAO, CMB, matter-power, or likelihood interpretation
from the current candidate set. If no new candidate equation is supplied, write
a physical-branch closure note that records the current physical-QFUDS route as
blocked by admission failure while preserving retained timing as a separate
phenomenological IV/IDE comparator.

## Status Boundary Closeout

QFUDS support: no.

Known-model distinction: no.

Roadmap status change: no.

Physical-QFUDS Level 2B change: no.

NASA/LAMBDA or BAO model-facing interpretation: no.
