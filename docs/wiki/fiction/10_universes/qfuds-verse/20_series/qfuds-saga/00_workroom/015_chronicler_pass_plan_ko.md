---
doc_id: qfuds_saga_chronicler_pass_plan_ko
title: QFUDS Verse Chronicler Pass 계획 (전문 감사·드리프트 원장·단계별 편집 플랜)
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_verse_worldbuilding_architecture_ko
  - qfuds_verse_canon_drift_and_tech_debt_report_ko
  - qfuds_saga_canon_authority_and_ssot_map_ko
  - qfuds_saga_restoration_mechanism_correction_ko
  - qfuds_saga_character_map_and_timeline_coordinates_ko
next_gate: Phase 1(명칭 잔재)부터 사용자 승인 하에 본문 정합. 캐논 위계·SSOT 우선순위 보존, drafts/revisions/archive 미수정
last_updated: 2026-07-01
---

# QFUDS Verse Chronicler Pass 계획 (전문 감사·드리프트 원장·단계별 편집 플랜)

## 0. 이 문서의 자리 / 방법

`qfuds-verse` 고정 범위 in-scope 문서를 전문 완독한 감사 결과 위에, **본문 정합(Chronicler
Pass)의 단계별 실행 계획**을 세운다. 분석·계획 전용이다. 이 문서는 캐논을 다시 쓰지 않고,
파일을 삭제·이동하지 않으며, `20_drafts`·`30_revisions`·`90_archive`를 건드리지 않는다.

- 파일명 주: 요청된 `012_...`는 이미
  [012 근미래 예측 패널 방법](012_near_future_forecast_panel_method_ko.md)이 점유해
  다음 빈 번호 **015**로 부여한다.
- 아키텍처 지도·의존 그래프는 [900](../../../00_continuity/900_worldbuilding_architecture_ko.md),
  살아 있는 드리프트 원장은 [901](../../../00_continuity/901_canon_drift_and_tech_debt_report_ko.md),
  지식 상태 원장은 [014](014_truth_state_ledger_ko.md)가 보유한다. 이 문서는 그 위에 실행 플랜을 더한다.
- 근거: 전문 완독(정독 루프 2~5 + 멀티에이전트 완독 감사 wf_8e897838, 80문서 role·drift 추출).

```text
fiction/provenance only
research evidence: no
external source claim: no
```

## 1. 전 문서 인덱스 (81문서)

전 문서 공통값: `stage: reference`, `evidence_role: provenance`. status는 표기 없으면 `draft`
(예외만 명기). class = canon / candidate / design / provenance 중 하나.

캐논 규칙 반영: `00_workroom` 전체와 `40_release/900`·전 README = provenance. `10_story_design`
= design(승격 전 stable canon 아님). `10_world/030~035·037·038`·`story_design/027`·`014 brainstorm`
= candidate. 나머지 `00_continuity`·`10_world`·`00_bible` = canon.

### 1.1 `00_continuity` (7)

| 파일 | doc_id | type | class |
| --- | --- | --- | --- |
| 000_canon_authority_and_ssot_map_ko | qfuds_saga_canon_authority_and_ssot_map_ko | index | canon(권위 루트) |
| 002_deep_time_restoration_timeline_ko | qfuds_saga_deep_time_restoration_timeline_ko | guide | canon(연표 SSOT) |
| 011_chronology_restoration_admin_black_hole_seat_ko | qfuds_saga_chronology_restoration_admin_black_hole_seat_ko | guide | canon |
| 036_far_future_deep_time_chronicle_ko | qfuds_verse_far_future_deep_time_chronicle_ko | guide | canon(확장 레이어) |
| 900_worldbuilding_architecture_ko | qfuds_verse_worldbuilding_architecture_ko | index | provenance(감사) |
| 901_canon_drift_and_tech_debt_report_ko | qfuds_verse_canon_drift_and_tech_debt_report_ko | reference | provenance(감사) |
| README | qfuds_verse_continuity_index_ko | index | provenance(index) |

