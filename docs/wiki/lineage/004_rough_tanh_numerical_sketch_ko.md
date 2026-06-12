---
doc_id: qfuds_lineage_rough_tanh_numerical_sketch_ko
title: QFUDS rough tanh 수치 스케치 - 대충 때려박으면 어디까지 가나
doc_type: summary
stage: reference
status: reference
evidence_role: provenance
depends_on:
  - roadmap
  - qfuds_research_flow_plain_language_ko
next_gate: provenance only; roadmap이 상태 권위; observer mode 유지
last_updated: 2026-06-12
---

# QFUDS rough tanh 수치 스케치 - 대충 때려박으면 어디까지 가나

## 상태 경계

이 문서는 provenance(연구 흐름 기록)다. 새 실험 결과가 아니고, QFUDS가 맞다는
주장도 아니며, 로드맵 상태를 바꾸지 않는다. observer mode는 그대로 유지된다.
현재 상태와 공식 판단은
[QFUDS Research Roadmap](../../05_next_steps/000_roadmap.md)이 정한다.

여기 담긴 곡선은 검증 증거가 아니라 **탐색용 스케치**다. 손으로 그린 현상론
파라미터화일 뿐, foam sector 미시구조에서 유도한 것이 하나도 없다. 읽는 사람은
이 문서를 "rough한 아이디어를 말 대신 곡선으로 한 번 밀어본 기록"으로만 받아들여야
한다.

## 무엇을 한 것인가

Notion 메모 "새로운 시도와 관점"에서 나온 가장 거친 아이디어를 그대로 코드로
밀어봤다. 그 아이디어는 이거였다.

```text
쉬운 비유
-> 물처럼 하나의 재료가 z~=2 근처에서 모습을 바꾼다
원래 과학 용어
-> 통합 암흑 유체의 상태방정식 w(a)가 0에서 -1로 매끄럽게 전환(tanh)
지금 레포에서의 의미
-> retained timing hook(z~=2)의 가장 단순한 수치 실현을 ΛCDM과 비교
```

질문은 하나였다. **이 rough 모델을 실제로 때려박으면 ΛCDM 대비 어디까지 가나?**

코드와 그림은 [`assets/004_rough_tanh/`](assets/004_rough_tanh/)에 있다.
`model.py`가 공유 계약서(파라미터, w(a), H(a))이고, `background.py`,
`growth.py`, `phase.py`가 각각 배경팽창, 구조성장, 위상 초상화를 계산한다.

> 이 문서는 **append 로그**다. 각 체크포인트(CP)는 이전 것을 덮어쓰지 않고 아래로
> 쌓인다. 결론도 체크포인트별로 따로 둬서, 결과가 발전해 가는 과정을 그대로
> 보존한다.

## CP1 (2026-06-12): rough tanh - 배경 / 성장 / 위상

## 모델 한 줄

```text
w(a) = tanh로 0(암흑물질처럼) -> -1(진공압처럼), 전환 중심 a_tr=0.33 (z~=2)
```

두 가지로 실현해 봤다.

- V1 통합(unified): 하나의 유체가 암흑물질 + 암흑에너지를 모두 대신함.
- V2 DE-only: 보통 물질은 그대로 두고, 암흑에너지 성분만 전환함.

## 세 가지 발견

| 축 | 발견 | 판정 |
| --- | --- | --- |
| 배경팽창 | V1은 z=5에서 H가 ΛCDM의 약 절반(E비 0.51). V2는 z=5에서 1.03이고 거리지수 차이가 전 구간 0.018 mag 미만(초신성 산포 ~0.05 mag 이내) | V1은 초기우주에서 즉시 깨짐. V2 배경은 초신성으로 ΛCDM과 구별 불가 |
| 구조성장(S8) | V2가 성장을 약 19% 억제. sigma8 0.81 -> 0.66, S8 0.83 -> 0.67 | 방향은 메모 주장대로 S8를 낮춤. 다만 관측이 원하는 ~0.76보다 더 내려가 과도하게 오버슈트 |
| 위상(DESI 비교) | QFUDS tanh는 w가 0 -> -1(시간이 갈수록 더 음으로, freezing). DESI w0wa 중심값은 w가 약 -1.7 -> -0.7(thawing). z=2에서 각각 -0.53 vs -1.37 | 부호와 메커니즘이 정반대 regime. 메모가 기대한 "DESI와 일치"는 성립 안 함 |

