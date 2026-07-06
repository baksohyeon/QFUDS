---
doc_id: qfuds_saga_revisions_origin_sael_webnovel_retention_gate_run_20260622_1308777_ko
title: 031 origin 웹소설 콘티 텔링 Retention Gate Run 2026-06-22 1308777
doc_type: gate
stage: reference
status: completed
evidence_role: provenance
depends_on:
  - qfuds_saga_revisions_first_second_arc_formal_retention_gate_protocol_ko
  - qfuds_saga_drafts_origin_sael_webnovel_storyboard_ko
next_gate: 차기 revision wave에서 S1(RET-001~003) 처리 후 새 baseline으로 재실행. release 승격 전 ran_passed 권장
last_updated: 2026-07-06
---

# 031 origin 웹소설 콘티 텔링 Retention Gate Run 2026-06-22 1308777

## Metadata

- Work id: qfuds-saga / 1부 origin (사엘)
- Gate id: RG-031-20260622-1308777
- Scope: `031_origin_sael_webnovel_storyboard_ko.md` 회차1~7(B1~B7) 전체, 첫 정식 retention run
- Source draft(s): 031 origin 웹소설 콘티 텔링 (030의 자매 텔링)
- Baseline commit/date: 1308777 / 2026-06-22
- Gate owner mode: `reader-sim` + `critic` + `chronicler`
- Production board: [408 production board](../00_workroom/408_saga_production_board_ko.md)
- Revision shelf output: 이 문서(30_revisions/012)
- Release target: 미정(1부 origin 텔링 draft). 이 run은 draft 진단용, release 승격은 별도

## Immutable Run Rule

이 문서는 baseline 1308777에 대한 고정 run 아티팩트다. 원고가 바뀌면 덮어쓰지 않고
새 baseline으로 새 run 문서를 만든다. 그때 이 문서를 `depends_on`에 적는다.

## Boundary

```text
fiction/provenance only
research evidence: no
release promotion without this artifact: no
raw private reasoning: do not record
```

## Source Baseline

| Source id | Path | Baseline commit | Blob hash | Notes |
| --- | --- | --- | --- | --- |
| S1 | 20_drafts/1부/031_origin_sael_webnovel_storyboard_ko.md | 1308777 | 83fcc975c0745605f1622e8dec0fa895f962b11b | 회차1~7 완본 |

## Persona Set

| Persona id | Reader profile | What this persona tests | Stop rule |
| --- | --- | --- | --- |
| P1 | 중학교 2학년(14세), 웹툰/웹소설 O, 암호 0지식 | 배경지식 0 어린 독자의 이해·지속 | 지루하거나 이해 안 되는 첫 지점 |
| P2 | 웹소설 속독(하루 수십 편) | 회차 후킹·절단·늘어짐, 콘티/산문 중복 | 다음 편 안 누르고 싶은 첫 지점 |
| P3 | 40대 기술 문외한 | 암호 개념 온보딩 전달력 | 이해 안 돼 그만두고 싶은 첫 지점 |
| P4 | 까다로운 순문학 독자 | 문장·톤·진부/작위, 콘티가 격을 깎는가 | 문장이 견디기 힘든 첫 지점 |
| P5 | 안티-AI 냉소가 | 잔존 AI-tell(병렬·요약결말·거푸집) | AI 티로 신뢰 깨지는 첫 지점 |
| P6 | SF 애호가(Chiang/Egan 취향) | 개념의 논리·함의·전개 속도 | 개념이 얕거나 논리 깨지는 첫 지점 |
| P7 | 30대 피곤한 일반 독자(취침 전) | 평범 대중의 회차 지속력 | "그만 자야지" 첫 지점 |

## Reading Units

| Unit | Source ref | Role | Expected hook |
| --- | --- | --- | --- |
| U1 | 1308777:.../031#L105-232 | B1·B2 도입 | 확인 막대가 거꾸로 열린다 |
| U2 | 1308777:.../031#L233-376 | B3 역연산 | 처음으로 멈추라고 안 누른다 |
| U3 | 1308777:.../031#L377-501 | B4 도장 | 마지막 "아니오" 자리가 책상으로 |
| U4 | 1308777:.../031#L502-594 | B5a 폭증 | 사십만+ 경보 |
| U5 | 1308777:.../031#L595-678 | B5b 경보 | 단 하나의 자리가 질서를 세운다 |
| U6 | 1308777:.../031#L679-771 | B6 자동화 | 지워진 이름 '베라' |
| U7 | 1308777:.../031#L772-871 | B7 첫 청구 | 마라 베이르 / THE LOCK WAS THE CROWN |

## Persona Result Sheets

