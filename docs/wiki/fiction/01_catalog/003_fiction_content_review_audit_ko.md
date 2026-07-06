---
doc_id: fiction_content_review_audit_ko
title: Fiction Content Review Audit
doc_type: summary
stage: reference
status: draft
evidence_role: audit
depends_on:
  - fiction_folder_classification_audit_ko
  - fiction_studio_index_ko
  - fiction_agentic_workflow_guide_ko
  - qfuds_saga_first_arc_template_coverage_audit_ko
  - qfuds_verse_canon_drift_and_tech_debt_report_ko
next_gate: continue folder-by-folder review with qfuds-verse continuity and world shelves
last_updated: 2026-07-06
---

# Fiction Content Review Audit

작성 기준일: 2026-07-06 KST. 이 문서는 `docs/wiki/fiction/` 하위 문서를
폴더 단위로 직접 읽고, 무엇이 운영 규칙인지, 무엇이 설정·원고·기획·수정 흔적인지
구분하기 위한 검토 원장이다.

이 문서는 새 캐논을 만들지 않는다. 기존 문서의 성격, 사용 여부, 정리 후보만
기록한다.

```text
fiction/provenance only
QFUDS research evidence: no
roadmap status: unchanged
external source claim: no
```

## 현재 결론

첫 검토 범위는 `00_studio/`와 `.agent/templates/fiction/`이다.

현재 확인된 사실은 다음과 같다.

- `.agent/templates/fiction/`은 버려진 폴더가 아니다. `tools/saga-fiction-studio`
  skill들과 SAGA 문서가 직접 참조한다.
- `00_studio/`는 canon이나 draft 선반이 아니라 전역 운영·craft·readability
  하네스 선반이다.
- 작업 시작점은 [00_studio README](../00_studio/README.md) 전체 표가 아니라
  [011 Fiction Agentic Workflow Guide](../00_studio/011_fiction_agentic_workflow_guide_ko.md)다.
- 기존 감사 문서들은 템플릿 부재가 아니라 **템플릿 집행 공백**을 문제로 기록한다.
- 특히 `session_brief_template`, `style_packet_template`, `continuity_audit_template`,
  `chronicler_pass_template` 계열은 "개념 또는 부분 적용"과 "독립 산출물 생성"을
  구분해야 한다.

## `.agent/templates/fiction/` 사용 상태

| 템플릿 | 확인된 사용 상태 | 판단 |
| --- | --- | --- |
| `universe_readme_template.md` | [qfuds-verse README](../10_universes/qfuds-verse/README.md)가 universe/IP, continuity, world, works, boundary 역할을 수행한다고 1부 템플릿 감사가 기록 | 유지. 새 universe 생성용 기준 |
| `work_readme_template.md` | [SAGA README](../10_universes/qfuds-verse/20_series/qfuds-saga/README.md)가 work shelf와 읽기 경로를 수행한다고 1부 템플릿 감사가 기록 | 유지. 새 work 생성용 기준 |
| `work_bible_template.md` | 단일 파일이 아니라 SAGA `00_bible/` 다중 문서로 분산 구현 | 유지. split bible crosswalk 필요 |
| `character_sheet_template.md` | Liora full sheet, ensemble/character depth sheet, Sael origin sheet 등이 직접 참조 | 사용 중 |
| `continuity_audit_template.md` | 1부 템플릿 감사에서 partial -> covered here로 처리. `continuity-pass` skill도 직접 참조 | 사용 중이나 독립 audit 산출물은 불규칙 |
| `session_brief_template.md` | `saga-showrunner` skill이 참조. 1부 legacy 작업에는 별도 session brief가 남지 않았다고 기록 | 미래 작업용. 과거 산출물 공백 |
| `gsd_phase_brief_template.md` | `00_studio/001-003`, workflow, Arc Two phase brief가 참조 | 사용 중 |
| `saga_production_board_template.md` | `saga-showrunner` skill과 SAGA production board 흐름이 참조 | 사용 중 |
| `chapter_intent_card_template.md` | `scene-writer` skill과 SAGA `409_chapter_intent_card_template_ko.md`가 참조 | 사용 중 |
| `review_wave_protocol_template.md` | agentic production workflow가 참조. SAGA revision/review gate에 부분 적용 | 부분 적용 |
| `chronicler_pass_template.md` | `continuity-pass` skill, 901 tech-debt report가 참조. 901은 Chronicler Pass를 P1로 기록 | 필요하나 본문 이관 pass는 미완료 |
| `style_packet_template.md` | `scene-writer` skill이 참조. 901은 QFUDS Style Packet을 부분 상태로 기록 | 부분 적용 |
| `truth_state_ledger_template.md` | `continuity-pass` skill이 참조. 901은 Truth-State Ledger 초안 작성됨으로 기록 | 초안 있음, 운영 정착 필요 |
| `reader_retention_gate_template.md` | `reader-retention-gate` skill과 production workflow가 참조 | 사용 중 후보. 실제 gate 산출물은 folder별 확인 필요 |

