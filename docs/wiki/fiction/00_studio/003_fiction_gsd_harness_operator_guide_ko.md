---
doc_id: fiction_gsd_harness_operator_guide_ko
title: Fiction GSD 하네스 운영 가이드
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - fiction_ip_management_system_ko
  - fiction_gsd_planning_bridge_ko
  - wiki_fiction_index
next_gate: use this guide before starting the next fiction GSD phase
last_updated: 2026-06-20
---

# Fiction GSD 하네스 운영 가이드

## 목적

이 문서는 `docs/wiki/fiction/` 작업을 시작할 때 사람이 바로 따라갈 수 있는
하네스 사용 설명서다.

짧게 말하면:

```text
fiction workflow = 어디에 속하는 작업인지 정한다
GSD = 이번 작업을 어떻게 닫을지 정한다
repo validation = 연구 경계와 문서 상태가 깨지지 않았는지 확인한다
```

## Workflow Boundary

This document introduces no external-source or source-product claim.

External-source handling remains governed by
[Research Asset and Product Workflow](../../../../.agent/workflows/research-asset-product-workflow.md).

Current workflow state:

```text
no_asset_found
```

## 구성 요소

| Layer | 파일/폴더 | 역할 |
| --- | --- | --- |
| Agent authority | [.agent/workflows/fiction-ip-management-workflow.md](../../../../.agent/workflows/fiction-ip-management-workflow.md) | fiction/IP 분류와 금지 규칙의 운영 SSOT |
| Human guide | [001 Fiction IP Management System](001_fiction_ip_management_system_ko.md) | 사람이 읽는 IP/studio 구조 설명 |
| GSD bridge | [002 Fiction GSD Planning Bridge](002_gsd_planning_bridge_ko.md) | GSD가 맡는 것과 맡지 않는 것 |
| Operator guide | 이 문서 | 실제 작업 시작 순서 |
| GSD state | `.planning/` | 현재 fiction/IP planning phase 상태 |
| Templates | [.agent/templates/fiction/](../../../../.agent/templates/fiction/) | work README, bible, session brief, GSD phase brief |
| Fiction shelf | [docs/wiki/fiction/](../README.md) | 실제 fiction system, 세계관, 개발, draft, archive |
| Craft harness | [004 Creative Writing Craft Harness](004_creative_writing_craft_harness_ko.md) | 문예창작 기본 개념, 한국어 용어 해설, 장면/인물/시점 체크리스트 |
| University reference matrix | [005 University Creative Writing Reference Matrix](005_university_creative_writing_reference_matrix_ko.md) | 대학/워크숍/과학 글쓰기 기준을 source state와 함께 반영하는 표 |

## 작업 시작 순서

새 fiction 작업은 아래 순서로 시작한다.

1. [Fiction IP Management Workflow](../../../../.agent/workflows/fiction-ip-management-workflow.md)를 읽는다.
2. [Creative Writing Craft Harness](004_creative_writing_craft_harness_ko.md)를 읽고
   용어, 장면, 인물, 시점 기준을 확인한다.
3. 대학, 문예창작과, writing program, workshop 기준을 참고한다면
   [University Creative Writing Reference Matrix](005_university_creative_writing_reference_matrix_ko.md)를
   먼저 확인한다.
4. 아이디어를 `studio`, `catalog`, `universe/IP`, `continuity`, `work`,
   `bible`, `story_design`, `draft`, `release`, `archive` 중 하나로 분류한다.
5. 새 작품이면 work README가 필요한지 먼저 판단한다.
6. 큰 작업이면 [Fiction GSD Phase Brief Template](../../../../.agent/templates/fiction/gsd_phase_brief_template.md)을 채운다.
7. `gsd-tools`로 phase 상태를 확인한다.
8. 사용자 확인이 필요한 선택지를 먼저 닫는다.
9. 문서/원고를 작성한다.
10. repo validation을 돌린다.
11. 좁게 stage하고 commit한다.

## GSD 명령 기본형

현재 worktree에서만 실행한다. 문서에는 개인 경로를 남기지 않는다.

