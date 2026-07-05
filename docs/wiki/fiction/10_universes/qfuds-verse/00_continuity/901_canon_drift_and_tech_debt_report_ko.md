---
doc_id: qfuds_verse_canon_drift_and_tech_debt_report_ko
title: QFUDS Verse Canon Drift·Tech Debt 리포트 (드리프트 원장·중복·리팩터 우선순위)
doc_type: reference
stage: reference
status: provenance
evidence_role: provenance
depends_on:
  - qfuds_verse_worldbuilding_architecture_ko
  - qfuds_verse_continuity_index_ko
  - qfuds_saga_canon_authority_and_ssot_map_ko
  - qfuds_saga_restoration_mechanism_correction_ko
next_gate: P0(025/021 정정 전파)부터 사용자 승인 하에 본문 정정. 각 항목은 근거 문서와 함께 원장에 남는다
last_updated: 2026-07-06
---

# QFUDS Verse Canon Drift·Tech Debt 리포트 (드리프트 원장·중복·리팩터 우선순위)

## 무엇인가

[900 아키텍처 지도](900_worldbuilding_architecture_ko.md)의 자매 문서. in-scope 80개
문서에서 발견한 **캐논 드리프트·중복·기술부채**를 원장으로 남기고, 리팩터 우선순위를
P0/P1/P2로 세운다. **읽기 전용 진단서**다. 여기서 본문을 고치지 않는다. 각 정정은
사용자 승인 하에 별건으로 진행하며, 이 원장이 그 회귀 범위를 규정한다.

```text
fiction/provenance only
research evidence: no
external source claim: no
```

## 1. Canon Drift Ledger

드리프트 = 상위 캐논이 바뀌었는데 하위 문서 본문이 옛 프레임을 아직 들고 있는 상태.

| # | 드리프트 | 근거·영향 문서 | 우선순위 근거 규칙 | 상태·수정 방향 |
| --- | --- | --- | --- | --- |
| D1 | **근미래 리센터(025) 부·시대좌표 라벨 잔존** | bible-008·012·016·019이 "1부/마라/Liora/먼 미래" 이전 라벨 보유. 002·018은 딥타임 캐논이라 리센터가 무효화하지 않음(월드 사실 유지) | 024·025·027 우선 | **부분 완화됨.** 해당 문서 상단에 리센터 배너 존재. 최종 정리 시 본문 라벨을 024 기준으로 치환하는 pass 필요(사용자 DRIFT-008과 동일) |
| D2 | **"부활/복원" 현대 gloss** | 021 §5가 005·002·007·011을 지목. 실제로는 005·002만 gloss 보유, 007·011은 잔재 없음 | **025 > 021** 최상위 | **해소됨(2026-07-01).** [038 원어 층](../10_world/038_far_future_native_lexicon_return_death_ko.md)으로 뿌리 정합. "부활/복원"은 현대 gloss, in-world 원어는 재현·N세대 귀환·해상·원리 재확인·새로 씀. 005·002 배너·021 §5 갱신 |
| D3 | **캐릭터 바이블 중복** | 012·016·019·024 4자 클러스터. Liora·Mara·Elias·Pell 핵심 정보 반복 | 024가 시대 좌표 SSOT | **의도된 layering으로 유지.** 016·019는 이미 상호 경계 주석·리센터 배너 보유. 병합하지 않음. 단 시대좌표·원본/사본 상태는 024로만 확정(사용자 DRIFT-010과 동일) |
| D4 | **candidate 승격 백로그** | 웨이브 030-035, 037 이기론, 038 원어 층, 027 프렐류드, story_design 011(4-6부), 014 sovereign-AI 모두 candidate | 승격 SSOT=015·024·003·026·028 | 승격 게이트 정식화(§4). 과잉승격 위험은 아래 DRIFT-005 참조 |
| D5 | **번호 체계 오해 소지** | 전역 유니크 000-038에서 029만 비어 보임 | 범위 경계 | 029는 결번 아님. `20_drafts/2부`에 존재(범위 밖). 문서화로 오해 제거(§5) |

### 1.1 로컬 정독 루프에서 추가된 드리프트 (루프 2-4, 2026-07-01)

