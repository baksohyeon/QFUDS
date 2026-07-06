---
doc_id: qfuds_saga_revisions_origin_sael_webnovel_retention_gate_run_20260622_bdff1c7_ko
title: 031 origin 웹소설 콘티 텔링 Retention Gate Run 2 2026-06-22 bdff1c7
doc_type: gate
stage: reference
status: completed
evidence_role: provenance
depends_on:
  - qfuds_saga_revisions_origin_sael_webnovel_retention_gate_run_20260622_1308777_ko
  - qfuds_saga_drafts_origin_sael_webnovel_storyboard_ko
next_gate: 잔류 S2(RET-008 반전 정형, RET-010 U7 콘티/산문 중복) polish 후 release 추진 시 최종 확인 재실행
last_updated: 2026-07-06
---

# 031 origin 웹소설 콘티 텔링 Retention Gate Run 2 2026-06-22 bdff1c7

## Metadata

- Work id: qfuds-saga / 1부 origin (사엘)
- Gate id: RG-031-20260622-bdff1c7 (2차, RET-001~003 revision wave 후)
- Scope: 031 회차1~7 전체 재실행. 1차(RG-031-1308777, [012](012_origin_sael_webnovel_retention_gate_run_20260622_1308777_ko.md))의 S1 수정 검증
- Baseline commit/date: bdff1c7 / 2026-06-22
- Gate owner mode: `reader-sim` + `critic` + `chronicler`
- Production board: [408](../00_workroom/408_saga_production_board_ko.md)
- Release target: 미정(draft 진단)

## Immutable Run Rule

이 문서는 baseline bdff1c7 고정 run이다. 1차 run([012])을 `depends_on`에 적었다. 이후
polish로 원고가 바뀌면 새 baseline 새 run 문서를 만든다.

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
| S1 | 20_drafts/1부/031_origin_sael_webnovel_storyboard_ko.md | bdff1c7 | 508d6cfd83633a3fe0668034b9368daae0e36736 | RET-001~003 수정본 |

Persona set·reading unit 정의는 [012] 상속(P1~P7, U1~U7). 신규 라인 범위:
U1 L105-232 / U2 L233-376 / U3 L377-500 / U4 L501-593 / U5 L594-673 / U6 L674-766 / U7 L767-866.

## Persona Result Sheets (2차)

전원 **완독**(7/7). 1차 대비 델타 중심.

| Persona | 완독 | U5 판정(1차 최약) | 1차 지적 해소 | 잔류/신규 지적 |
| --- | --- | --- | --- | --- |
| P1 중2 | 완독 | 6 (사건 없는 회차라 약간 처짐, 중단 아님) | U3 제도어 벽 뚫림(예) | 한자말 튐 '역연산'(L475)·'판례'(L799) |
| P2 속독 | 완독 | 부분 개선(새 압력 옳음, 산문 첫 문단으로 더 앞당기면 완벽) | U5 도장딜레마 반복 끊김, U5·U6 중복 거의 해소 | U5 산문 도입 3문단 후킹 약함(L636-649) |
| P3 문외한 | 완독 | 3/5 (가장 추상) | U3 제도어 평이화(예) | 부담이 U5'무판정'·U6'위임로그/권한계보'로 이동 |
| P4 순문학 | 완독 | 2/5 (작위 임계) | 도입 거푸집 변주됨(부분) | **좌우대칭/'A가 아니라 B' 통사 반복**(L646-649 등) |
| P5 안티AI | 완독 | 3 (양호) | 도입/엔딩 거푸집 끊김(부분) | **클라이맥스 'not A but B' 정형 + U7 콘티/산문 문장 중복**(L809=L858) |
| P6 SF | 완독 | 중(상향) | **U5 페이싱 살아남(예), U5/U6 개념 분리됨** | U7 사람=데이터 도약에 기술 발판 한 줄 권고 |
| P7 피곤 | 완독 | 3 (졸림 잡힘) | U5 졸림 구간 해소(예) | U3·U6 제도어 몰림 잔존(L443-455, L733-736) |

### 점수 요약 (전 회차 대비)

- 1차 최약 트로프였던 **U5가 회복**: P6 "중(상향)", P7 "졸림 잡힘", P2 "반복 끊김".
- **U3 제도어 병목 해소**: P1·P3 모두 "읽기 쉬워졌다".
- 새로 가장 높은 AI티 신호: P5가 U7=5(의심↑) — 콘티/산문 문장 중복 + 반전 정형.

