---
doc_id: exp_000_lcdm_baseline
title: "Experiment 000: Zero-Transfer LCDM Baseline"
doc_type: experiment
stage: "1"
status: completed
evidence_role: control
depends_on:
  - qfuds_v0_2
next_gate: gamma law background scan
last_updated: 2026-06-09
---

# Experiment 000: Zero-Transfer LCDM Baseline

Date: 2026-06-08

### Objective

Verify that the implemented two-phase QFUDS background reproduces LCDM when phase transfer is turned off.

### Hypothesis

If `Gamma(a) = 0`, phase A should scale as pressureless matter and phase B should remain constant. The result should be the LCDM limit of the model.

### Scope

This is a background-only control. It tests the null limit of the implemented
two-phase background equations. It does not test perturbations, CMB spectra,
matter power, survey likelihoods, or microphysical novelty.

### Method

Run the minimal model with zero transfer:

```bash
python3 scripts/run_minimal_model.py --gamma0 0 --beta 0
```

The test suite also checks this path in `tests/test_gamma_v03.py`.

### Parameters

```text
gamma_model = powerlaw
gamma0 = 0
beta = 0
H0 = 67.4
Omega_b0 = 0.0493
Omega_r0 = 9.2e-5
Omega_A0 = 0.2649
Omega_Bfoam0 = 0.6858
```

### Outputs

- `outputs/qfuds_gamma0_beta0.csv`
- `outputs/qfuds_gamma0_beta0.png`

CSV columns include `Gamma`, `H_over_H_LCDM`, `rho_A_over_rhocrit0`, `rho_Bfoam_over_rhocrit0`, `Omega_A`, `Omega_Bfoam`, `w_dark`, `w_Bfoam_eff`, `D`, and `f_sigma8_proxy`.

### Failure Criteria

The control fails if `Gamma(a)=0` does not keep phase B constant, does not make
phase A dilute as pressureless matter, produces non-finite outputs, or fails the
LCDM-limit regression checks in `tests/test_gamma_v03.py`.

### Result

The zero-transfer path is the exact LCDM-limit control case. It is required for reproducibility and for comparing all nonzero transfer laws.

### Decision

Keep as baseline. It is not a new QFUDS prediction.

### Next Step

Use this baseline for every future background, growth, perturbation, and Boltzmann-code comparison.
