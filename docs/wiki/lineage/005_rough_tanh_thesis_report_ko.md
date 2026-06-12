---
doc_id: qfuds_lineage_rough_tanh_thesis_report_ko
title: "통합 암흑 부문의 거친 tanh 상전이 현상론: 효과적 적합성, 반증 가능 신호, 그리고 이론적 천장의 체계적 지도화"
doc_type: summary
stage: reference
status: reference
evidence_role: provenance
depends_on:
  - roadmap
  - qfuds_lineage_rough_tanh_numerical_sketch_ko
next_gate: provenance only; roadmap이 상태 권위; observer mode 유지; 050 천장 무손상
last_updated: 2026-06-12
---

# 통합 암흑 부문의 거친 tanh 상전이 현상론: 효과적 적합성, 반증 가능 신호, 그리고 이론적 천장의 체계적 지도화

**A rough tanh phase-transition phenomenology of a unified dark sector: effective fit, falsifiable signatures, and a systematic mapping of the theoretical ceiling**

---

> **문서 성격 (반드시 먼저 읽을 것).** 이 보고서는 QFUDS(Quantum Foam Unified Dark
> Sector) 프로젝트의 `004 rough tanh` lineage 기록(provenance)에서 파생된 **학술
> 보고서 초안**이다. 새로운 검증 증거를 주장하지 않으며, 프로젝트 로드맵 상태·050
> 천장·observer mode를 바꾸지 않는다. 본문의 모든 수치 모델은 **거친 프록시(rough
> proxy)**이고, 엄밀한 검증은 Boltzmann 코드(CLASS/hi_class) 수준에서만 가능하며 현
> 단계에서는 미수행(blocked)이다. 이 보고서의 학술적 기여는 *"새 우주론의 발견"이
> 아니라*, **하나의 거친 통합 암흑부문 가설이 데이터에 어디까지 맞고 어디서 왜
> 막히는지를 체계적으로 지도화하고, 차세대 관측이 검증할 반증 가능 신호를 도출한
> 것**이다.

---

## 초록 (Abstract)

표준 우주론 ΛCDM은 정밀하지만 두 가지 긴장(S8 구조성장 진폭, H0 허블 상수)과
근본적 미설명(암흑물질의 정체, 암흑에너지의 우주상수 문제)을 안고 있다. 본 연구는
"암흑물질과 암흑에너지를 하나의 유체가 우주 전성기(z≈2) 부근의 상전이로 대신한다"는
가장 거친 통합 암흑부문 아이디어를, 손으로 그린 상태방정식 `w(a)=tanh` 한 줄에서
출발해 **곡선으로 끝까지 밀어** 그 도달 한계를 정량화했다.

세 가지를 확인했다. (1) **효과적 수준**에서, 보통 물질을 분리한 변형(V2)은 배경
팽창을 초신성으로 ΛCDM과 구별 불가능하게 재현하고, 작은 유효 음속(c_eff²≈10⁻⁵)을
도입하면 S8를 관측값으로 끌어내릴 수 있다. 그러나 이 적합은 ΛCDM 대비 우월하지 않고
(승리는 S8를 낮춘 보편적 효과일 뿐), H0 긴장은 오히려 악화된다. (2) 이 모델은
ΛCDM과 **갈라지는 반증 가능 신호 셋**을 남긴다: 약중력렌즈 물질 파워 스펙트럼의
스케일 의존 계단(k_J≈0.1 Mpc⁻¹), 후기 ISW의 스케일 의존 기울기, 그리고 스케일에
따라 흐르는 성장지수 γ_eff(k). 대표 Euclid급 토모그래픽 예측에서 이 계단은 ~24σ로
검출 가능하다. (3) **근본적 수준**에서, 데이터가 요구하는 파라미터를 미시 거품
구조에서 *유도*하려는 시도는 막힌다. 데이터가 선호하는 상관길이는 ξ≈10 Mpc(미시
거품이 아니라 거대구조 스케일)이고, 전이 시점은 임계밀도 ρ*≈ρ_Λ를 요구한다. 이
두 숫자를 메커니즘으로 brute-force 적합하면 튜닝은 *줄지 않고 위치만 옮겨가며*,
결국 둘은 **계층/스케일 문제**와 **우주상수 문제** 그 자체로 환원된다. 즉 이 가설의
이론적 천장은 이론물리학의 두 미해결 난제와 동일하며, 이는 이 가설 고유의 실패가
아니라 모든 동역학적 암흑에너지 모델이 공유하는 벽이다.

방법론적으로, 본 연구는 인식론적 규율을 강제하는 **자기교정 AI 에이전트 하베스트**
위에서 24개 원자적 체크포인트로 수행됐다. 이 하베스트는 (i) 운영 워크플로 SSOT
(`.agent/workflows/`)가 *연구 산출물이 상태 권위를 오염시키지 못하도록* 라우팅·전파·
금지 규칙을 강제하는 표준 인프라와, (ii) 세션 단위의 병렬 fan-out·적대적 검증·결정론적
게이트라는 실행 패턴으로 구성된다. 이 인프라가 가짜 돌파를 구조적으로 차단해, 투기적
가설을 끝까지 밀면서도 정직한 결론에 도달하게 한 점이 본 연구의 두 번째 기여다.

**키워드:** 통합 암흑 부문, 동역학적 암흑에너지, S8 긴장, 약중력렌즈, 반증 가능성,
일반화 암흑물질(GDM), 우주상수 문제, AI 연구 하베스트.

---

## 1. 서론 (Introduction)

### 1.1 동기

ΛCDM은 우주배경복사, 바리온 음향 진동, 거대구조, 중력렌즈를 130억 년에 걸쳐 정밀하게
설명한다. 그러나 두 가지 관측적 긴장이 누적되고 있다.

