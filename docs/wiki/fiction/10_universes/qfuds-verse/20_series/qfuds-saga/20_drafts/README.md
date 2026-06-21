---
doc_id: qfuds_saga_drafts_index_ko
title: QFUDS SAGA 20_drafts 지도
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_index_ko
next_gate: do not rewrite 028 or 019-024 until 10_story_design/013 scene cards pass review
last_updated: 2026-06-21
---

# QFUDS SAGA 20_drafts 지도

universe/IP: `qfuds-verse` / 작품 `qfuds-saga`. canon 상태: 초안(설정 승격은
`00_bible`). fiction/provenance only, QFUDS 연구 증거 아님.

## 왜 파일이 많은가 (6편짜리인데)

같은 6편이 **세 세대**로 존재하기 때문이다: 초기 영어 rough → 영어 v2 → 한국어
prototype. 거기에 프롤로그·통제문서·2부가 더해져 수가 늘었다. **지금 읽는 1부
prototype은 아래 "현행 읽기본"뿐이고, 나머지는 이전 세대·영어 카운터파트·작업
통제문서다.** 다음 정본 rewrite는 이 파일들을 문장 단위로 고치지 않고
`10_story_design/012`와 후속 scene cards 뒤에 백지 원고로 다시 쓴다.

## 현행 읽기본 (스토리 순서)

읽기 순서. 이것만 보면 된다.

| 순서 | 편 | 파일 |
| --- | --- | --- |
| 프롤로그 | The Broken Crown 사건 | [028](028_first_arc_opening_broken_crown_event_korean_primary.md) |
| 1 | Exhibit S-0 | [019](019_exhibit_s0_episode1_revised_v2_korean_adaptation.md) |
| 2 | The Dead Exchange | [020](020_the_dead_exchange_revised_v2_korean_adaptation.md) |
| 3 | The Last Hodler | [021](021_the_last_hodler_revised_v2_korean_adaptation.md) |
| 4 | Identity Flood | [022](022_identity_flood_revised_v2_korean_adaptation.md) |
| 5 | Hawking Court | [023](023_hawking_court_revised_v2_korean_adaptation.md) |
| 6 | The Broken Crown | [024](024_the_broken_crown_revised_v2_korean_adaptation.md) |

2부(진행 중): [025](025_who_may_author_loss_korean_primary.md)(KR)·
[027](027_who_may_refuse_korean_primary.md)(KR)·[026](026_who_may_author_loss_english_counterpart.md)(EN).

## 1부 백지 재설계 게이트

1부의 다음 산문 작업은 직접 rewrite가 아니다. 먼저
[012 통합 아웃라인](../10_story_design/012_first_arc_book1_outline_reboot_ko.md)을 기준으로
[013 scene cards](../10_story_design/013_first_arc_scene_cards_ko.md)를 검토·보강한다. 각 장면의 `POV`, `want`, `obstacle`,
`turn`, `cost`, `technical terms exposed`, `information revealed`, `hook into next
scene`이 통과된 뒤에만 028+019-024를 새 manuscript로 다시 쓴다.

## 나머지는 무엇인가 (역할별)

| 묶음 | 파일 | 역할 |
| --- | --- | --- |
| 1부 영어 카운터파트 | 012-017 | 같은 사건의 영어 독립 각색(보존) |
| 1부 이전 세대(영어 rough) | 003-010 | 1세대 초안. 정본에 의해 대체됨 |
| 1부 통제문서 | 011, 018 | revision/read-order 통제 기록 |
| Mara 프롤로그(legacy) | 001, 002 | 초기 프롤로그 실험 |
| 판본 스냅샷·회고 | [_versions/](_versions/README.md) | v0~v4 변천사와 회고·피드백 로그 |

이전 세대(003-010)와 통제문서(011·018)는 `_versions/1부_legacy/`로 옮겼다. 이 폴더엔 현행 정본만 남긴다.

## 규칙 (상속)

em dash 0(한·영), "박-" 슬랭 동사 금지, 민감 주제 0, 표식=mark, 기술·역사는
[009 §2.5 검증 대장](../00_bible/009_reader_accessibility_and_real_world_anchors_ko.md)
기준. 현재 active release build는 없으며, release 상태는 [40_release](../40_release/README.md)가 관리한다.
