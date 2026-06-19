---
doc_id: fiction_ip_management_system_ko
title: Fiction IP Management System
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - wiki_fiction_index
  - qfuds_saga_index_ko
next_gate: migrate active fiction folders only after user confirmation
last_updated: 2026-06-19
---

# Fiction IP Management System

## 목적

이 문서는 `docs/wiki/fiction/`을 단순 소설 폴더가 아니라 **fiction studio /
IP 관리 시스템**으로 다루기 위한 사람용 설명서다.

운영 authority는
[Fiction IP Management Workflow](../../../../.agent/workflows/fiction-ip-management-workflow.md)
다. 이 문서는 그 workflow를 사람이 읽기 쉽게 요약한다.

GSD phase로 실행할 때는
[Fiction GSD Planning Bridge](002_gsd_planning_bridge_ko.md)를 같이 읽는다.

## Workflow Boundary

This document does not introduce a new external asset, cached source, extraction
product, or QFUDS evidence claim.

External-source handling remains governed by
[Research Asset and Product Workflow](../../../../.agent/workflows/research-asset-product-workflow.md).

Current workflow state:

```text
not_extractable
```

## 핵심 판단

작품을 먼저 만들지 않는다. 먼저 IP 소속을 정한다.

```text
idea -> universe/IP -> continuity status -> work folder -> bible/design/draft
```

각 작품은 자기 폴더와 README를 가져야 한다. README는 계약서처럼 다음을
고정한다.

- 어떤 universe/IP에 속하는가.
- canon, soft-canon, elseworld, prototype, retired 중 무엇인가.
- 어떤 세계관/연표/과학 경계를 상속하는가.
- 이 작품만의 local override는 무엇인가.
- bible, story design, drafts, release가 어디에 있는가.
- fiction/provenance only boundary가 무엇인가.

## 권장 구조

새로운 대형 fiction 작업은 아래 구조를 목표로 한다.

```text
docs/wiki/fiction/
  00_studio/
  01_catalog/
  10_universes/
    00_multiverse/
    <universe-id>/
      README.md
      00_continuity/
      10_world/
      20_series/
      30_shorts/
      40_anthologies/
      50_elseworlds/
  90_archive/
```

각 작품 폴더는 아래 구조를 따른다.

```text
<work-id>/
  README.md
  00_bible/
  10_story_design/
  20_drafts/
  30_revisions/
  40_release/
```

## Layer Definitions

| Layer | 역할 | 예시 |
| --- | --- | --- |
| `00_studio/` | agent, MCP, template, approval gate, 검수 규칙 | 지금 문서 |
| `01_catalog/` | 전체 작품 목록, reading order, status board | future catalog |
| `10_universes/` | 여러 IP/world container | `qfuds-verse`, future universes |
| `00_continuity/` | canon, soft-canon, elseworld, prototype, retired 판정 | branch map |
| `10_world/` | universe 공통 세계관, 과학 경계, 기관, 연표 | QFUDS fiction universe |
| `20_series/` | 장편/SAGA/시즌제 작품 | `qfuds-saga` |
| `30_shorts/` | 단편 | future short |
| `40_anthologies/` | 단편 모음집 | future anthology |
| `50_elseworlds/` | What-if / 평행우주 / 실험 분기 | future elseworld |
| `00_bible/` | 작품별 내부 기준서 | cast, POV, local canon |
| `10_story_design/` | 플롯, arc, scene list, reveal order | outline |
| `20_drafts/` | 실제 원고 | prose draft |

## Bible Usage

`bible`은 전체 fiction 폴더명으로 쓰지 않는다. 각 작품 안에서만 쓴다.

이 repo에서 `00_bible/`은 "성경"이 아니라 작가실 내부 기준서다. 한 작품의
캐릭터, 시점, 말투, local canon, 금기, 상속한 세계관, local override를 관리한다.

독자에게 보이는 세계관 설명은 `10_world/`나 작품 README가 맡는다.

## Migration Boundary

현재 `qfuds-saga/`는 active prototype track이다. 바로 전체 migration하지 않는다.

다음 migration은 사용자 확인 후 별도 커밋으로 수행한다.

1. `docs/wiki/fiction/01_catalog/` 생성.
2. `docs/wiki/fiction/10_universes/qfuds-verse/` 생성.
3. 기존 `qfuds-saga/`를 `qfuds-verse/20_series/qfuds-saga/`로 이동할지 결정.
4. old archive를 `90_archive/`로 이동할지 결정.
5. 모든 README와 index를 재검증.

## GSD 사용 경계

GSD는 실행 phase를 관리한다. fiction/IP 분류를 대체하지 않는다.

즉 GSD는 "이번 작업에서 무엇을 끝낼 것인가"를 관리하고,
[Fiction IP Management Workflow](../../../../.agent/workflows/fiction-ip-management-workflow.md)
는 "이 아이디어가 어느 universe/IP와 continuity에 속하는가"를 관리한다.

fiction 작업을 GSD로 시작할 때는
[Fiction GSD Phase Brief Template](../../../../.agent/templates/fiction/gsd_phase_brief_template.md)
을 사용한다.

## 금지

- 작품 폴더 없이 원고만 추가하지 않는다.
- README 없이 series/short/anthology/elseworld를 만들지 않는다.
- "대충 QFUDS 느낌"이라고 쓰지 않는다. universe/IP와 continuity status를
  명시한다.
- fiction premise를 QFUDS evidence, validation, Level 2B admission으로 쓰지
  않는다.
