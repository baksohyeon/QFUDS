---
doc_id: qfuds_korean_overview
title: Quantum Foam Unified Dark Sector (QFUDS)
doc_type: reference
stage: "reference"
status: reference
evidence_role: reference
depends_on:
  - project_overview
next_gate: resolve Level 1.5 before Level 2
last_updated: 2026-06-08
---

# Quantum Foam Unified Dark Sector (QFUDS)

언어: [English](../README.md) | Korean

## 제목

Quantum Foam Unified Dark Sector (QFUDS):
암흑물질, 암흑에너지, 정보 순환을 하나의 quantum foam 관점에서 묶어보는 speculative toy framework

## 초록

이 저장소는 암흑물질과 암흑에너지가 같은 미시적 quantum spacetime foam sector의 서로 다른 거시적 상으로 나타날 수 있는지 탐색합니다. 표준 LCDM에서는 암흑물질과 암흑에너지를 서로 다른 성분으로 둡니다. QFUDS는 그 둘이 하나의 quantum foam medium이 큰 스케일에서 다르게 보인 결과일 수 있는지 묻습니다.

이 그림에서 clustering phase는 거의 압력이 없는 성분처럼 행동해야 합니다. 수식으로는 `w ~= 0`, `c_s^2 ~= 0`에 가까워야 하고, 그래야 cold dark matter처럼 은하와 대규모 구조 형성에 참여할 수 있습니다. residual phase는 `w ~= -1`에 가까운 느린 vacuum-pressure 성분처럼 행동하여 우주의 가속팽창을 설명해야 합니다. 블랙홀은 local information-compression node로 보고, black/white-hole remnant는 같은 foam sector 안의 부차적 topological-defect 후보로만 둡니다.

이 모델은 일반상대론의 Friedmann background는 유지합니다. 대신 dark energy evolution, 작은 스케일의 halo 구조, dark-sector clustering, 블랙홀 증발과 관련된 late-time information correlation에서 LCDM과 다른 신호가 가능한지 봅니다.

이 문서는 완성된 물리 이론이 아니라 research program이자 toy framework입니다. 목적은 원래 직관을 CMB, 대규모 구조, halo profile, dark matter direct detection, dark-energy equation-of-state 관측으로 반박 가능한 질문으로 바꾸는 것입니다.

### 개념 주석

`w`는 pressure와 energy density의 비율입니다. `w ~= 0`이면 먼지처럼 뭉치기 쉽고, `w ~= -1`이면 우주 전체를 밀어내는 암흑에너지처럼 행동합니다.

`c_s^2`는 effective sound speed squared입니다. 쉽게 말하면 이 암흑 매질이 얼마나 탱탱한지입니다. 너무 탱탱하면 은하 주변에 못 뭉칩니다. QFUDS가 살아남으려면 clustering phase는 거의 압력 없는 먼지처럼 움직여야 합니다.

## 프로젝트 노트

Quantum Foam Unified Dark Sector, 줄여서 QFUDS는 Dorito가 떠올린 암흑부문 사고실험입니다.

이 저장소는 “이 모델이 맞다”는 선언이 아닙니다. 호기심에서 나온 직관을 수식, 검증 조건, toy code로 낮춰보는 작업 공간입니다.

## 출발점: 정보 삭제에서 QFUDS까지

QFUDS는 처음부터 우주론으로 시작하지 않았습니다. 시작은 정보 열역학이었습니다.

```text
정보를 지우는 일은 공짜가 아니다.
1비트의 정보를 지우는 데에는 최소한의 열역학적 비용이 있다.
그 비용은 열로 나타나고, 우주의 엔트로피 장부에 남는다.
```

이 지점에서 정보는 단순한 이름표가 아니게 됩니다. 데이터를 지우는 일이 열과 엔트로피를 바꾼다면, 정보는 에너지, 물질, 시공간과 같은 물리 장부 안에 들어갑니다.

그다음 자연스럽게 블랙홀이 떠올랐습니다. 정보에 물리적 비용이 있다면, 블랙홀은 데이터를 그냥 버리는 쓰레기통처럼 취급할 수 없습니다. 블랙홀 안으로 들어간 정보가 어디에 인코딩되는지, 호킹복사가 그 정보를 극도로 뒤섞인 형태로 되돌릴 수 있는지, 그리고 블랙홀 증발이 양자역학의 unitarity와 양립 가능한지가 다음 질문이 됩니다.

