---
doc_id: asset_desi_dr2_lya_bao_2025_data_release_parse
title: "DESI DR2 Lyman-alpha BAO Data-Release Parse"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_desi_dr2_lya_bao_2025
next_gate: manual structured extraction before BAO penalty or likelihood use
last_updated: 2026-06-12
---

# DESI DR2 Lyman-alpha BAO Data-Release Parse

## Scope

This document converts the cached DESI DR2 Lyman-alpha BAO Zenodo figure-data
archive into a Markdown inspection record.

Quality state:

```text
source_text_parse
```

This is not `manual_structured_extract`, not `numeric_digitized`, and not a BAO
likelihood implementation.

## Source Asset

| Field | Value |
| --- | --- |
| Paper | DESI Collaboration 2025, arXiv:2503.14739 |
| Zenodo record | <https://zenodo.org/records/15690869> |
| Cached archive | `../source/desi-dr2-lya-bao-figdata.tgz` |
| Extracted README | `../source/extracted/README` |
| Source-page conversions | [Zenodo record](markitdown_zenodo_record_15690869.md), [arXiv page](markitdown_arxiv_2503.14739.md) |
| Archive-member conversions | [DESI DR2 archive MarkItDown index](desi_dr2_lya_bao_archive_markitdown_index.md) |
| Parse method | source-page conversion, archive-member conversion, source-file inspection, MarkItDown README conversion, and Markdown assembly |
| PageIndex used | no; no paper PDF body was parsed |
| MarkItDown used | yes, for [MarkItDown upstream README conversion](markitdown_upstream_README.md) |

## Upstream Figure-Data Map

The upstream README maps the archive contents to figures:

| Figure | Upstream files | Meaning recorded by upstream README |
| --- | --- | --- |
| 1 | `radec.fits`, `desi_north.npz`, `desi_south.npz`, `SDSS_DR16_north.npy`, `SDSS_DR16_south.npy`, `Y1_numtile.csv`, `Y3_numtile.csv` | footprint and quasar-observation count products |
| 2 | `loa-spectrum-84-z3.20-39627696665266273-main-dark.csv` | flux versus wavelength |
| 3 | `lyalyaxlyalya_data.csv`, `lyalyaxlyalya_model.csv`, `lyalyaxlyalyb_data.csv`, `lyalyaxlyalyb_model.csv` | wedge data and model products |
| 4 | `lyalyaxqso_data.csv`, `lyalyaxqso_model.csv`, `lyalybxqso_data.csv`, `lyalybxqso_model.csv` | wedge data and model products |
| 5 | `alphas.txt` | data points and errors |
| 6 | `residuals_2d.fits` | residual plot images |
| 7 | `bootstrap.fits` | 20 realizations shown in the figure |
| 8 | `mock_wedges.json` | dictionary of figure points and lines |
| 9 | `mock_pairs.txt` | data points and errors |
| 10 | `data_splits.txt` | data points and errors |
| 11 | `data_points_2D.csv`, `data_points_cov_ap_at.dat` | data points, errors, and covariance of `ap`, `at` |
| 12 | `dmdh_cmb.txt` | `D_M/r_d`, `D_H/r_d`, and correlation summaries |
| 13 | `variations.txt` | data points and errors |

## Compact Distance Summary

The cached `dmdh_cmb.txt` file contains:

| Variant | `D_M/r_d` | `D_H/r_d` | `rho` |
| --- | ---: | ---: | ---: |
| DESI DR1 Lyalpha BAO | `39.6964 +- 0.9105` | `8.5160 +- 0.1692` | `-0.46` |
| DESI DR2 stat | `38.9886 +- 0.5190` | `8.6315 +- 0.0978` | `-0.46` |
| DESI DR2 stat+sys | `38.9886 +- 0.5312` | `8.6316 +- 0.1011` | `-0.43` |
| CMB LambdaCDM | `39.0913 +- 0.1915` | `8.5939 +- 0.0774` | `1.00` |
| CMB + DESY5 `w_0 w_a`CDM | `39.0311 +- 0.5226` | `8.7257 +- 0.1805` | `0.95` |

These are source-product values copied into an inspection record. They are not a
QFUDS result and have not been propagated into a model comparison.

## Figure 11 `ap`, `at` Products

The cached `data_points_2D.csv` file contains seven rows:

| Name | Label | `ap` | `aperr` | `at` | `aterr` |
| --- | --- | ---: | ---: | ---: | ---: |
| DR1 | DESI DR1 configuration | `1.0039911881830086` | `0.011969594028499342` | `0.9916823225055956` | `0.013882736116989314` |
| BB | with BB | `0.9988055706205233` | `0.01034973693613811` | `1.0008979956366817` | `0.012857361683982771` |
| CP1 | No pairs theta < 20 arcmin, v < 4000 km/s | `0.9996099708908346` | `0.011732285688295985` | `0.9954359569981316` | `0.01340823311985273` |
| CP2 | No pairs theta < 10 arcmin, v < 2000 km/s | `1.0006508051570704` | `0.011480855744890273` | `0.9950258823550808` | `0.013264891905696408` |
| CP3 | No pairs theta < 5 arcmin, v < 1000 km/s | `1.0016303048796702` | `0.011436336037167427` | `0.994946279183328` | `0.013250419485229092` |
| NL | Free NL BAO | `1.0010583727345717` | `0.01118179176500117` | `0.9969678575142843` | `0.012397147449977663` |
| DR2 | DESI DR2 | `1.0016697419984024` | `0.011340488874880206` | `0.9949178539114953` | `0.01322692672758069` |

The companion `data_points_cov_ap_at.dat` file contains the covariance entry
used by the upstream Figure 11 product. A future audit must decide whether to
work in `ap`, `at` space or in `D_M/r_d`, `D_H/r_d` space.

## Open Product Choices

Before any BAO penalty or likelihood comparison, a future plan must decide:

- whether to use `stat` or `stat+sys` DESI DR2 values;
- whether to use the compact `D_M/r_d`, `D_H/r_d` summary or the `ap`, `at`
  product;
- whether to keep `r_d` fixed, ratio-eliminate it, or marginalize it;
- whether the comparison is diagnostic only or a formal likelihood.

No such decision is made here.

## Additional Source-Page Retrieval

The Zenodo and arXiv source pages were converted with MarkItDown after the
initial asset cache pass. The Zenodo source page confirms the release-level
record and points to the cached archive. The arXiv source page is retained only
as a paper metadata aid; paper-body parsing should use PageIndex if equation,
caption, or table provenance becomes necessary.

## Archive-Member Conversion

The cached `desi-dr2-lya-bao-figdata.tgz` archive was already unpacked under
`../source/extracted/`. The text, CSV, DAT, and JSON members were converted with
MarkItDown under `markitdown_extracted/` and indexed in
[DESI DR2 archive MarkItDown index](desi_dr2_lya_bao_archive_markitdown_index.md).
Binary FITS, NPY, and NPZ members were not converted.