- **S8 긴장**: 후기 우주 약중력렌즈가 측정한 구조성장 진폭 S8 = σ8·√(Ω_m/0.3)이
  CMB가 예측하는 값보다 낮다.
- **H0 긴장**: 국소 거리사다리(≈73)와 CMB 추론값(≈67.4)이 ~8% 어긋난다.

동시에 ΛCDM은 두 성분(암흑물질, 암흑에너지)을 *손으로 삽입*한다. 암흑물질의 입자
정체는 40년 직접탐색에도 미발견이고, 암흑에너지를 진공에너지로 해석하면 양자장론
예측이 관측보다 ~10¹²⁰배 크다(우주상수 문제).

이 배경에서 자연스러운 질문이 있다. **"암흑물질과 암흑에너지를 하나의 매질이 상전이로
대신한다"는 가장 거친 통합 아이디어를 실제로 코드로 밀면 ΛCDM 대비 어디까지 가는가?**
본 연구는 이 질문에 *말 대신 곡선으로* 답한다.

### 1.2 연구 설계와 방법론적 원칙

본 연구는 24개의 체크포인트(CP)로 구성된 append-only 탐색 로그로 수행됐다. 각 CP는
하나의 독립 스크립트, 그림(png/svg), 수치 결과(csv)를 남긴다. 두 가지 방법론적 원칙을
엄격히 지켰다.

1. **표준 우주론식은 직접 유도·검산 후 사용**한다(배경 E(z), 선형 성장, 거리, S8).
   근사는 모두 "프록시"로 명시한다.
2. **parametrize와 derive를 구분**한다. 손으로 값을 깔고 곡선을 맞추는 것
   (parametrize)과 미시구조에서 값이 나오는 것(derive)은 다르다. 본 연구의 핵심
   결론은 이 구분 위에 선다.

전체 토대는 "이 모든 것은 거친 프록시이고 진짜 검증은 CLASS이며 현재 blocked"라는
정직한 caveat 위에 놓인다.

---

## 2. 모델과 방법 (Model and Methods)

### 2.1 상태방정식 파라미터화

통합 암흑유체의 상태방정식을 우주 전성기 부근에서 매끄럽게 전환하는 tanh로 둔다.

```
w(a) = ½(w_f − w_i)·tanh((a − a_tr)/Δa) + ½(w_i + w_f),   w_i=0, w_f=−1, a_tr=0.33 (z≈2)
```

전이 *이전*(고적색편이)에는 w≈0으로 차가운 암흑물질처럼 군집하고, *이후*(후기)에는
w≈−1로 진공압처럼 가속을 만든다. 모델 전체가 이 네 손잡이 {a_tr, Δa, w_i, w_f}다.

두 가지 실현을 비교했다.

- **V1 (통합)**: 하나의 유체(Ω≈0.95)가 암흑물질+암흑에너지를 모두 대신.
- **V2 (DE-only 전이)**: 보통 물질(Ω_m=0.315)은 분리해 a⁻³로 두고, 암흑에너지
  성분만 w:0→−1 전이.

배경 팽창은 Friedmann 방정식에서 직접 유도했다:

```
E(a) = H(a)/H0 = √( Ω_b a⁻³ + Ω_r a⁻⁴ + ρ_X(a)/ρ_crit ),
ρ_X(a) = Ω_X0 · exp(−3∫₁ᵃ (1+w)/a' da')
```

### 2.2 상태변수 동역학과 밀도 구동 (CP2–CP3)

손으로 그린 w(a)를 한 단계 끌어올려, 상태변수 φ가 이중우물 자유에너지 안에서
이완하는 동역학(`dφ/dN = −M ∂F/∂φ`)에서 w_eff(a)=−φ가 *출력*으로 나오게 했다.
이로써 지연(lag), super-cooling 실패영역, 이력(hysteresis) 같은 검증 가능한
부수효과가 따라온다. 나아가 전이 구동항을 물질밀도가 임계밀도를 넘는 정도
(h(a) ∝ ρ_m/ρ* − 1)에 묶어, 전이 시점을 임의 입력이 아니라 임계밀도 하나에서
유도되도록 좁혔다.

### 2.3 섭동과 구조 성장

선형 성장은 e-folds N=ln a에서 `D'' + (2 + dlnE/dN)D' − (3/2)Ω_clust D = 0`로
풀었다. 음속 있는 암흑성분의 군집 억제는 Jeans 프록시
η(k,a)=1/(1+(c_s c k/aH)²)로 모형화하고, 이를 결합 2-유체 섭동계(Ma–Bertschinger
준정적 sub-horizon, 4변수)와 대조해 프록시 정확도를 검증했다.

**프록시 한계의 명시.** 2-유체 검증에서 η 프록시는 정성적으로 옳으나(스텝 위치,
극한 거동) 정량적으로 약 10–20% 어긋난다. 따라서 본문의 모든 토이 수치는 *경향과
자릿수*로만 읽어야 하며, 정밀값은 Boltzmann 코드를 요구한다.

### 2.4 연구 인프라: 자기교정 AI 에이전트 하베스트 (Self-correcting agent harness)

본 연구의 24개 체크포인트는 단일 연구자가 손으로 돌린 것이 아니라, **인식론적 규율을
강제하는 AI 에이전트 하베스트(harness)** 위에서 수행됐다. 투기적 가설을 끝까지 밀면서도
과대주장으로 미끄러지지 않게 한 것은 이 인프라이며, 따라서 그 자체로 본 연구의 방법론적
기여다. 인프라는 **두 층**으로 구성된다: 표준으로 존재하는 *운영 거버넌스 SSOT*와,
매 세션에서 도는 *실행 패턴*이다.

