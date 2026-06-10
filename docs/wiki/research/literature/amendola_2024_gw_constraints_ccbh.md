---
doc_id: lit_amendola_2024_gw_constraints_ccbh
title: Amendola 2024 GW Constraints CCBH
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

# Amendola 2024 GW Constraints CCBH

## Bibliographic Metadata

- Paper: "Constraints on cosmologically coupled black holes from gravitational
  wave observations and minimal formation mass"
- Authors: Luca Amendola, Davi C. Rodrigues, Sumit Kumar, Miguel Quartin
- DOI: [10.1093/mnras/stae143](https://doi.org/10.1093/mnras/stae143)
- Venue: Monthly Notices of the Royal Astronomical Society 528, 2377-2390
  (2024)

## Key Equations

- Tests black holes that grow as a power of scale factor, with coupling index
  `k`.
- Treats `k ~= 3` as the regime that may act as a dark-energy source.
- Uses minimal black-hole formation mass constraints for stellar-progenitor
  black holes observed by LIGO-Virgo-KAGRA.

## Coupling Definitions

- Primary cache variable: cosmological coupling index `k`.
- Main constraint logic: if observed black holes grew strongly after formation,
  their inferred initial masses may fall below plausible stellar black-hole
  formation thresholds.

## Datasets Used

- LIGO-Virgo-KAGRA black-hole observations.
- Power-law-plus-peak mass distribution comparisons.
- Minimum stellar black-hole formation mass assumptions.

## Redshift Coverage

- Gravitational-wave population redshift coverage rather than a reconstructed
  dark-energy timing curve.

## Available Products

- Tables: paper tables available through journal/PDF.
- Posterior samples: LVK public products exist generally, but paper-specific
  derived products are not cached locally.
- MCMC chains: not found in this quick 2026-06-10 source check.
- Covariance matrices: not found in this quick 2026-06-10 source check.
- Figures: paper figures available.
- Public code/data links: the paper lists code repositories:
  <https://github.com/itpamendola/CCBH-direct> and
  <https://github.com/davi-rodrigues/CCBH-Numerics>.

## Digitization Requirements

The paper is usable as a constraint and code-route record without figure
digitization. Reproducing the exact constraints would require the listed code
and the corresponding LVK data inputs.

## Public Code / Data Links

- Journal page: <https://academic.oup.com/mnras/article/528/2/2377/7529208>
- DOI: <https://doi.org/10.1093/mnras/stae143>
- Code: <https://github.com/itpamendola/CCBH-direct>
- Code: <https://github.com/davi-rodrigues/CCBH-Numerics>

## QFUDS Relevance

Reference role: constraint comparator and reproducibility route for the
black-hole-coupled source lane.

The paper is relevant because it supplies a gravitational-wave population test
for the coupling strength required by black-hole-as-dark-energy models. It does
not provide a QFUDS source equation, `Q^nu`, phase-B pressure rationale, or
`delta Q`.

## Use Restrictions

- Use as a known-model constraint comparator.
- Do not use its `k` constraints as a QFUDS result without mapping a specific
  QFUDS black-hole source model to `k`.

## Check History

- 2026-06-10: journal page, DOI metadata, abstract, and code links checked for
  black-hole-coupled source audit caching.
