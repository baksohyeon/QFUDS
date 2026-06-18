---
doc_id: audit_2026_06_18_fB_stress_energy_definition_audit
title: "2026-06-18 f_B Stress-Energy Definition Audit"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - audit_2026_06_18_foam_state_variable_definition_audit
  - audit_2026_06_17_foam_state_variable_definition_plan
  - qfuds_v0_2
  - qfuds_level_1_5_transfer_four_vector_derivation_attempt
  - result_004_p1_model_family_positioning
  - roadmap
next_gate: reject f_B as a physical route unless a future theory note supplies a non-bookkeeping stress tensor, phase-B equation of state, transfer law, and perturbation route
last_updated: 2026-06-18
---

# 2026-06-18 f_B Stress-Energy Definition Audit

## Purpose

This audit executes the next checkpoint implied by the
[Foam State Variable Definition Audit](005_foam_state_variable_definition_audit.md).

It asks whether the stress-energy-side `f_B(x,a)` bookkeeping route can supply
the missing objects before NASA/LAMBDA or BAO baseline constraints are used for
model-facing interpretation:

- `rho_A`;
- `rho_B`;
- `p_A`;
- `p_B`;
- conservation or transfer law;
- perturbation route;
- known-model reduction test.

This is a definition audit only. It is not an experiment result, not QFUDS
support, and not Physical-QFUDS Level 2B admission.

## Workflow Application

This audit uses the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md)
only to preserve the external baseline-source boundary.

Referenced source states remain:

- NASA/LAMBDA Graphic History: `asset_cached`;
- DESI DR2 Ly-alpha BAO: `asset_extracted_not_digitized` with `direct_table`
  products;
- eBOSS DR16 Ly-alpha BAO: `asset_cached` with `direct_table` products.

These states are baseline-source states only. They are not evidence for
`f_B`, `xi`, transition width, transition redshift, amplitude, or retained
timing.

## Local Evidence Used

| Source | Relevant constraint |
| --- | --- |
| [QFUDS v0.2 Two-Phase Background](../../../../../02_theory/000_qfuds_v0_2_two_phase_background.md) | Defines `rho_dark = rho_A + rho_B`, `w_A ~= 0`, `w_B ~= -1`, and the background `Gamma(a)` transfer equations. It also states that `Gamma = 0` is LCDM and free `Gamma(a)` is interacting dark sector. |
| [Level 1.5 Transfer Four-Vector Derivation Attempt](../../../../../02_theory/015_qfuds_level_1_5_transfer_four_vector_derivation_attempt.md) | Shows that a minimal `Q^nu` can reproduce the background equations as an interacting-vacuum ansatz, but does not derive phase-B vacuum pressure, a local source scalar, or `delta Q`. |
| [P1 Model-Family Positioning](../../../../../04_results/030_result_004_p1_model_family_positioning.md) | Classifies the retained branch as phenomenological IV/IDE comparator only, with no physical-QFUDS promotion. |
| [Foam State Variable Definition Audit](005_foam_state_variable_definition_audit.md) | Already classifies `f_B(x,a)` as bookkeeping-only unless a stress tensor, equation of state, transfer law, and perturbation route are supplied. |

## Attempted f_B Definition

The narrowest phase-fraction definition is:

```math
f_B = {\rho_B \over \rho_A + \rho_B},
\qquad
\rho_F = \rho_A + \rho_B.
```

This gives:

```math
\rho_B = f_B\rho_F,
\qquad
\rho_A = (1-f_B)\rho_F.
```

This is allowed as bookkeeping. It is not a physical definition because it
requires `rho_A`, `rho_B`, or `rho_F` to already exist. It does not say what
the foam sector is, why it splits, or why the phase-B part has vacuum pressure.

## Pressure Closure Attempt

The inherited two-phase pressure assignment is:

```math
p_A \simeq 0,
\qquad
p_B \simeq -\rho_B.
```

With the bookkeeping definition above, this implies:

```math
p_F = p_A + p_B \simeq -f_B\rho_F,
\qquad
w_F \simeq -f_B.
```

This is not a derivation. It inserts the phase-B equation of state and then
rewrites it as an effective equation of state. Without an independent reason
for `p_B ~= -rho_B`, the route reduces to effective `w(a)`, unified dark fluid,
or interacting-vacuum language.