#### (A) 운영 워크플로 SSOT: `.agent/workflows/`

연구가 문서·데이터·문헌·자산·산출물에 손을 대는 *반복 가능한 절차*는 모두
`.agent/workflows/`의 워크플로를 먼저 조회하고 따라야 한다. 채팅 기록이나 도구 메모리는
권위가 아니다. **워크플로 디렉터리가 단일 진실 원천(SSOT)**이다. 이 거버넌스가
강제하는 네 규칙이 관측자 모드(observer mode)를 *구조적으로* 지킨다.

1. **기능 기반 라우팅**(routing by function): "주제가 비슷한 곳"이 아니라 "그 문서의
   *역할*이 있는 곳"에 둔다. 예: 자산 산출물은 `research/assets/`, 그 산출물이 무엇을
   바꾸는지의 판단은 `research/investigations/.../conclusions/`, 가지 분류 변화는
   가지 관계가 *실제로* 바뀐 뒤에만 `lineage/`.
2. **상태 경계**(status boundary): 연구 산출물이 *존재한다는 이유만으로* roadmap·
   decision log·실험 결과·governance·lineage를 갱신하지 않는다. 각 문서는 *자신이
   소유한 주장*이 바뀔 때만 갱신된다.
3. **전파 규칙**(propagation): 각 연구 이벤트(새 문헌 요약, 캐시 자산, 수치 digitization,
   실행 결과 등)에 대해 *즉시 갱신할 것*과 *조건 충족 시에만 갱신할 것*을 표로 고정.
4. **금지 단축**(forbidden shortcuts): 연구 산출물로 "QFUDS 지지", 후보 `X`, `δQ`,
   "Level 2B 적격", "로드맵 전진", "known-model 구별"을 *주장하지 않는다*. 책임
   문서 유형이 실제로 그 증거를 공급하지 않는 한 말이다. 충돌 시 더 보수적인 규칙을 따르고
   audit/postmortem에 기록한다.

요지: **자산 산출물 상태는 물리적 적격 상태가 아니다**(예: 특정 그림의 CSV가 존재해도
물리-QFUDS Level 2B는 blocked로 남는다). 이 SSOT가 "현상론 곡선이 검증된 물리로
승격되는" 미끄러짐을 디렉터리·인덱스·게이트 차원에서 차단한다.

#### (B) 세션 실행 패턴: 병렬·적대적·결정론적

위 거버넌스 안에서 한 연구 세션은 다음 패턴으로 돈다.

- **Append-only provenance + 원자적 커밋.** 각 CP는 독립 스크립트 + 그림(png/svg) +
  수치(csv) + 문서 섹션을 **원자적 커밋 하나**로 묶고(1 CP = 1 commit), 이전 결론을
  덮지 않고 아래로 쌓는다.
- **병렬 fan-out + 직렬 통합.** 서로 독립인 계산(ISW, kill-test, 점성, γ 지문, 천장
  메커니즘 둘 등)은 다수 하위 에이전트로 *병렬 spawn*되고, 공유 자원(문서 append,
  CP 번호, git)은 충돌·번호 경합을 피하려 메인 에이전트가 *직렬*로 통합한다.
  연관성 순서가 필요한 부분만 직렬화하는 것이다.
- **적대적 검증(비대칭).** 모든 *positive* 주장(줄였다·유도했다·통과했다)은 커밋 전에
  적대적 에이전트의 반박을 거친다. 실제 catch 셋: (i) 천장 분해 초안의 ξ 사다리가
  미시 쪽으로 편향된 것을 red-team이 인과/Kibble 지평(거시 horn)을 빠뜨렸다고 지적해
  양면 교정. (ii) tracker attractor의 "진짜 부분 승리"를 적분기가 해석적 상태방정식
  w_φ=−2/(α+2)을 재현하는지 독립 재실행으로 검증. (iii) 우주상수 문제를 *환각 최대
  위험 지점*으로 분류해 "유도했다" 결과가 나오면 즉시 가짜로 플래그하도록 가드 강제.
  부정/제자리 결과는 안전 방향이라 라이트 검증, *긍정 주장만 빡세게* 검증한다.
- **인식론적 가드레일 4종.** (1) parametrize ≠ derive, (2) brute-force hit ≠
  derivation(출력은 "맞췄냐"가 아니라 *튜닝 장부*), (3) representative ≠ likelihood
  (외부 관측 숫자는 대표값/예시; 실제 데이터·공분산 적재는 observer mode 위반), (4)
  rough proxy(진짜 검증은 CLASS).
- **결정론적 게이트.** 매 커밋은 `validate_docs.py`·`research_consistency.py`·
  pre-commit 훅을 통과해야 한다(전 24 CP 통과). 이 게이트가 *로드맵 SSOT*, *미성숙
  완료 주장 금지*, *문서 인덱스 정합성*을 자동 강제한다.

요컨대 이 하베스트는 **"가짜 돌파가 조용히 살아남을 수 없도록"** 설계됐다. 표준
거버넌스(A)가 산출물의 상태 승격을 막고, 세션 실행(B)이 긍정 주장을 적대적 검증·
결정론적 게이트로 거른다. 본 연구가 투기적 가설을 24 CP에 걸쳐 끝까지 밀면서도
§6.2의 정직한 결론(*이것은 증거가 아니다*)에 도달할 수 있었던 것은 물리적 분석만큼이나
이 인프라 덕분이다. *자기교정이 내장된 AI 연구 하베스트가 과대주장 없는 투기적 탐색을
가능하게 한다*는 점이, 물리 결과와 나란히 놓이는 본 연구의 두 번째 기여다.

---