900·901 status = provenance.

### 1.2 `10_world` (25)

| 파일 | doc_id | type | class |
| --- | --- | --- | --- |
| 001_world_anchor_and_verisimilitude_ko | qfuds_saga_world_anchor_and_verisimilitude_ko | guide | canon |
| 003_factions_cultures_power_ecology_ko | qfuds_saga_factions_cultures_power_ecology_ko | guide | canon |
| 005_bitcoin_genesis_chain_and_restoration_myth_ko | qfuds_saga_bitcoin_genesis_chain_and_restoration_myth_ko | guide | canon |
| 006_post_agi_civilization_history_bilingual_protocol_ko | qfuds_saga_post_agi_civilization_history_bilingual_protocol_ko | guide | canon |
| 007_cryptographic_death_and_hash_covenant_ko | qfuds_saga_cryptographic_death_and_hash_covenant_ko | guide | canon |
| 009_reader_accessibility_and_real_world_anchors_ko | qfuds_saga_reader_accessibility_and_real_world_anchors_ko | guide | canon |
| 010_last_archive_origin_and_reversal_causality_ko | qfuds_saga_last_archive_origin_and_reversal_causality_ko | guide | canon(인과 SSOT·키스톤) |
| 013_cryptographic_death_era_and_crypto_concepts_ko | qfuds_saga_cryptographic_death_era_and_crypto_concepts_ko | guide | canon |
| 015_factions_canon_naming_ko | qfuds_saga_factions_canon_naming_ko | guide | canon(명칭 SSOT) |
| 017_bitcoin_stature_ideology_deeptime_ko | qfuds_saga_bitcoin_stature_ideology_deeptime_ko | guide | canon |
| 018_world_compendium_codex_ko | qfuds_saga_world_compendium_codex_ko | index | canon(색인) |
| 020_ai_automation_human_in_the_loop_ssot_ko | qfuds_saga_ai_automation_human_in_the_loop_ssot_ko | guide | canon(인간 확인 루프) |
| 021_restoration_mechanism_correction_ko | qfuds_saga_restoration_mechanism_correction_ko | guide | canon(복원 물리 SSOT) |
| 025_in_world_physics_information_unitarity_restoration_ko | qfuds_saga_in_world_physics_information_unitarity_restoration_ko | guide | canon(원본 부재 물리 최상위) |
| 026_qday_aftermath_timeline_and_world_ko | qfuds_saga_qday_aftermath_timeline_and_world_ko | guide | canon(Q-Day 여파 SSOT) |
| 028_qday_world_system_14domain_matrix_ko | qfuds_saga_qday_world_system_14domain_matrix_ko | guide | canon(026 부속) |
| 030~035_world_expansion_wave1~6 | qfuds_verse_world_expansion_wave1~6_* | guide | **candidate**(공유 세계 대사전) |
| 037_yi_gi_ideology_axis_ko | qfuds_verse_yi_gi_ideology_axis_ko | guide | **candidate**(이념 축) |
| 038_far_future_native_lexicon_return_death_ko | qfuds_verse_far_future_native_lexicon_return_death_ko | guide | **candidate**(원어 층) |
| README | qfuds_verse_world_index_ko | index | provenance(index) |

### 1.3 `00_bible` (11)

