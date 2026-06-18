---
doc_id: audit_2026_06_18_known_model_escape_equation_templates
title: "2026-06-18 Known-Model Escape Equation Templates"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - audit_2026_06_18_fB_known_model_reduction_checklist
  - audit_2026_06_18_fB_stress_energy_definition_audit
  - qfuds_positioning
  - wiki_governance_004_missing_physics_map
  - roadmap
next_gate: use these templates as preregistration gates before any f_B, xi, NASA, or BAO model-facing interpretation
last_updated: 2026-06-18
---

# 2026-06-18 Known-Model Escape Equation Templates

## Purpose

This document turns the
[f_B Known-Model Reduction Checklist](007_fB_known_model_reduction_checklist.md)
into equation templates.

It does not propose a new model. It states the minimum equations a future
candidate would need before claiming it escapes a known-model sink.

This is not an experiment result, not QFUDS support, not a roadmap change, and
not Physical-QFUDS Level 2B admission.

## Workflow Application

This audit uses the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md)
only to preserve the baseline-source boundary.

Referenced source states remain:

- NASA/LAMBDA Graphic History: `asset_cached`;
- DESI DR2 Ly-alpha BAO: `asset_extracted_not_digitized` with `direct_table`
  products;
- eBOSS DR16 Ly-alpha BAO: `asset_cached` with `direct_table` products.

These states are baseline-source states only. They are not evidence for any
candidate equation, scale, transition width, amplitude, or known-model
distinction.

## Template Rule

Every future `f_B`, `X`, `xi`, or foam-sector proposal must fill this shape
before NASA/LAMBDA, BAO, LSS, or retained timing is used for model-facing
interpretation:

```text
sink_to_escape =
candidate_new_object =
equation_of_motion_or_constraint =
stress_energy_mapping =
pressure_or_equation_of_state =
conservation_or_transfer_law =
perturbation_route =
scale_rule =
observable_not_absorbed_by_sink =
pre_observation_fixed_parameters =
kill_condition =
```

If any line is blank, the proposal remains in audit/comparison mode.

## Escape Templates

| Sink | Reduction symptom | Minimum escape equations | Non-circular rule | Current status |
| --- | --- | --- | --- | --- |
| bookkeeping identity | `f_B = rho_B/(rho_A + rho_B)` only renames the split | Define a new object `Y` with `rho_A[Y]`, `rho_B[Y]`, `p_A[Y]`, `p_B[Y]`, and an evolution equation for `Y`. | `Y` must be fixed before fitting expansion, BAO, LSS, or retained timing. | `not_supplied` |
| effective `w(a)` | only reconstructs background pressure or expansion | Supply `T_A^{mu nu}`, `T_B^{mu nu}`, sound speed, anisotropic stress rule, and an observable not reproducible by `w(a)`. | Do not choose `w(a)` or `f_B(a)` after inspecting the same distance data used as support. | `not_supplied` |
| unified dark fluid | collapses into one total dark-sector stress tensor | Supply non-adiabatic two-phase equations, phase-specific perturbations, controlled sound speed, and a measurable A/B split. | The phase split must not be an arbitrary decomposition of a fitted total fluid. | `not_supplied` |
| interacting vacuum / IV/IDE | phase A and phase B exchange energy through a coupling | Supply `Q^nu = Q^nu[X, ...]`, phase-B `w ~= -1` rationale, and `delta Q^nu` from the same `X`. | `Q^nu` must not be copied from retained `Gamma(a)` or tuned to retained timing. | `not_supplied` |
| LCDM null limit | no transfer or only constant CDM plus cosmological constant | Supply a nonzero derived deviation and a predeclared limit where it vanishes. | The deviation must be predicted before looking at NASA/LAMBDA, BAO, or LSS residuals. | `not_supplied` |
| running vacuum / HDE | vacuum density is a function of `H`, curvature, horizon area, or IR cutoff | Supply a foam-specific cutoff or state variable, `rho_B[Y]`, and a transfer or conservation law not reducible to ordinary running-vacuum/HDE terms. | Do not infer the cutoff scale from the same distance or BAO observations used as support. | `not_supplied` |
| LCDM+EFTofLSS / halo coarse graining | `xi` acts only as smoothing scale, cutoff, or counterterm | Supply a fixed coefficient or scale-dependent observable that cannot be absorbed by EFT counterterms or halo nuisance parameters. | `xi` must be declared as input or derived output before fitting clustering data. | `not_supplied` |
| backreaction | averaged inhomogeneous geometry changes expansion | Supply the averaging scheme, gauge treatment, effective stress-energy or modified Friedmann term, and a distinct observable. | Do not choose the averaging domain after matching the desired expansion history. | `not_supplied` |
| screened modified gravity | force law, slip, screening, or lensing/growth relation changes | Supply field equations, screening mechanism, conservation/Bianchi consistency, and lensing-growth split. | Screening scale and coupling must be fixed before fitting growth or lensing tensions. | `not_supplied` |
| scalar-field DE / k-essence | a scalar action supplies `rho`, `p`, and perturbations | Supply the action or coarse-grained limit, map it to `rho_A/rho_B`, and show which term is not standard scalar-field/k-essence behavior. | Do not rename a standard scalar action as foam without a new constrained term. | `not_supplied` |

## Equation Skeletons

These skeletons are placeholders for future proposals. They are not filled by
the current repository.

### Stress-Energy Escape

```text
Y =
T_A^{mu nu}[Y] =
T_B^{mu nu}[Y] =
p_A[Y] =
p_B[Y] =
nabla_mu (T_A^{mu nu} + T_B^{mu nu}) =
```

Fails if `p_B ~= -rho_B` is inserted only as a label.

### Transfer Escape

```text
X =
Q^nu[X, rho_A, rho_B, u_A^nu, u_B^nu, ...] =
delta Q^nu =
transfer frame =
covariant clock =
```

Fails if `Q^nu` is only `H Gamma(a) rho_A u_A^nu` with `Gamma(a)` chosen from
retained timing.

### Scale Escape

```text
xi =
xi role = input | derived_output | calibrated_input
xi equation =
calibration data =
test data =
```

Fails if `xi`, transition width, transition redshift, or amplitude are selected
after inspecting the same NASA/LAMBDA, BAO, LSS, or retained-timing targets
used as support.

### Observable Escape

```text
observable =
known-model sink =
why sink cannot absorb it =
required data product =
kill condition =
```

Fails if the observable is only a background-distance or expansion-history
reconstruction.

## Decision

The current repository fills none of the escape templates.

Therefore:

```text
f_B_known_model_escape = not_supplied
xi_known_model_escape = not_supplied
Q^nu_escape = not_supplied
delta_Q_escape = not_supplied
NASA_BAO_model_interpretation = blocked
Physical_QFUDS_Level_2B = no
```

## Status Boundary Closeout

QFUDS support: no.

Known-model distinction: no.

Roadmap status change: no.

Physical-QFUDS Level 2B change: no.

NASA/LAMBDA or BAO model-facing interpretation: no.
