---
doc_id: audit_2026_06_12_effective_phase_fraction_scaffold
title: "2026-06-12 Effective Phase-Fraction Scaffold"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_12_foam_sector_to_gamma_derivation_feasibility_result
  - audit_2026_06_12_foam_sector_to_gamma_derivation_feasibility_plan
  - audit_2026_06_11_known_model_distinction_audit_result
  - audit_2026_06_11_level2b_eligibility_review_observer_mode
  - roadmap
next_gate: no physical interpretation until a foam-sector state variable and perturbation closure are specified
last_updated: 2026-06-12
---

# 2026-06-12 Effective Phase-Fraction Scaffold

## Purpose

This document records a weak mathematical scaffold for the original
single-sector phase-fraction intuition:

```text
one effective dark sector
-> phase-A / phase-B fraction
-> effective equation of state
-> analytic background density
```

This is intentionally weaker than the forward foam-sector derivation requested
in the [Foam-Sector-to-Gamma Feasibility Result](050_foam_sector_to_gamma_derivation_feasibility_result.md).

It does not derive a foam-sector state variable.

It does not derive a physical phase transition.

It does not use or derive `Gamma(a)`.

It does not derive `Q^nu`.

It does not derive `delta Q`.

It does not claim QFUDS support.

It does not claim novelty.

It does not modify roadmap status.

It does not open Physical-QFUDS [Level 2B](../../../../glossary/repository_levels.md).

## Why This Scaffold Exists

The retained `Gamma(a)` lane worked backward from a phenomenological transfer
profile and reached the known-model distinction wall. Continuing to force every
forward foam-sector question through `Gamma(a)` risks erasing the original idea:
one dark sector might have two effective macroscopic phases.

This scaffold therefore relaxes the assumptions:

```text
strong assumption:
  foam microphysics physically derives phase A, phase B, and a transfer law

weak assumption used here:
  an effective dark sector can be parameterized by a phase-B fraction f_B(a)
  that interpolates between a matter-like regime and a vacuum-like regime
```

This is a background-level bookkeeping scaffold only.

## Definitions

Let the total effective dark-sector density be `rho_D(a)`.

Let `f_B(a)` be a dimensionless effective phase-B fraction:

```text
0 <= f_B(a) <= 1
```

Use two limiting effective equations of state:

```text
phase A: w_A = 0
phase B: w_B = -1
```

For the general derivation keep `w_A` and `w_B` symbolic. The effective equation
of state is:

```text
w_D(a) = [1 - f_B(a)] w_A + f_B(a) w_B
```

Equivalently:

```text
w_D(a) = w_A + f_B(a) [w_B - w_A]
```

This is not a two-fluid transfer model. It is a one-sector effective equation of
state.

## Smooth Phase-Fraction Ansatz

Use a smooth transition in `ln a`:

```text
u(a) = ln(a / a_tr) / sigma
```

```text
f_B(a) = 1/2 [1 + tanh u(a)]
```

where:

- `a_tr` is the center of the effective transition;
- `sigma = Delta ln a` is the width in logarithmic scale factor.

For small widths near `a_tr`,

```text
Delta a ~= a_tr sigma
Delta z ~= (1 + z_tr) sigma
```

up to convention-dependent factors describing whether the width means one
`sigma`, half-maximum support, or another interval. This document uses `sigma`
only as a shape parameter.

The corresponding effective equation of state is:

```text
w_D(a) = (w_A + w_B)/2 + (w_B - w_A)/2 tanh[ln(a/a_tr)/sigma]
```

For the QFUDS-like bookkeeping limits `w_A = 0`, `w_B = -1`:

```text
w_D(a) = - f_B(a)
```

or:

```text
w_D(a) = -1/2 [1 + tanh(ln(a/a_tr)/sigma)]
```

## Density Evolution

For a non-interacting effective one-sector fluid, background conservation gives:

```text
d rho_D / d ln a = -3 [1 + w_D(a)] rho_D
```

with solution normalized at `a = 1`:

```text
rho_D(a) = rho_D0 exp[-3 int_1^a (1 + w_D(a')) d ln a']
```

This is the `w(a)` route. It is not the `Gamma(a)` route.

## Analytic Solution For The `ln a` Tanh Ansatz

Define:

