---
doc_id: exp_003_phenomenological_perturbation_closure
title: "Experiment 003: Phenomenological Perturbation Closure Audit"
doc_type: experiment
stage: "2"
status: completed
evidence_role: proxy_scan
depends_on:
  - qfuds_phenomenological_perturbations
  - perturbation_gate
next_gate: result_003 phenomenological closure audit
last_updated: 2026-06-08
---

# Experiment 003: Phenomenological Perturbation Closure Audit

Date: 2026-06-08

## Objective

Determine whether the retained `Gamma(a)` branch can be written as a stable,
gauge-declared, mathematically closed linear perturbation system while
`Gamma(a)` remains phenomenological.

This is a Level 2A experiment specification. It is not a physical derivation of
QFUDS.

## Hypothesis

A phenomenological phase-A-frame interacting-vacuum closure may be mathematically
testable. It may still fail through gauge ambiguity, instability, arbitrary
transfer prescription, or equivalence to ordinary interacting dark energy.

## Scope

This experiment tests only linear perturbation closure.

It does not test:

- microphysical foam action;
- derived `Gamma(a)`;
- CLASS/CAMB CMB spectra;
- matter-power likelihoods;
- DESI, Euclid, Roman, BAO, or supernova likelihoods;
- QFUDS novelty.

## Baseline Closure

Use conformal Newtonian gauge for the first implementation.

Background:

```text
rho_A' + 3 Hc rho_A = -Q
rho_B' + 3 Hc (1 + w_B) rho_B = +Q
Q = Hc Gamma(a) rho_A
```

Transfer:

```text
Q_A^mu = -Q u_A^mu
Q_B^mu = +Q u_A^mu
```

Perturbative transfer:

```text
deltaQ = Q delta_A
deltaGamma = 0
```

This `deltaGamma = 0` rule is a phenomenological gauge-fixed closure, not a
derived physical statement.

Phase A:

```text
w_A = 0
c_s,A^2 = 0
sigma_A = 0
variables: delta_A, theta_A
```

Phase B variants:

```text
P1: interacting vacuum treatment, no ordinary theta_B fluid velocity
P2: regularized fluid with w_B = -0.999, c_s,B^2 = 1, sigma_B = 0
```

## Runs

Run all cases against the zero-transfer LCDM control. `R0` is the zero-transfer
control (exact LCDM). Every non-zero run uses the same `information_production`
`Gamma(a)` shape (`collapse_a = 0.35`, `collapse_nu = 5.0`) and differs only in
the amplitude `gamma0`:

```text
R0:  gamma0 = 0      zero-transfer LCDM control (no information production)
R1:  gamma0 = 0.02   retained information-production amplitude (documented exp_002 value)
R2a: gamma0 = 0.005  smaller predeclared amplitude
R2b: gamma0 = 0.01   smaller predeclared amplitude
R3:  gamma0 = 0.04   larger predeclared amplitude
```

Stopping criterion: escalate the amplitude in predeclared steps and stop at the
first background or perturbation failure. `R3` (`gamma0 = 0.04`) is the largest
amplitude tested. Do not retune after seeing perturbation failures.

## Execution

Reproduce all runs and diagnostics with:

```bash
python3 scripts/run_minimal_model.py --exp-003-perturbation-closure --outdir outputs
```

The `--exp-003-perturbation-closure` flag runs the full R0–R3 x P1/P2 suite with
the amplitudes above; `--outdir` selects the output directory (default
`outputs`). This writes the summary JSON, the stability-diagnostics CSV, and the
per-mode CSVs listed in the result document.

## Wavenumber Grid

Use a minimal logarithmic grid:

```text
k = 1e-4, 1e-3, 1e-2, 1e-1 h/Mpc
```

The first pass is a stability and closure audit, not a precision matter-power
calculation.

## Required Outputs

Record:

- `delta_A(a,k)`;
- `theta_A(a,k)`;
- `delta_B(a,k)` or interacting-vacuum substitute;
- `theta_B(a,k)` only for the regularized-fluid variant;
- metric perturbations;
- total curvature diagnostic;
- total energy-momentum conservation residual;
- instability flags;
- comparison to `Gamma=0`.

## Failure Criteria

The closure fails if any of the following occur:

1. unbounded superhorizon curvature growth;
2. negative physical densities;
3. singular behavior as `w_B -> -1`;
4. strong dependence on arbitrary `deltaQ` or transfer-frame choice;
5. loss of phase-A clustering behavior;
6. phase-B clustering incompatible with a vacuum-pressure interpretation;
7. no gauge-consistent interpretation;
8. equivalence to ordinary interacting vacuum without a QFUDS-specific constraint.

## Decision Rule

If all tested closures fail, QFUDS remains at Level 1.5 and the retained branch
is demoted to ordinary phenomenological interacting dark energy.

If one closure is stable, QFUDS may continue only as Level 2A phenomenology.
Level 2B remains blocked until `Gamma(a)` or the transfer four-vector is
physically derived or otherwise fixed by Level 1.5.

## Required Result Document

Implementation and execution produced:

```text
docs/04_results/030_result_003_phenomenological_perturbation_closure.md
```

No experiment 003 result is complete until the result document, decision-log
entry, and roadmap update exist.
