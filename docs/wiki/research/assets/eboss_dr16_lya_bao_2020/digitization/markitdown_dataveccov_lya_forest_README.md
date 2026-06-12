---
doc_id: asset_eboss_dr16_lya_bao_2020_markitdown_dataveccov_lya_forest_readme
title: "eBOSS DR16 Lyman-alpha BAO MarkItDown Data-Vector/Covariance README Conversion"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_eboss_dr16_lya_bao_2020
next_gate: download raw FITS assets only under a size-aware plan
last_updated: 2026-06-12
---

# eBOSS DR16 Lyman-alpha BAO MarkItDown Data-Vector/Covariance README Conversion

Quality state: `low_fidelity_search_text`.

This is a direct MarkItDown conversion of
`../source/dataveccov_lya_forest_README.txt`. Use
[eBOSS DR16 Lyman-alpha BAO likelihood-release parse](eboss_dr16_lya_bao_likelihood_release.md)
for the curated source-file inspection record.

This folder contains the correlation functions, covariances and associated files
from the publication "The Completed SDSS-IV extended Baryon Oscillation Spectroscopic Survey: Baryon acoustic oscillations with Lyman-α forests" (du Mas des Bourboux et al. 2020).

These files have been copied from https://svn.sdss.org/repo/eboss/lyaf/dr16/autocross/Work/Sources/correlations by Andreu Font-Ribera on October 15th 2020.

They files correspond to the 4 different measurements presented in that publication:
 - Lya(Lya) x Lya(Lya): auto-correlation of the Lya forest measured in the Lyman alpha region
 - Lya(Lya) x Lya(Lyb): correlation of the Lya forest in the Lya region, with the Lya forest in the Lyman beta region
 - Lya(Lya) x QSO: cross-correlation of the Lya forest in the Lya region with quasar positions
 - Lya(Lya) x QSO: cross-correlation of the Lya forest in the Lyb region with quasar positions

The format corresponds to the output format of Picca (https://github.com/igmhub/picca), and to the
input format of Picca's fitter2 (https://github.com/igmhub/picca/tree/master/py/picca/fitter2) and Vega's fitter (https://github.com/andreicuceu/vega).

Files with -exp correspond to "expanded correlation" files that include the "covariance matrix" for a particular measurement, as well as its "distortion matrix" used to convolve models in the fitters.

Files starting with metal_* below refer to "metal matrices" used in each of the 4 analysis to model the contamination by metal lines.

TO DO: We should add a link to a tutorial describing the format of these files in Picca or Vega.

Files included are:
 - cf_LYA_in_LYA_LYA_in_LYB_z_0_10-exp.fits.gz
 - cf_LYA_in_LYA_LYA_in_LYB_z_0_10.fits.gz
 - cf_z_0_10-exp.fits.gz
 - cf_z_0_10.fits.gz
 - metal_dmat_LYA_in_LYA_LYA_in_LYB_z_0_10.fits
 - metal_dmat_z_0_10.fits
 - metal_xdmat_LYA_in_LYB_z_0_10.fits
 - metal_xdmat_z_0_10.fits
 - xcf_LYA_in_LYB_z_0_10-exp.fits.gz
 - xcf_LYA_in_LYB_z_0_10.fits.gz
 - xcf_z_0_10-exp.fits.gz
 - xcf_z_0_10.fits.gz
