# exp_002_entropy_information_scan_v04

Date: 2026-06-08

## Objective

Test whether entropy-derived or information-production transfer laws produce a narrower and more falsifiable `Gamma(a)` source than the v0.3 physically labeled toy laws.

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

This is a background-level scan with a scale-independent growth proxy.

It does not establish perturbation stability, CMB viability, matter-power viability, survey-likelihood viability, or QFUDS novelty.

## Method

Run the default v0.4 suite:

```bash
python3 scripts/run_minimal_model.py --all-v04
```

The runner integrates the two-phase background, computes the smooth-phase-B growth proxy, compares each model against the zero-transfer LCDM baseline, writes CSV files, and writes PNG diagnostic plots when `matplotlib` is available.

## Parameters

Default v0.4 suite:

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

The result is documented in `docs/04_results/qfuds_v0_4_entropy_laws.md`.

Summary:

- HBM/KL gravitational entropy fails positivity at the tested amplitude.
- Horizon information is mathematically clean but reduces to standard horizon/interacting dark-energy phenomenology.
- Total black-hole entropy remains incomplete without an actual cosmic black-hole mass/accretion history.
- Collapse/information production is the only v0.4 branch worth carrying forward.

## Decision

Continue only the collapse/information-production branch as a narrow interacting-vacuum candidate with a fixed source shape. Terminate the broader claim that entropy production by itself explains dark energy.

## Next Step

Write perturbation equations for phase A, phase B, and transfer perturbations. Then test whether the information-production branch survives beyond the background/growth-proxy level.
