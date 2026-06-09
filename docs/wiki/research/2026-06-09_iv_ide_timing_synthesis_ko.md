---
doc_id: synthesis_2026_06_09_iv_ide_timing_ko
title: "IV/IDE 타이밍 조사 한국어 요약"
doc_type: summary
stage: reference
status: completed
evidence_role: audit
depends_on:
  - result_004_p1_model_family_positioning
  - result_005_timing_prior_usefulness
  - result_006_literature_timing_support_audit
  - audit_2026_06_09_exp006_coverage_expansion
  - audit_2026_06_09_li_2025_digitized_compression
next_gate: no roadmap change; use as Korean handoff summary only
last_updated: 2026-06-09
record_type: korean_synthesis
---

# IV/IDE 타이밍 조사 한국어 요약

이 문서는 최근 IV/IDE(interacting vacuum / interacting dark energy;
암흑물질 같은 성분과 암흑에너지 같은 성분 사이의 에너지 교환을 허용하는
모형군) timing 조사의 한국어 handoff summary(다음 세션이 바로 이어받기
위한 요약)다. 새 실험이 아니며, roadmap status(현재 프로젝트 진행 상태)나
Exp004, Exp005, Exp006 결론을 바꾸지 않는다.

## 한 줄 결론

```text
구조 형성 시기 직감은 완전히 죽지 않았지만,
retained Gamma(a)(QFUDS repo에서 쓰던 transfer timing function; 어느
시기에 phase A에서 phase B로 transfer가 강한지 나타내는 곡선) 구현은
Li & Zhang reconstruction(관측 데이터로부터 coupling history를 되짚어
추정한 결과)을 가장 잘 압축하는 family(간단한 함수꼴 묶음)가 아니었다.
```

더 정확히는:

```text
살아남은 것은 retained Gamma(a) 곡선이 아니라
structure-era transition timing intuition(구조 형성 시기 근처에서
interaction이 켜지거나 부호가 바뀔 수 있다는 timing 직감)이다.
```

## 무엇을 확인하려고 했나

처음 질문은 단순했다.

```text
내가 구조 형성 시기 근처를 의심한 게 완전 헛소리였나?
```

repository 언어로 바꾸면 다음 질문이었다.

```text
retained P1(Exp003 이후 살아남은 phase-A-frame interacting-vacuum closure;
phase A를 암흑물질처럼 clustering하는 성분으로 두고 phase B를
vacuum-like 성분으로 둔 perturbation prescription) / retained Gamma(a)가
실제 IV/IDE timing literature와 비교 가능한 phenomenological content
(미시적 원인 유도는 없지만 관측/문헌과 비교할 수 있는 effective model
내용)를 갖고 있는가?
```

아래 표는 다시 읽을 때 쓰는 용어표다. 본문에서는 중요한 용어가 처음
나올 때 괄호로 한 번 더 풀어쓴다.

| 용어 | 풀어쓴 의미 |
| --- | --- |
| `z` redshift | 우주의 과거 시점을 나타내는 좌표처럼 쓰인다. `z`가 클수록 더 과거다. 여기서 중요한 `z ~ 1.7-2.1`은 구조 형성이 활발해진 시기 근처다. |
| scale factor `a` | 우주 크기를 나타내는 변수. `a = 1 / (1 + z)`라서 `z`와 같은 시간 정보를 다른 방식으로 쓴 것이다. |
| `Gamma(a)` | QFUDS repo 안에서 쓴 transfer timing function. 어느 cosmic time에 phase A에서 phase B로 transfer가 강한지 나타내는 phenomenological profile이다. |
| `beta(z)` | Li & Zhang 논문이 reconstruction한 interacting dark energy coupling function. `beta(z)`가 positive/negative인지, zero와 compatible한지가 timing feature다. |
| IV/IDE | interacting vacuum / interacting dark energy. Dark matter-like component와 dark energy-like component 사이에 energy exchange를 허용하는 known model family다. |
| phenomenology | 미시적 원인은 아직 모른 채, effective equation이나 curve를 놓고 관측/문헌과 비교하는 단계다. "원리 증명"이 아니라 "측정 가능한 모양의 테스트"에 가깝다. |
| compression | 20-bin 같은 자유로운 reconstruction을 더 적은 parameter나 더 단순한 function family로 얼마나 잘 요약하는지 보는 것. 단순히 겹치는 것보다 강한 조건이다. |
| sign reversal | Coupling의 부호가 cosmic time에 따라 바뀌는 것. Li & Zhang에서는 low-z 쪽 negative/zero-compatible branch와 high-z positive branch가 이어지는 transition처럼 보인다. |
| posterior/covariance | Reconstruction의 불확실성 정보. Mean curve만 보면 "그럴듯한 모양"이고, posterior/covariance까지 있어야 그 모양이 데이터가 얼마나 강하게 요구한 것인지 말할 수 있다. |

