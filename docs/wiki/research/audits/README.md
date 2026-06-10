---
doc_id: research_audit_index
title: Research Audits
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - research_cache_index
next_gate: none; dated research audit records only
last_updated: 2026-06-10
---

# Research Audits

This folder stores dated research-cache audits, audit plans, feasibility checks,
and availability checks.

Use subdirectories for audit chains. Do not add new dated files directly under
this folder unless they are one-off index-level records.

## Filename Convention

Use chain-local execution order:

```text
<chain>/<NNN>_<short_name>.md
```

The date remains in the document title, frontmatter, and body. The filename
should optimize navigation by research flow, not by calendar grouping.

Current chains:

- `exp006_timing/`: IV/IDE timing and Li 2025 data-product audits.
- `source_x/`: Source-X and black-hole-coupled source audit plans/results.

## Record Boundaries

Research-cache audits may record:

- search queries;
- source pages checked;
- public tables, chains, posterior samples, covariance matrices, code, and
  figures found;
- products not found;
- whether author data or figure digitization is likely required;
- plan boundaries for a later audit;
- feasibility checks and reduction-test routing.

Research-cache audits must not replace experiment documents, result documents,
decision logs, or the roadmap. A cached "not found" entry means only that the
product was not found in the checked sources on the recorded date.

## Exp006 Timing Chain

| Order | Record | Type |
| ---: | --- | --- |
| 001 | [2026-06-09 Exp006 Literature Availability Audit](exp006_timing/001_literature_availability_audit.md) | availability audit |
| 002 | [2026-06-09 Exp006 Sharpening Path Audit](exp006_timing/002_sharpening_path_audit.md) | sharpening audit |
| 003 | [2026-06-09 Exp006 Coverage Expansion Audit](exp006_timing/003_coverage_expansion_audit.md) | coverage audit |
| 004 | [2026-06-09 Li 2025 Timing Feasibility Audit](exp006_timing/004_li_2025_timing_feasibility_audit.md) | feasibility audit |
| 005 | [2026-06-09 Li 2025 Timing-Overlap Matrix Plan](exp006_timing/005_li_2025_timing_overlap_matrix_plan.md) | plan |
| 006 | [2026-06-09 Li 2025 Public Product Search Audit](exp006_timing/006_li_2025_public_product_search_audit.md) | availability audit |
| 007 | [2026-06-09 Li 2025 Digitized Compression Audit](exp006_timing/007_li_2025_digitized_compression_audit.md) | digitized compression audit |

## Source-X Chain

| Order | Record | Type |
| ---: | --- | --- |
| 001 | [2026-06-10 Source-X Audit Plan](source_x/001_source_x_audit_plan.md) | plan |
| 002 | [2026-06-10 Source-X Audit](source_x/002_source_x_audit.md) | audit |
| 003 | [2026-06-10 Black-Hole-Coupled Source Audit Plan](source_x/003_black_hole_coupled_source_audit_plan.md) | plan |
