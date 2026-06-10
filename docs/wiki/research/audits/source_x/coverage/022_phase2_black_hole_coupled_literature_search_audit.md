---
doc_id: audit_2026_06_10_black_hole_coupled_literature_search
title: "2026-06-10 Black-Hole-Coupled Literature Search Audit"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_black_hole_coupled_source_audit
  - audit_2026_06_10_structure_era_activation_literature
  - literature_cache_index
next_gate: no physical branch; literature cache added for reduction-test comparators only
last_updated: 2026-06-10
record_type: availability_audit
audit_date: 2026-06-10
used_by:
  - source_x_black_hole_coupled_source_audit
---

# 2026-06-10 Black-Hole-Coupled Literature Search Audit

## Audit Objective

Cache verified web literature for the black-hole-coupled source lane.

This is a research-cache audit only. It does not modify roadmap status, open
Physical-QFUDS Level 2B, create a black-hole physical branch, or treat any
black-hole-coupled dark-energy result as QFUDS success.

This search was black-hole-keyword-centered. It should not be read as a claim
that structure-era activation, backreaction, vacuum activation, emergent dark
energy, phase-transition dark energy, or nonparametric IDE literature does not
exist. The broader coverage expansion is recorded in
[2026-06-10 Structure-Era Activation Literature Audit](024_phase2_structure_era_activation_literature_audit.md).

## Search Targets

Searched for:

- cosmologically coupled black holes;
- black holes as a source of dark energy;
- black-hole mass growth with cosmological expansion;
- black-hole-coupled dark energy;
- astrophysical black holes and dark energy;
- black-hole mass growth and cosmological constant;
- black-hole entropy and dark energy;
- black-hole remnants dark matter;
- DESI dark-energy evolution from cosmologically coupled black holes;
- JWST, Gaia, globular-cluster, and gravitational-wave constraints on
  cosmologically coupled black holes;
- public code/data links where surfaced by source pages.

## Sources Checked

| Source | Query or URL | Result |
| --- | --- | --- |
| arXiv | `cosmologically coupled black holes dark energy Farrah 2023` | Found Farrah et al. 2023, the primary black-hole-as-dark-energy claim record. |
| arXiv | `DESI Dark Energy Time Evolution is Recovered by Cosmologically Coupled Black Holes` | Found Croker et al. 2024, a DESI-era coupled-black-hole dark-energy comparator. |
| arXiv | `Black holes as the source of dark energy JWST AGNs` | Found Lei et al. 2024, a high-redshift JWST constraint record. |
| arXiv | `Constraints on the Cosmological Coupling of Black Holes from the Globular Cluster NGC 3201` | Found Rodriguez 2023, an old-stellar-population constraint record. |
| arXiv | `Constraints on the cosmological coupling of black holes from Gaia` | Found Andrae and El-Badry 2023, a Gaia BH1/BH2 constraint record. |
| MNRAS / Oxford Academic | `Constraints on cosmologically coupled black holes from gravitational wave observations and minimal formation mass` | Found Amendola et al. 2024, an LVK gravitational-wave constraint record with public code links. |
| arXiv | `Cosmological coupling of nonsingular black holes` | Found Cadoni et al. 2023, a theoretical comparator favoring weaker `k = 1` scaling for regular black holes. |
| arXiv | `black-hole entropy dark energy cosmology` | Found Afshordi 2010 and Tsilioukas et al. 2025 as entropy/topology dark-energy comparators. |
| arXiv | `black hole remnants dark matter`, `white hole remnants dark matter`, `Planck mass black hole remnants as dark matter` | Found Rovelli and Vidotto 2018, Barrau et al. 2021, and Rovelli and Vidotto 2024 as remnant-DM comparators. |
| General web/news/search results | Space.com, DESI, UH, Imperial, Nature news, Astrobites, Reddit, Physics StackExchange, YouTube, Medium, Facebook | Classified below; popular summaries and discussion pages were not used as paper-fact evidence when primary papers were available. |

