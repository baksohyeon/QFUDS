---
doc_id: plan_2026_06_18_three_branch_routing_ko
title: "세 갈래 분기점: 실증, 임의 탐색, 아이디어 계보"
doc_type: guide
stage: reference
status: completed
evidence_role: provenance
depends_on:
  - roadmap
  - safe_future_branch_candidates
  - qfuds_lineage_black_hole_information_public_bridge_ko
next_gate: route future black-hole, foam-scale, and timing work through one of the three branches; do not open Level 2B
last_updated: 2026-06-18
---

# 세 갈래 분기점: 실증, 임의 탐색, 아이디어 계보

## 목적

이 문서는 QFUDS의 출발점을 버리지 않기 위해 만든 분기점 장부다.

출발점은 투박했다. 정보가 사라지지 않는다면, 블랙홀은 정보를 없애는
쓰레기통인지, 우주의 하드디스크인지, 그 흔적이 dark sector 질문과 이어질
수 있는지 묻는 사고 실험이었다.

현재 이 사고 실험은 물리 QFUDS로 admitted되지 않았다. 그래서 다음 작업은
"QFUDS를 살리는 문서"가 아니라, 이 출발점을 세 갈래로 나누어 어디에 무엇을
적을지 고정하는 일이다.

## Status Boundary

이 문서는 새 실험 결과가 아니다.

이 문서는 roadmap status를 바꾸지 않는다.

이 문서는 Physical-QFUDS Level 2B를 열지 않는다.

이 문서는 QFUDS support, validation, survival, admission 언어로 읽으면 안 된다.

현재 상태는 항상 [QFUDS Research Roadmap](000_roadmap.md)이 정한다.

## Workflow Boundary

This guide applies the
[Research Asset and Product Workflow](../../.agent/workflows/research-asset-product-workflow.md)
only to preserve source-state boundaries.

No new external web, PDF, table, product, cache, digitization, or availability
claim is introduced here. Existing source-state tokens remain inherited from the
owning research records, including `asset_cached`,
`asset_extracted_not_digitized`, `hit_not_cached`,
`inspected_no_numerical_product`, `manual_structured_extract`, and
`direct_table`.

NASA/LAMBDA, BAO, LSS, CMB, black-hole literature, and retained timing records
are baseline or provenance sources only. They are not QFUDS evidence in this
document.

## 왜 지금 나누는가

지금 섞이면 위험한 것이 세 가지다.

1. 관측값을 먼저 본 뒤 scale, width, amplitude를 고르고 source라고 부르는 것.
2. 블랙홀 정보 서사를 physical source claim처럼 쓰는 것.
3. retained timing을 QFUDS 물리 기원처럼 되살리는 것.

그래서 이후 작업은 아래 세 갈래 중 하나로 먼저 분류해야 한다.

## 세 갈래

| 분기 | 질문 | 문서 위치 | 허용 출력 | 금지 |
| --- | --- | --- | --- | --- |
| 1. 실증적 분기 | 어떤 관측 문턱에서 먼저 죽는가? | `docs/wiki/research/investigations/` | IV/IDE timing comparator, NASA/BAO/LSS/CMB kill-map, baseline constraint map | 관측값으로 `xi`, transition width, amplitude를 고른 뒤 QFUDS source라고 부르기 |
| 2. 임의 탐색 분기 | 후보를 equation template에 넣으면 빈칸이 어디서 드러나는가? | `docs/05_next_steps/` plan 또는 `docs/wiki/research/investigations/` audit | candidate-equation sheet, missing-object ledger, known-model reduction checklist | 후보 이름만으로 `X`, `Q^nu`, phase-B pressure, `delta Q`를 대체하기 |
| 3. 아이디어 계보 분기 | 이 질문이 왜 생겼고 어떻게 좁혀졌는가? | `docs/wiki/lineage/` | origin narrative, public bridge, genealogy, demotion history | lineage 문서를 roadmap status, result, physical evidence로 쓰기 |

## 1. 실증적 분기

실증적 분기는 "맞는가"보다 "어디서 죽는가"를 묻는다.

