---
doc_id: lit_farrah_2023_cosmological_coupling_black_holes
title: Farrah 2023 Cosmological Coupling Black Holes
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-10
record_type: literature_record
paper_year: 2023
availability_last_checked: 2026-06-10
used_by:
  - source_x_black_hole_coupled_source_audit
---

# Farrah 2023 Cosmological Coupling Black Holes

## Bibliographic Metadata

- Paper: "Observational evidence for cosmological coupling of black holes and
  its implications for an astrophysical source of dark energy"
- Authors: Duncan Farrah, Kevin S. Croker, Gregory Tarle, Valerio Faraoni, Sara
  Petty, Jose Afonso, Nicolas Fernandez, Kurtis A. Nishimura, Chris Pearson,
  Lingyu Wang, Michael Zevin, David L. Clements, Andreas Efstathiou, Evanthia
  Hatziminaoglou, Mark Lacy, Conor McPartland, Lura K. Pitchford, Nobuyuki
  Sakai, Joel Weiner
- arXiv: [2302.07878](https://arxiv.org/abs/2302.07878)
- DOI: [10.3847/2041-8213/acb704](https://doi.org/10.3847/2041-8213/acb704)
- Venue: Astrophysical Journal Letters 944, L31 (2023)

## Key Equations

- Studies cosmological black-hole mass growth independent of ordinary accretion
  or mergers.
- Source-level variable: black-hole gravitating mass as a function of scale
  factor or redshift.
- Dark-energy-relevant claim: the inferred redshift dependence can make the
  black-hole population contribute an effectively constant energy density to
  Friedmann equations at late times.

## Coupling Definitions

- Primary cache variable: cosmological coupling of black-hole mass growth.
- The paper reports evidence for nonzero coupling from supermassive black holes
  in elliptical galaxies over `0 < z ~= 2.5`.
- The black-hole production route is tied to cosmic star-formation history.

## Datasets Used

- Supermassive black-hole and host-galaxy samples in elliptical galaxies.
- Cosmic star-formation-history input for the black-hole production estimate.
- Planck `Omega_Lambda` is used as the dark-energy density comparison target.
- Massive compact halo object constraints are considered as consistency checks.

## Redshift Coverage

- Black-hole growth test: `0 < z ~= 2.5`.
- Dark-energy-density implication discussed for `z <~ 7`.
- Claimed acceleration timing is around `z ~ 0.7`.

## Available Products

- Tables: not cached locally.
- Posterior samples: not found in this quick 2026-06-10 source check.
- MCMC chains: not found in this quick 2026-06-10 source check.
- Covariance matrices: not found in this quick 2026-06-10 source check.
- Figures: paper figures available through arXiv/PDF.
- Public code/data repository: not found in the quick source check.

## Digitization Requirements

Digitization or author data would be required before using this paper as a
numerical source-history input. The paper is immediately usable as a
known-model comparator and source definition reference for cosmologically
coupled black-hole mass growth.

## Public Code / Data Links

- arXiv abstract/PDF/source: <https://arxiv.org/abs/2302.07878>
- Journal DOI: <https://doi.org/10.3847/2041-8213/acb704>

## QFUDS Relevance

Reference role: primary comparator for the black-hole-coupled source lane.

The paper supplies a concrete adjacent model family: black-hole mass growth and
production as an astrophysical dark-energy source. It does not supply a QFUDS
phase-transfer law, QFUDS `Q^nu`, QFUDS `delta Q`, or a distinction between
QFUDS and cosmologically coupled black-hole dark energy.

## Use Restrictions

- Do not treat this record as support for QFUDS novelty.
- Do not treat black-hole mass growth as a QFUDS source unless a distinct QFUDS
  equation, observable, or perturbation route is supplied elsewhere.
- Do not use the paper as a numerical source history without data extraction,
  digitization, or author products.

## Check History

- 2026-06-10: arXiv abstract, DOI metadata, and availability links checked for
  black-hole-coupled source audit caching.
