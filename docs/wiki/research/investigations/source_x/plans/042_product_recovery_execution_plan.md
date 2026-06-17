---
doc_id: audit_2026_06_11_product_recovery_execution_plan
title: "2026-06-11 Product-Recovery Execution Plan"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_11_product_recovery_candidate_selection_plan
  - audit_2026_06_10_black_hole_data_product_audit
  - asset_lacy_2024_smbh_accretion_coupling_constraints
  - asset_chen_2026_merger_entropy_budget
  - roadmap
next_gate: approved 043 extraction only
last_updated: 2026-06-17
---

# 2026-06-11 Product-Recovery Execution Plan

## Purpose

This plan follows the
[2026-06-11 Product-Recovery Candidate Selection Plan](041_product_recovery_candidate_selection_plan.md).

The sequence is:

1. `041` selected the primary cached product-recovery candidates.
2. `042` defines the extraction procedure.
3. `043` will perform extraction later only if explicitly approved.

This document does not extract values, digitize figures, populate the product
schema, or modify asset manifests. It only defines how a future `043` extraction
should populate a structured recovery record.

## Status Boundary

Black-hole lanes remain `data_product_blocked`, not physics_blocked.

Physical-QFUDS Level 2B remains blocked.

Roadmap status remains unchanged.

Do not derive `Q^nu`.

Do not derive `delta Q`.

Do not open Physical-QFUDS Level 2B.

Do not claim QFUDS support.

Do not modify asset README files to claim extraction exists.

Do not create structured extract files in this task.

## 043 Output Rule

A future `043` extraction may write extracted products only under the selected
asset's `digitization/` directory. The future extract must remain labeled as a
source-history candidate or comparator unless it actually supplies units,
redshift coverage, uncertainty route, normalization route, provenance, and a
candidate `X` boundary.

This plan names future output paths, but it does not create them.

## Required Product Fields For 043

The future `043` extraction should populate the schema from `041` only after
checking the source files listed below.

Required fields:

| Field | Requirement for 043 |
| --- | --- |
| `product_id` | Stable identifier for each extracted row or structured block. |
| `lane` | `A` for Lacy or `B` for Chen. |
| `source_asset_key` | Exact asset directory key under `docs/wiki/research/assets/`. |
| `source_file` | Exact PDF, Markdown, TeX, figure, table, or archive file used. |
| `source_location` | Page, section, equation, table, figure, caption, or archive member. |
| `quantity` | One of the lane target quantities below. |
| `independent_variable` | Redshift, scale factor, lookback time, mass, or inventory state. |
| `z` | Redshift value or coverage range where available. |
| `a` | Scale factor derived from `a = 1 / (1 + z)` where relevant. |
| `ln_a` | Natural log scale factor where relevant. |
| `value` | Extracted value only after direct source verification. |
| `value_unit` | Source unit or verified converted unit. |
| `uncertainty_low` | Lower uncertainty if the source provides it. |
| `uncertainty_high` | Upper uncertainty if the source provides it. |
| `uncertainty_type` | Confidence interval, posterior interval, model spread, digitization error, or absent. |
| `normalization_reference` | Source normalization, cosmology, volume, density convention, or table baseline. |
| `extraction_method` | Manual table extraction, source-TeX parsing, figure digitization, or code reproduction. |
| `quality_state` | `manual_structured_extract` or `numeric_digitized`. |
| `redshift_coverage` | Stated coverage range and gaps. |
| `unit_status` | Verified, inferred, converted, inconsistent, or missing. |
| `provenance_note` | Short source trace for the row. |
| `qfuds_role` | Source-history candidate only, comparator, normalization check, or rejected for QFUDS use. |
| `limitations` | Missing fields, source caveats, interpretation limits, and reuse limits. |

If a field cannot be supported from the source, `043` must record the missing
field explicitly rather than inferring it.

## Lane A: Lacy 2024 Procedure

Primary candidate selected by `041`:
[Lacy 2024 SMBH accretion coupling assets](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/README.md).

Source asset directory:

```text
docs/wiki/research/assets/lacy_2024_smbh_accretion_coupling_constraints/
```

Future `043` output path:

```text
docs/wiki/research/assets/lacy_2024_smbh_accretion_coupling_constraints/digitization/lacy_2024_smbh_density_recovery_extract.md
```

Target quantity:

```text
rho_BH(a)
d rho_BH / dln(a)
```

### Lane A Source Files To Inspect

The future `043` extraction must inspect these files before recording values:

| Source type | File |
| --- | --- |
| Source PDF | [paper_arxiv_2312.12344.pdf](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/source/paper_arxiv_2312.12344.pdf) |
| [PageIndex](https://github.com/VectifyAI/PageIndex) Markdown | [paper_arxiv_2312.12344.md](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/digitization/paper_arxiv_2312.12344.md) |
| TeX source | [AGN_BHgrowth.tex](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/source/extracted/AGN_BHgrowth.tex) |
| Figure 1 PNG | [scenario1_revised.png](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/figures/extracted/scenario1_revised.png) |
| Figure 2 PNG | [Salpeter_plot_revised.png](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/figures/extracted/Salpeter_plot_revised.png) |

### Lane A Source Location Candidates

`043` should inspect, at minimum:

- Section 3.1, local SMBH mass density discussion.
- Equation 9, accretion-history density integral.
- Figure 1 caption and plotted curves for local SMBH density and accretion
  history.
- Figure 2 caption and parameter-space constraints.
- Text discussing local SMBH density estimates, including GD07,
  Kormendy-Ho/Thanjavur normalization, and GWB-based density estimates.
- Text discussing integration from `z=6` to `z=0`.
- Text discussing uncertainty from AGN luminosity density, radiative efficiency
  `eta`, Eddington ratio `lambda`, and local SMBH mass-density assumptions.

### Lane A Required Checks

Unit checks:

- Verify whether each SMBH density value is in `M_sun Mpc^-3`.
- If [PageIndex](https://github.com/VectifyAI/PageIndex) text and TeX/PDF disagree on powers of `Mpc`, treat the unit as
  inconsistent until checked against the PDF.
- Do not reuse any value numerically if its density unit cannot be verified.

Redshift coverage checks:

- Record whether a value is local only at `z=0`.
- Record whether an equation or curve covers the accretion integration from
  `z=6` to `z=0`.
- Convert any redshift point or range into `a = 1 / (1 + z)` and `ln_a` only
  when the redshift is explicit.

Uncertainty checks:

- Record local-density ranges separately from GWB posterior ranges.
- Record uncertainty sources for AGN luminosity density, `eta`, `lambda`, and
  local SMBH density.
- If no covariance or posterior product is available, record that absence.

Normalization checks:

- Record source cosmology and any `H0`, `Omega_M`, or `Omega_Lambda`
  conventions.
- Record whether density normalization comes from GD07, Kormendy-Ho/Thanjavur,
  GWB posterior assumptions, or the Shen et al. luminosity function.
- Do not create a QFUDS normalization route.

Provenance requirements:

- Each extracted item must cite the exact source file and source location.
- For figure-derived values, record the figure filename, caption, panel, axis,
  curve, and whether extraction was visual, manual, or digitized.
- For equation-derived structure, record the equation number and TeX/PDF source.

Failure criteria:

- Fail Lane A as a QFUDS-usable product if units cannot be verified.
- Fail Lane A as a QFUDS-usable product if only local `z=0` density exists and
  no usable history or derivative route is recovered.
- Fail Lane A as a QFUDS-usable product if uncertainty or normalization route is
  absent.
- Fail Lane A as a QFUDS-usable product if the record remains only a CCBH or
  accretion-history comparator.
- Never upgrade Lane A beyond `data_product_blocked` without a candidate `X`
  boundary and the later non-product admission items.

## Lane B: Chen 2026 Procedure

Primary candidate selected by `041`:
[Chen 2026 merger entropy assets](../../../assets/chen_2026_merger_entropy_budget/README.md).

Source asset directory:

```text
docs/wiki/research/assets/chen_2026_merger_entropy_budget/
```

Future `043` output path:

```text
docs/wiki/research/assets/chen_2026_merger_entropy_budget/digitization/chen_2026_merger_entropy_history_recovery_extract.md
```

Target quantity:

```text
S_BH(a)
dS_BH / dln(a)
```

### Lane B Source Files To Inspect

The future `043` extraction must inspect these files before recording values:

| Source type | File |
| --- | --- |
| Source PDF | [paper_arxiv_2601.13621.pdf](../../../assets/chen_2026_merger_entropy_budget/source/paper_arxiv_2601.13621.pdf) |
| [PageIndex](https://github.com/VectifyAI/PageIndex) Markdown | [paper_arxiv_2601.13621.md](../../../assets/chen_2026_merger_entropy_budget/digitization/paper_arxiv_2601.13621.md) |
| TeX source | [sample631.tex](../../../assets/chen_2026_merger_entropy_budget/source/extracted/sample631.tex) |
| Figure 5 PNG | [growth_entropy_gwtc4_only.png](../../../assets/chen_2026_merger_entropy_budget/figures/extracted/growth_entropy_gwtc4_only.png) |
| Figure 6 PNG | [cumulative_ent_den_gwtc4_only.png](../../../assets/chen_2026_merger_entropy_budget/figures/extracted/cumulative_ent_den_gwtc4_only.png) |
| Figure 7 PNG | [cumulative_tot_ent_gwtc4_pbh.png](../../../assets/chen_2026_merger_entropy_budget/figures/extracted/cumulative_tot_ent_gwtc4_pbh.png) |

### Lane B Source Location Candidates

`043` should inspect, at minimum:

- Table 1, updated entropy budget and entropy-density rows.
- Equations 1-16, especially entropy, merger, density, and cosmological density
  parameter definitions.
- Figure 5 caption and text for merger-generated entropy history.
- Figure 6 caption and text for cumulative entropy history and crossover
  redshifts.
- Figure 7 caption and text for PBH/BBH cumulative entropy comparisons if
  relevant to the selected history.
- Text describing `z in [0.01, 20]` coverage.
- Text describing peak redshifts, crossover redshifts, and uncertainty ranges.

### Lane B Required Checks

Unit checks:

- Verify whether each value is entropy in `k`, entropy density in `k m^-3`, or
  a redshift event rather than a scalar entropy product.
- Verify Table 1 exponents against the PDF or TeX before numeric reuse.
- Do not convert entropy to energy density.

Redshift coverage checks:

- Record whether the source item is present inventory, cumulative history,
  instantaneous/growth history, or derivative-like history.
- Record whether the source item covers `z in [0.01, 20]` or only a peak,
  crossover, or table inventory value.
- Convert explicit redshift points or ranges into `a = 1 / (1 + z)` and `ln_a`.

Uncertainty checks:

- Record table uncertainties separately from figure-text peak and crossover
  uncertainties.
- Record whether uncertainty comes from LVK population assumptions, model
  spread, quoted intervals, or digitization error.
- If no covariance or posterior product is available, record that absence.

Normalization checks:

- Record whether entropy is total observable-universe entropy, comoving-frame
  entropy, entropy density, cumulative entropy, or merger-generated entropy.
- Record the volume, population model, LVK/GWTC release, PBH fraction, or other
  source convention where stated.
- Do not create an entropy-to-energy conversion law or QFUDS normalization
  route.

Provenance requirements:

- Each extracted item must cite the exact source file and source location.
- For figure-derived values, record figure filename, caption, axis, curve,
  redshift range, and whether extraction was visual, manual, or digitized.
- For table values, record the table row and whether exponents were verified
  against PDF/TeX.
- For equations, record the equation number and whether the extracted product is
  an equation structure rather than a numerical product.

Failure criteria:

- Fail Lane B as a QFUDS-usable product if entropy units or Table 1 exponents
  cannot be verified.
- Fail Lane B as a QFUDS-usable product if the record is only a present
  inventory and no usable history or derivative route is recovered.
- Fail Lane B as a QFUDS-usable product if no uncertainty or normalization route
  is available.
- Fail Lane B as a QFUDS-usable product if the source remains only an entropy
  comparator with no entropy-to-energy conversion law.
- Never upgrade Lane B beyond `data_product_blocked` without a candidate `X`
  boundary and the later non-product admission items.

## 043 Closeout Requirements

After a future `043` extraction, the extractor must report:

- files created;
- files modified;
- exact source files inspected;
- whether outputs are `manual_structured_extract` or `numeric_digitized`;
- whether each lane has units, redshift coverage, uncertainty route,
  normalization route, provenance, and candidate `X` boundary;
- whether the lane remains `data_product_blocked`;
- confirmation that no `Q^nu`, `delta Q`, Level 2B opening, roadmap change, or
  QFUDS support claim was made.

If a later `043` extraction creates output files, it may update the relevant
asset digitization index and asset root manifest only to point to actual
existing extraction outputs.

## Validation Plan

After creating this plan, run:

```bash
rtk python3 scripts/validate_docs.py
rtk python3 scripts/research_consistency.py
rtk git diff --check
rtk git status --short
```

Expected status after this plan:

- only this `042` plan is created;
- roadmap status unchanged;
- Physical-QFUDS Level 2B remains blocked;
- black-hole lanes remain `data_product_blocked`;
- no `Q^nu` or `delta Q` derivation exists;
- no structured extract files exist.
