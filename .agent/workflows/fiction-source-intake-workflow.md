# Fiction Source Intake Workflow

Use this workflow when a real-world article, paper, book note, video, repository,
interview, image, or dataset informs fiction but is not being admitted as QFUDS
research evidence.

## Boundary

Fiction sources live under `fiction/research/`. They do not enter
`docs/wiki/research/`, research results, the decision log, or the roadmap. If a
source will also support a QFUDS research claim, run the separate Research Asset and
Product Workflow for that use; do not promote the fiction record.

## States

- `provided_unchecked`: supplied by the user; claims not independently checked
- `hit_not_cached`: source page located; no local copy retained
- `asset_available_not_downloaded`: downloadable product identified but not fetched
- `asset_cached`: authorized asset stored under `fiction/research/assets/<source-id>/`
- `inspected`: relevant content inspected and use boundary recorded
- `inaccessible`: attempted but access was blocked
- `no_source_found`: a scoped search found no reliable source

Do not convert `provided_unchecked` into `inspected` by paraphrasing it.

## Intake Record

Every adopted source records source id, title, creator/publisher, URL, access date,
state, inspected scope, allowed factual anchor, blocked claim, fictional
extrapolation, affected Zettels/world/work, and license when an asset is copied.

## Storage

```text
fiction/research/README.md
fiction/research/sources/<source-id>.md
fiction/research/assets/<source-id>/
```

Links from Zettels and projects point to the source record. Preserve direct
quotations narrowly and distinguish them from paraphrase.

## Article / Brain-Dump Flow

1. Preserve the user's original input in `fiction/inbox/` with a source id.
2. Verify only the claims needed for the requested fiction decision.
3. Create or update the source record.
4. Distill reusable ideas into Zettels while linking raw capture and source.
5. Label unsupported future consequences as fictional extrapolation.
6. Do not promote extrapolation to world canon without the normal canon gate.

## External Tools

Inspection does not authorize installation or execution. Before using executable
code, plugins, models, or converters, record license, capability, security scope,
local write/network effects, and whether user approval is required.

## Closeout

Report source state, allowed anchor, blocked claim, extrapolation, created links, and
unresolved verification. A missing source is a finding only after a scoped search is
recorded.
