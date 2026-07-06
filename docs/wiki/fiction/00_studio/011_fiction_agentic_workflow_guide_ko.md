---
doc_id: fiction_agentic_workflow_guide_ko
title: Fiction Agentic Workflow Guide
doc_type: guide
stage: reference
status: draft
evidence_role: reference
depends_on:
  - wiki_fiction_index
  - fiction_ip_management_system_ko
  - fiction_gsd_harness_operator_guide_ko
  - fiction_korean_fiction_prose_naturalness_harness_ko
  - fiction_reader_onboarding_harness_ko
next_gate: use as the single operating hub before active fiction production work
last_updated: 2026-07-06
---

# Fiction Agentic Workflow Guide

## 역할

이 문서는 fiction 작업을 시작할 때 읽는 단일 운영 허브다. 기존 README, workflow,
GSD brief, craft harness를 대체하지 않는다. 대신 작가와 에이전트가 매번 어디서
시작하고 무엇을 확인해야 하는지 한 화면에 고정한다.

작가 입장에서는 이 문서를 지나치게 오래 읽으면 실패다. 여기서 할 일은 하나다.

```text
011에서 시작점을 확인한다
-> SAGA production board에서 오늘 작업을 본다
-> 필요한 canon/story_design/draft만 연다
-> 009/010 품질 하네스로 원고 진입 전 결함을 막는다
```

README는 길 안내판이다. 실제 운영 허브는 이 문서이고, 오늘 작업판은 production
board다.

Boundary:

```text
fiction/provenance only
research evidence: no
roadmap status change: no
external source claim: no
```

## 권위 순서

| 층 | 읽을 것 | 역할 |
| --- | --- | --- |
| 연구 상태 | [Roadmap](../../../05_next_steps/000_roadmap.md) | QFUDS 현재 상태와 금지된 연구 주장 확인 |
| 라우팅 권위 | [Fiction IP Management Workflow](../../../../.agent/workflows/fiction-ip-management-workflow.md) | fiction 문서가 어느 shelf에 속하는지 결정 |
| 실행 권위 | [Agentic Fiction Production Workflow](../../../../.agent/workflows/agentic-fiction-production-workflow.md) | production board, intent card, review wave, chronicler pass 순서 결정 |
| agent skill | [fiction-production skill](../../../../.agents/skills/fiction-production/SKILL.md) | 다음 세션 에이전트의 필수 읽기 순서 |
| 사람이 보는 입구 | [Wiki Fiction](../README.md) | fiction 전체 shelf map |
| active work 입구 | [QFUDS SAGA](../10_universes/qfuds-verse/20_series/qfuds-saga/README.md) | 현재 SAGA 작업 선반과 읽기 경로 |
| 오늘 작업판 | [SAGA production board](../10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/408_saga_production_board_ko.md) | active unit, next action, risks |

충돌하면 `.agent/workflows/`가 이긴다. README는 사람이 보는 지도이고, 실행 권위가
아니다.

## 작업 시작 순서

active SAGA 작업은 아래 순서로 시작한다.

```text
roadmap
-> fiction IP workflow
-> agentic production workflow
-> this guide
-> QFUDS SAGA README
-> production board
-> relevant intent card / story design / bible / draft
```

문서 정리나 navigation 작업처럼 원고를 건드리지 않는 경우에도 같은 원칙을 따른다.
단, production board 상태 자체를 바꿀 필요가 없으면 링크만 확인하고 넘어간다.

원고나 큰 outline 작업이면 아래도 적용한다.

| 상황 | 추가로 읽을 것 |
| --- | --- |
| 한국어 prose 또는 polish | [한국어 소설 문장 자연스러움 하네스](009_korean_fiction_prose_naturalness_harness_ko.md) |
| 기술·법·제도·세계사 개념이 장면 압력인 경우 | [Reader Onboarding Harness](010_reader_onboarding_harness_ko.md) |
| 장기 SAGA production | [SAGA production board](../10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/408_saga_production_board_ko.md) |
| 장면·챕터 진입 | [Chapter intent card template](../10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/409_chapter_intent_card_template_ko.md) |

## Shelf 지도

