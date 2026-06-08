# QFUDS Project Overview

Date: 2026-06-08

This is the project-level overview entry point requested by the documentation plan.

The maintained detailed overview is `docs/00_project/overview.md`. This file keeps the top-level status in one place and points to the canonical supporting documents.

## Project Goals

QFUDS asks whether dark matter and dark energy can be modeled as two effective macroscopic phases of one underlying quantum-spacetime foam sector.

The goal is not to prove QFUDS correct. The goal is to determine whether each version survives progressively stronger tests or must be rejected, narrowed, or classified as a known model.

## Current Status

```text
Level 0: literature position                    completed
Level 1: background toy model                   completed
Level 2: perturbation equations                 in progress
Level 3: CLASS/CAMB integration                 blocked
Level 4: CMB comparison                         blocked
Level 5: matter power comparison                blocked
Level 6: DESI/Euclid/Roman constraints          blocked
```

The project is currently stopped at Level 2. Perturbation equations are not complete.

Level 1 contains three completed background validations:

```text
exp_000: zero-transfer LCDM baseline
exp_001: Gamma-law background scan
exp_002: entropy / information-source gate
```

## Known Limitations

- No microphysical foam action has been derived.
- The phase split remains phenomenological.
- The surviving transfer laws have passed only background-level checks.
- No transfer perturbation model exists.
- No CLASS/CAMB implementation exists.
- No CMB, matter-power, or survey-likelihood comparison exists.
- Background-level growth proxies are not matter-power predictions.

## Roadmap

The maintained roadmap is `docs/05_next_steps/roadmap.md`.

The required order is:

```text
literature position
-> background toy model
-> background transfer-law filters
-> perturbation equations
-> CLASS/CAMB integration
-> CMB comparison
-> matter power comparison
-> survey constraints
```

## Model Genealogy

```text
v0.1
  Conceptual unified-foam hypothesis.
  White-hole-universe image rejected as the central testable claim.

v0.2
  Minimal two-phase effective dark sector.
  Gamma = 0 gives the LCDM limit.
  Free Gamma(a) reduces to interacting dark energy.

qfuds_v0_3 / exp_001
  Background Gamma-law scan.
  Constant and ungated growth-driven transfer fail.
  Low-redshift proxies survive only as perturbation-test candidates.

exp_002
  Entropy/information-source background gate.
  Broad entropy language mostly fails or reduces to known model classes.
  Press-Schechter information production is kept as the narrow perturbation target.

Level 2 next
  Perturbation equations for phase A, phase B, and transfer perturbations.
```

## Primary Documents

- `PROJECT.md`: documentation control and validation order.
- `AGENTS.md`: agent constitution and research rules.
- `docs/00_project/overview.md`: detailed project overview.
- `docs/00_project/decision_log.md`: chronological decisions.
- `docs/00_project/verification_guide.md`: how to rerun and read current checks.
- `docs/05_next_steps/roadmap.md`: current levels and blockers.