판정: 템플릿은 살아 있다. 다만 모든 템플릿이 "복사해서 채운 독립 문서"로
남은 것은 아니다. 일부는 README, bible, revision audit, workroom 문서에 분산 구현됐고,
일부는 다음 prose/revision session부터 강제해야 할 빈 칸으로 남아 있다.

## `00_studio/` 내용 검토

| 문서 | 내용 성격 | 현재 판단 | 정리 후보 |
| --- | --- | --- | --- |
| [README](../00_studio/README.md) | 전역 studio 선반 지도 | 유지. 시작점은 011이라고 이미 명시 | `last_updated`만 다음 정리 때 갱신 후보 |
| `011_fiction_agentic_workflow_guide_ko.md` | fiction 작업 단일 운영 허브 | active entry. 매 작업 시작점 | 유지 |
| `001_fiction_ip_management_system_ko.md` | (구) fiction/IP 관리 규칙 요약 | 2026-07-06 003으로 통합. 포인터만 남음 | 완료. 포인터 유지(doc_id 보존) |
| `002_gsd_planning_bridge_ko.md` | (구) GSD와 fiction 작업 연결 규칙 | 2026-07-06 003으로 통합. 포인터만 남음 | 완료. 포인터 유지(doc_id 보존) |
| `003_fiction_gsd_harness_operator_guide_ko.md` | IP·GSD 운영 통합 가이드 (001·002 흡수) | 폴더 구조·레이어·bible·체크포인트를 담은 단일 운영 가이드 | 완료 |
| `004_creative_writing_craft_harness_ko.md` | 전제, 인물, 갈등, 시점, 세계관 등 craft 기준 | reference로 유지 | 009/010과 충돌하지 않게 "craft 일반"으로 고정 |
| `005_university_creative_writing_reference_matrix_ko.md` | 대학 창작/워크숍 기준 참고 매트릭스 | 외부 참고 근거가 있는 reference | 평소 시작 문서 아님. archive 아님 |
| `006_prose_verisimilitude_audit_checklist_ko.md` | 장면 핍진성·개연성 감사표 | prose/revision 때 유효 | 009/010과 중복되는 문체 항목은 나중에 링크 중심 축약 가능 |
| `007_craft_and_political_theory_research_ko.md` | 비약 없는 노출과 정치·경제 앵커 자료 | 특정 세계규칙/노출 문제에 대한 reference | active entry 아님. 세계관 본문과 중복 여부를 `10_world/106` 검토 때 재확인 |
| `008_agentic_fiction_harness_perspectives_ko.md` | (구) writer/critic/reader/continuity 관점 설명 | 2026-07-06 011의 `관점 요약` 절로 통합. 포인터만 남음 | 완료. 포인터 유지(doc_id 보존, 407 depends_on·415 참조 때문에 삭제 대신 stub) |
| `009_korean_fiction_prose_naturalness_harness_ko.md` | 한국어 문장 자연스러움, 번역투·AI 말투 제거 | active prose quality gate | 유지 |
| `010_reader_onboarding_harness_ko.md` | 어려운 기술·제도·역사 개념을 장면 안에서 풀기 위한 gate | active onboarding gate | 유지 |

## 혼란의 원인