| Shelf | 무엇을 둔다 | 넣지 말 것 |
| --- | --- | --- |
| `00_studio/` | 전역 fiction 운영 규칙, craft/readability harness, guide | SAGA canon, 산문 원고 |
| `01_catalog/` | active shelf, work list, migration 상태 | 세부 scene design |
| `10_universes/<id>/` | universe/IP scaffold, continuity, world | loose one-off draft |
| `qfuds-saga/00_workroom/` | SAGA 작가실 운영, GSD brief, production board | stable world canon |
| `qfuds-saga/00_bible/` | 작품 설정 기준서, 인물, 제도, 세계 사실 | 운영 절차 |
| `qfuds-saga/10_story_design/` | outline, arc map, reveal plan, scene card | release prose |
| `qfuds-saga/20_drafts/` | 한국어 primary, 영어 counterpart, scene test | canon 변경 단독 확정 |
| `qfuds-saga/30_revisions/` | release-facing revision plan, line-edit control | first draft prose |
| `qfuds-saga/40_release/` | release gate 통과 산출물 | rough draft |
| `90_archive/` | 폐기·대체된 prototype과 provenance | active SAGA decision |

## 현재 운영 판단

| 항목 | 판단 |
| --- | --- |
| active fiction track | `qfuds-verse / qfuds-saga` |
| active production entry | SAGA README와 workroom production board |
| active prose source | `20_drafts/` |
| release status | active release 없음. release gate 이후 `40_release/` 사용 |
| old prototype | `90_archive/` 또는 `20_drafts/2부/_versions/`에서 보존 |
| README 역할 | navigation과 shelf contract. 실행 권위 아님 |

## 건드리면 위험한 것

| 대상 | 위험 |
| --- | --- |
| [.agent/workflows](../../../../.agent/workflows/README.md) | agent behavior와 pre-commit workflow guard에 영향 |
| [fiction-production skill](../../../../.agents/skills/fiction-production/SKILL.md) | 다음 세션 필수 읽기 순서에 영향 |
| [Claude settings](../../../../.claude/settings.json)와 `.claude/hooks/` | Claude Code prompt/write hook 동작에 영향 |
| [fiction gate](../../../../scripts/fiction_gate.py), [pre-commit](../../../../scripts/git-hooks/pre-commit) | hard gate와 commit 가능 여부에 영향 |
| `20_drafts/1부/README.md`, `20_drafts/2부/README.md` | arc numbering cascade 확정 전 수정하면 번호 혼선 위험 |
| `90_archive/*` | provenance 보존 경로. 삭제·이동 금지 |

## 정리 원칙

- 새 운영 규칙은 먼저 `00_studio/`에 둔다.
- 작품별 운영 규칙은 `qfuds-saga/00_workroom/`에 둔다.
- README는 짧은 진입점으로 유지하고, 세부 실행 절차는 workflow/guide로 보낸다.
- 오래된 개별 draft 링크는 상위 wiki index에 직접 많이 두지 않는다. draft map이나
  archive README로 우회한다.
- 번호 cascade가 걸린 문서는 arc map과 origin outline이 확정된 뒤 별도 pass로 고친다.

## 왜 게이트로 강제하나 (관점 요약)

(구 `008 4관점 해설`에서 통합.) 단편 한 편은 머릿속 규칙으로 됐지만, 시리즈로
가자 세계관 구멍·균질한 인물 목소리·반복 구조·AI 티가 누적됐다. 원인은 도구가
없어서가 아니라 도구가 강제되지 않아서였다. 그래서 규칙을 훅과 게이트로 옮겼다.

| 관점 | 핵심 |
| --- | --- |
| 에이전트 | 하드 게이트 `scripts/fiction_gate.py --staged`(pre-commit, em dash·민감 주제 차단), 소프트 게이트 `.claude` PreToolUse/UserPromptSubmit 훅, 검증 에이전트(`ai-tell-detector`·`naturalness-reviewer`·`content-fidelity-auditor`), 집필 전 프리플라이트(`00_workroom/005`). 게이트가 막는 것은 결함이 아니라 설계다 |
| 작가 | 읽기=SAGA README read path, 설정=`00_bible/`, 기획=`10_story_design/`, 내 아이디어 추적=`00_workroom/006`, 어디에 두나=README 라우팅 표 |
| 독자 | 완성본(`40_release`)만 본다. 리텐션 테스트 통과가 release 조건 |
| 협업 | 원본은 `20_drafts` 하나. `40_release`는 gate 통과 시 manifest/export만. canon 충돌은 `00_bible` 기준 |

## 검증

문서 정리 후 최소 검증:

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/agent_workflow_guard.py --staged
python3 scripts/fiction_gate.py --staged
sh scripts/git-hooks/pre-commit
```
