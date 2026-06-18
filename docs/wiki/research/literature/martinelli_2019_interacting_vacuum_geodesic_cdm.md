---
doc_id: lit_martinelli_2019_interacting_vacuum_geodesic_cdm
title: Martinelli 2019 Interacting Vacuum Geodesic CDM
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-18
record_type: literature_record
paper_year: 2019
availability_last_checked: 2026-06-09
used_by:
  - exp_006
---

# Martinelli 2019 Interacting Vacuum Geodesic CDM

## Workflow Boundary

This record follows the
[Research Asset and Product Workflow](../../../../.agent/workflows/research-asset-product-workflow.md).

The 2026-06-18 update records a local source cache only. Current source state:
`asset_cached`; `asset_extracted_not_digitized`. This is not QFUDS evidence,
not retained `Gamma(a)` support, and not Level 2B admission.

## Bibliographic Metadata

- Paper: "Constraints on the interacting vacuum - geodesic CDM scenario"
- Authors: Matteo Martinelli, Natalie B. Hogg, Simone Peirone, Marco Bruni,
  David Wands
- arXiv: [1902.10694](https://arxiv.org/abs/1902.10694)
- DOI: [10.1093/mnras/stz1915](https://doi.org/10.1093/mnras/stz1915)
- Venue: Monthly Notices of the Royal Astronomical Society

## Key Equations

- Studies interacting vacuum energy with geodesic CDM.
- Presents linear perturbation theory for the interacting scenario.
- Uses MCMC sampling across multiple coupling parameterizations.

## Coupling Definitions

- Primary variable for the cache: `q_V(z)`.
- Includes single-parameter, transition-redshift, and binned interaction cases.

## Datasets Used

- Planck 2015 CMB data.
- BAO.
- RSD.
- Type Ia supernovae.

## Redshift Coverage

- Includes fixed and variable transition-redshift cases.
- Includes a four-bin reconstruction of `q_V(z)`.

## Available Products

- Tables: yes.
- Posterior samples: not found in the checked public sources.
- MCMC chains: not found in the checked public sources.
- Covariance matrices: not found in the checked public sources.
- Reconstructed histories: figures and table-level constraints.
- Figures: yes.

## Digitization Requirements

Digitization is optional for qualitative historical comparison and required for
curve-level timing comparison if chains or numerical reconstructions are not
available.

## Public Code / Data Links

- arXiv page provides PDF and TeX source.
- Repository-local asset cache:
  [Martinelli 2019 assets](../assets/martinelli_2019_interacting_vacuum_geodesic_cdm/README.md).
- Manual structured equation extract:
  [Martinelli 2019 IV/Geodesic-CDM Equation Extraction](../assets/martinelli_2019_interacting_vacuum_geodesic_cdm/digitization/equation_extraction_20260618.md).
- Public posterior products were not found during the 2026-06-09 check.

## QFUDS Relevance

Reference role: historical IV/geodesic-CDM reconstruction precedent.

This record is not a QFUDS conclusion.

## Use Restrictions

- Use as historical model-family context unless a future audit promotes it to a
  direct comparison target.
- Do not infer Exp006 classification changes from this record alone.

## Check History

- 2026-06-09: arXiv and article search checked for public source and product
  availability.
- 2026-06-18: arXiv PDF and source bundle cached locally for Source-X equation
  extraction. Current source state: `asset_cached`;
  `asset_extracted_not_digitized`.
- 2026-06-18: manual structured equation extract added for background `Q`,
  covariant `Q^mu`, CDM-frame/geodesic closure, perturbation equations, RSD
  growth adjustment, and modified CAMB/CosmoMC route. Current extraction state:
  `manual_structured_extract`.