그림: [`fig_background.png`](assets/004_rough_tanh/fig_background.png),
[`fig_growth.png`](assets/004_rough_tanh/fig_growth.png),
[`fig_phase.png`](assets/004_rough_tanh/fig_phase.png).

## 그래서 어디까지 가나

간다. rough한 V2는 배경팽창을 ΛCDM 수준으로 재현하고(초신성으로 못 깸), 구조성장
S8를 관측이 원하는 방향(아래)으로 움직인다. 즉 *"z~=2 전환으로 S8를 건드리는
현상론 모델"* 까지는 실제로 도달한다. 곡선으로 확인됐다.

그리고 멈춘다. 벽은 세 개다.

1. naive 통합(V1)은 그냥 깨진다. 단일 정규화로 두 역할을 한 유체에 넣으면 초기우주
   물질량이 눌려 z>2에서 팽창이 ΛCDM의 절반이 된다. 살리려면 물질을 따로 빼야
   하는데(V2), 그 순간 "통합"이라는 맛이 빠진다.
2. S8 오버슈트는 "맞췄다"가 아니라 자유 파라미터(a_tr, Δa)가 손에 쥐어져 있다는
   뜻이다. 숫자가 그럴듯해도 넣은 만큼 나온 것이지 예측이 아니다.
3. 메모가 가장 기대했던 외부 지지(DESI evolving-w)가 부호와 메커니즘 모두 반대였다.
   타이밍 직관이 기댈 곳 하나가 사라졌다.

## 천장의 정체

세 결과를 관통하는 한 줄은 이미 레포가 내린 판단과 같다.

```text
이 모든 건 현상론이다. foam sector에서 유도한 것이 하나도 없다.
```

w(a)=tanh(...)는 손으로 그린 곡선이고, a_tr=0.33을 z=2에 맞춘 것도 입력이다.
[049 Level 2B 적격성 검토](../research/investigations/source_x/conclusions/049_level2b_eligibility_review_and_observer_mode.md)와
[050 foam-sector-to-Gamma 유도 가능성](../research/investigations/source_x/conclusions/050_foam_sector_to_gamma_derivation_feasibility_result.md)가
말한 "상태변수와 최소 수식 객체 부재"가 여기서도 그대로 살아 있다. 곡선은 데이터를
흉내낼 수 있어도 foam에서 암흑이 창발한다는 근본 주장은 건드리지 못한다. 이 스케치는
그 천장을 곡선으로 재확인한 것이다.

DESI 비교는 로드맵의 생존 hook(`w0 ~= -1`, `|wa| > 0`, `z ~= 2` 부근 timing peak)에
실질적 단서를 하나 더한다. naive tanh 실현은 `w0 ~= -1`은 맞지만 진화 방향이 DESI가
선호하는 thawing과 반대다. 즉 retained timing을 데이터와 맞추려면 단순 0 -> -1 전환
이상의 무언가가 필요하다는 점을 보여준다. 이것은 외부 관측 추적 대상이지
in-repository 유도 대상이 아니다.

### CP1 결론 (2026-06-12)

```text
rough하게 때려박으면: z~=2 전환형 현상론 우주론 한 편의 출발점까지는 간다.
거기서 멈춘다: 상태변수가 없어서 곡선맞춤을 넘지 못한다.
덤으로 알게 된 것: naive 0->-1 전환은 DESI evolving-w와 방향이 반대다.
```

## CP2 (2026-06-12): 상태변수를 방정식으로 굴리기

다음 질문은 자연스러웠다. "w(a)를 손으로 그리지 말고, 상태변수 하나에서
*나오게* 할 수 있나?" 이것이 049/050이 말한 "최소 수식 객체"의 형태다.

거품을 매질로 보면 식은 정해진다. 나비에-스토크스를 문자 그대로 역산하는 것은
backward diffusion이라 ill-posed지만, 그 직감("매질 = 이완하는 장")을 살리면 상전이
order parameter가 자유에너지 안에서 이완하는 동역학이 된다.

