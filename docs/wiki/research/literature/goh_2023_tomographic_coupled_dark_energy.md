---
doc_id: lit_goh_2023_tomographic_coupled_dark_energy
title: Goh 2023 Tomographic Coupled Dark Energy
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-09
record_type: literature_record
paper_year: 2023
availability_last_checked: 2026-06-09
used_by:
  - exp_006
---

# Goh 2023 Tomographic Coupled Dark Energy

## Bibliographic Metadata

- Paper: "Constraining constant and tomographic coupled dark energy with
  low-redshift and high-redshift probes"
- Authors: Lisa W. K. Goh, Adria Gomez-Valent, Valeria Pettorino, Martin
  Kilbinger
- arXiv: [2211.13588](https://arxiv.org/abs/2211.13588)
- DOI: [10.1103/PhysRevD.107.083503](https://doi.org/10.1103/PhysRevD.107.083503)
- Venue: Physical Review D

## Key Equations

- Studies coupled dark energy with a scalar field mediating an additional force
  on dark matter.
- Uses constant and tomographic coupling parameterizations.

## Coupling Definitions

- Primary variable for the Exp006 cache: `beta(z)`.
- `beta(z)` is a scalar-field CDE coupling strength.
- It is not an interacting-vacuum transfer kernel.

## Datasets Used

- Planck.
- ACT.
- SPT.
- BAO.
- Supernovae.
- SH0ES prior in some combinations.
- RSD.
- KiDS-1000 weak lensing.
- BOSS galaxy clustering.
- 3x2pt galaxy-galaxy lensing cross-correlation.

## Redshift Coverage

- 7-bin tomographic model uses bins with edges `{0, 1, 2, 5, 100, 500, 1000}`.
- 4-bin low-redshift model uses bins with edges `{0, 0.5, 1, 2}`.

## Available Products

- Tables: yes.
- Posterior samples: not found in the checked public sources.
- MCMC chains: not found in the checked public sources.
- Covariance matrices: not found in the checked public sources.
- Reconstructed histories: table-level tomographic constraints and figures.
- Figures: yes.
- Code: public modified CLASS code was identified.

## Digitization Requirements

Digitization is not needed for the table-level proxy constraints used by Exp006.
It may be useful only if a later audit wants figure-level comparison across all
tomographic datasets.

## Public Code / Data Links

- Paper page: [arXiv:2211.13588](https://arxiv.org/abs/2211.13588)
- Code link found from paper text and public search:
  [LisaGoh/CDE](https://github.com/LisaGoh/CDE)

## QFUDS Relevance

Reference role: secondary scalar-field CDE timing proxy for Exp006.

This record does not state that Goh et al. provides direct IV/IDE support.

## Use Restrictions

- Use only as a secondary proxy for timing coverage.
- Do not promote `beta(z)` to a direct vacuum-transfer variable.

## Check History

- 2026-06-09: arXiv page, paper source notes, and public code reference checked.
