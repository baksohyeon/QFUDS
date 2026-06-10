---
doc_id: lit_abedin_2025_gp_ann_dark_sector_interaction
title: Abedin 2025 GP ANN Dark-Sector Interaction
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-10
record_type: literature_record
paper_year: 2025
availability_last_checked: 2026-06-10
used_by:
  - structure_era_activation_literature_audit
---

# Abedin 2025 GP ANN Dark-Sector Interaction

## Bibliographic Metadata

- Paper: "In search of an interaction in the dark sector through Gaussian
  Process and ANN approaches"
- Authors: S. Abedin et al.
- arXiv: [2505.04336](https://arxiv.org/abs/2505.04336)
- Journal reference: MNRAS 540, 2253-2268 (2025)

## Key Equations

- Reconstructs dark-sector interaction using Gaussian-process and artificial
  neural-network approaches.
- Reports weak or absent interaction in the `w = -1` case and stronger
  indications when `w` is allowed to deviate.

## Coupling Definitions

- Defines an interaction through dark-sector continuity equations.
- Cache variable: reconstructed interaction history under GP/ANN methods.

## Datasets Used

- Late-time cosmological datasets are used; this cache pass did not unpack all
  dataset combinations beyond the arXiv metadata and abstract.

## Redshift Coverage

- Late-time reconstruction coverage; no numerical history table found in this
  cache pass.

## Available Products

- Paper PDF available through arXiv.
- No public posterior chains or reconstruction arrays found during this cache
  pass.

## Digitization Requirements

Required for curve-level use unless author products are found.

## Public Code / Data Links

- arXiv page: [2505.04336](https://arxiv.org/abs/2505.04336)

## QFUDS Relevance

Reference role: recent nonparametric dark-sector interaction comparator.

## Use Restrictions

- Treat `w = -1` and `w != -1` cases separately.
- Do not collapse ANN/GP reconstruction outputs into QFUDS timing without sign,
  normalization, and convention checks.

## Check History

- 2026-06-10: arXiv page checked for metadata, method role, and product
  availability.