이 질문은 조사 중에 세 개로 쪼개졌다.

| 질문 | 현재 답 |
| --- | --- |
| P1은 어떤 model family인가? | interacting vacuum / time-dependent IDE |
| retained timing은 쓸모 있는 compression target인가? | potential에서 시작했지만, Li & Zhang 기준으로는 partial only |
| 구조 형성 시기 intuition은 살아남았나? | yes, but as transition timing, not retained Gamma(a) |

## 조사 흐름

### Exp004

Retained P1(Exp003 이후 살아남은 phase-A-frame interacting-vacuum
closure)은 다음으로 정리됐다.

```text
exact interacting-vacuum instance
time-dependent IDE subset under xi(a)=Gamma(a)
```

이건 좋은 소식과 나쁜 소식을 동시에 준다.

- 좋은 점: P1은 cosmology literature(기존 우주론 문헌)와 비교 가능한
  형태다.
- 나쁜 점: P1 자체는 새로운 physical QFUDS branch(새 물리 mechanism으로
  인정할 수 있는 이론 가지)가 아니다.

### Exp005

Retained `Gamma(a)` timing은 다음 fingerprint(곡선의 핵심 timing 특징)를
갖는다.

| Metric | Value |
| --- | ---: |
| peak redshift | `z ~= 2.046` |
| weighted mean redshift | `z ~= 1.746` |
| half-max support | `z ~= 0.259 to 4.632` |

Exp005 결론:

```text
potentially_useful_compression_target
```

즉, retained timing은 physical source가 아니라 IV/IDE timing history를
압축할 수 있는지 시험해볼 candidate였다.

### Exp006

Escamilla 2023 table-level product(논문 표에 공개된 숫자만 쓰는 수준의
문헌 데이터 산출물)와 비교했다.

결론:

```text
allowed_but_not_informative
```

겹치기는 했지만, table constraints(표에 있는 제약 범위)가 broad(너무
넓음)하거나 zero-compatible(0과 구별되지 않음)이거나 unconstrained(사실상
제약 안 됨)였다. 그래서 retained timing을 informative prior(실제로 정보를
주는 prior)로 쓰기에는 부족했다.

### Coverage Expansion

Exp006 이후 핵심 반문이 생겼다.

```text
Escamilla만 보고 끝내도 되나?
DESI-era nonparametric / sign-switching IDE literature를 충분히 봤나?
```

Coverage expansion(문헌 범위를 넓혀 빠진 target을 찾는 audit) 결과,
Li & Zhang 2025가 가장 중요한 missing target(아직 제대로 비교하지 않은
우선순위 문헌)으로 올라왔다.

### Li & Zhang 2025

Li & Zhang은 `Q = beta(a) H rho_de` 형태의 DESI DR2 sign-reversal
IDE reconstruction(DESI DR2 데이터를 포함해 coupling의 부호가 cosmic
time에 따라 바뀌는지 재건한 interacting dark energy 분석)이다.

중요한 점:

- `beta(z)`(Li & Zhang의 redshift별 coupling function)를 20 bins(20개의
  redshift 구간)로 reconstruction한다.
- mean `beta(z)`가 low-z에서 negative 또는 zero-compatible이고,
  high-z에서 positive로 간다.
- `z ~ 1.7-2.1` 부근이 retained weighted mean / peak와 겹친다.

여기까지는 좋은 결과였다.

```text
overlap은 있다.
```

하지만 여기서 멈추면 안 됐다.

```text
overlap != compression
```

### Digitized Compression Audit

