---
doc_id: postmortem-003-qfuds-scope-demotion-retrospective
id: postmortem-003-qfuds-scope-demotion-retrospective
seq: 3
title: "QFUDS 범위 축소 회고"
doc_type: postmortem
type: postmortem
stage: reference
status: reference
wiki_status: active
evidence_role: reference
depends_on:
  - roadmap
  - experiment_summary
  - decision_log
  - result_001_5_phase_transfer_physicality
  - result_003_phenomenological_perturbation_closure
  - result_004_p1_model_family_positioning
  - result_005_timing_prior_usefulness
  - result_006_literature_timing_support_audit
next_gate: no roadmap change; use this as a retrospective handoff for why the retained branch was demoted
date: 2026-06-10
context: GPT 회고 텍스트를 바탕으로 QFUDS 연구 범위 축소와 demotion 경로를 공식 postmortem으로 정리
audience: 주니어 개발자
length: 작업 단계별 풀어쓰기
created_at: 2026-06-10
created_by: dorito
updated_at: 2026-06-10
updated_by: dorito
last_updated: 2026-06-10
last_verified_at: 2026-06-10
last_verified_by: dorito
audit_log:
  - action: created
    at: 2026-06-10
    by: dorito
    note: "Created after reviewing the retrospective GPT summary against the roadmap, experiment summary, decision log, and retained-branch result documents."
tags: [postmortem, qfuds, scope-control, demotion, gamma]
relations:
  - docs/05_next_steps/000_roadmap.md
  - docs/04_results/000_experiment_summary.md
  - docs/00_project/decision_log.md
  - docs/04_results/015_result_001_5_phase_transfer_physicality.md
  - docs/04_results/030_result_003_phenomenological_perturbation_closure.md
  - docs/04_results/030_result_004_p1_model_family_positioning.md
  - docs/04_results/030_result_005_timing_prior_usefulness.md
  - docs/04_results/030_result_006_literature_timing_support_audit.md
  - outputs/postmortem/exp003_friction_bug/README.md
code_refs:
  - file: docs/05_next_steps/000_roadmap.md
    note: "Current project-status authority; records retained-branch demotion and blocked physical Level 2B."
  - file: docs/04_results/000_experiment_summary.md
    note: "Compact experiment-by-experiment evidence boundary."
  - file: docs/00_project/decision_log.md
    note: "Chronological record of demotions, reclassifications, and negative decisions."
  - file: outputs/postmortem/exp003_friction_bug/README.md
    note: "Detailed postmortem for the Exp003 Euler-friction bug."
---

# QFUDS 범위 축소 회고

이 문서는 새 실험 결과가 아니다. Roadmap status도 바꾸지 않는다.

역할은 하나다. GPT 회고 텍스트가 잘 잡은 핵심, 즉 "처음의 큰 직관을
검증 가능한 작은 질문으로 계속 깎아냈다"는 흐름을 저장소의 현재
문서 기준으로 고정한다.

## 사건 한 줄 요약

QFUDS는 Landauer, black-hole information, white-hole/remnant, quantum foam
직관에서 출발했지만, 저장소 안에서는 그 직관을 계속 낮은 증거 등급으로
내렸다. 현재 retained branch는 physical QFUDS가 아니라
structure-era `Gamma(a)` timing을 가진 phenomenological interacting-vacuum /
time-dependent IDE branch다.

현재 성과는 "이론 완성"이 아니다.

```text
큰 설명을 죽일 수 있는 변수와 gate로 바꿨고,
살아남은 branch도 물리 이론이 아니라 phenomenology로 강등했다.
```

## 0. 사전 지식

| 용어 | 이 문서에서의 의미 |
| --- | --- |
| QFUDS | dark matter와 dark energy가 common quantum-spacetime foam sector의 서로 다른 macroscopic phase일 수 있는지 묻는 speculative toy framework |
| phase A | clustering하고 nearly pressureless하게 행동하도록 둔 component. 목표 성질은 `w_A ~= 0`, `c_s,A^2 ~= 0` |
| phase B | smooth vacuum-pressure component. 목표 성질은 `w_B ~= -1` |
| `Gamma(a)` | phase A에서 phase B로 넘어가는 transfer timing function |
| retained branch | collapse/information-production timing에서 이어진 현재 surviving branch |
| P1 | Exp003에서 살아남은 phase-A-frame interacting-vacuum perturbation closure |
| P2 | Exp003에서 실패한 regularized near-vacuum fluid closure |
| IV/IDE | interacting vacuum / interacting dark energy |
| physical QFUDS | `X`, `Q^nu`, `w_B ~= -1`의 이유, `delta Q`, known-model distinction이 같은 mechanism에서 나오는 branch |
| phenomenology | 물리 원인 유도 없이 effective equation과 timing shape를 놓고 관측/수치 가능성을 보는 단계 |

