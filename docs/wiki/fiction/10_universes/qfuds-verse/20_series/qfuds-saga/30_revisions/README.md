---
doc_id: qfuds_saga_revisions_index_ko
title: QFUDS SAGA Revision Shelf
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_index_ko
next_gate: apply template coverage audit findings to episodes 2-6
last_updated: 2026-06-21
---

# QFUDS SAGA Revision Shelf

이 폴더는 reader-facing release 후보로 가기 전의 revision plan, line edit
control, continuity fix pass를 둔다.

현재 first arc의 기존 revision/provenance 문서는 migration 보존을 위해
`../20_drafts/`에 남아 있다. 새 revision 작업부터 이 폴더를 사용한다.

## Revision Plans

1. [1부 De-jargon·Polish 퇴고 계획](001_first_arc_dejargon_polish_revision_plan_ko.md)
   - 한국어 정본 019-024의 영어 코드스위칭을 자연 한국어로 전환하는 line-edit
     pass. 집행 기준은
     [이중언어 용어규율 글로서리](../00_workroom/003_bilingual_term_discipline_glossary_ko.md).
     검증: naturalness/content-fidelity 에이전트 + 토큰 density 측정.
2. [1부 Release 승격 현장감·묘사 강화 기준](002_first_arc_release_immersion_revision_plan_ko.md)
   - 019-024를 release 후보로 올리기 위한 구조·이해도·기술정확·보이스·리텐션
     게이트. 1편에는 `Series Gate Applied`를 역적용했고, 2-6편은 후속 적용 대상.
3. [1부 전역 템플릿 커버리지 감사](003_first_arc_template_coverage_audit_ko.md)
   - `.agent/templates/fiction/`와 fiction IP workflow 기준으로 1부 바이블 시스템의
     충족/누락/후속 차단 조건을 대조한 감사 기록.

## Boundary

이 폴더는 fiction/provenance 작업 전용이다. QFUDS research evidence,
roadmap status, physical-source claim을 만들지 않는다.

Current research asset workflow state:

```text
not searched
```

Extraction potential:

```text
not_extractable
```
