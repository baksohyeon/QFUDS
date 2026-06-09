---
doc_id: exp_002_entropy_information_gate
title: "Experiment 002: Entropy / Information-Source Gate"
doc_type: experiment
stage: "1"
status: provenance
evidence_role: provenance
depends_on:
  - exp_001_gamma_scan
next_gate: Level 1.5 phase transfer physicality
last_updated: 2026-06-08
---

# Experiment 002: Entropy / Information-Source Gate

Date: 2026-06-08

## Objective

Test whether entropy-derived or information-production transfer laws produce a narrower and more falsifiable `Gamma(a)` source than the experiment 001 physically labeled toy laws.

## Hypothesis

Broad entropy language will fail unless it supplies a concrete source history `X(a)` and a reproducible transfer law:

```math
\Gamma(a)=\gamma_0 {dX/d\ln a\over \max(dX/d\ln a)}.
```

The expected split is:

- horizon information should reduce to standard horizon/interacting dark-energy phenomenology;
- linear HBM/KL gravitational entropy should be too broad in time and may fail positivity;
- total black-hole entropy should remain incomplete without a mass/accretion history;
- Press-Schechter collapse or information production may survive as the narrowest candidate because it turns on after nonlinear structure formation begins.

## Scope

This is a background-level proxy scan with a scale-independent growth proxy.

It does not establish perturbation stability, CMB viability, matter-power viability, survey-likelihood viability, or QFUDS novelty.

It is not the Level 2 perturbation experiment. It does not evolve `delta_A`, `theta_A`, `delta_B`, or `theta_B`.

Post-audit status:

```text
Experiment 002 is retained as provenance, not as physical evidence.
Its surviving shape is not meaningful data for QFUDS physicality because the
phase-transfer mechanism, physical mass threshold, and self-consistent QFUDS
growth source were not defined before the scan.
```

## Method

Run experiment 002:

```bash
python3 scripts/run_minimal_model.py --exp-002-entropy-gate
```

The runner integrates the two-phase background, computes the smooth-phase-B growth proxy, compares each model against the zero-transfer LCDM baseline, writes CSV files, and writes PNG diagnostic plots when `matplotlib` is available.

## Parameters

Experiment 002 suite:

| Law | Parameters |
| --- | --- |
| collapsed fraction toy | `gamma0=0.03`, `collapse_a=0.35`, `collapse_nu=5` |
| black-hole entropy proxy | `gamma0=0.03`, `collapse_a=0.35`, `collapse_nu=6` |
| star-formation proxy | `gamma0=0.003`, `beta=0` |
| gravitational entropy | `gamma0=0.003`, `beta=0` |
| information production | `gamma0=0.02`, `collapse_a=0.35`, `collapse_nu=5` |
| horizon information | `gamma0=0.03`, `beta=0` |

## Failure Criteria

A law fails this background scan if it:

- produces negative `rho_A` or `rho_B`;
- exceeds the early phase-B safety threshold used by `qfuds/diagnostics.py`;
- moves CMB-era `H(a)` outside the minimal background tolerance;
- erases the scale-independent growth proxy in the pre-dark-energy era;
- reduces to a known model class without adding a fixed physical source or new falsifiable relation.

## Outputs

- `outputs/qfuds_collapsed_fraction_toy_gamma0.03_beta0.csv`
- `outputs/qfuds_collapsed_fraction_toy_gamma0.03_beta0.png`
- `outputs/qfuds_black_hole_entropy_proxy_gamma0.03_beta0.csv`
- `outputs/qfuds_black_hole_entropy_proxy_gamma0.03_beta0.png`
- `outputs/qfuds_star_formation_proxy_gamma0.003_beta0.csv`
- `outputs/qfuds_star_formation_proxy_gamma0.003_beta0.png`
- `outputs/qfuds_gravitational_entropy_gamma0.003_beta0.csv`
- `outputs/qfuds_gravitational_entropy_gamma0.003_beta0.png`
- `outputs/qfuds_information_production_gamma0.02_beta0.csv`
- `outputs/qfuds_information_production_gamma0.02_beta0.png`
- `outputs/qfuds_horizon_information_gamma0.03_beta0.csv`
- `outputs/qfuds_horizon_information_gamma0.03_beta0.png`

## Result

The result is documented in [docs/04_results/020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md).

Summary:

- HBM/KL gravitational entropy fails positivity at the tested amplitude.
- Horizon information is mathematically clean but reduces to standard horizon/interacting dark-energy phenomenology.
- Total black-hole entropy remains incomplete without an actual cosmic black-hole mass/accretion history.
- Collapse/information production is the only narrow shape retained for Level
  1.5 scrutiny, but experiment 002 itself is not physical evidence for that
  branch.

## Decision

Demote experiment 002 to a provenance scan. Continue only the
collapse/information-production shape as a question for Level 1.5, not as a
validated transfer law.

## Next Step

Complete the Level 1.5 phase-transfer physicality gate before any perturbation
experiment is created.