원래 사고 흐름은 이랬습니다.

```text
information
-> data
-> entropy
-> black holes
-> Hawking radiation
-> scrambled information recovery
-> reverse-process intuition
-> time-reversal or CPT counterpart
-> quantum foam
-> unified dark sector
```

처음에는 이미지가 훨씬 컸습니다.

```text
우리 우주 자체가 거대한 white-hole-like release처럼 행동하는 것은 아닐까?
```

이 이미지는 좋은 불씨였지만, 과학적 주장으로 세우기에는 너무 큽니다. 그래서 가지치기를 했고, 더 강한 중심은 이쪽으로 줄었습니다.

```text
Dark matter + dark energy
= two effective phases of quantum spacetime foam.
```

이 관점에서 암흑물질은 clustering phase입니다. 은하 주변에 뭉치고, 거의 압력 없는 물질처럼 행동해야 하는 부분입니다. 암흑에너지는 residual pressure phase입니다. 우주 전체에 매끈하게 남아서 가속팽창을 만드는 부분입니다. 블랙홀과 white-hole-like remnant는 정보 흐름이나 결함 구조로 남지만, 모델의 중심 엔진은 아닙니다.

## 발산, 수렴, 검증

이 저장소의 핵심은 가설 하나만이 아닙니다. 그 가설까지 가는 사고 과정 자체가 중요합니다.

첫 단계는 발산이었습니다. 작은 Landauer prompt가 여러 질문으로 뻗었습니다.

```text
정보 삭제가 열을 남긴다면,
정보는 물리적 비용을 가진다.

정보가 물리적 비용을 가진다면,
블랙홀 증발은 단순한 폐기 과정으로 볼 수 없다.

블랙홀이 정보를 처리한다면,
역과정이나 delayed-return channel을 묻는 것이 자연스럽다.

블랙홀과 진공 구조가 같은 정보 문제의 일부라면,
암흑부문도 그 구조가 우주 스케일에서 드러난 것일 수 있다.
```

이 단계는 일부러 넓게 열어둔 단계였습니다. 블랙홀은 정보 압축기처럼 보였고, white-hole-like remnant는 delayed outlet처럼 보였고, 우주는 release process처럼 보였고, vacuum fluctuation은 sparse structure처럼 보였습니다. 우주 가속팽창도 residual pressure라는 식으로 연결됐습니다.

중간에서 중요한 고리는 단순히 “블랙홀이니까 화이트홀”이 아니었습니다. 핵심은 복구 가능성과 비용이었습니다.

```text
호킹복사가 정보를 극도로 뒤섞인 형태로 담고 있다면,
이론적으로 완벽한 quantum decoder가 그 정보를 복구할 수 있을까?

unitarity가 복구 가능성을 허용하지만,
계산 복잡도가 그것을 막는다면,
정보는 파괴된 것이 아니라 decoding cost 뒤에 숨은 것이다.

완전한 시간역전 과정이 있다면,
물리적으로 무엇이 그 역할을 할 수 있을까?
```

여기서 reverse-process 이미지가 들어왔습니다. white hole, black/white-hole remnant, CPT-like symmetry, replica wormhole, island idea는 증거가 아니라 질문을 좁히는 장치였습니다. 블랙홀이 ordinary matter보다 큰 information-processing sector를 가리키는지 묻기 위한 중간 다리였습니다.

그다음 암흑물질 쪽으로 넘어간 직관은 별도로 중요합니다.

```text
암흑물질이 꼭 ordinary particle이어야 할까?
혹시 vacuum이나 spacetime foam의 energy-like collective excitation일 수 없을까?
거의 빈 공간의 구조에서 생긴 sparse gravitational trace라면 어떨까?
```

여기서 plasma-like라는 말은 비유입니다. QFUDS는 암흑물질이 전자기 플라즈마라고 주장하지 않습니다. 핵심은 collective behavior입니다. 어떤 매질은 개별 입자로 잡히기보다 큰 스케일의 모드로 더 잘 보일 수 있습니다.

두 번째 단계는 수렴이었습니다. 가장 큰 이미지를 잘라내고, 끝까지 남는 질문을 골랐습니다.

