---
doc_id: qfuds_saga_external_ai_writing_systems_gap_audit_ko
title: QFUDS SAGA 외부 AI 글쓰기 시스템 갭 감사
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_series_production_harness_ko
  - qfuds_saga_creative_inputs_traceability_ko
  - agentic_fiction_harness_perspectives_ko
  - qfuds_saga_five_core_dramatic_questions_spine_ko
next_gate: convert selected gaps into local production board, chapter intent card, and review-wave templates
last_updated: 2026-06-30
---

# QFUDS SAGA 외부 AI 글쓰기 시스템 갭 감사

## 역할

이 문서는 외부 AI 소설·웹소설·MCP·Claude Skills 레포의 README를 훑고, QFUDS SAGA
하네스에 무엇을 가져올지 정리한 작업실 감사다. 결론은 간단하다.

```text
외부 앱을 설치하는 문제가 아니다.
QFUDS에는 이미 강한 서랍·게이트·캐논 체계가 있다.
부족한 것은 실행 상태판, 역할 라우팅, 스캔 루프, 지식 회수의 반복 집행층이다.
```

## Boundary

- fiction/provenance only. QFUDS 연구 증거가 아니다.
- 외부 레포를 설치하거나 신뢰하지 않는다.
- 외부 README의 구조 패턴만 요약한다. 코드, 프롬프트, 문구를 복제하지 않는다.
- 외부 프로젝트의 품질, 보안, 라이선스 적합성을 보증하지 않는다.
- 설치·연동은 별도 보안 검토 전 금지한다.
- **갱신(2026-06-30):** adoption 규칙 해제 후 story-skills(MIT)는 검토를 거쳐
  채택했다(아래 "story-skills 채택" 절). 위 비설치 원칙은 그 외 미채택 레포에만 유지한다.

Research Asset and Product Workflow:

```text
workflow: Research Asset and Product Workflow
source type: GitHub repositories / README pages
state: hit_not_cached
extraction potential: code_reproduction_possible for app/server repositories; not_extractable for README-only architecture summaries
local cache: none
claim boundary: architecture inspiration only, no product availability or installation claim
```

Inspected source set:

| Source | URL | Local state |
| --- | --- | --- |
| AI Novel Writing Assistant | https://github.com/ExplosiveCoderflome/AI-Novel-Writing-Assistant | `hit_not_cached` |
| InkOS | https://github.com/Narcooo/inkos | `hit_not_cached` |
| Creative Writing Skills | https://github.com/haowjy/creative-writing-skills | `hit_not_cached` |
| fiction-forge | https://github.com/geobond13/fiction-forge | `hit_not_cached` |
| Novel-OS | https://github.com/forsonny/book-os | `hit_not_cached` |
| Vela | https://github.com/heider-x/vela | `hit_not_cached` |
| Knowrite | https://github.com/knoai/knowrite | `hit_not_cached` |
| SillyTavern / KoboldCPP / textgen family | https://github.com/SillyTavern/SillyTavern, https://github.com/LostRuins/koboldcpp, https://github.com/oobabooga/textgen | `hit_not_cached` |

## 현재 QFUDS 하네스가 이미 가진 것

| 층 | 현재 QFUDS 위치 | 이미 충분한가 |
| --- | --- | --- |
| IP 라우팅 | [fiction-ip-management-workflow](../../../../../../../../.agent/workflows/fiction-ip-management-workflow.md) | 충분 |
| 작업실 운영 | `00_workroom/001`, `005`, `007` | 부분 충분 |
| 작가 입력 추적 | `00_workroom/006` | 충분 |
| 세계·인물·기술 canon | `00_bible/` | 충분 |
| 아크·비트·질문 설계 | `10_story_design/011`, `015` | 충분 |
| 원고 SSOT | `20_drafts/` | 충분 |
| release gate | `30_revisions/`, `40_release/`, `scripts/fiction_gate.py` | 충분 |
| 문체·기술 grounding | `00_studio/004`, `006`, bible `009`, workroom `007` | 부분 충분 |

