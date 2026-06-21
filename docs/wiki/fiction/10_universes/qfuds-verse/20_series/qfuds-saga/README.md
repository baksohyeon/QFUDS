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
next_gate: write Chapter 6 final human hearing inside 20_drafts/1부/029 first-arc reboot manuscript
last_updated: 2026-06-21
---

# QFUDS SAGA

## 여기서 시작 (5초 요약)

- **qfuds-verse** = 세계(IP). **qfuds-saga** = 그 세계에서 쓰는 첫 장편 소설(작품).
  비유: qfuds-verse가 마블 유니버스라면, qfuds-saga는 그 안의 영화 한 편.
- 경로: `10_universes/qfuds-verse`(세계) 아래 `20_series/qfuds-saga`(작품).
- **무엇을 보나:** 원고는 부(arc) 단위 폴더로 관리한다. 새 active 1부 원고는
  `20_drafts/1부/029`, 2부 초안은 `20_drafts/2부/`. 직전 읽기용 prototype은
  `20_drafts/1부/_versions/`, 죽은 1세대는 `90_archive/qfuds-saga_1부_legacy/`.
  새 집필 기준은 `10_story_design/012` 아웃라인과 `013` scene cards. 설정 이해는
  `00_bible/`. 전체 목차는 이 README 아래 "먼저 읽을 것".
- **서랍(폴더) 역할:** 00_workroom 운영규칙 · 00_bible 설정집 · 10_story_design 기획 ·
  20_drafts 원고 초안 · 30_revisions 퇴고 · 40_release release manifest/export.

## 읽기 경로

새 1부 정본 작업은 [029 active reboot manuscript](20_drafts/1부/029_first_arc_book1_reboot_korean_primary.md)에서
진행한다. [012 통합 아웃라인](10_story_design/012_first_arc_book1_outline_reboot_ko.md)과
[013 scene cards](10_story_design/013_first_arc_scene_cards_ko.md)는 first draft entry
기준으로 통과했으며, 기존 prototype 본문을 문장 단위로 고치지 않는다.

| 상태 | 파일 | 설명 |
| --- | --- | --- |
| active reboot draft | [029](20_drafts/1부/029_first_arc_book1_reboot_korean_primary.md) | 1부 Book 1 한국어 primary 원고 SSOT. 프롤로그 + Ch1~5 작성됨, Ch6 남음 |
| pre-reboot prototype | [028](20_drafts/1부/_versions/1부_prototype/028_first_arc_opening_broken_crown_event_korean_primary.md) + [019](20_drafts/1부/_versions/1부_prototype/019_exhibit_s0_episode1_revised_v2_korean_adaptation.md)-[024](20_drafts/1부/_versions/1부_prototype/024_the_broken_crown_revised_v2_korean_adaptation.md) | provenance/readable prototype |

| 순서 | 편 | 한국어 prototype |
| --- | --- | --- |
| 프롤로그 | The Broken Crown 사건 | [028](20_drafts/1부/_versions/1부_prototype/028_first_arc_opening_broken_crown_event_korean_primary.md) |
| 1~6 | Exhibit S-0 … Broken Crown | [019](20_drafts/1부/_versions/1부_prototype/019_exhibit_s0_episode1_revised_v2_korean_adaptation.md)–[024](20_drafts/1부/_versions/1부_prototype/024_the_broken_crown_revised_v2_korean_adaptation.md) |
| release 상태 | active release 없음 | [40_release](40_release/README.md) |

- **드래프트가 왜 이렇게 많은지** + 현행/레거시 구분: [20_drafts 지도](20_drafts/README.md).
- **세계관 납득 사슬·검증 출처**: [bible 009 §2.5](00_bible/009_reader_accessibility_and_real_world_anchors_ko.md).
- **내 아이디어가 어디 갔나**: [작가 아이디어 추적 원장](00_workroom/006_creative_inputs_traceability_ko.md).
- **GSD 집필/승격 게이트**: [1부 Book 1 GSD Phase Brief](00_workroom/007_first_arc_book1_gsd_phase_brief_ko.md).
- **판본 변천사·회고**: [_versions 로그](20_drafts/1부/_versions/README.md).

이 폴더는 QFUDS에서 파생된 별도 창작 트랙이자 `qfuds-verse`의 canonical
series work다.

기존 [QFUDS Fiction Saga](../../../../90_archive/lineage-prototype/README.md)는 초기
프로토타입과 기원 기록으로 보존한다. 이 폴더는 이후 SAGA를 쓰기 위한
장편 시리즈 제작용 작업 선반이다.

핵심 원칙은 간단하다.

