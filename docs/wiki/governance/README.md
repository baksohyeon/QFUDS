---
doc_id: wiki_governance_index
title: Wiki Governance
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - repository_levels_glossary
next_gate: none; governance routing only
last_updated: 2026-06-17
---

# Wiki Governance

This folder stores repository-level admission rules, consistency checks, and
gates that control whether a research branch may be treated as stronger than a
reference, audit, or phenomenological result.

Use this folder when the checked object is QFUDS documentation itself: roadmap
consistency, decision-log consistency, glossary links, branch-classification
wording, missing admission-rule items, or cross-document drift.

Do not use this folder as a temporary holding area. A document belongs here only
if it defines, enforces, or audits a repository rule or admission gate.

Do not use this folder for external literature searches, asset availability
checks, data-product recovery, paper-source caching, or figure-digitization
workflow records. Those belong under
[Research Investigations](../research/investigations/README.md).

## Read Order

1. [Physical Branch Admission Summary](001_physical_branch_admission_summary.md)
2. [Terminology Backlink Consistency Check](002_terminology_backlink_consistency_check.md)
3. [Blocked Admission Rule Gate](003_blocked_admission_rule_gate.md)
4. [Missing Physics Map](004_missing_physics_map.md)
5. [Agent Workflow Enforcement Design](005_agent_workflow_enforcement_design.md)

## Boundary

- `docs/wiki/governance/`: internal admission rules, branch gates, roadmap/wiki
  consistency checks, and missing-physics maps.
- `docs/wiki/lineage/`: idea genealogy and branch dependency provenance.
- `docs/wiki/research/investigations/`: external literature/data/source/asset
  investigations.
