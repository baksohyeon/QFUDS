---
doc_id: fiction_gsd_harness_operator_guide_ko
title: Fiction GSD Harness Operator Guide
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - fiction_ip_management_system_ko
  - fiction_gsd_planning_bridge_ko
  - wiki_fiction_index
next_gate: use this guide before starting the next fiction GSD phase
last_updated: 2026-06-19
---

# Fiction GSD Harness Operator Guide

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

This document does not introduce a new external asset, cached source, extraction
product, source-product availability claim, or QFUDS evidence claim.

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

## 작업 시작 순서

새 fiction 작업은 아래 순서로 시작한다.

1. [Fiction IP Management Workflow](../../../../.agent/workflows/fiction-ip-management-workflow.md)를 읽는다.
2. 아이디어를 `studio`, `catalog`, `universe/IP`, `continuity`, `work`,
   `bible`, `story_design`, `draft`, `release`, `archive` 중 하나로 분류한다.
3. 새 작품이면 work README가 필요한지 먼저 판단한다.
4. 큰 작업이면 [Fiction GSD Phase Brief Template](../../../../.agent/templates/fiction/gsd_phase_brief_template.md)을 채운다.
5. `gsd-tools`로 phase 상태를 확인한다.
6. 사용자 확인이 필요한 선택지를 먼저 닫는다.
7. 문서/원고를 작성한다.
8. repo validation을 돌린다.
9. 좁게 stage하고 commit한다.

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

### 2. GSD 경계

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

### 3. Science Auditor 경계

fiction은 QFUDS research가 아니다.

금지:

- fiction premise를 QFUDS evidence처럼 쓰기;
- QFUDS support, validation, Level 2B admission 언어 쓰기;
- 외부 paper, PDF, web source, MCP output을 workflow state 없이 claim하기;
- 연구 문서를 소설 설정에 맞춰 뒤집어 해석하기.

## 다음 작업을 고르는 법

작업 유형별 추천 경로:

| 하고 싶은 일 | 먼저 할 일 | 산출물 위치 |
| --- | --- | --- |
| 새 장편/SAGA 시작 | universe/IP와 work README 결정 | `docs/wiki/fiction/10_universes/...` 또는 현행 `qfuds-saga/` |
| 기존 SAGA 계속 쓰기 | `qfuds-saga/README.md` read order 확인 | `qfuds-saga/20_development/` 또는 `30_drafts/` |
| 세계관 정리 | canon 후보인지 development인지 분리 | `10_series_bible/` 또는 `20_development/` |
| 원고 쓰기 | work README와 bible/design 경계 확인 | `30_drafts/` |
| 폴더 migration | GSD phase로 계획 후 사용자 확인 | 별도 commit |
| 외부 자료 참고 | Research Asset and Product Workflow 적용 | 문서별 workflow state 기록 |

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

남은 큰 결정은 migration이다. 현재 `qfuds-saga/`는 active prototype track으로
두고, 사용자 확인 전에는 `10_universes/qfuds-verse/` 아래로 이동하지 않는다.