- `00_workroom/`: 작가실 운영 규칙, agent harness, MCP/workflow boundary.
- `00_bible/`: 작품 설정 기준서. 세계관, 역사, 세력, naming, 과학 경계.
- `10_story_design/`: pitch, 방향 매트릭스, outline, visual package, 실험적 설계.
- `20_drafts/`: 실제 prose draft, 한국어/영어 counterpart, scene test.
- `30_revisions/`: release-facing revision plan, line edit, continuity fix.
- `40_release/`: active release manifest/export. 현재는 pre-reboot provenance만 보존.
- `../../../../90_archive/`: 더 이상 active가 아닌 prototype.

소설 본문은 `20_drafts/`에 둔다. 세계관 설정은 `00_bible/`에 둔다.
작업 방법과 검수 규칙은 `00_workroom/`에 둔다. 아직 canon이 아닌 기획안과
시각/구조 실험은 `10_story_design/`에 둔다. release 후보로 가기 전 revision
control은 `30_revisions/`에 두고, 통과된 release manifest/export는 `40_release/`에 둔다.

## What Is `00_bible`?

`bible`은 여기서 종교적 의미가 아니다. TV/장편 시리즈 제작에서 빌려온
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

즉 `00_bible/`은 "설정 모음"이라기보다 장기 연재를 위한 내부 기준서다.

## Routing Note

Codex와 Claude Code 기준의 운영 경로는
[Documentation Folder Routing Workflow](../../../../../../../.agent/workflows/documentation-folder-routing-workflow.md)
가 정한다.

전체 fiction/IP 운영 규칙은
[Fiction IP Management Workflow](../../../../../../../.agent/workflows/fiction-ip-management-workflow.md)
가 정한다. 이 SAGA 폴더는 `qfuds-verse/20_series/qfuds-saga/` 아래의
canonical series work다.

현재 active shelf와 migration record는
[Fiction Catalog](../../../../01_catalog/README.md)에서 관리한다.

## Workflow Boundary

이 index는 SAGA 창작 트랙의 선반과 read order를 정한다. 새 외부 paper, web
reference, PDF, MCP 실행 결과, cached asset, extraction product, source/product
availability claim을 만들지 않는다.

외부 자료를 새로 쓰는 문서는
[Research Asset and Product Workflow](../../../../../../../.agent/workflows/research-asset-product-workflow.md)
를 별도로 적용하고 workflow state token을 자기 문서 안에 기록해야 한다.

현재 research asset workflow state:

```text
not searched
```

추출 가능성 분류:

```text
not_extractable
```

```text
active SAGA operating specs -> 00_workroom/
active SAGA series bible / canon reference -> 00_bible/
active SAGA pitches, outlines, visual packages -> 10_story_design/
active SAGA prose drafts with harness/provenance boundary -> 20_drafts/
active SAGA revision/release prep -> 30_revisions/
active SAGA release candidate -> 40_release/
raw prose-only drafts without harness boundary -> do not add as-is
superseded fiction prototypes -> ../../../../90_archive/
```

즉 이 트랙은 "설정표 폴더"가 아니라 작은 출판사 편집실처럼 관리한다.
운영 규칙, 작품 설정 기준서, 개발 패키지, 원고는 서로 다른 shelf에 놓는다.

## Promotion Rule

새 아이디어는 바로 정사가 아니다.

```text
brainstorm -> 10_story_design draft/pitch
development item that becomes stable world fact -> 00_bible
scene written as prose -> 20_drafts
release-facing revision plan -> 30_revisions
reader-facing release candidate -> 40_release
repeatable writing or review rule -> 00_workroom
superseded or prototype material -> ../../../../90_archive
```

`20_drafts/`의 장면은 읽을 수 있는 원고지만 자동으로 canon은 아니다.
canon으로 승격하려면 `00_bible/`의 세계관/인물/제도 규칙에 반영되어야 한다.

## Draft / Revision Boundary

`20_drafts/`는 새 장면, 한국어 primary draft, 영어 Anglophone counterpart,
legacy provenance draft를 둔다. 아직 독자용 release 후보가 아닌 실제 원고
작업 공간이다.

`30_revisions/`는 이미 존재하는 원고를 독자용 release 후보로 밀어 올릴 때
사용한다. line edit plan, continuity fix matrix, field mark alignment,
한국어/영어 counterpart 점검처럼 release-facing control이 필요한 작업을 둔다.

`40_release/`에는 한국어 primary, 영어 counterpart, shared continuity check가
모두 끝난 산출물만 둔다.

## 먼저 읽을 것

1. [QFUDS SAGA 창작 시스템](00_workroom/001_agentic_saga_system_ko.md)
   - AI writers' room, MCP 후보, 사용자 승인 게이트, 연구/창작 경계.
2. [QFUDS SAGA 세계관 방향 선택 매트릭스](10_story_design/001_world_direction_matrix_ko.md)
   - Nested Cosmology, closed-world revelation, deep-time empire, tactical
     philosophy SF, it-from-bit mythos 후보 비교.
