---
doc_id: audit_2026_06_12_bao_asset_digitization_closeout
title: "2026-06-12 BAO Asset Digitization Closeout"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_12_bao_primary_source_covariance_inventory
  - asset_desi_dr2_lya_bao_2025_data_release_parse
  - asset_eboss_dr16_lya_bao_2020_likelihood_release_parse
  - roadmap
next_gate: no likelihood experiment until source-product choices and covariance semantics are specified
last_updated: 2026-06-12
---

# 2026-06-12 BAO Asset Digitization Closeout

## Purpose

This closeout records the data-release digitization pass for the cached DESI DR2
and eBOSS DR16 Lyman-alpha BAO assets.

This is not an experiment result.

It does not implement a likelihood.

It does not run a BAO, DESI, Euclid, CMB, supernova, or matter-power comparison.

It does not claim QFUDS support.

It does not derive a foam-sector state variable, `Q^nu`, or `delta Q`.

It does not open Physical-QFUDS Level 2B.

It does not change roadmap status.

## Created Asset Products

| Asset product | Quality state | Role |
| --- | --- | --- |
| [DESI DR2 data-release parse](../../assets/desi_dr2_lya_bao_2025/digitization/desi_dr2_lya_bao_data_release.md) | `source_text_parse` | Markdown inspection record for the cached Zenodo archive and source pages |
| [DESI DR2 archive MarkItDown index](../../assets/desi_dr2_lya_bao_2025/digitization/desi_dr2_lya_bao_archive_markitdown_index.md) | `low_fidelity_search_text` | MarkItDown index for text-like members of `desi-dr2-lya-bao-figdata.tgz` |
| [DESI DR2 digitization index](../../assets/desi_dr2_lya_bao_2025/digitization/README.md) | `source_text_parse` | asset-local digitization manifest |
| [eBOSS DR16 likelihood-release parse](../../assets/eboss_dr16_lya_bao_2020/digitization/eboss_dr16_lya_bao_likelihood_release.md) | `source_text_parse` | Markdown inspection record for the cached SDSS likelihood grids, source pages, and raw-product listing |
| [eBOSS DR16 digitization index](../../assets/eboss_dr16_lya_bao_2020/digitization/README.md) | `source_text_parse` | asset-local digitization manifest |

## Modified Manifests

- [DESI DR2 asset manifest](../../assets/desi_dr2_lya_bao_2025/README.md)
- [eBOSS DR16 asset manifest](../../assets/eboss_dr16_lya_bao_2020/README.md)
- [Exp006 timing investigation index](README.md)

## Method

Both assets were classified as data-release assets, not paper-PDF assets.
PageIndex was not used because no paper body needed to be parsed in this pass.
MarkItDown 0.1.6 was installed and used to convert cached upstream README files
and source pages. The curated Markdown products were assembled from cached
source README, CSV, TXT, XML, and source-page conversion files.

## Recovered Quantities

The DESI DR2 parse records:

- upstream figure-data file map;
- MarkItDown conversions for text-like members of the extracted Zenodo archive;
- compact `D_M/r_d`, `D_H/r_d`, and `rho` source values from `dmdh_cmb.txt`;
- Figure 11 `ap`, `at` rows from `data_points_2D.csv`.

The eBOSS DR16 parse records:

- SDSS BAO-only likelihood grid semantics;
- grid ranges and max-likelihood grid points for `LYAUTO` and `LYXQSO`;
- listed raw Lyman-alpha data-vector/covariance FITS candidates.
- raw-product README semantics for Picca/Vega-format correlation, covariance,
  and distortion-matrix files;
- raw FITS file sizes and `asset_available_not_downloaded` state for large
  FITS products.

## Missing Fields

Still missing before any likelihood or diagnostic penalty can be planned:

- source-product choice for DESI DR2 (`stat`, `stat+sys`, `D_M/D_H`, or `ap/at`);
- source-product choice for eBOSS DR16 (paper central values, likelihood grids,
  Gaussian approximation, or raw FITS products);
- `r_d` treatment;
- formal covariance and parameter-count semantics;
- likelihood-vs-diagnostic boundary.

## Status Boundary

Candidate `X`: no.

`Q^nu`: no.

`delta Q`: no.

QFUDS support: no.

Roadmap status change: no.

Physical-QFUDS Level 2B change: no.

Level 6 remains blocked because the repository still has no likelihood pipeline.
