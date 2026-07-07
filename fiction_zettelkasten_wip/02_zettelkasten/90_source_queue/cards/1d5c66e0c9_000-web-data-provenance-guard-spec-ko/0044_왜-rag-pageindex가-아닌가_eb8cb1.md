---
doc_id: srcidx_eb8cb1d67454dc40
title: "Source Index - 왜 RAG / PageIndex가 아닌가"
doc_type: reference
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_verse_web_data_provenance_guard_spec_ko
next_gate: distill this source-index card into an atomic permanent zettel, or mark it source-only
last_updated: 2026-07-06
---

# Source Index - 왜 RAG / PageIndex가 아닌가

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
- Source line: [line 44](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/web/000_web_data_provenance_guard_spec_ko.md)
- Heading level: `H2`
- Source heading: `왜 RAG / PageIndex가 아닌가`

## Parent Context

- H1: 웹 데이터 provenance 가드 — 설계 스펙 (2026-07-06)

## Captured Source

> 이 문제는 **검색(retrieval)이 아니라 참조 무결성(referential integrity)**이다.
> `world 113`이 실재 파일을 가리키는가 — 유사도가 아니라 **정확 일치(equality)**
> 질문이다.
>
> | 필요 속성 | 결정적 가드 | RAG / PageIndex |
> | --- | --- | --- |
> | 결정적(같은 입력→같은 결과) | 예 | 아니오 (LLM 추론) |
> | 오프라인·무료·CI 게이트 | 예 | 아니오 (API 키·호출) |
> | 환각 없음 | 예 (파일 존재는 사실) | 아니오 |
> | 의존성 | Python stdlib | LLM + LiteLLM |
>
> RAG를 이 린터에 쓰면 모든 축에서 더 나쁘다.
>
> **PageIndex의 실제 자리는 이 레포에 이미 있다** —
> [Research Asset Digitization Workflow](../../../../../../.agent/workflows/research-asset-digitization-workflow.md)가
> 외부 연구 논문 PDF를 마크다운(구조+전문)으로 변환하는 MCP로 쓴다. 우리 데이터
> 파일의 stale 참조와는 무관하다.
>
> **RAG의 별건 자리(범위 밖):** 커져가는 lore+world 코퍼스에 대한 의미 Q&A(에이전트/
> 웹앱이 캐논을 문서 추론으로 답하거나, bespoke 데이터 집필 시 원문 구절 검색). 필요
> 하면 별도 스펙으로 다룬다. 이 스펙은 그것을 하지 않는다.

## Processing Contract

This is a generated source-index card, not a permanent zettel.

To distill it:

1. Reopen the source document for the full context.
2. Extract one atomic claim, rule, tension, or open question.
3. Mark canon state explicitly as `canon`, `candidate`, `soft_canon`, `archive`, or `unknown`.
4. Link the distilled zettel back to this card and to related zettels.
5. If the source heading is only navigation or boilerplate, mark it `source-only` instead of inventing a note.