## 3. 효과적 수준의 결과: 배경과 구조성장 (CP1, CP3–CP8)

### 3.1 배경은 초신성으로 ΛCDM과 구별 불가

![배경 팽창: V1은 초기우주에서 깨지고 V2는 ΛCDM과 거리지수 차이 <0.02 mag](assets/004_rough_tanh/fig_background.png)

V1 통합 실현은 단일 정규화로 두 역할을 한 유체에 넣어 초기우주 물질량을 눌러 z>2에서
팽창이 ΛCDM의 절반이 되어 즉시 깨진다. 반면 V2는 z=5에서도 E비 1.03이고, 거리지수
차이가 전 구간 |Δμ| < 0.02 mag로 **초신성 산포(~0.05 mag) 안에 숨는다.** 밀도구동
모델로 다시 배경을 먹여도 max|Δμ|=0.017 mag로 일관되게 닫힌다. 즉 *배경만으로는 이
모델을 죽일 수 없다.*

### 3.2 S8 오버슈트는 구조적이며, c_eff²로 치료 가능하지만 튜닝이다

![성장/S8: 전이 모양을 바꿔도 S8 오버슈트는 그대로 = 구조적](assets/004_rough_tanh/fig_cp4_growth.png)

V2는 구조성장을 약 19% 억제해 S8를 0.83→0.67로 *과하게* 낮춘다(관측 ~0.76 아래로
오버슈트). 전이 모양(매끄러운 tanh vs 가파른 지연)을 바꿔도 오버슈트는 줄지 않는다.
즉 오버슈트의 원인은 전이 *모양*이 아니라, 전이 성분이 얼마나 매끄럽게(군집 안 하고)
변하느냐, 곧 유효 음속 c_eff²다.

![c_eff² 스캔: S8=0.76은 c_eff²≈3×10⁻⁵에서 달성](assets/004_rough_tanh/fig_cp5_sound_speed.png)

c_eff²를 0~1 사이로 열면 S8가 0.677(매끄러움)~0.955(완전 군집) 사이를 매끄럽게
움직이고, **관측 S8=0.76은 c_eff²≈3×10⁻⁵에서 달성된다.** 즉 오버슈트는 치명적이
아니라 고칠 수 있다. 단 그 대가는 *아주 작은 음속이라는 손잡이를 하나 더 손으로
맞추는 것*이다.

### 3.3 도출 시도: dial한 c_eff²는 비-거품 스케일을 숨긴다

![c_eff² 도출: fit값 4.6×10⁻⁶ ↔ 상관길이 ξ≈10 Mpc = 거대구조 스케일](assets/004_rough_tanh/fig_cp8_ceff2_derivation.png)

c_eff²를 자유값이 아니라 order parameter의 상관길이 ξ에서 유도하려 했다
(c_eff ≈ ξ/d_H). 데이터가 원하는 c_eff²≈4.6×10⁻⁶은 **ξ≈10 Mpc, 곧 우주 거대구조
스케일에 대응한다.** 그런데 "양자 거품" 전제는 ξ가 미시적이어야 하고, 미시 거품이면
c_eff²→0 → S8≈0.95로 오히려 *틀린 방향*(높게)으로 간다. 즉 자연스러운 거품
상관길이는 fit을 만들지 못한다. 이것이 첫 번째 천장 신호다.

### 3.4 H0 긴장은 풀리지 않고 악화된다

![H0 테스트: inverse distance ladder로 66.18, −1.81% (악화)](assets/004_rough_tanh/fig_cp10_h0_test.png)

역거리사다리(r_s·θ* 고정)로 H0를 추론하면 H0_QFUDS = 66.18, 즉 **−1.81%**. 긴장을
닫으려면 +8.3%가 필요한데 오히려 반대로 멀어진다. 이유는 명료하다: S8는 *섭동*
손잡이(c_eff²)라 배경과 독립이라 건드릴 수 있었지만, H0는 *배경* 양이고 그 배경은
초신성에 못박혀(§3.1) 움직일 여지가 없다. H0를 풀려면 재결합 이전(r_s)을 바꿔야
하는데, 늦은 z≈2 전이는 거길 건드리지 않는다. **S8와 H0 레버는 분리돼 있고, 이
모델은 S8만 닿는다.**

### 3.5 brute-force 적합과 그 정직한 해석

격자 brute-force 적합은 명목상 ΛCDM을 정보기준(AIC)으로 이기는 지점에 도달한다
(χ²_tot 18→8). 그러나 이 승리는 전적으로 S8를 낮춘 덕이고, **S8를 낮추는 어떤
모델이든 똑같이 이긴다**. QFUDS 고유의 승리가 아니다. 더해 best-fit의
c_eff²=4.6×10⁻⁶은 §3.3의 fine-tune이며, 분석 자체가 거칠다(프록시, 공분산 없음).
정직한 결론: *"데이터에 맞출 수 있다"를 넘어 "명목상 이길 수도 있다"까지 가지만,
그것은 튜닝의 힘이지 새 물리도 우월성도 아니다.*

---

## 4. 반증 가능 신호: 모델이 ΛCDM과 갈라지는 곳 (CP9, CP13, CP16, CP14, CP17–CP19)

배경·BAO로는 구별 불가하므로, 모델의 과학적 가치는 *갈라지는* 관측 신호에 있다.

### 4.1 약중력렌즈 P(k)의 스케일 의존 계단

![렌즈 P(k): k_J≈0.1에서 스케일 의존 계단 vs 균일 저-σ8은 평평](assets/004_rough_tanh/fig_cp9_lensing_pk.png)

