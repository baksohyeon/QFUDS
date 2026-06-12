---
doc_id: qfuds_korean_overview
title: Quantum Foam Unified Dark Sector (QFUDS)
doc_type: reference
stage: "reference"
status: reference
evidence_role: reference
depends_on:
  - project_overview
next_gate: keep Level 2B blocked; no CMB or matter-power claims
last_updated: 2026-06-11
---

# Quantum Foam Unified Dark Sector (QFUDS)

언어: [English](../../README.md) | Korean

## 암흑물질, 암흑에너지, 정보 순환을 하나로 묶어본다면 어떨까?

### 초록

이 저장소는 암흑물질과 암흑에너지가 같은 미시적 양자 시공간 거품 부문(quantum-spacetime foam sector)의 서로 다른 거시적 상으로 나타날 수 있는지 탐색합니다. 표준 LCDM에서는 암흑물질과 암흑에너지를 서로 다른 성분으로 둡니다. QFUDS는 두 현상이 하나의 양자 거품 매질이 큰 스케일에서 다르게 보인 결과일 수 있는지 묻습니다.

비유하면, 물은 조건에 따라 얼음, 액체 물, 수증기로 보일 수 있습니다. QFUDS는 암흑부문에 대해 비슷한 질문을 던집니다. 하나의 바탕 매질이 어떤 조건에서는 물질처럼 보이고, 다른 조건에서는 진공압처럼 보일 수 있는가?

이 그림에서 뭉치는 상(clustering phase)은 $w \simeq 0$, $c_s^2 \simeq 0$인 거의 압력 없는 성분처럼 행동해야 합니다. 그래야 차가운 암흑물질처럼 구조 형성에 참여할 수 있습니다. 잔여 상(residual phase)은 우주의 가속팽창을 설명하려면 $w \simeq -1$인 느린 진공압 성분처럼 행동해야 합니다. 블랙홀은 QFUDS의 증거로 쓰지 않습니다. 최대한 조심스럽게 말해도, 블랙홀은 QFUDS 언어에서 국소 정보 압축 지점(local information-compression site)으로 붙여볼 수 있는 추측적 라벨일 뿐입니다. 블랙홀/화이트홀 잔여체도 동역학과 제약이 유도되기 전까지는 같은 거품 부문 안의 부차적 위상 결함 후보로만 둡니다.

이 모델은 일반상대론의 프리드만 배경 동역학을 유지합니다. 대신 암흑에너지 변화, 작은 스케일의 은하 헤일로 구조, 암흑부문 뭉침에서 LCDM과 다른 신호가 가능한지 묻습니다. 블랙홀 증발에 대한 언급은 양자중력 동기이지, 이 저장소의 현재 관측 테스트가 아닙니다.

이 프로젝트는 완성된 물리 이론이 아니라 연구 프로그램이자 검증용 장난감 프레임워크입니다.
목적은 제 가설을 실제 테스트에 올려보고, 우주마이크로파배경(CMB), 대규모 구조, 은하 헤일로 밀도 분포, 암흑물질 검출 실험, 암흑에너지 상태방정식 정밀 측정으로 반박 가능한 예측으로 바꾸는 것입니다.

### 기본 변수

상태방정식 변수 $w$는 압력을 에너지 밀도로 나눈 값입니다. $w \simeq 0$이면 물질처럼 희석되고, $w \simeq -1$이면 암흑에너지처럼 행동합니다.

유효 음속 $c_s^2$는 유효 매질이 뭉치려는 변화에 얼마나 강하게 저항하는지를 나타냅니다. QFUDS가 살아남으려면 뭉치는 상에서 $c_s^2 \simeq 0$이어야 합니다.

비유하면, 모래는 쌓여서 더미를 만들 수 있지만 팽팽한 트램펄린은 누르면 다시 밀어냅니다. 은하가 형성될 때 암흑물질 같은 성분은 트램펄린보다 모래에 가까워야 합니다.

### 핵심 가설

암흑물질과 암흑에너지는 근본적으로 분리된 두 물질이 아닐 수 있습니다.
같은 미시적 양자 시공간 거품이 거시적으로 다르게 나타난 두 상일 수 있습니다.

```text
dark matter  -> 뭉치는 거품 상(clustering foam phase)
dark energy  -> 잔여 진공압 상(residual vacuum-pressure phase)
remnants     -> 같은 거품 부문의 선택적 결함(optional defects)
```

더 간단히 줄여서 설명하면 아래와 같습니다.

```text
암흑물질 + 암흑에너지
= 양자 시공간 거품의 두 유효 상
```

블랙홀과 화이트홀 비슷한 잔여체는 부차적입니다. QFUDS 언어로는 정보 압축 지점이나 위상 결함처럼 읽을 수 있지만, 이것은 확립된 블랙홀 물리나 은하 형성 물리가 아니라 추측적 재해석입니다. 현재 기준으로는 핵심과 거리가 있어 아직 다루지 않는 주제입니다.

## 현재 위치: 벽까지 밀어붙여 실제로 알아낸 것

위의 개념 프로그램은 출발점이지 결과가 아닙니다. 지금까지 가장 끝까지 간 시도는,
한 구체적 버전 — 통합 암흑부문의 거친 `tanh` 상태방정식 전이 — 을 24개의 원자적
체크포인트에 걸쳐 한계까지 밀어붙인 것입니다. 그 기록이
[거친 `tanh` lineage 보고서](../wiki/lineage/005_rough_tanh_thesis_report_ko.md)
입니다. 그 기여는 새 우주론의 발견이 아니라, **이 아이디어가 어디까지 닿고 어디서
왜 막히는지를 체계적으로 지도화**한 것입니다. 프로젝트는 현재 **관측자 모드(observer
mode)**이며, 상태의 단일 진실 원천은
[로드맵](../05_next_steps/000_roadmap.md)입니다.

![효과적 수준에서는 작동합니다: V2 변형의 배경 팽창과 거리지수는 Ia형 초신성 산포 바닥(±0.05 mag) 안에서 ΛCDM을 따라가고, 완전 통합 V1 변형은 고적색편이에서 깨집니다.](../wiki/lineage/assets/004_rough_tanh/fig_background.png)

