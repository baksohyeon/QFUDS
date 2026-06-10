---
doc_id: qfuds_phenomenological_perturbations
title: QFUDS Level 2A Phenomenological Perturbations
doc_type: theory_note
stage: "2"
status: completed
evidence_role: hypothesis
depends_on:
  - result_001_5_phase_transfer_physicality
  - perturbation_gate
next_gate: result_003 phenomenological closure audit
last_updated: 2026-06-08
---

# QFUDS Level 2A Phenomenological Perturbations

Date: 2026-06-08

## Executive Verdict

A microscopic derivation of `Gamma(a)` is not required before writing
perturbation equations. What is required is a mathematically closed perturbation
prescription for the stress-energy transfer.

Therefore QFUDS may enter [Level 2A](../wiki/glossary/repository_levels.md):

```text
phenomenological perturbation closure
```

QFUDS may not enter Level 2B:

```text
physical perturbation closure
```

until Level 1.5 resolves the physical meaning of `Gamma(a)`.

## Literature Audit

| Class | Perturbation status | Examples | Audit result |
| --- | --- | --- | --- |
| Interacting dark energy | Perturbations often developed before microscopic derivation | Valiviita, Majerotto, and Maartens found early-time large-scale instabilities in simple fluid interactions: <https://arxiv.org/abs/0804.0232>. Clemson et al. constrained a phenomenological IDE model with explicit momentum-transfer frame choices: <https://arxiv.org/abs/1109.6234>. | Microphysics is not required, but bad closures are killed by perturbations. |
| Interacting vacuum | Perturbations developed for phenomenological transfer models | Inhomogeneous vacuum energy can be written as interacting vacuum plus matter: <https://arxiv.org/abs/1209.0563>. Full linear perturbation theory was used for geodesic-CDM interacting-vacuum constraints: <https://arxiv.org/abs/1902.10694>. | Closest precedent for phase A plus vacuum-like phase B. |
| Coupled quintessence | Perturbations follow an effective action and coupling, not a full microscopic particle derivation | Amendola specified scalar potential and coupling, then computed CMB/LSS perturbations: <https://arxiv.org/abs/astro-ph/9908023>. | Stronger than current QFUDS because it has an effective field model. |
| Unified dark fluid / generalized dark matter | Perturbations developed phenomenologically | Hu's generalized dark matter specifies the stress tensor by equation of state, sound speed, and viscosity: <https://arxiv.org/abs/astro-ph/9801234>. | Direct precedent: phenomenological closure is allowed if stress variables are explicit. |
| Generalized Chaplygin gas | Perturbations tested a phenomenological equation of state | GCG unification uses `p=-A/rho^alpha`: <https://arxiv.org/abs/astro-ph/0210375>. Sandvik et al. ruled out most of the parameter space through matter-power behavior: <https://arxiv.org/abs/astro-ph/0212114>. | Perturbations can kill a phenomenological unified model. |
| k-essence | Perturbations follow an effective scalar action | K-essence has a noncanonical scalar action: <https://arxiv.org/abs/astro-ph/0006373>. Pure kinetic k-essence can give `rho = rho0 + rho1 a^-3` with small sound speed: <https://arxiv.org/abs/astro-ph/0402316>. | A physical Level 2B analogue would need this kind of effective action or equivalent closure. |
| PPF / phenomenological dark-sector couplings | Perturbations developed to stabilize or parameterize otherwise ambiguous couplings | Interacting PPF replaces problematic dark-energy pressure closures with a large-scale momentum relation: <https://arxiv.org/abs/1404.5220>. | If the first fluid closure fails, PPF is a known fallback class, not a QFUDS novelty claim. |

## Minimum Closure

The system starts from split conservation:

```text
nabla_mu T_A^{mu nu} = Q_A^nu
nabla_mu T_B^{mu nu} = Q_B^nu
Q_A^nu + Q_B^nu = 0
```

The background convention is:

```text
rho_A' + 3 Hc rho_A = -Q
rho_B' + 3 Hc (1 + w_B) rho_B = +Q
Q = Hc Gamma(a) rho_A
```

where `Hc` is the conformal Hubble rate.

The minimum variables are:

```text
delta_A
theta_A
delta_B
theta_B
Q
deltaQ
metric perturbations
```

The closure must specify:

1. gauge;
2. transfer four-vector;
3. momentum-transfer frame;
4. `deltaQ`;
5. whether `deltaGamma` is zero, sourced, or gauge-covariant;
6. phase-A sound speed and anisotropic stress;
7. phase-B treatment, especially if `w_B = -1`;
8. initial conditions;
9. stability and conservation diagnostics.

## Minimal Level 2A Closure To Audit

The smallest hostile test is:

```text
Gauge: conformal Newtonian
Transfer frame: phase-A-comoving
Q_A^mu = -Q u_A^mu
Q_B^mu = +Q u_A^mu
Q = Hc Gamma(a) rho_A
deltaQ = Q delta_A
deltaGamma = 0
phase A: w_A=0, c_s,A^2=0, sigma_A=0
phase B variant P1: interacting vacuum
phase B variant P2: regularized fluid, w_B=-0.999, c_s,B^2=1, sigma_B=0
```

This is not a physical derivation. It is a declared phenomenological closure.

## Implemented Equations

The implementation is in `qfuds/perturbations.py`. It uses `x=ln(a)` and
dimensionless velocity variables `theta/Hc`.

The metric potential is a Newtonian-gauge algebraic closure for the first
stability audit:

```text
Phi = -3 [Omega_A delta_A + Omega_B delta_B] / [2 (kappa^2 + 3)]
kappa = k / Hc
```

For phase A (velocity variable `theta/Hc`, so the Euler base friction constant is
`1`, consistent with `qfuds/growth.py`; see
[outputs/postmortem/exp003_friction_bug/README.md](../../outputs/postmortem/exp003_friction_bug/README.md)):

```text
delta_A,x = -theta_A - Gamma Phi
theta_A,x = -(1 + dlnHc/dx) theta_A + kappa^2 Phi
```

For phase B variant P1:

```text
delta_B = 0 substitute
theta_B = not an ordinary fluid variable
```

For phase B variant P2:

```text
S = Gamma rho_A / rho_B
delta_B,x =
  -(1+w_B) theta_B
  - 3 (c_s,B^2 - w_B) delta_B
  + S (delta_A - delta_B + Phi)

theta_B,x =
  -(1 + dlnHc/dx - 3 c_s,B^2) theta_B
  + kappa^2 [Phi + c_s,B^2 delta_B/(1+w_B)]
  + S (theta_A - theta_B)/(1+w_B)
```

The small denominator in P2 is not hidden. It is the exact reason this audit
tests whether a near-vacuum phase-B fluid closure becomes unstable.

## Risks

| Severity | Risk | Reason |
| --- | --- | --- |
| critical | gauge ambiguity in `deltaQ` | `Gamma(a)` is a background-time function unless a covariant clock is supplied. |
| critical | early-time large-scale instability | Known interacting dark energy models can blow up even for weak coupling. |
| critical | exact-vacuum velocity problem | If `w_B=-1`, `theta_B` is not a normal fluid velocity. |
| high | arbitrary momentum-transfer frame | A-frame and B-frame transfer can predict different growth. |
| high | loss of predictivity | Replacing failed `deltaQ` choices after the fact makes the model arbitrary. |
| high | equivalence to known IDE | A stable closure may still be ordinary interacting vacuum, not novel QFUDS. |
| medium | circular source history | `Gamma` depends on collapse history, while collapse depends on perturbation growth. |
| medium | Boltzmann-code stiffness or singularity | CLASS/CAMB need stable variables and initial conditions. |

## Decision

Proceed to Level 2A as a phenomenological perturbation audit.

Do not claim Level 2B, microphysics, novelty, CMB viability, matter-power
viability, or survey-likelihood viability from Level 2A.
