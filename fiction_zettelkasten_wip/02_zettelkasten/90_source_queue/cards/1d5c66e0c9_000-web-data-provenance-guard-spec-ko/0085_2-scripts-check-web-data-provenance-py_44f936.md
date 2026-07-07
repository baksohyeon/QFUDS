---
doc_id: srcidx_44f936c007bbb566
title: "Source Index - 2. `scripts/check_web_data_provenance.py`"
doc_type: reference
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_verse_web_data_provenance_guard_spec_ko
next_gate: distill this source-index card into an atomic permanent zettel, or mark it source-only
last_updated: 2026-07-07
---

# Source Index - 2. `scripts/check_web_data_provenance.py`

```text
fiction/provenance only
research evidence: no
canon action: none
layer: source index (not a permanent zettel)
processing_state: queued
```

## Source

- Source document: [웹 데이터 provenance 가드 — 설계 스펙 (2026-07-06)](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/web/000_web_data_provenance_guard_spec_ko.md)
- Source path: [docs/wiki/fiction/10_universes/qfuds-verse/web/000_web_data_provenance_guard_spec_ko.md](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/web/000_web_data_provenance_guard_spec_ko.md)
- Source line: [line 85](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/web/000_web_data_provenance_guard_spec_ko.md)
- Heading level: `H3`
- Source heading: `2. `scripts/check_web_data_provenance.py``

## Parent Context

- H1: 웹 데이터 provenance 가드 — 설계 스펙 (2026-07-06)
- H2: 설계

## Captured Source

> Python stdlib만 사용(레포 관례: `agent_workflow_guard.py` 스타일).
>
> 동작:
>
> 1. **진실 맵 구성** — 실제 선반 디렉터리를 스캔해 `{shelf: {존재하는 번호}}`를
>    만든다. 선반은 두 루트에 걸친다:
>    - `qfuds-verse/00_continuity` (continuity)
>    - `qfuds-verse/10_world` (world)
>    - `qfuds-verse/20_series/qfuds-saga/00_bible` (bible)
>    - `qfuds-verse/20_series/qfuds-saga/10_story_design` (story)
>    - `qfuds-verse/20_series/qfuds-saga/00_workroom` (workroom)
>    - `draft`/`prototype`는 `20_drafts` 하위(원고·`_versions/` 프로토타입)에서
>      번호 집합을 모은다.
> 2. **참조 추출** — 두 데이터 파일에서 한정 토큰을 file:line과 함께 모은다.
> 3. **판정** — 해석되지 않는 토큰마다 오류를 쌓고, 있으면 exit 2 + 위반 토큰·
>    위치·해당 선반의 유효 번호 힌트를 출력. 없으면 exit 0.
>
> 관례상 인자 없이 전체 검사; `--staged`는 뒤 확장 여지로 남긴다(초기 구현엔 불필요).

## Processing Contract

This is a generated source-index card, not a permanent zettel.

To distill it:

1. Reopen the source document for the full context.
2. Extract one atomic claim, rule, tension, or open question.
3. Mark canon state explicitly as `canon`, `candidate`, `soft_canon`, `archive`, or `unknown`.
4. Link the distilled zettel back to this card and to related zettels.
5. If the source heading is only navigation or boilerplate, mark it `source-only` instead of inventing a note.
