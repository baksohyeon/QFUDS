---
doc_id: qfuds_saga_revisions_mara_fullnovel_retention_comprehension_gate_20260623_a41bcb9_ko
title: 034 2부 마라 풀길이 소설 Retention + Comprehension Gate 2026-06-23 a41bcb9
doc_type: gate
stage: reference
status: completed
evidence_role: provenance
depends_on:
  - qfuds_saga_revisions_first_second_arc_formal_retention_gate_protocol_ko
  - qfuds_saga_drafts_mara_full_novel_korean_primary
next_gate: 거푸집 후렴(S1)·6장 물리댐/길이·QFUDS 한 줄 설명 polish 후 release 추진 시 재실행. 또는 3부
last_updated: 2026-06-30
---

# 034 2부 마라 풀길이 소설 Retention + Comprehension Gate 2026-06-23 a41bcb9

## Metadata

- Work id: qfuds-saga / 2부 마라 풀길이(034)
- Gate id: RG-034-20260623-a41bcb9 (2부 풀길이 6장 첫 정식 게이트, retention + comprehension)
- Scope: 034 1~6장 전체(본문 ~65,200자)
- Baseline commit/date: a41bcb9 / 2026-06-23
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
| S1 | 20_drafts/2부/034_mara_full_novel_korean_primary.md | a41bcb9 | efac06be21a0bded3d74514d79dbd53b79925dac | 1~6장 완결 |

Persona set([012] 상속): P1 중2 / P2 속독 / P3 문외한 / P4 순문학 / P5 안티AI / P6 SF /
P7 피곤. 장: 1장 L70 / 2장 L386 / 3장 L790 / 4장 L1212 / 5장 L1726 / 6장 L2447-3375.

## Retention

전원 **완독**(7/7), S0 0. 1장→6장 시간순 단일 줄기(P2 "한 줄기 장편"). 공통 처짐:
6장 물리 강의 댐(L2526~2638)과 3장 후반 추상 대화(P1·P2·P7), 6장 과길이(~20K).

## Comprehension (C1~C5, 본문만으로)

| Persona | C1 마라·상황 | C2 무대 | C3 갈등 | C4 행위·중요성 | C5 장르 | 1부 미독자 OK |
| --- | --- | --- | --- | --- | --- | --- |
| P1 중2 | can | can | can | can | can(SF) | 예 |
| P2 속독 | can | can | can | can | can | 예 |
| P3 문외한 | can | can | can | can | partial(SF/우화) | 예 |
| P4 순문학 | can | can | can | can | can | (암시 예) |
| P5 안티AI | can | can | can | can | can | (암시 예) |
| P6 SF | can | can | can | can | can | (암시 예) |
| P7 피곤 | can | can | can | can | can | (암시 예) |

- **C1~C4: 7/7 can_explain.** C5: 6 can + 1 partial(P3, SF/우화 톤 — 천사/종교/판타지
  오분류 아님). → **comprehension ran_passed.**
- **전원 "1부 안 읽어도 따라온다"**(독립 온보딩 성공). P3(문외한) 6장 물리 "확" 이해
  (탄 소금 비유로 정보보존≠회수가능 명료).

## Issue Ledger

| Issue id | Severity | Evidence | Source ref | Failure mode | Status |
| --- | --- | --- | --- | --- | --- |
| RET-2B-001 | S1 | P2,P4,P5 | 매 장 말미·주제문 | 거푸집 후렴 반복: "새 몸의 손…쥐는 법은 알았다"(4회), "보호의 문장은 서류철 밖에서 먼저 팔린다"(5회), "차가운 물도 불은 끈다"(3회), "울어도 부끄럽지 않게 계산된 길이의 복도"(4회), "A가 아니라 B + 한 핏줄" 공식 매 장 | open (fix: 반복 절반 이상 감축) |
| RET-2B-002 | S2 | P1,P2,P7 | a41bcb9:.../034#L2526-2638 | 6장 물리 강의 댐 + 6장 과길이(~20K) | open (압축) |
| RET-2B-003 | S2 | P3 | a41bcb9:.../034#L2682 | 'QFUDS' 단어가 정체 설명 없이 등장(시리즈 핵심어인데 한 줄 정의 부재) | open (Dahl 대사에 평이 한 줄) |
| RET-2B-004 | S2 | P7 | a41bcb9:.../034#L969-1210 | 3장 후반 추상 대화(보호 상품화) 늘어짐 | open |
| RET-2B-005 | S2 | P6 | a41bcb9:.../034#L2632-2638 | 6장 '둘로 갈라짐' 분기 메커니즘이 정보보존 논리와 미세 충돌 | closed (2026-06-30, α '한 벌을 두 길로 읽음'으로 통일; 034 달 대사에 "기록은 한 벌…베껴서 둘이 아니라 읽혀서 둘" 명시, 정보 복제 해석 차단) |
| RET-2B-006 | S3 | P6 | a41bcb9:.../034#L2780-2792 | Last Archive '한 박자 망설임' 미회수(도구/행위자 캐논과 긴장) | deferred(3부 의도) |
| COMP-C5 | S3 | P3 | 전반 톤 | SF/우화 톤 모호(오분류 아님) | open |

## Decision

```text
retention: ran_passed_with_risks
comprehension: ran_passed
```

근거: 7/7 완독·S0 0. Comprehension C1~C4 전원·C5 오분류 0 + 전원 "1부 미독자 OK" →
**comprehension ran_passed**(작가 이해 우려 2부에서도 해소, 독립 온보딩 성공). Retention은
거푸집 후렴 반복(RET-2B-001)이 3+ 페르소나 S1이나 이탈 없음 → ran_passed_with_risks.
잔여 S2(물리댐/길이·QFUDS gloss·3장 추상·분기 논리)는 polish 백로그.

Decision:

```text
retention ran_passed_with_risks + comprehension ran_passed —
2부 풀길이 리텐션·이해 통과. 거푸집 후렴 감축(RET-2B-001) 우선 polish 권장
```

## Verification

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/fiction_gate.py --staged
sh scripts/git-hooks/pre-commit
```
