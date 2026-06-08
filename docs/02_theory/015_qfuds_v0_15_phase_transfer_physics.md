---
doc_id: qfuds_v0_15_phase_transfer_physics
title: "QFUDS v0.15 / Level 1.5: Phase Transfer Physics"
doc_type: theory_note
stage: "1.5"
status: in_progress
evidence_role: audit
depends_on:
  - exp_002_entropy_information_gate
  - result_002_entropy_information_gate
next_gate: decide physical transfer hypothesis or demote to phenomenological law
last_updated: 2026-06-08
---

# QFUDS v0.15 / Level 1.5: Phase Transfer Physics

Date: 2026-06-08

Status: QFUDS v0.15 / Level 1.5 audit document. This is not a perturbation-theory document.

## 1. Executive Summary

The surviving branch from experiment 002 is:

```math
\Gamma(a) \propto {dF_{\rm coll}(>M,a)\over d\ln a}.
```

Current verdict: QFUDS does not yet have a derived physical phase-transfer law.
It has a phenomenological transfer law with a physically motivated source shape.

The minimum defensible interpretation is:

```text
Gamma(a) is an effective coarse-grained phase-conversion rate per d ln a,
whose time dependence is assumed to follow nonlinear collapse or information
production.
```

This is not yet:

- a fundamental coupling;
- a microphysical decay rate;
- a derived entropy-production law;
- evidence that structure formation creates dark energy;
- evidence that information production generates vacuum pressure.

The branch should remain at Level 1.5. It has not earned unrestricted entry into
perturbation closure. A limited perturbation exercise may be useful only as a
stress test of a phenomenological interacting-vacuum model.

## 2. Phase Transfer Physicality Assessment

### Why Should Phase Transfer Occur At All?

At present, QFUDS has no first-principles reason that phase A must convert into
phase B. The two-phase background equations assume transfer:

```math
{d\rho_A\over d\ln a}+3\rho_A=-\Gamma(a)\rho_A,
\qquad
{d\rho_B\over d\ln a}=\Gamma(a)\rho_A.
```

These equations are mathematically clear, but they do not derive `Gamma(a)`.
They say what happens if a transfer rate exists.

The proposed physical motivation is that nonlinear gravitational collapse
changes the coarse-grained state count of the dark sector. If phase A is the
clustering phase of a common foam sector, then virialization, horizon formation,
or irreversible coarse graining could in principle move some effective energy
from the clustering sector into a smooth vacuum-pressure sector.

That is a hypothesis, not a derivation.

### What Physical Mechanism Is Being Proposed?

The narrow mechanism currently proposed is:

1. Phase A clusters like cold matter at background level.
2. As structures collapse, the coarse-grained information or entropy associated
   with the dark-sector state increases.
3. The rate of that increase supplies the time shape of energy transfer from
   phase A to phase B.
4. The simplest implemented source is the Press-Schechter collapsed fraction
   above a threshold:

```math
F_{\rm coll}(>M,a)=
\operatorname{erfc}\left[
{\delta_c\over \sqrt{2}\,\sigma(M)D(a)}
\right].
```

Then:

```math
\Gamma(a)=\gamma_0
{dF_{\rm coll}/d\ln a\over
\max_a(dF_{\rm coll}/d\ln a)}.
```

This mechanism is physically minimal but incomplete. It defines a source shape.
It does not show why `dF_coll/dln a` must create vacuum pressure.

### Minimum Physical Interpretation Required

For the branch to remain scientifically meaningful, the minimum interpretation
must be:

- `Gamma(a)` is a coarse-grained effective rate, not a microscopic constant.
- `dF_coll/dln a` is a proxy for irreversible nonlinear structure formation.
- `gamma0` is an undetermined efficiency converting the source history into
  phase transfer.
- `M` must be fixed before comparison with data, or the model becomes a fitted
  shape.
- The source must eventually be recomputed from QFUDS growth, not from an LCDM
  growth approximation.

