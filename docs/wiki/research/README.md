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

This directory stores reusable research reference material, investigation
process records, cached external assets, and derived asset products. It is not
an experiment record, result record, decision log, or roadmap.

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
- [IV/IDE Timing Korean Synthesis](investigations/exp006_timing/008_iv_ide_timing_synthesis_ko.md)

## Folder Roles

- `literature/`: one Markdown record per paper or stable external reference.
  Bibliographic metadata, source-defined equations, available products, redshift
  coverage, datasets, and narrow relevance notes.
- `investigations/`: dated research-process records. Use this for search plans,
  availability checks, feasibility checks, data-product audits, digitization
  execution plans, synthesis handoffs, and audit-chain conclusions. Audit
  folders are process history and result interpretation, not asset storage.
- `assets/`: repository-cached external files and derived asset products,
  grouped by paper or release key. Use this for PDFs, TeX/source bundles,
  rendered figures, Markdown conversions, manual extracts, digitized CSV/JSON,
  and asset-level provenance.
- one-off synthesis files belong under the investigation chain they summarize,
  not at the research-cache root.

## Result Routing Rule

Plans and result interpretations must stay in `investigations/`. Raw cached
assets and derived asset products must stay in `assets/`.

When an investigation task creates or materially changes an asset-level product
such as a `manual_structured_extract` or `numeric_digitized` CSV, the same
investigation chain must also have a `conclusions/` closeout that states:

- what product was created;
- what quality state was reached;
- what remains missing;
- whether the product changes the investigation decision;
- whether roadmap status, Level 2B, or QFUDS support changed.

Do not rely on an asset README, a CSV, or a provenance file alone as the
investigation result. Asset records preserve product provenance; conclusion
records preserve audit-chain decisions.

For operational rules, state names, and required asset handling, use the
[Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md).
For placement of plans, asset products, and result closeouts, use the
[Research Investigation Result Routing Workflow](../../../.agent/workflows/research-investigation-result-routing-workflow.md).
