---
doc_id: asset_gwtc3_parameter_estimation_release
title: "GWTC-3 Parameter-Estimation Release Manifest"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_black_hole_data_product_audit
next_gate: selected HDF5 or contour recovery only if event-level PE samples become necessary
last_updated: 2026-07-06
---

# GWTC-3 Parameter-Estimation Release Manifest

Local manifest for the Zenodo GWTC-3 parameter-estimation data release.

Source URL: <https://zenodo.org/records/8177023>

## Asset Manifest

```text
source/zenodo_record_8177023.json
```

Asset type: Zenodo record metadata and file manifest.

Current asset state: `asset_cached`.

Extraction potential: `zenodo_data_available`, `code_reproduction_possible`.

## Why This Asset Matters

GWTC-3 parameter-estimation HDF5 products can support event-level posterior
work if a later analysis needs specific LVK samples.

The manifest does not by itself provide a QFUDS-ready `rho_BH(a)`,
`S_BH(a)`, or `Q^nu`.

## Dependent Audit

[2026-06-10 Black-Hole Data Product Audit](../../investigations/source_x/conclusions/040_black_hole_data_product_audit.md)
uses this manifest to record that event-level PE products exist but were not
downloaded.

## Known Limitations

The individual HDF5 products are large. They were not downloaded or extracted in
this pass.

A Markdown rendering of the Zenodo record metadata and the 76-file HDF5 manifest
is available at [digitization/zenodo_record.md](digitization/zenodo_record.md).
