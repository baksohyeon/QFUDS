---
doc_id: postmortem-002-iv-ide-timing-checkpoint
id: postmortem-002-iv-ide-timing-checkpoint
seq: 2
title: "IV/IDE 타이밍 조사 체크포인트"
doc_type: postmortem
type: postmortem
stage: reference
status: reference
wiki_status: active
evidence_role: reference
depends_on:
  - result_004_p1_model_family_positioning
  - result_005_timing_prior_usefulness
  - result_006_literature_timing_support_audit
  - audit_2026_06_09_exp006_coverage_expansion
  - audit_2026_06_09_li_2025_timing_feasibility
  - audit_2026_06_09_li_2025_digitized_compression
next_gate: no roadmap change; use this checkpoint as handoff context before any future timing or posterior-product work
date: 2026-06-09
context: QFUDS Exp004-Exp006 이후 IV/IDE timing branch 점검과 Li & Zhang 2025 digitized compression audit
audience: 주니어 개발자
length: 작업 단계별 풀어쓰기
created_at: 2026-06-09
created_by: dorito
updated_at: 2026-06-09
updated_by: dorito
last_updated: 2026-06-09
last_verified_at: 2026-06-09
last_verified_by: dorito
audit_log:
  - action: created
    at: 2026-06-09
    by: dorito
    note: "Created after Exp004-Exp006, coverage expansion, Li and Zhang timing analysis, and digitized compression audit."
tags: [postmortem, qfuds, iv-ide, timing, li-2025]
relations:
  - docs/04_results/030_result_004_p1_model_family_positioning.md
  - docs/04_results/030_result_005_timing_prior_usefulness.md
  - docs/04_results/030_result_006_literature_timing_support_audit.md
  - docs/wiki/research/audits/2026-06-09_exp006_coverage_expansion_audit.md
  - docs/wiki/research/audits/2026-06-09_li_2025_timing_feasibility_audit.md
  - docs/wiki/research/audits/2026-06-09_li_2025_digitized_compression_audit.md
  - docs/00_project/project_identity.md
  - docs/00_project/qfuds_positioning.md
  - docs/00_project/success_criteria.md
  - docs/05_next_steps/000_roadmap.md
  - docs/00_project/decision_log.md
  - docs/04_results/000_experiment_summary.md
code_refs:
  - file: scripts/run_li2025_digitized_compression_audit.py
    note: "Digitized Li and Zhang figure products and compared retained timing against transition, pulse, and tomographic families."
  - file: outputs/li2025_digitized_compression_audit/li2025_digitized_compression_metrics.csv
    note: "Metric table for signed, positive-support, and evidence-weighted-support timing comparisons."
  - file: outputs/li2025_digitized_compression_audit/li2025_digitized_compression_summary.json
    note: "Machine-readable summary of the partial_compression classification."
---

# IV/IDE 타이밍 조사 체크포인트

이번 문서는 새 실험 결과가 아니다. Exp004, Exp005, Exp006의 공식
classification(실험 결과 분류)도 바꾸지 않는다. Roadmap status(현재
프로젝트 진행 상태)도 바꾸지 않는다.

이 문서의 역할은 세션 리셋용 checkpoint(다음 세션이 바로 이어받기 위한
중간 정리 문서)다. 최근 IV/IDE(interacting vacuum / interacting dark
energy; 암흑물질 같은 성분과 암흑에너지 같은 성분 사이의 에너지 교환을
허용하는 모형군) timing 조사가
무엇을 죽였고, 무엇을 살렸고, 다음 사람이 어디서부터 읽으면 되는지 한
곳에 모은다.

## 사건 한 줄 요약

처음 질문은 retained P1(Exp003 이후 살아남은 phase-A-frame
interacting-vacuum closure; phase A를 암흑물질처럼 clustering하는 성분으로
두고 phase B를 vacuum-like 성분으로 둔 perturbation prescription)과
retained `Gamma(a)`(`a`라는 우주 scale factor에 따른 transfer timing
function; 어느 시기에 phase A에서 phase B로 energy transfer가 강한지
나타내는 곡선) timing이 물리적 QFUDS 신호인지, 아니면 알려진 interacting
vacuum / interacting dark energy phenomenology(미시적 원인 유도 없이
effective equation을 놓고 관측 가능성을 테스트하는 단계)인지 확인하는
것이었다.

