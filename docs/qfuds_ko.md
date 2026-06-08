# Quantum Foam Unified Dark Sector (QFUDS)

언어: [English](../README.md) | Korean

## 이 문서는 뭐냐

QFUDS는 내가 GPT랑 계속 질문을 주고받다가 만든 speculative toy framework다.

처음부터 “새 우주론을 만들자” 같은 목표가 있었던 건 아니다. 원래 관심 있던 주제가 있었다.

```text
정보
엔트로피
블랙홀
호킹복사
양자역학
진공 구조
암흑물질
암흑에너지
```

처음에는 그냥 궁금해서 물었다. 그런데 질문이 계속 이어졌다.

```text
정보를 지우면 열이 난다
-> 그럼 정보는 물리적인 문제다
-> 이거 블랙홀 정보 손실 문제랑 같은 논점 아닌가?
-> 호킹복사에 정보가 섞여 나온다면 복구 가능한가?
-> 복구 가능하다면 역과정은 뭔가?
-> 블랙홀의 시간역전이면 화이트홀 아닌가?
-> 그 정보는 어디에 저장되나?
-> quantum foam 같은 진공 구조가 medium일 수 있나?
-> 암흑물질도 입자라기보다 foam의 collective mode일 수 있나?
-> 암흑에너지는 같은 foam의 residual pressure일 수 있나?
```

이 저장소는 그 사고 흐름을 그냥 말로 끝내지 않고, 수식과 코드로 내려보려는 작업이다.

증명하려는 문서가 아니다. 어디서 죽는지 보려는 문서다.

## GPT랑 어떻게 진행했나

GPT는 정답을 준 도구라기보다, 생각을 튕겨보는 상대였다.

내가 raw 질문을 던졌다. GPT가 관련 개념을 설명했다. 나는 다시 반문했다. 그러면서 한동안 크게 발산했다.

```text
Landauer principle
black-hole information paradox
Hawking radiation
Page curve
island proposal
replica wormhole
CPT / time reversal
white-hole-like return channel
quantum foam
dark matter as a collective mode
dark energy as residual pressure
cosmological constant problem
SF worldbuilding
```

중간에는 일부러 SF 쪽으로도 확장했다. 우주가 거대한 white-hole-like release일 수 있나, black hole / white hole / vacuum foam이 평형을 만들 수 있나 같은 큰 그림도 던졌다.

그런데 그대로 두면 그냥 멋있는 설정이다. 그래서 다시 줄였다.

```text
우주가 문자 그대로 화이트홀이다
```

이 주장은 너무 크고 바로 공격받는다.

살릴 만한 중심은 이쪽이었다.

```text
암흑물질과 암흑에너지가
완전히 별개의 두 성분이기보다
하나의 quantum foam sector에서 나온
두 effective mode일 수 있나?
```

여기서부터 QFUDS가 됐다.

## 핵심 아이디어

표준 LCDM에서는 암흑물질과 암흑에너지를 따로 둔다.

QFUDS는 이렇게 묻는다.

```text
같은 underlying medium이
작은 스케일에서는 clump하고
큰 스케일에서는 smooth pressure처럼 보일 수 있나?
```

최소 버전은 이렇다.

```text
rho_dark = rho_cluster + rho_residual + rho_rem
```

`rho_cluster`:

```text
dark matter-like mode
rho_cluster ~ a^-3
w ~= 0
c_s^2 ~= 0
```

은하 halo와 structure formation에 들어가려면 거의 cold dark matter처럼 움직여야 한다.

`rho_residual`:

```text
dark energy-like mode
rho_residual ~= rho_*
w ~= -1
```

우주 전체에 거의 균일하게 남는 residual vacuum pressure처럼 행동해야 한다.

`rho_rem`:

```text
optional remnant sector
rho_rem = integral M f(M) dM
```

black/white-hole remnant는 메인 엔진이 아니다. 정보 저장소나 topological defect 후보 정도로만 둔다.

## 내가 버린 것

처음엔 이런 그림이 있었다.

```text
우리 우주가 거대한 white-hole-like release일 수 있다
블랙홀은 흡입
화이트홀은 방출
quantum foam은 중간 medium
암흑물질은 진공 떨림의 sparse energy
우주상수는 남은 residual pressure
```

이건 직관으로는 재밌다. SF 설정으로도 좋다.

하지만 물리 모델로는 너무 넓다. 그래서 중심에서 내렸다.

현재 연구 버전은 이것만 본다.

```text
QFUDS가 LCDM이 이미 맞춘 background와 structure를 망치지 않으면서
dark matter-like mode와 dark energy-like mode를
하나의 dark sector 안에서 만들 수 있나?
```

## 첫 번째 검증에서 나온 결론

첫 번째 hostile review 결과는 꽤 중요했다.

판정은 이거였다.

```text
QFUDS는 지금 형태로는 새 이론이 아니다.
보수적으로 쓰면 LCDM으로 정확히 줄어든다.
phase transfer를 넣으면 interacting dark energy,
unified dark fluid, k-essence 계열과 매우 가까워진다.
```

이건 실패가 아니다. 오히려 위치가 잡힌 것이다.

