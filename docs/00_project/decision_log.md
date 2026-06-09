---
doc_id: decision_log
title: QFUDS Decision Log
doc_type: decision_log
stage: "1.5"
status: in_progress
evidence_role: ssot
depends_on:
  - roadmap
next_gate: retained branch demoted; no physical Level 2B without a new admitted physical branch
last_updated: 2026-06-09
---

# QFUDS Decision Log

This log records research decisions, not only implementation changes.

## 2026-06-08

Decision:
Keep the zero-transfer run as the LCDM regression baseline.

Reason:
With `Gamma(a)=0`, the two-phase background reproduces the LCDM control path. This is not a novel QFUDS prediction, but it is the required null comparison for every nonzero transfer law.

Evidence:
[docs/03_experiments/000_exp_000_lcdm_baseline.md](../03_experiments/000_exp_000_lcdm_baseline.md), [docs/04_results/000_result_000_lcdm_baseline.md](../04_results/000_result_000_lcdm_baseline.md), `outputs/qfuds_gamma0_beta0.csv`, `outputs/figures/result000_lcdm_baseline.png`, `tests/test_gamma_v03.py`

## 2026-06-08

Decision:
Reject the white-hole-universe image as the central QFUDS claim.

Reason:
It is too broad to test directly and does not provide a controlled cosmological model.

Evidence:
[docs/01_origin/concept_origin.md](../01_origin/concept_origin.md), [docs/00_project/research_program.md](research_program.md), [docs/02_theory/000_qfuds_v0_1_conceptual_origin.md](../02_theory/000_qfuds_v0_1_conceptual_origin.md)

## 2026-06-08

Decision:
Adopt the two-phase dark-sector formulation as the minimal working model.

Reason:
It makes the LCDM limit, phase-transfer problem, sound-speed constraint, and observational kill criteria explicit.

Evidence:
[docs/02_theory/900_qfuds_research_report.md](../02_theory/900_qfuds_research_report.md), [docs/02_theory/000_qfuds_v0_2_two_phase_background.md](../02_theory/000_qfuds_v0_2_two_phase_background.md), `qfuds/background.py`

## 2026-06-08

Decision:
Treat QFUDS as non-novel until it specifies a derived microphysical action, a fixed transfer law, or a perturbation prescription that survives data.

Reason:
With `Gamma=0`, the model is LCDM. With free `Gamma(a)`, it is a known interacting dark-sector model.

Evidence:
[docs/02_theory/900_qfuds_research_report.md](../02_theory/900_qfuds_research_report.md)

## 2026-06-08

Decision:
Reject constant Gamma transfer at the tested amplitude.

Reason:
It creates negative `rho_B` in the backward-integrated background and fails early-universe viability checks.

Evidence:
[docs/04_results/010_result_001_gamma_scan.md](../04_results/010_result_001_gamma_scan.md), [docs/03_experiments/010_exp_001_gamma_scan.md](../03_experiments/010_exp_001_gamma_scan.md), `outputs/qfuds_constant_gamma0.01_beta0.csv`, `outputs/figures/result001_gamma_scan_summary.png`

## 2026-06-08

Decision:
Reject ungated growth-driven Gamma transfer at the tested amplitude.

Reason:
The growth proxy is active during matter domination, so the transfer turns on too early and fails the background viability checks.

Evidence:
[docs/04_results/010_result_001_gamma_scan.md](../04_results/010_result_001_gamma_scan.md), `outputs/qfuds_growth_driven_gamma0.01_beta0.csv`, `outputs/figures/result001_gamma_scan_summary.png`

## 2026-06-08

Decision:
Keep low-redshift collapse, black-hole-entropy, and star-formation proxies as candidate shapes for later scrutiny.

Reason:
They pass minimal background checks in the experiment 001 scan and naturally defer transfer until late times. Later Level 1.5 work blocks direct perturbation promotion until phase-transfer physicality is resolved.

