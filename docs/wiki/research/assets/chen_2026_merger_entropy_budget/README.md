---
doc_id: asset_chen_2026_merger_entropy_budget
title: "Chen Jani Kephart 2026 Merger Entropy Assets"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_black_hole_data_product_audit
next_gate: inspect Markdown conversion or digitize figure/table products before entropy-history classification
last_updated: 2026-06-17
---

# Chen Jani Kephart 2026 Merger Entropy Assets

Local access copies for "Cosmological Budget of Entropy from Merging Black
Holes" by Chen, Jani, and Kephart (2026).

Source URL: <https://arxiv.org/abs/2601.13621>

## Asset Manifest

```text
source/paper_arxiv_2601.13621.pdf
source/arxiv_html_2601.13621.html
source/arxiv_source_2601.13621.tar
source/extracted/
digitization/paper_arxiv_2601.13621.md
figures/extracted/
```

Asset type: arXiv PDF, arXiv HTML, arXiv source bundle, extracted TeX/figure
assets.

Current asset state: `asset_extracted_not_digitized`; PDF converted to
Markdown, but entropy-history figure/table digitization not done.

Extraction potential: `direct_table`, `figure_digitization_possible`,
`source_tex_parse_possible`.

## Why This Asset Matters

Chen, Jani, and Kephart 2026 is the strongest Lane B hit for redshift-shaped
merger-generated black-hole entropy. The extracted source contains figure PNGs
and TeX text for entropy budget and redshift-history discussion.

This asset is not QFUDS evidence and does not define a QFUDS-ready `S_BH(a)`,
`dS_BH/dln(a)`, entropy-to-energy conversion law, or `Q^nu`.

## Dependent Audit

[2026-06-10 Black-Hole Data Product Audit](../../../governance/source_x/conclusions/040_black_hole_data_product_audit.md)
depends on this asset cache before calling the entropy-history product absent.

## Known Limitations

The source bundle contains TeX and figure PNGs, plus arXiv build metadata, and
the PDF now has a [MarkItDown](https://github.com/microsoft/markitdown) Markdown conversion for text inspection, plus a
[PageIndex](https://github.com/VectifyAI/PageIndex) hierarchical structure parse (`source_text_parse`,
[pageindex_structure.md](digitization/pageindex_structure.md)) for section/page
targeting. Neither is
numerical digitization; the asset state remains `asset_extracted_not_digitized`.
No standalone machine-readable entropy-history table, posterior sample, or
covariance product was identified in the extracted source tree.

The [MarkItDown](https://github.com/microsoft/markitdown) conversion includes seven local figure references. Rendered PNGs
live under `figures/extracted/`, with source links back to `source/extracted/`.
