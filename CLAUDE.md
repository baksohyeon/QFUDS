# CLAUDE.md

Claude-specific entry point for the QFUDS repository. This file intentionally
carries no project status and no research rules of its own. It is a thin wrapper
that points to the authoritative documents and must stay that way.

## Authority Chain

- [CLAUDE.md](CLAUDE.md)
- [AGENTS.md](AGENTS.md) — project constitution: process and rules
- [docs/05_next_steps/000_roadmap.md](docs/05_next_steps/000_roadmap.md) —
  single source of truth for status
- [docs/00_project/decision_log.md](docs/00_project/decision_log.md) — why each
  decision was made
- [docs/03_experiments/](docs/03_experiments/) — experiment definitions
- [docs/04_results/](docs/04_results/) — experiment evidence

Each level references the one below it. Nothing above the roadmap maintains its
own copy of project status.

## Where To Look

- Project constitution (process, research rules, agent behavior):
  [AGENTS.md](AGENTS.md).
- Current project status, current level, active branch, and blockers
  (single source of truth):
  [docs/05_next_steps/000_roadmap.md](docs/05_next_steps/000_roadmap.md).
- Why research decisions were made:
  [docs/00_project/decision_log.md](docs/00_project/decision_log.md).
- Experiment and result evidence:
  [docs/03_experiments/](docs/03_experiments/) and
  [docs/04_results/](docs/04_results/).

## Rules For Claude

- Read [AGENTS.md](AGENTS.md) in full before doing any work. It overrides
  default behavior.
- Read the roadmap for status before making any status claim. Do not maintain,
  cache, or restate project status in this file.
- Before any external literature, web, source, asset, extraction,
  product-availability, NASA/LAMBDA, BAO, DESI/eBOSS, or cache claim, read
  [.agent/workflows/README.md](.agent/workflows/README.md) and apply
  [Research Asset and Product Workflow](.agent/workflows/research-asset-product-workflow.md).
  Any resulting research document must record the workflow marker and a state
  token such as `hit_not_cached`, `asset_cached`, `no_asset_found`, or
  `inaccessible`.
- Before moving, creating, or indexing documentation, read
  [Documentation Folder Routing Workflow](.agent/workflows/documentation-folder-routing-workflow.md)
  and [Wiki Maintenance Workflow](.agent/workflows/wiki-maintenance-workflow.md).
  For fiction/IP work, also read
  [Fiction IP Management Workflow](.agent/workflows/fiction-ip-management-workflow.md).
  For SAGA fiction, route operating specs to
  `docs/wiki/fiction/qfuds-saga/00_system/`, series bible / 작품 설정 기준서
  material to `docs/wiki/fiction/qfuds-saga/10_series_bible/`,
  pitches/outlines/visual packages to `docs/wiki/fiction/qfuds-saga/20_development/`,
  prose drafts with harness boundaries to `docs/wiki/fiction/qfuds-saga/30_drafts/`,
  and archived prototypes to `docs/wiki/fiction/archive/`.
- Do not duplicate roadmap, decision-log, theory, or experiment content here.
- When this file disagrees with [AGENTS.md](AGENTS.md) or the roadmap, those win and this
  file must be corrected.

## Consistency Checks

Before major experiment milestones, run:

```bash
make research-audit        # validate_docs.py + research_consistency.py
make agent-workflow-guard  # staged external-research workflow guard
# or, without make:
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/agent_workflow_guard.py --staged
```
