---
doc_id: asset_eboss_dr16_lya_bao_2020_likelihood_release_parse
title: "eBOSS DR16 Lyman-alpha BAO Likelihood-Release Parse"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_eboss_dr16_lya_bao_2020
next_gate: manual structured extraction before BAO penalty or likelihood use
last_updated: 2026-06-12
---

# eBOSS DR16 Lyman-alpha BAO Likelihood-Release Parse

## Scope

This document converts the cached eBOSS DR16 Lyman-alpha BAO likelihood-release
files into a Markdown inspection record.

Quality state:

```text
source_text_parse
```

This is not `manual_structured_extract`, not `numeric_digitized`, and not a BAO
likelihood implementation.

## Source Asset

| Field | Value |
| --- | --- |
| Paper | du Mas des Bourboux et al. 2020, arXiv:2007.08995 |
| SDSS final results page | <https://www.sdss4.org/science/final-bao-and-rsd-measurements/> |
| BAO-only likelihood directory | <https://svn.sdss.org/public/data/eboss/DR16cosmo/tags/v1_0_1/likelihoods/BAO-only/> |
| Data-vector/covariance directory | <https://svn.sdss.org/public/data/eboss/DR16cosmo/tags/v1_0_1/dataveccov/lya_forest/> |
| Source-page conversions | [SDSS final BAO/RSD page](markitdown_sdss_final_bao_rsd_measurements.md), [BAO-only directory](markitdown_sdss_bao_only_directory.md), [data-vector/covariance directory](markitdown_sdss_dataveccov_lya_forest_directory.md), [arXiv page](markitdown_arxiv_2007.08995.md) |
| Parse method | source-page conversion, source-file inspection, MarkItDown README conversion, and Markdown assembly |
| PageIndex used | no; no paper PDF body was parsed |
| MarkItDown used | yes, for [MarkItDown BAO-only README conversion](markitdown_BAO-only_README.md) |

## Cached Likelihood Files

| Local file | Upstream role |
| --- | --- |
| `../source/BAO-only_README.txt` | format description for DR16 BAO likelihood products |
| `../source/dataveccov_lya_forest_README.txt` | format description for raw Lyman-alpha data-vector/covariance products |
| `../source/sdss_DR16_LYAUTO_BAO_DMDHgrid.txt` | Ly-alpha auto-correlation likelihood grid |
| `../source/sdss_DR16_LYxQSO_BAO_DMDHgrid.txt` | Ly-alpha/quasar cross-correlation likelihood grid |
| `../source/dataveccov_lya_forest_listing.xml` | directory listing for raw Lyman-alpha data-vector/covariance assets |

## Upstream Grid Semantics

The upstream README states that DR16 Lyman-alpha BAO likelihoods are provided
separately for auto-correlation and cross-correlation and can be treated as
independent.

Each grid has:

```text
Column 1: D_M(z=2.334)/r_d
Column 2: D_H(z=2.334)/r_d
Column 3: likelihood ratio relative to the best point on the grid
```

The README also states that `r_d` is the sound horizon at the drag epoch and is
`147.8 Mpc` in the fiducial cosmology used by eBOSS.

## Grid Inspection

| File | Rows excluding header | `D_M/r_d` range | `D_H/r_d` range | Max-likelihood point |
| --- | ---: | --- | --- | --- |
| `sdss_DR16_LYAUTO_BAO_DMDHgrid.txt` | `2500` | `31.3628` to `47.0442` | `6.88088` to `10.32132` | `D_M/r_d = 37.763371428571425`, `D_H/r_d = 8.917058775510204`, likelihood ratio `1.0` |
| `sdss_DR16_LYxQSO_BAO_DMDHgrid.txt` | `2500` | `31.3628` to `47.0442` | `6.88088` to `10.32132` | `D_M/r_d = 37.44334285714286`, `D_H/r_d = 9.057484897959185`, likelihood ratio `1.0` |

These grid maxima are inspection products only. They are not combined and are
not a substitute for the published combined BAO result.

## Raw Data-Vector/Covariance Listing

The cached `dataveccov_lya_forest_listing.xml` identifies these upstream raw
asset candidates:

| File | Local state |
| --- | --- |
| `README.txt` | listed only |
| `cf_LYA_in_LYA_LYA_in_LYB_z_0_10-exp.fits.gz` | listed only |
| `cf_LYA_in_LYA_LYA_in_LYB_z_0_10.fits.gz` | listed only |
| `cf_z_0_10-exp.fits.gz` | listed only |
| `cf_z_0_10.fits.gz` | listed only |
| `metal_dmat_LYA_in_LYA_LYA_in_LYB_z_0_10.fits` | listed only |
| `metal_dmat_z_0_10.fits` | listed only |
| `metal_xdmat_LYA_in_LYB_z_0_10.fits` | listed only |
| `metal_xdmat_z_0_10.fits` | listed only |
| `xcf_LYA_in_LYB_z_0_10-exp.fits.gz` | listed only |
| `xcf_LYA_in_LYB_z_0_10.fits.gz` | listed only |
| `xcf_z_0_10-exp.fits.gz` | listed only |
| `xcf_z_0_10.fits.gz` | listed only |

Those FITS products were not downloaded or parsed in this pass.

The source-page retrieval added the upstream `dataveccov_lya_forest_README.txt`.
It states that the folder contains correlation functions, covariances, and
associated files from du Mas des Bourboux et al. 2020. Files ending in `-exp`
include the covariance matrix for a particular measurement and its distortion
matrix. The format corresponds to Picca output and Picca/Vega fitter input.

## Raw FITS Size Inventory

The raw FITS assets were size-checked but not downloaded because several are
hundreds of MB to about 1 GB each.

| File | Size bytes | Local state |
| --- | ---: | --- |
| `cf_LYA_in_LYA_LYA_in_LYB_z_0_10-exp.fits.gz` | `55307441` | `asset_available_not_downloaded` |
| `cf_LYA_in_LYA_LYA_in_LYB_z_0_10.fits.gz` | `33804112` | `asset_available_not_downloaded` |
| `cf_z_0_10-exp.fits.gz` | `55804251` | `asset_available_not_downloaded` |
| `cf_z_0_10.fits.gz` | `33797900` | `asset_available_not_downloaded` |
| `metal_dmat_LYA_in_LYA_LYA_in_LYB_z_0_10.fits` | `1001629440` | `asset_available_not_downloaded` |
| `metal_dmat_z_0_10.fits` | `1001629440` | `asset_available_not_downloaded` |
| `metal_xdmat_LYA_in_LYB_z_0_10.fits` | `1000814400` | `asset_available_not_downloaded` |
| `metal_xdmat_z_0_10.fits` | `1000814400` | `asset_available_not_downloaded` |
| `xcf_LYA_in_LYB_z_0_10-exp.fits.gz` | `205520221` | `asset_available_not_downloaded` |
| `xcf_LYA_in_LYB_z_0_10.fits.gz` | `66241631` | `asset_available_not_downloaded` |
| `xcf_z_0_10-exp.fits.gz` | `204731684` | `asset_available_not_downloaded` |
| `xcf_z_0_10.fits.gz` | `67408974` | `asset_available_not_downloaded` |

## Open Product Choices

Before any BAO penalty or likelihood comparison, a future plan must decide:

- whether to use the published paper central values, the two SDSS likelihood
  grids, or a Gaussian approximation;
- whether and how to combine the auto-correlation and cross-correlation grids;
- whether raw FITS data-vector/covariance products are required;
- whether `r_d` is fixed, ratio-eliminated, or marginalized;
- whether the comparison is diagnostic only or a formal likelihood.

No such decision is made here.
