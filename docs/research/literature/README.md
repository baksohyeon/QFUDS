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
