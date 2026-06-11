---
doc_id: asset_gwtc3_pe_release_record_document
title: "GWTC-3 Parameter-Estimation Release — Zenodo Record Document"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_gwtc3_pe_release_digitization_index
next_gate: selected HDF5 or contour recovery only if event-level PE samples become necessary
last_updated: 2026-06-11
---

# GWTC-3 Parameter-Estimation Release — Zenodo Record Document

Markdown rendering of the Zenodo record metadata for this data release, produced
because the asset has no paper/text/HTML source to transcribe — only the Zenodo
record JSON (`source/zenodo_record_8177023.json`). The HTML description below was
converted with [MarkItDown](https://github.com/microsoft/markitdown); the file
manifest is rendered from the record JSON. Quality: `source_text_parse`.

- **Title:** GWTC-3: Compact Binary Coalescences Observed by LIGO and Virgo During the Second Part of the Third Observing Run — Parameter estimation data release
- **DOI:** [10.5281/zenodo.8177023](https://doi.org/10.5281/zenodo.8177023)
- **Publication date:** 2023-10-23
- **License:** cc-by-4.0
- **Creators:** 1 (first: LIGO Scientific Collaboration and Virgo Collaboration and KAGRA Collaboration)
- **Files in record:** 76

## Description (converted from the Zenodo HTML)

This material is part of several data products associated with GWTC-3, the third Gravitational-Wave Transient Catalog from the [LIGO](https://www.ligo.org/) Scientific Collaboration, the [Virgo](https://www.virgo-gw.eu/) Collaboration, and the [KAGRA](https://gwcenter.icrr.u-tokyo.ac.jp/en/) Collaboration. For more information, see the paper ([dcc.ligo.org/LIGO-P2000318/public](https://dcc.ligo.org/LIGO-P2000318/public)), the related material linked from this page, and the GWTC-3 data release documentation ([www.gw-openscience.org/GWTC-3/](https://www.gw-openscience.org/GWTC-3/)).

**Parameter estimation data release**

This data release contains posterior samples (\*.h5) for gravitational-wave candidates from the second part of the third observing run (O3b).We provide results for the 35 candidates that have a probability of astrophysical origin of over 0.5, plus [GW200105\_162426](https://doi.org/10.3847/2041-8213/ac082e), which is a clear outlier from the noise background. There are two .h5 files per event

* Cosmologically reweighted (\*cosmo.h5)
* Not cosmologically reweighted (\*nocosmo.h5)

The cosmologically reweighted posteriors are reweighted to have a luminosity-distance prior that has a uniform merger rate in the source's comoving frame. See the [paper](http://dcc.ligo.org/LIGO-P2000318/public) appendices for further information. In addition to containing the posterior samples, the .h5 files also contain metadata about the analyses including the configuration files (which specify details such as the detector data analysed), noise power spectral densities (potentially for a superset of the detectors used in the analysis) and calibration uncertainty envelopes.

The inference of the source parameters were performed with [Bilby](https://lscsoft.docs.ligo.org/bilby/), [Parallel Bilby](https://lscsoft.docs.ligo.org/parallel_bilby/) and [RIFT](https://git.ligo.org/richard-oshaughnessy/research-projects-RIT/tree/temp-RIT-Tides). The results are formatted using [PESummary](https://lscsoft.docs.ligo.org/pesummary/).

**A note about mixed samples:** The samples provided here are produced using different waveform approximants. The Mixed label indicates that equal numbers of samples have been included from two different waveform approximants. For the binary black holes, these are IMRPhenomXPHM and SEOBNRv4PHM (for more details, see GWTC3p0PEDataReleaseExample.ipynb included in this data release and the paper). As different waveforms were analysed with different codes, there are sometimes differences in some parameters due to conventions in the codes. For example:

* As RIFT does not sample over time of coalescence as Bilby does, the RIFT time of coalescence results have a posterior distribution with a single spike, whereas the Bilby results have a distribution of peaks representing different sky positions for the source.
* There are different conventions for the range of the polarization angle (either 0 to π or 0 to 2 π). The parameter psi\_wrapped maps all results to the range 0 to π, should consistency be important.
* The likelihood may show small differences when different sampling rates were used for Bilby and RIFT. The log-likelihood is expected to have a relative shift between the two runs of a few nats.

Due to these differences, care must be taken when using Mixed samples, which will contain results using both codes' conventions. This should not impact the most interesting quantities, such as the masses, and so should only be rarely an issue.

A [similar parameter-estimation release has been made to accompany GWTC-2.1](https://doi.org/10.5281/zenodo.5117702) for results from the first part of the third observing run.

**Sky localization data release**

The sky localization tar file (IGWN-GWTC3p0-v2-PESkyLocalizations.tar.gz) contains candidate sky localizations corresponding to different parameter estimation configurations (.fits). Two waveforms are used for the majority of targets (IMRPhenomXPHM and SEOBNRv4PHM) and additional waveforms are used for possible neutron star--black hole mergers (see the [paper](https://dcc.ligo.org/LIGO-P2000318/public) for further information). If you do not mind which waveform, the sky localizations labelled "Mixed" include posterior samples from both waveforms used. A machine readable list (skyLocalizationFileList.csv) of sky localization files is included within the .tar.gz file for ease of use, where the Mixed results are indicated as Default=True.

**Contour data release**

The contour tar file (IGWN-GWTC3p0-v2-PEContours.tar.gz) contains the contour files used to produce Figures 8 and 9 in the [paper](http://dcc.ligo.org/LIGO-P2000318/public). The python notebook (GWTC3p0PEPlotContourData.ipynb) explains how to reproduce these figures (and an interactive version of these plots can be accessed at [gwtc3-contours.streamlit.app/](https://gwtc3-contours.streamlit.app/)).

**Python notebook**

The Python notebook (GWTC3p0PEDataReleaseExample.ipynb) explains how to read and use the posterior samples with a selection of examples.

**How to download all files from this page**

If you would like to download all files on this page, we recommend [zenodo\_get](https://gitlab.com/dvolgyes/zenodo_get):

```
pip install zenodo_get
zenodo-get RECORD_ID_OR_DOI
```

where the record ID for the most recent version of this page is 5546662 and IDs for other versions can be found in the Versions section at the side of this page.

For more general background on gravitational-wave parameter estimation, try the materials from a [GW Open Data Workshop](https://www.gw-openscience.org/workshops/) or the [guide to LIGO–Virgo data analysis](https://doi.org/10.1088/1361-6382/ab685e).

## File manifest (76 files)

| File | Size (bytes) |
| --- | --- |
| `IGWN-GWTC3p0-v2-GW191204_171526_PEDataRelease_mixed_nocosmo.h5` | 547592204 |
| `IGWN-GWTC3p0-v2-GW191216_213338_PEDataRelease_mixed_nocosmo.h5` | 786787624 |
| `IGWN-GWTC3p0-v2-GW191129_134029_PEDataRelease_mixed_nocosmo.h5` | 397827928 |
| `IGWN-GWTC3p0-v2-GW191127_050227_PEDataRelease_mixed_nocosmo.h5` | 581904576 |
| `IGWN-GWTC3p0-v2-GW200311_115853_PEDataRelease_mixed_cosmo.h5` | 275864563 |
| `IGWN-GWTC3p0-v2-GW200308_173609_PEDataRelease_mixed_cosmo.h5` | 25850600 |
| `IGWN-GWTC3p0-v2-GW200208_130117_PEDataRelease_mixed_cosmo.h5` | 106432410 |
| `IGWN-GWTC3p0-v2-GW200208_130117_PEDataRelease_mixed_nocosmo.h5` | 530596264 |
| `IGWN-GWTC3p0-v2-GW191103_012549_PEDataRelease_mixed_nocosmo.h5` | 433414064 |
| `IGWN-GWTC3p0-v2-GW200129_065458_PEDataRelease_mixed_nocosmo.h5` | 619139816 |
| `IGWN-GWTC3p0-v2-GW191126_115259_PEDataRelease_mixed_nocosmo.h5` | 431112456 |
| `IGWN-GWTC3p0-v2-GW200112_155838_PEDataRelease_mixed_nocosmo.h5` | 370862808 |
| `IGWN-GWTC3p0-v2-GW200220_061928_PEDataRelease_mixed_nocosmo.h5` | 389200016 |
| `IGWN-GWTC3p0-v2-GW200210_092254_PEDataRelease_mixed_cosmo.h5` | 216131345 |
| `IGWN-GWTC3p0-v2-GW191105_143521_PEDataRelease_mixed_nocosmo.h5` | 481764032 |
| `IGWN-GWTC3p0-v2-GW200129_065458_PEDataRelease_mixed_cosmo.h5` | 213979989 |
| `IGWN-GWTC3p0-v2-GW200224_222234_PEDataRelease_mixed_cosmo.h5` | 221122047 |
| `IGWN-GWTC3p0-v2-GW200302_015811_PEDataRelease_mixed_cosmo.h5` | 91892080 |
| `IGWN-GWTC3p0-v2-GW191215_223052_PEDataRelease_mixed_nocosmo.h5` | 130769360 |
| `IGWN-GWTC3p0-v2-GW200208_222617_PEDataRelease_mixed_nocosmo.h5` | 662275416 |
| `IGWN-GWTC3p0-v2-GW200209_085452_PEDataRelease_mixed_cosmo.h5` | 84134657 |
| `IGWN-GWTC3p0-v2-GW191126_115259_PEDataRelease_mixed_cosmo.h5` | 133959252 |
| `IGWN-GWTC3p0-v2-GW200210_092254_PEDataRelease_mixed_nocosmo.h5` | 481697144 |
| `IGWN-GWTC3p0-v2-GW200311_115853_PEDataRelease_mixed_nocosmo.h5` | 793976232 |
| `IGWN-GWTC3p0-v2-PESkyLocalizations.tar.gz` | 71637588 |
| `IGWN-GWTC3p0-v2-GW200115_042309_PEDataRelease_mixed_cosmo.h5` | 434593331 |
| `IGWN-GWTC3p0-v2-GW200306_093714_PEDataRelease_mixed_nocosmo.h5` | 321983216 |
| `IGWN-GWTC3p0-v2-GW200306_093714_PEDataRelease_mixed_cosmo.h5` | 71574310 |
| `IGWN-GWTC3p0-v2-GW191204_110529_PEDataRelease_mixed_nocosmo.h5` | 393188576 |
| `IGWN-GWTC3p0-v2-PEContours.tar.gz` | 162645706 |
| `IGWN-GWTC3p0-v2-GW191129_134029_PEDataRelease_mixed_cosmo.h5` | 173489025 |
| `IGWN-GWTC3p0-v2-GW200128_022011_PEDataRelease_mixed_nocosmo.h5` | 367652680 |
| `IGWN-GWTC3p0-v2-GW200224_222234_PEDataRelease_mixed_nocosmo.h5` | 824227520 |
| `IGWN-GWTC3p0-v2-GW200219_094415_PEDataRelease_mixed_nocosmo.h5` | 596647888 |
| `IGWN-GWTC3p0-v2-GW200112_155838_PEDataRelease_mixed_cosmo.h5` | 138976202 |
| `IGWN-GWTC3p0-v2-GW200316_215756_PEDataRelease_mixed_cosmo.h5` | 322627943 |
| `IGWN-GWTC3p0-v2-GW191204_110529_PEDataRelease_mixed_cosmo.h5` | 93629171 |
| `IGWN-GWTC3p0-v2-GW200105_162426_PEDataRelease_mixed_nocosmo.h5` | 163637320 |
| `IGWN-GWTC3p0-v2-GW191109_010717_PEDataRelease_mixed_cosmo.h5` | 232709707 |
| `IGWN-GWTC3p0-v2-GW200220_124850_PEDataRelease_mixed_nocosmo.h5` | 266999048 |
| `GWTC3p0PEPlotContourData.ipynb` | 718612 |
| `IGWN-GWTC3p0-v2-GW191216_213338_PEDataRelease_mixed_cosmo.h5` | 499848402 |
| `IGWN-GWTC3p0-v2-GW191113_071753_PEDataRelease_mixed_cosmo.h5` | 155767527 |
| `IGWN-GWTC3p0-v2-GW200202_154313_PEDataRelease_mixed_nocosmo.h5` | 574649168 |
| `IGWN-GWTC3p0-v2-GW200128_022011_PEDataRelease_mixed_cosmo.h5` | 60018120 |
| `IGWN-GWTC3p0-v2-GW191103_012549_PEDataRelease_mixed_cosmo.h5` | 54447816 |
| `IGWN-GWTC3p0-v2-GW191127_050227_PEDataRelease_mixed_cosmo.h5` | 75647260 |
| `IGWN-GWTC3p0-v2-GW191219_163120_PEDataRelease_mixed_cosmo.h5` | 349463547 |
| `IGWN-GWTC3p0-v2-GW200302_015811_PEDataRelease_mixed_nocosmo.h5` | 279341800 |
| `IGWN-GWTC3p0-v2-GW200322_091133_PEDataRelease_mixed_nocosmo.h5` | 402501336 |
| `IGWN-GWTC3p0-v2-GW200322_091133_PEDataRelease_mixed_cosmo.h5` | 21425500 |
| `IGWN-GWTC3p0-v2-GW191109_010717_PEDataRelease_mixed_nocosmo.h5` | 673672600 |
| `IGWN-GWTC3p0-v2-GW191113_071753_PEDataRelease_mixed_nocosmo.h5` | 437698792 |
| `IGWN-GWTC3p0-v2-GW191230_180458_PEDataRelease_mixed_nocosmo.h5` | 450101024 |
| `IGWN-GWTC3p0-v2-GW200209_085452_PEDataRelease_mixed_nocosmo.h5` | 537095528 |
| `IGWN-GWTC3p0-v2-GW200219_094415_PEDataRelease_mixed_cosmo.h5` | 79836429 |
| `IGWN-GWTC3p0-v2-GW200202_154313_PEDataRelease_mixed_cosmo.h5` | 336376074 |
| `IGWN-GWTC3p0-v2-GW200225_060421_PEDataRelease_mixed_nocosmo.h5` | 514369184 |
| `IGWN-GWTC3p0-v2-GW200115_042309_PEDataRelease_mixed_nocosmo.h5` | 624864792 |
| `IGWN-GWTC3p0-v2-GW191105_143521_PEDataRelease_mixed_cosmo.h5` | 175259650 |
| `IGWN-GWTC3p0-v2-GW200105_162426_PEDataRelease_mixed_cosmo.h5` | 235674408 |
| `IGWN-GWTC3p0-v2-GW191230_180458_PEDataRelease_mixed_cosmo.h5` | 61745327 |
| `IGWN-GWTC3p0-v2-GW191222_033537_PEDataRelease_mixed_cosmo.h5` | 60856121 |
| `IGWN-GWTC3p0-v2-GW200220_124850_PEDataRelease_mixed_cosmo.h5` | 34263899 |
| `IGWN-GWTC3p0-v2-GW191219_163120_PEDataRelease_mixed_nocosmo.h5` | 599422376 |
| `IGWN-GWTC3p0-v2-GW200220_061928_PEDataRelease_mixed_cosmo.h5` | 25440384 |
| `IGWN-GWTC3p0-v2-GW200308_173609_PEDataRelease_mixed_nocosmo.h5` | 408844352 |
| `GWTC3p0PEDataReleaseExample.ipynb` | 3604815 |
| `IGWN-GWTC3p0-v2-GW191215_223052_PEDataRelease_mixed_cosmo.h5` | 28148762 |
| `IGWN-GWTC3p0-v2-GW200216_220804_PEDataRelease_mixed_nocosmo.h5` | 452240608 |
| `IGWN-GWTC3p0-v2-GW191204_171526_PEDataRelease_mixed_cosmo.h5` | 268709247 |
| `IGWN-GWTC3p0-v2-GW200225_060421_PEDataRelease_mixed_cosmo.h5` | 183024128 |
| `IGWN-GWTC3p0-v2-GW200316_215756_PEDataRelease_mixed_nocosmo.h5` | 837534464 |
| `IGWN-GWTC3p0-v2-GW200208_222617_PEDataRelease_mixed_cosmo.h5` | 69591983 |
| `IGWN-GWTC3p0-v2-GW191222_033537_PEDataRelease_mixed_nocosmo.h5` | 365937320 |
| `IGWN-GWTC3p0-v2-GW200216_220804_PEDataRelease_mixed_cosmo.h5` | 52323503 |
