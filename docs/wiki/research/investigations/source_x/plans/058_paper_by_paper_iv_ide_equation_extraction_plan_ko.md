---
doc_id: plan_2026_06_18_paper_by_paper_iv_ide_equation_extraction_ko
title: "2026-06-18 Paper-by-Paper IV/IDE Equation Extraction Plan"
doc_type: guide
stage: reference
status: completed
evidence_role: audit
depends_on:
  - audit_2026_06_18_iv_ide_formalism_notes_ledger_ko
  - audit_2026_06_18_iv_ide_formalism_study_map_ko
  - audit_2026_06_18_academic_derivation_bridge_ko
  - result_006_literature_timing_support_audit
  - baseline_reference_nasa_bao_constraint_map
  - roadmap
next_gate: execute exact equation extraction before any timing fit or observational kill-map use
last_updated: 2026-06-18
---

# 2026-06-18 Paper-by-Paper IV/IDE Equation Extraction Plan

## Purpose

이 문서는 [057 IV/IDE Formalism Notes Ledger](../conclusions/057_iv_ide_formalism_notes_ledger_ko.md)
다음 실행 계획이다.

목적은 retained `Gamma(a)`를 다시 fitting하는 것이 아니다. 목적은 실제
IV/IDE 논문들이 어떤 순서로 다음 객체들을 정의하는지 paper-by-paper로
뽑는 것이다.

```text
Q
Q^mu
transfer frame
delta Q
coupling perturbation
stability prescription
solver/product readiness
```

이 extraction이 끝나기 전에는 NASA/LAMBDA, BAO, CMB, LSS, DESI/Euclid,
CLASS/CAMB, likelihood 비교로 가지 않는다.

## Workflow Boundary

This plan follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md)
as a source-state boundary.

No new external source, PDF, page family, cache, digitization, posterior product,
or product-absence claim is introduced here. This plan only schedules exact
equation extraction from repo-owned literature records and the source states
already recorded there.

Inherited states and tokens that must be preserved during execution:

```text
literature_record_cached
asset_available_not_downloaded
asset_cached
asset_extracted_not_digitized
manual_structured_extract
direct_table
numeric_digitized
inspected_no_numerical_product
data_product_blocked
```

If an extraction step needs a paper/source that is currently only
`literature_record_cached` or `asset_available_not_downloaded`, the next task
must cache the PDF/source first. Do not infer missing equations from a summary
record.

## Hard Boundary

The local retained convention is only the comparison anchor:

```math
\rho_A' + 3\mathcal{H}\rho_A = -Q,
\qquad
\rho_B' + 3\mathcal{H}(1+w_B)\rho_B = +Q,
```

```math
Q = \mathcal{H}\Gamma(a)\rho_A.
```

Positive `Q` in this repo convention means phase A/CDM-like density loses
energy and phase B/vacuum-like density gains energy.

This cannot be compared to `beta(z)`, `Pi_DE(z)`, `q_V(z)`, `alpha(a)`, or
`xi(a)` by symbol shape alone.

Required translations:

```text
time variable
Hubble normalization
sign convention
density factor
dimension of coupling variable
redshift/scale-factor/bin convention
```

## Extraction Schema

Each paper row must fill this schema. Unknown values must stay
`extraction_needed`; do not guess.

```yaml
paper_id:
record_path:
source_state:
equation_status: exact_in_cached_record | partial_in_cached_record | extraction_needed
model_class: interacting_vacuum | IDE_fluid | scalar_field_CDE | dark_scattering | running_vacuum | adjacent_only
background_Q:
time_derivative_variable: conformal_time | cosmic_time | ln_a | redshift | scale_factor | extraction_needed
hubble_factor_in_Q: H | Hc/mathcalH | H0 | none/kernel | extraction_needed
sign_convention_raw:
positive_coupling_direction:
density_factor: rho_c | rho_de | rho_A | rho_V | total_dark | kernel | other | extraction_needed
coupling_variable:
coupling_dimension: dimensionless | dimensionful | extraction_needed
time_dependence: a | z | bins | GP_nodes | constant | parametric_transition | extraction_needed
Q_mu_defined: yes | no | extraction_needed
Q_mu_direction: parallel_to_DM_u | parallel_to_DE_u | parallel_to_total_u | source_derived_vector | pure_momentum_exchange | not_defined | extraction_needed
momentum_transfer_frame: DM_frame | DE_frame | total_frame | scalar_field_frame | dark_scattering_frame | not_stated | extraction_needed
gauge:
delta_Q:
delta_coupling:
pressure_perturbation:
sound_speed:
anisotropic_stress:
initial_conditions:
stability_rule:
PPF_or_ePPF_rule:
solver_route:
posterior_covariance_PCA_products:
retained_Gamma_mapping:
translation_hazards:
stop_status: continue_to_perturbation_extract | background_only_stop | frame_only_stop | adjacent_comparator_stop | cache_first_stop
```

