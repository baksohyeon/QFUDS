---
doc_id: audit_2026_06_10_compact_object_transient_source_literature
title: "2026-06-10 Compact-Object Transient Source Literature Audit"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_source_x_audit
  - audit_2026_06_10_black_hole_coupled_source_audit
  - audit_2026_06_10_structure_era_activation_literature
  - literature_cache_index
next_gate: no physical branch; compact-object transient source remains literature coverage only
last_updated: 2026-06-10
record_type: coverage_audit
audit_date: 2026-06-10
used_by:
  - source_x_audit
---

# 2026-06-10 Compact-Object Transient Source Literature Audit

## Purpose

This audit expands Source-X literature coverage into compact-object transient
source histories. It does not rely only on the existing repository cache: the
repository cache was checked first, then external literature searches were used
where coverage was insufficient.

A missing cache record is not a claim that the literature does not exist.

This audit does not:

- open Physical-QFUDS Level 2B;
- modify roadmap status;
- create a physical branch;
- claim support from timing overlap;
- treat compact-object production, merger rates, DSNB flux, or r-process
  production as QFUDS success.

External literature is only useful for physical admission if it supplies all of:

```text
X =
Q^nu =
why phase B has w ~= -1 =
delta Q route =
known-model distinction =
```

## Research Axes

Searched axes:

- core-collapse supernova rate;
- cosmic supernova rate redshift evolution;
- diffuse supernova neutrino background;
- neutron-star formation rate;
- black-hole formation rate;
- compact-object merger rate;
- binary black-hole merger rate;
- neutron-star merger rate;
- black-hole neutron-star merger rate;
- gravitational-wave background;
- kilonova / r-process production history;
- massive-star death and dark energy;
- structure-era compact-object production.

## Repository Cache State Before Expansion

The repository cache already contained black-hole-coupled dark-energy records
and DESI/IDE records, but it did not contain dedicated compact-object transient
source records for CCSN rates, DSNB, remnant formation, LVK compact-binary
population rates, stochastic gravitational-wave background limits, or
kilonova/r-process production.

Relevant already-cached adjacent records:

| Source | Classification | Use in this audit |
| --- | --- | --- |
| Farrah et al. 2023 / Croker et al. 2024 black-hole-coupled DE records | already cached | Adjacent black-hole-coupled comparator, not a compact-object transient rate source. |
| Amendola et al. 2024 GW constraints on cosmologically coupled BHs | already cached | Uses GW populations for a CCBH constraint; not cached as a general merger-rate product. |
| Lacy et al. 2024 SMBH accretion constraints | already cached | Accretion-history comparator, not a stellar compact-object transient source. |
| Sukhbold/Kresse/LVK/Madau/Strolger/Kasen records | not cached before this audit | Added below as compact-object transient source records. |

## Source Classification

