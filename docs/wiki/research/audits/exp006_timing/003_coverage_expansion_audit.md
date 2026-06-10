---
doc_id: audit_2026_06_09_exp006_coverage_expansion
title: "2026-06-09 Exp006 Coverage Expansion Audit"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_09_exp006_sharpening_path
  - literature_cache_index
next_gate: none; coverage-expansion audit only
last_updated: 2026-06-09
record_type: availability_audit
audit_date: 2026-06-09
used_by:
  - exp_006_coverage_expansion
---

# 2026-06-09 Exp006 Coverage Expansion Audit

## Audit Objective

Assess whether the literature coverage behind Exp006 is representative enough
to judge retained structure-era timing fairly.

This is a coverage audit only. It does not run Exp006, change Exp006
conclusions, modify roadmap status, or introduce new physical hypotheses.

## Baseline Coverage

| Literature family | Status | Current cache records | Coverage note |
| --- | --- | --- | --- |
| Escamilla-style model-independent IV/IDE kernel reconstruction | already covered | [Escamilla 2023 Interacting Dark Energy Kernel](../../literature/escamilla_2023_interacting_dark_energy_kernel.md) | primary table-level product, but no public posterior histories found |
| Scalar-field tomographic CDE proxy | already covered | [Goh 2023 Tomographic Coupled Dark Energy](../../literature/goh_2023_tomographic_coupled_dark_energy.md) | secondary proxy only |
| GP dark-sector interaction reconstruction | partially covered | [Bonilla 2022 Dark Sector Interaction GP](../../literature/bonilla_2022_dark_sector_interaction_gp.md), [You 2025 DESI DR2 Coupled Dark Sector](../../literature/you_2025_desi_dr2_coupled_dark_sector.md) | figure-level or indirect coupling products |
| Vacuum-geodesic CDM binned reconstruction | already covered | [Martinelli 2019 Interacting Vacuum Geodesic CDM](../../literature/martinelli_2019_interacting_vacuum_geodesic_cdm.md), [Hogg 2020 Vacuum Geodesic CDM Interaction](../../literature/hogg_2020_vacuum_geodesic_cdm_interaction.md) | historical/pre-DESI |
| Nonparametric dark matter-vacuum reconstruction | already covered | [Wang 2015 Dark Matter Vacuum Interaction](../../literature/wang_2015_dark_sector_interaction_reconstruction.md) | historical |
| DESI-era nonparametric sign-reversal IV/IDE | high-priority missing coverage | [Li 2025 DESI DR2 Sign-Reversal IDE](../../literature/li_2025_desi_dr2_sign_reversal_ide.md) | strongest new timing target |
| DESI-era sign-switching IDE and parameterized IDE | high-priority missing coverage | [Silva 2025 DESI DR2 IDE and S-IDE](../../literature/silva_2025_desi_dr2_ide_s_ide.md), [Figueruelo 2026 DESI DR2 Linear Nonlinear IDE](../../literature/figueruelo_2026_desi_dr2_linear_nonlinear_ide.md) | tests sign-switching/timing families but not free histories |
| Weak-lensing, RSD, and full-shape growth-sensitive IDE | high-priority missing coverage | [Tsedrik 2025 BOSS DES Y3 Dark Scattering](../../literature/tsedrik_2025_boss_des_y3_dark_scattering.md) | growth-sensitive, not direct energy-transfer timing |
| Euclid-era non-linear growth and forecast IDE | partially covered | [Silva 2024 Nonlinear Matter Power IDE](../../literature/silva_2024_nonlinear_matter_power_ide.md) | forecast/growth consequences, not present-data timing support |
| PCA/Bayesian timing reconstruction | partially covered | [Li 2025 DESI DR2 Sign-Reversal IDE](../../literature/li_2025_desi_dr2_sign_reversal_ide.md) | PCA appears in one high-priority DESI-era target |

## Newly Identified Targets

| Paper or family | Coupling variable | Timing information | Product availability | Relevance to retained timing | Could sharpen Exp006 |
| --- | --- | --- | --- | --- | --- |
| Li and Zhang 2025 DESI DR2 sign-reversal IDE | `beta(z)` in vacuum-energy IDE | 20 redshift bins, sign reversal, PCA modes, high-z deviation reported | tables, figures, PCA summaries; no public posterior products found | high | yes, strongest new target |
| Silva et al. 2025 DESI DR2 IDE/S-IDE | coupling parameter in IDE and `S-IDE` | sign-switching model timing and DESI DR2 BAO redshift span | tables, figures, public CLASS_IDE code surfaced | high for sign-switch coverage | yes, mainly for redundancy/disfavor tests |
| You et al. 2025 DESI DR2 coupled dark sector | potential coupling inferred from reconstructed EoS | low-redshift GP/EoS timing around `z ~ 0.4` | figures and paper summaries; no public posterior products found | medium-low for structure-era timing | limited |
| Tsedrik et al. 2025 BOSS/DES Y3 dark scattering | Dark Scattering parameters | growth-sensitive constraints from DES Y3 and BOSS DR12 full shape | tables, figures, public BOSS likelihood data link | medium for growth consequences | limited, not direct timing |
| Figueruelo et al. 2026 DESI DR2 linear/nonlinear IDE | model-specific coupling parameters | sign-switching and late-time background behavior across eight IDE models | tables and figures; no public posterior products found | medium | moderate for family coverage |
| Silva et al. 2024 non-linear matter-power IDE | `xi` | growth-factor, non-linear `P(k)`, Euclid forecast sensitivity | open article tables/figures; no posterior products found | medium for structure-era consequences | limited for Exp006 classification |

## Coverage Risk

Yes: Exp006 could remain `allowed_but_not_informative` because the search space
was too narrow.

The original Exp006 coverage was centered on Escamilla 2023, with Goh as a
secondary scalar-field proxy and Bonilla/Hogg/Martinelli/Wang as optional or
historical supports. That was sufficient for a coarse table-level audit, but it
did not cover the DESI-era nonparametric and sign-switching literature that now
appears directly relevant to timing support.

The strongest missing coverage is not an Escamilla data-product detail. It is
DESI-era IV/IDE timing literature, especially nonparametric `beta(z)` and
sign-switching reconstructions.

## Prioritized Expansion Targets

| Rank | Target | Expected information gain | Relevance to retained timing | Practical executability | Likelihood of changing interpretation |
| ---: | --- | --- | --- | --- | --- |
| 1 | Li and Zhang 2025 DESI DR2 sign-reversal IDE | very high | high | medium | high |
| 2 | Silva et al. 2025 DESI DR2 IDE/S-IDE | high | high | high | medium-high |
| 3 | Figueruelo et al. 2026 DESI DR2 linear/nonlinear IDE | medium-high | medium | high | medium |
| 4 | Tsedrik et al. 2025 BOSS/DES Y3 dark scattering | medium | medium | medium | medium-low |
| 5 | You et al. 2025 DESI DR2 coupled dark sector | medium | low-medium | medium | low-medium |
| 6 | Silva et al. 2024 non-linear matter-power IDE | medium | medium for growth consequences | medium | low-medium |

## Recommendation

The current IV/IDE timing-literature coverage is not sufficient to judge the
retained timing intuition fairly. Broader DESI-era timing coverage should come
before Escamilla-specific posterior recovery.

The next non-experiment step should be a DESI-era timing-literature feasibility
audit centered on Li and Zhang 2025 and Silva et al. 2025, with attention to
whether their public tables, figures, code, or author-provided products can
support timing-family comparison.
