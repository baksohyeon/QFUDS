---
doc_id: lit_you_2025_desi_dr2_coupled_dark_sector
title: You 2025 DESI DR2 Coupled Dark Sector
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-09
record_type: literature_record
paper_year: 2025
availability_last_checked: 2026-06-09
used_by:
  - exp_006_coverage_expansion
---

# You 2025 DESI DR2 Coupled Dark Sector

## Bibliographic Metadata

- Paper: "Dynamical Dark Energy Implies a Coupled Dark Sector: Insights from
  DESI DR2 via a Data-Driven Approach"
- Authors: Changyu You, Dan Wang, Tao Yang
- arXiv: [2504.00985](https://arxiv.org/abs/2504.00985)
- DOI: [10.1103/f6v7-n9fr](https://doi.org/10.1103/f6v7-n9fr)
- Venue: Physical Review D

## Key Equations

- Uses Gaussian-process regression and a non-parametric formalism.
- Reconstructs dark energy equation of state behavior and explores its
  implication for possible dark-sector coupling.

## Coupling Definitions

- Primary cache variable: potential interaction/coupling inferred from the
  reconstructed dark energy equation of state.
- This is not a direct IV kernel reconstruction in the same sense as
  Escamilla `Pi_DE(z)`.

## Datasets Used

- DESI DR2.
- Cosmic chronometers.
- Observational Hubble data.
- Type Ia supernovae.

## Redshift Coverage

- The paper reports a phantom crossing around `z ~ 0.4`.
- It is mainly low-redshift timing coverage, not structure-era peak coverage.

## Available Products

- Tables: limited paper-level summaries.
- Posterior samples: not found in the checked public sources.
- MCMC chains: not found in the checked public sources.
- Covariance matrices: not found in the checked public sources.
- Reconstructed histories: figures.
- Figures: yes.

## Digitization Requirements

Digitization would be required for curve-level timing extraction. For Exp006 it
is lower priority than direct IV/IDE coupling reconstructions.

## Public Code / Data Links

- arXiv page provides PDF, HTML, and TeX source links.
- Public posterior products were not found during the 2026-06-09 check.

## QFUDS Relevance

Reference role: DESI-era data-driven coupled-dark-sector coverage.

This record does not state that retained timing is supported.

## Use Restrictions

- Treat as indirect coupling-timing evidence unless a direct coupling history is
  extracted from author products.
- Do not use low-redshift interaction indication as structure-era timing
  support.

## Check History

- 2026-06-09: arXiv page and public search checked for bibliographic metadata
  and data-product availability.