전원 **완독**(7/7). 아래는 reading unit별 점수 매트릭스와 페르소나별 핵심 행이다.

### 몰입 점수 (1-10)

| Persona | U1 | U2 | U3 | U4 | U5 | U6 | U7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P1 중2 | 8 | 9 | 8 | 9 | 7 | 8 | 9 |
| P2 속독 | 7 | 8 | 7 | 8 | 6 | 6 | 8 |
| P3 문외한 | 8 | 9 | 8 | 9 | 8 | 9 | 9 |
| P4 순문학 | 7 | 8 | 7 | 6 | 6 | 7 | 8 |
| P5 안티AI | 7 | 8 | 7 | 6 | 6 | 7 | 7 |
| P6 SF | 8 | 9 | 8 | 8 | 7 | 8 | 9 |
| P7 피곤 | 8 | 8 | 7 | 7 | 6 | 7 | 8 |
| **중앙값** | **8** | **8** | **7** | **8** | **6** | **7** | **8** |

### 명료도/대체축 점수 (1-10, P5는 AI티 의심=낮을수록 양호로 환산, P6은 개념 견고함)

| Persona | U1 | U2 | U3 | U4 | U5 | U6 | U7 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | 8 | 9 | 7 | 9 | 7 | 8 | 8 |
| P3 | 8 | 9 | 7 | 8 | 7 | 8 | 8 |
| P4 | 9 | 9 | 8 | 8 | 7 | 8 | 8 |
| P6 견고함 | 9 | 9 | 8 | 8 | 7 | 8 | 9 |
| P7 | 7 | 7 | 6 | 7 | 6 | 7 | 8 |

### 페르소나별 핵심

| Persona | 완독 | 최대 위험 ref | 가장 센 훅 | 가장 큰 마찰 |
| --- | --- | --- | --- | --- |
| P1 | 완독 | U3 L444-456 | 마라 베이르 등장(U7) | U3 비준/기각/잠정도장 제도 용어 뭉치 |
| P2 | 완독 | U5 L643 / U6 L730 | "도둑이 아니라 기계"(U2)·점층·제목회수 | U5·U6 정서 중복 + 콘티/산문 1:1 중복 늘어짐 |
| P3 | 완독 | U3 L431-440 | L307 "기계가 자물쇠 보고 열쇠를 깎는다" | 암호는 OK, 회사 제도어(빈/미정 표식·봉인) 장벽 |
| P4 | 완독 | (없음) | L310-312 일방향성 한 문장 안착 | 망설임/자기-불투명 후렴구 반복(작위) |
| P5 | 완독 | (없음) | L307 재정의·판례 한 줄(U7) | 도입 "처음엔 X"·엔딩 "그가 본 건 하나" 거푸집 |
| P6 | 완독 | U5 L666-668 | U2 "장부 그대로/거래 유효/독점 서명권 무너짐" 네 줄 | U5 새 개념 밀도 최저(분위기 처리) |
| P7 | 완독 | U5 L643-650 | L307·L833 핵심 비유 두 줄 | 중반(U3~U5) 도장 딜레마 3회 반복 + 제도어 누적 |

## Cross-Persona Evidence Matrix

| Unit | 중앙 몰입 | 최저 몰입 페르소나 | 공통 이탈/위험 트리거 | 반복 혼란 | 강한 훅 합의 |
| --- | --- | --- | --- | --- | --- |
| U1 | 8 | P2/P4/P5 (7) | 중반 설명 문단(L187-190) 살짝 길다 | 서명/공개키 관계(P3) | catch-22 셋업, L229 거꾸로 열리는 문 |
| U2 | 8 | (최저 없음, 전 페르소나 최고점대) | 거의 없음 | 없음 | **L307 "기계가 자물쇠 보고 열쇠를 깎는다"(만장일치)** |
| U3 | 7 | P2/P4/P5/P7 (7) | L431-456 제도어 4종 뭉치 | 비준/기각/잠정도장/봉인 | "남의 삶 앞에서 멈췄다"(L465) |
| U4 | 8 | P4/P5 (6) | 수치 점층 나열 평탄(L564-570) | "근거 선례"(맥락으로 해소) | 사십만+경보 절단(L588-591) |
| U5 | **6 (최저 트로프)** | P2/P4/P5/P7 (6) | **U3·U4와 감정·논리 중복("또 도장 고민")** | 무판정(L643), 좌우대칭 딜레마 | "단 하나의 자리"(L666-668, 단 약함) |
| U6 | 7 | P2 (6) | L730-744 위임로그/권한계보 용어 밀도 | 위임/계보 | 지워진 이름 '베라'(L758) |
| U7 | 8 | P5 (7) | 양식 확장 나열 약간 늘어짐(L819-828) | 없음 | **판례 한 줄 + THE LOCK WAS THE CROWN(만장일치)** |

