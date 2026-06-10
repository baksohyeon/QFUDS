---
doc_id: lit_croker_2024_desi_coupled_black_holes
title: Croker 2024 DESI Coupled Black Holes
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-10
record_type: literature_record
paper_year: 2024
availability_last_checked: 2026-06-10
used_by:
  - source_x_black_hole_coupled_source_audit
---

# Croker 2024 DESI Coupled Black Holes

## Bibliographic Metadata

- Paper: "DESI Dark Energy Time Evolution is Recovered by Cosmologically
  Coupled Black Holes"
- Authors: Kevin S. Croker, Gregory Tarle, Steve P. Ahlen, Brian G. Cartwright,
  Duncan Farrah, Nicolas Fernandez, Rogier A. Windhorst
- arXiv: [2405.12282](https://arxiv.org/abs/2405.12282)
- DOI: [10.1088/1475-7516/2024/10/094](https://doi.org/10.1088/1475-7516/2024/10/094)
- Venue: JCAP 10, 094 (2024)

## Short Summary

Croker et al. present a DESI-era comparison in which cosmologically coupled
black-hole production recovers a dark-energy time evolution similar to DESI
dark-energy fits. For QFUDS this is a high-priority known-model comparator: if a
black-hole production lane is used as a source for phase B, it risks reducing to
CCBH dark energy unless it supplies a distinct QFUDS source equation,
perturbation route, and observable distinction.

## Key Equations

- Assumes dark energy is sourced by cosmologically coupled black-hole
  production.
- Source-level variable: fraction of baryonic density converted into black
  holes, constrained using DESI BAO and BBN-informed priors.
- Model is compared to DESI best-fit `w0 wa` dark-energy histories.

## Coupling Definitions

- Primary cache variable: black-hole production and associated dark-energy
  density history.
- The model is a cosmologically coupled black-hole dark-energy model, not a
  generic IV/IDE coupling kernel.

## Datasets Used

- DESI BAO measurements.
- Big Bang Nucleosynthesis-informed baryon-density priors.
- DESI best-fit `w0 wa` histories used as comparison targets.
- External `H0` comparisons are discussed.

## Redshift Coverage

- DESI BAO late-time redshift coverage.
- The paper highlights behavior at `z <~ 0.2` as a limitation of the `w0 wa`
  parameterization for this comparison.

## Available Products

- Tables: paper tables available.
- Posterior samples: not found in this quick 2026-06-10 source check.
- MCMC chains: not found in this quick 2026-06-10 source check.
- Covariance matrices: not found in this quick 2026-06-10 source check.
- Figures: paper figures available through arXiv/PDF/HTML.
- Public code/data repository: not found in the quick source check.

## Digitization Requirements

Digitization or author products would be required to reuse the paper as a
numerical dark-energy source history. The paper is usable without digitization
as a reduction-test comparator for black-hole production as a dark-energy
source.

## Public Code / Data Links

- arXiv abstract/PDF/HTML/source: <https://arxiv.org/abs/2405.12282>
- Journal DOI: <https://doi.org/10.1088/1475-7516/2024/10/094>

## QFUDS Relevance

Reference role: primary DESI-era comparator for the black-hole-coupled source
lane.

This paper strengthens the known-model reduction risk: a QFUDS black-hole lane
that uses black-hole production to source dark energy must distinguish itself
from cosmologically coupled black-hole dark energy, not merely reproduce a
similar timing history.

## Use Restrictions

- Do not treat DESI agreement in this paper as evidence for QFUDS.
- Do not import the model as QFUDS without a distinct source equation and
  perturbation route.
- Do not use figure-level histories numerically without a digitization protocol
  or author products.

## Check History

- 2026-06-10: arXiv abstract, DOI metadata, and availability links checked for
  black-hole-coupled source audit caching.
