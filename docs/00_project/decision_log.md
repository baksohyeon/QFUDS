# Decision Log

This log records research decisions, not only implementation changes.

## 2026-06-08

Decision:
Keep the zero-transfer run as the LCDM regression baseline.

Reason:
With `Gamma(a)=0`, the two-phase background reproduces the LCDM control path. This is not a novel QFUDS prediction, but it is the required null comparison for every nonzero transfer law.

Evidence:
`docs/03_experiments/000_exp_000_lcdm_baseline.md`, `docs/04_results/000_result_000_lcdm_baseline.md`, `outputs/qfuds_gamma0_beta0.csv`, `tests/test_gamma_v03.py`

## 2026-06-08

Decision:
Reject the white-hole-universe image as the central QFUDS claim.

Reason:
It is too broad to test directly and does not provide a controlled cosmological model.

Evidence:
`docs/01_origin/concept_origin.md`, `docs/00_project/research_program.md`, `docs/02_theory/010_qfuds_v0_1.md`

## 2026-06-08

Decision:
Adopt the two-phase dark-sector formulation as the minimal working model.

Reason:
It makes the LCDM limit, phase-transfer problem, sound-speed constraint, and observational kill criteria explicit.

Evidence:
`docs/02_theory/900_qfuds_research_report.md`, `docs/02_theory/020_qfuds_v0_2.md`, `qfuds/background.py`

## 2026-06-08

Decision:
Treat QFUDS as non-novel until it specifies a derived microphysical action, a fixed transfer law, or a perturbation prescription that survives data.

Reason:
With `Gamma=0`, the model is LCDM. With free `Gamma(a)`, it is a known interacting dark-sector model.

Evidence:
`docs/02_theory/900_qfuds_research_report.md`

## 2026-06-08

Decision:
Reject constant Gamma transfer at the tested amplitude.

Reason:
It creates negative `rho_B` in the backward-integrated background and fails early-universe viability checks.

Evidence:
`docs/04_results/010_result_001_gamma_scan.md`, `docs/03_experiments/010_exp_001_gamma_scan.md`, `outputs/qfuds_constant_gamma0.01_beta0.csv`

## 2026-06-08

Decision:
Reject ungated growth-driven Gamma transfer at the tested amplitude.

Reason:
The growth proxy is active during matter domination, so the transfer turns on too early and fails the background viability checks.

Evidence:
`docs/04_results/010_result_001_gamma_scan.md`, `outputs/qfuds_growth_driven_gamma0.01_beta0.csv`

## 2026-06-08

Decision:
Keep low-redshift collapse, black-hole-entropy, and star-formation proxies as candidate shapes for later scrutiny.

Reason:
They pass minimal background checks in the experiment 001 scan and naturally defer transfer until late times. Later Level 1.5 work blocks direct perturbation promotion until phase-transfer physicality is resolved.

Evidence:
`docs/04_results/010_result_001_gamma_scan.md`, `outputs/qfuds_collapsed_fraction_toy_gamma0.03_beta0.csv`, `outputs/qfuds_black_hole_entropy_proxy_gamma0.03_beta0.csv`, `outputs/qfuds_star_formation_proxy_gamma0.003_beta0.csv`

## 2026-06-08

Decision:
Make documentation the primary source of truth for experiment history.

Reason:
Future researchers need the reasoning trail, failed ideas, surviving assumptions, code paths, outputs, and next decisions without relying on chat history.

Evidence:
`docs/00_project/overview.md`, `docs/03_experiments/`, `docs/04_results/`, `docs/05_next_steps/000_roadmap.md`

## 2026-06-08

Decision:
Keep only the collapse/information-production branch from experiment 002.

Reason:
Horizon information is physically clean but reduces to standard horizon/interacting dark energy. HBM/KL gravitational entropy is too broad in time and fails positivity unless the coupling is tiny. Press-Schechter information production is the only tested entropy-derived shape that naturally vanishes in radiation domination, peaks after nonlinear collapse begins, and gives a falsifiable relation between `w(a)` and growth history.

Evidence:
`docs/04_results/020_result_002_entropy_information_gate.md`, `outputs/qfuds_information_production_gamma0.02_beta0.csv`, `outputs/qfuds_horizon_information_gamma0.03_beta0.csv`, `outputs/qfuds_gravitational_entropy_gamma0.003_beta0.csv`

## 2026-06-08

Decision:
Insert Level 1.5, phase transfer physicality, before perturbation closure.

Reason:
The surviving collapse/information-production branch is narrower than a free `Gamma(a)`, but the repository has not derived why collapse or information production should convert phase A into vacuum-pressure phase B. The current `Gamma(a) proportional to dF_coll/dln(a)` law is best classified as a phenomenological coarse-grained interacting-vacuum transfer law with a physically motivated source shape. It also uses LCDM-style growth approximations in the source and does not yet define a physical mass threshold `M`.

Evidence:
`docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md`, `qfuds/gamma_laws.py`, `qfuds/growth.py`, `docs/04_results/020_result_002_entropy_information_gate.md`

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
`docs/04_results/015_result_001_5_phase_transfer_physicality.md`, `docs/04_results/020_result_002_entropy_information_gate.md`, `docs/03_experiments/020_exp_002_entropy_information_gate.md`
