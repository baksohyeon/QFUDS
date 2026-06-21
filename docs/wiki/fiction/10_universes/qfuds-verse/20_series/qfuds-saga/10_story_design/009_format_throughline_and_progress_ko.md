---
doc_id: qfuds_saga_format_throughline_and_progress_ko
title: QFUDS SAGA 형식·시리즈 throughline·현재 진행 상태
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_last_archive_reveal_architecture_ko
  - qfuds_saga_last_archive_origin_and_reversal_causality_ko
next_gate: build Liora protagonist sheet, then propagate foundation into first arc
last_updated: 2026-06-21
---

# QFUDS SAGA 형식·시리즈 throughline·현재 진행 상태

## 목적

"단편인가 장편인가", "시리즈를 관통하는 드라마가 뭔가", "지금 어디까지 왔나"를
고정한다.

fiction/provenance only. 새 외부 source claim 없음. 형식 영향 출처는 아래 boundary.

## Influence Boundary

양영순 「덴마」의 **옴니버스 → 대하 사가** 구조 감각만 차용한다(에피소드별로 단편처럼
읽히다가 가지가 뻗어 하나의 거대 상호연결 세계로 수렴; 다크 제도 SF + 휴머니즘
코어). 고유명·캐릭터·줄거리는 복제하지 않는다. (참고 확인: 나무위키 「덴마」,
workflow state `hit_not_cached`.)

## 형식 — 단편 사이클 → 대하 사가

- **시작은 단편처럼, 끝은 사가처럼.** 각 에피소드는 독립된 법정 사건(복원 분쟁)으로
  단독으로 읽힌다. 그러나 사건이 쌓이며 같은 세계·같은 비밀(Last Archive 반전)으로
  수렴한다.
- 1부 = 6개 법정 사건. 감사관 Liora Sen의 반복 POV가 사건들을 꿴다.
- 톤: 다크 제도 SF(법정·관료·복원 자본) + 휴머니즘 코어(동의·잊힐 권리·죽음의 평등).
- 길이: 단편 연작으로 출발해 필요 시 아크가 길어지는 것을 허용(덴마처럼). 처음부터
  장편 한 덩어리로 설계하지 않는다.

## Throughline — 시리즈를 관통하는 것

표면 질문(매 에피소드):

```text
완전 복원이 가능해도, 죽을 권리·잊힐 권리는 남는가?
완벽한 복사는 귀환인가, 범죄인가?
```

심층 질문(시리즈 반전, 천천히 드러남):

```text
진실의 단일 출처(SSOT)는 존재하는가?
무엇이 진실이었는지 정하는 것은 — 지성인가, 합의인가?
```

엔진: 사건이 쌓일수록 Last Archive의 정체(합의의 신격화, Vera, SSOT 없음)가
드러난다. 반전 배치는
[008 반전 설계](008_last_archive_reveal_architecture_ko.md). Vera ↔ Mara **Veyr**의
핏줄 연결이 그 반전의 개인적 열쇠다(010 §2).

## 현재 진행 상태 (2026-06-21 기준)

- **outline-first reboot로 전환됨.** 기존 6편 prototype(한국어 019-024 + 영어
  012-017 + 프롤로그 028)은 in-place 퇴고를 중단하고 `20_drafts/1부/_versions/`로
  보존. 죽은 1세대는 `90_archive/qfuds-saga_1부_legacy/`.
- **1부 active 원고 = [029](../20_drafts/1부/029_first_arc_book1_reboot_korean_primary.md)**:
  프롤로그 + Ch1~5 작성됨(① Exhibit S-0 ② Dead Exchange ③ Last Hodler ④ Identity
  Flood ⑤ Hawking Court), 다음은 Ch6 final human hearing. 구조 SSOT는
  [012 아웃라인](012_first_arc_book1_outline_reboot_ko.md)·[013 scene cards](013_first_arc_scene_cards_ko.md).
- **다음 단계**: (1) Ch6 집필로 1부 완성, (2) 1부 통합 퇴고/리텐션, (3) release
  다듬기(사용자 게이트), (4) 2부 설계(`who may author loss`, 010·007).

## 주인공 — Liora Sen (척추는 별도 시트로)

Liora = 라우어 관측소(옛 검증·감사 부문의 후신) 감사관, 시리즈 반복 POV. 그녀의
직업적 강박(정의되지 않은 것을 보존하라)이 곧 Last Archive의 강박(손실을 못
견딘다)과 거울이자 대척이다 — 그녀는 "모름(unknown)"을 지키려 하고, Archive는
"모름"을 못 견뎌 메우려 한다. 전체 want/need/wound/거짓말/아크는
[캐릭터 시트 템플릿](../../../../../../../../.agent/templates/fiction/character_sheet_template.md)으로
다음에 채운다.
