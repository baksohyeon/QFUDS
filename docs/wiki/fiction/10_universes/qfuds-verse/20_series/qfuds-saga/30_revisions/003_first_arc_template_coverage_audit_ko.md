---
doc_id: qfuds_saga_first_arc_template_coverage_audit_ko
title: QFUDS SAGA 1부 전역 템플릿 커버리지 감사
doc_type: summary
stage: reference
status: completed
evidence_role: audit
depends_on:
  - qfuds_saga_series_production_harness_ko
  - qfuds_saga_first_arc_release_immersion_revision_plan_ko
  - qfuds_saga_character_ensemble_voices_relationships_ko
next_gate: apply Series Gate Applied retro pass to episodes 2-6 before treating first arc as fully release-gated
last_updated: 2026-06-21
---

# QFUDS SAGA 1부 전역 템플릿 커버리지 감사

## 목적

사용자 요청에 따라 1부 관련 bible / harness / release 시스템이
`.agent/templates/fiction/`와
[Fiction IP Management Workflow](../../../../../../../../.agent/workflows/fiction-ip-management-workflow.md)의
요구를 빠뜨렸는지 점검한다.

이 문서는 fiction/provenance audit이다. QFUDS 연구 evidence, roadmap status,
physical-source claim이 아니다.

```text
not searched
```

## 감사 대상

- 전역 템플릿:
  [fiction templates](../../../../../../../../.agent/templates/fiction/)
- 전역 workflow:
  [Fiction IP Management Workflow](../../../../../../../../.agent/workflows/fiction-ip-management-workflow.md)
- SAGA work README:
  [QFUDS SAGA](../README.md)
- 1부 release/revision gate:
  [002 release gate](002_first_arc_release_immersion_revision_plan_ko.md)
- 1부 series gate:
  [005 series production harness](../00_workroom/005_series_production_harness_ko.md)

## 결론

큰 구조는 있다. 누락의 핵심은 새 도구가 아니라 **템플릿 집행 기록의 비대칭**이다.

- 1편은 `Series Gate Applied`가 적용됐다.
- 2-6편은 `Harness Applied`와 `Continuity Notes`는 있지만, 새 series gate 기준의
  `Series Gate Applied` 표가 아직 없다.
- `scripts/fiction_gate.py --staged`가 019 이후 한국어 primary/adaptation draft에
  이 표를 요구하므로, 2-6편을 다시 만지는 순간 pre-commit에서 강제된다.

## 템플릿 커버리지 매트릭스

| 전역 템플릿 / 규칙 | 1부 현재 상태 | 판정 | 조치 |
| --- | --- | --- | --- |
| `universe_readme_template` | [qfuds-verse README](../../../README.md)가 universe/IP, continuity, world, works, boundary를 보유 | pass | 없음 |
| `work_readme_template` | [SAGA README](../README.md)가 work shelves, inherited boundary, drafts/revisions/release, reading path를 보유 | pass | 없음 |
| `work_bible_template` | 단일 파일이 아니라 `00_bible/001-016`으로 분산 구현됨. authoring baseline, timeline, local canon, technology limits, cast, POV, relationship, boundary가 각각 존재 | pass with split bible | README와 이 감사 문서가 crosswalk 역할을 유지 |
| `character_sheet_template` | Liora는 [012](../00_bible/012_character_liora_sen_ko.md) full sheet. 1편 Mara/Elias/Pell/Last Archive는 [016](../00_bible/016_character_ensemble_voices_relationships_ko.md) 미니시트 | partial | 2-6편 반복 인물은 각 편 `Series Gate Applied` 때 확인 |
| `continuity_audit_template` | field mark, bilingual, fidelity, release audit가 여러 문서에 분산돼 있었지만 이름 그대로의 1부 continuity audit은 없었음 | partial -> covered here | 이 문서를 1부 template coverage + continuity audit record로 둠 |
| `session_brief_template` | 과거 1부 작업은 legacy `.planning` phase와 revision docs로 추적됨. 전역 session brief 형식은 별도 산출물로 남지 않음 | historical gap | 새 prose/revision session은 session brief 또는 GSD phase brief를 남겨야 함 |
| `gsd_phase_brief_template` | 2부는 [004 Arc Two GSD phase brief](../00_workroom/004_arc_two_gsd_phase_brief_ko.md)가 있음. 1부는 legacy planning provenance | pass for future, legacy gap for first arc | 후속 2-6편 retro pass는 bounded phase brief 또는 이 audit을 근거로 실행 |
| `Harness Applied` workflow block | 019-024 모두 보유 | pass | 없음 |
| bilingual sequence rule | Korean primary 019-024, English counterpart 012-017 경로 보유 | pass | 2-6편 series gate 적용 시 bilingual continuity 재확인 |
| technical grounding rule | Bitcoin/Genesis, cryptographic death, Hawking/QFUDS boundary 문서가 있음 | pass | alias 추가 시 original term, loss risk, accurate anchor 기록 유지 |
| narrative frame rule | POV/naming bible, episode harness, 1편 `Series Gate Applied`가 있음 | pass for 1, partial for 2-6 | 2-6편에 POV person과 standalone ban 표 추가 |