정독 진행률: **고정 범위 완독 완료** (00_continuity · 10_world · 00_bible · 00_workroom ·
10_story_design 완료, 40_release는 README+900 매니페스트로 인덱스 완료). drafts/revisions/
archive는 고정 범위 밖(확장 여부는 사용자 결정). 루프 2-5가 아래를 추가 확인했고, D1-D5와
겹치는 항목은 위 표에서 상태로 반영했다.

| # | 드리프트 | 관련 문서 | 처리 |
| --- | --- | --- | --- |
| DRIFT-005 | Candidate 웨이브 과잉승격 위험 | 030-035 | "candidate" 배너 유지. 원고 등장 순간 030 §7 6체크로 개별 승격 판정 |
| DRIFT-006 | Vera / Vera Dace 이름 충돌 | 031 | Last Archive 핵 Vera와 철자 근접. 승격 전 Bera Dace 등 개명 권장 |
| DRIFT-007 | craft domain의 in-world 오인 | 028(13·14), 035 | 생산측 렌즈이며 in-world canon 아님. "production-side only" 라벨 유지 |
| DRIFT-008 | bible 내 리센터 이전 부 라벨 잔존 | 008·012·016·019 | D1로 흡수. 배너 유지, 최종 라벨 치환 pass 필요 |
| DRIFT-009 | 004 Naming Table vs 015 명칭 SSOT | 004·015·016 | formal faction name은 015 우선(016은 Domus Clavium 공식·House Tabularii 폐기 명시). 004 Naming Table을 015 기준으로 재검수 대상 |
| DRIFT-010 | Character Canon 중복 | 012·016·019·024 | D3로 흡수. 의도된 reference layering. 시대좌표·원본/사본 상태만 024로 확정 |
| DRIFT-011 | **Migration compatibility layer** (본문 미이관, disclaimer로만 차단) | 008·012·016·019 등 | 리센터가 본문을 고친 게 아니라 상단 20줄 disclaimer로 막아둔 상태. 배너는 안전판이지 이관 완료 아님. **Chronicler Pass**(§6 P1)로 본문 라벨을 024 기준 치환하면 문서 품질 상승 |
| DRIFT-012 | 004 Naming Layer에 예전 명칭 소량 잔존 | 004·015 | DRIFT-009 정련. 하드 충돌은 없음(015만 보면 해소). Chronicler Pass에서 자동 정리 가능 |
| DRIFT-013 | 019 Arc Sheet가 012·016 Core Drive 일부 반복(중복률 20-30%) | 012·016·019 | D3/DRIFT-010 정련. 019는 Arc 변화가 본령이므로 반복 Core Drive는 "012·019 참조"로 축약 가능(의도된 layering 훼손 없이) |
| DRIFT-014 | workroom 일부가 legacy 번호 체계 유지 | 004·006·007 | 004 "2부"=새 체계 3부, 007 029=legacy sprint. workroom은 provenance라 삭제 대신 "legacy/reference" 라벨 유지, 실제 실행은 production board(009) 기준 |
| DRIFT-015 | 운영 선반이 release/revision 링크 다수 참조 | 003·004·005·007 | 30_revisions·20_drafts는 범위 밖이나 workroom이 자주 참조. 링크는 허용, 완독 범위에선 참조만 기록(release 판단 별 루프) |
| DRIFT-016 | Truth-State Ledger가 빈 모듈(TBD) | 008 | **해소 착수(2026-07-01).** workroom 014로 초안 작성: 부 단위 원장 + 1.5부 B1-B7 비트 + 떡밥 회수 원장 + 5대 질문 축. 남은 부(0부 세부·2부 마라·3부)는 story_design 완독 뒤 채움 |
| DRIFT-017 | 10_story_design 내부 번호 체계 혼재 | 007·009·010·011·012·016 | 새 구조는 024 기준인데 일부 제목·본문이 legacy "1부/2부/Arc Two" 유지. 실행 기준=011 §10+024. stable ID 정책상 제목 보류 가능하나 상단 경고 유지. Chronicler Pass 대상 |
| DRIFT-018 | 012/013 Mara reboot vs 016/017 Sael origin 병렬성 | 012·013·016·017 | 둘 다 "1부" 계열로 보이나 현 구조에선 사엘=1.5부/별도 origin, Mara=2부 자산. README·009 board에서 진입 경로 계속 강제 |
| DRIFT-019 | story_design brainstorm의 승격 위험 | 014·027 | 014 sovereign-AI 축·027 프렐류드는 brainstorm/candidate. 선택된 씨앗만 bible 승격. candidate/brainstorm 라벨 유지(DRIFT-005와 동류) |
| DRIFT-020 | 새 1부 체계와 기존 사엘 origin 체계 병존 | 016-023·024·025 | 016-023은 사엘 origin 중심 설계, 024·025가 오르페우스/캐스/사엘로 재중심화. 폐기 말고 "1.5부 사엘 origin 실행 패키지"로 라벨 고정 |
| DRIFT-021 | 027 candidate 과잉밀도 | 027 | 신규 조직·인물·사건 대량 생성. 상단 candidate 경고 유지, 030-035와 같은 6체크 승격 게이트(DRIFT-005 동류) |
| DRIFT-022 | 023 "복제품" 쉬운 표현 | 023 | 독자 오리엔테이션에서만 허용. canon 문서는 "사본/재구성체" 사용(025·021 정밀 구분). 038 원어 층과도 정합 |

