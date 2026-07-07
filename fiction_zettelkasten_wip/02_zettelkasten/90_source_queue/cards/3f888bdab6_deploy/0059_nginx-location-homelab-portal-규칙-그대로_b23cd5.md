---
doc_id: srcidx_b23cd5ee28ae23e0
title: "Source Index - nginx location (homelab-portal 규칙 그대로)"
doc_type: reference
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_verse_codex_web_deploy_ko
next_gate: distill this source-index card into an atomic permanent zettel, or mark it source-only
last_updated: 2026-07-06
---

# Source Index - nginx location (homelab-portal 규칙 그대로)

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
- Source line: [line 59](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/web/DEPLOY.md)
- Heading level: `H3`
- Source heading: `nginx location (homelab-portal 규칙 그대로)`

## Parent Context

- H1: 4) 컨테이너 포트(5000)를 호스트 포트로 매핑

## Captured Source

> `/etc/nginx/conf.d/00-default-vhost.conf`:
>
> ```nginx
> location = /qfuds-fiction { return 301 /qfuds-fiction/; }
> location /qfuds-fiction/ {
>   proxy_pass http://127.0.0.1:<PORT>/;   # 끝 슬래시가 /qfuds-fiction/ 프리픽스를 벗겨줌
>   proxy_set_header Host $host;
> }
> ```
>
> ```bash
> sudo nginx -t && sudo systemctl reload nginx
> ```
>
> > 앱은 **모든 자산 경로가 상대경로**(`./app.js`, `./api/query` …)라, `/qfuds-fiction/`
> > 서브패스 밑에서 그대로 동작합니다. 절대경로(`/app.js`)는 쓰지 않습니다.

## Processing Contract

This is a generated source-index card, not a permanent zettel.

To distill it:

1. Reopen the source document for the full context.
2. Extract one atomic claim, rule, tension, or open question.
3. Mark canon state explicitly as `canon`, `candidate`, `soft_canon`, `archive`, or `unknown`.
4. Link the distilled zettel back to this card and to related zettels.
5. If the source heading is only navigation or boilerplate, mark it `source-only` instead of inventing a note.