`00_studio/` 자체가 문제라기보다, 아래 성격의 문서가 같은 선반에 함께 보이는 것이
혼란을 만든다.

- 운영 허브: 011 (008 관점 요약 흡수)
- 운영 통합 가이드: 003 (001·002 흡수)
- 통합 후 포인터: 001, 002, 008
- craft/reference 하네스: 004, 005, 006, 007
- 실제 원고 품질 gate: 009, 010

2026-07-06 정리 루프에서 001·002는 003으로, 008은 011로 통합했다(포인터만 남김,
doc_id 보존). 남은 정리 방향은 삭제가 아니라 README와 catalog에서 역할을 더 강하게
나누는 것이다. 특히 "작업 시작은 011, 원고 품질은 009/010, 나머지는 필요할 때만
참조"라는 규칙을 유지하면 된다.

## `01_catalog/` 내용 검토

| 문서 | 내용 성격 | 현재 판단 | 정리 후보 |
| --- | --- | --- | --- |
| [README](README.md) | fiction 전체의 active shelf, active work, migration decision record | active catalog entry. 사람이 먼저 보는 catalog 시작점 | 유지. 실행 지시는 production board와 011로 넘기는 현재 구조가 적절 |
| [001 world density index](001_qfuds_verse_world_density_index_ko.md) | qfuds-verse world density, 117-122 candidate wave, 003 continuity expansion을 한 장에 묶은 보조 색인 | catalog 하위의 특수 색인. active work 시작점 아님 | `canon 아님`, `candidate register` 신호를 유지. `10_world/117-122` 검토 때 상태 문구 재확인 |
| [002 folder classification audit](002_fiction_folder_classification_audit_ko.md) | 폴더 구조, archive/tool/plugin 분리, 다음 루프 후보 | active cleanup state board | 유지. 이 문서와 역할 분리 완료 |
| 이 문서 | 폴더별 내용 검토, template 집행 상태 | active review ledger | 계속 갱신 |

### `01_catalog/` 판단

`01_catalog/`는 유지한다. 다만 안에는 두 종류가 섞여 있다.

- 전체 fiction shelf/catalog: [README](README.md), [002 folder classification audit](002_fiction_folder_classification_audit_ko.md), 이 문서
- qfuds-verse 전용 세계 밀도 색인: [001 world density index](001_qfuds_verse_world_density_index_ko.md)

따라서 `001`은 "fiction 전체 catalog"가 아니라 qfuds-verse world/candidate density
색인으로 읽어야 한다. `001`이 세계 밀도와 후보 이름을 많이 담고 있어 처음 읽으면
canon처럼 보일 수 있지만, 본문은 `캐논 상태: 관리용 색인(candidate register)`와
`새 캐논·새 고유명 생성 안 함`을 명시한다. 이 경계를 유지한다.

### 범위 밖에서 발견한 hygiene 항목

[416 Fable worldview canon audit prompt](../10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/416_fable_worldview_canon_audit_prompt_ko.md)는
[001 world density index](001_qfuds_verse_world_density_index_ko.md)를 must-read로
참조하면서 `/Users/dorito/dev/QFUDS/...` 절대 경로를 여러 줄 포함한다. `01_catalog/`
문제는 아니지만, `00_workroom/` 검토 때 repo-relative path로 바꾸는 hygiene 후보로
남긴다.

## 다음 검토 순서

1. `10_universes/qfuds-verse/00_continuity/`를 검토한다. canon 권위·드리프트·연표가
   서로 충돌하지 않는지 본다.
2. `10_universes/qfuds-verse/10_world/`를 검토한다. `canon`, `candidate`, `reference`
   상태가 실제 내용과 맞는지 본다.
3. 그 다음 SAGA 하위 `00_workroom/`, `00_bible/`, `10_story_design/`, `20_drafts/`,
   `30_revisions/`, `40_release/` 순서로 내려간다.

## 지금은 하지 않을 것

- `00_studio/` 문서를 병합하거나 삭제하지 않는다.
- `.agent/templates/fiction/`을 제거하지 않는다.
- partial template를 pass로 승격하지 않는다.
- fiction 문서를 QFUDS 연구 evidence처럼 다루지 않는다.
