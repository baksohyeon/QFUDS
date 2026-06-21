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
next_gate: review completed 029 Ch6 pass and reconcile 029/030 queue before physical cascade
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
| Active unit | 병렬 작업: 029 Mara/Book 1 Ch6 completion on `codex/complete-029-book1`; 030 origin draft remains separate active origin asset |
| Phase | `draft` -> `review` |
| Owner mode | `writer` + `reader-sim` + `continuity` |
| Status | `in_progress`; 029 Ch6 drafted, review/chronicler/verification pending |
| Failure reason | 029는 canonical 2부 Mara 자산이지만 물리 경로는 legacy `1부/`; 030 병렬 수정도 존재 |
| Next action | 029 Ch6 자연스러움/continuity pass, then commit branch; do not physical-cascade in this pass |
| Source files | `10_story_design/016`, `10_story_design/017`, `10_story_design/019`, `10_story_design/018`, `10_story_design/011` |
| Output files | `20_drafts/1부/030_origin_arc_sael_korean_primary.md` |
| Approval needed | no for continued B2 drafting; yes before physical cascade |

## Unit Queue

| Unit | Phase | Intent card | Last review wave | Chronicler pass | Status |
| --- | --- | --- | --- | --- | --- |
| 1부 origin B1 | draft | [017 B1](../10_story_design/017_first_arc_origin_scene_cards_ko.md) | B1 AI-tell/온보딩/후킹 패스 반영 | pending | `in_progress` |
| 1부 origin B2 | draft | [017 B2](../10_story_design/017_first_arc_origin_scene_cards_ko.md) | none | none | `ready_next` |
| 2부 Mara / 029 Ch6 | draft/review | [013 Ch6](../10_story_design/013_first_arc_scene_cards_ko.md) | Ch6 writer pass complete on `codex/complete-029-book1` | Continuity Notes updated in 029 | `review_pending` |
| 2부 Mara repositioning | plan | 011에서 구조 이동됨 | none | none | `hold` until 030 B1-B7 stabilizes |
| 3부 author-loss assets | plan | 025-027 자산 보존 | none | none | `hold` until physical cascade |

## Active Risks

| Risk | Scope | Severity | Owner mode | Next action |
| --- | --- | --- | --- | --- |
| Origin protagonist becomes observer | 1부 origin | release-blocking | showrunner / critic | protagonist must choose, fail, ratify, or stay silent in a way that opens the standard-authoring regime |
| Number cascade confusion | 011, 025-027, 007, 010 | high | continuity | update labels only after origin outline locks; stable file IDs can remain |
| External-system overfit | `.agent`, workroom | medium | science_auditor / critic | keep external repos inspiration-only; no install or prompt/code copy |
| Humanize misuse | prose polish | medium | style_editor | polish only after structure/continuity pass; no AI-detector evasion framing |

## Cascade Drift Ledger

번호 SSOT는 [011 §10](../10_story_design/011_saga_arc_map_multiarc_ko.md)이다. 현재
`20_drafts/`의 물리 폴더명은 legacy 상태로 남겨 두고, origin 초안이 안정화된 뒤
한 번에 physical cascade를 실행한다.

| Asset | Current physical path | Canonical role after 011 | Current action |
| --- | --- | --- | --- |
| 030 origin Sael draft | `20_drafts/1부/030_origin_arc_sael_korean_primary.md` | 신규 1부 origin | keep in current folder until cascade |
| 029 Mara reboot | `20_drafts/1부/029_first_arc_book1_reboot_korean_primary.md` | 2부 Mara asset | freeze/relabel later; do not continue Ch6 now |
| 025-027 author-loss drafts | `20_drafts/2부/` | 3부 author-loss assets | preserve/relabel later |
| draft READMEs | `20_drafts/README.md`, `1부/README.md`, `2부/README.md` | temporary navigation over legacy paths | banner now, cascade later |

Deletion policy: no delete or archive movement before physical cascade, link/gate verification,
and at least two stable commits after the new paths are accepted.

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
| 2026-06-21 | 029 Ch6 writer/chronicler pass | final human hearing drafted; `who may author loss` field mark and protected pending hook added | run prose/continuity review and validation before commit |
