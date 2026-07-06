---
doc_id: qfuds_verse_fiction_v2_source_triage_ko
title: QFUDS Verse fiction_v2 소스 분류 원장
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_final_chronicler_report_ko
  - qfuds_saga_chronicler_pass_plan_ko
  - qfuds_saga_canon_authority_and_ssot_map_ko
next_gate: update only when a source document changes class or the reader report stops matching current canon
last_updated: 2026-07-06
---

# QFUDS Verse fiction_v2 소스 분류 원장

이 원장은 `fiction_v2` 리더가 어떤 원본을 어떻게 읽었는지 남기는 문서다. 새 정사 선언이 아니다. 기존 문서를 이동하거나 이름을 바꾸거나 번호를 고치지 않는다.

분류 기준은 간단하다.

- `core`: 현재 리더가 중심 해석을 세울 때 직접 의존한 원본이다.
- `support`: 중심 해석을 보강하지만, 처음 읽을 때 반드시 외울 필요는 없는 원본이다.
- `candidate`: 좋은 재료지만 아직 정사처럼 읽으면 위험한 원본이다.
- `stale_or_provenance`: 역사, 감사, 이전 구조, 레거시 흔적을 담은 원본이다. 현재 세계관 이해의 첫 독서 목록에서는 뒤로 미룬다.
- `ignore_for_reader`: 이번 리더 작성에서는 의도적으로 제외한 영역이다.

## 최상위 권위

| Source label | Class | Why it matters | Reader use |
| --- | --- | --- | --- |
| `qfuds_saga_canon_authority_and_ssot_map_ko` | core | 캐논 권위와 SSOT 위계를 잡는 루트다. | 충돌이 나면 먼저 확인하는 뿌리로 둔다. |
| `qfuds_saga_chronicler_pass_plan_ko` | core | 드리프트, 후보, stale, 단계별 정리 계획을 가장 직접적으로 말한다. | `fiction_v2`의 분류 원칙을 가져온다. |
| `qfuds_saga_final_chronicler_report_ko` | core | 전 범위 감사 결과와 P0/P1/P2 상태를 정리한다. | “캐논은 대체로 건강하지만 라벨과 후보 혼합이 문제”라는 판단의 근거로 둔다. |
| `qfuds_saga_drafts_index_ko` | support | 현 원고 배치와 part 폴더 상태를 보여 준다. | 파트 라벨이 헷갈릴 때 현재 배치만 확인한다. |

## 연표와 연속성

| Source label | Class | Why it matters | Reader use |
| --- | --- | --- | --- |
| `qfuds_saga_deep_time_restoration_timeline_ko` | core | 장기 복원 문명사의 큰 흐름을 잡는다. | 복원이 부활이 아니라 장기 행정과 문명사라는 점을 읽는다. |
| `qfuds_saga_chronology_restoration_admin_black_hole_seat_ko` | core | 연표, 복원 행정, black-hole-scale 본거지 감각을 연결한다. | Last Archive와 복원 행정의 시간 규모를 잡는다. |
| `qfuds_verse_far_future_deep_time_chronicle_ko` | support | 먼 미래 심층시간을 넓게 펼친다. | 딥타임 분위기는 참고하되 첫 독해의 중심으로 삼지 않는다. |
| `qfuds_verse_worldbuilding_architecture_ko` | stale_or_provenance | 월드빌딩 아키텍처와 의존 그래프를 보존한다. | 구조 감사용으로 보되, 독해 보고서 본문에는 끌어오지 않는다. |
| `qfuds_verse_canon_drift_and_tech_debt_report_ko` | stale_or_provenance | drift와 tech debt를 기록한다. | 충돌 원인을 확인할 때만 본다. |

## 세계 시스템 핵심

