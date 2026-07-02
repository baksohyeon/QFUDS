# saga-fiction-studio

Web-novel / SAGA fiction production skills for the QFUDS repo. Manage fiction like
an IP studio, not loose documents. Every skill references the repo's
`.agent/workflows/` and `.agent/templates/fiction/` as the single source of truth
(SSOT) and never restates that authority here.

## Skills

| Skill | Runs when | Purpose |
| --- | --- | --- |
| `canon-guardian` | before any canon-touching edit | classify the change, read related canon first, report conflict risk before writing |
| `scene-writer` | writing/rewriting prose | draft a scene/chapter with the reader-onboarding harness, Korean-primary |
| `continuity-pass` | after a draft or major revision | recover state, check canon/chronology/knowledge-state conflicts (chronicler pass) |
| `reader-retention-gate` | before release | comprehension + retention gate, persona subagents, writes a gate artifact |
| `note-curator` | capturing raw material | classify and route loose notes/memos/ideas into the SAGA folder structure |
| `saga-showrunner` | multi-step writing sprint | orchestrate a session end to end, enforce execution order + production board |

## Fidelity notes

- `canon-guardian` and `reader-retention-gate` were authored from the exact
  Customize-UI text of the uploaded plugin.
- `continuity-pass`, `note-curator`, `saga-showrunner`, and `scene-writer` were
  reconstructed from their UI descriptions and triggers, aligned to the repo's
  existing workflows and templates. Compare against the originals in Customize and
  paste corrections if any diverge.

## Layout

```
docs/wiki/fiction/saga-fiction-studio/
  .claude-plugin/
    plugin.json
    marketplace.json
  skills/
    canon-guardian/SKILL.md
    scene-writer/SKILL.md
    continuity-pass/SKILL.md
    reader-retention-gate/SKILL.md
    note-curator/SKILL.md
    saga-showrunner/SKILL.md
  README.md
```

## Using it

This directory is a real Claude plugin. To use the skills in the app, upload /
re-upload this folder (or its `.claude-plugin/marketplace.json`) under
Settings > Capabilities. Cowork sessions load skills from the enabled plugin set;
enabling happens in the app, not from inside a session.
