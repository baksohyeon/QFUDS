---
doc_id: wiki_content_index
title: Wiki Content Index
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - roadmap
next_gate: none; content navigation only
last_updated: 2026-06-19
---

# Wiki Content Index

This is the content-oriented catalog for the QFUDS wiki.

Operational workflow rules live in
[Wiki Maintenance Workflow](../../.agent/workflows/wiki-maintenance-workflow.md)
and
[Documentation Folder Routing Workflow](../../.agent/workflows/documentation-folder-routing-workflow.md).

## Core Navigation

- [Wiki Landing Page](README.md) - human-facing entry point for the wiki
  directory.
- [Repository Levels](glossary/repository_levels.md) - glossary for repository
  level terminology.

## Governance

- [Wiki Governance](governance/README.md) - index for admission gates and
  consistency checks.
- [Physical Branch Admission Summary](governance/001_physical_branch_admission_summary.md)
  - retained-branch admission classification summary.
- [Terminology Backlink Consistency Check](governance/002_terminology_backlink_consistency_check.md)
  - level-term backlink consistency record.
- [Blocked Admission Rule Gate](governance/003_blocked_admission_rule_gate.md)
  - five-item physical-branch admission gate.
- [Missing Physics Map](governance/004_missing_physics_map.md) - map of missing
  physics required before a physical branch can open.
- [Agent Workflow Enforcement Design](governance/005_agent_workflow_enforcement_design.md)
  - design record for enforcing research workflow state markers across Codex,
    Claude Code, and git pre-commit.

## Lineage

- [Wiki Lineage](lineage/README.md) - index for idea genealogy and branch
  dependency provenance.
- [QFUDS Idea Genealogy](lineage/001_qfuds_genealogy.md) - provenance trail for
  retained, demoted, and blocked ideas.
- [QFUDS Branch Dependency Graph](lineage/002_branch_graph.md) - branch
  relationship and routing map.
- [QFUDS 연구 흐름 쉬운 설명](lineage/003_research_flow_plain_language_ko.md)
  - non-specialist Korean summary of the QFUDS research flow and current
    status boundaries.
- [QFUDS rough tanh 수치 스케치](lineage/004_rough_tanh_numerical_sketch_ko.md)
  - append-only checkpoint log (CP1~CP24) of the rough tanh phenomenology
    sketch; provenance only, observer mode.
- [QFUDS rough tanh 논문 보고서](lineage/005_rough_tanh_thesis_report_ko.md)
  - thesis-style synthesis of the CP1~CP24 sketch and the agent-based workflow
    methodology; provenance only, 050 ceiling intact. The 2026-06-18
    baseline-reference addendum keeps `f_B` bookkeeping-only and NASA/BAO as
    kill-map-only sources.
- [QFUDS 에이전트 기반 연구 운영 절차](lineage/006_agentic_research_system_ko.md)
  - workflow, document/status boundary, parser routing, cache state,
    adversarial review, and git-hook gate record.
- [블랙홀은 우주의 하드디스크인가?](lineage/007_black_hole_information_public_bridge_ko.md)
  - public bridge for the black-hole information origin story; provenance only,
    not physical evidence.

## Fiction

- [Wiki Fiction](fiction/README.md) - index for separate fiction companion
  tracks derived from provenance records.
- [QFUDS SAGA](fiction/qfuds-saga/README.md) - active fiction-system track for
  the QFUDS-inspired SAGA; not research evidence.
- [QFUDS SAGA 창작 시스템](fiction/qfuds-saga/system/001_agentic_saga_system_ko.md)
  - AI writers' room, MCP candidates, and user-confirmation workflow.
- [QFUDS SAGA 세계관 방향 선택 매트릭스](fiction/qfuds-saga/system/002_world_direction_matrix_ko.md)
  - world-direction comparison for Nested Cosmology, closed-world revelation,
    deep-time empire, tactical philosophy SF, and it-from-bit mythos.

## Postmortems

- [Wiki Postmortems](postmortem/README.md) - index for process-failure records.
- [Li 2025 Data Cache Incident](postmortem/001-20260609-dorito-li-2025-data-cache.md)
  - data-cache and PDF extraction incident.
- [IV/IDE Timing Handoff Checkpoint](postmortem/002-20260609-dorito-iv-ide-timing-checkpoint.md)
  - timing-analysis handoff record.
- [QFUDS Scope Demotion Retrospective](postmortem/003-20260610-dorito-qfuds-scope-demotion-retrospective.md)
  - scope-demotion process retrospective.
- [Source-X Data Product Audit Retrospective](postmortem/004-20260610-dorito-source-x-data-product-audit.md)
  - data-product audit process retrospective.
- [Research Asset Digitization Automation Retrospective](postmortem/005-20260611-dorito-research-asset-digitization-automation.md)
  - research asset digitization workflow retrospective.
- [Pre-commit Regression Test Scope Retrospective](postmortem/006-20260611-dorito-precommit-regression-test-scope.md)
  - pre-commit validation-scope retrospective.
- [Source-X Product Routing Workflow Retrospective](postmortem/007-20260611-dorito-source-x-product-routing-workflow.md)
  - asset-product and investigation-result routing retrospective.
- [Source-X Progress Checkpoint](postmortem/008-20260611-dorito-source-x-progress-checkpoint.md)
  - end-of-day Source-X product-recovery and next-gate checkpoint.
- [QFUDS observer-mode closing retrospective](postmortem/009-20260611-dorito-qfuds-observer-mode-closing-retro.md)
  - observer-mode transition closure retrospective.
- [rough tanh lineage descent retrospective (CP13~CP24)](postmortem/010-20260612-dorito-rough-tanh-lineage-descent-retro.md)
  - falsifiable signals → cosmological-constant problem descent retrospective.
- [rough tanh lineage natural closing retrospective (CP25)](postmortem/011-20260612-dorito-rough-tanh-lineage-natural-closing-retro.md)
  - three intuitions independently rediscovering the 2000s–2025 literature arc;
    lineage natural closing.
- [QFUDS math and documentation audit retrospective](postmortem/012-20260613-dorito-qfuds-math-doc-audit.md)
  - formula, lineage asset, and documentation consistency audit retrospective.
- [Agent research workflow guard retrospective](postmortem/013-20260617-dorito-agent-research-workflow-guard.md)
  - workflow miss retrospective and commit-gate enforcement record.
- [Parser tool link guard false-positive retrospective](postmortem/014-20260617-dorito-parser-tool-link-guard-false-positive.md)
  - PageIndex/MarkItDown tool-link guard false-positive and narrow exception record.

## Research Cache

- [Research Cache](research/README.md) - index for reusable research reference
  material.
- [Literature Cache](research/literature/README.md) - paper and external
  reference records.
- [Research Investigations](research/investigations/README.md) - dated
  research-process records.
- [Baseline Reference Investigations](research/investigations/baseline_reference/README.md)
  - NASA/LAMBDA cache, BAO kill-map, non-circularity ledger, `f_B`
    stress-energy audit, known-model reduction, and escape-equation templates.
- [Source-X Research Investigations](research/investigations/source_x/README.md)
  - Source-X plans 041-050, Chen digitization, known-model distinction, and
    observer-mode routing boundaries.
- [Research Assets](research/assets/README.md) - cached external source and
  derived inspection assets.
- [IV/IDE Timing Korean Synthesis](research/investigations/exp006_timing/008_iv_ide_timing_synthesis_ko.md)
  - Korean timing synthesis reference.
