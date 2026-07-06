---
doc_id: qfuds_saga_production_board_ko
title: QFUDS SAGA Production Board
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_agentic_system_ko
  - qfuds_saga_series_production_harness_ko
  - qfuds_saga_external_ai_writing_systems_gap_audit_ko
next_gate: "320 근미래 리센터로 관통선(씨앗-제도-신) 재정렬. 다음=0부 캐스(036) 착수 / 새 1부 오르페우스(035) 작성 / 1.5부(033)·2부(034) 풀길이 유지 / 2부 S2 polish / 3부 author-loss 풀길이 / release 정식 게이트"
last_updated: 2026-07-06
---

# QFUDS SAGA Production Board

## 역할

이 문서는 QFUDS SAGA의 현재 집필 실행 상태판이다. canon 문서가 아니다. 장편 생산
상태, 막힌 이유, 다음 행동, 검증 로그를 한 장에 모아 다음 에이전트가 같은 규칙을
다시 발견하느라 시간을 쓰지 않게 한다.

Operational workflow:
[Agentic Fiction Production Workflow](../../../../../../../../.agent/workflows/agentic-fiction-production-workflow.md).
IP routing:
[Fiction IP Management Workflow](../../../../../../../../.agent/workflows/fiction-ip-management-workflow.md).

Boundary:

```text
fiction/provenance only
research evidence: no
external AI writing systems: adoption/adaptation allowed (license + source 기록; 2026-06-30 해제)
workflow state: hit_not_cached
install external tools: fiction 한정 허용 (보안 점검 + repo/vault 스코프)
```

## Current State

| Field | Value |
| --- | --- |
| Active unit | 320 근미래 리센터로 관통선(씨앗:제도:신) 재정렬; 0부 캐스(036) 착수 예정; 033 origin(1.5부)·034 Mara(2부) 풀길이 소설 초고 + retention/comprehension 게이트(015/016) 유지; 새 1부 035 오르페우스(오웬·리브) 별도 작성 중 |
| Phase | `verify` passed -> `gated`(retention+comprehension) |
| Owner mode | `writer` + `continuity` + `reader-sim` + `comprehension` + `polish` |
| Status | 두 권 풀길이 초고 완결; comprehension 통과(ran_passed), retention 통과(ran_passed_with_risks); release 정식 게이트는 미실행 |
| Failure reason | 없음(두 권 초고 완결). 잔여=2부 S2 polish, 3부 풀길이 미착수, 영어 각색 2화+ |
| Next action | 320 근미래 리센터로 씨앗:제도:신 관통선 정렬 후 0부 캐스(036) 착수; 병행으로 2부 S2 polish(RET-2B-001-005, [30_revisions/016]) 또는 3부 author-loss 풀길이; `40_release` 승격 전 정식 게이트 |
| Source files | `30_revisions/015`, `30_revisions/016`, `10_story_design/306`, `00_bible/208`, `30_revisions/011` |
| Output files | `20_drafts/1.5부/033_origin_sael_full_novel_korean_primary.md`, `20_drafts/2부/034_mara_full_novel_korean_primary.md`; 보조 `20_drafts/1.5부/031`(콘티), `32`(영어 각색); 새 1부 `20_drafts/1부/035_orpheus_full_novel_korean_primary.md`(작성 중, 별도) |
| Approval needed | no(초고/게이트); yes before release promotion |

## Unit Queue