주의할 점이 있다. `z ~= 2`는 redshift다. Equation-of-state `w`가 아니다.
QFUDS에서 matter-like 성분은 `w ~= 0`, vacuum-like 성분은 `w ~= -1`이다.

## 1. 증상

GPT 회고 텍스트는 저장소의 큰 흐름을 대체로 맞게 읽었다.

```text
Landauer intuition
-> black-hole information question
-> white-hole/remnant/quantum-foam origin trail
-> two-phase dark sector
-> Gamma(a) transfer problem
-> low-redshift structure-era timing
-> physicality audit failure
-> phenomenological interacting-vacuum branch
-> IV/IDE timing-prior question
```

다만 이 흐름을 문서화할 때 조심해야 하는 위험이 있다.

| 위험 | 왜 위험한가 | 문서에서의 처리 |
| --- | --- | --- |
| "QFUDS가 살아남았다" | 현재 살아남은 것은 physical QFUDS가 아니라 P1 phenomenology다 | survival이라는 말 앞에 항상 scope를 붙인다 |
| "Gamma(a)가 물리적으로 유도됐다" | retained relation은 source derivation을 통과하지 못했다 | `Gamma(a)`는 timing shape 또는 ansatz로 둔다 |
| "문헌이 timing을 지지한다" | Exp006은 allowed but not informative다 | literature support를 overlap 수준으로 제한한다 |
| "화이트홀/블랙홀이 중심 증거다" | 현재 docs에서는 origin/provenance 또는 future branch 후보에 가깝다 | central claim이 아니라 downgraded origin trail로 둔다 |
| "버그 수정 후 P1이 물리적으로 검증됐다" | Exp003 bug fix는 P1 stability classification만 재검증했다 | [Level 2A](../glossary/repository_levels.md) phenomenology로 제한한다 |

즉 이 postmortem의 목적은 회고 텍스트를 더 멋있게 만드는 것이 아니다.
강한 문장을 저장소의 증거 등급에 맞게 낮추는 것이다.

## 2. 첫 의문 + 가설

| 가설 | 왜 그럴 수 있는지 | 어떻게 확인할지 |
| --- | --- | --- |
| H1. GPT 회고의 중심 흐름은 repo 상태와 맞다 | Roadmap, experiment summary, decision log가 같은 demotion chain을 기록할 가능성이 높다 | `000_roadmap.md`, `000_experiment_summary.md`, `decision_log.md`를 확인한다 |
| H2. 회고 텍스트가 retained branch를 너무 강하게 말할 수 있다 | "survival", "timing support", "학계 미해결 영역" 같은 표현은 쉽게 과대해석된다 | result 003-006의 scope와 verdict를 대조한다 |
| H3. 새 실험 문서가 아니라 postmortem/checkpoint가 맞다 | 사용자는 회고록 정리를 요청했고, 새 hypothesis/result chain을 요구하지 않았다 | 기존 `docs/wiki/postmortem` 형식과 postmortem policy를 따른다 |
| H4. Roadmap이나 decision log를 갱신하면 안 된다 | 새 evidence가 없고 status authority를 건드리면 drift가 생긴다 | 상태 문서는 읽기만 하고 새 reference 문서 하나만 추가한다 |

검증 순서는 싸고 강한 증거부터 잡았다. 먼저 roadmap과 summary로 status
boundary를 확인하고, 그 다음 result 문서로 각 claim의 강도를 낮췄다.

## 3. 진단: 실제 상태 확인

### 3.1 Roadmap 확인

사용한 명령:

```bash
rtk sed -n '1,220p' docs/05_next_steps/000_roadmap.md
```

핵심 확인:

```text
stage: "1.5"
status: in_progress
next_gate: retained branch demoted; retained timing allowed but not informative as an IV/IDE prior
```

Roadmap의 현재 gate는 명확하다.

```text
Retained branch demoted to phenomenological interacting vacuum.
Physical Level 2B remains blocked.
CLASS/CAMB, CMB, matter power, survey likelihoods remain blocked.
```

H1은 지지된다. GPT 회고의 "계속 강등했다"는 큰 흐름은 현재 roadmap과
맞다.

H4도 지지된다. 새 증거가 없으므로 roadmap을 바꿀 이유가 없다.

### 3.2 Experiment summary 확인

사용한 명령:

```bash
rtk sed -n '1,260p' docs/04_results/000_experiment_summary.md
```

핵심 확인:

```text
Current Evidence Boundary:
The repository has validated background behavior and one phenomenological
perturbation closure. It has not validated physical QFUDS perturbations, CMB
spectra, matter power, BAO, supernovae, DESI, Euclid, Roman, or survey
likelihoods.
```

Summary table도 같은 결론을 준다.