부족한 것은 새 서랍이 아니다. 이미 서랍은 많다. 부족한 것은 **매 장면·매 장·매 턴이
현재 어느 상태인지, 어떤 실패를 다음 실행에 다시 넣는지**를 눈에 보이게 하는 층이다.

## 외부 시스템별 패턴 감사

### 1. AI Novel Writing Assistant

README상 핵심 패턴은 장편을 단락 생성이 아니라 **자동 감독식 장편 생산 흐름**으로
본다는 점이다. 눈에 띄는 구성은 Creative Hub, Agent Runtime, 자동 감독, 본서 세계
컨텍스트, 장편 생산 주 체인, 작성법 엔진, 상태 카드, 승인 노드, 중단 복구다.

QFUDS 대응:

| 외부 패턴 | QFUDS에 이미 있는 것 | 부족한 것 | 결정 |
| --- | --- | --- | --- |
| Creative Hub | workroom + story_design + drafts | 한눈에 보는 현재 실행 상태 | 채택 |
| Agent Runtime | Codex/Claude + workflows | 역할별 입출력 계약 | 채택 |
| approval node | 사용자 release 확인, GSD brief | 장/비트 단위 승인점 | 부분 채택 |
| status card / resume | 없음에 가까움 | 실패 원인, 다음 제안, 재개점 | 채택 |
| writing engine | craft harness, Korean style hook | 작품별 style packet과 적용 여부 | 부분 채택 |

채택 요약:

```text
QFUDS에는 자동 생성 엔진이 필요하지 않다.
대신 "현재 단계 / 실패 이유 / 다음 행동 / 사용자 승인 필요 여부"를 가진 production board가 필요하다.
```

### 2. InkOS

InkOS는 소설, 극본, 인터랙티브 게임, IP 콘텐츠를 같은 이야기 창작 시스템에서 다루는
방향이다. Studio, TUI, CLI, 설정, 역할, 기억, 심사, 수정, 표지, 인터랙티브 상태를
공유 자산으로 본다.

QFUDS 대응:

| 외부 패턴 | QFUDS 대응 | 결정 |
| --- | --- | --- |
| 여러 형식의 IP 제작 | fiction IP workflow와 qfuds-saga 폴더 구조 | 이미 충분 |
| shared memory | bible, traceability, continuity docs | 충분하나 실행 후 회수 필요 |
| review / revision 분리 | `30_revisions/` | 충분 |
| Studio/TUI/CLI | Codex/Claude 작업실 | 앱 도입 보류 |

채택 요약:

```text
InkOS식 통합 앱은 도입하지 않는다.
다만 "같은 IP가 prose, outline, bible, review를 오가도 하나의 상태를 공유한다"는 운영 원칙은 유지한다.
```

### 3. Creative Writing Skills

이 레포는 Claude Skills와 agents를 창작 공정에 맞춰 나눈다. README상 핵심 역할은
muse, writer, revision-writer, bridge-writer, critic, reader-sim, character-sim,
continuity-checker, brainstormer, outliner, style-creator, chronicler다.

QFUDS 대응:

| 외부 역할 | QFUDS 현재 대응 | 부족한 것 | 결정 |
| --- | --- | --- | --- |
| critic | release gate, naturalness/audit 에이전트 | 장면별 적대 리뷰 체크리스트 | 채택 |
| reader-sim | retention gate | 독자 경험 moment report 포맷 | 채택 |
| continuity-checker | bible + continuity template | 장별 자동 회수 프로토콜 | 채택 |
| style-creator | Korean style hook, craft harness | QFUDS prose style packet | 채택 |
| chronicler | traceability, bible 수동 갱신 | draft 후 canon delta 회수 | 강하게 채택 |
| character-sim | character bible | 장면 전 대사 압력 테스트 | 선택 채택 |

채택 요약:

```text
QFUDS에는 "더 많은 작가 에이전트"보다 "각 작업에 어떤 모자를 쓰는지"가 필요하다.
하나의 에이전트라도 writer / critic / chronicler / reader-sim 모드를 분리해 실행한다.
```

### 4. fiction-forge

이 레포는 AI-assisted novel editing toolkit으로 prose scanner, MCP context server,
publisher, editorial workflow를 묶는다. README상 특히 중요한 것은 스캔 -> 비중 있는
문제 장 식별 -> 비중첩 파일 병렬 수정 -> 재스캔 -> 순차 보이스 polish 흐름이다.

QFUDS 대응:

| 외부 패턴 | QFUDS 현재 대응 | 부족한 것 | 결정 |
| --- | --- | --- | --- |
| prose scanner | `fiction_gate.py`, craft audit | severity tier와 cluster report | 채택 |
| MCP context server | repo 파일 직접 읽기 | 별도 서버는 불필요 | 설치 보류 |
| fix in waves | 없음 | 겹치지 않는 파일 묶음 수정 규칙 | 채택 |
| re-scan | pre-commit + manual review | 수정 후 재검증 체크리스트 | 채택 |
| publisher | `40_release/` | 지금은 불필요 | 보류 |

채택 요약:

```text
MCP 서버 설치보다 "scan -> fix wave -> re-scan -> polish" 루프를 문서화하는 편이 안전하다.
```

### 5. Novel-OS

Novel-OS는 Standards, Novel, Manuscripts의 세 층으로 컨텍스트를 나눈다. Claude Code,
Cursor, 일반 AI 도구에서 쓸 수 있는 구조적 workflow에 가깝다.

QFUDS 대응:

| Novel-OS 층 | QFUDS 대응 | 결정 |
| --- | --- | --- |
| Standards | `00_studio/`, `.agent/workflows/`, `.agent/templates/fiction/` | 이미 충분 |
| Novel | `qfuds-saga/00_bible`, `10_story_design` | 충분 |
| Manuscripts | `20_drafts`, `30_revisions`, `40_release` | 충분 |

채택 요약:

```text
Novel-OS의 큰 구조는 이미 QFUDS에 있다.
가져올 것은 "각 층의 lite context packet"이다.
```

### 6. Vela

Vela는 local-first/BYOK/RAG 기반의 AI novel writing IDE다. 대강의 장점은 편집기,
AI 패널, 대纲/장 생성, 자동 리뷰, 로컬 지식베이스다.

QFUDS 결정:

```text
별도 IDE는 도입하지 않는다.
QFUDS는 Git repo가 이미 원본 편집기이므로, 앱형 도구를 들이면 source of truth가 갈라진다.
RAG와 local-first 원칙만 참고한다.
```

### 7. Knowrite

Knowrite는 multi-agent backend에 가깝다. README상 Writer, Editor, Humanizer,
Proofreader, Reader, Summarizer 같은 chapter pipeline, Fitness 평가, RAG memory,
Temporal Truth Database, Author Fingerprint, Prompt evolution, MCP endpoint를 가진다.

QFUDS 대응:

| 외부 패턴 | QFUDS에서 필요한 축소판 |
| --- | --- |
| Temporal Truth Database | 장별 truth-state ledger |
| Author Fingerprint | QFUDS prose style packet |
| Fitness assessment | release gate 점수표가 아니라 fail/pass 사유표 |
| Prompt evolution | 작업 후 프롬프트 교정 postmortem |
| RAG retrieval | repo 파일 직접 참조 + context packet |
| MCP endpoint | 지금은 불필요 |

채택 요약:

```text
Knowrite는 너무 무겁다.
하지만 truth-state ledger와 chapter intent card는 QFUDS에 바로 필요하다.
```

### 8. 유명 로컬 LLM / RP 도구군

SillyTavern, KoboldCPP, textgen 계열은 유명하지만 QFUDS에 바로 필요한 유형은 아니다.
이들은 모델 실행, 캐릭터 대화, 로컬 추론, RP UI에 강하다.