| 파일 | doc_id | type | class |
| --- | --- | --- | --- |
| 004_narrative_pov_theme_naming_ko | qfuds_saga_narrative_pov_theme_naming_ko | guide | canon(시점·주제 규칙) |
| 008_first_arc_canon_consolidation_ko | qfuds_saga_first_arc_canon_consolidation_ko | guide | canon(Bridge, 검증 필요) |
| 012_character_liora_sen_ko | qfuds_saga_character_liora_sen_ko | guide | canon(Liora SSOT) |
| 014_authorial_lenses_compression_ssot_soft_editing_ko | qfuds_saga_authorial_lenses_compression_ssot_soft_editing_ko | guide | canon(작가 렌즈) |
| 016_character_ensemble_voices_relationships_ko | qfuds_saga_character_ensemble_voices_relationships_ko | guide | canon(앙상블 Voice) |
| 019_character_depth_sheets_ko | qfuds_saga_character_depth_sheets_ko | guide | canon(Arc 변화) |
| 022_authorship_of_the_standard_theme_axis_ko | qfuds_saga_authorship_of_the_standard_theme_axis_ko | guide | canon(기준 작성권) |
| 023_ideological_incoherence_triad_ko | qfuds_saga_ideological_incoherence_triad_ko | guide | canon(삼각) |
| 024_character_map_and_timeline_coordinates_ko | qfuds_saga_character_map_and_timeline_coordinates_ko | guide | canon(캐릭터·시대 좌표 SSOT) |
| 027_machine_childhood_ai_history_narrator_throughline_ko | qfuds_saga_machine_childhood_ai_history_narrator_throughline_ko | guide | canon(AI사 관통선 ref) |
| README | qfuds_saga_bible_index_ko | index | provenance(index) |

### 1.4 `00_workroom` (14) 전부 provenance

001 창작 시스템 · 003 용어 글로서리 · 004 2부 GSD brief · 005 제작 하네스 · 006 아이디어 추적 ·
007 1부 Book1 GSD brief · 008 갭 감사 · 009 Production Board · 010 Intent Card 템플릿 ·
011 패널 인계 · 012 근미래 예측 방법 · 013 리서치 앵커 · 014 Truth-State Ledger · README.
(doc_id는 `qfuds_saga_*`. 006·004·007은 legacy 번호 주의, §6.)

### 1.5 `10_story_design` (23) 전부 design (승격 전 stable canon 아님)

002 시각 전시 · 007 Arc Two 계획(legacy명) · 008 반전 설계 · 009 형식·throughline ·
010 2부 에피소드 맵 · 011 아크 지도(부 번호 remap SSOT) · 012 1부 outline reboot(status=completed) ·
013 씬 카드(status=completed) · 014 sovereign-AI(**candidate/brainstorm**) · 015 5대 질문 스파인 ·
016 origin 아웃라인 · 017 origin 씬 카드 · 018 암호 온보딩 · 019 사엘 실행 시트 · 020 bridge ·
021 리빌 사다리 · 022 causal master · 023 오리엔테이션 · 024 오르페우스 설계 · 025 근미래 리센터 ·
026 기계 화자 · 027 근미래 프렐류드(**candidate**) · README.

### 1.6 `40_release` (2) + 루트 (2)

40_release/900 Pre-Reboot 매니페스트(status=provenance) · 40_release/README ·
qfuds-verse README(루트) · qfuds-saga README(series 루트). 전부 provenance/index.

## 2. SSOT Authority Tree

권위 루트 = [000 캐논 권위·SSOT 지도](../../../00_continuity/000_canon_authority_and_ssot_map_ko.md).
000 §도메인 권위 표 + 037 경계에서 확정한 도메인별 최종 권위:

```text
000 (권위 루트: 명시 우선 > 도메인 표 > last_updated > unknown)
├─ 복원 물리      → 021  (그 위 원본 부재 물리 025가 최상위)
├─ 명칭·세력명     → 015
├─ Q-Day 여파     → 026 (부속 028)
├─ 인과·Last Archive → 010
├─ 연표·복원 행정   → 011 (+ 딥타임 002, 심층시간 036)
├─ 인간 확인 루프   → 020
├─ 시대 좌표(인물)  → 024  (series bible)
└─ 이념 형이상학    → 037 (candidate, 025·026 진자 위)
```

충돌 우선순위(000·037): **025 > 021 > 026 > 003 > 015**. 피의존 키스톤 = 010(in-degree 18).
상세 트리·허브·블라스트 반경은 [900 §2·§4](../../../00_continuity/900_worldbuilding_architecture_ko.md).

