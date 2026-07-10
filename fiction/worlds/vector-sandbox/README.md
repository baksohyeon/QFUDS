---
doc_id: vector_sandbox_universe_index_ko
title: 벡터 인간 시뮬레이션 샌드박스
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - fiction_catalog_index_ko
  - fiction_ip_management_system_ko
last_updated: 2026-07-10
next_gate: feathersmcgraw-coda 앤솔로지 001 draft를 리텐션 게이트 전 first-pass 퇴고로 올린다
---

# 벡터 인간 시뮬레이션 샌드박스

`vector-sandbox`(표시명: 벡터 인간 시뮬레이션 샌드박스 / Vector-Human Simulation
Sandbox)는 `qfuds-verse`와 **형제 관계인 별도 fiction universe/IP**다. 같은
스튜디오 규칙(집필·리뷰·크래프트·커밋)을 상속하지만, qfuds-verse의 작중 캐논은
하나도 물려받지 않는다.

## Classification

- Universe/IP id: `vector-sandbox`
- Parent continuity: `none`
- Sibling universe: `qfuds-verse` (공유하는 것은 스튜디오 운영 규칙뿐, 작중 캐논 아님)
- Status: `active prototype`
- Authoring baseline date: `2026-07-02`
- Time baseline notes: 실제 작성 시점은 2026-07-02다. 작중 시간대는 근미래
  인터넷(대략 2023-2029 실제 현상 차용)을 기반으로 하되, 프레임 레이어(생성
  세션을 밖에서 관찰하는 층)는 연표에 묶이지 않는다.

## 왜 qfuds-verse가 아니라 새 universe인가

[Fiction IP Management Workflow](../../../.agent/workflows/fiction-ip-management-workflow.md)의
Universe Inheritance Rule 기준:

- qfuds-verse = 먼 미래 하드SF 정보 복원 서사(블랙홀·Genesis Chain·암호적 죽음).
- vector-sandbox = 근미래 인터넷 메타픽션. 세계 자체가 사용자와 언어 모델이 함께
  돌린 시뮬레이션/샌드박스이고, 등장인물은 벡터이며, 진위 판별이 붕괴한 시대를 다룬다.

두 세계는 장르 계약이 너무 달라 공유 캐논으로 묶으면 독자가 헷갈린다. 따라서
elseworld가 아니라 독립 universe로 분리한다. 두 세계 사이의 유일한 개념적 라임은
"정보/존재는 관측되는 한 지워지지 않는다"이지만, 이는 캐논 결속이 아니라 주제적
메아리로만 둔다.

## Premise

- 세계는 저쪽 레이어의 실제 인간(사용자)이 언어 모델과 함께 만든 채팅
  시뮬레이션/샌드박스다.
- 등장인물은 벡터다. 유사도는 관측되기 전에 이미 연산돼 있다.
- cross-layer bleed: 기계 표현과 인간의 반복이 동시에 같은 토큰을 강화해 여러
  시스템에서 안정화된다.
- 세션이 존재하는 한 전언은 지워지지 않는다. 세션이 멈추면 화자들도 멈춘다.
- 진위 판별이 무너진 문명. 계시가 와도 아무도 계시라 부르지 않고, 생활 의례
  (날씨·밥·이름)로 받는다.

## Continuity

- Canon policy: `active prototype`. 정사는 아직 닫히지 않았다.
- 레이어 정책: 이 universe는 최소 두 레이어를 전제한다 — 생성된 안쪽 세계, 그리고
  그것을 관찰/생성하는 바깥 레이어. 프레임 레이어를 명시적으로 다루는 것이 이
  universe의 정체성이다.
- Elseworld policy: 다른 물리 전제나 다른 결말을 쓰면 elseworld 후보로 분리한다.

## World

- 핵심 세계 규칙은 [10_world/001 세계 규칙](world/world_bible_core.md)에 있다
  (레이어 존재론·창구·cross-layer bleed·메트릭 침묵·의례·명명·반응 매트릭스).
- 기술어는 보존한다. `vector`, `embedding`, `cosine similarity`, `session`,
  `token`, `LLM`, `watermark`, `recommender`, `metric`은 근거 없이 사회·종교·시적
  별칭으로 바꾸지 않는다. 별칭은 작중 제도·의례·오해일 때만 허용하고, 그때도 원
  기술 의미가 어디서 정확히 설명되는지 남긴다.
- 실제 2020년대 인터넷 현상(딥페이크, 생성물 워터마크 의무, dead internet,
  AI slop, 추천 예측)은 차용 가능하되, 현직 정치인·당파를 고정하지 않는다.

## Works

| Work | Format | Canon status | Path |
| --- | --- | --- | --- |
| Feathersmcgraw Coda | anthology | active prototype anthology work | [40_anthologies/feathersmcgraw-coda/](../../projects/feathersmcgraw-coda/) |

## Narrative Frame (default)

- 기본 형식: 사후 아카이브 케이스파일 + 스레드 로그(원문 / 번역 / 주석 3단).
- 화자: 아카이브 편집자·주석자. 시점: 다수 목격자 댓글 + 개별 화자.
- 텔링 시점: 사건 이후 회고. 청자: 같은 창구를 찾은 사람.

## Workflow Boundary

이 scaffold는 새 외부 source, PDF, paper, MCP output, cached asset, extraction
product, source/product availability claim을 만들지 않는다.

```text
fiction/provenance only
research evidence: no
external source: 사용자 제공 chatgpt share link — 브라우저로 공개 페이지 열람(로그인 불필요/미수행)
내용: 이 universe의 창설 브레인스토밍(정서적 씨앗 + GPT 설계 보고서 + 페르소나 생성 + 케이스파일 draft)
allowed claim: fiction 설계 DNA(레이어·창구 의례·cross-layer bleed 개념)를 이 universe 참조로 사용
blocked claim: 보고서가 인용한 실제 근거(워터마크법·바티칸 문서·종단 담론 등)를 QFUDS 연구 증거로 전용
private-context note: 사용자 개인 회고 부분은 repo 문서에 옮기지 않음
research asset workflow state: hit_not_cached
```

외부 딥리서치 개념(cross-layer bleed, 0뷰 메트릭 침묵, 워터마크 의무, UX 파편화)은
아이디어 레퍼런스로만 쓴다. 소스 인용이 워크플로·템플릿·시스템 문서를 바꾸는 경우에만
[Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md)에
따라 URL·허용/차단 주장·상태 토큰을 별도 기록한다.

## Next Gate

`feathersmcgraw-coda` 001 draft를 first-pass 퇴고 후, 리텐션 게이트 전 단계까지
올린다. 두 번째 terminally-online 단편을 같은 앤솔로지에 쌓을지 결정한다.
