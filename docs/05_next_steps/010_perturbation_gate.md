---
doc_id: perturbation_gate
title: Level 2 Perturbation Gate
doc_type: gate
stage: "2"
status: blocked
evidence_role: ssot
depends_on:
  - qfuds_v0_15_phase_transfer_physics
  - result_001_5_phase_transfer_physicality
next_gate: create exp_003 only after Level 1.5 is resolved
last_updated: 2026-06-08
---

# Level 2 Perturbation Gate

Date: 2026-06-08

This file records the exact gate from background scans to perturbation theory.

The background phase-transfer scans are complete, but the phase-transfer
physicality audit added Level 1.5 before perturbation closure. Do not add new
speculative mechanisms before Level 1.5 is addressed.

## Surviving Branch

The only branch promoted from experiment 002 is:

```math
\Gamma(a)\propto {dF_{\rm coll}(>M,a)\over d\ln a}.
```

Interpretation:

```text
phase transfer follows nonlinear structure collapse / information production
```

This is not yet a confirmed physical law. It remains a Level 1.5 branch to try
to kill before full perturbation closure.

## Killed Branches

Do not continue these as core claims without new equations and evidence:

- generic entropy-production language;
- HBM/KL linear gravitational entropy at the tested amplitude;
- horizon information as a distinct structure-production law;
- black-hole entropy without a real mass function and accretion history.

## Required Work Before Level 2 Closure

1. Resolve `docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md`.
2. Decide whether `Gamma(a)` is a physical phase-transfer hypothesis or only a phenomenological interacting-vacuum law.
3. Recompute `dF_coll/dln a` using QFUDS self-consistent growth `D(a)`, not an LCDM-source approximation, once the required growth ingredients exist.
4. Fix the mass threshold `M` from a physical criterion.
5. Derive perturbation equations for `delta_A`, `theta_A`, `delta_B`, and `theta_B` only after the Level 1.5 gate is satisfied.
6. Define the transfer perturbation variable and gauge prescription.
7. Check whether the redshift-ratio relation between `w(a)` and `f sigma8(a)` survives.

## Required Level 2 Documents

Do not create these as active experiment documents until Level 1.5 is resolved.
Before Level 2 is considered complete, create:

- `docs/02_theory/040_qfuds_perturbations.md`
- `docs/03_experiments/030_exp_003_perturbation_prescriptions.md`
- `docs/04_results/030_result_003_perturbation_prescriptions.md`

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

Remain at Level 1.5 for the collapse/information-production branch.

Do not treat experiment 002 as a perturbation result, and do not treat the
current `Gamma(a) proportional to dF_coll/dln(a)` law as derived physics.