## Cross-Persona Evidence Matrix (델타)

| 항목 | 1차 | 2차 | 판정 |
| --- | --- | --- | --- |
| U5 중반 정체(RET-001) | S1 (P2·P5·P6·P7) | 해소(페이싱·개념분리 확인) | **fixed** |
| 제도어 과부하(RET-002) | S1 (P1·P3·P7), U3 집중 | U3 해소, U5·U6로 일부 이동 | **partial** |
| 도입/엔딩 거푸집(RET-003) | S1 (P4·P5) | 도입 변주됨; 'A가 아니라 B' 정형으로 전이 | **partial → 신규 RET-008** |

## Issue Ledger (2차)

| Issue id | Severity | Evidence personas | Source ref | Failure mode | Proposed fix | Status |
| --- | --- | --- | --- | --- | --- | --- |
| RET-001 | S1→resolved | P2,P6,P7 | U5 | (1차) 중반 정체 | U5 '판정권 수렴' 새 압력 투입 | fixed (verified) |
| RET-002 | S1→partial | P1,P3,P7 | U3 해소 / U5·U6 잔존 | 제도어 과부하 | U3 평이화 완료. U6 위임로그/권한계보·U5 무판정 추가 평이화 | partial(잔여 S2) |
| RET-003 | S1→partial | P4,P5 | 도입 해소 / 정형 전이 | 거푸집 | 도입 변주 완료 → RET-008로 이관 | superseded |
| RET-008 | S2 | P4,P5 | bdff1c7:.../031#L646-649 외 | 클라이맥스 'A가 아니라 B' 반전 정형이 회차마다 반복(U3·U6 등). U2/U7 iconic 2개는 보존 | 중간 회차(U3·U6) 반전 통사 일부 변주 | open |
| RET-010 | S2 | P5 | bdff1c7:.../031#L809 vs L858 | U7 콘티 자막과 산문 훅이 거의 동일 문장 1:1 | 콘티 자막을 짧은 다른 표현으로 | open |
| RET-009 | S2 | P3,P7 | bdff1c7:.../031#L733-736 | U6 위임로그/권한계보 제도어 몰림 | 1개로 풀어쓰기 | open |
| RET-011 | S3 | P1 | bdff1c7:.../031#L475,L799 | '역연산'·'판례' 한자말이 평이 흐름에서 튐 | 첫 등장에 한 줄 평이 병기 | open |
| RET-012 | S3 | P6 | bdff1c7:.../031#L831-833 | 사람=데이터 도약에 기술 발판 부재(2부 이월이라 의도적) | 선택: 한 줄 발판 또는 2부로 유지 | deferred |

## Decision

```text
ran_passed_with_risks
```

근거: 2차에도 7/7 완독·S0 0. **1차 repeated S1 3건 중 RET-001 완전 해소, RET-002·003은
주요 병목(U3 제도어·도입 거푸집) 해소되고 잔여는 S2로 강등.** 신규 S2(RET-008 반전 정형,
RET-010 U7 중복)는 release-blocking이 아니다. clean `ran_passed`는 RET-008·010 polish +
최종 확인 재실행 시 도달한다.

Decision:

```text
ran_passed_with_risks — 1차 S1 해소 검증 완료. 잔여 S2(RET-008·010·009) polish 후
release 추진 시 최종 재실행 권장
```

## Revision Mapping

| Issue id | Fix wave | Baseline source ref | Changed files | 상태 |
| --- | --- | --- | --- | --- |
| RET-001 | rev wave 1 (bdff1c7) | 1308777:.../031#L595-678 | 031 | fixed·verified(2차) |
| RET-002 | rev wave 1 (bdff1c7) | 1308777:.../031#L431-456 | 031 | U3 fixed; U5·U6 잔여 open |
| RET-003 | rev wave 1 (bdff1c7) | 도입/엔딩 | 031 | 도입 fixed; RET-008로 이관 |
| RET-008/010/011 | rev wave 2 (예정) | bdff1c7 refs | 031 (예정) | pending |

## Verification

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/fiction_gate.py --staged
sh scripts/git-hooks/pre-commit
```
