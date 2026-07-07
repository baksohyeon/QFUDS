---
doc_id: srcidx_f25e4b374fd8c3c7
title: "Source Index - 4. fiction-forge"
doc_type: reference
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_external_ai_writing_systems_gap_audit_ko
next_gate: distill this source-index card into an atomic permanent zettel, or mark it source-only
last_updated: 2026-07-07
---

# Source Index - 4. fiction-forge

```text
fiction/provenance only
research evidence: no
canon action: none
layer: source index (not a permanent zettel)
processing_state: queued
```

## Source

- Source document: [QFUDS SAGA 외부 AI 글쓰기 시스템 갭 감사](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/407_external_ai_writing_systems_gap_audit_ko.md)
- Source path: [docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/407_external_ai_writing_systems_gap_audit_ko.md](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/407_external_ai_writing_systems_gap_audit_ko.md)
- Source line: [line 151](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/407_external_ai_writing_systems_gap_audit_ko.md)
- Heading level: `H3`
- Source heading: `4. fiction-forge`

## Parent Context

- H1: QFUDS SAGA 외부 AI 글쓰기 시스템 갭 감사
- H2: 외부 시스템별 패턴 감사

## Captured Source

> 이 레포는 AI-assisted novel editing toolkit으로 prose scanner, MCP context server,
> publisher, editorial workflow를 묶는다. README상 특히 중요한 것은 스캔 -> 비중 있는
> 문제 장 식별 -> 비중첩 파일 병렬 수정 -> 재스캔 -> 순차 보이스 polish 흐름이다.
>
> QFUDS 대응:
>
> | 외부 패턴 | QFUDS 현재 대응 | 부족한 것 | 결정 |
> | --- | --- | --- | --- |
> | prose scanner | `fiction_gate.py`, craft audit | severity tier와 cluster report | 채택 |
> | MCP context server | repo 파일 직접 읽기 | 별도 서버는 불필요 | 설치 보류 |
> | fix in waves | 없음 | 겹치지 않는 파일 묶음 수정 규칙 | 채택 |
> | re-scan | pre-commit + manual review | 수정 후 재검증 체크리스트 | 채택 |
> | publisher | `40_release/` | 지금은 불필요 | 보류 |
>
> 채택 요약:
>
> ```text
> MCP 서버 설치보다 "scan -> fix wave -> re-scan -> polish" 루프를 문서화하는 편이 안전하다.
> ```

## Processing Contract

This is a generated source-index card, not a permanent zettel.

To distill it:

1. Reopen the source document for the full context.
2. Extract one atomic claim, rule, tension, or open question.
3. Mark canon state explicitly as `canon`, `candidate`, `soft_canon`, `archive`, or `unknown`.
4. Link the distilled zettel back to this card and to related zettels.
5. If the source heading is only navigation or boilerplate, mark it `source-only` instead of inventing a note.