```text
암흑물질과 암흑에너지를
같은 quantum-foam medium의 두 effective mode로 볼 수 있는가?
```

이 질문은 원래 이미지보다 작습니다. 대신 훨씬 더 위험합니다. 하나의 sector가 구조 형성 스케일에서는 dust-like하게 보이고, 우주 배경 스케일에서는 vacuum-like하게 보여야 하기 때문입니다.

세 번째 단계는 검증 압력이었습니다. dark-sector toy model로 쓰는 순간, 더는 은유로 버틸 수 없습니다. 평범한 우주론 관측 앞에 세워야 합니다.

```text
zero-deviation limit에서 LCDM을 회복하는가?
clustering phase가 c_s^2 ~= 0을 유지할 수 있는가?
CMB acoustic peak를 망가뜨리지 않는가?
matter power spectrum을 보존하는가?
realistic halo를 만들 수 있는가?
remnant sector가 compact-object constraint를 통과하는가?
```

그래서 이 저장소가 생겼습니다. 아이디어를 적어두는 데서 끝나는 것이 아니라, 확인하고, 제약하고, 필요하면 죽일 수 있는 형태로 밀어 넣기 위한 저장소입니다.

## 가지치기된 것

초기 아이디어에는 여러 가지가 섞여 있었습니다.

```text
black holes as information processors
white-hole-like reverse channels
the universe as a white-hole-like release
vacuum fluctuations as sparse dark structure
cosmic acceleration as residual vacuum pressure
```

이 저장소는 그중 변수, 방정식, 테스트로 낮출 수 있는 부분만 남깁니다. 현재 연구 버전은 이것이 아닙니다.

```text
우주는 문자 그대로 화이트홀이다.
```

현재 연구 버전은 이것입니다.

```text
quantum-foam unified dark sector가
암흑물질과 암흑에너지로 설명되는 관측 효과를
재현할 수 있는가?
```

기준은 단순합니다.

```text
이 아이디어를 틀릴 수 있을 만큼 정확하게 만들 수 있는가?
```

그럴 수 없다면 이야기에 머뭅니다. 그럴 수 있다면 CMB, structure formation, halo profile, dark-energy measurement로 공격받을 수 있는 toy framework가 됩니다.

## 이 저장소가 존재하는 이유

이 저장소는 발산한 직관이 연구 프로그램으로 바뀌는 과정을 기록합니다.

```text
intuition
-> pruning
-> hypothesis
-> toy equations
-> kill criteria
-> code and future Boltzmann tests
```

목표는 QFUDS를 증명하는 것이 아닙니다. 목표는 무엇이 이 모델을 가장 먼저 죽이는지 찾는 것입니다. 혹은 살아남는 버전을 LCDM, unified dark fluid, k-essence, interacting dark energy, scalar-field dark matter, black/white-hole remnant model과 비교할 수 있을 만큼 좁히는 것입니다.

현재 상태는 QFUDS v0.15 / Level 1.5 phase-transfer physicality 단계입니다. `exp_000` baseline, `exp_001` Gamma-law scan, `exp_002` entropy/information gate를 통해 어떤 transfer law가 바로 죽는지, 어떤 형태가 알려진 interacting dark energy로 환원되는지 정리했습니다. 다만 `exp_002`는 physical evidence가 아니라 provenance로 격하되었습니다. perturbation equation, CLASS/CAMB integration, CMB power-spectrum comparison, matter-power comparison은 아직 시작할 수 없습니다.

## 현재 검증 단계

```text
Level 0: literature position       draft form 완료
Level 1: background validation     완료
  exp_000: LCDM baseline
  exp_001: Gamma-law background scan
  exp_002: entropy/information gate, provenance only
QFUDS v0.15 / Level 1.5: phase-transfer physicality 진행 중
Level 2: perturbation equations    blocked
Level 3: CLASS or CAMB integration 시작 전
Level 4: CMB comparison            시작 전
Level 5: matter power comparison   시작 전
Level 6: DESI/Euclid/Roman tests   시작 전
```

