---
doc_id: audit_2026_06_18_fB_known_model_reduction_checklist
title: "2026-06-18 f_B Known-Model Reduction Checklist"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - audit_2026_06_18_fB_stress_energy_definition_audit
  - audit_2026_06_18_foam_state_variable_definition_audit
  - qfuds_positioning
  - wiki_governance_001_physical_branch_summary
  - audit_2026_06_17_effective_foam_assumption_ledger_result
  - roadmap
next_gate: keep f_B as bookkeeping unless a future branch passes the known-model reduction checklist before NASA or BAO model-facing interpretation
last_updated: 2026-06-18
---

# 2026-06-18 f_B Known-Model Reduction Checklist

## Purpose

This checklist closes the next audit step after the
[f_B Stress-Energy Definition Audit](006_fB_stress_energy_definition_audit.md).

It asks where a proposed `f_B(x,a)` route is absorbed first if it tries to move
beyond bookkeeping without supplying new equations.

This document is not an experiment result, not QFUDS support, not a roadmap
change, and not Physical-QFUDS Level 2B admission.

## Workflow Application

This audit uses the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md)
only to preserve the baseline-source boundary.

Referenced source states remain:

- NASA/LAMBDA Graphic History: `asset_cached`;
- DESI DR2 Ly-alpha BAO: `asset_extracted_not_digitized` with `direct_table`
  products;
- eBOSS DR16 Ly-alpha BAO: `asset_cached` with `direct_table` products.

These states are baseline-source states only. They are not evidence for
`f_B`, `xi`, transition width, transition redshift, amplitude, retained timing,
or any known-model distinction.

## Reduction Order

Use this order before claiming that `f_B` defines a distinct foam-sector route.

| Step | Question | If yes, first reduction |
| ---: | --- | --- |
| 1 | Is `f_B` only `rho_B/(rho_A + rho_B)`? | bookkeeping identity |
| 2 | Is only the background pressure reconstructed as `w_F ~= -f_B`? | effective `w(a)` |
| 3 | Is the dark sector treated as one total stress tensor with pressure? | unified dark fluid |
| 4 | Are phase A and phase B kept separate with a transfer law? | interacting vacuum / IV/IDE |
| 5 | Is the vacuum density tied to `H`, curvature, or horizon scale? | running vacuum / HDE |
| 6 | Is `xi` only a smoothing, cutoff, or clustering scale? | LCDM+EFTofLSS or halo-model coarse graining |
| 7 | Is the effect attributed to averaged inhomogeneous geometry? | backreaction |
| 8 | Does the route modify forces, lensing, or screening? | screened modified gravity |

If the route reaches any row without the escape condition in the table below,
it is not a physical-QFUDS branch. It is a known-model comparison target.

## Known-Model Checklist

| Candidate `f_B` move | First known-model sink | Why it reduces | Required escape condition | Current verdict |
| --- | --- | --- | --- | --- |
| `f_B = rho_B/(rho_A + rho_B)` | bookkeeping identity | It only names an already-existing split. | Independent equations for `rho_A`, `rho_B`, `p_A`, and `p_B`. | `reject_as_physical` |
| `w_F(a) = -f_B(a)` | effective `w(a)` | The route reconstructs an expansion history without a physical phase source. | Stress tensor, perturbation prescription, and observable split not captured by `w(a)`. | `known_model_sink` |
| `p_F = -f_B rho_F` as one medium | unified dark fluid | The A/B language becomes a decomposed total dark-sector fluid. | Non-adiabatic two-phase equations with controlled sound speed and phase-specific observables. | `known_model_sink` |
| Separate A/B sectors plus `Q^nu` | interacting vacuum / IV/IDE | A vacuum-like phase exchanging energy with CDM-like phase A is the standard interacting-vacuum form. | Non-fitted source `X`, derived `Q^nu[X,...]`, phase-B `w ~= -1` rationale, and `delta Q` route. | `known_model_sink` |
| `df_B/dln(a)` matched to retained timing | phenomenological IV/IDE fit | It rewrites retained `Gamma(a)` in phase-fraction variables. | A forward source equation fixed before retained timing or baseline observations are inspected. | `circular_stop` |
| Constant or LCDM-matching phase split | LCDM null limit | With no physical transfer, the split can reproduce CDM plus cosmological constant bookkeeping. | A nonzero, derived, testable deviation that is not fitted after the fact. | `known_model_sink` |
| `f_B` tied to `H`, curvature, or horizon area | running vacuum / HDE | Vacuum-density evolution from background scalars is already a known dark-energy route. | Foam-specific state variable and transfer relation not expressible as ordinary running-vacuum/HDE terms. | `known_model_sink` |
| `xi` controls only clustering counterterms | LCDM+EFTofLSS | A coarse-graining or cutoff scale can be absorbed into EFT/halo-model nuisance structure. | Fixed coefficient or observable consequence not absorbed by EFT counterterms. | `known_model_sink` |
| `f_B` from averaged cosmic-web geometry | backreaction | Expansion changes from inhomogeneous averaging are backreaction language. | Defined averaging scheme, gauge treatment, and observable distinction from existing backreaction models. | `known_model_sink` |
| `xi` changes force law, slip, or screening | screened modified gravity | A large-scale transition in growth/lensing belongs first to modified-gravity parameterizations. | Field equation, screening mechanism, and lensing/growth split fixed before fitting. | `known_model_sink` |
| `f_B` as scalar order parameter with action | scalar-field DE / k-essence | Once an action gives `rho`, `p`, and perturbations, the route enters scalar-field model space. | Show the action or coarse-grained limit is not an existing scalar-field or k-essence construction. | `known_model_risk` |

## Required Distinction Package

No `f_B` route may claim known-model distinction unless it supplies all items
below before using NASA/LAMBDA, BAO, LSS, or retained timing as model-facing
inputs:

1. A state variable that is not just `rho_B/(rho_A + rho_B)`.
2. A non-bookkeeping `T_A^{\mu\nu}` and `T_B^{\mu\nu}`.
3. A reason phase B has `w ~= -1`.
4. A conservation-compatible `Q^\nu` derived from the source.
5. A `delta Q` route with gauge/frame handling.
6. A rule for `xi` that is fixed before the target observations.
7. A perturbation prescription with sound-speed and stability conditions.
8. An observable not absorbed by effective `w(a)`, unified dark fluid, IV/IDE,
   running vacuum, HDE, EFTofLSS, backreaction, or screened modified gravity.

Failure to supply any item keeps the route in comparison/audit mode.

## NASA/BAO Boundary

NASA/LAMBDA and BAO products may still be used later as an observational
kill-map. They must not be used to select `f_B`, `xi`, transition width,
transition redshift, or amplitude and then described as supporting the source.

The retained timing near `z ~= 2` remains a phenomenological timing fingerprint
only. It is not a physical source, and it cannot rescue a route that failed the
checklist above.

## Decision

The current `f_B` route reduces in this order:

```text
identity/bookkeeping
-> effective w(a) if only background pressure is reconstructed
-> unified dark fluid if written as one total stress tensor
-> interacting vacuum / IV/IDE if written as two sectors plus transfer
```

The route does not currently pass known-model distinction.

## Status Boundary Closeout

`f_B` physical route: rejected at current definition.

Known-model distinction: not supplied.

QFUDS support: no.

Roadmap status change: no.

Physical-QFUDS Level 2B change: no.

NASA/LAMBDA or BAO model-facing interpretation: no.
