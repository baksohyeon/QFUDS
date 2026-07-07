---
doc_id: srcidx_7ab44ace0bdc56e5
title: "Source Index - docker"
doc_type: reference
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_verse_codex_web_deploy_ko
next_gate: distill this source-index card into an atomic permanent zettel, or mark it source-only
last_updated: 2026-07-07
---

# Source Index - docker

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
- Source line: [line 92](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/web/DEPLOY.md)
- Heading level: `H1`
- Source heading: `docker`

## Parent Context

- none

## Captured Source

> docker build -t qfuds-codex . && docker run -p 8080:5000 -e GEMINI_API_KEY=xxx qfuds-codex

## Processing Contract

This is a generated source-index card, not a permanent zettel.

To distill it:

1. Reopen the source document for the full context.
2. Extract one atomic claim, rule, tension, or open question.
3. Mark canon state explicitly as `canon`, `candidate`, `soft_canon`, `archive`, or `unknown`.
4. Link the distilled zettel back to this card and to related zettels.
5. If the source heading is only navigation or boilerplate, mark it `source-only` instead of inventing a note.
