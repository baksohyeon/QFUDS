---
doc_id: qfuds_saga_agentic_system_ko
title: QFUDS SAGA 창작 시스템
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_index_ko
  - qfuds_agentic_research_system_ko
  - qfuds_fiction_saga_index_ko
next_gate: user-confirmed world-direction matrix before story drafting
last_updated: 2026-06-19
---

# QFUDS SAGA 창작 시스템

## 목적

이 문서는 QFUDS SAGA를 쓰기 위한 별도 agentic fiction system의 초안이다.

QFUDS 본 연구와 분리한다. 여기서 만드는 세계관, 인물, 장면, 설정은 연구
결과가 아니다. 물리 증거가 아니다. QFUDS support, validation, Level 2B
admission으로 읽지 않는다.

전체 fiction/IP 운영 규칙은
[Fiction IP Management Workflow](../../../../../.agent/workflows/fiction-ip-management-workflow.md)
가 관리한다. 이 문서는 그중 `qfuds-saga` series track의 작가실 운영 규칙이다.

SAGA의 창작 premise는 다음 문장으로 시작한다.

```text
QFUDS는 현실 연구에서는 증명되지 않았다.
하지만 어떤 fiction 층위에서는 QFUDS가 정답인 세계가 존재한다.
```

이 premise는 이야기를 움직이는 장치다. 연구 판정이 아니다.

## Workflow Boundary

This document touches external web references, AI-writing examples, MCPs,
papers, PDFs, and code/tool concepts only as creative-system references.

External-source handling remains governed by
[Research Asset and Product Workflow](../../../../../.agent/workflows/research-asset-product-workflow.md).

Current workflow states:

```text
hit_not_cached
asset_available_not_downloaded
not_extractable
```

No new external asset cache, source bundle, PDF extraction, numerical product,
or QFUDS-ready product is created by this document.

## 기본 구조

소설을 바로 쓰지 않는다. 먼저 writers' room을 만든다.

각 agent는 결과물을 직접 확정하지 않는다. 주요 단계는 사용자 확인을 거친다.

```text
idea -> direction matrix -> user confirmation
     -> series bible / 작품 설정 기준서 -> user confirmation
     -> pilot arc -> user confirmation
     -> episode draft -> user confirmation
     -> revision -> commit
```

## Agent Roles

| Agent | 역할 | 산출물 | 금지 |
| --- | --- | --- | --- |
| `showrunner` | 시즌 구조, 중심 테마, 장기 반전 관리 | season premise, arc map, episode order | 장면을 멋대로 확정하지 않음 |
| `worldbuilder` | 기관, 문화, 금기, 경제, 기술, 역사 설계 | series bible entry, faction sheet, ritual map | 기존 장르 고유 설정을 복제하지 않음 |
| `science_auditor` | QFUDS 연구 경계, known-model 환원, 관측 제약 감시 | science boundary note, forbidden-claim list | fiction premise를 evidence로 승격하지 않음 |
| `plot_architect` | 미션 구조, 반전, 정보 공개 순서 설계 | act outline, reveal schedule, mission brief | 과학적 결론을 plot convenience로 바꾸지 않음 |
| `character_room` | 인물 욕망, 관계, 상처, 말투 관리 | character sheet, relationship graph | 인물을 논문 설명 도구로만 쓰지 않음 |
| `style_editor` | 문장 리듬, 장면성, show/tell 균형 퇴고 | revision memo, prose pass | 기존 문장을 무단 삭제하지 않음 |

## Sub-Agent Operation Rule

위 agent들은 먼저 **역할 분리 규칙**이다. 실제 Codex/Claude Code 세션에서
sub-agent 도구가 제공될 때만 병렬 실행한다.

운영 규칙:

```text
1. 사용자가 sub-agent/병렬 작업을 명시적으로 허용한다.
2. 각 sub-agent에 겹치지 않는 질문이나 파일 범위를 준다.
3. read-only scout와 writer를 분리한다.
4. writer는 단일 main agent가 통합한다.
5. fiction premise를 research evidence로 승격하지 않는다.
6. 결과는 staged guard와 pre-commit으로 검증한다.
```

현재 권장 분리:

| Sub-agent | Use when | Output |
| --- | --- | --- |
| `science_auditor` scout | 과학/출처/증거 경계가 흐려질 때 | forbidden-claim list, workflow-state check |
| `visual_exhibit` scout | 기존 asset을 fiction exhibit로 쓸 때 | asset 후보, caption risk, provenance note |
| `style_editor` scout | 대사가 많고 장면성이 약할 때 | sensory/metaphor pass memo |
| `showrunner` scout | 장면이 장기 arc와 어긋날 때 | arc-fit note, reveal-order risk |

sub-agent가 없으면 위 표는 main agent의 체크리스트로 사용한다. sub-agent가 있어도
최종 문서 수정, stage, commit은 main agent가 책임진다.

