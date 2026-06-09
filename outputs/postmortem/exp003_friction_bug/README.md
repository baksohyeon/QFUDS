---
doc_id: exp003_friction_bug_postmortem
title: "Postmortem: exp_003 Phase-A Euler Friction Bug"
doc_type: reference
stage: "2"
status: provenance
evidence_role: provenance
depends_on:
  - result_003_phenomenological_perturbation_closure
next_gate: none; archival provenance only
last_updated: 2026-06-08
---

# Postmortem: exp_003 Phase-A Euler Friction Bug

Date: 2026-06-08

This directory archives the original (pre-correction) exp_003 Level 2A
perturbation outputs. They are preserved as provenance. They are **not** valid
diagnostics. Use `outputs/exp003_*.csv` (corrected) for any analysis.

## What the bug was

`qfuds/perturbations.py` integrated the dimensionless velocity variable
`theta/Hc` (the continuity equation uses `d delta/dx = -theta/Hc`). For that
variable the conformal-Newtonian Euler friction is:

```text
phase A (CDM):       d(theta/Hc)/dx = -(1 + dlnHc/dx)(theta/Hc) + kappa^2 Phi
phase B (fluid):     d(theta/Hc)/dx = -[(1 - 3 cs_B^2) + dlnHc/dx](theta/Hc) + ...
```

The code computed `dln_hc_dx = 1 + dlnH/dlna` (the conformal log-derivative,
already containing the `+1` from `Hc = a H`) and then used base constant `2.0`:

```text
buggy phase A:  -(2.0 + dln_hc_dx) theta
buggy phase B:  -(2.0 + dln_hc_dx - 3 cs_B^2) theta
```

That is one extra unit of Hubble friction in **both** Euler equations.

## Root cause

Double counting of the `+1` conformal term. The author appears to have written
the friction as "`2 + conformal-derivative`" (mixing the physical-H growth form
`2 + dlnH/dlna` with the conformal derivative `dln_hc_dx = 1 + dlnH/dlna`),
which sums to `3 + dlnH/dlna` instead of the correct `2 + dlnH/dlna`.

The repository's own validated growth equation `qfuds/growth.py` uses the correct
friction `2 + dlnH/dlna` and was the reference that exposed the inconsistency.
The buggy Euler equation was also internally inconsistent with its own
continuity equation, which already assumed `theta/Hc`.

## Affected diagnostics

- `delta_A`, `theta_A`, `delta_B`, `theta_B`, `Phi`, `Q`, `deltaQ`,
  `curvature_proxy` in every `exp003_*_*.csv`.
- `max_abs_perturbation` and `max_abs_curvature_proxy` in
  `exp003_stability_diagnostics.csv`.
- The qualitative clustering statement in
  [docs/04_results/030_result_003_phenomenological_perturbation_closure.md](../../../docs/04_results/030_result_003_phenomenological_perturbation_closure.md).

Not affected: `conservation_residual` (identically zero, the transfer is
antisymmetric by construction); the gauge/transfer metadata.

## Impact on conclusions

| Quantity | Buggy | Corrected | Conclusion impact |
| --- | --- | --- | --- |
| phase-A matter-era slope `dln delta_A / dln a` (k=0.1) | ~0.60 | ~0.90 | The buggy run **under-clustered** phase A by a large margin; the corrected run approximately matches `growth.py` (~0.97). |
| P1 stability classification | stable | stable | **unchanged** |
| P2 stability classification (R1 0.02, R3 0.04) | unstable (all k) | unstable (all k) | **unchanged** |
| P1 `max_abs_perturbation` | ~8.3e-4 | ~8.3e-3 | magnitude changed ~10x (correct growth) |

The survive/fail verdict did not change. The bug corrupted the clustering
diagnostic and the instability magnitudes, not the classification. In
particular, the original result document's statement that phase-A clustering
loss was "not triggered for P1" was unjustified under the buggy code (clustering
was degraded), and is only justified after the correction.

## Fix

`qfuds/perturbations.py`: base friction constant `2.0 -> 1.0` in both Euler
equations. See the inline comments at the `d_ta` and `d_tb` definitions.
