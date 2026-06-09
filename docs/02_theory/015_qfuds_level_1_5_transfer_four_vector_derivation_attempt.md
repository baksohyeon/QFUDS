---
doc_id: qfuds_level_1_5_transfer_four_vector_derivation_attempt
title: QFUDS Level 1.5 Transfer Four-Vector Derivation Attempt
doc_type: theory_note
stage: "1.5"
status: completed
evidence_role: audit
depends_on:
  - qfuds_level_1_5_equivalence_source_perturbation_audit
  - qfuds_v0_15_phase_transfer_physics
  - level_1_5_resolution_gate
next_gate: retained branch demoted; no physical Level 2B without a new admitted physical branch
last_updated: 2026-06-09
---

# QFUDS Level 1.5 Transfer Four-Vector Derivation Attempt

Date: 2026-06-09

This note attempts the smallest possible Level 1.5 derivation:

```text
Can collapse or information production source a non-ad hoc transfer four-vector
Q^nu?
```

It does not start `exp_004`, physical Level 2B, CLASS/CAMB, CMB, matter-power,
or survey-likelihood work. Current status remains in
[000_roadmap.md](../05_next_steps/000_roadmap.md).

## Starting Point

The background QFUDS transfer equations are:

```math
{d\rho_A\over d\ln a}+3\rho_A=-\Gamma(a)\rho_A,
\qquad
{d\rho_B\over d\ln a}=\Gamma(a)\rho_A.
```

The retained source shape is:

```math
\Gamma(a) \propto {dF_{\rm coll}(>M,a)\over d\ln a}.
```

The task is to see whether this can be lifted from a background source shape to
a covariant transfer law:

```math
\nabla_\mu T_A^{\mu\nu}=-Q^\nu,
\qquad
\nabla_\mu T_B^{\mu\nu}=+Q^\nu.
```

## Candidate Source Scalar

The narrowest background source scalar is:

```math
X(a;M)={dF_{\rm coll}(>M,a)\over d\ln a}.
```

`F_coll` is a collapsed mass fraction and is dimensionless. Since `ln(a)` is
dimensionless, `X(a;M)` is also dimensionless.

The implemented normalized source shape can be written as:

```math
\widehat X(a;M)=
{X(a;M)\over \max_a X(a;M)},
\qquad
\Gamma(a)=\epsilon\,\widehat X(a;M).
```

Here `epsilon` is the same role as `gamma0`: an effective transfer strength per
`dln(a)`. It is dimensionless in the repository background equations. The
physical energy-transfer rate is then `H Gamma rho_A`, with units of energy
density per time.

### Local Source Option

A local version would need a field such as:

```math
X(x,a;M)={dF_{\rm coll}(x;>M,a)\over d\ln a}.
```

This is not defined in the repository. It would require a smoothing scale,
window function, halo finder or collapse criterion, and a prescription for how
local collapsed fraction sources homogeneous phase-B energy.

Unsupported assumption:

```text
The repository currently has only a background source shape, not a local
source scalar.
```

## Mass Threshold M

For the source to be physical, `M` must be fixed before fitting.

Current repository state:

- the implementation uses an implicit timing parameter like `collapse_a`;
- no halo mass threshold `M` is selected by QFUDS microphysics;
- no observational threshold has been pre-registered;
- no QFUDS spherical-collapse calculation fixes `M`.

Therefore `M` cannot currently be fixed without adding an unsupported new
assumption.

Smallest acceptable future fix:

```text
Choose M from an external physical criterion before looking at QFUDS background
or perturbation success, then record why that mass scale is relevant.
```

Until that happens, `M` remains assumed and the source remains phenomenological.

## Minimal Candidate Transfer Four-Vector

The minimal candidate is:

```math
Q^\nu = H\,\epsilon\,\widehat X(a;M)\,\rho_A\,u_A^\nu.
```

With the sign convention:

```math
\nabla_\mu T_A^{\mu\nu}=-Q^\nu,
\qquad
\nabla_\mu T_B^{\mu\nu}=+Q^\nu.
```

In the homogeneous phase-A frame this gives:

```math
\dot\rho_A+3H\rho_A=-H\epsilon\widehat X\rho_A,
\qquad
\dot\rho_B=+H\epsilon\widehat X\rho_A.
```

Dividing by `H` recovers:

```math
{d\rho_A\over d\ln a}+3\rho_A=-\Gamma(a)\rho_A,
\qquad
{d\rho_B\over d\ln a}=+\Gamma(a)\rho_A.
```

This is mathematically consistent as an interacting-vacuum ansatz.

Unsupported assumptions:

- `u_A^\nu` is the correct transfer direction.
- collapse-sourced energy becomes smooth phase B rather than local stress,
  heat, radiation, halo binding energy, or another component.
- phase B has vacuum pressure after receiving energy.
- the background collapsed-fraction rate can source a homogeneous transfer.
- `epsilon` is constant and universal.

These assumptions are not derived by the current repository.

## Conservation-Law Role

The candidate `Q^\nu` conserves total stress-energy by construction:

```math
\nabla_\mu(T_A^{\mu\nu}+T_B^{\mu\nu})=0.
```

It also states how phase A loses energy and phase B gains energy at background
level.

What it does not prove:

- why collapse produces phase B;
- why the produced component has `w_B ~= -1`;
- why the transfer direction follows `u_A^\nu`;
- why `X(a;M)` rather than another collapse, entropy, Weyl, binding-energy, or
  halo-formation scalar is the correct source.

Therefore this is a conservation-compatible ansatz, not a physical derivation.

## Epsilon / Gamma0 Classification

Current classification:

```text
epsilon / gamma0 is phenomenological.
```

It is not derived. It is not independently bounded in the repository. It is not
fixed by microphysics, halo physics, entropy accounting, or observational input.

Possible future upgrades:

- `derived`: follows from a microscopic or coarse-grained state-counting model;
- `bounded`: constrained by an external physical limit before fitting;
- `fitted`: fit to data with no physical prior, which would not pass Level 1.5;
- `phenomenological`: assumed efficiency used for model exploration.

The current status is the last one.

## Can Delta Q Follow From The Same Source?

If the candidate transfer law were accepted, a formal perturbation would begin
from:

```math
\delta Q^\nu =
\delta(H\epsilon\widehat X\rho_A u_A^\nu).
```

At minimum this contains perturbations of:

- `H`;
- `rho_A`;
- `u_A^\nu`;
- `epsilon`, if not constant;
- `X`.

The first three are standard once a gauge and frame are chosen. The last term is
the blocker:

```text
delta X is not defined because the repository has no local collapse/information
source scalar.
```

Setting `delta X = 0` would be an additional phenomenological closure, not a
result of the source model. Setting `delta X proportional to delta_A` would also
be an extra assumption unless derived from a collapse model.

Therefore `delta Q` cannot currently follow from the same source without adding
new unsupported assumptions.

## Derivation Verdict

The smallest candidate `Q^\nu` can reproduce the background equations, but it
does not derive physical QFUDS transfer.

Verdict:

```text
The retained collapse/information-production Gamma(a) branch fails physical
Level 1.5 promotion and is demoted to phenomenological interacting-vacuum
status. This does not falsify the broader DM-to-DE phase-transition hypothesis;
it rejects only the current retained source relation as a physical derivation.
```

## Clean Demotion Recommendation

If no further derivation is supplied, record this branch as:

```text
The retained collapse/information-production Gamma(a) branch is a
phenomenological interacting-vacuum transfer law. It is useful as a constrained
source shape, but it is not a physical QFUDS phase-transfer derivation.
```

Consequences:

- physical QFUDS Level 2B remains blocked;
- future work may continue only as phenomenological interacting-vacuum model
  comparison;
- `Gamma(a)` must not be described as derived from collapse, entropy,
  information, foam, or black-hole physics;
- failed physical-transfer interpretation remains preserved as Level 1.5
  provenance.

## Future-Branch Admission Rule

No new physical-QFUDS branch should be opened unless it provides, at minimum:

- `X =`
- `Q^nu =`
- `why phase B has w ~= -1 =`
- `delta Q route =`
- `known-model distinction =`
