---
doc_id: literature_cache_index
title: Literature Cache
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - research_cache_index
next_gate: none; raw literature records only
last_updated: 2026-06-17
---

# Literature Cache

This folder stores stable paper facts used by QFUDS experiments and audits.

Each record should answer:

```text
What did the paper define, measure, reconstruct, publish, and make available?
```

It must not answer:

```text
What should QFUDS conclude from this?
```

## Naming

Use:

```text
<lead_author>_<year>_<short_topic>.md
```

Examples:

```text
escamilla_2023_interacting_dark_energy_kernel.md
goh_2023_tomographic_coupled_dark_energy.md
```

## Required Sections

```text
## Bibliographic Metadata
## Key Equations
## Coupling Definitions
## Datasets Used
## Redshift Coverage
## Available Products
## Digitization Requirements
## Public Code / Data Links
## QFUDS Relevance
## Use Restrictions
## Check History
```

## Evidence Levels

The `index.csv` `evidence_level` column is a routing label only:

- `primary`: direct target for an experiment or audit;
- `secondary`: adjacent proxy target;
- `optional`: relevant but not usable without stronger data products;
- `historical`: background precedent or older reconstruction family.

Use [index.csv](index.csv) to find individual literature records.

## Coverage Expansion Records

- [NASA LAMBDA Graphic History Cosmological Parameters](nasa_lambda_graphic_history_cosmological_parameters.md) -
  reference-only baseline-parameter coverage; routed through the
  [baseline reference chain](../investigations/baseline_reference/README.md).
- [Li 2025 DESI DR2 Sign-Reversal IDE](li_2025_desi_dr2_sign_reversal_ide.md)
- [Silva 2025 DESI DR2 IDE and S-IDE](silva_2025_desi_dr2_ide_s_ide.md)
- [You 2025 DESI DR2 Coupled Dark Sector](you_2025_desi_dr2_coupled_dark_sector.md)
- [Tsedrik 2025 BOSS DES Y3 Dark Scattering](tsedrik_2025_boss_des_y3_dark_scattering.md)
- [Figueruelo 2026 DESI DR2 Linear Nonlinear IDE](figueruelo_2026_desi_dr2_linear_nonlinear_ide.md)
- [Silva 2024 Nonlinear Matter Power IDE](silva_2024_nonlinear_matter_power_ide.md)

## Black-Hole-Coupled Source Records

- [Farrah 2023 Cosmological Coupling Black Holes](farrah_2023_cosmological_coupling_black_holes.md)
- [Croker 2024 DESI Coupled Black Holes](croker_2024_desi_coupled_black_holes.md)
- [Lei 2024 JWST Black Holes Dark Energy Test](lei_2024_jwst_black_holes_dark_energy_test.md)
- [Rodriguez 2023 NGC3201 Coupling Constraints](rodriguez_2023_ngc3201_coupling_constraints.md)
- [Andrae 2023 Gaia Coupling Constraints](andrae_2023_gaia_coupling_constraints.md)
- [Amendola 2024 GW Constraints CCBH](amendola_2024_gw_constraints_ccbh.md)
- [Cadoni 2023 Nonsingular Black Hole Coupling](cadoni_2023_nonsingular_black_hole_coupling.md)
- [Lacy 2024 SMBH Accretion Coupling Constraints](lacy_2024_smbh_accretion_coupling_constraints.md)
- [Parnovsky 2023 Black Holes Dark Energy Critique](parnovsky_2023_black_holes_dark_energy_critique.md)
- [Avelino 2023 Gravastar Dark Energy Critique](avelino_2023_gravastar_dark_energy_critique.md)
- [Mistele 2023 Coupling Dark Energy Comment](mistele_2023_coupling_dark_energy_comment.md)
- [Faraoni 2024 Black Hole Event Horizon Coupling](faraoni_2024_black_hole_event_horizon_coupling.md)
- [Afshordi 2010 Black Hole Entropy Dark Energy](afshordi_2010_black_hole_entropy_dark_energy.md)
- [Tsilioukas 2025 Topological Black Hole Dark Energy](tsilioukas_2025_topological_black_hole_dark_energy.md)
- [Rovelli 2018 White Hole Dark Matter](rovelli_2018_white_hole_dark_matter.md)
- [Barrau 2021 White Hole Remnant Constraints](barrau_2021_white_hole_remnant_constraints.md)
- [Rovelli 2024 Planck Star Remnant Review](rovelli_2024_planck_star_remnant_review.md)

## Structure-Era Activation Records

- [Buchert 2007 Dark Energy From Structure](buchert_2007_dark_energy_from_structure.md)
- [Paranjape 2008 Structure Backreaction Weak Fields](paranjape_2008_structure_backreaction_weak_fields.md)
- [Lapi 2025 Structure Emergent Dark Energy](lapi_2025_structure_emergent_dark_energy.md)
- [Parker 1999 Vacuum Metamorphosis](parker_1999_vacuum_metamorphosis.md)
- [Sola 2021 Running Vacuum Tensions](sola_2021_running_vacuum_tensions.md)
- [Li 2020 Phenomenological Emergent Dark Energy](li_2020_phenomenological_emergent_dark_energy.md)
- [Martins 2018 Late-Time DE Transitions](martins_2018_late_time_de_transitions.md)
- [Yang 2015 GP Dark-Sector Interaction](yang_2015_gp_dark_sector_interaction.md)
- [Mukherjee 2021 Nonparametric Dark-Sector Interaction](mukherjee_2021_nonparametric_dark_sector_interaction.md)
- [Abedin 2025 GP ANN Dark-Sector Interaction](abedin_2025_gp_ann_dark_sector_interaction.md)
- [Yang 2025 Variable Couplings DESI DR2](yang_2025_variable_couplings_desi_dr2.md)
- [Paliathanasis 2026 Late-Time Interacting Transition](paliathanasis_2026_late_time_interacting_transition.md)

## Compact-Object Transient Source Records

- [Madau 2014 Cosmic Star Formation History](madau_2014_cosmic_star_formation_history.md)
- [Horiuchi 2011 Cosmic Core-Collapse Supernova Rate](horiuchi_2011_cosmic_core_collapse_supernova_rate.md)
- [Strolger 2015 Core-Collapse Supernova Rate to Redshift 2.5](strolger_2015_core_collapse_supernova_rate_z2_5.md)
- [Kresse 2021 Stellar Collapse Diversity DSNB](kresse_2021_stellar_collapse_diversity_dsnb.md)
- [Sukhbold 2016 Core-Collapse Remnant Masses](sukhbold_2016_core_collapse_remnant_masses.md)
- [Abbott 2023 GWTC-3 Population Merging Compact Binaries](abbott_2023_gwtc3_population_merging_compact_binaries.md)
- [Abbott 2021 Isotropic Gravitational-Wave Background O3](abbott_2021_isotropic_gwb_o3.md)
- [Kasen 2017 Kilonova R-Process GW170817](kasen_2017_kilonova_r_process_gw170817.md)