## 2. Deprecated / 구프레임

- **복원=부활(엔트로피 역전 가능)**: 폐기됨. [021 복원 메커니즘 정정](../10_world/021_restoration_mechanism_correction_ko.md)이
  복원=열역학적으로 비가역인 손실 사본으로 확정했고, [025 in-world 물리](../10_world/025_in_world_physics_information_unitarity_restoration_ko.md)가
  "미리 존재하는 원본 없음"(마라의 두 읽기)로 최상위에서 이긴다. D2 대상 문서의 옛 문구는
  개념이 아니라 **표현**만 남은 잔재다.
- **단일 초월 AGI로서의 Last Archive**: 폐기됨. Last Archive는 [010](../10_world/010_last_archive_origin_and_reversal_causality_ko.md)에서
  합의의 신격화이지 전지한 단일 AI가 아니다. 초월자는 "합의를 깨는 인간"으로만 등장한다.
- 위 두 구프레임을 새 문서에서 다시 끌어오지 않는다.

### 2.1 전문 완독 감사(멀티에이전트, 12에이전트 · 80문서)가 확인한 추가 드리프트

프론트매터 그래프·스캔 위에 80문서 본문 완독 감사를 돌린 결과가 D2 해소 방향을 뒷받침했다.
000이 "005·002의 완전복원/역연산을 작중 금지·논쟁 이론으로 강등"으로 이미 기록하고 있었고,
011은 본문이 "재구성·금지 기술 한정"으로 이미 정합돼 D2 대상이 아님이 재확인됐다. 완독이
집어낸 추가 구체 드리프트(문구 단위):

| # | 드리프트(문구) | 문서 | 처리 |
| --- | --- | --- | --- |
| D6 | "1부=Cryptographic Death"·"사엘 origin=1부" | 002 | 024 시대좌표(1부 오르페우스=Q-Day 직후, 사엘=1.5부)와 충돌하는 리센터 이전 부 라벨. D1 라벨 치환 pass에 포함 |
| D7 | Baseline "In-world chronology: not fixed / Era IDs: not fixed" | 00_continuity/README | 002 연표 골격·024 부 번호 확정 이후의 잔존 표기. 소프트 정책 유지 여부는 작가 판단(하드락 아님) |
| D8 | "완벽하게 재구성"(독자 훅 질문) | 001 | 021(반복할수록 흐려지는 손실 사본)과 약한 긴장. 038 원어 층·021 앵커로 흡수, 강도 낮음 |

전체 구조화 추출 원본(80문서 role·authority·drift·deprecated·terms·overlap)은 감사 실행 산출물로
남는다(세션 워크플로 `wf_8e897838-e3d`).

## 3. 중복·병합 후보

| 후보 | 상태 | 제안 |
| --- | --- | --- |
| 016 앙상블 보이스·관계 ↔ 019 입체 시트 | 인물 심층 정보가 양쪽에 흩어짐 | 019=심층 시트(개인 내면 SSOT), 016=관계·보이스(상호작용 SSOT)로 경계 명문화. 겹치는 프로필은 019로 단일화하고 016은 019를 참조 |
| 012 주인공 · 024 지도·좌표 | 012=Liora 개인 SSOT, 024=시대 좌표 SSOT로 이미 분리 | 유지. 단 016/019가 024 좌표를 재기술하지 않도록 링크로만 참조 |
| 026 여파 · 028 14도메인 | 028이 026 부속으로 명시됨 | 유지(중복 아님, 부속 관계). |

