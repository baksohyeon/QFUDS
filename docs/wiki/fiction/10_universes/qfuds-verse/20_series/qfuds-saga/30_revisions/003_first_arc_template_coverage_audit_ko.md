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
next_gate: apply template coverage checks to 029 first-arc reboot manuscript as chapters are drafted
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

큰 구조는 있다. 누락의 핵심은 새 도구가 아니라 **템플릿 집행**이었고, pre-reboot
prototype 기준의 비대칭은 retro pass로 닫혔다.

- 1-6편 prototype에는 `Series Gate Applied`가 적용됐다.
- `scripts/fiction_gate.py --staged`가 019 이후 한국어 primary/adaptation draft에
  이 표를 요구하므로, 새 029 원고도 같은 차단 규칙을 상속한다.
- active first-arc 작업은 019-024 in-place가 아니라
  [029 reboot manuscript](../20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md)다.

## 템플릿 커버리지 매트릭스

| 전역 템플릿 / 규칙 | 1부 현재 상태 | 판정 | 조치 |
| --- | --- | --- | --- |
| `universe_readme_template` | [qfuds-verse README](../../../README.md)가 universe/IP, continuity, world, works, boundary를 보유 | pass | 없음 |
| `work_readme_template` | [SAGA README](../README.md)가 work shelves, inherited boundary, drafts/revisions/release, reading path를 보유 | pass | 없음 |
| `work_bible_template` | 단일 파일이 아니라 `00_bible/001-016`으로 분산 구현됨. authoring baseline, timeline, local canon, technology limits, cast, POV, relationship, boundary가 각각 존재 | pass with split bible | README와 이 감사 문서가 crosswalk 역할을 유지 |
| `character_sheet_template` | Liora는 [012](../00_bible/012_character_liora_sen_ko.md) full sheet. Mara/Elias/Pell/Last Archive/Noor/Ione은 [016](../00_bible/016_character_ensemble_voices_relationships_ko.md) 미니시트와 013 archetype gate를 상속 | pass for first draft entry | 029 장별 draft가 늘어날 때 인물별 Want/Need/Fear/Wound/Lie drift 재점검 |
| `continuity_audit_template` | field mark, bilingual, fidelity, release audit가 여러 문서에 분산돼 있었지만 이름 그대로의 1부 continuity audit은 없었음 | partial -> covered here | 이 문서를 1부 template coverage + continuity audit record로 둠 |
| `session_brief_template` | 과거 1부 작업은 legacy `.planning` phase와 revision docs로 추적됨. 전역 session brief 형식은 별도 산출물로 남지 않음 | historical gap | 새 prose/revision session은 session brief 또는 GSD phase brief를 남겨야 함 |
| `gsd_phase_brief_template` | 2부는 [004 Arc Two GSD phase brief](../00_workroom/004_arc_two_gsd_phase_brief_ko.md)가 있음. 1부는 legacy planning provenance | pass for future, legacy gap for first arc | 후속 2-6편 retro pass는 bounded phase brief 또는 이 audit을 근거로 실행 |
| `Harness Applied` workflow block | 019-024 모두 보유 | pass | 없음 |
| bilingual sequence rule | Korean primary 019-024, English counterpart 012-017 경로 보유. 029는 한국어 primary 먼저 작성 중 | pass | 029 완료 후 영어 Anglophone adaptation 때 shared continuity 재확인 |
| technical grounding rule | Bitcoin/Genesis, cryptographic death, Hawking/QFUDS boundary 문서가 있음 | pass | alias 추가 시 original term, loss risk, accurate anchor 기록 유지 |
| narrative frame rule | POV/naming bible, episode harness, 1-6편 prototype `Series Gate Applied`, 013 scene cards, 029 `Series Gate Applied`가 있음 | pass for first draft entry | 029 각 장 작성 시 scene-card POV를 벗어나면 중단 |

## continuity audit cross-check

| Dimension | Bible says | Draft/release shows | Match? | Action |
| --- | --- | --- | --- | --- |
| Timeline / era placement | deep-time restoration civilization, Continuity Court era | 019-024가 Waiting City, Continuity Court, Genesis Chain afterlife를 사용 | yes | 없음 |
| Factions & institutions | Bureau Laurien/Laur, Continuity Court, Ledger Houses, Aletheia, Last Archive | 1부 전체에서 반복 등장 | yes | 세력명은 [015](../00_bible/015_factions_canon_naming_ko.md) 유지 |
| Naming / proper nouns | 고유명·필드 마크는 영어 유지, 일반명사는 한국어 우선 | 019-024 Korean primary와 pre-reboot release manifest가 이 규칙을 기록 | yes | 신규 용어 추가 시 glossary 갱신 |
| Technology limits & forbidden claims | Bitcoin/QFUDS/black-hole terms are fiction premise only | release boundary와 draft boundary가 연구 evidence 금지 명시 | yes | 유지 |
| Character knowledge state | Liora limited POV, Last Archive no direct inner POV | prototype 1-6편과 029 prologue gate에 명시 | yes for current scope | 029 Chapter 1 이후 장별 continuity ledger에서 재점검 |
| POV / narrative frame | 기본 3인칭 제한, 필요 시 rotating focalizers | 1부는 Liora 중심으로 고정 | yes | 2부부터 POV 로테이션 후보는 [016]과 [010 episode map](../10_story_design/010_arc_two_episode_map_ko.md) 확인 |

## 누락 / 리스크

| Severity | Issue | Impact | Fix |
| --- | --- | --- | --- |
| P1 | 029는 아직 Prologue만 draft됨 | 1부 active manuscript가 release나 complete draft로 오해될 수 있음 | README/20_drafts/40_release가 모두 release 아님을 명시. Chapter 1-6은 029 안에서 계속 작성 |
| P1 | 029 장별 인물 arc가 013 scene cards에서 drift될 수 있음 | Noor/Ione/Tamas 등 후속 반복 인물이 장면 기능만 있고 욕망 축이 약해질 수 있음 | 029 각 장에 scene-card continuity note를 추가하고 016/013과 대조 |
| P2 | session brief가 1부 legacy 작업에 별도 산출물로 남지 않음 | 나중에 "왜 이 세션에서 이 범위만 했나" 추적이 약함 | 후속 revision session은 `session_brief_template` 또는 GSD phase brief를 먼저 작성 |
| P2 | 떡밥/회수 원장이 005 안에 작게만 있음 | 긴 연재에서 open/partial/resolved 상태가 흩어질 수 있음 | 안정화 후 `00_bible/017` 또는 `30_revisions/004`로 독립 원장화 |

## 즉시 판정

1부 시스템은 전역 템플릿의 큰 축을 갖췄고, pre-reboot prototype의 series gate
비대칭은 닫혔다. 다만 현재 active first-arc는 release 후보가 아니라
[029](../20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md)에서 다시 쓰는
Book 1 draft다.

따라서 다음 작업 우선순위는 새 문서 발명이 아니라 029 Chapter 1 `Exhibit S-0`를
013 scene cards에 맞춰 이어 쓰는 것이다.