QFUDS 결정:

```text
설치 보류.
QFUDS의 병목은 모델 실행 환경이 아니라 구조-연속성-장면 압력의 집행이다.
```

## QFUDS에 실제로 부족한 6개 모듈

### A. SAGA Production Board

장편 전체가 지금 어디 있는지 보여 주는 단일 상태판.

| 필드 | 의미 |
| --- | --- |
| active unit | 지금 작업 중인 부/장/문서 |
| phase | plan / outline / draft / critique / revise / verify / release |
| owner mode | writer / critic / chronicler / reader-sim / continuity |
| status | blocked / in_progress / needs_user / ready_next |
| failure reason | 막힌 이유 |
| next action | 다음 한 동작 |
| source files | 입력 문서 |
| output files | 생성·수정 문서 |
| approval needed | 사용자 확인 필요 여부 |

### B. Chapter Intent Card

장 또는 큰 장면을 쓰기 전의 최소 계약.

| 필드 | 의미 |
| --- | --- |
| desire | 이 장면에서 누가 무엇을 원하는가 |
| threat | 몇 분/몇 시간/며칠 안에 무엇이 끝장나는가 |
| choice | 선택지는 무엇인가 |
| cost | 선택마다 잃는 것은 무엇인가 |
| 015 question | 5대 질문 중 무엇을 심거나 터뜨리나 |
| reveal budget | 보여줄 것 / 숨길 것 / 설명 금지 |
| handoff | 다음 장면으로 넘길 압력 |

### C. Chronicler Pass

원고를 쓴 뒤 반드시 회수하는 정리 단계.

| 회수 항목 | 목적 |
| --- | --- |
| new canon facts | bible 승격 후보 |
| changed character state | 인물 관계·상처·욕망 변화 |
| opened hooks | 떡밥 원장 추가 |
| closed hooks | 회수 처리 |
| technical terms introduced | glossary/bible 갱신 후보 |
| continuity risks | 다음 작업 전 차단 항목 |

### D. Review Wave Protocol

수정 작업을 한 번에 전부 고치지 않고 파동으로 나눈다.

```text
foundation scan -> high-severity fix -> re-scan -> continuity fix -> voice polish -> release gate
```

규칙:

- 같은 파일을 여러 에이전트가 동시에 고치지 않는다.
- high-severity issue를 고치기 전 문장 polish를 하지 않는다.
- re-scan 없이 release로 가지 않는다.

### E. QFUDS Style Packet

소설 작성 시 매번 전체 문체 규칙을 읽지 않기 위한 짧은 context packet.

필수 항목:

- 한국어 primary, 번역투 금지.
- 기술어는 숨기지 말고 장면 안에서 쉬운 손잡이를 준다.
- 개념보다 사람의 선택, 손, 서명, 비준, 침묵을 우선한다.
- 대화는 인물별 이해관계와 상처가 달라야 한다.
- AI 티, 장식적 거대 문장, premature emotional resolution 금지.

### F. Truth-State Ledger

데이터베이스가 아니라 장별 표면 충분하다.

| 장 | 인물이 아는 것 | 독자가 아는 것 | 세계가 확정한 것 | 열린 모순 |
| --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | TBD |

## 채택 결정

| 항목 | 결정 |
| --- | --- |
| AI Novel Writing Assistant 설치 | 보류 |
| InkOS 설치 | 보류 |
| Creative Writing Skills 설치 | 보류, 역할 분리만 채택 |
| fiction-forge MCP 설치 | 보류, scanner workflow만 채택 |
| Novel-OS 설치 | 보류, 3층 context packet만 채택 |
| Vela 설치 | 보류 |
| Knowrite 설치 | 보류, truth-state/chapter intent만 채택 |
| QFUDS local templates | 채택 |

## 다음 구현 순서

