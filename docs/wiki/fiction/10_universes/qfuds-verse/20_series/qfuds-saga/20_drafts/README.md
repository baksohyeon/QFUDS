---
doc_id: qfuds_saga_drafts_index_ko
title: QFUDS SAGA 20_drafts 지도
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_index_ko
next_gate: 1부 origin·2부 Mara 초고 완성 + cascade 완료. release-facing reader-retention 게이트
last_updated: 2026-06-21
---

# QFUDS SAGA 20_drafts 지도

universe/IP: `qfuds-verse` / 작품 `qfuds-saga`. canon 상태: 초안(설정 승격은
`00_bible`). fiction/provenance only, QFUDS 연구 증거 아님.

## 한눈에 (부/arc 단위로 본다)

원고는 **부(arc) 단위 서브폴더**로 관리한다. 평면 번호가 아니라 폴더가 "몇 부인지"를
말한다(마블 타이틀이 volume/arc로 나뉘듯). 원고 번호(029·030·025-027)는 한 번
부여하면 바꾸지 않는 **stable ID**다. 폐기된 1세대는 시리즈 밖 `90_archive/`로 보낸다.

## Cascade 완료 (2026-06-21)

번호 physical cascade를 [011 §10](../10_story_design/011_saga_arc_map_multiarc_ko.md)
기준으로 실행했다. 폴더는 이제 canonical 부 번호와 일치한다.

| 부(arc) | 폴더 | 현행 원고 | 비고 |
| --- | --- | --- | --- |
| **1부 origin** | [1부/](1부/README.md) | [030 origin (사엘)](1부/030_origin_arc_sael_korean_primary.md) | B1~B7 초고 완성 + 윤문 |
| **2부 Mara** | [2부/](2부/README.md) | [029 Mara reboot](2부/029_first_arc_book1_reboot_korean_primary.md) | Prologue~Ch6 초고 완성 |
| **3부 author-loss** | [3부/](3부/README.md) | [025](3부/025_who_may_author_loss_korean_primary.md)·[027](3부/027_who_may_refuse_korean_primary.md)(KR), [026](3부/026_who_may_author_loss_english_counterpart.md)(EN) | author-loss 자산 보존 |

원고 파일명·doc_id는 stable ID라 바꾸지 않았다(029·030·025-027, 그리고 `arc_two`
계열 007·010·004). 폴더 위치와 README·배너 서술 라벨만 cascade로 갱신했다.

Mara 직전 세대(prototype, v3 스냅샷)는 2부로 함께 이동해
[2부/_versions/](2부/_versions/README.md)에 있다.

## 폐기된 1세대는 어디에

1부 1세대 영어 rough(003-010) + 통제문서(011·018) + 초기 Mara 프롤로그(001·002)는
시리즈 밖 아카이브
[90_archive/qfuds-saga_1부_legacy/](../../../../../90_archive/qfuds-saga_1부_legacy/README.md)에
있다. 읽기 가능한 직전 세대(prototype)와 죽은 1세대(legacy)를 구분한다: 전자는
부 폴더 안 `_versions/`(계보 보존), 후자는 `90_archive/`(시리즈 밖 폐기).

## 집필 기준 (상속)

신규 1부 origin 산문은 [1부/030](1부/030_origin_arc_sael_korean_primary.md), 2부 Mara는
[2부/029](2부/029_first_arc_book1_reboot_korean_primary.md), 3부 author-loss는
[3부/](3부/README.md)에서 관리한다.

## 규칙 (상속)

em dash 0(한·영), "박-" 슬랭 동사 금지, 민감 주제 0, 표식=mark, 기술·역사는
[009 §2.5 검증 대장](../00_bible/009_reader_accessibility_and_real_world_anchors_ko.md)
기준. 현재 active release build는 없으며, release 상태는
[40_release](../40_release/README.md)가 관리한다.
