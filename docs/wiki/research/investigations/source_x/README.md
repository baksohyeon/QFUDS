---
doc_id: source_x_investigation_index
title: Source-X Research Investigations
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - research_investigations_index
next_gate: candidate-equation template only; do not open Level 2B
last_updated: 2026-06-18
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
041-047  Product-recovery selection, extraction, digitization, and shape comparison follow-up
048      Phase 5: known-model distinction for the Chen-Gamma lane
049      Level 2B admission eligibility review and foam-sector feasibility plan
050      Foam-sector-to-Gamma feasibility result
051-059  Later Phase 5 or admission follow-up
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
| 047 | [Chen-Gamma Shape Comparison Result](conclusions/047_chen_gamma_shape_comparison_result.md) | qualitative Chen-Gamma shape comparison closeout |
| 048 | [Known-Model Distinction Audit Plan](plans/048_known_model_distinction_audit_plan.md) | plan-only known-model distinction audit scope |
| 048 | [Known-Model Distinction Audit Result](conclusions/048_known_model_distinction_audit_result.md) | Phase 5 known-model distinction closeout |
| 049 | [Foam-Sector-to-Gamma Derivation Feasibility Plan](plans/049_foam_sector_to_gamma_derivation_feasibility_plan.md) | forward-direction feasibility plan; no derivation or admission |
| 049 | [Level 2B Admission Eligibility Review and Observer-Mode Routing](conclusions/049_level2b_eligibility_review_and_observer_mode.md) | gate-check verdict; routes the lane to observer mode |
| 050 | [Foam-Sector-to-Gamma Derivation Feasibility Result](conclusions/050_foam_sector_to_gamma_derivation_feasibility_result.md) | forward-direction feasibility closeout; minimum objects missing |
| 051 | [Effective Phase-Fraction Scaffold](conclusions/051_effective_phase_fraction_scaffold.md) | weak single-sector phase-fraction scaffold; analytic density only |
| 052 | [Foam-State Variable Literature Question Plan](plans/052_foam_state_variable_literature_question_plan.md) | question plan for literature-neighbor state variables before selecting `xi` |
| 052 | [Foam-State Variable Literature Question Result](conclusions/052_foam_state_variable_literature_question_result.md) | executes the `xi_gal`/known-model-sink question; no `xi` selected |
| 053 | [Black-Hole Vacuum Foam Falsifiability Ledger](conclusions/053_black_hole_vacuum_foam_falsifiability_ledger_ko.md) | integrated falsifiability ledger for five public-origin questions; no Level 2B |
| 054 | [Candidate Equation Template Attempts](conclusions/054_candidate_equation_template_attempts_ko.md) | applies the candidate-equation template to all five routes; no route admitted |
| 055 | [Academic Derivation Bridge](conclusions/055_academic_derivation_bridge_ko.md) | translates retained `Gamma(a)` into academic IV/IDE source-term language; no physical branch |
| 056 | [IV/IDE Formalism Study Map](conclusions/056_iv_ide_formalism_study_map_ko.md) | defines the safe study route from `Q` to `Q^mu`, perturbations, stability, and likelihood readiness |
| 057 | [IV/IDE Formalism Notes Ledger](conclusions/057_iv_ide_formalism_notes_ledger_ko.md) | executes the first formalism ledger: background `Q`, `Q^mu` frame, perturbation closure, and stop rules |
| 058 | [Paper-by-Paper IV/IDE Equation Extraction Plan](plans/058_paper_by_paper_iv_ide_equation_extraction_plan_ko.md) | plans exact per-paper extraction before any timing fit or observational constraint use |
| 059 | [Li 2025 IV/IDE Equation Extraction Result](conclusions/059_li_2025_iv_ide_equation_extraction_result_ko.md) | executes the Li 2025 pilot extraction; comparator only, no QFUDS admission |
| 059 | [Escamilla 2023 IV/IDE Kernel Equation Extraction Result](conclusions/059_escamilla_2023_iv_ide_kernel_equation_extraction_result_ko.md) | executes the Escamilla 2023 background-kernel extraction; background-only stop |
| 059 | [Li/Escamilla IV/IDE Convention Comparison Note](conclusions/059_li_escamilla_iv_ide_convention_comparison_note_ko.md) | compares the two extracted conventions before any timing fit or baseline-constraint use |

Reserved future records:

| Prefix | Future record | Boundary |
| ---: | --- | --- |
| 051-059 | reserved later Phase 5 or admission follow-up | do not use to bypass the 048 Chen-Gamma distinction result or 050 feasibility result |
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
- `047` also includes a result closeout that records limited qualitative
  timing-shape resemblance and material peak/tail mismatch. It preserves the
  `data_product_blocked` boundary and makes no QFUDS support claim.
- `048` plans a known-model distinction audit for the current black-hole
  entropy / Chen-Gamma lane. It does not execute the audit, claim novelty,
  define candidate `X`, derive `Q^nu`, derive `delta Q`, open Level 2B, or
  modify roadmap status.
- `048` also includes a result closeout that executes Phase 5 known-model
  distinction for the current Chen-Gamma lane. It finds no supported
  known-model distinction and leaves all five admission-rule items blocked.
- `049` is the Level 2B admission eligibility review. It finds the lane
  ineligible for Level 2B because all five admission-rule items remain
  unsatisfied, frames the outcome as audit success rather than model success or
  failure, and routes the lane to observer mode with an external watchlist
  (DESI DR3, Euclid, Roman, Rubin/LSST, CCBH, entropic/IV-IDE products). It does
  not open Level 2B and does not itself modify roadmap status.
- `049` also includes a forward-direction foam-sector-to-`Gamma(a)` feasibility
  plan. It defines the minimum mathematical objects needed before attempting a
  derivation from foam-sector phase structure to a `Gamma(a)`-like profile. It
  does not perform the derivation, admit a physical source, open Level 2B, or
  modify roadmap status.
- `050` executes the foam-sector-to-`Gamma(a)` feasibility plan. It finds that
  the route is not ready for derivation because the minimum objects are missing:
  no foam-sector state variable, no calculable phase definitions, no replacement
  transition object, and no foam-sector equation set. It does not open Level 2B
  or modify roadmap status.
- `051` relaxes the foam-sector route into a weak one-sector effective
  phase-fraction scaffold. It derives the analytic background density for a
  smooth `f_B(a)`/`w_D(a)` ansatz without using `Gamma(a)`, deriving a physical
  source, opening Level 2B, or modifying roadmap status.
- `052` plans the next question pass: before choosing `xi ~= 10 Mpc`, ask
  whether nearby literature variables already absorb the idea through EFTofLSS,
  backreaction, running vacuum, screened modified gravity, spacetime-foam
  correlation, stochastic Lambda, or the internal phase-fraction scaffold. It
  does not select `xi`, define candidate `X`, open Level 2B, or modify roadmap
  status.
- `052` also includes a result closeout. It finds `xi_gal` not ready as a QFUDS
  state variable because the candidate scale is first absorbed by EFTofLSS,
  backreaction, screened modified gravity, running vacuum, stochastic Lambda,
  or a neighboring spacetime-foam dark-energy comparator.
- `053` integrates five public-origin questions into a falsifiability ledger:
  black-hole information, vacuum energy, evaporation information return,
  white-hole/remnant storage, and galaxy-scale foam. It preserves the questions
  as audit material and records kill conditions, but it does not create QFUDS
  support, validation, novelty, or Level 2B admission.
- `054` applies the candidate-equation template to the same five routes. Each
  route remains blocked or rejected because it cannot fill the required source
  object, phase-B pressure, transfer vector, perturbation route, and
  known-model escape equation together.
- `055` translates the retained `Gamma(a)` intuition into academic
  interacting-vacuum / interacting-dark-energy language. It records that the
  bridge is useful for learning `Q`, `Q^mu`, transfer frames, perturbation
  closure, and constraints, but it does not derive physical QFUDS or open
  Level 2B.
- `056` turns that bridge into a study map: model taxonomy, background `Q`,
  covariant `Q^mu`, perturbation closure, stability, and likelihood readiness.
  It is a learning route and guardrail against repeating brute-force fitting,
  not a new QFUDS branch.
- `059` includes the Li 2025 pilot extraction and the Escamilla 2023
  background-kernel extraction. Together they show why retained `Gamma(a)` can
  be a formalism comparator but still cannot be used as a physical source:
  Li supplies `Q^mu`/frame/ePPF machinery while Escamilla stops at a
  background kernel.
- `059` also includes a convention-comparison note. It freezes the translation
  hazards before any retained-timing fit, NASA/BAO/CMB/LSS interpretation, or
  next-target literature extraction.
- None of these records opens Level 2B, changes roadmap status, or creates a
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