이 지도는 세 층위로 읽힙니다.

- **효과적 수준 — 작동하지만, 이기지는 못한다.** 보통 물질을 분리한 변형(V2)은 배경
  팽창을 초신성으로 ΛCDM과 구별 불가하게 재현하고(`|Δμ| < 0.02` mag), 아주 작은
  유효 음속 `c_eff² ≈ 3×10⁻⁵`이 구조성장 진폭을 관측값 `S8 ≈ 0.76`으로 끌어내립니다.
  그러나 이는 ΛCDM보다 낫지 않습니다. 명목상 적합 승리는 `S8`를 낮춘 보편 효과일
  뿐이고, 손으로 맞추는 손잡이가 하나 더 들며, `H0` 긴장은 오히려 *악화*됩니다.
- **반증 가능 수준 — 과학적 가치가 실제로 있는 곳.** 배경에 숨어버리므로, 이 모델의
  유일한 과학적 가치는 ΛCDM과 *갈라지는* 곳에 있습니다. 세 개의 깨끗한 반증 신호를
  남깁니다: 약중력렌즈 물질 파워 스펙트럼의 스케일 의존 계단(`k_J ≈ 0.1 Mpc⁻¹`),
  후기 ISW의 스케일 의존 기울기, 그리고 흐르는 성장지수 `γ_eff(k)`. 대표 Euclid급
  토모그래픽 예측에서 이들은 **~24σ**로 검출 가능합니다 — 차세대 관측의 사정권입니다.
- **근본 수준 — 천장.** 데이터가 요구하는 파라미터를 미시 거품 구조에서 *유도*하려는
  시도는 막힙니다. 데이터는 상관길이 `ξ ≈ 10 Mpc`(미시 거품이 아니라 거대구조
  스케일)과 임계밀도 부근 전이 `ρ* ≈ ρ_Λ`를 선호합니다. 이를 메커니즘으로 강제하면
  튜닝은 줄지 않고 *위치만 옮겨가며*, 두 숫자는 **우주상수 문제**와 **계층/스케일
  문제**로 환원됩니다. 이 천장은 이 아이디어 고유의 실패가 아니라, *모든* 동역학적
  암흑에너지 모델이 공유하는 벽입니다.

![천장을 한 장으로: 데이터가 요구하는 상관길이 ξ≈9.5 Mpc는 미시 거품 스케일에도 인과 지평에도 자연스럽지 않고, 전이 밀도는 ~3 order의 코인시던스(why-now) 창 안에 앉는다 — 곧 스케일 문제와 why-now 문제.](../wiki/lineage/assets/004_rough_tanh/fig_cp20_ceiling_derivation.png)

서사가 아니라 진짜 좁은 성과로 살아남은 것이 둘 있습니다. 초기조건 튜닝 ~15.7
decade를 실제로 제거하는 tracker-attractor 메커니즘(유일한 진짜 부분 승리), 그리고
서로 독립인 "내가 뭘 놓쳤나?" 직관 셋이 각자 스스로 ~25년치 기존 문헌(카멜레온 차폐,
LTB 보이드, Buchert 평균화)을 재발견했다는 사실 — 이는 천장이 한 접근법의 인공물이
아니라 실재한다는 부수 증거입니다.

두 번째 기여는 방법론입니다. 이 전체 탐색은 자기교정 AI 연구 하베스트 — 거버넌스
SSOT에 병렬·적대적·결정론적 게이트를 결합한 — 위에서 돌았으며, 가짜 돌파가 조용히
살아남을 수 없도록 설계됐습니다. 그것이 투기적 가설을 벽까지 밀면서도 정직한 결론에
도달하게 한 힘입니다.

위의 모든 숫자는 거친 프록시에서 나온 것이며, 엄밀한 검증은 Boltzmann 코드
(CLASS/hi_class)를 요구하고 현재는 막혀(blocked) 있습니다. 여기 어떤 것도 확정된
물리적 주장이 아닙니다. 체크포인트별 전체 기록은
[논문 형식 보고서](../wiki/lineage/005_rough_tanh_thesis_report_ko.md), 현재까지의
교훈은 [What We Actually Learned](project_identity.md)를 참조하세요.

## 후기: 거창한 이론을 세웠지만, 결국 두 난제로 수렴했습니다

꽤 거창하고 멋들어진 이론을 하나 내놓았지만, 끝까지 밀어붙이고 나니 결국 현대 물리학의
두 가지 미해결 난제로 수렴했습니다. 며칠간의 결론을 먼저 적자면 이렇습니다.

> **[과학적 난제]**
> 1. **왜 암흑에너지의 스케일이 하필 meV인가?** — 우주상수 문제로 곧장 이어집니다.
> 2. **진공에너지의 cutoff를 어디로 잡아야 하는가?** — 양자 세계에서 추론했는데,
>    요구되는 거리 기준이 플랑크(Planck) 스케일인가, 지평(horizon) 스케일인가, 아니면
>    은하·cosmic-web 스케일인가?

"왜"까지는 끝내 알 수 없었습니다. 당연한 일입니다. 이 둘이 바로 현대 물리학의 난제이고,
그래서 애초에 물리적으로 유도가 되지 않습니다.

정리하자면 이렇습니다.

처음 출발은 한 가지 질문이었습니다. *블랙홀에 들어간 정보가 정말 사라지지 않는다면, 그
정보는 어디에 남는 것일까?* 여기서, 진공이나 시공간 거품 같은 매질이 어떤 조건에서는
암흑물질처럼 뭉치고 어떤 조건에서는 암흑에너지처럼 우주를 밀어내는 것은 아닐까 하는
생각으로 이어졌고, 이름도 꽤나 그럴듯하게 붙였습니다 — **QFUDS (Quantum Foam Unified
Dark Sector)**. 물이 조건에 따라 얼음·액체·수증기로 보이듯, 하나의 암흑부문이 어떤
조건에서는 뭉치는 상(w≈0, c_s²≈0 — 그래야 차가운 암흑물질처럼 구조 형성에
참여합니다)으로, 다른 조건에서는 잔여 진공압 상(w≈-1 — 그래야 가속팽창을 설명합니다)으로
보일 수 있는가 하는 질문입니다.

