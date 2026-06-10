---
doc_id: qfuds_level_1_5_equivalence_source_perturbation_audit
title: QFUDS Level 1.5 Equivalence Source Perturbation Audit
doc_type: theory_note
stage: "1.5"
status: completed
evidence_role: audit
depends_on:
  - qfuds_v0_15_phase_transfer_physics
  - level_1_5_resolution_gate
  - retained_branch_source_closure_plan_provenance
next_gate: retained branch demoted; future physical-QFUDS branches must pass the admission rule
last_updated: 2026-06-09
---

# QFUDS Level 1.5 Equivalence Source Perturbation Audit

Date: 2026-06-09

This document performs the [Level 1.5](../wiki/glossary/repository_levels.md) audit before any numerical `exp_004` or
physical Level 2B work begins. It asks whether the retained
collapse/information-production transfer shape is physical, equivalent to known
interacting-vacuum models, or only phenomenological.

It does not change roadmap status. Current status remains in
[000_roadmap.md](../05_next_steps/000_roadmap.md).

## Summary Verdict

Final retained-branch verdict:

```text
The retained collapse/information-production Gamma(a) branch fails physical
Level 1.5 promotion and is demoted to phenomenological interacting-vacuum
status. This does not falsify the broader DM-to-DE phase-transition hypothesis;
it rejects only the current retained source relation as a physical derivation.
```

The branch remains useful only as a constrained phenomenological source shape.
It is not promoted to physical Level 2B.

## Evidence Reviewed

Repository evidence:

- [015_qfuds_v0_15_phase_transfer_physics.md](015_qfuds_v0_15_phase_transfer_physics.md)
- [015_level_1_5_resolution_gate.md](../05_next_steps/015_level_1_5_resolution_gate.md)
- [015_retained_branch_source_closure_plan_provenance.md](../05_next_steps/015_retained_branch_source_closure_plan_provenance.md)
- [015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md)
- [020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md)
- [030_result_003_phenomenological_perturbation_closure.md](../04_results/030_result_003_phenomenological_perturbation_closure.md)
- `qfuds/gamma_laws.py`
- `qfuds/growth.py`
- `qfuds/perturbations.py`

External comparison points:

- Interacting dark energy and interacting vacuum models:
  https://arxiv.org/abs/1603.08299,
  https://arxiv.org/abs/2404.02110
- Perturbation stability and closure frameworks:
  https://arxiv.org/abs/0804.0232,
  https://arxiv.org/abs/1404.5220,
  https://arxiv.org/abs/2504.17293
- Unified dark-sector and decomposed-fluid models:
  https://arxiv.org/abs/astro-ph/0212114,
  https://arxiv.org/abs/1301.5315
- Collapse and information-source background:
  https://adsabs.harvard.edu/pdf/1974ApJ...187..425P,
  https://arxiv.org/abs/gr-qc/0402076
- Structure-linked acceleration and black-hole coupling neighbors:
  https://arxiv.org/abs/0707.2153,
  https://arxiv.org/abs/2302.07878

## Equivalence Audit

Question:

```text
Can QFUDS be rewritten as an existing interacting-vacuum or interacting
dark-energy model?
```

### Evidence Reviewed

The QFUDS background equations are:

```math
{d\rho_A\over d\ln a}+3\rho_A=-\Gamma(a)\rho_A,
\qquad
{d\rho_B\over d\ln a}=\Gamma(a)\rho_A.
```

This can be mapped to an interacting-vacuum form with energy transfer

```math
Q = H\Gamma(a)\rho_A,
```

up to sign convention and frame choice. At this level, phase A behaves as a
dust-like component and phase B behaves as a vacuum-like component receiving
energy.

The candidate novelty is not the existence of a dark-sector interaction. The
candidate novelty would have to be the fixed relation:

```math
\Gamma(a) \propto {dF_{\rm coll}(>M,a)\over d\ln a}.
```

### Pass Criteria

The equivalence audit passes for physical QFUDS only if QFUDS supplies something
not absorbed into an arbitrary interacting-vacuum `Q(a)`, such as:

- a derived stress-energy transfer equation `Q^\nu`;
- a fixed source relation tied to a physical scalar rather than a fitted time
  function;
- a constraint or observable relation not already present in generic
  interacting-vacuum or unified-fluid models.

### Fail Criteria

The branch fails as distinct physical QFUDS if:

- all dynamics can be written as ordinary interacting vacuum with selected
  `Q(a)`;
- `Gamma(a)` is only a reparameterized coupling function;
- the source relation does not impose a new constraint, prediction, or
  perturbation prescription.

### Current Status

Current status: fail for distinct physical promotion.

QFUDS can currently be rewritten as an interacting-vacuum background model with
the special ansatz `Q = H Gamma(a) rho_A`. What is genuinely new is only the
proposed collapse/information timing ansatz. What is merely reparameterized is
the existence of dark-sector energy transfer.