## continuity audit cross-check

| Dimension | Bible says | Draft/release shows | Match? | Action |
| --- | --- | --- | --- | --- |
| Timeline / era placement | deep-time restoration civilization, Continuity Court era | 019-024가 Waiting City, Continuity Court, Genesis Chain afterlife를 사용 | yes | 없음 |
| Factions & institutions | Bureau Laurien/Laur, Continuity Court, Ledger Houses, Aletheia, Last Archive | 1부 전체에서 반복 등장 | yes | 세력명은 [015](../00_bible/015_factions_canon_naming_ko.md) 유지 |
| Naming / proper nouns | 고유명·필드 마크는 영어 유지, 일반명사는 한국어 우선 | 019-024 Korean primary와 40_release build가 이 규칙을 따름 | yes | 신규 용어 추가 시 glossary 갱신 |
| Technology limits & forbidden claims | Bitcoin/QFUDS/black-hole terms are fiction premise only | release boundary와 draft boundary가 연구 evidence 금지 명시 | yes | 유지 |
| Character knowledge state | Liora limited POV, Last Archive no direct inner POV | 1편은 명시 완료, 2-6편은 implied 상태 | partial | 2-6편 `Series Gate Applied`에 POV person 기록 |
| POV / narrative frame | 기본 3인칭 제한, 필요 시 rotating focalizers | 1부는 Liora 중심으로 고정 | yes | 2부부터 POV 로테이션 후보는 [016]과 [010 episode map](../10_story_design/010_arc_two_episode_map_ko.md) 확인 |

## 누락 / 리스크

| Severity | Issue | Impact | Fix |
| --- | --- | --- | --- |
| P1 | 2-6편에 `Series Gate Applied` 표가 아직 없음 | 새 series gate 기준으로는 1부 전체 release gate가 완전히 닫히지 않음 | 020-024에 반복 인물, POV, 인과, 상승, 중심질문, standalone ban을 편별 기록 |
| P1 | 2-6편 반복 인물 Want/Need/Fear/Wound/Lie가 편별로 완전히 차단되지 않음 | Noor/Ione/Tamas 등 후속 반복 인물이 장면 기능만 있고 욕망 축이 약해질 수 있음 | 016에 편별 미니시트 확장 또는 개별 character sheet 작성 |
| P2 | session brief가 1부 legacy 작업에 별도 산출물로 남지 않음 | 나중에 "왜 이 세션에서 이 범위만 했나" 추적이 약함 | 후속 revision session은 `session_brief_template` 또는 GSD phase brief를 먼저 작성 |
| P2 | 떡밥/회수 원장이 005 안에 작게만 있음 | 긴 연재에서 open/partial/resolved 상태가 흩어질 수 있음 | 안정화 후 `00_bible/017` 또는 `30_revisions/004`로 독립 원장화 |

## 즉시 판정

1부 시스템은 전역 템플릿의 큰 축을 갖췄다. 다만 새로 만든 series gate가
1편에만 완전 적용됐으므로, 현재 release 후보는 **구 release gate 통과 +
신 series gate 부분 적용** 상태다.

따라서 다음 작업 우선순위는 새 문서 발명이 아니라 020-024에 같은 gate를
반복 적용하는 것이다.
