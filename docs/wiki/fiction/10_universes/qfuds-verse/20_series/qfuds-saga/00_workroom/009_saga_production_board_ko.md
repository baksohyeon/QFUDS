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
next_gate: formal 9-persona retention gate before any 40_release promotion
last_updated: 2026-06-22
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
| Active unit | 010 release-facing revision wave: 030 origin(1부) + 029 Mara(2부) prose/onboarding pass |
| Phase | `verify` passed -> `release_gate_blocked` |
| Owner mode | `writer` + `continuity` + `reader-sim` + `polish` |
| Status | `validated`; 010 revision wave applied to 030/029; release promotion still blocked |
| Failure reason | 없음(초고 완결). 잔여=release-facing reader-retention 정식 게이트(40_release 승격), 영어 각색판 |
| Next action | formal 9-persona retention gate before any `40_release` manifest |
| Source files | `10_story_design/016`, `10_story_design/017`, `10_story_design/019`, `10_story_design/018`, `10_story_design/011`, `10_story_design/013` |
| Output files | `20_drafts/1부/030_origin_arc_sael_korean_primary.md`(B1~B7+윤문), `20_drafts/2부/029_...md`(cross-arc), `20_drafts/{1,2,3}부/` cascade |
| Approval needed | no(초고/cascade); yes before release promotion |

## Unit Queue

| Unit | Phase | Intent card | Last review wave | Chronicler pass | Status |
| --- | --- | --- | --- | --- | --- |
| 1부 origin B1~B2 | review/verify | [017 B1·B2](../10_story_design/017_first_arc_origin_scene_cards_ko.md) | AI-tell/온보딩/후킹/stakes 패스 반영 | pending | `drafted` |
| 1부 origin B3~B7 | verified | [017 B3~B7](../10_story_design/017_first_arc_origin_scene_cards_ko.md) | 010 release-facing wave: B3 로그화, B5b~B7 경구 제거 | 010 notes in 030 | `validated` |
| 2부 Mara / 029 전체 | verified | [013](../10_story_design/013_first_arc_scene_cards_ko.md) | 010 release-facing wave: 프롤로그 압축, Ch3 반복 완화, Ch5 QFUDS boundary, Ch6 반복 완화 | Continuity Notes in 029 + 010 notes | `validated` |
| 2부 Mara repositioning | plan | 011에서 구조 이동됨 | none | none | `hold` until 030 B1-B7 stabilizes |
| 3부 author-loss assets | plan | 025-027 자산 보존 | none | none | `hold` until physical cascade |

## Active Risks

| Risk | Scope | Severity | Owner mode | Next action |
| --- | --- | --- | --- | --- |
| Release promotion without formal retention gate | 030/029 | release-blocking | reader-sim / critic | keep `40_release` empty until formal 9-persona retention gate passes |
| Number cascade confusion | 011, 025-027, 007, 010 | medium | continuity | stable IDs remain; verify labels only when touching affected docs |
| External-system overfit | `.agent`, workroom | medium | science_auditor / critic | keep external repos inspiration-only; no install or prompt/code copy |
| Humanize misuse | prose polish | medium | style_editor | polish only after structure/continuity pass; no AI-detector evasion framing |

## Cascade Ledger (완료)

번호 SSOT는 [011 §10](../10_story_design/011_saga_arc_map_multiarc_ko.md)이다. 번호
physical cascade를 2026-06-21에 실행 완료했다. 물리 폴더는 canonical 부 번호와 일치한다.

| Asset | Physical path (cascade 후) | Canonical role (011) | Status |
| --- | --- | --- | --- |
| 030 origin Sael draft | `20_drafts/1부/030_origin_arc_sael_korean_primary.md` | 1부 origin | done (제자리) |
| 029 Mara reboot | `20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md` | 2부 Mara | done (1부→2부 이동) |
| 025-027 author-loss drafts | `20_drafts/3부/` | 3부 author-loss | done (2부→3부 이동) |
| Mara prototypes | `20_drafts/2부/_versions/` | 2부 Mara 계보 | done (1부→2부 이동) |
| draft READMEs | `20_drafts/README.md`, `1부/`, `2부/`(신설), `3부/` | 부 번호 일치 네비게이션 | done (doc_id book1/2/3 정합) |

stable ID 보존: 원고 파일명(029·030·025-027)과 `arc_two` doc_id·파일명(007·010·004)은
바꾸지 않았다. 폴더 위치와 README·배너 서술 라벨만 갱신했다.

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
| 2026-06-21 | 030 reader-retention 9 persona 게이트 (중2/고2/일반/웹소설속독/순문학/문외한/안티AI/Chiang/SF) | 전원 완독·다음 편 진행=예; 공통 약점=B5b·B6 늘어짐, B3 인과 누락, AI-tell 경구 클러스터 | 윤문 패스 → 재검증 |
| 2026-06-21 | 030 B3~B7 deep AI-tell (ai-tell-detector ×2) + 윤문 16건 | 1차 S1 4건/S2 7건 → 윤문 → 재검증 "새 S1 없음", 안티AI "사람이 쓴 것처럼=예", 순문학 전 지적 개선 | release 시 정식 retention 게이트 |
| 2026-06-21 | 번호 physical cascade (011 §10) | 029 1부→2부, 025-027 2부→3부, _versions 동반 이동; 백링크·README(book1/2/3)·배너 일괄 갱신; validate_docs PASS | stable ID(파일명·arc_two doc_id) 보존 확인 |
| 2026-06-21 | 029 reader-retention 6 persona (일반/웹소설속독/순문학/문외한/안티AI/SF) + ai-tell-detector ×2 | 전원 완독·진행=예; 강점 Ch1·Ch4·Ch6; 공통 약점=프롤로그 세계사 infodump, "X아니라Y" 안티테제 30+회·격언 마무리·Ch6 6연 anaphora | 피드백 통합 → [30_revisions/009] |
| 2026-06-21 | 029 윤문 패스 13건 + 재검증 | 프롤로그 ~42→16줄 압축, Ch6 6연→3항, 격언/삼분/anaphora de-tell; 안티AI 재독 "프롤로그·Ch6 개선"; em dash 0·박- 0 | 인물 대사 안티테제·Ch5 강의는 release 게이트 잔여 |
| 2026-06-22 | 010 release-facing revision wave + validation | 030 B3~B7 경구형 문장 로그/화면 중심으로 낮춤; 029 프롤로그·Ch3·Ch5·Ch6 압축; `validate_docs`, `research_consistency`, full `fiction_gate`, staged workflow/fiction gates, pre-commit all PASS | formal 9-persona retention gate before release promotion |
