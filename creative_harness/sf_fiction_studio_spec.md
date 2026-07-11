---
doc_id: sf_fiction_studio_spec_ko
title: 범용 SF 창작 스튜디오 개선 스펙
doc_type: guide
stage: reference
status: completed
evidence_role: provenance
depends_on:
  - fiction_creative_writing_craft_harness_ko
  - fiction_university_creative_writing_reference_matrix_ko
next_gate: run one real work through the chapter or release tier and measure friction
last_updated: 2026-07-11
---

# 범용 SF 창작 스튜디오 개선 스펙

## Problem Statement

현재 창작 시스템은 QFUDS SAGA의 과거 경로, 한국어-first 정책, 금지어 검사,
중복 체크리스트가 글로벌 규칙에 섞여 있다. 그 결과 다른 SF 작품을 시작하기
어렵고, 설정과 검수 문서는 늘어나지만 실제 문장·장면·수정 능력을 훈련하는 증거는
약하다.

## Target Users

- QFUDS와 무관한 새 SF 단편·장편을 쓰는 작가
- 세계관·연속성 정리는 에이전트에게 맡기되 창작 결정권은 유지하려는 작가
- 한국어, 영어, 이중언어 등 작품별 언어 정책을 고르려는 작가
- hard SF, social SF, literary SF, horror, technothriller를 넘나드는 작가

## Goals

1. 글로벌 studio 규칙에서 QFUDS SAGA와 특정 언어 정책을 제거한다.
2. 사변적 전제→제한·비용→인물 선택→결말 비용의 인과를 모든 SF 작업의 core로 둔다.
3. reading lab, 단일 기술 실험, workshop, revision plan, revision memo를 실제 산출물로 남긴다.
4. 외부 `story-skills`는 연속성·링크·상태 검증 엔진으로 재사용하고 창작 판단과 분리한다.
5. `docs/wiki/fiction/`은 legacy read-only로 유지하고 active routing에서 제거한다.

## Non-Goals

- 기존 qfuds-verse canon이나 보존 문서를 전면 재작성하지 않는다.
- 모든 작품을 하나의 폴더 스키마로 즉시 마이그레이션하지 않는다.
- 대학 교육과정을 그대로 복제하거나 특정 작가의 스타일을 모사하지 않는다.
- 단어 블랙리스트나 AI 탐지 점수로 작품 품질을 판정하지 않는다.
- `tools/story-skills` vendored submodule의 upstream 코드를 이 작업에서 포크하지 않는다.

## User Stories

- 새 SF 작가로서, QFUDS 문서를 읽지 않고도 새 universe와 work를 시작하고 싶다.
- 작가로서, 작품마다 언어·문체·하위 장르 규칙을 선택하고 싶다.
- 비평을 받는 작가로서, 에이전트가 내 의도를 덮어쓰지 않고 텍스트 근거를 보여 주길 원한다.
- 장편 작가로서, 인물 사망·지식 상태·약속 회수 같은 연속성 오류는 기계적으로 잡고 싶다.
- 퇴고하는 작가로서, 구조 문제를 문장 polish로 숨기지 않고 변경 이유를 추적하고 싶다.

## Must-Have Requirements (P0)

### P0-1. Generic authority split

Acceptance criteria:

- [x] `fiction-production` skill은 QFUDS roadmap을 필수 읽기로 요구하지 않는다.
- [x] 전역 workflow와 template은 SAGA 역할명과 한국어-first를 기본값으로 강제하지 않는다.
- [x] QFUDS 연구/fiction 경계는 repository boundary와 fiction 전용 source workflow로 분리한다.
- [x] 작품별 정책은 work README와 필요할 때 style packet에 기록한다.

### P0-2. Craft loop

- [x] core harness에 reading-as-writer, micro-imitation, draft, workshop,
  revision plan, macro revision, prose polish, revision memo가 있다.
- [x] workshop 출력은 관찰→독자 효과→근거→질문 순서를 사용한다.
- [x] 문장 polish는 구조·인과·POV·장면 수정 뒤에만 실행된다.

### P0-3. SF core

- [x] 사변 요소마다 capability, limit, cost, vulnerability, failure mode,
  second-order effect가 기록된다.
- [x] 전제를 제거해도 같은 선택·결말인지 substitution test를 한다.
- [x] opening, exposition, science accuracy, ending gate가 장르 선택을 존중한다.

### P0-4. Active vs legacy paths

- [x] `docs/wiki/fiction/`은 legacy read-only로 표시된다.
- [x] active control files의 숫자 접두사 제거 전 경로가 모두 고쳐진다.
- [x] closed SAGA paths는 실행 경로가 아니라 `git show` provenance로만 남는다.

### P0-5. Tool boundaries

- [x] `tools/story-skills`는 deterministic continuity engine으로 문서화한다.
- [x] `tools/saga-fiction-studio`는 legacy SAGA adapter로 분류한다.
- [x] generic workflow는 외부 submodule이 없어도 최소 기능으로 동작한다.

## Nice-to-Have (P1)

- work별 `story-skills` schema-v2 adapter와 migration command: 실제 장편 채택 전까지 deferred
- 장르 모듈: hard SF, social SF, literary SF, horror, technothriller: completed
- revision plan / memo 전용 템플릿: completed
- 대표 단편 하나에 대한 before/after evaluation fixture: 실제 작품 수정 시 수행

## Future Considerations (P2)

- 원고 AST나 frontmatter를 이용한 POV·지식상태 자동 검사
- word-count, promise/payoff, timeline을 CI에 연결
- 독자 페르소나 결과의 통계적 집계
- 별도 저장소로 fiction studio를 분리하는 것

## Success Metrics

Leading indicators:

- active control 파일의 stale path 0건
- 새 work 시작 시 QFUDS research doc 필수 읽기 0건
- substantial revision마다 revision plan과 memo 존재
- 검증 명령이 active path와 실제 template을 일치시킴

Lagging indicators:

- 냉독자 반복 이탈 지점 감소
- 구조 수정 이후 문장 polish 재작업량 감소
- 새 작품에서 세계관 설정만 쌓이고 초고가 없는 기간 감소
- continuity 오류가 독자 테스트 전에 기계 검사에서 발견되는 비율 증가

## Timeline / Phasing

1. P0 문서·skill·template·gate 정합성 수정
2. active 작품 하나에 새 loop 적용
3. `story-skills` adapter 여부 결정
4. 필요하면 fiction studio를 QFUDS repo 밖 독립 저장소로 분리

## Completion Evidence

- 운영 진입점: `creative_harness/fiction_studio_operating_guide.md`
- fiction 전용 외부 자료 경계: `.agent/workflows/fiction-source-intake-workflow.md`
- release baseline과 승격: fiction IP/production workflow 및 release checklist
- workshop/revision: workshop response, revision plan, revision memo templates
- 기계 계약: `scripts/fiction_gate.py`와 `tests/test_fiction_gate.py`
- 선택형 장르 질문: `creative_harness/craft/sf_genre_lenses.md`

## Open Questions

- 별도 저장소 분리는 P0 검증 뒤 결정한다. 현재는 repository boundary만 분리한다.
- 기존 QFUDS universe 문서의 오래된 plain-text shelf 표기는 역사 기록인지 active
  instruction인지 파일별로 구분한다.
- 전역 prose lint는 hard gate보다 작품별 style profile 기반 warning이 적합하다.
