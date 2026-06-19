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
next_gate: create qfuds-saga work README after user confirmation
last_updated: 2026-06-19
---

# QFUDS Verse

`qfuds-verse`는 QFUDS에서 파생된 fiction universe/IP 컨테이너다.

이번 scaffold는 상위 세계관 선반만 만든다. 기존
`docs/wiki/fiction/qfuds-saga/`는 이동하지 않는다.

## Classification

- Universe/IP id: `qfuds-verse`
- Parent continuity: `none`
- Status: `active prototype`
- Authoring baseline date: `2026-06-19`
- Time baseline notes: 실제 작성 시점은 2026-06-19다. 작중 연표는 아직
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
- Institutions: [10_world/](10_world/)에서 관리한다.
- Factions: 아직 `qfuds-saga` prototype 문서에서만 개발 중이다.
- Technology limits: 기술어는 보존한다. `hash`, `KDF`, `key`, `salt`,
  `collision`, `entropy`, `Hawking radiation`, `AGI`, `QFUDS`는 근거 없이
  별칭으로 바꾸지 않는다.
- Terms and symbols: Bitcoin, Genesis Chain, Last Archive, Continuity Court,
  Cryptographic Death는 canon candidate다.
- Forbidden claims: fiction premise를 QFUDS 연구 evidence로 쓰지 않는다.

## Works

| Work | Format | Canon status | Path |
| --- | --- | --- | --- |
| QFUDS SAGA | series candidate | active prototype, not migrated | [../../qfuds-saga/](../../qfuds-saga/) |
| Laur Observatory prototype | short prototype sequence | archived prototype | [../../archive/lineage-prototype/](../../archive/lineage-prototype/) |

## Workflow Boundary

이 scaffold는 새 외부 source, PDF, paper, MCP output, cached asset, extraction
product, source/product availability claim을 만들지 않는다.

Current workflow state:

```text
not_extractable
```

## Next Gate

다음 작업은 `qfuds-saga` work README 초안이다. 그 전까지 기존
`qfuds-saga/` 폴더는 현재 위치에 둔다.
