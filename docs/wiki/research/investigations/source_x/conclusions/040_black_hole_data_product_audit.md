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
  - wiki_governance_004_missing_physics_map
  - wiki_governance_003_blocked_admission_rule_gate
next_gate: no derivation; black-hole lanes remain data-product blocked until a QFUDS-usable product is recovered
last_updated: 2026-06-11
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

## Asset-State Vocabulary

This rerun separates missing products from uncollected or unprocessed assets.
In this document:

- `not found` means no relevant product was found after the asset availability
  check below.
- `not downloaded` means a source exposes an asset, but this audit did not
  retrieve it.
- `not extracted` means an asset exists or was downloaded, but table, figure,
  source, or code extraction was not attempted.
- `recorded_gap_only` must not hide downloadable PDFs, arXiv source bundles,
  figure files, Zenodo records, code repositories, or other raw assets.

Future product audits must use the workflow state ladder instead of collapsing
everything into "not found":

| Display state | Meaning |
| --- | --- |
| `not searched` | No source/product search was attempted. |
| `searched_no_hit` | A search was run and no candidate source was found. |
| `hit_not_cached` | A source was found but no local cache record or asset was created. |
| `asset_available_not_downloaded` | Source assets exist, but were not retrieved. |
| `asset_downloaded_not_extracted` | Source assets were cached, but extraction/inspection was not attempted. |
| `asset_extracted_not_digitized` | Assets were unpacked, extracted, or Markdown-converted, but figure/table digitization or numerical classification was not done. |
| `asset_digitized` | Numeric points were digitized, but not yet classified against the research criterion. |
| `asset_cached` | Raw asset and manifest README are stored in the repo. |
| `inspected_no_numerical_product` | Contents were inspected and no machine-readable numerical product was found. |
| `no_asset_found` | PDF/source/supplement/archive/figure/table/code/raw asset checks found no relevant asset. |

Operational checklist for future agents:
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).

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

External asset availability was rechecked under the repository workflow. PDFs,
arXiv source bundles, arXiv HTML, Zenodo record manifests, selected small Zenodo
table/figure assets, and GitHub repository metadata were cached under
paper/release-level directories in `docs/wiki/research/assets/`.

No new literature notes were created. External hits are recorded here as audit
coverage and asset cache entries, not promoted into the literature cache.

## Asset Availability Check

This check records whether the source exposes raw or extractable assets. It does
not claim that the assets were downloaded, extracted, digitized, or QFUDS-ready.

| External hit | PDF | arXiv HTML | arXiv source tar | Supplementary material | Zenodo dataset | Figure data | Table data | Code repository | Downloadable raw assets |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Farrah 2023 arXiv `2302.07878` | cached | no HTML link found | cached and extracted | no separate supplement found | no | source figure PDFs cached | no standalone table product found | no code repo found | PDF/source cached under [Farrah 2023 assets](../../../assets/farrah_2023_cosmological_coupling_black_holes/README.md) |
| Croker 2024 arXiv `2405.12282` | cached | cached | cached and extracted | no separate supplement found | no | source figure PDFs cached | paper-level table in TeX | no paper-specific code repo found | PDF/HTML/source cached under [Croker 2024 assets](../../../assets/croker_2024_desi_coupled_black_holes/README.md) |
| Lacy 2024 arXiv `2312.12344` | cached | cached | cached and extracted | no separate supplement found | no | source figures cached | paper-level values in TeX | no code repo found | PDF/HTML/source cached under [Lacy 2024 assets](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/README.md) |
| Amendola 2024 arXiv/journal `2307.02474` | cached | cached | cached and extracted | online supplementary table claimed by paper | no Zenodo found in this pass | source figures cached | paper-level and supplementary-table route | GitHub metadata and README snapshots cached | PDF/HTML/source/GitHub metadata cached under [Amendola 2024 assets](../../../assets/amendola_2024_gw_constraints_ccbh/README.md) |
| GWTC-3 population Zenodo `11254021` | linked paper PDF, not primary asset | n/a | n/a | release README cached | manifest cached | `paper_figures.tar.gz` cached and extracted | `table_data.tar.gz` cached and extracted | tutorial/requirements cached, large analyses not downloaded | selected Zenodo assets cached under [GWTC-3 population assets](../../../assets/abbott_2023_gwtc3_population_merging_compact_binaries/README.md) |
| GWTC-3 parameter-estimation Zenodo `8177023` | linked paper PDF, not primary asset | n/a | n/a | release metadata cached | manifest cached | contour/skylocalization assets listed but not downloaded | HDF5 posterior samples listed but not downloaded | notebooks/tools listed by release | manifest cached under [GWTC-3 PE manifest](../../../assets/gwtc3_parameter_estimation_release/README.md) |
| GWTC-4.0 population Zenodo `16911563` | linked paper PDF, not primary asset | n/a | n/a | release README cached | manifest cached | `figures.tar` cached and extracted | event list cached and extracted; large `popsummary` analysis tarballs listed but not downloaded | figure scripts and tutorial cached | selected Zenodo assets cached under [GWTC-4.0 population assets](../../../assets/gwtc4_population_release/README.md) |
| Chen, Jani, and Kephart 2026 arXiv `2601.13621` | cached | cached | cached and extracted | no separate supplement found | no Zenodo found in this pass | source figure PNGs cached | table text in TeX; no standalone table product found | no code repo found | PDF/HTML/source cached under [Chen 2026 assets](../../../assets/chen_2026_merger_entropy_budget/README.md) |
| Lineweaver entropy-budget chapter PDF | cached | n/a | n/a | no separate supplement found | no | PDF figures cached | PDF table-level entropy budget, not extracted | no code repo found | PDF cached under [Lineweaver entropy-budget asset](../../../assets/lineweaver_entropy_budget/README.md) |

