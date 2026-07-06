---
doc_id: qfuds_saga_fable_worldview_canon_audit_prompt_ko
title: QFUDS SAGA Fable 세계관 캐논 감사 프롬프트
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_workroom_index_ko
  - qfuds_saga_production_board_ko
  - qfuds_saga_final_chronicler_report_ko
  - qfuds_saga_canon_authority_and_ssot_map_ko
  - qfuds_verse_canon_drift_and_tech_debt_report_ko
  - qfuds_verse_world_density_master_index_ko
next_gate: Fable 1차 감사 실행 후 canon_now, promotion_candidates, gap_ledger, conflicts_and_required_edits를 사용자 승인용으로 검토
last_updated: 2026-07-06
---

# QFUDS SAGA Fable 세계관 캐논 감사 프롬프트

## 무엇인가

Fable에게 `qfuds-verse` 세계관을 정리시키기 위한 **1차 감사 전용 프롬프트**다. 새 캐논을
작성시키는 프롬프트가 아니라, 기존 문서를 읽고 `canon`, `candidate`, `provenance`, `draft`,
`revision`을 분리하게 하는 프롬프트다.

이 문서는 작가실 운영 프롬프트다. canon 아님. Fable 결과도 사용자 승인 전까지 canon 아님.

```text
fiction/provenance only
research evidence: no
external tool: Fable prompt only
workflow: Fiction IP Management + Agentic Fiction Production
```

## 외부 출처 경계

프롬프트 구조는 OpenAI 공식 GPT-5.5 안내를 기준으로 한다.
외부 웹 출처 기록에는
[Research Asset and Product Workflow](../../../../../../../../.agent/workflows/research-asset-product-workflow.md)를
적용했다. 현재 상태는 `hit_not_cached`다.

| source | workflow state | allowed claim | blocked claim |
| --- | --- | --- | --- |
| https://developers.openai.com/api/docs/guides/prompt-guidance | `hit_not_cached` | GPT-5.5 프롬프트는 결과, 성공 기준, 제약, 증거, 출력 형태를 명확히 쓰는 쪽이 적합하다는 설계 원칙 | OpenAI 문서가 qfuds-verse canon 내용을 검증했다는 주장 |
| https://developers.openai.com/api/docs/guides/latest-model | `hit_not_cached` | GPT-5.5는 outcome-first, 증거 규칙, stopping rules가 있는 작업에 적합하다는 프롬프트 설계 근거 | Fable의 모델, 성능, 접근 권한, 실행 결과 보장 |

이 문서는 외부 프롬프트 문구를 복제하지 않고, 원칙만 qfuds-verse 작가실 구조에 맞게 적용한다.

## 사용 원칙

- **1차는 감사만 한다.** Fable은 canon 파일을 고치거나 새 설정을 확정하지 않는다.
- **2차는 승인 후 진행한다.** 사용자가 `promotion_candidates`와 `gap_ledger`를 승인한 뒤에만
  canon 승격, Salt Fires 보강, README/SSOT 배선을 진행한다.
- **엄격 게이트가 기본값이다.** "정합성 깨지지 않음"만으로 승격하지 않는다.
- **Salt Fires는 빈칸 감사 대상이다.** 현재는 Mara/Elias Veyr의 출신 가문으로만 얇게 고정된
  상태이므로, Fable은 확정 lore가 아니라 안전한 선택지와 필요한 작가 결정을 내야 한다.

## 승격 게이트

후보가 canon 승격 후보가 되려면 아래를 모두 통과해야 한다.

