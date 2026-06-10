---
doc_id: lit_yang_2015_gp_dark_sector_interaction
title: Yang 2015 GP Dark-Sector Interaction
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-10
record_type: literature_record
paper_year: 2015
availability_last_checked: 2026-06-10
used_by:
  - structure_era_activation_literature_audit
---

# Yang 2015 GP Dark-Sector Interaction

## Bibliographic Metadata

- Paper: "Reconstructing the interaction between dark energy and dark matter
  using Gaussian Processes"
- Authors: Weiqiang Yang, Lixin Xu
- arXiv: [1505.04443](https://arxiv.org/abs/1505.04443)

## Key Equations

- Reconstructs dark-sector interaction nonparametrically using Gaussian
  processes.
- Includes a decaying-vacuum case with `w = -1` and cases where dark-energy
  equation of state may deviate from `-1`.

## Coupling Definitions

- Defines an interaction term in the dark-sector continuity equations.
- Cache variable: reconstructed interaction history, not directly converted to
  retained QFUDS `Gamma(a)`.

## Datasets Used

- Union2.1 supernova sample is reported on the arXiv page.

## Redshift Coverage

- Supernova redshift coverage; no public binned interaction-history product was
  found in this cache pass.

## Available Products

- Paper PDF available through arXiv.
- No public posterior chains, covariance products, or numerical reconstruction
  table found during this cache pass.

## Digitization Requirements

Required for curve-level use unless author data are found.

## Public Code / Data Links

- arXiv page: [1505.04443](https://arxiv.org/abs/1505.04443)

## QFUDS Relevance

Reference role: historical Gaussian-process interaction reconstruction. It
expands the nonparametric IDE search axis beyond the cached DESI-era records.

## Use Restrictions

- Do not compare reconstructed interaction functions across conventions without
  mapping units, signs, density normalization, and time variable.

## Check History

- 2026-06-10: arXiv page checked for metadata, reconstruction role, and
  product availability.
