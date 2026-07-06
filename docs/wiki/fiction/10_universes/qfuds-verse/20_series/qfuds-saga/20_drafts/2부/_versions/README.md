---
doc_id: qfuds_saga_drafts_versions_index_ko
title: QFUDS SAGA 2부 Mara 판본 변천사·회고 로그
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_drafts_index_ko
next_gate: append a row + snapshot each time a pass changes the manuscript
last_updated: 2026-06-21
---

# QFUDS SAGA 2부 Mara 판본 변천사·회고 로그

이 폴더는 2부 Mara(029)의 판본 스냅샷과 그 변천사를 보관한다(cascade 전 "1부"
라벨이었던 first-arc 계보). 현행 정본은 상위 `2부/029`이며,
여기엔 직전 prototype(`1부_prototype/`: 프롤로그 028 + 한국어 019-024 + 영어 v2
012-017), v3 스냅샷(`1부_v3_pre_R4/`), 그리고 각 판본의 회고·피드백·개선을 적는다.
죽은 1세대(003-011·018·001·002)는 시리즈 밖 `90_archive/qfuds-saga_1부_legacy/`로
보냈다. 패스가 매뉴스크립트를 바꿀 때마다 행 하나와(필요 시) 스냅샷을 추가한다.
스냅샷(`1부_v3_pre_R4/`) 내부 상호 링크는 보관 시점 기준의 동결 상태이며 갱신하지
않는다(스냅샷 충실도 보존).

## 변천사 (v0 → 현재)

| 판본 | 무엇을 했나 | 작가 피드백 → 개선 | 근거/스냅샷 |
| --- | --- | --- | --- |
| v0 최초 조립 | 영어 rough를 한국어 정본 019-024로 조립(읽기 순서 확정) | 영어 코드스위칭 과다, 비트코인 갑툭튀 | Phase 18 |
| v1 De-jargon | 영어 일반명사를 한국어로, 직역투 제거 | "직역투·AI 티" → 자연 한국어 | [30_revisions/001] |
| v2 현장감 강화 | 묘사·현장감 + release 감사(ai-tell CLEAN, naturalness A) + Series Gate | 흡입력 부족 → 묘사·비유 강화 | [30_revisions/002] |
| v3 구조 패스 | 필드마크 의식 변주, QFUDS 실체, 영어 밀도↓, ep1 cold-open + 비트코인 정확·평이 | "뭐야 어쩌라고"(도입 난해), "비트코인 정확히" → cold-open·실제 개념 | [30_revisions/004], 스냅샷 `1부_v3_pre_R4/` |
| v4 격언·의식 | 격언 절반, 닫는 의식 변주, ep1 비트코인 압축, ep6 저자 해설 삭제 | em dash 금지(한·영), 격언 균질화 지적 | [30_revisions/005] |
| v5 구조 재구성(진행) | 극화 프롤로그(028) 선공개, 유니터리 다리 교정, 검증 출처(009 §2.5), ep1 사다리 제거, ep2~6 무대·시점 다변화 + 떡밥 드립 | "받아들여라 식·조현병 같다"(세계관 미납득), "소설가 흉내로 뭉개지 마라" → 극화·검증 출처·기술적 정확 | [30_revisions/006] |
| outline-first reboot decision | R6 in-place prose patching 중단. 세계관은 유지하고 1부 원고는 outline/scene-card gate 뒤 백지에서 재작성 | "아웃라인이 없어서 망하는 듯" → prose보다 Book 1 cause/effect chain 우선 | [10_story_design/012](../../../10_story_design/307_first_arc_book1_outline_reboot_ko.md), [10_story_design/013](../../../10_story_design/308_first_arc_scene_cards_ko.md) |

## 리텐션 테스트 기록

| 라운드 | 대상 | 결과 |
| --- | --- | --- |
| 라운드 2 | v3 | 하드 이탈 2→1, 2편 이탈 해소 |
| 라운드 3 | v4 | 캐주얼 잔존 12~18%, 고등 55%, SF 60%. 만장일치 병목: 의식 반복·영어 밀도·세계관 미납득. ep1 훅·Mara 편지는 호평 |
| 라운드 4 | v5 | (예정) 세계관 납득·캐주얼 잔존 재측정 |

## 표준 피드백 원칙 (누적, 모든 판본에 적용)

- 세계관은 내레이터 선언이 아니라 **목격된 사건**으로. "받아들여라 아니면 말고" 금지.
- 초안은 **기술적으로 정확하게**. 어설픈 소설가 흉내로 내용을 뭉개지 않는다.
- 비트코인·기술은 [009 §2.5 검증 대장]만 사용. 다리는 **유니터리(정보 보존)**,
  엔트로피는 비용·주제.
- em dash 0(한·영), "박-" 슬랭 동사 0, 민감 주제 0. 톤: Black Mirror식 냉소, "AI evil" 회피.

## 스냅샷·아카이브

- `1부_prototype/` — 029 reboot 이전의 1부 prototype: 프롤로그 028 + 한국어 019-024
  + 영어 v2 012-017. 읽기 가능, 보존용(029의 프롤로그가 028을 흡수).
- `1부_legacy/` — 1부 1세대 영어 rough(003-010) + 통제문서(011·018).
- `1부_v3_pre_R4/` — R4 직전(v3) 019-024 스냅샷. 현행(v5) 정본과 비교용.
