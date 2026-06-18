---
doc_id: plan_2026_06_18_public_bridge_lineage_ko
title: "블랙홀 정보 서사 연결 계획"
doc_type: guide
stage: reference
status: completed
evidence_role: provenance
depends_on:
  - roadmap
  - concept_origin
  - concept_survival_audit
  - qfuds_strong_gravity_source_mechanism_audit
  - audit_2026_06_11_level2b_eligibility_review_observer_mode
  - plan_2026_06_18_candidate_equation_proposal_template
next_gate: write lineage 007 as public bridge only; preserve admission gates and no Level 2B language
last_updated: 2026-06-18
---

# 블랙홀 정보 서사 연결 계획

## 목적

이 문서는 QFUDS의 SF적 출발점인 블랙홀 정보 문제, 블랙홀 증발,
white-hole/remnant 직관, quantum foam 언어를 버리지 않고 다음 문서로
연결하기 위한 폴더 구조와 경계 규칙을 정한다.

이 문서는 물리 결과가 아니다.

이 문서는 QFUDS 지지 근거가 아니다.

이 문서는 Physical-QFUDS Level 2B를 열지 않는다.

## Workflow Boundary

This guide applies the
[Research Asset and Product Workflow](../../.agent/workflows/research-asset-product-workflow.md)
only to preserve source-state boundaries.

No new external web, PDF, table, product, cache, digitization, or availability
claim is introduced here. Existing source-state tokens remain inherited from the
repository research cache, including `asset_cached`,
`asset_extracted_not_digitized`, `hit_not_cached`, and `inspected_no_numerical_product`
where recorded by the owning research notes.

## 정리 원칙

지금까지 한 작업을 살리는 방식은 QFUDS를 억지로 살리는 것이 아니다.

살릴 것은 세 가지다.

1. 원래 질문의 흐름:
   정보 보존, 블랙홀 증발, remnant, vacuum residual, dark sector로 이어진
   사고 경로.
2. 과학적 엄밀함:
   수식, admission rule, known-model reduction, validation, cache state,
   pre-commit gate.
3. 대중적 설명 가치:
   일반인에게는 "블랙홀은 우주의 하드디스크인가?"라는 질문이 가장
   이해하기 쉽다.

살리면 안 되는 것은 세 가지다.

1. 블랙홀 증발을 QFUDS dark-energy source로 이미 검증된 것처럼 쓰기.
2. black-hole entropy, remnant, quantum foam, `xi_gal` 언어를 `X`, `Q^nu`,
   `delta Q`, phase-B pressure 대신 쓰기.
3. NASA/BAO/LSS/CMB/retained timing을 먼저 보고 후보 scale, width,
   amplitude를 고른 뒤 source라고 부르기.

## 폴더 구조

현재 구조를 유지한다.

| 역할 | 위치 | 이유 |
| --- | --- | --- |
| 원래 SF적 사고 경로 | `docs/01_origin/` | 동기와 provenance는 여기서 보존한다. |
| 엄밀한 물리 판정 | `docs/02_theory/`, `docs/03_experiments/`, `docs/04_results/` | 수식, 실험, 결과, 실패 판정은 기존 stage 구조에 둔다. |
| 현재 상태와 다음 gate | `docs/05_next_steps/` | roadmap, safe branch, public bridge 계획을 둔다. |
| 대중용 연결 서사 | `docs/wiki/lineage/` | idea genealogy와 branch demotion을 설명하는 곳이다. |
| 레퍼런스와 외부 자료 | `docs/wiki/research/` | literature, asset, digitization, source-state 기록은 여기서만 관리한다. |
| 강제 규칙 | `.agent/workflows/`, scripts, git hooks | agent workflow와 commit gate는 여기서 유지한다. |

새 top-level 폴더는 만들지 않는다. 지금 필요한 것은 폴더 확장이 아니라
문서 역할 분리다.

## 다음 문서

다음 실행 문서는 `docs/wiki/lineage/007_black_hole_information_public_bridge_ko.md`
로 둔다.

문서 역할:

```text
public_bridge
provenance_only
not_physical_evidence
not_result
not_Level_2B
```

권장 제목:

```text
블랙홀은 우주의 하드디스크인가?
```

이 문서는 일반 독자가 읽을 수 있는 문서여야 한다. 단, 문서 안에서 모든
과학적 경계는 명시한다.

## 007 문서의 필수 구조

1. 왜 이 질문이 재미있는가:
   정보는 사라지는가, 보존되는가, 어디에 저장되는가.
2. 블랙홀 정보 문제:
   Hawking radiation, Page curve, island, unitary evaporation은 동기와
   이론적 배경이다.
3. QFUDS로 넘어간 사고 경로:
   information preservation -> black-hole compression -> remnant/vacuum
   residual -> dark-sector question.
4. 지금까지 검증한 것:
   Gamma scans, entropy/information gate, Level 1.5 demotion, Level 2A
   phenomenology, Source-X digitization, known-model reduction.
5. 지금까지 검증하지 못한 것:
   `entropy -> energy transfer -> smooth w ~= -1 phase B` 변환 방정식.
6. 그래서 남는 가치:
   QFUDS 물리 이론의 지지가 아니라, speculative idea를 audit harness로
   해부한 기록.
7. 다음 연구문:
   black-hole evaporation/remnant falsifiability ledger 또는
   candidate-equation template.

## 금지 문장

007 문서는 아래 문장을 쓰면 안 된다.

```text
블랙홀이 dark energy를 만든다.
블랙홀 증발이 QFUDS를 지지한다.
화이트홀/remnant가 phase B다.
정보 보존이 곧 vacuum pressure다.
Chen entropy curve가 Gamma(a)를 검증한다.
```

허용되는 문장은 아래처럼 좁혀 쓴다.

```text
블랙홀 정보 문제는 QFUDS의 출발 동기였다.
블랙홀 entropy/growth/remnant route는 후보 source lane이었다.
현재 repository는 그 route가 phase-B vacuum pressure로 이어지는
방정식을 갖고 있지 않다.
그래도 이 경로는 어떤 수식이 없으면 speculative idea가 죽는지
명확히 보여주는 audit record로 남는다.
```

## 과학 엄밀성 유지 규칙

007 문서와 이후 public-facing 문서는 다음 규칙을 따른다.

| 보존할 요소 | 적용 방식 |
| --- | --- |
| 수식 경계 | `X`, `Q^nu`, `delta Q`, `w ~= -1`, `T_mu_nu`가 없으면 물리 claim 금지. |
| 레퍼런스 시스템 | 새 외부 claim은 research cache 또는 workflow state를 통해서만 추가. |
| 검증 언어 | `tested`, `failed`, `blocked`, `provenance`, `motivation`을 구분. |
| known-model reduction | HDE, IV/IDE, CCBH, remnant DM, backreaction 등 먼저 비교. |
| roadmap SSOT | 현재 상태는 roadmap에만 둔다. lineage 문서는 status authority가 아니다. |
| 대중성 | 비유는 허용하지만 비유를 evidence로 쓰지 않는다. |

## 현재 판정

현재까지의 결론은 다음과 같이 써야 한다.

```text
QFUDS as a physical theory: not admitted.
Black-hole information route: motivation and candidate-source provenance.
Retained timing: phenomenological IV/IDE comparator only.
Research value: high as an audit harness and negative-result map.
Public value: high as a readable story about how a speculative idea is forced
through constraints.
```

## 다음 실행 지시

다음 작업은 `docs/wiki/lineage/007_black_hole_information_public_bridge_ko.md`
를 작성하는 것이다. 그 문서는 public bridge/provenance 문서로만 작성하고,
roadmap status, Physical-QFUDS Level 2B, model support, validation language를
열지 않는다. 작성 후 [docs/wiki/lineage/README.md](../wiki/lineage/README.md),
[docs/wiki/index.md](../wiki/index.md), [docs/README.md](../README.md), 필요하면
[README.md](../../README.md)의 Start Here 또는 Documents 섹션만 좁게
연결한다.
