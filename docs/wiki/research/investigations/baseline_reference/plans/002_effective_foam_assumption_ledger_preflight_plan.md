---
doc_id: audit_2026_06_17_effective_foam_assumption_ledger_preflight_plan
title: "2026-06-17 Effective Foam Assumption Ledger Preflight Plan"
doc_type: reference
stage: reference
status: draft
evidence_role: audit
depends_on:
  - roadmap
  - qfuds_positioning
  - result_005_timing_prior_usefulness
  - audit_2026_06_12_foam_sector_to_gamma_derivation_feasibility_result
  - audit_2026_06_17_nasa_lambda_graphic_history_cache_closeout
  - asset_desi_dr2_lya_bao_2025
  - asset_eboss_dr16_lya_bao_2020
next_gate: execute only as a non-circularity ledger before any NASA or BAO baseline constraint map
last_updated: 2026-06-17
---

# 2026-06-17 Effective Foam Assumption Ledger Preflight Plan

## Purpose

This is a plan-only preflight record for the next checkpoint:

```text
effective galaxy/cosmic-web foam assumption ledger
```

The checkpoint asks whether a candidate effective foam scale such as
`xi ~= 10 Mpc` can be handled without circularly choosing the scale,
transition width, or amplitude after inspecting the same observations used as
support.

This document does not execute a physical derivation.

It does not create an experiment result.

It does not claim QFUDS support.

It does not use NASA/LAMBDA or BAO products as QFUDS evidence.

It does not promote retained timing near `z ~= 2` beyond phenomenological
IV/IDE comparator status.

It does not open Physical-QFUDS Level 2B.

## Status Boundary

Current repository status remains observer mode. The retained `Gamma(a)` branch
is a phenomenological IV/IDE comparator, not physical QFUDS. The forward
foam-sector route remains blocked until a non-circular foam-sector state
variable, calculable phase definitions, replacement transition object, and
equation set exist.

NASA/LAMBDA parameter-history assets and DESI/eBOSS Ly-alpha BAO products are
baseline constraint sources only. They may define what a future model must pass.
They must not be used to pick `xi`, width, and amplitude and then re-described
as the foam source.

## Preflight Verdict Labels

| Label | Meaning |
| --- | --- |
| `allowed_pre_model` | Allowed as a predeclared modeling assumption or bookkeeping choice, but not physical evidence. |
| `allowed_if_derived` | Allowed only if an independent equation derives it before comparison to baseline constraints. |
| `known_model_risk` | Likely collapses into LCDM+EFTofLSS, backreaction, running vacuum, screened modified gravity, IV/IDE, or effective `w(a)` unless an extra distinction is supplied. |
| `defer_until_defined` | Cannot be assessed until a missing variable, equation, or mapping is specified. |
| `circular_stop` | Do not proceed; the assumption was chosen from the same observational target later used as support. |

## Exhaustive Preflight Case Matrix

### 1. Role Of `xi ~= 10 Mpc`

| Case | Treatment | Verdict | Required next action |
| --- | --- | --- | --- |
| `xi` is predeclared before looking at NASA/BAO/LSS constraints | Input scale | `allowed_pre_model` | Record why this scale was chosen and what would falsify it. |
| `xi` follows from a foam-sector state equation | Derived output | `allowed_if_derived` | State the variable, units, normalization, equation, and failure criterion. |
| `xi` is inferred from independent non-overlapping data | Calibrated input | `known_model_risk` | Split calibration data from test data and state why this is not ordinary EFT or modified gravity fitting. |
| `xi` is picked after matching BAO/LSS/NASA axes | Post-hoc fit | `circular_stop` | Stop; cannot be described as foam-source evidence. |
| `xi` is left undefined while using `10 Mpc` language | Ambiguous scale | `defer_until_defined` | Define whether it is a length, cutoff, correlation scale, transition width, or coarse-graining cell. |

### 2. Meaning Of `xi`

| Case | Interpretation | Verdict | Main risk |
| --- | --- | --- | --- |
| Correlation length of a foam-sector variable | Physical-ish state property | `allowed_if_derived` | Needs a field, two-point function, and evolution law. |
| Coarse-graining scale for cosmic-web effective description | Effective description | `allowed_pre_model` | May be only analysis smoothing, not physics. |
| EFT cutoff or counterterm scale | EFTofLSS-like parameter | `known_model_risk` | Likely LCDM+EFTofLSS unless new observable appears. |
| Transition width in redshift or `ln(a)` | Timing-shape parameter | `circular_stop` if tuned to retained timing | Reuses the answer as the source. |
| Halo/nonlinear scale proxy | Structure proxy | `known_model_risk` | Can reduce to collapse-history or halo-model fitting. |
| BAO-related scale | Observational ruler | `circular_stop` if used to set the source scale | Confuses baseline standard ruler with foam micro/effective scale. |

### 3. Equation-Side Placement