새로우려면 이름을 새로 붙이는 것만으로는 안 된다. `quantum foam`, `phase`, `information-compression node` 같은 단어가 실제 변수와 방정식에 붙어야 한다.

그래서 다음 질문은 `Gamma(a)`가 됐다.

```text
d rho_A / d ln a + 3 rho_A = -Gamma(a) rho_A
d rho_B / d ln a           =  Gamma(a) rho_A
```

`Gamma(a)`는 clustering phase가 residual phase로 넘어가는 rate다.

`Gamma(a) = 0`이면 LCDM이다.

그래서 QFUDS가 뭔가 다르려면 `Gamma(a)`를 그냥 fitting function으로 두면 안 된다. 물리량에 묶어야 한다.

후보는 이런 것들이다.

```text
Gamma(a) ∝ d ln D / d ln a
Gamma(a) ∝ d f_coll / d ln a
Gamma(a) ∝ d S_BH / d ln a
Gamma(a) ∝ cosmic star formation history
Gamma(a) ∝ horizon entropy / holographic bound
```

이게 v0.3의 핵심이다.

## 지금 레포의 위치

현재 상태는 이 정도다.

```text
Level 0: 아이디어 위치 확인
Level 1: background toy model
Level 2: Gamma(a) toy laws
Level 3: perturbation equation 미완성
Level 4: CLASS/CAMB integration 시작 전
Level 5: CMB / matter power spectrum 비교 시작 전
```

지금은 아직 이론이 아니다. toy model이다.

물리적으로 흥미로워지려면 최소한 이것들을 통과해야 한다.

```text
rho_A > 0
rho_B > 0
early dark energy가 너무 크면 안 됨
matter domination을 망치면 안 됨
CMB-era H(a)가 LCDM과 크게 다르면 안 됨
structure growth를 망치면 안 됨
c_s^2 ~= 0이 유지돼야 함
```

## 핵심 생존 조건

제일 중요한 건 `c_s^2 ~= 0`이다.

암흑물질처럼 보이려면 clustering phase가 pressure support를 거의 만들면 안 된다.

쉽게 말하면:

```text
너무 탱탱하면 은하 halo가 안 생긴다.
```

dark energy 쪽은 `w ~= -1`에 가까워야 한다.

문제는 하나의 sector가 이 둘을 동시에 만들어야 한다는 점이다.

```text
small scale: clumpy, dust-like
large scale: smooth, vacuum-like
```

여기서 실패하면 QFUDS는 그냥 단어 바꾸기다.

## 내가 보는 핵심 질문

현재 제일 중요한 질문은 이것이다.

```text
암흑물질과 암흑에너지가 같은 foam의 두 상이라는 말만으로는 부족하다.
두 상 사이의 전환율 Gamma(a)가
블랙홀 엔트로피, structure growth, horizon entropy 같은
실제 물리량에 묶일 수 있는가?
```

이게 되면 연구할 만하다.

안 되면 LCDM 또는 기존 interacting dark sector의 다른 이름이다.

## 비과학자용 짧은 주석

`Landauer principle`:
정보를 지우는 일에도 최소 열 비용이 든다는 원리.

`black-hole information problem`:
블랙홀이 정보를 삼키고 호킹복사로 증발하면 정보가 사라지는지 묻는 문제.

`Hawking radiation`:
블랙홀이 양자 효과로 아주 천천히 에너지를 내보내는 과정.

`Page curve / island`:
블랙홀 정보가 완전히 사라지지 않는다는 쪽으로 계산을 맞춰주는 반고전적 도구.

`quantum foam`:
Planck scale에서 시공간이 매끈하지 않고 요동할 수 있다는 그림.

`dark matter mode`:
foam이 은하 주변에서 clump해서 중력 효과를 내는 모드.

`dark energy mode`:
foam이 우주 전체에서 smooth residual pressure처럼 보이는 모드.

`sound speed`:
유효 매질이 얼마나 압력으로 버티는지 보는 값. dark matter 역할을 하려면 거의 0이어야 한다.

## 문서

- `docs/concept_origin.md`: 사고 흐름 원점
- `docs/research_program.md`: research program과 validation roadmap
- `docs/qfuds_research_report.md`: 문헌 비교와 수학적 formulation
- `docs/qfuds_v0_3_gamma_laws.md`: `Gamma(a)` phase-transfer law 실험

## 참고 anchor

이 링크들은 QFUDS를 증명하지 않는다. 근처에 있는 실제 연구 축이다.

- [Hawking evaporation and the Landauer Principle](https://arxiv.org/abs/2407.08777)
- [Entanglement Wedge Reconstruction and the Information Paradox](https://arxiv.org/abs/1905.08255)
- [Replica wormholes and the black hole interior](https://arxiv.org/abs/1911.11977)
- [Black hole fireworks: black-to-white-hole tunneling](https://arxiv.org/abs/1407.0989)
- [Small black/white hole stability and dark matter](https://arxiv.org/abs/1805.03872)
- [Planck 2018 cosmological parameters](https://arxiv.org/abs/1807.06209)
- [DESI DR2 results guide](https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/)
- [Unified dark fluid with null sound speed](https://arxiv.org/abs/2509.16155)
