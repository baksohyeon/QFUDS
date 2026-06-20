---
doc_id: fiction_creative_writing_craft_harness_ko
title: 창작 문예 하네스
doc_type: guide
stage: reference
status: draft
evidence_role: reference
depends_on:
  - fiction_ip_management_system_ko
  - fiction_gsd_harness_operator_guide_ko
  - wiki_fiction_index
next_gate: apply this checklist before creating a new work bible or prose draft
last_updated: 2026-06-20
---

# 창작 문예 하네스

## 목적

이 문서는 fiction 작업을 "설정표 작성"에서 "소설 쓰기"로 올리기 위한
craft 체크리스트다.

기준은 단순하다.

- 영어권 창작 용어를 기준으로 삼되, 한국어 독자가 읽을 수 있게 바로 풀이한다.
- 약어와 업계 용어는 처음 나올 때 해설한다.
- 설정, 과학, 세계관보다 인물의 욕망, 선택, 장면, 갈등을 먼저 본다.
- 소설 본문을 쓰기 전에 어떤 문학적 장치를 쓰는지 기록한다.
- active SAGA prose는 한국어 본문을 먼저 쓰고, 영어판은 영미권 독자용 독립
  각색판으로 뒤따르게 한다.

## Workflow Boundary

This document uses external craft references as writing-background sources.

Research-source handling follows
[Research Asset and Product Workflow](../../../../.agent/workflows/research-asset-product-workflow.md).

Current workflow state:

```text
hit_not_cached
```

## 바로 쓰는 용어 해설

| Term | 한국어 풀이 | 쓰는 이유 |
| --- | --- | --- |
| `TBD` | 아직 정하지 않음. `To Be Determined`의 약자 | 템플릿의 빈칸 표시 |
| `POV` | 시점. `Point of View`의 약자 | 누가 보고 말하는지 정함 |
| `focalizer` | 초점 인물/초점 주체 | 누가 "보는가"를 말함 |
| `narrator` | 화자 | 누가 "말하는가"를 말함 |
| `canon` | 정사 | 작품 세계에서 확정된 설정 |
| `soft-canon` | 준정사 | 아직 바뀔 수 있지만 임시로 따르는 설정 |
| `elseworld` | 별도 분기/평행 설정 | 본편 canon과 충돌해도 되는 실험작 |
| `prototype` | 원형/실험 초안 | 나중에 버리거나 고칠 수 있는 초기 형태 |
| `retired` | 폐기/보관 | active가 아니지만 기록으로 남기는 설정 |
| `bible` | 작품 설정 기준서 | 인물, 세계관, 시점, 용어를 맞추는 내부 문서 |
| `beat` | 장면 안의 작은 전환점 | 감정, 정보, 권력관계가 바뀌는 순간 |
| `arc` | 변화 곡선 | 인물, 관계, 사건이 시간에 따라 변하는 흐름 |
| `scene` | 장면 | 인물이 목표를 가지고 부딪히는 구체적 단위 |
| `summary` | 요약 서술 | 장면으로 보여주지 않고 압축해서 넘기는 서술 |
| `subtext` | 속뜻 | 대사 표면 아래의 진짜 욕망이나 압력 |
| `motif` | 반복 이미지/관념 | 작품 안에서 의미를 쌓는 반복 요소 |

템플릿에는 가능하면 `TBD`만 남기지 말고 `TBD: 아직 정하지 않음`처럼 쓴다.

## Bilingual Prose Gate

SAGA 본문 작성 순서는 다음을 기본값으로 둔다.

```text
한국어 primary draft -> English Anglophone adaptation -> continuity check
```

점검 기준:

| 항목 | 통과 기준 |
| --- | --- |
| 한국어 본문 | 직역투가 아니라 한국어 소설로 읽힌다 |
| 영어 각색판 | 한국어판의 문장 순서를 따라 베끼지 않고 영미권 독자 리듬으로 재구성한다 |
| 공유 사건 | plot event, field mark, 인물 선택, boundary가 양쪽에서 어긋나지 않는다 |
| 기술어 | `hash`, `key`, `Bitcoin`, `QFUDS` 같은 기술/고유 용어는 필요하면 원어를 보존한다 |
| 독자 경로 | README/read order는 한국어판을 먼저, 영어 counterpart를 다음에 둔다 |

## 문예창작 기본 축

| 축 | 질문 | 실패 신호 |
| --- | --- | --- |
| Premise / 전제 | 한 문장으로 무슨 이야기인가? | 설정 설명은 많은데 사건이 없다 |
| Character / 인물 | 누가 무엇을 원하고 무엇을 두려워하는가? | 인물이 세계관 설명 도구다 |
| Conflict / 갈등 | 무엇이 욕망을 막는가? | 모두가 설명만 하고 충돌하지 않는다 |
| Stakes / 판돈 | 실패하면 무엇을 잃는가? | 사건이 커도 인물에게 의미가 없다 |
| Plot / 플롯 | 원인과 결과가 이어지는가? | 사건이 나열된다 |
| Structure / 구조 | 시작, 중간 전환, 끝의 압력이 있는가? | 어디서 읽어야 할지 모르겠다 |
| Scene / 장면 | 지금 이 장면에서 바뀌는 것은 무엇인가? | 대사와 설명이 돌고 끝난다 |
| POV / 시점 | 누가 보고, 누가 말하고, 무엇을 모르는가? | 카메라가 근거 없이 이동한다 |
| Voice / 문체 목소리 | 이 문장은 누가 쓴 것처럼 들리는가? | 모든 인물과 문서가 같은 말투다 |
| Dialogue / 대사 | 대사가 정보 전달 말고도 일을 하는가? | 모든 대사가 설정 설명이다 |
| Setting / 배경 | 장소와 제도가 인물 선택을 바꾸는가? | 배경이 장식이다 |
| Worldbuilding / 세계관 | 생활, 권력, 비용, 제약이 있는가? | 멋진 명칭만 있다 |
| Theme / 주제 | 독자가 어떤 질문을 들고 나가는가? | 결론을 설교한다 |
| Motif / 반복 장치 | 반복되는 이미지가 의미를 쌓는가? | 상징이 한 번 나오고 사라진다 |
| Pacing / 속도 | 장면, 요약, 침묵의 비율이 맞는가? | 계속 설명하거나 계속 폭발한다 |
| Revision / 퇴고 | 무엇을 자르고, 무엇을 더 선명하게 할 것인가? | 초안이 곧 완성본 취급된다 |

