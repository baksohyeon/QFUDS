---
doc_id: asset_gwtc3_population_release
title: "GWTC-3 Population Release Assets"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - lit_abbott_2023_gwtc3_population_merging_compact_binaries
  - audit_2026_06_10_black_hole_data_product_audit
next_gate: selected population-product extraction if a merger-population proxy is needed
last_updated: 2026-07-06
---

# GWTC-3 Population Release Assets

Local access copies for the Zenodo data release "The population of merging
compact binaries inferred using gravitational waves through GWTC-3".

Source URL: <https://zenodo.org/records/11254021>

## Asset Manifest

```text
source/zenodo_record_11254021.json
source/zenodo_README.txt
source/zenodo_README_GWTC-3-population-data.txt
source/GWTC-3-population_py_requirements.txt
source/table_data.tar.gz
source/paper_figures.tar.gz
source/extracted/
figures/extracted/
```

Asset type: Zenodo record metadata, release README assets, table-data tarball,
paper-figure tarball, extracted table/figure assets, rendered PNG figure
mirror.

Current asset state: `asset_extracted_not_digitized`.

Extraction potential: `zenodo_data_available`, `direct_table`,
`figure_digitization_possible`, `code_reproduction_possible`.

## Why This Asset Matters

GWTC-3 population products can support merger-population or mass-distribution
checks. They do not directly provide a cosmic SMBH `rho_BH(a)` source history
or QFUDS normalization route.

## Dependent Audit

[2026-06-10 Black-Hole Data Product Audit](../../investigations/source_x/conclusions/040_black_hole_data_product_audit.md)
depends on this cache for distinguishing LVK reproducible products from
QFUDS-ready Lane A source histories.

## Known Limitations

Large analysis tarballs were not downloaded. This pass cached and extracted
small table/figure assets and manifest files only. Thirty-four extracted figure
PDFs were rendered to PNG under `figures/extracted/` for local Markdown/image
inspection.

A [MarkItDown](https://github.com/microsoft/markitdown) markdown document of this release (release notes, the six
numerical tables, and an inventory of all 34 figures with working image links) is
available at [digitization/gwtc3_population_release.md](digitization/gwtc3_population_release.md).