## MCP Candidates

| MCP or tool family | Planned use | State | Boundary |
| --- | --- | --- | --- |
| PageIndex / MarkItDown | 연구 PDF, 자료 문서, figure/table reference가 필요할 때 구조화된 읽기 보조 | `asset_available_not_downloaded` | fiction science background 보조만 수행 |
| WordNet / NLTK | 어휘 반복, 의미장, 상징어, 문체 팔레트 점검 | `hit_not_cached` | 자동 동의어 치환기로 쓰지 않음 |
| Saga canon / RAG MCP | 인물, 기관, 사건, 금기, 이전 episode의 일관성 검색 | `not_extractable` | canon check만 수행하고 story decision은 사용자 승인 |
| Scene / revision tool | 장면 초안, show-don't-tell pass, rhythm pass | `not_extractable` | 초안 생성은 가능하지만 최종 문체 확정은 별도 review |
| Git / repository helper | staged diff, narrow commit, index sync 확인 | `not_extractable` | 연구 status 변경 도구가 아님 |

MCP는 별도 창작 보조 시스템이다. 본 연구의 Level, roadmap, admission gate를
바꾸지 않는다.

## Research Basis

영어권 AI-assisted fiction 사례는 네 계열로 참고한다.

| 계열 | 사례 | 창작 시스템에서 얻는 교훈 | Workflow state |
| --- | --- | --- | --- |
| 기계 실험형 | Ross Goodwin, *1 the Road*; [Columbia DSL](https://digitalstorytellinglab.com/breakthroughs/1-the-road) | 기계가 세계를 잘못 읽는 방식도 작품 장치가 될 수 있음 | `hit_not_cached` |
| 인간-AI 공동저작형 | Stephen Marche, *Death of an Author*; [The Creative Penn](https://www.thecreativepenn.com/2023/05/12/intentionality-beauty-and-authorship-co-writing-with-ai-with-stephen-marche/) | AI는 초안, 변주, 문장 생성 장치이고 구조 선택은 인간이 맡음 | `hit_not_cached` |
| 기억 반사판형 | Vauhini Vara, "Ghosts"; [The Believer](https://www.thebeliever.net/ghosts/) | AI를 정답기가 아니라 기억과 상실을 비추는 거울로 쓸 수 있음 | `hit_not_cached` |
| 절차적 생성형 | [NaNoGenMo](https://nanogenmo.github.io/) | 소설보다 "소설을 만드는 시스템" 자체가 작품의 일부가 될 수 있음 | `hit_not_cached` |
| multi-agent story generation | [ACL In2Writing 2025](https://aclanthology.org/2025.in2writing-1.9.pdf), [StoryWriter](https://arxiv.org/pdf/2506.16445) | 장기 일관성, 캐릭터 시뮬레이션, 수정 루프를 분리해야 함 | `asset_available_not_downloaded` |

## Major-Step Confirmation Gate

아래 단계는 하나씩 사용자 확인을 받은 뒤 진행한다.

| Step | 확인 질문 | 완료 조건 |
| --- | --- | --- |
| 1. System boundary | 창작 트랙 위치와 연구 분리 경계가 맞는가? | 이 문서와 index가 통과 |
| 2. World direction | 어떤 세계관 프레임을 1차 작품 설정 기준서로 삼을 것인가? | direction matrix에서 하나 또는 hybrid 선택 |
| 3. Series bible | 기관, 문화, 인물, 과학 금기, 정보 공개 순서가 충분한가? | 작품 설정 기준서 초안 승인 |
| 4. Pilot arc | 3-5화 arc가 장편 엔진을 보여 주는가? | pilot outline 승인 |
| 5. Episode draft | 본문을 계속 확장할 만한 톤인가? | draft + revision memo 승인 |

## Science Boundary

SAGA는 과학적으로 유용해야 하지만 과학을 위조하면 안 된다.

- QFUDS가 맞는 세계를 가정할 수 있다.
- 현실 연구에서는 그 가정이 증명되지 않았음을 매번 보존한다.
- `Gamma(a)`는 fiction 안에서 흔적, 신호, 작전명으로 쓸 수 있다.
- 연구 문서에서는 여전히 phenomenological IV/IDE timing comparator다.
- NASA/BAO/LSS/CMB는 fiction 안에서 심판/감시 장치로 쓸 수 있다.
- 연구 문서에서는 baseline constraint source일 뿐이다.

## Next Gate

다음 문서는 세계관 방향 선택 매트릭스다.

그 문서가 해야 할 일은 "학원물로 갈지 말지"가 아니다. 더 넓게, 어떤 장편
구조가 QFUDS의 실패, 회고, audit harness, 정보-물리 상상력을 가장 잘 살리는지
비교하는 것이다.
