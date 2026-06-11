---
doc_id: research_cache_index
title: Research Cache
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on: []
next_gate: none; reference cache only
last_updated: 2026-06-11
---

# Research Cache

This directory stores reusable research reference material. It is not an
experiment record, result record, decision log, or roadmap.

The cache separates reusable research records from QFUDS status documents.

Cached records must reduce repeated paper rereading without creating hidden
QFUDS conclusions.

Agent workflow rules for literature/product search, asset caching, extraction,
and digitization live in
[Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md).
This directory records research knowledge and cached artifacts; it is not the
agent workflow SSOT.

## Directory Layout

```text
docs/wiki/research/
  literature/
  investigations/
  assets/
    <paper_or_release_key>/
```

## Local Indexes

- [Literature Cache](literature/README.md)
- [Research Investigations](investigations/README.md)
- [Research Assets](assets/README.md)
- [IV/IDE Timing Korean Synthesis](2026-06-09_iv_ide_timing_synthesis_ko.md)

## Folder Roles

- `literature/`: one Markdown record per paper or stable external reference.
  Bibliographic metadata, source-defined equations, available products, redshift
  coverage, datasets, and narrow relevance notes.
- `investigations/`: dated research-process records. Use this for search plans,
  availability checks, feasibility checks, data-product audits, and audit-chain
  conclusions. Audit folders are process history, not asset storage.
- `assets/`: repository-cached external files and derived asset products,
  grouped by paper or release key.
- top-level one-off synthesis files, such as
  [IV/IDE Timing Korean Synthesis](2026-06-09_iv_ide_timing_synthesis_ko.md),
  are allowed only when they are research-cache summaries, not roadmap status or
  experiment results.

For operational rules, state names, and required asset handling, use the
[Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md).
