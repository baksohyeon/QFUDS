---
doc_id: fiction_catalog_index_ko
title: Fiction Catalog
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - wiki_fiction_index
  - fiction_ip_management_system_ko
  - qfuds_saga_index_ko
next_gate: use the SAGA README and production board before choosing the next active drafting or design unit
last_updated: 2026-06-21
---

# Fiction Catalog

이 폴더는 `docs/wiki/fiction/`의 작품 목록, active shelf, migration 결정을
관리한다.

운영 규칙은
[Fiction IP Management Workflow](../../../../.agent/workflows/fiction-ip-management-workflow.md)
가 정한다. 이 catalog는 그 규칙을 사람이 보기 쉽게 적용한 상태판이다.

## Authoring Baseline

- 기준일: 2026-06-20
- 기준 역할: 실제 작성 시점과 repo 구조를 판단하는 기준
- 작중 canon 여부: 아님

`ancient`, `modern`, `future`, `post-AGI` 같은 말은 작품 문서 안에서 별도
기준을 잡아야 한다. 완전 창작 세계관은 현실 기준일과 작중 era id를 분리한다.

## Current Shelves

이 catalog는 active work 목록과 shelf 상태만 관리한다. 오늘 무엇을 할지는
[SAGA production board](../10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/009_saga_production_board_ko.md)가
정한다.

| Shelf | Path | Role | Status |
| --- | --- | --- | --- |
| Studio system | [../00_studio/](../00_studio/) | fiction/IP 관리, GSD bridge, craft harness | active |
| Universe scaffold | [../10_universes/qfuds-verse/](../10_universes/qfuds-verse/) | QFUDS-derived fiction universe/IP 컨테이너 | active prototype |
| Active SAGA | [../10_universes/qfuds-verse/20_series/qfuds-saga/](../10_universes/qfuds-verse/20_series/qfuds-saga/) | QFUDS-inspired long-form SAGA 작업 선반 | active series work |
| Archive | [../90_archive/](../90_archive/) | superseded prototype fiction | archived |

## Active Works

| Work | Current path | Format | Continuity status | Next decision |
| --- | --- | --- | --- | --- |
| QFUDS SAGA | [../10_universes/qfuds-verse/20_series/qfuds-saga/](../10_universes/qfuds-verse/20_series/qfuds-saga/) | long-form SAGA / series candidate | active series work | Check the SAGA README, production board, and latest story_design/draft map before choosing the next unit |
| Laur Observatory prototype | [../90_archive/lineage-prototype/](../90_archive/lineage-prototype/) | short prototype sequence | archived prototype | Keep archived unless a later work explicitly adapts it |

## Migration Decision Record

`qfuds-saga`와 legacy archive는 canonical fiction 구조로 이동 완료됐다. 새 작업은
canonical 경로에만 만들고, 옛 top-level `qfuds-saga/` 또는 `archive/` 경로를
재생성하지 않는다.

SAGA 내부 shelf는 `00_workroom/`, `00_bible/`, `10_story_design/`, `20_drafts/`,
`30_revisions/`, `40_release/`를 사용한다.

## Workflow Boundary

이 catalog는 새 외부 source, PDF, paper, MCP output, cached asset, extraction
product, source/product availability claim을 만들지 않는다.

Current research asset workflow state:

```text
not searched
```

Extraction potential:

```text
not_extractable
```

## Next Task Candidates

1. 작업 시작 전 [Fiction Agentic Workflow Guide](../00_studio/011_fiction_agentic_workflow_guide_ko.md)를 읽고,
   [SAGA production board](../10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/009_saga_production_board_ko.md)의
   현재 unit을 확인한다.
2. 원고 작업은 [SAGA README](../10_universes/qfuds-verse/20_series/qfuds-saga/README.md)와 production board가
   가리키는 active unit에서만 시작한다.
3. arc 번호 cascade가 걸린 draft README는 story design과 사용자 승인 후
   별도 pass로 정리한다.
4. `40_release/001_` active release는 한국어 primary, 영어 독립 각색판, shared continuity
   check, release-facing revision gate 이후에만 만든다.