```text
exp_001_5: retained branch fails physical Level 1.5 promotion
exp_003: P2 fails; P1 remains stable only as phenomenological interacting vacuum
exp_004: P1 is exact interacting-vacuum instance and time-dependent IDE subset
exp_005: retained timing is a potential IV/IDE prior-compression target
exp_006: retained timing is allowed but not informative
```

H2는 지지된다. 회고 텍스트는 좋은 방향을 잡았지만, 문서에는 반드시
evidence boundary를 같이 써야 한다.

### 3.3 Decision log 확인

사용한 명령:

```bash
rtk sed -n '1,260p' docs/00_project/decision_log.md
```

핵심 결정 흐름:

```text
zero-transfer LCDM baseline kept as control
white-hole-universe image rejected as central claim
two-phase dark-sector formulation adopted as minimal working model
constant Gamma and ungated growth-driven Gamma rejected
experiment 002 demoted from evidence to provenance
Level 1.5 inserted before perturbation closure
P2 failed; P1 retained only as non-novel Level 2A interacting vacuum
retained branch failed physical promotion
retained P1 classified as IV/IDE subset
retained Gamma(a) timing classified as potential prior-compression target
```

이 로그는 회고 텍스트의 핵심 문장을 뒷받침한다.

```text
증명하려고 밀어붙인 기록이 아니라,
과대주장을 제거하면서 마지막에 남는 최소 질문을 찾은 기록이다.
```

### 3.4 Result 003-006 확인

사용한 명령:

```bash
rtk sed -n '1,260p' docs/04_results/030_result_003_phenomenological_perturbation_closure.md
rtk sed -n '1,260p' docs/04_results/030_result_004_p1_model_family_positioning.md
rtk sed -n '1,260p' docs/04_results/030_result_005_timing_prior_usefulness.md
rtk sed -n '1,240p' docs/04_results/030_result_006_literature_timing_support_audit.md
```

확인된 verdict:

| Result | Verdict | 이 회고에서의 의미 |
| --- | --- | --- |
| Result 003 | P1 stable as Level 2A phenomenology; P2 fails at retained amplitude | "perturbation survival"은 P1 closure scope 안에서만 맞다 |
| Result 004 | retained P1 is exact interacting-vacuum instance and time-dependent IDE subset | QFUDS 독립 물리 이론이 아니라 known family 안에 들어간다 |
| Result 005 | retained timing is potentially useful compression target | 남은 가치는 timing-prior 후보 수준이다 |
| Result 006 | allowed but not informative | 문헌상 배제는 아니지만 informative prior 근거도 아니다 |

따라서 H3도 지지된다. 이 문서는 result나 experiment가 아니라
postmortem/checkpoint가 맞다.

## 4. 실제로 줄어든 범위

아래 표가 이 postmortem의 핵심이다.

| 초기 표현 | 저장소에서 살아남은 형태 | 현재 등급 |
| --- | --- | --- |
| 정보 삭제에는 물리 비용이 있다 | Landauer-trigger origin trail | provenance |
| 블랙홀이 정보 압축기일 수 있다 | strong-gravity/remnant 후보 | speculative, optional |
| 화이트홀/우주론 이미지 | central claim에서 제거 | rejected as central claim |
| quantum foam이 dark sector를 만든다 | two-phase effective dark-sector toy language | hypothesis/model language |
| dark matter와 dark energy가 같은 sector의 phase일 수 있다 | phase A/B background equations | working model, not proven |
| phase transfer가 물리적으로 일어난다 | `Gamma(a)` background ansatz | test variable |
| entropy/information production이 transfer source다 | `Gamma(a) proportional to dF_coll/dln(a)` timing shape | provenance, not physical source |
| retained branch가 physical QFUDS다 | interacting-vacuum / time-dependent IDE subset | demoted phenomenology |
| P1 survives perturbations | P1 stable under declared Level 2A closure | non-novel phenomenological survival |
| timing is supported by literature | table-level literature allows overlap but is not informative | allowed but not informative |

가장 짧게 쓰면 이렇다.

```text
화이트홀-정보-foam 통합 직관
-> 두 phase dark sector
-> Gamma(a) transfer problem
-> low-redshift collapse/information-production timing
-> physical derivation failure
-> phenomenological interacting-vacuum branch
-> IV/IDE timing-prior candidate
-> allowed but not informative literature status
```

## 5. 결론 / 해결

GPT 회고 텍스트의 좋은 점은 "QFUDS가 맞다"가 아니라 "QFUDS가 계속
작아졌다"를 중심으로 읽었다는 점이다. 이건 저장소의 실제 record와 맞다.

하지만 공식 문서에서는 다음처럼 더 보수적으로 써야 한다.

```text
현재 retained branch는 physical QFUDS가 아니다.
retained P1은 known interacting-vacuum / time-dependent IDE phenomenology다.
retained Gamma(a)는 z ~= 2 structure-era timing intuition을 담은
potential compression target일 뿐이다.
문헌상 배제되지는 않았지만, informative prior로 쓸 만큼 지지되지도 않았다.
```

