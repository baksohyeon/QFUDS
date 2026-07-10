# Documentation Folder Routing Workflow

Use this workflow whenever a task creates, moves, classifies, or cross-links
repository documentation.

This file is the operational SSOT for deciding where QFUDS documentation
belongs and when research-support work should propagate into status, lineage,
governance, postmortem, or roadmap documents.

It is process-only. It does not change roadmap status, open Level 2B, or turn a
research artifact into QFUDS support.

Workflow index: [QFUDS Agent Workflows](README.md).

## Core Rule

Put a document where its job is, not where the topic sounds related.

For example, a Chen entropy digitization belongs under `research/assets/`
because it is an asset product. The judgment about what that product changes
belongs under `research/investigations/source_x/conclusions/`. A later branch
classification may belong under `lineage/`, but only after the branch relation
actually changes.

## Top-Level Repository Docs

| Path | Use for | Do not use for |
| --- | --- | --- |
| `docs/00_project/` | project identity, decision log, conventions, success criteria | raw research notes, transient investigation products |
| `docs/01_origin/` | original motivation and concept origin trail | current status or active blockers |
| `docs/02_theory/` | theory notes, equations, derivations, hostile audits of model structure | source PDFs, literature cache, process retrospectives |
| `docs/03_experiments/` | planned or executable experiments with hypotheses and failure criteria | post-hoc research notes without runnable experiment scope |
| `docs/04_results/` | completed experiment results and experiment summary | literature investigations or asset digitization products |
| `docs/05_next_steps/` | roadmap, active gates, future work constraints | duplicate status tables elsewhere |
| `docs/wiki/` | support material: glossary, governance aids, lineage maps, research cache, postmortems | authoritative roadmap status |
| `fiction/` | fiction-vault content: inbox, knowledge, research, worlds (`continuity/`, `world/`, `series-bible/`), and projects (README + `drafts/`) | research evidence, roadmap status, physical-source claims |
| `creative_harness/` | human-readable craft/method references for fiction work | world facts, prose drafts, project status |

## Wiki Folder Roles

| Path | Use for | Do not use for |
| --- | --- | --- |
| `docs/wiki/glossary/` | stable vocabulary and repository terminology | project status, experiment results |
| `docs/wiki/governance/` | admission rules, branch gates, missing-physics maps, consistency checks | raw research products or incident narratives |
| `docs/wiki/lineage/` | idea genealogy, branch dependency maps, demotion/routing provenance | daily progress, external literature, asset products, incident retrospectives |
| `docs/wiki/postmortem/` | incident retrospectives, process failures, long-form checkpoints, handoff retrospectives | source products, roadmap status changes |
| `docs/wiki/research/` | external literature records, cached assets, investigations, source/product recovery work | accepted physical-status claims |

## Fiction Folder Roles

Use these routes for QFUDS-inspired creative work. Fiction can preserve
motivation, emotional continuity, public explanation, and speculative imagery,
but it must not be promoted into a physical QFUDS source claim.

| Path | Use for | Do not use for |
| --- | --- | --- |
| `fiction/README.md` | landing page for the fiction vault and inbox routing | detailed canon, source claims, roadmap status |
| `fiction/inbox/` | uncategorized raw material awaiting routing | long-term storage |
| `fiction/knowledge/` | reusable creative ideas not tied to one project | world facts, prose drafts |
| `fiction/research/` | real-world reference material for verisimilitude | in-world canon, prose |
| `fiction/worlds/<universe-id>/` | facts currently true in a fictional world: `continuity/`, `world/`, `series-bible/` | project-local drafts, operational rules |
| `fiction/projects/<work-id>/` | a specific work's README (classification, inherited rules, local overrides, work bible, story design, boundary) and its `drafts/` | universe-wide canon, operational workflow authority |
| `creative_harness/craft/` | fiction craft/verisimilitude/prose-quality references | world facts, prose drafts, research evidence |
| `creative_harness/methods/` | panel/research/work-method references | world facts, prose drafts |

The QFUDS SAGA production track (story design, drafts, revisions, release, and
workroom material except research anchors `411`/`412`, and the archive) closed
2026-07-10; it and the old `docs/wiki/fiction/` shelves are Git history only
(`git show bbbcb970:<old-path>`), not a live routing target and not to be
recreated.

For Codex and Claude Code, the routing rule is:

```text
fiction content -> fiction/ (inbox/knowledge/research/worlds/projects)
human craft/method reference -> creative_harness/ (craft/, methods/)
new universe/IP world facts -> fiction/worlds/<universe-id>/
new work README, local overrides, work bible, story design, boundary -> fiction/projects/<work-id>/README.md
new work prose draft -> fiction/projects/<work-id>/drafts/
shared universe series bible -> fiction/worlds/<universe-id>/series-bible/
idea genealogy that changes research branch classification -> docs/wiki/lineage/
external source, PDF, paper, data, or product claim -> docs/wiki/research/
```

If a fiction document touches an external paper, web reference, PDF, code
repository, MCP, or source/product availability claim, also apply
[Research Asset and Product Workflow](research-asset-product-workflow.md) and
record the workflow state token in the fiction document.

## Research Folder Roles

| Path | Use for | Do not use for |
| --- | --- | --- |
| `docs/wiki/research/literature/` | reusable paper/reference summaries | execution plans, derived products, project status |
| `docs/wiki/research/assets/<paper_or_release_key>/source/` | source PDFs, TeX/source bundles, archives, raw downloads | audit conclusions |
| `docs/wiki/research/assets/<paper_or_release_key>/figures/` | extracted or rendered figure assets | digitized CSVs or Source-X judgments |
| `docs/wiki/research/assets/<paper_or_release_key>/digitization/` | Markdown conversions, manual extracts, digitized CSV/JSON, asset provenance | Source-X decision closeouts |
| `docs/wiki/research/investigations/<chain>/plans/` | candidate selection, execution plans, digitization plans, prompt/scope records | result claims |
| `docs/wiki/research/investigations/<chain>/conclusions/` | result closeouts, decision summaries, blocker judgments | raw assets or numeric tables |
| `docs/wiki/research/investigations/<chain>/coverage/` | search-breadth and coverage-expansion records | product files |

For asset-product interpretation details, also apply
[Research Investigation Result Routing Workflow](research-investigation-result-routing-workflow.md).

## Propagation Rules

Research work can affect other docs, but only after it changes the thing those
docs own.

| Research event | Update immediately | Update only if condition is met |
| --- | --- | --- |
| New literature summary | `docs/wiki/research/literature/README.md` if discoverability requires it | roadmap only if a formal result changes project status |
| New cached source asset | `docs/wiki/research/assets/README.md`, asset-level README, and relevant asset subfolder README | Source-X conclusions only if the asset is interpreted for an investigation |
| Manual structured extract | asset `digitization/README.md`; investigation conclusion closeout | roadmap only if all physical-admission items are supplied |
| Numeric digitization CSV/JSON | asset `digitization/README.md`; investigation conclusion closeout | lineage only if later result changes branch dependency or classification |
| Plan-only investigation record | investigation `plans/README.md`; chain read order | conclusions only after execution or judgment |
| Executed investigation result | investigation `conclusions/README.md`; chain read order | governance only if an admission rule itself changes |
| Known-model distinction result | investigation conclusion closeout | lineage if branch classification changes; roadmap only if admission status changes |
| Incident or process lesson | `docs/wiki/postmortem/README.md`; `docs/wiki/index.md` if useful | workflows only if a repeatable operating rule is created |
| Fiction companion or SAGA harness record | `fiction/README.md`; `docs/wiki/index.md` if useful | lineage only if the research branch genealogy changes |

## Status Boundary

Do not update roadmap, decision log, experiment results, governance, or lineage
just because a research artifact exists.

Update those docs only when their owned claim changes:

- roadmap: current project level, active blocker, or next gate changes;
- decision log: a formal project decision is made;
- experiment results: a declared experiment completes;
- governance: an admission rule, missing-physics map, or consistency gate
  changes;
- lineage: idea genealogy or branch dependency classification changes.

## Source-X Example

Current Source-X product-recovery routing follows this pattern:

```text
assets/.../digitization/
  stores manual extracts, digitized CSVs, and asset provenance

research/investigations/source_x/plans/
  stores future execution scopes

research/investigations/source_x/conclusions/
  stores what each execution changed and what remains blocked

postmortem/
  stores process retrospectives and end-of-day checkpoints

lineage/
  waits until a known-model result changes branch classification
```

This means a Chen Figure 5 CSV can exist while Physical-QFUDS Level 2B remains
blocked. Asset product state is not physical-admission state.

## Forbidden Shortcuts

Do not use research products to claim:

- QFUDS support;
- candidate `X`;
- `Q^nu`;
- `delta Q`;
- Level 2B admission;
- roadmap advancement;
- known-model distinction;

unless the responsible document type actually supplies that evidence.

When uncertain, write the narrower routing document first and leave status
authorities unchanged.
