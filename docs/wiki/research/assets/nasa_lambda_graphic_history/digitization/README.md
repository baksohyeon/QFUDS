---
doc_id: asset_nasa_lambda_graphic_history_digitization_index
title: NASA LAMBDA Graphic History Digitization Assets
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_nasa_lambda_graphic_history
next_gate: numeric plot digitization only if an audit needs exact plotted values
last_updated: 2026-06-17
---

# NASA LAMBDA Graphic History Digitization Assets

This folder stores derived inspection products for the NASA LAMBDA Graphic
History cache.

The source is a NASA HTML page family, not a paper PDF or data-release archive.
This pass therefore used direct HTML caching, link extraction, linked asset
download, and table extraction from `data_ref.html`.

## Records

- [Data reference matrix](data_reference_matrix.csv) - 57-row source-derived
  table mapping LAMBDA data-reference labels to the parameter-history plots they
  feed.
- [Link inventory](link_inventory.tsv) - 106 page-level link records resolving
  to 90 unique downloaded figure/vector URLs.
- [Download queue](download_queue.tsv) - unique URL and local-path map used for
  the crawl.

## Quality State

- `data_reference_matrix.csv`: `manual_structured_extract` of a source HTML
  table.
- `link_inventory.tsv`: asset-provenance inventory.
- Parameter-history plots: `asset_extracted_not_digitized`; no numerical plot
  points have been digitized.

## Use Restrictions

The extracted matrix is useful for source coverage and citation tracing. It
must not be treated as a numerical cosmological-parameter dataset or as QFUDS
evidence.