3. [QFUDS SAGA 세계 기준점과 핍진성 규칙](00_bible/001_world_anchor_and_verisimilitude_ko.md)
   - SAGA가 현대 2023-2026 AI 현실감 붕괴를 고대사로 삼는 우리 우주의 먼
     미래라는 점, 그리고 기적을 제도/계급/절차로 바꾸는 핍진성 규칙.
4. [QFUDS SAGA 장기 복원 문명사 타임라인](00_bible/002_deep_time_restoration_timeline_ko.md)
   - 완전 복원, 라스트 아카이브, 망각권, 알레테이아 베일, 라우어 관측소를
     시간순 역사로 정리한 작품 설정 기준서 항목.
5. [QFUDS SAGA 세력 문화 권력 생태계 장부](00_bible/003_factions_cultures_power_ecology_ko.md)
   - 복원 문명의 세력, 공동체, 정치권력, 종교적 언어, 원장 자본주의,
     망각권, 잔상 유목민 생태계를 정리한 작품 설정 기준서 항목.
6. [QFUDS SAGA 시점 주제 고유명사 규칙](00_bible/004_narrative_pov_theme_naming_ko.md)
   - 3인칭 제한 시점의 decision rationale, 중심 주제, 역사 차용 규칙,
     common/formal name 이중 구조와 종교/제국/수도원/유목 naming strata를
     고정하는 작품 설정 기준서 항목.
7. [QFUDS SAGA Bitcoin Genesis Chain과 복원 신화](00_bible/005_bitcoin_genesis_chain_and_restoration_myth_ko.md)
   - Bitcoin을 Genesis Chain artifact로 사용하고, `it from bit`, 현실 편집,
     암호학 붕괴, 블랙홀/화이트홀 복원, Mara Veyr 사건을 연결하는 SAGA
     기원 신화. 최신 비트코인 위상·이념전쟁 적용은 017이 우선한다.
8. [QFUDS SAGA Post-AGI 문명사와 한국어 우선 이중언어 프로토콜](00_bible/006_post_agi_civilization_history_bilingual_protocol_ko.md)
   - AI/AGI 이후 문명사, Marxian general intellect lens, cryptographic death,
     `It from bit(s)`/Bitcoin irony layer, 한국어 본문 우선/영어 독립 각색
     작성 프로토콜.
9. [QFUDS SAGA 암호학적 죽음과 해시 계약](00_bible/007_cryptographic_death_and_hash_covenant_ko.md)
   - 사용자 제공 hash/KDF/cryptographic-hash 개념 노트를 SAGA의 Cryptographic
     Death, Preimage Restoration, Genesis Chain, identity-flood attack,
     key/salt sovereignty 설정 기준서로 변환한 science-auditor reference.
10. [QFUDS SAGA 첫 Arc Canon 정리](00_bible/008_first_arc_canon_consolidation_ko.md)
    - `The Broken Crown` first arc rough draft set에서 생긴 field mark chain,
      인물/세력 기능, science-fiction boundary, arc two hook, revision checklist를
      정리한 series-bible bridge.
11. [QFUDS SAGA Mara Veyr 프롤로그 연구 하네스](00_workroom/002_mara_veyr_prologue_research_harness_ko.md)
   - Mara Veyr 프롤로그를 쓰기 전, 소설 craft, COVID 이후 digital afterlife,
     right to be forgotten, AI reality editing, Bitcoin artifact, science-audit
     경계를 묶는 writer harness.
12. [QFUDS SAGA Mara Veyr 프롤로그 초안](../../../../90_archive/qfuds-saga_1부_legacy/001_mara_veyr_prologue_draft_ko.md)
   - cryptographic death, Genesis Chain, Last Archive, The Broken Crown,
     Continuity Court, Mara Veyr 자기부정 복원체 사건을 실제 프롤로그 장면으로
     테스트한 초안.
13. [QFUDS SAGA Mara Veyr Prologue English Revision](../../../../90_archive/qfuds-saga_1부_legacy/002_mara_veyr_prologue_english_revision_ko.md)
    - legacy English-first tone revision. 한국어 번역을 포함한 bilingual
      provenance이며, 이후 active prose는 한국어 본문 우선 정책을 따른다.
14. [QFUDS SAGA 시각 전시물 설계](10_story_design/002_visual_exhibit_design_ko.md)
    - 기존 rough-tanh PNG/SVG asset을 court exhibit, archive plate, visual
      metaphor로 쓰는 후보와 caption 규칙. fiction/provenance only.
15. [QFUDS SAGA 출범 패키지](10_story_design/003_saga_launch_package_ko.md)
    - SAGA를 첫 작품 기획으로 옮기는 launch package. 핵심 질문, first arc,
      주인공 후보, 첫 episode hook, 세력 기능, technical kill-switch,
      non-canon 항목을 정리한다.
16. [QFUDS SAGA Liora Sen 첫 Episode Beat Sheet](10_story_design/004_liora_sen_first_episode_beat_sheet_ko.md)
    - `Exhibit S-0` working title의 first episode beat sheet. Liora 중심
      장면 순서, 인물 압력, reveal order, technical guard, 다음 draft 후보를
      정리한다.
