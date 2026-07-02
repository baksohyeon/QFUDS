---
doc_id: qfuds_saga_encyclopedia_ko
title: QFUDS SAGA 백과사전 (자동 생성 · 한 장 요약)
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - qfuds_saga_index_ko
  - qfuds_saga_drafts_index_ko
next_gate: 문서 변경 후 python3 scripts/build_saga_digest.py 재실행으로 갱신
last_updated: 2026-07-02
---

# QFUDS SAGA 백과사전 (자동 생성 · 한 장 요약)

> **자동 생성 파일.** 손으로 고치지 마세요. 원고·설계 문서가 바뀌면 `python3 scripts/build_saga_digest.py`를 다시 돌리면 이 한 장이 최신으로 갱신됩니다. 이 페이지는 SAGA 전체를 위에서 아래로 쭉 읽는 백과사전이고, 실제 편집은 각 원본 문서에서 합니다.

수록 문서 94개 · 최신 갱신 기준 2026-07-02 · 완성/작성중 같은 판단은 [20_drafts 지도](20_drafts/README.md)가 최종 기준(SSOT)이다.

**리센터 이전 라벨 포함 5개** (본문에 옛 부 번호 잔존, 상단 SSOT 우선): [QFUDS SAGA 첫 Arc Canon 정리](00_bible/008_first_arc_canon_consolidation_ko.md) · [QFUDS SAGA 주인공 시트 — Liora Sen](00_bible/012_character_liora_sen_ko.md) · [QFUDS SAGA 앙상블 캐릭터 보이스·관계 바이블](00_bible/016_character_ensemble_voices_relationships_ko.md) · [QFUDS SAGA 입체 캐릭터 시트](00_bible/019_character_depth_sheets_ko.md) · [QFUDS SAGA Truth-State Ledger](00_workroom/014_truth_state_ledger_ko.md)

## 1. 선반 지도 — 폴더가 곧 성숙 단계

아이디어 → 설계 → 원고 → 교정 → 출간 순으로 익어간다.

| 선반 | 역할 | 문서 수 |
| --- | --- | --- |
| [`20_drafts`](20_drafts/) | 실제 원고 (부/arc별). 지금 읽고 고치는 소설 | 30 |
| [`10_story_design`](10_story_design/) | 아이디어·아웃라인·arc 지도·씬카드 (확정 전 설계) | 23 |
| [`00_bible`](00_bible/) | 확정된 세계 사실·인물·제도·과학 경계 (설정 기준서) | 10 |
| [`30_revisions`](30_revisions/) | 출간용 교정·게이트 기록 | 15 |
| [`00_workroom`](00_workroom/) | 운영 규칙·GSD brief·오늘 작업 상태판 | 15 |
| [`40_release`](40_release/) | 출간 후보·내보내기 (게이트 통과 후) | 1 |

## 2. 최근 갱신 — 지금 뜨거운 곳

가장 최근에 손댄 문서들. "지금 뭘 작업 중인가"의 데이터 기반 신호다.

| 갱신일 | 문서 | 선반 |
| --- | --- | --- |
| 2026-07-02 | [QFUDS SAGA 형식·시리즈 throughline·현재 진행 상태](10_story_design/009_format_throughline_and_progress_ko.md) | `10_story_design` |
| 2026-07-02 | [QFUDS SAGA 세계관·인물 한눈에 (독자·작가 오리엔테이션)](10_story_design/023_first_arc_reader_orientation_world_and_cast_ko.md) | `10_story_design` |
| 2026-07-02 | [QFUDS SAGA 근미래 프렐류드 대사전 (2020s-2090s 예측, candidate)](10_story_design/027_near_future_prelude_forecast_ko.md) | `10_story_design` |
| 2026-07-02 | [QFUDS SAGA 시점 주제 고유명사 규칙](00_bible/004_narrative_pov_theme_naming_ko.md) | `00_bible` |
| 2026-07-02 | [QFUDS SAGA 이념 비일관성 삼각 (세 양립 불가 신앙)](00_bible/023_ideological_incoherence_triad_ko.md) | `00_bible` |
| 2026-07-02 | [QFUDS SAGA 캐릭터 지도와 타임라인 좌표](00_bible/024_character_map_and_timeline_coordinates_ko.md) | `00_bible` |
| 2026-07-02 | [QFUDS SAGA Production Board](00_workroom/009_saga_production_board_ko.md) | `00_workroom` |
| 2026-07-01 | [QFUDS SAGA Last Archive 반전 설계와 떡밥 배치](10_story_design/008_last_archive_reveal_architecture_ko.md) | `10_story_design` |
| 2026-07-01 | [QFUDS SAGA 다부작 아크 지도](10_story_design/011_saga_arc_map_multiarc_ko.md) | `10_story_design` |
| 2026-07-01 | [QFUDS SAGA 5대 극적 질문 스파인](10_story_design/015_five_core_dramatic_questions_spine_ko.md) | `10_story_design` |
| 2026-07-01 | [QFUDS SAGA 1부 origin 아웃라인](10_story_design/016_first_arc_origin_outline_ko.md) | `10_story_design` |
| 2026-07-01 | [QFUDS SAGA 암호 개념 독자 온보딩 점검](10_story_design/018_crypto_concepts_reader_onboarding_check_ko.md) | `10_story_design` |

## 3. 작업 큐 — 각 문서의 다음 할 일 (next_gate)

각 문서가 스스로 적어둔 "다음 관문". 원고(20_drafts)와 설계(10_story_design)의 미완 항목이 곧 당신의 결정·집필 대기열이다. 버전 히스토리(`_versions/`)는 뺐다 — 옛 판본 계보는 4절 전체 목록에서 볼 수 있다.

### 20_drafts

- **[QFUDS SAGA 캐스 풀길이 소설 (한국어 primary)](20_drafts/0부/036_jua_full_novel_korean_primary.md)** — 보이스 확정 후 5비트 따라 풀길이. 구조 통합(캐스 단일화)은 새 세션에서 정리
- **[QFUDS SAGA origin(신규 1부) 사엘 한국어 primary 원고](20_drafts/1.5부/030_origin_arc_sael_korean_primary.md)** — B1~B7 origin 초고 완성(2026-06-21). continuity(030 1부 → 029 2부 handoff)·AI-tell·reader-sim 검수 후 release-facing revision 게이트
- **[QFUDS SAGA origin(1부) 사엘 · 웹소설 콘티 텔링(이해 우선)](20_drafts/1.5부/031_origin_sael_webnovel_storyboard_ko.md)** — 회차1(하네싱 정합 온보딩) draft 완료(2026-06-22). 톤 승인 후 회차2~7 self-paced append. continuity(031↔030↔029)·AI-tell·reader-sim 후 revision 게이트
- **[QFUDS SAGA origin (Book 1) Sael · Web-Serial Storyboard (English adaptation)](20_drafts/1.5부/032_origin_sael_webnovel_storyboard_en.md)** — Episode 1 voice draft (2026-06-22). On voice approval, adapt Episodes 2-7 then run shared continuity check (EN vs 031 KO)
- **[QFUDS SAGA origin(1.5부) 사엘 풀길이 소설 (한국어 primary)](20_drafts/1.5부/033_origin_sael_full_novel_korean_primary.md)** — 1장(B1) 풀길이 draft(2026-06-22). 결 승인 후 2~8장 집필, retention+comprehension 게이트
- **[QFUDS SAGA 1부 「오르페우스」 풀길이 소설 (한국어 primary)](20_drafts/1부/035_orpheus_full_novel_korean_primary.md)** — 1장 draft(2026-06-30). 보이스 승인 후 2~8장 집필 + 과학 부록
- **[QFUDS SAGA 1부 Book 1 Reboot Korean Primary](20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md)** — run review/chronicler pass for completed Ch6; this manuscript is canonical 2부 Mara asset under 011 §10
- **[QFUDS SAGA 2부 마라 풀길이 소설 (한국어 primary)](20_drafts/2부/034_mara_full_novel_korean_primary.md)** — 1장(풀길이) draft(2026-06-22). 결 승인 후 2~6장 집필, retention+comprehension 게이트
- **[QFUDS SAGA Who May Author Loss Korean Primary](20_drafts/3부/025_who_may_author_loss_korean_primary.md)** — write English counterpart (026) then advance to next KR primary 027 (who may refuse)
- **[QFUDS SAGA Who May Author Loss English Counterpart](20_drafts/3부/026_who_may_author_loss_english_counterpart.md)** — this is EN counterpart (026) of KR primary 025; next KR primary is 027 (who may refuse)
- **[QFUDS SAGA Who May Refuse Korean Primary](20_drafts/3부/027_who_may_refuse_korean_primary.md)** — decide English Anglophone counterpart or episode 028 Korean primary