음속 있는 암흑성분은 Jeans 스케일 k_J≈1/ξ *아래*에서만 군집하고 *위*에선 매끄럽다.
이는 P(k)를 **스케일 의존적으로** 억제한다. 데이터-fit ξ≈10 Mpc면 그 계단이 k≈0.1
Mpc⁻¹로, 약중력렌즈 감도 정중앙에 온다. 결정적으로 이것은 단순히 σ8를 균일하게 낮춘
ΛCDM(모든 k에서 평평한 억제)과 *질적으로 다르다.* 이 계단은 균일 저-σ8이 위조할 수
없는 깨끗한 반증 신호다.

### 4.2 후기 ISW의 스케일 의존 기울기

![ISW: C_ℓ 비가 0.35→0.82로 기울어짐 vs 균일 저-σ8은 flat 0.857](assets/004_rough_tanh/fig_cp13_isw.png)

세 번째 채널로 후기 CMB(적분 Sachs–Wolfe)를 쳤다. QFUDS의 ISW는 부호는 ΛCDM과
같으나(양의 ISW–galaxy 교차, 뒤집힘 없음) 진폭이 낮고, 핵심은 *모양*이다: C_ℓ
비가 저-ℓ에서 0.35, 고-ℓ에서 0.82로 **기울어진다.** 균일 저-σ8(모든 ℓ에서 0.857)과
원리적으로 구별된다. 단 ISW가 사는 저-ℓ는 cosmic variance가 커서 검출 자체는
별개의 문제임을 명시한다.

### 4.3 성장지수 γ의 스케일 의존성

![γ 지문: 단일 스케일 f(R)와 축퇴, 그러나 γ_eff(k) running으로 구별](assets/004_rough_tanh/fig_cp16_growth_index.png)

성장률 f=Ω_m^γ의 유효 지수를 환산하면, S8 스케일(k=0.2)에서 γ_eff(z=0)≈0.48로 수정
중력 f(R)(0.42)과 *단일 스케일에서는 축퇴*된다. 그러나 γ_eff는 k에 따라 0.22→0.55로
강하게 *흐른다*(Δγ≈0.33). 진짜 수정중력은 선형 스케일에서 γ가 거의 무관하므로, 이
**running 자체가 QFUDS를 f(R)/DGP와 구별하는 단서**다.

### 4.4 실제 오차로의 채점과 내부 정합성

![kill test: w(z) freezing은 대표 DESI에서 반대 사분면, P(k) 스텝은 Stage-IV 사정권](assets/004_rough_tanh/fig_cp14_kill_test.png)

두 신호를 대표 오차로 채점했다(외부 숫자는 모두 *대표값/예시*이며 likelihood가 아님을
명시). w(z)를 CPL (w0,wa)로 투영하면 우리 모델은 동결(freezing, wa>0)로, 대표 DESI가
선호하는 해동(thawing)과 *정반대 사분면*에 놓인다. 한편 P(k) 계단은 진폭을 주변화한
뒤에도 대표 Stage-IV 설정에서 ~18σ의 모양 신호로 남고, 균일 이동은 0σ(sanity).

![CMB렌즈 내부정합: 늦은 유체라 z>1 가중 CMB렌즈를 거의 안 건드림](assets/004_rough_tanh/fig_cp17_cmb_lensing.png)

중요한 내부 정합성 검증: S8를 낮춘 그 c_eff²가 ACT급 CMB렌즈(ΛCDM과 일치)를
과억제해 모순을 일으키지 않는가? 답은 *아니오*다. 약중력렌즈는 z~0.3, CMB렌즈는
가중치 91%가 z>1이라, z<1에 몰린 우리 성장 변형이 CMB렌즈를 거의 건드리지 않는다.
이 모델은 "늦은 유체"라는 성질 덕에 두 렌즈 사이 바늘귀를 통과한다(H0 실패와는 반대
결과).

![DESI z>2 Lyα: D_H/r_d는 대표 정밀도 경계선, 가장 가까운 손잡이](assets/004_rough_tanh/fig_cp18_desi_highz_bao.png)

CP14가 freezing 신호는 z≳2에서만 산다는 점을 보였고, DESI DR2가 정밀해진 곳이 바로
그 z>2(Lyα)다. r_d는 재결합 이전이 ΛCDM과 동일하므로 공유되고, 거리비 차이는 오직
후기 E(z)에서 온다. z_eff=2.33에서 D_M/r_d는 −0.10%(숨음), D_H/r_d는
−1.06%(대표 ±1.1% 경계선)로, 가장 강한 곳에서도 아직 죽이긴 어렵지만 D_H/r_d가 가장
가까운 손잡이다.

![Euclid forecast: P(k) 스텝 다중-bin ~24σ, γ running ~24σ로 구별](assets/004_rough_tanh/fig_cp19_euclid_forecast.png)

대표 Euclid급 토모그래픽 약중력렌즈 Fisher 예측에서, 진폭을 bin별로 주변화한 뒤에도
P(k) 계단은 **~24σ**, γ_eff(k) running은 상수-γ 수정중력과 **~24σ**로 구별된다.
균일 진폭 이동은 0σ(sanity 통과). 즉 이 모델의 반증 가능 신호는 차세대 관측의
사정권에 있다.

---

## 5. 이론적 위치와 천장 (CP11–CP12, CP15, CP20–CP24)

### 5.1 기존 유체/EFT 이론 안에서의 좌표

![유체/EFT 위치: GDM(c_vis²=0) 특수경우 + 강하게 비표준인 k-essence](assets/004_rough_tanh/fig_cp12_fluid_frameworks.png)