| Unit | Phase | Intent card | Last review wave | Chronicler pass | Status |
| --- | --- | --- | --- | --- | --- |
| 0부 캐스(036) | plan | 320 근미래 리센터: 씨앗(제도의 씨앗) | 미착수; 320 자산으로 씨앗:제도:신 관통선의 출발점 정렬 | none | `hold` until 036 착수 |
| 1.5부 사엘 origin 풀길이(033) | verified/gated | [015 retention+comprehension](../30_revisions/015_origin_sael_fullnovel_retention_comprehension_gate_20260622_c91e9be_ko.md) | 8장 - 45K 초고; retention ran_passed_with_risks + comprehension ran_passed | 109 게이트 in 120 | `validated` |
| 1부 「오르페우스」 풀길이(035) | draft | 오웬·리브 (작성 중) | 별도 작성 중 | none | `drafting` (별도) |
| SAGA 단편 연작 | draft | [324 단편 연작 브리프](../10_story_design/324_saga_short_story_cycle_brief_ko.md); [325 S1 intent](../10_story_design/325_short_s1_reject_button_intent_card_ko.md) | [001 반려 버튼](../20_drafts/단편집/001_reject_button_korean_primary.md) | [019 S1 chronicler](../30_revisions/019_short_s1_reject_button_chronicler_pass_ko.md) | `drafted`; canon promotion pending review |
| 2부 Mara 풀길이(034) | verified/gated | [016 retention+comprehension](../30_revisions/016_mara_fullnovel_retention_comprehension_gate_20260623_a41bcb9_ko.md) | 6장 - 65K 초고; 독립 온보딩 성공; S2 polish 잔여(RET-2B-001-005) | 205 게이트 in 121 | `validated` |
| 1.5부 콘티 텔링(031) | verified/gated | [014 retention](../30_revisions/014_origin_sael_webnovel_retention_gate_run_20260622_b5f0edf_ko.md) | 웹소설 콘티; ran_passed; 033 풀길이의 blueprint로 보존 | 014 notes in 031 | `blueprint` |
| 영어 각색(119) | draft | Anglophone Episode 1 | 영어 각색 1화 draft | none | `drafted` |
| 030 origin 프로토타입 | provenance | [312](../10_story_design/312_first_arc_origin_scene_cards_ko.md) | flat 프로토타입; 033으로 대체, provenance 보존 | 409 notes in 030 | `archived-provenance` |
| 029 Mara 캐논 원천 | provenance | [308](../10_story_design/308_first_arc_scene_cards_ko.md) | 2부 reboot 캐논 원천; 034의 source, 원천 보존 | Continuity Notes in 029 | `archived-provenance` |
| 3부 author-loss 풀길이 | plan | 114-210 자산 보존 | none | none | `hold` until 풀길이 착수 |
| 14도메인 세계-체계 확장(410→116) | done | [410 인계 브리프](410_expert_panel_world_system_handoff_ko.md) | canon-guardian 충돌 분류 완료(116 §1, hard-conflict 0) | 116 §4 원장 | `promoted` → [world 116](../../../10_world/116_qday_world_system_14domain_matrix_ko.md)(115 부속). 410은 provenance |
| 세계 확장 웨이브 1-6(universe 10_world/117-122) | done(candidate) | [117](../../../10_world/117_world_expansion_wave1_names_places_events_ko.md)·[118](../../../10_world/118_world_expansion_wave2_factions_relationships_ko.md)·[119](../../../10_world/119_world_expansion_wave3_geography_event_chains_ko.md)·[120](../../../10_world/120_world_expansion_wave4_economy_rites_calendar_ko.md)·[121](../../../10_world/121_world_expansion_wave5_language_tech_infra_ko.md)·[122](../../../10_world/122_world_expansion_wave6_ecology_education_media_index_ko.md) | 109/209/115 충돌 대조 완료(기존명 재배정 0) | 122 §4 크로스 인덱스·117 §7 | `candidate` @ universe 공유 세계; **6웨이브 완료 선언**, 전부 보류 = 원고 수요 때 개별 승격(117 §7) |

## Active Risks

| Risk | Scope | Severity | Owner mode | Next action |
| --- | --- | --- | --- | --- |
| Release promotion without artifact-backed retention gate | 030/029 | release-blocking | reader-sim / critic | keep `40_release` empty until a `012` run artifact has persona sheets, source refs, issue ledger, decision |
| Number cascade confusion | 002, 114-210, 105, 107 | medium | continuity | stable IDs remain; verify labels only when touching affected docs |
| External-system adoption (rule relaxed 2026-06-30) | fiction only | medium | critic / continuity | 픽션 한정 adoption/adaptation 허용; 라이선스 확인 + source/license/claim 기록 필수; QFUDS 연구 증거엔 절대 반입 금지 |
| Humanize misuse | prose polish | medium | style_editor | polish only after structure/continuity pass; no AI-detector evasion framing |

## Cascade Ledger (완료)