### 10_story_design

- **[QFUDS SAGA 시각 전시물 설계](10_story_design/002_visual_exhibit_design_ko.md)** — decide whether one visual exhibit enters the next prose revision
- **[QFUDS SAGA Arc Two Korean-Primary Plan](10_story_design/007_arc_two_korean_primary_plan_ko.md)** — 025/027 Korean primary + 026 English counterpart written; next write 027 English counterpart or 028 Korean primary
- **[QFUDS SAGA Last Archive 반전 설계와 떡밥 배치](10_story_design/008_last_archive_reveal_architecture_ko.md)** — thread Act-1 deception + planted clues into prologue and first arc
- **[QFUDS SAGA 형식·시리즈 throughline·현재 진행 상태](10_story_design/009_format_throughline_and_progress_ko.md)** — build Liora protagonist sheet, then propagate foundation into first arc
- **[QFUDS SAGA 2부 에피소드 맵](10_story_design/010_arc_two_episode_map_ko.md)** — user approves arc length + ep3-6 direction, then write 028 Korean primary
- **[QFUDS SAGA 다부작 아크 지도](10_story_design/011_saga_arc_map_multiarc_ko.md)** — 1부 POV(사엘 능동화 vs 새 POV)를 작가가 확정하면 1부 origin 아웃라인을 별도 문서로 분기한다
- **[QFUDS SAGA 1부 Book 1 백지 재설계 통합 아웃라인](10_story_design/012_first_arc_book1_outline_reboot_ko.md)** — draft 20_drafts/029 first-arc Book 1 Korean-primary reboot manuscript
- **[QFUDS SAGA 1부 Book 1 씬 카드](10_story_design/013_first_arc_scene_cards_ko.md)** — draft 20_drafts/029 first-arc Book 1 Korean-primary reboot manuscript from this scene-card gate
- **[QFUDS SAGA 소버린 AI·오픈/봉쇄 축 브레인스토밍](10_story_design/014_sovereign_ai_open_closed_axis_brainstorm_ko.md)** — select seeds to promote into 00_bible (factions/SSOT) and 1부/2부 prose pressure
- **[QFUDS SAGA 5대 극적 질문 스파인](10_story_design/015_five_core_dramatic_questions_spine_ko.md)** — rebuild the multiarc map (011) and outlines on top of this spine (origin=1부 / Mara=2부)
- **[QFUDS SAGA 1부 origin 아웃라인](10_story_design/016_first_arc_origin_outline_ko.md)** — 작가가 사엘 원죄 형태(§4)와 콜드오픈(§5)을 승인하면 1부 비트를 scene-card로 분기
- **[QFUDS SAGA 1부 origin 씬 카드](10_story_design/017_first_arc_origin_scene_cards_ko.md)** — 작가가 카드를 승인하면 011 §10 번호 cascade 후 1부 origin 원고로 들어간다
- **[QFUDS SAGA 암호 개념 독자 온보딩 점검](10_story_design/018_crypto_concepts_reader_onboarding_check_ko.md)** — revise B1-B7 cards only if this check finds a release-blocking onboarding gap
- **[QFUDS SAGA 사엘 원고 실행 시트](10_story_design/019_sael_origin_execution_sheet_ko.md)** — 사엘 시트 승인 후 017 B1 reader-onboarding 보강 → 1부 origin 원고 진입
- **[QFUDS SAGA Q-Day 사건 사슬 bridge 아웃라인 (B1↔B2)](10_story_design/020_qday_incident_bridge_outline_ko.md)** — bridge 승인 후 B1 종착점 정합 확인 → B2(검증 요청) 산문 진입
- **[QFUDS SAGA 1부 독자 정보 공개 사다리 (reader reveal ladder)](10_story_design/021_first_arc_reader_reveal_ladder_ko.md)** — ladder 승인 후 B1을 "첫 균열 + 파일 handoff"로 압축 재배치 → B2 진입
- **[QFUDS SAGA 1부 통합 causal master outline](10_story_design/022_first_arc_causal_master_outline_ko.md)** — master outline 승인 → B1 압축(030↔카드 정렬) → B2 산문 진입
- **[QFUDS SAGA 세계관·인물 한눈에 (독자·작가 오리엔테이션)](10_story_design/023_first_arc_reader_orientation_world_and_cast_ko.md)** — 게이트 comprehension 테스트와 함께 사용. 원고가 이 오리엔테이션을 본문 안에서 전달하는지 점검
- **[새 1부 「오르페우스」 설계 — 사별·복원 사본·돌아봄](10_story_design/024_new_book1_orpheus_design_ko.md)** — 사용자 검토 후 1.5부 강등 정리 + 8챕터 초고 착수. 신규 주인공 024 캐논 등록
- **[사가 방향 전환 — 근미래 grounded SF로 무게중심 이동](10_story_design/025_near_future_recenter_direction_ko.md)** — 0부 착수(근미래 grounded). 기존 024 timeline·011 arc map·026은 점진적으로 이 방향에 맞춰 재조정
- **[기계 화자 보이스·복선·시대건너뛰기 구조 트리트먼트 (서사·보이스 렌즈)](10_story_design/026_machine_narrator_voice_and_setup_payoff_treatment_ko.md)** — 0부 프롤로그층 착수. 화자 문법·복선 회수 지도를 draft 집필의 연출 SSOT로 사용. 사실 앵커는 027이 우선
- **[QFUDS SAGA 근미래 프렐류드 대사전 (2020s-2090s 예측, candidate)](10_story_design/027_near_future_prelude_forecast_ko.md)** — 0부 앞 근미래 활주로 candidate 대사전. 캐논 승격은 원고 수요 때 030 §7 6체크. 026 Q-Day로 연결
- **[QFUDS SAGA 레지스터 전환 오프닝(판타지→하드SF)과 결말 옵션 (candidate/brainstorm)](10_story_design/028_register_morph_opening_and_ending_options_ko.md)** — 결말은 미정(옵션만). 선택된 방향만 011 아크 지도·024 좌표로 승격. 오프닝 장치는 008 반전과 동기화

## 4. 전체 문서 — 선반별 요약

각 문서의 한 문단 요약. 여기서 훑고, 자세히 볼 것만 링크로 연다.

### `20_drafts` — 실제 원고 (부/arc별). 지금 읽고 고치는 소설

#### [QFUDS SAGA 캐스 풀길이 소설 (한국어 primary)](20_drafts/0부/036_jua_full_novel_korean_primary.md)
`draft` · 2026-06-30 · reference

> [025 방향 전환](../../10_story_design/025_near_future_recenter_direction_ko.md) 결정에 따른

다음: 보이스 확정 후 5비트 따라 풀길이. 구조 통합(캐스 단일화)은 새 세션에서 정리

#### [QFUDS SAGA origin(신규 1부) 사엘 한국어 primary 원고](20_drafts/1.5부/030_origin_arc_sael_korean_primary.md)
`draft` · 2026-06-21 · reference

> 이 문서는 016/017/019 설계 스택으로 새로 짠 **origin 아크**(사엘 primary)의 active Korean-primary manuscript다. 015 spine이 폐기 지정한 029의 *수동 목격자 프롤로그*를

다음: B1~B7 origin 초고 완성(2026-06-21). continuity(030 1부 → 029 2부 handoff)·AI-tell·reader-sim 검수 후 release-facing revision 게이트

#### [QFUDS SAGA origin(1부) 사엘 · 웹소설 콘티 텔링(이해 우선)](20_drafts/1.5부/031_origin_sael_webnovel_storyboard_ko.md)
`draft` · 2026-06-22 · reference

> 이 문서는 [030 사엘 origin primary 원고](030_origin_arc_sael_korean_primary.md)의

다음: 회차1(하네싱 정합 온보딩) draft 완료(2026-06-22). 톤 승인 후 회차2~7 self-paced append. continuity(031↔030↔029)·AI-tell·reader-sim 후 revision 게이트

#### [QFUDS SAGA origin (Book 1) Sael · Web-Serial Storyboard (English adaptation)](20_drafts/1.5부/032_origin_sael_webnovel_storyboard_en.md)
`draft` · 2026-06-22 · reference

> This is the **Anglophone adaptation** of the Korean-primary web-serial telling [031](031_origin_sael_webnovel_storyboard_ko.md). Per the bilingual sequence it is a same-story counterpart written for English rhythm, idiom, and web-serial genre expectations, **not a literal transla…

