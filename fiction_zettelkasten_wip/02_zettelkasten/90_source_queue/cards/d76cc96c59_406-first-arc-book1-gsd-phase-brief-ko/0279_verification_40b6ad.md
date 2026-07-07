---
doc_id: srcidx_40b6ad4bc49be144
title: "Source Index - Verification"
doc_type: reference
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_first_arc_book1_gsd_phase_brief_ko
next_gate: distill this source-index card into an atomic permanent zettel, or mark it source-only
last_updated: 2026-07-07
---

# Source Index - Verification

```text
fiction/provenance only
research evidence: no
canon action: none
layer: source index (not a permanent zettel)
processing_state: queued
```

## Source

- Source document: [QFUDS SAGA 1부 Book 1 GSD Phase Brief](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/406_first_arc_book1_gsd_phase_brief_ko.md)
- Source path: [docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/406_first_arc_book1_gsd_phase_brief_ko.md](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/406_first_arc_book1_gsd_phase_brief_ko.md)
- Source line: [line 279](../../../../../docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/00_workroom/406_first_arc_book1_gsd_phase_brief_ko.md)
- Heading level: `H2`
- Source heading: `Verification`

## Parent Context

- H1: QFUDS SAGA 1부 Book 1 GSD Phase Brief

## Captured Source

> Run before commit:
>
> ```bash
> python3 scripts/fiction_gate.py
> python3 scripts/validate_docs.py
> python3 scripts/research_consistency.py
> python3 scripts/agent_workflow_guard.py --staged
> git diff --check
> make preflight
> sh scripts/git-hooks/pre-commit
> ```

## Processing Contract

This is a generated source-index card, not a permanent zettel.

To distill it:

1. Reopen the source document for the full context.
2. Extract one atomic claim, rule, tension, or open question.
3. Mark canon state explicitly as `canon`, `candidate`, `soft_canon`, `archive`, or `unknown`.
4. Link the distilled zettel back to this card and to related zettels.
5. If the source heading is only navigation or boilerplate, mark it `source-only` instead of inventing a note.
