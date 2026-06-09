---
doc_id: verification_guide
title: QFUDS Verification Guide
doc_type: guide
stage: "1.5"
status: in_progress
evidence_role: ssot
depends_on:
  - exp_000_lcdm_baseline
  - exp_001_gamma_scan
  - exp_002_entropy_information_gate
next_gate: retained branch demoted; keep Level 2B blocked
last_updated: 2026-06-09
---

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
- [docs/03_experiments/000_exp_000_lcdm_baseline.md](../03_experiments/000_exp_000_lcdm_baseline.md)
- [docs/04_results/000_result_000_lcdm_baseline.md](../04_results/000_result_000_lcdm_baseline.md)

What it means:

This confirms the null limit. With no phase transfer, the two-phase background behaves as LCDM. This is a control case, not evidence of novelty.

## 2. Experiment 001: Gamma-Law Background Scan

Command:

```bash
python3 scripts/run_minimal_model.py --exp-001-gamma-scan
```

What to inspect:

- [docs/03_experiments/010_exp_001_gamma_scan.md](../03_experiments/010_exp_001_gamma_scan.md)
- [docs/04_results/010_result_001_gamma_scan.md](../04_results/010_result_001_gamma_scan.md)
- `outputs/qfuds_constant_gamma0.01_beta0.csv`
- `outputs/qfuds_growth_driven_gamma0.01_beta0.csv`
- `outputs/qfuds_collapsed_fraction_toy_gamma0.03_beta0.csv`
- `outputs/qfuds_black_hole_entropy_proxy_gamma0.03_beta0.csv`
- `outputs/qfuds_star_formation_proxy_gamma0.003_beta0.csv`
- PNG diagnostics in `outputs/` with the same file stems.

What it means:

This scan asks whether candidate `Gamma(a)` laws already fail at the background level. Constant transfer and ungated growth-driven transfer fail at the tested amplitudes. Low-redshift proxies survive only as candidates for stronger tests.

## 3. Experiment 002: Entropy / Information-Source Gate

Command:

```bash
python3 scripts/run_minimal_model.py --exp-002-entropy-gate
```

What to inspect:

- [docs/03_experiments/020_exp_002_entropy_information_gate.md](../03_experiments/020_exp_002_entropy_information_gate.md)
- [docs/04_results/020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md)
- `outputs/qfuds_gravitational_entropy_gamma0.003_beta0.csv`
- `outputs/qfuds_information_production_gamma0.02_beta0.csv`
- `outputs/qfuds_horizon_information_gamma0.03_beta0.csv`
- PNG diagnostics in `outputs/` with the same file stems.

What it means:

This scan asks whether the transfer law can be tied to a concrete entropy or information source. Broad entropy language mostly fails or reduces to known models. Press-Schechter-style information production was the narrow branch kept for the Level 1.5 physicality audit, and that retained branch is now demoted to phenomenological interacting-vacuum status.

Where the branch decision is recorded:

- [docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md](../02_theory/015_qfuds_v0_15_phase_transfer_physics.md)
- [docs/05_next_steps/010_perturbation_gate.md](../05_next_steps/010_perturbation_gate.md)

What it is not:

This is not the perturbation-theory task. It does not evolve `delta_A`, `theta_A`, `delta_B`, or `theta_B`, and it is not a CLASS/CAMB result.

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

## 4. Experiment 003: Level 2A Perturbation Closure

Command:

```bash
python3 scripts/run_minimal_model.py --exp-003-perturbation-closure
```

What to inspect:

- [docs/04_results/000_experiment_summary.md](../04_results/000_experiment_summary.md)
- [docs/02_theory/030_qfuds_phenomenological_perturbations.md](../02_theory/030_qfuds_phenomenological_perturbations.md)
- [docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md](../03_experiments/030_exp_003_phenomenological_perturbation_closure.md)
- [docs/04_results/030_result_003_phenomenological_perturbation_closure.md](../04_results/030_result_003_phenomenological_perturbation_closure.md)
- [docs/05_next_steps/010_perturbation_gate.md](../05_next_steps/010_perturbation_gate.md)
- `outputs/exp003_stability_diagnostics.csv`
- `outputs/exp003_phenomenological_perturbation_summary.json`

What it means:

This is a completed Level 2A phenomenological perturbation-closure audit. P2
fails at the retained amplitude. P1 is stable only as ordinary
phenomenological interacting vacuum. This is not a physical derivation of
`Gamma(a)`.

## 5. Regression Tests

Command:

```bash
python3 -m unittest discover -s tests -p 'test_*.py'
```

What to inspect:

- `tests/test_gamma_v03.py`
- `tests/test_exp003_perturbations.py`

What it means:

The tests check implementation invariants: the zero-transfer path reproduces
the LCDM baseline, all gamma models return finite aligned arrays, viability
flags are explicit booleans, and an invalid constant-transfer parameter choice
is detected by the positive-density check. They also cover the corrected
phenomenological perturbation closure used by `exp_003`.

## 6. Documentation Validation

Command:

```bash
python3 scripts/validate_docs.py
```

What it means:

This validates frontmatter, H1/title alignment, active-stage filename prefixes,
required experiment/result document pairs, required experiment/result sections,
and the roadmap/decision-log stop line. It does not validate physics. It checks
that the documentation control surface is internally coherent.

## 7. Documentation Integrity

Commands:

```bash
python3 scripts/research_consistency.py
python3 scripts/preflight_exp004.py
```

What they mean:

`research_consistency.py` checks cross-document authority: roadmap evidence
paths, decision-log coverage, experiment/result pairing, and whether human-facing
documents defer current status to the roadmap.

`preflight_exp004.py` checks the specific exp_003 to exp_004 transition record:
exp_003 documents, referenced outputs, decision-log verdict, postmortem
reference, and premature CLASS/CMB/matter-power claims.

## Current Stop Line

Physical QFUDS perturbation theory is blocked because the retained Level 1.5
collapse/information-production branch failed physical promotion.
Level 2A is complete for the baseline closure. It does not establish CMB,
matter-power, survey-likelihood, or physical QFUDS viability.

Do not claim that the retained `Gamma(a)` branch is derived physics. It has
been demoted to phenomenological interacting vacuum. Do not claim CMB viability,
matter-power viability, or survey-likelihood viability until phase-A
perturbations, phase-B behavior, and transfer perturbations are specified and
implemented in CLASS/CAMB or an equivalent Boltzmann-code workflow.
