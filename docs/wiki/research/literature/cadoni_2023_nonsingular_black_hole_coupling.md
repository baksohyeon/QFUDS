---
doc_id: lit_cadoni_2023_nonsingular_black_hole_coupling
title: Cadoni 2023 Nonsingular Black Hole Coupling
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

# Cadoni 2023 Nonsingular Black Hole Coupling

## Bibliographic Metadata

- Paper: "Cosmological coupling of nonsingular black holes"
- Authors: M. Cadoni, A. P. Sanna, M. Pitzalis, B. Banerjee, R. Murgia, N.
  Hazra, M. Branchesi
- arXiv: [2306.11588](https://arxiv.org/abs/2306.11588)
- DOI: [10.1088/1475-7516/2023/11/007](https://doi.org/10.1088/1475-7516/2023/11/007)
- Venue: JCAP 11, 007 (2023)

## Short Summary

Cadoni et al. study cosmological coupling for nonsingular black holes and find a
weaker mass-growth scaling than the `k ~= 3` dark-energy-source case. For QFUDS
this is a theoretical comparator showing reduction risk and possible failure
modes for regular black-hole source claims. It does not provide a QFUDS-specific
transfer vector, phase-B pressure derivation, or perturbation route.

## Key Equations

- Studies cosmological coupling of singularity-free black holes and horizonless
  compact objects in general relativity.
- Finds a leading mass-growth scaling `M_BH proportional to a^k` with `k = 1`
  from the curvature term for regular black holes.

## Coupling Definitions

- Primary cache variable: black-hole mass growth exponent `k`.
- The record is a theoretical comparator for the `k ~= 3` dark-energy-source
  claim.

## Datasets Used

- Supermassive black-hole data in elliptical galaxies at `z = 0.8--0.9`.
- JWST high-redshift black-hole mass measurements are used for comparison.

## Redshift Coverage

- Elliptical-galaxy test sample: `z = 0.8--0.9`.
- JWST comparison: higher-redshift black-hole measurements.

## Available Products

- Tables: not cached locally.
- Posterior samples: not found in this quick 2026-06-10 source check.
- MCMC chains: not found in this quick 2026-06-10 source check.
- Covariance matrices: not found in this quick 2026-06-10 source check.
- Figures: paper figures available through arXiv/PDF/HTML.
- Public code/data repository: not found in the quick source check.

## Digitization Requirements

This paper can be used qualitatively as a theoretical and observational
comparator. Numerical reuse would require extracting the reported comparisons
or obtaining author products.

## Public Code / Data Links

- arXiv abstract/PDF/HTML/source: <https://arxiv.org/abs/2306.11588>
- Journal DOI: <https://doi.org/10.1088/1475-7516/2023/11/007>

## QFUDS Relevance

Reference role: theoretical comparator for whether black-hole cosmological
coupling naturally supplies dark-energy-scale behavior.

The paper is relevant because it supports weaker coupling than the `k ~= 3`
dark-energy-source case for regular black holes and concludes that the studied
objects are unlikely to be the source of dark energy.

## Use Restrictions

- Use as a comparator for coupling exponent and dark-energy-source viability.
- Do not use as a direct QFUDS result without a specific mapping from QFUDS
  source assumptions to the paper's compact-object class.

## Check History

- 2026-06-10: arXiv abstract, DOI metadata, and availability links checked for
  black-hole-coupled source audit caching.
