---
doc_id: qfuds_verse_continuity_index_ko
title: QFUDS Verse Continuity
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_verse_universe_index_ko
next_gate: maintain the retained universe authority map; QFUDS SAGA production remains closed
last_updated: 2026-07-11
---

# QFUDS Verse Continuity

이 폴더는 `qfuds-verse`의 continuity policy와 캐논 권위·연표 SSOT를 둔다.

## Continuity 문서 (SSOT)

2026-07-01 재레벨링으로 series bible에서 승격. 시대 좌표(인물별) SSOT는 series
[209 캐릭터 지도](../series-bible/character_map_and_timeline_coordinates.md)가 유지한다.

| 문서 | 역할 |
| --- | --- |
| [000 캐논 권위·SSOT 지도](canon_authority_and_ssot_map.md) | 충돌 시 어느 문서가 이기나(제작 권위 지도) |
| [001 장기 복원 문명사 타임라인](deep_time_restoration_timeline.md) | 0-9기 딥타임 연대기(연표 SSOT) |
| [002 연표·복원 행정·블랙홀 본거지](chronology_restoration_admin_black_hole_seat.md) | 연표·기술곡선·복원 행정 구조 |
| [003 먼 미래 심층시간 연대기](far_future_deep_time_chronicle.md) | 001 5-9기를 수만-수억 년 물리 시계에 건 심층시간 확장(스파이스=검증 기록). 001 SSOT 위 레이어 |

## 감사·메타 리포트 (900번대, 읽기 전용 산출물)

| 문서 | 역할 |
| --- | --- |
| [900 월드빌딩 아키텍처 지도](worldbuilding_architecture.md) | in-scope 80문서 인덱스·권위 트리·도메인 소유·의존/영향 그래프 |
| [901 Canon Drift·Tech Debt 리포트](canon_drift_and_tech_debt_report.md) | 드리프트 원장·중복 병합 후보·candidate 백로그·리팩터 P0/P1/P2 |

## Current Policy

| Layer | Status | Rule |
| --- | --- | --- |
| Universe | active prototype | 상위 premise만 열린 상태 |
| QFUDS SAGA | production closed 2026-07-10 | retained `series-bible/` is reference; production is Git history only |
| Laur Observatory | archived prototype | 새 작품이 명시적으로 각색할 때만 재사용 |
| Elseworld | not created | 다른 물리 premise가 필요할 때 만든다 |

## Canon Rule

현재 정사는 닫히지 않았다. 유지된 [`series-bible/`](../series-bible/README.md)은
QFUDS SAGA의 과거 series reference로 읽는다. 새 작품이 내용을 상속하려면 해당
project README에서 candidate를 명시하고, universe-level canon 승격은 이 폴더의
권위 지도에 기록한다.

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

## Legacy Numbering

과거 story design, workroom, draft, revision 번호 체계는 Git history에만 남는다.
현재 active 경로와 승격 규칙으로 사용하지 않는다.
