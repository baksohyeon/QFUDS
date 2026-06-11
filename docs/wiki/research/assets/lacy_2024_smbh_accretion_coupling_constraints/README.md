---
doc_id: asset_lacy_2024_smbh_accretion_coupling_constraints
title: "Lacy 2024 SMBH Accretion Coupling Assets"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - lit_lacy_2024_smbh_accretion_coupling_constraints
  - audit_2026_06_10_black_hole_data_product_audit
next_gate: inspect Markdown conversion or extract figure/table values if Lacy 2024 is reused as an accretion-history constraint
last_updated: 2026-06-11
---

# Lacy 2024 SMBH Accretion Coupling Assets

Local access copies for "Constraints on cosmological coupling from the accretion
history of supermassive black holes" by Mark Lacy, Athena Engholm, Duncan
Farrah, and Kiana Ejercito (2024).

Source URL: <https://arxiv.org/abs/2312.12344>

## Asset Manifest

```text
source/paper_arxiv_2312.12344.pdf
source/arxiv_html_2312.12344.html
source/arxiv_source_2312.12344.tar
source/extracted/
digitization/paper_arxiv_2312.12344.md
figures/extracted/
```

Asset type: arXiv PDF, arXiv HTML, arXiv source bundle, extracted TeX/figure
assets.

Current asset state: `asset_extracted_not_digitized`; PDF converted to
Markdown, but numerical figure/table digitization not done.

Extraction potential: `direct_table`, `figure_digitization_possible`,
`source_tex_parse_possible`.

## Why This Asset Matters

Lacy 2024 constrains cosmological coupling from SMBH accretion history. It is a
constraint comparator for black-hole mass-growth lanes.

This asset is not QFUDS evidence and does not define a QFUDS-ready `rho_BH(a)`
or `Q^nu`.

## Dependent Audit

[2026-06-10 Black-Hole Data Product Audit](../../../governance/source_x/conclusions/040_black_hole_data_product_audit.md)
depends on this asset cache before treating Lacy 2024 as only a qualitative
constraint.

## Known Limitations

The extracted source contains TeX and figure images, and the PDF now has a
MarkItDown Markdown conversion for text inspection, plus a PageIndex hierarchical
structure parse (`source_text_parse`,
[pageindex_structure.md](digitization/pageindex_structure.md)) for section/page
targeting. Neither is numerical digitization; the asset state
remains `asset_extracted_not_digitized`. It does not include a machine-readable
SMBH accretion-history table, posterior chain, covariance matrix, or QFUDS
normalization route.

The MarkItDown conversion includes two local figure references. Rendered PNGs
live under `figures/extracted/`, with source links back to `source/extracted/`.
