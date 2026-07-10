---
doc_id: fiction_university_creative_writing_reference_matrix_ko
title: 대학 문예창작 참고 매트릭스
doc_type: guide
stage: reference
status: draft
evidence_role: reference
depends_on:
  - fiction_creative_writing_craft_harness_ko
  - fiction_ip_management_system_ko
  - wiki_fiction_index
next_gate: use this matrix only after source state is recorded
last_updated: 2026-07-10
---

# 대학 문예창작 참고 매트릭스

## 목적

이 문서는 대학식 문예창작 기준을 fiction harness에 가져올 때 쓰는 기준표다.

핵심은 간단하다.

- 웹 자료를 참고하면 source state를 먼저 남긴다.
- 대학명을 장식으로 쓰지 않는다. 확인된 운영 원칙만 가져온다.
- 문예창작 용어는 영어 기준을 유지하되, 한국어 풀이를 같이 둔다.
- 출처가 불확실하면 fiction 규칙으로 승격하지 않는다.

## Workflow Boundary

External-source handling follows
[Research Asset and Product Workflow](../../../../.agent/workflows/research-asset-product-workflow.md).

Current workflow state:

```text
hit_not_cached
```

This document uses official university web pages as reference hits. It does not
cache page HTML or downloadable PDF assets.

## Source State Rule

fiction 문서라도 외부 웹 자료를 근거로 harness를 바꾸면 아래 표를 남긴다.

| Required field | 뜻 |
| --- | --- |
| Source | 사용한 웹 페이지 또는 검색 대상 |
| Claim allowed | 그 출처로 말할 수 있는 것 |
| Claim blocked | 그 출처만으로 말하면 안 되는 것 |
| Workflow state | `hit_not_cached`, `asset_available_not_downloaded`, `searched_no_hit` 등 |
| Harness effect | 실제로 workflow, template, checklist에 반영할 항목 |

출처가 Source Notes에 없으면 문서 결론의 근거로 쓰지 않는다.

## 대학 기준에서 뽑을 수 있는 축

| Axis | 한국어 풀이 | Harness effect |
| --- | --- | --- |
| Workshop | 초안 제출, 비평, 수정 루프 | draft는 바로 release가 아니다. critique/revision 단계를 둔다. |
| Close reading | 기존 작품을 작법 관점에서 읽기 | 좋은 문장을 베끼지 말고 장면 기능, 시점, 전환을 분석한다. |
| Manuscript | 실제 원고 | 설정표만 쌓지 말고 장면/단편/챕터 원고를 만든다. |
| Research for writers | 작가를 위한 조사 | 논문, 웹, 인터뷰, 기록물을 장면 재료로 바꾸되 source state를 남긴다. |
| Audience | 독자와 매체 | SF 단편, SAGA, 웹연재, 에세이형 기록 중 무엇인지 먼저 정한다. |
| Thesis / capstone | 장기 프로젝트 완성본 | 큰 fiction phase는 최종 산출물과 평가 기준을 둔다. |
| Science writing | 과학을 일반 독자에게 쓰기 | 기술어는 유지하고, 필요한 만큼만 설명한다. |
| Ethics | 비평, 출처, 재현의 책임 | 실존 집단/민감 이념을 직접 복제하지 않고 fictionalization 근거를 둔다. |

## Reference Matrix

| Reference | 확인한 내용 | Harness에 반영할 것 | 쓰면 안 되는 것 | Workflow state |
| --- | --- | --- | --- | --- |
| Harvard Extension School creative-writing program URL check | 요청 후보 URL은 2026-06-19 확인 시 404였다. | Harvard 기준은 아직 확정 규칙으로 쓰지 않는다. | Harvard program rule, thesis rule, admission rule을 현재 문서 근거로 주장하지 않는다. | `searched_no_hit` |
| [MIT Course 21W Catalog](https://catalog.mit.edu/subjects/21w/) | creative writing, science writing, digital media 과목군이 있고, science writing seminar는 workshop, critique, research tools, ordinary readers, audience/publics를 강조한다. thesis 과목은 tutor, revision, oral presentation, committee discussion을 둔다. | science-fiction 작업은 workshop, research-for-writers, audience, revision, thesis-style closeout을 가진다. | MIT가 QFUDS SAGA의 과학성을 보증한다고 쓰지 않는다. | `asset_available_not_downloaded` |
| [SNU College of Humanities department page](https://humanities.snu.ac.kr/academics/department) | 국어국문학과, 비교문학, 공연예술학 등 인문학 교육 단위와 한국어/문학 연구 맥락을 확인했다. | 한국어 독자용 용어 풀이, 문학/언어/비교문화 축을 별도 체크한다. | 이 페이지를 SNU 문예창작 커리큘럼 전체 근거로 쓰지 않는다. | `hit_not_cached` |

## Harness Additions

대학 기준을 fiction workflow에 반영할 때는 아래 gate를 추가한다.

| Gate | 질문 | 통과 조건 |
| --- | --- | --- |
| `craft_source_state` | 참고한 웹 자료가 Source Notes에 있는가? | URL, claim boundary, workflow state가 있다. |
| `craft_term_glossary` | 영어 작법 용어가 한국어로 풀렸는가? | 첫 등장에 짧은 풀이가 있다. |
| `craft_workshop_loop` | 초안이 비평/퇴고 루프를 갖는가? | draft, critique, revision 위치가 분리된다. |
| `craft_scene_output` | 실제 장면 산출물이 있는가? | 설정표만 있지 않고 scene/beat/chapter 목표가 있다. |
| `craft_research_use` | 조사 내용이 장면 기능으로 바뀌었는가? | 출처 요약이 아니라 인물, 갈등, 제도, 비용으로 연결된다. |
| `craft_audience_fit` | 독자와 형식이 정해졌는가? | short, novel, SAGA, anthology, webtoon-like run 중 하나가 있다. |
| `craft_closeout` | phase 종료 기준이 있는가? | release 후보 또는 다음 revision 조건이 있다. |

## 적용 규칙

새 fiction 작업이 "대학식 문예창작 기준"을 요구하면 순서는 이렇다.

1. 외부 source를 확인하고 Source Notes를 남긴다.
2. 확인된 내용만 harness gate로 옮긴다.
3. 출처가 불확실한 대학명은 참고 후보로만 둔다.
4. 과학 SF 작업은 MIT식 science writing 축을 적용한다.
5. 한국어 독자용 문서는 SNU 인문학 축처럼 언어/문학 맥락을 분리해서 점검한다.
6. 장기 SAGA는 thesis/capstone처럼 phase closeout을 둔다.

## Source Notes

| Source | Used for | Workflow state |
| --- | --- | --- |
| `https://extension.harvard.edu/academics/programs/creative-writing-literature-masters-degree-program/` | negative check only; URL returned 404 during current verification | `searched_no_hit` |
| [MIT Course 21W Catalog](https://catalog.mit.edu/subjects/21w/) | science writing, workshop, critique, research-for-writers, audience, thesis/revision process | `asset_available_not_downloaded` |
| [SNU College of Humanities department page](https://humanities.snu.ac.kr/academics/department) | Korean humanities/literature reference layer and Korean-reader support | `hit_not_cached` |