QFUDS는 Level 1.5에서 `Gamma(a)`의 물리적 의미를 통과한 뒤에야 perturbation으로 넘어갈 수 있습니다. `exp_001`과 `exp_002`는 background-level 작업입니다. 특히 `exp_002`는 선행 물리 조건 없이 돌린 proxy scan이므로 CMB나 structure-formation viability는 물론 phase-transfer evidence도 주장할 단계가 아닙니다.

## 한 문장 thesis

암흑물질과 암흑에너지는 완전히 다른 두 물질이 아닐 수 있습니다. 같은 microscopic quantum-spacetime foam이 거시적으로 다르게 나타난 두 상일 수 있습니다.

```text
dark matter  -> clustering foam phase
dark energy  -> residual vacuum-pressure phase
remnants     -> optional defects in the same foam sector
```

가장 강한 버전은 “우주는 화이트홀이다”가 아닙니다. 그 말은 너무 크고 너무 쉽게 공격받습니다.

더 강한 버전은 이것입니다.

```text
Dark matter + dark energy
= two effective phases of quantum spacetime foam.
```

블랙홀과 white-hole-like remnant는 부차적인 구조입니다. information-compression node나 topological defect로 볼 수는 있지만, 모델의 중심 엔진은 아닙니다.

## 사고 흐름

아이디어는 암흑물질이 아니라 정보에서 시작했습니다.

```text
Information is physical.
정보가 그냥 사라질 수 없다면, 블랙홀은 그 정보를 어떻게 처리하는가?
블랙홀에 시간역전 counterpart가 있다면 delayed return channel이 가능한가?
vacuum foam이 정보를 저장하거나 매개한다면 dark sector는 그 foam의 large-scale equilibrium일 수 있는가?
```

처음 나온 conceptual chain은 다음과 같습니다.

```text
information conservation
-> black-hole information problem
-> white-hole-like return channel
-> quantum foam as a medium
-> dark matter as a clustering foam mode
-> dark energy as residual foam pressure
-> black/white-hole remnants as optional defects
```

각 단계는 증명이 아닙니다. 질문의 초점이 이동한 것입니다.

```text
Landauer:
정보는 물리적 비용을 가진다.

black-hole information:
블랙홀에 들어간 정보는 어디에 인코딩되는가?

white-hole-like return:
블랙홀의 시간역전 구조가 있다면,
return channel을 remnant나 defect로 모델링할 수 있는가?

quantum foam:
시공간 자체가 미시적으로 요동한다면,
그 요동이 dark-sector behavior를 실어 나르는 매질일 수 있는가?

dark matter:
긴 파장 foam mode가 w ~= 0, c_s^2 ~= 0으로 뭉칠 수 있는가?

dark energy:
다른 foam mode가 w ~= -1의 smooth residual pressure로 남을 수 있는가?

QFUDS:
이 둘을 하나의 dark sector의 두 effective phase로 볼 수 있는가?
```

가장 speculative한 부분을 잘라낸 뒤 남은 질문은 더 좁아졌습니다.

```text
quantum foam이 effective cosmic medium처럼 행동한다면,
어떤 관측 제약이 이 모델을 가장 먼저 죽이는가?
```

## 현재 작업 가설: v0.2 모델

더 안전한 공식화는 일반상대론 안의 unified dark sector입니다.

```text
rho_dark = rho_QF + rho_rem
```

`rho_QF`는 quantum-foam unified dark fluid입니다. 두 effective piece를 가집니다.

```text
rho_QF(a) = rho_cluster(a) + rho_residual(a)
```

clustering piece는 cold dark matter처럼 행동해야 합니다.

```text
rho_cluster ~ a^-3
w ~= 0
c_s^2 ~= 0
```

residual piece는 dark energy처럼 행동해야 합니다.

```text
rho_residual ~= rho_*
w ~= -1
```

optional remnant piece는 이렇게 둡니다.

```text
rho_rem = integral M f(M) dM
```

이 항은 microlensing, CMB, structure-formation constraint를 통과하기 전까지 subdominant로 두는 것이 안전합니다.

### 개념 주석

`rho_cluster ~ a^-3`은 우주가 커질수록 밀도가 부피에 따라 희석된다는 뜻입니다. 보통 물질이나 cold dark matter가 이런 식으로 줄어듭니다.

`rho_residual ~= rho_*`는 거의 일정하게 남는 residual vacuum density를 뜻합니다. 이것이 `w ~= -1`로 보이면 암흑에너지처럼 우주 가속팽창을 설명할 수 있습니다.