```text
상태변수 φ            (0 = A상/암흑물질, 1 = B상/암흑에너지)
이중우물 자유에너지   F(φ, a) + z~=2에서 부호 뒤집는 tilt h(a)
이완 방정식           dφ/dN = -M ∂F/∂φ   (N = ln a)
나오는 것             w_eff(a) = -φ(a)   (손으로 그리지 않음)
```

실제로 돌려보니([`state_variable.py`](assets/004_rough_tanh/state_variable.py),
[`fig_state_variable.png`](assets/004_rough_tanh/fig_state_variable.png)),
맨 tanh가 못 하는 세 가지가 나왔다.

| 발견 | 의미 |
| --- | --- |
| w(a)가 입력이 아니라 출력이 됨 | φ가 방정식을 따라 굴러서 w가 결과로 나온다. 손그림 곡선에서 한 칸 올라간 형태 |
| 일반적 지연(lag) | trigger(tilt)를 z=2에 둬도 실제 전이는 z<1로 늦게 완성된다. 손그림 tanh가 숨겼던 결합 |
| super-cooling 실패 영역 | 장벽이 높으면 φ가 false vacuum에 갇혀 오늘까지 암흑에너지가 안 생긴다. "전이를 완성해야 한다"는 구조적 제약 |

특히 지연(②)이 실질적이다. 관측이 원하는 "전이 z~=2"를 얻으려면 미시 trigger를
z=2보다 더 일찍 두고 mobility를 맞춰야 한다. tanh는 이 결합을 z=2에 손으로 박아
숨겼던 것이다. 부수적으로 lag와 hysteresis는 이완동역학의 비가역성, 즉 시간
화살표가 방정식에 내장된 형태로 나타난다.

천장은 그대로다. 자의성을 한 칸 내렸을 뿐이다. 전에는 w(a)=tanh를 손으로 그렸고,
이제는 F(φ,a)와 구동항 h(a)를 손으로 그린다. 대신 손잡이가 물리적으로 해석되고
(장벽=잠열, M=이완률, h=구동) 검증가능한 신호(lag, super-cooling, hysteresis)가
따라온다. 진짜 050 천장(h(a)를 foam 미시구조에서 유도하는 것)은 넘지 않았지만,
"곡선 한 개"에서 "방정식 + 검증가능한 부수효과"로 한 칸 올라간 것은 맞다.

다음 굴착은 h(a)를 임의 함수에서 실제 물리량(물질밀도 `rho_m(a)`)에 연동해
trigger 적색편이를 자의적 입력이 아니라 임계밀도 하나에서 유도하는 방향이다.

### CP2 결론 (2026-06-12)

```text
상태변수 φ를 자유에너지 안에서 굴리면 w가 출력으로 나온다 (더 이상 손으로 안 그림).
부수효과: 지연(lag), super-cooling 실패영역, hysteresis - 모두 검증가능.
형태는 CP1보다 한 칸 올라가지만, 천장(h(a)를 foam에서 유도)은 그대로.
다음(CP3): h(a)를 물질밀도 rho_m(a)에 연동해 trigger를 임계밀도에서 유도한다.
```

## CP3 (2026-06-12): 전이를 물질밀도 rho_m(a)로 구동

CP2의 tilt h(a)는 아직 손으로 그린 함수였다. CP3은 그걸 **실제 물리량**에 묶었다.
거품이 빽빽하면(초기) 뭉치는 A상이 유리하고, 묽으면(후기) 진공압 B상이 유리하다.
그래서 tilt를 물질밀도가 임계밀도 `rho*`를 얼마나 넘는지로 정의했다.

```text
h(a) = lambda * ( rho_m(a)/rho* - 1 ) = lambda * ( (a*/a)^3 - 1 )
a* = 1/(1+z*) : rho_m = rho* 가 되는 시점
```

이제 위치 손잡이가 `{a_tr, Δa}` 임의 한 쌍에서 **물리적 임계밀도 하나(z*로 표현)**로
줄었다. 전이 시점은 손으로 박는 입력이 아니라 임계밀도에서 유도되고, 거기에 CP2의
지연이 얹힌다.

