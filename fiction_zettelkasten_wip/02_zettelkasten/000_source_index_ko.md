---
doc_id: qfuds_fiction_source_index_ko
title: QFUDS Fiction Source Index
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - wiki_fiction_index
next_gate: distill source-index cards into permanent zettels without deleting source documents
last_updated: 2026-07-07
---

# QFUDS Fiction Source Index

```text
fiction/provenance only
research evidence: no
layer: source index (not a Zettelkasten; reserve "zettel" for hand-authored atomic notes)
canon action: migration operating layer
```

## 목적

이 선반은 소스 문서(`docs/wiki/fiction`)를 heading 단위로 색인한
**소스 인덱스**다. 제텔카스텐이 아니다 — 카드는 원자적 아이디어가 아니라 heading별 발췌·역링크다.
원문 문서는 삭제하지 않고 source layer로 보존하며, 작가가 카드를 하나씩 permanent zettel로
증류한다. 이미 원자적인 zettel(템플릿 준수)은 색인 대상에서 제외한다.

## 현재 생성 상태

| 항목 | 수 |
| --- | ---: |
| source markdown files | 209 |
| H1-H6 index cards | 2536 |
| source maps | 209 |

## 선반

| 경로 | 역할 |
| --- | --- |
| [90_source_queue/000_queue_index_ko.md](90_source_queue/000_queue_index_ko.md) | 전체 source map 진입점 |
| `90_source_queue/sources/` | 원문 파일별 heading 색인 |
| `90_source_queue/cards/` | heading 단위 색인 카드 |

## 처리 원칙

- 색인 카드는 permanent zettel이 아니다. "zettel" 명칭은 수기 원자 노트에만 쓴다.
- 원문을 대체하거나 삭제하지 않는다.
- canon/candidate/unknown은 처리자가 출처를 다시 확인한 뒤 표시한다.
- archive 문서도 provenance로 색인한다. active canon처럼 승격하지 않는다.
- boilerplate heading은 `source-only`로 표시하고 새 설정을 만들지 않는다.
