# Wiki Maintenance Workflow

This file is the operational SSOT for maintaining the repository LLM wiki.

The pattern is:

- raw sources and cached assets live in `docs/wiki/research/assets/`;
- LLM-maintained wiki records live under `docs/wiki/`;
- workflow rules live only under `.agent/workflows/`;
- project status remains governed only by
  `docs/05_next_steps/000_roadmap.md`.

Do not duplicate this workflow inside `docs/wiki/`. Wiki pages may link back to
this file, but executable agent procedure belongs here.

## Layer Boundaries

| Layer | Path | Owner | Rule |
| --- | --- | --- | --- |
| Agent schema | `.agent/` | agents and user | Defines how agents operate. |
| Raw/cached sources | `docs/wiki/research/assets/` | user/agent cache | Preserve originals and derived inspection assets. |
| Wiki records | `docs/wiki/` | LLM-maintained | Store indexes, summaries, lineage, governance records, postmortems, and research cache records. |
| Status authority | `docs/05_next_steps/000_roadmap.md` | project process | Only source for current project status. |

## Required Wiki Files

- `docs/wiki/README.md`: human landing page for the wiki directory.
- `docs/wiki/index.md`: content-oriented catalog of wiki pages.

## Ingest Workflow

Use this when a new source, paper, asset, result, postmortem, or wiki page is
added.

1. Classify the item:
   - external source or raw asset;
   - literature record;
   - investigation record;
   - governance/gate record;
   - lineage/provenance record;
   - postmortem;
   - synthesis or index page.
2. Store files in the existing `docs/wiki/` structure. If the item touches an
   external product or downloadable asset, apply
   [Research Asset and Product Workflow](research-asset-product-workflow.md).
3. Update relevant wiki pages and cross-links.
4. Update `docs/wiki/index.md` with the page link and one-line role.
5. Run validation:

```text
rtk python3 scripts/validate_docs.py
rtk python3 scripts/research_consistency.py
rtk git diff --check
```

## Query Workflow

Use this when answering a question from the wiki.

1. Read `docs/wiki/index.md` first.
2. Drill into the linked pages needed for the answer.
3. If the answer creates a reusable synthesis, write it back into the proper
   wiki location and index it from `docs/wiki/index.md`.
4. Do not turn a query answer into roadmap status, QFUDS support, or Level 2B
   progress unless the project process explicitly updates the authoritative
   roadmap and evidence documents.

## Lint Workflow

Use this when asked to health-check the wiki.

Check for:

- stale links or renamed paths;
- orphan pages missing from `docs/wiki/index.md`;
- fiction pages still parked under `docs/wiki/lineage/` instead of
  `docs/wiki/fiction/` unless they are true idea-genealogy records;
- pages that duplicate operational workflow rules from `.agent/`;
- asset/product claims not backed by the research asset workflow;
- status claims outside the roadmap;
- investigation records that should be linked from the content index;
- raw assets stored outside the asset cache.

For substantive repairs, update the owning README/index, postmortem, or
research investigation. Routine maintenance history lives in git history.

## Indexing Rule

`docs/wiki/index.md` is content-oriented. Keep each entry short:

```text
- [Page Title](path/to/page.md) - one-line role.
```

Do not copy long summaries into the index. Link to the page that owns the
details.

## Change History Boundary

Do not create a parallel wiki maintenance log.

Use the existing owner for each kind of history:

- Routine file maintenance: git history.
- Process failures or lessons learned: `docs/wiki/postmortem/`.
- External literature/data/source investigations:
  `docs/wiki/research/investigations/`.
- Project status: `docs/05_next_steps/000_roadmap.md`.
- Project decisions: `docs/00_project/decision_log.md`.
