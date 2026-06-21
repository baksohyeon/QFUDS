---
phase: "19"
name: "Fiction IP Structure Migration"
created: 2026-06-20
---

# Phase 19: Fiction IP Structure Migration - Context

## Decisions

- Treat `qfuds-verse` as the canonical universe/IP container for current QFUDS
  fiction work.
- Move active QFUDS SAGA work from top-level `docs/wiki/fiction/qfuds-saga/`
  into `docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/`.
- Move old fiction archive material from `docs/wiki/fiction/archive/` into
  `docs/wiki/fiction/90_archive/`.
- Leave README-only compatibility notices at the old top-level entrypoints.
- Keep internal SAGA shelf names unchanged for this migration:
  `00_system/`, `10_series_bible/`, `20_development/`, `30_drafts/`.

## Boundary

This phase is routing and documentation architecture work only. It does not
change QFUDS research status, fiction canon, or the Phase 18 Korean-primary
story content.

## Deferred Ideas

- Normalize the SAGA internal shelves to the generic work layout
  `00_bible/`, `10_story_design/`, `20_drafts/`, `30_revisions/`,
  `40_release/`.
- Add a dedicated work-level continuity document if the first arc canon closes.
- Start Arc Two under the canonical SAGA series path.
