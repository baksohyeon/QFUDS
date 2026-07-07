---
doc_id: srcidx_cd0b1b10dad8f869
title: "Source Index - story-skills 채택 (2026-06-30, adoption 규칙 해제 후)"
doc_type: reference
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_external_ai_writing_systems_gap_audit_ko
next_gate: distill this source-index card into an atomic permanent zettel, or mark it source-only
last_updated: 2026-07-06
---

# Source Index - story-skills 채택 (2026-06-30, adoption 규칙 해제 후)

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
- Source line: [line 355](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/407_external_ai_writing_systems_gap_audit_ko.md)
- Heading level: `H2`
- Source heading: `story-skills 채택 (2026-06-30, adoption 규칙 해제 후)`

## Parent Context

- H1: QFUDS SAGA 외부 AI 글쓰기 시스템 갭 감사

## Captured Source

> 위 "보류" 판단은 inspiration-only 시절 결론이다. 2026-06-30 외부 도구 adoption 규칙이
> 픽션 한정 해제되어(IP 워크플로우 External Tool and Code Adoption), 비교 평가 후
> **story-skills를 결정론적 연속성 엔진 용도로 채택**한다.
>
> 비교 결과(후보 4종, 전부 MIT): story-skills / howells-fiction / Claude-Book / Crucible.
> 선정 사유 — Claude Code 플러그인 + 마크다운/YAML 철학 일치 + **결정론적 continuity CLI**
> (deaths·promises·questions·casts·durable state) + 의존성 0. Claude-Book은 GPU·로컬 LLM
> 인프라 과중, Crucible은 데스크톱 앱이라 탈락.
>
> 채택 기록(adoption 규칙 필수 항목):
>
> | 항목 | 값 |
> | --- | --- |
> | source | https://github.com/danjdewhurst/story-skills |
> | license | MIT |
> | 고정 commit | `c482d48f4eb9b488f120a77a51f9fae55cc0d75f` |
> | 도입 방식 | git submodule `tools/story-skills/` (프로젝트 동행, 업데이트 가능) |
> | allowed claim | 픽션 연속성 QA 도구로 사용; CLI를 원고에 실행 |
> | blocked claim | QFUDS 연구 증거·이론·결과에 반입 금지; 픽션 전제를 연구 주장화 금지 |
> | workflow state | `asset_cached` (submodule로 고정) |
> | boundary | fiction/provenance only |
>
> 사용법(원고 연속성 QA):
>
> ```bash
> node tools/story-skills/bin/story.js import <draft.md> --title <T> --dir /tmp/<T>
> node tools/story-skills/bin/story.js continuity /tmp/<T>
> node tools/story-skills/bin/story.js report /tmp/<T>
> ```
>
> 한계(정직): `import`는 챕터 heading 규칙이 달라 긴 원고를 일부만 분할하고, 엔진의
> 완전한 값을 내려면 인물(death/status)·promise·question·scene cast를 채워야 한다. 즉
> "import하면 즉시 검사 완료"가 아니라 **work별 1회 셋업 후 결정론적 검사가 공짜**가 된다.
>
> 역할 분담:
>
> - **story-skills CLI** = 범용 연속성(죽은 인물·복선 회수 순서·안 쏜 떡밥·장면 캐스트·상태).
> - **`scripts/fiction_continuity.py`** = QFUDS 전용 딥타임 시대(부) 정합 — story-skills가
>   모르는 1부(21c)↔2부(4기) 규칙 전담. 두 도구는 보완 관계로 둘 다 유지한다.
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