## 핵심 생존 조건

가장 중요한 조건은 effective sound speed입니다.

```text
c_s^2 ~= 0
```

쉽게 말하면:

```text
QFUDS foam은 배경 우주에서는 우주를 밀어내는 압력을 남길 수 있지만,
은하 형성 단계에서는 압력 없는 먼지처럼 뭉쳐야 한다.
```

foam이 너무 stiff하면 압력이 구조 형성을 지워버립니다. 그러면 모델은 바로 죽습니다.

## 이 모델이 설명하려는 것

QFUDS가 묶으려는 핵심은 세 가지입니다.

1. Unified dark sector: 암흑물질과 암흑에너지가 같은 origin을 가질 수 있는가.
2. Coincidence problem: 왜 현재 우주에서 암흑물질과 암흑에너지 비율이 비슷한 시기를 사는가.
3. Dynamic vacuum energy: cosmological constant가 손으로 넣은 고정 숫자가 아니라 느리게 relax하는 equilibrium value일 수 있는가.

이 단계에서는 일반상대론을 바꾸려 하지 않습니다. Friedmann background는 유지합니다.

## 예측 후보

아래 항목은 검증된 예측이 아닙니다. 모델을 죽일 수 있는 후보 지점입니다.

1. 표준 WIMP direct detection은 계속 null일 수 있습니다.
2. Dark energy는 아주 작지만 0이 아닌 time evolution을 보일 수 있습니다.

```text
w(a) = w_0 + w_a(1 - a)
LCDM:   w_0 = -1, w_a = 0
QFUDS: w_0 ~= -1, |w_a| > 0 but small
```

3. Large-scale structure와 CMB는 거의 LCDM-like해야 합니다.
4. 작은 은하 halo는 sharp cusp보다 core를 선호할 수 있지만, baryonic feedback과 구분해야 합니다.
5. Dark matter 구조와 baryonic structure 사이에 pure collisionless CDM보다 약간 더 강한 상관이 남을 수 있습니다.
6. 완전한 quantum description에서 black-hole evaporation은 정확히 thermal하기만 해서는 안 됩니다.
7. black/white-hole remnant가 있다면 허용 가능한 mass function은 매우 좁아야 합니다.

가까운 테스트의 핵심은 white hole이 아닙니다. `w = -1`이 계속 정밀하게 지지되는지, 아니면 작은 nonzero `w_a` 쪽으로 움직이는지가 더 중요합니다.

## 먼저 공격해야 할 지점

적대적인 리뷰어라면 이 순서로 공격할 것입니다.

1. zero-deviation limit에서 LCDM을 정확히 회복하는가?
2. 같은 effective medium이 `w ~= 0`과 `w ~= -1`을 hand-waving 없이 만들 수 있는가?
3. 왜 `c_s^2`가 0에 가까운가?
4. CMB acoustic peak를 보존하는가?
5. matter power spectrum을 보존하는가?
6. 기존 unified dark fluid나 k-essence보다 나은 것이 있는가?
7. remnant sector는 실제 예측을 추가하는가, 아니면 story language인가?

여기서 실패하면 QFUDS는 이름만 바꾼 vocabulary shift입니다.

## 비과학자용 주석

```text
Information erasure:
기억이나 데이터를 지우는 일도 우주의 열/엔트로피 장부에 비용을 남긴다.

Hawking radiation:
블랙홀이 아주 천천히 에너지를 내보내며 증발할 수 있다는 이론적 과정.
정보가 완전히 사라지는지, 극도로 뒤섞여 나오는지가 핵심 문제다.

Quantum foam:
시공간이 아주 작은 스케일에서 완전히 매끈하지 않고 요동할 수 있다는 가설적 그림.

Dark matter mode:
foam의 뭉치는 파도. 은하 주변에서 중력을 더해주는 역할을 해야 한다.

Dark energy mode:
foam의 균일한 잔여 압력. 우주 전체의 가속팽창을 설명해야 한다.

Sound speed:
이 유효 매질이 얼마나 탱탱한지를 나타내는 값.
너무 탱탱하면 못 뭉치고, 못 뭉치면 암흑물질 역할을 못 한다.

White-hole remnant:
블랙홀의 역과정이나 정보 방출 통로를 떠올리게 하는 speculative한 결함 구조.
현재 QFUDS에서는 메인 주장이 아니라 부차적 가능성이다.
```

