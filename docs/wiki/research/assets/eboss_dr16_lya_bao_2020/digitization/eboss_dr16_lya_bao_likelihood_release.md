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
| Parse method | source-file inspection, MarkItDown README conversion, and Markdown assembly |
| PageIndex used | no; no paper PDF body was parsed |
| MarkItDown used | yes, for [MarkItDown BAO-only README conversion](markitdown_BAO-only_README.md) |

## Cached Likelihood Files

| Local file | Upstream role |
| --- | --- |
| `../source/BAO-only_README.txt` | format description for DR16 BAO likelihood products |
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

## Open Product Choices

Before any BAO penalty or likelihood comparison, a future plan must decide:

- whether to use the published paper central values, the two SDSS likelihood
  grids, or a Gaussian approximation;
- whether and how to combine the auto-correlation and cross-correlation grids;
- whether raw FITS data-vector/covariance products are required;
- whether `r_d` is fixed, ratio-eliminated, or marginalized;
- whether the comparison is diagnostic only or a formal likelihood.

No such decision is made here.
