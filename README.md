# Quantum Foam Unified Dark Sector (QFUDS)

## Title

Quantum Foam Unified Dark Sector (QFUDS):  
A Speculative Framework for Dark Matter, Dark Energy, and Information Cycling

## Abstract

We propose a speculative cosmological framework in which dark matter and dark energy emerge as two macroscopic phases of a common microscopic quantum-spacetime foam sector. In contrast to the standard LCDM paradigm, where dark matter and dark energy are treated as fundamentally distinct components, we explore the possibility that both phenomena arise from different infrared manifestations of a single quantum foam medium.

In this framework, the clustering phase behaves as an effectively pressureless component characterized by `w ~= 0` and `c_s^2 ~= 0`, reproducing the large-scale structure formation normally attributed to cold dark matter. The residual phase behaves as a slowly relaxing vacuum-pressure component with `w ~= -1`, providing an effective description of cosmic acceleration. We further interpret black holes as local information-compression nodes and black/white-hole remnants, motivated by loop quantum gravity tunneling scenarios, as subdominant topological defects within the same foam sector.

The model preserves the Friedmann background dynamics of general relativity while suggesting possible deviations from LCDM in the evolution of dark energy, small-scale halo structure, dark-sector clustering behavior, and late-time information correlations associated with black-hole evaporation.

We emphasize that the present work should be regarded as a research program and toy framework rather than a complete physical theory. The primary objective is to formulate a falsifiable set of predictions that can be tested against CMB observations, large-scale structure surveys, halo profiles, dark matter detection experiments, and future precision measurements of the dark-energy equation of state.

## Project Note

Quantum Foam Unified Dark Sector (QFUDS) is a speculative toy framework proposed by Dorito for thinking about dark matter, dark energy, and information flow in cosmology.

This repository is not a claim that the model is correct. It is a workspace for turning an intuition into falsifiable questions.

## Current Validation Stage

The project is currently at Level 1.

```text
Level 0: literature position       done in draft form
Level 1: background toy model      in progress / first version implemented
Level 2: perturbation equations    not complete
Level 3: CLASS or CAMB integration not started
Level 4: CMB comparison            not started
Level 5: matter power comparison   not started
Level 6: DESI/Euclid/Roman tests   not started
```

This matters because QFUDS becomes interesting only after it survives the first numerical checks. The model must first reproduce an LCDM-like background and then preserve CMB and structure-formation observables.

## One-Sentence Thesis

Dark matter and dark energy may not be fundamentally separate substances. They may be two macroscopic phases of the same microscopic quantum-spacetime foam.

```text
dark matter  -> clustering foam phase
dark energy  -> residual vacuum-pressure phase
remnants     -> optional defects in the same foam sector
```

The strongest version of the idea is not "the universe is a white hole." That is too large and too easy to attack.

The stronger version is:

```text
Dark matter + dark energy
= two effective phases of quantum spacetime foam.
```

Black holes and white-hole-like remnants are secondary. They may act as information-compression nodes or topological defects, but they are not the main engine of the model.

## The Thought Flow

The idea started from information, not from dark matter.

```text
Information is physical.
If information cannot simply disappear, what does a black hole do with it?
If a black hole has a time-reversed counterpart, could there be a delayed return channel?
If vacuum foam stores or mediates information, could the dark sector be a large-scale equilibrium of that foam?
```

That produced the first conceptual chain:

```text
information conservation
-> black-hole information problem
-> white-hole-like return channel
-> quantum foam as a medium
-> dark matter as a clustering foam mode
-> dark energy as residual foam pressure
-> black/white-hole remnants as optional defects
```

After pruning the more speculative parts, the useful research question became narrower:

```text
If quantum foam behaves like an effective cosmic medium,
what observational constraint kills it first?
```

## The v0.2 Model

The safer formulation is a unified dark sector inside ordinary general relativity.

```text
rho_dark = rho_QF + rho_rem
```

`rho_QF` is a quantum-foam unified dark fluid. It has two effective pieces:

```text
rho_QF(a) = rho_cluster(a) + rho_residual(a)
```

The clustering piece must behave like cold dark matter:

```text
rho_cluster ~ a^-3
w ~= 0
c_s^2 ~= 0
```

The residual piece must behave like dark energy:

```text
rho_residual ~= rho_*
w ~= -1
```

The optional remnant piece is written as:

```text
rho_rem = integral M f(M) dM
```

It should stay subdominant unless its mass function survives microlensing, CMB, and structure-formation constraints.

## The Key Survival Condition

The most important condition is the effective sound speed.

```text
c_s^2 ~= 0
```

Plain language:

```text
QFUDS foam may leave a pressure that pushes the universe apart,
but during galaxy formation it must still clump almost like pressureless dust.
```

If the foam is too stiff, pressure erases structure. Then the model dies immediately.

## What The Model Tries To Explain

The model tries to connect three strong ideas:

- Unified dark sector: dark matter and dark energy may share one origin.
- Coincidence problem: the dark matter and dark energy densities are comparable near the present epoch.
- Dynamic vacuum energy: the cosmological constant may be a slowly relaxing equilibrium value, not a fixed number placed by hand.

It does not try to replace general relativity at this stage. The Friedmann background is kept.

## Prediction Candidates

These are not verified predictions. They are places where the model can be killed.

1. Standard WIMP direct detection may keep returning null results.
2. Dark energy may show a small but nonzero time evolution.

