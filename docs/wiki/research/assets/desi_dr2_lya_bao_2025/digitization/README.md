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
last_updated: 2026-06-12
---

# DESI DR2 Lyman-alpha BAO Digitization Assets

This folder stores derived inspection products for the DESI DR2 Lyman-alpha BAO
asset.

The cached Zenodo product is a data-release asset, not a paper-PDF asset. This
pass therefore used source-file inspection, MarkItDown conversion of the
upstream README, and Markdown assembly from tabular files, not PageIndex PDF
parsing.

The resulting Markdown is `source_text_parse` only. It is not numerical
digitization, not a likelihood implementation, and not QFUDS evidence.

## Records

- [DESI DR2 Lyman-alpha BAO data-release parse](desi_dr2_lya_bao_data_release.md)
  - source-file inventory, figure-product map, compact `D_M/r_d` and `D_H/r_d`
  source table, and open source-product choices.
- [MarkItDown upstream README conversion](markitdown_upstream_README.md) -
  low-fidelity Markdown conversion of the cached upstream README.
