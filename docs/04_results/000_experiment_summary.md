---
doc_id: experiment_summary
title: QFUDS Experiment Summary
doc_type: summary
stage: "2"
status: in_progress
evidence_role: audit
depends_on:
  - result_000_lcdm_baseline
  - result_001_gamma_scan
  - result_001_5_phase_transfer_physicality
  - result_002_entropy_information_gate
  - result_003_phenomenological_perturbation_closure
next_gate: keep Level 2B blocked; use roadmap for current status
last_updated: 2026-06-09
---

# QFUDS Experiment Summary

Date: 2026-06-09

This summary answers what each completed or in-progress experiment has taught
so far. It is not the current project-status authority. For current level,
active branch, and blockers, use [docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md).

## Current Evidence Boundary

The repository has validated background behavior and one phenomenological
perturbation closure. It has not validated physical QFUDS perturbations, CMB
spectra, matter power, BAO, supernovae, DESI, Euclid, Roman, or survey
likelihoods.

## Summary Table

| Experiment | Scope | Target | Primary evidence | Verdict | Epistemic classification | Next gate |
| --- | --- | --- | --- | --- | --- | --- |
| `exp_000` | background control | zero-transfer LCDM limit | `outputs/qfuds_gamma0_beta0.csv`, `tests/test_gamma_v03.py` | control passed | not novel; regression baseline | compare every nonzero transfer law against it |
| `exp_001` | background scan plus growth proxy | candidate `Gamma(a)` laws | `outputs/qfuds_*gamma*.csv`, [docs/04_results/010_result_001_gamma_scan.md](010_result_001_gamma_scan.md) | constant and ungated growth-driven laws rejected; low-redshift proxies retained | proxy scan only | phase-transfer physicality |
| `exp_001_5` | physicality audit | whether retained collapse/information-production transfer is physical | [docs/04_results/015_result_001_5_phase_transfer_physicality.md](015_result_001_5_phase_transfer_physicality.md), `qfuds/gamma_laws.py` | `Gamma(a)` remains phenomenological | audit; physical Level 2B blocked | define mechanism, mass threshold, self-consistent growth, and transfer perturbations |
| `exp_002` | background entropy/information-source scan | entropy or information source for transfer | `outputs/qfuds_information_production_gamma0.02_beta0.csv`, [docs/04_results/020_result_002_entropy_information_gate.md](020_result_002_entropy_information_gate.md) | broad entropy language killed; collapse/information-production shape retained only as a question | provenance, not current evidence | Level 1.5 physicality audit |
| `exp_003` | Level 2A phenomenological perturbation stability | P1 interacting-vacuum vs P2 regularized-fluid closure | `outputs/exp003_stability_diagnostics.csv`, [docs/04_results/030_result_003_phenomenological_perturbation_closure.md](030_result_003_phenomenological_perturbation_closure.md) | P2 fails at retained amplitude; P1 remains stable only as phenomenological interacting vacuum | non-novel Level 2A phenomenology | physical Level 2B remains blocked |

## Conclusions So Far

1. QFUDS has a correct LCDM null limit when `Gamma(a)=0`.
2. Free or early-active transfer laws are either rejected or collapse into known
   interacting-dark-energy behavior.
3. Low-redshift collapse/information-production timing is the only retained
   shape, but it is not physical evidence.
4. The retained transfer source still lacks a derived mechanism, fixed mass
   threshold, and self-consistent QFUDS growth source.
5. P2, the regularized near-vacuum fluid closure, fails at the retained
   amplitude.
6. P1 can be integrated stably in the current audit, but only as a
   phenomenological interacting-vacuum closure. It is not a physical QFUDS
   derivation and is not novel by itself.

## Postmortem Coverage

There is one formal postmortem so far:

[outputs/postmortem/exp003_friction_bug/README.md](../../outputs/postmortem/exp003_friction_bug/README.md)

It records the exp_003 Euler-friction bug, affected diagnostics, correction, and
old-vs-new conclusion. Earlier negative results do not require separate
postmortems because their failure modes are already recorded in their result
documents and the decision log.

Future bugs, superseded outputs, or conclusion changes should get a postmortem
under the policy in [docs/00_project/experiment_record_convention.md](../00_project/experiment_record_convention.md).

## Verification Commands

Use these commands to check the record:

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/preflight_exp004.py
```