## Stop Status Rules

| Stop status | Meaning | Allowed next action |
| --- | --- | --- |
| `continue_to_perturbation_extract` | Paper/source gives background `Q`, `Q^mu`/frame, and a perturbation or stability route. | Extract equations into a structured record. |
| `background_only_stop` | Paper gives continuity-level `Q` or scalar coupling variable only. | Do not infer frame or perturbations; cache/source-extract first if useful. |
| `frame_only_stop` | `Q^mu` or frame is stated, but perturbation/stability equations are absent. | Stop before solver or CMB/LSS comparison. |
| `adjacent_comparator_stop` | Paper is scalar-field CDE, dark scattering, running vacuum, backreaction, or indirect `w(z)` rather than direct IV/IDE energy-transfer history. | Use only for known-model-sink comparison. |
| `cache_first_stop` | Repo has a literature summary but no cached source/PDF sufficient for exact equations. | Apply Research Asset and Product Workflow before extracting. |

## Priority Set

### Tier 1: Direct Extraction Targets

| Order | Paper key | Model family | Current variable | Current state | 058 decision |
| ---: | --- | --- | --- | --- | --- |
| 1 | `lit_li_2025_desi_dr2_sign_reversal_ide` | DESI-era nonparametric IV/IDE | `beta(a)`, `beta(z)` | `asset_cached`; source TeX extracted; no machine-readable `beta(z)`, covariance, chains, or PCA arrays found | Start here. Exact equation extraction is locally possible. |
| 2 | `lit_escamilla_2023_interacting_dark_energy_kernel` | IV/IDE kernel reconstruction | `Pi_DE(z)`, `Pi_DM=-Pi_DE`, `I_Q(z)` | `literature_record_cached`; raw assets treated as `asset_available_not_downloaded` for this route | Cache/source first, then extract exact convention. |
| 3 | `lit_martinelli_2019_interacting_vacuum_geodesic_cdm` | interacting vacuum / geodesic CDM | `q_V(z)` | `literature_record_cached`; exact `Q^mu` not in summary record | Cache/source first, then extract `Q^mu`, frame, perturbations. |
| 4 | `lit_hogg_2020_vacuum_geodesic_cdm_interaction` | interacting vacuum / geodesic CDM | `q_V(z)` / coupling function | `literature_record_cached`; request-available data noted | Cache/source first; use after Martinelli for same-family comparison. |
| 5 | `lit_wang_2015_dark_sector_interaction_reconstruction` | dark matter-vacuum interaction reconstruction | `alpha(a)` | `literature_record_cached`; exact equations absent from summary record | Cache/source first; use for historical convention mapping. |

### Tier 2: Modern Comparator Targets

| Order | Paper key | Model family | Current variable | 058 decision |
| ---: | --- | --- | --- | --- |
| 6 | `lit_silva_2025_desi_dr2_ide_s_ide` | DESI DR2 IDE / sign-switching IDE | coupling parameter / S-IDE parameters | Extract exact parameterized IDE equations after Tier 1. |
| 7 | `lit_yang_2025_variable_couplings_desi_dr2` | DESI DR2 variable-coupling IDE | `xi(a)` | Extract after source cache; useful density-factor comparator. |
| 8 | `lit_paliathanasis_2026_late_time_interacting_transition` | thresholded late-time interacting dark sector | activated interaction term | Extract only as activation-form comparator. |
| 9 | `lit_figueruelo_2026_desi_dr2_linear_nonlinear_ide` | linear/nonlinear DESI DR2 IDE | model-specific coupling parameters | Lower-priority taxonomy target; stop if background-only. |

### Tier 3: Historical/Adjacent Targets