다음: Episode 1 voice draft (2026-06-22). On voice approval, adapt Episodes 2-7 then run shared continuity check (EN vs 031 KO)

#### [QFUDS SAGA origin(1.5부) 사엘 풀길이 소설 (한국어 primary)](20_drafts/1.5부/033_origin_sael_full_novel_korean_primary.md)
`draft` · 2026-06-23 · reference

> 이 문서는 1.5부 origin의 **풀길이 소설본**이다. [031 콘티 텔링](031_origin_sael_webnovel_storyboard_ko.md)을 뼈대(리텐션 통과한 설계도)로, [030 프로토타입](030_origin_arc_sael_korean_primary.md)을 참고로 삼아, 세계가 **설명이 아니라 체험으로 도착하도록** 분량을 제대로 준다. 031의 이해 우선 온보딩은 유지하되, 각 비트를 여러 장면의 챕터로 펼친다. 캐논은 016/017/030에서 상속하고 새 설정을…

다음: 1장(B1) 풀길이 draft(2026-06-22). 결 승인 후 2~8장 집필, retention+comprehension 게이트

#### [QFUDS SAGA 1부 「오르페우스」 풀길이 소설 (한국어 primary)](20_drafts/1부/035_orpheus_full_novel_korean_primary.md)
`draft` · 2026-06-30 · reference