trigger z* 를 바꿔가며 실제 관측 전이(w=-0.5)가 어디 찍히는지 본 결과
([`density_driven.py`](assets/004_rough_tanh/density_driven.py),
[`fig_density_driven.png`](assets/004_rough_tanh/fig_density_driven.png)):

| trigger z* (임계밀도) | 관측 전이 z_obs | 지연 Δz | w(z=0) |
| --- | --- | --- | --- |
| 2.0 | 0.53 | 1.47 | -1.000 |
| 3.0 | 1.04 | 1.96 | -1.000 |
| 4.0 | 1.55 | 2.45 | -1.000 |
| 5.0 | 2.05 | 2.95 | -1.000 |

두 가지가 나왔다.

1. retained hook인 **관측 전이 z~=2를 얻으려면 임계밀도가 z*~=5에 있어야 한다.** 즉
   거품은 z~=5(훨씬 빽빽한 시점)에 "전이 결정"을 내리지만, 이완 지연 때문에 눈에
   보이는 전이는 z~=2로 늦어진다. 맨 tanh는 이 결합을 z=2에 손으로 박아 숨겼다.
2. 그렇게 튜닝한 밀도구동 w(a)를 다시 배경에 먹여도 거리지수가 ΛCDM과
   `max|Δμ| = 0.017 mag (< 0.05)` 로 **여전히 초신성으로 구별 불가**다. CP1의 V2
   결과와 일관되게 닫힌다.

천장은 그대로다. z*는 이제 물리적이지만 `rho*` 자체(왜 그 임계밀도냐)와 장벽·이완률은
여전히 선택값이다. 다만 "왜 z~=2냐"라는 질문이 "왜 임계밀도가 z*~=5에 대응하냐"라는
더 물리적인 질문으로 바뀌었다. 이것이 050 천장을 향해 한 칸 더 좁힌 지점이다.

### CP3 결론 (2026-06-12)

```text
전이를 임계밀도 하나로 구동하면 trigger 시점이 유도된다 (임의 입력 제거).
관측 전이 z~=2를 보려면 임계밀도가 z*~=5에 있어야 한다 (지연 Δz~=3).
배경은 여전히 ΛCDM과 SNe로 구별 불가 (max|Δμ|=0.017).
남은 천장: rho*(왜 그 밀도냐) + 장벽 + 이완률은 아직 선택값. 050 그대로.
```

## CP4 (2026-06-12): 밀도구동 모델로 성장 / S8 루프 닫기

CP1에서 hand-tanh V2가 S8를 0.83 -> 0.67로 약 19% 과하게 낮춘 걸 봤다. CP3의
밀도구동 모델은 관측 전이는 같은 z~=2지만 모양이 다르다(z*=5 트리거 + 지연으로 더
가파르고 늦게 완성). 그래서 물었다. **모양을 바꾸면 오버슈트가 줄어드나?**

세 배경(ΛCDM / CP1 hand-tanh / CP3 밀도구동)에 같은 군집물질 Ω_m0=0.315로 선형
성장을 풀었다([`cp4_growth.py`](assets/004_rough_tanh/cp4_growth.py),
[`fig_cp4_growth.png`](assets/004_rough_tanh/fig_cp4_growth.png)).

| 모델 | D(1)/D_ΛCDM | sigma8 | S8 | ΔS8 |
| --- | --- | --- | --- | --- |
| ΛCDM | 1.000 | 0.810 | 0.830 | — |
| CP1 hand-tanh V2 | 0.812 | 0.658 | 0.674 | -18.8% |
| CP3 밀도구동 | 0.816 | 0.661 | 0.677 | -18.4% |

**거의 차이가 없다.** 성장곡선도 fσ8도 CP1과 CP3가 겹친다. 즉 전이 모양(매끄러운
tanh vs 가파른 지연)을 바꿔도 S8 오버슈트는 안 줄어든다. 둘 다 관측 S8~=0.76보다
한참 아래인 0.68로 내려간다.

이건 의미 있는 **음성 결과**다. S8를 과하게 낮추는 원인은 전이의 모양이 아니라
**z~=2까지 암흑부문(Ω_X~=0.685)이 얼마나 매끄럽게(군집 안 하고) 변하느냐**다.
모양은 부차적이고, 전이 시점과 최종 상분율이 지배한다.

