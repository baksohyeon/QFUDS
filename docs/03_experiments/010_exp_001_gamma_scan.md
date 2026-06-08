---
doc_id: exp_001_gamma_scan
title: "Experiment 001: Gamma-Law Background Scan"
doc_type: experiment
stage: "1"
status: completed
evidence_role: proxy_scan
depends_on:
  - exp_000_lcdm_baseline
next_gate: Level 1.5 phase transfer physicality
last_updated: 2026-06-08
---

# Experiment 001: Gamma-Law Background Scan

Date: 2026-06-08

### Objective

Test whether physically labeled `Gamma(a)` transfer laws can pass minimal background-level viability checks.

### Hypothesis

Transfer laws that are active during the early universe will fail by producing negative `rho_B`, excessive early dark-energy fraction, or non-LCDM-like CMB-era expansion. Transfer laws gated to low redshift may survive background checks and become candidates for perturbation-level testing.

### Method

Run experiment 001:

```bash
python3 scripts/run_minimal_model.py --exp-001-gamma-scan
```

The runner integrates the two-phase background, computes a scale-independent growth proxy, compares each model against the zero-transfer LCDM baseline, writes CSV files, and writes PNG diagnostic plots when `matplotlib` is available.

### Parameters

Experiment 001 suite:

| Law | Parameters |
| --- | --- |
| constant | `gamma0=0.01`, `beta=0` |
| power law | `gamma0=0.03`, `beta=5` |
| growth driven | `gamma0=0.01`, `beta=0` |
| collapsed fraction toy | `gamma0=0.03`, `collapse_a=0.35`, `collapse_nu=5` |
| horizon entropy | `gamma0=0.03`, `beta=4` |
| black-hole entropy proxy | `gamma0=0.03`, `collapse_a=0.35`, `collapse_nu=6` |
| star-formation proxy | `gamma0=0.003`, `beta=0` |

### Outputs

- `outputs/qfuds_constant_gamma0.01_beta0.csv`
- `outputs/qfuds_constant_gamma0.01_beta0.png`
- `outputs/qfuds_gamma0.03_beta5.csv`
- `outputs/qfuds_gamma0.03_beta5.png`
- `outputs/qfuds_growth_driven_gamma0.01_beta0.csv`
- `outputs/qfuds_growth_driven_gamma0.01_beta0.png`
- `outputs/qfuds_collapsed_fraction_toy_gamma0.03_beta0.csv`
- `outputs/qfuds_collapsed_fraction_toy_gamma0.03_beta0.png`
- `outputs/qfuds_horizon_entropy_gamma0.03_beta4.csv`
- `outputs/qfuds_horizon_entropy_gamma0.03_beta4.png`
- `outputs/qfuds_black_hole_entropy_proxy_gamma0.03_beta0.csv`
- `outputs/qfuds_black_hole_entropy_proxy_gamma0.03_beta0.png`
- `outputs/qfuds_star_formation_proxy_gamma0.003_beta0.csv`
- `outputs/qfuds_star_formation_proxy_gamma0.003_beta0.png`

### Result

The scan found:

| Law | Result |
| --- | --- |
| constant | fails by negative `rho_B` and CMB-era `H(a)` deviation |
| power law | passes minimal checks but remains standard interacting dark energy |
| growth driven | fails by negative `rho_B` and CMB-era `H(a)` deviation |
| collapsed fraction toy | passes minimal checks and is worth testing next |
| horizon entropy | passes minimal checks but is still standard interacting dark energy unless derived |
| black-hole entropy proxy | passes minimal checks and is worth testing next |
| star-formation proxy | passes minimal checks and is worth testing next |

### Decision

Reject constant and ungated growth-driven transfer at the tested amplitudes.
Preserve low-redshift collapse, black-hole-entropy, and star-formation proxies
only as candidate shapes for later scrutiny. QFUDS v0.15 / Level 1.5 must
resolve phase-transfer physicality before perturbation work.

### Next Step

Do not proceed directly to perturbations from this scan. Complete the
phase-transfer physicality gate first, then specify transfer perturbations only
for branches that survive that gate. Do not claim CMB viability from this
experiment alone.