이 토이를 기존 지도 위에 위치시키면 좌표가 명료하다. (i) **GDM**(Hu 1998)에서 세
함수 {w(a), c_eff², c_vis²} 중 점성 c_vis²=0인 특수경우. (ii) **EFT of Dark
Energy**에서 braiding 없는 minimal k-essence(pure-α_K) 구석. (iii) **k-essence**
비표준성 N_X ≡ 2X·P_XX/P_X = 1/c_s²−1 ≈ 2×10⁵로, canonical 스칼라에서 약 5자릿수
떨어진 극단적 비표준 운동항을 요구한다. 별도로 점성 c_vis²를 열면(CP15) c_eff²와
독립적인 S8/P(k) 손잡이가 *하나 더* 생긴다(천장 재확인). 이 모든 좌표는 parametrize
이지 derive가 아니다.

### 5.2 천장의 분해: 두 고전 난제

![050 천장 직격: 스펙 3개 → 스케일 문제 + 코인시던스 문제](assets/004_rough_tanh/fig_cp20_ceiling_derivation.png)

데이터가 요구하는 스펙 {ξ≈10 Mpc, N_X≈2×10⁵, z*~2}를 Ginzburg–Landau order
parameter ansatz에서 *유도 시도*하면, 셋이 두 고전 문제로 분해된다.

- **스케일 문제**: ξ≈10 Mpc은 미시 거품(너무 작음)에도, z~2 인과/Kibble
  지평(~4400 Mpc 공변, 461배 큼)에도 자연스럽지 않다. 그것이 일치하는 유일한
  스케일은 비선형/σ8 구조 스케일(R8≈12 Mpc)인데, 이는 표준 물리가 정하는 값이라
  재현해도 독립 증거력이 0이다(매칭≠유도). N_X는 ξ로 환원되어 둘은 사실 하나다.
- **코인시던스 문제**: 전이가 관측 가능하려면 임계밀도 ρ*가 ρ_Λ의 ~3 order 안
  (전체 ~120 order 중)에 앉아야 한다. 바로 why-now 문제 그 자체다.

> *방법론 주석:* 본 절의 초안은 ξ 스케일 사다리를 미시 쪽으로만 제시하는 편향이
> 있었고, 적대적 교차검토(adversarial review)가 인과/Kibble 지평이라는 거시 horn을
> 빠뜨렸음을 지적해 양면(too-small / too-big)으로 교정했다. 결론은 같으나 더
> 정직하고 강해졌다. 이 자기교정 절차 자체를 기록으로 남긴다(§2.4 참조).

### 5.3 brute-force 메커니즘: 튜닝은 줄지 않고 옮겨간다

![ξ 근임계/Kibble-Zurek: 칼날 튜닝, relocated not reduced](assets/004_rough_tanh/fig_cp21_xi_criticality.png)

천장의 두 숫자를 메커니즘으로 brute-force 적합하면 어떻게 되는가? **ξ**(근임계
ξ~|T−Tc|⁻ν 또는 Kibble–Zurek 동결)는 맞출 수 있으나, Planck 척도에서 출발하면
임계점 근접도 ε를 10⁻⁵⁹~10⁻¹¹⁷까지, 또는 quench 비율을 10¹¹⁶~10²³³까지 *칼날같이*
공급해야 한다. 손잡이 개수는 줄지 않고 ε/τ_Q로 *옮겨가며*, "왜 2차 상전이점
근처인가"라는 메타튜닝까지 더해진다. **relocated, not reduced.**

![coincidence tracker: IC 튜닝은 16 decade 진짜 제거, meV는 잔존](assets/004_rough_tanh/fig_cp22_coincidence_tracker.png)

**코인시던스**(tracker quintessence, Ratra–Peebles)는 다르다. 초기조건 φ_i를 19
decade에 걸쳐 훑으면 약 **15.7 decade**가 같은 attractor로 빨려들어 Ω_DE(0)=0.685에
착지한다. 초기조건 튜닝이 *실제로* 사라지는 것이다(적분기가 tracker 상태방정식
w_φ=−2/(α+2)=−0.667을 재현해 검증됨). 이것은 본 연구 전체에서 **유일하게 진짜인 부분
승리**다. 그러나 에너지 스케일 M_eff가 관측 창에 들려면 M_eff∈[1.71,3.50] meV(0.31
decade)로 여전히 손으로 맞춰야 한다. 튜닝 장부는 2개{초기조건, 스케일} → 1개{스케일}로
*부분* 환원될 뿐, why-now는 풀리지 않는다.

### 5.4 최심층: 두 숫자는 곧 이론물리의 두 난제

![meV = 우주상수 문제: anthropic은 select, transmutation은 작음만 natural](assets/004_rough_tanh/fig_cp23_cc_problem.png)

남은 두 숫자를 정면으로 보면 정체가 드러난다. **meV 스케일**은 우주상수 문제 그
자체다. 순진한 진공에너지는 관측 ρ_Λ보다 10¹²³(Planck)/10⁵⁹(TeV)배 크다. 알려진
공략은 모두 *유도가 아니다*: Weinberg anthropic 천장은 관측값을 천장 바로 아래로
"선택"할 뿐(landscape로 이전), 차원전환은 *작음 그 자체*만 technically natural하게
만들 뿐(O(1) 결합이 input으로 남고, 진공에너지 문제 자체는 미해결), SUSY/sequestering/
swampland는 모두 relocate한다.

![ξ = σ8 스케일: circular, 차원전환은 relocate, 독립 유도 후보 없음](assets/004_rough_tanh/fig_cp24_scale_problem.png)

