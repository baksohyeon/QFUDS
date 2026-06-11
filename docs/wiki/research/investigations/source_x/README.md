---
doc_id: source_x_investigation_index
title: Source-X Research Investigations
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - research_investigations_index
next_gate: none; navigation and audit routing only
last_updated: 2026-06-11
---

# Source-X Research Investigations

This folder separates Source-X investigation planning, conclusions, and
literature coverage. Coverage records can change the cache state or search
scope; only conclusion records state the current investigation decision.

## Subdirectories

- [plans/](plans/README.md): planned scope, search targets, and failure
  criteria.
- [conclusions/](conclusions/README.md): investigation conclusions and closeouts.
- [coverage/](coverage/README.md): coverage expansion and search-breadth
  checks.

## Filename Convention

Use phase-reserved prefixes:

```text
010-019  Phase 1: Source-X audit
020-029  Phase 2: Source-X candidate selection and coverage
030-039  Phase 3: Q^nu derivation attempt
040      Data-product interlock before Phase 4 derivation work
041-049  Product-recovery selection, extraction, and digitization follow-up
050-059  Phase 5: known-model distinction
060-069  Final: Level 2B admission audit
```

This keeps future derivation and admission records from colliding with coverage
records. The prefix is a route number, not a project-status claim.

## Current Read Order

| Order | Record | Role |
| ---: | --- | --- |
| 010 | [Source-X Audit Plan](plans/010_phase1_source_x_audit_plan.md) | Phase 1 plan |
| 011 | [Source-X Audit](conclusions/011_phase1_source_x_audit.md) | Phase 1 conclusion |
| 020 | [Black-Hole-Coupled Source Audit Plan](plans/020_phase2_black_hole_coupled_source_audit_plan.md) | Phase 2 plan |
| 021 | [Black-Hole-Coupled Source Audit](conclusions/021_phase2_black_hole_coupled_source_audit.md) | Phase 2 conclusion |
| 022 | [Black-Hole-Coupled Literature Search Audit](coverage/022_phase2_black_hole_coupled_literature_search_audit.md) | Phase 2 coverage |
| 023 | [Compact-Object Transient Source Literature Audit](coverage/023_phase2_compact_object_transient_source_literature_audit.md) | Phase 2 coverage |
| 024 | [Structure-Era Activation Literature Audit](coverage/024_phase2_structure_era_activation_literature_audit.md) | Phase 2 coverage |
| 029 | [Phase 2 Candidate Selection Closeout](conclusions/029_phase2_candidate_selection_closeout.md) | Phase 2 closeout |
| 030 | [Phase 3 Q^nu Derivation Attempt Plan](plans/030_phase3_qnu_derivation_attempt_plan.md) | Phase 3 plan |
| 031 | [Phase 3 Q^nu Derivation Attempt](conclusions/031_phase3_qnu_derivation_attempt.md) | Phase 3 feasibility result |
| 040 | [Black-Hole Data Product Audit Plan](plans/040_black_hole_data_product_audit_plan.md) | data-product interlock before Phase 4 |
| 040 | [Black-Hole Data Product Audit](conclusions/040_black_hole_data_product_audit.md) | data-product interlock result |
| 041 | [Product-Recovery Candidate Selection Plan](plans/041_product_recovery_candidate_selection_plan.md) | product-recovery candidate selection |
| 042 | [Product-Recovery Execution Plan](plans/042_product_recovery_execution_plan.md) | product-recovery extraction procedure |
| 043 | [Product-Recovery Extraction Plan](plans/043_product_recovery_extraction_plan.md) | product-recovery extraction execution scope |
| 043 | [Product-Recovery Extraction Result](conclusions/043_product_recovery_extraction_result.md) | product-recovery extraction closeout |
| 044 | [Numeric Digitization Planning Audit](plans/044_numeric_digitization_planning_audit.md) | numeric digitization target selection |
| 045 | [Chen Figure 5 Numeric Digitization Execution Plan](plans/045_chen_figure5_numeric_digitization_execution_plan.md) | Chen Figure 5 digitization execution specification |
| 046 | [Numeric Digitization Execution Plan](plans/046_numeric_digitization_execution_plan.md) | approved Chen Figure 5 numeric digitization scope |
| 046 | [Chen Figure 5 Numeric Digitization Result](conclusions/046_chen_figure5_numeric_digitization_result.md) | Chen Figure 5 numeric digitization closeout |
| 047 | [Chen-Gamma Shape Comparison Plan](plans/047_chen_gamma_shape_comparison_plan.md) | plan-only qualitative shape comparison scope |

