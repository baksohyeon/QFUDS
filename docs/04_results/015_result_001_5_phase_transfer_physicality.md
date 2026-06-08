---
doc_id: result_001_5_phase_transfer_physicality
title: "Result 001.5: Phase Transfer Physicality Audit"
doc_type: result
stage: "1.5"
status: in_progress
evidence_role: audit
depends_on:
  - exp_001_5_phase_transfer_physicality
  - result_002_entropy_information_gate
next_gate: resolve physicality before exp_003
last_updated: 2026-06-08
---

# Result 001.5: Phase Transfer Physicality Audit

Date: 2026-06-08

## What Did We Learn?

The surviving experiment 002 branch:

```math
\Gamma(a) \propto {dF_{\rm coll}(>M,a)\over d\ln a}
```

has not earned direct promotion to perturbation theory.

Stronger audit result: experiment 002 is not meaningful physical data for the
surviving branch. It was run before the phase-transfer mechanism, physical mass
threshold, and self-consistent QFUDS growth source were defined.

Current result:

```text
Gamma(a) is a phenomenological coarse-grained transfer law with a physically
motivated source shape. It is not yet derived physical phase transfer.
```

This is a Level 1.5 result, not a Level 2 perturbation result.

## Scope

This audit evaluates physical interpretation and self-consistency only. It does
not implement perturbation equations, CLASS/CAMB, CMB spectra, matter power, or
survey likelihoods.

## Main Finding

The collapse/information-production branch remains the only narrow shape left
after experiment 002, but this should not be read as survival evidence. The
repository has not derived why nonlinear collapse or information production
should convert phase A into smooth vacuum-pressure phase B.

The branch is therefore retained only as a question to clarify, not as a
physical law and not as data to carry directly into Level 2.

## Parameter Status

| Quantity | Current classification | Reason |
| --- | --- | --- |
| `gamma0` | fitted or assumed | No microscopic efficiency or conservation law fixes it. |
| `M` | assumed | The implementation uses `collapse_a`; no physical halo mass threshold is fixed. |
| `F_coll` | modeled input, partly standard-theory derived | Press-Schechter collapse is known, but not QFUDS-derived. |
| `D(a)` | model-dependent input in `Gamma(a)` | The current source uses LCDM-style growth approximations. |

## Self-Consistency Result

`F_coll` cannot yet be recomputed self-consistently from repository contents.

Required missing ingredients:

- closed phase-A, phase-B, and transfer perturbation equations;
- QFUDS matter power spectrum `P(k,a)`;
- QFUDS spherical-collapse threshold or a justified imported threshold;
- fixed mass threshold `M`;
- non-circular iteration because `Gamma(a)` depends on `F_coll`, while
  `F_coll` depends on growth, and growth depends on `Gamma(a)`.

## Hostile Verdict

A referee would reject:

- calling `Gamma(a)` fundamental;
- calling `dF_coll/dln(a)` a derivation of dark energy;
- claiming CMB or matter-power viability from background tests;
- using LCDM growth to define the QFUDS source while claiming self-consistency;
- tuning `M` or `collapse_a` after looking at results;
- treating entropy language as a stress-energy derivation.

## Decision

Remain at QFUDS v0.15 / Level 1.5.

Demote experiment 002 to provenance:

```text
exp_002 killed broad entropy language and identified a useful shape to audit.
It did not produce physically meaningful evidence for phase transfer.
```

Do not create `exp_003` or begin Level 2 perturbation closure until the
Level 1.5 gate is resolved or the branch is explicitly demoted to a
phenomenological interacting-vacuum model.

Evidence:

- `docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md`
- `docs/03_experiments/015_exp_001_5_phase_transfer_physicality.md`
- `docs/04_results/020_result_002_entropy_information_gate.md`
- `qfuds/gamma_laws.py`
- `qfuds/growth.py`
