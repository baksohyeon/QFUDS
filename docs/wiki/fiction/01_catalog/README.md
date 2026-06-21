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
next_gate: continue qfuds-saga 029 first-arc Book 1 Korean-primary reboot manuscript
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

| Shelf | Path | Role | Status |
| --- | --- | --- | --- |
| Studio system | [../00_studio/](../00_studio/) | fiction/IP 관리, GSD bridge, craft harness | active |
| Universe scaffold | [../10_universes/qfuds-verse/](../10_universes/qfuds-verse/) | QFUDS-derived fiction universe/IP 컨테이너 | active prototype |
| Active SAGA | [../10_universes/qfuds-verse/20_series/qfuds-saga/](../10_universes/qfuds-verse/20_series/qfuds-saga/) | QFUDS-inspired long-form SAGA 작업 선반 | active series work |
| Archive | [../90_archive/](../90_archive/) | superseded prototype fiction | archived |

## Active Works

| Work | Current path | Format | Continuity status | Next decision |
| --- | --- | --- | --- | --- |
| QFUDS SAGA | [../10_universes/qfuds-verse/20_series/qfuds-saga/](../10_universes/qfuds-verse/20_series/qfuds-saga/) | long-form SAGA / series candidate | active reboot manuscript in progress | Continue 029 Chapter 2 after Prologue + Chapter 1 draft pass |
| Laur Observatory prototype | [../90_archive/lineage-prototype/](../90_archive/lineage-prototype/) | short prototype sequence | archived prototype | Keep archived unless a later work explicitly adapts it |

## Target Structure

새 major fiction work는 장기적으로 아래 구조를 따른다.

```text
docs/wiki/fiction/
  01_catalog/
  10_universes/
    <universe-id>/
      README.md
      00_continuity/
      10_world/
      20_series/
      30_shorts/
      40_anthologies/
      50_elseworlds/
```

기존 top-level `qfuds-saga/`와 `archive/`는 이동 완료 후 삭제됐다. 새 작업은
canonical 경로에만 만들고, 옛 경로를 재생성하지 않는다.

## Migration Decision Record

`qfuds-verse` scaffold와 기존 SAGA/archive 이동에 대한 결정은 아래와 같다.

1. Universe/IP id: `qfuds-verse`
2. Continuity policy: `active prototype`이며 canon은 아직 닫지 않는다.
3. Work id: `qfuds-saga`
4. Work format: long-form SAGA / series candidate
5. Work README contract: 기존 SAGA README를 series work README로 승격한다.
6. Existing shelf policy: 기존 `qfuds-saga/`는 canonical path로 이동하고,
   old path는 삭제한다.
7. Archive policy: `archive/`는 `90_archive/`로 이동하고, old path는
   삭제한다.
8. Internal shelf policy: SAGA 내부는 `00_workroom/`, `00_bible/`,
   `10_story_design/`, `20_drafts/`, `30_revisions/`, `40_release/`를 사용한다.

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

1. QFUDS SAGA 1부 [029 active reboot manuscript](../10_universes/qfuds-verse/20_series/qfuds-saga/20_drafts/029_first_arc_book1_reboot_korean_primary.md)에서 [007 GSD phase brief](../10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/007_first_arc_book1_gsd_phase_brief_ko.md)의 hard floor를 지키며 Chapter 2 `The Dead Exchange`를 이어 쓴다.
2. [013 scene cards](../10_universes/qfuds-verse/20_series/qfuds-saga/10_story_design/013_first_arc_scene_cards_ko.md)는 first draft entry 기준으로 통과했지만 release gate는 아니다.
3. `40_release/001_` active release는 029 전체 한국어 primary, 영어 독립 각색판, shared continuity check, release-facing revision gate 이후에만 만든다.
