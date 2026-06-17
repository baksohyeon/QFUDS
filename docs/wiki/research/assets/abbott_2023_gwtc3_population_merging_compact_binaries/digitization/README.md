---
doc_id: asset_abbott_2023_gwtc3_pop_digitization_index
title: Abbott 2023 GWTC-3 Population Digitization Assets
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_abbott_2023_gwtc3_population_merging_compact_binaries
next_gate: targeted manual extraction before numerical reuse
last_updated: 2026-06-17
---

# Abbott 2023 GWTC-3 Population Digitization Assets

This folder stores derived inspection products for the GWTC-3 population data
release (arXiv:2111.03634; Zenodo 11254021). This asset is a data release rather
than a single paper PDF, so there is no manuscript to transcribe; instead the
release text, numerical tables, and figures were converted to Markdown with
[MarkItDown](https://github.com/microsoft/markitdown).

All converted outputs are `source_text_parse` quality: faithful conversions of
the release text and CSV tables, machine-extracted and not line-for-line
verified. They must not be treated as numerical digitization or audited provenance.

## Records

- [Paper full text](paper_arxiv_2111.03634.md) - the complete published paper
  (arXiv:2111.03634v5, Phys. Rev. X 13, 011048), all 75 pages page-by-page via
  [PageIndex](https://github.com/VectifyAI/PageIndex): the full narrative (Sections I–XI) and all appendices (A–E)
  transcribed with every numbered equation verbatim. The six large numerical
  tables (I–IV, XV, XVI) and 34 figures are referenced to the data-release
  document; the reference list and author affiliations (pp. 52–75) are summarized.
- [PageIndex structure](pageindex_structure.md) - complete section-by-section
  outline with page ranges (`source_text_parse`).
- [Data release document](gwtc3_population_release.md) - release overview, the
  six numerical tables (Tables I–IV, XV, XVI) converted from the release CSVs,
  and an inventory of all 34 paper figures (high-resolution, 2000 px) with
  working image links to the PNG mirrors under `../figures/extracted/figures/`.
- [Release notes (converted)](zenodo_README.md) - [MarkItDown](https://github.com/microsoft/markitdown) conversion of
  `source/zenodo_README.txt`.
- [Reproduction notes (converted)](zenodo_README_GWTC-3-population-data.md) -
  [MarkItDown](https://github.com/microsoft/markitdown) conversion of `source/zenodo_README_GWTC-3-population-data.txt`.
