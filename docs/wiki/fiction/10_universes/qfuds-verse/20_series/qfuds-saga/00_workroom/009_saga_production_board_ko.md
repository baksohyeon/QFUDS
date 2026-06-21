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
| Active unit | first-arc 완결 sprint on `complete-first-arc-novel`: 030 origin(1부) B1~B7 초고 완성; 029(2부 Mara)는 closing pass(continuity/AI-tell/reader-sim) 대상 |
| Phase | `draft` -> `review` |
| Owner mode | `writer` + `continuity` + `reader-sim` + `polish` |
| Status | `in_progress`; 030 B1~B7 drafted(2026-06-21), 029 Prologue~Ch6 drafted; 030↔029 continuity·harness·AI-tell pass 진행 중 |
| Failure reason | 번호 cascade 미실행(물리 경로 legacy `1부/`), release-facing reader-retention 게이트 미실행 |
| Next action | 030↔029 handoff continuity 확인 → 029 harness/AI-tell 스캔 → validation(validate_docs/research_consistency/fiction_gate) → commit + origin push |
| Source files | `10_story_design/016`, `10_story_design/017`, `10_story_design/019`, `10_story_design/018`, `10_story_design/011`, `10_story_design/013` |
| Output files | `20_drafts/1부/030_origin_arc_sael_korean_primary.md`(B1~B7), `20_drafts/1부/029_first_arc_book1_reboot_korean_primary.md`(closing pass) |
| Approval needed | no for closing passes on existing drafts; yes before physical cascade / release promotion |

## Unit Queue

| Unit | Phase | Intent card | Last review wave | Chronicler pass | Status |
| --- | --- | --- | --- | --- | --- |
| 1부 origin B1~B2 | draft | [017 B1·B2](../10_story_design/017_first_arc_origin_scene_cards_ko.md) | AI-tell/온보딩/후킹/stakes 패스 반영 | pending | `drafted` |
| 1부 origin B3~B7 | draft | [017 B3~B7](../10_story_design/017_first_arc_origin_scene_cards_ko.md) | writer pass on `complete-first-arc-novel`(2026-06-21); em dash 0·박- 0·노출예산 self-check 통과 | pending | `drafted` |
| 2부 Mara / 029 전체 | draft/review | [013](../10_story_design/013_first_arc_scene_cards_ko.md) | Prologue~Ch6 writer pass; closing(continuity/AI-tell) 진행 | Continuity Notes in 029 | `closing_pass` |
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
| 2026-06-21 | 030 origin B3~B7 writer pass (`complete-first-arc-novel`) | 역연산→경첩→큐/경보→구조→사다리 drafted; 닫는 mark `THE LOCK WAS THE CROWN`; Mara handoff에서 029로 연결 | 030↔029 continuity + 029 AI-tell/harness scan + validation before commit |
| 2026-06-21 | 030 B3~B7 harness self-check | em dash 0, 박- embed-verb 0, Karvath 미등장/Vera 그림자 1회/Last Archive 미노출 노출예산 준수 | 029 동일 스캔 |