```text
w(a) = w_0 + w_a(1 - a)
LCDM:   w_0 = -1, w_a = 0
QFUDS: w_0 ~= -1, |w_a| > 0 but small
```

3. Large-scale structure and the CMB must remain almost LCDM-like.
4. Small galaxy halos may prefer cores over sharp cusps, but this must be separated from baryonic feedback.
5. Dark matter and baryonic structure may show a slightly tighter relation than in pure collisionless CDM.
6. Black-hole evaporation should not be exactly thermal in the full quantum description.
7. If black/white-hole remnants exist, the allowed mass function must be narrow.

The hottest near-term test is probably not white holes. It is whether precision surveys keep supporting `w = -1` or move toward a small nonzero `w_a`.

## First Attacks

A hostile reviewer should attack the model in this order:

1. Can it recover LCDM exactly in the zero-deviation limit?
2. Can the same effective medium produce `w ~= 0` and `w ~= -1` without hand-waving?
3. Why is `c_s^2` near zero?
4. Does it preserve the CMB acoustic peaks?
5. Does it preserve the matter power spectrum?
6. Does it improve anything beyond existing unified dark fluid or k-essence models?
7. Does the remnant sector add real predictions, or only story language?

If these fail, the model is only a vocabulary shift.

## Black Holes In This Picture

Black holes are not the central proof of QFUDS.

Observational fact:

```text
Most large galaxies host central supermassive black holes.
```

Examples include the Milky Way's central black hole and the black hole in M87. Their existence is observationally established. Their exact formation route is still an active research question.

The conservative interpretation is:

```text
quantum foam -> dark halo -> galaxy -> central black hole
```

That respects the usual structure-formation picture better than saying black holes create galaxies.

The stronger but still speculative QFUDS question is:

```text
If dark matter is a foam phase,
could central black holes mark special compression or phase-transition sites
inside that foam sector?
```

The speculative QFUDS interpretation proposed by Dorito is:

```text
black hole = local information-compression node
```

or, more boldly:

```text
black hole = possible phase-transition site of the foam sector
```

This is a useful worldbuilding image and a possible research direction, but it is not yet an observational result.

The safe statement is:

```text
QFUDS may reinterpret central black holes as information-compression nodes
within foam-dominated halos, but it does not yet explain why every large
galaxy has one.
```

## Current Status

QFUDS is not a theory yet.

It is a speculative framework with a clearer center than the original white-hole-universe idea:

```text
quantum foam unified dark sector with near-zero sound speed
```

The next meaningful step is not more story. It is a validation roadmap:

```text
background equation
-> perturbation equation
-> CLASS or CAMB implementation
-> CMB comparison
-> matter power spectrum comparison
-> DESI, Euclid, Roman constraints
```

The project becomes physically interesting only if the model survives the first CMB and structure-formation checks.

## Documents

- `docs/concept_origin.md`: how the raw information-flow idea became the QFUDS question
- `docs/research_program.md`: abstract, model v0.2, validation roadmap, and kill criteria
- `docs/qfuds_research_report.md`: adversarial literature comparison and mathematical formulation

---

# 한국어 설명

QFUDS는 Dorito가 제안한, 암흑물질과 암흑에너지를 양자 시공간 foam의 두 가지 거시적 상으로 해석해 보는 사고실험이다.

핵심은 화이트홀이 아니다. 더 강한 핵심은 이것이다.

```text
암흑물질과 암흑에너지는 완전히 다른 두 존재가 아니라,
같은 quantum foam의 서로 다른 거시적 상태일 수 있다.
```

아이디어의 출발은 정보 보존이었다.

```text
정보는 물리적이다.
블랙홀이 정보를 삼키면 그 정보는 어디로 가는가?
블랙홀의 역과정이 있다면 정보가 되돌아오는 통로가 있을 수 있는가?
진공 요동과 정보 보존이 암흑부문의 평형 구조를 만들 수 있는가?
```

이 흐름이 다음 가설로 정리됐다.

```text
암흑물질 = 뭉치는 foam 상
암흑에너지 = 균일하게 남는 foam 잔여 압력
블랙홀 = foam의 정보 압축 노드
화이트홀 잔재 = 선택적 정보 방출 결함
```

현재 가장 안전한 버전은 `QFUDS v0.2`다.

```text
rho_dark = rho_QF + rho_rem
```

여기서 `rho_QF`는 quantum foam unified dark fluid다.

```text
rho_QF(a) = rho_cluster(a) + rho_residual(a)
```

`rho_cluster`는 암흑물질처럼 행동해야 한다.

```text
rho_cluster ~ a^-3
w ~= 0
c_s^2 ~= 0
```

`rho_residual`은 암흑에너지처럼 행동해야 한다.

```text
rho_residual ~= rho_*
w ~= -1
```

가장 중요한 조건은 `c_s^2 ~= 0`이다.

쉽게 말하면:

```text
QFUDS foam은 배경 우주에서는 우주를 밀어내는 압력을 남기지만,
은하 형성에서는 압력 없는 먼지처럼 뭉쳐야 한다.
```

이 조건을 만족하지 못하면 은하 halo와 대규모 구조가 만들어지지 않는다. 그러면 모델은 바로 죽는다.

현재 이 프로젝트는 이론이 아니라 검증 가능한 toy framework다. 다음 단계는 CLASS/CAMB에 넣을 수 있는 배경 방정식과 섭동 방정식을 만들고, CMB와 matter power spectrum에서 LCDM을 얼마나 망가뜨리는지 확인하는 것이다.
