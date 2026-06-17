---
doc_id: asset_desi_dr2_lya_bao_2025_markitdown_upstream_readme
title: "DESI DR2 Lyman-alpha BAO MarkItDown Upstream README Conversion"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_desi_dr2_lya_bao_2025
next_gate: use curated data-release parse for source-product decisions
last_updated: 2026-06-17
---

# DESI DR2 Lyman-alpha BAO MarkItDown Upstream README Conversion

Quality state: `low_fidelity_search_text`.

This is a direct [MarkItDown](https://github.com/microsoft/markitdown) conversion of
`../source/extracted/README`. Use
[DESI DR2 Lyman-alpha BAO data-release parse](desi_dr2_lya_bao_data_release.md)
for the curated source-file inspection record.

Data files to reproduce figures in DESI DR2 Results I: Baryon Acoustic Oscillations from the Lyman Alpha Forest by the DESI Collaboration.

Figure 1:
radec.fits: fits table with RA,DEC for Healpix (NSIDE=64) of the quasar catalog
desi_north.npz: zip archive of DESI northern footprint
desi_south.npz: zip archive of DESI southern footprint
SDSS_DR16_north.npy: numpy data file of SDSS northern footprint
SDSS_DR16_south.npy: numpy data file of SDSS southern footprint
Y1_numtile.csv: Y1 number of quasars with given number of observations
Y3_numtile.csv: Y3 number of quasars with given number of observations

Figure 2:
loa-spectrum-84-z3.20-39627696665266273-main-dark.csv: flux vs. wavelength

Figure 3:
lyalyaxlyalya_data.csv: data points and errorbars for 4 wedges
lyalyaxlyalya_model.csv: baseline and BB model values for 4 wedges
lyalyaxlyalyb_data.csv
lyalyaxlyalyb_model.csv

Figure 4:
lyalyaxqso_data.csv: data points and errorbars for 4 wedges
lyalyaxqso_model.csv: baseline and BB model values for 4 wedges
lyalybxqso_data.csv
lyalybxqso_model.csv

Figure 5:
alphas.txt: data points and errors

Figure 6:
residuals_2d.fits: residual plot images

Figure 7:
bootstrap.fits: 20 realizations shown in figure

Figure 8:
mock_wedges.json: python dictionary of all points and lines in figure

Figure 9:
mock_pairs.txt: data points and errors

Figure 10:
data_splits.txt: data points and errors

Figure 11:
data_points_2D.csv: data points and errors
data_points_cov_ap_at.dat: covariance of ap, at

Figure 12:
dmdh_cmb.txt: data points and errors

Figure 13:
variations.txt: data points and errors
