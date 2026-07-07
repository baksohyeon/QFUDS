---
doc_id: qfuds_fiction_zettelkasten_system_index_ko
title: QFUDS Fiction 제텔카스텐 시스템 인덱스
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - wiki_fiction_index
next_gate: process queue cards into permanent zettels without deleting source documents
last_updated: 2026-07-07
---

# QFUDS Fiction 제텔카스텐 시스템 인덱스

```text
fiction/provenance only
research evidence: no
canon action: migration operating layer
```

## 목적

이 선반은 `docs/wiki/fiction/` 전체를 제텔카스텐 방식으로 처리하기 위한 운영 층이다.
원문 문서는 삭제하지 않고 source layer로 보존한다. 모든 H1-H6 heading은 queue card로
분해되며, 작가나 에이전트가 하나씩 permanent zettel로 처리한다.

## 현재 생성 상태

| 항목 | 수 |
| --- | ---: |
| source markdown files | 228 |
| H1-H6 queue cards | 2666 |
| source maps | 228 |

## 선반

| 경로 | 역할 |
| --- | --- |
| [90_source_queue/000_queue_index_ko.md](90_source_queue/000_queue_index_ko.md) | 전체 source map 진입점 |
| `90_source_queue/sources/` | 원문 파일별 heading queue |
| `90_source_queue/cards/` | heading 단위 처리 대기 카드 |

## 처리 원칙

- queue card는 permanent zettel이 아니다.
- 원문을 대체하거나 삭제하지 않는다.
- canon/candidate/unknown은 처리자가 출처를 다시 확인한 뒤 표시한다.
- archive 문서도 provenance로 queue화한다. active canon처럼 승격하지 않는다.
- boilerplate heading은 `source-only`로 표시하고 새 설정을 만들지 않는다.
