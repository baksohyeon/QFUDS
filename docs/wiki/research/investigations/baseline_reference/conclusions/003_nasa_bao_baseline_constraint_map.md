---
doc_id: audit_2026_06_17_nasa_bao_baseline_constraint_map
title: "2026-06-17 NASA + BAO Baseline Constraint Map"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - audit_2026_06_17_effective_foam_assumption_ledger_result
  - audit_2026_06_17_nasa_lambda_graphic_history_cache_closeout
  - asset_nasa_lambda_graphic_history
  - asset_desi_dr2_lya_bao_2025
  - asset_eboss_dr16_lya_bao_2020
  - roadmap
next_gate: define a foam-sector state variable and equation-side placement before using this map for model-facing interpretation
last_updated: 2026-06-17
---

# 2026-06-17 NASA + BAO Baseline Constraint Map

## Purpose

This document creates a status-neutral observational kill-map from the existing
NASA/LAMBDA and Lyman-alpha BAO caches.

It uses the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).

Workflow state:

- NASA/LAMBDA Graphic History: `asset_cached`;
- DESI DR2 Ly-alpha BAO: `asset_extracted_not_digitized` with
  `zenodo_data_available` and `direct_table` products;
- eBOSS DR16 Ly-alpha BAO: `asset_cached` with `direct_table` grid products.

This is not a likelihood implementation.

This is not a QFUDS result.

This does not claim QFUDS support.

This does not derive `xi`, transition width, amplitude, candidate `X`,
`Q^nu`, `delta Q`, or a foam-sector state variable.

This does not open Physical-QFUDS Level 2B.

## Source Boundary

| Source | Local role | State | What it contributes |
| --- | --- | --- | --- |
| [NASA LAMBDA Graphic History Assets](../../../assets/nasa_lambda_graphic_history/README.md) | Standard-cosmology parameter-axis reference | `asset_cached` | CMB, supernovae, galaxies/quasars, intensity mapping, power spectrum, and historical parameter axes. |
| [NASA LAMBDA data-reference matrix](../../../assets/nasa_lambda_graphic_history/digitization/data_reference_matrix.csv) | Source provenance matrix | `manual_structured_extract` | Literature/data source labels mapped to parameter-history plots. |
| [DESI DR2 Lyman-alpha BAO Assets](../../../assets/desi_dr2_lya_bao_2025/README.md) | High-redshift BAO geometry source product | `asset_extracted_not_digitized` | `D_M/r_d`, `D_H/r_d`, and covariance/correlation products near `z_eff = 2.33`. |
| [eBOSS DR16 Lyman-alpha BAO Assets](../../../assets/eboss_dr16_lya_bao_2020/README.md) | Previous high-redshift BAO geometry source product | `asset_cached` | Ly-alpha auto/cross BAO likelihood grids and public compressed geometry values near `z = 2.33`. |

The source web pages were re-opened on 2026-06-17 for scope verification:
NASA/LAMBDA Graphic History landing, parameters, and data-reference pages;
DESI DR2 arXiv and Zenodo pages; eBOSS DR16 arXiv and SDSS final BAO/RSD pages.

## Baseline Axes

NASA/LAMBDA is useful here because it names the standard cosmology axes that any
future physical QFUDS branch would need to respect. It is not a numerical
likelihood in this repository.

| Baseline axis | NASA/LAMBDA role | Future physical-QFUDS requirement | Retained timing can test? |
| --- | --- | --- | --- |
| CMB acoustic structure and power spectrum | Core observation and power-spectrum reference axis | Compute perturbations and CMB observables without destroying acoustic structure. | No. Retained timing is not a Boltzmann calculation. |
| Scalar index `n_s` | Historical parameter axis | Avoid using foam language to absorb primordial-spectrum constraints without an inflation/initial-condition prescription. | No. |
| Universe age `t0` | Historical parameter axis | Produce a background expansion history compatible with age constraints. | Only weakly, through background-timing shape if an `H(z)` model exists. |
| Optical depth `tau` | Historical parameter axis | Preserve reionization/CMB consistency if perturbations are implemented. | No. |
| Matter density `Omega_m` | Historical parameter axis | Match matter content and distance/growth constraints without post-hoc tuning. | No, except as a comparison target after an independent model exists. |
| Baryon density `Omega_b h^2` | Historical parameter axis | Preserve BBN/CMB baryon-density consistency. | No. |
| CDM density `Omega_c h^2` | Historical parameter axis | Explain or reproduce clustering matter without relabeling LCDM. | No. |
| Matter clustering `sigma8` | Historical parameter axis | Compute growth and matter-power observables. | No. |
| Hubble constant `H0` | Historical parameter axis | Fit low- and high-redshift distance ladder/CMB-inferred constraints without hiding tension in a fitted transition. | Only as a phenomenological background comparator, not as evidence. |
| Supernova distance ladder | Observation class | Match luminosity-distance data if a background model is proposed. | Not directly. |