**10 Mpc 스케일**은 표준 물리가 정하는 비선형/σ8 스케일(R8≈11.9 Mpc)이다. 1/k_eq
(~95 Mpc), r_d(~147 Mpc), z~2 지평(~4400 Mpc)은 전부 크기가 맞지 않는다. 차원전환은
튜닝을 결합상수로 relocate할 뿐(10⁵⁸ 길이 튜닝을 ~0.26% 결합 튜닝으로 줄이는 부분
점수는 인정하되, 10 Mpc를 *고르지는* 못함), 암흑유체 Jeans 길이는 c_eff²로 만들어
구성상 일치하므로 circular다. **암흑 부문에서 10 Mpc를 독립 유도하는 후보는 없으며,
이 모델은 표준 계층/스케일 문제를 그대로 상속한다.**

---

## 6. 논의 (Discussion)

### 6.1 효과적 수준 대 근본적 수준

이 연구의 결과는 두 레벨에서 정반대로 읽힌다. *효과적* 수준(파라미터를 입력으로
가정)에서 모델은 작동한다: 배경·S8·CMB렌즈·BAO를 통과한다. 그러나 이는 ΛCDM도 하는
일(Λ를 입력으로 가정)이라 우월성을 주지 않으며, 파라미터를 더 쓰고 H0는 악화시키므로
경제성에서 진다. *근본적* 수준(미시구조에서 유도)에서 모델은 막힌다. 바로 이것이
이 가설("Q=quantum foam"의 유도 야망)의 정체성이자 천장이다. "10 Mpc를 가정으로
깔면 된다"는 진술은 효과적 레벨을 택한다는 뜻이며, 정당하지만 그 선택의 대가(증거력
상실, 경제성 손실, 유도 야망의 포기)를 동반한다.

### 6.2 무엇이 증거인가

이 가설의 천장이 이론물리의 두 난제(우주상수+계층)와 동일하다는 사실은 *이 가설을
지지하는 증거가 아니다.* 증거는 경쟁 이론들 사이를 *구별*해야 하는데, 모든 동역학적
암흑에너지 모델이 같은 두 난제를 상속하므로, 그 공유된 벽은 어느 모델도 편들지
못한다. 이 가설이 증거를 얻을 수 있는 유일한 자리는 ΛCDM과 *갈라지는* 곳, 곧 §4의
반증 가능 신호(P(k) 계단, ISW 기울기, γ running)다.

### 6.3 한계의 명시

- 모든 토이는 거친 프록시다. Jeans-η 성장은 full 2-유체와 10–20% 어긋난다.
- 외부 관측 숫자(DESI, ACT, Euclid 정밀도)는 *대표값/예시*로만 사용했고, 실제
  데이터 벡터·공분산·likelihood는 사용하지 않았다. 따라서 본문의 σ 값은 *자릿수
  감*이며, 진짜 채점은 CLASS likelihood를 요구한다.
- foam 미시구조에서 어떤 파라미터도 유도되지 않았다(parametrize-not-derive).

---

## 7. 결론 (Conclusion)

거친 통합 암흑부문 tanh 가설을 곡선으로 끝까지 밀어 다음을 정량화했다.

1. **간다**: 보통 물질을 분리한 변형(V2)은 배경을 ΛCDM과 구별 불가하게 재현하고,
   작은 음속으로 S8를 관측값에 맞춘다.
2. **그러나 낫지 않다**: 명목상 AIC 승리는 S8를 낮춘 보편 효과이고, H0는 악화되며,
   필요한 음속은 fine-tune이다.
3. **세 반증 신호를 남긴다**: P(k) 스케일 의존 계단(k≈0.1), ISW 스케일 의존 기울기,
   γ_eff(k) running. Euclid급 토모그래피에서 ~24σ로 검출 가능.
4. **천장은 두 고전 난제다**: 데이터가 요구하는 ξ≈10 Mpc(스케일 문제)과 ρ*≈ρ_Λ
   (우주상수/코인시던스 문제). 메커니즘으로 brute-force 적합하면 튜닝은 위치만
   옮겨가며(코인시던스의 초기조건 부분만 진짜로 부분 환원), 둘 다 미해결로 남는다.

핵심 기여는 둘이다. **물리적으로**, 하나의 거친 가설을 효과적 적합성·반증 가능성·
이론적 천장의 세 축에서 체계적으로 지도화하고, 그 천장이 가설 고유의 실패가 아니라
모든 동역학적 암흑에너지가 공유하는 이론물리의 두 난제임을 정량적으로 보였다.
**방법론적으로**, 운영 워크플로 SSOT(거버넌스)와 병렬·적대적·결정론적 실행 패턴을
결합한 자기교정 AI 연구 하베스트가, 투기적 가설을 끝까지 밀면서도 가짜 돌파를 구조적
으로 차단하고 정직한 결론에 도달하게 함을 실증했다. 다음 단계는 둘로 명확하다:
(a) 2026년 Euclid 우주론 자료와 DESI 후속이 §4의 반증 신호를 검증, (b) 천장의 두
숫자에 대한 원리적 유도다. 이는 우주상수 문제에 직접 들어가는 일이다.

---

## 부록 A: 체크포인트–결과 대응표