17. [QFUDS SAGA Genesis Chain 유물 장면 패킷](10_story_design/005_genesis_chain_artifact_scene_packet_ko.md)
    - Bitcoin/Genesis Chain을 zero price, crown artifact, broken
      cryptography, black-hole restoration myth로 나누어 first arc 장면
      압력으로 바꾸는 development packet.
18. [QFUDS SAGA 첫 Arc 6화 Outline](10_story_design/006_first_arc_six_episode_outline_ko.md)
    - `The Broken Crown` 첫 arc를 여섯 episode로 나누어 Mara Veyr, Genesis
      Chain, Cryptographic Death, Identity Flood, Hawking Court를 단계적으로
      배치한 development outline.
19. [QFUDS SAGA Exhibit S-0 Opening English Draft](../../../../90_archive/qfuds-saga_1부_legacy/003_exhibit_s0_opening_english_draft.md)
    - `The Broken Crown` 1화 opening candidate. Liora Sen이 Waiting City와
      Court of Continuance를 통과하며 Mara Veyr hearing으로 들어가는
      legacy English-first prose draft.
20. [QFUDS SAGA Exhibit S-0 Hearing Continuation English Draft](../../../../90_archive/qfuds-saga_1부_legacy/004_exhibit_s0_hearing_continuation_english_draft.md)
    - 003 opening을 이어 Mara Veyr hearing, Broken Crown exhibit,
      continuity tests, `RECOVERABLE / NOT CLAIMABLE` category, Last Archive
      question correction까지 진행한 legacy English-first continuation draft.
21. [QFUDS SAGA Exhibit S-0 Episode 1 Revised English Draft](../../../../90_archive/qfuds-saga_1부_legacy/005_exhibit_s0_episode1_revised_english_draft.md)
    - 003 opening과 004 hearing continuation을 보존한 상태에서 하나의
      Episode 1 rough cut으로 압축한 revision pass.
22. [QFUDS SAGA The Dead Exchange English Draft](../../../../90_archive/qfuds-saga_1부_legacy/006_the_dead_exchange_english_draft.md)
    - Episode 2 legacy English-first draft. Genesis Chain을 죽은 시장이 아니라
      살아 있는 상속/권력 장치로 보여 주고, `ACCESS != AUTHORITY` mark를
      도입한다.
23. [QFUDS SAGA The Last Hodler English Draft](../../../../90_archive/qfuds-saga_1부_legacy/007_the_last_hodler_english_draft.md)
    - Episode 3 legacy English-first draft. Bitcoin/Genesis Chain을 현재 시장 예측이
      아니라 미래 신화와 `civilization-scale consent artifact`로 다루고,
      `NO CONSENT BY ANALOGY` mark를 도입한다.
24. [QFUDS SAGA Identity Flood English Draft](../../../../90_archive/qfuds-saga_1부_legacy/008_identity_flood_english_draft.md)
    - Episode 4 legacy English-first draft. Null-Key Cells의 identity graph flood로
      깨끗한 identity proof를 무너뜨리고, `PLURALITY IS NOT CONSENT` mark를
      도입한다.
25. [QFUDS SAGA Hawking Court English Draft](../../../../90_archive/qfuds-saga_1부_legacy/009_hawking_court_english_draft.md)
    - Episode 5 legacy English-first draft. Genesis Chain을 cosmic audit 문제로
      확장하되, black-hole/Hawking restoration과 QFUDS는 fiction premise로만
      두고 `PHYSICS IS NOT JURISDICTION` mark를 도입한다.
26. [QFUDS SAGA The Broken Crown English Draft](../../../../90_archive/qfuds-saga_1부_legacy/010_the_broken_crown_english_draft.md)
    - Episode 6 legacy English-first first-arc finale draft. Mara의 sealed letter와
      field mark chain으로 첫 arc를 닫고, `who may author loss`를 다음 arc
      질문으로 연다.
27. [QFUDS SAGA First Arc Full Revision Pass](../../../../90_archive/qfuds-saga_1부_legacy/011_first_arc_full_revision_pass.md)
    - 1-6화 rough draft를 직접 덮어쓰기 전, arc-level cut/addition,
      episode-level revision matrix, field mark rules, continuity fixes,
      다음 rewrite loop를 고정한 revision control pass.
28. [QFUDS SAGA Exhibit S-0 Episode 1 Revised V2 English Draft](20_drafts/1부/_versions/1부_prototype/012_exhibit_s0_episode1_revised_v2_english_draft.md)
    - Episode 1 preserved English v2 counterpart. Mara의 active refusal을 더 앞당기고, Genesis/Broken
      Crown 설명을 chamber pressure 안으로 압축하며, `RECOVERABLE / NOT
      CLAIMABLE`을 provisional field mark로 유지한다.