Asset-state and extraction-potential classification:

| External hit | Asset state | Extraction potential | Follow-up product-recovery task |
| --- | --- | --- | --- |
| Farrah 2023 | `asset_extracted_not_digitized`; `inspected_no_numerical_product` | `figure_digitization_possible`; `source_tex_parse_possible` | Low-fidelity search text exists; targeted manual extraction or source-TeX parsing required before numerical reuse. |
| Croker 2024 | `asset_extracted_not_digitized` | `direct_table`; `figure_digitization_possible`; `source_tex_parse_possible` | Low-fidelity search text exists; table extraction or figure digitization only if DESI CCBH comparison is reused. |
| Lacy 2024 | `asset_extracted_not_digitized`; `inspected_no_numerical_product` | `direct_table`; `figure_digitization_possible`; `source_tex_parse_possible` | Low-fidelity search text exists; figure/table extraction only if accretion-history constraints are reused numerically. |
| Amendola 2024 | `asset_extracted_not_digitized` | `code_reproduction_possible`; `direct_table`; `figure_digitization_possible`; `source_tex_parse_possible` | Low-fidelity search text exists; clone/run GitHub repos only if CCBH constraint reproduction is needed. |
| GWTC-3 population Zenodo | `asset_extracted_not_digitized` | `zenodo_data_available`; `direct_table`; `code_reproduction_possible`; `figure_digitization_possible` | Large analysis tarballs remain available but not downloaded. |
| GWTC-3 parameter-estimation Zenodo | `asset_cached`; `asset_available_not_downloaded` for HDF5 products | `zenodo_data_available`; `code_reproduction_possible` | Download selected HDF5/contour products only if event-level PE samples become necessary. |
| GWTC-4.0 population Zenodo | `asset_extracted_not_digitized` | `zenodo_data_available`; `direct_table`; `code_reproduction_possible`; `figure_digitization_possible` | Large `analyses_*` tarballs remain available but not downloaded. |
| Chen, Jani, and Kephart 2026 | `asset_extracted_not_digitized`; `inspected_no_numerical_product` | `direct_table`; `figure_digitization_possible`; `source_tex_parse_possible` | Low-fidelity search text exists; figure/table digitization before entropy-history classification. |
| Lineweaver entropy-budget chapter | `asset_extracted_not_digitized` | `direct_table`; `figure_digitization_possible` | Low-fidelity search text exists; table extraction still required before numerical use. |

## Lane A Search Trace

