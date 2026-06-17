---
doc_id: audit_2026_06_11_product_recovery_candidate_selection_plan
title: "2026-06-11 Product-Recovery Candidate Selection Plan"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_black_hole_data_product_audit
  - asset_lacy_2024_smbh_accretion_coupling_constraints
  - asset_chen_2026_merger_entropy_budget
  - roadmap
next_gate: manually structure or numerically digitize the selected cached candidates; no derivation
last_updated: 2026-06-17
---

# 2026-06-11 Product-Recovery Candidate Selection Plan

## Purpose

This plan executes the product-recovery follow-up recommended by the
[2026-06-10 Black-Hole Data Product Audit](../conclusions/040_black_hole_data_product_audit.md).

The goal is only to choose which already cached assets should be manually
structured or numerically digitized next for:

- Lane A: `rho_BH(a)` or `d rho_BH / dln(a)`.
- Lane B: `S_BH(a)` or `dS_BH / dln(a)`.

This is a product-recovery plan, not a physics derivation.

## Status Boundary

Black-hole lanes remain `data_product_blocked`, not physics_blocked.

Do not derive `Q^nu`.

Do not derive `delta Q`.

Do not open Physical-QFUDS Level 2B.

Do not modify roadmap status.

Do not claim QFUDS support.

Cached papers, [PageIndex](https://github.com/VectifyAI/PageIndex) full text, figures, tables, TeX source, and Zenodo
assets are not QFUDS-ready products until a future extraction records units,
redshift coverage, uncertainty route, normalization route, provenance, and
limitations.

## Candidate Selection

Primary Lane A candidate:
[Lacy 2024 SMBH accretion coupling assets](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/README.md).

Primary Lane B candidate:
[Chen 2026 merger entropy assets](../../../assets/chen_2026_merger_entropy_budget/README.md).

Selection rationale:

| Lane | Selected asset                                     | Product target                                               | Why selected                                                                                                                                                                                                                                               |
| ---- | -------------------------------------------------- | ------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| A    | Lacy 2024 SMBH accretion coupling constraints      | `rho_BH(a)` or accretion-history-derived `d rho_BH / dln(a)` | It directly discusses local SMBH mass density, AGN accretion integration from `z=6` to `z=0`, uncertainty sources, and figure-level constraints. It is the best cached Lane A source for manual structuring, even though it is not a QFUDS source product. |
| B    | Chen, Jani, and Kephart 2026 merger entropy budget | `S_BH(a)` or `dS_BH / dln(a)` redshift-history candidate     | It contains cached redshift entropy-history figures, entropy equations, and Table 1. It is the best cached Lane B source for numeric digitization, even though it has no entropy-to-energy conversion law.                                                 |

## Lane A Evaluation

Selected asset key:
`lacy_2024_smbh_accretion_coupling_constraints`.

Target output for a future extraction:
`rho_BH(a)` or an accretion-history-derived `d rho_BH / dln(a)` candidate, with
the extraction clearly marked as source-history structure only.

| Criterion                   | Evaluation                                                                                                                                                                                              |
| --------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Asset availability          | PDF, arXiv HTML, arXiv source tar, extracted TeX, extracted figures, rendered figure PNGs, [PageIndex](https://github.com/VectifyAI/PageIndex) structure, and [PageIndex](https://github.com/VectifyAI/PageIndex) full text are cached under `docs/wiki/research/assets/`.                  |
| Markdown conversion quality | `source_text_parse`; useful for section search and equation targeting, not numerical digitization.                                                                                                      |
| Figure/table availability   | Figure 1 contains mass-density and accretion-history constraints; Figure 2 contains parameter-space constraints. No standalone machine-readable product table or covariance product is cached.          |
| Numerical extractability    | Medium-high. Future work should manually verify equations and units against the PDF/source and digitize figure curves or structured values only where provenance is clear.                              |
| Uncertainty route           | Local SMBH density range, Shen et al. luminosity-density uncertainty, radiative efficiency range, Eddington-ratio assumptions, and GWB posterior discussion. No reusable covariance product is present. |
| Unit availability           | SMBH mass density is expected in `M_sun Mpc^-3`; future extraction must verify units against the PDF/source because the extracted text has unit inconsistencies.                                        |
| Redshift coverage           | Accretion integration from `z=6` to `z=0`; high-redshift constraint discussion around `z~4`.                                                                                                            |
| QFUDS relevance             | Source-history candidate only. It does not define a QFUDS transfer law, phase-B pressure rationale, `Q^nu`, `delta Q`, or known-model distinction.                                                      |
| Extraction difficulty       | Medium-high because the useful product is partly figure/equation structured rather than a standalone table.                                                                                             |

Future Lane A extraction review scope:
manually structure the relevant local SMBH density values, accretion-history
equations, redshift interval, and uncertainty sources before attempting any
numeric curve digitization.

## Lane B Evaluation

Selected asset key:
`chen_2026_merger_entropy_budget`.

Target output for a future extraction:
`S_BH(a)` or `dS_BH / dln(a)` redshift-history candidate for merger-generated
black-hole entropy only, with the extraction clearly marked as entropy-history
structure only.

| Criterion                   | Evaluation                                                                                                                                                                                     |
| --------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Asset availability          | PDF, arXiv HTML, arXiv source tar, extracted TeX, source figure PNGs, rendered figure PNG mirrors, [PageIndex](https://github.com/VectifyAI/PageIndex) structure, and [PageIndex](https://github.com/VectifyAI/PageIndex) full text are cached under `docs/wiki/research/assets/`. |
| Markdown conversion quality | `source_text_parse`; includes Table 1 and Eqs. 1-16 for targeting, but remains machine-extracted and not numerical digitization.                                                               |
| Figure/table availability   | Figures 5-7 provide redshift entropy-history products; Table 1 provides an entropy inventory.                                                                                                  |
| Numerical extractability    | Medium. Future work can digitize cached PNG figures and manually verify equations/captions against the PDF/source.                                                                             |
| Uncertainty route           | LVK population assumptions and quoted peak/crossover uncertainties are present. No standalone covariance product is cached.                                                                    |
| Unit availability           | Entropy in `k`, entropy density in `k m^-3`, redshift `z`, and lookback time where applicable.                                                                                                 |
| Redshift coverage           | Figures and text cover merger entropy histories over `z in [0.01, 20]`.                                                                                                                        |
| QFUDS relevance             | Best cached Lane B redshift-history product shape. It does not provide an entropy-to-energy conversion law, transfer frame, `Q^nu`, `delta Q`, or phase-B pressure rationale.                  |
| Extraction difficulty       | Medium because figure digitization is plausible from cached PNGs, but uncertainty and normalization must be documented carefully.                                                              |

Future Lane B extraction review scope:
digitize or manually structure the redshift entropy-history figures and any
supporting Table 1 values, then record whether the result is a present inventory,
a cumulative history, or a derivative-like history.

## Non-Primary Cached Assets

These assets remain useful but are not the primary next extraction targets:

| Asset                                 | Lane        | Reason not primary                                                                                                                                |
| ------------------------------------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------------- |
| Farrah 2023                           | A           | Important CCBH comparator, but the 040 audit found no reusable `rho_BH(a)` product and no public code route.                                      |
| Croker 2024                           | A           | Strong DESI-era CCBH comparator, but product recovery risks reducing to the known CCBH comparison before recovering a black-hole density history. |
| Amendola 2024                         | A           | Better suited to CCBH constraint reproduction and code setup than direct `rho_BH(a)` recovery.                                                    |
| GWTC-3 and GWTC-4 population releases | A/B support | Strong reproducible population products, but not direct cosmic SMBH density or total entropy-history products without additional modeling.        |
| Lineweaver entropy-budget chapter     | B           | Useful present-day entropy inventory comparator, but lacks redshift history; use as a secondary normalization/check after Chen 2026 extraction.   |

## Structured Product Schema

The future extraction product schema is defined here but intentionally left
empty. This plan does not populate the schema and does not recover a product.

Required fields:

| Field                     | Meaning                                                                                    |
| ------------------------- | ------------------------------------------------------------------------------------------ |
| `product_id`              | Stable local identifier for the extracted product.                                         |
| `lane`                    | `A` or `B`.                                                                                |
| `source_asset_key`        | Cached asset folder key under `docs/wiki/research/assets/`.                                |
| `source_file`             | Exact PDF, TeX, Markdown, figure, table, or archive file used.                             |
| `source_location`         | Page, section, equation, table, figure, caption, or archive member.                        |
| `quantity`                | `rho_BH(a)`, `d rho_BH / dln(a)`, `S_BH(a)`, or `dS_BH / dln(a)`.                          |
| `independent_variable`    | Primary x-axis or indexing variable.                                                       |
| `z`                       | Redshift value if available.                                                               |
| `a`                       | Scale factor value if available or derived from `z`.                                       |
| `ln_a`                    | Natural log scale-factor value if available or derived from `a`.                           |
| `value`                   | Extracted numerical value.                                                                 |
| `value_unit`              | Unit as stated or normalized.                                                              |
| `uncertainty_low`         | Lower uncertainty bound if available.                                                      |
| `uncertainty_high`        | Upper uncertainty bound if available.                                                      |
| `uncertainty_type`        | Confidence interval, posterior interval, digitization error, model spread, or absent.      |
| `normalization_reference` | Source normalization, cosmology, volume, density convention, or table baseline.            |
| `extraction_method`       | Manual table extraction, source-TeX parsing, figure digitization, or code reproduction.    |
| `quality_state`           | `manual_structured_extract` or `numeric_digitized`.                                        |
| `redshift_coverage`       | Stated coverage range and any gaps.                                                        |
| `unit_status`             | Verified, inferred, converted, inconsistent, or missing.                                   |
| `provenance_note`         | Short note tying the row back to source evidence.                                          |
| `qfuds_role`              | Source-history candidate only, comparator, normalization check, or rejected for QFUDS use. |
| `limitations`             | Known extraction, interpretation, or reuse limitations.                                    |

Allowed `quality_state` values:

```text
manual_structured_extract
numeric_digitized
```

The future extracted product should be stored under the selected asset's
`digitization/` directory, not in this plan. A future extraction must not upgrade
the black-hole lane out of `data_product_blocked` unless it actually supplies
units, redshift coverage, uncertainty route, normalization route, provenance,
and a candidate `X` boundary.

## Execution Order

1. Lane A: prepare for a future manual structured extraction from Lacy 2024 for SMBH density,
   accretion-history equations, redshift interval, and uncertainty sources.
2. Lane B: prepare for a future manual or numeric extraction from Chen 2026 for
   redshift entropy history, figure provenance, units, and uncertainty route.
3. Compare extracted products only against the 040 audit's data-product criteria.
4. If either extraction lacks units, uncertainty, redshift coverage, or
   normalization route, record the missing field explicitly rather than
   inferring it.
5. Do not attempt `delta Q` unless a later accepted product first defines a
   candidate `X` with the required product fields.

## Validation Plan

After this plan is written, run:

```bash
rtk python3 scripts/validate_docs.py
rtk python3 scripts/research_consistency.py
rtk git diff --check
rtk git status --short
```

Expected status after this plan:

- roadmap status unchanged;
- Physical-QFUDS Level 2B remains blocked;
- black-hole lanes remain `data_product_blocked`;
- no `Q^nu` or `delta Q` derivation exists.
