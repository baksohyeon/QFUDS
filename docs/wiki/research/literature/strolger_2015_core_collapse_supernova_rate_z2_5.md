---
doc_id: lit_strolger_2015_core_collapse_supernova_rate_z2_5
title: Strolger 2015 Core-Collapse Supernova Rate to Redshift 2.5
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-10
record_type: literature_record
paper_year: 2015
availability_last_checked: 2026-06-10
used_by:
  - compact_object_transient_source_literature_audit
---

# Strolger 2015 Core-Collapse Supernova Rate to Redshift 2.5

## Bibliographic Metadata

- Paper: "The Rate of Core Collapse Supernovae to Redshift 2.5 From The
  CANDELS and CLASH Supernova Surveys"
- Authors: Louis-Gregory Strolger, Tomas Dahlen, Steven A. Rodney, Or Graur,
  Adam G. Riess, Curtis McCully, Swara Ravindranath, Bahram Mobasher,
  A. Kristin Shahady
- arXiv: [1509.06574](https://arxiv.org/abs/1509.06574)
- Journal reference: Astrophys. J. 813, 93 (2015)

## Key Equations

- Measures volumetric core-collapse supernova rates `R_CC(z)` from CANDELS and
  CLASH.
- Uses six redshift bins over `0.1 < z < 2.5`.

## Coupling Definitions

- No dark-sector coupling is defined.
- Candidate source variable: binned volumetric CCSN rate `R_CC(z)`.

## Datasets Used

- CANDELS supernova survey.
- CLASH supernova survey.
- Literature CCSN rate compilation.

## Redshift Coverage

- `0.1 < z < 2.5` for the HST survey measurement.
- The abstract reports an increase from local rates to values near `z ~ 2`.

## Available Products

- Paper PDF and arXiv source available.
- The paper reports rate bins and figures.
- No separate public chain, covariance, or QFUDS-ready source-history product
  found during this cache pass.

## Digitization Requirements

Optional for binned-rate use if table values in the paper are sufficient;
required for curve-level uncertainty propagation if no machine-readable product
is found.

## Public Code / Data Links

- arXiv: [1509.06574](https://arxiv.org/abs/1509.06574)

## QFUDS Relevance

Reference role: direct cosmic supernova-rate source history. It helps bound a
compact-object transient `X(z)` based on observed massive-star deaths.

## Use Restrictions

- Do not treat `R_CC(z)` as a physical energy-transfer law.
- Host extinction and luminosity-function systematics must remain visible if
  this source is used.

## Check History

- 2026-06-10: arXiv page checked for metadata, redshift range, source quantity,
  and product availability.
