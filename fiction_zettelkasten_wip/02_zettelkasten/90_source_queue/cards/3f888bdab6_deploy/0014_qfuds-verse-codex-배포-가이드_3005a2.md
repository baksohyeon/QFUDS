---
doc_id: srcidx_3005a218f7ea7203
title: "Source Index - QFUDS Verse Codex 배포 가이드"
doc_type: reference
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_verse_codex_web_deploy_ko
next_gate: distill this source-index card into an atomic permanent zettel, or mark it source-only
last_updated: 2026-07-06
---

# Source Index - QFUDS Verse Codex 배포 가이드

```text
fiction/provenance only
research evidence: no
canon action: none
layer: source index (not a permanent zettel)
processing_state: queued
```

## Source

- Source document: [QFUDS Verse Codex 배포 가이드](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/web/DEPLOY.md)
- Source path: [docs/wiki/fiction/10_universes/qfuds-verse/web/DEPLOY.md](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/web/DEPLOY.md)
- Source line: [line 14](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/web/DEPLOY.md)
- Heading level: `H1`
- Source heading: `QFUDS Verse Codex 배포 가이드`

## Parent Context

- none

## Captured Source

> `docs/wiki/fiction/10_universes/qfuds-verse/web/` 의 자기완결 앱.
> 성좌(3D)·연대기·인물·체계·사전 + 시드 보관함 + 아카이브 질의.
>
> - **런타임**: 의존성 0개 Node 서버(`server.js`) — 정적 코덱스 서빙 + 선택적 `/api/query`(Gemini 프록시).
> - **오프라인**: three.js·IBM Plex 폰트 전부 로컬 벤더링. 인터넷 없이 동작(질의 기능만 키 필요).
> - **엔트리**: `index.html` (= "qfuds.html" 디자인의 실제 구현). 서버가 `/` 로 서빙.
>
> 로컬 실행:
>
> ```bash
> cd docs/wiki/fiction/10_universes/qfuds-verse/web
> node server.js            # http://localhost:5000

## Processing Contract

This is a generated source-index card, not a permanent zettel.

To distill it:

1. Reopen the source document for the full context.
2. Extract one atomic claim, rule, tension, or open question.
3. Mark canon state explicitly as `canon`, `candidate`, `soft_canon`, `archive`, or `unknown`.
4. Link the distilled zettel back to this card and to related zettels.
5. If the source heading is only navigation or boilerplate, mark it `source-only` instead of inventing a note.
