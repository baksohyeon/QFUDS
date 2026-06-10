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
- `source_x/`: Source-X plans, conclusions, and coverage audits. Start at
  [source_x/README.md](source_x/README.md).

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
| index | [Source-X Research Audits](source_x/README.md) | chain index |
| 010 | [2026-06-10 Source-X Audit Plan](source_x/plans/010_phase1_source_x_audit_plan.md) | Phase 1 plan |
| 011 | [2026-06-10 Source-X Audit](source_x/conclusions/011_phase1_source_x_audit.md) | Phase 1 conclusion |
| 020 | [2026-06-10 Black-Hole-Coupled Source Audit Plan](source_x/plans/020_phase2_black_hole_coupled_source_audit_plan.md) | Phase 2 plan |
| 021 | [2026-06-10 Black-Hole-Coupled Source Audit](source_x/conclusions/021_phase2_black_hole_coupled_source_audit.md) | Phase 2 conclusion |
| 022 | [2026-06-10 Black-Hole-Coupled Literature Search Audit](source_x/coverage/022_phase2_black_hole_coupled_literature_search_audit.md) | Phase 2 coverage |
| 023 | [2026-06-10 Compact-Object Transient Source Literature Audit](source_x/coverage/023_phase2_compact_object_transient_source_literature_audit.md) | Phase 2 coverage |
| 024 | [2026-06-10 Structure-Era Activation Literature Audit](source_x/coverage/024_phase2_structure_era_activation_literature_audit.md) | Phase 2 coverage |
| 029 | [2026-06-10 Phase 2 Candidate Selection Closeout](source_x/conclusions/029_phase2_candidate_selection_closeout.md) | Phase 2 closeout |
| 030 | [2026-06-10 Phase 3 Q^nu Derivation Attempt Plan](source_x/plans/030_phase3_qnu_derivation_attempt_plan.md) | Phase 3 plan |
| 031 | [2026-06-10 Phase 3 Q^nu Derivation Attempt](source_x/conclusions/031_phase3_qnu_derivation_attempt.md) | Phase 3 feasibility result |
| 040 | [2026-06-10 Black-Hole Data Product Audit Plan](source_x/plans/040_black_hole_data_product_audit_plan.md) | data-product interlock plan |
