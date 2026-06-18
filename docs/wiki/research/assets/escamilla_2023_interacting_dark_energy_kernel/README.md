---
doc_id: asset_escamilla_2023_interacting_dark_energy_kernel
title: "Escamilla 2023 Interacting Dark Energy Kernel Assets"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - lit_escamilla_2023_interacting_dark_energy_kernel
next_gate: structured equation extraction before IV/IDE convention comparison
last_updated: 2026-06-18
---

# Escamilla 2023 Interacting Dark Energy Kernel Assets

## Workflow Boundary

This cache follows the
[Research Asset and Product Workflow](../../../../../.agent/workflows/research-asset-product-workflow.md).

These files are research assets only. They do not create QFUDS evidence, change
roadmap status, open Level 2B, or support retained `Gamma(a)`.

## Bibliographic Metadata

- Paper: "Model-independent reconstruction of the Interacting Dark Energy
  Kernel: Binned and Gaussian process"
- Authors: Luis A. Escamilla, Ozgur Akarsu, Eleonora Di Valentino, J. Alberto
  Vazquez
- Year: 2023
- arXiv: [2305.16290](https://arxiv.org/abs/2305.16290)
- DOI: [10.1088/1475-7516/2023/11/051](https://doi.org/10.1088/1475-7516/2023/11/051)
- Venue: JCAP

## Asset State

| Field | Value |
| --- | --- |
| Source URL | <https://arxiv.org/abs/2305.16290> |
| Asset type | arXiv PDF, arXiv source tarball, extracted TeX/source figures |
| Current asset state | `asset_cached`; `asset_extracted_not_digitized` |
| Extraction potential | `source_tex_parse_possible`; `figure_digitization_possible`; `direct_table` for paper tables |
| Text quality | TeX source parse available through `source/extracted/main.tex` |
| Depends on | Source-X 060 Escamilla equation extraction target |
| Known blocked step | no structured equation extract exists yet |

## Files

- `source/paper_arxiv_2305.16290.pdf` - full arXiv paper PDF.
- `source/arxiv_source_2305.16290.tar.gz` - downloaded arXiv source bundle.
- `source/extracted/main.tex` - extracted manuscript TeX source.
- `source/extracted/bibliography.bib` - extracted bibliography.
- `source/extracted/*.pdf` - extracted source figure PDFs, including `Pi_*`,
  `Q_*`, `IQ_*`, `qz_*`, density, effective-EOS, and triangle-plot figures.
- `figures/.gitkeep` - reserved for rendered or copied figure mirrors if later
  needed.
- `digitization/.gitkeep` - reserved for future structured extracts or
  digitization products.

## Immediate Use

The next Source-X task may inspect `source/extracted/main.tex` for:

```text
Q sign convention
Pi_DE / Pi_DM definitions
I_Q definition
redshift continuity equations
background-only limitation
whether Q^mu, frame, delta Q, and perturbation closure are absent or deferred
```

Do not use the figure PDFs as numerical products without a later digitization
protocol.