| Source or search result | Search axis | Classification | Cache action / reason |
| --- | --- | --- | --- |
| Madau and Dickinson 2014, "Cosmic Star Formation History" | structure-era compact-object production | externally found and cached | [Madau 2014](../../../literature/madau_2014_cosmic_star_formation_history.md). SFRD is a parent source for massive-star death and delayed compact-object production. |
| Horiuchi et al. 2011, "The Cosmic Core-collapse Supernova Rate does not match the Massive-Star Formation Rate" | core-collapse supernova rate | externally found and cached | [Horiuchi 2011](../../../literature/horiuchi_2011_cosmic_core_collapse_supernova_rate.md). Useful for observed-vs-predicted CCSN and hidden/dark collapse caveat. |
| Strolger et al. 2015, CANDELS/CLASH CCSN rate to `z = 2.5` | cosmic supernova rate redshift evolution | externally found and cached | [Strolger 2015](../../../literature/strolger_2015_core_collapse_supernova_rate_z2_5.md). Direct binned CCSN rate source. |
| Kresse et al. 2021, "Stellar Collapse Diversity and the Diffuse Supernova Neutrino Background" | DSNB / BH-forming collapse | externally found and cached | [Kresse 2021](../../../literature/kresse_2021_stellar_collapse_diversity_dsnb.md). Connects successful and failed collapse diversity to DSNB. |
| Sukhbold et al. 2016, 9-120 solar-mass core-collapse remnant grid | neutron-star and black-hole formation rate | externally found and cached | [Sukhbold 2016](../../../literature/sukhbold_2016_core_collapse_remnant_masses.md). Provides remnant outcome map and supplementary archive. |
| LVK 2023, GWTC-3 population of merging compact binaries | compact-object merger rate / BBH / BNS / NSBH | externally found and cached | [Abbott 2023](../../../literature/abbott_2023_gwtc3_population_merging_compact_binaries.md). Primary public rate/posterior product source. |
| LVK 2021, isotropic gravitational-wave background O3 | gravitational-wave background | externally found and cached | [Abbott 2021](../../../literature/abbott_2021_isotropic_gwb_o3.md). Integrated background constraint comparator. |
| Kasen et al. 2017, GW170817 kilonova r-process origin | kilonova / r-process production history | externally found and cached | [Kasen 2017](../../../literature/kasen_2017_kilonova_r_process_gw170817.md). Event-level r-process yield comparator. |
| Dahlen et al. 2012, CCSN rate to `z ~ 1` | cosmic supernova rate redshift evolution | externally found but not cached | Relevant but not cached because Strolger 2015 extends the HST CCSN-rate lane to `z = 2.5` and cites prior HST work. |
| SDSS-II CCSN rate, `arXiv:1407.0999` | local CCSN rate | externally found but not cached | Relevant low-redshift rate point; not cached because this pass prioritized high-redshift and hidden-collapse coverage. |
| Ando et al. 2023 DSNB review, `arXiv:2306.16076` | DSNB review | externally found but not cached | Relevant review; not cached because Kresse 2021 gives a concrete collapse-diversity model for this audit. |
| DSNB with up-to-date star-formation rate, `arXiv:2310.15254` | DSNB / SFRD | externally found but not cached | Relevant; left for a later DSNB product audit to avoid duplicating Kresse/Madau roles. |
| DSNB extensive stellar population/binary effects, `arXiv:2506.22699` | DSNB / binary evolution | externally found but not cached | Relevant but newer and not cached in first compact-object pass; would be useful in a DSNB-specific follow-up. |
| Kuroda et al. 2021 core-collapse simulations | NS/BH formation | externally found but not cached | Relevant simulations; not cached because Sukhbold 2016 has a public supplementary progenitor/remnant archive. |
| GWTC-3 compact-binary catalog, `arXiv:2111.03606` | compact-object merger catalog | externally found but not cached | Relevant event catalog; not cached separately because the GWTC-3 population record and event posterior release cover the source-rate role. |
| GWTC-3 event posterior Zenodo 8177023 | compact-object merger product | externally found but not cached as standalone | Product link recorded inside [Abbott 2023](../../../literature/abbott_2023_gwtc3_population_merging_compact_binaries.md). |
| O1+O2+O3 search-sensitivity Zenodo records | compact-binary population product | externally found but not cached as standalone | Product-family link recorded through the LVK population cache; separate product audit would be needed for execution. |
| GWTC-4.0 / GWTC-5.0 population products | compact-object merger rate | externally found but not cached | Relevant newer population products; not cached because this pass used stable GWTC-3 records with public release and broad class coverage. |
| Fishbach 2026 low neutron-star merger rates | neutron-star merger rate / r-process | externally found but not cached | Relevant and current, but not cached because the audit first needed baseline GWTC-3 population plus GW170817 r-process records. |
| Binary neutron-star merger evolution and r-process enrichment, `arXiv:2605.20596` | r-process production history | externally found but not cached | Relevant but very recent; left for a dedicated r-process production-history audit. |
| Neutron-star mergers as dominant heavy r-process source, MNRAS 2024 | r-process production history | externally found but not cached | Relevant galactic chemical-evolution comparator; not cached in this first pass. |
| "massive-star death and dark energy" direct query | massive-star death and dark energy | no useful hit | Searches surfaced generic supernova/dark-energy pages, Type Ia supernova rate work, or non-primary public pages, not a useful compact-object source-to-DE mechanism. |
| "structure-era compact-object production" direct query | structure-era compact-object production | no useful hit for exact phrase | The exact phrase was not productive; useful results came from SFRD, CCSN, remnant, LVK, DSNB, and r-process terminology. |
| Wikipedia, Instagram, Facebook, general NASA photo pages, university overview pages | broad web results | irrelevant | Discovery/background only; not used as paper-fact evidence. |
| ProQuest thesis pages and some DOI/paywall-only pages | broad web results | inaccessible | Not used because primary arXiv, Zenodo, GWOSC, or journal-open pages were available for the cached records. |

