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
장편 시리즈 제작용 작업 선반이다.

핵심 원칙은 간단하다.

- `00_system/`: 작가실 운영 규칙, agent harness, MCP/workflow boundary.
- `10_series_bible/`: 작품 설정 기준서. 세계관, 역사, 세력, naming, 과학 경계.
- `20_development/`: pitch, 방향 매트릭스, outline, visual package, 실험적 설계.
- `30_drafts/`: 실제 prose draft, revision, 번역 원고.
- `../archive/`: 더 이상 active가 아닌 prototype.

소설 본문은 `30_drafts/`에 둔다. 세계관 설정은 `10_series_bible/`에 둔다.
작업 방법과 검수 규칙은 `00_system/`에 둔다. 아직 canon이 아닌 기획안과
시각/구조 실험은 `20_development/`에 둔다.

## What Is `series_bible`?

`series bible`은 여기서 종교적 의미가 아니다. TV/장편 시리즈 제작에서 빌려온
작업 용어다. 이 repo에서는 더 직접적으로 **작품 설정 기준서**라고 읽는다.

역할은 다음과 같다.

- 여러 에이전트나 여러 세션이 같은 세계관을 쓰도록 기준을 잡는다.
- 인물, 세력, 기관, 사건 연표, 금기, 용어, 기술 수준, 과학 경계를 모은다.
- 이미 정사로 받아들인 설정과 아직 개발 중인 아이디어를 분리한다.
- 초안이 canon과 충돌할 때 어느 쪽을 고쳐야 하는지 판단하게 해준다.

하지 않는 일도 명확하다.

- 완성 원고가 아니다.
- episode outline이 아니다.
- 연구 증거가 아니다.
- QFUDS support, validation, Level 2B admission이 아니다.

즉 `10_series_bible/`은 "설정 모음"이라기보다 장기 연재를 위한 내부 기준서다.

## Routing Note

Codex와 Claude Code 기준의 운영 경로는
[Documentation Folder Routing Workflow](../../../../.agent/workflows/documentation-folder-routing-workflow.md)
가 정한다.

전체 fiction/IP 운영 규칙은
[Fiction IP Management Workflow](../../../../.agent/workflows/fiction-ip-management-workflow.md)
가 정한다. 이 SAGA 폴더는 장기적으로 `qfuds-verse` 같은 universe/IP 아래의
series work로 이동할 수 있다. 이동은 사용자 확인 후 별도 migration으로만 한다.

현재 active shelf와 migration gate는
[Fiction Catalog](../01_catalog/README.md)에서 관리한다.

## Workflow Boundary

이 index는 SAGA 창작 트랙의 선반과 read order를 정한다. 새 외부 paper, web
reference, PDF, MCP 실행 결과, cached asset, extraction product, source/product
availability claim을 만들지 않는다.

외부 자료를 새로 쓰는 문서는
[Research Asset and Product Workflow](../../../../.agent/workflows/research-asset-product-workflow.md)
를 별도로 적용하고 workflow state token을 자기 문서 안에 기록해야 한다.

현재 workflow state:

```text
not_extractable
```

```text
active SAGA operating specs -> 00_system/
active SAGA series bible / canon reference -> 10_series_bible/
active SAGA pitches, outlines, visual packages -> 20_development/
active SAGA prose drafts with harness/provenance boundary -> 30_drafts/
raw prose-only drafts without harness boundary -> do not add as-is
superseded fiction prototypes -> ../archive/
```

즉 이 트랙은 "설정표 폴더"가 아니라 작은 출판사 편집실처럼 관리한다.
운영 규칙, 작품 설정 기준서, 개발 패키지, 원고는 서로 다른 shelf에 놓는다.

## Promotion Rule

새 아이디어는 바로 정사가 아니다.

```text
brainstorm -> 20_development draft/pitch
development item that becomes stable world fact -> 10_series_bible
scene written as prose -> 30_drafts
repeatable writing or review rule -> 00_system
superseded or prototype material -> ../archive
```