```text
C = 1 + (w_A + w_B)/2
D = (w_B - w_A)/2
u(a) = ln(a / a_tr) / sigma
u_0 = u(1) = ln(1 / a_tr) / sigma
```

Then:

```text
1 + w_D(a) = C + D tanh u(a)
```

and:

```text
int_1^a [1 + w_D(a')] d ln a'
  = C ln a + D sigma [ln cosh u(a) - ln cosh u_0]
```

Therefore:

```text
rho_D(a)
  = rho_D0
    a^(-3C)
    [cosh u(a) / cosh u_0]^(-3 D sigma)
```

For `w_A = 0`, `w_B = -1`:

```text
C = 1/2
D = -1/2
```

so:

```text
rho_D(a)
  = rho_D0
    a^(-3/2)
    [cosh(ln(a/a_tr)/sigma) / cosh(ln(1/a_tr)/sigma)]^(3 sigma / 2)
```

## Asymptotic Behavior

For `a << a_tr`, `u(a) << 0`, so:

```text
f_B(a) -> 0
w_D(a) -> w_A
```

For `w_A = 0`:

```text
rho_D(a) proportional to a^(-3)
```

This is matter-like at the background level.

For `a >> a_tr`, `u(a) >> 0`, so:

```text
f_B(a) -> 1
w_D(a) -> w_B
```

For `w_B = -1`:

```text
rho_D(a) -> constant
```

This is vacuum-like at the background level.

## Difference From The Gamma Route

The `Gamma(a)` route uses coupled continuity equations such as:

```text
d rho_A / d ln a + 3 rho_A = -Gamma(a) rho_A
d rho_B / d ln a = +Gamma(a) rho_A
```

or an equivalent interacting-vacuum parameterization.

The phase-fraction scaffold here instead uses:

```text
d rho_D / d ln a = -3 [1 + w_D(a)] rho_D
```

with:

```text
w_D(a) = [1 - f_B(a)] w_A + f_B(a) w_B
```

There is no transfer four-vector, no source term, and no separate conserved
phase densities in this scaffold. A future model may later define those, but
they are not assumed here.

## What This Buys

This weak scaffold is useful because it gives a minimal analytic background
object that preserves the original single-sector intuition:

- early-time matter-like behavior;
- late-time vacuum-like behavior;
- a bounded phase fraction;
- an analytic density history;
- an explicit transition width parameter.

It does this without inserting the retained `Gamma(a)` profile by hand.

## What This Does Not Buy

This scaffold does not establish:

- phase A clustering at perturbation level;
- phase B smoothness at perturbation level;
- `c_s,A^2 ~= 0`;
- absence of unified-dark-fluid sound-speed pathologies;
- a physical foam-sector state variable;
- a microscopic phase transition;
- latent heat, defects, or correlation-length physics;
- known-model distinction;
- QFUDS support.

## Immediate Failure Modes

The scaffold fails or remains unsupported if:

- `f_B(a)` is treated as physical without a state-variable definition;
- the one-sector fluid develops unacceptable effective sound speed;
- the model reduces to a generic unified dark fluid with no new observable;
- the transition width is tuned only to fit data;
- `sigma` is reinterpreted as latent heat, correlation length, or defect
  dynamics without equations;
- the scaffold is used to claim Level 2B admission.

## Known-Model Reduction Risk

The closest known-model risk is high:

| Known family | Reduction risk |
| --- | --- |
| Unified dark fluid | Very high: this is a one-sector effective equation of state. |
| Barotropic dark fluid | High if pressure is only a function of density. |
| Generalized Chaplygin-like behavior | Possible if a pressure-density relation is fitted afterward. |
| Smooth `w(a)` dark energy | High if the matter-like early limit is ignored and only the late component is used. |
| Interacting dark energy | Indirect: an effective `w(a)` can often be reconstructed from an interacting background. |

This is acceptable at the scaffold stage because the purpose is not novelty. The
purpose is to recover a mathematically inspectable version of the original
single-sector phase-fraction intuition.

## Next Gate

The next useful step is not BAO likelihood work and not a return to retained
`Gamma(a)`.

The next gate is:

```text
Can this effective phase-fraction scaffold define perturbations without
immediate unified-fluid sound-speed failure?
```

Until that is answered, this scaffold remains a background-level mathematical
toy.
