---
doc_id: plan_2026_06_18_legacy_workflow_marker_migration
title: "2026-06-18 Legacy Workflow-Marker Migration Plan"
doc_type: guide
stage: reference
status: completed
evidence_role: audit
depends_on:
  - roadmap
  - plan_2026_06_18_public_bridge_lineage_ko
  - wiki_governance_005_agent_workflow_enforcement_design
next_gate: core-first marker migration before lineage 007; leave full all-doc migration as backlog
last_updated: 2026-06-18
---

# 2026-06-18 Legacy Workflow-Marker Migration Plan

## Purpose

This guide records the migration debt exposed by
`scripts/agent_workflow_guard.py --all` after the Research Asset and Product
Workflow gate was strengthened.

It is not a research result.

It is not QFUDS support.

It does not change roadmap status.

It does not open Physical-QFUDS Level 2B.

## Workflow Boundary

This guide applies the
[Research Asset and Product Workflow](../../.agent/workflows/research-asset-product-workflow.md)
only to preserve source-state boundaries.

No new external web, PDF, table, product, cache, digitization, or availability
claim is introduced here. Existing source-state tokens remain inherited from the
owning research records, including `asset_cached`,
`asset_extracted_not_digitized`, `hit_not_cached`, and
`inspected_no_numerical_product`.

## Current Debt

The whole-repository guard is not the current acceptance gate because it
retroactively applies the new workflow-marker rule to legacy documents.

Current snapshot:

```text
agent_workflow_guard --all failed_files = 199
acceptance_gate_for_new_work = agent_workflow_guard --staged
```

Failure categories from the 2026-06-18 snapshot:

| Category | Failed files |
| --- | ---: |
| `docs/00_project/` | 3 |
| `docs/01_origin/` | 1 |
| `docs/02_theory/` | 6 |
| `docs/03_experiments/` | 4 |
| `docs/04_results/` | 6 |
| `docs/05_next_steps/` | 1 |
| `docs/wiki/lineage/` | 4 |
| `docs/wiki/governance/` | 1 |
| `docs/wiki/postmortem/` | 10 |
| `docs/wiki/research/literature/` | 59 |
| `docs/wiki/research/investigations/` | 36 |
| `docs/wiki/research/assets/` | 68 |

This is migration debt, not a new physics or roadmap problem.

## Core-First Scope

Do not migrate all 199 files now.

Before writing
[007_black_hole_information_public_bridge_ko.md](../wiki/lineage/007_black_hole_information_public_bridge_ko.md),
only the direct core references are marker-migrated:

1. [concept_origin.md](../01_origin/concept_origin.md)
2. [concept_survival_audit.md](../00_project/concept_survival_audit.md)
3. [015_qfuds_strong_gravity_source_mechanism_audit.md](../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md)
4. [049_level2b_eligibility_review_and_observer_mode.md](../wiki/research/investigations/source_x/conclusions/049_level2b_eligibility_review_and_observer_mode.md)

These documents should receive a short `Workflow Boundary` section that:

- links to the Research Asset and Product Workflow;
- says no new external asset, product, cache, or availability claim is
  introduced by the marker migration;
- preserves existing source-state tokens from owning research records;
- states that the document is not QFUDS support, validation, roadmap
  advancement, or Level 2B admission.

## Backlog Policy

After lineage 007 is complete, any broader migration should be phased:

1. lineage and origin-facing documents;
2. governance and status-adjacent documents;
3. active theory, experiment, and result documents;
4. research investigation conclusions and plans;
5. literature cache records;
6. asset README and digitization records.

Each phase should be committed separately and verified with:

```text
rtk python3 scripts/validate_docs.py
rtk python3 scripts/research_consistency.py
rtk python3 scripts/agent_workflow_guard.py --staged
rtk make preflight
rtk sh scripts/git-hooks/pre-commit
```

Do not make `--all` an acceptance gate until the migration backlog has been
explicitly completed or the guard receives a documented legacy-exemption mode.

## Decision

```text
migration_scope = core_first
all_docs_migration = backlog
current_acceptance_gate = staged_only
roadmap_status_change = no
Level_2B_change = no
```

