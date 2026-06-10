---
doc_id: lit_abbott_2023_gwtc3_population_merging_compact_binaries
title: Abbott 2023 GWTC-3 Population Merging Compact Binaries
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
  - compact_object_transient_source_literature_audit
---

# Abbott 2023 GWTC-3 Population Merging Compact Binaries

## Bibliographic Metadata

- Paper: "The population of merging compact binaries inferred using
  gravitational waves through GWTC-3"
- Authors: LIGO Scientific Collaboration, Virgo Collaboration, KAGRA
  Collaboration
- arXiv: [2111.03634](https://arxiv.org/abs/2111.03634)
- Journal reference: Phys. Rev. X 13, 011048 (2023)

## Key Equations

- Infers population properties and merger-rate distributions for compact
  binaries in GWTC-3.
- Covers binary black hole, binary neutron star, and neutron-star-black-hole
  mergers.

## Coupling Definitions

- No dark-sector coupling is defined.
- Candidate source variables: merger-rate density, redshift evolution of merger
  rate, class-specific BBH/BNS/NSBH rates.

## Datasets Used

- LIGO/Virgo/KAGRA compact-binary events through GWTC-3.
- Search sensitivity estimates and population-inference models.

## Redshift Coverage

- Detector-limited compact-binary redshift coverage. The public summary reports
  BBH rate evolution at a fiducial redshift `z = 0.2`; detailed posterior
  products are available through the data release.

## Available Products

- Paper PDF available through arXiv.
- Zenodo data release includes figure/table data and population parameter
  samples.
- Separate GWTC-3 event posterior products and search-sensitivity estimates are
  public through LVK/GWOSC/Zenodo releases.

## Digitization Requirements

Not needed for many population-rate products if the Zenodo release is sufficient.
Still required only for figures not represented in the release.

## Public Code / Data Links

- arXiv: [2111.03634](https://arxiv.org/abs/2111.03634)
- Zenodo data release:
  [10.5281/zenodo.11254021](https://zenodo.org/records/11254021)
- GWTC-3 event posterior release:
  [Zenodo 8177023](https://zenodo.org/records/8177023)

## QFUDS Relevance

Reference role: primary compact-object merger-rate source for BBH, BNS, and
NSBH axes.

It can help define an empirical `X(a)` for merger-rate histories. It does not
define `Q^nu`, `w ~= -1`, or `delta Q`.

## Use Restrictions

- Use LVK rate conventions and selection effects explicitly.
- Do not treat merger-rate timing overlap as physical support for QFUDS.

## Check History

- 2026-06-10: arXiv and Zenodo data-release pages checked for metadata, merger
  classes, product links, and QFUDS-use limitations.
