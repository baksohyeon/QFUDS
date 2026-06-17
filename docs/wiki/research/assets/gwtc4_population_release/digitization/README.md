---
doc_id: asset_gwtc4_pop_release_digitization_index
title: GWTC-4.0 Population Release Digitization Assets
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_gwtc4_population_release
next_gate: targeted manual extraction before numerical reuse
last_updated: 2026-06-17
---

# GWTC-4.0 Population Release Digitization Assets

This folder stores derived inspection products for the GWTC-4.0 population data
release (Zenodo 16911563). This asset is a data release rather than a single
paper PDF, so there is no manuscript to transcribe; instead the release notes,
event lists, tutorial notebook, and figures were converted to Markdown with
[MarkItDown](https://github.com/microsoft/markitdown).

All converted outputs are `source_text_parse` quality: faithful conversions of
the release text and notebook, machine-extracted and not line-for-line verified.

## Records

- [Data release document](gwtc4_population_release.md) - main document: release
  overview, the two event lists (BBH-only and full-spectrum) as tables, and an
  inventory of all 22 paper figures with working image links to the PNG mirrors
  under `../figures/extracted/`.
- [Release notes (converted)](zenodo_README.md) - [MarkItDown](https://github.com/microsoft/markitdown) conversion of
  `source/zenodo_README.txt`.
- [popsummary tutorial (converted)](popsummary_tutorial.md) - [MarkItDown](https://github.com/microsoft/markitdown)
  conversion of `source/popsummary_tutorial.ipynb`.