### Interpretations Ruled Out

The current evidence rules out these interpretations:

| Interpretation | Status | Reason |
| --- | --- | --- |
| `Gamma(a)` is a fundamental coupling | ruled out for current model | The implemented law is explicitly time-dependent and normalized from a source history. |
| `Gamma(a)` is derived from microphysics | ruled out for current model | No action, state-count model, horizon accounting, or entropy balance derives it. |
| `Gamma(a)` is observational input | ruled out for current model | It is not measured directly; the source is a model proxy. |
| `dF_coll/dln a` proves structure creates dark energy | ruled out | It only supplies timing. No causal conversion law is derived. |
| Information production proves vacuum pressure | ruled out | No equation links information increase to `p=-rho`. |
| The branch is novel by construction | ruled out | It is an interacting-vacuum model unless the source relation is fixed by new physics. |

## 3. Parameter Classification Table

| Quantity | Current implementation | Classification | What would upgrade it? |
| --- | --- | --- | --- |
| `gamma0` | Normalization of `Gamma(a)` after source-shape normalization | fitted or assumed | Derive it from a microscopic efficiency, conservation law, or independently measured source. |
| `M` | Represented indirectly by `collapse_a`; no physical halo mass is specified | assumed | Fix a mass threshold from QFUDS microphysics, halo physics, or a pre-registered observational criterion. |
| `F_coll` | Press-Schechter-style collapsed fraction above a threshold | modeled input; partly derived within standard collapse theory | Recompute from QFUDS `P(k,a)`, QFUDS spherical collapse, and a fixed mass threshold. |
| `D(a)` | LCDM approximation inside `gamma_laws.py`; separate QFUDS scale-independent proxy exists in `qfuds/growth.py` | currently assumed/model-dependent input for `Gamma`; implemented proxy for diagnostics | Derive from closed QFUDS perturbation equations and use it consistently in `F_coll`. |

Additional implementation note: the code uses `collapse_a` rather than an
explicit `M`. In the Press-Schechter interpretation, this is equivalent to
choosing the variance scale `sigma(M)` by requiring collapse near a selected
scale factor. That is a tuning knob unless fixed before looking at results.

## 4. Literature Comparison

### Press-Schechter Collapse

Press and Schechter introduced a statistical model for self-gravitating mass
condensation in an expanding Friedmann cosmology. Modern presentations write the
collapsed mass fraction above a threshold in terms of the Gaussian-smoothed
variance and spherical-collapse threshold:

```math
F_{\rm coll}(>M,a)=
\operatorname{erfc}\left[
{\delta_c\over \sqrt{2}\sigma(M,a)}
\right].
```

This supports using `F_coll` as a collapse-history proxy. It does not support
the extra QFUDS claim that collapse produces vacuum-pressure energy.

Sources:

- Press and Schechter, "Formation of Galaxies and Clusters of Galaxies by
  Self-Similar Gravitational Condensation", ApJ 187, 425, 1974:
  https://adsabs.harvard.edu/pdf/1974ApJ...187..425P
- Dynamics and Astrophysics of Galaxies, halo mass function chapter:
  https://galaxiesbook.org/chapters/IV-01.-Formation-of-Dark-Matter-Halos_4-The-halo-mass-function.html

### Information Entropy In Cosmology

Hosoya, Buchert, and Morita define a relative-information entropy for
inhomogeneous cosmology using the Kullback-Leibler distinguishability of the
local density field from its spatial average. This supports the statement that
structure formation can be associated with increasing coarse-grained
information.

It does not derive a transfer from clustered matter into vacuum pressure.

Source:

- Hosoya, Buchert, and Morita, "Information Entropy in Cosmology",
  Phys. Rev. Lett. 92, 141302, 2004:
  https://arxiv.org/abs/gr-qc/0402076

### Interacting Dark Energy And Interacting Vacuum

