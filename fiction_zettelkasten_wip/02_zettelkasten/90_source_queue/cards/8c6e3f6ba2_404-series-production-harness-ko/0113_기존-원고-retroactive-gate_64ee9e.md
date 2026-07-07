---
doc_id: srcidx_64ee9eda6eaa25d9
title: "Source Index - 기존 원고 retroactive gate"
doc_type: reference
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_series_production_harness_ko
next_gate: distill this source-index card into an atomic permanent zettel, or mark it source-only
last_updated: 2026-07-06
---

# Source Index - 기존 원고 retroactive gate

```text
fiction/provenance only
research evidence: no
canon action: none
layer: source index (not a permanent zettel)
processing_state: queued
```

## Source

- Source document: [QFUDS SAGA 시리즈 제작 하네스](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/404_series_production_harness_ko.md)
- Source path: [docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/404_series_production_harness_ko.md](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/404_series_production_harness_ko.md)
- Source line: [line 113](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/404_series_production_harness_ko.md)
- Heading level: `H2`
- Source heading: `기존 원고 retroactive gate`

## Parent Context

- H1: QFUDS SAGA 시리즈 제작 하네스

## Captured Source

> 이 게이트가 생기기 전에 작성된 원고도 예외가 아니다. 이미 개요가 잡힌 1편이라도
> release 후보로 유지하려면 아래를 역적용한다.
>
> 1. draft의 `Harness Applied` 아래에 `Series Gate Applied` 표를 넣는다.
> 2. 반복 인물은 [205 앙상블 바이블](../00_bible/205_character_ensemble_voices_relationships_ko.md)
>    또는 개별 시트로 Want/Need/Fear/Wound/Lie/관계기능이 확인돼야 한다.
> 3. 1편이 단독 완결이 아니라 다음 편으로 넘어갈 연재 스레드를 실제 본문에 남겨야 한다.
> 4. draft를 고쳐도 release 본문 중복 build를 수기로 유지하지 않는다. active release가
>    필요할 때만 [Release Shelf](../40_release/README.md)에 manifest/export를 새로 만든다.
> 5. [002 release gate](../30_revisions/002_first_arc_release_immersion_revision_plan_ko.md)에
>    편별 적용 결과를 남긴다.
>
> 기계 집행: `scripts/fiction_gate.py --staged`는 `20_drafts/019` 이후 한국어
> primary/adaptation draft를 staged 상태로 올릴 때 `## Series Gate Applied` 표가 없으면
> pre-commit을 실패시킨다. 즉 다음 편을 고치려면 먼저 이 게이트를 통과시켜야 한다.

## Processing Contract

This is a generated source-index card, not a permanent zettel.

To distill it:

1. Reopen the source document for the full context.
2. Extract one atomic claim, rule, tension, or open question.
3. Mark canon state explicitly as `canon`, `candidate`, `soft_canon`, `archive`, or `unknown`.
4. Link the distilled zettel back to this card and to related zettels.
5. If the source heading is only navigation or boilerplate, mark it `source-only` instead of inventing a note.
