---
doc_id: asset_martinelli_2019_interacting_vacuum_geodesic_cdm
title: "Martinelli 2019 Interacting Vacuum Geodesic CDM Assets"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - lit_martinelli_2019_interacting_vacuum_geodesic_cdm
next_gate: structured equation extraction before IV/geodesic-CDM convention comparison
last_updated: 2026-06-18
---

# Martinelli 2019 Interacting Vacuum Geodesic CDM Assets

## Workflow Boundary

This cache follows the
[Research Asset and Product Workflow](../../../../../.agent/workflows/research-asset-product-workflow.md).

These files are research assets only. They do not create QFUDS evidence, change
roadmap status, open Level 2B, or support retained `Gamma(a)`.

## Bibliographic Metadata

- Paper: "Constraints on the interacting vacuum - geodesic CDM scenario"
- Authors: Matteo Martinelli, Natalie B. Hogg, Simone Peirone, Marco Bruni,
  David Wands
- Year: 2019
- arXiv: [1902.10694](https://arxiv.org/abs/1902.10694)
- DOI: [10.1093/mnras/stz1915](https://doi.org/10.1093/mnras/stz1915)
- Venue: Monthly Notices of the Royal Astronomical Society

## Asset State

| Field | Value |
| --- | --- |
| Source URL | <https://arxiv.org/abs/1902.10694> |
| Asset type | arXiv PDF, arXiv source bundle, extracted TeX/source figures |
| Current asset state | `asset_cached`; `asset_extracted_not_digitized` |
| Extraction potential | `source_tex_parse_possible`; `figure_digitization_possible`; `direct_table` for paper tables |
| Text quality | TeX source parse available through `source/extracted/void.tex` |
| Depends on | Source-X 059 Martinelli equation extraction target |
| Known blocked step | no structured equation extract exists yet |
| Local metadata check | extracted source and raw bundle string search found no local path or sync metadata markers |

## Files

- `source/paper_arxiv_1902.10694.pdf` - full arXiv paper PDF.
- `source/arxiv_source_1902.10694.tar.gz` - downloaded arXiv source bundle.
- `source/extracted/void.tex` - extracted manuscript TeX source.
- `source/extracted/void.bib` - extracted bibliography.
- `source/extracted/void.bbl` - extracted compiled bibliography.
- `source/extracted/*.pdf` - extracted source figure PDFs, including
  interaction, density, CMB, matter power, Hubble, and tension figures.
- `figures/.gitkeep` - reserved for rendered or copied figure mirrors if later
  needed.
- `digitization/.gitkeep` - reserved for future structured extracts or
  digitization products.

## Immediate Use

The next Source-X task may inspect `source/extracted/void.tex` for:

```text
interacting-vacuum background Q convention
geodesic CDM frame condition
q_V(z) definition and normalization
linear perturbation equations
CAMB/CosmoMC or other solver route
whether posterior chains or numeric q_V histories are absent from this cache
```

Do not use the figure PDFs as numerical products without a later digitization
protocol.