`30_drafts/`의 장면은 읽을 수 있는 원고지만 자동으로 canon은 아니다.
canon으로 승격하려면 `10_series_bible/`의 세계관/인물/제도 규칙에 반영되어야 한다.

## 먼저 읽을 것

1. [QFUDS SAGA 창작 시스템](00_system/001_agentic_saga_system_ko.md)
   - AI writers' room, MCP 후보, 사용자 승인 게이트, 연구/창작 경계.
2. [QFUDS SAGA 세계관 방향 선택 매트릭스](20_development/001_world_direction_matrix_ko.md)
   - Nested Cosmology, closed-world revelation, deep-time empire, tactical
     philosophy SF, it-from-bit mythos 후보 비교.
3. [QFUDS SAGA World Anchor and Verisimilitude](10_series_bible/001_world_anchor_and_verisimilitude_ko.md)
   - SAGA가 현대 2023-2026 AI 현실감 붕괴를 고대사로 삼는 우리 우주의 먼
     미래라는 점, 그리고 기적을 제도/계급/절차로 바꾸는 핍진성 규칙.
4. [QFUDS SAGA 장기 복원 문명사 타임라인](10_series_bible/002_deep_time_restoration_timeline_ko.md)
   - 완전 복원, 라스트 아카이브, 망각권, 알레테이아 베일, 라우어 관측소를
     시간순 역사로 정리한 작품 설정 기준서 항목.
5. [QFUDS SAGA 세력 문화 권력 생태계 장부](10_series_bible/003_factions_cultures_power_ecology_ko.md)
   - 복원 문명의 세력, 공동체, 정치권력, 종교적 언어, 원장 자본주의,
     망각권, 잔상 유목민 생태계를 정리한 작품 설정 기준서 항목.
6. [QFUDS SAGA 시점 주제 고유명사 규칙](10_series_bible/004_narrative_pov_theme_naming_ko.md)
   - 3인칭 제한 시점의 decision rationale, 중심 주제, 역사 차용 규칙,
     common/formal name 이중 구조와 종교/제국/수도원/유목 naming strata를
     고정하는 작품 설정 기준서 항목.
7. [QFUDS SAGA Bitcoin Genesis Chain and Restoration Myth](10_series_bible/005_bitcoin_genesis_chain_and_restoration_myth_ko.md)
   - Bitcoin을 Genesis Chain artifact로 사용하고, `it from bit`, 현실 편집,
     암호학 붕괴, 블랙홀/화이트홀 복원, Mara Veyr 사건을 연결하는 SAGA
     canon 후보.
8. [QFUDS SAGA Post-AGI Civilization History and Bilingual Protocol](10_series_bible/006_post_agi_civilization_history_bilingual_protocol_ko.md)
   - AI/AGI 이후 문명사, Marxian general intellect lens, cryptographic death,
     `It from bit(s)`/Bitcoin joke layer, 영어 원문 우선 작성 프로토콜.
9. [QFUDS SAGA Cryptographic Death and Hash Covenant](10_series_bible/007_cryptographic_death_and_hash_covenant_ko.md)
   - 사용자 제공 hash/KDF/cryptographic-hash 개념 노트를 SAGA의 Cryptographic
     Death, Preimage Restoration, Genesis Chain, identity-flood attack,
     key/salt sovereignty 설정 기준서로 변환한 canon-candidate reference.
10. [QFUDS SAGA Mara Veyr Prologue Research Harness](00_system/002_mara_veyr_prologue_research_harness_ko.md)
   - Mara Veyr 프롤로그를 쓰기 전, 소설 craft, COVID 이후 digital afterlife,
     right to be forgotten, AI reality editing, Bitcoin artifact, science-audit
     경계를 묶는 writer harness.
11. [QFUDS SAGA Mara Veyr Prologue Draft](30_drafts/001_mara_veyr_prologue_draft_ko.md)
   - cryptographic death, Genesis Chain, Last Archive, The Broken Crown,
     Continuity Court, Mara Veyr 자기부정 복원체 사건을 실제 프롤로그 장면으로
     테스트한 초안.
