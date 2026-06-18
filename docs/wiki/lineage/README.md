---
doc_id: wiki_lineage_index
title: Wiki Lineage
doc_type: index
stage: reference
status: reference
evidence_role: provenance
depends_on:
  - roadmap
next_gate: none; lineage is routing provenance only; 005 has 2026-06-18 baseline-reference ceiling addendum
last_updated: 2026-06-18
---

# Wiki Lineage

This folder stores idea genealogy and branch dependency maps.

Use it only to explain where a QFUDS idea came from, how it narrowed, what was
demoted, and which retained branch descended from which earlier question. These
documents are provenance and routing aids, not roadmap status authorities and
not new theory evidence.

Do not use this folder for:

- admission gates or missing-physics rules; use
  [Wiki Governance](../governance/README.md);
- external literature or data-product work; use
  [Research Investigations](../research/investigations/README.md);
- incident retrospectives; use [Postmortems](../postmortem/).

## Read Order

1. [QFUDS Idea Genealogy](001_qfuds_genealogy.md)
2. [QFUDS Branch Dependency Graph](002_branch_graph.md)
3. [QFUDS 연구 흐름 쉬운 설명](003_research_flow_plain_language_ko.md)
4. [QFUDS rough tanh 수치 스케치](004_rough_tanh_numerical_sketch_ko.md) - Season 2 대표 탐색 기록
5. [QFUDS rough tanh 논문 보고서](005_rough_tanh_thesis_report_ko.md) - 선택적으로 읽는 논문형 압축본; 2026-06-18 baseline-reference audits added the `f_B` bookkeeping, known-model reduction, escape-template, and NASA/BAO kill-map-only boundary
6. [QFUDS 에이전트 기반 연구 운영 절차 기록](006_agentic_research_system_ko.md)

The 006 document records the agent-based workflow that produced and checked
the rough-tanh lineage. It is provenance and process analysis, not physical
evidence and not a roadmap-status authority.

## Current 005 Boundary

The 2026-06-18 baseline-reference audit chain narrows the 005 thesis-style
report without changing roadmap status:

- `xi ~= 10 Mpc` is not a state variable;
- `X(x,a)` is not defined enough to supply `rho_F[X]`, `p_F[X]`, or an
  evolution equation;
- `f_B(x,a)` is bookkeeping only unless `p_B`, `T_mu_nu`, `Q^nu`, and
  `delta Q` are independently supplied;
- current `f_B` routes reduce first to effective `w(a)`, unified dark fluid, or
  IV/IDE;
- NASA/LAMBDA and BAO remain baseline kill-map sources only, not model-facing
  QFUDS evidence.
