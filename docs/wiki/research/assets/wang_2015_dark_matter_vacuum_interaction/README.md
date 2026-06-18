---
doc_id: asset_wang_2015_dark_matter_vacuum_interaction
title: "Wang 2015 Dark Matter Vacuum Interaction Assets"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - lit_wang_2015_dark_matter_vacuum_interaction
next_gate: structured equation extraction before historical convention comparison
last_updated: 2026-06-18
---

# Wang 2015 Dark Matter Vacuum Interaction Assets

## Workflow Boundary

This cache follows the
[Research Asset and Product Workflow](../../../../../.agent/workflows/research-asset-product-workflow.md).

These files are research assets only. They do not create QFUDS evidence, change
roadmap status, open Level 2B, or support retained `Gamma(a)`.

## Bibliographic Metadata

- Paper: "Reconstruction of the dark matter-vacuum energy interaction"
- Authors: Yuting Wang, Gong-Bo Zhao, David Wands, Levon Pogosian, Robert G.
  Crittenden
- Year: 2015
- arXiv: [1505.01373](https://arxiv.org/abs/1505.01373)
- DOI: [10.1103/PhysRevD.92.103005](https://doi.org/10.1103/PhysRevD.92.103005)
- Venue: Physical Review D

## Asset State

| Field | Value |
| --- | --- |
| Source URL | <https://arxiv.org/abs/1505.01373> |
| Asset type | arXiv PDF, extracted arXiv TeX/source figures |
| Current asset state | `asset_cached`; `asset_extracted_not_digitized` |
| Extraction potential | `source_tex_parse_possible`; `figure_digitization_possible`; `direct_table` for paper tables |
| Text quality | TeX source parse available through `source/extracted/Recon_Inter-resubmit_2.tex` |
| Depends on | Source-X 059 Wang equation extraction target |
| Known blocked step | no structured equation extract exists yet |
| Raw bundle boundary | arXiv source bundle was fetched and extracted, but the raw bundle is not retained because extracted EPS metadata contained upstream local path metadata |
| Local metadata check | extracted source path metadata was inspected; `bayes-evi.eps` title metadata was normalized from an upstream local path to `bayes-evi.eps` |

## Files

- `source/paper_arxiv_1505.01373.pdf` - full arXiv paper PDF.
- `source/extracted/Recon_Inter-resubmit_2.tex` - extracted manuscript TeX
  source.
- `source/extracted/alpha-compare.eps` - extracted alpha reconstruction figure
  asset.
- `source/extracted/bao-fs8-pca.eps` - extracted BAO/RSD/PCA figure asset.
- `source/extracted/bayes-evi.eps` - extracted Bayesian-evidence figure asset,
  with upstream local path title metadata normalized.

## Immediate Use

The next Source-X task may inspect
`source/extracted/Recon_Inter-resubmit_2.tex` for:

```text
historical alpha(a) convention
Q = 3 alpha H rho_dm V / (rho_dm + V)
Q^mu / DM-frame geodesic condition
delta_dm perturbation equation
RSD growth observable adjustment
40-bin correlated-prior reconstruction
PCA and Bayesian evidence boundary
```

Do not use the EPS figure assets as numerical products without a later
digitization protocol.
