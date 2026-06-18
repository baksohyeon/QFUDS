---
doc_id: research_assets_index
title: Research Assets
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - research_cache_index
next_gate: none; repository asset-cache routing only
last_updated: 2026-06-18
---

# Research Assets

This folder stores repository-cached research assets. Asset records do not create
QFUDS evidence, change roadmap status, or promote a paper into extracted
evidence status by themselves.

## Operational Authority

Agent workflow rules for asset discovery, caching, extraction, digitization,
layout, and state classification live in
[Research Asset and Product Workflow](../../../../.agent/workflows/research-asset-product-workflow.md).

This README is an asset-cache index and local layout description only. If this
file and the `.agent/` workflow disagree, the `.agent/` workflow wins and this
README should be corrected.

## Current Layout

```text
docs/wiki/research/assets/
  <paper_or_release_key>/
    source/
    figures/
    digitization/
```

## Asset Manifests

Each paper, release, or product-family directory has an asset README manifest.
The required fields and handling rules are defined only in the
[Research Asset and Product Workflow](../../../../.agent/workflows/research-asset-product-workflow.md).

Current product-family caches include:

- [NASA LAMBDA Graphic History](nasa_lambda_graphic_history/README.md) -
  cached 20-page NASA LAMBDA Graphic History web family, linked figure/vector
  products, and the source-derived data-reference matrix. Interpretation and
  use restrictions live in the
  [baseline reference chain](../investigations/baseline_reference/README.md).
- [Escamilla 2023 Interacting Dark Energy Kernel](escamilla_2023_interacting_dark_energy_kernel/README.md) -
  cached arXiv PDF/source assets for Source-X IV/IDE equation extraction.
- [Martinelli 2019 Interacting Vacuum Geodesic CDM](martinelli_2019_interacting_vacuum_geodesic_cdm/README.md) -
  cached arXiv PDF/source assets for Source-X IV/geodesic-CDM equation extraction.
- [Hogg 2020 Vacuum Geodesic CDM Interaction](hogg_2020_vacuum_geodesic_cdm_interaction/README.md) -
  cached arXiv PDF/source assets for Source-X IV/geodesic-CDM same-family extraction.
