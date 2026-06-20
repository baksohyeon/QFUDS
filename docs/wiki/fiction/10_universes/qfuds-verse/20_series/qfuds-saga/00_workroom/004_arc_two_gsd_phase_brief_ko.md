---
doc_id: qfuds_saga_arc_two_gsd_phase_brief_ko
title: QFUDS SAGA 2부 GSD Phase Brief
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_arc_two_korean_primary_plan_ko
  - qfuds_saga_who_may_refuse_korean_primary
next_gate: approve arc-two episode map, then write 028 Korean primary
last_updated: 2026-06-20
---

# QFUDS SAGA 2부 GSD Phase Brief

이 문서는 [Fiction IP Management Workflow](../../../../../../../../.agent/workflows/fiction-ip-management-workflow.md)의
GSD Planning Integration 규칙에 따라, 2부를 **다단계 writing sprint**로 실행하기
위한 phase brief다. (단발 에피소드는 brief 없이 진행 가능하나, arc 단위 sprint는
brief를 둔다.)

## Phase

- Phase name: QFUDS SAGA 2부 Writing Sprint (`who may author loss`)
- GSD mode: `plan` → 이후 episode 단위 `execute`/`verify`
- Applicable workflow:
  [Fiction IP Management Workflow](../../../../../../../../.agent/workflows/fiction-ip-management-workflow.md)
- Authoring baseline date: `2026-06-20`

## Objective

1부 finale가 연 질문 `who may author loss`를, mercy가 제도→시장→권력으로 굳는
과정으로 전개해 2부 arc를 완성한다. ep1(025)·ep2(027)은 작성·감사 완료. 이 sprint는
[2부 에피소드 맵](../10_story_design/010_arc_two_episode_map_ko.md)을 확정하고,
ep3(028)부터 한국어 정본 + 영어 counterpart를 편별로 쌓아 release 후보까지 간다.

## Reader Support

- English craft terms used: deep POV, field mark, incluing, beat, throughline.
- Korean-friendly explanations: 각 용어는 [craft harness](../../../../../00_studio/004_creative_writing_craft_harness_ko.md)와
  [강화 기준](../30_revisions/002_first_arc_release_immersion_revision_plan_ko.md)에 정의됨.
- Bare `TBD` placeholders allowed? `no`

## IP Classification

- Universe/IP: `qfuds-verse`
- Continuity status: canon-candidate (ep 확정 전까지 momentum으로 canon 고정 금지)
- Work id: `qfuds-saga`
- Work format: `series`
- Target folder: `10_story_design/`(맵) → `20_drafts/`(prose) → `30_revisions/` → `40_release/`
- Time baseline notes: 작중 Continuity Court Era. author baseline 2026-06-20.

## Scope

Allowed outputs:

- 2부 episode map(`10_story_design/010`) — ep1·ep2 통합 + ep3~ **proposed**.
- ep3(028)+ 한국어 정본 prose, 영어 Anglophone counterpart.
- 편별 continuity / field-mark chain 정합.
- release 준비물(arc 완성 후).

Forbidden outputs:

- Research evidence / roadmap status 변경.
- work README 없는 draft (work README는 이미 존재).
- continuity 분류 없는 canon 변경 (ep3~는 proposed 표기 유지).
- Research Asset and Product Workflow state 없는 외부 source claim.
- 과학·기술어의 무근거 개명.
- narrative frame 결정 없는 장면.
- 민감한 사회·정치 주제의 레포·작중 기입(작가 지시).

## Tone Rules

- 전체 evidence disclaimer 반복 금지; local boundary/workflow state만.
- reference 산문은 간결·직접. 장엄체·장식 비유 금지.
- `ancient`/`future` 등은 author baseline 또는 in-world era ID 기준.

## Technical Grounding

- `hash`, `key`, `signature`, `entropy`, `Genesis Chain`은 기술어로 보존.
- 작중 제도명(거부 등록부 등)은 그 기술어가 만든 사회적 결과를 보여 주는 장치.

## Narrative Frame

- Who speaks: 비개입 3인칭 서술자.
- Who sees / focalizer: Liora Sen 제한 시점(arc 일관).
- Telling time: 사건 동시 진행(직접 장면), Continuity Court Era.
- Narrative form: 직접 장면 + Last Archive 응답/필드 마크 삽입.
- Implied audience: 복원 문명 이후를 읽는 일반 독자(밈/전문지식 없이 읽힘).
- Narrator motive: 제도가 자비를 상품화하는 과정을 인물의 절차·비용·계급으로 보여줌.
- Knowledge limits: Liora가 아는 범위; Last Archive의 정체는 천천히 드러남(반전축).
- Distortion risk: 서술자가 교훈을 먼저 닫지 않도록 격언 1:1 부착 금지(027 감사 교훈).

## Required Reads

- [Fiction IP Management Workflow](../../../../../../../../.agent/workflows/fiction-ip-management-workflow.md)
- [Documentation Folder Routing Workflow](../../../../../../../../.agent/workflows/documentation-folder-routing-workflow.md)
- [Wiki Maintenance Workflow](../../../../../../../../.agent/workflows/wiki-maintenance-workflow.md)
- 작품 index: [QFUDS SAGA README](../README.md)
- Arc 설계: [Arc Two Plan](../10_story_design/007_arc_two_korean_primary_plan_ko.md),
  [반전 설계](../10_story_design/008_last_archive_reveal_architecture_ko.md)
- bible: [인과 척추](../00_bible/010_last_archive_origin_and_reversal_causality_ko.md),
  [세력 canon](../00_bible/015_factions_canon_naming_ko.md),
  [Liora 시트](../00_bible/012_character_liora_sen_ko.md)

## Acceptance Criteria

- 2부 episode map 확정(사용자 승인) — ep 수, 각 ep 질문·turn·cost·field mark.
- 각 한국어 정본 ep: `ai-tell-detector` CLEAN(S1 0) + `naturalness-reviewer` A +
  content-fidelity(플롯·수치·필드 마크 불변) 통과.
- 영어 counterpart는 같은 사건 공유(직역 아님), 필드 마크 verbatim.
- 영어성 토큰 density 비증가, 단문 절제 보이스 유지.
- `validate_docs.py` 통과; 민감어 sweep CLEAN.

## Verification

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/agent_workflow_guard.py --staged
make preflight
sh scripts/git-hooks/pre-commit
```

## Handoff

- Commit boundary: episode map 1커밋, 이후 ep별(한국어→영어→continuity) 커밋.
- Next phase: episode map 승인 → ep3(028) 한국어 정본 execute.
- User confirmation needed: **arc 길이(ep 수)·각 ep 방향·field mark 후보**는 작가
  승인 후 canon 고정. momentum으로 확정하지 않는다.