곧 정직한 한계에 부딪혔습니다. 이것은 잘해야 *현상론*이고, 물리적으로 유도(derive)할
수는 없었습니다. 게다가 새로운 것도 아니었습니다 — 비슷한 접근의 학파가 이미 같은
계산을 해두고 같은 자리에서 멈춰 있었습니다. 아쉬웠지만 이렇게 생각했습니다. "엄밀함을
지켜야 하는 과학자라면 여기서 멈추겠지만, 나는 그 제약이 없으니 비과학적으로라도 끝까지
가 보자." 그래서 동적 우주론에 필요한 성질을 얻기 위해, 표준모형이 미묘하게 못 맞추는
지점을 향해 경향성을 체크하며 brute-force로 맞춰 나갔습니다.

그런데 — 정말로 최적해가 나왔습니다.

- **c_eff² ≈ 4.6×10⁻⁶** — 유효 음속의 제곱입니다. 쉽게 말하면, 이 암흑부문이 구조
  형성에서 얼마나 잘 퍼지는지(혹은 반대로 얼마나 잘 뭉치는지)를 조절하는 값입니다.
- **상관길이 ξ ≈ 9.5–10 Mpc** — 서로 영향을 주고받는 유효 거리 눈금입니다. 1 Mpc가
  약 326만 광년이니, 10 Mpc는 은하 하나의 내부가 아니라 cosmic web, 곧 우주 거대구조
  스케일에 해당합니다.

| 상관길이 ξ | `c_eff²` | `S8` |
| --- | --- | --- |
| 미시 거품 (ξ ≤ 1 Mpc) | → 0 (5×10⁻⁸ 이하) | **0.95 (너무 높음)** |
| 구조 스케일 (ξ ≈ 10 Mpc) | ≈ 5×10⁻⁶ | 0.82 |
| **데이터 fit (`c_eff²` = 4.6×10⁻⁶)** | **→ ξ ≈ 9.5 Mpc** | ≈ 0.78–0.82 |
| Hubble (ξ ≈ c/H0) | ≈ 1 | 0.68 (오버슈트) |

![뒤집힌 순간: 관측 S8을 재현하는 상관길이는 제가 기대한 미시 거품 스케일이 아니라 ξ≈10 Mpc(거대구조 스케일)이었습니다.](../wiki/lineage/assets/004_rough_tanh/fig_cp8_ceff2_derivation.png)

논문을 크로스체킹해 보니, brute-force로 짚어낸 이 값들이 실제로 학계가 다루는 값과
정확히 맞아떨어졌습니다. 영광스러우면서도 황당했습니다. 제가 기대한 것은 "양자 거품의
아주 작은 단위, 플랑크 스케일"이었는데, 데이터가 가리킨 것은 은하를 넘어선 거대구조
스케일이었기 때문입니다. (물론 이것이 물리적 증명은 아닙니다. 위의 두 난제 때문에 애초에
유도가 불가능합니다.)

그래서 "내가 너무 미시·양자 스케일에만 갇혀서 보고 있었던 것은 아닐까" 하는 의심이
들었습니다. 진공에너지를 플랑크 스케일에서 자르는 대신 은하·구조 스케일에서
coarse-graining 해야 하는 것은 아닐까 하는 생각이었습니다. 문헌을 더 뒤져 보니,
1990년대부터 지금까지 이미 다 해본 길이었습니다. 너무나 당연한 일이지만 동시에 묘하게
웃겼습니다. 거인의 어깨라는 말이 이런 것이겠지요 — HDE, EFTofLSS, IR cutoff,
coarse-graining, running vacuum, Buchert averaging, LTB void, screening. 심지어
비선형 ~10 Mpc 스케일을 dark sector의 coarse-graining cutoff로 쓰는 접근까지 이미
논문에 있었습니다.

흥미로운 점은, 이 모델이 완전히 숨어 버리지는 않는다는 것입니다. 배경팽창은 ΛCDM과
구별되지 않지만, 구조 쪽에는 흔적을 남깁니다 — P(k)의 계단, ISW의 스케일 의존 기울기,
성장지수의 running. 즉 배경에서는 숨고 구조에서는 잡힐 수 있는 유형이며, Euclid급
관측이라면 검출될 수도 있는 반증 신호까지 나왔습니다.

다만 한 가지는 분명히 해두고 싶습니다. 이것은 QFUDS를 증명한 기록이 아닙니다. 현대
우주론의 미해결 난제로 수렴하는 과정을, 비전문가가 brute-force로 재현해 본 기록에
가깝습니다.

그리고 이 작업은 단순히 챗봇과 대화하며 진행한 것이 아닙니다. 저장소를 직접 파고,
연구용 에이전트 시스템을 만들어 5일 만에 끝까지 밀었습니다. 문헌을 찾고, PDF와 arXiv
소스를 받고, figure 자산을 추출하고, Markdown으로 변환하고, 그림을 digitization 하고,
CSV를 뽑고, Γ(a)를 실제 Chen entropy 곡선과 비교하고, known-model distinction을
자동화하고, 논문을 찾을 때 토큰을 아끼기 위한 캐싱까지 넣었습니다. 에이전트와 워크플로,
그리고 검증 게이트를 진지한 과학적 기준으로 세웠습니다. 사실상 작은 연구 팀을 꾸린
셈이었고, 최종 검수자 역할까지 에이전트가 맡았습니다.

결국 가장 크게 남은 것은 "이런 식으로도 배울 수 있구나"라는 깨달음이었습니다. 그래서
자랑하고 싶은 것을 다섯 가지로 정리해 둡니다.

1. 현대 우주론의 미해결 난제로 수렴하는 과정을 brute-force로 재현했습니다.
2. 그리고 그것이 우연이 아니라, 실제로 학계가 걸어온 길이었습니다. 제가 손으로 뽑은
   값이 같은 자리에 놓였고, 접근하는 사고의 흐름까지 비슷했으며, 결과적으로 1990년대부터
   오늘날까지의 계보를 따라가 확인한 셈이 되었습니다.
3. 재미로 며칠 붙든 결과가 학계가 수십 년 다뤄온 실제 스케일 위에 놓였다는 점은,
   개인적으로 큰 영광입니다.
