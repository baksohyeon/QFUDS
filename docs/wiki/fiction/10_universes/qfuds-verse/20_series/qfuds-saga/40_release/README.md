---
doc_id: qfuds_saga_release_index_ko
title: QFUDS SAGA Release Shelf
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_index_ko
next_gate: create 001 active release manifest only after first-arc reboot prose passes scene-card and continuity gates
last_updated: 2026-06-21
---

# QFUDS SAGA Release Shelf

이 폴더는 독자에게 보여 줄 수 있는 release manifest와 export-ready 산출물만 둔다.
현재 active release는 없다.

다음 1부 정본은 [012 통합 아웃라인](../10_story_design/012_first_arc_book1_outline_reboot_ko.md)과
[013 scene cards](../10_story_design/013_first_arc_scene_cards_ko.md)를 통과한 뒤
`20_drafts/`에서 백지 원고로 다시 쓴다. 그 전까지 release build를 만들지 않는다.

현재 보존 문서:

- [900 Pre-Reboot 1부 Release Manifest](900_pre_reboot_first_arc_release_manifest_ko.md)
  — outline-first reboot 전 release 후보였던 상태의 provenance manifest. 본문
  중복본은 SSOT 유지를 위해 두지 않는다.

## Prefix Policy

- `001_`-`099_`: active release manifest/export. 1부 reboot prose가 통과하기 전에는
  만들지 않는다.
- `900_`-`999_`: archived/provenance release metadata. 독자용 active release가 아니다.

## 소스 / 빌드 모델 (배치 규칙)

- **편집 정본(SSOT) = `20_drafts/`** — 모든 prose 수정은 여기서 한다.
- **release shelf = `40_release/`** — active release가 있을 때 manifest/export만 둔다.
- 본문 조립 원고를 수기로 유지하지 않는다. generated manuscript가 필요하면
  생성 절차와 source hash를 함께 기록한 뒤 release 산출물로 만든다.

새 산출물은 한국어 primary draft, 영어 독립 각색판, shared continuity check가
모두 끝난 뒤에만 이 폴더에 둔다.

## Boundary

이 폴더는 fiction/provenance 작업 전용이다. QFUDS research evidence,
roadmap status, physical-source claim을 만들지 않는다.

Current research asset workflow state:

```text
not searched
```

Extraction potential:

```text
not_extractable
```