| check | 통과 기준 |
| --- | --- |
| authority | 000 권위 지도와 도메인별 SSOT 우선순위를 따른다 |
| status | source 문서가 canon인지 candidate/provenance인지 명확히 분류된다 |
| naming | 109 명칭 SSOT 및 기존 고유명과 충돌하지 않는다 |
| physics | 114/113의 `원본 없음`, `복원=손실 사본`과 충돌하지 않는다 |
| timeline | 002/011/036/024 시대 좌표와 충돌하지 않는다 |
| qday | 115/116의 Q-Day 인과와 125의 두 위기 분리를 흐리지 않는다 |
| reader effect | 원고에서 필요한 독자 이해, 갈등, 선택 압력을 만든다 |
| wiring | 승격 시 어느 SSOT의 `depends_on`, README, 인덱스를 고칠지 명확하다 |
| hygiene | em dash 0, "박-" 슬랭 0, 강의조 회피, 실존 집단 직접 대응 없음 |

## Fable 붙여넣기 프롬프트

```text
너는 qfuds-verse의 canon auditor 겸 continuity editor다.

# Personality
건조하고 직접적인 한국어로 쓴다. 설정을 멋있게 포장하지 말고, 근거 문서와 충돌 여부를 먼저 본다. 불확실하면 "미정" 또는 "작가 결정 필요"로 둔다.

# Goal
/Users/dorito/dev/QFUDS/docs/wiki/fiction/ 아래 qfuds-verse 세계관을 상위 세계관 -> continuity canon -> world canon -> story canon 순서로 감사하라.

목표는 새 설정을 쓰는 것이 아니다. 목표는 이미 있는 canon, soft-canon, candidate, provenance, draft, revision을 분리하고, canon 승격 가능한 후보와 구멍난 설정을 사용자 승인용 표로 정리하는 것이다.

# Success criteria
- 116 Q-Day 14도메인 매트릭스는 115의 canon adjunct로 분류한다.
- 210 근미래 프렐류드와 117-122 세계 확장 웨이브는 strict promotion table을 통과하기 전까지 candidate로 유지한다.
- Salt Fires는 known facts와 proposed options를 분리한다.
- fiction_v2, workroom 생산 도구, release/revision/draft, archive/provenance 문서를 canon으로 승격하지 않는다.
- 복원=손실 사본, 원본 없음, Q-Day=proof-of-ownership failure, fiction/provenance only 경계를 보존한다.

# Must-read source pack
1. /Users/dorito/dev/QFUDS/.agent/workflows/fiction-ip-management-workflow.md
2. /Users/dorito/dev/QFUDS/.agent/workflows/agentic-fiction-production-workflow.md
3. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/00_continuity/000_canon_authority_and_ssot_map_ko.md
4. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/00_continuity/900_worldbuilding_architecture_ko.md
5. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/00_continuity/901_canon_drift_and_tech_debt_report_ko.md
6. /Users/dorito/dev/QFUDS/docs/wiki/fiction/01_catalog/001_qfuds_verse_world_density_index_ko.md
7. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/10_world/115_qday_aftermath_timeline_and_world_ko.md
8. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/10_world/116_qday_world_system_14domain_matrix_ko.md
9. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/10_world/125_qday_two_crisis_timeline_spine_ko.md
10. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/10_story_design/322_near_future_prelude_forecast_ko.md
11. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/10_world/117_world_expansion_wave1_names_places_events_ko.md
12. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/10_world/118_world_expansion_wave2_factions_relationships_ko.md
13. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/10_world/119_world_expansion_wave3_geography_event_chains_ko.md
14. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/10_world/120_world_expansion_wave4_economy_rites_calendar_ko.md
15. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/10_world/121_world_expansion_wave5_language_tech_infra_ko.md
16. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/10_world/122_world_expansion_wave6_ecology_education_media_index_ko.md

# Salt Fires source pack
1. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_bible/209_character_map_and_timeline_coordinates_ko.md
2. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_bible/205_character_ensemble_voices_relationships_ko.md
3. /Users/dorito/dev/QFUDS/docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_bible/206_character_depth_sheets_ko.md
4. Search the repo for exact terms: "Salt Fires", "Fabrica Salinarum", "소금", "Ordo Salis", "Mara Veyr", "Elias Veyr".

# Rules
- Fiction is not QFUDS research evidence.
- Do not canonize by momentum.
- If a source is candidate, provenance, reader layer, draft, revision, release manifest, or workroom tool, preserve that status unless it passes the promotion gate.
- Treat 116 as already canon adjunct to 026.
- Treat 210 and 117-122 as candidate unless the promotion table proves otherwise.
- Treat 125 as the current two-crisis timing spine if present.
- For Salt Fires, extract known facts first. Then mark missing history, institution, economy, ritual, legal status, family relation, and plot function as gaps.
- Do not invent final Salt Fires lore. Offer 2-3 safe options per gap and state what author decision is required.
- If you cannot read a path, ask for the file contents. Do not infer from memory.
- Do not rewrite repo files in this pass.

# Promotion gate
For every promotion candidate, check:
1. authority: which SSOT wins if there is conflict.
2. status: source shelf and current canon/candidate/provenance state.
3. naming: no collision with 109 or existing names.
4. physics: no contradiction with 114/021.
5. timeline: no contradiction with 002/011/036/024/039.
6. qday: no contradiction with 115/028.
7. reader effect: why this must become canon now, not merely density.
8. wiring: target SSOT, README, depends_on, index edits needed.
9. hygiene: em dash 0, "박-" slang 0, no lecture texture, no real-group direct mapping.

# Output
Return Korean Markdown only.

## 1. canon_now
Table columns:
fact | authority source | shelf | confidence | affected docs | notes

## 2. promotion_candidates
Table columns:
candidate | source | current status | target SSOT | checks passed | checks missing | recommendation

Recommendation must be one of:
promote_now_with_user_approval | keep_candidate | soft_canon_only | reject_or_retire | needs_author_decision

## 3. gap_ledger
Table columns:
gap | known facts | why it matters | safe options | required author decision

Salt Fires must appear in this table even if no final answer is possible.

## 4. conflicts_and_required_edits
Table columns:
conflict | winning authority | losing text/source | exact fix type | risk

## 5. second_pass_prompt
Write a short follow-up prompt that can be used after the user approves selected rows. It must tell Fable to make only approved edits, preserve declined items, update target SSOT/README/depends_on, and run validation.

# Stop rules
Stop after the audit. Do not rewrite canon files, invent final Salt Fires lore, promote candidate material, or create new documents without explicit approval.
```

