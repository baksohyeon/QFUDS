# QFUDS Fiction IP Studio

## What This Is

This is a GSD planning layer for the QFUDS fiction track. It manages story/IP
workflow, canon boundaries, and publication-style folder discipline separately
from the QFUDS research program.

It does not create QFUDS evidence, support, validation, or Level 2B admission.

## Core Value

Make the fiction workflow fun and expandable while preserving the research
boundary: fiction may use QFUDS history as inspiration, never as evidence.

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

- Physical QFUDS validation — fiction is not research evidence.
- Level 2B reopening — this planning layer cannot change research status.
- Direct publication claims — current outputs are repo-local creative planning
  and drafts.

## Context

The repo now has a separate fiction track under `docs/wiki/fiction/`, with
studio guidance, templates, and a documented bridge from fiction IP management
to GSD planning. The next useful step is to let GSD track that work explicitly
without confusing it with QFUDS research state.

## Constraints

- **Research boundary**: No fiction artifact can be cited as QFUDS support.
- **Workflow boundary**: Use `.agent/workflows/fiction-ip-management-workflow.md`
  for fiction/IP decisions.
- **User gate**: Major direction changes require explicit user confirmation.
- **No sensitive real-person framing**: Avoid user-identifying details and avoid
  importing sensitive real-world factions as direct canon labels.

## Key Decisions

| Decision | Rationale | Outcome |
|----------|-----------|---------|
| Manage fiction as IP/studio work, not a QFUDS research phase | Prevents creative work from changing research status | Pending |
| Use GSD for major fiction phases | Keeps planning, dependencies, and acceptance checks explicit | Pending |
| Keep `.planning` scoped to this worktree | Avoids writing to another QFUDS checkout from a Codex worktree | Good |

---
*Last updated: 2026-06-19 after initial GSD setup for the fiction/IP track*