| Case | Placement | Verdict | Required object |
| --- | --- | --- | --- |
| Geometry-side correction | Modified Einstein equation | `defer_until_defined` | Need field equation and Bianchi-compatible conservation statement. |
| Stress-energy-side component | Effective dark-sector `T_mu_nu` | `defer_until_defined` | Need density, pressure, equation of state, sound speed, and perturbation route. |
| Interaction-source form | IV/IDE-style `Q^nu` | `known_model_risk` | Need non-fitted source law and known-model distinction. |
| Background-only effective `w(a)` | Expansion reconstruction | `known_model_risk` | Not enough for physical QFUDS or perturbation viability. |
| Mixed geometry/stress-energy language | Unfixed bookkeeping | `circular_stop` if used to dodge constraints | Must choose a side before claiming a test. |

### 4. Replacement For Retained `Gamma(a)`

| Case | Replacement object | Verdict | Reason |
| --- | --- | --- | --- |
| Independent phase fraction `f_B(a)` with equation | Candidate transition object | `allowed_if_derived` | Can define transfer without inserting retained `Gamma(a)`. |
| Hazard rate from independent state variable `X` | Candidate source law | `allowed_if_derived` | Needs normalization and positivity constraints. |
| Direct reuse of retained `Gamma(a)` | Prototype curve as source | `circular_stop` | Retained timing is the output being explained. |
| External IV/IDE reconstructed coupling | Comparator | `allowed_pre_model` | Phenomenological comparison only, not physical source. |
| No replacement object | Missing model | `defer_until_defined` | Cannot test foam source. |

### 5. Data Handling

| Case | Data role | Verdict | Boundary |
| --- | --- | --- | --- |
| NASA/LAMBDA axes define baseline parameter families | Reference context | `allowed_pre_model` | No QFUDS evidence. |
| DESI/eBOSS Ly-alpha BAO define geometry kill thresholds | Baseline constraint | `allowed_pre_model` | No likelihood claim unless implemented. |
| NASA/BAO data select `xi`, width, and amplitude | Fit target | `circular_stop` | Do not call the fitted values a foam source. |
| Retained timing near `z ~= 2` selects candidate scale | Phenomenological prompt | `known_model_risk` | Comparator only; not source derivation. |
| Independent derivation predicts a scale, then NASA/BAO test it | Forward test | `allowed_if_derived` | This is the only route toward a non-circular observational checkpoint. |

### 6. Closest Known-Model Outcomes

| Candidate behavior | Closest known model risk | Verdict | Escape condition |
| --- | --- | --- | --- |
| Extra scale modifies clustering statistics only | LCDM+EFTofLSS | `known_model_risk` | Predict a fixed coefficient or observable not absorbed by EFT counterterms. |
| Averaging of inhomogeneous geometry changes expansion | Backreaction | `known_model_risk` | Provide averaging scheme and observable distinction from existing backreaction models. |
| Vacuum density runs with curvature or `H` | Running vacuum / HDE | `known_model_risk` | Show foam-specific state variable and transfer law. |
| Large-scale force or screening scale changes growth | Screened modified gravity | `known_model_risk` | Define field equation, screening behavior, and lensing/growth split. |
| Energy exchange between CDM-like and vacuum-like sectors | IV/IDE | `known_model_risk` | Supply non-fitted `Q^nu`, `delta Q`, and phase-B rationale. |

## Non-Circularity Checklist

Before executing any NASA + BAO baseline constraint map, the ledger must answer
all items below.

1. Define `xi` in units and semantics.
2. Mark `xi` as input, derived output, calibrated input, or unknown.
3. Record whether `xi ~= 10 Mpc` was chosen before or after looking at the
   target observations.
4. Separate calibration data from test data if any calibration is used.
5. Choose geometry-side, stress-energy-side, or IV/IDE-side placement.
6. State the conservation or consistency condition required by that placement.
7. Name the replacement object for retained `Gamma(a)`, or mark it missing.
8. State the closest known model family before claiming novelty.
9. State what observation or consistency check kills the assumption.
10. Stop if `xi`, width, or amplitude are tuned to the same NASA/BAO/LSS data
    later used as support.

## Minimum Ledger Output

The executed ledger should produce exactly one assumption table with these
columns:

| Column | Required content |
| --- | --- |
| `assumption` | The proposed scale, side choice, source object, or data-use rule. |
| `input_or_output` | `input`, `derived_output`, `calibrated_input`, `fitted_output`, or `unknown`. |
| `geometry_or_stress_energy` | `geometry`, `stress_energy`, `interaction_source`, `effective_w`, or `unassigned`. |
| `independent_or_fitted` | Whether the assumption is independent of the target observations. |
| `closest_known_model` | LCDM+EFTofLSS, backreaction, running vacuum, screened modified gravity, IV/IDE, effective `w(a)`, or unknown. |
| `required_equation` | The missing or supplied equation needed before testing. |
| `kill_condition` | The condition that blocks or rejects the assumption. |
| `preflight_verdict` | One of the verdict labels above. |

## Execution Decision

The next checkpoint should execute Candidate A first.

Candidate B, the NASA + BAO baseline constraint map, is deferred until this
ledger freezes the independent assumptions. If the ledger returns
`circular_stop` for `xi ~= 10 Mpc`, transition width, or amplitude, Candidate B
may still be written later as a general observational kill-map, but it must not
be used to support the effective foam assumption.