## Source Classification

| Source | Search lane | Classification | Cache action | Note |
| --- | --- | --- | --- | --- |
| Farrah et al. 2023, `arXiv:2302.07878` | CCBH / black holes as dark energy | already cached | [Farrah 2023](../../../literature/farrah_2023_cosmological_coupling_black_holes.md) | Primary black-hole-as-dark-energy claim. |
| Croker et al. 2024, `arXiv:2405.12282` | DESI / CCBH | already cached | [Croker 2024](../../../literature/croker_2024_desi_coupled_black_holes.md) | DESI-era CCBH comparator. |
| Lei et al. 2024, `arXiv:2305.03408` | JWST constraints | already cached | [Lei 2024](../../../literature/lei_2024_jwst_black_holes_dark_energy_test.md) | High-z AGN tension test. |
| Rodriguez 2023, `arXiv:2302.12386` | globular-cluster constraints | already cached | [Rodriguez 2023](../../../literature/rodriguez_2023_ngc3201_coupling_constraints.md) | Old stellar-mass BH constraint. |
| Andrae and El-Badry 2023, `arXiv:2305.01307` | Gaia constraints | already cached | [Andrae 2023](../../../literature/andrae_2023_gaia_coupling_constraints.md) | Gaia BH1/BH2 constraint. |
| Amendola et al. 2024, MNRAS | GW constraints | already cached | [Amendola 2024](../../../literature/amendola_2024_gw_constraints_ccbh.md) | LVK constraints and public code links. |
| Cadoni et al. 2023, `arXiv:2306.11588` | nonsingular BH coupling | already cached | [Cadoni 2023](../../../literature/cadoni_2023_nonsingular_black_hole_coupling.md) | Theoretical `k = 1` comparator. |
| Lacy et al. 2024, `arXiv:2312.12344` | SMBH accretion constraints | externally found and cached | [Lacy 2024](../../../literature/lacy_2024_smbh_accretion_coupling_constraints.md) | Accretion-history constraint on `k`. |
| Parnovsky 2023, `arXiv:2302.13333` | black holes as dark energy critique | externally found and cached | [Parnovsky 2023](../../../literature/parnovsky_2023_black_holes_dark_energy_critique.md) | Conceptual critique. |
| Avelino 2023, `arXiv:2303.06630` | gravastar / vacuum interior critique | externally found and cached | [Avelino 2023](../../../literature/avelino_2023_gravastar_dark_energy_critique.md) | Compact-object dark-energy critique. |
| Mistele 2023, `arXiv:2304.09817` | CCBH theoretical comment | externally found and cached | [Mistele 2023](../../../literature/mistele_2023_coupling_dark_energy_comment.md) | Theoretical critique of the dark-energy link. |
| Faraoni and Rinaldi 2024, `arXiv:2407.14549` | event-horizon coupling | externally found and cached | [Faraoni 2024](../../../literature/faraoni_2024_black_hole_event_horizon_coupling.md) | Theoretical BH/cosmology coupling comparator. |
| Afshordi 2010, `arXiv:1003.4811` | black-hole entropy and dark energy | externally found and cached | [Afshordi 2010](../../../literature/afshordi_2010_black_hole_entropy_dark_energy.md) | Entropy/vacuum-pressure comparator. |
| Tsilioukas et al. 2025, `arXiv:2412.21146` | BH formations/mergers and topological DE | externally found and cached | [Tsilioukas 2025](../../../literature/tsilioukas_2025_topological_black_hole_dark_energy.md) | Topological/entropy DE comparator. |
| Rovelli and Vidotto 2018, `arXiv:1804.04147` | white-hole remnants dark matter | externally found and cached | [Rovelli 2018](../../../literature/rovelli_2018_white_hole_dark_matter.md) | Remnant-DM comparator. |
| Barrau et al. 2021, `arXiv:2101.01949` | white-hole remnant constraints | externally found and cached | [Barrau 2021](../../../literature/barrau_2021_white_hole_remnant_constraints.md) | Remnant-DM constraint comparator. |
| Rovelli and Vidotto 2024, `arXiv:2407.09584` | Planck stars / remnants review | externally found and cached | [Rovelli 2024](../../../literature/rovelli_2024_planck_star_remnant_review.md) | Remnant-sector review. |
| Ghodla et al. 2023, Open Journal of Astrophysics | CCBH observational implications | externally found but not cached | none | Relevant; not cached because Amendola/Gaia/NGC3201/Lacy already cover constraint routing for this audit. |
| DESI/UH/Imperial/Michigan/Nature/Astrobites news pages | popular or institutional summaries | externally found but not cached | none | Useful discovery pointers; not used as paper-fact evidence where primary papers exist. |
| OpenReview CCBH/Hubble-tension page | preprint/forum record | externally found but not cached | none | Potentially relevant but lower priority than arXiv/journal sources in this pass. |
| APS DOI page for Faraoni and Rinaldi 2024 | event-horizon coupling | inaccessible | cached via arXiv instead | DOI page was found; arXiv page was accessible and used. |
| Space.com current black-hole mass/news pages | general SMBH/JWST news | irrelevant | none | Not about black holes as dark energy, CCBH, entropy source, or remnant DM. |
| Physics StackExchange / Reddit / YouTube / Medium / Facebook discussion pages | public discussion | irrelevant | none | Not primary research evidence for repository cache. |

