---
doc_id: lit_horiuchi_2011_cosmic_core_collapse_supernova_rate
title: Horiuchi 2011 Cosmic Core-Collapse Supernova Rate
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-10
record_type: literature_record
paper_year: 2011
availability_last_checked: 2026-06-10
used_by:
  - compact_object_transient_source_literature_audit
---

# Horiuchi 2011 Cosmic Core-Collapse Supernova Rate

## Bibliographic Metadata

- Paper: "The Cosmic Core-collapse Supernova Rate does not match the
  Massive-Star Formation Rate"
- Authors: Shunsaku Horiuchi, John F. Beacom, Christopher S. Kochanek,
  Jose L. Prieto, K. Z. Stanek, Todd A. Thompson
- arXiv: [1102.1977](https://arxiv.org/abs/1102.1977)
- Journal reference: Astrophys. J. 738, 154 (2011)

## Key Equations

- Compares measured cosmic core-collapse supernova rate against the rate
  predicted from massive-star formation.
- Identifies a factor-of-order-two supernova-rate problem in the checked
  literature record.

## Coupling Definitions

- No dark-sector coupling is defined.
- Candidate source variable: cosmic core-collapse rate density or inferred
  hidden/dark collapse rate.

## Datasets Used

- Literature compilation of cosmic star-formation and core-collapse supernova
  rate measurements.
- Local-volume supernova discovery study for dim or missed supernovae.

## Redshift Coverage

- Uses cosmic rate measurements over low-to-intermediate redshift as available
  in 2011. No single QFUDS-ready binned table was found in this cache pass.

## Available Products

- Paper PDF and arXiv source available.
- No public posterior chain, covariance, or machine-readable compact-object
  source history found during this cache pass.

## Digitization Requirements

Likely required for curve-level use unless a later product search finds the
underlying rate compilation in machine-readable form.

## Public Code / Data Links

- arXiv: [1102.1977](https://arxiv.org/abs/1102.1977)

## QFUDS Relevance

Reference role: core-collapse source-rate comparator and warning that observed
optical supernova rates may miss dim or failed collapses.

It can help define a candidate `X(a)` only as a rate-history input. It does not
define `Q^nu`, phase-B pressure, or `delta Q`.

## Use Restrictions

- Do not treat missing optical supernovae as dark energy.
- Do not identify hidden collapses with a smooth vacuum-pressure component
  without a stress-energy derivation.

## Check History

- 2026-06-10: arXiv page checked for metadata, rate-problem finding, source
  quantity, and product availability.