| Source label | Class | Why it matters | Reader use |
| --- | --- | --- | --- |
| `qfuds_saga_factions_cultures_power_ecology_ko` | core | 세력, 문화, 권력 생태계의 기본 장부다. | 세력을 “같은 질문에 대한 다른 답”으로 재해석할 때 쓴다. |
| `qfuds_saga_bitcoin_genesis_chain_and_restoration_myth_ko` | core | Bitcoin Genesis Chain과 복원 신화의 연결을 둔다. | 비트코인을 현실 기반 앵커로 읽고, 마법화하지 않는다. |
| `qfuds_saga_cryptographic_death_and_hash_covenant_ko` | core | 암호학적 죽음과 hash covenant를 다룬다. | Q-Day 이후 죽음과 장부가 왜 결합하는지 잡는다. |
| `qfuds_saga_last_archive_origin_and_reversal_causality_ko` | core | Last Archive 기원, 역연산 인과, 죽음의 평등을 다룬다. | Last Archive를 신이 아니라 최종 검증 권위로 읽는다. |
| `qfuds_saga_cryptographic_death_era_and_crypto_concepts_ko` | core | Q-Day, 암호 개념, techno-feudal order를 한 번에 담는다. | 암호 개념을 독자 수준으로 낮춰 설명할 때 쓴다. |
| `qfuds_saga_factions_canon_naming_ko` | core | 세력 명칭 canon을 확정한다. | Domus Clavium 등 현재 명칭을 우선한다. |
| `qfuds_saga_bitcoin_stature_ideology_deeptime_ko` | support | 비트코인의 위상과 심층시간 유효성을 다룬다. | Bitcoin Genesis Chain을 세계의 오래된 검증 신화로 읽을 때 쓴다. |
| `qfuds_saga_ai_automation_human_in_the_loop_ssot_ko` | core | AI 자동화와 인간 확인 루프의 SSOT다. | 검증경제가 왜 인간 확인과 법정으로 돌아오는지 설명한다. |
| `qfuds_saga_restoration_mechanism_correction_ko` | core | 복원을 부활이 아닌 정보 역산과 인공 신체로 정정한다. | “복원은 데이터 기반 사본”이라는 문장을 고정한다. |
| `qfuds_saga_in_world_physics_information_unitarity_restoration_ko` | core | 정보, 유니터리, 복원의 in-world 물리 캐논이다. | 복원을 종교적 기적이 아니라 정보 문제로 읽는다. |
| `qfuds_saga_qday_aftermath_timeline_and_world_ko` | core | Q-Day 여파 타임라인과 세계 설정을 정리한다. | Q-Day를 최종 암호 앵커 붕괴로 설명할 때 쓴다. |
| `qfuds_saga_qday_world_system_14domain_matrix_ko` | support | Q-Day 이후 14도메인 세계 체계를 펼친다. | 필요할 때만 도메인별 재료를 꺼낸다. |
| `qfuds_verse_qday_two_crisis_timeline_spine_ko` | core | 인식 위기와 먼 미래 Q-Day를 분리하는 타임라인 척추다. | 두 위기를 섞지 않게 하는 핵심 기준으로 둔다. |
| `qfuds_verse_deeptime_catastrophe_pillar_spine_ko` | candidate | 딥타임 파국 기둥을 추가로 세운다. | 강한 재료지만 처음 독해에서는 후보 레이어로 둔다. |

## SAGA bible과 story design

| Source label | Class | Why it matters | Reader use |
| --- | --- | --- | --- |
| `qfuds_saga_authorship_of_the_standard_theme_axis_ko` | core | 기준 작성권과 사상축을 다룬다. | “누가 기준을 쓰는가”를 “누가 상실을 쓰는가”로 연결한다. |
| `qfuds_saga_ideological_incoherence_triad_ko` | core | 세 양립 불가 신앙의 긴장을 둔다. | 세력을 단순 선악이 아닌 서로 다른 믿음으로 읽는다. |
| `qfuds_saga_character_map_and_timeline_coordinates_ko` | core | 인물과 시대 좌표를 정리한다. | 캐스, 오웬, 사엘, 마라의 역할을 분리한다. |
| `qfuds_saga_machine_childhood_ai_history_narrator_throughline_ko` | support | AI 발전사와 기계 화자 관통선을 둔다. | 기계 화자와 역사 회고를 다룰 때 참고한다. |
| `qfuds_saga_first_arc_reader_orientation_world_and_cast_ko` | core | 세계와 인물을 처음 잡는 오리엔테이션이다. | `fiction_v2` 이전의 가장 가까운 입문 문서로 본다. |
| `qfuds_saga_new_book1_orpheus_design_ko` | core | 새 1부 오르페우스, 사별, 복원 사본, 돌아봄을 설계한다. | 오웬 축을 애도와 검증의 이야기로 읽는다. |
| `qfuds_saga_near_future_recenter_direction_ko` | core | 근미래 grounded SF로 무게중심을 옮긴다. | 캐스와 근미래 인식 위기를 앞쪽에 둔다. |
| `qfuds_saga_near_future_prelude_forecast_ko` | candidate | 2020s-2090s 근미래 프렐류드 재료가 많다. | 현재는 소재 후보로만 읽는다. |
| `qfuds_saga_sovereign_ai_open_closed_axis_brainstorm_ko` | candidate | 소버린 AI와 open/closed 축 브레인스토밍이다. | 아이디어는 보되 canon처럼 고정하지 않는다. |

## 후보 확장