The current QFUDS background equations are in the interacting dark-sector family.
The literature already studies dark matter and dark energy transforming into
each other through phenomenological interaction functions. Reviews emphasize
that the functional form of the coupling is usually assumed rather than derived.

This is the closest known model class. QFUDS is not distinct unless the
collapse/information source is fixed by a new derivation or creates a new
observable relation that survives data.

Sources:

- Harko and collaborators, "Observational constraints on the interacting dark
  energy-dark matter cosmological models", Physics of the Dark Universe 37,
  101106, 2022:
  https://www.sciencedirect.com/science/article/abs/pii/S2212686422001042
- "Theoretical and observational bounds on some interacting vacuum energy
  scenarios", 2021:
  https://arxiv.org/abs/2104.04505

### Backreaction And Structure-Linked Acceleration

Backreaction literature studies whether nonlinear structure affects the average
cosmic expansion. This is the closest conceptual neighbor to "structure affects
dark energy", but it is not the same mechanism. Backreaction modifies averaged
geometry or effective expansion; QFUDS keeps a two-phase dark sector and adds an
energy-transfer law.

This literature supports asking whether structure and expansion can be linked.
It does not support the current QFUDS phase-transfer equation.

Sources:

- Buchert, "Dark Energy from structure: a status report", 2007:
  https://arxiv.org/abs/0707.2153
- Buchert and Raesenen, "Backreaction in Late-Time Cosmology", Annual Review of
  Nuclear and Particle Science 62, 57, 2012:
  https://www.annualreviews.org/content/journals/10.1146/annurev.nucl.012809.104435

### Perturbation Instability Warning

Interacting dark-energy models can be unstable unless their perturbations are
specified consistently. This directly applies to QFUDS. A background-safe
`Gamma(a)` is not enough.

Source:

- Valiviita, Majerotto, and Maartens, "Large-scale instability in interacting
  dark energy and dark matter fluids", JCAP 2008:
  https://arxiv.org/abs/0804.0232

## 5. Self-Consistency Review

### Current Problem

The implemented information-production law depends on an LCDM growth
approximation:

- `lcdm_growth_factor_approx` computes `D(a)`.
- `_press_schechter_production` uses that `D(a)` and its logarithmic derivative.
- `gamma_information_production` normalizes the resulting source shape.

Therefore the current `Gamma(a)` source is not self-consistent QFUDS growth.

### Can `F_coll` Be Recomputed Self-Consistently Using QFUDS Growth?

In principle, yes.

Required ingredients:

1. A closed perturbation model for phase A, phase B, and transfer perturbations.
2. A QFUDS matter power spectrum `P(k,a)`, not only a scale-independent growth
   proxy.
3. A QFUDS spherical-collapse threshold `delta_c(M,a)` or a justified decision
   to keep the LCDM value.
4. A fixed mass threshold `M`.
5. A non-circular algorithm because `Gamma(a)` depends on `F_coll`, while
   `F_coll` depends on growth, and growth depends on `Gamma(a)`.

### Can It Be Done With Current Repository Contents?

No.

The current `qfuds/growth.py` growth diagnostic is useful but insufficient. It
assumes smooth phase B, dust-like phase A, and a scale-independent sub-horizon
growth equation. It does not provide:

- scale-dependent transfer functions;
- baryon/CDM separation;
- radiation-era perturbation evolution;
- transfer perturbations;
- a matter power spectrum;
- a nonlinear collapse threshold in QFUDS;
- a halo mass function.

At most, the current growth proxy could be used for an internal toy iteration:
compute background, compute scale-independent `D(a)`, recompute a toy
`F_coll`, update `Gamma(a)`, and iterate. That would still not be a physical
halo-collapse calculation.

## 6. Hidden Assumptions

The surviving branch currently smuggles in these assumptions:

1. Nonlinear collapse produces a dark-sector entropy or information measure.
2. That measure is proportional to `F_coll` rather than halo entropy, black-hole
   entropy, binding energy, virialization rate, Weyl curvature, or another
   quantity.