| Search axis | Query keywords used | Source found | Source status | Product status | Cache action | Reason for inclusion or rejection |
| --- | --- | --- | --- | --- | --- | --- |
| SMBH mass density evolution | `SMBH mass density evolution public data table rho_BH redshift`; `Lacy 2024 SMBH accretion history cosmological coupling data code` | [Lacy 2024](../../../literature/lacy_2024_smbh_accretion_coupling_constraints.md), Farrah 2023, Croker 2024 | already_cached plus asset cache created | figure/table-level assets cached and extracted | reused_existing_cache; created_asset_cache; inspected_no_numerical_product for Farrah/Lacy | Literature hit and figure/table-level constraint hit, but no public `rho_BH(a)` table with uncertainty and normalization route was found. Product hit / QFUDS-ready product not found. |
| Black-hole mass function evolution | `black hole mass function evolution public data table redshift SMBH`; `evolution black hole mass function with redshift public data` | A&A 2024 binary-black-hole population evolution result surfaced externally; LVK population products surfaced through GWTC releases | externally_found_and_cached for LVK manifests/assets | downloadable_data_available; selected table/figure assets cached | created_asset_cache; asset_extracted_not_digitized for selected LVK products | LVK population products are real downloadable products, but they are merger-population distributions, not a cosmic SMBH `rho_BH(a)` or BHMF-to-density history. Product hit / QFUDS-ready product not found. |
| Accretion history reconstructions | `supermassive black hole accretion history constraints cosmological coupling data code`; `arXiv 2312.12344 code data` | [Lacy 2024](../../../literature/lacy_2024_smbh_accretion_coupling_constraints.md) | already_cached plus asset cache created | figure/table-level assets cached and extracted | reused_existing_cache; created_asset_cache; inspected_no_numerical_product | Accretion-history constraints and arXiv assets exist. A public code repository, chains, or machine-readable accretion-history product was not found in this pass. Literature hit / QFUDS-ready product not found. |
| Black-hole growth histories | `Farrah 2023 cosmological coupling black holes data repository`; `Croker 2024 DESI cosmologically coupled black holes code data repository` | [Farrah 2023](../../../literature/farrah_2023_cosmological_coupling_black_holes.md), [Croker 2024](../../../literature/croker_2024_desi_coupled_black_holes.md) | already_cached plus asset cache created | figure/source assets cached and extracted | reused_existing_cache; created_asset_cache; asset_extracted_not_digitized | Both papers define adjacent CCBH growth/source histories and expose paper/source assets, but no public reusable numeric source-history product was found. Product hit / QFUDS-ready product not found. |
| Merger-driven growth products | `GWTC-3 population data release Zenodo figure data population samples`; `GWTC-4.0 population properties data release` | [Abbott 2023 GWTC-3 population record](../../../literature/abbott_2023_gwtc3_population_merging_compact_binaries.md), GWTC-3 Zenodo, GWTC-4 Zenodo | already_cached and externally_found_and_cached | downloadable_data_available; selected table/figure/event-list assets cached | reused_existing_cache; created_asset_cache; asset_extracted_not_digitized | LVK products are reproducible merger-population products. They can support merger-rate or mass-distribution checks, but not by themselves `rho_BH(a)` or `d rho_BH/dln(a)` with QFUDS normalization. Reproducibility hit / QFUDS-ready product not found. |

## Lane B Search Trace

| Search axis | Query keywords used | Source found | Source status | Product status | Cache action | Reason for inclusion or rejection |
| --- | --- | --- | --- | --- | --- | --- |
| Black-hole entropy inventories | `black hole entropy inventory cosmic entropy budget public data table`; `cosmic entropy budget black holes entropy table Egan Lineweaver data` | Lineweaver entropy-budget chapter; Chen, Jani, and Kephart 2026 arXiv page | externally_found_and_cached | table_available; Lineweaver table not extracted; Chen source extracted | created_asset_cache; asset_downloaded_not_extracted for Lineweaver; asset_extracted_not_digitized for Chen | Present-day inventory tables and entropy-history paper assets exist, but no accepted `S_BH(a)` product with provenance, uncertainty, and normalization route was recovered. Data-product hit / QFUDS-ready product not found. |
| Cosmic entropy budgets | `cosmic entropy budget black holes entropy table Egan Lineweaver data`; `Cosmological Budget of Entropy from Merging Black Holes` | Lineweaver entropy-budget chapter; Chen, Jani, and Kephart 2026 arXiv page | externally_found_and_cached | figure/table/source assets cached | created_asset_cache; asset_extracted_not_digitized; inspected_no_numerical_product for Chen source tree | Literature and figure/table products exist. The 2026 preprint gives redshift-shaped merger entropy figures and equations, but no standalone numerical product or QFUDS conversion law was found. Product hit / QFUDS-ready product not found. |
| SMBH entropy evolution | `supermassive black hole entropy evolution redshift data product`; `SMBH entropy evolution cosmic history` | Lineweaver present-day entropy discussion; no direct SMBH entropy evolution product found | externally_found_and_cached | PDF table asset cached; no evolution asset found | created_asset_cache; asset_downloaded_not_extracted | SMBHs dominate present entropy budgets. A present-day PDF table asset exists, but no `S_SMBH(a)` or `dS_SMBH/dln(a)` evolution product was recovered. |
| Remnant entropy accounting | `black hole remnants entropy accounting data`; cached remnant comparator records | [Rovelli 2018](../../../literature/rovelli_2018_white_hole_dark_matter.md), [Barrau 2021](../../../literature/barrau_2021_white_hole_remnant_constraints.md), [Rovelli 2024](../../../literature/rovelli_2024_planck_star_remnant_review.md), Chen, Jani, and Kephart 2026 | already_cached and externally_found_and_cached for Chen | Chen figure/source assets cached; cached remnant records not productized | reused_existing_cache; created_asset_cache for Chen | Remnant and merger-entropy literature exists. The cached remnant records do not expose a cosmic entropy-history data product; Chen source is cached but remains not QFUDS-ready. |
| Entropy history reconstructions | `black hole entropy history reconstruction cosmic black hole mass function`; `merger generated entropy redshift history data` | Chen, Jani, and Kephart 2026 arXiv page | externally_found_and_cached | reconstructable_from_paper_assets; source figures cached | created_asset_cache; asset_extracted_not_digitized; inspected_no_numerical_product | The paper provides equations and redshift-history figures for merger-generated entropy. It may be reconstructable from the paper plus LVK products, but is not yet QFUDS-usable. Reproducibility not attempted / QFUDS-ready product not found. |