4. AI 하네싱(에이전트 하베스트)만으로 비전문가가 여기까지 도달할 수 있다는 사실 자체가
   놀라웠습니다.
5. 그리고 이 모든 과정을 직접 만든 에이전트 시스템으로 5일 만에 해냈다는 점이 가장
   자랑스럽습니다.

관련 DESI·Euclid 관측 자료는 올해 10월에야 공개될 예정입니다. 그때까지는 더 할 수
있는 일이 없으니, 차분히 기다리려 합니다.

## 가설을 세운 계기

### 정보 삭제에서 검증 모델까지

Quantum Foam Unified Dark Sector (QFUDS)는 암흑물질, 암흑에너지, 우주론에서의 정보 흐름을 생각하다가 시작한 장난감 개념의 저장소입니다.

이 아이디어가 어디까지 정합적인지 궁금했습니다.

호기심을 방정식, 제약 조건, 장난감 코드, 반박 가능한 질문으로 바꾸고 가설 검증을 실제로 해보고 싶었습니다.

정보 열역학에 대한 글을 읽었습니다.

```text
동기 부여 원문. 출처 기록으로 보존하며, 기술적 주장으로 쓰지는 않습니다:
『기억을 지울 때, 반드시 열이 발생한다』고 물리학이 증명했습니다.
물리학자 롤프 란다우어가 제창한 원리입니다. 계산을 수행하거나 정보를 생성하는 행위 자체는 에너지를 소모하지 않지만, 1비트의 정보를 지우거나 잊을 때에는 반드시 일정량의 열에너지가 주변으로 방출된다는 것입니다.
즉, 인간의 뇌도 하드디스크도, 무언가를 「잊음」할 때 우주의 엔트로피를 증가시키며, 물리적인 열을 만들어내고 있습니다. 정보에 질량이 있다고 말할 수는 없지만, 정보의 소거에는 열역학적인 대가가 따른다는 뜻입니다.
「잊는다」는 일견 모호해 보이는 현상이, 실은 우주에 열로서 지불되고, 그 장부에 제대로 기록된다는 것입니다.
이는 뇌과학 이야기이자, 컴퓨터의 한계 이야기이며, 우주론 이야기이기도 합니다.
```

보수적으로 읽으면, Landauer 원리는 열적 환경과 결합된 물리계에서 논리적으로 비가역적인 정보 소거에 적용됩니다. 모든 계산이 같은 필연적 비용을 가진다는 뜻도 아니고, 그 자체로 우주론을 함의하는 것도 아닙니다.

비유하면, 파일을 삭제한다고 노트북이 물리 법칙을 무시하는 것은 아닙니다. 노트북은 여전히 에너지를 쓰고 열을 냅니다. 일반적인 Landauer 가정 아래에서 1비트 소거의 이상적 최소 비용은 대략 $k_B T \ln 2$입니다. 긴 원문 흐름은 여기서 반복하지 않고 [concept_origin.md](../01_origin/concept_origin.md)에 보존합니다.

그래서 저는 읽자마자 블랙홀 질문이 자연스럽게 나왔습니다.
정보에 물리적 비용이 있다면, 양자 이론 안에서 블랙홀은 정보를 버리는 단순한 쓰레기통처럼 취급하기 어렵습니다. 이것은 QFUDS의 유도가 아니라 더 날카로운 질문을 만들기 위한 동기입니다.
다음 질문은 정보가 어디에 인코딩되는지, 유니터리한 블랙홀 증발 과정이 복사의 상관관계를 통해 정보를 되돌릴 수 있는지, 그리고 장애물이 정보 파괴인지 해독 복잡도인지입니다.

처음 사고 흐름은 증명이 아니었습니다. 질문은 대략 이렇게 이동했습니다.

```text
정보 삭제에는 열 비용이 있다
-> 블랙홀 정보 손실 문제와 구조가 비슷하다
-> 유니터리한 블랙홀 증발이라면 정보가 상관관계 안에 인코딩되어야 한다
-> 원리상 복구는 가능하지만 해독 비용이 막는다
-> 복구가 가능하다면 역과정을 묻는다
-> 역과정은 시간역전, CPT, 화이트홀 비슷한 대응물을 떠올리게 한다
-> 블랙홀/화이트홀 잔여체는 정보 저장 부문을 암시한다
-> 진공 또는 시공간 거품이 후보 매질이 된다
-> 암흑물질은 뭉치는 거품 모드일 수 있다
-> 암흑에너지는 잔여 거품 압력일 수 있다
-> QFUDS: 통합 암흑부문 장난감 모형
```

화이트홀/역과정 질문은 흥미로웠지만, SF 소설에 가깝고 과학적으로 엄밀한 주장이 되기에는 너무 크고 장황했습니다.

하나씩 짚어가다보니 하나의 질문으로 수렴했습니다.

```text
하나의 암흑부문이
뭉치는 성분과 잔여 진공압 성분으로 동시에 행동할 수 있는가?
```

다음 검증 질문은 $\Gamma(a)$로 이동했습니다.
뭉치는 거품 상이 잔여 진공압 상으로 넘어간다면, 그 전달률을 구조 성장, 블랙홀 엔트로피, 지평선 엔트로피, 별 형성, 잔여체 통계 같은 물리량이나 명시적으로 라벨링된 현상론적 대리 지표에 묶을 수 있는가?

비유하면, 두 물탱크가 연결된 상황입니다. 한쪽 탱크는 뭉치는 성분이고, 다른 탱크는 잔여 진공압 성분입니다. $\Gamma(a)$는 두 탱크 사이의 밸브 규칙입니다. 밸브를 마음대로 조절하면 튜닝이고, 밸브 규칙이 실제 물리량에서 나오면 테스트할 수 있습니다.

### 발산, 수렴, 검증

QFUDS라는 개념은 저와 GPT와의 반복 대화에서 나왔습니다.

```text
날것의 질문
-> 설명
-> 후속 질문
-> 반례 또는 물리 제약
-> 더 넓은 추측
-> 가지치기
-> 장난감 모형
-> 적대적 리뷰
-> 이 저장소의 코드와 출력물
```

