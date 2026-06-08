# Decision Log

This log records research decisions, not only implementation changes.

## 2026-06-08

Decision:
Reject the white-hole-universe image as the central QFUDS claim.

Reason:
It is too broad to test directly and does not provide a controlled cosmological model.

Evidence:
`docs/concept_origin.md`, `docs/research_program.md`, `docs/02_theory/qfuds_v0_1.md`

## 2026-06-08

Decision:
Adopt the two-phase dark-sector formulation as the minimal working model.

Reason:
It makes the LCDM limit, phase-transfer problem, sound-speed constraint, and observational kill criteria explicit.

Evidence:
`docs/qfuds_research_report.md`, `docs/02_theory/qfuds_v0_2.md`, `qfuds/background.py`

## 2026-06-08

Decision:
Treat QFUDS as non-novel until it specifies a derived microphysical action, a fixed transfer law, or a perturbation prescription that survives data.

Reason:
With `Gamma=0`, the model is LCDM. With free `Gamma(a)`, it is a known interacting dark-sector model.

Evidence:
`docs/qfuds_research_report.md`

## 2026-06-08

Decision:
Reject constant Gamma transfer at the tested amplitude.

Reason:
It creates negative `rho_B` in the backward-integrated background and fails early-universe viability checks.

Evidence:
`docs/qfuds_v0_3_gamma_laws.md`, `docs/03_experiments/exp_001_gamma_scan_v03.md`, `outputs/qfuds_constant_gamma0.01_beta0.csv`

## 2026-06-08

Decision:
Reject ungated growth-driven Gamma transfer at the tested amplitude.

Reason:
The growth proxy is active during matter domination, so the transfer turns on too early and fails the background viability checks.

Evidence:
`docs/qfuds_v0_3_gamma_laws.md`, `outputs/qfuds_growth_driven_gamma0.01_beta0.csv`

## 2026-06-08

Decision:
Keep low-redshift collapse, black-hole-entropy, and star-formation proxies as next perturbation-test candidates.

Reason:
They pass minimal background checks in the v0.3 scan and naturally defer transfer until late times.

Evidence:
`docs/qfuds_v0_3_gamma_laws.md`, `docs/04_results/result_001_gamma_scan_v03.md`, `outputs/qfuds_collapsed_fraction_toy_gamma0.03_beta0.csv`, `outputs/qfuds_black_hole_entropy_proxy_gamma0.03_beta0.csv`, `outputs/qfuds_star_formation_proxy_gamma0.003_beta0.csv`

## 2026-06-08

Decision:
Make documentation the primary source of truth for experiment history.

Reason:
Future researchers need the reasoning trail, failed ideas, surviving assumptions, code paths, outputs, and next decisions without relying on chat history.

Evidence:
`docs/00_project_overview.md`, `docs/03_experiments/`, `docs/04_results/`, `docs/05_next_steps/roadmap.md`