## Useful Source Matrix

| Source | Source quantity | Redshift range / peak | Usable products | Helps define `X` | Helps define `Q^nu` | Helps explain `w ~= -1` | Helps define `delta Q` | Known-model reduction risk |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Madau and Dickinson 2014 | cosmic star-formation-rate density | broad cosmic history; peak `z ~ 1.9` reported by arXiv abstract | NED tables and review figures; no compact-object `X(a)` directly | yes, as parent SFRD proxy after conversion | no | no | no | high: ordinary SFRD or astrophysical source-history proxy |
| Horiuchi et al. 2011 | observed/predicted cosmic CCSN rate and hidden-collapse inference | low-to-intermediate redshift compilation; no single product found | paper/source only; likely digitization or literature table extraction | partial, for CCSN or hidden-collapse `X(z)` | no | no | no | high: ordinary CCSN/failed-collapse astrophysics |
| Strolger et al. 2015 | binned volumetric CCSN rate `R_CC(z)` | six bins over `0.1 < z < 2.5`; rate traced to `z ~ 2` | paper tables/figures; no separate chain found | yes, empirical CCSN `X(z)` candidate | no | no | no | high: observed transient rate, not dark-sector model |
| Kresse et al. 2021 | DSNB flux, failed-collapse fraction, BH-forming collapse contribution | cosmological DSNB integral; source history not separately public | paper tables/figures; no QFUDS-ready product found | partial, for failed-collapse or DSNB-weighted collapse source | no | no | no | high: neutrino-background / collapse astrophysics |
| Sukhbold et al. 2016 | progenitor-to-NS/BH outcome and remnant masses | no redshift; progenitors 9-120 solar masses | MPA supplementary archive; needs convolution with SFR/metallicity history | yes, as conversion map from massive stars to remnants | no | no | no | high: stellar-evolution/remnant model |
| LVK GWTC-3 population 2023 | BBH/BNS/NSBH merger-rate density and population parameters | detector-limited; BBH rate reported at fiducial `z = 0.2`; posterior products available | Zenodo figure/table data and population samples | yes, merger-rate `X(z)` candidate | no | no | no | high: ordinary compact-binary population / SGWB source model |
| LVK 2021 isotropic GWB O3 | `Omega_GW` upper limits and compact-binary background comparator | unresolved integrated cosmic source; joint constraints relevant at `z <~ 2` | paper/source and general GWOSC data; no `Omega_GW(z)` product found | partial, integrated background constraint only | no | no | no | high: gravitational-wave background constraint |
| Kasen et al. 2017 | kilonova ejecta mass/composition and r-process yield from GW170817 | single nearby event; no cosmic history | paper/source; no production-history table found | partial, if convolved with BNS/NSBH merger rates | no | no | no | high: nucleosynthesis / chemical enrichment |

## Gap Taxonomy

| Gap type | Finding |
| --- | --- |
| repository-cache gap | Present before this audit for CCSN rates, DSNB, neutron-star/black-hole remnant formation, LVK compact-binary population rates, stochastic GWB limits, and kilonova/r-process production. Reduced by the eight new cache records. |
| search-keyword gap | Present if the search stays on black-hole-coupled or dark-energy terminology. Useful literature appears under supernova-rate, DSNB, remnant-formation, GWTC population, stochastic GWB, kilonova, and r-process terms. |
| external-literature gap | Not a broad-field gap. External literature exists for compact-object transient production and merger histories. A narrower gap remains for any literature that directly turns these histories into a QFUDS dark-sector source. |
| actual evidence gap | Still present. No checked source supplies a QFUDS-specific `X`, covariant `Q^nu`, phase-B `w ~= -1` rationale, `delta Q` route, and known-model distinction together. |
| product/data gap | Mixed. LVK GWTC-3 has strong public products; Sukhbold has supplementary progenitor/remnant products; Madau has review tables. CCSN/DSNB/kilonova records still need digitization, table extraction, author data, or a dedicated product audit before curve-level use. None is QFUDS-ready. |

