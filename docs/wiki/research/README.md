---
doc_id: research_cache_index
title: Research Cache
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on: []
next_gate: none; reference cache only
last_updated: 2026-06-09
---

# Research Cache

This directory stores reusable research reference material. It is not an
experiment record, result record, decision log, or roadmap.

The cache separates three categories:

- literature records: stable facts from papers;
- availability audits: dated search and data-product checks;
- research conclusions: experiment, result, decision, and roadmap documents only.

Cached records must reduce repeated paper rereading without creating hidden
QFUDS conclusions.

## Directory Layout

```text
docs/research/
  literature/
  audits/
  assets/
    figures/
    digitization/
```

## Local Indexes

- [Literature Cache](literature/README.md)
- [Availability Audits](audits/README.md)

## Rules

Literature records may store bibliographic metadata, paper-defined equations,
coupling definitions, datasets, redshift coverage, available products,
digitization requirements, and narrow QFUDS relevance.

Availability audits may store what was searched, where it was searched, what
was found, what was not found, and when the check happened.

Neither record type may store QFUDS conclusions, roadmap status, experiment
classifications, or GPT opinions as facts.