그리고 이건 003의 ["c_eff^2 = 0은 해결책이 아니라 미해결 조건"](003_research_flow_plain_language_ko.md)
절에 숫자를 붙인다. 전이 성분을 매끄럽다고(c_eff²=1, 군집 안 함) 두면 성장이 과하게
눌린다. 반대로 c_eff²=0(물질처럼 군집)이면 안 눌리지만 그건 섭동에서 암흑에너지답지
않다. S8 레버는 전이 모양이 아니라 바로 이 **c_eff² 미해결 조건**에 걸려 있다.

### CP4 결론 (2026-06-12)

```text
밀도구동(CP3)도 S8를 똑같이 0.68로 과하게 낮춘다 (CP1과 사실상 동일).
전이 모양을 바꿔도 오버슈트는 안 줄어든다 -> 오버슈트는 구조적.
진짜 레버는 전이 모양이 아니라 c_eff²(전이 성분이 군집하느냐) 미해결 조건.
다음 후보: c_eff²를 0~1 사이로 열어 S8를 0.76에 맞출 수 있는지, 아니면
           rho*/장벽을 또 다른 물리상수에 묶어 050 천장을 직격.
```

## CP5 (2026-06-12): c_eff²를 열어 S8가 고쳐지는지 본다

CP4가 가리킨 진짜 레버를 직접 돌렸다. 전이 성분이 매끄러우면(c_eff²~1) 군집을 안
해서 성장이 과하게 눌리고, c_eff²가 작으면 물질처럼 군집해 안 눌린다. 그 사이
어딘가에서 관측 S8~=0.76이 나올 수 있나?

거친 Jeans 프록시를 썼다. 모드는 음속 지평선 위에서 압력에 눌리므로(k·c_s > aH),
S8 스케일 k_8에서 암흑성분이 군집하는 효율을 η(a) = 1/(1+R²),
R = c_s·c·k_8/(a·H0·E) 로 두고, 성장 source의 군집분율을 Ω_m + η·Ω_X로 바꿨다
([`cp5_sound_speed.py`](assets/004_rough_tanh/cp5_sound_speed.py),
[`fig_cp5_sound_speed.png`](assets/004_rough_tanh/fig_cp5_sound_speed.png)).

결과: S8가 c_eff²에 따라 **0.677(매끄러움) ~ 0.955(완전 군집)** 사이를 매끄럽게
움직이고, **관측 S8=0.76은 c_eff² ~= 3e-5에서 달성된다.**

| c_eff² | S8 |
| --- | --- |
| 1.0 (매끄러움) | 0.677 |
| 1e-4 | 0.726 |
| **~3e-5 (fit)** | **0.760** |
| 1e-6 | 0.887 |
| 1e-8 (완전 군집) | 0.955 |

즉 CP4의 오버슈트는 **치명적이 아니라 고칠 수 있다.** 단, 그 대가는 **아주 작은
음속(c_eff²~3e-5)이라는 손잡이를 하나 더 손으로 맞추는 것**이다. 이것이 정확히
003이 말한 "c_eff²=0은 해결책이 아니라 미해결 조건"이다. 이제 그 미해결 조건에
숫자가 붙었다: 관측을 맞추려면 c_eff²가 1보다 5자리수 작아야 한다.

