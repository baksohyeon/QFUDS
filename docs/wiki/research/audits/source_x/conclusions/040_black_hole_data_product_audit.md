---
doc_id: audit_2026_06_10_black_hole_data_product_audit
title: "2026-06-10 Black-Hole Data Product Audit"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_black_hole_data_product_audit_plan
  - audit_2026_06_10_phase3_qnu_derivation_attempt
  - audit_2026_06_10_phase3_qnu_derivation_attempt_plan
  - audit_2026_06_10_phase2_candidate_selection_closeout
  - audit_2026_06_10_black_hole_coupled_literature_search
  - literature_cache_index
  - roadmap
  - repository_levels_glossary
  - missing_physics_map
  - blocked_admission_rule_checkpoint
next_gate: no derivation; black-hole lanes remain data-product blocked until a QFUDS-usable product is recovered
last_updated: 2026-06-10
---

# 2026-06-10 Black-Hole Data Product Audit

## Purpose

Execute the approved
[2026-06-10 Black-Hole Data Product Audit Plan](../plans/040_black_hole_data_product_audit_plan.md).

This is a dated, scope-limited product-coverage audit for the retained
black-hole quantities after the Phase 3 `Q^nu` feasibility result.

Current Phase 3 state: `data_product_blocked`.

This audit asks whether usable data products can be constructed for:

- Lane A: `rho_BH(a)` or `d rho_BH / dln(a)`.
- Lane B: `S_BH(a)` or `dS_BH / dln(a)`.

## Status Boundary

This audit remains `data_product_blocked`, not physics_blocked.

Do not derive Q^nu.

No `Q^nu` is derived here.

No source-to-transfer equation is introduced here.

No physical branch is opened here.

Physical-QFUDS Level 2B remains blocked.

Roadmap unchanged.

## Product-State Definitions Used

This audit uses the product-state distinctions required by the plan:

| State | Definition |
| --- | --- |
| `literature exists` | Relevant paper or model exists, but no extractable product has been confirmed. |
| `data product exists` | Figures, tables, code, samples, or downloadable assets exist. |
| `reproducible data product exists` | Public data/code or numeric tables allow reconstruction with documented units and uncertainty. |
| `QFUDS-usable data product exists` | Product has units, redshift coverage, uncertainty, normalization route, provenance, and can define `X`; it still does not by itself admit `Q^nu`. |

Candidate classifications used:

```text
literature_only
data_product_exists
reproducible_data_product_exists
qfuds_usable_candidate
inaccessible
irrelevant
```

This audit keeps literature hit, data-product hit, reproducibility hit, and
QFUDS-usable hit separate.

## Search Method

The audit used the repository cache first, then a bounded external product pass
for the search axes required by the plan.

Repository starting points:

- [2026-06-10 Phase 3 Q^nu Derivation Attempt](031_phase3_qnu_derivation_attempt.md)
- [2026-06-10 Phase 3 Q^nu Derivation Attempt Plan](../plans/030_phase3_qnu_derivation_attempt_plan.md)
- [2026-06-10 Phase 2 Candidate Selection Closeout](029_phase2_candidate_selection_closeout.md)
- [2026-06-10 Black-Hole-Coupled Literature Search Audit](../coverage/022_phase2_black_hole_coupled_literature_search_audit.md)
- [Literature Cache](../../../literature/README.md)

External pages checked:

- Farrah 2023 arXiv page:
  <https://arxiv.org/abs/2302.07878>
- Croker 2024 arXiv page:
  <https://arxiv.org/abs/2405.12282>
- Amendola 2024 journal page:
  <https://academic.oup.com/mnras/article/528/2/2377/7529208>
- GWTC-3 population data release:
  <https://zenodo.org/records/11254021>
- GWTC-3 parameter-estimation data release:
  <https://zenodo.org/records/8177023>
- GWTC-4.0 population data release:
  <https://zenodo.org/records/16911563>
- Chen, Jani, and Kephart 2026 entropy-budget arXiv page:
  <https://arxiv.org/html/2601.13621v1>
- Lineweaver entropy-budget chapter:
  <https://www.mso.anu.edu.au/~charley/papers/Chapter22Lineweaver.pdf>

No external assets were downloaded. No raw or extracted assets were added under
`docs/wiki/research/assets/`.

No new literature notes were created. External hits are recorded here as audit
coverage, not promoted into the literature cache.

## Lane A Search Trace