여기에 들어갈 수 있는 작업:

- retained timing을 IV/IDE comparator로만 비교한다.
- NASA/LAMBDA, BAO, LSS, CMB 축을 observational kill-map으로 정리한다.
- DESI, eBOSS, Euclid, Roman, Rubin/LSST 같은 관측 문턱을 baseline
  constraint로만 둔다.

이 분기는 물리 QFUDS의 증거가 아니다. 관측 문턱을 먼저 고정하는 장부다.

## 2. 임의 탐색 분기

임의 탐색 분기는 sandbox다. 하지만 아무렇게나 상상하는 곳은 아니다.

여기에 들어갈 수 있는 후보:

- `xi_gal` 또는 galaxy/cosmic-web coarse-graining scale.
- foam-sector state variable 후보.
- black-hole evaporation, remnant, compact-object abundance, information
  storage 같은 source 후보.

이 분기의 첫 문서는 반드시 candidate-equation template 성격이어야 한다. 최소
빈칸은 다음과 같다.

```text
X =
Q^nu =
why phase B has w ~= -1 =
delta Q route =
known-model distinction =
```

하나라도 비면 exploratory provenance 또는 blocked audit로 남긴다. Level 2B로
올리지 않는다.

## 3. 아이디어 계보 분기

아이디어 계보 분기는 이 작업이 왜 시작됐는지 보존한다.

여기에 들어갈 수 있는 내용:

- black-hole information problem.
- black-hole evaporation과 scrambled output 직관.
- white-hole/remnant 상상.
- quantum foam medium 직관.
- public bridge와 쉬운 설명.

이 분기는 중요하지만 물리 증거가 아니다. 계보 문서는 질문의 출처와 narrowing
history를 보존한다. 검증, 기각, known-model reduction은 research investigation
또는 theory/audit 문서에서 처리한다.

## 라우팅 규칙

새 작업을 시작할 때 먼저 아래 규칙으로 분류한다.

| 새 문장 또는 작업 | 보내는 곳 |
| --- | --- |
| "관측값이 어디까지 허용하나?" | 실증적 분기 |
| "이 후보가 source variable이 될 수 있나?" | 임의 탐색 분기 |
| "이 아이디어가 왜 나왔나?" | 아이디어 계보 분기 |
| "블랙홀이 dark energy를 만든다" | 어느 분기도 통과 불가; source equation 전에는 금지 |
| "`xi ~= 10 Mpc`가 맞아 보인다" | 임의 탐색 분기; input/output/unknown부터 고정 |
| "NASA/BAO를 보면 scale을 고를 수 있다" | circularity stop |
| "retained timing이 물리 기원을 시사한다" | 금지; IV/IDE comparator로만 허용 |

## Circularity Stop

아래 조건 중 하나라도 발생하면 작업을 멈춘다.

- 관측값을 먼저 보고 `xi`, transition width, amplitude를 고른다.
- fitted timing을 physical source로 재명명한다.
- black-hole, remnant, entropy, information, foam이라는 이름으로 `X` 또는
  `Q^nu` 빈칸을 채운 것처럼 쓴다.
- baseline constraint를 QFUDS support로 표현한다.
- lineage 문서를 result 문서처럼 인용한다.

## 다음 실행 후보

이 라우팅 문서 이후의 안전한 다음 작업은 둘 중 하나다.

1. `black-hole evaporation/remnant falsifiability ledger`
   - 분기: 임의 탐색 분기와 실증적 분기의 경계.
   - 목적: 증발, remnant, compact-object source 후보가 어떤 constraint에서
     먼저 죽는지 정리한다.
   - 금지: dark-energy source claim.

2. `idea lineage continuation note`
   - 분기: 아이디어 계보 분기.
   - 목적: 007 이후 "왜 이 출발점이 여전히 public bridge로 의미가 있는지"
     짧게 정리한다.
   - 금지: 검증 결과처럼 쓰기.

기본 추천은 첫 번째다. 계보는 이미 007에 남았으므로, 다음에는 후보가
과학적으로 어디서 막히는지 장부화하는 편이 더 유용하다.