> 이 문서는 새 1부 **「오르페우스」**의 풀길이 소설본이다. 현 1부(사엘)는 1.5부로 내리고, 그 자리에 **세계를 설명 전에 느끼게 하는 인간 입구**를 둔다. 설계는 [10_story_design/024 오르페우스 설계](../../10_story_design/024_new_book1_orpheus_design_ko.md), 세계 여파는 [00_bible/026 Q-Day 여파](../../../../10_world/026_qday_aftermath_timeline_and_world_ko…

다음: 1장 draft(2026-06-30). 보이스 승인 후 2~8장 집필 + 과학 부록

#### [QFUDS SAGA 1부 Book 1 Reboot Korean Primary](20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md)
`draft` · 2026-06-22 · reference

> 번호 physical cascade 완료(011 §10, 2026-06-21). 이 원고는 신규 구조의 **2부 Mara 자산**이며, 물리 경로도 이제 `20_drafts/2부/`다. **1.5부 사엘 origin**은 [030 origin Sael draft](../1.5부/030_origin_arc_sael_korean_primary.md)가 담당한다 (2026-06-30에 1부→1.5부 강등; 새 1부는 「오르페우스」 035).

다음: run review/chronicler pass for completed Ch6; this manuscript is canonical 2부 Mara asset under 011 §10

#### [QFUDS SAGA 2부 마라 풀길이 소설 (한국어 primary)](20_drafts/2부/034_mara_full_novel_korean_primary.md)
`draft` · 2026-06-22 · reference

> 이 문서는 2부 마라의 **풀길이 소설본**이다. [029 2부 reboot](029_first_arc_book1_reboot_korean_primary.md)을 캐논 원천(프롤로그~Ch6)으로, [033 1.5부 사엘 origin 풀길이](../1.5부/033_origin_sael_full_novel_korean_primary.md)의 보이스와 결을 모델로 삼아, 세계가 **설명이 아니라 체험으로 도착하도록** 분량을 제대로 준다. 029의 이해 우선 온보딩은 유지하되, 각 비트를 여러 장면의…

다음: 1장(풀길이) draft(2026-06-22). 결 승인 후 2~6장 집필, retention+comprehension 게이트

#### [QFUDS SAGA Exhibit S-0 Episode 1 Revised V2 English Draft](20_drafts/2부/_versions/1부_prototype/012_exhibit_s0_episode1_revised_v2_english_draft.md)
`draft` · 2026-06-20 · reference

> This document is fiction draft material.

다음: revise episodes 3-4 after user review

#### [QFUDS SAGA The Dead Exchange Revised V2 English Draft](20_drafts/2부/_versions/1부_prototype/013_the_dead_exchange_revised_v2_english_draft.md)
`draft` · 2026-06-20 · reference

> This document is fiction draft material.

다음: revise episodes 3-4 after user review

#### [QFUDS SAGA The Last Hodler Revised V2 English Draft](20_drafts/2부/_versions/1부_prototype/014_the_last_hodler_revised_v2_english_draft.md)
`draft` · 2026-06-20 · reference

> This document is fiction draft material.

다음: revise episodes 5-6 after user review

#### [QFUDS SAGA Identity Flood Revised V2 English Draft](20_drafts/2부/_versions/1부_prototype/015_identity_flood_revised_v2_english_draft.md)
`draft` · 2026-06-20 · reference

> This document is fiction draft material.

다음: revise episodes 5-6 after user review

#### [QFUDS SAGA Hawking Court Revised V2 English Draft](20_drafts/2부/_versions/1부_prototype/016_hawking_court_revised_v2_english_draft.md)
`draft` · 2026-06-20 · reference

> This document is fiction draft material.

다음: first arc polish or arc two planning after user review

#### [QFUDS SAGA The Broken Crown Revised V2 English Draft](20_drafts/2부/_versions/1부_prototype/017_the_broken_crown_revised_v2_english_draft.md)
`draft` · 2026-06-20 · reference

> This document is fiction draft material.

다음: first arc polish or arc two planning after user review

#### [QFUDS SAGA Exhibit S-0 Episode 1 Revised V2 Korean Adaptation](20_drafts/2부/_versions/1부_prototype/019_exhibit_s0_episode1_revised_v2_korean_adaptation.md)
`draft` · 2026-06-21 · reference

> This document is fiction draft material.

다음: read episode 2 Korean adaptation

#### [QFUDS SAGA The Dead Exchange Revised V2 Korean Adaptation](20_drafts/2부/_versions/1부_prototype/020_the_dead_exchange_revised_v2_korean_adaptation.md)
`draft` · 2026-06-21 · reference

> This document is fiction draft material.

다음: read episode 3 Korean adaptation

#### [QFUDS SAGA The Last Hodler Revised V2 Korean Adaptation](20_drafts/2부/_versions/1부_prototype/021_the_last_hodler_revised_v2_korean_adaptation.md)
`draft` · 2026-06-21 · reference

> This document is fiction draft material.

다음: read episode 4 Korean adaptation

#### [QFUDS SAGA Identity Flood Revised V2 Korean Adaptation](20_drafts/2부/_versions/1부_prototype/022_identity_flood_revised_v2_korean_adaptation.md)
`draft` · 2026-06-21 · reference

> This document is fiction draft material.

다음: read episode 5 Korean adaptation

#### [QFUDS SAGA Hawking Court Revised V2 Korean Adaptation](20_drafts/2부/_versions/1부_prototype/023_hawking_court_revised_v2_korean_adaptation.md)
`draft` · 2026-06-21 · reference

> This document is fiction draft material.

다음: read episode 6 Korean adaptation

#### [QFUDS SAGA The Broken Crown Revised V2 Korean Adaptation](20_drafts/2부/_versions/1부_prototype/024_the_broken_crown_revised_v2_korean_adaptation.md)
`draft` · 2026-06-21 · reference

> This document is fiction draft material.

다음: arc two planning around who may author loss

#### [QFUDS SAGA 1부 여는 사건 The Broken Crown](20_drafts/2부/_versions/1부_prototype/028_first_arc_opening_broken_crown_event_korean_primary.md)
`draft` · 2026-06-21 · reference

> fiction/provenance only. QFUDS 연구 증거 아님. 세계 사실은 bible 010이, 반전 배치는 story_design 008이 보유한다. 이 문서는 그 빅이벤트를 독자에게 처음 보여주는 극화된 오프닝 초안이다. 기술·역사 내용(비트코인 제네시스·딥페이크 시대·Shor/ECDSA·정보 보존)은 [009 §2.5 검증 출처 대장](../../../../../../10_world/009_reader_accessibility_and_real_world_anchors_ko.md)에…

다음: user approves direction; then renumber arc (this becomes ep1, Exhibit S-0 becomes ep2) and propagate

#### [QFUDS SAGA Exhibit S-0 Episode 1 Revised V2 Korean Adaptation](20_drafts/2부/_versions/1부_v3_pre_R4/019_exhibit_s0_episode1_revised_v2_korean_adaptation.md)
`draft` · 2026-06-21 · reference

> This document is fiction draft material.

다음: read episode 2 Korean adaptation

#### [QFUDS SAGA The Dead Exchange Revised V2 Korean Adaptation](20_drafts/2부/_versions/1부_v3_pre_R4/020_the_dead_exchange_revised_v2_korean_adaptation.md)
`draft` · 2026-06-21 · reference

> This document is fiction draft material.

다음: read episode 3 Korean adaptation

#### [QFUDS SAGA The Last Hodler Revised V2 Korean Adaptation](20_drafts/2부/_versions/1부_v3_pre_R4/021_the_last_hodler_revised_v2_korean_adaptation.md)
`draft` · 2026-06-21 · reference

> This document is fiction draft material.

다음: read episode 4 Korean adaptation

#### [QFUDS SAGA Identity Flood Revised V2 Korean Adaptation](20_drafts/2부/_versions/1부_v3_pre_R4/022_identity_flood_revised_v2_korean_adaptation.md)
`draft` · 2026-06-21 · reference

> This document is fiction draft material.

다음: read episode 5 Korean adaptation

#### [QFUDS SAGA Hawking Court Revised V2 Korean Adaptation](20_drafts/2부/_versions/1부_v3_pre_R4/023_hawking_court_revised_v2_korean_adaptation.md)
`draft` · 2026-06-21 · reference

> This document is fiction draft material.

다음: read episode 6 Korean adaptation

#### [QFUDS SAGA The Broken Crown Revised V2 Korean Adaptation](20_drafts/2부/_versions/1부_v3_pre_R4/024_the_broken_crown_revised_v2_korean_adaptation.md)
`draft` · 2026-06-21 · reference

> This document is fiction draft material.

다음: arc two planning around who may author loss

#### [QFUDS SAGA Who May Author Loss Korean Primary](20_drafts/3부/025_who_may_author_loss_korean_primary.md)
`draft` · 2026-06-20 · reference

> 이 문서는 한국어 primary fiction draft다.

다음: write English counterpart (026) then advance to next KR primary 027 (who may refuse)

#### [QFUDS SAGA Who May Author Loss English Counterpart](20_drafts/3부/026_who_may_author_loss_english_counterpart.md)
`draft` · 2026-06-20 · reference

> This document is fiction draft material.

다음: this is EN counterpart (026) of KR primary 025; next KR primary is 027 (who may refuse)

#### [QFUDS SAGA Who May Refuse Korean Primary](20_drafts/3부/027_who_may_refuse_korean_primary.md)
`draft` · 2026-06-20 · reference

> 이 문서는 한국어 primary fiction draft다.

다음: decide English Anglophone counterpart or episode 028 Korean primary

### `10_story_design` — 아이디어·아웃라인·arc 지도·씬카드 (확정 전 설계)

#### [QFUDS SAGA 시각 전시물 설계](10_story_design/002_visual_exhibit_design_ko.md)
`draft` · 2026-06-20 · guide

> 이 문서는 fiction-system 설계 노트다.

다음: decide whether one visual exhibit enters the next prose revision

#### [QFUDS SAGA Arc Two Korean-Primary Plan](10_story_design/007_arc_two_korean_primary_plan_ko.md)
`draft` · 2026-06-21 · guide

> 이 문서는 `The Broken Crown` 1부 이후 바로 새 prose로 들어가기 위한 최소 Arc Two 설계다. 전체 시즌을 과하게 닫지 않고, 다음 한국어 primary 장면이 흔들리지 않을 정도만 정한다.

다음: 025/027 Korean primary + 026 English counterpart written; next write 027 English counterpart or 028 Korean primary

#### [QFUDS SAGA Last Archive 반전 설계와 떡밥 배치](10_story_design/008_last_archive_reveal_architecture_ko.md)
`draft` · 2026-07-01 · guide

> 옵션 3(= Last Archive는 진짜 지성이 아니라 "합의의 신격화", SSOT는 없다)을

다음: thread Act-1 deception + planted clues into prologue and first arc

#### [QFUDS SAGA 형식·시리즈 throughline·현재 진행 상태](10_story_design/009_format_throughline_and_progress_ko.md)
`draft` · 2026-07-02 · guide

> "단편인가 장편인가", "시리즈를 관통하는 드라마가 뭔가", "지금 어디까지 왔나"를 고정한다.

다음: build Liora protagonist sheet, then propagate foundation into first arc

#### [QFUDS SAGA 2부 에피소드 맵](10_story_design/010_arc_two_episode_map_ko.md)
`draft` · 2026-06-21 · guide

> 2부(`who may author loss`)를 에피소드 단위로 배치한다. ep1·ep2는 작성·감사 완료 상태이고, ep3-ep6은 **제안(proposed)**이다 — momentum으로 canon 고정하지 않으며 작가 승인 후 확정한다. 실행 계약은 [2부 GSD Phase Brief](../00_workroom/004_arc_two_gsd_phase_brief_ko.md).

다음: user approves arc length + ep3-6 direction, then write 028 Korean primary

#### [QFUDS SAGA 다부작 아크 지도](10_story_design/011_saga_arc_map_multiarc_ko.md)
`draft` · 2026-07-01 · guide

> 이 문서는 QFUDS SAGA의 **상위 아크 실행 계획서**다. 주제 SSOT는 [015 5대 극적 질문 스파인](015_five_core_dramatic_questions_spine_ko.md)이 보유하고, 이 문서는 그 위에 부(arc) 골격을 얹어 "무엇을 어느 부에서 심고 터뜨리고 회수하는가" 를 배치한다. 정밀 아웃라인이며 소설 산문이 아니다.

다음: 1부 POV(사엘 능동화 vs 새 POV)를 작가가 확정하면 1부 origin 아웃라인을 별도 문서로 분기한다

#### [QFUDS SAGA 1부 Book 1 백지 재설계 통합 아웃라인](10_story_design/012_first_arc_book1_outline_reboot_ko.md)
`completed` · 2026-06-21 · guide

> 이 문서는 1부를 새 prose로 쓰기 전의 **통합 outline SSOT**다. 기존 beat 문서 004·005·006·008·009·011과 bible 009·010·017·018·019·020을 합친다. 원고는 백지에서 다시 쓰되, grounding은 버리지 않는다.

다음: draft 20_drafts/029 first-arc Book 1 Korean-primary reboot manuscript

#### [QFUDS SAGA 1부 Book 1 씬 카드](10_story_design/013_first_arc_scene_cards_ko.md)
`completed` · 2026-06-21 · guide

> 이 문서는 1부를 백지에서 다시 쓰기 전의 scene-card gate다. 산문 초안이 아니다. 장면마다 `POV`, `want`, `obstacle`, `turn`, `cost`, `technical terms exposed`,

다음: draft 20_drafts/029 first-arc Book 1 Korean-primary reboot manuscript from this scene-card gate

#### [QFUDS SAGA 소버린 AI·오픈/봉쇄 축 브레인스토밍](10_story_design/014_sovereign_ai_open_closed_axis_brainstorm_ko.md)
`draft` · 2026-06-21 · guide

> 가둘 것인가"**(오픈소스 vs 폐쇄·수출 통제)를 작품 축으로 끌어온 brainstorm이다. 파이프라인상 아직 brainstorm이며, 선택된 씨앗만 `00_bible`로 승격한다.

다음: select seeds to promote into 00_bible (factions/SSOT) and 1부/2부 prose pressure

#### [QFUDS SAGA 5대 극적 질문 스파인](10_story_design/015_five_core_dramatic_questions_spine_ko.md)
`draft` · 2026-07-01 · guide

> origin=1부 / Mara=2부 재구조화에 앞서, **사가 전체가 답해 가는 5개 극적 질문**을 한 장에 고정한다. 아크 번호가 어떻게 밀리든 이 5개는 안 흔들린다. 새 설정을 만들지 않고 기존 캐논([022 기준 작성권](../00_bible/022_authorship_of_the_standard_theme_axis_ko.md) 중심 + [021](../../../10_world/021_restoration_mechanism_correction_ko.md)·[020](../../../10…

다음: rebuild the multiarc map (011) and outlines on top of this spine (origin=1부 / Mara=2부)

#### [QFUDS SAGA 1부 origin 아웃라인](10_story_design/016_first_arc_origin_outline_ko.md)
`draft` · 2026-07-01 · guide

> 1부(origin) 실행 아웃라인이다. 주제 SSOT는 [015 5대 극적 질문 스파인](015_five_core_dramatic_questions_spine_ko.md), 부 배치는 [011 아크 맵](011_saga_arc_map_multiarc_ko.md), origin 역사 사실은 [bible 013 PART A(Hinge Era)](../../../10_world/013_cryptographic_death_era_and_crypto_concepts_ko.md)· [017 §1](../..…

다음: 작가가 사엘 원죄 형태(§4)와 콜드오픈(§5)을 승인하면 1부 비트를 scene-card로 분기

#### [QFUDS SAGA 1부 origin 씬 카드](10_story_design/017_first_arc_origin_scene_cards_ko.md)
`draft` · 2026-06-21 · guide

> [016 origin 아웃라인](016_first_arc_origin_outline_ko.md)의 B1-B7을 씬 카드 초안으로 분기한다. 산문이 아니다. 각 카드가 아래 10칸을 못 채우면 원고로 넘어가지 않는다.

다음: 작가가 카드를 승인하면 011 §10 번호 cascade 후 1부 origin 원고로 들어간다

#### [QFUDS SAGA 암호 개념 독자 온보딩 점검](10_story_design/018_crypto_concepts_reader_onboarding_check_ko.md)
`draft` · 2026-07-01 · guide

> 이 문서는 1부 origin 원고 진입 전, 비트코인·블록체인·암호 개념이 일반 독자에게 장면 압력으로 전달되는지 점검한다. 원고 산문이 아니며 새 설정을 만들지 않는다.

다음: revise B1-B7 cards only if this check finds a release-blocking onboarding gap

#### [QFUDS SAGA 사엘 원고 실행 시트](10_story_design/019_sael_origin_execution_sheet_ko.md)
`draft` · 2026-06-21 · guide

> 이건 **캐릭터 만들기가 아니라 원고 실행 계약서**다. [character_sheet_template](../../../../../../../../.agent/templates/fiction/character_sheet_template.md) 구조를 쓰되 **최소만** 채운다. 사엘은 멋있는 주인공이 아니라 **선택 비용이 분명한 원죄 참여자**로 고정한다.

다음: 사엘 시트 승인 후 017 B1 reader-onboarding 보강 → 1부 origin 원고 진입

#### [QFUDS SAGA Q-Day 사건 사슬 bridge 아웃라인 (B1↔B2)](10_story_design/020_qday_incident_bridge_outline_ko.md)
`draft` · 2026-06-21 · guide

> B1 prose(030)와 B2 scene-card(017) 사이의 **사건 사슬**을 1장으로 고정한다. 산문이 아니다. "Q-Day 직후 세계가 어떻게 반응했고, 도난/해킹처럼 보이던 사건이 어떻게 검증 요청으로 전환되어 Aletheia/사엘에게 도달하는가"의 사건 순서·원인 오인·제도 대응을 정리한다. 이걸 안 잡고 산문을 만지면 "그래서 누가 훔쳤나 / 정부는 뭐 하나 / 사엘 파일은 왜 생기나"로 계속 되돌아온다.

다음: bridge 승인 후 B1 종착점 정합 확인 → B2(검증 요청) 산문 진입

#### [QFUDS SAGA 1부 독자 정보 공개 사다리 (reader reveal ladder)](10_story_design/021_first_arc_reader_reveal_ladder_ko.md)
`draft` · 2026-06-21 · guide

> 작가/에이전트가 이미 아는 캐논이 아니라, **독자가 실제로 읽으며 따라가는 정보 순서**를 설계한다. B1-B7이 각각 어떤 질문을 만들고, 무엇에 답하고, 무엇을 뒤로 넘기는지 정리해 산문에서 **과설명·과은폐·과밀**을 막는다.

다음: ladder 승인 후 B1을 "첫 균열 + 파일 handoff"로 압축 재배치 → B2 진입

#### [QFUDS SAGA 1부 통합 causal master outline](10_story_design/022_first_arc_causal_master_outline_ko.md)
`draft` · 2026-06-21 · guide

> 016(outline)·017(scene cards)·020(Q-Day bridge)·021(reveal ladder)에 흩어진 결정을

다음: master outline 승인 → B1 압축(030↔카드 정렬) → B2 산문 진입

#### [QFUDS SAGA 세계관·인물 한눈에 (독자·작가 오리엔테이션)](10_story_design/023_first_arc_reader_orientation_world_and_cast_ko.md)
`draft` · 2026-07-02 · guide

> 이 문서는 "이게 대체 무슨 이야기냐"를 **가장 쉬운 말로** 한 장에 정리한 것이다. 캐논을 새로 만들지 않는다. 016/015/005 등 기존 설정에서 상속해 평이하게 옮긴 것뿐이다. 원고가 어려울 때 작가·독자가 돌아와 방향을 잡는 용도다.

다음: 게이트 comprehension 테스트와 함께 사용. 원고가 이 오리엔테이션을 본문 안에서 전달하는지 점검

#### [새 1부 「오르페우스」 설계 — 사별·복원 사본·돌아봄](10_story_design/024_new_book1_orpheus_design_ko.md)
`draft` · 2026-06-30 · guide

> 현 1부(033 사엘)를 **1.5부**(제도 기원 interlude)로 내리고, 그 자리에 **인간 입구**가 되는 새 1부를 둔다. 세계를 *설명*하기 전에 *느끼게* 한다.

다음: 사용자 검토 후 1.5부 강등 정리 + 8챕터 초고 착수. 신규 주인공 024 캐논 등록

#### [사가 방향 전환 — 근미래 grounded SF로 무게중심 이동](10_story_design/025_near_future_recenter_direction_ko.md)
`draft` · 2026-07-01 · guide

> 2026-06-30 사용자 결정. 사가의 무게중심을 **먼 미래 오페라(4기 연속성 법원 등)에서 근미래 grounded SF(2026-2040s)로 당긴다.** 기존 캐논을 버리지 않되, 중심을 옮긴다.

다음: 0부 착수(근미래 grounded). 기존 024 timeline·011 arc map·026은 점진적으로 이 방향에 맞춰 재조정

#### [기계 화자 보이스·복선·시대건너뛰기 구조 트리트먼트 (서사·보이스 렌즈)](10_story_design/026_machine_narrator_voice_and_setup_payoff_treatment_ko.md)
`draft` · 2026-07-01 · guide

> 이 문서는 7인 패널 중 **서사·보이스 작가 렌즈**의 산출물이다. 027(기계의 회고, 사실 앵커 연표)이

다음: 0부 프롤로그층 착수. 화자 문법·복선 회수 지도를 draft 집필의 연출 SSOT로 사용. 사실 앵커는 027이 우선

#### [QFUDS SAGA 근미래 프렐류드 대사전 (2020s-2090s 예측, candidate)](10_story_design/027_near_future_prelude_forecast_ko.md)
`draft` · 2026-07-02 · guide

> 002 §2·011·026이 이름만 두고 비워 둔 **2020s-2090s "지수 성장기" 활주로**를, 근미래 예측 패널([workroom 012](../00_workroom/012_near_future_forecast_panel_method_ko.md))로 채운 대사전이다. 15개 전문가 렌즈가 오늘의 실제 앵커에서 2020s→2090s를 예측·생성하고, 교차압력 합성·캐논가드·현실성·인간욕망 검증을 거쳐 다층 타임라인(굵직/중요/국지/나비효과)과 신규 조직·인물·대립구도로 엮었다. 0부(20…

다음: 0부 앞 근미래 활주로 candidate 대사전. 캐논 승격은 원고 수요 때 030 §7 6체크. 026 Q-Day로 연결

#### [QFUDS SAGA 레지스터 전환 오프닝(판타지→하드SF)과 결말 옵션 (candidate/brainstorm)](10_story_design/028_register_morph_opening_and_ending_options_ko.md)
`draft` · 2026-07-01 · guide

> 작가 발상: "세계를 **빅뱅부터 판타지소설처럼** 소개했다가, 인과가 과학적으로 맞물리는

다음: 결말은 미정(옵션만). 선택된 방향만 011 아크 지도·024 좌표로 승격. 오프닝 장치는 008 반전과 동기화

### `00_bible` — 확정된 세계 사실·인물·제도·과학 경계 (설정 기준서)

#### [QFUDS SAGA 시점 주제 고유명사 규칙](00_bible/004_narrative_pov_theme_naming_ko.md)
`draft` · 2026-07-02 · guide

> 이 문서는 시점, 중심 주제, 고유명사 체계, 역사 차용 규칙의 active 기본값을 고정한다. 세력 formal name은 [015](../../../10_world/015_factions_canon_naming_ko.md)가 우선한다.

다음: apply as active POV/theme/naming defaults; 015 overrides faction formal names

#### [QFUDS SAGA 첫 Arc Canon 정리](00_bible/008_first_arc_canon_consolidation_ko.md)
`draft` · 2026-07-01 · guide

**주의 — 리센터 이전 라벨 포함:** 이 문서 본문은 옛 부 번호를 담을 수 있다. 현행 매핑은 024·025·027 SSOT가 우선.

> 이 문서는 `The Broken Crown` first arc rough draft 6개에서 새로 생긴 설정, 인물 기능, 제도 규칙, 미해결 hook을 series bible 관점으로 정리한 bridge다. 현행 독자 경로는 028 opening + 019-024 한국어 primary story order다.

다음: align R6 first-arc rewrite with 028 + 019-024 story order

#### [QFUDS SAGA 주인공 시트 — Liora Sen](00_bible/012_character_liora_sen_ko.md)
`draft` · 2026-07-01 · guide

**주의 — 리센터 이전 라벨 포함:** 이 문서 본문은 옛 부 번호를 담을 수 있다. 현행 매핑은 024·025·027 SSOT가 우선.

> [캐릭터 시트 템플릿](../../../../../../../../.agent/templates/fiction/character_sheet_template.md)을 Liora에 적용. fiction/provenance only. 새 외부 source claim 없음.

다음: thread Liora's wound/lie into first-arc R6 and keep 019 in close POV

#### [QFUDS SAGA 작가 사유 렌즈 — 압축·SSOT·동기화 + Soft Editing 텍스처](00_bible/014_authorial_lenses_compression_ssot_soft_editing_ko.md)
`draft` · 2026-06-20 · guide

> Soft Editing 댓글 전쟁)에서 세계관에 박을 렌즈를 모은다. 작가의 사유 자산이자 이 작품의 사상적 지문.

다음: apply compression lens to restoration scenes; soft-editing texture to Exhibit S-0

#### [QFUDS SAGA 앙상블 캐릭터 보이스·관계 바이블](00_bible/016_character_ensemble_voices_relationships_ko.md)
`draft` · 2026-07-01 · guide

**주의 — 리센터 이전 라벨 포함:** 이 문서 본문은 옛 부 번호를 담을 수 있다. 현행 매핑은 024·025·027 SSOT가 우선.

> 리텐션 테스트에서 독자들이 "모든 인물이 같은 한 명(작가)처럼 말한다"고 지적했다. 원인은 인물별 **목소리·배경·욕망**이 따로 설계되지 않아 대사가 전부 같은 격언 핑퐁으로 균질화된 것. 이 문서가 각 인물을 **대사 태그 없이도 누가 말하는지 알 수 있게** 차별화한다. Liora 상세는 [012 Liora 시트](012_character_liora_sen_ko.md)가 보유하고, 이 문서는 앙상블 전체의 보이스·관계를 잡는다.

다음: differentiate dialogue per this sheet across 1부 (R2 voice pass)

#### [QFUDS SAGA 입체 캐릭터 시트](00_bible/019_character_depth_sheets_ko.md)
`draft` · 2026-07-01 · guide

**주의 — 리센터 이전 라벨 포함:** 이 문서 본문은 옛 부 번호를 담을 수 있다. 현행 매핑은 024·025·027 SSOT가 우선.

> [012 Liora 시트](012_character_liora_sen_ko.md)는 주인공 한 명을, [016 앙상블 바이블](016_character_ensemble_voices_relationships_ko.md)은 전원의 보이스·관계 지도를, [010 기원](../../../10_world/010_last_archive_origin_and_reversal_causality_ko.md)은 Karvath·Vera의 출생과 Vera-Mara 거울을 보유한다. 이 문서는 그 셋이 이미 가진 설정을…

다음: thread each arc turn into 1부 R6 beat sheets and prose

#### [QFUDS SAGA 기준 작성권 사상축](00_bible/022_authorship_of_the_standard_theme_axis_ko.md)
`draft` · 2026-06-21 · guide

> 이고, 일반화하면 "누가 현실의 기준(진실·가치·정상·복원 자격)을 쓰는가 = 권력"이다. 이 문서는 작가의 사유에서 나온 사상축을 작품 캐논으로 고정한다.

다음: thread authorship-of-the-standard + Exit/Voice + half-right antagonists into prose

#### [QFUDS SAGA 이념 비일관성 삼각 (세 양립 불가 신앙)](00_bible/023_ideological_incoherence_triad_ko.md)
`draft` · 2026-07-02 · guide

> 이 문서는 복원 문명이 **왜** 그렇게 굴러갔는지의 척추 하나를 적어 둔다. 세 가지 믿음이 동시에 인기를 끌었는데, 그 셋은 서로 양립할 수 없었다. 사람들은 그 모순을 외면한 채 셋을 한꺼번에 들었고, 그 비일관성이 검증 제국·복원 국가·깨진 화폐를 동시에 키웠다. **단, 이 삼각의 뿌리는 이념이 아니라 욕망이다**(아래 §뿌리). 신앙은 겉이고 욕망이 속이다. 1부·2부 프로즈가 "이 세계가 왜 이런가"를 인물 장면으로 깔 때의 근거이며, 강의가 아니라 *원하는 인물*로 보여 준다.

다음: thread the incoherent-triad as in-world texture into 1·2부 prose; do not lecture

#### [QFUDS SAGA 캐릭터 지도와 타임라인 좌표](00_bible/024_character_map_and_timeline_coordinates_ko.md)
`draft` · 2026-07-02 · guide

> 이 문서는 인물 캐논(012 Liora / 016 앙상블 / 019 입체 시트)을 **시대 좌표 위에** 한 장으로 모은 지도다. 새 인물을 만들지 않는다. 충돌·미정은 지어내지 않고 '결정 필요'로 표기한다. authoring baseline: 2026-06-30. fiction/provenance only, QFUDS 연구 증거 아님.

다음: 빈 구간(28세기→첫 복원) 보강과 사건×인물 연결의 백본으로 사용. 미정 항목은 chronicler pass로 확정

#### [기계의 회고 - 실제 AI 발전사를 사가 서두 관통선으로](00_bible/027_machine_childhood_ai_history_narrator_throughline_ko.md)
`draft` · 2026-07-01 · guide

> fiction/provenance only research evidence: no external source claim: 실명 차용(OpenAI·Anthropic·Google·Nvidia·C2PA·SynthID·grief-tech 등)은 핍진성용 worldbuilding이며 실제 예측·정치 주장 아님. 현직 정치인 실명·당파 고정 없음. 비판은 문화·자본·게이팅 "구조"로만. §7 일부 항목은 사실 앵커의 개연적 외삽(사실 아님)임을 명시. workflow: Fiction IP Managemen…

다음: 서두 프롤로그층(0부 진입 이전) 착수. 각 노드 사실 앵커는 §7 웹확인 기준, 화자 문장은 초고

### `30_revisions` — 출간용 교정·게이트 기록

#### [QFUDS SAGA 1부 De-jargon·Polish 퇴고 계획](30_revisions/001_first_arc_dejargon_polish_revision_plan_ko.md)
`draft` · 2026-07-01 · guide

> 이 문서는 release-facing 퇴고 통제 문서다. fiction/provenance only. QFUDS 연구 결과·물리 증거·support·validation 아님. 새 외부 source claim 없음. workflow state: `not searched`.

다음: apply to 019-024, then audit with naturalness/content-fidelity agents

#### [QFUDS SAGA 1부 Release 승격 — 현장감·묘사 강화 퇴고 기준](30_revisions/002_first_arc_release_immersion_revision_plan_ko.md)
`draft` · 2026-06-30 · guide

> 이 문서는 원래 1부 한국어 prototype 6편 ([019](../20_drafts/2부/_versions/1부_prototype/019_exhibit_s0_episode1_revised_v2_korean_adaptation.md)-[024](../20_drafts/2부/_versions/1부_prototype/024_the_broken_crown_revised_v2_korean_adaptation.md))을

다음: apply these release gates to 030 origin draft after B1-B7 and cascade stabilize

#### [QFUDS SAGA 1부 전역 템플릿 커버리지 감사](30_revisions/003_first_arc_template_coverage_audit_ko.md)
`completed` · 2026-07-01 · summary

> 사용자 요청에 따라 1부 관련 bible / harness / release 시스템이

다음: apply template coverage checks to 029 first-arc reboot manuscript as chapters are drafted

#### [QFUDS SAGA 1부 편별 통합 아웃라인](30_revisions/007_first_arc_integration_outline_ko.md)
`provenance` · 2026-07-01 · guide

> 1부(프롤로그 028 + 6편 019-024)를 **편별 정밀 통합 스펙**으로 묶었던 provenance 문서다. 이것은 소설 산문이 아니라 설계 스펙이며, 현재 active first-arc 경로는 [016 origin 아웃라인](../10_story_design/016_first_arc_origin_outline_ko.md), [017 origin scene cards](../10_story_design/017_first_arc_origin_scene_cards_ko.md), [030 ori…

다음: superseded by 016 origin outline, 017 scene cards, 030 origin draft, and 011 §10 cascade ledger

#### [QFUDS SAGA Series Bible Drift Alignment Audit](30_revisions/008_series_bible_drift_alignment_audit_ko.md)
`completed` · 2026-06-21 · summary

> 001-020 bible 전체를 훑어 active canon drift를 정리했다. 이 문서는 fiction/provenance audit이며 QFUDS 연구 증거, Bitcoin 투자 판단, 암호·물리 조언이 아니다.

다음: apply this alignment before first-arc R6 rewrite

#### [QFUDS SAGA 1부·2부 독자 피드백 + AI-tell 통합 정리 및 개선 계획](30_revisions/009_first_arc_reader_feedback_and_ai_tell_consolidation_ko.md)
`draft` · 2026-06-30 · guide

> 이 문서는 사엘 origin([030](../20_drafts/1.5부/030_origin_arc_sael_korean_primary.md), 2026-06-30 1부→1.5부 강등)과 2부 Mara([029](../20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md))에 대해 실행한 reader-persona 이탈 테스트와 `ai-tell-detector` 패스 결과를 **페르소나별로** 통합하고, 그 피드백을 반영한 윤문·퇴고 개선 계획과 적…

다음: 029 윤문 패스 적용 후 재검증, release 승격 시 정식 9-persona retention 게이트

#### [QFUDS SAGA 1부·2부 release-facing revision wave](30_revisions/010_first_second_arc_release_revision_wave_ko.md)
`draft` · 2026-06-30 · guide

> 이 문서는 사엘 origin([030](../20_drafts/1.5부/030_origin_arc_sael_korean_primary.md), 2026-06-30 1부→1.5부 강등)과 2부 Mara([029](../20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md))에 대한 release-facing 전 단계 수정 파동이다. 원고 source는 `20_drafts/`이고, 이 문서는 수정 이유와 잔여 위험을 남기는 revision 기록이다.

다음: run staged fiction gate and keep release promotion blocked until formal 9-persona retention gate

#### [QFUDS SAGA 1부·2부 정식 reader retention gate protocol](30_revisions/011_first_second_arc_formal_retention_gate_protocol_ko.md)
`draft` · 2026-06-30 · guide

> 이 문서는 사엘 origin([030](../20_drafts/1.5부/030_origin_arc_sael_korean_primary.md), 2026-06-30 1부→1.5부 강등; 아래 baseline-pinned 소스 경로는 당시 커밋 기준이라 그대로 둠)과 2부 Mara([029](../20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md))를

다음: create 012 retention gate run artifact with doc_type gate before any 40_release promotion

#### [031 origin 웹소설 콘티 텔링 Retention Gate Run 2026-06-22 1308777](30_revisions/012_origin_sael_webnovel_retention_gate_run_20260622_1308777_ko.md)
`completed` · 2026-06-22 · gate

> 이 문서는 baseline 1308777에 대한 고정 run 아티팩트다. 원고가 바뀌면 덮어쓰지 않고 새 baseline으로 새 run 문서를 만든다. 그때 이 문서를 `depends_on`에 적는다.

다음: 차기 revision wave에서 S1(RET-001~003) 처리 후 새 baseline으로 재실행. release 승격 전 ran_passed 권장

#### [031 origin 웹소설 콘티 텔링 Retention Gate Run 2 2026-06-22 bdff1c7](30_revisions/013_origin_sael_webnovel_retention_gate_run_20260622_bdff1c7_ko.md)
`completed` · 2026-06-22 · gate

> 이 문서는 baseline bdff1c7 고정 run이다. 1차 run([012])을 `depends_on`에 적었다. 이후 polish로 원고가 바뀌면 새 baseline 새 run 문서를 만든다.

다음: 잔류 S2(RET-008 반전 정형, RET-010 U7 콘티/산문 중복) polish 후 release 추진 시 최종 확인 재실행

#### [031 origin 웹소설 콘티 텔링 Retention Gate Run 3 (confirm) 2026-06-22 b5f0edf](30_revisions/014_origin_sael_webnovel_retention_gate_run_20260622_b5f0edf_ko.md)
`completed` · 2026-06-22 · gate

> baseline b5f0edf 고정 run. 2차 run([013])을 `depends_on`에 적었다.

다음: ran_passed. 잔여 S2 backlog는 release-facing 최종 윤문에서 선택 처리. 다음 단계는 영어 Anglophone 각색판 + shared continuity check

#### [033 origin 풀길이 소설 Retention + Comprehension Gate 2026-06-22 c91e9be](30_revisions/015_origin_sael_fullnovel_retention_comprehension_gate_20260622_c91e9be_ko.md)
`completed` · 2026-06-22 · gate

> fiction/provenance only research evidence: no release promotion without this artifact: no raw private reasoning: do not record

다음: 잔여 S1(중반 반복)·S2(거푸집) polish 후 release 추진 시 재실행. 다음 작업=2부 풀길이 또는 영어 각색

#### [034 2부 마라 풀길이 소설 Retention + Comprehension Gate 2026-06-23 a41bcb9](30_revisions/016_mara_fullnovel_retention_comprehension_gate_20260623_a41bcb9_ko.md)
`completed` · 2026-06-30 · gate

> fiction/provenance only research evidence: no release promotion without this artifact: no raw private reasoning: do not record

다음: 거푸집 후렴(S1)·6장 물리댐/길이·QFUDS 한 줄 설명 polish 후 release 추진 시 재실행. 또는 3부

#### [034 2부 마라 — '순서' 토템 + 두 읽기 복선 설계 (B-i)](30_revisions/017_mara_order_totem_two_readings_seed_design_ko.md)
`draft` · 2026-06-30 · guide

> fiction/provenance only research evidence: no in-world 형이상학(it-from-bit 풍미): 소설 내부 논리일 뿐, QFUDS 연구 주장 아님 workflow state: not searched (외부 문헌 미인용; 사용자 브레인스토밍 발원의 픽션 전제)

다음: 사용자 검토 후 034 본문에 씨앗 5곳 + 6장 정산 반영. 이후 RET-2B-001/002 polish

#### [QFUDS SAGA 전문서 정합 감사 (2026-07-01)](30_revisions/018_saga_consistency_audit_2026_07_01_ko.md)
`draft` · 2026-07-01 · guide

> fiction/provenance only research evidence: no 이 문서는 사가 문서 정합 감사 기록이다. QFUDS 연구 증거·roadmap status 아님. workflow: 멀티에이전트 감사(7 폴더 리더 + 편집자 종합 + 완결성 검수), 발견·정리 기록.

다음: "사용자 게이트 대기 항목(036 리네임 여부·본문 전면 재라벨·status 강등·011 번호 지위) 결정 후 2차 패스"

### `00_workroom` — 운영 규칙·GSD brief·오늘 작업 상태판

#### [QFUDS SAGA 창작 시스템](00_workroom/001_agentic_saga_system_ko.md)
`draft` · 2026-06-20 · guide

> 이 문서는 QFUDS SAGA를 쓰기 위한 별도 agentic fiction system의 초안이다.

다음: user-confirmed world-direction matrix before story drafting

#### [QFUDS SAGA 이중언어 용어규율 글로서리](00_workroom/003_bilingual_term_discipline_glossary_ko.md)
`draft` · 2026-07-01 · guide

> 한국어 prose 본문에서 어떤 단어를 영어로 남기고 어떤 단어를 한국어로 옮길지 정하는 집행 기준. SAGA 한국어판이 "영어가 섞인 기계 초안"이 아니라 "한국어 소설"로 읽히게 한다.

다음: apply to first-arc Korean adaptations 019-024 dejargon polish

#### [QFUDS SAGA 2부 GSD Phase Brief](00_workroom/004_arc_two_gsd_phase_brief_ko.md)
`draft` · 2026-07-01 · guide

> 이 문서는 [Fiction IP Management Workflow](../../../../../../../../.agent/workflows/fiction-ip-management-workflow.md)의 GSD Planning Integration 규칙에 따라, 2부를 **다단계 writing sprint**로 실행하기 위한 phase brief다. (단발 에피소드는 brief 없이 진행 가능하나, arc 단위 sprint는 brief를 둔다.)

다음: approve arc-two episode map, then write 028 Korean primary

#### [QFUDS SAGA 시리즈 제작 하네스](00_workroom/005_series_production_harness_ko.md)
`draft` · 2026-07-01 · guide

> 기존 하네스는 **문서(에피소드) 단위**만 검증했다. AI-tell·자연스러움·이해도· validate는 한 편 안에서만 본다. 그래서 단편은 통과한다. 그러나 6편을 쌓자

다음: promote series gates to global .agent workflow + templates

#### [QFUDS SAGA 작가 아이디어 추적 원장](00_workroom/006_creative_inputs_traceability_ko.md)
`draft` · 2026-07-01 · index

> 작가가 그동안 준 아이디어가 **어느 문서에 담겼고, 무엇에 적용되는지** 한눈에 추적한다. 아무것도 버려지지 않았다. 서랍별로 정리됐을 뿐이다.

다음: keep updated as new author ideas land; respect cascade drift ledger before pointing to active drafts

#### [QFUDS SAGA 1부 Book 1 GSD Phase Brief](00_workroom/007_first_arc_book1_gsd_phase_brief_ko.md)
`draft` · 2026-07-01 · guide

> 이 brief는 029를 1부 Book 1로 완성하려던 legacy completion sprint다. [011 §10](../10_story_design/011_saga_arc_map_multiarc_ko.md) 이후 신규 구조에서는 029가 **2부 Mara 자산**으로 이동 예정이고, active 사엘 origin 원고는 [030](../20_drafts/1.5부/030_origin_arc_sael_korean_primary.md)이다(2026-06-30에 1부→1.5부 강등; 새 1부는 「…

다음: reference only; 029 is canonical 2부 Mara asset under 011 §10 and active origin drafting continues in 030

#### [QFUDS SAGA 외부 AI 글쓰기 시스템 갭 감사](00_workroom/008_external_ai_writing_systems_gap_audit_ko.md)
`draft` · 2026-06-30 · guide

> 이 문서는 외부 AI 소설·웹소설·MCP·Claude Skills 레포의 README를 훑고, QFUDS SAGA 하네스에 무엇을 가져올지 정리한 작업실 감사다. 결론은 간단하다.

다음: convert selected gaps into local production board, chapter intent card, and review-wave templates

#### [QFUDS SAGA Production Board](00_workroom/009_saga_production_board_ko.md)
`draft` · 2026-07-02 · guide

> 이 문서는 QFUDS SAGA의 현재 집필 실행 상태판이다. canon 문서가 아니다. 장편 생산 상태, 막힌 이유, 다음 행동, 검증 로그를 한 장에 모아 다음 에이전트가 같은 규칙을 다시 발견하느라 시간을 쓰지 않게 한다.

다음: "025 근미래 리센터로 관통선(씨앗-제도-신) 재정렬. 다음=0부 캐스(036) 착수 / 새 1부 오르페우스(035) 작성 / 1.5부(033)·2부(034) 풀길이 유지 / 2부 S2 polish / 3부 author-loss 풀길이 / release 정식 게이트"

#### [QFUDS SAGA Chapter Intent Card Template](00_workroom/010_chapter_intent_card_template_ko.md)
`draft` · 2026-06-21 · guide

> 이 문서는 SAGA 장/대형 장면을 쓰기 전 채우는 의도 카드의 로컬 템플릿이다. 장면을 멋있게 쓰기 전에, 누가 무엇을 원하고 무엇을 잃는지 먼저 고정한다.

다음: fill one card for the approved 1부 origin POV before drafting origin prose

#### [QFUDS SAGA 전문가 패널 세계-체계 확장 인계 브리프](00_workroom/011_expert_panel_world_system_handoff_ko.md)
`draft` · 2026-07-01 · guide

> 이 문서는 "Q-Day 이후 문명 재편을 14개 도메인 패널로 세분화하자"는 작가 입력을 저장소 규칙에 맞춰 정리한 **작업 인계 브리프**다. 무엇을 읽고 어떤 순서로 실행하며 어디서 멈춰야 하는지를 한 장에 모은다.

다음: 승격 완료(2026-07-01, 경로 A). 스펙은 bible 028로 승격됨. 이 브리프는 작업 provenance로 보존

#### [QFUDS SAGA 근미래 예측 패널 방법 (휴머노이드 로봇 → 노동 재편 → Q-Day)](00_workroom/012_near_future_forecast_panel_method_ko.md)
`draft` · 2026-07-01 · guide

> [011 전문가 패널 세계-체계 인계](011_expert_panel_world_system_handoff_ko.md)의 자매다. 011/028의 14도메인이 **Q-Day 이후 인과 감사 렌즈**였다면, 이 문서는 같은 렌즈를 **Q-Day 이전 근미래(2020s-2090s) 예측용**으로 재조준한 작가실 생산 도구다. 목적은 002 §2·011·026이 이름만 두고 비워 둔 "지수 성장기" 활주로를 현실적 예측으로 채워 0부(카산드라)와 026 Q-Day에 잇는 것이다.

다음: 이 방법으로 예측 실행 → story_design 027 근미래 프렐류드 산출. 캐논 승격은 사용자 게이트

#### [QFUDS SAGA 실세계·물리 리서치 앵커 대장 (핍진성 닻)](00_workroom/013_real_world_and_physics_research_anchors_ko.md)
`draft` · 2026-07-01 · guide

> 근미래 예측 세계관(로봇→노동→Q-Day)과 in-world 물리·먼 미래 우주론 substrate의 **핍진성 닻**을 신뢰 출처에서 긁어와 중립 톤으로 정리한 대장이다. 08개 리서치 렌즈(근미래 5 + 물리 3)의 결과다. 픽션은 이 자료를 "그럴듯함"의 근거로만 인용하고, 실제 예측·투자·정치 주장으로 쓰지 않는다.

다음: 근미래 프렐류드(story_design 027)와 in-world 물리(025)의 핍진성 닻으로 인용. 픽션 전용, QFUDS 증거 아님

#### [QFUDS SAGA Truth-State Ledger (인물·독자·세계 지식 상태 원장)](00_workroom/014_truth_state_ledger_ko.md)
`draft` · 2026-07-01 · guide

**주의 — 리센터 이전 라벨 포함:** 이 문서 본문은 옛 부 번호를 담을 수 있다. 현행 매핑은 024·025·027 SSOT가 우선.

> 008 갭 감사가 지정한 필요 집행 모듈 6개 중 유일하게 비어 있던 모듈(빈 표, TBD)을 채운

다음: 장(scene)마다 네 칸(인물/독자/세계/열린 모순)을 채워 리빌 페어플레이·과설명·모순을 점검. 부 라벨은 024 기준

#### [QFUDS Verse Chronicler Pass 계획 (전문 감사·드리프트 원장·단계별 편집 플랜)](00_workroom/015_chronicler_pass_plan_ko.md)
`draft` · 2026-07-01 · guide

> Pass)의 단계별 실행 계획**을 세운다. 분석·계획 전용이다. 이 문서는 캐논을 다시 쓰지 않고, 파일을 삭제·이동하지 않으며, `20_drafts`·`30_revisions`·`90_archive`를 건드리지 않는다.

다음: Phase 1(명칭 잔재)부터 사용자 승인 하에 본문 정합. 캐논 위계·SSOT 우선순위 보존, drafts/revisions/archive 미수정

#### [QFUDS Verse 최종 통합 Chronicler Report (전 범위 감사·의존성 그래프·P0/P1/P2 로드맵)](00_workroom/016_qfuds_verse_final_chronicler_report_ko.md)
`provenance` · 2026-07-01 · guide

> 최종 리포트다. 앞선 산출물([900 아키텍처](../../../00_continuity/900_worldbuilding_architecture_ko.md)· [901 드리프트/부채](../../../00_continuity/901_canon_drift_and_tech_debt_report_ko.md)· [015 Chronicler Pass 계획](015_chronicler_pass_plan_ko.md)·[014 Truth-State Ledger](014_truth_state_ledger_ko.m…

다음: P0 없음. P1 Chronicler Pass(015 5-Phase)부터 사용자 승인 하에. 그래프는 scripts/build_doc_graph.py 재생성

### `40_release` — 출간 후보·내보내기 (게이트 통과 후)

#### [QFUDS SAGA Pre-Reboot 1부 Release Manifest](40_release/900_pre_reboot_first_arc_release_manifest_ko.md)
`provenance` · 2026-06-21 · index

> release 후보로 묶였던 상태를 보존하는 **provenance manifest**다. active release candidate가 아니다.

다음: no active release until 029 reboot prose passes continuity, counterpart, and release gates

---

이 파일은 `scripts/build_saga_digest.py`가 생성한다. fiction/provenance only이며 QFUDS 연구 증거·roadmap status가 아니다.