## 3. Domain Ownership Map

[900 §3·§3.1·§3.3](../../../00_continuity/900_worldbuilding_architecture_ko.md)가 보유. 요약:

- **World Canon** = `10_world`(물리·암호·세력·제도·확장 대사전).
- **Continuity Canon** = `00_continuity`(권위·연표·복원 행정·심층시간).
- **Story Canon** = `00_bible`(인물·주제·시점·Arc·AI 관통선·작가 철학).
- **집행/설계층**(canon 아님) = `00_workroom`(provenance) · `10_story_design`(design) · `40_release`.
- 산문·개정·아카이브(`20_drafts`·`30_revisions`·`90_archive`) = 범위 밖.

## 4. Canon Drift Ledger (통합 D1~D22)

살아 있는 원장은 [901 §1·§1.1](../../../00_continuity/901_canon_drift_and_tech_debt_report_ko.md).
Chronicler Pass 대상만 상태와 함께 통합한다(근거 경로·행 표기).

| # | 드리프트 | 근거 위치 | 상태 |
| --- | --- | --- | --- |
| D2 | "부활/완전 복원" 현대 gloss | 021 §5(line 126~128), 002 §배너(line 24~29), 005 §목적 배너(line 24~30) | **해소**: 038 원어 층 + 배너 |
| D6 | "1부=Cryptographic Death"·"사엘=1부" | 002 line 24 이하 1기 서술 | Phase 2 |
| DRIFT-008/017/020 | legacy 부 라벨(arc two, 사엘=1부, Mara=1부) | 008 §Arc Two Hook(line 182~239), 007 title·§Arc Two(line 3·17·53·77), 012 line 94, 013 line 148, **024 line 108 "사엘(1부)"** | Phase 2 (024 최우선) |
| DRIFT-009/012 | 004 Naming Table가 015와 어긋날 소지 | 004 line 187 `Castra Tabularii`, 015 §명칭 충돌(line 87~95·139) | Phase 1 (검증 필요) |
| DRIFT-013 | 019 Core Drive가 012·016 반복(20~30%) | 019 §Identity 이하 | Phase 3(참조화) |
| DRIFT-011 | Migration compatibility layer(배너로만 차단) | 008·012·016·019 상단 배너 | Phase 2 전체가 이 부채 해소 |
| DRIFT-005/021 | candidate 과잉승격 위험 | 030~035, 027, 037, 038 | Phase 4(라벨·게이트) |
| DRIFT-022 | 023 "복제품" 표현 | 023 line 88·91·157 | 독자용 허용, canon 문서는 사본/재구성체 |

주의(검증 필요): **024 line 108 "사엘(1부)"**는 시대 좌표 SSOT 본문이 현재 매핑(사엘=1.5부)과
어긋나는 지점이다. SSOT 자체의 라벨이므로 Phase 2에서 가장 먼저 처리한다. 단, 024가 "1부"를
포괄 의미(사엘 계열 = 넓은 1부군)로 쓴 것인지 엄밀히 1.5부 오기인지는 저자 확인이 필요하다(미정).

## 5. Candidate Promotion Register

전부 candidate. 승격은 [030 §7 6체크 게이트](../../../10_world/030_world_expansion_wave1_names_places_events_ko.md)
+ [901 §4](../../../00_continuity/901_canon_drift_and_tech_debt_report_ko.md) 게이트.

| candidate | 위치 | 승격 타깃 SSOT | 특이 리스크 |
| --- | --- | --- | --- |
| 030~035 세계 확장 웨이브 | 10_world | 명칭→015, 세력→003, 여파→026 | Vera/Vera Dace 충돌(031, 개명 권장) |
| 037 이기 이념 축 | 10_world | 003·026 진자·025 물리 | 실존 성리학 비대응 유지 |
| 038 먼 미래 원어 층 | 10_world | 021·025·037 | 라틴은 기존 제도 관습 상속(034), 신규 conlang 아님 |
| 027 근미래 프렐류드 | story_design | 026·002·bible-027 | 과잉밀도(DRIFT-021), 6체크 개별 승격 |
| 014 sovereign-AI 축 | story_design | 022·023 | brainstorm, 선택 씨앗만 |

