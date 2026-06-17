---
doc_id: asset_eboss_dr16_lya_bao_2020_markitdown_sdss_final_bao_rsd
title: "eBOSS DR16 Lyman-alpha BAO MarkItDown SDSS Final BAO/RSD Page Conversion"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_eboss_dr16_lya_bao_2020
next_gate: use curated likelihood-release parse for source-product decisions
last_updated: 2026-06-17
---

# eBOSS DR16 Lyman-alpha BAO MarkItDown SDSS Final BAO/RSD Page Conversion

Quality state: `low_fidelity_search_text`.

This is a direct [MarkItDown](https://github.com/microsoft/markitdown) conversion of
<https://www.sdss4.org/science/final-bao-and-rsd-measurements/>. It is a
source-page aid for locating official SDSS products.

[![sdsslogo](/wp-content/uploads/2014/05/sdsslogowhite.png)](/)

![sdsslogo](/wp-content/uploads/2014/05/sdsslogowhite.png)

* [Data](https://www.sdss4.org/dr17/)
* [Surveys](https://www.sdss4.org/surveys/)
* [Instruments](https://www.sdss4.org/instruments/)
* [Collaboration](https://www.sdss4.org/collaboration/)
* [Results](https://www.sdss4.org/science/)
* [Education](https://www.sdss4.org/education/)
* [The Future](https://www.sdss4.org/future/)
* [Contact](https://www.sdss4.org/contact/)

This is Data Release 17.
See our full list of [data releases](/science/data-release-publications).

php// echo do\_shortcode('[wpdreams\_ajaxsearchlite]'); ?

Search for:

Search

# Final BAO and RSD Measurements

BAO and RSD Results

![Snapshot of the three-dimensional map of galaxies and quasars observed over four generations of SDSS spectroscopy.  Image credit: Anand Raichoor (EPFL), Ashley Ross (Ohio State University) and the SDSS Collaboration.  A full video rendering of these data can be found in the <a href="https://youtu.be/UTlYUxucEZA">3D visualization</a> appropriate for scientific presentations. ](https://www.sdss4.org/wp-content/uploads/2020/06/eboss_map.png)

Snapshot of the three-dimensional map of galaxies and quasars observed over four generations of SDSS spectroscopy. Image credit: Anand Raichoor (EPFL), Ashley Ross (Ohio State University) and the SDSS Collaboration. A full video rendering of these data can be found in the [3D visualization](https://youtu.be/UTlYUxucEZA) appropriate for scientific presentations.

The SDSS-I and -II, [BOSS](../../surveys/boss), and [eBOSS](../../surveys/eboss/) spectroscopic surveys provide galaxy and quasar samples out to redshifts z<3.5. The main tracers for these measurements are the low redshift galaxies (MGS) from the earlier phases of SDSS, the luminous galaxies from BOSS, luminous red galaxies (LRG) from eBOSS, emission line galaxies (ELG) from eBOSS, and quasars, primarily from BOSS and eBOSS. The three dimensional clustering in these samples was used to make 15 distinct, high precision measurements of Baryon Acoustic Oscillations (BAO) and six measurements of redshift space distortions (RSD). The aggregate precision of the expansion history measurements is 0.70% at redshifts z < 1 and 1.19% at redshifts z > 1, while the aggregate precision of the growth measurements is 4.78% over the redshift interval 0 < z < 1.5. With this redshift coverage and sensitivity, the SDSS experiment is [unparalleled in its ability to explore models of cosmology](https://www.sdss4.org/science/cosmology-results-from-eboss/).

Both BOSS and eBOSS used the upgraded [1000-fiber spectrographs](https://ui.adsabs.harvard.edu/abs/2013AJ....146...32S/abstract) that were installed at the 2.5 meter Sloan Telescope in 2009. The BOSS design and survey strategy are described in [the 2009-2014 BOSS overview](https://ui.adsabs.harvard.edu/abs/2013AJ....145...10D/abstract) while the eBOSS scientific justification and survey plan are described in [the 2014-2019 eBOSS overview](https://ui.adsabs.harvard.edu/abs/2016AJ....151...44D/abstract). Key to the BAO and RSD measurements in SDSS, BOSS, and eBOSS are advanced processing of imaging data, carefully crafted target selection, well vetted catalogs of redshifts, weights, and randoms, clustering analysis, and assessment of statistical and systematic errors through mock catalogs.

The likelihoods, covariance matrices, and cosmoMC chains with the SDSS data can be found [here](https://svn.sdss.org/public/data/eboss/DR16cosmo/tags/v1_0_1/). The background of these measurements for each of the SDSS cosmology samples can be found in the table below.

The table below may be cut off in your browser, so we also have [a full-width version of the table](/science/final-bao-and-rsd-measurements-table/).

| Parameter | Main Galaxy Sample (MGS) | BOSS Galaxy | BOSS Galaxy | eBOSS LRG | eBOSS ELG | eBOSS Quasar | Lyα-Lyα | Lyα-Quasar |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Imaging, Target Selection, and Spectroscopic Properties of Each Sample | | | | | | | | |
| Imaging for Target Selection | [SDSS](https://www.sdss4.org/dr17/imaging/) | [SDSS](https://www.sdss4.org/dr17/imaging/) | [SDSS](https://www.sdss4.org/dr17/imaging/) | [SDSS](https://www.sdss4.org/dr17/imaging/) + [WISE](https://ui.adsabs.harvard.edu/abs/2016AJ....151...36L/abstract) | [DECaLS](https://ui.adsabs.harvard.edu/abs/2019AJ....157..168D/abstract) | [SDSS](https://www.sdss4.org/dr17/imaging/) + [WISE](https://ui.adsabs.harvard.edu/abs/2016AJ....151...36L/abstract) | [SDSS](https://www.sdss4.org/dr17/imaging/) + [WISE](https://ui.adsabs.harvard.edu/abs/2016AJ....151...36L/abstract) + MISC | [SDSS](https://www.sdss4.org/dr17/imaging/) + [WISE](https://ui.adsabs.harvard.edu/abs/2016AJ....151...36L/abstract) + MISC |
| Target Selection | [g,r](https://ui.adsabs.harvard.edu/abs/2015MNRAS.449..835R/abstract) | [g,r,i](https://ui.adsabs.harvard.edu/abs/2016MNRAS.455.1553R/abstract) | [g,r,i](https://ui.adsabs.harvard.edu/abs/2016MNRAS.455.1553R/abstract) | [g,r,i,z,W1](https://ui.adsabs.harvard.edu/abs/2016ApJS..224...34P/abstract) | g,r,z | [u,g,r,i,z,W1,W2](https://ui.adsabs.harvard.edu/abs/2015ApJS..221...27M/abstract) | [misc](https://ui.adsabs.harvard.edu/abs/2012ApJS..199....3R/abstract) | [misc](https://ui.adsabs.harvard.edu/abs/2012ApJS..199....3R/abstract) |
| Spectroscopic Program | SDSS-I and -II | BOSS | BOSS | BOSS and eBOSS | eBOSS | primarily eBOSS | BOSS and eBOSS | BOSS and eBOSS |
| redshift range | 0.07 < z < 0.20 | 0.2 < z < 0.5 | 0.4 < z < 0.6 | 0.6 < z < 1.0 | 0.6 < z < 1.1 | 0.8 < z < 2.2 | z > 2.1 | z > 1.77 |
| Number of Tracers | 63,163 | 604,001 | 686,370 | 377,458 | 173,736 | 343,708 | 210,005 | 341,468 |
| Effective Redshift | 0.15 | 0.38 | 0.51 | 0.70 | 0.85 | 1.48 | 2.33 | 2.33 |
| Effective Volume (Gpc3) | 0.24 | 3.7 | 4.2 | 2.7 | 0.6 | 0.6 |  |  |
| Clustering Catalog Documentation | [Ross et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020yCat..74490835R/abstract) | [Reid et al. (2016)](https://ui.adsabs.harvard.edu/abs/2016MNRAS.455.1553R/abstract) | [Reid et al. (2016)](https://ui.adsabs.harvard.edu/abs/2016MNRAS.455.1553R/abstract) | [Ross et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200709000R/abstract) | [Raichoor et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200709007R/abstract) | [Ross et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200709000R/abstract), [Lyke et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200709001L/abstract) | [du Mas des Bourboux et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708995D/abstract), [Lyke et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200709001L/abstract) | [du Mas des Bourboux et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708995D/abstract), [Lyke et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200709001L/abstract) |
| N-body and Mock Catalogs |  | [Kitaura et al. (2016)](https://ui.adsabs.harvard.edu/abs/2016MNRAS.456.4156K/abstract) | [Kitaura et al. (2016)](https://ui.adsabs.harvard.edu/abs/2016MNRAS.456.4156K/abstract) | [Zhao et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708997Z/abstract), [Rossi et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200709002R/abstract) | [Zhao et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708997Z/abstract), [Lin et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708996L/abstract), [Alam et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200709004A/abstract), [Avila et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200709012A/abstract) | [Zhao et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708997Z/abstract), [Smith et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200709003S/abstract) | [Farr et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020JCAP...03..068F/abstract) | [Farr et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020JCAP...03..068F/abstract) |
| BAO-only Measurements | | | | | | | | |
| Correlation Function Measurement | [![](https://www.sdss4.org/wp-content/uploads/2020/07/xi_MGS_NSbaofitpostrecon.png)](https://www.sdss4.org/wp-content/uploads/2020/07/xi_MGS_NSbaofitpostrecon.png) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/xi_BOSSlow_NSbaofitpostrecon.png)](https://www.sdss4.org/wp-content/uploads/2020/07/xi_BOSSlow_NSbaofitpostrecon.png) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/xi_BOSSmid_NSbaofitpostrecon.png)](https://www.sdss4.org/wp-content/uploads/2020/07/xi_BOSSmid_NSbaofitpostrecon.png) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/xi_LRG_NSbaofitpostrecon.png)](https://www.sdss4.org/wp-content/uploads/2020/07/xi_LRG_NSbaofitpostrecon.png) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/xi_ELG_NSbaofitpostrecon.png)](https://www.sdss4.org/wp-content/uploads/2020/07/xi_ELG_NSbaofitpostrecon.png) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/xi_QSO_NSbaofitprerecon.png)](https://www.sdss4.org/wp-content/uploads/2020/07/xi_QSO_NSbaofitprerecon.png) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/xiw_Lyacf_z_0_10_mu950.png)](https://www.sdss4.org/wp-content/uploads/2020/07/xiw_Lyacf_z_0_10_mu950.png) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/xiw_Lyaxcf_z_0_10_mu950.png)](https://www.sdss4.org/wp-content/uploads/2020/07/xiw_Lyaxcf_z_0_10_mu950.png) |
| Power Spectrum Measurement | [![](https://www.sdss4.org/wp-content/uploads/2020/07/MGSPkBAO_monoWJP.png)](https://www.sdss4.org/wp-content/uploads/2020/07/MGSPkBAO_monoWJP.png) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/BOSSz1PkBAO_monoWJP.png)](https://www.sdss4.org/wp-content/uploads/2020/07/BOSSz1PkBAO_monoWJP.png) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/BOSSz2PkBAO_monoWJP.png)](https://www.sdss4.org/wp-content/uploads/2020/07/BOSSz2PkBAO_monoWJP.png) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/LRGPkBAO_monoWJP.png)](https://www.sdss4.org/wp-content/uploads/2020/07/LRGPkBAO_monoWJP.png) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/ELGPkBAO_monoWJP.png)](https://www.sdss4.org/wp-content/uploads/2020/07/ELGPkBAO_monoWJP.png) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/QSOPkBAO_monoWJP.png)](https://www.sdss4.org/wp-content/uploads/2020/07/QSOPkBAO_monoWJP.png) |
| DV(z)/rd | 4.47 +/- 0.17 |  |  |  | 18.33-0.62+0.57 |  |  |  |
|
| DM(z)/rd |  | 10.23 +/- 0.17 | 13.36 +/- 0.21 | 17.86 +/- 0.33 |  | 30.69 +/- 0.80 | 37.6 +/- 1.9 | 37.3 +/- 1.7 |
| DH(z)/rd |  | 25.00 +/- 0.76 | 22.33 +/- 0.58 | 19.33 +/- 0.53 |  | 13.26 +/- 0.55 | 8.93 +/- 0.28 | 9.08 +/- 0.34 |
| Reference for final results | [Ross et al. (2015)](https://ui.adsabs.harvard.edu/abs/2015MNRAS.449..835R/abstract) | [BOSS Collaboration (2017)](https://ui.adsabs.harvard.edu/abs/2017MNRAS.470.2617A/abstract) | [BOSS Collaboration (2017)](https://ui.adsabs.harvard.edu/abs/2017MNRAS.470.2617A/abstract) | [Bautista et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708993B/abstract), [Gil-Marin et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708994G/abstract) | [Raichoor et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200709007R/abstract), [de Mattia et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200709008D/abstract) | [Hou et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708998H/abstract), [Neveux et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708999N/abstract) | [du Mas des Bourbuox et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708995D/abstract) | [du Mas des Bourbuox et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708995D/abstract) |
| RSD Measurements |
| Correlation Function Measurement | [![](https://www.sdss4.org/wp-content/uploads/2020/07/2dcontour_mgs_NSbaofit.png)](https://www.sdss4.org/wp-content/uploads/2020/07/2dcontour_mgs_NSbaofit.pdf) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/2dcontour_bossdr12_lowz_NSbaofit.png)](https://www.sdss4.org/wp-content/uploads/2020/07/2dcontour_bossdr12_lowz_NSbaofit.png) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/2dcontour_bossdr12_intz_NSbaofit.png)](https://www.sdss4.org/wp-content/uploads/2020/07/2dcontour_bossdr12_intz_NSbaofit.pdf) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/2dcontour_LRG_NSbaofit.png)](https://www.sdss4.org/wp-content/uploads/2020/07/2dcontour_LRG_NSbaofit.pdf) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/2dcontour_elg_NSbaofit.png)](https://www.sdss4.org/wp-content/uploads/2020/07/2dcontour_elg_NSbaofit.pdf) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/2dcontour_qso_NSbaofit.png)](https://www.sdss4.org/wp-content/uploads/2020/07/2dcontour_qso_NSbaofit.pdf) |  |  |
| f σ8(z) | 0.53 +/- 0.16 | 0.500 +/- 0.047 | 0.455 +/- 0.039 | 0.448 +/- 0.043 | 0.315 +/- 0.095 | 0.462 +/- 0.045 |  |  |
| BAO+RSD Measurements |
| Correlation Function Multipoles | [![](https://www.sdss4.org/wp-content/uploads/2020/07/mgs_xi2m.png)](https://www.sdss4.org/wp-content/uploads/2020/07/mgs_xi2m.pdf) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/bossdr12_lowz_xi2m.png)](https://www.sdss4.org/wp-content/uploads/2020/07/bossdr12_lowz_xi2m.pdf) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/bossdr12_intz_xi2m.png)](https://www.sdss4.org/wp-content/uploads/2020/07/bossdr12_intz_xi2m.pdf) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_lrg_xi3m.png)](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_lrg_xi3m.pdf) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_elg_xi3m.png)](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_elg_xi3m.pdf) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_qso_xi3m.png)](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_qso_xi3m.pdf) |  |  |
| Power Spectrum Multipoles |  | [![](https://www.sdss4.org/wp-content/uploads/2020/07/bossdr12_lowz_pk3m.png)](https://www.sdss4.org/wp-content/uploads/2020/07/bossdr12_lowz_pk3m.pdf) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/bossdr12_intz_pk3m.png)](https://www.sdss4.org/wp-content/uploads/2020/07/bossdr12_intz_pk3m.pdf) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_lrg_pk3m.png)](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_lrg_pk3m.pdf) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_elg_pk3m_pix64.png)](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_elg_pk3m_pix64.pdf) | [![](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_qso_pk3m.png)](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_qso_pk3m.pdf) |  |  |
| DV(z)/rd | 4.51 +/- 0.14 |  |  |  |  |  |  |  |
| DM(z)/rd |  | 10.27 +/- 0.15 | 13.38 +/- 0.18 | 17.65 +/- 0.30 | 19.5 +/- 1.0 | 30.21 +/- 0.79 | 37.6 +/- 1.9 | 37.3 +/- 1.7 |
| DH(z)/rd |  | 24.89 +/- 0.58 | 22.43 +/- 0.48 | 19.78 +/- 0.46 | 19.6 +/- 2.1 | 13.23 +/- 0.47 | 8.93 +/- 0.28 | 9.08 +/- 0.34 |
| f σ8 | 0.53 +/- 0.16 | 0.497 +/- 0.045 | 0.459 +/- 0.038 | 0.473 +/- 0.041 | 0.315 +/- 0.095 | 0.462 +/- 0.045 |  |  |
| Reference for final results | [Howlett et al. (2015)](https://ui.adsabs.harvard.edu/abs/2015MNRAS.449..848H/abstract) | [BOSS Collaboration (2017)](https://ui.adsabs.harvard.edu/abs/2017MNRAS.470.2617A/abstract) | [BOSS Collaboration (2017)](https://ui.adsabs.harvard.edu/abs/2017MNRAS.470.2617A/abstract) | [Bautista et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708993B/abstract), [Gil-Marin et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708994G/abstract) | [Tamone et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200709009T/abstract), [de Mattia et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200709008D/abstract) | [Hou et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708998H/abstract), [Neveux et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708999N/abstract) | [du Mas des Bourbuox et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708995D/abstract) | [du Mas des Bourbuox et al. (2020)](https://ui.adsabs.harvard.edu/abs/2020arXiv200708995D/abstract) |

### Additional Cosmology Measurements

The spectroscopic samples from BOSS and eBOSS allow for a diverse array of cosmology studies beyond the cosmic expansion history and growth of structure presented above. These data have been used to advance models for the summed neutrino mass and inflation. In addition, new techniques have been developed to use combinations of tracers or new tracers for direct measurements of BAO and RSD.

[![](https://www.sdss4.org/wp-content/uploads/2020/07/MgII.png)](https://www.sdss4.org/wp-content/uploads/2020/07/MgII.png)[Measurements of the cross-correlation of the CIV forest with quasars](https://ui.adsabs.harvard.edu/abs/2018JCAP...05..029B/abstract) allowed constraints on the clustering properties of CIV and indication that future surveys should be able to use this technique to measure BAO. [Measurements of the cross-correlation of the Mg II forest with galaxies and quasars](https://ui.adsabs.harvard.edu/abs/2019ApJ...878...47D/abstract) played a similar role, with detection of a feature consistent with BAO at a significance of χ2 = 7.25.

[![](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_LRGpCMASSxELG_xi3m.png)](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_LRGpCMASSxELG_xi3m.pdf)[![](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_LRGpCMASSxELG_pk3m.png)](https://www.sdss4.org/wp-content/uploads/2020/07/dr16_LRGpCMASSxELG_pk3m.pdf)Multi-tracer BAO and RSD measurements in [configuration space](https://ui.adsabs.harvard.edu/abs/2020arXiv200709010W/abstract) and [Fourier space](https://ui.adsabs.harvard.edu/abs/2020arXiv200709011Z/abstract) using the eBOSS LRG ELG samples are complementary to those above. The effective redshifts, central values of the BAO and RSD parameters, and covariance matrix are included in a [compressed file for the configuration space measurement](https://www.sdss4.org/wp-content/uploads/2020/07/MultiTracer_CF_BAORSD_measurements.zip) and in a [compressed file for the Fourier space measurement](https://www.sdss4.org/wp-content/uploads/2020/07/MultiTracer_PK_BAORSD_measurements.zip)

[![](https://www.sdss4.org/wp-content/uploads/2020/07/Lymanalpha1d.png)](https://www.sdss4.org/wp-content/uploads/2020/07/Lymanalpha1d.png)[The one-dimensional power spectrum from the SDSS DR14 Lyman-alpha forests](https://ui.adsabs.harvard.edu/abs/2019JCAP...07..017C/abstract) Measurements of the flux power spectrum over the redshift range 2.2 < z < 4.6 and scales up to k=0.02 (km/s)-1. Measurements are performed from a sample of 43,751 quasar spectra.

[![](https://www.sdss4.org/wp-content/uploads/2020/07/fnl.png)](https://www.sdss4.org/wp-content/uploads/2020/07/fnl.pdf)[Constraints on primordial non-Gaussianity](https://ui.adsabs.harvard.edu/abs/2019JCAP...09..010C/abstract) using eBOSS quasars led to constraints of -51 < fNLloc < 21 at the 95% confidence level. This is the tightest constraint on primordial non-Gaussianities using Large Scale Structure data alone.

[![](https://www.sdss4.org/wp-content/uploads/2020/07/void-galaxy.png)](https://www.sdss4.org/wp-content/uploads/2020/07/void-galaxy.png)[The first void detections in eBOSS](https://ui.adsabs.harvard.edu/abs/2020JCAP...06..012H/abstract) were made using DR14 LRGs and quasars and [later extended](https://ui.adsabs.harvard.edu/abs/2020arXiv200709013A/abstract) to the final eBOSS sample. Using the cross-correlation of these voids with other tracers allows complementary constraints on the linear redshift-space distortion parameter to those above.

[![](https://www.sdss4.org/wp-content/uploads/2020/08/dr16_lrg_voidgalaxy_xi2m.png)](https://www.sdss4.org/wp-content/uploads/2020/08/dr16_lrg_voidgalaxy_xi2m.png)[Measurement of the anisotropic void-galaxy correlation in the LRG sample](https://ui.adsabs.harvard.edu/abs/2020JCAP...06..012H/abstract) allows measurement of the Alcock-Paczynski parameter ratio DM/DH and the growth rate of structure. This measurement is complementary to the BAO and RSD analyses above; combining the void results with galaxy clustering leads to a 55% reduction in parameter uncertainties for DM/rd, DM/rd and f σ8 for the eBOSS LRG bin.

* [Science Results](https://www.sdss4.org/science/)
* [Cosmology](https://www.sdss4.org/science/cosmology-results-from-eboss/)
* [BAO / RSD](https://www.sdss4.org/science/final-bao-and-rsd-measurements/)
* [Milky Way](https://www.sdss4.org/science/milky-way-science-results/)
* [Stellar Astrophysics](https://www.sdss4.org/science/stellar-astrophysics/)
* [Press Releases](//www.sdss.org/press-releases/)
* [Publications](https://www.sdss4.org/science/publications/)
* [SDSS-IV Publications](https://www.sdss4.org/science/publications/)
* [SDSS III Publications](http://www.sdss3.org/science/publications.php)
* [SDSS Data Release Publications](https://www.sdss4.org/science/data-release-publications/)
* [SDSS Technical Publications](https://www.sdss4.org/science/technical_publications/)
* [Image Gallery](https://www.sdss4.org/science/image-gallery/)
* [SDSS Classic Gallery](http://classic.sdss.org/gallery/)

##### **Explore**

* [Data Release 17](/dr17/)
* [DR17 Data Access](/dr17/data_access/)
* [DR17 Scope](/dr17/scope/)
* [DR17 Tutorials](/dr17/tutorials/)

##### **Learn**

* [Surveys](/surveys/)
* [Instruments](/instruments/)
* [Education](/education/)
* [Results & Science](/science/)

##### **About**

* [How to Cite SDSS](/collaboration/citing-sdss/)
* [Image Use Policy](/collaboration/#image-use)
* [Publication Policy](/collaboration/#publication-policy)
* [Contact Us](/contact/)

##### SDSS is supported by

[![Alfred P. Sloan Foundation logo](/wp-content/uploads/2014/06/sloan.png)](https://www.sloan.org)

[![US Department of Energy logo](/wp-content/uploads/2014/06/US-DeptOfEnergy-Seal.svg_.png)](https://www.energy.gov)

Funding for SDSS is provided by the Alfred P. Sloan Foundation, the Participating Institutions, and the U.S. Department of Energy Office of Science.
