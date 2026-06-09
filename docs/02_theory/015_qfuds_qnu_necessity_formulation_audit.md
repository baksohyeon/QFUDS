---
doc_id: qfuds_qnu_necessity_formulation_audit
title: QFUDS Qnu Necessity Formulation Audit
doc_type: theory_note
stage: "1.5"
status: completed
evidence_role: audit
depends_on:
  - qfuds_v0_15_phase_transfer_physics
  - qfuds_level_1_5_equivalence_source_perturbation_audit
  - qfuds_level_1_5_transfer_four_vector_derivation_attempt
next_gate: retained branch demoted; future branches must choose explicit formulation before physical Level 2B
last_updated: 2026-06-09
---

# QFUDS Qnu Necessity Formulation Audit

Date: 2026-06-09

This note answers a narrower formulation question:

```text
Is a transfer four-vector Q^nu required for a dark-matter-like phase to become a
dark-energy-like phase?
```

It does not by itself change viability. The retained-branch decision is recorded
in [000_roadmap.md](../05_next_steps/000_roadmap.md).

## Short Answer

`Q^nu` is not a theorem that every phase-transition model must use.

The theorem-level requirement is total stress-energy conservation:

```math
\nabla_\mu T_{\rm total}^{\mu\nu}=0.
```

In ordinary GR this follows from the Einstein equations together with the
contracted Bianchi identity. If the dark sector is split into two effective
components,

```math
T_{\rm total}^{\mu\nu}=T_A^{\mu\nu}+T_B^{\mu\nu},
```

and energy-momentum moves between those components, then a transfer term is the
standard covariant bookkeeping:

```math
\nabla_\mu T_A^{\mu\nu}=-Q^\nu,
\qquad
\nabla_\mu T_B^{\mu\nu}=+Q^\nu.
```

So the chain is:

```text
phase transition -> stress-energy accounting is required
two-component effective-fluid split -> Q^nu is the standard formulation
single-field or unified-fluid model -> Q^nu may be absent or only implicit
```

## Established Physics

### Total conservation is required

In GR, the Einstein tensor obeys a geometric identity:

```math
\nabla_\mu G^{\mu\nu}=0.
```

For Einstein equations with matter on the right-hand side, consistency requires
the total stress-energy source to be covariantly conserved:

```math
\nabla_\mu T_{\rm total}^{\mu\nu}=0.
```

This is the established constraint. It does not by itself require dark matter
and dark energy to be separately conserved, nor does it require a particular
split into dark-matter and dark-energy pieces.

### A split creates an accounting question

If one writes the dark sector as two components, then either:

```math
\nabla_\mu T_A^{\mu\nu}=0,
\qquad
\nabla_\mu T_B^{\mu\nu}=0,
```

or the components exchange energy-momentum. In the exchange case, defining
`Q^nu` is just the covariant way to keep total conservation exact.

This is why interacting dark-energy and interacting-vacuum papers introduce
energy-momentum transfer vectors. Reviews of interacting dark energy emphasize
that the interaction changes background evolution and perturbations, not just
notation:

- [Dark Matter and Dark Energy Interactions](https://arxiv.org/abs/1603.08299)
- [Large-scale instability in interacting dark energy and dark matter fluids](https://arxiv.org/abs/0804.0232)
- [Momentum transfer models of interacting dark energy](https://arxiv.org/abs/2107.03235)
- [Covariantizing the interaction between dark energy and dark matter](https://arxiv.org/abs/1405.7288)

## Common Modeling Practice

### Interacting dark energy and interacting vacuum

In a two-fluid dark-sector model, the common formulation is:

```math
\nabla_\mu T_c^{\mu\nu}=Q_c^\nu,
\qquad
\nabla_\mu T_x^{\mu\nu}=Q_x^\nu,
\qquad
\sum_i Q_i^\nu=0.
```

The vector has an energy-transfer part and a momentum-transfer part. Choosing
its direction, for example parallel to dark matter velocity, dark energy
velocity, or total velocity, is not a harmless detail. It affects perturbations
and can create instabilities.

This is standard modeling practice, not a unique theorem. It becomes necessary
only after the model chooses to represent the dark sector as separate interacting
components.

### Unified dark-sector models

Some models avoid explicit `Q^nu` by not splitting the dark sector into two
interacting fluids. They use one stress tensor instead:

```math
\nabla_\mu T_{\rm dark}^{\mu\nu}=0.
```

The dark-sector behavior changes through an equation of state, scalar-field
Lagrangian, sound speed, potential, or other internal dynamics. Examples include
dark-fluid and unified scalar-field approaches:

- [Constraining the dark fluid](https://arxiv.org/abs/0908.3197)
- [Cosmological constraints on a unified dark matter-energy scalar field model with fast transition](https://arxiv.org/abs/1706.01706)

In those models, a transition from dark-matter-like behavior to
dark-energy-like behavior can be described without an explicit transfer vector
between two components. The accounting is internal to a single stress tensor.

### Phase-transition models

A phase transition can be modeled without `Q^nu` if the theory supplies an
underlying field, order parameter, potential, or effective action whose
stress-energy tensor is conserved as a whole. Then the "transition" is encoded
in the field dynamics.

If the phase transition is instead described as "component A loses energy and
component B gains energy", then a `Q^nu`-like object is needed, whether named
explicitly or hidden inside the equations.

## QFUDS-Specific Assumptions

The current QFUDS implementation is not a single-field Lagrangian or unified
stress tensor. It explicitly writes two effective components:

- phase A: clustering and nearly pressureless;
- phase B: smooth and vacuum-pressure-like;
- `Gamma(a)`: a background transfer rate from A to B.

That choice makes QFUDS a two-component effective-fluid model at the current
implementation level. Once QFUDS says phase A becomes phase B, a hostile reader
will ask:

```text
What is transferred, in which frame, with what stress-energy tensor, and how is
total conservation maintained?
```

For the current formulation, `Q^nu` is not an arbitrary Codex preference. It is
the natural covariant form of the accounting that the current two-component
QFUDS equations already imply.

## Is Qnu Unavoidable?

### Not unavoidable for every phase-transition theory

`Q^nu` is avoidable if QFUDS is reformulated as one of these:

- a single dark fluid with a changing equation of state;
- a scalar or effective field with a Lagrangian;
- a unified stress tensor with internal phase behavior;
- a modified-gravity or backreaction model where the effective dark sector is
  not split into separately tracked A/B fluids.

In those cases the required object is the total stress tensor and its dynamics,
not a transfer vector between named components.

### Unavoidable for current two-phase bookkeeping

`Q^nu` or an equivalent transfer equation is unavoidable if QFUDS keeps all of
these statements:

1. phase A and phase B are separate effective components;
2. phase A loses energy;
3. phase B gains energy;
4. total stress-energy is conserved;
5. perturbations are to be defined.

One can rename `Q^nu`, but the mathematical role remains.

## What A Hostile Reviewer Would Expect

Before accepting a phase-transition claim as physically meaningful, a hostile
reviewer would expect one of two complete formulations.

### Two-component interacting formulation

Required:

- `T_A^{mu nu}` and `T_B^{mu nu}`;
- `Q^nu` or equivalent transfer law;
- sign convention showing phase A loss and phase B gain;
- transfer frame and momentum-transfer prescription;
- perturbation prescription, including `delta Q`;
- physical source for the transfer, not only a timing function;
- comparison to interacting-vacuum and interacting-dark-energy models.

### Unified or field formulation

Required:

- one total dark-sector stress tensor or action;
- equation of state, potential, or order parameter that creates the transition;
- sound speed and perturbation behavior;
- mapping to observed DM-like and DE-like regimes;
- comparison to unified dark fluid, scalar-field, and Chaplygin-like models.

Either path can be legitimate. What is not acceptable is claiming a transition
without any stress-energy accounting.

## Consequence For Level 1.5

The current Level 1.5 blocker is not "no `Q^nu`, therefore no phase transition
is possible." The blocker is:

```text
QFUDS currently uses a two-component transfer language, but has not supplied the
stress-energy accounting required by that language.
```

Therefore the retained `Gamma(a)` branch can fail as a physical two-component
transfer derivation while the broader phase-transition hypothesis remains open.

Future QFUDS work has two clean choices:

1. keep the two-component A/B formulation and derive an explicit transfer law;
2. reformulate QFUDS as a unified dark-sector or field model and stop requiring
   a separate A-to-B `Q^nu`.

Mixing the two without a stress-energy account is not defensible.
