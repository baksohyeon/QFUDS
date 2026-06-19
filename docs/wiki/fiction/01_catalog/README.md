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
next_gate: create universe/work scaffold only after user confirmation
last_updated: 2026-06-19
---

# Fiction Catalog

이 폴더는 `docs/wiki/fiction/`의 작품 목록, active shelf, migration 후보를
관리한다.

운영 규칙은
[Fiction IP Management Workflow](../../../../.agent/workflows/fiction-ip-management-workflow.md)
가 정한다. 이 catalog는 그 규칙을 사람이 보기 쉽게 적용한 상태판이다.

## Authoring Baseline

- 기준일: 2026-06-19
- 기준 역할: 실제 작성 시점과 repo 구조를 판단하는 기준
- 작중 canon 여부: 아님

`ancient`, `modern`, `future`, `post-AGI` 같은 말은 작품 문서 안에서 별도
기준을 잡아야 한다. 완전 창작 세계관은 현실 기준일과 작중 era id를 분리한다.

## Current Shelves

| Shelf | Path | Role | Status |
| --- | --- | --- | --- |
| Studio system | [../00_studio/](../00_studio/) | fiction/IP 관리, GSD bridge, craft harness | active |
| Universe scaffold | [../10_universes/qfuds-verse/](../10_universes/qfuds-verse/) | QFUDS-derived fiction universe/IP 컨테이너 | active prototype |
| Active SAGA | [../qfuds-saga/](../qfuds-saga/) | QFUDS-inspired long-form SAGA 작업 선반 | active prototype |
| Archive | [../archive/](../archive/) | superseded prototype fiction | archived |

## Active Works

| Work | Current path | Format | Continuity status | Next decision |
| --- | --- | --- | --- | --- |
| QFUDS SAGA | [../qfuds-saga/](../qfuds-saga/) | long-form SAGA / series candidate | active prototype, not migrated | Create work README before any move under `qfuds-verse` |
| Laur Observatory prototype | [../archive/lineage-prototype/](../archive/lineage-prototype/) | short prototype sequence | archived prototype | Keep archived unless a later work explicitly adapts it |

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

현재 `qfuds-saga/`는 바로 이동하지 않는다. 이동은 별도 migration task로만 한다.

## Migration Gate

`qfuds-verse` scaffold는 생성됐다. `qfuds-saga/`를 IP 구조로 옮기려면 먼저
아래를 결정한다.

1. Universe/IP id: `qfuds-verse`
2. Continuity policy: canon, soft-canon, elseworld, prototype 기준
3. Work id: 예: `qfuds-saga`
4. Work format: series, novel, short, anthology, webtoon-like run 중 무엇인지
5. README contract: universe README와 work README를 먼저 만들지 여부
6. Existing shelf policy: 기존 `qfuds-saga/`를 이동할지, compatibility link를 남길지
7. Archive policy: `archive/`를 `90_archive/`로 바꿀지 여부

## Workflow Boundary

이 catalog는 새 외부 source, PDF, paper, MCP output, cached asset, extraction
product, source/product availability claim을 만들지 않는다.

Current workflow state:

```text
not_extractable
```

## Next Task Candidates

1. `qfuds-saga` work README 초안을 만들지 사용자 확인.
2. Liora Sen `Exhibit S-0` beat sheet를 실제 prose draft로 확장할지 결정.
3. Mara Veyr prologue와 Liora episode가 같은 continuity인지 분리할지 결정.
