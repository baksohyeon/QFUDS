---
doc_id: result_001_5_phase_transfer_physicality
title: "Result 001.5: Phase Transfer Physicality Audit"
doc_type: result
stage: "1.5"
status: completed
evidence_role: audit
depends_on:
  - exp_001_5_phase_transfer_physicality
  - result_002_entropy_information_gate
  - qfuds_level_1_5_transfer_four_vector_derivation_attempt
next_gate: retained branch demoted; no physical Level 2B without a new admitted physical branch
last_updated: 2026-06-09
---

# Result 001.5: Phase Transfer Physicality Audit

Date: 2026-06-08

## What Did We Learn?

The surviving experiment 002 branch:

```math
\Gamma(a) \propto {dF_{\rm coll}(>M,a)\over d\ln a}
```

has not earned direct promotion to physical perturbation theory.

Stronger audit result: experiment 002 is not meaningful physical data for the
surviving branch. It was run before the phase-transfer mechanism, physical mass
threshold, and self-consistent QFUDS growth source were defined.

Final result for the retained branch:

```text
The retained collapse/information-production Gamma(a) branch fails physical
Level 1.5 promotion and is demoted to phenomenological interacting-vacuum
status. This does not falsify the broader DM-to-DE phase-transition hypothesis;
it rejects only the current retained source relation as a physical derivation.
```

This is a Level 1.5 result, not a Level 2 perturbation result. It does not
forbid a Level 2A phenomenological perturbation-closure audit.

## Scope

This audit evaluates physical interpretation and self-consistency only. It does
not implement perturbation equations, CLASS/CAMB, CMB spectra, matter power, or
survey likelihoods.

## Main Finding

The collapse/information-production branch remains the only narrow shape left
after experiment 002, but this should not be read as survival evidence. The
repository has not derived why nonlinear collapse or information production
should convert phase A into smooth vacuum-pressure phase B.

The branch is therefore closed as a physical Level 1.5 candidate. It remains
usable only as a phenomenological interacting-vacuum transfer shape, not as data
to carry directly into physical Level 2B.

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

Close the retained-branch Level 1.5 investigation as a physical-promotion
failure.

Demote experiment 002 to provenance:

```text
exp_002 killed broad entropy language and identified a useful shape to audit.
It did not produce physically meaningful evidence for phase transfer.
```

Do not treat `exp_003` as physical QFUDS evidence. `exp_003` may proceed only
as Level 2A phenomenological perturbation closure. Level 2B remains blocked for
this retained branch because it has been explicitly demoted to a
phenomenological interacting-vacuum model.

Evidence:

- [docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md](../02_theory/015_qfuds_v0_15_phase_transfer_physics.md)
- [docs/02_theory/015_qfuds_level_1_5_equivalence_source_perturbation_audit.md](../02_theory/015_qfuds_level_1_5_equivalence_source_perturbation_audit.md)
- [docs/02_theory/015_qfuds_level_1_5_transfer_four_vector_derivation_attempt.md](../02_theory/015_qfuds_level_1_5_transfer_four_vector_derivation_attempt.md)
- [docs/03_experiments/015_exp_001_5_phase_transfer_physicality.md](../03_experiments/015_exp_001_5_phase_transfer_physicality.md)
- [docs/04_results/020_result_002_entropy_information_gate.md](020_result_002_entropy_information_gate.md)
- `qfuds/gamma_laws.py`
- `qfuds/growth.py`

## Evidence

The audit is supported by the theory note, experiment specification, demoted
experiment 002 result, and implementation files listed above. It produced a
classification decision, not a new numerical output table.

## Future-Branch Admission Rule

No new physical-QFUDS branch should be opened unless it provides, at minimum:

- `X =`
- `Q^nu =`
- `why phase B has w ~= -1 =`
- `delta Q route =`
- `known-model distinction =`

## Next Gate

Keep physical Level 2B blocked. A future physical-QFUDS branch must first pass
the admission rule above and then satisfy the Level 1.5 evidence gate before
physical perturbation equations are opened.
