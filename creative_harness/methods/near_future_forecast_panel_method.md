---
doc_id: fiction_near_future_forecast_panel_method_ko
title: 근미래 SF 전망 패널 방법
doc_type: guide
stage: reference
status: completed
evidence_role: reference
depends_on:
  - fiction_creative_writing_craft_harness_ko
next_gate: use the method on a work-local question and record sources, scenarios, and story consequences
last_updated: 2026-07-11
---

# 근미래 SF 전망 패널 방법

## 목적

근미래 SF의 기술·노동·정치·생활 변화를 한 가지 예언으로 고정하지 않고, 여러
전문 관점과 불확실성 분기로 검토한다. 산출물은 작품 후보이며 현실 예측, 투자 조언,
연구 증거가 아니다.

## 입력

- work id와 target reader
- 기준 연도와 전망 기간
- 사변적 변화 하나
- plot-critical 질문
- 이미 채택한 world constraints
- 만들 수 있는 것과 만들면 안 되는 것

## 렌즈 선택

질문에 필요한 렌즈만 고른다.

- 기술 역량과 물리적 병목
- 노동, 계급, 돌봄
- 경제, 자원, 에너지
- 법, 제도, 거버넌스
- 국제관계와 안보
- 인구, 이주, 가족
- 정보, 미디어, 기록
- 생태와 기후
- 종교, 의례, 의미
- 언어, 교육, 일상

렌즈 수를 늘리는 것이 목표가 아니다. 같은 원인을 다른 관점에서 압박해 빠진
2차 효과를 찾는 것이 목표다.

## 시나리오 규율

최소 세 분기를 만든다.

| Branch | 질문 |
| --- | --- |
| constrained | 기술·제도가 예상보다 느리거나 제한적이면 무엇이 남는가 |
| broad adoption | 성능과 비용이 충분히 개선되면 무엇이 재분류되는가 |
| backlash / rollback | 법, 문화, 사고, 전쟁, 자원 때문에 되돌리면 무엇이 보존되는가 |

각 분기는 다음을 반환한다.

```text
time window
-> enabling event
-> causal mechanism
-> winners / losers
-> daily-life change
-> institutional response
-> contradiction or failure mode
-> scene pressure
```

## 멀티에이전트 사용

사용자가 병렬 조사를 승인했을 때만 렌즈별 에이전트를 쓴다.

1. Master가 질문, 기간, 출처 기준, 금지 주장을 고정한다.
2. Research agents는 서로 겹치지 않는 렌즈와 1차 출처를 맡는다.
3. Synthesis agent는 합의보다 인과 충돌과 불확실성을 먼저 찾는다.
4. Story architect는 현실 전망을 인물의 비용, 선택, 장면으로 번역한다.
5. Continuity agent는 기존 world constraints와 충돌을 분류한다.

에이전트 합의는 canon이 아니다. 새 이름, 기관, 사건은 candidate이며 사용자가
promote하기 전에는 world authority에 들어가지 않는다.

## Source Boundary

현실 앵커마다 Fiction Source Intake Workflow를 적용한다. 같은 자료를 QFUDS 연구
주장에 쓸 때만 별도 Research Asset and Product Workflow를 실행한다.

- URL, 발표 주체, 날짜, asset state
- allowed claim과 blocked claim
- 직접 관측, 기관 전망, 작가의 외삽을 구분
- 서로 다른 시점의 수치를 한 현재 상태처럼 합치지 않음
- `없다`는 주장은 실제 asset inspection 뒤에만 사용

## Output

| Item | Required content |
| --- | --- |
| Source ledger | URL, state, allowed/blocked claim |
| Scenario table | constrained / broad adoption / rollback |
| Cross-pressure map | 한 변화가 다른 영역에 만든 2차 효과 |
| Story consequences | 인물, 일상, 제도, 비용, 선택 |
| Candidate ledger | new names/events/rules and promotion blockers |
| Unknowns | 현실 조사와 작가 결정이 더 필요한 지점 |

설정 목록만 만들지 않는다. 사변 요소를 제거하면 사라지는 장면과 선택이 최소 하나
있어야 한다.