Evidence:
[docs/04_results/010_result_001_gamma_scan.md](../04_results/010_result_001_gamma_scan.md), `outputs/qfuds_collapsed_fraction_toy_gamma0.03_beta0.csv`, `outputs/qfuds_black_hole_entropy_proxy_gamma0.03_beta0.csv`, `outputs/qfuds_star_formation_proxy_gamma0.003_beta0.csv`, `outputs/figures/result001_gamma_scan_summary.png`

## 2026-06-08

Decision:
Make documentation the primary source of truth for experiment history.

Reason:
Future researchers need the reasoning trail, failed ideas, surviving assumptions, code paths, outputs, and next decisions without relying on chat history.

Evidence:
[docs/00_project/overview.md](overview.md), `docs/03_experiments/`, `docs/04_results/`, [docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md)

## 2026-06-08

Decision:
Keep only the collapse/information-production branch from experiment 002.

Reason:
Horizon information is physically clean but reduces to standard horizon/interacting dark energy. HBM/KL gravitational entropy is too broad in time and fails positivity unless the coupling is tiny. Press-Schechter information production is the only tested entropy-derived shape that naturally vanishes in radiation domination, peaks after nonlinear collapse begins, and gives a falsifiable relation between `w(a)` and growth history.

Evidence:
[docs/04_results/020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md), `outputs/qfuds_information_production_gamma0.02_beta0.csv`, `outputs/qfuds_horizon_information_gamma0.03_beta0.csv`, `outputs/qfuds_gravitational_entropy_gamma0.003_beta0.csv`, `outputs/figures/result002_entropy_information_summary.png`

## 2026-06-08

Decision:
Insert Level 1.5, phase transfer physicality, before perturbation closure.

Reason:
The surviving collapse/information-production branch is narrower than a free `Gamma(a)`, but the repository has not derived why collapse or information production should convert phase A into vacuum-pressure phase B. The current `Gamma(a) proportional to dF_coll/dln(a)` law is best classified as a phenomenological coarse-grained interacting-vacuum transfer law with a physically motivated source shape. It also uses LCDM-style growth approximations in the source and does not yet define a physical mass threshold `M`.

Evidence:
[docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md](../02_theory/015_qfuds_v0_15_phase_transfer_physics.md), `qfuds/gamma_laws.py`, `qfuds/growth.py`, [docs/04_results/020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md), `outputs/figures/result002_entropy_information_summary.png`

## 2026-06-08

Decision:
Demote experiment 002 from evidence to provenance.

Reason:
The experiment 002 information-production scan was run before the physical
phase-transfer mechanism, fixed mass threshold `M`, and self-consistent QFUDS
growth source were defined. Its outputs can show that broad entropy language
and some proxy shapes fail, but they are not physically meaningful data for a
surviving QFUDS branch.

Evidence:
[docs/04_results/015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md), [docs/04_results/020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md), [docs/03_experiments/020_exp_002_entropy_information_gate.md](../03_experiments/020_exp_002_entropy_information_gate.md), `outputs/figures/result001_5_physicality_audit.png`

## 2026-06-08

Decision:
Split Level 2 into Level 2A phenomenological perturbation closure and Level 2B physical perturbation closure.

Reason:
The literature does not require a microscopic derivation before perturbation theory. Interacting dark energy, interacting vacuum, generalized dark matter, generalized Chaplygin gas, and PPF-style models all use perturbation closures to test phenomenological dark-sector assumptions. The missing requirement is not microphysics by itself; it is a closed, covariant, gauge-declared transfer prescription. Level 1.5 remains required for physical QFUDS claims.

Evidence:
[docs/02_theory/030_qfuds_phenomenological_perturbations.md](../02_theory/030_qfuds_phenomenological_perturbations.md), [docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md](../03_experiments/030_exp_003_phenomenological_perturbation_closure.md), [docs/05_next_steps/010_perturbation_gate.md](../05_next_steps/010_perturbation_gate.md)

## 2026-06-08

Decision:
Record experiment 003 as a partial failure: P2 regularized phase-B fluid fails, P1 interacting vacuum remains mathematically closed.

