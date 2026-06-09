---
doc_id: lit_bonilla_2022_dark_sector_interaction_gp
title: Bonilla 2022 Dark Sector Interaction GP
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-09
record_type: literature_record
paper_year: 2022
availability_last_checked: 2026-06-09
used_by:
  - exp_006
---

# Bonilla 2022 Dark Sector Interaction GP

## Bibliographic Metadata

- Paper: "Reconstruction of the dark sectors' interaction: A
  model-independent inference and forecast from GW standard sirens"
- Authors: Alexander Bonilla, Suresh Kumar, Rafael C. Nunes, Supriya Pan
- arXiv: [2102.06149](https://arxiv.org/abs/2102.06149)
- DOI: [10.1093/mnras/stac687](https://doi.org/10.1093/mnras/stac687)
- Venue: Monthly Notices of the Royal Astronomical Society

## Key Equations

- Uses Gaussian processes to infer a reconstructed coupling function between
  dark components.
- Includes cases with `w = -1` and with a general dark-energy equation of state.

## Coupling Definitions

- Primary variable for the Exp006 cache: `delta(z)`.
- The paper defines `delta(z)=q(1+z)^-6`, with `q=Q/H0^3`.

## Datasets Used

- Cosmic chronometers.
- Supernovae.
- BAO.
- H0LiCOW.
- Mock gravitational-wave standard sirens for forecast/kernel optimization.

## Redshift Coverage

- Paper figures show reconstructions over low-to-intermediate redshift ranges.
- The mock standard-siren catalogue is described up to `z = 2`.
- Exp006 treated the paper as optional because no table-level timing history was
  used.

## Available Products

- Tables: no table-level reconstructed timing history found.
- Posterior samples: not found in the checked public sources.
- MCMC chains: not found in the checked public sources.
- Covariance matrices: not found in the checked public sources.
- Reconstructed histories: figure-only in checked sources.
- Figures: yes.

## Digitization Requirements

Digitization is required before using this paper for timing-shape comparison,
unless author-provided numerical histories become available.

## Public Code / Data Links

- arXiv page provides PDF and TeX source.
- The paper data availability statement says observational data are available on
  reasonable request to the corresponding author.

## QFUDS Relevance

Reference role: optional GP reconstruction target for Exp006-style timing
audits.

This record does not classify Bonilla et al. as supporting retained timing.

## Use Restrictions

- Do not treat figure-only curves as numerical evidence without a digitization
  protocol.
- Do not use mock-GW forecast output as current observational support.

## Check History

- 2026-06-09: arXiv page, paper source notes, and data availability text
  checked.
