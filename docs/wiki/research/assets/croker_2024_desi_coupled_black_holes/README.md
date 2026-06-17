---
doc_id: asset_croker_2024_desi_coupled_black_holes
title: "Croker 2024 DESI Coupled Black-Hole Assets"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - lit_croker_2024_desi_coupled_black_holes
  - audit_2026_06_10_black_hole_data_product_audit
next_gate: inspect Markdown conversion, extract tables, or digitize figures if Croker 2024 is reused as a DESI CCBH comparator
last_updated: 2026-06-17
---

# Croker 2024 DESI Coupled Black-Hole Assets

Local access copies for "DESI Dark Energy Time Evolution is Recovered by
Cosmologically Coupled Black Holes" by Kevin S. Croker et al. (2024).

Source URL: <https://arxiv.org/abs/2405.12282>

## Asset Manifest

```text
source/paper_arxiv_2405.12282.pdf
source/arxiv_html_2405.12282.html
source/arxiv_source_2405.12282.tar
source/extracted/
digitization/paper_arxiv_2405.12282.md
figures/extracted/
```

Asset type: arXiv PDF, arXiv HTML, arXiv source bundle, extracted TeX/figure
assets.

Current asset state: `asset_extracted_not_digitized`; PDF converted to
Markdown, but numerical figure/table digitization not done.

Extraction potential: `direct_table`, `figure_digitization_possible`,
`source_tex_parse_possible`.

## Why This Asset Matters

Croker 2024 is a DESI-era CCBH comparator. It contains paper-level tables and
figures relevant to known-model reduction pressure on any black-hole-sourced
dark-energy lane.

This asset is not QFUDS evidence and does not define a QFUDS-ready `rho_BH(a)`
or `Q^nu`.

## Dependent Audit

[2026-06-10 Black-Hole Data Product Audit](../../../governance/source_x/conclusions/040_black_hole_data_product_audit.md)
depends on this asset cache for table/figure/source inspection.

## Known Limitations

The extracted source includes TeX and figure PDFs, and the PDF now has a
[MarkItDown](https://github.com/microsoft/markitdown) Markdown conversion for text inspection, plus a [PageIndex](https://github.com/VectifyAI/PageIndex) hierarchical
structure parse (`source_text_parse`,
[pageindex_structure.md](digitization/pageindex_structure.md)) for section/page
targeting. Neither is numerical digitization; the asset state
remains `asset_extracted_not_digitized`. It cites DESI BAO data and external
BAO/cosmology inputs, but no paper-specific public posterior chain or
QFUDS-normalized source-history product was identified in this cache pass.

The [MarkItDown](https://github.com/microsoft/markitdown) conversion includes three local figure references. Rendered PNGs
live under `figures/extracted/`, with source links back to `source/extracted/`.