결론은 보수적이다.

```text
retained P1은 IV/IDE phenomenology로 남았고,
retained Gamma(a)는 leading compression implementation이 아니며,
살아남은 것은 특정 Gamma(a) 모양이 아니라 structure-era transition timing
intuition(구조 형성 시기 근처에서 interaction이 켜지거나 부호가 바뀔 수
있다는 timing 직감)이다.
```

## 0. 사전 지식

| 용어 | 이 문서에서의 의미 |
| --- | --- |
| redshift `z` | 우주 팽창 때문에 빛의 파장이 늘어난 정도. 큰 `z`일수록 더 과거 우주다. 이 문서에서 `z ~ 2`는 지금보다 훨씬 이른 구조 형성 시기 근처를 뜻한다. |
| phase A | QFUDS toy language에서 clustering하고 nearly pressureless하게 행동하도록 둔 dark-matter-like component. 대략 `w_A ~= 0`, `c_s,A^2 ~= 0` 역할이다. |
| phase B | QFUDS toy language에서 smooth하고 vacuum-pressure처럼 행동하도록 둔 dark-energy-like component. 대략 `w_B ~= -1` 역할이다. |
| phase transfer | phase A에서 phase B로 에너지 밀도가 이동한다고 가정한 phenomenological bookkeeping. 현재 retained branch에서는 이것이 physical mechanism으로 유도되지 않았다. |
| P1 | Exp003에서 테스트한 perturbation closure 중 하나. Energy transfer를 phase-A/comoving frame에 맞춘 interacting-vacuum closure로 취급한다. 쉽게 말해 phase A는 CDM처럼 clustering하고, phase B는 vacuum-like component로 두며, transfer perturbation은 `delta Q = Q delta_A`, `deltaGamma = 0` 형태로 닫은 phenomenological prescription이다. |
| retained P1 | Exp003 이후 살아남은 P1 closure. Exp004에서 interacting vacuum / time-dependent IDE와 동등한 phenomenology로 분류됐다. Physical QFUDS branch가 아니다. |
| retained `Gamma(a)` | Exp002/Exp005에서 이어진 normalized information-production timing profile |
| IV/IDE | interacting vacuum / interacting dark energy |
| timing intuition | 구조 형성 시기 근처에 dark-sector interaction timing feature가 있을 수 있다는 직감 |
| compression | 자유로운 `beta(z)` reconstruction을 더 적은 timing parameter로 설명하는 능력 |
| supported compression target | 단순 overlap이 아니라, 경쟁 timing family보다 더 효율적으로 reconstruction structure를 설명하는 경우 |

아래 표는 다시 읽을 때 쓰는 용어표다. 본문에서는 중요한 용어가 처음
나올 때 괄호로 한 번 더 풀어쓴다.

