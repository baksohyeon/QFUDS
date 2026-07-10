---
doc_id: qfuds_verse_continuity_index_ko
title: QFUDS Verse Continuity
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_verse_universe_index_ko
next_gate: 권위 지도(000)·딥타임 연표(001)·복원 행정 연표(002)를 여기서 관리. 시대 좌표 SSOT는 series 209
last_updated: 2026-07-10
---

# QFUDS Verse Continuity

이 폴더는 `qfuds-verse`의 continuity policy와 캐논 권위·연표 SSOT를 둔다.

## Continuity 문서 (SSOT)

2026-07-01 재레벨링으로 series bible에서 승격. 시대 좌표(인물별) SSOT는 series
[209 캐릭터 지도](../series-bible/209_character_map_and_timeline_coordinates_ko.md)가 유지한다.

| 문서 | 역할 |
| --- | --- |
| [000 캐논 권위·SSOT 지도](000_canon_authority_and_ssot_map_ko.md) | 충돌 시 어느 문서가 이기나(제작 권위 지도) |
| [001 장기 복원 문명사 타임라인](001_deep_time_restoration_timeline_ko.md) | 0-9기 딥타임 연대기(연표 SSOT) |
| [002 연표·복원 행정·블랙홀 본거지](002_chronology_restoration_admin_black_hole_seat_ko.md) | 연표·기술곡선·복원 행정 구조 |
| [003 먼 미래 심층시간 연대기](003_far_future_deep_time_chronicle_ko.md) | 001 5-9기를 수만-수억 년 물리 시계에 건 심층시간 확장(스파이스=검증 기록). 001 SSOT 위 레이어 |

## 감사·메타 리포트 (900번대, 읽기 전용 산출물)

| 문서 | 역할 |
| --- | --- |
| [900 월드빌딩 아키텍처 지도](900_worldbuilding_architecture_ko.md) | in-scope 80문서 인덱스·권위 트리·도메인 소유·의존/영향 그래프 |
| [901 Canon Drift·Tech Debt 리포트](901_canon_drift_and_tech_debt_report_ko.md) | 드리프트 원장·중복 병합 후보·candidate 백로그·리팩터 P0/P1/P2 |

## Current Policy

| Layer | Status | Rule |
| --- | --- | --- |
| Universe | active prototype | 상위 premise만 열린 상태 |
| QFUDS SAGA | active prototype series work | 20_series/qfuds-saga를 참조 |
| Laur Observatory | archived prototype | 새 작품이 명시적으로 각색할 때만 재사용 |
| Elseworld | not created | 다른 물리 premise가 필요할 때 만든다 |

## Canon Rule

현재 정사는 닫히지 않았다. `20_series/qfuds-saga/`의 series bible 문서는 canon
candidate로 읽고, universe-level canon으로 승격하려면 이 폴더에 별도 기록한다.

## Baseline

- Authoring baseline date: `2026-06-20`
- In-world chronology: not fixed
- Era IDs: not fixed

## Workflow Boundary

새 외부 자료나 source/product claim을 만들지 않는다.

Current research asset workflow state:

```text
not searched
```

Extraction potential:

```text
not_extractable
```

## 번호 체계 (2026-07-06 재번호)

선반별 밴드 번호를 쓴다(continuity 0xx / world 1xx / bible 2xx / story_design 3xx / workroom 4xx). 구→신 매핑은 workroom 417이 보유한다. 원고(20_drafts)·revisions·archive는 구번호 유지.