| Search axis | Query keywords used | Source found | Source status | Product status | Cache action | Reason for inclusion or rejection |
| --- | --- | --- | --- | --- | --- | --- |
| SMBH mass density evolution | `SMBH mass density evolution public data table rho_BH redshift`; `Lacy 2024 SMBH accretion history cosmological coupling data code` | [Lacy 2024](../../../literature/lacy_2024_smbh_accretion_coupling_constraints.md), Farrah 2023, Croker 2024 | already_cached | figure_only | reused_existing_cache | Literature hit and figure/table-level constraint hit, but no public `rho_BH(a)` table with uncertainty and normalization route was found. Product hit / QFUDS miss. |
| Black-hole mass function evolution | `black hole mass function evolution public data table redshift SMBH`; `evolution black hole mass function with redshift public data` | A&A 2024 binary-black-hole population evolution result surfaced externally; LVK population products surfaced through GWTC releases | externally_found_not_cached | downloadable_data_available | recorded_gap_only | LVK population products are real downloadable products, but they are merger-population distributions, not a cosmic SMBH `rho_BH(a)` or BHMF-to-density history. Product hit / QFUDS miss. |
| Accretion history reconstructions | `supermassive black hole accretion history constraints cosmological coupling data code`; `arXiv 2312.12344 code data` | [Lacy 2024](../../../literature/lacy_2024_smbh_accretion_coupling_constraints.md) | already_cached | figure_only | reused_existing_cache | Accretion-history constraints exist, but no public code, chains, or machine-readable accretion-history product were found in this pass. Literature hit / product miss for QFUDS use. |
| Black-hole growth histories | `Farrah 2023 cosmological coupling black holes data repository`; `Croker 2024 DESI cosmologically coupled black holes code data repository` | [Farrah 2023](../../../literature/farrah_2023_cosmological_coupling_black_holes.md), [Croker 2024](../../../literature/croker_2024_desi_coupled_black_holes.md) | already_cached | figure_only | reused_existing_cache | Both papers define adjacent CCBH growth/source histories and figures, but no public reusable numeric source-history product was found. Product hit / QFUDS miss. |
| Merger-driven growth products | `GWTC-3 population data release Zenodo figure data population samples`; `GWTC-4.0 population properties data release` | [Abbott 2023 GWTC-3 population record](../../../literature/abbott_2023_gwtc3_population_merging_compact_binaries.md), GWTC-3 Zenodo, GWTC-4 Zenodo | already_cached and externally_found_not_cached | downloadable_data_available | reused_existing_cache; recorded_gap_only | LVK products are reproducible merger-population products. They can support merger-rate or mass-distribution checks, but not by themselves `rho_BH(a)` or `d rho_BH/dln(a)` with QFUDS normalization. Reproducibility hit / QFUDS miss. |

## Lane B Search Trace

| Search axis | Query keywords used | Source found | Source status | Product status | Cache action | Reason for inclusion or rejection |
| --- | --- | --- | --- | --- | --- | --- |
| Black-hole entropy inventories | `black hole entropy inventory cosmic entropy budget public data table`; `cosmic entropy budget black holes entropy table Egan Lineweaver data` | Lineweaver entropy-budget chapter; Chen, Jani, and Kephart 2026 arXiv page | externally_found_not_cached | table_available | recorded_gap_only | Present-day inventory tables exist, but no accepted `S_BH(a)` product with provenance, uncertainty, and normalization route was recovered. Data-product hit / QFUDS miss. |
| Cosmic entropy budgets | `cosmic entropy budget black holes entropy table Egan Lineweaver data`; `Cosmological Budget of Entropy from Merging Black Holes` | Lineweaver entropy-budget chapter; Chen, Jani, and Kephart 2026 arXiv page | externally_found_not_cached | figure_only | recorded_gap_only | Literature and figure/table products exist. The 2026 preprint gives redshift-shaped merger entropy figures and equations, but no downloadable numerical product or QFUDS conversion law was found. Product hit / QFUDS miss. |
| SMBH entropy evolution | `supermassive black hole entropy evolution redshift data product`; `SMBH entropy evolution cosmic history` | Lineweaver present-day entropy discussion; no direct SMBH entropy evolution product found | externally_found_not_cached | no_product | recorded_gap_only | SMBHs dominate present entropy budgets, but no `S_SMBH(a)` or `dS_SMBH/dln(a)` product was recovered. Literature hit / product miss. |
| Remnant entropy accounting | `black hole remnants entropy accounting data`; cached remnant comparator records | [Rovelli 2018](../../../literature/rovelli_2018_white_hole_dark_matter.md), [Barrau 2021](../../../literature/barrau_2021_white_hole_remnant_constraints.md), [Rovelli 2024](../../../literature/rovelli_2024_planck_star_remnant_review.md), Chen, Jani, and Kephart 2026 | already_cached and externally_found_not_cached | figure_only | reused_existing_cache; recorded_gap_only | Remnant and merger-entropy literature exists, but the cached remnant records do not expose a cosmic entropy-history data product. Literature hit / product miss for QFUDS. |
| Entropy history reconstructions | `black hole entropy history reconstruction cosmic black hole mass function`; `merger generated entropy redshift history data` | Chen, Jani, and Kephart 2026 arXiv page | externally_found_not_cached | reconstructable_from_paper | recorded_gap_only | The paper provides equations and redshift-history figures for merger-generated entropy, but no public numeric table/code was found. It may be reconstructable from the paper plus LVK products, but is not yet QFUDS-usable. Reproducibility miss / QFUDS miss. |

