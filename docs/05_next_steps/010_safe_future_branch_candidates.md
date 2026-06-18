---
doc_id: safe_future_branch_candidates
title: Safe Future Branch Candidates
doc_type: guide
stage: "2"
status: in_progress
evidence_role: audit
depends_on:
  - roadmap
  - wiki_governance_003_blocked_admission_rule_gate
  - result_005_timing_prior_usefulness
  - result_006_literature_timing_support_audit
  - qfuds_strong_gravity_source_mechanism_audit
  - audit_2026_06_18_candidate_equation_triage_closeout
next_gate: choose only safe non-Level-2B branch work; candidate-equation template first
last_updated: 2026-06-18
---

# Safe Future Branch Candidates

## Status Boundary

This document lists safe follow-up branches after the accepted physical-branch
audit. It does not update roadmap status and does not open Physical-QFUDS
[Level 2B](../wiki/glossary/repository_levels.md).

Current status remains governed by
[000_roadmap.md](000_roadmap.md). The retained branch remains classified as
phenomenological IV/IDE and not yet a physical model.

Workflow boundary: this guide applies the
[Research Asset and Product Workflow](../../.agent/workflows/research-asset-product-workflow.md)
only to preserve source-state boundaries. No new external asset, table, PDF,
or product claim is introduced here. Existing baseline states remain
`asset_cached`, `manual_structured_extract`, `asset_extracted_not_digitized`,
and `direct_table` as recorded in the baseline-reference chain.

## Allowed Safe Branches

| Branch | Allowed scope | Required boundary |
| --- | --- | --- |
| IV/IDE timing-prior test | Compare retained structure-era timing against reconstructed or tomographic IV/IDE timing products. | Phenomenological only; no physical QFUDS claim. |
| black-hole-coupled source audit | Ask whether black-hole production, mass growth, or coupled-vacuum histories can define a candidate `X`. | Audit only unless it supplies all admission-rule items. |
| HDE reduction test | Test whether a horizon or holographic route reduces QFUDS to known HDE or interacting vacuum. | Known-model reduction test, not physical promotion. |
| remnant-sector audit as DM-only, not DE | Treat remnants as compact-object or defect-sector candidates. | Do not use remnants as a DE source unless smooth vacuum-pressure stress-energy is derived. |
| causal-set Lambda comparison as separate DE comparison | Compare stochastic or causal-set Lambda behavior as an adjacent DE model. | Separate DE comparison, not a DM-to-DE phase-transfer branch. |
| galaxy/cosmic-web coarse-graining hypothesis | Ask whether foam language can be made meaningful only after averaging over a preregistered galaxy/cosmic-web scale `xi_gal`. | `xi_gal` is an input unless derived by an equation; no NASA/BAO/LSS target may be used to choose it; known-model reduction must be checked first. |

## Forbidden Physical Branches

Do not create Landauer, generic quantum foam, or white-hole physical branches
unless the proposal introduces equations, observables, or falsifiable tests.

Also do not create a physical branch from:

- retained `Gamma(a)` timing alone;
- a fitted source profile without a physical `X`;
- a galaxy-scale or cosmic-web-scale label without a preregistered `xi_gal`,
  an effective stress tensor or geometry equation, and a known-model sink test;
- broad entropy or information language;
- a `Q^nu` ansatz that only reproduces the background equations;
- a remnant or compact-object story that produces radiation or compact DM, not
  smooth `w ~= -1` phase B.

## Required Evidence Anchors

Use existing repo records before adding any new literature summary:

- [030_result_005_timing_prior_usefulness.md](../04_results/030_result_005_timing_prior_usefulness.md)
- [030_result_006_literature_timing_support_audit.md](../04_results/030_result_006_literature_timing_support_audit.md)
- [015_qfuds_strong_gravity_source_mechanism_audit.md](../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md)
- [001_physical_branch_admission_summary.md](../wiki/governance/001_physical_branch_admission_summary.md)
- [003_blocked_admission_rule_gate.md](../wiki/governance/003_blocked_admission_rule_gate.md)
- [Candidate Equation Proposal Template](../wiki/research/investigations/baseline_reference/plans/010_candidate_equation_proposal_template.md)
- [Candidate Equation Triage Closeout](../wiki/research/investigations/baseline_reference/conclusions/010_candidate_equation_triage_closeout.md)
- [docs/wiki/research/literature/README.md](../wiki/research/literature/README.md)
- [index.csv](../wiki/research/literature/index.csv)
- [Exp006 Coverage Expansion Audit](../wiki/research/investigations/exp006_timing/003_coverage_expansion_audit.md)
- [Li 2025 Digitized Compression Audit](../wiki/research/investigations/exp006_timing/007_li_2025_digitized_compression_audit.md)

These records should be referenced, not duplicated.

## Acceptance Criteria For Future Work

A safe future branch must state:

1. which allowed branch lane it belongs to;
2. which existing evidence anchor it uses;
3. whether it is phenomenology, reduction testing, source audit, DM-only audit,
   or separate DE comparison;
4. why it does not open Physical-QFUDS Level 2B;
5. what equation, observable, viability decision, or reproducible experiment it
   would add if it continues.

For a galaxy/cosmic-web coarse-graining branch, the branch must additionally
state whether `xi_gal` is an input, derived output, calibrated input, or
unknown; whether the correction is on the geometry side or stress-energy side;
and which first known-model sink would absorb it.
