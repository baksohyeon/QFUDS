---
doc_id: qfuds_saga_revisions_origin_sael_fullnovel_retention_comprehension_gate_20260622_c91e9be_ko
title: 033 origin 풀길이 소설 Retention + Comprehension Gate 2026-06-22 c91e9be
doc_type: gate
stage: reference
status: completed
evidence_role: provenance
depends_on:
  - qfuds_saga_revisions_first_second_arc_formal_retention_gate_protocol_ko
  - qfuds_saga_drafts_origin_sael_full_novel_korean_primary
next_gate: 잔여 S1(중반 반복)·S2(거푸집) polish 후 release 추진 시 재실행. 다음 작업=2부 풀길이 또는 영어 각색
last_updated: 2026-06-22
---

# 033 origin 풀길이 소설 Retention + Comprehension Gate 2026-06-22 c91e9be

## Metadata

- Work id: qfuds-saga / 1부 origin (사엘) 풀길이 소설(033)
- Gate id: RG-033-20260622-c91e9be (풀길이 8장 첫 정식 게이트, **comprehension 차원 포함**)
- Scope: 033 1~8장 전체(~45,100자). 작가의 "이해 안 됨" 지적 해소 검증
- Baseline commit/date: c91e9be / 2026-06-22
- Gate owner mode: `reader-sim` + `critic` + `chronicler`
- Production board: [009](../00_workroom/009_saga_production_board_ko.md)

## Boundary

```text
fiction/provenance only
research evidence: no
release promotion without this artifact: no
raw private reasoning: do not record
```

## Source Baseline

| Source id | Path | Baseline | Blob | Notes |
| --- | --- | --- | --- | --- |
| S1 | 20_drafts/1부/033_origin_sael_full_novel_korean_primary.md | c91e9be | c420b3970253322dcbf734952a9a7d5a6fd052a2 | 1~8장 완결 |

Persona set([012] 상속): P1 중2 / P2 웹소설속독 / P3 기술문외한 / P4 순문학 / P5 안티AI /
P6 SF / P7 피곤한 일반. 장 라인: 1장 L69 / 2장 L180 / 3장 L278 / 4장 L378 / 5장 L457 /
6장 L508 / 7장 L547 / 8장 L602-668.

## Retention (완독·이탈)

전원 **완독**(7/7), release-blocking S0 = 0. 1장 익명 훅 + 8장 "자물쇠가 곧 왕관" 회수가
강하고, 1장→2장(서류 직접 도착)→…→8장(첫 청구서)이 단편 모음이 아닌 한 줄기 장편으로
읽힘(P2 "단일 사슬"). 공통 약점: 중반 5~7장 "통제 상실/도장 자동화" 비트 반복(P1·P2·P7).

## Comprehension (이해 테스트 C1~C5, 본문만으로)

이 게이트의 핵심. 작가가 풀길이 전까지 이해하지 못한 항목을 본문만으로 설명 가능한지 측정.

| Persona | C1 주인공 | C2 무대 | C3 무너진것 | C4 행위·문제 | C5 장르 |
| --- | --- | --- | --- | --- | --- |
| P1 중2 | can | can | can | can | can(SF) |
| P2 속독 | can | can | can | can | can(SF) |
| P3 문외한 | can | can | can | can | can(SF) |
| P4 순문학 | can | can | can | can | can(우화) |
| P5 안티AI | can | can | can | can | can(SF) |
| P6 SF | can | can | can | can | can(SF) |
| P7 피곤 | can | can | can | can | **partial(톤모호)** |

- **C1~C4: 7/7 can_explain.** C5: 6 can_explain + 1 partial(P7, 스릴러/우화 톤 사이 모호 — 천사/종교/판타지 오분류 아님).
- **P3(기술 문외한) 결정적 호전**: 이전 3대 차단(사엘 정체·회사 정체·천사 세계관 오해) 전부 해소. "비트코인이란 단어 한 번 없이 스스로 깨닫게 만든다." 성공 요인: (1) 암호 용어 미사용·일상어(지갑/열쇠/자물쇠/도장)만, (2) 2장이 검증 회사 정체·존재 이유를 명시, (3) '사엘' 이름에 천사 떡밥 0 → SF로 자연 인지.

## Issue Ledger

| Issue id | Severity | Evidence | Source ref | Failure mode | Status |
| --- | --- | --- | --- | --- | --- |
| RET-016 | S1(retention) | P1,P2,P7 | c91e9be:.../033#L508-563 | 중반 5~7장 '통제 상실/도장 자동화' 비트 반복(늘어짐). 단 완독엔 지장 없음(no dropout) | deferred (fix: 6장 압축 + 베라 떡밥 앞당김) |
| RET-017 | S2 | P5,P4 | 매 장 클라이맥스 | 'A가 아니라 B' + 양자택일 평행 단문 + 잠언 요약 거푸집이 매 장 같은 자리 | open |
| RET-018 | S2 | P4 | c91e9be:.../033#L73-84,L130 | 1장 죽은 어머니 도입의 손쉬운 정서 동원 + '사형 선고처럼' 직유 과함 | open |
| RET-019 | S2 | P7,P3 | 자물쇠/한방향 비유 반복 | 같은 비유가 1·3·8장 반복, 한 번쯤 쳐낼 여지 | open |
| RET-020 | S3 | P6 | c91e9be:.../033#L624-637 | 사람=데이터 기술 발판이 은유적(제도적 청구로 의도 처리) | deferred(2부) |
| COMP-C5 | S3 | P7 | 전반 톤 | 스릴러/우화 톤 모호(오분류 아님) | open |

## Decision

```text
retention: ran_passed_with_risks
comprehension: ran_passed
```

근거: 7/7 완독·S0 0. **Comprehension C1~C4 전원 통과, C5 오분류 0 → comprehension ran_passed**
(작가 "이해 안 됨" 지적의 정식 해소). Retention은 중반 반복(RET-016)이 3+ 페르소나
반복 S1이나 이탈 없음 → 사유 명시 deferred로 ran_passed_with_risks. 잔여는 전부 S2/S3.

Decision:

```text
retention ran_passed_with_risks + comprehension ran_passed —
1부 origin 풀길이 소설 리텐션·이해 통과. 중반 반복(RET-016)·거푸집(RET-017) polish 권장
```

## Verification

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/fiction_gate.py --staged
sh scripts/git-hooks/pre-commit
```
