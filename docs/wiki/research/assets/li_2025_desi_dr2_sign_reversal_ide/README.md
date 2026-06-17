---
doc_id: asset_li_2025_desi_dr2_sign_reversal_ide
title: "Li and Zhang 2025 DESI DR2 Sign-Reversal IDE Assets"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - lit_li_2025_desi_dr2_sign_reversal_ide
next_gate: Li 2025 timing-overlap digitization or author-data request
last_updated: 2026-06-17
---

# Li and Zhang 2025 DESI DR2 Sign-Reversal IDE Assets

Local access copies for Li and Zhang 2025, arXiv:2506.18477.

These files are research assets only. They do not create a new experiment,
change Exp006 conclusions, or change roadmap status.

## Files

- `source/paper_arxiv_2506.18477v2.pdf` - full arXiv paper PDF.
- `source/arxiv_source_2506.18477v2.tar.gz` - downloaded arXiv source bundle.
- `source/extracted/` - extracted arXiv source bundle contents, copied
  file-for-file from the downloaded source package.
- `digitization/` - Markdown conversion, [PageIndex](https://github.com/VectifyAI/PageIndex) hierarchical structure parse
  (`pageindex_structure.md`, `source_text_parse`), and future numeric
  digitization products.
- `figures/extracted/` - rendered PNG mirror of source figure PDFs for
  figure-level inspection and Markdown image references.

The top-level directory is for human entrypoints only. The `source/` directory is
the canonical location for arXiv source-package materials:

- `source/extracted/fig_reconstruct.pdf` - main reconstructed beta(z) figure.
- `source/extracted/fig_pc.pdf` - PCA eigenvector figure.
- `source/extracted/fig_evals.pdf` - PCA inverse-eigenvalue figure.
- `source/extracted/fig_bin30.pdf` - 30-bin robustness figure.
- `source/extracted/fig_zmax.pdf` - extended-redshift robustness figure.
- `source/extracted/fig_mock_lcdm.pdf` - synthetic LCDM validation figure.
- `source/extracted/fig_bayes_data.pdf` - Bayes-factor figure.

## Timing-Overlap Relevance

The highest-priority files for a future timing-overlap digitization protocol are:

1. `source/extracted/fig_reconstruct.pdf`
2. `source/extracted/fig_pc.pdf`
3. `source/extracted/fig_evals.pdf`

The source bundle still does not contain machine-readable beta(z), covariance,
posterior-chain, or PCA-array products. It contains manuscript source, style and
bibliography files, and figure PDFs.