주의: 이 η는 거친 프록시다. 정확한 값(3e-5인지 1e-4인지)은 CLASS의 clustering-DE
섭동 계산이 필요하고 그건 Level 3 = blocked이다. 하지만 정성적 결론("S8를 맞추는
작은 c_eff²가 존재한다 = 오버슈트는 튜닝으로 치료가능하지만 유도는 아니다")은 견고하다.

### CP5 결론 (2026-06-12)

```text
S8 오버슈트는 치명적이 아니다. c_eff² ~= 3e-5에서 관측 0.76이 나온다.
대가: 아주 작은 음속이라는 튜닝 손잡이 하나 추가 (003의 미해결 조건).
"살아있나?" -> 현상론으로는 S8 시험도 통과. 단 생존마다 손잡이가 하나씩 는다.
050 천장(c_eff²/rho*/장벽을 foam에서 유도)은 그대로. 관측 우월성도 아직 없음.
```

## CP6 (2026-06-12): 천장 직격(6a)과 반증 설계(6b) - 병렬

### CP6a: 손잡이가 하나의 foam 척도로 무너지나

쌓인 튜닝 손잡이 {z*, Δa, barrier, M, c_eff²}가 하나의 물리 척도에서 나오는지
봤다([`cp6a_ceiling_probe.py`](assets/004_rough_tanh/cp6a_ceiling_probe.py),
[`fig_cp6a_ceiling.png`](assets/004_rough_tanh/fig_cp6a_ceiling.png)).

핵심: 장 이론에서 order parameter의 음속은 자유 손잡이가 아니라 운동항이 정한다.
**표준(canonical) 스칼라는 c_eff²=1 (정확히).** c_eff²≪1은 비표준(k-essence) 운동항
+ 자체 튜닝이 있어야 나온다. 그런데 CP5가 S8에 요구한 값은 c_eff²~=3e-5다.

- 자연스러운 canonical c_eff² = 1 -> S8 = 0.677 (오버슈트)
- S8=0.76 요구 c_eff² ~= 3e-5 -> 둘 사이 **약 4.5 자릿수 갭**
- 단일 척도(z*=ρ*) 가정 후 손잡이 수: **5 -> 5 (하나도 안 무너짐).** barrier/M/lam은
  무차원 비, c_eff²는 운동 부문이라 위치 부문(ρ*)과 독립.

즉 CP6a는 **050 천장을 넘지 못한다.** 오히려 천장을 *수치로* 못박았다: 단일 척도
가정이 자유 파라미터를 하나도 제거하지 못하고, c_eff²는 canonical 값보다 4.5자릿수
아래로 튜닝돼야 하며 그걸 메울 foam 메커니즘이 없다. 상전이 동역학은 형태만 줄 뿐,
그 거품-고유의 숫자는 QFUDS가 미시구조에서 채워야 할 빈자리다.

### CP6b: 어디서 죽일 수 있나 (반증 설계)

배경(SNe μ, BAO 거리)은 CP1에서 이미 ΛCDM과 구별 불가다. 그래서 구별 가능한 곳을
찾았다([`cp6b_falsification.py`](assets/004_rough_tanh/cp6b_falsification.py),
[`fig_cp6b_falsification.png`](assets/004_rough_tanh/fig_cp6b_falsification.png)).

| 관측량 | ΛCDM과 차이 | 죽이는 조건 |
| --- | --- | --- |
| SNe μ(z) | 거의 없음 (<0.02 mag) | 배경으로는 못 죽임 |
| BAO 거리 | 거의 없음 (배경 추종) | 못 죽임 |
| fσ8(z)/RSD | QFUDS가 ΛCDM보다 ~7-8% 낮음. crude χ²: ΛCDM 6.2 vs QFUDS 12.0 (7점) | 약하게 불리, 아직 산포 안. z=0.5-0.9에서 ~5% 정밀도면 판별 |
| **w(z)/DESI w0wa** | **정반대 방향.** QFUDS는 freezing(0->-1), DESI 중심은 thawing(-1.7->-0.7). z=2에서 \|Δw\|=0.72 | **가장 약한 고리.** DESI thawing(wa<0)이 3σ로 굳으면 freezing 모델 사망 |

w(z) 값: z=0에서 QFUDS −1.00 / DESI −0.70, z=2에서 QFUDS −0.65 / DESI −1.37.
z~=0.5에서 두 곡선이 교차해 거기선 구별 불가지만, z≳1에서 갈라진다.

### CP6 결론 (2026-06-12)

```text
CP6a: 손잡이는 단일 foam 척도로 안 무너진다 (5->5). c_eff²는 canonical 1에서
      4.5자릿수 떨어져야 하고 메울 foam 메커니즘 없음. 050 천장 = 수치로 재확인.
CP6b: 이 모델은 배경/BAO로는 ΛCDM과 구별 불가, fσ8로 약하게 불리,
      w(z) freezing vs DESI thawing이 가장 강한 킬러 (z≳1).
종합: rough QFUDS는 "데이터에 맞출 수 있다"까지 왔지만 "ΛCDM보다 낫다"도,
      "foam에서 유도된다"도 아직 아니다. 가장 빨리 죽일 수 있는 곳은 DESI w0wa.
```

## CP7 (2026-06-12): brute-force 현상론 피팅 - 끼워맞추면 어디까지

애매한 손잡이를 (문헌 기반 prior 범위에서) 격자로 다 때려박아 데이터에 최대한
끼워맞췄다. 스캔: z\*∈{2..6}, c_eff²∈logspace(-7,-2), Ω_m0∈{0.29,0.31,0.33}.
타겟: RSD fσ8 7점 + weak-lensing S8=0.76±0.02 + 배경 \|Δμ\|<0.10 게이트.
([`cp7_brute_fit.py`](assets/004_rough_tanh/cp7_brute_fit.py),
[`fig_cp7_brute_fit.png`](assets/004_rough_tanh/fig_cp7_brute_fit.png);
스캔 격자 [`cp7_brute_fit_scan.csv`](assets/004_rough_tanh/cp7_brute_fit_scan.csv),
요약 [`cp7_brute_fit_summary.csv`](assets/004_rough_tanh/cp7_brute_fit_summary.csv))

| 모델 | S8 | χ²_fσ8 | χ²_S8 | χ²_tot | k | AIC |
| --- | --- | --- | --- | --- | --- | --- |
| ΛCDM | 0.830 | 6.22 | 12.25 | 18.47 | 1 | 20.47 |
| **QFUDS best** (z\*=6, Ω_m0=0.29, c_eff²=4.6e-6) | 0.778 | 7.24 | 0.81 | 8.05 | 4 | **16.05** |

명목상 **QFUDS가 AIC로 4.42 이긴다** — 손잡이 3개를 더 쓰고도. fσ8은 ΛCDM만큼
맞추면서(7.24 vs 6.22) S8 prior를 훨씬 잘 맞춘다(0.81 vs 12.25).

**그런데 이 승리는 전적으로 S8 prior 덕분이다.** 정직한 캐비엇:

1. ΛCDM이 지는 이유는 ΛCDM의 S8=0.83이 weak-lensing 0.76에서 3.5σ 떨어져
   χ²_S8=12.25를 무는 것뿐이다. **S8를 0.78로 낮추는 *어떤* 모델도** (wCDM, 낮은
   σ8 등) 똑같이 이긴다. QFUDS 고유의 승리가 아니다.
2. best fit의 c_eff²=4.6e-6은 CP6a가 말한 그 **fine-tuned 작은 음속**이다 (canonical
   1에서 5자릿수 아래). 050 천장 그대로.
3. 거친 분석이다: Jeans 프록시, 대표 데이터(공분산 없음), S8를 hard prior로 둔 것
   자체가 모델 선택이다. 제대로 하려면 CLASS likelihood = Level 3 = blocked.
4. RSD fσ8만 보면 S8≈0.78-0.83(ΛCDM 근처)을 선호하고 weak-lensing은 0.76을 원한다.
   모델은 그 사이 0.78에 앉아 둘을 가른다 (그림 b의 줄다리기).

### CP7 결론 (2026-06-12)

```text
brute-force로 끼워맞추면: 명목상 ΛCDM을 AIC로 이기는 지점까지 간다 (χ²_tot 18->8).
단 그 승리는 S8를 낮춘 덕분이고, S8 낮추는 어떤 모델이든 똑같이 이긴다 = QFUDS 고유 아님.
대가: c_eff²=4.6e-6 fine-tune (050 천장) + 손잡이 4개 + 거친 분석.
한 줄: "데이터에 맞출 수 있다"를 넘어 "명목상 이길 수도 있다"까지 가지만,
       그건 튜닝의 힘이지 새 물리도 우월성도 아니다. 진짜 판정은 CLASS likelihood(Level 3, blocked).
```

## CP8 (2026-06-12): c_eff²를 dial 말고 rough 도출 시도

CP5~CP7은 c_eff²를 데이터에 맞게 돌렸다(best≈4.6e-6). CP8은 묻는다. **어떤
물리량이 그 값을 *내놓나*, 아니면 거품 전제는 다른 값을 주나?**

물리 핸들 = order parameter의 **상관길이 ξ**. 자유에너지에 gradient 항을 넣으면
장은 ξ보다 작은 요동을 매끄럽게 지우고, 섭동 음속도 같은 stiffness가 정한다.

```text
c_eff ≈ ξ / d_H      (음속 지평선 ~ 상관길이, d_H = c/H0 ≈ 4448 Mpc)
c_eff² ≈ (ξ H0 / c)²
```

즉 c_eff²는 자유값이 아니라 **거품의 상관길이를 정하면 따라 나온다.** 계산 결과
([`cp8_ceff2_derivation.py`](assets/004_rough_tanh/cp8_ceff2_derivation.py),
[`fig_cp8_ceff2_derivation.png`](assets/004_rough_tanh/fig_cp8_ceff2_derivation.png)):

| 상관길이 ξ | c_eff² | S8 |
| --- | --- | --- |
| 미시 거품 ξ≤1 Mpc | →0 (5e-8 이하) | **0.95 (너무 높음)** |
| 구조 스케일 ξ≈10 Mpc | ~5e-6 | 0.82 |
| 데이터 fit (c_eff²=4.6e-6) | → ξ≈**9.5 Mpc** | ~0.78-0.82 |
| Hubble ξ≈c/H0 | ~1 | 0.68 (오버슈트) |

핵심: **데이터가 원하는 c_eff²≈4.6e-6은 상관길이 ξ≈10 Mpc = 우주 거대구조(cosmic
web) 스케일에 대응한다.** 그런데 "양자 거품"이라는 전제는 ξ가 **미시적**이어야
한다(Planck~은하 이하). 미시 거품이면 c_eff²→0 → 암흑성분이 CDM처럼 완전히 뭉쳐
**S8≈0.95로 오히려 ΛCDM(0.83)보다 더 높아지고 관측 0.76에서 더 멀어진다.**

즉 **rough 도출은 fit 값을 자연스럽게 내놓지 못한다.** 오히려 거품 전제(미시 ξ)는
S8를 *틀린 방향*으로(높게) 민다. 맞추려면 ξ를 10 Mpc로 키워야 하는데 그건 거품이
아니라 구조 스케일이다. 이것이 050 천장을 **c_eff² 쪽에서** 재확인한 것이다 — 이번엔
"왜 막히나"에 물리적 의미가 붙었다: *데이터가 원하는 음속은 미시 거품이 아니라
10 Mpc 상관길이를 요구한다.*

### CP8 결론 (2026-06-12)

```text
c_eff² rough 도출(상관길이 ξ 경유): 데이터 fit 값 4.6e-6 = ξ≈10 Mpc(구조 스케일).
미시 '양자 거품'(ξ≪Mpc) -> c_eff²→0 -> S8≈0.95 (틀린 방향, ΛCDM보다 나쁨).
=> 자연스러운 거품 상관길이는 fit을 못 만든다. 도출 실패 = 050 천장 재확인.
의미: dial한 c_eff²는 "10 Mpc 상관길이"라는 비-거품 스케일을 숨기고 있었다.
```

## 재현

```bash
cd docs/wiki/lineage/assets/004_rough_tanh
python3 model.py        # 공유 모델 smoke test
python3 background.py   # fig_background.png
python3 growth.py       # fig_growth.png
python3 phase.py        # fig_phase.png
python3 state_variable.py        # fig_state_variable.png (CP2 상태변수 동역학)
python3 density_driven.py        # fig_density_driven.png (CP3 밀도구동)
python3 cp4_growth.py            # fig_cp4_growth.png (CP4 성장/S8)
python3 cp5_sound_speed.py       # fig_cp5_sound_speed.png (CP5 c_eff² 스캔)
python3 cp6a_ceiling_probe.py    # fig_cp6a_ceiling.png (CP6a 천장 직격)
python3 cp6b_falsification.py    # fig_cp6b_falsification.png (CP6b 반증 설계)
python3 cp7_brute_fit.py         # fig_cp7_brute_fit.png + scan/summary csv (CP7)
python3 cp8_ceff2_derivation.py  # fig_cp8_ceff2_derivation.png + csv (CP8 도출 시도)
```

각 스크립트는 그림을 `.png`와 `.svg`로, 수치 결과를 `*_results.csv`(또는 CP7은
`cp7_brute_fit_scan.csv` / `_summary.csv`)로 남긴다.

의존성: numpy, scipy, matplotlib.