따라서 이번 문서의 해결은 roadmap 변경이 아니라 회고의 위치를 고정하는
것이다.

```text
이 postmortem = scope-demotion narrative
roadmap = current status authority
result docs = evidence authority
decision log = why authority
```

## 6. 재발 방지 / 운영 메모

앞으로 QFUDS를 설명할 때는 아래 문장들을 기준으로 삼는다.

1. "survived"라고 쓰기 전에 무엇을 통과했는지 붙인다.
2. `Gamma(a)`를 physical source처럼 쓰지 않는다. 지금은 timing ansatz 또는
   prior-compression target이다.
3. black hole, white hole, remnant, quantum foam은 origin/provenance 또는
   future branch 후보로 둔다. 현재 retained branch의 증거로 쓰지 않는다.
4. `z ~= 2` timing과 `w` equation-of-state를 섞지 않는다.
5. Exp003 P1 survival은 bug correction 이후에도 Level 2A phenomenology다.
6. Exp006 literature overlap은 "allowed but not informative"다. "supported"로
   올리지 않는다.
7. 새 physical branch를 열려면 roadmap의 admission rule을 먼저 채운다:

```text
X =
Q^nu =
why phase B has w ~= -1 =
delta Q route =
known-model distinction =
```

## 7. 타임라인

- Origin: Landauer intuition에서 information cost와 black-hole information
  question이 생겼다.
- Early pruning: white-hole-universe image는 central claim에서 내려왔다.
- Model narrowing: QFUDS는 two-phase dark-sector toy framework로 줄었다.
- Background gate: `Gamma(a)=0` LCDM baseline이 control로 정리됐다.
- Gamma scan: constant와 ungated growth-driven transfer는 early activation
  때문에 탈락했다.
- Entropy/information gate: broad entropy language는 죽고
  collapse/information-production timing만 provenance로 남았다.
- Level 1.5: retained branch는 physical phase-transfer law로 승격하지
  못했다.
- Exp003: P1은 Level 2A phenomenology로 안정, P2는 retained amplitude에서
  실패했다.
- Bug postmortem: Euler-friction bug를 수정했고 P1/P2 classification은
  유지됐지만 clustering diagnostic은 재평가됐다.
- Exp004: retained P1은 interacting-vacuum / time-dependent IDE subset으로
  분류됐다.
- Exp005: retained timing은 potential IV/IDE prior-compression target으로
  낮춰졌다.
- Exp006: retained timing은 literature table level에서 allowed but not
  informative로 정리됐다.

## 부록 A - 디버깅 명령어 모음

이 문서는 코드 버그를 고친 postmortem은 아니지만, claim hygiene를 위해
문서 증거를 확인했다.

### 현재 상태 확인

```bash
rtk sed -n '1,220p' docs/05_next_steps/000_roadmap.md
```

`sed -n '1,220p'`는 파일 앞 220줄만 출력한다. 이 사건에서는 roadmap
frontmatter와 status table을 확인했다. 출력에서 `next_gate`와 Level 1.5,
2A, 2B 상태를 읽었다.

### 실험 요약 확인

```bash
rtk sed -n '1,260p' docs/04_results/000_experiment_summary.md
```

이 명령은 전체 실험 흐름과 evidence boundary를 빠르게 확인하는 용도다.
여기서는 "validated background behavior and one phenomenological
perturbation closure"라는 경계를 읽었다.

### 결정 이유 확인

```bash
rtk sed -n '1,260p' docs/00_project/decision_log.md
```

Decision log는 "무엇을 왜 내렸는지"를 확인하는 파일이다. 이 사건에서는
white-hole central claim rejection, Level 1.5 insertion, retained-branch
demotion, IV/IDE classification을 확인했다.

### 개별 결과 확인

```bash
rtk sed -n '1,260p' docs/04_results/030_result_003_phenomenological_perturbation_closure.md
rtk sed -n '1,260p' docs/04_results/030_result_004_p1_model_family_positioning.md
rtk sed -n '1,260p' docs/04_results/030_result_005_timing_prior_usefulness.md
rtk sed -n '1,240p' docs/04_results/030_result_006_literature_timing_support_audit.md
```

Result 문서는 verdict의 강도를 확인하는 곳이다. 이 사건에서는 각 result의
Scope, Executive Verdict, Decision 섹션을 확인했다.

이런 부류의 문제는 보통 이 순서로 푼다.

```text
roadmap으로 현재 상태 확인
-> experiment summary로 전체 evidence boundary 확인
-> decision log로 왜 그렇게 됐는지 확인
-> result docs로 각 claim의 강도 확인
-> 새 상태 변경 없이 reference/postmortem으로 narrative만 고정
```
