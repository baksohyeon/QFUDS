---
doc_id: qfuds_saga_index_ko
title: QFUDS SAGA
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - wiki_fiction_index
  - qfuds_fiction_saga_index_ko
  - qfuds_lineage_agentic_research_system_ko
next_gate: check 011 guide and production board before choosing the next active unit
last_updated: 2026-07-01
---

# QFUDS SAGA

## Start Here

이 README는 SAGA 작업 선반의 짧은 입구다. 실행 절차는
[Fiction Agentic Workflow Guide](../../../../00_studio/011_fiction_agentic_workflow_guide_ko.md)가,
오늘 작업은 [SAGA production board](00_workroom/009_saga_production_board_ko.md)가 정한다.

```text
작업 시작 순서:
011 운영 허브 -> SAGA production board -> 필요한 story_design/bible/draft만 열기
```

QFUDS SAGA는 `qfuds-verse` 안의 active long-form SAGA work다. fiction/provenance
only이며 QFUDS 연구 증거, roadmap status, Level 2B claim이 아니다.

## Current Work

| 목적 | 열 문서 |
| --- | --- |
| **"이게 무슨 이야기냐"가 안 잡힐 때 (가장 쉬운 한 장)** | [023 세계관·인물 한눈에](10_story_design/023_first_arc_reader_orientation_world_and_cast_ko.md) |
| 오늘 active unit 확인 | [SAGA production board](00_workroom/009_saga_production_board_ko.md) |
| 전체 arc 구조 확인 | [011 saga arc map](10_story_design/011_saga_arc_map_multiarc_ko.md) |
| 극적 질문 spine 확인 | [015 five core dramatic questions](10_story_design/015_five_core_dramatic_questions_spine_ko.md) |
| 1.5부 사엘 origin 구조 확인 | [016 origin outline](10_story_design/016_first_arc_origin_outline_ko.md), [017 origin scene cards](10_story_design/017_first_arc_origin_scene_cards_ko.md) |
| 암호 개념 독자 온보딩 확인 | [018 crypto onboarding check](10_story_design/018_crypto_concepts_reader_onboarding_check_ko.md) |
| 사엘 실행 시트 확인 | [019 Sael execution sheet](10_story_design/019_sael_origin_execution_sheet_ko.md) |

작업 상태가 서로 다르면 production board와 최신 story_design을 먼저 본다. draft README와
arc 번호 cascade는 별도 승인 전까지 고치지 않는다.

## Canon

| Shelf | 역할 |
| --- | --- |
| [00_bible](00_bible/) | 작품 설정 기준서. 세계 사실, 인물, 제도, 과학 경계 |
| [00_bible/000 canon authority map](../../00_continuity/000_canon_authority_and_ssot_map_ko.md) | bible/story_design/draft 사이의 authority 확인 |
| [00_bible/024 character map and timeline coordinates](00_bible/024_character_map_and_timeline_coordinates_ko.md) | 시대좌표. 인물 지도와 딥타임 구조 (캐논 진입점) |
| [00_bible/025 near-future recenter](../../10_world/025_in_world_physics_information_unitarity_restoration_ko.md) | 근미래 리센터. 인월드 물리 복원 기준 (캐논 진입점) |
| [00_bible/026 Q-Day aftermath](../../10_world/026_qday_aftermath_timeline_and_world_ko.md) | Q-Day 여파. 여파 타임라인과 세계 (캐논 진입점) |
| [00_bible/027 AI history throughline](00_bible/027_machine_childhood_ai_history_narrator_throughline_ko.md) | AI발전사 관통선. 기계 화자 throughline (캐논 진입점) |
| [00_workroom](00_workroom/) | SAGA-local 운영 규칙, GSD brief, production board, traceability |
| [10_story_design](10_story_design/) | outline, arc map, reveal plan, scene cards |

새 아이디어는 바로 canon이 아니다.

```text
brainstorm -> 10_story_design
stable world fact -> 00_bible
prose scene -> 20_drafts
release-facing revision -> 30_revisions
release candidate -> 40_release
```

## Draft

| Shelf | 역할 |
| --- | --- |
| [20_drafts](20_drafts/README.md) | active prose drafts, Korean-primary manuscripts, counterparts, prototypes |
| 0부 캐스 (씨앗) | 0부 캐스 origin (036, 씨앗) |
| 1부 오르페우스 (오웬) | 1부 오르페우스 origin (035, 오웬) |
| 1.5부 사엘 (제도) | 1.5부 사엘 origin (033, 제도). 현행 사엘 자산은 033 (030은 폐기 프로토타입) |
| [20_drafts/2부](20_drafts/2부/README.md) | 2부 마라 (034, 신) |
| [30_revisions](30_revisions/README.md) | release-facing revision plans and audits |
| [40_release](40_release/README.md) | release manifest/export shelf. active release는 gate 통과 후 생성 |

원고는 `20_drafts/`에서만 직접 고친다. release shelf의 export는 source가 아니다.

## Quality Harness

| 필요 | 문서 |
| --- | --- |
| 한국어 문장 자연스러움, AI 말투 제거 | [009 Korean prose naturalness harness](../../../../00_studio/009_korean_fiction_prose_naturalness_harness_ko.md) |
| 기술·제도·역사 개념 독자 온보딩 | [010 reader onboarding harness](../../../../00_studio/010_reader_onboarding_harness_ko.md) |
| 장편 생산 게이트 | [005 series production harness](00_workroom/005_series_production_harness_ko.md) |
| chapter/scene intent 작성 | [010 chapter intent card template](00_workroom/010_chapter_intent_card_template_ko.md) |

## Boundary

이 index는 SAGA 창작 트랙의 shelf와 start path만 정한다. 새 외부 paper, web reference,
PDF, MCP 실행 결과, cached asset, extraction product, source/product availability claim을
만들지 않는다.

외부 자료를 새로 쓰는 문서는
[Research Asset and Product Workflow](../../../../../../../.agent/workflows/research-asset-product-workflow.md)를
별도로 적용하고 workflow state token을 자기 문서 안에 기록해야 한다.

Current research asset workflow state:

```text
not searched
```

Extraction potential:

```text
not_extractable
```

## Archive

Superseded or prototype SAGA material belongs under
[fiction archive](../../../../90_archive/README.md). Archive README와 legacy prototype은 provenance로
보존하며 active 작업처럼 읽지 않는다.
