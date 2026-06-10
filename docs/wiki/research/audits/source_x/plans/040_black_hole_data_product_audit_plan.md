---
doc_id: audit_2026_06_10_black_hole_data_product_audit_plan
title: "2026-06-10 Black-Hole Data Product Audit Plan"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_phase3_qnu_derivation_attempt
  - audit_2026_06_10_phase3_qnu_derivation_attempt_plan
  - audit_2026_06_10_phase2_candidate_selection_closeout
  - audit_2026_06_10_black_hole_coupled_literature_search
  - literature_cache_index
  - roadmap
  - repository_levels_glossary
  - missing_physics_map
  - blocked_admission_rule_checkpoint
next_gate: audit only whether required black-hole data products exist; no derivation
last_updated: 2026-06-10
---

# 2026-06-10 Black-Hole Data Product Audit Plan

## Purpose

Plan a dated, scope-limited product-coverage audit for the retained black-hole
quantities after the Phase 3 `Q^nu` feasibility result.

Current Phase 3 state: `data_product_blocked`.

This plan asks only whether usable data products can be constructed for:

- Lane A: `rho_BH(a)` or `d rho_BH / dln(a)`.
- Lane B: `S_BH(a)` or `dS_BH / dln(a)`.

This document is the plan for a future audit. It does not perform external
product recovery, download assets, extract tables, digitize figures, or derive a
physical transfer law.

## Status Boundary

This interlock is `data_product_blocked`, not physics_blocked.

The distinction matters:

- `data_product_blocked` means the retained lanes may be testable only after a
  source history, units, uncertainty, redshift coverage, and normalization route
  are located or reconstructed.
- `not physics_blocked` means this audit has not proven that no physical
  black-hole route can exist.
- It also has not shown that a physical route exists.

Do not derive Q^nu.

Do not open Physical-QFUDS Level 2B.

Do not modify roadmap status.

Do not treat a product hit as physical admission. A product can define a
candidate `X` without supplying:

```text
Q^nu =
why phase B has w ~= -1 =
delta Q route =
known-model distinction =
```

## Product-State Definitions

The future audit must use these product-state distinctions:

| State | Definition |
| --- | --- |
| `literature exists` | Relevant paper or model exists, but no extractable product has been confirmed. |
| `data product exists` | Figures, tables, code, samples, or downloadable assets exist. |
| `reproducible data product exists` | Public data/code or numeric tables allow reconstruction with documented units and uncertainty. |
| `QFUDS-usable data product exists` | Product has units, redshift coverage, uncertainty, normalization route, provenance, and can define `X`; it still does not by itself admit `Q^nu`. |

Candidate classifications:

```text
literature_only
data_product_exists
reproducible_data_product_exists
qfuds_usable_candidate
inaccessible
irrelevant
```

A literature hit, data-product hit, reproducibility hit, and QFUDS-usable hit
are not the same thing.

If a paper exists but has no extractable data product, record it as literature
hit / product miss.

If data exists but lacks units, uncertainty, redshift coverage, or a
normalization route, record it as product hit / QFUDS miss.

## Candidate Lanes

| Lane | Candidate product | Audit question |
| --- | --- | --- |
| Lane A | `rho_BH(a)` or `d rho_BH / dln(a)` | Can a black-hole mass-density or growth-history product define a candidate `X` with usable units, redshift coverage, uncertainty, normalization route, and provenance? |
| Lane B | `S_BH(a)` or `dS_BH / dln(a)` | Can a cosmic black-hole entropy or entropy-growth product define a candidate `X` with usable units, redshift coverage, uncertainty, normalization route, and provenance? |

Both lanes remain audit material only.

## Lane A Product Search Plan

Search axes:

- SMBH mass density evolution.
- Black-hole mass function evolution.
- Accretion history reconstructions.
- Black-hole growth histories.
- Merger-driven growth products.

For each axis, the future audit must check whether a candidate source supplies:

- literature source;
- public data availability;
- reproducibility;
- units;
- redshift coverage;
- uncertainty;
- update frequency;
- whether it can define `X`;
- whether it could eventually support `Q^nu`;
- final classification.

Priority starting points:

- Farrah 2023 and Croker 2024 for cosmologically coupled black-hole comparator
  pressure.
- Lacy 2024 for SMBH accretion-history constraints.
- Amendola 2024 and LVK/GWTC products for gravitational-wave population and
  merger-growth products.
- Repaired black-hole literature cache records for constraint and critique
  routing.

## Lane B Product Search Plan

Search axes:

- Black-hole entropy inventories.
- Cosmic entropy budgets.
- SMBH entropy evolution.
- Remnant entropy accounting.
- Entropy history reconstructions.

For each axis, the future audit must check whether a candidate source supplies:

- literature source;
- public data availability;
- reproducibility;
- units;
- redshift coverage;
- uncertainty;
- update frequency;
- whether it can define `X`;
- whether it could eventually support `Q^nu`;
- final classification.

Priority starting points:

- Entropy and topology comparators in the repaired black-hole literature cache.
- Remnant comparator notes for white-hole, Planck-star, and compact-remnant
  accounting.
- Any explicit cosmic entropy budget that exposes black-hole mass functions,
  entropy normalization, and redshift-dependent reconstruction inputs.

## Literature/Product Search Trace

The future audit must record search coverage and cache status, not only final
candidate products.

For every search axis, include a hit/miss/cache table with these columns:

