---
doc_id: asset_eboss_dr16_lya_bao_2020_digitization_index
title: eBOSS DR16 Lyman-alpha BAO Digitization Assets
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_eboss_dr16_lya_bao_2020
next_gate: manual structured extraction before numerical reuse
last_updated: 2026-06-17
---

# eBOSS DR16 Lyman-alpha BAO Digitization Assets

This folder stores derived inspection products for the eBOSS DR16 Lyman-alpha
BAO asset.

The cached SDSS product is a data-release asset, not a paper-PDF asset. This
pass therefore used source-file inspection, [MarkItDown](https://github.com/microsoft/markitdown) conversion of the
upstream README, and Markdown assembly from grid files, not [PageIndex](https://github.com/VectifyAI/PageIndex) PDF
parsing.

The resulting Markdown is `source_text_parse` only. It is not numerical
digitization, not a likelihood implementation, and not QFUDS evidence.

## Records

- [eBOSS DR16 Lyman-alpha BAO likelihood-release parse](eboss_dr16_lya_bao_likelihood_release.md)
  - source-file inventory, grid semantics, grid ranges, maxima, and open
  source-product choices.
- [MarkItDown BAO-only README conversion](markitdown_BAO-only_README.md) -
  low-fidelity Markdown conversion of the cached upstream README.
- [MarkItDown SDSS final BAO/RSD page conversion](markitdown_sdss_final_bao_rsd_measurements.md)
  - low-fidelity Markdown conversion of the SDSS source page that points to
  likelihoods and covariance matrices.
- [MarkItDown SDSS BAO-only directory conversion](markitdown_sdss_bao_only_directory.md)
  - low-fidelity Markdown conversion of the SDSS SVN BAO-only directory.
- [MarkItDown SDSS data-vector/covariance directory conversion](markitdown_sdss_dataveccov_lya_forest_directory.md)
  - low-fidelity Markdown conversion of the SDSS SVN raw Lyman-alpha directory.
- [MarkItDown data-vector/covariance README conversion](markitdown_dataveccov_lya_forest_README.md)
  - low-fidelity Markdown conversion of the cached raw-product README.
- [MarkItDown arXiv page conversion](markitdown_arxiv_2007.08995.md) -
  low-fidelity Markdown conversion of the source abstract page.