## Candidate Product Evaluation Matrix

| Candidate | Lane | Literature source | Public data availability | Reproducible? | Units | Redshift coverage | Uncertainty | Update frequency | Can define `X`? | Could eventually support `Q^nu`? | Classification | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CCBH SMBH mass-growth evidence | A | Farrah 2023 | Paper PDF/source cached and extracted; no public repository found | No | BH mass and density language in paper; no reusable `rho_BH(a)` product | `0 < z ~= 2.5` growth test; implication discussed to `z <~ 7` | Paper-level confidence, not reusable covariance product | Static paper | Partial source concept only | No; lacks QFUDS transfer equation, frame, and perturbation route | `data_product_exists` | Product hit / QFUDS-ready product not found. Strong comparator, not QFUDS source evidence. |
| DESI-era CCBH dark-energy source history | A | Croker 2024 | Paper PDF/HTML/source cached and extracted; paper figures/tables available | No | DE density and baryon-conversion parameters in paper, not QFUDS `rho_BH(a)` | DESI late-time BAO range | Paper-level parameter constraints, not reusable chain product found | Static paper | Partial source concept only | No; would reduce toward CCBH without distinct QFUDS equation | `data_product_exists` | Product hit / QFUDS-ready product not found. Strong known-model reduction pressure. |
| SMBH accretion-history coupling constraint | A | Lacy 2024 | Paper PDF/HTML/source cached and extracted | No | SMBH mass density and accreted AGN mass constraints | Accretion-history comparison to `z ~= 6` | Paper-level bounds on `k` | Static paper | Constraint only; not source `X` | No; constrains CCBH-like assumptions | `data_product_exists` | Useful constraint, not a source-history product. |
| CCBH LVK constraint code route | A | Amendola 2024 | Paper PDF/HTML/source cached and extracted; GitHub metadata/README snapshots cached; LVK products public | Partially | Coupling index and LVK mass/redshift population variables | LVK population range, not cosmic `rho_BH(a)` | Reproducible only after code/data setup | Static code unless repositories change | No; constraint route only | No; tests CCBH-like `k`, not QFUDS `Q^nu` | `reproducible_data_product_exists` | Reproducibility hit / QFUDS-ready product not found. |
| GWTC-3 compact-binary population release | A | Abbott 2023; Zenodo 11254021 | Manifest, READMEs, table-data tarball, and paper-figure tarball cached; large analyses not downloaded | Yes for selected LVK table/figure products | Merger population, mass, spin, redshift variables | Detector-limited compact-binary population | Population products and uncertainties available in release | Static release, v3 as checked | Can define merger-rate or mass-distribution proxy, not `rho_BH(a)` | No; no phase transfer or phase-B pressure law | `reproducible_data_product_exists` | Strong product hit, but wrong quantity for QFUDS admission. |
| GWTC-4.0 compact-binary population release | A | LVK 2025 Zenodo 16911563 | Manifest, README, event list, figures, figure scripts, and tutorial cached; large analyses not downloaded | Yes for selected LVK event/figure products | Merger population, mass, spin, redshift variables | O4a/GWTC-4 population scope | Population products expose model uncertainty | Static release, v1 as checked | Can define updated merger-population proxy, not `rho_BH(a)` | No; no QFUDS transfer law | `reproducible_data_product_exists` | Externally found product; selected assets now cached. |
| Present-day cosmic black-hole entropy inventory | B | Lineweaver entropy-budget chapter | PDF cached; table not extracted | Partially from paper after extraction | Entropy in `k` units | Present-day only | Literature-level estimates | Static chapter | Defines present entropy inventory only | No; no entropy-to-energy conversion law | `data_product_exists` | Data-product hit / QFUDS-ready product not found. |
| Merger-generated black-hole entropy history | B | Chen, Jani, and Kephart 2026 | ArXiv PDF/HTML/source cached and extracted; figures and equations available; no standalone numeric product found | Reconstructable from paper plus LVK inputs, not directly reproduced here | Entropy and entropy density | Redshift-history figures and equations, including merger history | Uses LVK population uncertainty assumptions | Static preprint as checked | Partial for merger entropy, not total `S_BH(a)` | No; no QFUDS conversion law, frame, or `delta Q` route | `data_product_exists` | Best Lane B hit, but still QFUDS-ready product not found. |
| Remnant/white-hole entropy accounting | B | Rovelli 2018; Barrau 2021; Rovelli 2024 | Literature records only in current cache | No | Remnant/Planck-star concepts, not productized entropy history | Not a redshift product | No product uncertainty | Static papers/reviews | No | No | `literature_only` | Literature hit / QFUDS-ready product not found in cached remnant records. |

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