29. [QFUDS SAGA The Dead Exchange Revised V2 English Draft](20_drafts/1부/_versions/1부_prototype/013_the_dead_exchange_revised_v2_english_draft.md)
    - Episode 2 preserved English v2 counterpart. Noor의 household privacy, maternal burial record,
      kinship graph cost를 먼저 제시하고, `ACCESS != AUTHORITY`를 living
      cost에 묶는다.
30. [QFUDS SAGA The Last Hodler Revised V2 English Draft](20_drafts/1부/_versions/1부_prototype/014_the_last_hodler_revised_v2_english_draft.md)
    - Episode 3 preserved English v2 counterpart. 군중 rhetoric을 줄이고, Ione을 통해 Aletheia split을
      앞당기며, Elias의 analogy transfer가 `NO CONSENT BY ANALOGY`로 막히는
      과정을 더 직접적으로 보여준다.
31. [QFUDS SAGA Identity Flood Revised V2 English Draft](20_drafts/1부/_versions/1부_prototype/015_identity_flood_revised_v2_english_draft.md)
    - Episode 4 preserved English v2 counterpart. Null-Key Cells를 단순 공격자가 아니라 court appetite를
      드러내는 애매한 고발자로 먼저 제시하고, `PLURALITY IS NOT CONSENT`를
      proof overflow의 living cost에 묶는다.
32. [QFUDS SAGA Hawking Court Revised V2 English Draft](20_drafts/1부/_versions/1부_prototype/016_hawking_court_revised_v2_english_draft.md)
    - Episode 5 preserved English v2 counterpart. H-1을 technical exhibit보다 먼저 mothers, graves,
      testimony pressure로 무섭게 만들고, QFUDS-adjacent lattice를
      `REJECTED / USEFUL / UNSAFE AS TRUTH CLAIM`으로 제한한다.
33. [QFUDS SAGA The Broken Crown Revised V2 English Draft](20_drafts/1부/_versions/1부_prototype/017_the_broken_crown_revised_v2_english_draft.md)
    - Episode 6 preserved English v2 counterpart. city fracture 설명을 줄이고, field marks가 이미 권력
      문법으로 재사용되는 위험을 앞당기며, `who may author loss`로 arc two를
      연다.
34. [QFUDS SAGA First Arc Polish Read-Order Pass](../../../../90_archive/qfuds-saga_1부_legacy/018_first_arc_polish_read_order_pass.md)
    - Phase 18 control checkpoint. 한국어 primary read order, 영어 v2 counterpart,
      continuity issue, exposition cut, field mark misuse risk를 고정한다.
35. [QFUDS SAGA Exhibit S-0 Episode 1 Korean Adaptation](20_drafts/1부/_versions/1부_prototype/019_exhibit_s0_episode1_revised_v2_korean_adaptation.md)
    - Episode 1 한국어 primary adaptation. `RECOVERABLE / NOT CLAIMABLE`을
      reader-facing 첫 장면 경로로 제시한다.
36. [QFUDS SAGA The Dead Exchange Korean Adaptation](20_drafts/1부/_versions/1부_prototype/020_the_dead_exchange_revised_v2_korean_adaptation.md)
    - Episode 2 한국어 primary adaptation. Noor의 living cost와
      `ACCESS != AUTHORITY`를 한국어 본문으로 읽게 한다.
37. [QFUDS SAGA The Last Hodler Korean Adaptation](20_drafts/1부/_versions/1부_prototype/021_the_last_hodler_revised_v2_korean_adaptation.md)
    - Episode 3 한국어 primary adaptation. Elias의 analogy error와
      `NO CONSENT BY ANALOGY`를 한국어 장면 압력으로 옮긴다.
38. [QFUDS SAGA Identity Flood Korean Adaptation](20_drafts/1부/_versions/1부_prototype/022_identity_flood_revised_v2_korean_adaptation.md)
    - Episode 4 한국어 primary adaptation. Null-Key Cells, witness rings,
      `PLURALITY IS NOT CONSENT`를 한국어 독서 경로로 둔다.
39. [QFUDS SAGA Hawking Court Korean Adaptation](20_drafts/1부/_versions/1부_prototype/023_hawking_court_revised_v2_korean_adaptation.md)
    - Episode 5 한국어 primary adaptation. H-1, QFUDS-adjacent warning,
      `PHYSICS IS NOT JURISDICTION`을 fiction boundary 안에 둔다.
40. [QFUDS SAGA The Broken Crown Korean Adaptation](20_drafts/1부/_versions/1부_prototype/024_the_broken_crown_revised_v2_korean_adaptation.md)
    - Episode 6 한국어 primary adaptation. protected pending doctrine과
      `who may author loss`로 첫 arc를 닫는다.
41. [QFUDS SAGA Revision Shelf](30_revisions/README.md)
    - 첫 arc 한국어 polish, line edit, continuity-fix pass처럼 release-facing
      control이 필요한 작업을 두는 선반.
