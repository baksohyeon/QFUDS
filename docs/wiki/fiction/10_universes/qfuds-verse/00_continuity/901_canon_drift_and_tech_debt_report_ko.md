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
last_updated: 2026-07-01
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

| # | 드리프트 | 근거·영향 문서 | 우선순위 근거 규칙 | 수정 방향 |
| --- | --- | --- | --- | --- |
| D1 | **근미래 리센터(025) 미전파** | 025가 무게중심을 근미래 grounded SF로 옮겼으나 002·018·bible-008·bible-012·story_design-009·023이 옛 어조·시대 좌표 유지 | 026(여파)·024(좌표) 우선 | 리센터 배너/시대 좌표를 025·026 기준으로 정렬 |
| D2 | **복원=부활 옛 표현 잔재** | 021이 005·002·007·011을 "부활/복원(엔트로피 역전)" 옛 문구 보유로 지목 | **025 > 021** 최상위 | 본문 문구를 "복원=손실 사본"으로 교정(개념은 이미 021·025가 이김) |
| D3 | **캐릭터 바이블 중복** | 016 앙상블 보이스·관계 ↔ 019 입체 시트 겹침. 012 주인공·024 좌표와 4자 클러스터 | 024가 시대 좌표 SSOT | 016↔019 경계 재정의 또는 병합(§3) |
| D4 | **candidate 승격 백로그** | 웨이브 030~035, 037 이기론, 027 프렐류드, story_design 011(4~6부), 014 sovereign-AI 모두 candidate | 승격 SSOT=015·024·003·026·028 | 승격 게이트 정식화(§4) |
| D5 | **번호 체계 오해 소지** | 전역 유니크 000~037에서 029만 비어 보임 | 범위 경계 | 029는 결번 아님. `20_drafts/2부`에 존재(범위 밖). 문서화로 오해 제거 |

## 2. Deprecated / 구프레임

- **복원=부활(엔트로피 역전 가능)**: 폐기됨. [021 복원 메커니즘 정정](../10_world/021_restoration_mechanism_correction_ko.md)이
  복원=열역학적으로 비가역인 손실 사본으로 확정했고, [025 in-world 물리](../10_world/025_in_world_physics_information_unitarity_restoration_ko.md)가
  "미리 존재하는 원본 없음"(마라의 두 읽기)로 최상위에서 이긴다. D2 대상 문서의 옛 문구는
  개념이 아니라 **표현**만 남은 잔재다.
- **단일 초월 AGI로서의 Last Archive**: 폐기됨. Last Archive는 [010](../10_world/010_last_archive_origin_and_reversal_causality_ko.md)에서
  합의의 신격화이지 전지한 단일 AI가 아니다. 초월자는 "합의를 깨는 인간"으로만 등장한다.
- 위 두 구프레임을 새 문서에서 다시 끌어오지 않는다.

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
| 030~035 세계 확장 웨이브 | 10_world | 명칭→015, 세력→003, 여파→026 |
| 037 이기론 | 10_world | 003·026 진자·025 물리 |
| 027 근미래 프렐류드 | story_design | 026·002·bible-027 |
| story_design 011 4~6부 | story_design | 011 아크 지도 |
| 014 sovereign-AI 축 | story_design | 022·023 |

**제안 게이트(승격 6점검):** (1) 신규 고유명이 015 명칭과 충돌 없음, (2) 025/021 물리와
모순 없음, (3) 026 여파 타임라인에 착지, (4) em dash 0·"박-" 슬랭 0·강의조 없음,
(5) 실존 집단 비대응, (6) 승격 시 상위 SSOT의 `depends_on`/인덱스에 배선. 통과분만 candidate에서
canon으로 올리고 이 원장에 기록한다.

## 5. Tech Debt

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
- **016↔019 병합/경계 정리(D3·§3):** 캐릭터 SSOT 단일화.
- **고아 신규 캐논 배선:** 036·037·027을 소비 문서(036→002·011, 037→003·026·025,
  027→026·bible-027)의 `depends_on`/인덱스에 배선.

### P2 (정비, 위생)
- **status 위생:** 안정 문서 draft→reference 승격.
- **029 결번 문서화:** 범위 경계 아티팩트임을 000/README에 각주.
- **웨이브 030~037 승격 게이트 정식화(§4):** candidate→canon 절차 명문화.

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
