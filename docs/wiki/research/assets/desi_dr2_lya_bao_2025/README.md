---
doc_id: asset_desi_dr2_lya_bao_2025
title: "DESI DR2 Lyman-alpha BAO 2025 Assets"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - exp006_timing_investigation_index
next_gate: manual structured extraction only if a status-neutral BAO geometry audit needs it
last_updated: 2026-06-12
---

# DESI DR2 Lyman-alpha BAO 2025 Assets

Local access copies for DESI DR2 Results I: Baryon Acoustic Oscillations from
the Lyman Alpha Forest, arXiv:2503.14739.

These files are research assets only. They do not create a new experiment,
change Exp006 conclusions, open a likelihood pipeline, or change roadmap status.

## Source

- Paper: <https://arxiv.org/abs/2503.14739>
- Supplementary record: <https://zenodo.org/records/15690869>
- Downloaded archive endpoint:
  <https://zenodo.org/api/records/15690869/files/desi-dr2-lya-bao-figdata.tgz/content>

## Files

- `source/desi-dr2-lya-bao-figdata.tgz` - original Zenodo archive.
- `source/extracted/README` - upstream file manifest for figure-data products.
- `source/extracted/data_points_2D.csv` - Figure 11 data points and errors in
  `ap` and `at`.
- `source/extracted/data_points_cov_ap_at.dat` - covariance entry for the
  `ap`, `at` Figure 11 product.
- `source/extracted/dmdh_cmb.txt` - compact `D_M/r_d`, `D_H/r_d`, and `rho`
  summary used for Figure 12.
- `source/extracted/` - full extracted Zenodo archive contents.
- `figures/` - reserved for rendered or copied figure assets.
- `digitization/` - reserved for manual structured extracts or derived numeric
  products.

## Current Asset State

- Asset state: `asset_extracted_not_digitized`.
- Extraction potential: `zenodo_data_available`, `direct_table`.
- Markdown conversion quality: not applicable.

The archive has been downloaded and unpacked. No QFUDS-specific likelihood,
pipeline, fit, or derived statistic has been produced.

## Recovered Quantities

The upstream `dmdh_cmb.txt` file contains the compact DESI DR2 Ly-alpha BAO
summary at `z_eff = 2.33`:

| Variant | `D_M/r_d` | `D_H/r_d` | `rho` |
| --- | ---: | ---: | ---: |
| DESI DR2 stat | `38.9886 +- 0.5190` | `8.6315 +- 0.0978` | `-0.46` |
| DESI DR2 stat+sys | `38.9886 +- 0.5312` | `8.6316 +- 0.1011` | `-0.43` |

These values remain source-product inventory, not a QFUDS result.

## Known Limits

- The cached products are figure-data and compact summary products, not a full
  DESI cosmology likelihood implementation.
- The current repository still has no BAO, DESI, Euclid, CMB, supernova, or
  matter-power likelihood pipeline.
- This asset does not supply candidate `X`, `Q^nu`, `delta Q`, a foam-sector
  state variable, or known-model distinction.
