# QFUDS / Dorito

Quantum Foam Unified Dark Sector, nicknamed Dorito, is a toy research program in theoretical astrophysics and cosmology.

The goal is not to prove a new theory. The goal is to turn a speculative idea into a small set of equations and prediction candidates that can fail.

## Research Question

Can dark matter and dark energy be two large-scale modes of the same underlying quantum spacetime foam?

The starting hypothesis is:

```text
Dark matter and dark energy are not separate substances.
They may be two macroscopic modes of quantum foam.
```

The clustering mode behaves like dark matter:

```text
rho_foam_wave ~ a^-3
w ~= 0
sound speed ~= 0
```

The nearly uniform residual-pressure mode behaves like dark energy:

```text
rho_foam_residual ~= rho_*
w ~= -1
```

Optional black-hole or white-hole remnants are treated as a subdominant third term, not as the core of the model.

```text
rho_dark
= rho_foam_wave
+ rho_foam_residual
+ rho_remnant
```

## Why This Is Only A Toy Model

The standard Friedmann equation is kept intact. General relativity is not modified at this stage.

```text
H^2 = (8 pi G / 3)
      (rho_b + rho_r + rho_foam_wave + rho_foam_residual + rho_remnant)
      - k c^2 / a^2
```

The model only changes the interpretation of the dark sector:

```text
rho_DM     -> rho_foam_wave
rho_Lambda -> rho_foam_residual
```

That makes this a controlled reinterpretation of the dark sector, not a complete theory. It must reproduce the successes of LCDM before any deviation is worth discussing.

## Physical Picture

Imagine an empty universe-sized box. There are no stars, no gas, and no galaxies. Classical physics would call it empty. Quantum field theory does not. The vacuum still has a lowest-energy state, and that state can fluctuate. With gravity included, spacetime itself may have microscopic fluctuations. This is the broad intuition behind quantum foam.

Dorito adds one assumption:

```text
The microscopic foam almost cancels itself, but not perfectly.
Its long-wavelength collective motion looks like dark matter.
Its nearly uniform leftover pressure looks like dark energy.
```

In plain terms, the foam has waves and a background tension.

The waves can cluster around galaxies. The background tension stays smooth across the universe.

## Minimal Equations

The clustering part must dilute like matter:

```text
rho_foam_wave ~ a^-3
w_foam_wave ~= 0
```

A simple way to model that behavior is an oscillating scalar field:

```text
V(phi) = (1/2) m_eff^2 phi^2
<w_phi> ~= 0
```

This is similar to scalar-field dark matter. The Dorito interpretation is different: `phi` is not introduced as a new particle first. It is treated as an effective collective vibration of spacetime foam.

The residual-pressure part must stay nearly constant:

```text
rho_foam_residual ~= rho_*
w_foam_residual ~= -1
```

The relaxation toy equation is:

```text
d rho_Lambda / dt = -Gamma (rho_Lambda - rho_*)
```

`rho_*` is the small positive equilibrium value left after large vacuum contributions almost cancel.

```text
rho_vac,total = rho_+ + rho_- + rho_*
rho_+ + rho_- ~= 0
rho_* > 0
```

This is not yet a solution to the cosmological constant problem. It only states what a self-regulating foam model would need to do.

## Prediction Candidates

These are not confirmed predictions. They are quantitative targets that can be tested or ruled out.

1. Direct dark matter detection may remain null for WIMP-like particles.

   In this model, dark matter is a collective foam mode, not a standard particle species. Null results from LZ, XENON, and similar nuclear-recoil searches would not prove Dorito, but they would remain compatible with it.

2. Dark energy may vary weakly with time.

   A common observational form is:

   ```text
   w(a) = w_0 + w_a (1 - a)
   LCDM:   w_0 = -1, w_a = 0
   Dorito: w_0 ~= -1, |w_a| > 0 but small
   ```

   DESI-like measurements of expansion history are relevant here, but current hints of evolving dark energy are not enough to reject LCDM.

3. Small galaxy halos may have softer centers than collisionless CDM predicts.

   Flat rotation curves still require:

   ```text
   v^2(r) = G M(r) / r ~= constant
   rho_dark(r) ~ 1 / r^2
   ```

   The possible Dorito deviation is a central flattening:

   ```text
   rho(r) -> rho_0
   ```

   This would have to come from foam self-interaction or pressure-like collective behavior.

4. Dark matter structure may correlate slightly more strongly with baryonic structure.

   In standard LCDM, dark halos form first and baryonic matter falls into them. In Dorito, baryonic matter may deform the foam, and the foam may feed back into the gravitational field. If true, galaxy morphology and halo structure should show a tighter relation than pure collisionless CDM expects.

5. The cosmological constant may be a slow relaxation process.

   If

   ```text
   d rho_Lambda / dt = -Gamma (rho_Lambda - rho_*)
   ```

   is even approximately correct, then high-redshift measurements of `H(z)`, BAO scale, and supernova distances should contain small deviations from a perfect constant Lambda.

6. Black-hole radiation should not be exactly thermal in the full quantum description.

   Dorito treats black holes as information-compression sites for the foam or remnant sector. A white-hole-like remnant would release information only after a long delay. This connects to Page-curve and island-style reasoning, but it is not presently an astrophysical test for ordinary black holes.

7. If white-hole remnants contribute to dark matter, their mass function must be narrow and constrained.

   The simple abundance relation is:

   ```text
   rho_remnant = n_r M_r
   ```

   Heavy remnants face microlensing constraints. Very light remnants face structure-formation, evaporation, and detectability constraints. The real question is not whether remnants can be named, but whether an allowed mass function `f(M)` exists.

## What Would Kill The Model

The model fails if any of the following cannot be satisfied:

- the exact LCDM limit is not recovered when deviations are set to zero;
- the clustering foam mode cannot keep `w ~= 0` and sound speed near zero;
- the residual mode cannot keep `w ~= -1` without fine-tuning only by declaration;
- galaxy halos cannot form with realistic rotation curves;
- CMB, BAO, weak-lensing, or growth data are spoiled;
- remnant abundance violates microlensing or structure-formation bounds;
- the model remains only a new vocabulary for existing unified-dark-fluid or k-essence models.

## Current Assessment

At the current stage, QFUDS/Dorito is not a finished theory.

It is a mathematically organized thought experiment. The safest version is close to known ideas: unified dark fluids, scalar-field dark matter, k-essence, interacting dark energy, and remnant dark matter.

The potentially useful part is the combined test:

```text
one foam origin
two infrared modes
one clustering mode with w ~= 0
one residual-pressure mode with w ~= -1
optional constrained remnants
```

The next step is to make each term predictive enough to fail.

## Repository Contents

- `docs/qfuds_research_report.md`: literature comparison, mathematical formulation, observational tests, and failure modes
- `qfuds/background.py`: two-phase background toy model
- `qfuds/growth.py`: linear growth toy model with a smooth residual phase
- `scripts/run_minimal_model.py`: writes `H(a)`, `Omega(a)`, `w(a)`, and `D(a)` to CSV
- `outputs/*.csv`: generated baseline outputs

## Minimal Run

```bash
python3 scripts/run_minimal_model.py --gamma0 0 --beta 0
python3 scripts/run_minimal_model.py --gamma0 0.03 --beta 5
```

`gamma0 = 0` is the exact LCDM limit. If this limit fails, the rest of the model is not worth testing.

---

# 한국어 설명

QFUDS, 별칭 Dorito는 양자 시공간 foam으로 암흑부문을 다시 해석해 보는 사고실험이다.

목표는 이 아이디어가 맞다고 주장하는 것이 아니다. 목표는 다음 질문을 수식으로 세우고, 실제 관측과 충돌하는지 확인하는 것이다.

```text
암흑물질과 암흑에너지가 서로 다른 물질이 아니라,
같은 quantum foam의 두 가지 거시적 모드일 수 있는가?
```

핵심 그림은 단순하다.

우주는 완전히 빈 공간이 아니라 아주 미세하게 출렁이는 시공간 foam의 바다라고 둔다. 그 바다에는 두 가지 큰 움직임이 있다.

첫째는 뭉치는 파도다. 이 모드는 은하 주변에 모일 수 있어야 하고, 압력이 거의 없어야 한다. 그래서 암흑물질처럼 보이려면 다음 조건이 필요하다.

```text
rho_foam_wave ~ a^-3
w ~= 0
```

둘째는 바닥에 깔린 잔여 압력이다. 이 모드는 거의 균일하게 퍼져 있고, 우주가 커져도 잘 희석되지 않아야 한다. 그래서 암흑에너지처럼 보이려면 다음 조건이 필요하다.

```text
rho_foam_residual ~= rho_*
w ~= -1
```

전체 암흑부문은 이렇게 쓴다.

```text
rho_dark
= rho_foam_wave
+ rho_foam_residual
+ rho_remnant
```

여기서 `rho_remnant`는 black-hole 또는 white-hole remnant가 암흑물질 일부일 가능성을 적은 보조항이다. 핵심은 remnant가 아니라 `foam-wave`와 `foam-residual`이다.

이 모델이 말하는 예측 후보는 다음과 같다.

1. WIMP식 암흑물질 직접 검출은 계속 실패할 수 있다. 암흑물질이 입자 알갱이가 아니라 foam의 집단모드라면 핵반동 신호가 약하거나 없을 수 있다.
2. 암흑에너지는 완벽한 상수가 아니라 아주 약하게 시간 변화할 수 있다.

```text
w(a) = w_0 + w_a(1 - a)
LCDM:   w_0 = -1, w_a = 0
Dorito: w_0 ~= -1, |w_a| > 0 but small
```

3. 작은 은하의 중심부 halo는 완전한 collisionless CDM보다 더 부드러운 core를 가질 수 있다.
4. 암흑물질 분포와 보통물질 분포 사이에 표준 LCDM보다 약간 더 강한 상관관계가 남을 수 있다.
5. 우주상수는 고정된 숫자가 아니라 평형값 주변으로 천천히 돌아가는 과정일 수 있다.

```text
d rho_Lambda / dt = -Gamma (rho_Lambda - rho_*)
```

6. 블랙홀 정보 방출은 완전히 열적인 복사가 아니라, 아주 늦은 시점에 미세한 상관관계를 가져야 한다.
7. white-hole remnant가 암흑물질 일부라면, 허용 가능한 질량분포는 매우 좁아야 한다.

이 사고실험은 다음 조건을 통과해야 한다.

- `gamma0 = 0`에서 정확히 LCDM으로 돌아가야 한다.
- foam-wave는 은하 halo를 만들 만큼 잘 뭉쳐야 한다.
- foam-residual은 우주 가속팽창을 설명할 만큼 균일해야 한다.
- CMB, BAO, 약한 중력렌즈, 구조형성 자료를 망치면 안 된다.
- remnant를 넣는다면 microlensing과 구조형성 제약을 통과해야 한다.

현재 결론은 보수적이다.

Dorito는 아직 완성된 이론이 아니다. 지금은 기존 Friedmann 우주론 위에서 암흑물질과 암흑에너지의 정체를 다르게 해석하는 toy model이다. 의미가 생기려면 `foam-wave`, `foam-residual`, `rho_remnant` 각각이 실제 수치 예측을 내고, 그 예측이 관측으로 틀릴 수 있어야 한다.

