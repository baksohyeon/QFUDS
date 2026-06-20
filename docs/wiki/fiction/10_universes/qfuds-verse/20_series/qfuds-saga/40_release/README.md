---
doc_id: qfuds_saga_release_index_ko
title: QFUDS SAGA Release Shelf
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_index_ko
next_gate: create release candidate only after revision and continuity checks
last_updated: 2026-06-20
---

# QFUDS SAGA Release Shelf

이 폴더는 독자에게 보여 줄 수 있는 release candidate, bundled read order,
export-ready manuscript를 둔다.

현재 release candidate:

- [001 1부 Release Candidate — The Broken Crown](001_first_arc_release_candidate_ko.md)
  — release **기록(메타데이터)**: 읽기 순서, 영어 counterpart 매핑, 통과 게이트
  (ai-tell CLEAN, naturalness A, 필드 마크 무결성, validate).
- [002 1부 Release 원고 — The Broken Crown](002_first_arc_manuscript_ko.md)
  — 실제 **독자용 조립 원고**(6편 본문 + 필드 마크).

## 소스 / 빌드 모델 (배치 규칙)

이 트랙은 코드의 `src`/`dist`처럼 운영한다.

- **편집 정본(SSOT) = `20_drafts/`** — 모든 prose 수정은 여기서 한다.
- **완성 산출물 = `40_release/`** — drafts에서 **본문만 조립한 읽기 원고**(build).
  production harness 메타데이터·영어 counterpart는 drafts에 남는다.
- draft가 바뀌면 release 원고를 **재생성**한다(release 원고를 수기 편집하지 않는다).

이렇게 두면 prose 사본이 둘이어도 정본은 하나(drafts)라 SSOT가 깨지지 않고,
"완성 읽기본은 release에 물리적으로 존재"한다는 요구도 만족한다.

새 산출물은 한국어 primary draft, 영어 독립 각색판, shared continuity check가
모두 끝난 뒤에만 이 폴더에 둔다.

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
