---
doc_id: lit_kresse_2021_stellar_collapse_diversity_dsnb
title: Kresse 2021 Stellar Collapse Diversity DSNB
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-10
record_type: literature_record
paper_year: 2021
availability_last_checked: 2026-06-10
used_by:
  - compact_object_transient_source_literature_audit
---

# Kresse 2021 Stellar Collapse Diversity DSNB

## Bibliographic Metadata

- Paper: "Stellar Collapse Diversity and the Diffuse Supernova Neutrino
  Background"
- Authors: Daniel Kresse, Thomas Ertl, Hans-Thomas Janka
- arXiv: [2010.04728](https://arxiv.org/abs/2010.04728)
- Journal reference: Astrophys. J. 909, 169 (2021)

## Key Equations

- Computes diffuse supernova neutrino background predictions from landscapes of
  successful and failed stellar collapses.
- Varies explosion-engine strength, failed-supernova fraction, neutron-star mass
  limit, neutrino spectra, and alternative neutron-star formation channels.

## Coupling Definitions

- No dark-sector coupling is defined.
- Candidate source variables: total stellar core-collapse rate, failed-collapse
  fraction, black-hole-forming collapse contribution, DSNB flux.

## Datasets Used

- Sukhbold and Ertl stellar-collapse model sets.
- Proto-neutron-star cooling simulations.
- Cosmic stellar core-collapse rate assumptions.

## Redshift Coverage

- Cosmological DSNB integral over past stellar collapses. No public binned
  collapse-history product was found in this cache pass.

## Available Products

- Paper PDF and arXiv source available.
- Paper reports figures and tables.
- No public posterior chains, compact-object production table, or QFUDS-ready
  `X(a)` product found during this cache pass.

## Digitization Requirements

Likely required for curve-level use unless the needed table can be extracted
from the paper source or author data.

## Public Code / Data Links

- arXiv: [2010.04728](https://arxiv.org/abs/2010.04728)

## QFUDS Relevance

Reference role: DSNB and failed-collapse comparator. It is useful because failed
stellar collapses can form black holes without ordinary optical transient
visibility.

## Use Restrictions

- DSNB flux is not dark energy.
- Failed-collapse timing does not explain `w ~= -1` without a separate
  stress-energy receiver model.

## Check History

- 2026-06-10: arXiv page checked for metadata, source variables, DSNB role, and
  product availability.
