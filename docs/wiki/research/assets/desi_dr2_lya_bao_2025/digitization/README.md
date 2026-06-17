---
doc_id: asset_desi_dr2_lya_bao_2025_digitization_index
title: DESI DR2 Lyman-alpha BAO Digitization Assets
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_desi_dr2_lya_bao_2025
next_gate: manual structured extraction before numerical reuse
last_updated: 2026-06-17
---

# DESI DR2 Lyman-alpha BAO Digitization Assets

This folder stores derived inspection products for the DESI DR2 Lyman-alpha BAO
asset.

The cached Zenodo product is a data-release asset, not a paper-PDF asset. This
pass therefore used source-file inspection, [MarkItDown](https://github.com/microsoft/markitdown) conversion of the
upstream README, and Markdown assembly from tabular files, not [PageIndex](https://github.com/VectifyAI/PageIndex) PDF
parsing.

The resulting Markdown is `source_text_parse` only. It is not numerical
digitization, not a likelihood implementation, and not QFUDS evidence.

## Records

- [DESI DR2 Lyman-alpha BAO data-release parse](desi_dr2_lya_bao_data_release.md)
  - source-file inventory, figure-product map, compact `D_M/r_d` and `D_H/r_d`
  source table, and open source-product choices.
- [DESI DR2 archive [MarkItDown](https://github.com/microsoft/markitdown) index](desi_dr2_lya_bao_archive_markitdown_index.md)
  - [MarkItDown](https://github.com/microsoft/markitdown) conversion index for text, CSV, DAT, and JSON members extracted
  from `desi-dr2-lya-bao-figdata.tgz`.
- [MarkItDown upstream README conversion](markitdown_upstream_README.md) -
  low-fidelity Markdown conversion of the cached upstream README.
- [MarkItDown Zenodo record conversion](markitdown_zenodo_record_15690869.md)
  - low-fidelity Markdown conversion of the source record page.
- [MarkItDown arXiv page conversion](markitdown_arxiv_2503.14739.md) -
  low-fidelity Markdown conversion of the source abstract page.