## QFUDS-Ready Products Not Found

As of this 2026-06-10 audit, within the sources checked here:

- no public QFUDS-ready `rho_BH(a)` table was found;
- no public QFUDS-ready `d rho_BH / dln(a)` table was found;
- no public QFUDS-ready `S_BH(a)` table was found;
- no public QFUDS-ready `dS_BH / dln(a)` table was found;
- no source supplied a non-circular normalization route into QFUDS;
- no source supplied `Q^nu`;
- no source supplied a `delta Q` route;
- no source supplied a known-model distinction for QFUDS.

This is a dated "not found" statement for QFUDS-ready products in the checked
sources only. It does not say that source assets are unavailable. The asset
availability check above records multiple PDFs, arXiv source bundles, Zenodo
assets, table/figure assets, and code repositories that were available but not
downloaded or extracted in this audit.

It also does not imply exhaustive literature coverage.

## Remaining Product-Recovery Tasks

These are recovery tasks, not Level 2B openings and not QFUDS support claims:

1. If GWTC-4.0 is used quantitatively, select and download only the needed
   large `analyses_*` population tarball rather than all release products.
2. If GWTC-3 event-level posterior samples are needed, select the needed HDF5
   or contour files from the cached Zenodo manifest before download.
3. If Amendola 2024 constraints must be reproduced, clone/run the two GitHub
   repositories and record exact LVK inputs.
4. If Lineweaver is used numerically, use the MarkItDown output only for rough
   navigation, then manually extract the entropy table values with units into a
   digitized product from the PDF.
5. If Chen 2026 is used for a redshift entropy history, digitize or extract the
   relevant figure/table products and document the uncertainty route.

## Post-Cache Development Readiness

After the 2026-06-11 asset-cache and paper-parse cleanup, Source-X can be
developed further, but only at the product-recovery and equation-extraction
layer.

The information gap changed from:

```text
papers/products may be missing
```

to:

```text
papers and selected products are cached; QFUDS-usable structured products are
still missing
```

That makes these follow-ups admissible:

1. Extract a structured `rho_BH(a)` or `d rho_BH / dln(a)` candidate from the
   cached CCBH/LVK/Lacy/Amendola materials, with units, redshift coverage,
   uncertainty route, and provenance.
2. Extract a structured `S_BH(a)` or `dS_BH / dln(a)` candidate from
   Chen 2026 or Lineweaver, with units, redshift coverage, uncertainty route,
   and provenance.
3. Search the cached source text for an explicit entropy-to-energy or
   mass-growth-to-transfer equation. If none exists, record the absence as a
   failed derivation precondition rather than filling it with a fitted
   `Gamma(a)`.
