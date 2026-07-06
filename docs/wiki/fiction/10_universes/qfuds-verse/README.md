---
doc_id: qfuds_verse_universe_index_ko
title: QFUDS Verse
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - fiction_catalog_index_ko
  - fiction_ip_management_system_ko
  - qfuds_saga_index_ko
next_gate: continue qfuds-saga arc planning under normalized work shelves
last_updated: 2026-07-06
---

# QFUDS Verse

`qfuds-verse`는 QFUDS에서 파생된 fiction universe/IP 컨테이너다.

이 scaffold는 QFUDS SAGA를 정식 series work로 포함한다. 기존
`docs/wiki/fiction/qfuds-saga/` 호환 폴더는 migration 완료 후 삭제됐고,
canonical 작업 위치는 `20_series/qfuds-saga/`이다.

## Codex (시각화 웹앱)

세계관을 3D 성좌 + 연대기/인물/체계/사전으로 훑고, 아카이브에 질의하고,
시드를 모아 문서 승격 재료로 뽑는 자기완결 웹앱: **[`web/`](web/)**
(배포: [배포 가이드](web/DEPLOY.md), Dokku `git push dokku main`).
데이터는 이 유니버스 문서(001 딥타임 연표·115/116 Q-Day·117–122 확장 웨이브·
003/126 심층시간·123 이념축 등)에서 파생한다.

## Classification

- Universe/IP id: `qfuds-verse`
- Parent continuity: `none`
- Status: `active prototype`
- Authoring baseline date: `2026-06-20`
- Time baseline notes: 실제 작성 시점은 2026-06-20이다. 작중 연표는 아직
  확정하지 않는다.

## Premise

이 universe는 QFUDS 연구 과정에서 나온 질문을 fiction premise로 다룬다.

- 정보 보존과 완전 복원
- cryptographic death와 암호학 붕괴
- post-AGI 문명과 현실 편집
- Bitcoin / Genesis Chain artifact
- black-hole, white-hole, Hawking radiation, restoration myth
- QFUDS가 현실 증거가 아니라 어떤 story layer에서는 맞는 가정

## Continuity

- Canon policy: 현재는 `active prototype`. 정사는 아직 닫히지 않았다.
- Master timeline: [00_continuity/](00_continuity/)에서 관리한다.
- Branch map: 아직 없음.
- Elseworld policy: 다른 물리 premise나 다른 결말을 쓰면 elseworld 후보로
  분리한다.

## World

- Core science-fiction premise: 정보는 완전히 사라지지 않을 수 있고, 먼
  미래 문명은 그 잔상을 복원하려 한다.
- Institutions: [10_world/](10_world/)에서 관리한다. 공유 세계 캐논(세력 102·명칭 109·
  물리 113/114·암호 전제 105/108·역사 103/104/110·Q-Day 115/116 등)은 이제 여기(`10_world`)에
  산다. 듄급 세계 밀도 대사전은 [10_world/117](10_world/117_world_expansion_wave1_names_places_events_ko.md)
  candidate register에서 웨이브로 확장한다.
- Factions: SSOT는 `10_world/`(102 세력·109 명칭)이 보유하고, 하위 가문·분파 확장은
  10_world/117에서 후보로 짓는다.
- Continuity: 캐논 권위 지도(000)·딥타임 연표(001)·복원 행정 연표(002)는 [00_continuity/](00_continuity/)에 있다.
- Technology limits: 기술어는 보존한다. `hash`, `KDF`, `key`, `salt`,
  `collision`, `entropy`, `Hawking radiation`, `AGI`, `QFUDS`는 근거 없이
  별칭으로 바꾸지 않는다.
- Terms and symbols: Bitcoin, Genesis Chain, Last Archive, Continuity Court,
  Cryptographic Death는 canon candidate다.
- Forbidden claims: fiction premise를 QFUDS 연구 evidence로 쓰지 않는다.

## Works

| Work | Format | Canon status | Path |
| --- | --- | --- | --- |
| QFUDS SAGA | series candidate | active prototype series work | [20_series/qfuds-saga/](20_series/qfuds-saga/) |
| Laur Observatory prototype | short prototype sequence | archived prototype | [../../90_archive/lineage-prototype/](../../90_archive/lineage-prototype/) |

## Workflow Boundary

이 scaffold는 새 외부 source, PDF, paper, MCP output, cached asset, extraction
product, source/product availability claim을 만들지 않는다.

Current research asset workflow state:

```text
not searched
```

Extraction potential:

```text
not_extractable
```

## Next Gate

다음 작업은 canonical `20_series/qfuds-saga/` 아래의 normalized work shelves에서
Arc Two 또는 first-arc polish task를 시작하는 것이다.
