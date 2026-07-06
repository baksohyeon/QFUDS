---
doc_id: fiction_studio_index_ko
title: Fiction Studio 지도
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - wiki_fiction_index
next_gate: 작업 시작은 011 운영 허브에서 한다. 이 README는 선반 지도만 맡는다
last_updated: 2026-07-06
---

# Fiction Studio 지도

전역 fiction 운영 규칙과 craft/readability 하네스가 사는 선반이다. 작품 canon이나
산문 원고는 여기 두지 않는다. authoring baseline: 2026-06-30.

작업을 **시작**할 때는 표를 훑지 말고 [011 운영 허브](011_fiction_agentic_workflow_guide_ko.md)
하나만 연다. 아래는 "무엇이 어디 있나"를 위한 지도다.

## 먼저 여기

| 목적 | 문서 |
| --- | --- |
| fiction 작업 시작 (단일 운영 허브) | [011 Fiction Agentic Workflow Guide](011_fiction_agentic_workflow_guide_ko.md) |
| 한국어 문장 자연스러움·AI 말투 제거 | [009 한국어 소설 문장 자연스러움 하네스](009_korean_fiction_prose_naturalness_harness_ko.md) |
| 기술·제도·역사 개념 독자 온보딩 | [010 Reader Onboarding Harness](010_reader_onboarding_harness_ko.md) |

## 전체 선반 지도

`유형` 열: `허브`=매번 여기서 시작, `운영 가이드`=IP/GSD 절차 설명(내용 중복 정리
검토 대상), `craft/readability`=작업 중 적용하는 점검 하네스.

| 문서 | 역할 | 유형 |
| --- | --- | --- |
| [001 Fiction IP 관리 시스템](001_fiction_ip_management_system_ko.md) | 003으로 통합됨. 포인터만 남음 | 포인터 |
| [002 Fiction GSD 계획 브리지](002_gsd_planning_bridge_ko.md) | 003으로 통합됨. 포인터만 남음 | 포인터 |
| [003 Fiction GSD 하네스 운영 가이드](003_fiction_gsd_harness_operator_guide_ko.md) | IP·GSD 운영 통합 가이드 (001·002 흡수). 폴더 구조·레이어·bible·체크포인트 | 운영 가이드 |
| [004 창작 문예 하네스](004_creative_writing_craft_harness_ko.md) | 전제·인물·갈등·시점·대사·세계관·주제·페이싱 craft 점검 | craft/readability |
| [005 대학 문예창작 참고 매트릭스](005_university_creative_writing_reference_matrix_ko.md) | 워크숍·창작 프로그램 수준 벤치마크 요청 시 | craft/readability |
| [006 핍진성·개연성 장면 감사 체크리스트](006_prose_verisimilitude_audit_checklist_ko.md) | 장면이 "그럴듯한가"를 따지는 감사표 | craft/readability |
| [007 창작 기법·정치이론 자료조사](007_craft_and_political_theory_research_ko.md) | 비약 없는 노출 + 세계규칙 실증 앵커 자료 | craft/readability |
| [008 에이전틱 픽션 하네스 4관점](008_agentic_fiction_harness_perspectives_ko.md) | 011로 통합됨. 포인터만 남음 | 포인터 |
| [009 한국어 소설 문장 자연스러움 하네스](009_korean_fiction_prose_naturalness_harness_ko.md) | 번역투·AI 말투 탐지·제거 | craft/readability |
| [010 Reader Onboarding Harness](010_reader_onboarding_harness_ko.md) | 어려운 개념을 장면 안에서 풀어내는 점검 | craft/readability |
| [011 Fiction Agentic Workflow Guide](011_fiction_agentic_workflow_guide_ko.md) | **단일 운영 허브.** 매번 여기서 시작 | 허브 |

## 읽기/작업 시작점

- 사람 읽기 시작: [011 운영 허브](011_fiction_agentic_workflow_guide_ko.md).
- 에이전트 작업 시작: 운영 authority
  [.agent/workflows/fiction-ip-management-workflow.md](../../../../.agent/workflows/fiction-ip-management-workflow.md)
  -> 011 허브.
- canon 문서: 없음. 세계 사실/정사는 `10_world/`와 작품 `00_bible/`가 맡는다.
- workflow/agent-facing: 003, 011. (001·002는 003으로, 008은 011로 통합된 포인터)
- 작업 중 적용 reference: 004~007, 009, 010.

## Boundary

```text
fiction/provenance only
research evidence: no
external source claim: no
```

이 README는 새 외부 source, PDF, paper, MCP output, cached asset를 만들지 않는다.