번호 SSOT는 [306 §10](../10_story_design/306_saga_arc_map_multiarc_ko.md)이다. 번호
physical cascade를 2026-06-21에 실행 완료했다. 물리 폴더는 canonical 부 번호와 일치한다.

| Asset | Physical path (cascade 후) | Canonical role (002) | Status |
| --- | --- | --- | --- |
| 030 origin Sael draft | `20_drafts/1.5부/030_origin_arc_sael_korean_primary.md` | 1.5부 사엘 origin | done (1부→1.5부 강등 2026-06-30) |
| 029 Mara reboot | `20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md` | 2부 Mara | done (1부→2부 이동) |
| 025-027 author-loss drafts | `20_drafts/3부/` | 3부 author-loss | done (2부→3부 이동) |
| Mara prototypes | `20_drafts/2부/_versions/` | 2부 Mara 계보 | done (1부→2부 이동) |
| draft READMEs | `20_drafts/README.md`, `1부/`, `2부/`(신설), `3부/` | 부 번호 일치 네비게이션 | done (doc_id book1/2/3 정합) |

stable ID 보존: 원고 파일명(029·030·025-027)과 `arc_two` doc_id·파일명(302·305·403)은
바꾸지 않았다. 폴더 위치와 README·배너 서술 라벨만 갱신했다.

## Execution Loop

For every new major chapter or episode:

```text
production board update
-> chapter intent card
-> writer pass
-> critic / reader-sim pass
-> continuity pass
-> chronicler pass
-> verification
```

If a step is skipped, record why in this board or in the relevant GSD phase
brief.

## Verification Log

