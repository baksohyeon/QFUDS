---
doc_id: qfuds_saga_drafts_index_ko
title: QFUDS SAGA 20_drafts 지도
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_index_ko
next_gate: keep legacy physical paths until origin B1-B7 stabilizes, then run cascade from 011 §10
last_updated: 2026-06-21
---

# QFUDS SAGA 20_drafts 지도

universe/IP: `qfuds-verse` / 작품 `qfuds-saga`. canon 상태: 초안(설정 승격은
`00_bible`). fiction/provenance only, QFUDS 연구 증거 아님.

## 한눈에 (부/arc 단위로 본다)

원고는 **부(arc) 단위 서브폴더**로 관리한다. 평면 번호가 아니라 폴더가 "몇 부인지"를
말한다(마블 타이틀이 volume/arc로 나뉘듯). 번호는 한 번 부여하면 바꾸지 않는
**stable ID**다. 폐기된 1세대는 시리즈 밖 `90_archive/`로 보낸다.

## Cascade Drift Banner

현재 물리 폴더명은 legacy 상태다. 번호 SSOT는
[011 §10](../10_story_design/011_saga_arc_map_multiarc_ko.md)이다.

| 물리 위치 | 현재 보유 자산 | 011 기준 canonical role |
| --- | --- | --- |
| `1부/030` | 신규 origin 사엘 원고 | **1부 origin** |
| `1부/029` | 기존 Mara reboot 원고 | **2부 Mara** |
| `2부/025-027` | 기존 author-loss 원고 | **3부 author-loss** |

origin B1~B7 초안이 안정화될 때까지 파일 이동·rename·삭제는 하지 않는다. 지금 단계는
배너와 ledger만 둔다.

| 부(arc) | 폴더 | 현행 | 상태 |
| --- | --- | --- | --- |
| **legacy 1부 폴더** | [1부/](1부/README.md) | [030 origin](1부/030_origin_arc_sael_korean_primary.md), [029 Mara reboot](1부/029_first_arc_book1_reboot_korean_primary.md) | cascade 보류 |
| **legacy 2부 폴더** | [2부/](2부/README.md) | [025](2부/025_who_may_author_loss_korean_primary.md)·[027](2부/027_who_may_refuse_korean_primary.md)(KR), [026](2부/026_who_may_author_loss_english_counterpart.md)(EN) | canonical 3부 자산 |

각 부 폴더 안에 그 부의 현행 원고와 `_versions/`(그 부의 폐기·스냅샷 판본)가 들어
있다. 1부의 직전 prototype(읽기 가능)과 v3 스냅샷은
[1부/_versions/](1부/_versions/README.md)에 있다.

## 폐기된 1세대는 어디에

1부 1세대 영어 rough(003-010) + 통제문서(011·018) + 초기 Mara 프롤로그(001·002)는
시리즈 밖 아카이브
[90_archive/qfuds-saga_1부_legacy/](../../../../../90_archive/qfuds-saga_1부_legacy/README.md)로
옮겼다. 읽기 가능한 직전 세대(prototype)와 죽은 1세대(legacy)를 구분한다: 전자는
부 폴더 안 `_versions/`(계보 보존), 후자는 `90_archive/`(시리즈 밖 폐기).

## 집필 기준 (상속)

신규 1부 origin 산문은 [1부/030](1부/030_origin_arc_sael_korean_primary.md)에서 쓴다.
029는 011 §10 기준 2부 Mara 자산으로 동결한다. 029의 분할·이동 여부는 origin
B1~B7 초안 안정화 뒤 별도 cascade pass에서 결정한다.

## 규칙 (상속)

em dash 0(한·영), "박-" 슬랭 동사 금지, 민감 주제 0, 표식=mark, 기술·역사는
[009 §2.5 검증 대장](../00_bible/009_reader_accessibility_and_real_world_anchors_ko.md)
기준. 현재 active release build는 없으며, release 상태는
[40_release](../40_release/README.md)가 관리한다.
