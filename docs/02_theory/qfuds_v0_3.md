# QFUDS v0.3 Theory Note

Date: 2026-06-08

## Status

v0.3 tests whether the phase-transfer law `Gamma(a)` can be connected to a physical history rather than used as an arbitrary fitting function. This version is still background-level only.

## Assumptions

1. The v0.2 two-phase background equations remain in force.
2. Positive `Gamma(a)` transfers energy from phase A to phase B.
3. Present-day densities are boundary data and the background is integrated backward.
4. CMB safety requires transfer to be small at early times.
5. A physically useful `Gamma(a)` should be fixed by a named source history before fitting its amplitude.

## Equations

Background transfer:

```math
d rho_A / d ln a + 3 rho_A = - Gamma(a) rho_A
d rho_B / d ln a = Gamma(a) rho_A
```

Candidate law family:

```math
Gamma(a) = gamma_0 F_phys(a)
```

Implemented examples:

```text
constant
powerlaw
growth_driven
collapsed_fraction_toy
horizon_entropy
black_hole_entropy_proxy
star_formation_proxy
```

Effective phase-B equation of state:

```math
w_B,eff(a) = -1 - Gamma(a) rho_A(a) / [3 rho_B(a)]
```

The growth diagnostic assumes smooth phase B and nearly dust-like phase A:

```math
D'' + [2 + d ln H / d ln a] D' - (3/2) Omega_clustering(a) D = 0
```

## Physical Interpretation

v0.3 asks whether phase conversion should turn on with ordinary structure formation rather than during the early universe. The most relevant surviving toy laws are tied to low-redshift collapse, black-hole entropy growth, or star-formation history.

This does not prove QFUDS novel. It narrows the next target to low-redshift, physically sourced transfer histories.

## Differences From v0.2

1. Added named `Gamma(a)` laws.
2. Added background comparison against the LCDM limit.
3. Added viability flags for positivity, early dark-energy fraction, CMB-era `H(a)` deviation, matter domination, and growth preservation.
4. Produced reproducible CSV and PNG outputs.
5. Classified each law as trivial LCDM, standard interacting dark energy, observationally dead, or worth testing next.

## Unresolved Issues

1. All physically motivated laws are still toy proxies.
2. The black-hole entropy proxy is not derived from a real black-hole mass function.
3. The collapsed-fraction proxy is not a calibrated nonlinear structure history.
4. The star-formation proxy is empirical and may become curve fitting if not fixed before tests.
5. Background safety does not establish perturbation stability.
6. CLASS/CAMB implementation is blocked until transfer perturbations are specified.

## Decision

Reject constant and ungated growth-driven transfer at the tested amplitudes. Preserve low-redshift collapse, black-hole-entropy, and star-formation proxies as next targets, with the explicit caveat that they are not evidence of novelty.