| 전문 용어 | 풀어쓴 의미 |
| --- | --- |
| interacting vacuum | Dark matter처럼 clustering하는 성분과 vacuum energy처럼 smooth한 성분 사이에 에너지가 오간다고 쓰는 cosmology model family. "진공이 입자처럼 움직인다"는 뜻이 아니라, vacuum-pressure component의 에너지 밀도가 CDM-like component와 coupled되어 있다고 parameterize한다는 뜻이다. |
| interacting dark energy, IDE | Dark matter와 dark energy 사이의 에너지 교환을 허용하는 더 넓은 model family. Coupling function을 자유롭게 두면 새 물리라기보다 IDE parameterization이 된다. |
| phenomenology | 미시적 원인을 아직 유도하지 않고, 관측 가능한 effective equation만 세워서 테스트하는 단계. 공학적으로 말하면 "원인 모델은 아직 없지만 input-output law를 놓고 검증하는 단계"에 가깝다. |
| physical derivation | 왜 그런 transfer law가 나오는지 source, units, stress-energy relation, perturbation까지 한 mechanism에서 유도하는 것. QFUDS가 아직 못 한 부분이다. |
| perturbation closure | 평균 우주 배경만이 아니라 작은 density fluctuation이 어떻게 진화하는지 방정식을 닫는 규칙. Closure가 없으면 matter power, CMB 같은 structure observables를 책임 있게 계산할 수 없다. |
| `Gamma(a)` | QFUDS repo 내부에서 쓴 phase-transfer timing function. `a`는 scale factor이고, `a=1/(1+z)`다. 이 함수가 크면 그 시기에 transfer가 강하다는 뜻이다. |
| `beta(z)` | Li & Zhang이 재건한 IDE coupling function. `z`별로 dark-sector coupling이 positive인지 negative인지, zero와 compatible한지 보는 대상이다. |
| sign reversal | `beta(z)`의 부호가 cosmic time에 따라 바뀌는 현상. 여기서는 low-z에서 negative/zero-compatible, high-z에서 positive 쪽으로 가는 transition-like structure를 뜻한다. |
| posterior / covariance | MCMC나 likelihood 분석에서 나온 불확실성 정보. Mean curve만 있으면 "모양"은 볼 수 있지만, covariance/posterior가 있어야 그 모양이 데이터가 강제한 것인지 prior나 noise인지 더 엄밀히 판단할 수 있다. |
| PCA mode | 복잡한 binned function을 독립적인 주요 패턴들로 분해한 것. Li & Zhang에서 "data-dominated modes"는 데이터가 실제로 constrain한 timing pattern을 뜻한다. |
| DESI-era | DESI BAO 데이터가 들어간 최근 dark-energy reconstruction 문헌군을 가리키는 shorthand. 단순히 최신이라는 뜻이 아니라, redshift coverage와 BAO precision 때문에 timing 질문에 민감할 수 있다는 뜻이다. |

## 1. Starting Question

원래 질문은 다음이었다.

```text
구조 형성 시기와 맞물린 retained Gamma(a) timing이
실제 IV/IDE reconstruction(관측 데이터로부터 coupling history를 되짚어
추정한 결과)에서 정보가 있는 feature인가,
아니면 QFUDS 내부에서만 그럴듯한 curve인가?
```

이 질문 안에는 세 단계가 섞여 있었다.

1. retained P1이 어떤 model family에 속하는가?
2. retained `Gamma(a)` timing이 useful compression target인가?
3. 실제 IV/IDE 문헌, 특히 DESI-era reconstruction이 이 timing을 지지하는가?

조사 후 이 세 질문은 분리됐다.

```text
model family: IV/IDE로 정리됨
retained implementation: partial_compression까지만 남음
surviving intuition: sign-reversal transition / high-z support timing으로 재해석됨
```

## 2. Investigation Path

### 2.1 Exp004: P1의 위치 확인

Exp004는 retained P1이 독립적인 QFUDS physical branch(새 물리 mechanism을
가진 별도 이론 가지)인지 확인했다.

결론:

```text
retained P1 = exact interacting-vacuum instance
generic time-dependent IDE subset under xi(a) = Gamma(a)
```

의미:

- P1은 cosmology literature 밖에 떠 있는 것이 아니었다.
- interacting vacuum / IDE machinery로 비교할 수 있는 형태였다.
- 하지만 이것은 novelty나 physical QFUDS survival이 아니다.
- retained branch의 차이는 model family가 아니라 transfer-shape parameterization이다.

여기서 첫 번째 분리가 생겼다.

```text
P1 closure survival != physical QFUDS survival
```

### 2.2 Exp005: retained timing의 usefulness audit

Exp005는 retained normalized `Gamma(a)` timing profile이 단순 family로
환원되는지 확인했다.

Retained fingerprint(곡선의 핵심 timing 특징):

| Metric | Value |
| --- | ---: |
| peak redshift | `z ~= 2.046` |
| weighted mean redshift | `z ~= 1.746` |
| half-max support | `z ~= 0.259 to 4.632` |
| `z > 10` leakage | `0.000215` |

