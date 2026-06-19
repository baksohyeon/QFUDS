# QFUDS Fiction IP Studio

## What This Is

This is a GSD planning layer for the QFUDS fiction track. It manages story/IP
workflow, canon boundaries, and publication-style folder discipline separately
from the QFUDS research program.

## Core Value

Make the fiction workflow fun, expandable, and easy to resume without blurring
research status.

## Boundary

Fiction work may use QFUDS history as inspiration only. It cannot create
research evidence, support claims, validation claims, or Level 2B admission.

## Requirements

### Validated

- Fiction documents live under `docs/wiki/fiction/`.
- QFUDS research authority remains in the roadmap, research docs, and workflow
  guards, not in fiction prose.

### Active

- [ ] Keep fiction/IP work routed through the fiction IP management workflow.
- [ ] Use GSD planning for larger fiction phases before drafting major story
  material.
- [ ] Separate studio system docs, universe/canon material, works, drafts, and
  archives.
- [ ] Preserve science-auditor boundaries in every major story plan.

### Out of Scope

- QFUDS research status changes.
- Practical security or cryptography advice.
- Direct publication claims.
- Sensitive real-person framing.

## Context

The repo now has a separate fiction track under `docs/wiki/fiction/`, with
studio guidance, templates, and a documented bridge from fiction IP management
to GSD planning. The next useful step is to let GSD track that work explicitly
without confusing it with QFUDS research state.

## Constraints

- **Workflow authority**: Use `.agent/workflows/fiction-ip-management-workflow.md`
  for fiction/IP decisions.
- **User gate**: Major direction changes require explicit user confirmation.
- **Planning prose**: Keep boundary language in one section. Phase plans should
  use one local boundary line and avoid repeating the same claim through
  `truths`, `artifacts`, `key_links`, tasks, and summaries.
- **Issue comments**: When reporting tooling issues, prefer a compact
  `Issue | Impact | Fix` table over long narrative comments.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Manage fiction as IP/studio work, not a QFUDS research phase | Prevents creative work from changing research status | Active |
| Use GSD for major fiction phases | Keeps planning, dependencies, and acceptance checks explicit | Active |
| Keep `.planning` scoped to this worktree | Avoids writing to another QFUDS checkout from a Codex worktree | Good |

---
*Last updated: 2026-06-19 after STATE/ROADMAP reconciliation and planning prose cleanup*