## Cached Literature Records Added

| Record | Role |
| --- | --- |
| [Farrah 2023 Cosmological Coupling Black Holes](../../../literature/farrah_2023_cosmological_coupling_black_holes.md) | Primary adjacent black-hole-as-dark-energy claim. |
| [Croker 2024 DESI Coupled Black Holes](../../../literature/croker_2024_desi_coupled_black_holes.md) | DESI-era black-hole-production dark-energy comparator. |
| [Lei 2024 JWST Black Holes Dark Energy Test](../../../literature/lei_2024_jwst_black_holes_dark_energy_test.md) | High-redshift JWST constraint on strong coupling. |
| [Rodriguez 2023 NGC3201 Coupling Constraints](../../../literature/rodriguez_2023_ngc3201_coupling_constraints.md) | Globular-cluster constraint on strong coupling. |
| [Andrae 2023 Gaia Coupling Constraints](../../../literature/andrae_2023_gaia_coupling_constraints.md) | Gaia BH1/BH2 binary constraint on strong coupling. |
| [Amendola 2024 GW Constraints CCBH](../../../literature/amendola_2024_gw_constraints_ccbh.md) | LVK gravitational-wave population constraint with code links. |
| [Cadoni 2023 Nonsingular Black Hole Coupling](../../../literature/cadoni_2023_nonsingular_black_hole_coupling.md) | Theoretical comparator for weaker coupling and dark-energy-source viability. |
| [Lacy 2024 SMBH Accretion Coupling Constraints](../../../literature/lacy_2024_smbh_accretion_coupling_constraints.md) | SMBH accretion-history constraint on coupling index `k`. |
| [Parnovsky 2023 Black Holes Dark Energy Critique](../../../literature/parnovsky_2023_black_holes_dark_energy_critique.md) | Critique of black holes as a dark-energy source. |
| [Avelino 2023 Gravastar Dark Energy Critique](../../../literature/avelino_2023_gravastar_dark_energy_critique.md) | Gravastar/vacuum-interior compact-object critique. |
| [Mistele 2023 Coupling Dark Energy Comment](../../../literature/mistele_2023_coupling_dark_energy_comment.md) | Theoretical comment on the CCBH dark-energy link. |
| [Faraoni 2024 Black Hole Event Horizon Coupling](../../../literature/faraoni_2024_black_hole_event_horizon_coupling.md) | Event-horizon/cosmology coupling comparator. |
| [Afshordi 2010 Black Hole Entropy Dark Energy](../../../literature/afshordi_2010_black_hole_entropy_dark_energy.md) | Black-hole entropy/vacuum-pressure comparator. |
| [Tsilioukas 2025 Topological Black Hole Dark Energy](../../../literature/tsilioukas_2025_topological_black_hole_dark_energy.md) | Black-hole formation/merger topology dark-energy comparator. |
| [Rovelli 2018 White Hole Dark Matter](../../../literature/rovelli_2018_white_hole_dark_matter.md) | White-hole remnant dark-matter comparator. |
| [Barrau 2021 White Hole Remnant Constraints](../../../literature/barrau_2021_white_hole_remnant_constraints.md) | White-hole remnant constraint comparator. |
| [Rovelli 2024 Planck Star Remnant Review](../../../literature/rovelli_2024_planck_star_remnant_review.md) | Planck-star/white-hole remnant review. |