12. [QFUDS SAGA Mara Veyr Prologue English Revision](30_drafts/002_mara_veyr_prologue_english_revision_ko.md)
    - 008 초안을 보존한 상태에서 영어 원문 우선으로 다시 쓴 tone revision.
      quiet catastrophe, Continuity Court, Genesis Chain, Last Archive의
      question-correction 기능을 실제 장면으로 테스트한다.
13. [QFUDS SAGA Visual Exhibit Design](20_development/002_visual_exhibit_design_ko.md)
    - 기존 rough-tanh PNG/SVG asset을 court exhibit, archive plate, visual
      metaphor로 쓰는 후보와 caption 규칙. fiction/provenance only.
14. [QFUDS SAGA Launch Package](20_development/003_saga_launch_package_ko.md)
    - SAGA를 첫 작품 기획으로 옮기는 launch package. 핵심 질문, first arc,
      주인공 후보, 첫 episode hook, 세력 기능, technical kill-switch,
      non-canon 항목을 정리한다.
15. [QFUDS SAGA Liora Sen First Episode Beat Sheet](20_development/004_liora_sen_first_episode_beat_sheet_ko.md)
    - `Exhibit S-0` working title의 first episode beat sheet. Liora 중심
      장면 순서, 인물 압력, reveal order, technical guard, 다음 draft 후보를
      정리한다.
16. [QFUDS SAGA Genesis Chain Artifact Scene Packet](20_development/005_genesis_chain_artifact_scene_packet_ko.md)
    - Bitcoin/Genesis Chain을 zero price, crown artifact, broken
      cryptography, black-hole restoration myth로 나누어 first arc 장면
      압력으로 바꾸는 development packet.
17. [QFUDS SAGA First Arc Six-Episode Outline](20_development/006_first_arc_six_episode_outline_ko.md)
    - `The Broken Crown` 첫 arc를 여섯 episode로 나누어 Mara Veyr, Genesis
      Chain, Cryptographic Death, Identity Flood, Hawking Court를 단계적으로
      배치한 development outline.
18. [QFUDS SAGA Exhibit S-0 Opening English Draft](30_drafts/003_exhibit_s0_opening_english_draft.md)
    - `The Broken Crown` 1화 opening candidate. Liora Sen이 Waiting City와
      Court of Continuance를 통과하며 Mara Veyr hearing으로 들어가는
      English-first prose draft.
19. [QFUDS SAGA Exhibit S-0 Hearing Continuation English Draft](30_drafts/004_exhibit_s0_hearing_continuation_english_draft.md)
    - 003 opening을 이어 Mara Veyr hearing, Broken Crown exhibit,
      continuity tests, `RECOVERABLE / NOT CLAIMABLE` category, Last Archive
      question correction까지 진행한 English-first continuation draft.
20. [QFUDS SAGA Exhibit S-0 Episode 1 Revised English Draft](30_drafts/005_exhibit_s0_episode1_revised_english_draft.md)
    - 003 opening과 004 hearing continuation을 보존한 상태에서 하나의
      Episode 1 rough cut으로 압축한 revision pass.
21. [QFUDS SAGA The Dead Exchange English Draft](30_drafts/006_the_dead_exchange_english_draft.md)
    - Episode 2 English-first draft. Genesis Chain을 죽은 시장이 아니라
      살아 있는 상속/권력 장치로 보여 주고, `ACCESS != AUTHORITY` mark를
      도입한다.
22. [QFUDS SAGA The Last Hodler English Draft](30_drafts/007_the_last_hodler_english_draft.md)
    - Episode 3 English-first draft. Bitcoin/Genesis Chain을 현재 시장 예측이
      아니라 미래 신화와 `civilization-scale consent artifact`로 다루고,
      `NO CONSENT BY ANALOGY` mark를 도입한다.
23. [Fiction Catalog](../01_catalog/README.md)
    - SAGA가 아직 active prototype shelf에 있으며, `qfuds-verse` universe/work
      구조로 옮기려면 별도 migration gate를 통과해야 함을 기록한다.

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
