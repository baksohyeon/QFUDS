---
doc_id: audit_2026_06_12_bao_primary_source_covariance_inventory
title: "2026-06-12 BAO Primary-Source and Covariance Inventory"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - exp006_timing_investigation_index
  - asset_desi_dr2_lya_bao_2025
  - asset_eboss_dr16_lya_bao_2020
  - roadmap
next_gate: no likelihood experiment until source-product choices and covariance semantics are specified
last_updated: 2026-06-12
---

# 2026-06-12 BAO Primary-Source and Covariance Inventory

## Purpose

This inventory records source-product availability for a possible future
status-neutral BAO geometry audit of structure-era timing features.

It is not an experiment plan.

It does not implement a likelihood.

It does not run a BAO, DESI, Euclid, CMB, supernova, or matter-power comparison.

It does not claim QFUDS support.

It does not derive a foam-sector state variable, `Q^nu`, or `delta Q`.

It does not open Physical-QFUDS Level 2B.

It does not change roadmap status.

## Roadmap Boundary

The roadmap remains in observer mode. Level 6 remains blocked because the
repository has no likelihood pipeline. This inventory only reduces ambiguity
around external BAO source products that a future status-neutral audit would
need to choose between.

## Cached Assets

| Asset | Local manifest | Asset state |
| --- | --- | --- |
| DESI DR2 Lyman-alpha BAO 2025 | [DESI DR2 Ly-alpha BAO Assets](../../assets/desi_dr2_lya_bao_2025/README.md) | `asset_extracted_not_digitized` |
| eBOSS DR16 Lyman-alpha BAO 2020 | [eBOSS DR16 Ly-alpha BAO Assets](../../assets/eboss_dr16_lya_bao_2020/README.md) | `asset_cached` |

## DESI DR2 Lyman-alpha BAO

| Field | Value |
| --- | --- |
| Primary paper | DESI Collaboration 2025, arXiv:2503.14739 |
| Supplementary record | <https://zenodo.org/records/15690869> |
| Downloaded archive | `desi-dr2-lya-bao-figdata.tgz` |
| Local archive path | `docs/wiki/research/assets/desi_dr2_lya_bao_2025/source/desi-dr2-lya-bao-figdata.tgz` |
| Extracted upstream README | `docs/wiki/research/assets/desi_dr2_lya_bao_2025/source/extracted/README` |
| Compact distance summary | `docs/wiki/research/assets/desi_dr2_lya_bao_2025/source/extracted/dmdh_cmb.txt` |
| Figure 11 covariance product | `docs/wiki/research/assets/desi_dr2_lya_bao_2025/source/extracted/data_points_cov_ap_at.dat` |
| Effective redshift | `z_eff = 2.33` |

The upstream `dmdh_cmb.txt` product contains:

| Variant | `D_M/r_d` | `D_H/r_d` | `rho` |
| --- | ---: | ---: | ---: |
| DESI DR2 stat | `38.9886 +- 0.5190` | `8.6315 +- 0.0978` | `-0.46` |
| DESI DR2 stat+sys | `38.9886 +- 0.5312` | `8.6316 +- 0.1011` | `-0.43` |

These are cached source-product values. They are not a QFUDS result.

## eBOSS DR16 Lyman-alpha BAO

| Field | Value |
| --- | --- |
| Primary paper | du Mas des Bourboux et al. 2020, arXiv:2007.08995 |
| SDSS final results page | <https://www.sdss4.org/science/final-bao-and-rsd-measurements/> |
| BAO-only likelihood directory | <https://svn.sdss.org/public/data/eboss/DR16cosmo/tags/v1_0_1/likelihoods/BAO-only/> |
| Lyman-alpha data-vector/covariance directory | <https://svn.sdss.org/public/data/eboss/DR16cosmo/tags/v1_0_1/dataveccov/lya_forest/> |
| Local README path | `docs/wiki/research/assets/eboss_dr16_lya_bao_2020/source/BAO-only_README.txt` |
| Local auto-correlation grid | `docs/wiki/research/assets/eboss_dr16_lya_bao_2020/source/sdss_DR16_LYAUTO_BAO_DMDHgrid.txt` |
| Local cross-correlation grid | `docs/wiki/research/assets/eboss_dr16_lya_bao_2020/source/sdss_DR16_LYxQSO_BAO_DMDHgrid.txt` |
| Local raw-asset listing | `docs/wiki/research/assets/eboss_dr16_lya_bao_2020/source/dataveccov_lya_forest_listing.xml` |
| Effective redshift | `z = 2.334` in likelihood grids; paper abstract reports `z = 2.33` |

The SDSS BAO-only README states that the DR16 Lyman-alpha BAO likelihoods are
provided separately for auto-correlation and cross-correlation and can be
treated as independent. The grid columns are:

```text
Column 1: D_M(z=2.334)/r_d
Column 2: D_H(z=2.334)/r_d
Column 3: likelihood ratio
```

This differs from the earlier candidate summary that treated eBOSS DR16 as an
already recovered 2x2 Gaussian covariance block. The cached primary product is
a pair of likelihood grids, not a direct covariance matrix.

## Source-Product Decisions Still Open

A future audit or experiment plan must decide:

- whether DESI DR2 should use the `stat` or `stat+sys` compact summary;
- whether DESI DR2 should use `D_M/r_d`, `D_H/r_d`, `ap`, `at`, or another
  upstream representation;
- whether eBOSS DR16 should use the paper abstract central values, the SDSS
  auto/cross likelihood grids, or an explicitly defined Gaussian approximation;
- whether `r_d` is fixed, ratio-eliminated, or marginalized;
- whether any comparison is a diagnostic penalty or a formal likelihood.

No such choice is made here.

## Status Boundary

This inventory does not unblock Level 6. It records that relevant external BAO
source products exist and are now cached enough for a later status-neutral audit
to make explicit source-product choices.

Roadmap status remains unchanged.

Physical-QFUDS Level 2B remains blocked.
