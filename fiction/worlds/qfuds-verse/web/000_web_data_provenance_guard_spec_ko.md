---
doc_id: qfuds_verse_web_data_provenance_guard_spec_ko
title: 웹 데이터 provenance 가드 — 설계 스펙 (2026-07-06)
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - qfuds_verse_shelf_renumber_map_ko
next_gate: 사용자 스펙 리뷰 → writing-plans로 구현 계획 작성 → TDD로 가드+테스트 구현
last_updated: 2026-07-10
---

# 웹 데이터 provenance 가드 — 설계 스펙 (2026-07-06)

## 무엇을 푸는가

`web/data/chronicle-data.js`와 `web/data/lore-data.js`는 본문 곳곳에 원본 문서를
가리키는 doc-번호 참조(예: `기전 (021)`, 헤더의 `출처:` 줄)를 담는다. 2026-07-06
선반 밴드 재번호(417 매핑)로
그 번호들이 옛 값을 가리켜 stale이 됐다.

앞선 "코스메틱" 패스는 두 파일의 헤더 `출처:` 주석만 고쳤고, 본문에 남은 inline
참조 7개를 놓쳤다:

- `lore-data.js`: `기전 (021)`, `(036)`, `(040)`, `(039)`, `(024)`
- `chronicle-data.js`: `(004)`, `(011)`

이 재발을 손이 아니라 **테스트 실패로 막는 것**이 이 스펙의 목표다.

## 왜 "생성기"가 아닌가

`build_saga_digest.py`는 문서의 frontmatter + 첫 문단을 그대로 떠서 digest를
만든다(문서 → 요약). 두 데이터 파일은 그런 파생물이 아니다:

- 손으로 쓴 HTML 산문(`body`), 용어 툴팁 `T()` 마이크로카피
- 큐레이션된 지식 그래프(`links` 무방향 간선), `era`/`idx` 순서
- 14도메인 매트릭스(`broke`/`power`/`anchor`/`spice`)

이 내용은 **원본 마크다운에 존재하지 않는다.** 웹앱 UX를 위해 새로 쓴 것이다.
"문서에서 생성"은 읽을 원천이 없어 성립하지 않는다. 데이터를 먼저 문서 안 구조화
블록으로 이관해야 하는데, 그건 문서의 성격 자체를 바꾼다(범위 밖).

## 왜 RAG / PageIndex가 아닌가

이 문제는 **검색(retrieval)이 아니라 참조 무결성(referential integrity)**이다.
`world 113`이 실재 파일을 가리키는가 — 유사도가 아니라 **정확 일치(equality)**
질문이다.

| 필요 속성 | 결정적 가드 | RAG / PageIndex |
| --- | --- | --- |
| 결정적(같은 입력→같은 결과) | 예 | 아니오 (LLM 추론) |
| 오프라인·무료·CI 게이트 | 예 | 아니오 (API 키·호출) |
| 환각 없음 | 예 (파일 존재는 사실) | 아니오 |
| 의존성 | Python stdlib | LLM + LiteLLM |

RAG를 이 린터에 쓰면 모든 축에서 더 나쁘다.

**PageIndex의 실제 자리는 이 레포에 이미 있다** —
[Research Asset Digitization Workflow](../../../../.agent/workflows/research-asset-digitization-workflow.md)가
외부 연구 논문 PDF를 마크다운(구조+전문)으로 변환하는 MCP로 쓴다. 우리 데이터
파일의 stale 참조와는 무관하다.

**RAG의 별건 자리(범위 밖):** 커져가는 lore+world 코퍼스에 대한 의미 Q&A(에이전트/
웹앱이 캐논을 문서 추론으로 답하거나, bespoke 데이터 집필 시 원문 구절 검색). 필요
하면 별도 스펙으로 다룬다. 이 스펙은 그것을 하지 않는다.

## 설계

### 1. 참조 형식 — shelf 한정 토큰

모든 provenance 참조를 모호하지 않은 shelf 한정 토큰으로 정규화한다. 재번호로
bare 번호가 선반 간 충돌하기 때문이다(같은 `024`가 여러 선반에 있음).

- 재번호된 선반: `continuity 003`, `world 113`, `bible 201`, `story 310`,
  `workroom 408`
