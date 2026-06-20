---
doc_id: qfuds_saga_first_arc_dejargon_polish_revision_plan_ko
title: QFUDS SAGA 1부 De-jargon·Polish 퇴고 계획
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_bilingual_term_discipline_glossary_ko
  - qfuds_saga_first_arc_polish_read_order_pass
  - fiction_prose_verisimilitude_audit_checklist_ko
next_gate: apply to 019-024, then audit with naturalness/content-fidelity agents
last_updated: 2026-06-20
---

# QFUDS SAGA 1부 De-jargon·Polish 퇴고 계획

## Boundary

이 문서는 release-facing 퇴고 통제 문서다. fiction/provenance only.
QFUDS 연구 결과·물리 증거·support·validation 아님. 새 외부 source claim 없음.
workflow state: `not searched`.

## 문제 (근거)

한국어 정본 v2 각색본(019-024)이 prose 본문에서 영어 일반명사를 과도하게
유지한다. 이는 canon 규칙
[bible 006](../00_bible/006_post_agi_civilization_history_bilingual_protocol_ko.md)
§389-393("한국어 본문은 직역투가 아니라 한국어 소설로 읽혀야 한다")을 위반한다.

퇴고 전 영어성 토큰 density(측정):

| 파일 | 토큰 | 줄 |
| --- | --- | --- |
| 019 episode1 | ~605 | 422 |
| 020 dead exchange | ~734 | 426 |
| 021 last hodler | ~729 | 470 |
| 022 identity flood | ~831 | 457 |
| 023 hawking court | ~716 | 416 |
| 024 broken crown | ~873 | 463 |

잔존 영어가 고유명사가 아니라 일반명사(queue, rumor, screen, banner, relic,
invoice, access, authority, petition, residence 등). 프롤로그
[001](../20_drafts/001_mara_veyr_prologue_draft_ko.md)은 규칙을 지키는 기준 모델.

## 집행 기준

[이중언어 용어규율 글로서리](../00_workroom/003_bilingual_term_discipline_glossary_ko.md)의
Keep 4범주(고유명사·제도 분위기어·기술어·의도적 장치)만 영어 유지, 나머지
일반명사는 한국어. 제도 분위기어는 사용자 선택 "중간" 기준으로 Trust, Court,
Ledger House 등 최소 집합만 유지.

## 범위와 방식

| 대상 | 작업 | 방식 |
| --- | --- | --- |
| 019-024 (한국어 정본) | de-jargon + 라인 다듬기 (주 작업) | in-place 편집 |
| 012-017 (영어 v2) | 군더더기/과한 비유 정리 + story state·고유명사 일치 | in-place 점검 |
| 001 (한국어 프롤로그) | 기준 모델, 미세 보정만 | in-place |

버전 폭증을 피해 in-place 편집한다. 퇴고 전 상태는 git history가 보존한다.

## 각 편 작업 항목

1. 글로서리대로 일반명사 영어 → 자연 한국어.
2. 라인 다듬기: 과한 은유·장엄체 제거, 직역투 어순 교정.
3. [핍진성 체크리스트](../../../../../00_studio/006_prose_verisimilitude_audit_checklist_ko.md)로
   장면별 스폿체크.
4. 비트코인/역연산 동기 전달 문장 보존·강화(coin은 죽고 access/권한만 산다).
5. 의미 불변: 사실·수치·인용·플롯 순서 그대로.

## 검증 게이트

- [ ] 영어성 토큰 density 재측정 → Keep 4범주로 수렴.
- [ ] `naturalness-reviewer` + `ai-tell-detector` 에이전트로 잔존 AI 티/과윤문 점검.
- [ ] `content-fidelity-auditor`로 의미·수치·인용·플롯 순서 불변 확인.
- [ ] `make research-audit`, `make agent-workflow-guard` 통과.

## 결과 기록

각 편 퇴고 결과는 해당 draft의 Continuity Notes에 한 줄로, 종합은 이 문서
하단 로그에 남긴다.

## 퇴고 로그

- 2026-06-20: 019-024 한국어 primary draft에 1차 de-jargon line polish를
  in-place 적용했다. 일반명사 영어를 한국어로 줄이고, 각 draft의 Continuity
  Notes에 de-jargon pass 기록을 추가했다. Naturalness/content-fidelity 전용
  에이전트 감사와 release 후보 승격은 아직 남아 있다.