결론:

```text
potentially_useful_compression_target
```

의미:

- constant/power-law timing은 너무 rigid했다.
- compact smooth pulse는 가깝지만 declared threshold를 통과하지 못했다.
- 8-knot flexible reconstruction은 retained shape를 잘 복원했다.
- retained timing은 physical source가 아니라 IV/IDE timing-prior candidate로만 남았다.

이 시점에서 살아남은 것은 다음 정도였다.

```text
structure-era, low-leakage, finite timing support may be useful as a compression target.
```

### 2.3 Exp006: table-level literature timing support audit

Exp006은 Escamilla 2023 중심의 table-level(논문 표에 공개된 숫자만 쓰는
수준) IV/IDE literature product(문헌에서 바로 쓸 수 있는 표, 그림,
posterior 같은 데이터 산출물)로 retained timing을 검사했다.

결론:

```text
allowed_but_not_informative
```

의미:

- retained weighted mean과 peak region은 Escamilla 제품과 겹쳤다.
- 하지만 constraints(제약 범위)가 broad(너무 넓음), zero-compatible(0과
  구별되지 않음), unconstrained(사실상 제약 안 됨)였다.
- high-z shoulder(큰 redshift 쪽으로 이어지는 support 꼬리)는 table-level
  product로 테스트되지 않았다.
- 따라서 retained timing은 배제되지 않았지만 informative prior(실제로
  정보를 주는 prior)로 승격되지 않았다.

여기서 중요한 반성이 생겼다.

```text
Exp006이 약한 이유가 timing intuition의 실패 때문인지,
아니면 literature coverage가 좁았기 때문인지 분리해야 했다.
```

### 2.4 Coverage Expansion Audit: DESI-era coverage gap 확인

Coverage Expansion Audit(문헌 범위를 넓혀 빠진 target을 찾는 audit)은
Exp006의 literature coverage가 충분한지 확인했다.

결론:

```text
DESI-era nonparametric/sign-switching IV/IDE timing literature가 충분히 반영되지 않았다.
```

가장 중요한 추가 target:

```text
Li & Zhang 2025 DESI DR2 sign-reversal IDE
```

이 audit은 Exp006 결론을 바꾸지 않았다. 대신 다음 질문을 만들었다.

```text
Li & Zhang 2025는 retained timing을 실제로 sharpen할 수 있는가?
```

### 2.5 Li & Zhang 2025 timing analysis

Li & Zhang 2025는 다음 점에서 중요했다.

- 직접 interacting-vacuum energy-transfer form(vacuum-like 성분과
  CDM-like 성분 사이의 에너지 교환식을 명시한 형태)을 사용한다.
- `Q = beta(a) H rho_de` 형태다.
- `beta(z)`(Li & Zhang의 redshift별 coupling function)를 20 bins(20개의
  redshift 구간)로 nonparametric reconstruction(특정 함수꼴을 미리 고정하지
  않고 구간별로 재건)한다.
- DESI DR2, Planck, PP, DESY5, Union3를 사용한다.
- sign reversal과 high-z positive support를 보고한다.
- PCA summary로 data-dominated degrees of freedom을 논한다.

Figure-level analysis에서 확인된 것:

```text
retained weighted mean z ~= 1.746
retained peak z ~= 2.046
Li & Zhang positive beta region: broadly z ~ 1.7-2.1 and beyond
```

해석:

```text
moderate timing-region overlap
```

하지만 이 단계는 아직 compression이 아니었다.

```text
overlap != compression
```

### 2.6 Digitized Compression Audit

Digitized Compression Audit은 `fig_reconstruct`, `fig_bin30`, `fig_zmax`를
digitize(그림에서 curve와 uncertainty band를 수치로 추출)해서 retained
timing과 competing timing families(경쟁하는 간단한 timing 함수꼴들)를
비교했다.

비교 family:

- zero coupling;
- logistic transition;
- Gaussian pulse;
- logistic pulse;
- low-bin tomography;
- retained Exp005 timing.

