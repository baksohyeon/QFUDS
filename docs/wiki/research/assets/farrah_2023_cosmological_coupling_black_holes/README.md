---
doc_id: asset_farrah_2023_cosmological_coupling_black_holes
title: "Farrah 2023 Cosmological Coupling Black-Hole Assets"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - lit_farrah_2023_cosmological_coupling_black_holes
  - audit_2026_06_10_black_hole_data_product_audit
next_gate: inspect Markdown conversion or digitize figures if Farrah 2023 is reused as a source-history comparator
last_updated: 2026-06-17
---

# Farrah 2023 Cosmological Coupling Black-Hole Assets

Local access copies for "Observational evidence for cosmological coupling of
black holes and its implications for an astrophysical source of dark energy" by
Duncan Farrah et al. (2023).

Source URL: <https://arxiv.org/abs/2302.07878>

## Asset Manifest

```text
source/paper_arxiv_2302.07878.pdf
source/arxiv_source_2302.07878.tar
source/extracted/
digitization/paper_arxiv_2302.07878.md
figures/extracted/
```

Asset type: arXiv PDF, arXiv source bundle, extracted TeX/figure assets.

Current asset state: `asset_extracted_not_digitized`; PDF converted to
Markdown, but numerical figure/table digitization not done.

Extraction potential: `figure_digitization_possible`,
`source_tex_parse_possible`.

## Why This Asset Matters

Farrah 2023 is a primary comparator for black-hole cosmological coupling. It can
constrain whether a future black-hole source lane is merely reusing an existing
CCBH source idea.

This asset is not QFUDS evidence and does not define a QFUDS-ready `rho_BH(a)`
or `Q^nu`.

## Dependent Audit

[2026-06-10 Black-Hole Data Product Audit](../../../governance/source_x/conclusions/040_black_hole_data_product_audit.md)
depends on this asset cache for source-level inspection before repeating any
Farrah 2023 product-absence claim.

## Known Limitations

The source bundle exposes TeX and figure assets, and the PDF now has a
[MarkItDown](https://github.com/microsoft/markitdown) Markdown conversion for text inspection, plus a [PageIndex](https://github.com/VectifyAI/PageIndex) hierarchical
structure parse (`source_text_parse`,
[pageindex_structure.md](digitization/pageindex_structure.md)) for section/page
targeting. Neither is numerical digitization; the asset state
remains `asset_extracted_not_digitized`. No machine-readable `rho_BH(a)`,
covariance, posterior sample, or QFUDS normalization product was identified in
the extracted source tree.

The [MarkItDown](https://github.com/microsoft/markitdown) conversion includes six local figure references. Rendered PNGs
live under `figures/extracted/`, with source links back to `source/extracted/`.