6체크(승격 전 필수): (1) 015 명칭 충돌 없음, (2) 025/021 물리 모순 없음, (3) 026 여파 착지,
(4) em dash 0·"박-" 슬랭 0·강의조 없음, (5) 실존 집단 비대응, (6) 상위 SSOT depends_on·인덱스 배선.

## 6. Deprecated / Legacy 용어 표

| 폐기·legacy 표기 | canon 표기 | 근거(폐기 선언) | 잔재 위치(검증 필요) |
| --- | --- | --- | --- |
| Domus Registri / Domus Tabularii / House Tabularii | **Domus Clavium** (House of Keys) | 015 line 87~95·139, 000 line 40, 016 line 109 | 004 line 187 `Castra Tabularii`(원장 성채=Ledger Keeps): 어근 Tabularii 잔존. 지명 의도인지 검증 필요 |
| "완전 복원 / 완전 역연산 / 부활(원본 회복)" | 재현·N세대 귀환·해상 손실 (038), 기전=사본(021) | 021 §5, 038 대응표 | 002·005 배너로 gloss 처리됨(해소). 잔여 canon 본문 naive 표현 없음 |
| "복제품"(독자 설명어) | 사본 / 재구성체 | 025·021 정밀 구분 | 023 line 88·91·157: 독자 오리엔테이션은 허용, canon 문서 확산 금지 |
| legacy 부 라벨: "Arc Two / 아크 투 / 사엘=1부 / Mara=1부" | 024 매핑: 0부 캐스 / 1부 오르페우스 / 1.5부 사엘 / 2부 마라 / 3부 author-loss | 024, 025, 011 §부 번호 remap(line 277) | 007·008·012·013·024 line 108 (§4 D6·DRIFT-017) |

## 7. 내부 링크·의심 참조

- **깨진 마크다운 링크: 0** (전 범위 스캔). 권위 링크 전부 유효.
- **범위 경계 교차 depends_on 24건**: in-scope 문서가 `20_drafts`/`30_revisions` doc_id를 참조.
  대부분 의도적(bible·story가 산문 원고 근거). 주시:
  - `00_bible/008` depends_on 원고 7건(exhibit_s0·dead_exchange·last_hodler·identity_flood·
    hawking_court·broken_crown·broken_crown_event). 원고 reboot 시 대상 소멸 가능.
  - `10_world/025` depends_on `qfuds_saga_revisions_mara_order_totem_two_readings_seed_design_ko`.
  - `story_design/012·013`(completed) depends_on 원고 id.
- **legacy 라벨 링크**: story_design README line 65가 `007 Arc Two Korean-Primary Plan`을 "2부
  계획"으로 안내하나 011 remap상 author-loss는 3부. 안내 문구 검증 필요(Phase 2 동반).

## 8. 리팩터 우선순위

| 순위 | 대상 | 근거 | 위험 |
| --- | --- | --- | --- |
| P1 | 명칭 잔재(Castra Tabularii 검증·004 Naming↔015) | DRIFT-009/012 | 낮음(기계적) |
| P1 | 부 라벨 정합(024 line 108 우선 → 007·008·012·013·README) | DRIFT-008/017/020·D6·DRIFT-011 | 중(SSOT·완료 문서 포함) |
| P2 | 019 Core Drive 참조화 | DRIFT-013 | 낮음 |
| P2 | candidate 배너·6체크 명문화(030~035·027·037·038·014) | DRIFT-005/019/021 | 낮음 |
| P3 | status 위생(안정 문서 draft→reference), 029 결번 각주 | 901 §5 | 낮음 |

복원 용어(D2)·원어 층(038)·Truth-State Ledger(014)는 이미 처리됨(재작업 불필요).