결론:

```text
partial_compression
```

핵심 metric:

| Representation | Family | UW RMS | Support overlap | High-z capture | Explained vs zero |
| --- | --- | ---: | ---: | ---: | ---: |
| evidence-weighted support | retained | `0.4836` | `0.4056` | `0.6971` | `0.1664` |
| evidence-weighted support | logistic transition | `0.1043` | `0.8118` | `0.8525` | `0.9516` |
| evidence-weighted support | Gaussian pulse | `0.1099` | `0.8200` | `0.8451` | `0.9429` |
| signed history | retained | `0.7733` | `0.4997` | `0.5958` | `-2.2463` |
| signed history | logistic transition | `0.1048` | `0.8008` | `0.8602` | `0.9134` |

해석:

- retained timing은 high-z(큰 redshift, 더 과거) structure-era component
  일부를 잡는다.
- 하지만 Li & Zhang의 full shape(전체 곡선 모양)는 sign-reversal
  transition(부호가 바뀌는 전이형 구조)에 가깝다.
- logistic transition(S자 모양으로 한 상태에서 다른 상태로 넘어가는
  2-parameter 전이 함수)과 Gaussian/pulse families(중심과 폭을 가진
  봉우리형 함수군)가 retained보다 훨씬 효율적으로 reconstruction을 압축했다.
- retained `Gamma(a)`는 leading compression implementation이 아니다.

## 3. What Was Rejected

### 3.1 물리 해석으로서 rejected

다음은 repository evidence 기준으로 rejected 또는 demoted다.

| Claim | Status | 근거 |
| --- | --- | --- |
| retained `Gamma(a)`가 physical QFUDS source다 | rejected for retained branch | Level 1.5 physicality gate |
| retained P1이 known IV/IDE와 구별되는 physical model family다 | rejected | Exp004 exact IV mapping |
| two-phase naming만으로 novelty가 생긴다 | rejected | qfuds_positioning, Exp004 |
| Exp006 table overlap만으로 retained timing이 informative prior다 | rejected | Exp006 `allowed_but_not_informative` |
| Li & Zhang overlap만으로 supported compression target이다 | rejected | Digitized Compression Audit |
| retained `Gamma(a)`가 Li & Zhang reconstruction의 best low-dimensional compressor다 | rejected at digitized evidence level | logistic transition / Gaussian pulse outperform retained |
| retained `Gamma(a)`가 signed sign-reversal history를 설명한다 | rejected | signed-history metrics |

### 3.2 구현으로서 rejected 또는 demoted

| Implementation | Current interpretation |
| --- | --- |
| retained information-production `Gamma(a)` | physical source로는 rejected; timing object로는 partial |
| retained `Gamma(a)` as leading compression family | rejected by digitized audit |
| P1 closure | stable Level 2A phenomenology only |
| P2 regularized fluid closure | failed at retained amplitude |
| Escamilla-only literature coverage | insufficient as fairness check for DESI-era timing |

### 3.3 문서 위치에 대한 판단

Digitized Compression Audit은 `docs/04_results/`에 넣지 않았다.

이유:

- 새 experiment로 선언하지 않았다.
- roadmap status를 바꾸지 않는다.
- Exp004/Exp005/Exp006 classification을 바꾸지 않는다.
- `docs/wiki/research/audits/`의 follow-up audit로 충분하다.

`docs/04_results/`에 넣으려면 별도 experiment spec, result boundary,
decision-log/roadmap handling이 필요하다. 지금 작업은 그 수준이 아니다.

## 4. What Survived

### 4.1 Surviving intuition

가장 중요한 생존 내용:

```text
structure-era timing intuition survived as transition-era IV/IDE timing,
not as the retained Gamma(a) implementation.
```

즉, 살아남은 것은 특정 `Gamma(a)` 곡선이 아니라 다음 직감이다.

```text
dark-sector interaction reconstruction may contain a relevant timing feature
around the structure-formation / DESI-sensitive redshift range.
```

### 4.2 Surviving timing features

살아남은 feature:

- high-z positive support;
- `z ~ 1.7-2.1` 근처의 activity timing;
- DESI DR2 reconstruction에서 보이는 sign-reversal transition;
- low-z negative/zero-compatible branch와 high-z positive branch 사이의 transition timing;
- broader `z ~ 1-2.5` support localization.

덜 살아남은 feature:

- retained `Gamma(a)`의 exact finite-pulse shape;
- retained low-z positive tail;
- retained half-max support 전체를 Li & Zhang의 full history compressor로 쓰는 해석.

### 4.3 Surviving phenomenological content

다음은 여전히 유효하다.

```text
retained P1 is usable as IV/IDE phenomenology.
retained timing is a partial high-z component overlap.
Li & Zhang points more strongly toward sign-reversal transition families.
```

이것은 QFUDS proof가 아니다. 하지만 연구 질문으로는 더 선명해졌다.

## 5. Current Position

### 5.1 retained P1

현재 retained P1의 위치:

```text
exact interacting-vacuum instance
time-dependent IDE subset under xi(a)=Gamma(a)
Level 2A phenomenology only
```

말하면 안 되는 것:

```text
physical QFUDS derivation
novel model family
Level 2B-ready physical branch
```

### 5.2 structure-era timing intuition

현재 structure-era timing intuition의 위치:

```text
not dead
not proven
not retained-Gamma-specific
```

가장 정직한 표현:

```text
The intuition survived as activity/transition timing near the structure-era
redshift range, especially as high-z support and sign-reversal transition
behavior in DESI-era IV/IDE reconstructions.
```

### 5.3 broader QFUDS hypothesis

broader QFUDS hypothesis는 여전히 open이다.

하지만 현재 repository evidence로는 다음이 없다.

- physical source `X`;
- derived `Q^nu`;
- phase-B vacuum-pressure rationale;
- physical `delta Q` route;
- known-model distinction;
- CMB/matter-power/survey-likelihood viability.

따라서 broader QFUDS는 다음 상태다.

```text
open as design-space question
not validated as physical theory
```

## 6. Key Lessons

조사 시작 전과 비교해 바뀐 점:

1. P1의 model family가 모호하지 않게 됐다.
   - 이제 retained P1은 IV/IDE phenomenology로 봐야 한다.

2. retained timing의 역할이 줄었다.
   - Exp005에서는 potential compression target이었다.
   - Li & Zhang digitized audit 후에는 leading implementation이 아니다.

3. overlap과 compression이 분리됐다.
   - `z ~ 1.7-2.1` overlap은 있다.
   - 하지만 compression에서는 logistic transition / simple pulse가 더 강하다.

4. Escamilla-only audit의 한계가 드러났다.
   - Exp006은 valid coarse audit이지만 DESI-era timing literature coverage로는 부족했다.

5. 사용자의 원래 직감은 완전히 죽지 않았다.
   - "구조 형성 시기 근처가 중요할 수 있다"는 intuition은 살아남았다.
   - 다만 "retained `Gamma(a)`가 그 정답이다"는 아니다.

6. 다음 질문이 더 정확해졌다.
   - 이제 질문은 "retained Gamma를 살릴 수 있나?"가 아니다.
   - 질문은 "DESI-era IV/IDE reconstructions가 어떤 low-dimensional timing family를 가리키나?"이다.

## 7. Open Questions

진짜로 남은 질문만 적는다.

1. Li & Zhang의 author-provided numerical histories, covariance, posterior
   samples가 있으면 digitized-audit conclusion이 유지되는가?

2. PCA eigenvectors/eigenvalues를 numerical product로 얻으면 logistic
   transition family가 data-dominated modes에서도 retained보다 우세한가?

3. Silva 2025, Figueruelo 2026 같은 DESI-era sign-switching / IDE targets도
   Li & Zhang처럼 transition timing을 선호하는가?

4. Sign-reversal transition timing이 단순 DESI/BAO/SN reconstruction artifact인지,
   아니면 여러 IV/IDE reconstructions에서 반복되는 phenomenological feature인지?

