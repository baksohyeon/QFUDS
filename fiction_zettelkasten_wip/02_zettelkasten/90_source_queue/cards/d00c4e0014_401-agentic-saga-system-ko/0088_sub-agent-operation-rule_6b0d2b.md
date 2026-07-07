---
doc_id: srcidx_6b0d2b54bf52d614
title: "Source Index - Sub-Agent Operation Rule"
doc_type: reference
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_agentic_system_ko
next_gate: distill this source-index card into an atomic permanent zettel, or mark it source-only
last_updated: 2026-07-07
---

# Source Index - Sub-Agent Operation Rule

```text
fiction/provenance only
research evidence: no
canon action: none
layer: source index (not a permanent zettel)
processing_state: queued
```

## Source

- Source document: [QFUDS SAGA 창작 시스템](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/401_agentic_saga_system_ko.md)
- Source path: [docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/401_agentic_saga_system_ko.md](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/401_agentic_saga_system_ko.md)
- Source line: [line 88](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/401_agentic_saga_system_ko.md)
- Heading level: `H2`
- Source heading: `Sub-Agent Operation Rule`

## Parent Context

- H1: QFUDS SAGA 창작 시스템

## Captured Source

> 위 agent들은 먼저 **역할 분리 규칙**이다. 실제 Codex/Claude Code 세션에서
> sub-agent 도구가 제공될 때만 병렬 실행한다.
>
> 운영 규칙:
>
> ```text
> 1. 사용자가 sub-agent/병렬 작업을 명시적으로 허용한다.
> 2. 각 sub-agent에 겹치지 않는 질문이나 파일 범위를 준다.
> 3. read-only scout와 writer를 분리한다.
> 4. writer는 단일 main agent가 통합한다.
> 5. fiction premise를 research evidence로 승격하지 않는다.
> 6. 결과는 staged guard와 pre-commit으로 검증한다.
> ```
>
> 현재 권장 분리:
>
> | Sub-agent | Use when | Output |
> | --- | --- | --- |
> | `science_auditor` scout | 과학/출처/증거 경계가 흐려질 때 | forbidden-claim list, workflow-state check |
> | `visual_exhibit` scout | 기존 asset을 fiction exhibit로 쓸 때 | asset 후보, caption risk, provenance note |
> | `style_editor` scout | 대사가 많고 장면성이 약할 때 | sensory/metaphor pass memo |
> | `showrunner` scout | 장면이 장기 arc와 어긋날 때 | arc-fit note, reveal-order risk |
>
> sub-agent가 없으면 위 표는 main agent의 체크리스트로 사용한다. sub-agent가 있어도
> 최종 문서 수정, stage, commit은 main agent가 책임진다.

## Processing Contract

This is a generated source-index card, not a permanent zettel.

To distill it:

1. Reopen the source document for the full context.
2. Extract one atomic claim, rule, tension, or open question.
3. Mark canon state explicitly as `canon`, `candidate`, `soft_canon`, `archive`, or `unknown`.
4. Link the distilled zettel back to this card and to related zettels.
5. If the source heading is only navigation or boilerplate, mark it `source-only` instead of inventing a note.