Reason:
The retained information-production amplitude `gamma0=0.02` produces instability in the P2 regularized-fluid closure for every tested wavenumber. The P1 interacting-vacuum closure remains numerically stable, but this is not a physical QFUDS derivation and is closest to known phenomenological interacting-vacuum models.

Evidence:
[docs/04_results/030_result_003_phenomenological_perturbation_closure.md](../04_results/030_result_003_phenomenological_perturbation_closure.md), `outputs/exp003_stability_diagnostics.csv`, `outputs/exp003_phenomenological_perturbation_summary.json`, `outputs/figures/exp003_stability_summary.png`, `qfuds/perturbations.py`

## 2026-06-08

Decision:
Correct the exp_003 phase-A and phase-B Euler friction bug, re-run the suite, and
re-evaluate the P1 verdict from scratch. Keep P1 as a surviving but non-novel
Level 2A interacting-vacuum closure.

Reason:
Hostile verification against the repository's own validated `qfuds/growth.py`
showed both Euler equations in `qfuds/perturbations.py` carried one extra unit of
Hubble friction (base constant `2.0` on the conformal log-derivative
`dln_hc_dx = 1 + dlnH/dlna`, where the correct base for the integrated `theta/Hc`
variable is `1.0`). The bug over-damped phase A: its matter-era growing-mode
exponent was approximately 0.6 instead of the cold-dark-matter value approximately
1.0. After the fix phase A clusters with exponent approximately 0.9, close to the
`growth.py` reference approximately 0.97. The corrected run did not kill P1: P1 is
stable at every tested amplitude and wavenumber, and P2 still fails at the
retained `gamma0=0.02` and at `gamma0=0.04`. The survive/fail classification was
unchanged; the bug had corrupted the clustering diagnostic and instability
magnitudes, and had made the original "phase-A clustering not lost" statement
unjustified. P1 survival remains qualified: the algebraic Newtonian-gauge `Phi`
closure cannot test superhorizon curvature instability, the Poisson source omits
baryons, and `deltaGamma=0` is phenomenological. Original outputs are preserved as
provenance, not deleted.

Evidence:
`qfuds/perturbations.py`, [outputs/postmortem/exp003_friction_bug/README.md](../../outputs/postmortem/exp003_friction_bug/README.md), `outputs/postmortem/exp003_friction_bug/`, `outputs/exp003_stability_diagnostics.csv`, [docs/04_results/030_result_003_phenomenological_perturbation_closure.md](../04_results/030_result_003_phenomenological_perturbation_closure.md)

## 2026-06-09

Decision:
The retained collapse/information-production Gamma(a) branch fails physical
Level 1.5 promotion and is demoted to phenomenological interacting-vacuum
status. This does not falsify the broader DM-to-DE phase-transition hypothesis;
it rejects only the current retained source relation as a physical derivation.

Reason:
The retained relation `Gamma(a) proportional to dF_coll/dln(a)` can be written
as an interacting-vacuum background ansatz, but the repository does not derive a
non-ad hoc source scalar, physical threshold `M`, transfer four-vector,
phase-B vacuum-pressure response, or `delta Q` prescription from the same
mechanism. The smallest attempted candidate `Q^nu` reproduces the background
equations only by adding unsupported assumptions, so it is conservation-compatible
phenomenology rather than physical QFUDS.

Future-branch admission rule:
No new physical-QFUDS branch should be opened unless it provides, at minimum:

- `X =`
- `Q^nu =`
- `why phase B has w ~= -1 =`
- `delta Q route =`
- `known-model distinction =`

Evidence:
[docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md), [docs/05_next_steps/015_level_1_5_resolution_gate.md](../05_next_steps/015_level_1_5_resolution_gate.md), [docs/02_theory/015_qfuds_level_1_5_equivalence_source_perturbation_audit.md](../02_theory/015_qfuds_level_1_5_equivalence_source_perturbation_audit.md), [docs/02_theory/015_qfuds_level_1_5_transfer_four_vector_derivation_attempt.md](../02_theory/015_qfuds_level_1_5_transfer_four_vector_derivation_attempt.md), [docs/02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md](../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md), [docs/04_results/015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md), `outputs/figures/result001_5_physicality_audit.png`, `qfuds/gamma_laws.py`