## Source-X Admission Check

Compact-object transient histories can help define candidate source scalars:

- `X_CCSN(z) = R_CC(z)`;
- `X_failed(z) = R_failed_collapse(z)`;
- `X_NS_form(z)` and `X_BH_form(z)` after convolving SFRD with a remnant-outcome
  map;
- `X_BBH(z)`, `X_BNS(z)`, and `X_NSBH(z)` from merger-rate posteriors;
- `X_GWB(f)` or an integrated `Omega_GW` constraint;
- `X_rprocess(z)` from merger-rate times ejecta yield.

These candidates are audit material only. Current evidence does not supply:

- a covariant transfer vector `Q^nu`;
- a reason compact-object production creates a smooth component with
  `w ~= -1`;
- a perturbation route for `delta Q`;
- a distinction from ordinary astrophysical source histories, compact-binary
  population synthesis, stochastic gravitational-wave background modeling, or
  chemical-enrichment models.

## Search Axis Outcomes

| Axis | Outcome |
| --- | --- |
| core-collapse supernova rate | useful sources found and cached: Horiuchi 2011, Strolger 2015 |
| cosmic supernova rate redshift evolution | useful source found and cached: Strolger 2015; additional Dahlen/SDSS sources found but not cached |
| diffuse supernova neutrino background | useful source found and cached: Kresse 2021; newer DSNB sources found but not cached |
| neutron-star formation rate | partial useful source cached: Sukhbold 2016 remnant map; no standalone cosmic NS-formation rate product found in this pass |
| black-hole formation rate | partial useful sources cached: Sukhbold 2016 and Kresse 2021; no standalone cosmic BH-formation-rate product found in this pass |
| compact-object merger rate | useful source found and cached: LVK GWTC-3 population |
| binary black-hole merger rate | useful source found and cached: LVK GWTC-3 population |
| neutron-star merger rate | useful source found and cached: LVK GWTC-3 population; Fishbach 2026 found but not cached |
| black-hole neutron-star merger rate | useful source found and cached: LVK GWTC-3 population |
| gravitational-wave background | useful source found and cached: LVK O3 isotropic GWB upper limits |
| kilonova / r-process production history | useful event-level source found and cached: Kasen 2017; production-history sources found but not cached |
| massive-star death and dark energy | no useful direct primary hit |
| structure-era compact-object production | useful indirect sources found and cached through SFRD, CCSN, remnant, and merger-rate terminology; exact phrase no useful hit |

## Unresolved Evidence Gaps

- no compact-object transient source has an admitted QFUDS `Q^nu`;
- no source explains why phase B should have smooth `w ~= -1`;
- no compact-object rate source defines `delta Q` or a stable perturbation
  prescription;
- no source distinguishes a QFUDS compact-object source from ordinary
  astrophysical rate histories, population synthesis, SGWB modeling, or
  chemical-enrichment models;
- no public product found for a ready-to-use QFUDS `X(a)` table with
  normalization, units, covariance, and sign convention;
- direct "massive-star death and dark energy" searches did not find a useful
  primary compact-object source-to-DE mechanism.

## Recommendation

Keep compact-object transient production as a literature-backed audit lane, not
a physical branch. A later executable audit should start with products, not
interpretation:

1. build or locate machine-readable `R_CC(z)`, `R_failed(z)`, `R_BBH(z)`,
   `R_BNS(z)`, and `R_NSBH(z)` histories;
2. define units and normalization before comparing to retained timing;
3. document whether each curve is observed, inferred, simulated, or convolved
   from another source;
4. run a reduction test against ordinary astrophysical source-history coupling;
5. reject physical admission unless `Q^nu`, `w ~= -1`, `delta Q`, and a
   known-model distinction are supplied.

## Repository Impact

- Roadmap unchanged.
- Level 2B remains blocked.
- No physical branch opened.
- Literature cache expanded with compact-object transient source records.
- Product/data gaps are recorded explicitly rather than converted into negative
  literature claims.
