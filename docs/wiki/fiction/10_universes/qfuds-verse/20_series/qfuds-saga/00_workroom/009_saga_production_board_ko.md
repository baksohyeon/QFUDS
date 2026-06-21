---
doc_id: qfuds_saga_production_board_ko
title: QFUDS SAGA Production Board
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_agentic_system_ko
  - qfuds_saga_series_production_harness_ko
  - qfuds_saga_external_ai_writing_systems_gap_audit_ko
next_gate: update active unit after 1부 POV decision and origin outline approval
last_updated: 2026-06-21
---

# QFUDS SAGA Production Board

## 역할

이 문서는 QFUDS SAGA의 현재 집필 실행 상태판이다. canon 문서가 아니다. 장편 생산
상태, 막힌 이유, 다음 행동, 검증 로그를 한 장에 모아 다음 에이전트가 같은 규칙을
다시 발견하느라 시간을 쓰지 않게 한다.

Operational workflow:
[Agentic Fiction Production Workflow](../../../../../../../../.agent/workflows/agentic-fiction-production-workflow.md).
IP routing:
[Fiction IP Management Workflow](../../../../../../../../.agent/workflows/fiction-ip-management-workflow.md).

Boundary:

```text
fiction/provenance only
research evidence: no
external AI writing systems: architecture inspiration only
workflow state: hit_not_cached
install external tools: no
```

## Current State

| Field | Value |
| --- | --- |
| Active unit | 1부 origin restructuring / POV decision lane |
| Phase | `plan` |
| Owner mode | `showrunner` + `critic` + `continuity` |
| Status | `needs_user` after 011 review; ready for 1부 POV decision |
| Failure reason | origin이 프롤로그 목격담으로 남으면 설정 교과서가 될 위험 |
| Next action | 1부 POV를 사엘 능동화 / 새 POV / 절충 중 결정한 뒤 origin outline 작성 |
| Source files | `10_story_design/011`, `10_story_design/015`, `00_workroom/008`, `00_workroom/005` |
| Output files | next: `10_story_design/018` or approved origin outline doc |
| Approval needed | yes: 1부 POV 선택 |

## Unit Queue

| Unit | Phase | Intent card | Last review wave | Chronicler pass | Status |
| --- | --- | --- | --- | --- | --- |
| 1부 origin POV decision | plan | 필요: [010](010_chapter_intent_card_template_ko.md) 기반 결정 카드 | none | none | `needs_user` |
| 1부 origin outline | outline | pending POV decision | none | none | `blocked` |
| 2부 Mara repositioning | plan | 011에서 구조 이동됨 | none | none | `ready_next` after origin outline |
| 3부 author-loss assets | plan | 025-027 자산 보존 | none | none | `ready_next` after numbering cascade |

## Active Risks

| Risk | Scope | Severity | Owner mode | Next action |
| --- | --- | --- | --- | --- |
| Origin protagonist becomes observer | 1부 origin | release-blocking | showrunner / critic | protagonist must choose, fail, ratify, or stay silent in a way that opens the standard-authoring regime |
| Number cascade confusion | 011, 025-027, 007, 010 | high | continuity | update labels only after origin outline locks; stable file IDs can remain |
| External-system overfit | `.agent`, workroom | medium | science_auditor / critic | keep external repos inspiration-only; no install or prompt/code copy |
| Humanize misuse | prose polish | medium | style_editor | polish only after structure/continuity pass; no AI-detector evasion framing |

## Execution Loop

For every new major chapter or episode:

```text
production board update
-> chapter intent card
-> writer pass
-> critic / reader-sim pass
-> continuity pass
-> chronicler pass
-> verification
```

If a step is skipped, record why in this board or in the relevant GSD phase
brief.

## Verification Log

| Date | Command or review | Result | Follow-up |
| --- | --- | --- | --- |
| 2026-06-21 | external AI writing systems gap audit | local patterns selected; install rejected | create templates and warn-first gate |
| 2026-06-21 | 011 restructuring review | origin=1부, Mara=2부, existing 025-027=3부 asset direction accepted as structure | choose 1부 POV before origin outline |
