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
next_gate: continue qfuds-saga arc planning under canonical series path
last_updated: 2026-06-20
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
| Compatibility notices | [../qfuds-saga/](../qfuds-saga/), [../archive/](../archive/) | old top-level entrypoints | moved notices only |

## Active Works

| Work | Current path | Format | Continuity status | Next decision |
| --- | --- | --- | --- | --- |
| QFUDS SAGA | [../10_universes/qfuds-verse/20_series/qfuds-saga/](../10_universes/qfuds-verse/20_series/qfuds-saga/) | long-form SAGA / series candidate | active prototype series work | Plan the next arc from the Korean-primary read order |
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

기존 top-level `qfuds-saga/`와 `archive/`는 이동 완료됐다. 옛 경로에는 README
호환 안내문만 남긴다.

## Migration Decision Record

`qfuds-verse` scaffold와 기존 SAGA/archive 이동에 대한 결정은 아래와 같다.

1. Universe/IP id: `qfuds-verse`
2. Continuity policy: `active prototype`이며 canon은 아직 닫지 않는다.
3. Work id: `qfuds-saga`
4. Work format: long-form SAGA / series candidate
5. Work README contract: 기존 SAGA README를 series work README로 승격한다.
6. Existing shelf policy: 기존 `qfuds-saga/`는 canonical path로 이동하고,
   old path에는 compatibility notice만 남긴다.
7. Archive policy: `archive/`는 `90_archive/`로 이동하고, old path에는
   compatibility notice만 남긴다.

## Workflow Boundary

이 catalog는 새 외부 source, PDF, paper, MCP output, cached asset, extraction
product, source/product availability claim을 만들지 않는다.

Current workflow state:

```text
not_extractable
```

## Next Task Candidates

1. Arc Two 또는 first-arc polish task를 canonical SAGA path 아래에서 시작.
2. Liora Sen `Exhibit S-0` beat sheet를 실제 prose draft로 확장할지 결정.
3. Mara Veyr prologue와 Liora episode가 같은 continuity인지 분리할지 결정.