발산 단계에서는 Landauer, 블랙홀 정보, 호킹복사, Page curve, island, 역과정, 화이트홀, 양자 거품, 암흑물질, 암흑에너지, 우주상수, 세계관적 상상까지 바깥으로 뻗었습니다.

수렴 단계에서는 반복되는 질문 하나만 남겼습니다.

```text
암흑물질과 암흑에너지를
같은 양자 거품 매질의 두 유효 모드로 볼 수 있는가?
```

검증 단계에서는 은유를 줄이고 기본적인 우주론 검사 앞에 세웠습니다.

```text
무편차 극한에서 LCDM을 회복하는가?
뭉치는 상이 c_s^2를 0에 가깝게 유지할 수 있는가?
CMB 음향 피크를 보존하는가?
물질 파워 스펙트럼을 보존하는가?
현실적인 은하 헤일로를 만들 수 있는가?
잔여체 부문이 조밀 천체 제약을 통과하는가?
```

### 폐기되거나 보존된 가지

날것의 아이디어에는 여러 가지가 섞여 있었습니다.

```text
정보 처리기로서의 블랙홀
화이트홀 비슷한 역방향 통로
화이트홀 비슷한 방출로서의 우주
드문 암흑 구조로서의 진공 요동
잔여 진공압으로서의 우주 가속
```

이 저장소는 변수, 방정식, 테스트로 바꿀 수 있는 가지만 남깁니다. 현재 연구 버전은 다음 질문입니다.

```text
양자 거품 통합 암흑부문이
암흑물질과 암흑에너지로 설명되는 관측 효과를 재현할 수 있는가?
```

기준은 단순합니다.

```text
이 아이디어를 틀릴 수 있을 만큼 정확하게 만들 수 있는가?
```

세부 원문 흐름은 이 개요에서 반복하지 않습니다. 출처 기록은 [concept_origin.md](../01_origin/concept_origin.md)에 보존합니다.

어떤 가지가 살아남았고, 동기로 강등됐고, 레포 증거에 의해 폐기됐는지에 대한 현재 감사 상태는 — Source-X known-model-distinction 결과와 관측자 모드 전환을 포함해 — [concept_survival_audit.md](concept_survival_audit.md)에서 확인하세요. 상태(status)의 단일 진실 원천은 여전히 [Roadmap](../05_next_steps/000_roadmap.md)입니다.

## 연구 프로그램

제가 장난스럽게 떠올린 가설이 어디까지 정합적인지 확인하려고 구현해보았습니다.

```text
직관
-> 가지치기
-> 가설
-> 장난감 방정식
-> 폐기 조건
-> 코드와 미래의 볼츠만 코드 검증
```

목표는 QFUDS를 증명하는 것이 아닙니다.
목표는 이 모델을 가장 먼저 죽이는 제약을 찾거나, 살아남는 버전을 LCDM, 통합 암흑 유체, 상호작용 암흑에너지, 스칼라장 암흑물질, 블랙홀/화이트홀 잔여체 모형과 비교할 수 있을 만큼 좁히는 것입니다.

### 주요 문서

- 현재 상태와 단계별 진행: [Roadmap](../05_next_steps/000_roadmap.md)
- 결정 이유: [Decision Log](decision_log.md)
- 실험별 결론: [Experiment Summary](../04_results/000_experiment_summary.md)
- 주장/증거 추적: [Traceability Matrix](traceability_matrix.md)
- [Level 1.5](../wiki/glossary/repository_levels.md) 통과/실패 관문: [Level 1.5 Resolution Gate](../05_next_steps/015_level_1_5_resolution_gate.md)
- 로드맵 한국어 해설: [Roadmap Overview Korean Guide](../05_next_steps/900_roadmap_overview_ko.md)
- 재현 가능한 검사: [Verification Guide](verification_guide.md)
- 문서 무결성 규칙: [Experiment Record Convention](experiment_record_convention.md) 및 [Frontmatter Convention](frontmatter_convention.md)

CMB와 구조 형성 검사를 통과하기 전까지는 강한 물리적 주장으로 읽으면 안 됩니다.