병합은 캐릭터 SSOT를 하나로 모아 story_design·drafts가 참조할 단일 출처를 만드는 것이 목적.
실제 병합은 P1에서 사용자 승인 하에.

## 4. Candidate 승격 백로그 + 게이트 제안

전부 candidate이며 승격 경로가 문서마다 흩어져 있다. 공통 게이트를 제안한다.

| candidate | 선반 | 승격 타깃 SSOT |
| --- | --- | --- |
| 030-035 세계 확장 웨이브 | 10_world | 명칭→015, 세력→003, 여파→026 |
| 037 이기론 | 10_world | 003·026 진자·025 물리 |
| 027 근미래 프렐류드 | story_design | 026·002·bible-027 |
| story_design 011 4-6부 | story_design | 011 아크 지도 |
| 014 sovereign-AI 축 | story_design | 022·023 |

**제안 게이트(승격 6점검):** (1) 신규 고유명이 015 명칭과 충돌 없음, (2) 025/021 물리와
모순 없음, (3) 026 여파 타임라인에 착지, (4) em dash 0·"박-" 슬랭 0·강의조 없음,
(5) 실존 집단 비대응, (6) 승격 시 상위 SSOT의 `depends_on`/인덱스에 배선. 통과분만 candidate에서
canon으로 올리고 이 원장에 기록한다.

**2026-07-06 승격 기록(사용자 승인, Fable 2차 pass):** 038 원어 층 canon 승격(000 등재).
036 정식 승격 마감. 031 §1.4 베이르→Ordo Salis 평신도 계보 확정(탐 소르 024 등록, Salt
Fires 정의는 024 §Salt Fires + 015 비세력 고유명 등록). 024는 039 두 위기 스파인에 재정렬.
Vera–Mara는 계보 확정 없는 주제적 거울로 통일(010·018·019·story 008·workroom 014,
의도된 모호성). 030~035 나머지·027 프렐류드·037·040·014는 candidate 유지. D2 관련 038
depends_on 역배선(021·002·005)은 P1 chronicler pass 잔여 항목.

## 5. Tech Debt

- **집행층 공백(005·008 진단):** 실패 원인은 도구 부재가 아니라 **미집행**이다. 시트·감사·
  하네스는 있으나 필수 게이트가 없어 집필에서 건너뛰었다(005). 008이 필요 집행 모듈 6개를
  지정한다. 현재 상태:

  | 008 필요 모듈 | 상태 | 위치 |
  | --- | --- | --- |
  | Production Board | 있음 | workroom 009 |
  | Chapter Intent Card | 템플릿 있음 | workroom 010 |
  | Chronicler Pass | 개념 있음·미집행 | §6 P1(본문 라벨 이관) |
  | Review Wave Protocol | 부분 | 005 하네스 |
  | QFUDS Style Packet | 부분 | 003 글로서리·스타일 가드 |
  | **Truth-State Ledger** | **초안 작성됨** | workroom 014(2026-07-01, DRIFT-016 해소착수) |

- **Migration compatibility layer(최대 부채, DRIFT-011):** 리센터는 본문을 이관한 게 아니라
  다수 문서(008·012·016·019 등) 상단 20줄 disclaimer로 옛 구조를 막아 두었다. 배너는 안전판
  이지 이관 완료가 아니다. 이 상태가 "이관 끝"으로 오독되면 옛 라벨이 산문으로 새어 나간다.
  해소는 아래 **Chronicler Pass**(§6 P1): 배너를 걷고 본문 라벨을 024/025/027 기준으로 치환.
- **status 신호 소실:** 80개 중 78개가 `status: draft` 고정(예외: story_design 012·013=completed,
  release 900=provenance). 안정 문서까지 draft라 status가 진행도 신호로 무용하다. 안정 문서는
  `reference`로 승격해 "아직 유동적인 것"과 구분하자(P2).
