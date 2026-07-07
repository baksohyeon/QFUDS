---
doc_id: srcidx_25ad9807ce76c777
title: "Source Index - 4. Dependency & Impact Graph (수정 시 영향)"
doc_type: reference
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_verse_worldbuilding_architecture_ko
next_gate: distill this source-index card into an atomic permanent zettel, or mark it source-only
last_updated: 2026-07-06
---

# Source Index - 4. Dependency & Impact Graph (수정 시 영향)

```text
fiction/provenance only
research evidence: no
canon action: none
layer: source index (not a permanent zettel)
processing_state: queued
```

## Source

- Source document: [QFUDS Verse 월드빌딩 아키텍처 지도 (문서 인덱스·권위 트리·의존/영향 그래프)](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/00_continuity/900_worldbuilding_architecture_ko.md)
- Source path: [docs/wiki/fiction/10_universes/qfuds-verse/00_continuity/900_worldbuilding_architecture_ko.md](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/00_continuity/900_worldbuilding_architecture_ko.md)
- Source line: [line 253](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/00_continuity/900_worldbuilding_architecture_ko.md)
- Heading level: `H2`
- Source heading: `4. Dependency & Impact Graph (수정 시 영향)`

## Parent Context

- H1: QFUDS Verse 월드빌딩 아키텍처 지도 (문서 인덱스·권위 트리·의존/영향 그래프)

## Captured Source

> 핵심 캐논 척추의 의존 관계(화살표 = "A는 B를 근거로 선다", 즉 B를 고치면 A가 흔들린다).
> 가독성을 위해 상위 허브와 그 직접 연결만 도식한다.
>
> ```mermaid
> graph TD
>   N114[114 원본없음 물리]
>   N113[113 복원=사본]
>   N107[107 Last Archive]
>   N115[115 Q-Day 여파]
>   N116[116 14도메인]
>   N102[102 세력]
>   N109[109 명칭]
>   N001[001 딥타임]
>   N105[105 암호죽음]
>   N108[108 암호개념]
>   N110[110 비트코인]
>   N106[106 독자접근]
>   N112[112 인간확인루프]
>   N209[209 캐릭터지도]
>   N123[123 이기론]
>   Q109[310 질문 스파인]
>   Q205[311 origin]
>
>   N107 --> N115
>   N114 --> N115
>   N108 --> N115
>   N001 --> N115
>   N115 --> N116
>   N115 --> N123
>   N102 --> N123
>   N114 --> N123
>   N107 --> N112
>   N107 --> N110
>   N107 --> N108
>   N105 --> N108
>   N103A[103 Genesis] --> N105
>   N106 --> N107
>   N107 --> N113
>   N112 --> N113
>   N001 --> N102
>
> _(excerpt truncated — open the source for the full text)_

## Processing Contract

This is a generated source-index card, not a permanent zettel.

To distill it:

1. Reopen the source document for the full context.
2. Extract one atomic claim, rule, tension, or open question.
3. Mark canon state explicitly as `canon`, `candidate`, `soft_canon`, `archive`, or `unknown`.
4. Link the distilled zettel back to this card and to related zettels.
5. If the source heading is only navigation or boilerplate, mark it `source-only` instead of inventing a note.
