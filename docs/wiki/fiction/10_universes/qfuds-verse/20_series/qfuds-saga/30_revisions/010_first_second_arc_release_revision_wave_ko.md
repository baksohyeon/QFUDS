---
doc_id: qfuds_saga_revisions_first_second_arc_release_wave_ko
title: QFUDS SAGA 1부·2부 release-facing revision wave
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_revisions_reader_feedback_ai_tell_consolidation_ko
  - qfuds_saga_production_board_ko
  - qfuds_saga_drafts_origin_sael_korean_primary
  - qfuds_saga_first_arc_book1_reboot_korean_primary
next_gate: run staged fiction gate and keep release promotion blocked until formal 9-persona retention gate
last_updated: 2026-07-06
---

# QFUDS SAGA 1부·2부 release-facing revision wave

## 역할 / 경계

이 문서는 사엘 origin([030](../20_drafts/1.5부/030_origin_arc_sael_korean_primary.md), 2026-06-30 1부→1.5부 강등)과
2부 Mara([029](../20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md))에 대한
release-facing 전 단계 수정 파동이다. 원고 source는 `20_drafts/`이고, 이 문서는
수정 이유와 잔여 위험을 남기는 revision 기록이다.

Boundary:

```text
fiction/provenance only
research evidence: no
external MCP install: no
new source claim: no
release promotion: no
```

## Tool Policy

이번 수정은 repo-local bible, scene cards, production board, 009/010 하네스만 사용한다.
Context7은 API·SDK 시그니처 확인이 필요할 때만 켠다. Playwright는 웹 UI 검증이 있을 때만
쓴다. GSC, memory, sequential-thinking, prompt-generator 계열 MCP는 이번 prose revision에
사용하지 않는다.

## Review Wave

| Wave | Question | Result | Follow-up |
| --- | --- | --- | --- |
| Foundation scan | 030과 029가 desire, threat, choice, turn, cost, handoff를 유지하는가 | pass | 구조 재작성 금지, line/scene pressure만 수정 |
| High-severity fix | release 전 막는 결함은 무엇인가 | 030의 B5b·B6 경구화, 029의 프롤로그 설명 과밀·Ch3 반복·Ch5 강의 비중·Ch6 수사 반복 | 해당 구간만 직접 수정 |
| Re-scan | 수정이 continuity나 field mark를 깨는가 | pass | staged validation 통과, 030/029 field mark 유지 |
| Continuity fix | 030 B7이 029 Mara 청구로 자연스럽게 넘어가는가 | pass with edits | 030 B7의 handoff는 유지, 029 prologue는 source counterpart로 보존 |
| Voice polish | 한국어 primary 문장이 번역투·기획서투 없이 읽히는가 | pass with residual risk | 설명 과밀 구간은 압축, 029 Ch5 기술 장면은 release gate에서 재독 필요 |
| Release gate | 40_release 승격 가능한가 | no | 정식 9-persona retention gate와 English adaptation 전까지 blocked |

## Edit Scope

| File | Mode | Edit intent |
| --- | --- | --- |
| `20_drafts/1.5부/030_origin_arc_sael_korean_primary.md` | `polish` + `continuity` | B1 stakes 정렬 유지, B3~B7의 경구형 문장과 추상 명제 일부를 손/화면/로그 중심으로 낮춤 |
| `20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md` | `polish` + `reader-sim` | 프롤로그 설명 압축, Ch3 삼분파 반복 비대칭화, Ch5 물리 강의 압축, Ch6 수사 반복 완화 |
| `00_workroom/408_saga_production_board_ko.md` | `chronicler` | active revision wave와 잔여 release risk만 기록 |

## Reader Onboarding Note

기술 설명은 숨기지 않는다. 다만 설명 뒤에는 즉시 손실, 버튼, 도장, 경보, 기록판, 판결문,
상신 버튼 중 하나가 따라와야 한다. 독자가 완전한 이론을 외우지 않아도 누가 무엇을 잃는지
말할 수 있어야 한다.

## Chronicler Pass

| Delta | Status | Destination | Rationale |
| --- | --- | --- | --- |
| 030 B3 공개키→개인키 역산은 더 기술적 표현으로 정리 | note-only | 030 draft | 기존 canon 변화 없음 |
| 030 B7 handoff는 Mara 청구의 근거로 유지 | soft-canon | existing story_design retained | 011 §10 cascade와 일치 |
| 029 Ch5 QFUDS forbidden lattice는 증거가 아니라 rejected courtroom argument로 유지 | note-only | 029 draft | 연구 경계 보존 |
| 029 Ch6 protected pending doctrine은 release gate 잔여 위험으로 유지 | canon-candidate | future bible/revision only after release review | 자동 canon 승격 금지 |

## Residual Risk

| Risk | Severity | Owner mode | Next action |
| --- | --- | --- | --- |
| 029 Ch5는 기술 자체가 장면 재미라 완전 압축하면 장점이 죽음 | medium | science_auditor + reader-sim | 강의 삭제가 아니라 Liora/Dahl의 책임 경계로 압축 |
| 029 Ch6의 `who may author loss`는 의도된 수사라 과도하게 평탄화하면 결말 힘이 줄어듦 | medium | showrunner + style_editor | 반복을 줄이되 field mark와 판결문은 보존 |
| 030 B6/B7은 origin의 원죄를 닫는 구간이라 추상어가 완전히 사라지면 arc 의미가 흐려짐 | medium | continuity | 추상 결론은 한 줄 이하, 주변은 로그·화면·행동으로 유지 |

## Verification

Required after edits:

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/agent_workflow_guard.py --staged
python3 scripts/fiction_gate.py --staged
sh scripts/git-hooks/pre-commit
```

2026-06-22 result: all required checks passed.
