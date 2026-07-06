---
doc_id: fiction_folder_classification_audit_ko
title: Fiction Folder Classification Audit
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - fiction_catalog_index_ko
  - wiki_fiction_index
  - qfuds_verse_world_canon_orientation_ko
  - qfuds_saga_canon_authority_and_ssot_map_ko
next_gate: classify one folder at a time and move only confirmed legacy/tool material out of active universe shelves
last_updated: 2026-07-06
---

# Fiction Folder Classification Audit

작성 기준일: 2026-07-06 KST. 이 문서는 `docs/wiki/fiction/`을 폴더 단위로
정리하기 위한 작업 상태판이다. 새 캐논을 만들지 않는다. 기존 문서가 여러 루프에서
쌓이며 설정, 하네스, 기획, 수정 흔적이 한꺼번에 보이는 문제를 줄이기 위해, 폴더의
역할과 다음 조치를 분리한다.

```text
fiction/provenance only
QFUDS research evidence: no
roadmap status: unchanged
external source claim: no
```

## 분류 기준

| 분류 | 뜻 | 기본 조치 |
| --- | --- | --- |
| `active_system` | 현재 fiction 운영 규칙, catalog, harness | 유지. README와 index만 간결화 |
| `active_universe` | 현재 살아 있는 universe/IP | 유지. 첫 진입점과 권위 지도를 명확히 함 |
| `active_work` | 현재 작업 가능한 series/anthology/short work | 유지. work README와 production board 우선 |
| `prototype` | 살아 있으나 정사/릴리즈가 닫히지 않은 실험 | 유지하되 active canon처럼 읽지 않게 표시 |
| `archive` | 과거 구조, 레거시, superseded material | `90_archive/`에 보존. active read order에서 제외 |
| `tool_plugin` | 창작 도구, Claude plugin, skill source | canon 아님. active universe와 분리 후보 |
| `stray_noise` | macOS 산출물, 임시 파일 등 | 제거 |

## Top-Level Folder Map

| Folder | 분류 | 판단 | 조치 |
| --- | --- | --- | --- |
| `00_studio/` | `active_system` | fiction/IP 운영 규칙, craft/readability harness, guide가 모여 있다. | 유지. 중복 선언이 많아지면 `.agent/workflows/` 링크 중심으로 축소 |
| `01_catalog/` | `active_system` | 작품 목록, active shelf, migration 결정을 관리한다. | 유지. 이 문서를 catalog 상태판으로 사용 |
| `10_universes/` | `active_universe` container | universe/IP 컨테이너다. | 유지. universe별 active/prototype/archive 상태를 catalog에 반영 |
| `90_archive/` | `archive` | superseded/prototype fiction 보존소다. | 유지. archive read order를 계속 갱신 |
| `../../../../tools/saga-fiction-studio/` | `tool_plugin` | 실제 Claude plugin source다. 세계관, canon, draft가 아니다. | 2026-07-06 `docs/wiki/fiction/` 밖의 `tools/`로 이동 완료 |

## Universe Folder Map

| Folder | 분류 | 판단 | 조치 |
| --- | --- | --- | --- |
| `10_universes/qfuds-verse/` | `active_universe` | QFUDS-derived fiction universe/IP. 현재 SAGA의 부모 universe다. | 유지. 첫 진입점은 [000 세계관 한 장 기준서](../10_universes/qfuds-verse/000_world_canon_orientation_ko.md) |
| `10_universes/qfuds-verse/00_continuity/` | `active_universe/continuity` | 캐논 권위, 연표, continuity drift를 관리한다. | 유지. 충돌 시 권위 지도 우선 |
| `10_universes/qfuds-verse/10_world/` | `active_universe/world` | 공유 세계 규칙, 세력, Q-Day, 복원, 언어, 확장 wave가 있다. | 유지. 후보 wave는 canon처럼 읽지 않게 각 문서 상태 확인 필요 |
| `10_universes/qfuds-verse/20_series/` | `active_work_container` | qfuds-verse의 series shelf다. | 유지 |
| `10_universes/qfuds-verse/20_series/qfuds-saga/` | `active_work` | 현재 active long-form SAGA work다. | 유지. SAGA README, production board, 209 시대좌표 우선 |
| `10_universes/qfuds-verse/web/` | `prototype/tool_surface` | 세계관 시각화 웹앱과 파생 data/font/vendor를 포함한다. canon source가 아니다. | 유지 후보. 다음 루프에서 `web/`을 active universe 밑에 둘지 별도 artifact shelf로 둘지 결정 |
| `10_universes/vector-sandbox/` | `prototype` | qfuds-verse와 형제인 별도 universe/IP. qfuds-verse canon을 상속하지 않는다. | 유지. catalog에서 active prototype으로 표시 |
| `10_universes/vector-sandbox/10_world/` | `prototype/world` | vector-sandbox의 세계 규칙이다. | 유지 |
| `10_universes/vector-sandbox/40_anthologies/feathersmcgraw-coda/` | `active_work/prototype` | vector-sandbox의 anthology work다. | 유지. SAGA와 별개 work로 계속 분리 |

