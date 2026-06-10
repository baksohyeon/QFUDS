---
doc_id: lit_andrae_2023_gaia_coupling_constraints
title: Andrae 2023 Gaia Coupling Constraints
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

# Andrae 2023 Gaia Coupling Constraints

## Bibliographic Metadata

- Paper: "Constraints on the cosmological coupling of black holes from Gaia"
- Authors: Rene Andrae, Kareem El-Badry
- arXiv: [2305.01307](https://arxiv.org/abs/2305.01307)
- DOI: [10.1051/0004-6361/202346350](https://doi.org/10.1051/0004-6361/202346350)
- Venue: Astronomy & Astrophysics 673, L10 (2023)

## Key Equations

- Tests mass growth following cosmological expansion for black holes in Gaia
  BH1 and Gaia BH2.
- Uses the implication that strong coupling would make current black-hole
  masses much smaller at formation.

## Coupling Definitions

- Primary cache variable: `M_BH` growth under the strong coupling scaling used
  in black-hole-as-dark-energy tests.
- Evaluates whether inferred formation masses fall below conventional
  black-hole formation thresholds.

## Datasets Used

- Gaia BH1 and Gaia BH2 binary systems.
- Stellar properties of luminous companions used for age constraints.
- Gaia astrometry and follow-up spectroscopy as reported by the paper.

## Redshift Coverage

- Not a redshift-reconstruction paper.
- Constrains long-term mass growth in nearby detached black-hole-star binary
  systems through age estimates.

## Available Products

- Tables: not cached locally.
- Posterior samples: not found in this quick 2026-06-10 source check.
- MCMC chains: not found in this quick 2026-06-10 source check.
- Covariance matrices: not found in this quick 2026-06-10 source check.
- Figures: paper figures available through arXiv/PDF.
- Public code/data repository: not found in the quick source check.

## Digitization Requirements

The paper can be used qualitatively as a constraint record. Numerical reuse
would require table/figure extraction or author products.

## Public Code / Data Links

- arXiv abstract/PDF/source: <https://arxiv.org/abs/2305.01307>
- Journal DOI: <https://doi.org/10.1051/0004-6361/202346350>

## QFUDS Relevance

Reference role: constraint comparator for strong black-hole mass-growth source
ideas.

The paper is relevant because it identifies nearby binary systems that can test
the strong coupling needed for black holes to act as a dark-energy candidate.
It does not provide QFUDS-specific `Q^nu`, phase-B stress energy, or `delta Q`.

## Use Restrictions

- Use as a constraint comparator only.
- Do not treat the Gaia constraint as a general rejection of every possible
  black-hole-related QFUDS source without a model-specific mapping.

## Check History

- 2026-06-10: arXiv abstract, DOI metadata, and availability links checked for
  black-hole-coupled source audit caching.