| Search axis | Query keywords used | Source found | Source status | Product status | Cache action | Reason for inclusion or rejection |
| --- | --- | --- | --- | --- | --- | --- |
| placeholder | placeholder | placeholder | placeholder | placeholder | placeholder | placeholder |

Allowed source status values:

```text
already_cached
externally_found_and_cached
externally_found_not_cached
inaccessible
irrelevant
no_useful_hit
```

Allowed product status values:

```text
no_product
figure_only
table_available
code_available
downloadable_data_available
reconstructable_from_paper
qfuds_usable_candidate
```

Allowed cache action values:

```text
reused_existing_cache
created_literature_cache
created_product_cache
recorded_gap_only
```

Cache locations:

- Literature notes go under [Literature Cache](../../../literature/).
- Data-product audit results go under
  [Source-X Research Audits](../README.md).
- Raw or extracted assets go under `docs/wiki/research/assets/` only when
  actually downloaded or extracted.

Do not imply exhaustive literature coverage. This remains a dated,
scope-limited product-coverage audit.

## Candidate Product Evaluation Matrix

For every candidate product, record:

| Candidate | Lane | Literature source | Public data availability | Reproducible? | Units | Redshift coverage | Uncertainty | Update frequency | Can define `X`? | Could eventually support `Q^nu`? | Classification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| placeholder | A or B | placeholder | placeholder | placeholder | placeholder | placeholder | placeholder | placeholder | placeholder | placeholder | placeholder | placeholder |

Evaluation rules:

- Classify a paper without extractable data as `literature_only`.
- Classify a figure, table, code link, sample, or downloadable file as
  `data_product_exists` only if the product is identifiable.
- Classify as `reproducible_data_product_exists` only if the product can be
  reconstructed with documented units and uncertainty.
- Classify as `qfuds_usable_candidate` only if the product has units, redshift
  coverage, uncertainty, normalization route, provenance, and can define `X`.
- Classify inaccessible products as `inaccessible`, even if a paper claims they
  exist.
- Classify products outside Lane A and Lane B as `irrelevant` for this audit.

## Evidence Sources To Search

Start from repository evidence:

- [2026-06-10 Phase 3 Q^nu Derivation Attempt](../conclusions/031_phase3_qnu_derivation_attempt.md)
- [2026-06-10 Phase 3 Q^nu Derivation Attempt Plan](030_phase3_qnu_derivation_attempt_plan.md)
- [2026-06-10 Phase 2 Candidate Selection Closeout](../conclusions/029_phase2_candidate_selection_closeout.md)
- [2026-06-10 Black-Hole-Coupled Literature Search Audit](../coverage/022_phase2_black_hole_coupled_literature_search_audit.md)
- [Literature Cache](../../../literature/README.md)
- [Missing Physics Map](../../../../checkpoints/missing_physics_map.md)
- [Blocked Admission Rule](../../../../checkpoints/blocked-admission-rule.md)
- [Repository Levels](../../../../glossary/repository_levels.md)
- [Roadmap](../../../../../05_next_steps/000_roadmap.md)

Named starting records include Farrah 2023, Croker 2024, Lacy 2024, Amendola
2024, LVK/GWTC products, and entropy/remnant comparator notes.

The future audit may perform external product recovery. It must record the query
terms, source status, product status, cache action, and reason for inclusion or
rejection for each search axis.

## Acceptance Criteria

The future audit is complete when it:

- records search coverage for every Lane A and Lane B axis;
- distinguishes literature hit, data-product hit, reproducibility hit, and
  QFUDS-usable hit;
- classifies every candidate as one of the required candidate classifications;
- records cache status and cache action for every search axis;
- identifies whether any candidate can define `X`;
- states whether any candidate could eventually support `Q^nu`;
- preserves the `data_product_blocked` versus `not physics_blocked` boundary;
- records all product misses as dated, scope-limited findings.

## Failure Criteria

A candidate fails as QFUDS-usable for this audit if it:

- has only literature and no extractable product;
- has only a figure with no recoverable axis units or uncertainty;
- lacks redshift coverage;
- lacks uncertainty or a route to uncertainty;
- lacks a normalization route;
- lacks provenance;
- cannot define `X`;
- could only support `Q^nu` by circularly fitting retained `Gamma(a)`;
- reduces directly to a known black-hole-coupled dark-energy or entropy model
  without a distinct QFUDS route.

The audit itself fails if it collapses literature hits, data-product hits,
reproducibility hits, and QFUDS-usable hits into one category.

## Reporting Requirements

The future audit report must include:

- one search trace table per search axis;
- one candidate product evaluation matrix;
- separate Lane A and Lane B conclusions;
- explicit cache actions for new or reused records;
- a dated statement of products not found;
- a statement that any "not found" result is limited to sources checked on the
  audit date;
- a no-derivation confirmation.

If the audit downloads or extracts assets, it must add an asset README under
`docs/wiki/research/assets/` describing source, method, files, and limitations.

If the audit creates new literature notes, it must update
[Literature Cache](../../../literature/README.md) and
`docs/wiki/research/literature/index.csv`.

## Level 2B / Roadmap Boundary

Physical-QFUDS Level 2B remains blocked.

Roadmap unchanged.

This plan does not modify roadmap status, roadmap level, decision-log state, or
the current retained branch classification.

This plan does not derive `Q^nu`, does not open Physical-QFUDS Level 2B, and
does not convert a black-hole data product into a physical source mechanism.

The next admissible step is only a data-product audit that records whether the
required black-hole products exist and whether any product can define a
candidate `X`.
