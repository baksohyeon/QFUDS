---
doc_id: asset_gwtc4_population_release
title: "GWTC-4.0 Population Release Assets"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_black_hole_data_product_audit
next_gate: selected population-product extraction if an updated LVK merger-population proxy is needed
last_updated: 2026-06-11
---

# GWTC-4.0 Population Release Assets

Local access copies for the Zenodo data release "GWTC-4.0: Population
Properties of Merging Compact Binaries".

Source URL: <https://zenodo.org/records/16911563>

## Asset Manifest

```text
source/zenodo_record_16911563.json
source/zenodo_README.txt
source/o4a_event_list.tar
source/download_gwtc3_data.py
source/popsummary_tutorial.ipynb
source/figures.tar
source/figure_scripts.tar
source/extracted/
figures/extracted/
```

Asset type: Zenodo record metadata, release README asset, event-list tarball,
figure tarball, figure-script tarball, tutorial notebook, extracted event/figure
assets, rendered PNG figure mirror.

Current asset state: `asset_extracted_not_digitized`.

Extraction potential: `zenodo_data_available`, `direct_table`,
`figure_digitization_possible`, `code_reproduction_possible`.

## Why This Asset Matters

GWTC-4.0 population products are the newest LVK population-products hit in this
audit. They can support merger-population or mass-distribution checks, but they
do not directly provide a QFUDS-ready cosmic SMBH `rho_BH(a)` source history.

## Dependent Audit

[2026-06-10 Black-Hole Data Product Audit](../../../governance/source_x/conclusions/040_black_hole_data_product_audit.md)
depends on this cache before using updated LVK merger-population products.

## Known Limitations

Large analysis tarballs were not downloaded. This pass cached and extracted the
README, event list, tutorial, figure assets, and figure scripts only.
Twenty-two extracted figure PDFs were rendered to PNG under
`figures/extracted/` for local Markdown/image inspection.

A MarkItDown markdown document of this release (release notes, event lists, the
converted popsummary tutorial, and an inventory of all 22 figures with working
image links) is available at [digitization/gwtc4_population_release.md](digitization/gwtc4_population_release.md).