Reserved future records:

| Prefix | Future record | Boundary |
| ---: | --- | --- |
| 048-049 | reserved product-recovery follow-up records | use only after the numeric product state is known; no perturbation viability claim without equations |
| 050 | `050_phase5_known_model_distinction.md` | compare against CCBH, IV/IDE, HDE, remnant-DM, and adjacent known models |
| 060 | `060_level2b_admission_audit.md` | final admission audit only after all required evidence exists |

## Short Interpretation

- `021` is the black-hole lane conclusion.
- `022` checks whether the black-hole conclusion was caused by missing
  black-hole literature.
- `023` expands into compact-object transient source histories: CCSN, DSNB,
  remnant formation, compact mergers, GWB, and r-process/kilonova sources.
- `024` expands beyond black-hole keywords into structure-era activation:
  backreaction, vacuum activation, emergent/transition DE, and nonparametric
  IDE.
- `029` closes Phase 2 and retains the black-hole-coupled lane for Phase 3 audit
  only.
- `030` plans the Phase 3 `Q^nu` feasibility audit without executing a
  derivation.
- `031` executes the Phase 3 feasibility audit and records that both retained
  lanes are data-product blocked.
- `040` is an intentional data-product interlock before Phase 4 delta-Q
  derivation work. It plans and records product coverage only; it does not
  derive `Q^nu`, open Level 2B, or modify roadmap status.
- `041` selects cached product-recovery candidates for future manual
  structuring or numeric digitization. It does not populate an extracted
  product, derive `delta Q`, open Level 2B, or modify roadmap status.
- `042` defines the extraction procedure for the selected Lacy and Chen
  product-recovery lanes. It does not extract or digitize values.
- `043` records both the extraction plan and the extraction-result closeout.
  The result confirms that manual structured extracts exist, but a
  QFUDS-usable numeric product does not.
- `044` selects the first numeric digitization target. It does not digitize,
  create a structured product, open Level 2B, or modify roadmap status.
- `045` defines how a future approved `046` task should digitize Chen Figure 5.
  It does not digitize, create a CSV, open Level 2B, or modify roadmap status.
- `046` records the approved numeric digitization execution scope for Chen
  Figure 5. The asset-level CSV remains a source-history candidate product, not
  a physical branch.
- `046` also includes a result closeout that records the product-state advance
  to `numeric_digitized` while preserving the `data_product_blocked` physical
  admission boundary.
- `047` plans a qualitative Chen-Gamma shape comparison. It does not execute the
  comparison, fit parameters, create candidate `X`, derive `Q^nu`, derive
  `delta Q`, open Level 2B, or modify roadmap status.
- None of these records opens Level 2B, modifies the roadmap, or creates a
  physical branch.

## Current Decision

The black-hole-coupled lane is not rejected because literature is absent.
External literature exists and is cached. The lane remains audit-only because no
checked source supplies all admission-rule items together:

```text
X =
Q^nu =
why phase B has w ~= -1 =
delta Q route =
known-model distinction =
```

The broader Source-X question is not closed by black-hole literature alone.
Coverage records `023` and `024` document additional source-history lanes and
search-keyword gaps, but they also leave the same physical-admission gap open.
