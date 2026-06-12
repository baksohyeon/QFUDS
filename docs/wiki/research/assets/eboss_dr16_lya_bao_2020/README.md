---
doc_id: asset_eboss_dr16_lya_bao_2020
title: "eBOSS DR16 Lyman-alpha BAO 2020 Assets"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - exp006_timing_investigation_index
next_gate: manual structured extraction only if a status-neutral BAO geometry audit needs it
last_updated: 2026-06-12
---

# eBOSS DR16 Lyman-alpha BAO 2020 Assets

Local access copies for the completed SDSS-IV eBOSS DR16 Lyman-alpha BAO
products associated with du Mas des Bourboux et al. 2020, arXiv:2007.08995.

These files are research assets only. They do not create a new experiment,
change Exp006 conclusions, open a likelihood pipeline, or change roadmap status.

## Source

- Paper: <https://arxiv.org/abs/2007.08995>
- SDSS final BAO/RSD results page:
  <https://www.sdss4.org/science/final-bao-and-rsd-measurements/>
- SDSS DR16 cosmology likelihood directory:
  <https://svn.sdss.org/public/data/eboss/DR16cosmo/tags/v1_0_1/likelihoods/BAO-only/>
- SDSS DR16 Lyman-alpha data-vector/covariance directory:
  <https://svn.sdss.org/public/data/eboss/DR16cosmo/tags/v1_0_1/dataveccov/lya_forest/>

## Files

- `source/BAO-only_README.txt` - upstream README for DR16 BAO likelihood files.
- `source/sdss_DR16_LYAUTO_BAO_DMDHgrid.txt` - Ly-alpha auto-correlation
  likelihood grid.
- `source/sdss_DR16_LYxQSO_BAO_DMDHgrid.txt` - Ly-alpha/quasar
  cross-correlation likelihood grid.
- `source/dataveccov_lya_forest_listing.xml` - cached directory listing for raw
  Lyman-alpha forest data-vector/covariance assets.
- `figures/` - reserved for rendered or copied figure assets.
- `digitization/` - reserved for manual structured extracts or derived numeric
  products.

## Current Asset State

- Asset state: `asset_cached`.
- Extraction potential: `direct_table`.
- Markdown conversion quality: not applicable.

The BAO-only README and Lyman-alpha likelihood grids have been downloaded. Raw
data-vector/covariance FITS products were identified by directory listing but
were not downloaded or parsed in this pass.

## Recovered File Semantics

The upstream `BAO-only_README.txt` states that the DR16 Lyman-alpha BAO
likelihoods are supplied separately for auto-correlation (`LYAUTO`) and
cross-correlation (`LYXQSO`) and can be treated as independent.

Each grid uses:

```text
Column 1: D_M(z=2.334)/r_d
Column 2: D_H(z=2.334)/r_d
Column 3: likelihood ratio
```

This is not a simple cached 2x2 Gaussian covariance block. A future
status-neutral BAO audit must decide whether to use the published compressed
central values from the paper, the two grid likelihoods, or a separate Gaussian
approximation.

## Known Limits

- The cached eBOSS Lyman-alpha files are likelihood grids and directory
  listings, not a QFUDS-ready likelihood pipeline.
- The current repository still has no BAO, DESI, Euclid, CMB, supernova, or
  matter-power likelihood pipeline.
- This asset does not supply candidate `X`, `Q^nu`, `delta Q`, a foam-sector
  state variable, or known-model distinction.