| Date | Command or review | Result | Follow-up |
| --- | --- | --- | --- |
| 2026-06-21 | external AI writing systems gap audit | local patterns selected; install rejected | create templates and warn-first gate |
| 2026-06-21 | 002 restructuring review | origin=1부, Mara=2부, existing 114-210=3부 asset direction accepted as structure | choose 1부 POV before origin outline |
| 2026-06-21 | 029 Ch6 writer/chronicler pass | final human hearing drafted; `who may author loss` field mark and protected pending hook added | run prose/continuity review and validation before commit |
| 2026-06-21 | 030 origin B3-B7 writer pass (`complete-first-arc-novel`) | 역연산→경첩→큐/경보→구조→사다리 drafted; 닫는 mark `THE LOCK WAS THE CROWN`; Mara handoff에서 029로 연결 | 030↔029 continuity + 029 AI-tell/harness scan + validation before commit |
| 2026-06-21 | 117 B3-B7 harness self-check | em dash 0, 박- embed-verb 0, Karvath 미등장/Vera 그림자 1회/Last Archive 미노출 노출예산 준수 | 029 동일 스캔 |
| 2026-06-21 | 030 reader-retention 9 persona 게이트 (중2/고2/일반/웹소설속독/순문학/문외한/안티AI/Chiang/SF) | 전원 완독·다음 편 진행=예; 공통 약점=B5b·B6 늘어짐, B3 인과 누락, AI-tell 경구 클러스터 | 윤문 패스 → 재검증 |
| 2026-06-21 | 117 B3-B7 deep AI-tell (ai-tell-detector ×2) + 윤문 16건 | 1차 S1 4건/S2 7건 → 윤문 → 재검증 "새 S1 없음", 안티AI "사람이 쓴 것처럼=예", 순문학 전 지적 개선 | release 시 정식 retention 게이트 |
| 2026-06-21 | 번호 physical cascade (002 §10) | 029 1부→2부, 025-027 2부→3부, _versions 동반 이동; 백링크·README(book1/2/3)·배너 일괄 갱신; validate_docs PASS | stable ID(파일명·arc_two doc_id) 보존 확인 |
| 2026-06-21 | 029 reader-retention 6 persona (일반/웹소설속독/순문학/문외한/안티AI/SF) + ai-tell-detector ×2 | 전원 완독·진행=예; 강점 Ch1·Ch4·Ch6; 공통 약점=프롤로그 세계사 infodump, "X아니라Y" 안티테제 30+회·격언 마무리·Ch6 6연 anaphora | 피드백 통합 → [30_revisions/009] |
| 2026-06-21 | 029 윤문 패스 13건 + 재검증 | 프롤로그 - 42→16줄 압축, Ch6 6연→3항, 격언/삼분/anaphora de-tell; 안티AI 재독 "프롤로그·Ch6 개선"; em dash 0·박- 0 | 인물 대사 안티테제·Ch5 강의는 release 게이트 잔여 |
| 2026-06-22 | 010 release-facing revision wave + validation | 030 B3-B7 경구형 문장 로그/화면 중심으로 낮춤; 029 프롤로그·Ch3·Ch5·Ch6 압축; `validate_docs`, `research_consistency`, full `fiction_gate`, staged workflow/fiction gates, pre-commit all PASS | formal 9-persona retention gate before release promotion |
| 2026-06-22 | retention gate artifact hardening | workflow/template/011 protocol added; prior chat-only or summary-only retention claims are not release gates | fill 011 persona sheets and issue ledger before any release promotion |
| 2026-06-22 | 031 origin 웹소설 콘티 텔링 정식 retention gate (RG-031-20260622-1308777, 7 persona: 중2/속독/문외한/순문학/안티AI/SF/피곤) | ran_passed_with_risks — 7/7 완독·진행=예, S0 0; 반복 S1 3건 open(RET-001 U5 중반 정체, RET-002 제도어 과부하, RET-003 도입·엔딩 거푸집) | [30_revisions/012](../30_revisions/012_origin_sael_webnovel_retention_gate_run_20260622_1308777_ko.md); revision wave 후 새 baseline 재실행으로 ran_passed 도달 권장 |
| 2026-06-22 | 031 revision wave 1 후 retention 재게이트 (RG-031-20260622-bdff1c7, 동일 7 persona) | ran_passed_with_risks — 7/7 재완독; RET-001 완전 해소(U5 페이싱), RET-002/003 주요 병목(U3 제도어·도입) 해소·잔여 S2 강등; 신규 S2 RET-008('A가 아니라 B' 정형)·RET-010(U7 콘티/산문 중복) | [30_revisions/013](../30_revisions/013_origin_sael_webnovel_retention_gate_run_20260622_bdff1c7_ko.md); RET-008·107 polish(rev wave 2) 후 release 시 최종 재실행 |
| 2026-06-22 | 031 polish wave 2 후 최종 확인 retention 게이트 (RG-031-20260622-b5f0edf, 동일 7 persona) | **ran_passed** — 7/7 완독, S0 0, open S1 0; RET-008/010 closed·improved, 잔여는 전부 S2/S3 backlog(RET-009 U6 제도어·108 무판정 용어·204 단문 리듬·109 손 모티프·002 한자말) | [30_revisions/014](../30_revisions/014_origin_sael_webnovel_retention_gate_run_20260622_b5f0edf_ko.md); 1부 origin 텔링 리텐션 통과. 다음=영어 Anglophone 각색판 |
| 2026-06-22 | 033 origin 풀길이 소설(8장 - 45K) 신설 + retention+comprehension 게이트 (RG-033-c91e9be, 7 persona) | retention **ran_passed_with_risks** + comprehension **ran_passed** — 7/7 완독·S0 0; 이해 C1-C4 전원 can_explain, C5 오분류 0(작가 '이해 안 됨' 지적 해소, 특히 기술문외한 P3 '확 나아짐'). 잔여 S1=중반 5-7장 반복(RET-016, deferred), S2=거푸집(RET-017)·1장 도입 정서동원(RET-018)·비유 반복(RET-019) | [30_revisions/015](../30_revisions/015_origin_sael_fullnovel_retention_comprehension_gate_20260622_c91e9be_ko.md); 콘티(118)는 blueprint·117은 flat 프로토타입으로 보존 |
| 2026-06-22-23 | 034 2부 마라 풀길이 소설(6장 본문 - 65K) 신설 + retention+comprehension 게이트 (RG-034-a41bcb9, 7 persona) | retention **ran_passed_with_risks** + comprehension **ran_passed** — 7/7 완독·S0 0; 이해 C1-C4 전원 can_explain, C5 오분류 0, **전원 "1부 미독자도 따라옴"**(독립 온보딩 성공), P3 6장 물리 '확' 이해. 잔여 S1=거푸집 후렴 반복(RET-2B-001), S2=6장 물리댐/길이·QFUDS 한 줄 설명·3장 추상·분기 논리 | [30_revisions/016](../30_revisions/016_mara_fullnovel_retention_comprehension_gate_20260623_a41bcb9_ko.md); 1부(120)+2부(121) 풀길이 두 권 완성 |
| 2026-06-30 | 외부 도구/코드 adoption 규칙 픽션 한정 해제(user decision); fiction-production 스킬·IP 워크플로우·이 board 정합 | inspiration-only/no-copy → 라이선스+출처 기록 하에 adoption 허용으로 변경. 연구 증거 경계는 불변 | 외부 도구 채택 시 source/license/allowed·blocked claim·workflow state를 변경 문서에 기록 |
| 2026-06-30 | continuity 엔진 파일럿(2부 마라 034 기준): `fiction_continuity.py` 전체 실행 + intent-mark suppression 신설 | 직전 8개 플래그(1부 030-033이 2부 마라·엘리아스 선행 참조)는 전부 **의도된 딥타임 시딩**으로 판정 → 209 `## 의도된 교차 등장` 허용목록에 (인물·부·파일번호)로 등록 → 엔진 **PASS**(9인물/9원고, strict 0). 민감도 회귀 테스트: 미등록 파일/인물의 교차는 여전히 플래그. 034 단독 0 플래그(2부 정합). validate_docs·research_consistency PASS | 침묵=신뢰 상태 확보. 새 1부 챕터가 2부 인물을 의도 참조하면 209 허용목록에 파일번호 추가; 의도 아니면 그대로 두고 수정 |
| 2026-07-01 | 세계 확장 웨이브 1 착수 + universe 레벨로 배치: 듄급 밀도 목표로 고유명사 대량 생성 1차 웨이브(명명법 백본 + 장부 가문 6가문·라우어 감사조직·베일 세포·유목 부족 등 하위 분파 + 신규 인물 14(빈 좌표만) + 지명·성계 15+ + 명명 사건 20+ + in-world 어휘집). 109/209 대조로 기존명 재배정 0, 복원=사본·필드마크·실존집단 비대응 가드 준수. **레벨 결정(사용자):** 공유 세계 대사전은 한 시리즈가 아니라 universe 공유 세계라 `qfuds-verse/10_world/117`로 배치(story_design 322에서 git mv). 새 universe는 안 만듦(같은 전제, Universe Inheritance Rule) | candidate @ universe 10_world. 109(명칭)·209(인물)·102(세력)·115/116(사건)로 웨이브별 승격 대기. "새 고유명사 금지"는 115/116 종합문서 한정 규율이며 생성 register엔 적용 안 됨(사용자 방향: 대량 생성) |
| 2026-07-01 | 근미래 프렐류드 예측 실행(멀티에이전트, 사용자 지시): 근미래 예측 패널(workroom 411)로 15렌즈가 2020s-2090s를 예측·생성 → story_design 322 근미래 대사전(신규 조직 75·인물 72·다층 타임라인 6시대). 실세계·물리 리서치 앵커 대장(workroom 412, 8클러스터, 중립·출처표·hit_not_cached)로 핍진성 근거 확보. 405에 근미래·물리 사유·성리학 창작입력 기록. 노동=재분류(304 IMF/ILO), 역량 A/B/C patchwork, convergesInto로 캐논 수렴 | candidate 전부 보류, 원고 수요 때 117 §7 6체크 승격. 예측 렌즈 2종(에너지·법제도) 스키마 실패로 미완=재실행 대상. 물리 substrate는 114·White Hole 스레드 in-world 사변 한정, QFUDS roadmap·status 불변. validate_docs·fiction_gate·research_consistency PASS |
| 2026-07-01 | 14도메인 세계-체계 스펙 00_bible 승격(경로 A, 사용자 승인): 411 스펙을 `00_bible/116_qday_world_system_14domain_matrix_ko.md`로 git mv, 프레이밍을 candidate→canon 부속(115 SSOT)으로 정정. 115에 부속 매트릭스 참조 추가, 000 권위 지도에 Q-Day 여파 세계-체계 행 추가, bible/workroom README·board 정합. 410은 워크룸 provenance로 보존 | 새 고유명사·인물·사건 0 유지. 026이 도메인 상세 우선. validate_docs·fiction_gate 재실행 |
| 2026-07-01 | 14도메인 세계-체계 확장 인계·스펙 신설(410·411): 작가 입력(전문가 패널 세분화)을 후보 인계 브리프(011)+14도메인 스펙(411)으로 저장. canon-guardian 충돌 분류(411 §1) 결과 hard-conflict 0, 14개 중 6개 확인(CONFIRMS)·2개 가드레일·2개 craft. "정보·기록·검증"은 신규 축이 아니라 기존 스파이스(검증경제/Aletheia) 재확인 | 새 고유명사·인물·사건 0(115 §0 하드 제약 준수). 00_bible 승격은 사용자 승인 게이트 대기; 권장=115 부속 매트릭스 병합(411 §5 경로 A) |
| 2026-06-30 | 1.5부 강등 + 새 1부 오르페우스 착수: 사엘 origin(030·031·032·033·README)을 `20_drafts/1부/`→`20_drafts/1.5부/`로 git mv; 새 1부 「오르페우스」(주인공 오웬·어머니 리브, 035 별도 작성) 자리 신설; continuity 엔진 `ARC_DIRS`/`ARC_ORDER`에 1.5부 삽입; 209 인물 표에 오웬·리브 추가 + 사엘 시대 1부→1.5부, 교차 허용목록 마라·엘리아스 1부→1.5부 | validate_docs PASS, fiction_continuity PASS (11인물/4원고 등록 후 시대 불일치 0). 035는 미생성(별도 작성 중)이라 엔진 미검사 | 035 초고 완성 후 retention/comprehension 게이트; 1부가 2부 인물 의도 참조 시 209 허용목록에 035 파일번호 추가 |
| 2026-07-02 | 125 Q-Day 두 위기 스파인 candidate→canon 승격(사용자 승인). 앵커 소프트 재정렬: 002/011(연도 척추: 21세기말=인식 위기 정점, Q-Day=인식위기 이후 먼 미래), 115(부 좌표: 0/1/1.5부=근미래 인식위기 Q-Day 이전, 2부=Q-Day 이후 먼 미래), 210(2090s=인식 위기 정점, 394/398 파열 시점 정정 + 상단 읽기 규칙) | validate_docs PASS. 두 위기 분리(딥페이크 인식위기 근미래 ↔ 양자 암호붕괴 Q-Day 먼 미래), 암호=최후 앵커→그마저 붕괴 논리 확정. 하드 연도 없음 | **잔여**: 210 §7-§10의 Q-Day-2090s 시점 표현 전면 정합은 chronicler pass 대상. 다음=122 오르페우스 ch2-8(이 2단 척추를 본문에서 전달) |
| 2026-07-06 | SAGA 단편 연작 선반 신설: 별도 QFUDS Verse anthology가 아니라 SAGA 내부 short-story cycle로 정정. 324 브리프와 `20_drafts/단편집/README` 생성 | validate_docs·fiction_gate 재실행 대상 | 다음=첫 단편 S1 `반려 버튼` intent card. 단편 초안은 canon이 아니며 chronicler pass 후 SAGA 기준 문서 반영 여부 결정 |
| 2026-07-06 | S1 `반려 버튼` intent card·한국어 primary 초고·chronicler pass 작성. 병렬 writer/continuity/reader-sim 출력을 반영하되 주요 SAGA 인물·Q-Day·Last Archive·제국 정치 미노출 유지 | validate_docs·research_consistency·fiction_gate 재실행 대상 | 다음=reader/continuity review 후 canon candidate 여부 결정 |
| 2026-07-06 | 901 P2 위생: 206 Core Drive 반복을 203·205·209·107 참조로 축약, 206 `status: reference` 승격, archive 018 깨진 019-024/012-017 링크를 현 보존 위치로 수정, archive 018 `status: provenance` 정정 | validate_docs·archive link smoke·continuity link smoke 재실행 대상 | Salt Fires 관련 Mara 세대 번호 등은 209 `결정 필요` 유지. 원고 수요 전에는 지어내지 않음 |