## Findings

The web search found a concrete adjacent literature family: cosmologically
coupled black holes as a possible dark-energy source. The strongest source
quantity is black-hole mass growth, often parameterized by an exponent `k` in a
mass-scale-factor relation. The dark-energy-source case is tied to strong
growth, especially `k ~= 3`, because that can make the physical black-hole
density behave like an effectively constant component.

The search also found multiple constraint or criticism routes: JWST high-z AGN
host comparisons, globular-cluster black-hole candidates, Gaia black-hole
binaries, LVK gravitational-wave mass distributions, and theoretical work
favoring weaker coupling for regular black holes.

## Products Found

| Product | Status |
| --- | --- |
| Paper metadata and abstracts | Found for all cached records. |
| Paper PDFs/HTML/source links | Found through arXiv or journal pages where applicable. |
| Public code | Found for Amendola et al. 2024 through journal-listed repositories. |
| Public posterior products, chains, covariance matrices, or source-history tables | Not found during this quick 2026-06-10 cache pass, except general public LVK products implied by the GW literature route. |

## QFUDS Boundary

The literature search changes the cache state, not the admission result.

The black-hole-coupled lane now has concrete known-model comparators and
constraints. It still does not supply the five QFUDS admission-rule items:

```text
X =
Q^nu =
why phase B has w ~= -1 =
delta Q route =
known-model distinction =
```

Current audit implication:

- black-hole mass growth is a sharper known-model comparator than the local-only
  audit could show;
- the reduction risk is stronger, because a black-hole-mass-growth QFUDS lane
  would need to distinguish itself from cosmologically coupled black-hole dark
  energy;
- black-hole entropy/topological dark-energy sources are external model-family
  comparators, not QFUDS phase-transfer evidence;
- white-hole/Planck remnants are routed to remnant-DM, not phase-B dark energy;
- no physical QFUDS branch is opened by this cache update.

## Products Not Found

No public product was found in this quick pass for a QFUDS-ready black-hole
source history:

- no QFUDS `X(a)` table;
- no QFUDS `Q^nu`;
- no phase-B stress-energy derivation;
- no `delta Q` perturbation prescription;
- no black-hole source history with QFUDS-specific normalization.

This is a dated "not found" statement for the checked sources only.

## Recommendation

Keep the black-hole-coupled lane as an audit lane. If it is revisited, start
from a reduction-test question:

```text
Does a proposed QFUDS black-hole source predict anything beyond
cosmologically coupled black-hole dark energy with a chosen mass-growth or
production history?
```

Do not open a physical branch unless the proposal supplies all five admission
items and a falsifiable distinction from the cached comparator family.

## Later Coverage Expansion Note

The later structure-era activation audit classifies this black-hole-lane result
as robust only within its dated scope. It weakens any broader global-negative
reading, redirects the next broad Source-X search toward structure-era
activation, and leaves physical admission unresolved because QFUDS-ready data
products and admission-rule items remain missing.
