---
doc_id: results_index
title: 04 Results
doc_type: index
stage: "1.5"
status: in_progress
evidence_role: ssot
depends_on:
  - result_003_phenomenological_perturbation_closure
next_gate: retained P1 classified as interacting-vacuum/IDE phenomenology; keep Level 2B blocked
last_updated: 2026-06-09
---

# 04 Results

Results, reports, and hostile-referee conclusions.

Reader-facing summary figures live under `outputs/figures/`. Result documents
embed PNG files for review and retain matching SVG files for scalable reuse.
Regenerate the summary figures with:

```bash
python3 scripts/generate_result_figures.py
```

- [000_experiment_summary.md](000_experiment_summary.md): lightweight summary of experiment outcomes and postmortem coverage.
- [000_result_000_lcdm_baseline.md](000_result_000_lcdm_baseline.md): zero-transfer LCDM baseline result.
- [010_result_001_gamma_scan.md](010_result_001_gamma_scan.md): experiment 001 result interpretation and next target.
- [015_result_001_5_phase_transfer_physicality.md](015_result_001_5_phase_transfer_physicality.md): Level 1.5 hostile result; retained `Gamma(a)` branch failed physical promotion and is demoted to phenomenological interacting vacuum.
- [020_result_002_entropy_information_gate.md](020_result_002_entropy_information_gate.md): experiment 002 provenance scan; collapse/information production later failed Level 1.5 physical promotion.
- [030_result_003_phenomenological_perturbation_closure.md](030_result_003_phenomenological_perturbation_closure.md): Level 2A closure result; P2 fails at retained amplitude, P1 survives only as phenomenological interacting vacuum.
- [030_result_004_p1_model_family_positioning.md](030_result_004_p1_model_family_positioning.md): retained P1 model-family classification; exact interacting-vacuum instance and time-dependent IDE subset.
- [030_result_005_timing_prior_usefulness.md](030_result_005_timing_prior_usefulness.md): timing-prior usefulness audit; retained timing is a potential IV/IDE prior-compression target, not a physical source.