## Conservation-Law Attempt

Total conservation can be imposed in the usual split form:

```math
\nabla_\mu T_A^{\mu\nu} = -Q^\nu,
\qquad
\nabla_\mu T_B^{\mu\nu} = +Q^\nu,
\qquad
\nabla_\mu(T_A^{\mu\nu}+T_B^{\mu\nu}) = 0.
```

But `f_B` alone does not define `T_A^{\mu\nu}`, `T_B^{\mu\nu}`, or `Q^\nu`.
If `df_B/d\ln a` is chosen to match the retained timing, then `f_B` is just a
reparameterized `Gamma(a)` output. That is the circular route this checkpoint
was meant to prevent.

## Definition Matrix

| Required object | Current `f_B` route can supply? | Reason | Verdict |
| --- | --- | --- | --- |
| `rho_A` | formal only | `rho_A = (1-f_B)rho_F` is an identity unless `rho_F` and `f_B` have independent equations. | bookkeeping |
| `rho_B` | formal only | `rho_B = f_B rho_F` does not explain phase-B origin. | bookkeeping |
| `p_A` | assumed | `p_A ~= 0` is inherited from CDM-like phase A. | not derived |
| `p_B` | no | `p_B ~= -rho_B` is inserted, not produced by `f_B`. | fail |
| `T_A^{mu nu}` | no | No full stress tensor, sound speed, frame, anisotropic stress, or perturbation prescription follows from `f_B`. | fail |
| `T_B^{mu nu}` | no | Vacuum-like stress is assumed, not derived. | fail |
| `Q^nu` | no | `f_B` does not define the transfer direction, covariant clock, source scalar, or efficiency. | fail |
| `delta Q` | no | A perturbation of the transfer requires local source and gauge/frame choices absent from the route. | fail |
| `xi` | no | `xi ~= 10 Mpc` is not generated by `f_B`; using observations to choose it would be circular. | blocked |
| known-model distinction | no | The route first lands in effective `w(a)`, unified dark fluid, or IV/IDE unless new equations are supplied. | fail |

## Rejection Rule

The `f_B` stress-energy route fails as a physical route if any of these remain
true:

1. `f_B` is defined only as `rho_B/(rho_A + rho_B)`.
2. `p_B ~= -rho_B` is assumed without a stress-energy or equation-of-state
   derivation.
3. `df_B/dln(a)` is fitted to retained timing or baseline observations.
4. `Q^nu` is absent or copied from a phenomenological IV/IDE ansatz.
5. `delta Q` is set by closure choice instead of a local source route.
6. `xi`, transition width, transition redshift, or amplitude are chosen after
   inspecting NASA/LAMBDA, DESI/eBOSS BAO, LSS, or retained-timing targets.

All six conditions apply to the current repository state except where the
route is explicitly kept as bookkeeping.

## Decision

The audit returns:

```text
f_B_bookkeeping = allowed
f_B_physical_state_variable = rejected_current_definition
rho_A_rho_B_route = identity_only
p_B_route = missing_derivation
T_mu_nu_route = missing
Q^nu_route = missing
delta_Q_route = missing
known_model_distinction = not_supplied
NASA_BAO_model_interpretation = blocked
Physical_QFUDS_Level_2B = no
```

The remaining admissible use of `f_B` is notation for an already-defined phase
split. It must not be treated as the source of the split.

## Next Task Boundary

Do not proceed to model-facing NASA/BAO interpretation from this route.

The next executable checkpoint, if continued, must be a rejection-preserving
theory-definition note that either supplies all of the following or closes the
route:

- a non-bookkeeping `T_A^{\mu\nu}` and `T_B^{\mu\nu}`;
- a reason phase B has `w ~= -1`;
- a conservation-compatible `Q^\nu`;
- a `delta Q` route;
- a rule for `xi` that is not fitted from the same observations used for
  claimed support;
- an explicit reduction test against unified dark fluid, IV/IDE, effective
  `w(a)`, running vacuum, and screened modified gravity.

Until then, `f_B` remains an accounting variable only.

## Status Boundary Closeout

QFUDS support: no.

Roadmap status change: no.

Physical-QFUDS Level 2B change: no.

Retained `Gamma(a)` physical promotion: no.

NASA/LAMBDA or BAO model-facing interpretation: no.