3. The derivative `dF_coll/dln a`, not `F_coll` itself or a delayed kernel,
   controls phase transfer.
4. The sign is fixed so phase A converts into phase B.
5. The produced phase has vacuum pressure, `w_B ~= -1`.
6. The efficiency `gamma0` is constant in time.
7. A single threshold `M` is physically meaningful.
8. The Press-Schechter shape is adequate outside LCDM.
9. The LCDM growth approximation is close enough for the current source shape.
10. Phase B remains smooth even though its production is tied to clustered
    regions.
11. Local structure production can be represented by a homogeneous background
    transfer rate.
12. The model does not double-count ordinary structure effects already present
    in GR plus CDM.

## 7. Referee Objections

### Why Should Structure Formation Generate Dark Energy?

It should not be assumed. Standard structure formation already occurs in LCDM
without creating dark energy. QFUDS must supply a conservation law, state-count
argument, action, or coarse-graining derivation showing why collapsed phase-A
degrees of freedom become smooth phase-B vacuum pressure.

Current answer: not supplied.

### Why Should Information Production Generate Vacuum Pressure?

Information production can be a coarse-grained description of inhomogeneity. It
does not by itself imply negative pressure. A referee would reject a direct jump
from "information increases" to "`w=-1` component grows" unless the stress
tensor is derived.

Current answer: not supplied.

### Is This Merely A Useful Shape?

Currently, yes. `dF_coll/dln a` is a useful shape because it is quiet in the
early universe and active around nonlinear collapse. That is a timing argument,
not a physical derivation.

### Can It Be Derived From A Microscopic Picture?

Not in the current repository. A possible future derivation would need:

- microscopic foam states or an effective action;
- a coarse-graining map from clustered phase-A states to phase-B energy;
- an entropy or information functional;
- a stress-tensor derivation showing vacuum pressure;
- a fixed efficiency and mass threshold.

### Is It Equivalent To Known Interacting Dark Energy?

At the present level, yes in broad model class. The equations are interacting
vacuum/dark-sector equations with a selected interaction function. The
collapse-sourced shape may be an interesting ansatz, but it does not escape the
known interacting-dark-energy category until the source relation is derived or
predictively fixed.

### What Would A Referee Reject Immediately?

A hostile referee would reject:

- calling `Gamma(a)` fundamental;
- calling `dF_coll/dln a` a derivation of dark energy;
- claiming CMB or matter-power viability from background tests;
- using LCDM growth to define the QFUDS source while claiming self-consistency;
- tuning `M` or `collapse_a` after seeing fits;
- treating entropy language as a stress-energy derivation;
- ignoring interacting-DE perturbation instabilities.

## 8. Recommendation

Recommendation: remain at Level 1.5.

Do not reject the branch yet, because `dF_coll/dln a` is a falsifiable,
physically motivated source shape and is narrower than a free `Gamma(a)`.

Do not proceed to full perturbation closure as if the branch were physically
derived. The branch has not earned that status.

Allowed next work:

1. Recast the branch explicitly as a phenomenological interacting-vacuum model.
2. Replace `collapse_a` with an explicit mass threshold `M` or document why that
   cannot yet be done.
3. Attempt a toy self-consistent `D(a)` iteration, clearly labeled as a toy.
4. Define the exact conditions under which the branch would be rejected before
   any perturbation implementation.

Kill or demote the branch if:

- `M` remains a tunable shape parameter;
- `gamma0` remains the only meaningful degree of freedom and absorbs all signal;
- self-consistent QFUDS growth erases the low-redshift source peak;
- perturbation closure requires arbitrary transfer perturbations;
- the branch remains indistinguishable from known interacting vacuum models.

## 9. Decision

Current classification:

```text
Gamma(a) is a phenomenological, coarse-grained effective transfer law.
The surviving source shape is motivated by collapse/information production,
but it is not derived.
```

Level status:

```text
Level 1.5: in progress
Level 2: blocked for this branch until Level 1.5 gates are satisfied
```
