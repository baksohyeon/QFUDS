# Level 2 Perturbation Gate

Date: 2026-06-08

This file records the exact gate from background scans to perturbation theory.

The background phase-transfer scans are complete. Do not add new speculative mechanisms before this gate is addressed.

## Surviving Branch

The only branch promoted from experiment 002 is:

```math
\Gamma(a)\propto {dF_{\rm coll}(>M,a)\over d\ln a}.
```

Interpretation:

```text
phase transfer follows nonlinear structure collapse / information production
```

This is not yet a confirmed physical law. It is the next branch to try to kill.

## Killed Branches

Do not continue these as core claims without new equations and evidence:

- generic entropy-production language;
- HBM/KL linear gravitational entropy at the tested amplitude;
- horizon information as a distinct structure-production law;
- black-hole entropy without a real mass function and accretion history.

## Required Work Before CLASS/CAMB

1. Recompute `dF_coll/dln a` using QFUDS self-consistent growth `D(a)`, not an LCDM-source approximation.
2. Fix the mass threshold `M` from a physical criterion.
3. Derive perturbation equations for `delta_A`, `theta_A`, `delta_B`, and `theta_B`.
4. Define the transfer perturbation variable and gauge prescription.
5. Check whether the redshift-ratio relation between `w(a)` and `f sigma8(a)` survives.

## Required Level 2 Documents

Before Level 2 is considered complete, create:

- `docs/02_theory/qfuds_perturbations.md`
- `docs/03_experiments/exp_003_perturbation_prescriptions.md`
- `docs/04_results/result_003_perturbation_prescriptions.md`

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

Proceed to Level 2 only for the collapse/information-production branch.

Do not treat experiment 002 as a perturbation result.
