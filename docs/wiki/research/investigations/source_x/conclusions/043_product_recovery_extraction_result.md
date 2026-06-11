---
doc_id: audit_2026_06_11_product_recovery_extraction_result
title: "2026-06-11 Product-Recovery Extraction Result"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_black_hole_data_product_audit
  - audit_2026_06_11_product_recovery_candidate_selection_plan
  - audit_2026_06_11_product_recovery_execution_plan
  - asset_lacy_2024_smbh_density_recovery_extract
  - asset_chen_2026_merger_entropy_history_recovery_extract
  - roadmap
next_gate: choose whether to plan numeric digitization; do not derive delta Q before candidate X exists
last_updated: 2026-06-11
---

# 2026-06-11 Product-Recovery Extraction Result

## Purpose

This document closes out the `043` product-recovery extraction step for the
retained black-hole lanes.

The source extraction records remain under the paper-level asset directories:

- [Lacy 2024 SMBH density recovery extract](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/digitization/lacy_2024_smbh_density_recovery_extract.md)
- [Chen 2026 merger entropy history recovery extract](../../../assets/chen_2026_merger_entropy_budget/digitization/chen_2026_merger_entropy_history_recovery_extract.md)

Those files are asset-level extraction records. This file is the Source-X
conclusion record that states what the extraction changed and what remains
blocked.

## Status Boundary

The black-hole lanes remain `data_product_blocked`, not physics_blocked.

`manual_structured_extract` records now exist.

`qfuds_usable_numeric_product` does not exist.

Candidate `X` boundary is missing.

No `Q^nu` is derived here.

No `delta Q` is derived here.

No Physical-QFUDS Level 2B branch is opened here.

Roadmap status is unchanged.

No QFUDS support claim is made here.

## Result Summary

| Lane | Extract record | What was recovered | What remains missing | Result |
| --- | --- | --- | --- | --- |
| A | [Lacy 2024 SMBH density recovery extract](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/digitization/lacy_2024_smbh_density_recovery_extract.md) | local `rho_BH` normalization records; Equation 9 source-history structure; Figure 1 route over `z=6` to `z=0`; Figure 2 high-redshift constraint target | standalone digitized `rho_BH(a)` curve; `d rho_BH / dln(a)`; candidate `X`; resolved unit conflict for the adopted local range | `manual_structured_extract`; still `data_product_blocked` |
| B | [Chen 2026 merger entropy history recovery extract](../../../assets/chen_2026_merger_entropy_budget/digitization/chen_2026_merger_entropy_history_recovery_extract.md) | Table 1 entropy and entropy-density values; Figure 5 entropy landmarks and power-law structure; Figure 6 crossover landmarks; Figure 7 retrospective entropy-density structure; Equation 16 definition | standalone digitized `S_BH(a)` curve; `dS_BH / dln(a)`; candidate `X`; entropy-to-energy conversion law; QFUDS normalization route | `manual_structured_extract`; still `data_product_blocked` |

## Lane A Decision

Lane A recovered useful source-history material, but not a QFUDS-usable product.

Recovered:

- local SMBH density normalization checks at `z=0`;
- Equation 9 as a structured `rho_BH(z)` route;
- Figure 1 as a non-digitized route for accretion-history density curves;
- Figure 2 as a non-digitized high-redshift constraint target.

Still missing:

- full numeric `rho_BH(a)` curve;
- `d rho_BH / dln(a)`;
- reusable covariance or posterior product;
- resolved `Mpc^-1` versus `Mpc^-3` unit conflict in the adopted local range;
- QFUDS normalization route;
- candidate `X` boundary.

Lane A remains `data_product_blocked`.

## Lane B Decision

Lane B recovered useful entropy-history landmarks and structure, but not a
QFUDS-usable product.

Recovered:

- Table 1 BBH merger entropy and entropy-density inventory values;
- Figure 5 total entropy peak, entropy-density peak redshift, and low-redshift
  power-law structure;
- Figure 6 cumulative-entropy crossover landmarks;
- Figure 7 retrospective entropy-density peak and Equation 16 structure.

Still missing:

- full numeric `S_BH(a)` curve;
- `dS_BH / dln(a)`;
- reusable covariance, posterior product, or code reproduction route;
- entropy-to-energy conversion law;
- QFUDS normalization route;
- candidate `X` boundary.

Lane B remains `data_product_blocked`.

## Product-State Decision

The product state has advanced only to:

```text
asset_extracted_not_digitized
manual_structured_extract
```

The product state has not advanced to:

```text
numeric_digitized
qfuds_usable_candidate
qfuds_usable_numeric_product
```

The extraction improves audit precision by separating what is present from what
is missing. It does not change the physical admission status.

## Next Gate

The next responsible step is a separate decision about numeric digitization.

Possible next plan:

```text
044 numeric digitization plan
```

That plan should choose one curve target before extracting points, for example:

- Lacy Figure 1 for a candidate `rho_BH(a)` curve; or
- Chen Figure 5 or Figure 7 for a candidate `S_BH(a)` or entropy-density curve.

Do not attempt `delta Q` unless a later accepted product first defines a
candidate `X` with the required product fields.

## Final Decision

The 043 extraction is valid as product recovery.

It is not QFUDS evidence.

It is not a physical derivation.

It is not a Level 2B admission result.

The black-hole lane remains:

```text
data_product_blocked
```
