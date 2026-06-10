---
doc_id: lit_sukhbold_2016_core_collapse_remnant_masses
title: Sukhbold 2016 Core-Collapse Remnant Masses
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-10
record_type: literature_record
paper_year: 2016
availability_last_checked: 2026-06-10
used_by:
  - compact_object_transient_source_literature_audit
---

# Sukhbold 2016 Core-Collapse Remnant Masses

## Bibliographic Metadata

- Paper: "Core-Collapse Supernovae from 9 to 120 Solar Masses Based on
  Neutrino-powered Explosions"
- Authors: Tuguldur Sukhbold, T. Ertl, S. E. Woosley, Justin M. Brown,
  H.-T. Janka
- arXiv: [1510.04643](https://arxiv.org/abs/1510.04643)
- Journal reference: Astrophys. J. 821, 38 (2016)

## Key Equations

- Evolves massive-star progenitors from 9 to 120 solar masses through
  neutrino-powered explosion models.
- Reports explosion outcomes, remnant masses, nucleosynthesis, and black-hole
  formation in non-exploding progenitors.

## Coupling Definitions

- No dark-sector coupling is defined.
- Candidate source variables: neutron-star remnant mass distribution,
  black-hole remnant mass distribution, failed-explosion outcome map.

## Datasets Used

- Solar-metallicity massive-star progenitor grid.
- One-dimensional calibrated neutrino-transport explosion model.

## Redshift Coverage

- No cosmological redshift history. This is a progenitor-to-remnant conversion
  record for use with an external star-formation or metallicity history.

## Available Products

- Paper PDF and arXiv source available.
- MPA Garching supplementary archive provides calculation/model data.
- No direct cosmic `X(a)` product is provided; the record needs convolution with
  a cosmic progenitor history.

## Digitization Requirements

Not needed for progenitor-grid use if the MPA archive products are sufficient.
Required only if later work uses paper-only figures not present in the archive.

## Public Code / Data Links

- arXiv: [1510.04643](https://arxiv.org/abs/1510.04643)
- Supplementary archive:
  [MPA CCSN archive SEWBJ 2015](https://wwwmpa.mpa-garching.mpg.de/ccsnarchive/data/SEWBJ_2015/index.html)

## QFUDS Relevance

Reference role: remnant-formation mapping. It can help convert massive-star
death histories into neutron-star or black-hole formation source histories.

## Use Restrictions

- Do not treat a remnant formation map as a cosmological energy-transfer law.
- It supplies no `Q^nu`, no phase-B pressure rationale, and no perturbation
  route.

## Check History

- 2026-06-10: arXiv and MPA archive pages checked for metadata, source
  variables, product links, and redshift limitation.