- 불변 문서(옛 번호 유지): `draft 024`, `prototype 018`
  — 재번호 불변 규칙(417)에 따라 `20_drafts`(원고 029~036·프로토타입 015~028),
  `30_revisions`, `90_archive`, `40_release`는 옛 번호를 유지한다. 이 토큰이 있으면
  가드는 재번호를 기대하지 않는다.

가드 정규식은 **이 한정 토큰만** 매칭한다. bare `(2008)`(연도)나 bare `(039)`는
매칭하지 않아 오탐이 없다.

### 2. `scripts/check_web_data_provenance.py`

Python stdlib만 사용(레포 관례: `agent_workflow_guard.py` 스타일).

동작:

1. **진실 맵 구성** — 실제 선반 디렉터리를 스캔해 `{shelf: {존재하는 번호}}`를
   만든다. 선반은 두 루트에 걸친다:
   - `qfuds-verse/00_continuity` (continuity)
   - `qfuds-verse/10_world` (world)
   - `qfuds-verse/20_series/qfuds-saga/00_bible` (bible)
   - `qfuds-verse/20_series/qfuds-saga/10_story_design` (story)
   - `qfuds-verse/20_series/qfuds-saga/00_workroom` (workroom)
   - `draft`/`prototype`는 `20_drafts` 하위(원고·`_versions/` 프로토타입)에서
     번호 집합을 모은다.
2. **참조 추출** — 두 데이터 파일에서 한정 토큰을 file:line과 함께 모은다.
3. **판정** — 해석되지 않는 토큰마다 오류를 쌓고, 있으면 exit 2 + 위반 토큰·
   위치·해당 선반의 유효 번호 힌트를 출력. 없으면 exit 0.

관례상 인자 없이 전체 검사; `--staged`는 뒤 확장 여지로 남긴다(초기 구현엔 불필요).

### 3. Fix 패스

놓친 inline 참조를 해석해 한정 토큰으로 바꾸고, 헤더 `출처:` 주석도 같은 토큰
형식으로 통일한다.

| 파일 | 현재(옛) | 조치 | 근거 |
| --- | --- | --- | --- |
| lore | `기전 (021)` | `world 113` | 021→113 restoration_mechanism_correction |
| lore | `(036)` | `continuity 003` | 036→003 far_future_deep_time_chronicle |
| lore | `(040)` | `world 126` | 040→126 deeptime_catastrophe_pillar |
| lore | `(039)` | `world 125` | 039→125 qday_two_crisis_timeline_spine |
| lore | `(024)` | `draft 024` (유지) | 024는 20_drafts 불변 번호 — stale 아님 |
| chronicle | `(004)` | `bible 201` | 004→201 narrative_pov_theme_naming |
| chronicle | `(011)` | 구현 시 문맥 확정 | "아크(011)" — story/bible arc 문서, renames로 확정 |

재번호 매핑은 재번호 커밋(`df573ab`)의 rename 기록으로 대조한다. `(011)`처럼
문맥 없이 모호한 것은 추측하지 않고 구현 단계에서 rename 기록 + 노드 문맥으로
확정한다(불확실하면 사용자에게 확인).

### 4. 배선

- `Makefile`의 `research-audit` 타깃에 가드 추가.
- pre-commit 훅에 추가(레포의 다른 문서 게이트와 나란히).

## 테스트 계획

`tests/test_web_data_provenance.py` (pytest, 레포 관례):

1. 현행 수정본에서 가드 통과(exit 0).
2. 합성 stale 토큰(`world 999`)에서 실패(exit 2), 위반 위치 보고.
3. bare 번호/연도(`(2008)`, bare `(039)`)는 무시(오탐 없음).
4. 불변 토큰(`draft 024`, `prototype 018`)은 존재하면 통과.
5. 진실 맵이 실제 선반 파일명에서 구성됨(선반별 번호 파싱 단위 테스트).

## 비목표(Non-goals)

- bespoke 산문·`links` 그래프의 재생성(불가 — 문서에 없음).
- 데이터를 YAML/JSON SSOT로 이관하는 리팩터(별건, 여기선 안 함).
- 코퍼스 의미 검색 / RAG / PageIndex 파이프라인(별건).
- bare `(NNN)` 자동 해석(모호 — 한정 토큰만 검사).

## Boundary

```text
fiction/provenance only
research evidence: no
external source claim: no
```
