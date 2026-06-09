---
doc_id: qfuds_v0_2
title: QFUDS v0.2 Theory Note
doc_type: theory_note
stage: "1"
status: completed
evidence_role: hypothesis
depends_on:
  - qfuds_v0_1
next_gate: gamma law background scan
last_updated: 2026-06-08
---

# QFUDS v0.2 Theory Note

Date: 2026-06-08

## Status

v0.2 is the first mathematically useful formulation. It rewrites QFUDS as a minimal two-phase effective dark sector in unmodified general relativity.

## Assumptions

1. GR is retained at background level.
2. The dark sector can be split into two effective phases.
3. Phase A clusters like cold dark matter:

```text
w_A = 0
c_s,A^2 = 0
```

4. Phase B is smooth and vacuum-like:

```text
w_B = -1
delta_B = 0
```

5. Baryons and radiation follow their standard background scalings.
6. Compact remnant/defect components are optional and subdominant unless separately modeled.

## Equations

Minimal dark-sector split:

```math
rho_dark = rho_A + rho_B
```

LCDM-limit densities:

```math
rho_A = rho_A0 a^{-3}
rho_B = rho_B0
```

Flat-background Friedmann equation:

```math
H^2(a) = H_0^2 [
Omega_r0 a^{-4}
+ Omega_b0 a^{-3}
+ Omega_A0 a^{-3}
+ Omega_B0
]
```

With phase transfer:

```math
d rho_A / d ln a + 3 rho_A = - Gamma(a) rho_A
d rho_B / d ln a = Gamma(a) rho_A
```

Total dark-sector equation of state:

```math
w_dark(a) = - rho_B / (rho_A + rho_B)
```

## Physical Interpretation

Phase A is the foam-sector part that must behave gravitationally like cold dark matter. Phase B is the residual vacuum-pressure part that mimics dark energy.

The main value of v0.2 is negative: it shows that QFUDS is not automatically novel. With `Gamma = 0`, it is exactly LCDM at background level. With free `Gamma(a)`, it becomes an interacting dark-sector model.

## Differences From v0.1

1. Removed the white-hole-universe image from the central claim.
2. Introduced an explicit two-phase dark-sector split.
3. Identified the LCDM limit.
4. Identified the sound-speed constraint as a first kill criterion.
5. Framed remnants as optional defects rather than the main explanation.

## Unresolved Issues

1. `Gamma(a)` is not derived from microphysics.
2. Perturbation equations are not complete.
3. Transfer perturbations `delta_Q` are unspecified.
4. Background equivalence to known models is not resolved.
5. The physical distinction between a real phase split and bookkeeping remains unproven.

## Decision

Keep v0.2 as the minimal formulation and baseline for later tests. Treat novelty as unproven.
