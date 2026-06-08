---
doc_id: perturbation_gate
title: Level 2 Perturbation Gate
doc_type: gate
stage: "2"
status: completed
evidence_role: ssot
depends_on:
  - qfuds_v0_15_phase_transfer_physics
  - result_001_5_phase_transfer_physicality
next_gate: keep Level 2B blocked; classify P1 continuation as phenomenological interacting vacuum
last_updated: 2026-06-08
---

# Level 2 Perturbation Gate

Date: 2026-06-08

This file records the gate from background scans to perturbation theory.

The old blocking assumption was too strong:

```text
No perturbation theory until Gamma(a) receives a physical derivation.
```

The hostile-audit result is narrower:

```text
No physical QFUDS perturbation claim until Level 1.5 is resolved.
Phenomenological perturbation closure may begin as Level 2A if the closure is
covariant, gauge-declared, and explicitly labeled as phenomenological.
```

Do not add new speculative mechanisms before Level 1.5 is addressed.

## Surviving Branch

The only branch promoted from experiment 002 is:

```math
\Gamma(a)\propto {dF_{\rm coll}(>M,a)\over d\ln a}.
```

Interpretation:

```text
phase transfer follows nonlinear structure collapse / information production
```

This is not yet a confirmed physical law. It remains a Level 1.5 branch for
physical interpretation and a Level 2A phenomenological closure target for
perturbative kill tests.

## Killed Branches

Do not continue these as core claims without new equations and evidence:

- generic entropy-production language;
- HBM/KL linear gravitational entropy at the tested amplitude;
- horizon information as a distinct structure-production law;
- black-hole entropy without a real mass function and accretion history.

## Level 2 Split

| Level | Status | Meaning | Gate |
| --- | --- | --- | --- |
| 2A | completed | Phenomenological perturbation closure for a known interacting-dark-sector style model | P2 failed at retained amplitude; P1 survives as phenomenological interacting vacuum |
| 2B | blocked | Physical QFUDS perturbation closure | Resolve Level 1.5 or explicitly derive/fix the transfer physics |

Level 2A may test whether the current branch is even mathematically usable.
Level 2A may not claim microphysics, novelty, CMB viability, matter-power
viability, or survey-likelihood viability.

## Required Work Before Level 2A Closure

1. Use a declared gauge, preferably conformal Newtonian for the first audit.
2. Specify the transfer four-vector `Q_A^mu` and `Q_B^mu`.
3. Specify whether momentum transfer vanishes in the phase-A frame, phase-B frame, or another frame.
4. Specify `Q = Hc Gamma(a) rho_A` and a perturbation rule for `deltaQ`.
5. Specify whether `deltaGamma = 0`, and state that this is a phenomenological gauge-fixed closure unless a covariant clock is supplied.
6. Specify phase-A pressure and stress closure: `w_A=0`, `c_s,A^2=0`, `sigma_A=0` unless changed by a documented test.
7. Specify phase-B closure. Exact `w_B=-1` requires interacting-vacuum treatment; a fluid regularization must declare `w_B=-1+epsilon`, `c_s,B^2`, and the `epsilon -> 0` test.
8. Define superhorizon initial conditions and stability diagnostics.

## Required Work Before Level 2B Closure

1. Resolve `docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md`.
2. Decide whether `Gamma(a)` is a physical phase-transfer hypothesis or only a phenomenological interacting-vacuum law.
3. Recompute `dF_coll/dln a` using QFUDS self-consistent growth `D(a)`, not an LCDM-source approximation, once the required growth ingredients exist.
4. Fix the mass threshold `M` from a physical criterion.
5. Derive or physically justify the transfer perturbation variable.
6. Check whether any claimed redshift relation between `w(a)` and `f sigma8(a)` survives.

## Required Level 2 Documents

Level 2A documents:

- `docs/02_theory/040_qfuds_phenomenological_perturbations.md`
- `docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md`

Level 2A result:

- `docs/04_results/030_result_003_phenomenological_perturbation_closure.md`

Each must state that no CMB or matter-power claim is valid until CLASS/CAMB or equivalent Boltzmann-code output exists.

## Kill Criteria

Terminate or narrow the surviving branch if:

- the perturbation equations are gauge-ambiguous or not mathematically closed;
- transfer perturbations cause early-time instabilities;
- phase B clusters in a way that destroys the vacuum-pressure interpretation;
- growth is excessively suppressed or enhanced;
- the model reduces to standard interacting dark energy without a new fixed source relation;
- the proposed redshift-ratio relation fails once `D(a)` is computed self-consistently.

## Current Decision

Level 2A is complete for the baseline closure. P2 failed at the retained
amplitude. P1 is stable only as phenomenological interacting vacuum. Remain at
Level 1.5 for the physical interpretation of the collapse/information-production
branch, and keep Level 2B blocked.

Do not treat experiment 002 as a perturbation result, and do not treat the
current `Gamma(a) proportional to dF_coll/dln(a)` law as derived physics.
