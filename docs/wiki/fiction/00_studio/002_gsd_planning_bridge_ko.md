---
doc_id: fiction_gsd_planning_bridge_ko
title: Fiction GSD Planning Bridge
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - fiction_ip_management_system_ko
  - wiki_fiction_index
next_gate: use this bridge when starting a fiction/IP GSD phase
last_updated: 2026-06-19
---

# Fiction GSD Planning Bridge

## 목적

GSD는 fiction/IP 시스템을 대체하지 않는다. GSD는 실행 phase를 관리한다.

이 문서는 fiction 작업을 GSD로 굴릴 때 역할을 분리하기 위한 bridge다.

```text
Fiction IP workflow = 이 아이디어가 어디에 속하고 무엇인지 정한다
GSD planning = 이번 phase에서 무엇을 끝낼지 정한다
```

운영 authority:

- [Fiction IP Management Workflow](../../../../.agent/workflows/fiction-ip-management-workflow.md)
- [Fiction GSD Phase Brief Template](../../../../.agent/templates/fiction/gsd_phase_brief_template.md)

## Workflow Boundary

This document introduces no external-source or source-product claim.

External-source handling remains governed by
[Research Asset and Product Workflow](../../../../.agent/workflows/research-asset-product-workflow.md).

Current workflow state:

```text
no_asset_found
```

## GSD가 맡는 것

GSD는 작업 단위를 닫는 데 쓴다.

- `qfuds-saga`를 `qfuds-verse` 아래로 migration할지 검토.
- `01_catalog/`와 `10_universes/` scaffold를 만드는 phase.
- 새 단편/장편/웹툰식 run의 README, bible, story design, draft를 순서대로
  만드는 phase.
- 여러 문서를 건드리는 restructuring.
- review, verification, commit, handoff를 묶는 phase.

## GSD가 맡으면 안 되는 것

GSD는 canon을 결정하지 않는다.

- GSD phase plan은 fiction canon이 아니다.
- GSD가 universe/IP 분류를 생략하면 안 된다.
- GSD가 README 없는 원고 추가를 허용하면 안 된다.
- GSD가 fiction premise를 연구 결과나 상태 변경으로 바꾸면 안 된다.

## Phase 문서에 반드시 들어갈 것

fiction/IP GSD phase는 최소한 아래 항목을 가져야 한다.

| 항목 | 이유 |
| --- | --- |
| Applicable workflow | 반드시 fiction IP workflow를 따른다는 선언 |
| Universe/IP | 어느 세계관/IP 소속인지 |
| Continuity status | canon, soft-canon, elseworld, prototype, retired |
| Work id / format | series, novel, short, anthology, webtoon, elseworld |
| Target folder | 어디에 파일을 만들지 |
| Allowed outputs | 이번 phase가 만들 수 있는 산출물 |
| Forbidden outputs | 원고만 추가, 증거화, canon 점프를 막음 |
| Acceptance criteria | phase 완료 기준 |
| Verification | commit 전 검증 루프 |

## 추천 사용법

새 fiction 작업은 이렇게 시작한다.

```text
1. 아이디어를 fiction/IP workflow로 분류한다.
2. universe/IP와 continuity status를 정한다.
3. work README가 필요한지 판단한다.
4. GSD phase brief를 작성한다.
5. phase acceptance criteria를 사용자에게 확인한다.
6. 실행한다.
7. 검증하고 commit한다.
```

## 다음 후보 phase

가장 자연스러운 다음 GSD phase는 **Fiction IP Studio Scaffold**다.

목표:

- `docs/wiki/fiction/01_catalog/` scaffold 생성.
- `docs/wiki/fiction/10_universes/qfuds-verse/` scaffold 생성.
- 현재 `qfuds-saga/`는 이동하지 않고, 이동 후보로만 분류.
- 사용자 확인 전에는 전체 migration을 하지 않음.

이 phase는 계획/스캐폴드 작업이지 원고 작성 작업이 아니다.