## Candidate Product Evaluation Matrix

| Candidate | Lane | Literature source | Public data availability | Reproducible? | Units | Redshift coverage | Uncertainty | Update frequency | Can define `X`? | Could eventually support `Q^nu`? | Classification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CCBH SMBH mass-growth evidence | A | Farrah 2023 | Paper figures; no public repository found | No | BH mass and density language in paper; no reusable `rho_BH(a)` product | `0 < z ~= 2.5` growth test; implication discussed to `z <~ 7` | Paper-level confidence, not reusable covariance product | Static paper | Partial source concept only | No; lacks QFUDS transfer equation, frame, and perturbation route | `data_product_exists` | Product hit / QFUDS miss. Strong comparator, not QFUDS source evidence. |
| DESI-era CCBH dark-energy source history | A | Croker 2024 | Paper figures/tables; no public repository found | No | DE density and baryon-conversion parameters in paper, not QFUDS `rho_BH(a)` | DESI late-time BAO range | Paper-level parameter constraints, not reusable chain product found | Static paper | Partial source concept only | No; would reduce toward CCBH without distinct QFUDS equation | `data_product_exists` | Product hit / QFUDS miss. Strong known-model reduction pressure. |
| SMBH accretion-history coupling constraint | A | Lacy 2024 | Paper figures/tables; no public code/data found | No | SMBH mass density and accreted AGN mass constraints | Accretion-history comparison to `z ~= 6` | Paper-level bounds on `k` | Static paper | Constraint only; not source `X` | No; constrains CCBH-like assumptions | `data_product_exists` | Useful constraint, not a source-history product. |
| CCBH LVK constraint code route | A | Amendola 2024 | Public code repositories listed in cached record; LVK products public | Partially | Coupling index and LVK mass/redshift population variables | LVK population range, not cosmic `rho_BH(a)` | Reproducible only after code/data setup | Static code unless repositories change | No; constraint route only | No; tests CCBH-like `k`, not QFUDS `Q^nu` | `reproducible_data_product_exists` | Reproducibility hit / QFUDS miss. |
| GWTC-3 compact-binary population release | A | Abbott 2023; Zenodo 11254021 | Downloadable population data, figure data, table data, scripts/tutorials | Yes for LVK population products | Merger population, mass, spin, redshift variables | Detector-limited compact-binary population | Population samples and product uncertainties available | Static release, v3 as checked | Can define merger-rate or mass-distribution proxy, not `rho_BH(a)` | No; no phase transfer or phase-B pressure law | `reproducible_data_product_exists` | Strong product hit, but wrong quantity for QFUDS admission. |
| GWTC-4.0 compact-binary population release | A | LVK 2025 Zenodo 16911563 | Large downloadable `popsummary` products, figure scripts, event list, tutorial | Yes for LVK population products | Merger population, mass, spin, redshift variables | O4a/GWTC-4 population scope | Population products expose model uncertainty | Static release, v1 as checked | Can define updated merger-population proxy, not `rho_BH(a)` | No; no QFUDS transfer law | `reproducible_data_product_exists` | Externally found product; recorded here only, not cached. |
| Present-day cosmic black-hole entropy inventory | B | Lineweaver entropy-budget chapter | Table-level entropy budget | Partially from paper | Entropy in `k` units | Present-day only | Literature-level estimates | Static chapter | Defines present entropy inventory only | No; no entropy-to-energy conversion law | `data_product_exists` | Data-product hit / QFUDS miss. |
| Merger-generated black-hole entropy history | B | Chen, Jani, and Kephart 2026 | ArXiv figures, equations, tables; no downloadable numeric product found | Reconstructable from paper plus LVK inputs, not directly reproduced here | Entropy and entropy density | Redshift-history figures and equations, including merger history | Uses LVK population uncertainty assumptions | Static preprint as checked | Partial for merger entropy, not total `S_BH(a)` | No; no QFUDS conversion law, frame, or `delta Q` route | `data_product_exists` | Best Lane B hit, but still QFUDS miss. |
| Remnant/white-hole entropy accounting | B | Rovelli 2018; Barrau 2021; Rovelli 2024 | Literature records only in current cache | No | Remnant/Planck-star concepts, not productized entropy history | Not a redshift product | No product uncertainty | Static papers/reviews | No | No | `literature_only` | Literature hit / product miss. |