| Source label | Class | Why it matters | Reader use |
| --- | --- | --- | --- |
| `qfuds_verse_world_expansion_wave1_names_places_events_ko` | candidate | 이름, 장소, 사건, 어휘를 확장한다. | 원고에 필요할 때만 재료로 쓴다. |
| `qfuds_verse_world_expansion_wave2_factions_relationships_ko` | candidate | 세력 내부와 관계망을 확장한다. | 세력 디테일 후보로 둔다. |
| `qfuds_verse_world_expansion_wave3_geography_event_chains_ko` | candidate | 지리와 사건 연쇄를 확장한다. | 공간/사건 후보로 둔다. |
| `qfuds_verse_world_expansion_wave4_economy_rites_calendar_ko` | candidate | 경제, 통화, 의례, 달력을 확장한다. | checksum 의례 같은 재료는 선별해서 쓴다. |
| `qfuds_verse_world_expansion_wave5_language_tech_infra_ko` | candidate | 언어와 기술 인프라를 확장한다. | 용어 후보로만 읽는다. |
| `qfuds_verse_world_expansion_wave6_ecology_education_media_index_ko` | candidate | 생태, 교육, 미디어와 확장 인덱스를 둔다. | 지금은 폭을 확인하는 데만 쓴다. |
| `qfuds_verse_yi_gi_ideology_axis_ko` | candidate | 원본 실재와 기질뿐 축을 둔다. | 복원 사본 논쟁의 철학 후보로 둔다. |
| `qfuds_verse_far_future_native_lexicon_return_death_ko` | candidate | 먼 미래 원어 층과 return/death 명칭을 둔다. | 용어 후보로 둔다. |
| `qfuds_saga_register_morph_opening_and_ending_options_ko` | candidate | 판타지에서 hard SF로 전환하는 선택지를 둔다. | 형식 실험 후보로만 읽는다. |

## stale와 provenance

| Source label | Class | Why it matters | Reader use |
| --- | --- | --- | --- |
| `qfuds_saga_world_compendium_codex_ko` | stale_or_provenance | 넓은 compendium이지만 legacy와 후보가 섞일 위험이 있다. | 처음 독해에서는 피하고, 나중에 검색용으로만 쓴다. |
| pre-reboot release manifest | stale_or_provenance | 이전 release-facing 구조를 보존한다. | 현재 세계관 이해에는 넣지 않는다. |
| old part labels | stale_or_provenance | 사엘, 마라, 1부, 1.5부, 2부 표기가 과거 구조를 남긴다. | 현재 리더에서는 새 역할 좌표로 다시 읽는다. |
| old faction names | stale_or_provenance | Domus Tabularii와 Domus Registri 같은 옛 명칭 흔적이 있다. | 현재는 Domus Clavium을 우선한다. |

## 이번 리더에서 제외한 영역

| Area | Class | Why excluded | Reader use |
| --- | --- | --- | --- |
| `90_archive` | ignore_for_reader | 실패한 시도와 과거 구조가 섞여 있다. | 보존용이다. 지금 이해용으로 읽지 않는다. |
| `_versions` | ignore_for_reader | draft/version 흔적이다. | stale와 canon이 섞이므로 제외한다. |
| 숫자 없는 개인 plugin 폴더 | ignore_for_reader | 작가 개인 플러그인 용도다. | 세계관 독해 소스로 쓰지 않는다. |
| raw graph/output files | ignore_for_reader | 감사 보조 산출물이다. | 필요하면 chronicler report를 통해 간접 확인한다. |

## 오라클 가이드 처리 원칙

`fiction_v2`가 하는 일은 원본 문서 안에 흩어진 질문을 하나의 이해 경로로 묶는 것이다.

오라클 문제는 이 리더에서 다음 뜻으로 고정한다.

- 원래 뜻: 검증 시스템 안의 기록은 확인할 수 있지만, 바깥 현실 데이터는 누가 보증하는가.
- QFUDS Verse 확장: 문명 전체가 바깥 현실을 못 믿게 될 때, 현실, 신원, 소유, 죽음, 복원, 기억, 망각을 누가 보증하는가.
- 사용: 새 설정을 추가할 때마다 “무엇을 보증하려고 생긴 설정인가”, “누가 권력을 얻는가”, “누가 손실을 입는가”를 확인한다.
- 경계: `fiction_v2`는 새 정사가 아니라, 기존 설정을 이해하기 위한 해석 레이어다.

## 운영 규칙

앞으로 `fiction_v2`를 갱신할 때는 이 원칙을 따른다.

1. 원본 문서를 이동하지 않는다.
2. `doc_id`를 바꾸지 않는다.
3. 후보 문서는 후보로 남긴다.
4. stale 문서는 삭제하지 않고 “지금은 읽지 말 것”으로 둔다.
5. reader report가 canon과 어긋나면 reader report를 고친다.
6. 새 고유명사를 추가하기보다 중심 질문을 먼저 확인한다.
7. 중심 질문은 “누가 진짜를 판정하고, 누가 상실을 author할 수 있는가”다.