## 이 그림에서 블랙홀의 위치

블랙홀은 QFUDS의 중심 증거가 아닙니다.

관측 사실:

```text
대부분의 큰 은하는 중심에 supermassive black hole을 가진다.
```

우리 은하 중심 블랙홀과 M87의 블랙홀이 대표적인 예입니다. 존재 자체는 관측적으로 확립되어 있습니다. 다만 정확한 형성 경로는 여전히 연구 중입니다.

보수적인 해석은 이렇습니다.

```text
quantum foam -> dark halo -> galaxy -> central black hole
```

이 순서는 블랙홀이 은하를 만든다고 말하는 것보다 표준 구조 형성 그림을 더 잘 존중합니다.

QFUDS가 더 강하게 묻는 질문은 이것입니다.

```text
dark matter가 foam phase라면,
central black hole은 그 foam sector 안의
특수한 compression site나 phase-transition site일 수 있는가?
```

speculative한 해석은 다음과 같습니다.

```text
black hole = local information-compression node
```

더 강하게 말하면:

```text
black hole = possible phase-transition site of the foam sector
```

이것은 좋은 worldbuilding 이미지이자 연구 방향이 될 수 있지만, 아직 관측 결과는 아닙니다.

안전한 문장은 이 정도입니다.

```text
QFUDS는 central black hole을 foam-dominated halo 안의
information-compression node로 재해석할 수 있지만,
큰 은하마다 왜 하나씩 있는지를 아직 설명하지는 못한다.
```

## 현재 상태

QFUDS는 아직 이론이 아닙니다.

원래 white-hole-universe 이미지보다 더 선명한 중심은 이것입니다.

```text
quantum foam unified dark sector with near-zero sound speed
```

다음 의미 있는 단계는 더 많은 이야기가 아니라 QFUDS v0.15 / Level 1.5 physicality gate입니다.

```text
background equation
-> Gamma(a) transfer-law filters
-> QFUDS v0.15 / Level 1.5 phase-transfer physicality
-> perturbation equation
-> CLASS or CAMB implementation
-> CMB comparison
-> matter power spectrum comparison
-> DESI, Euclid, Roman constraints
```

이 프로젝트는 CMB와 structure-formation 검사를 처음 통과한 뒤에야 물리적으로 흥미로워집니다.

## 문서

- `docs/01_origin/concept_origin.md`: 정보 흐름에서 QFUDS 질문까지 어떻게 이동했는지
- `docs/00_project/research_program.md`: abstract, validation roadmap, kill criteria
- `docs/00_project/verification_guide.md`: 현재 검증을 다시 실행하고 출력물을 읽는 법
- `docs/03_experiments/020_exp_002_entropy_information_gate.md`: experiment 002 entropy/information-source 실험 정의
- `docs/02_theory/900_qfuds_research_report.md`: 적대적 문헌 비교와 수학적 formulation
- `docs/04_results/010_result_001_gamma_scan.md`: experiment 001 `Gamma(a)` transfer-law 진단과 viability table
- `docs/04_results/020_result_002_entropy_information_gate.md`: experiment 002 entropy/information-source 결과와 hostile verdict

## 참고 anchor

아래 링크들은 QFUDS를 증명하지 않습니다. 다만 근처에 있는 실제 연구 축을 잡아주는 anchor입니다.

- [Hawking evaporation and the Landauer Principle](https://arxiv.org/abs/2407.08777)
- [Entanglement Wedge Reconstruction and the Information Paradox](https://arxiv.org/abs/1905.08255)
- [Replica wormholes and the black hole interior](https://arxiv.org/abs/1911.11977)
- [Black hole fireworks: black-to-white-hole tunneling](https://arxiv.org/abs/1407.0989)
- [Small black/white hole stability and dark matter](https://arxiv.org/abs/1805.03872)
- [Planck 2018 cosmological parameters](https://arxiv.org/abs/1807.06209)
- [DESI DR2 results guide](https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/)
- [Unified dark fluid with null sound speed](https://arxiv.org/abs/2509.16155)
