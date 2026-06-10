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
- research audits: dated plans, feasibility checks, availability checks, and
  data-product audits;
- research conclusions: experiment, result, decision, and roadmap documents only.

Cached records must reduce repeated paper rereading without creating hidden
QFUDS conclusions.

## Directory Layout

```text
docs/wiki/research/
  literature/
  audits/
  assets/
    figures/
    digitization/
```

## Local Indexes

- [Literature Cache](literature/README.md)
- [Research Audits](audits/README.md)
- [IV/IDE Timing Korean Synthesis](2026-06-09_iv_ide_timing_synthesis_ko.md)

## Rules

Literature records may store bibliographic metadata, paper-defined equations,
coupling definitions, datasets, redshift coverage, available products,
digitization requirements, and narrow QFUDS relevance.

Research audits may store what was searched, where it was searched, what was
found, what was not found, what audit was planned, and when the check happened.

Neither record type may store QFUDS conclusions, roadmap status, experiment
classifications, or GPT opinions as facts.
