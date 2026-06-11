# Research Investigation Result Routing Workflow

Use this workflow whenever a research investigation creates, changes, judges, or
routes an asset-level product under `docs/wiki/research/`.

This workflow is the operational SSOT for separating research plans, asset
products, provenance, and result closeouts. It is process-only: it does not
change roadmap status, open Level 2B, or turn a literature/product overlap into
QFUDS support.

Workflow index: [QFUDS Agent Workflows](README.md).

Related SSOT:
[Research Asset and Product Workflow](research-asset-product-workflow.md).

## Core Rule

Do not leave product interpretation only inside `assets/`.

If a task creates or materially changes a derived asset product, such as a
manual extraction, digitized CSV, structured table, or provenance note, the
matching investigation chain must have a conclusion closeout that states what
the product changed and what remains blocked.

## Folder Roles

Use these destinations:

| Destination | Use for | Do not use for |
| --- | --- | --- |
| `docs/wiki/research/literature/` | reusable paper/reference summaries | execution plans, derived products, project status |
| `docs/wiki/research/assets/<paper_or_release_key>/source/` | source PDFs, TeX/source bundles, archives, raw downloads | audit conclusions |
| `docs/wiki/research/assets/<paper_or_release_key>/figures/` | extracted or rendered figure assets | digitized CSVs |
| `docs/wiki/research/assets/<paper_or_release_key>/digitization/` | Markdown conversions, manual extracts, digitized CSV/JSON, asset provenance | Source-X decision closeouts |
| `docs/wiki/research/investigations/<chain>/plans/` | candidate selection, execution plans, digitization plans, prompt/scope records | result claims |
| `docs/wiki/research/investigations/<chain>/conclusions/` | result closeouts, decision summaries, blocker judgments | raw assets or numeric tables |
| `docs/wiki/research/investigations/<chain>/coverage/` | search-breadth and coverage-expansion records | product files |

## When A Conclusion Closeout Is Required

Create or update a conclusion closeout when any of these occur:

- a `manual_structured_extract` is created;
- a `numeric_digitized` CSV/JSON is created;
- an asset product changes the product-state ladder;
- a product is judged insufficient for QFUDS use;
- a plan execution produces a failure record;
- a search or extraction result changes the investigation's next gate.

A plan-only task does not require a matching conclusion. A conclusion is needed
only after an execution, extraction, digitization, failure, or judgment occurs.

## Required Closeout Content

Every result closeout must state:

- created asset product paths;
- modified manifest/index paths;
- method used;
- quality state reached;
- recovered quantities;
- missing fields;
- whether uncertainty, units, redshift coverage, normalization, and provenance
  are sufficient;
- whether candidate `X` exists;
- whether `Q^nu`, `delta Q`, roadmap status, Level 2B, or QFUDS support changed.

If the answer is no, say no directly.

## Status Boundaries

Asset product states are not physical-admission states.

Use:

- `manual_structured_extract` for curated source values or structures;
- `numeric_digitized` for digitized points with method, units, axis mapping, and
  provenance;
- `data_product_blocked` when a product still lacks the fields needed for the
  investigation's physical route;
- `qfuds_usable_numeric_product` only if all required source-product fields and
  investigation admission boundaries are actually satisfied.

Do not use a digitized curve to claim:

- QFUDS support;
- candidate `X`;
- `Q^nu`;
- `delta Q`;
- Level 2B admission;
- roadmap advancement.

## Index Updates

When adding a plan or conclusion, update the local investigation read order and
the relevant `plans/README.md` or `conclusions/README.md`.

When adding an asset product, update the asset's `digitization/README.md`.

Do not update unrelated README files for appearance or completeness.

## Verification

Run:

```bash
rtk python3 scripts/validate_docs.py
rtk python3 scripts/research_consistency.py
rtk git diff --check
rtk git status --short
```

Report validation results and status boundaries in the final response.
