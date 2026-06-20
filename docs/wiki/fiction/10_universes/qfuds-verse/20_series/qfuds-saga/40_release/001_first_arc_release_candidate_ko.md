---
doc_id: qfuds_saga_first_arc_release_candidate_ko
title: QFUDS SAGA 1부 Release Candidate — The Broken Crown
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_release_index_ko
  - qfuds_saga_first_arc_release_immersion_revision_plan_ko
next_gate: apply series gate retroactively to episodes 2-6; reader review of first-arc bundle
last_updated: 2026-06-20
---

# QFUDS SAGA 1부 Release Candidate — The Broken Crown

## 무엇인가

`The Broken Crown` 1부 6편의 **독자용 release 후보 기록(메타데이터)**이다. 한국어
정본을 첫 읽기 경로로 두고, 영어 독립 각색판을 같은 사건의 보존 counterpart로
둔다. 이 문서는 de-jargon 퇴고(1차)와 현장감·묘사 강화 퇴고(2차)를 모두 통과한
상태를 가리킨다.

실제 독자용 조립 원고는 [002 1부 Release 원고](002_first_arc_manuscript_ko.md)에
있다 — `20_drafts/019`–`024`에서 본문만 조립한 산출물(build)이며, draft 수정 시
재생성한다. 즉 **편집 정본(SSOT)은 drafts, 완성 읽기본은 40_release**다.

## Boundary

이 문서는 fiction/provenance 작업물이다. QFUDS 연구 증거, roadmap status,
physical-source claim이 아니다. 새 외부 웹/PDF/asset/product claim을 만들지
않는다. 외부 자료 handling은
[Research Asset and Product Workflow](../../../../../../../../.agent/workflows/research-asset-product-workflow.md).

```text
not searched
```

## 읽기 순서 (한국어 정본 우선)

| # | Episode | 한국어 정본 | 영어 counterpart | 필드 마크 |
| --- | --- | --- | --- | --- |
| 1 | Exhibit S-0 | [019](../20_drafts/019_exhibit_s0_episode1_revised_v2_korean_adaptation.md) | [012](../20_drafts/012_exhibit_s0_episode1_revised_v2_english_draft.md) | `RECOVERABLE / NOT CLAIMABLE` |
| 2 | The Dead Exchange | [020](../20_drafts/020_the_dead_exchange_revised_v2_korean_adaptation.md) | [013](../20_drafts/013_the_dead_exchange_revised_v2_english_draft.md) | `ACCESS != AUTHORITY` |
| 3 | The Last Hodler | [021](../20_drafts/021_the_last_hodler_revised_v2_korean_adaptation.md) | [014](../20_drafts/014_the_last_hodler_revised_v2_english_draft.md) | `NO CONSENT BY ANALOGY` |
| 4 | Identity Flood | [022](../20_drafts/022_identity_flood_revised_v2_korean_adaptation.md) | [015](../20_drafts/015_identity_flood_revised_v2_english_draft.md) | `PLURALITY IS NOT CONSENT` |
| 5 | Hawking Court | [023](../20_drafts/023_hawking_court_revised_v2_korean_adaptation.md) | [016](../20_drafts/016_hawking_court_revised_v2_english_draft.md) | `PHYSICS IS NOT JURISDICTION` |
| 6 | The Broken Crown | [024](../20_drafts/024_the_broken_crown_revised_v2_korean_adaptation.md) | [017](../20_drafts/017_the_broken_crown_revised_v2_english_draft.md) | `who may author loss` (arc-two hook) |

프롤로그를 먼저 읽고 싶다면
[Mara Veyr 프롤로그](../20_drafts/001_mara_veyr_prologue_draft_ko.md)를 1화 앞에 둔다.

## 관통선

표면 질문은 "완전 복원이 가능해도 죽을 권리·잊힐 권리는 남는가"이고, 시리즈
반전축은 "진실의 단일 출처(SSOT)는 존재하는가 — 정하는 것은 지성인가 합의인가"다.
1부는 필드 마크 사슬로 그 질문을 한 겹씩 쌓아 `who may author loss`로 닫고
[2부](../20_drafts/025_who_may_author_loss_korean_primary.md)로 넘긴다.

## 통과한 퇴고 게이트

이 번들의 6편은 두 차례 퇴고와 release 감사를 통과했다. 이후 추가된
`00_workroom/005` 시리즈 프리플라이트는 1편에 먼저 역적용됐고, 2-6편은 같은 방식의
후속 적용 대상이다.

- 1차: de-jargon·자연 한국어 line edit
  ([001 퇴고 계획](../30_revisions/001_first_arc_dejargon_polish_revision_plan_ko.md)).
- 2차: 현장감·묘사 강화
  ([002 강화 기준](../30_revisions/002_first_arc_release_immersion_revision_plan_ko.md)).
- release 감사 결과(편별):
  - `ai-tell-detector`: 6편 S1 0 (CLEAN).
  - `naturalness-reviewer`: 6편 A (release-ready). 강화 패스가 남긴 국소
    과윤문 4건(020 심박 중복, 022 잉크 냄새, 023 통사 반복, 024 클라이맥스
    외양 묘사)은 트림 완료.
  - 필드 마크 무결성: 6편 ```text``` 블록 전부 byte-identical(HEAD 대조).
  - 영어성 토큰 density: 강화 전후 불변(새 영어 일반명사 0).
  - `validate_docs.py`: 통과.
- 신규 시리즈 게이트:
  - 1편: 반복 인물 시트·POV 선언·단독 완결 금지·Pell 후속 위험 스레드 적용 완료.
  - 2-6편: 후속 retroactive pass 필요.

## release 경계

이 문서는 release **후보**다. 실제 배포 포맷(EPUB/PDF/연재 분할)·표지·법적
표기는 별도 단계다. 한국어 정본과 영어 counterpart는 같은 사건을 공유하되
서로의 직역이 아니다.