5. Future physical QFUDS branch가 admission rule을 만족하는 source `X`,
   `Q^nu`, phase-B rationale, `delta Q`, known-model distinction을 실제로 줄 수 있는가?

열린 질문이 아닌 것:

- retained `Gamma(a)`가 physical source인지 여부: retained branch에서는 닫힘.
- retained P1이 IV/IDE인지 여부: Exp004에서 닫힘.
- Exp006 table-level evidence만으로 informative prior인지 여부: 닫힘.

## 8. Recommended Next Directions

| Rank | Direction | Recommendation | 이유 |
| ---: | --- | --- | --- |
| 1 | broader IV/IDE DESI-era coverage | continue | Li & Zhang 하나만으로 family-level conclusion을 일반화하면 안 된다. Silva/Figueruelo 계열이 같은 transition timing을 가리키는지 봐야 한다. |
| 2 | posterior / covariance recovery | continue if products exist | Digitized audit는 강한 hint지만 posterior/covariance가 있어야 redundancy 또는 supported-family conclusion을 세게 말할 수 있다. |
| 3 | continue timing work | continue, but not as retained-Gamma rescue | Timing work의 대상은 retained `Gamma(a)`가 아니라 sign-reversal transition / simple pulse / low-bin family comparison이어야 한다. |
| 4 | archive retained-Gamma implementation as leading candidate | yes, archive as leading candidate | retained `Gamma(a)`는 partial overlap object로 보존하되, leading compression family로 밀면 안 된다. |
| 5 | physical-source work | only after admission ingredients | 지금 timing 결과를 physical source로 역해석하면 Level 1.5를 우회하게 된다. `X`, `Q^nu`, phase-B rationale, `delta Q`, known-model distinction 없이는 금지. |
| 6 | new experiment spec | defer | 데이터 제품 또는 broader DESI-era family comparison question이 더 정리된 뒤에만 의미가 있다. |

추천 한 줄:

```text
Continue timing work only as DESI-era IV/IDE phenomenological family comparison,
not as a retained Gamma(a) rescue program.
```

## 9. Strongest Statements

### 9.1 오늘 repository evidence만으로 할 수 있는 가장 강한 과학적 statement

```text
The retained P1 branch is an interacting-vacuum / time-dependent IDE
phenomenology, and the original structure-era timing intuition survives only
in a narrower form: DESI-era IV/IDE reconstructions, especially Li and Zhang
2025, show timing structure near the retained structure-era redshift range,
but the digitized Li and Zhang reconstruction is better compressed by
sign-reversal transition or simple pulse families than by the retained
Gamma(a) implementation.
```

더 짧게:

```text
The intuition survived as transition-era timing; the retained Gamma(a)
implementation did not survive as the leading compression family.
```

### 9.2 아직 할 수 없는 가장 강한 statement

아직 말하면 안 되는 것:

```text
QFUDS has found a physical dark-matter-to-dark-energy phase-transfer mechanism.
```

또는:

```text
retained Gamma(a) is a supported IV/IDE compression target.
```

또는:

```text
Li and Zhang validates the retained QFUDS timing prior.
```

이 세 문장은 현재 repository evidence로는 모두 과장이다.

## 10. 결론 / 해결

이번 조사의 결론은 "QFUDS가 맞았다"가 아니다.

정확한 결론은 다음이다.

```text
retained Gamma(a)는 구현으로는 밀렸다.
하지만 structure-era timing intuition은 sign-reversal transition timing이라는
더 일반적인 phenomenological question으로 살아남았다.
```

그래서 앞으로의 기본 태도는 다음이어야 한다.

- retained `Gamma(a)`를 구조하지 않는다.
- Level 1.5를 다시 열지 않는다.
- physical branch를 만들지 않는다.
- DESI-era IV/IDE timing family comparison으로만 좁혀서 본다.
- posterior/covariance products가 없으면 강한 classification을 말하지 않는다.

## 11. 재발 방지 / 운영 메모

다음 세션에서 agent가 실수하기 쉬운 지점:

1. `partial_compression`을 `supported_compression_target`처럼 쓰면 안 된다.
2. Li & Zhang overlap을 QFUDS evidence처럼 쓰면 안 된다.
3. retained `Gamma(a)`를 다시 rescue하려고 하면 안 된다.
4. `docs/04_results`에 후속 audit을 넣고 Exp006을 암묵적으로 바꾸면 안 된다.
5. roadmap status는 그대로 roadmap에서만 관리한다.

체크리스트:

```text
Before future timing work:
- Am I comparing families, not rescuing retained Gamma(a)?
- Am I using posterior/covariance or only digitized figure evidence?
- Am I separating overlap from compression?
- Am I avoiding physical-source language?
- Am I leaving roadmap and existing result classifications unchanged unless explicitly instructed?
```

## 12. 타임라인

- Exp004: retained P1을 interacting vacuum / time-dependent IDE로 위치시켰다.
- Exp005: retained timing을 potential compression target으로만 남겼다.
- Exp006: Escamilla table-level literature 기준으로 `allowed_but_not_informative`가 됐다.
- Coverage Expansion Audit: DESI-era timing literature gap을 확인했다.
- Li & Zhang 2025 product search: public numerical products는 못 찾았고, figure-level digitization route를 확보했다.
- Li & Zhang timing analysis: retained timing과 moderate overlap을 확인했다.
- Digitized Compression Audit: retained는 `partial_compression`; logistic transition / Gaussian pulse가 더 강한 compressor임을 확인했다.
- This checkpoint: retained implementation과 surviving timing intuition을 분리했다.

## 부록 A -- 진단 명령어 모음

이 checkpoint를 만들 때 쓴 명령은 단순 문서 열람과 검증 명령이다.

### 관련 파일 찾기

```bash
rtk rg --files docs | rtk rg 'project_identity|qfuds_positioning|success_criteria|roadmap|decision_log|experiment_summary|030_result_004|030_result_005|030_result_006|coverage_expansion|li_2025|digitized_compression'
```

일반적으로 `rg --files`는 repo 파일 목록을 빠르게 뽑고, 뒤의 `rg`는
그 목록에서 필요한 키워드만 거른다. 이 작업에서는 source document가
실제로 어디 있는지 확인했다.

### 결과 문서 읽기

```bash
rtk sed -n '1,260p' docs/04_results/030_result_004_p1_model_family_positioning.md
rtk sed -n '1,260p' docs/04_results/030_result_005_timing_prior_usefulness.md
rtk sed -n '1,260p' docs/04_results/030_result_006_literature_timing_support_audit.md
```

`sed -n '1,260p'`는 파일의 앞 260줄만 읽는다. 긴 문서에서 executive
verdict, scope, decision을 먼저 보기 좋다.

### Project-level SSOT 확인

```bash
rtk sed -n '1,240p' docs/00_project/project_identity.md
rtk sed -n '1,240p' docs/00_project/qfuds_positioning.md
rtk sed -n '1,240p' docs/00_project/success_criteria.md
rtk sed -n '1,260p' docs/05_next_steps/000_roadmap.md
```

이 명령들은 timing 결과를 QFUDS 전체 상태로 과장하지 않기 위해 썼다.
특히 roadmap은 status SSOT라서 반드시 확인해야 한다.

### Digitized audit 결과 확인

```bash
rtk cat outputs/li2025_digitized_compression_audit/li2025_digitized_compression_summary.json
```

`cat`은 작은 파일 전체를 그대로 보여준다. 여기서는
`partial_compression`, `retained_best_count: 0`, best family 정보를 확인했다.

### 검증

```bash
rtk python3 scripts/validate_docs.py
rtk python3 scripts/research_consistency.py
rtk git diff --check
```

첫 번째는 문서 frontmatter/schema 검증이다. 두 번째는 roadmap/decision
consistency를 확인한다. 세 번째는 whitespace error를 잡는다.

이런 부류의 문제는 보통 다음 순서로 푼다.

```text
status SSOT 확인 -> result verdict 확인 -> audit evidence 확인 -> synthesis 작성 -> validators 실행
```