1. `00_workroom/009_saga_production_board_ko.md`를 만든다.
2. `00_workroom/010_chapter_intent_card_template_ko.md`를 만든다.
3. `00_workroom/005_series_production_harness_ko.md`에 Chronicler Pass와 Review Wave를 연결한다.
4. `30_revisions` 쪽 release gate에 re-scan requirement를 명시한다.
5. 필요할 때만 `fiction-forge` 스타일 prose scanner를 별도 스크립트로 흉내 낸다. 외부 MCP 서버 설치는 마지막이다.

## 현 판단

현재 QFUDS 하네스는 레퍼런스가 부족해서 약한 것이 아니다. 오히려 일반적인 AI 소설
도구보다 서랍과 경계가 강하다. 약점은 다음이다.

```text
좋은 규칙이 많지만, 매 실행마다 어떤 규칙이 적용됐고 무엇이 실패했는지 한 장에 남지 않는다.
```

그래서 보강 방향은 앱 도입이 아니라 **작업 상태판 + 장면 의도 카드 + 회수 패스**다.
이 세 가지가 들어가면 외부 도구들이 자랑하는 장편 생산 안정성의 핵심만 QFUDS 방식으로
흡수할 수 있다.

## story-skills 채택 (2026-06-30, adoption 규칙 해제 후)

위 "보류" 판단은 inspiration-only 시절 결론이다. 2026-06-30 외부 도구 adoption 규칙이
픽션 한정 해제되어(IP 워크플로우 External Tool and Code Adoption), 비교 평가 후
**story-skills를 결정론적 연속성 엔진 용도로 채택**한다.

비교 결과(후보 4종, 전부 MIT): story-skills / howells-fiction / Claude-Book / Crucible.
선정 사유 — Claude Code 플러그인 + 마크다운/YAML 철학 일치 + **결정론적 continuity CLI**
(deaths·promises·questions·casts·durable state) + 의존성 0. Claude-Book은 GPU·로컬 LLM
인프라 과중, Crucible은 데스크톱 앱이라 탈락.

채택 기록(adoption 규칙 필수 항목):

| 항목 | 값 |
| --- | --- |
| source | https://github.com/danjdewhurst/story-skills |
| license | MIT |
| 고정 commit | `c482d48f4eb9b488f033a77a51f9fae55cc0d75f` |
| 도입 방식 | git submodule `tools/story-skills/` (프로젝트 동행, 업데이트 가능) |
| allowed claim | 픽션 연속성 QA 도구로 사용; CLI를 원고에 실행 |
| blocked claim | QFUDS 연구 증거·이론·결과에 반입 금지; 픽션 전제를 연구 주장화 금지 |
| workflow state | `asset_cached` (submodule로 고정) |
| boundary | fiction/provenance only |

사용법(원고 연속성 QA):

```bash
node tools/story-skills/bin/story.js import <draft.md> --title <T> --dir /tmp/<T>
node tools/story-skills/bin/story.js continuity /tmp/<T>
node tools/story-skills/bin/story.js report /tmp/<T>
```

한계(정직): `import`는 챕터 heading 규칙이 달라 긴 원고를 일부만 분할하고, 엔진의
완전한 값을 내려면 인물(death/status)·promise·question·scene cast를 채워야 한다. 즉
"import하면 즉시 검사 완료"가 아니라 **work별 1회 셋업 후 결정론적 검사가 공짜**가 된다.

역할 분담:

- **story-skills CLI** = 범용 연속성(죽은 인물·복선 회수 순서·안 쏜 떡밥·장면 캐스트·상태).
- **`scripts/fiction_continuity.py`** = QFUDS 전용 딥타임 시대(부) 정합 — story-skills가
  모르는 1부(21c)↔2부(4기) 규칙 전담. 두 도구는 보완 관계로 둘 다 유지한다.

story-skills의 7개 writing 스킬은 자체 폴더 구조(characters/·plot/)에 묶여 QFUDS
거버넌스(00_bible/20_drafts)와 충돌하므로 `.claude/skills`로 자동 로드하지 않는다.
submodule 안에 참고용으로 둔다.