## High-Redshift BAO Geometry Thresholds

The retained timing peak near `z ~= 2` makes high-redshift Ly-alpha BAO a useful
kill-map axis. It does not make Ly-alpha BAO evidence for QFUDS.

| Source product | Redshift | `D_M/r_d` | `D_H/r_d` | Correlation / note | Role |
| --- | ---: | ---: | ---: | --- | --- |
| DESI DR2 Ly-alpha BAO `stat+sys` compact product | `z_eff = 2.33` | `38.9886 +- 0.5312` | `8.6316 +- 0.1011` | `rho = -0.43` | Primary current high-z geometry threshold in local cache. |
| DESI DR2 Ly-alpha BAO `stat` compact product | `z_eff = 2.33` | `38.9886 +- 0.5190` | `8.6315 +- 0.0978` | `rho = -0.46` | Statistical-only comparison, not the conservative threshold. |
| eBOSS DR16 Ly-alpha combined paper value | `z = 2.33` | `37.5 +- 1.1` | `8.99 +- 0.19` | statistical errors | Historical comparison against DESI DR2. |
| eBOSS DR16 SDSS public table, Ly-alpha auto | `z = 2.33` | `37.6 +- 1.9` | `8.93 +- 0.28` | public compressed value | Cross-check axis. |
| eBOSS DR16 SDSS public table, Ly-alpha x QSO | `z = 2.33` | `37.3 +- 1.7` | `9.08 +- 0.34` | public compressed value | Cross-check axis. |

No QFUDS model in the repository currently computes these quantities.

## Kill-Map

| Threshold | A future physical branch must provide | Immediate kill condition |
| --- | --- | --- |
| `H(z)` and `D_H(z)=c/H(z)` | Background expansion equation and units sufficient to compute `D_H/r_d`. | Cannot compute `H(z)` near `z ~= 2.33`. |
| `D_M(z)` | Comoving transverse distance integral tied to the same `H(z)`. | Produces a distance curve that cannot be compared to BAO geometry. |
| `r_d` | Sound horizon prescription or explicit decision to import a baseline value. | Uses BAO ratios without defining or importing `r_d`. |
| DESI/eBOSS Ly-alpha geometry | Comparison to `D_M/r_d`, `D_H/r_d`, and covariance/correlation semantics. | Tunes transition redshift, width, amplitude, or `xi` after seeing the BAO target. |
| NASA/LAMBDA parameter axes | Clear statement of which axes are in scope and which are not. | Treats educational/reference plots as likelihood evidence. |
| Perturbation stability | Perturbation prescription, sound speed, and conservation route. | Claims CMB, matter-power, or clustering viability from background-only timing. |
| Known-model distinction | Comparison against LCDM+EFTofLSS, backreaction, running vacuum/HDE, screened modified gravity, IV/IDE, and effective `w(a)`. | Reproduces a known model with renamed foam language and no new observable. |

## Retained Timing Boundary

Retained timing near `z ~= 2` can only do this:

```text
compare a phenomenological timing fingerprint against the redshift region where
high-z Ly-alpha BAO geometry is measured
```

It cannot do this:

```text
derive a foam source
define xi ~= 10 Mpc
compute D_M/r_d or D_H/r_d
fit DESI/eBOSS
claim QFUDS support
open Level 2B
```

The retained `Gamma(a)` branch remains a phenomenological IV/IDE comparator.

## Circularity Stop Rules

Stop if any route does the following:

1. looks at NASA/LAMBDA, DESI, eBOSS, BAO, LSS, or retained timing targets;
2. chooses `xi`, transition width, transition redshift, or amplitude afterward;
3. calls those chosen values the foam source.

That is a post-hoc fit.

Allowed use is narrower:

```text
freeze state variable and equation-side placement first
-> compute H(z), D_M/r_d, D_H/r_d, perturbations, or other observables
-> compare to this baseline map as a possible kill test
```

## Decision

The NASA + BAO baseline map is usable as an observational kill-map only.

It is not yet usable for model-facing interpretation because the repository has
not defined:

- a foam-sector state variable;
- whether the modification is geometry-side or stress-energy-side;
- a replacement for retained `Gamma(a)`;
- a non-circular `xi` definition;
- a BAO/CMB/SNe/matter-power likelihood pipeline.

## Status Boundary Closeout

Candidate `X`: no.

`Q^nu`: no.

`delta Q`: no.

`xi ~= 10 Mpc` derived: no.

QFUDS support: no.

Roadmap status change: no.

Physical-QFUDS Level 2B change: no.