## 장면 작성 최소 조건

장면은 다음을 가져야 한다.

| 항목 | 질문 |
| --- | --- |
| Scene purpose | 이 장면이 작품에서 하는 일은 무엇인가? |
| Character want | 장면 안에서 인물이 원하는 것은 무엇인가? |
| Obstacle | 무엇이 그 욕망을 막는가? |
| Pressure | 왜 지금 해야 하는가? |
| Turn | 장면 끝에서 무엇이 바뀌는가? |
| Cost | 바뀐 대가가 무엇인가? |
| Reveal | 새 정보가 있다면 누가 알게 되는가? |
| Cut line | 어디서 장면을 끝내야 긴장이 남는가? |

장면이 이 표를 못 채우면 아직 본문으로 쓰지 않는다. 먼저 design note로 둔다.

## 인물 설계 최소 조건

인물은 설정값보다 압력이 중요하다.

| 항목 | 질문 |
| --- | --- |
| Want | 겉으로 원하는 것 |
| Need | 사실 필요한 것 |
| Fear | 잃기 싫은 것 |
| Wound | 과거의 손상 |
| Lie | 스스로 믿는 잘못된 문장 |
| Choice under pressure | 압박을 받으면 어떤 선택을 하는가 |
| Contradiction | 말과 행동이 어긋나는 지점 |
| Relationship function | 다른 인물을 어떻게 바꾸는가 |

## 시점과 서술 형식

`1인칭`과 `3인칭`은 출발점일 뿐이다. work bible에는 아래를 기록한다.

| 항목 | 설명 |
| --- | --- |
| Who speaks | 누가 말하는가. 예: 화자, 기록관, 회고록 작성자 |
| Who sees | 누구의 인식으로 보는가. 예: Mara, 법정 기록, archive |
| Telling time | 사건과 서술 시점의 거리 |
| Form | 역사록, 회고록, 수필, 재판 기록, 편지, 직접 장면 |
| Implied audience | 누구에게 말하는가 |
| Motive | 왜 지금 말하는가 |
| Knowledge limit | 무엇을 모르는가 |
| Distortion risk | 무엇을 숨기거나 왜곡할 수 있는가 |

이 구분은 중요하다. 같은 사건도 "재판 기록"이면 증거와 절차가 중심이고,
"회고록"이면 기억과 자기변명이 중심이다.

## 세계관 설계 최소 조건

세계관은 명칭보다 작동 방식이 중요하다.

| 항목 | 질문 |
| --- | --- |
| Resource | 무엇이 부족한가? |
| Cost | 원하는 것을 얻으려면 무엇을 지불해야 하는가? |
| Institution | 누가 규칙을 집행하는가? |
| Law / taboo | 무엇이 금지되어 있는가? |
| Technology limit | 기술이 못 하는 것은 무엇인가? |
| Social class | 누가 혜택을 받고 누가 밀려나는가? |
| Ritual | 사람들이 제도를 어떻게 생활로 받아들이는가? |
| Failure mode | 시스템이 무너지면 어떤 일이 생기는가? |

## SF 기술어 사용 규칙

과학자가 쓴 SF처럼 보이려면 기술어를 지워서는 안 된다.

예를 들어 `hash`, `KDF`, `key`, `salt`, `collision`은 먼저 정확한 기술어로
둔다. 작중 사회가 이를 법이나 의례로 바꾸어 부른다면, 별칭은 아래 표를
채운 뒤에만 쓴다.

| Original term | Fictional alias | Rationale | Loss risk | Accurate anchor | Scene purpose |
| --- | --- | --- | --- | --- | --- |
| `hash` | TBD: 아직 정하지 않음 | TBD: 아직 정하지 않음 | TBD: 아직 정하지 않음 | TBD: 아직 정하지 않음 | TBD: 아직 정하지 않음 |

## Source Notes

| Source | Used for | Workflow state |
| --- | --- | --- |
| [Oregon State, "What is a Frame Story?"](https://liberalarts.oregonstate.edu/wlf/what-frame-story) | frame narrative questions: why told, audience, relation between frame and inner story | `hit_not_cached` |
| [Focalisation overview](https://en.wikipedia.org/wiki/Focalisation) | separating who speaks from who sees | `hit_not_cached` |
| [Narration overview](https://en.wikipedia.org/wiki/Narration) | narrator, point of view, tense, unreliable narration | `hit_not_cached` |
| [Creative writing overview](https://en.wikipedia.org/wiki/Creative_writing) | common craft categories: character, conflict, dialogue, genre, narration, pace, plot, scene, setting, style, theme, voice | `hit_not_cached` |
| [Narrative overview](https://en.wikipedia.org/wiki/Narrative) | character, conflict, plot, setting, theme as narrative elements | `hit_not_cached` |
| [Dialogue in writing overview](https://en.wikipedia.org/wiki/Dialogue_in_writing) | dialogue as character presentation and scene work | `hit_not_cached` |