## Issue Ledger

| Issue id | Severity | Evidence personas | Source ref | Failure mode | Proposed fix | Owner mode | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RET-001 | S1 | P2,P5,P6,P7 | 1308777:.../031#L595-678 | U5(회차5)가 U3·U4와 감정(한 사람 살릴까)·깨달음(어느 쪽도 답 없음) 중복, 새 개념 밀도 최저 → 중반 정체·최대 이탈 위험 | U5에 '단 하나의 자리'의 압력을 앞당겨 가시화(새 압력 1개 투입)하거나 U5를 U4/U6로 흡수해 1회 압축 | writer | open |
| RET-002 | S1 | P1,P3,P7 | 1308777:.../031#L431-456 | 인월드 행정 용어(빈 표식·미정 표식·잠정 도장·무판정·봉인·위임 로그·권한 계보)가 회차마다 새로 쏟아져 비전문가 누적 부담. 암호 온보딩은 성공, 제도어는 욱여넣음 | "회차당 새 개념 1개" 원칙을 제도어에도 적용. 용어 수 감축·1개씩 풀어쓰기·반복 노출로 분산 | writer | open |
| RET-003 | S1 | P4,P5 (P2 보강) | 1308777:.../031#L171,L291,L496,L547,L762,L862 | 회차 도입("처음엔 X였다")·엔딩("그가 본 건 하나")·좌우대칭 딜레마 정리가 거푸집으로 반복 → 작위·AI티 의심 누적 | 도입/엔딩 구문 변주, 대칭 정리문 일부 비대칭화 | writer | open |
| RET-004 | S2 | P2(강),P4 | 콘티 vs 산문 전반 | 콘티(컷)와 산문이 같은 장면·대사·감정을 1:1 재생(중복 늘어짐). 콘티 '감정: 등골' 라벨은 정독 시 싸구려 | 연재 노출본은 콘티를 HTML 주석/별도 작화본으로 접기. 콘티 감정 라벨 정리 | writer | deferred |
| RET-005 | S2 | P6 | 1308777:.../031#L303-305 | 역산을 brute-force 후보 소거처럼 묘사(개념적으로 약간 헐거움) | "후보를 지운다" 뉘앙스를 구조적 역산 쪽으로 미세 조정 | writer | open |
| RET-006 | S2 | P6 | 1308777:.../031#L201-203 | catch-22로 멈춘 돈이 어떻게 검증대로 왔는지 한 박자 비약 | 한 줄 연결(결국 보냈다/시도하다 노출됐다 등) 또는 의도적 생략 명시 | writer | open |
| RET-007 | S3 | P3 | 1308777:.../031#L867 | 마지막 영어 mark가 비영어 독자에겐 멋부림 | 직전 한글 해석이 이미 풀어줌. field mark는 캐논이라 유지 | n/a | deferred |

`RET-004`·`RET-007` deferred 사유: 콘티 가시화는 사용자가 선택한 작화/시나리오 목적이며, 영어 field mark는 캐논 자산이다. 연재 release 시점에 노출본 분리로 처리.

## Decision

Gate state:

```text
ran_passed_with_risks
```

근거: 페르소나 7/7 전원 완독, 모든 회차 "다음 진행=예", **release-blocking S0 = 0.**
다만 반복 S1 3건(RET-001~003)이 미해결(open)이라 clean `ran_passed`는 아니다. release
승격은 차단되지 않으나(차단 상태는 not_run/invalid/ran_failed), release 전에 S1 처리
+ 새 baseline 재실행으로 `ran_passed` 도달을 권장한다.

Decision:

```text
ran_passed_with_risks — draft 진단 통과, revision wave(RET-001~003) 후 재실행 권장
```

## Revision Mapping

| Issue id | Fix wave/doc | Baseline source ref | Changed files | Fix commit/blob | Verification | Residual risk |
| --- | --- | --- | --- | --- | --- | --- |
| RET-001 | pending(차기 wave) | 1308777:.../031#L595-678 | 031 (예정) | pending | 재실행 RG | 중반 정체 |
| RET-002 | pending | 1308777:.../031#L431-456 | 031 (예정) | pending | 재실행 RG | 제도어 부담 |
| RET-003 | pending | 도입/엔딩 거푸집 | 031 (예정) | pending | 재실행 RG | AI티 의심 |

## Verification

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/agent_workflow_guard.py --staged
python3 scripts/fiction_gate.py --staged
sh scripts/git-hooks/pre-commit
```
