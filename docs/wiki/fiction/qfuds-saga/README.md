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
  - qfuds_agentic_research_system_ko
next_gate: choose world direction after user confirmation
last_updated: 2026-06-19
---

# QFUDS SAGA

이 폴더는 QFUDS에서 파생된 별도 창작 트랙이다.

기존 [QFUDS Fiction Saga](../archive/lineage-prototype/README.md)는 초기
프로토타입과 기원 기록으로 보존한다. 이 폴더는 이후 SAGA를 쓰기 위한
출판사식 작업 선반이다.

핵심 원칙은 간단하다.

- `00_system/`: 작가실 운영 규칙, agent harness, MCP/workflow boundary.
- `10_bible/`: 정사 후보로 쓰는 세계관, 역사, 세력, naming, 과학 경계.
- `20_development/`: pitch, 방향 매트릭스, outline, visual package, 실험적 설계.
- `30_drafts/`: 실제 prose draft, revision, 번역 원고.
- `../archive/`: 더 이상 active가 아닌 prototype.

소설 본문은 `30_drafts/`에 둔다. 세계관 설정은 `10_bible/`에 둔다.
작업 방법과 검수 규칙은 `00_system/`에 둔다. 아직 canon이 아닌 기획안과
시각/구조 실험은 `20_development/`에 둔다.

## Routing Note

Codex와 Claude Code 기준의 운영 경로는
[Documentation Folder Routing Workflow](../../../../.agent/workflows/documentation-folder-routing-workflow.md)
가 정한다.

```text
active SAGA operating specs -> 00_system/
active SAGA canon/world bible -> 10_bible/
active SAGA pitches, outlines, visual packages -> 20_development/
active SAGA prose drafts with harness/provenance boundary -> 30_drafts/
raw prose-only drafts without harness boundary -> do not add as-is
superseded fiction prototypes -> ../archive/
```

즉 이 트랙은 "설정표 폴더"가 아니라 작은 출판사 편집실처럼 관리한다.
운영 규칙, canon bible, 개발 패키지, 원고는 서로 다른 shelf에 놓는다.

## Promotion Rule

새 아이디어는 바로 정사가 아니다.

```text
brainstorm -> 20_development draft/pitch
development item that becomes stable world fact -> 10_bible
scene written as prose -> 30_drafts
repeatable writing or review rule -> 00_system
superseded or prototype material -> ../archive
```

`30_drafts/`의 장면은 읽을 수 있는 원고지만 자동으로 canon은 아니다.
canon으로 승격하려면 `10_bible/`의 세계관/인물/제도 규칙에 반영되어야 한다.

## 먼저 읽을 것

1. [QFUDS SAGA 창작 시스템](00_system/001_agentic_saga_system_ko.md)
   - AI writers' room, MCP 후보, 사용자 승인 게이트, 연구/창작 경계.
2. [QFUDS SAGA 세계관 방향 선택 매트릭스](20_development/002_world_direction_matrix_ko.md)
   - Nested Cosmology, closed-world revelation, deep-time empire, tactical
     philosophy SF, it-from-bit mythos 후보 비교.
3. [QFUDS SAGA 장기 복원 문명사 타임라인](10_bible/003_deep_time_restoration_timeline_ko.md)
   - 완전 복원, 라스트 아카이브, 망각권, 알레테이아 베일, 라우어 관측소를
     시간순 역사로 정리한 SAGA bible 전 단계.
4. [QFUDS SAGA 세력 문화 권력 생태계 장부](10_bible/004_factions_cultures_power_ecology_ko.md)
   - 복원 문명의 세력, 공동체, 정치권력, 종교적 언어, 원장 자본주의,
     망각권, 잔상 유목민 생태계를 정리한 SAGA bible 전 단계.
5. [QFUDS SAGA 시점 주제 고유명사 규칙](10_bible/005_narrative_pov_theme_naming_ko.md)
   - 3인칭 제한 시점의 decision rationale, 중심 주제, 역사 차용 규칙,
     common/formal name 이중 구조와 종교/제국/수도원/유목 naming strata를
     고정하는 SAGA bible 전 단계.
6. [QFUDS SAGA Bitcoin Genesis Chain and Restoration Myth](10_bible/006_bitcoin_genesis_chain_and_restoration_myth_ko.md)
   - Bitcoin을 Genesis Chain artifact로 사용하고, `it from bit`, 현실 편집,
     암호학 붕괴, 블랙홀/화이트홀 복원, Mara Veyr 사건을 연결하는 SAGA
     canon 후보.
7. [QFUDS SAGA Mara Veyr Prologue Research Harness](00_system/007_mara_veyr_prologue_research_harness_ko.md)
   - Mara Veyr 프롤로그를 쓰기 전, 소설 craft, COVID 이후 digital afterlife,
     right to be forgotten, AI reality editing, Bitcoin artifact, science-audit
     경계를 묶는 writer harness.
8. [QFUDS SAGA Mara Veyr Prologue Draft](30_drafts/008_mara_veyr_prologue_draft_ko.md)
   - cryptographic death, Genesis Chain, Last Archive, The Broken Crown,
     Continuity Court, Mara Veyr 자기부정 복원체 사건을 실제 프롤로그 장면으로
     테스트한 초안.
9. [QFUDS SAGA Post-AGI Civilization History and Bilingual Protocol](10_bible/009_post_agi_civilization_history_bilingual_protocol_ko.md)
   - AI/AGI 이후 문명사, Marxian general intellect lens, cryptographic death,
     `It from bit(s)`/Bitcoin joke layer, 영어 원문 우선 작성 프로토콜.
10. [QFUDS SAGA Mara Veyr Prologue English Revision](30_drafts/010_mara_veyr_prologue_english_revision_ko.md)
    - 008 초안을 보존한 상태에서 영어 원문 우선으로 다시 쓴 tone revision.
      quiet catastrophe, Continuity Court, Genesis Chain, Last Archive의
      question-correction 기능을 실제 장면으로 테스트한다.
11. [QFUDS SAGA Visual Exhibit Design](20_development/011_visual_exhibit_design_ko.md)
    - 기존 rough-tanh PNG/SVG asset을 court exhibit, archive plate, visual
      metaphor로 쓰는 후보와 caption 규칙. fiction/provenance only.
12. [QFUDS SAGA World Anchor and Verisimilitude](10_bible/012_world_anchor_and_verisimilitude_ko.md)
    - SAGA가 현대 2023-2026 AI 현실감 붕괴를 고대사로 삼는 우리 우주의 먼
      미래라는 점, 그리고 기적을 제도/계급/절차로 바꾸는 핍진성 규칙.

## 역할

이 트랙의 목표는 QFUDS를 증명하는 것이 아니다.

목표는 다음 세 가지다.

- 재미있는 장편 SF SAGA를 만들기.
- 사용자가 거쳐 온 QFUDS 탐색, 실패, 회고, audit harness 경험을 이야기의
  구조로 보존하기.
- 과학적 정합성 경계를 유지하면서도 "증명되지는 않았지만 어떤 층위에서는
  정답인 세계"라는 fiction premise를 활용하기.

## 금지

- fiction premise를 물리 evidence로 쓰지 않는다.
- QFUDS support, validation, Level 2B admission 언어를 쓰지 않는다.
- 기존 연구 문서를 소설 설정에 맞추어 재해석하지 않는다.
- 외부 자료를 쓰면서 workflow state 없이 source/product claim을 쓰지 않는다.
