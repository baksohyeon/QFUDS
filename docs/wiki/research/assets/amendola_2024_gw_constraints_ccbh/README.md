---
doc_id: asset_amendola_2024_gw_constraints_ccbh
title: "Amendola 2024 GW Constraint CCBH Assets"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - lit_amendola_2024_gw_constraints_ccbh
  - audit_2026_06_10_black_hole_data_product_audit
next_gate: code checkout or table extraction if CCBH constraint reproduction is needed
last_updated: 2026-07-06
---

# Amendola 2024 GW Constraint CCBH Assets

Local access copies for "Constraints on cosmologically coupled black holes from
gravitational wave observations and minimal formation mass" by Luca Amendola,
Davi C. Rodrigues, Sumit Kumar, and Miguel Quartin (2024).

Source URL: <https://arxiv.org/abs/2307.02474>

## Asset Manifest

```text
source/paper_arxiv_2307.02474.pdf
source/arxiv_html_2307.02474.html
source/arxiv_source_2307.02474.tar
source/github_itpamendola_CCBH-direct.json
source/github_itpamendola_CCBH-direct_README.txt
source/github_davi-rodrigues_CCBH-Numerics.json
source/github_davi-rodrigues_CCBH-Numerics_README.txt
source/extracted/
digitization/paper_arxiv_2307.02474.md
figures/extracted/
```

Asset type: arXiv PDF, arXiv HTML, arXiv source bundle, extracted TeX/figure
assets, GitHub repository metadata, GitHub README snapshots.

Current asset state: `asset_extracted_not_digitized`; PDF converted to
Markdown, but code reproduction and numerical table extraction not done.

Extraction potential: `code_reproduction_possible`, `direct_table`,
`figure_digitization_possible`, `source_tex_parse_possible`.

## Why This Asset Matters

Amendola 2024 is the strongest code-route comparator for gravitational-wave
constraints on CCBH-like assumptions. Its paper states that data are available
in the article, online supplementary table, and the two listed code
repositories.

This asset is not QFUDS evidence and does not define a QFUDS-ready `rho_BH(a)`
or `Q^nu`.

## Dependent Audit

[2026-06-10 Black-Hole Data Product Audit](../../investigations/source_x/conclusions/040_black_hole_data_product_audit.md)
depends on this asset cache for distinguishing code-reproducible CCBH
constraints from QFUDS-ready source products.

## Known Limitations

The PDF now has a [MarkItDown](https://github.com/microsoft/markitdown) Markdown conversion for text inspection, plus a
[PageIndex](https://github.com/VectifyAI/PageIndex) hierarchical structure parse (`source_text_parse`,
[pageindex_structure.md](digitization/pageindex_structure.md)) for section/page
targeting. Neither is
numerical digitization; the asset state remains `asset_extracted_not_digitized`.
The GitHub repositories were not cloned in this pass. Repository metadata and README
snapshots were cached only. Reproducing constraints requires a separate code
checkout and LVK input setup.

The [MarkItDown](https://github.com/microsoft/markitdown) conversion includes twenty local figure references. Rendered PNGs
live under `figures/extracted/`, with source links back to `source/extracted/`.
