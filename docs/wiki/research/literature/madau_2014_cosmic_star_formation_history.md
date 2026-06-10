---
doc_id: lit_madau_2014_cosmic_star_formation_history
title: Madau 2014 Cosmic Star Formation History
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-10
record_type: literature_record
paper_year: 2014
availability_last_checked: 2026-06-10
used_by:
  - compact_object_transient_source_literature_audit
---

# Madau 2014 Cosmic Star Formation History

## Bibliographic Metadata

- Paper: "Cosmic Star Formation History"
- Authors: Piero Madau, Mark Dickinson
- arXiv: [1403.0007](https://arxiv.org/abs/1403.0007)
- Journal reference: Annual Review of Astronomy and Astrophysics 52, 415-486
  (2014)

## Key Equations

- Reviews empirical star-formation-rate density histories.
- Provides a standard source-history comparator for massive-star birth and
  delayed compact-object transient production.

## Coupling Definitions

- No dark-sector coupling `Q` is defined.
- Candidate source variable for later audit: cosmic star-formation-rate density
  or a massive-star death proxy derived from it.

## Datasets Used

- Multiwavelength galaxy survey compilations from far-UV to far-IR.

## Redshift Coverage

- Cosmic star-formation history from early cosmic time to the present.
- The arXiv abstract reports a peak at approximately `z ~ 1.9`.

## Available Products

- Paper PDF and arXiv source available.
- NED review page exposes tabulated literature values used in the review.
- No QFUDS-ready compact-object production history is provided directly.

## Digitization Requirements

Not needed for high-level timing comparison if tabulated SFRD values are used
from the review page. A compact-object source history would still require a
separate conversion model and uncertainty propagation.

## Public Code / Data Links

- arXiv: [1403.0007](https://arxiv.org/abs/1403.0007)
- NED review page with tables:
  [Cosmic Star Formation History](https://ned.ipac.caltech.edu/level5/March14/Madau/Madau5.html)

## QFUDS Relevance

Reference role: background source-history anchor for massive-star death,
core-collapse, remnant formation, and delayed merger histories.

It can help define a phenomenological `X(a)` proxy only after a declared
conversion from star formation to compact-object production.

## Use Restrictions

- Do not treat SFRD timing overlap as evidence for QFUDS.
- Do not use star-formation history as `Q^nu`, `w ~= -1` rationale, or
  `delta Q` without additional physics.

## Check History

- 2026-06-10: arXiv and NED pages checked for metadata, source quantity, peak
  redshift, and public data availability.
