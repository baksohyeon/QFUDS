---
doc_id: audit_2026_06_18_li_2025_iv_ide_equation_extraction_result_ko
title: "2026-06-18 Li 2025 IV/IDE Equation Extraction Result"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - plan_2026_06_18_paper_by_paper_iv_ide_equation_extraction_ko
  - audit_2026_06_18_iv_ide_formalism_notes_ledger_ko
  - asset_li_2025_desi_dr2_sign_reversal_ide
  - asset_li_2025_desi_dr2_sign_reversal_ide_equation_extract_20260618
  - lit_li_2025_desi_dr2_sign_reversal_ide
  - roadmap
next_gate: cache/source-extract Escamilla 2023 before comparing IDE kernel conventions
last_updated: 2026-06-18
---

# 2026-06-18 Li 2025 IV/IDE Equation Extraction Result

## Purpose

이 문서는 [058 paper-by-paper IV/IDE extraction plan](../plans/058_paper_by_paper_iv_ide_equation_extraction_plan_ko.md)의
첫 실행 결과다.

대상은 Li and Zhang 2025 DESI DR2 sign-reversal IDE paper다. 목적은
retained `Gamma(a)`를 맞추는 것이 아니라, 실제 IV/IDE 논문이 배경 source
term, covariant transfer, frame, perturbation/stability route를 어떻게
정의하는지 구조화하는 것이다.

## Workflow Boundary

This result follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).

No new external source, PDF, page family, posterior product, covariance product,
PCA array, chain, numerical `beta(z)` product, or product-absence claim is
introduced here. The extraction uses the already cached Li 2025 arXiv source:

```text
docs/wiki/research/assets/li_2025_desi_dr2_sign_reversal_ide/source/extracted/idenpr.tex
```

A manual structured extract was added at:

```text
docs/wiki/research/assets/li_2025_desi_dr2_sign_reversal_ide/digitization/equation_extraction_20260618.md
```

Workflow states:

```text
asset_cached
asset_extracted_not_digitized
source_text_parse
manual_structured_extract
```

This is not numerical digitization and not QFUDS evidence.

## Short Result

Li 2025 passes the 058 extraction gate as:

```text
stop_status = continue_to_perturbation_extract
```

Reason: the cached source gives a background `Q`, an energy-momentum transfer
vector/frame choice, and an ePPF perturbation/stability route.

It does not provide:

```text
QFUDS physical source X
QFUDS-derived Q^mu[X, ...]
phase-B pressure derivation
source-side delta Q for QFUDS
machine-readable beta(z) history
posterior chains
covariance/PCA arrays
```

## Structured Extraction Row

| Field | Extracted value |
| --- | --- |
| `paper_id` | `lit_li_2025_desi_dr2_sign_reversal_ide` |
| `record_path` | [Li 2025 literature record](../../../literature/li_2025_desi_dr2_sign_reversal_ide.md) |
| `source_state` | `asset_cached`; source TeX extracted; `manual_structured_extract` added |
| `equation_status` | `exact_in_cached_record` for background equation, `Q`, frame, and ePPF mapping |
| `model_class` | `interacting_vacuum` / DESI-era IDE |
| `background_Q` | `Q = beta(a) H rho_de` |
| `time_derivative_variable` | conformal time in density equations; `H` in `Q` |
| `hubble_factor_in_Q` | `H` |
| `sign_convention_raw` | DE gains `+aQ`; CDM loses `-aQ` in the background equations |
| `positive_coupling_direction` | positive early-time `beta(z)` is interpreted by the source as CDM-to-DE transfer |
| `density_factor` | `rho_de`, not `rho_A` |
| `coupling_variable` | `beta(a)` / `beta(z)` |
| `coupling_dimension` | dimensionless |
| `time_dependence` | piecewise constant bins in scale factor; discussed as redshift history |
| `Q_mu_defined` | yes |
| `Q_mu_direction` | parallel to CDM/dark-matter four-velocity |
| `momentum_transfer_frame` | DM frame; momentum transfer rate vanishes in the dark-matter rest frame |
| `gauge` | not extracted as a standalone gauge declaration in this pass |
| `delta_Q` | not explicitly extracted as an independent formula in this pass |
| `delta_coupling` | not explicitly extracted as an independent formula in this pass |
| `pressure_perturbation` | handled through ePPF route rather than a QFUDS pressure derivation |
| `sound_speed` | not extracted as a standalone field in this pass |
| `anisotropic_stress` | not extracted as a standalone field in this pass |
| `initial_conditions` | `beta(a)=0` before `a_1=0.0001` for the coupling history |
| `stability_rule` | ePPF is used to avoid possible large-scale instability in standard linear perturbation theory |
| `PPF_or_ePPF_rule` | for the `beta(a)` model, `C_1=D_2=Q` and `C_2=C_3=D_1=0` |
| `solver_route` | IDECAMB implementation in CAMB; Cobaya/PolyChord sampling |
| `posterior_covariance_PCA_products` | paper reports figures/tables/PCA summaries, but no machine-readable posterior chains, covariance/PCA arrays, or numerical `beta(z)` product are present in the cached asset |
| `retained_Gamma_mapping` | comparator only; no direct equivalence |
| `translation_hazards` | `rho_de` density factor, signed sign-reversal coupling, DESI-era reconstruction, ePPF stabilization |
| `stop_status` | `continue_to_perturbation_extract` |

## Translation Boundary

The repo-local retained convention is:

```math
Q = \mathcal{H}\Gamma(a)\rho_A.
```

Li 2025 uses:

```math
Q = \beta(a)H\rho_{de}.
```

Therefore the paper cannot be mapped to retained `Gamma(a)` by comparing curve
shape alone. A valid translation would first need:

```text
rho_de vs rho_A density conversion
H vs Hc convention conversion
sign convention mapping
redshift/scale-factor bin mapping
uncertainty-aware beta(z) product
```

The source also reconstructs a signed history: positive at earlier times and
negative at later times. Retained `Gamma(a)` is not a signed sign-reversal
model.

## What This Teaches

This is exactly where the QFUDS brute-force intuition stopped.

The paper starts with a background interaction history, but it does not stop
there. It specifies an energy-momentum transfer vector, a momentum-transfer
frame, a perturbation/stability prescription, and a solver route.

Retained `Gamma(a)` currently fills only the background comparator slot. It does
not fill the physical source, perturbation, or solver-readiness slots.

## Decision

| Question | Decision |
| --- | --- |
| Can Li 2025 be used as an IV/IDE formalism teaching target? | Yes. |
| Can Li 2025 `beta(z)` be treated as direct support for retained `Gamma(a)`? | No. |
| Can retained `Gamma(a)` be translated directly into Li `beta(a)`? | No; density, sign, and Hubble conventions differ. |
| Does this open QFUDS Level 2B? | No. |
| Does this allow NASA/BAO/CMB/LSS model comparison now? | No. |
| What is the next safe step? | Cache/source-extract Escamilla 2023, then compare its `Pi_DE` convention against this Li 2025 extraction. |

## Next Executable Instruction

Create the next equation extraction task for Escamilla 2023. First apply the
Research Asset and Product Workflow because the current Source-X route treats
the Escamilla raw assets as `asset_available_not_downloaded`. Cache the
PDF/source, then extract only the exact background kernel convention, sign
mapping, density factor, `Q^mu`/frame if present, perturbation route if present,
and product-state boundary. Do not use the extracted convention to fit
`Gamma(a)`.