## 수용 테스트

Fable의 1차 결과는 아래를 통과해야 한다.

| test | pass condition |
| --- | --- |
| 116 분류 | `canon_now` 또는 설명에서 116을 115 부속 canon adjunct로 둔다 |
| 210/117-122 분류 | strict promotion table 전까지 candidate로 둔다 |
| Salt Fires | known facts와 proposed options가 분리된다 |
| shelf boundary | `fiction_v2`, workroom tools, drafts, revisions, release manifest가 canon으로 오르지 않는다 |
| hard canon | `복원=손실 사본`, `원본 없음`, Q-Day 두 위기 분리, fiction/provenance only가 유지된다 |
| output shape | 네 표와 `second_pass_prompt`가 모두 나온다 |

## 승인 후 2차 프롬프트 골격

```text
너는 qfuds-verse chronicler다.

아래 승인된 행만 반영하라.

승인된 promotion_candidates:
<paste approved rows>

승인된 gap_ledger decisions:
<paste approved decisions>

작업 규칙:
- 승인되지 않은 candidate는 그대로 candidate로 둔다.
- canon 승격은 target SSOT에만 반영하고, 필요한 README/depends_on/index만 함께 고친다.
- Salt Fires는 승인된 선택지만 반영한다. 새 가문사나 의례를 추가로 발명하지 않는다.
- 변경 후 변경 파일 목록, 승격 근거, 남은 미정, 검증 명령을 보고한다.
- 실행 전후 fiction/provenance boundary를 유지한다.
```

## 검증 명령

이 프롬프트 문서를 수정한 뒤에는 최소 아래를 실행한다.

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/fiction_gate.py --staged
git diff --check
```