42. [QFUDS SAGA Release Shelf](40_release/README.md)
    - active release manifest/export를 두는 선반. 현재 1부는 029 reboot draft
      진행 중이므로 `900_` provenance manifest만 보존하고 본문 중복 build는 두지 않는다.
43. [Fiction Catalog](../../../../01_catalog/README.md)
    - SAGA의 canonical series path, old-path deletion policy, archive
      routing, next task candidates를 기록한다.
44. [QFUDS SAGA 이중언어 용어규율 글로서리](00_workroom/003_bilingual_term_discipline_glossary_ko.md)
    - 한국어 prose 본문에서 영어를 유지할 4범주(고유명사·제도 분위기어·암호물리
      용어·의도적 장치)와 한국어로 옮길 일반명사를 정한 집행 기준.
45. [QFUDS SAGA 1부 De-jargon·Polish 퇴고 계획](30_revisions/001_first_arc_dejargon_polish_revision_plan_ko.md)
    - 019-024 한국어 정본을 자연 한국어로 다듬은 line-edit pass의 통제 문서와
      검증 게이트(토큰 density, naturalness/content-fidelity 감사).
46. [QFUDS SAGA 독자 접근성과 실제 세계 앵커](00_bible/009_reader_accessibility_and_real_world_anchors_ko.md)
    - 비트코인·AI·AGI·LLM 인격 논쟁을 중·고생도 비약 없이 이해할 현실 앵커
      source pack. Bitcoin legal title/private-key control, AI infrastructure,
      AGI capability/autonomy, model welfare, self-report, legal personhood,
      authorship/inventorship, A-corp 논쟁의 allowed/blocked claim과 workflow
      state를 관리한다.
    - 짝 문서: [Last Archive 기원과 역연산 인과·이념사](00_bible/010_last_archive_origin_and_reversal_causality_ko.md)
      — Aletheia Systems/창업자 Adrian Karvath(아이언맨·머스크형 매드 사이언티스트,
      동력핵 the Arc)의 폭주 후신이 Last Archive·Laur·Aletheia Veil이 됨; 강제
      업로드된 비서 Vera가 핵; 비트코인 중심 인과(C2PA·블록체인 공증→포획→역산);
      AGI는 없다(합의의 신격화, SSOT 없음); 죽음의 평등.
    - 짝 문서: [연표·복원 행정·블랙홀 본거지](00_bible/011_chronology_restoration_admin_black_hole_seat_ko.md)
      — 지수→로그 기술곡선과 deep-time 연표, 복원 행정 절차·세대 해상도(낙인·계급),
      Last Archive의 은하 중심 블랙홀 본거지(홀로그래피=최대 정보 저장).
    - 짝 문서: [Last Archive 반전 설계](10_story_design/008_last_archive_reveal_architecture_ko.md)
      — 옵션 3(합의의 신격화)을 반전으로 터뜨리는 3막 속임·떡밥 9개·페어플레이.
    - 짝 문서: [형식·throughline·진행 상태](10_story_design/009_format_throughline_and_progress_ko.md)
      — 덴마식 단편→대하 사가 형식, 시리즈 관통 질문, 1부 6편 드래프트 완료 현황.
47. [QFUDS SAGA Arc Two Korean-Primary Plan](10_story_design/007_arc_two_korean_primary_plan_ko.md)
    - `who may author loss` 이후 2부를 열기 위한 최소 설계. 보호 미결 교리가
      시장, 신청서, 계급 경계가 되는 위험을 025의 장면 목표로 고정한다.
48. [QFUDS SAGA Who May Author Loss Korean Primary](20_drafts/2부/025_who_may_author_loss_korean_primary.md)
    - Arc Two 첫 한국어 primary draft. `protected pending doctrine`이 상실 접수
      창구와 상품이 되는 순간을 열고, `UNRECOVERED IS NOT UNREAL`을 새 임시
      field mark로 제시한다.
49. [QFUDS SAGA 1부 전역 템플릿 커버리지 감사](30_revisions/003_first_arc_template_coverage_audit_ko.md)
    - `.agent/templates/fiction/` 기준으로 1부 바이블·하네스·release 시스템의
      충족/누락을 점검한다. pre-reboot prototype의 series gate 비대칭은 닫혔고,
      현재 active check 대상은 029다.
50. [QFUDS SAGA Series Bible Drift Alignment Audit](30_revisions/008_series_bible_drift_alignment_audit_ko.md)
    - 001-020 bible 전체를 점검해 오래된 후보/승인 전/영어 rough/Bitcoin dead-relic
      drift를 015·017·018·028 story-order 기준으로 정렬한 감사 기록.
51. [QFUDS SAGA 1부 Book 1 백지 재설계 통합 아웃라인](10_story_design/012_first_arc_book1_outline_reboot_ko.md)
    - 흩어져 있던 beat 문서(004·005·006·008·009·011)와 bible grounding을 Book 1
      cause/effect chain, 정보 공개 장부, 인물 arc, 장별 목적표로 통합한 active outline SSOT.