## Lane A Conclusion

Lane A remains `data_product_blocked`.

Strong products exist for adjacent questions:

- CCBH paper figures and tables.
- CCBH constraint code routes.
- LVK/GWTC downloadable compact-binary population products.

No checked source supplies a QFUDS-usable `rho_BH(a)` or
`d rho_BH / dln(a)` product with all of:

```text
units =
redshift coverage =
uncertainty =
normalization route =
provenance =
candidate X =
```

LVK/GWTC products are the strongest reproducibility hit. They are not a direct
QFUDS mass-density source history and do not support `Q^nu` by themselves.

## Lane B Conclusion

Lane B remains `data_product_blocked`.

Entropy literature exists, and a recent entropy-budget preprint gives the
strongest product-shaped hit for merger-generated black-hole entropy history.

No checked source supplies a QFUDS-usable `S_BH(a)` or `dS_BH / dln(a)` product
with all of:

```text
units =
redshift coverage =
uncertainty =
normalization route =
provenance =
candidate X =
```

The best Lane B hit is still not a physical QFUDS source. It lacks an
entropy-to-energy conversion law, a transfer frame, phase-B `w ~= -1` rationale,
and a perturbation route for `delta Q`.

## Products Not Found

As of this 2026-06-10 audit, within the sources checked here:

- no public QFUDS-ready `rho_BH(a)` table was found;
- no public QFUDS-ready `d rho_BH / dln(a)` table was found;
- no public QFUDS-ready `S_BH(a)` table was found;
- no public QFUDS-ready `dS_BH / dln(a)` table was found;
- no source supplied a non-circular normalization route into QFUDS;
- no source supplied `Q^nu`;
- no source supplied a `delta Q` route;
- no source supplied a known-model distinction for QFUDS.

This is a dated "not found" statement for the checked sources only. It does not
imply exhaustive literature coverage.

## Cache Actions

No new literature cache records were created.

No new product cache records were created.

No assets were downloaded or extracted.

Existing cache records reused:

- [Farrah 2023](../../../literature/farrah_2023_cosmological_coupling_black_holes.md)
- [Croker 2024](../../../literature/croker_2024_desi_coupled_black_holes.md)
- [Lacy 2024](../../../literature/lacy_2024_smbh_accretion_coupling_constraints.md)
- [Amendola 2024](../../../literature/amendola_2024_gw_constraints_ccbh.md)
- [Abbott 2023 GWTC-3 population](../../../literature/abbott_2023_gwtc3_population_merging_compact_binaries.md)
- [Rovelli 2018](../../../literature/rovelli_2018_white_hole_dark_matter.md)
- [Barrau 2021](../../../literature/barrau_2021_white_hole_remnant_constraints.md)
- [Rovelli 2024](../../../literature/rovelli_2024_planck_star_remnant_review.md)

External product hits recorded as gaps only:

- GWTC-4.0 population data release.
- Chen, Jani, and Kephart 2026 entropy-budget preprint.
- Lineweaver entropy-budget chapter.

## No-Derivation Confirmation

Do not derive Q^nu.

This audit did not derive `Q^nu`.

This audit did not define a new physical `X`.

This audit did not define a source-to-transfer law.

This audit did not define `delta Q`.

This audit did not change the known-model reduction risk.

## Level 2B / Roadmap Boundary

Physical-QFUDS Level 2B remains blocked.

Roadmap unchanged.

This audit does not modify roadmap status, roadmap level, decision-log state, or
the current retained branch classification.

Result: the black-hole lanes remain `data_product_blocked`, not physics_blocked.

The next admissible step is still not a Physical-QFUDS Level 2B derivation. It
would be either:

- a narrower product-recovery pass that caches a specific candidate data
  product; or
- a separate future derivation attempt only after a QFUDS-usable `X` product
  exists.