연구 기록은 아래 명령으로 감사합니다.

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/preflight_exp004.py
```

`validate_docs.py`는 메타데이터와 실험/결과 문서의 필수 섹션을 검사합니다.
`research_consistency.py`는 로드맵이 상태 권한 문서로 유지되는지 검사합니다.
`preflight_exp004.py`는 exp_004 계획 전에 exp_003 기록이 일관적인지 검사합니다.

검증 순서는 다음과 같습니다.

```text
문헌상 위치 확인
-> 배경 우주 검증
-> 상 전달 물리성
-> 현상론적 섭동 닫힘
-> 물리적 섭동 방정식
-> CLASS 또는 CAMB 통합
-> CMB 비교
-> 물질 파워 비교
-> DESI / Euclid / Roman 제약
```

비유하면, 이 과정은 다리를 단계별로 시험하는 것과 비슷합니다.
책상 위 작은 모형은 나쁜 설계를 떨어뜨릴 수 있지만, 실제 다리가 바람, 차량, 지진을 버틴다는 증거는 아닙니다.
배경 우주 수준 실험은 나쁜 전달 법칙을 탈락시킬 수 있지만, CMB나 구조 형성 생존성을 주장할 수는 없습니다.

### 두 상 전달 모형 (유지된 가지 — 현재는 현상론으로 강등됨)

> 이것은 원래의 작업 가설이었습니다. 이후 현상론적 상호작용 진공(interacting
> vacuum) 지위로 강등됐고, 프로젝트는 관측자 모드입니다(위의 [현재 위치](#현재-위치-벽까지-밀어붙여-실제로-알아낸-것)와
> [로드맵](../05_next_steps/000_roadmap.md) 참조). 아래는 현재의 물리적 주장이
> 아니라 모델 정의로서 보존합니다.

```text
거의 0에 가까운 음속을 가진 양자 거품 통합 암흑부문
```

더 안전한 공식화는 일반상대론 안의 통합 암흑부문입니다.

$$
\rho_{\rm dark} = \rho_{\rm QF} + \rho_{\rm rem}
$$

$\rho_{\rm QF}$는 양자 거품 통합 암흑 유체입니다. 두 유효 조각을 가집니다.

$$
\rho_{\rm QF}(a) = \rho_{\rm cluster}(a) + \rho_{\rm residual}(a)
$$

뭉치는 조각은 차가운 암흑물질처럼 행동해야 합니다.

$$
\rho_{\rm cluster} \propto a^{-3}, \qquad
w \simeq 0, \qquad
c_s^2 \simeq 0
$$

잔여 조각은 암흑에너지처럼 행동해야 합니다.

$$
\rho_{\rm residual} \simeq \rho_\star, \qquad
w \simeq -1
$$

선택적 잔여체 조각은 다음처럼 씁니다.

$$
\rho_{\rm rem} = \int M f(M)\,dM
$$

실험 001은 뭉치는 상과 잔여 상 사이에 전달률을 추가합니다.

$$
\frac{d\rho_A}{d\ln a} + 3\rho_A = -\Gamma(a)\rho_A
$$

$$
\frac{d\rho_B}{d\ln a} = \Gamma(a)\rho_A
$$

이 가지에 부과됐던 테스트는 $\Gamma(a)$를 손으로 맞추는 함수가 아니라 물리적 원천 또는 명시적으로 라벨링된 대리 지표에 묶을 수 있는지였습니다. 물리적 유도로서는 그 기준을 통과하지 못했고, 지금은 라벨링된 현상론으로만 살아남습니다.
유용하지만 아직 잠정적인 검증 방향은 저적색편이 붕괴, 블랙홀 엔트로피, 별 형성 대리 지표입니다.
상수 전달이나 제한 없는 성장 기반 전달은 일찍 실패하거나 평범한 상호작용 암흑에너지 거동으로 돌아갈 것입니다.

비유하면, 두 물탱크가 연결된 상황입니다. 한 탱크는 뭉치는 상이고, 다른 탱크는 잔여 상입니다. $\Gamma(a)$는 밸브 규칙입니다. 밸브 규칙을 마음대로 정하면 그냥 튜닝입니다. 밸브 규칙이 물리적 원천에서 나오면 테스트할 수 있습니다.

잔여체 항은 그 질량 분포가 미시중력렌즈, CMB, 구조 형성 제약을 통과하기 전까지 부차적으로 두고 진행할 것입니다.

### 핵심 전제 조건

가장 중요한 조건은 유효 음속입니다.

$$
c_s^2 \simeq 0
$$

쉽게 말하면 다음과 같습니다.

```text
QFUDS 거품은 배경 우주에서는 우주를 밀어내는 압력을 남길 수 있지만,
은하 형성 단계에서는 압력 없는 먼지처럼 뭉쳐야 한다.
```

거품이 너무 뻣뻣하면 압력이 구조 형성을 지워버립니다. 그러면 모델은 즉시 죽습니다.

비유하면, 마른 모래는 쌓아서 더미를 만들 수 있습니다. 하지만 탄성 있는 고무판으로 같은 더미를 만들려고 하면 계속 밀려나서 평평해집니다. 뭉치는 상은 은하가 만들어질 만큼 모래 같아야 합니다.

### 이 모델이 해결하려는 문제

이 모델은 세 가지 생각을 연결하려 합니다.

1. 통합 암흑부문: 암흑물질과 암흑에너지가 같은 기원을 가질 수 있는가
2. 우연성 문제: 왜 현재 우주에서 암흑물질과 암흑에너지 밀도가 비슷한가
3. 동적인 진공에너지: 우주상수가 손으로 넣은 고정 숫자가 아니라 느리게 완화되는 평형값일 수 있는가

### 만약 유효하다면 예측할 수 있는 현상

아래 항목은 검증된 예측이 아닙니다. 모델을 죽일 수 있는 후보 지점이며, 몇몇 항목은 QFUDS만의 고유 신호도 아닙니다.

1. 표준 WIMP 직접 검출은 계속 무검출일 수 있습니다. 하지만 이것만으로 QFUDS가 유리해지는 것은 아닙니다. 직접 검출 신호가 약하거나 숨겨진 비-QFUDS 암흑물질 모형도 많기 때문입니다.
2. 암흑에너지는 작지만 0이 아닌 시간 변화를 보일 수 있습니다.

$$
w(a) = w_0 + w_a(1-a)
$$

LCDM에서는 $w_0=-1$, $w_a=0$입니다. QFUDS가 차이를 만들려면 $w_0 \simeq -1$이면서 $|w_a|>0$인 작은 편차가 필요합니다.

3. 대규모 구조와 CMB는 거의 LCDM처럼 보여야 합니다.
4. 작은 은하 헤일로는 뾰족한 중심부보다 완만한 중심부를 선호할 수 있지만, 보통 물질 되먹임과 구분해야 합니다.
5. 암흑물질 구조와 보통 물질 구조 사이에 순수한 무충돌 CDM보다 약간 더 강한 상관이 남을 수 있습니다. 하지만 QFUDS 고유의 관계식은 아직 유도되지 않았습니다.
6. 완전한 유니터리 양자 서술에서는 최종 블랙홀 증발 상태가 정보가 전혀 없는 순수 열복사로만 기술되면 안 됩니다. 이것은 양자중력의 정합성 기대이지, 관측된 천체물리 신호는 아닙니다.
7. 블랙홀/화이트홀 잔여체가 있다면 허용 가능한 질량 분포는 좁아야 합니다.

현재 검증하려는 테스트의 핵심은 화이트홀이 아닙니다.
정밀 관측이 계속 $w=-1$을 지지하는지, 아니면 작은 0이 아닌 $w_a$ 쪽으로 움직이는지가 더 중요합니다.

### 폐기 테스트: 먼저 공격해야 할 지점

적대적인 리뷰어라면 이 순서로 공격할 것입니다.

1. 무편차 극한에서 LCDM을 정확히 회복하는가?
2. 같은 유효 매질이 $w \simeq 0$과 $w \simeq -1$을 손흔들기식 설명 없이 만들 수 있는가?
3. 왜 $c_s^2$가 0에 가까운가?
4. CMB 음향 피크를 보존하는가?
5. 물질 파워 스펙트럼을 보존하는가?
6. 기존 통합 암흑 유체나 k-에센스 모형보다 나은 것이 있는가?
7. 잔여체 부문은 실제 예측을 추가하는가, 아니면 이야기용 언어인가?

여기서 실패하면 QFUDS는 이름만 바꾼 용어 교체입니다.

## 블랙홀 해석: 증거가 아닌 재읽기

블랙홀은 QFUDS의 중심 증거가 아닙니다.

관측 기준선은 다음과 같습니다.

```text
많은 대질량 은하, 특히 중심 팽대부를 가진 은하는 중심에 대질량 블랙홀을 가진다.
```

우리 은하 중심 블랙홀과 M87의 블랙홀이 대표적인 예입니다. 존재 자체는 별 궤도 동역학과 사건지평선 스케일 영상으로 관측적으로 확립되어 있습니다. 다만 정확한 형성 경로는 여전히 연구 중입니다. 씨앗 블랙홀 형성, 가스 강착, 은하와 블랙홀 병합, 직접 붕괴, 조밀한 항성계 동역학, 암흑물질 헤일로 안의 형성 같은 표준 천체물리 설명은 여전히 중요합니다.

표준 구조 형성 순서는 다음에 더 가깝습니다.

```text
원시 밀도 요동
-> 차가운 암흑물질 헤일로
-> 가스 냉각, 별 형성, 은하
-> 중심 대질량 블랙홀 씨앗과 강착/병합 성장
```

이것은 블랙홀이 은하를 만든다는 말과 다릅니다. 블랙홀은 특히 활동은하핵 피드백을 통해 숙주 은하에 영향을 줄 수 있지만, 표준 그림에서 은하 형성의 일반적인 출발점은 아닙니다.

QFUDS는 다른 질문을 던질 수 있습니다.

```text
암흑 헤일로가 유효 거품 상이라면,
중심 블랙홀은 그 상의 특수한 고밀도,
고엔트로피, 높은 정보 밀도 영역을 추적하는가?
```

첫 번째 조건은 QFUDS 가정이지 표준 결과가 아닙니다. 표준 우주론은 다음을 말하지 않습니다.

```text
양자 거품 -> 암흑 헤일로
```

QFUDS가 더 강하게 묻는 질문은 다음과 같습니다.

```text
암흑물질이 거품 상이라면,
중심 블랙홀은 그 거품 부문 안의
특수한 압축 지점이나 상전이 지점일 수 있는가?
```

만약 QFUDS 관점으로 해석한다면 다음과 같습니다.

```text
black hole = 가능한 국소 정보 압축 지점
```

더 강하게 말하면:

```text
black hole = 거품 부문의 추측적 상전이 후보 지점
```

이것은 확립된 블랙홀 물리가 아닙니다. 기존 문헌에도 "블랙홀 상전이"라는 표현은 있지만, 보통 반-드 지터(AdS) 공간이나 확장된 블랙홀 열역학 문맥의 Hawking-Page 전이 등을 뜻합니다. 그것이 관측된 은하 중심 블랙홀이 양자 거품 암흑부문의 상전이 지점이라는 뜻은 아닙니다.

비유하면, 큰 도시에는 보통 데이터가 많이 오가는 경로 근처에 큰 데이터 센터가 있을 수 있습니다. 하지만 데이터 센터가 있다고 해서 도시 전체가 그 네트워크 때문에 생겼다는 증거는 아닙니다. 마찬가지로 중심 블랙홀은 QFUDS 언어로 압축 지점이나 경로 지점처럼 읽을 수 있지만, QFUDS를 증명하지는 않으며 표준 블랙홀 형성 물리를 대체하지도 않습니다.

안전한 문장은 다음 정도입니다.

```text
QFUDS는 중심 블랙홀을 거품이 지배하는 헤일로 안의 가능한 정보 압축 지점으로 재해석할 수 있지만, 이것은 추측이며 많은 대질량 은하가 왜 중심 블랙홀을 가지는지는 아직 설명하지 못합니다.
```

### 문서

문서 권한 구조:

- [CLAUDE.md](../../CLAUDE.md)와 [AGENTS.md](../../AGENTS.md)는 에이전트 행동을 정의합니다.
- [Roadmap](../05_next_steps/000_roadmap.md)은 현재 상태, 활성 관문, 막힌 지점의 단일 진실 공급원입니다.
- [Decision Log](decision_log.md)는 결정 이유를 기록합니다.
- [Experiments](../03_experiments/)와 [Results](../04_results/)는 증거를 보관합니다.

유지되는 연구 문서:

- [PROJECT.md](../../PROJECT.md): 문서 관리와 검증 순서
- [docs/README.md](../README.md): 문서 색인과 폴더 지도
- [overview.md](overview.md): 프로젝트 목표, 한계, 모델 계보
- [project_identity.md](project_identity.md): 현재 프로젝트 정체성, 범위, 비목표, 유지-가지 분류, "What We Actually Learned"
- [success_criteria.md](success_criteria.md): 최소/중간/강한 성공 기준과 물리-가지 admission rule
- [qfuds_positioning.md](qfuds_positioning.md): QFUDS 아이디어를 기존 우주론 모델군과 대조
- [concept_survival_audit.md](concept_survival_audit.md): 원래 직관을 현재 증거와 대조 — demotion과 열린 후보
- [decision_log.md](decision_log.md): 이유와 증거가 포함된 시간순 결정 기록
- [verification_guide.md](verification_guide.md): 현재 검증을 다시 실행하고 읽는 방법
- [frontmatter_convention.md](frontmatter_convention.md): 표준 메타데이터 스키마
- [experiment_record_convention.md](experiment_record_convention.md): 실험/결과 섹션 규칙, 요약 정책, postmortem 정책
- [traceability_matrix.md](traceability_matrix.md): 양방향 주장/증거 추적 색인
- [000_qfuds_v0_1_conceptual_origin.md](../02_theory/000_qfuds_v0_1_conceptual_origin.md): 개념 기원 단계 이론 노트
- [000_qfuds_v0_2_two_phase_background.md](../02_theory/000_qfuds_v0_2_two_phase_background.md): 최소 두 상 유효 유체 이론 노트
- [010_qfuds_v0_3_gamma_laws.md](../02_theory/010_qfuds_v0_3_gamma_laws.md): 물리적으로 라벨링된 $\Gamma(a)$ 전달 법칙 이론 노트
- [015_qfuds_v0_15_phase_transfer_physics.md](../02_theory/015_qfuds_v0_15_phase_transfer_physics.md): 상 전달 물리성 감사
- [030_qfuds_phenomenological_perturbations.md](../02_theory/030_qfuds_phenomenological_perturbations.md): 현상론적 섭동 닫힘 이론 노트
- [000_exp_000_lcdm_baseline.md](../03_experiments/000_exp_000_lcdm_baseline.md): 무전달 LCDM 대조군 실행
- [010_exp_001_gamma_scan.md](../03_experiments/010_exp_001_gamma_scan.md): 전달 법칙 스캔
- [015_exp_001_5_phase_transfer_physicality.md](../03_experiments/015_exp_001_5_phase_transfer_physicality.md): 물리성 관문
- [020_exp_002_entropy_information_gate.md](../03_experiments/020_exp_002_entropy_information_gate.md): 엔트로피/정보원 관문
- [030_exp_003_phenomenological_perturbation_closure.md](../03_experiments/030_exp_003_phenomenological_perturbation_closure.md): 섭동 닫힘 감사
- [000_result_000_lcdm_baseline.md](../04_results/000_result_000_lcdm_baseline.md): 무전달 기준 결과
- [010_result_001_gamma_scan.md](../04_results/010_result_001_gamma_scan.md): 결과 해석과 다음 표적
- [015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md): 물리성 결과
- [020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md): 엔트로피/정보원 provenance 결과
- [030_result_003_phenomenological_perturbation_closure.md](../04_results/030_result_003_phenomenological_perturbation_closure.md): 섭동 닫힘 결과
- [000_experiment_summary.md](../04_results/000_experiment_summary.md): 가벼운 실험별 결론 요약과 postmortem 현황
- [000_roadmap.md](../05_next_steps/000_roadmap.md): 검증 단계, 상태, 막힌 지점
- [010_perturbation_gate.md](../05_next_steps/010_perturbation_gate.md): 섭동 관문
- [015_level_1_5_resolution_gate.md](../05_next_steps/015_level_1_5_resolution_gate.md): Level 1.5 통과, 실패, demotion의 증거 기준

역사/출처 노트:

- [004_rough_tanh_numerical_sketch_ko.md](../wiki/lineage/004_rough_tanh_numerical_sketch_ko.md): 24개 체크포인트 거친 `tanh` 수치 탐색 로그
- [005_rough_tanh_thesis_report_ko.md](../wiki/lineage/005_rough_tanh_thesis_report_ko.md): 거친 `tanh` lineage의 논문 형식 종합 — 효과적 적합, 반증 가능 신호, 이론적 천장
- [concept_origin.md](../01_origin/concept_origin.md): 날것의 정보 흐름 아이디어가 QFUDS 질문이 된 과정
- [README.md](../../README.md): 이 문서의 영어판
- [research_program.md](research_program.md): 초록, 검증 로드맵, 폐기 조건
- [900_qfuds_research_report.md](../02_theory/900_qfuds_research_report.md): 적대적 문헌 비교와 수학적 공식화

### 저장소 검사

문서 frontmatter와 교차 링크를 검증합니다.

```bash
python3 scripts/validate_docs.py        # 또는: make validate
```

저장소 상태 권한 일관성을 검사합니다.

```bash
python3 scripts/research_consistency.py  # 또는: make research-audit
```

주요 실험 마일스톤 전에 전체 preflight 감사를 실행합니다.

```bash
make preflight
```

커밋 전에 같은 문서/회귀 검사를 강제하고 싶다면 로컬 git pre-commit hook을 설치합니다.

```bash
make install-git-hooks
```

이 hook은 검증을 실행하기 전에 staged Markdown frontmatter의 `last_updated`
날짜도 자동으로 갱신합니다.

experiment 004 preflight gate를 실행합니다.

```bash
python3 scripts/preflight_exp004.py
```

이 관문은 [030_exp003_record_consistency_gate.md](../05_next_steps/030_exp003_record_consistency_gate.md)에 문서화되어 있으며 `make preflight-exp004`로도 실행됩니다.

### 참조 문헌

아래 링크들은 결이 비슷한 참조 문헌입니다. QFUDS를 증명하지는 않습니다.

- [Hawking evaporation and the Landauer Principle](https://arxiv.org/abs/2407.08777)
- [Landauer Principle Stands up to Quantum Test](https://physics.aps.org/articles/v11/49)
- [Entanglement Wedge Reconstruction and the Information Paradox](https://arxiv.org/abs/1905.08255)
- [Replica wormholes and the black hole interior](https://arxiv.org/abs/1911.11977)
- [Black hole fireworks: black-to-white-hole tunneling](https://arxiv.org/abs/1407.0989)
- [Small black/white hole stability and dark matter](https://arxiv.org/abs/1805.03872)
- [The Thermodynamics of Black Holes](https://link.springer.com/article/10.12942/lrr-2001-6)
- [Coevolution (Or Not) of Supermassive Black Holes and Host Galaxies](https://arxiv.org/abs/1304.7762)
- [The origins of massive black holes](https://www.nature.com/articles/s42254-021-00364-9)
- [Formation of Supermassive Black Hole Seeds](https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/formation-of-supermassive-black-hole-seeds/DA9F246C7A0C6C1C0E057CCBF40220F6)
- [First M87 Event Horizon Telescope Results IV](https://arxiv.org/abs/1906.11241)
- [First Sagittarius A* Event Horizon Telescope Results III](https://arxiv.org/abs/2311.09479)
- [Cold dark matter: Controversies on small scales](https://pmc.ncbi.nlm.nih.gov/articles/PMC4603506/)
- [Direct Detection of Dark Matter: A Critical Review](https://www.mdpi.com/2073-8994/16/2/201)
- [Planck 2018 cosmological parameters](https://arxiv.org/abs/1807.06209)
- [DESI DR2 results guide](https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/)
- [Unified dark fluid with null sound speed](https://arxiv.org/abs/2509.16155)