Figure-level digitization(논문 그림에서 curve와 uncertainty band를 수치로
추출하는 작업)으로 retained timing과 competing timing families(경쟁하는
간단한 timing 함수꼴들)를 비교했다.

비교 family:

- logistic transition;
- Gaussian pulse;
- logistic pulse;
- low-bin tomography;
- retained Exp005 timing.

결론:

```text
partial_compression
```

핵심 수치:

| Family | UW RMS | Support overlap | High-z capture | Explained vs zero |
| --- | ---: | ---: | ---: | ---: |
| retained Gamma(a) | `0.4836` | `0.4056` | `0.6971` | `0.1664` |
| logistic transition | `0.1043` | `0.8118` | `0.8525` | `0.9516` |
| Gaussian pulse | `0.1099` | `0.8200` | `0.8451` | `0.9429` |

즉:

```text
retained Gamma(a)는 high-z component 일부를 잡지만,
Li & Zhang reconstruction 전체 timing structure는 logistic transition /
simple pulse family가 훨씬 잘 압축한다.
```

## 버린 것

이번 조사로 버린 해석:

- retained `Gamma(a)`가 physical QFUDS source라는 해석;
- retained P1이 IV/IDE와 구별되는 new physical family라는 해석;
- Escamilla table overlap만으로 retained timing이 informative prior라는 해석;
- Li & Zhang overlap만으로 retained timing이 supported compression target이라는 해석;
- retained `Gamma(a)`가 Li & Zhang의 best low-dimensional compressor라는 해석.

특히 마지막이 중요하다.

```text
retained Gamma(a)를 살리려고 하면 안 된다.
```

## 살아남은 것

살아남은 intuition:

```text
dark-sector interaction timing may matter around the structure-era / DESI-sensitive redshift range.
```

살아남은 feature:

- `z ~ 1.7-2.1` 근처의 activity timing;
- high-z positive support;
- low-z negative/zero-compatible branch에서 high-z positive branch로 넘어가는 transition timing;
- sign-reversal IV/IDE family와의 관련성.

살아남지 못한 feature:

- retained `Gamma(a)`의 exact finite-pulse shape;
- retained low-z positive tail;
- retained `Gamma(a)`를 leading compression prior로 쓰는 해석.

## 현재 위치

현재 repository evidence 기준:

```text
retained P1 = IV/IDE phenomenology
retained Gamma(a) = partial high-z component overlap
structure-era intuition = transition timing으로 재해석
broader QFUDS = physical theory로 검증되지 않음
```

이 문장은 가능하다.

```text
Li & Zhang 2025는 구조 형성 시기 근처의 IV/IDE timing feature가
현대 DESI-era reconstruction에서도 비교 가능한 질문임을 보여준다.
```

하지만 이 문장은 아직 불가능하다.

```text
Li & Zhang 2025가 retained Gamma(a) 또는 QFUDS를 검증했다.
```

## 다음에 뭘 해야 하나

우선순위는 다음이다.

1. DESI-era IV/IDE timing coverage를 더 넓힌다.
   - Silva 2025, Figueruelo 2026 등에서 sign-switching / transition timing이 반복되는지 확인한다.

2. Li & Zhang posterior/covariance/numerical products를 찾거나 요청한다.
   - digitized figure evidence보다 강한 classification을 하려면 필요하다.

3. Timing work를 계속하되 retained `Gamma(a)` rescue로 하지 않는다.
   - 질문은 이제 "retained Gamma가 맞나?"가 아니다.
   - 질문은 "DESI-era IV/IDE가 어떤 low-dimensional timing family를 가리키나?"이다.

4. Physical-source work는 admission rule 없이는 시작하지 않는다.
   - `X`, `Q^nu`, phase-B rationale, `delta Q`, known-model distinction 없이는 Level 1.5를 다시 열면 안 된다.

## 세션 리셋용 문장

다음 세션이 이 문서만 읽고 시작한다면 이 문장만 기억하면 된다.

```text
QFUDS retained branch는 물리 이론으로 살아난 게 아니다.
하지만 구조 형성 시기 timing intuition은 DESI-era IV/IDE sign-reversal
transition family라는 더 일반적인 phenomenological question으로 살아남았다.
retained Gamma(a)는 그 intuition의 첫 구현이었지만, 현재 best compressor는 아니다.
```