- **고아 신규 캐논:** 036·037·027(story_design)이 어떤 문서의 `depends_on`에도 없다(README에만
  등록). 소비 문서로 배선되지 않은 미승격 후보다. 승격/배선 전까지 다른 문서가 이들을 근거로
  삼지 못한다(P1).
- **000 권위 지도 피의존 0:** 루트라 예상되나 교차링크가 약하다. 900/901에서 상호링크로 보강함.
- **범위 경계 교차 의존 24건:** in-scope 문서가 `20_drafts`/`30_revisions` id를 `depends_on`.
  대부분 의도적(bible·story가 산문 원고를 근거로 참조). 주시 대상: bible-008(원고 7건 참조),
  10_world/025(revisions seed 참조), story_design/012·013(completed, 원고 참조). 원고가
  reboot로 교체되면 이 링크들의 대상이 사라질 수 있으니 승격 시 재확인.

## 6. 리팩터 우선순위 (P0/P1/P2)

### P0 (지금, 캐논 정합 직결)
- **025/021 정정 전파(D1·D2):** 복원=손실 사본·원본 없음을 리센터 배너 6문서
  (002·018·bible-008·bible-012·story_design-009·023)와 잔재 문서(005·002·007·011) 본문에 반영.
  회귀 점검 강도 최상(010 계열 다수 포함).

### P1 (다음, 구조 정리)
- **Chronicler Pass(DRIFT-011·D1·D6):** 리센터 이전 disclaimer로 막아둔 본문을 실제 이관.
  배너를 걷고 "1부/사엘=1부/마라·Liora=1부/먼 미래가 무대" 등 옛 라벨을 024(시대좌표)·
  025(리센터)·027(관통선) 기준으로 치환. 대상 시작점 008·012·016·019·002. 004 Naming
  잔재(DRIFT-012)도 015 기준으로 함께 정리. 산문·본문에 손대므로 사용자 승인 하에 별 pass.
- **Truth-State Ledger 작성(DRIFT-016·008):** 008이 지정한 6모듈 중 유일한 빈 모듈. 장별
  "인물이 아는 것 / 독자가 아는 것 / 세계가 확정한 것 / 열린 모순" 표를 실제 문서화. 리빌
  설계(story_design 008·021)·인물 지식(024)과 물리므로 story_design 완독(루프 5) 뒤 착수 적기.
- **캐릭터 layering 축약(D3·DRIFT-013):** 019가 반복하는 Core Drive를 "012·016 참조"로 축약
  (중복률 20-30%). 병합이 아니라 참조화. 시대좌표·원본/사본 상태는 024로만 확정.
- **고아 신규 캐논 배선:** 036·037·038·027을 소비 문서(036→002·011, 037→003·026·025,
  038→021·025·037·011, 027→026·bible-027)의 `depends_on`/인덱스에 배선.

### P2 (정비, 위생)
- **status 위생:** 안정 문서 draft→reference 승격.
- **029 결번 문서화:** 범위 경계 아티팩트임을 000/README에 각주.
- **웨이브 030-037 승격 게이트 정식화(§4):** candidate→canon 절차 명문화.

## 7. Impact 표 (수정 시 회귀 점검 필수)

블라스트 반경(피의존) 순. P0 정정 시 아래 상위 문서를 함께 회귀 점검한다.

| 문서 | 피의존 | P0에서 건드리나 |
| --- | --- | --- |
| 010 Last Archive | 18 | 간접(연결 문서 다수) |
| 002 딥타임 | 10 | 예(D1·D2 대상) |
| 017 비트코인 / 015 질문 | 10 | 간접 |
| 026 Q-Day 여파 | 8 | 간접(정합 확인) |
| 007 암호죽음 | 7 | 예(D2 대상) |
| 003·013·024·009·016 | 7 | 부분 |

근거·상위 참조: [900 아키텍처 지도](900_worldbuilding_architecture_ko.md) ·
[000 권위 지도](000_canon_authority_and_ssot_map_ko.md) ·
[021 복원 정정](../10_world/021_restoration_mechanism_correction_ko.md) ·
[025 in-world 물리](../10_world/025_in_world_physics_information_unitarity_restoration_ko.md).

```text
fiction/provenance only
research evidence: no
external source claim: no
```
