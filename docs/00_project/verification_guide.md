# QFUDS Verification Guide

Date: 2026-06-08

This guide explains the current reproducible checks and what each one means.

None of these checks proves QFUDS correct. They only say which toy versions survive the specific test that was run.

## 1. LCDM Baseline

Command:

```bash
python3 scripts/run_minimal_model.py --gamma0 0 --beta 0
```

What to inspect:

- `outputs/qfuds_gamma0_beta0.csv`
- `outputs/qfuds_gamma0_beta0.png`
- `docs/03_experiments/exp_000_lcdm_baseline.md`
- `docs/04_results/result_000_lcdm_baseline.md`

What it means:

This confirms the null limit. With no phase transfer, the two-phase background behaves as LCDM. This is a control case, not evidence of novelty.

## 2. v0.3 Gamma-Law Background Scan

Command:

```bash
python3 scripts/run_minimal_model.py --all-v03
```

What to inspect:

- `docs/03_experiments/exp_001_gamma_scan_v03.md`
- `docs/04_results/result_001_gamma_scan_v03.md`
- `docs/04_results/qfuds_v0_3_gamma_laws.md`
- `outputs/qfuds_constant_gamma0.01_beta0.csv`
- `outputs/qfuds_growth_driven_gamma0.01_beta0.csv`
- `outputs/qfuds_collapsed_fraction_toy_gamma0.03_beta0.csv`
- `outputs/qfuds_black_hole_entropy_proxy_gamma0.03_beta0.csv`
- `outputs/qfuds_star_formation_proxy_gamma0.003_beta0.csv`

What it means:

This scan asks whether candidate `Gamma(a)` laws already fail at the background level. Constant transfer and ungated growth-driven transfer fail at the tested amplitudes. Low-redshift proxies survive only as candidates for stronger tests.

## 3. v0.4 Entropy / Information Scan

Command:

```bash
python3 scripts/run_minimal_model.py --all-v04
```

What to inspect:

- `docs/03_experiments/exp_002_entropy_information_scan_v04.md`
- `docs/04_results/qfuds_v0_4_entropy_laws.md`
- `outputs/qfuds_gravitational_entropy_gamma0.003_beta0.csv`
- `outputs/qfuds_information_production_gamma0.02_beta0.csv`
- `outputs/qfuds_horizon_information_gamma0.03_beta0.csv`

What it means:

This scan asks whether the transfer law can be tied to a concrete entropy or information source. Broad entropy language mostly fails or reduces to known models. Press-Schechter-style information production is the narrow branch kept for perturbation tests.

## 4. Regression Tests

Command:

```bash
python3 -m unittest discover -s tests
```

What to inspect:

- `tests/test_gamma_v03.py`

What it means:

The tests check implementation invariants: the zero-transfer path reproduces the LCDM baseline, all gamma models return finite aligned arrays, viability flags are explicit booleans, and an invalid constant-transfer parameter choice is detected by the positive-density check.

## How To Read CSV Outputs

The most useful columns are:

- `a`, `z`: scale factor and redshift.
- `Gamma`: phase-transfer rate used by the model.
- `H_over_H_LCDM`: background expansion compared with the zero-transfer baseline.
- `rho_A_over_rhocrit0`, `rho_Bfoam_over_rhocrit0`: phase densities.
- `Omega_A`, `Omega_Bfoam`: fractional densities.
- `w_dark`, `w_Bfoam_eff`: effective equation-of-state diagnostics.
- `D`, `f`, `f_sigma8_proxy`: scale-independent growth proxy outputs.
- `delta_w_dark_vs_LCDM`, `delta_f_sigma8_vs_LCDM`: differences from the LCDM baseline.

Warning: `f_sigma8_proxy` is not a full matter-power calculation. It is a proxy under the current smooth-phase-B assumption.

## Current Stop Line

The project is blocked at perturbations.

Do not claim CMB viability, matter-power viability, or survey-likelihood viability until phase-A perturbations, phase-B behavior, and transfer perturbations are specified and implemented in CLASS/CAMB or an equivalent Boltzmann-code workflow.