### What Would Change The Verdict

The verdict changes only if the branch derives or externally fixes the
collapse/information source relation so that `Q(a)` is no longer a freely chosen
interaction history.

## Source Audit

Question:

```text
Is Gamma(a) = dF_coll/dln(a) a physically defined source quantity?
```

### Evidence Reviewed

The implemented source shape uses a Press-Schechter-style collapsed fraction and
normalizes the derivative:

```math
\Gamma(a)=\gamma_0
{dF_{\rm coll}/d\ln a\over \max_a(dF_{\rm coll}/d\ln a)}.
```

`F_coll` is dimensionless. `dF_coll/dln(a)` is also dimensionless because
`ln(a)` is dimensionless. Therefore the normalized source shape is dimensionless
and `gamma0` carries the effective transfer strength per `dln(a)` in the
repository equations.

### Pass Criteria

The source audit passes only if all of the following are supplied before fitting:

- units and normalization of the source scalar;
- physical threshold `M`, not implicit `collapse_a`;
- a conservation-law role explaining what phase A loses and what phase B gains;
- a non-circular derivation path for `F_coll` using QFUDS growth or an explicitly
  bounded proxy;
- classification of `gamma0` as derived, externally fixed, independently
  bounded, fitted, or phenomenological.

### Fail Criteria

The source audit fails as physical QFUDS if:

- `collapse_a` remains the operational threshold;
- `dF_coll/dln(a)` only supplies timing;
- LCDM growth is used while self-consistency is claimed;
- `gamma0` remains an unconstrained efficiency;
- no equation links collapse or information production to vacuum-pressure phase
  B.

### Current Status

Current status: fail for physical source definition; retain only as a
phenomenological source shape.

The source has a mathematically clear shape, but not a physical conservation-law
role. It is not enough to say that collapse or information production occurs.
The missing step is why that scalar converts clustered phase-A energy into a
smooth `w_B ~= -1` phase.

Missing assumptions are:

- the physical mass threshold `M`;
- the QFUDS-specific `P(k,a)` or growth computation;
- the QFUDS spherical-collapse threshold or justified imported threshold;
- the conversion efficiency behind `gamma0`;
- the stress-energy accounting that creates phase B.

### What Would Change The Verdict

The verdict changes if a derivation or externally fixed model supplies:

```math
Q^\nu = Q^\nu[X, u^\nu, \rho_A, \rho_B, ...]
```

with `X` identified as a real collapse/information scalar, fixed thresholds, and
non-circular source computation. A better numerical fit does not change this
verdict.

## Perturbation Readiness Audit

Question:

```text
Can delta Q, frame choice, gauge choice, and phase-A/phase-B perturbation
prescriptions be specified without introducing new ad hoc assumptions?
```

### Evidence Reviewed

The Level 2A `exp_003` closure deliberately treated `Gamma(a)` as
phenomenological. It used a declared perturbation closure to test stability, not
to derive transfer physics.

The Level 1.5 gate requires the transfer frame, gauge assumptions, `delta Q`,
and phase responses to be specified before physical Level 2B begins.

### Pass Criteria

The perturbation-readiness audit passes only if the model can state, before
Level 2B:

- the transfer four-vector `Q^\nu`;
- whether transfer is parallel to phase-A, phase-B, total-fluid, or another
  four-velocity;
- the gauge and frame used to define perturbations;
- whether `delta Gamma`, `delta F_coll`, or `delta X` exists and how it is
  computed;
- phase-A continuity/Euler response;
- phase-B response, including whether phase B is smooth vacuum, a regularized
  fluid, or another object.

### Fail Criteria

The audit fails for physical Level 2B if:

- `delta Q` is chosen only to make the equations stable;
- phase B is declared smooth without a physical reason after being sourced by
  clustered collapse;
- the transfer frame is selected after seeing stability behavior;
- pressure, sound speed, or momentum-transfer terms are added only as regulators;
- the prescription reduces to known interacting-vacuum phenomenology without a
  new source relation.

### Current Status

Current status: fail for physical Level 2B readiness.

The repository can run a phenomenological closure. It cannot yet specify a
physical perturbation prescription derived from the collapse/information source.
In particular, `delta Q` is not derived from `delta F_coll`, halo formation, an
entropy functional, or a stress-energy source.

### What Would Change The Verdict

The verdict changes only if the transfer law fixes perturbations before the
stability test is run. The minimum upgrade is a written prescription for
`delta Q` and the transfer frame that follows from the same source model used at
background level.

## Overall Decision

The retained branch is demoted to phenomenological interacting vacuum. Do not
start physical Level 2B for this branch.

## Future-Branch Admission Rule

No new physical-QFUDS branch should be opened unless it provides, at minimum:

- `X =`
- `Q^nu =`
- `why phase B has w ~= -1 =`
- `delta Q route =`
- `known-model distinction =`