| CP | 주제 | 핵심 결과 | 그림 |
| --- | --- | --- | --- |
| CP1 | 배경/성장/위상 | V2 배경 SNe-불가구별, S8 오버슈트, DESI 방향 반대 | `fig_background/growth/phase` |
| CP2 | 상태변수 동역학 | w가 출력, lag·super-cooling·hysteresis | `fig_state_variable` |
| CP3 | 밀도 구동 | 전이 시점 임계밀도서 유도, z*≈5→z_obs≈2 | `fig_density_driven` |
| CP4 | 성장/S8 | 오버슈트는 전이 모양 무관 = 구조적 | `fig_cp4_growth` |
| CP5 | c_eff² 스캔 | S8=0.76 @ c_eff²≈3×10⁻⁵ (튜닝) | `fig_cp5_sound_speed` |
| CP6 | 천장+반증 | 손잡이 5→5, 킬러=DESI w(z) | `fig_cp6a/cp6b` |
| CP7 | brute-force | 명목 AIC 승리, 단 S8 prior 덕 | `fig_cp7_brute_fit` |
| CP8 | c_eff² 도출 | fit값=ξ≈10 Mpc(비-거품 스케일) | `fig_cp8_ceff2_derivation` |
| CP9 | 렌즈 P(k) | k_J≈0.1 스케일 의존 계단 | `fig_cp9_lensing_pk` |
| CP10 | H0 | 66.18, −1.81% (악화) | `fig_cp10_h0_test` |
| CP11 | 2-유체 검증 | η 프록시 정성 OK, 정량 10–20% off | `fig_cp11_two_fluid` |
| CP12 | 유체/EFT 위치 | GDM(c_vis²=0)+비표준 k-essence(N_X≈2e5) | `fig_cp12_fluid_frameworks` |
| CP13 | 후기 ISW | C_ℓ 비 tilt 0.35→0.82, 구별 가능 | `fig_cp13_isw` |
| CP14 | 실오차 채점 | freezing 반대 사분면, P(k) ~18σ | `fig_cp14_kill_test` |
| CP15 | 점성 c_vis² | 독립 손잡이, 천장 재확인 | `fig_cp15_viscosity` |
| CP16 | 성장지수 γ | f(R) 단일 축퇴, running으로 구별 | `fig_cp16_growth_index` |
| CP17 | CMB렌즈 정합 | tension 없음(늦은 유체) | `fig_cp17_cmb_lensing` |
| CP18 | DESI z>2 | D_H/r_d −1.06% (경계선) | `fig_cp18_desi_highz_bao` |
| CP19 | Euclid forecast | P(k) ~24σ, γ running ~24σ | `fig_cp19_euclid_forecast` |
| CP20 | 천장 직격 | 스케일+코인시던스 문제로 분해 | `fig_cp20_ceiling_derivation` |
| CP21 | ξ brute-force | relocated(ε=10⁻⁵⁹~⁻¹¹⁷) | `fig_cp21_xi_criticality` |
| CP22 | coincidence tracker | IC 16 decade 부분환원, meV 잔존 | `fig_cp22_coincidence_tracker` |
| CP23 | meV=우주상수 문제 | 아무도 derive 못 함 | `fig_cp23_cc_problem` |
| CP24 | ξ=σ8 스케일 | circular, 독립 유도 없음 | `fig_cp24_scale_problem` |
| CP25 | "덜 본 것" 직관 학계 위치 | S1·S2·S3 모두 학계 이미 답사 → lineage 자연 닫힘 | (수치 없음, 문헌) |

## 부록 B: 재현 (Reproducibility)

모든 결과는 `docs/wiki/lineage/assets/004_rough_tanh/`의 독립 스크립트로 재현된다.
의존성: numpy(≥2.4, `np.trapezoid`), scipy, matplotlib. 각 스크립트는 그림(png+svg)과
수치(csv)를 남기며, 표준 우주론식은 코드 내에서 직접 유도·assert로 검산된다. 전체
실행 목록은 [004 수치 스케치](004_rough_tanh_numerical_sketch_ko.md)의 '재현' 절을 참조.

```bash
cd docs/wiki/lineage/assets/004_rough_tanh
python3 model.py                 # 공유 모델 smoke test
python3 cp9_lensing_pk.py        # 반증 신호 #1 (P(k) 계단)
python3 cp13_isw.py              # 반증 신호 #3 (ISW)
python3 cp19_euclid_forecast.py  # Euclid forecast
python3 cp20_ceiling_derivation.py  # 천장 분해
python3 cp22_coincidence_tracker.py # tracker attractor (부분 승리)
```

## 부록 C: 연구 하베스트 운영 SSOT

본 연구의 인프라(§2.4)는 `.agent/workflows/`에 운영 SSOT로 문서화돼 있다.

| 워크플로 | 역할 |
| --- | --- |
| `documentation-folder-routing-workflow.md` | 기능 기반 문서 라우팅 + 상태 경계 + 금지 단축 |
| `wiki-maintenance-workflow.md` | wiki 인덱스·레코드 유지 |
| `research-asset-product-workflow.md` | 외부 논문·자산·산출물 가용성 처리 |
| `research-asset-digitization-workflow.md` | 캐시 자산 → Markdown/CSV digitization |
| `research-investigation-result-routing-workflow.md` | assets/plans/conclusions 라우팅 |

세션 단위 회고는 `docs/wiki/postmortem/`에 원자적으로 기록된다(본 연구 세션:
`010-...-rough-tanh-lineage-descent-retro.md`).

## 참고 개념 및 문헌 (대표)

- Hu, W. (1998), *Generalized Dark Matter*, astro-ph/9801234. 세 함수 {w, c_eff², c_vis²} 도입.
- Armendariz-Picon, Mukhanov, Steinhardt (2000), *k-essence*. c_s² = P_X/(P_X+2X P_XX).
- Ratra & Peebles (1988); Steinhardt, Zlatev, Wang (1999). tracker quintessence.
- Weinberg, S. (1987), *Anthropic bound on the cosmological constant*, PRL 59, 2607.
- Ma & Bertschinger (1995). 결합 유체 섭동.
- DESI DR2 BAO (2025); ACT DR6 CMB lensing; Euclid Q1 (2025). 대표 관측 맥락(인용,
  likelihood 미사용).

> 본 보고서의 모든 수치는 거친 프록시이며, 엄밀한 검증은 Boltzmann 코드(CLASS/hi_class)
> 수준에서 수행되어야 한다. 현 단계에서 그 검증은 미수행(blocked)이다.