52. [QFUDS SAGA 1부 Book 1 씬 카드](10_story_design/013_first_arc_scene_cards_ko.md)
    - 012 outline을 장면별 `POV`, `want`, `obstacle`, `turn`, `cost`, 기술어 노출,
      정보 공개, 다음 hook으로 쪼갠 prose 직전 차단 게이트.
53. [QFUDS SAGA 1부 Book 1 Reboot Korean Primary](20_drafts/1부/029_first_arc_book1_reboot_korean_primary.md)
    - 012 outline과 013 scene-card gate를 통과한 active Korean-primary manuscript
      SSOT. 기존 028+019-024를 문장 단위로 고치지 않고 Prologue부터 백지 재작성한다.
54. [QFUDS SAGA 1부 Book 1 GSD Phase Brief](00_workroom/007_first_arc_book1_gsd_phase_brief_ko.md)
    - 029를 장편 SAGA 원고로 완성하기 위한 GSD brief. 프롤로그/각 장 최소 분량,
      한국어 primary 우선, 영어 독립 각색판, shared continuity, 사용자 pre-release
      확인 후 `40_release/001_` 승격 조건을 고정한다.

## First Arc Provenance Draft Set

`The Broken Crown` first arc의 6개 legacy rough draft가 모두 작성되었다.

| Episode | Draft |
| --- | --- |
| 1. Exhibit S-0 | [005](../../../../90_archive/qfuds-saga_1부_legacy/005_exhibit_s0_episode1_revised_english_draft.md) |
| 2. The Dead Exchange | [006](../../../../90_archive/qfuds-saga_1부_legacy/006_the_dead_exchange_english_draft.md) |
| 3. The Last Hodler | [007](../../../../90_archive/qfuds-saga_1부_legacy/007_the_last_hodler_english_draft.md) |
| 4. Identity Flood | [008](../../../../90_archive/qfuds-saga_1부_legacy/008_identity_flood_english_draft.md) |
| 5. Hawking Court | [009](../../../../90_archive/qfuds-saga_1부_legacy/009_hawking_court_english_draft.md) |
| 6. The Broken Crown | [010](../../../../90_archive/qfuds-saga_1부_legacy/010_the_broken_crown_english_draft.md) |

전체 arc revision control pass는
[011 First Arc Full Revision Pass](../../../../90_archive/qfuds-saga_1부_legacy/011_first_arc_full_revision_pass.md)
로 정리되었다. Revised v2 English counterpart pass는 현재 1-6화까지 진행되었다.

| English counterpart | Draft |
| --- | --- |
| 1. Exhibit S-0 v2 | [012](20_drafts/1부/_versions/1부_prototype/012_exhibit_s0_episode1_revised_v2_english_draft.md) |
| 2. The Dead Exchange v2 | [013](20_drafts/1부/_versions/1부_prototype/013_the_dead_exchange_revised_v2_english_draft.md) |
| 3. The Last Hodler v2 | [014](20_drafts/1부/_versions/1부_prototype/014_the_last_hodler_revised_v2_english_draft.md) |
| 4. Identity Flood v2 | [015](20_drafts/1부/_versions/1부_prototype/015_identity_flood_revised_v2_english_draft.md) |
| 5. Hawking Court v2 | [016](20_drafts/1부/_versions/1부_prototype/016_hawking_court_revised_v2_english_draft.md) |
| 6. The Broken Crown v2 | [017](20_drafts/1부/_versions/1부_prototype/017_the_broken_crown_revised_v2_english_draft.md) |

## Korean Primary First Arc Reading Path

Phase 18부터 first-reader path는 한국어판을 먼저 둔다. 현재 1부 한국어판은
pre-reboot prototype이며, 영어 v2는 같은 사건을 공유하는 preserved counterpart로 둔다.
새 정본 작업은 [029](20_drafts/1부/029_first_arc_book1_reboot_korean_primary.md) 한 파일에서
진행한다.

| Active reboot | Korean primary manuscript | English counterpart |
| --- | --- | --- |
| Book 1 | [029](20_drafts/1부/029_first_arc_book1_reboot_korean_primary.md) | not started. Korean draft first, then Anglophone independent adaptation |