```bash
gsd-tools --cwd <WORKTREE> validate health
gsd-tools --cwd <WORKTREE> init plan-phase 1 --skip-research --text --raw
gsd-tools --cwd <WORKTREE> phase-plan-index 1
```

새 phase를 추가해야 할 때는 먼저 phase brief를 작성하고, 사용자가 승인한 뒤
`phase add`를 사용한다.

```bash
gsd-tools --cwd <WORKTREE> phase add "Short description of the fiction/IP phase"
```

## 체크포인트

### 1. IP 분류

작업 전 반드시 답한다.

- 어느 universe/IP인가?
- canon, soft-canon, elseworld, prototype, retired 중 무엇인가?
- series, novel, short, anthology, webtoon-like run, elseworld 중 무엇인가?
- 작품 README가 이미 있는가?
- 기존 세계관을 상속하는가, 아니면 local override를 만드는가?

### 2. Tone / baseline

새 reference, work README, bible, scene plan은 authoring baseline date를 둔다.
기준일은 문서를 시작한 날짜다. `ancient`, `modern`, `post-COVID`, `pre-AGI`,
`future` 같은 말은 그 기준일과의 관계가 보여야 한다.

완전 창작 세계관이면 현실 기준일을 작중 canon으로 쓰지 않는다. 현실 기준일은
제작 맥락이고, 작중 시간은 calendar, year zero, story year, era id로 따로
정의한다.

문체는 짧고 직접적으로 쓴다.

- 전체 evidence disclaimer를 문서마다 반복하지 않는다.
- 비유는 장면이나 독해에 필요한 경우에만 쓴다.
- 설정 기준서는 정의, 표, 규칙, 장면 사용법 중심으로 쓴다.
- 사용자 개인 맥락은 내부 독자 감각에만 쓰고 문서/소설에 직접 넣지 않는다.

### 3. GSD 경계

GSD는 실행을 닫는다. canon을 결정하지 않는다.

GSD phase에 반드시 들어갈 것:

- applicable workflow;
- universe/IP;
- continuity status;
- target folder;
- allowed outputs;
- forbidden outputs;
- acceptance criteria;
- verification commands.

### 4. Science Auditor 경계

fiction은 QFUDS research가 아니다.

금지:

- fiction premise를 연구 결과처럼 쓰기;
- roadmap 상태 변경처럼 읽히는 문장 쓰기;
- 외부 paper, PDF, web source, MCP output을 workflow state 없이 claim하기;
- 연구 문서를 소설 설정에 맞춰 뒤집어 해석하기.

### 5. Technical grounding

기술어는 먼저 기술어로 둔다. `hash`, `KDF`, `key`, `salt`, `collision`처럼
이미 정확한 의미가 있는 말은 임의로 권리, 비용, 신원, 절차 같은 제도어로
바꾸지 않는다.

바꿔야 한다면 아래를 문서에 남긴다.

| 항목 | 질문 |
| --- | --- |
| Original term | 원래 기술어는 무엇인가? |
| Fictional alias | 작중 별칭은 무엇인가? |
| Rationale | 왜 바꾸는가? |
| Loss risk | 어떤 기술 의미가 흐려지는가? |
| Accurate anchor | 정확한 설명은 어디에 남는가? |
| Scene purpose | 이 별칭이 장면에서 하는 일은 무엇인가? |

### 6. Narrative frame

작업 전 아래를 답한다.

| 항목 | 질문 |
| --- | --- |
| Who speaks | 누가 말하는가? |
| Who sees | 누구의 인식으로 보는가? |
| Telling time | 사건과 말하는 시점의 거리는? |
| Form | 역사록, 회고록, 수필, 재판 기록, archive note, 직접 장면 중 무엇인가? |
| Implied audience | 누구에게 말하는가? |
| Motive | 왜 지금 말하는가? |
| Knowledge limit | 무엇을 알 수 없는가? |
| Distortion risk | 무엇을 왜곡하거나 숨길 수 있는가? |

### 7. Jargon / Korean-reader support

영어권 창작 용어를 쓰되, 한국어 독자가 바로 이해할 수 있게 첫 등장에 풀이한다.

예:

- `TBD`: 아직 정하지 않음. `To Be Determined`의 약자.
- `POV`: 시점. `Point of View`의 약자.
- `canon`: 정사. 작품 세계에서 확정된 설정.
- `beat`: 장면 안의 작은 전환점.

새 용어나 약어를 추가하면
[Creative Writing Craft Harness](004_creative_writing_craft_harness_ko.md)의
용어 해설 방식과 맞춘다.

### 8. Korean-primary prose sequence

active SAGA prose는 기본적으로 아래 순서로 작성한다.

```text
1. 한국어 본문 초안
2. 영어권 독자용 독립 각색판
3. 양쪽 continuity / field mark / boundary 점검
```

한국어판은 독자가 먼저 읽는 본문으로 자연스럽게 쓴다. 영어판은 한국어판을
직역하지 않고 같은 사건을 영미권 문체와 독서 리듬에 맞춰 다시 쓴다. 기존
English-first 원고는 provenance로 보존하되, active read order에서는 한국어
경로를 먼저 보여 준다.

### 9. Harness Applied 기록

active prose draft, release-facing revision plan, release candidate에는 본문
앞쪽에 `Harness Applied` 블록을 남긴다.

필수 항목:

- craft harness link;
- narrative frame;
- scene 또는 revision의 goal/obstacle/turn/cost;
- 한국어 primary / 영어 Anglophone sibling-text gate;
- 외부 source/product claim 여부와 research asset workflow boundary.

기존 legacy draft는 provenance로 보존할 때 생략할 수 있다. 그러나 그 원고를 새
revision이나 release 후보로 올릴 때는 먼저 이 블록을 추가한다.

## 다음 작업을 고르는 법

작업 유형별 추천 경로:

| 하고 싶은 일 | 먼저 할 일 | 산출물 위치 |
| --- | --- | --- |
| 새 장편/SAGA 시작 | universe/IP와 work README 결정 | `docs/wiki/fiction/10_universes/...` |
| 기존 SAGA 계속 쓰기 | canonical SAGA README read order 확인 | `docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/10_story_design/` 또는 `20_drafts/` |
| 세계관 정리 | canon 후보인지 development인지 분리 | `00_bible/` 또는 `10_story_design/` |
| 원고 쓰기 | work README와 bible/design 경계 확인 | `20_drafts/` |
| revision 준비 | continuity/line edit 목표 확인 | `30_revisions/` |
| release 후보 만들기 | 한국어 primary, 영어 counterpart, shared continuity check 완료 | `40_release/` |
| 폴더 migration | GSD phase로 계획 후 사용자 확인 | 별도 commit; 완료 후 catalog에 record |
| 외부 자료 참고 | Research Asset and Product Workflow 적용 | 문서별 workflow state 기록 |
| 대학식 문예창작 기준 참고 | 005 reference matrix 적용 | source state와 claim boundary 기록 |

## 최소 검증 루프

commit 전에는 아래를 실행한다.

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/agent_workflow_guard.py --staged
make preflight
sh <PRE_COMMIT_HOOK>
```

`<PRE_COMMIT_HOOK>`는 [scripts/git-hooks/pre-commit](../../../../scripts/git-hooks/pre-commit)을 뜻한다.

GSD phase를 만졌다면 추가로 아래를 확인한다.

```bash
gsd-tools --cwd <WORKTREE> validate health
gsd-tools --cwd <WORKTREE> phase-plan-index 1
```

## 현재 판정

현재 하네스는 기본 동작 가능하다.

- [Fiction IP Management Workflow](../../../../.agent/workflows/fiction-ip-management-workflow.md)가 운영 authority다.
- `001`은 사람용 IP/studio 설명서다.
- `002`는 GSD와 fiction workflow의 역할 분리 문서다.
- `.planning`은 현재 worktree 안에서 fiction/IP GSD phase를 추적한다.
- 이 문서는 실제 작업 시작 순서를 제공한다.

큰 구조 migration은 완료됐다. 현재 `qfuds-saga`는
`docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/` 아래의
canonical series work다. 옛 top-level `qfuds-saga/`와 `archive/`는
compatibility notice만 유지한다.
