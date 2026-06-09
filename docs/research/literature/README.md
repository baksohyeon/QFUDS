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
last_updated: 2026-06-09
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

- [Li 2025 DESI DR2 Sign-Reversal IDE](li_2025_desi_dr2_sign_reversal_ide.md)
- [Silva 2025 DESI DR2 IDE and S-IDE](silva_2025_desi_dr2_ide_s_ide.md)
- [You 2025 DESI DR2 Coupled Dark Sector](you_2025_desi_dr2_coupled_dark_sector.md)
- [Tsedrik 2025 BOSS DES Y3 Dark Scattering](tsedrik_2025_boss_des_y3_dark_scattering.md)
- [Figueruelo 2026 DESI DR2 Linear Nonlinear IDE](figueruelo_2026_desi_dr2_linear_nonlinear_ide.md)
- [Silva 2024 Nonlinear Matter Power IDE](silva_2024_nonlinear_matter_power_ide.md)