## 9. 단계별 편집 플랜 (Chronicler Pass)

원칙: SSOT 우선순위(025>021>026>003>015) 보존. 한 Phase = 한 커밋. drafts/revisions/archive
미수정. 산문·본문에 손대므로 **각 Phase 착수 전 사용자 승인**. 배너는 본문 정합이 끝난 뒤에만 걷는다.

- **Phase 0 준비:** 대상 파일 목록 확정, `git status` 청결 확인, 이 계획서 승인. 편집 없음.
- **Phase 1 명칭 잔재(최저 위험):**
  - 004 line 187 `Castra Tabularii`가 지명(Ledger Keeps)으로 의도된 것인지 확인. 015 단일화와
    충돌이면 라틴명 정합, 지명 고유라면 015에 예외로 등록. (미정 → 저자 확인)
  - 004 Naming Table 전반을 015 기준으로 대조, 폐기 표기 잔재 정리. Domus Clavium 유지.
- **Phase 2 부 라벨 정합(핵심, DRIFT-011 해소):**
  - **024 line 108 "사엘(1부)"를 최우선**으로 024 매핑(1.5부)에 맞춰 정합(또는 포괄 의미 명시).
  - 008(§Arc Two Hook·line 111~239)·007(title·본문)·012·013(completed)·story_design README line 65의
    legacy "Arc Two / 사엘=1부"를 024·011 remap 기준으로 치환. stable ID 정책상 파일명·doc_id는
    유지, 본문 라벨만 정합. 정합 완료 문서에서 상단 리센터 배너를 축약·제거(compatibility layer 해소).
  - 002 1기 서술(D6)은 038 원어 층·현대 gloss 프레임 유지가 이미 되어 있으므로 부 라벨 표기만 점검.
- **Phase 3 캐릭터 참조화:** 019 반복 Core Drive를 "012·016 참조"로 축약(병합 아님). 시대좌표·
  원본/사본 상태 서술은 024로만.
- **Phase 4 candidate 위생:** 030~035·027·037·038·014에 candidate 배너·6체크(§5) 링크 확인/보강.
- **Phase 5 위생·마감:** status 안정 문서 reference 승격 검토, 029 결번 각주(000/README), 900·901·015
  상호 정합 갱신. 검증 스위트 통과 후 커밋.

각 Phase 후 900/901/014를 갱신해 원장과 본문이 어긋나지 않게 한다.

## 10. 커밋 전 안전 점검 명령

```bash
# 문서·픽션 게이트
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/agent_workflow_guard.py --staged
python3 scripts/fiction_gate.py --staged
sh scripts/git-hooks/pre-commit

# 스타일 가드 (편집 파일에 대해)
grep -nP '\x{2014}' <edited_files>         # em dash(U+2014) = 0 확인
grep -nE '박(는|았|혀|은다)' <edited_files>  # "박-" 슬랭 0 (못질 등 의도적 비유는 예외)

# 정합 스모크
grep -rniE "Domus Registri|Domus Tabularii|House Tabularii" 10_world 00_continuity \
  20_series/qfuds-saga/00_bible 20_series/qfuds-saga/10_story_design   # 폐기 표기 잔재
grep -rniE "사엘.{0,4}1부|Arc Two" 20_series/qfuds-saga                 # 부 라벨 잔재
git --no-pager diff --stat                 # drafts/revisions/archive 미포함 확인
```

편집은 in-scope canon/design/provenance 문서에만. `20_drafts`·`30_revisions`·`90_archive`가
diff에 나타나면 중단하고 되돌린다.

```text
fiction/provenance only
research evidence: no
external source claim: no
```

이 문서는 전문 완독 감사 위에 세운 Chronicler Pass 실행 계획(분석·계획 전용)이다. 캐논을 아직
고치지 않으며, 각 Phase는 사용자 승인 하에 진행한다. 살아 있는 원장은 901, 아키텍처는 900,
지식 상태는 014가 보유한다.
