# QFUDS Project Overview

Date: 2026-06-08

## Project Goals

Quantum Foam Unified Dark Sector (QFUDS) is a speculative research program that asks whether the observed dark sector can be modeled as two effective macroscopic phases of one underlying quantum-spacetime foam sector:

- phase A: a clustering, nearly pressureless component with `w_A ~= 0` and `c_s,A^2 ~= 0`;
- phase B: a smooth vacuum-pressure component with `w_B ~= -1`;
- optional defects/remnants: subdominant black/white-hole-like information-storage candidates, not the main dark-sector explanation.

The scientific goal is not to defend the idea as correct. The goal is to make the idea precise enough to compare with LCDM, unified dark fluids, k-essence, interacting dark energy, scalar-field dark matter, and compact-remnant scenarios.

The working standard is:

```text
Can this version be made precise enough to fail?
```

## Current Status

The project is currently between roadmap Level 1.6 and Level 2.

- Level 0 literature positioning exists in draft form.
- Level 1 background toy model exists.
- v0.3 Gamma-law background diagnostics are complete for a small suite of transfer laws.
- v0.4 entropy/information-source background diagnostics are complete.
- Perturbation equations are incomplete.
- CLASS/CAMB integration has not started.
- CMB and matter-power comparisons have not been performed.

Current implementation anchors:

- `qfuds/background.py`: two-phase background integration.
- `qfuds/gamma_laws.py`: candidate `Gamma(a)` transfer laws.
- `qfuds/growth.py`: scale-independent growth proxy under smooth phase-B assumptions.
- `qfuds/diagnostics.py`: LCDM comparison and minimal viability flags.
- `scripts/run_minimal_model.py`: reproducible CLI runner.
- `outputs/`: generated CSV and PNG files for the baseline, v0.3, and v0.4 diagnostic suites.

## Known Limitations

QFUDS is not yet a complete physical theory.

1. No covariant microscopic foam action has been derived.
2. The phase split is phenomenological.
3. `Gamma(a)` laws in v0.3 are toy prescriptions or empirical proxies.
4. The v0.4 information-production branch is still a background/growth-proxy candidate, not a perturbation result.
5. Background-level viability does not imply CMB viability.
6. The perturbation prescription for coupled phase transfer is not specified.
7. A single adiabatic unified fluid with late `w -> -1` can fail structure formation through an excessive sound speed.
8. Compact black/white-hole remnants are optional and must remain subdominant unless their abundance and mass function are derived.
9. Existing data already strongly constrain deviations from LCDM.

## Roadmap

The immediate research path is:

1. Preserve the version history and experiment decisions in docs.
2. Keep v0.3 and v0.4 as background-only diagnostic results.
3. Write the perturbation equations for phase A, phase B, and transfer perturbations.
4. Implement a Boltzmann-code version only after the perturbation assumptions are explicit.
5. Compare against CMB and matter power before adding new speculative mechanisms.

The maintained roadmap is `docs/05_next_steps/roadmap.md`.

## Model Genealogy

```text
Concept origin
  Landauer/information-cost prompt
  -> black-hole information and Hawking-radiation questions
  -> reverse-channel and white-hole-like remnant speculation
  -> quantum foam as possible medium
  -> dark matter as clustering foam mode
  -> dark energy as residual foam pressure

qfuds_v0_1
  Conceptual unified-foam hypothesis.
  No validated equations. White-hole-universe image pruned out of the core claim.

qfuds_v0_2
  Minimal two-phase effective dark sector in unmodified GR.
  Gamma = 0 reproduces LCDM.
  Free Gamma(a) reduces to interacting dark energy.

qfuds_v0_3
  Background diagnostic scan over physically labeled Gamma(a) laws.
  Constant and ungated growth-driven transfer fail immediately.
  Low-redshift collapse, black-hole-entropy, and star-formation proxies survive
  only as toy targets for perturbation-level tests.

qfuds_v0_4
  Entropy/information-source diagnostic scan.
  Broad entropy language is rejected as a general explanation.
  Collapse/information production is kept only as a background-level target for
  perturbation tests.
```

## Primary Source Documents

Maintained documentation:

- `docs/README.md`
- `docs/00_project/overview.md`
- `docs/00_project/decision_log.md`
- `docs/00_project/verification_guide.md`
- `docs/02_theory/qfuds_v0_1.md`
- `docs/02_theory/qfuds_v0_2.md`
- `docs/02_theory/qfuds_v0_3.md`
- `docs/03_experiments/exp_000_lcdm_baseline.md`
- `docs/03_experiments/exp_001_gamma_scan_v03.md`
- `docs/03_experiments/exp_002_entropy_information_scan_v04.md`
- `docs/04_results/result_000_lcdm_baseline.md`
- `docs/04_results/result_001_gamma_scan_v03.md`
- `docs/04_results/qfuds_v0_4_entropy_laws.md`
- `docs/05_next_steps/roadmap.md`

Historical/source notes retained for provenance:

- `docs/01_origin/concept_origin.md`
- `docs/00_project/research_program.md`
- `docs/02_theory/qfuds_research_report.md`
- `docs/04_results/qfuds_v0_3_gamma_laws.md`
- `docs/00_project/qfuds_ko.md`