4. Only after a candidate `X` product exists, attempt the Phase 4 `delta Q`
   derivation or record why it fails.

These follow-ups still do not open Level 2B. A cached paper, full-text parse,
figure, table, or source bundle is not a QFUDS-ready source product until it is
manually structured or numerically digitized with provenance and uncertainty.

## Markdown Conversion Outputs

MarkItDown PDF-to-Markdown conversions were created for cached paper PDFs as
low-fidelity search text:

- [Farrah 2023 Markdown](../../../assets/farrah_2023_cosmological_coupling_black_holes/digitization/paper_arxiv_2302.07878.md)
- [Croker 2024 Markdown](../../../assets/croker_2024_desi_coupled_black_holes/digitization/paper_arxiv_2405.12282.md)
- [Lacy 2024 Markdown](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/digitization/paper_arxiv_2312.12344.md)
- [Amendola 2024 Markdown](../../../assets/amendola_2024_gw_constraints_ccbh/digitization/paper_arxiv_2307.02474.md)
- [Chen 2026 Markdown](../../../assets/chen_2026_merger_entropy_budget/digitization/paper_arxiv_2601.13621.md)
- [Lineweaver entropy-budget Markdown](../../../assets/lineweaver_entropy_budget/digitization/chapter22_lineweaver.md)

These conversions are not faithful paper transcriptions. They are expected to
damage two-column flow, equations, tables, captions, signs, and spacing. Use
them only for rough keyword, section, and citation search. They do not
constitute numerical digitization, table extraction, equation provenance, or
QFUDS-ready evidence.

Figure/image-link check: the MarkItDown text was regenerated with a local figure
reference section appended for each paper asset that exposes extracted figures.
Each generated image link points to `../figures/extracted/...`; each source link
points back to `../source/extracted/...`. The Lineweaver PDF has no local
extracted figure assets in this cache.

## Cache Actions

No new literature cache records were created.

New raw asset and Markdown-conversion records were created under
paper/release-level directories in `docs/wiki/research/assets/`.

Selected assets were downloaded and extracted. Large LVK/GWTC analysis products
were not bulk-downloaded; their Zenodo manifests were cached and selected small
table/figure/event-list assets were recovered where useful.

Existing cache records reused:

- [Farrah 2023](../../../literature/farrah_2023_cosmological_coupling_black_holes.md)
- [Croker 2024](../../../literature/croker_2024_desi_coupled_black_holes.md)
- [Lacy 2024](../../../literature/lacy_2024_smbh_accretion_coupling_constraints.md)
- [Amendola 2024](../../../literature/amendola_2024_gw_constraints_ccbh.md)
- [Abbott 2023 GWTC-3 population](../../../literature/abbott_2023_gwtc3_population_merging_compact_binaries.md)
- [Rovelli 2018](../../../literature/rovelli_2018_white_hole_dark_matter.md)
- [Barrau 2021](../../../literature/barrau_2021_white_hole_remnant_constraints.md)
- [Rovelli 2024](../../../literature/rovelli_2024_planck_star_remnant_review.md)

External product hits with remaining product-recovery work:

- GWTC-4.0 population data release: selected assets cached/extracted; large
  `analyses_*` tarballs not downloaded.
- Chen, Jani, and Kephart 2026 entropy-budget preprint: PDF/HTML/source
  cached/extracted and Markdown-converted; numerical history still not
  digitized or classified.
- Lineweaver entropy-budget chapter: PDF cached and Markdown-converted; table
  extraction still required.

New asset records:

- [Farrah 2023 assets](../../../assets/farrah_2023_cosmological_coupling_black_holes/README.md)
- [Croker 2024 assets](../../../assets/croker_2024_desi_coupled_black_holes/README.md)
- [Lacy 2024 assets](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/README.md)
- [Amendola 2024 assets](../../../assets/amendola_2024_gw_constraints_ccbh/README.md)
- [Chen 2026 assets](../../../assets/chen_2026_merger_entropy_budget/README.md)
- [Lineweaver entropy-budget asset](../../../assets/lineweaver_entropy_budget/README.md)
- [GWTC-3 population assets](../../../assets/abbott_2023_gwtc3_population_merging_compact_binaries/README.md)
- [GWTC-3 parameter-estimation manifest](../../../assets/gwtc3_parameter_estimation_release/README.md)
- [GWTC-4.0 population assets](../../../assets/gwtc4_population_release/README.md)

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
