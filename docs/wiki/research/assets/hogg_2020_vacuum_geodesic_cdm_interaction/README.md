---
doc_id: asset_hogg_2020_vacuum_geodesic_cdm_interaction
title: "Hogg 2020 Vacuum Geodesic CDM Interaction Assets"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - lit_hogg_2020_vacuum_geodesic_cdm_interaction
next_gate: Martinelli/Hogg same-family comparison note before any retained timing fit
last_updated: 2026-06-18
---

# Hogg 2020 Vacuum Geodesic CDM Interaction Assets

## Workflow Boundary

This cache follows the
[Research Asset and Product Workflow](../../../../../.agent/workflows/research-asset-product-workflow.md).

These files are research assets only. They do not create QFUDS evidence, change
roadmap status, open Level 2B, or support retained `Gamma(a)`.

## Bibliographic Metadata

- Paper: "Latest evidence for a late time vacuum - geodesic CDM interaction"
- Authors: Natalie B. Hogg, Marco Bruni, Robert Crittenden, Matteo Martinelli,
  Simone Peirone
- Year: 2020
- arXiv: [2002.10449](https://arxiv.org/abs/2002.10449)
- DOI: [10.1016/j.dark.2020.100583](https://doi.org/10.1016/j.dark.2020.100583)
- Venue: Physics of the Dark Universe

## Asset State

| Field | Value |
| --- | --- |
| Source URL | <https://arxiv.org/abs/2002.10449> |
| Asset type | arXiv PDF, arXiv source bundle, extracted TeX/source figures |
| Current asset state | `asset_cached`; `asset_extracted_not_digitized`; `manual_structured_extract` |
| Extraction potential | `source_tex_parse_possible`; `figure_digitization_possible`; `direct_table` for paper tables |
| Text quality | TeX source parse available through `source/extracted/17bins.tex` |
| Depends on | Source-X 059 Hogg equation extraction target |
| Known blocked step | no machine-readable posterior, chain, covariance, or numerical `q(z)` product is created by the current extraction |
| Local metadata check | extracted source and raw bundle string search found no local path or sync metadata markers |

## Files

- `source/paper_arxiv_2002.10449.pdf` - full arXiv paper PDF.
- `source/arxiv_source_2002.10449.tar.gz` - downloaded arXiv source bundle.
- `source/extracted/17bins.tex` - extracted manuscript TeX source.
- `source/extracted/17bins.bib` - extracted bibliography.
- `source/extracted/17bins.bbl` - extracted compiled bibliography.
- `source/extracted/plots/*` - extracted source figure assets, including
  coupling-bin, GP/spline, cumulative-variance, and tension plots.
- `figures/.gitkeep` - reserved for rendered or copied figure mirrors if later
  needed.
- `digitization/.gitkeep` - reserved for future structured extracts or
  digitization products.
- [digitization/README.md](digitization/README.md) - digitization and
  structured-extract index.
- [digitization/equation_extraction_20260618.md](digitization/equation_extraction_20260618.md) -
  manual structured extract of the source TeX equations and reconstruction
  boundary.

## Immediate Use

The next Source-X task may compare Hogg 2020 with Martinelli 2019 as the same
vacuum-geodesic CDM family:

```text
shared Q / Q^mu / CDM-frame closure
Martinelli detailed perturbation equations
Hogg 17-bin CPZ-prior reconstruction
PCA prior-dominance check
Bayesian evidence boundary
```

Do not use the figure assets as numerical products without a later digitization
protocol.
