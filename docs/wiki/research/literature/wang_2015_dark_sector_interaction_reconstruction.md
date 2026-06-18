---
doc_id: lit_wang_2015_dark_matter_vacuum_interaction
title: Wang 2015 Dark Matter Vacuum Interaction
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: Wang versus Martinelli/Hogg convention comparison before any retained timing fit
last_updated: 2026-06-18
record_type: literature_record
paper_year: 2015
availability_last_checked: 2026-06-09
used_by:
  - exp_006
---

# Wang 2015 Dark Matter Vacuum Interaction

## Workflow Boundary

This record follows the
[Research Asset and Product Workflow](../../../../.agent/workflows/research-asset-product-workflow.md).

The 2026-06-18 updates record a local source cache and manual structured
equation extract. Current source state: `asset_cached`;
`asset_extracted_not_digitized`; `manual_structured_extract`. The arXiv source
bundle was fetched and extracted, but the raw bundle is not retained because
extracted EPS metadata contained upstream local path metadata. This is not
QFUDS evidence, not retained `Gamma(a)` support, and not Level 2B admission.

## Bibliographic Metadata

- Paper: "Reconstruction of the dark matter-vacuum energy interaction"
- Authors: Yuting Wang, Gong-Bo Zhao, David Wands, Levon Pogosian, Robert G.
  Crittenden
- arXiv: [1505.01373](https://arxiv.org/abs/1505.01373)
- DOI: [10.1103/PhysRevD.92.103005](https://doi.org/10.1103/PhysRevD.92.103005)
- Venue: Physical Review D

## Key Equations

- Reconstructs the temporal evolution of the coupling strength between dark
  matter and vacuum energy.
- Uses a nonparametric Bayesian approach.
- Source extraction records `Q = 3 alpha H rho_dm V / (rho_dm + V)`,
  DM-frame `Q^mu`, the `delta_dm` perturbation equation, RSD observable
  replacement, 40-bin CPZ-prior reconstruction, PCA, and evidence boundary.

## Coupling Definitions

- Primary cache variable: `alpha(a)`.
- The variable represents the temporal evolution of coupling strength between
  dark matter and vacuum energy in the paper's framework.

## Datasets Used

- CMB.
- Supernovae.
- Large-scale structure.

## Redshift Coverage

- Expressed as a scale-factor reconstruction.
- This cache entry has not yet expanded the figure-level support into a
  redshift-domain table.

## Available Products

- Tables: not fully audited.
- Posterior samples: not found in checked public sources.
- MCMC chains: not found in checked public sources.
- Covariance matrices: not found in checked public sources.
- Reconstructed histories: figures.
- Figures: yes.

## Digitization Requirements

Digitization is optional for historical comparison and required for curve-level
timing extraction if numerical products are unavailable.

## Public Code / Data Links

- arXiv page provides PDF and TeX source.
- Repository-local asset cache:
  [Wang 2015 assets](../assets/wang_2015_dark_matter_vacuum_interaction/README.md).
- Repository-local equation extract:
  [2026-06-18 Wang equation extraction](../assets/wang_2015_dark_matter_vacuum_interaction/digitization/equation_extraction_20260618.md).
- Public posterior products were not found during the 2026-06-09 check.

## QFUDS Relevance

Reference role: historical nonparametric dark matter-vacuum interaction
reconstruction.

This record does not provide a QFUDS conclusion.

## Use Restrictions

- Use as historical context unless a future audit defines a direct comparison
  against `alpha(a)`.
- Do not mix this paper's coupling convention with IV/IDE kernels without an
  explicit mapping.

## Check History

- 2026-06-09: arXiv page checked for metadata and public source availability.
- 2026-06-18: arXiv PDF and source bundle fetched from arXiv; PDF and extracted
  source retained locally. Current source state: `asset_cached`;
  `asset_extracted_not_digitized`.
- 2026-06-18: manual structured equation extraction added from cached source
  TeX. Current workflow state additionally includes `manual_structured_extract`.
