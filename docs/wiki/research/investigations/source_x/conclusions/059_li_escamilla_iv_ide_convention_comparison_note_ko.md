---
doc_id: audit_2026_06_18_li_escamilla_iv_ide_convention_comparison_note_ko
title: "2026-06-18 Li/Escamilla IV/IDE Convention Comparison Note"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - audit_2026_06_18_li_2025_iv_ide_equation_extraction_result_ko
  - audit_2026_06_18_escamilla_2023_iv_ide_kernel_equation_extraction_result_ko
  - asset_li_2025_desi_dr2_sign_reversal_ide_equation_extract_20260618
  - asset_escamilla_2023_interacting_dark_energy_kernel_equation_extract_20260618
  - roadmap
next_gate: choose the next IV/IDE formalism target only after preserving the comparator-only boundary
last_updated: 2026-06-18
---

# 2026-06-18 Li/Escamilla IV/IDE Convention Comparison Note

## Purpose

이 문서는 Source-X 059의 Li 2025 extraction과 Escamilla 2023 extraction을
나란히 비교한다.

목적은 retained `Gamma(a)`를 fitting하는 것이 아니다. 목적은 실제 IV/IDE
문헌이 `Q`, 부호, density factor, 시간 변수, `Q^mu`/frame, perturbation
route를 서로 다르게 정의한다는 점을 고정하고, QFUDS 쪽에서 어떤 항목이
비어 있는지 확인하는 것이다.

## Workflow Boundary

This note follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).

No new external source, PDF, posterior product, covariance product, chain,
numerical curve, or product-absence claim is introduced here. This is a
repo-internal comparison of two already cached and manually extracted records:

```text
docs/wiki/research/assets/li_2025_desi_dr2_sign_reversal_ide/digitization/equation_extraction_20260618.md
docs/wiki/research/assets/escamilla_2023_interacting_dark_energy_kernel/digitization/equation_extraction_20260618.md
```

Workflow states inherited by this comparison:

```text
asset_cached
asset_extracted_not_digitized
source_text_parse
manual_structured_extract
```

This is not numerical digitization and not QFUDS evidence.

## Convention Matrix

| Field | Li 2025 | Escamilla 2023 | QFUDS bridge implication |
| --- | --- | --- | --- |
| `model_class` | interacting vacuum / IDE | interacting DE-DM background kernel | both are formalism comparators only |
| `background_Q` | `Q = beta(a) H rho_de` | `dot rho_DM + 3H rho_DM = Q`; `dot rho_DE + 3H rho_DE(1+w_DE) = -Q` | no direct retained `Gamma(a)` equality |
| `sign_direction` | source result records positive early `beta(z)` as CDM-to-DE | `Q>0` is DE-to-DM; `Q<0` is DM-to-DE | sign must be translated before any shape comparison |
| `density_factor` | `rho_de` | `rho_c,0` through `Pi_DE = Q/(3H rho_c,0)` | density normalization differs from retained `rho_A` |
| `Hubble_factor` | physical `H` in `Q`; conformal time in density equations | physical `H` in cosmic-time and redshift-normalized equations | `H` vs `mathcal H` cannot be skipped |
| `time_variable` | scale-factor/redshift binned `beta(a)` history | redshift binned/GP `Pi_DE(z)` nodes | node/bin choices are reconstruction choices |
| `Q_mu_frame` | yes; transfer parallel to DM four-velocity | no covariant `Q^mu` extracted | Escamilla cannot carry perturbation closure |
| `momentum_transfer_frame` | DM frame | not defined | QFUDS has no frame prescription yet |
| `perturbation_route` | ePPF route recorded | full perturbation analysis deferred | retained `Gamma(a)` remains background comparator |
| `solver_route` | IDECAMB/CAMB plus Cobaya/PolyChord | SimpleMC plus dynesty for background expansion/distance inference | different readiness levels |
| `product_status` | no machine-readable `beta(z)`/posterior/covariance/PCA product in cached asset | no curve-level numeric product created by this extraction | no timing fit should be run from these notes |
| `stop_status` | `continue_to_perturbation_extract` | `background_only_stop` | compare conventions first; do not merge them |

## Minimal Translation Rules

Before retained `Gamma(a)` can be compared to either paper, the following
must be fixed explicitly:

1. sign convention;
2. density factor;
3. physical `H` versus conformal `mathcal H`;
4. redshift versus scale-factor binning;
5. whether the comparison is background-only or perturbation-ready;
6. whether a numerical product exists or only a source-text equation exists.

If any of these are left implicit, the comparison is not an IV/IDE bridge. It
is just curve-shape matching.

## Stop Rule

Do not run NASA/BAO/CMB/LSS model interpretation from this note.

Do not choose a retained `Gamma(a)` width, amplitude, transition redshift, or
foam scale after looking at the Li/Escamilla reconstruction choices.

Do not treat Escamilla's redshift-bin smoothing `xi = 0.15` as a QFUDS
physical scale. It is an interpolation parameter in that paper's reconstruction
setup.

## Decision

| Question | Decision |
| --- | --- |
| Are Li 2025 and Escamilla 2023 directly interchangeable? | No. |
| Which one reaches perturbation/formalism machinery? | Li 2025, through `Q^mu`/frame/ePPF. |
| Which one is the cleaner background-kernel teaching target? | Escamilla 2023. |
| Does either create a physical QFUDS source? | No. |
| Does retained `Gamma(a)` still have value? | Yes, as a phenomenological timing/background comparator only. |
| What is the next safe step? | Choose the next IV/IDE formalism target, then repeat source cache plus exact equation extraction before any interpretation. |

## Next Executable Instruction

Select the next IV/IDE formalism target from the 058 plan, then apply the same
sequence used here: cache/source-state record first, exact equation extraction
second, convention comparison third. Keep retained `Gamma(a)` in observer-mode
comparator language and do not use observational baseline constraints as model
evidence.
