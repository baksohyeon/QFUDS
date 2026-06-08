<INSTRUCTIONS>
@/Users/cnai/.codex/RTK.md
</INSTRUCTIONS>

# CLAUDE.md

Claude-specific entry point for the QFUDS repository. This file intentionally
carries no project status and no research rules of its own. It is a thin wrapper
that points to the authoritative documents and must stay that way.

## Authority Chain

```text
CLAUDE.md
  -> AGENTS.md                              (project constitution: process + rules)
    -> docs/05_next_steps/000_roadmap.md    (single source of truth for status)
      -> docs/00_project/decision_log.md    (why each decision was made)
        -> docs/03_experiments/             (experiment definitions)
        -> docs/04_results/                 (experiment evidence)
```

Each level references the one below it. Nothing above the roadmap maintains its
own copy of project status.

## Where To Look

- Project constitution (process, research rules, agent behavior): `AGENTS.md`.
- Current project status, current level, active branch, and blockers
  (single source of truth): `docs/05_next_steps/000_roadmap.md`.
- Why research decisions were made: `docs/00_project/decision_log.md`.
- Experiment and result evidence: `docs/03_experiments/` and `docs/04_results/`.

## Rules For Claude

- Read `AGENTS.md` in full before doing any work. It overrides default behavior.
- Read the roadmap for status before making any status claim. Do not maintain,
  cache, or restate project status in this file.
- Do not duplicate roadmap, decision-log, theory, or experiment content here.
- When this file disagrees with `AGENTS.md` or the roadmap, those win and this
  file must be corrected.

## Consistency Checks

Before major experiment milestones, run:

```bash
make research-audit        # validate_docs.py + research_consistency.py
# or, without make:
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
```