## QFUDS SAGA Work Shelf Map

| Folder | 분류 | 판단 | 조치 |
| --- | --- | --- | --- |
| `qfuds-saga/00_workroom/` | `active_work/workroom` | SAGA-local 운영 규칙, production board, review/gate 문서가 있다. | 유지. 세계 canon을 여기에 넣지 않음 |
| `qfuds-saga/00_bible/` | `active_work/bible` | 시리즈 전용 캐릭터, POV, 주제, 캐스트 기준서다. | 유지. 공유 세계 규칙은 `10_world/` 우선 |
| `qfuds-saga/10_story_design/` | `active_work/story_design` | outline, arc map, reveal plan, reader orientation, 후보 설계가 있다. | 유지. 후보와 확정 상태를 각 문서에서 확인 |
| `qfuds-saga/20_drafts/` | `active_work/drafts` | 산문 draft와 부별 원고 shelf다. | 유지. 원고 직접 수정은 여기서만 |
| `qfuds-saga/30_revisions/` | `active_work/revisions` | release-facing revision, audit, gate 준비 문서다. | 유지. release gate와 연결 |
| `qfuds-saga/40_release/` | `active_work/release` | release/export shelf다. | 유지. source가 아니라 gate 통과 산출물로 취급 |

## Archive Map

| Folder | 분류 | 판단 | 조치 |
| --- | --- | --- | --- |
| `90_archive/lineage-prototype/` | `archive` | Laur Observatory 초기 fiction companion. | 보존. active read order에서 제외 |
| `90_archive/qfuds-saga_1부_legacy/` | `archive` | 1세대 1부 drafts. 현 SAGA 구조가 대체했다. | 보존 |
| `90_archive/qfuds-saga_pre_reboot_planning/` | `archive` | reboot 이전 workroom/story_design/revision 계획. | 보존 |
| `90_archive/fiction_v2_legacy/` | `archive` | `fiction_v2` reader/report/HTML explorer layer. 새 첫 진입점으로 대체됨. | 2026-07-06 active `qfuds-verse` shelf에서 archive로 이동 완료 |

## 이번 루프에서 처리한 것

| 항목 | 처리 |
| --- | --- |
| `qfuds-verse/fiction_v2/` | active universe에서 제거하고 `90_archive/fiction_v2_legacy/`로 이동 |
| `saga-fiction-studio/` | active fiction tree에서 제거하고 `tools/saga-fiction-studio/`로 이동 |
| `qfuds-verse/000_world_canon_orientation_ko.md` | 새 첫 진입점으로 추가 |
| `qfuds-verse/README.md` | Start Here에 세계관 한 장 기준서 연결 |
| `qfuds-saga/README.md` | SAGA 시작 표에 전체 세계관 진입 링크 추가 |
| `10_universes/.DS_Store` | 추적되지 않는 macOS 산출물 제거 |
| `00_studio/` + `.agent/templates/fiction/` | [003 content review audit](003_fiction_content_review_audit_ko.md)에 첫 내용 검토 기록 |
| `00_studio/` 중복 가이드 통합 | 2026-07-06 001·002를 003으로, 008을 011로 통합(포인터 stub, doc_id 보존). README 유형 열 추가 |

## 다음 루프 후보

1. [003 content review audit](003_fiction_content_review_audit_ko.md)의 순서대로
   `qfuds-verse/00_continuity/`, `qfuds-verse/10_world/`를 검토한다.
2. `qfuds-verse/web/`을 active universe 산출물로 둘지, artifact/web shelf로 분리할지
   결정한다.
3. `10_world/117-122` 같은 expansion wave 문서가 canon인지 candidate인지 각 문서
   frontmatter와 본문을 기준으로 표기한다.
4. `20_drafts/` 부별 README와 production board가 같은 active unit을 가리키는지
   확인한다.
5. archive 폴더의 read order가 active README와 상호 충돌하지 않는지 확인한다.

## 금지

- 레거시를 지운 뒤 없었던 일처럼 처리하지 않는다.
- candidate/prototype을 canon으로 승격하지 않는다.
- fiction premise를 QFUDS 연구 증거로 쓰지 않는다.
- active workroom, draft, release, plugin source를 같은 성격의 문서처럼 읽지 않는다.