| Episode | Korean primary | English counterpart |
| --- | --- | --- |
| 1. Exhibit S-0 | [019](20_drafts/1부/_versions/1부_prototype/019_exhibit_s0_episode1_revised_v2_korean_adaptation.md) | [012](20_drafts/1부/_versions/1부_prototype/012_exhibit_s0_episode1_revised_v2_english_draft.md) |
| 2. The Dead Exchange | [020](20_drafts/1부/_versions/1부_prototype/020_the_dead_exchange_revised_v2_korean_adaptation.md) | [013](20_drafts/1부/_versions/1부_prototype/013_the_dead_exchange_revised_v2_english_draft.md) |
| 3. The Last Hodler | [021](20_drafts/1부/_versions/1부_prototype/021_the_last_hodler_revised_v2_korean_adaptation.md) | [014](20_drafts/1부/_versions/1부_prototype/014_the_last_hodler_revised_v2_english_draft.md) |
| 4. Identity Flood | [022](20_drafts/1부/_versions/1부_prototype/022_identity_flood_revised_v2_korean_adaptation.md) | [015](20_drafts/1부/_versions/1부_prototype/015_identity_flood_revised_v2_english_draft.md) |
| 5. Hawking Court | [023](20_drafts/1부/_versions/1부_prototype/023_hawking_court_revised_v2_korean_adaptation.md) | [016](20_drafts/1부/_versions/1부_prototype/016_hawking_court_revised_v2_english_draft.md) |
| 6. The Broken Crown | [024](20_drafts/1부/_versions/1부_prototype/024_the_broken_crown_revised_v2_korean_adaptation.md) | [017](20_drafts/1부/_versions/1부_prototype/017_the_broken_crown_revised_v2_english_draft.md) |

이 6편은 현장감·묘사 강화 퇴고([002 기준](30_revisions/002_first_arc_release_immersion_revision_plan_ko.md))와
편별 release 감사(ai-tell CLEAN, naturalness A, 필드 마크 무결성)를 통과했던
pre-reboot 상태로, 현재는 [900 release manifest](40_release/900_pre_reboot_first_arc_release_manifest_ko.md)에
provenance만 보존한다.

## Arc Two Korean Primary Start

| Step | Output |
| --- | --- |
| Arc Two plan | [007](10_story_design/007_arc_two_korean_primary_plan_ko.md) |
| 세력 명칭 canon 확정 | [015](00_bible/015_factions_canon_naming_ko.md) |
| Episode 025 Korean primary (`who may author loss`) | [025](20_drafts/2부/025_who_may_author_loss_korean_primary.md) |
| Episode 025 English counterpart | [026](20_drafts/2부/026_who_may_author_loss_english_counterpart.md) |
| Episode 027 Korean primary (`who may refuse`) | [027](20_drafts/2부/027_who_may_refuse_korean_primary.md) |

025·027은 사용자 승인 후 작성된 한국어 primary draft이며 AI-tell·자연스러움 감사를
통과했다(둘 다 CLEAN/A급). 026은 025의 영어 Anglophone counterpart다. 027의 영어
counterpart는 아직 작성하지 않았다. 세력 명칭은 [015](00_bible/015_factions_canon_naming_ko.md)에서
candidate 상태를 걷어내고 canon으로 고정했다(Domus Clavium·Ordo Salis·Custodes
Umbrae·Curia Continuum·Cellulae Sine Clave 등).

## Next Korean-Primary Prose Task Gate

다음 한국어 prose 작업은 [029](20_drafts/1부/029_first_arc_book1_reboot_korean_primary.md)
안에서 Chapter 3 `The Last Hodler`를 이어 쓰는 것이다. 1부는 outline-first reboot
상태로 전환됐고, [013 scene cards](10_story_design/013_first_arc_scene_cards_ko.md)는
first draft entry 기준으로 통과했다.

| Gate | Output shelf | When to choose |
| --- | --- | --- |
| First-arc Book 1 manuscript | [029](20_drafts/1부/029_first_arc_book1_reboot_korean_primary.md) | 013을 통과한 새 1부 한국어 primary 원고를 이어 쓸 때 |
| Arc Two planning | `10_story_design/` | `who may author loss` 이후의 사건, 인물, field mark를 아직 설계해야 할 때 |
| First-arc Korean line polish | `30_revisions/` | 기존 019-024 prototype을 보존용으로만 미세 정리할 때. 새 정본 rewrite 용도 아님 |
| English Anglophone counterpart for 025 | `20_drafts/026_*_english_adaptation.md` 또는 별도 번호 | 025의 사건을 영미권 독자 리듬으로 독립 각색할 때 |
| New Korean primary scene | `20_drafts/026_*_korean_primary.md` | Arc Two 다음 episode를 한국어로 바로 이어 쓸 때 |

first-arc Korean line polish의 1차 pass(영어 코드스위칭 제거 de-jargon)는
[30_revisions/001 퇴고 계획](30_revisions/001_first_arc_dejargon_polish_revision_plan_ko.md)으로
실행되었다. Arc Two planning, 025·027 한국어 primary draft, 025 영어 counterpart(026),
세력 명칭 canon(015)이 사용자 승인 후 작성·감사 완료되었다. 하지만 1부는 prose
patching 대신 백지 재설계로 전환했다. 다음 자연스러운 작업은 027 영어 독립 각색판이나
Arc Two 확장이 아니라, 029에서 Chapter 3 `The Last Hodler`를 이어 쓰는 것이다.

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