| Paper key | Model family | Decision |
| --- | --- | --- |
| `lit_bonilla_2022_dark_sector_interaction_gp` | GP IV/IDE reconstruction | Extract exact normalization for `delta(z)` / `q=Q/H0^3`; no curve use without digitization. |
| `lit_goh_2023_tomographic_coupled_dark_energy` | scalar-field CDE | Secondary comparator only; do not map `beta(z)` as vacuum transfer. |
| `lit_yang_2015_gp_dark_sector_interaction` | historical GP dark-sector interaction | Optional historical convention target. |
| `lit_mukherjee_2021_nonparametric_dark_sector_interaction` | nonparametric dark-sector interaction | Optional cautionary comparator. |
| `lit_abedin_2025_gp_ann_dark_sector_interaction` | GP/ANN dark-sector interaction | Optional modern nonparametric comparator. |
| `lit_tsedrik_2025_boss_des_y3_dark_scattering` | dark scattering / momentum exchange | Adjacent comparator only; not an energy-transfer timing target. |
| `lit_silva_2024_nonlinear_matter_power_ide` | nonlinear growth IDE | Appendix only unless solver/growth route is opened later. |
| `lit_you_2025_desi_dr2_coupled_dark_sector` | indirect coupled dark sector | Adjacent only unless direct transfer equations are extracted. |

## Li 2025 Pilot Row

Li 2025 is the only Tier 1 paper whose source text is already local enough for
an immediate pilot extraction.

Known local fields:

| Field | Current value |
| --- | --- |
| `source_state` | `asset_cached`; source TeX extracted |
| `equation_status` | `exact_in_cached_record` for background and transfer-vector setup |
| `background_Q` | `Q = beta(a) H rho_de` |
| `time_derivative_variable` | conformal time in density equations; `H` in `Q` definition |
| `density_factor` | `rho_de`, not `rho_A` or `rho_c` |
| `coupling_variable` | `beta(a)` / `beta(z)` |
| `coupling_dimension` | dimensionless |
| `Q_mu_defined` | yes |
| `Q_mu_direction` | DM-frame in the checked source text |
| `momentum_transfer_frame` | DM-frame; momentum transfer vanishes in the CDM rest frame |
| `stability_route` | ePPF route must be extracted before any solver claim |
| `retained_Gamma_mapping` | comparator only; not direct equivalence |
| `translation_hazards` | signed sign-reversal history, `rho_de` density factor, and DESI-era data-driven reconstruction |

Pilot stop rule:

```text
Even for Li 2025, do not compare beta(z) to Gamma(a) until the exact sign,
density-factor, Q_mu/frame, perturbation, and ePPF equations are extracted into
a structured record.
```

## Execution Order

1. Create a structured extraction template from the schema above.
2. Execute Li 2025 pilot extraction from the cached source TeX.
3. Cache/source-extract Escamilla 2023 before exact equation claims.
4. Cache/source-extract Martinelli 2019, then Hogg 2020.
5. Cache/source-extract Wang 2015.
6. Only after Tier 1, decide whether Tier 2 DESI-era parameterized papers are
   needed.
7. Keep Tier 3 as known-model-sink / adjacent-formalism comparison unless a
   later checkpoint opens a solver/growth appendix.

## Failure Conditions

The extraction checkpoint fails if any of the following happens:

- `Gamma(a)` is fit or retuned.
- A paper symbol is compared to `Gamma(a)` without sign, density, and Hubble
  convention translation.
- NASA/LAMBDA, BAO, CMB, LSS, DESI/Euclid, or likelihood constraints are used to
  choose a transition scale, amplitude, width, or source timing.
- A scalar background `Q` is treated as a perturbation prescription.
- A frame choice is copied into QFUDS as source physics.
- PPF/ePPF stabilization is treated as novelty rather than a phenomenological
  stability prescription.
- Table/figure overlap is treated as posterior-level support.
- A `literature_record_cached` summary is treated as exact equation evidence
  without the source/PDF being cached and inspected.

## Output Of The Next Checkpoint

The next checkpoint should not be a result claim. It should produce a structured
extraction record, beginning with Li 2025:

```text
059_li_2025_iv_ide_equation_extraction_result_ko.md
```

Allowed output:

- exact equation snippets or short paraphrases with source locations;
- structured field values from the schema;
- `continue_to_perturbation_extract`, `background_only_stop`,
  `frame_only_stop`, `adjacent_comparator_stop`, or `cache_first_stop`;
- cache/product-state updates if a missing source has to be retrieved.

Forbidden output:

- QFUDS support language;
- Level 2B admission language;
- physical source derivation language;
- NASA/BAO/CMB/LSS observational pass/fail language;
- retained timing as an informative IV/IDE prior.