## 2026-06-09

Decision:
Classify retained P1 as an exact interacting-vacuum instance and a subset of
generic time-dependent interacting dark energy under `xi(a)=Gamma(a)`.

Reason:
Experiment 004 compared retained P1 against LCDM, the direct interacting-vacuum
mapping, generic time-dependent IDE, constant-coupling transfer, power-law
transfer, and an effective non-interacting `w(a)` reconstruction. The direct
interacting-vacuum mapping has zero background, transfer, growth, and Level 2A
P1 perturbation differences. Generic IDE is a broader analytic family, not an
independent numerical baseline unless a distinct IDE closure is supplied.
Constant and power-law transfer baselines do not reproduce the retained transfer
shape within the predeclared thresholds, so their differences are
parameterization differences, not physical distinctions. The effective `w(a)`
route is background-degenerate only and has no transfer perturbation.

Evidence:
[docs/03_experiments/030_exp_004_p1_model_family_positioning.md](../03_experiments/030_exp_004_p1_model_family_positioning.md), [docs/04_results/030_result_004_p1_model_family_positioning.md](../04_results/030_result_004_p1_model_family_positioning.md), `outputs/exp004_positioning_summary.json`, `outputs/exp004_baseline_comparison.csv`, `outputs/exp004_closure_frame_mapping.csv`, `outputs/figures/exp004_gamma_shape_comparison.png`, `qfuds/positioning.py`

## 2026-06-09

Decision:
Classify retained `Gamma(a)` timing as a potential IV/IDE prior-compression
target, not as a physical source or distinct model family.

Reason:
Experiment 005 compared the retained normalized timing profile against rigid
constant and power-law couplings, compact transition and smooth-pulse families,
tomographic approximations, and a flexible reconstruction proxy. Constant,
power-law, transition, logistic-rate, Gaussian, and low-bin tomographic
families did not pass the predeclared timing-shape threshold. The eight-knot
reconstruction proxy did pass. The retained profile is therefore not supported
as a unique physical or timing family, but it remains potentially useful as a
compact, interpretable target for compressing reconstructed IV/IDE coupling
histories if future reconstructions prefer similar support.

Evidence:
[docs/03_experiments/030_exp_005_timing_prior_usefulness.md](../03_experiments/030_exp_005_timing_prior_usefulness.md), [docs/04_results/030_result_005_timing_prior_usefulness.md](../04_results/030_result_005_timing_prior_usefulness.md), `outputs/exp005_timing_prior_summary.json`, `outputs/exp005_timing_family_comparison.csv`, `outputs/exp005_timing_fingerprint.csv`, `outputs/figures/exp005_timing_family_errors.png`, `qfuds/timing_prior.py`

## 2026-06-09

Decision:
Classify retained `Gamma(a)` timing as `allowed_but_not_informative` against
the inspected table-level literature products.

Reason:
Experiment 006 used Escamilla et al. 2023 as the primary IV/IDE kernel target,
Goh et al. 2023 as a secondary scalar-field CDE proxy, and left Bonilla et al.
2022 optional because no table-level coupling history was available without
author data or digitization. Escamilla's GP nodes overlap the retained weighted
mean and peak regions, and the paper reports a weak structure-era feature near
`z ~ 2.3`, but the relevant `Pi_DE` table constraints are broad,
zero-compatible, or unconstrained. The high-redshift shoulder is not tested
because `Pi_5` is unconstrained in all Escamilla cases. Goh does not contradict
the broad timing allowance, but it is only a proxy and cannot promote the
conclusion.

Evidence:
[docs/03_experiments/030_exp_006_literature_timing_support_audit.md](../03_experiments/030_exp_006_literature_timing_support_audit.md), [docs/04_results/030_result_006_literature_timing_support_audit.md](../04_results/030_result_006_literature_timing_support_audit.md), `outputs/exp006_literature_target_feasibility.csv`, `outputs/exp006_literature_timing_support_matrix.csv`, `outputs/exp006_literature_classification.json`
