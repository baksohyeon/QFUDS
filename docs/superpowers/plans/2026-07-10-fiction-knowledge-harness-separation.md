---
doc_id: plan_2026_07_10_fiction_knowledge_harness_separation
title: Fiction knowledge and creative harness separation plan
doc_type: guide
stage: reference
status: in_progress
evidence_role: reference
depends_on: []
next_gate: execute the migration sequentially and run whole-branch review
last_updated: 2026-07-10
---

# Fiction knowledge and creative harness separation plan

> Fable 5 produced the repository inventory and first architecture pass. The
> coordinator then corrected it against the user's final decisions and the live
> worktree: all moves use Obsidian, the old atomization attempt is not restored,
> and `tools/story-skills` remains a real submodule.

## Outcome

Separate three concerns that are currently mixed under `docs/wiki/fiction/`:

1. durable fiction knowledge under repository-root `fiction/`;
2. human-readable writing methods under repository-root `creative_harness/`;
3. operational agent workflows, templates, skills, and tools in their existing
   `.agent/`, `.agents/`, `.claude/`, and `tools/` layers.

Remove all QFUDS SAGA prose, manuscripts, outlines, production state, revision
artifacts, release artifacts, generated encyclopedia output, and legacy prose
archives from the active tree. Git history is the recovery mechanism.

Research status, the roadmap, experiment evidence, result evidence, and the
decision log are out of scope. Fiction remains non-evidence.

## Binding decisions

- Content root is exactly `fiction/`.
- Human craft and method documents live in `creative_harness/`, visibly separate
  from the content vault and movable through Obsidian.
- Operational harness files already under dot-directories stay in place; they
  are edited only to point at the new locations.
- Every existing file or directory move is performed through the isolated
  worktree-root Obsidian vault. No `git mv` exception is allowed.
- Deletions use narrowly scoped `git rm`; new files use `apply_patch`.
- Links are ordinary relative Markdown links. Obsidian wikilinks are forbidden.
- The historical generated source queue and hand-split atomic-note experiment
  are not restored or imported. They remain recoverable from Git history.
- The new `fiction/knowledge/` shelf stores coherent, reusable ideas. It does
  not require tiny files or one-heading-per-card atomization.
- World and continuity documents are retained as fiction canon/reference.
- The former SAGA series bible is retained only as a world-reference shelf; it
  does not imply an active SAGA project.
- The QFUDS Verse web reader remains a tool and moves to
  `tools/qfuds-verse-web/` through Obsidian.
- The non-SAGA `feathersmcgraw-coda` project is preserved.
- `tools/story-skills` stays intact as the initialized submodule at its pinned
  commit.

## Target layout

```text
fiction/
├── README.md
├── inbox/
│   └── README.md
├── knowledge/
│   └── README.md
├── research/
│   ├── README.md
│   └── 412_real_world_and_physics_research_anchors_ko.md
├── worlds/
│   ├── README.md
│   ├── qfuds-verse/
│   │   ├── README.md
│   │   ├── 000_world_canon_orientation_ko.md
│   │   ├── continuity/
│   │   ├── world/
│   │   └── series-bible/
│   └── vector-sandbox/
│       ├── README.md
│       └── world/
└── projects/
    ├── README.md
    └── feathersmcgraw-coda/
        └── drafts/

creative_harness/
├── README.md
├── craft/
│   ├── 004_creative_writing_craft_harness_ko.md
│   ├── 005_university_creative_writing_reference_matrix_ko.md
│   ├── 006_prose_verisimilitude_audit_checklist_ko.md
│   ├── 007_craft_and_political_theory_research_ko.md
│   ├── 009_korean_fiction_prose_naturalness_harness_ko.md
│   └── 010_reader_onboarding_harness_ko.md
└── methods/
    └── 411_near_future_forecast_panel_method_ko.md

tools/qfuds-verse-web/
```

## Disposition rules

| Source | Disposition |
| --- | --- |
| `00_continuity/`, `10_world/`, universe orientation | move to `fiction/worlds/qfuds-verse/` |
| SAGA `00_bible/` | move to `fiction/worlds/qfuds-verse/series-bible/`; mark as inactive-series reference |
| workroom `412` | move to `fiction/research/` with fiction-only boundary intact |
| studio `004`-`007`, `009`, `010`; workroom `411` | move to `creative_harness/` |
| vector-sandbox world and Coda project | move to the corresponding world/project shelves |
| QFUDS Verse web app | move to `tools/qfuds-verse-web/` |
| SAGA story design, drafts, revisions, release, other workroom state | delete; Git history only |
| generated SAGA encyclopedia and digest tooling | delete |
| `docs/wiki/fiction/90_archive/` | delete; Git history only |
| obsolete studio routing docs and catalog audit boards | delete after their durable guidance is represented by current workflows/landing pages |
| historical atomization queue and atomic extracts | do not restore |

## Execution protocol

- Follow `superpowers:subagent-driven-development` task by task.
- Keep one writer active in this worktree at a time.
- Model routing follows the user's token budget: Haiku for bounded inventory and
  specification checks, Sonnet for ordinary implementation/review, Opus 4.8 1M
  only when very long context is materially required, GPT-5.5 xhigh for heavy
  implementation/debugging, and Fable only as the master agent for architecture,
  task decomposition, and final whole-branch judgment. Do not use Sol.
- Luna and Terra were requested initially but became unavailable through the
  local CLI after the 2026-07-10 app update; do not retry them repeatedly.
- `codex-rescue` is unavailable as an executable in this environment; do not
  claim it ran. GPT-5.5 xhigh is the implementation fallback.
- At each task boundary, the coordinator inspects the actual diff and reruns the
  named checks before accepting the worker result.
- Each implementation task receives a specification review and a code-quality
  review before the next writer starts.

## Task 1: Baseline and independent Markdown-link gate

1. Verify the isolated worktree baseline with `make preflight` and `make test`.
   Baseline observed before migration: 89 tests, all passing.
2. Verify root-vault settings in ignored `.obsidian/app.json`:
   `alwaysUpdateLinks=true`, `useMarkdownLinks=true`, `newLinkFormat=relative`.
3. Add a tested `scripts/check_markdown_link_targets.py` that:
   - scans specified roots recursively;
   - ignores fenced code, external URLs, mail links, and anchor-only links;
   - resolves URL-encoded and angle-bracket Markdown destinations;
   - checks both document and image links;
   - reports file, line, and missing target;
   - skips absent optional roots.
4. Add unit tests first, confirm the red state, implement minimally, then run the
   targeted tests and full suite.
5. Commit the plan and checker as one reviewable foundation commit.

Review: direct diff inspection, targeted tests, full suite, and a baseline scan
of `docs/wiki/fiction`, `.agent`, `.agents`, `.claude`, and relevant tools.

## Task 2: Remove SAGA production/prose and obsolete active archives

Delete only the confirmed history-only families:

```text
docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/10_story_design/
docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/20_drafts/
docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/30_revisions/
docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/40_release/
docs/wiki/fiction/90_archive/
```

Also delete the SAGA root README/encyclopedia, series index, every workroom file
except `411` and `412`, obsolete studio routing pages, superseded catalog audit
boards, `scripts/build_saga_digest.py`, `scripts/fiction_continuity.py`, and
tests whose entire subject was removed. Remove the digest hook and Make target.

Repair references to deleted targets conservatively: navigation entries vanish;
historical prose mentions become plain text marked as Git-history-only. Do not
rewrite world content beyond link-target repair.

Review: prove that `00_bible/`, `00_continuity/`, `10_world/`, `411`, `412`,
vector-sandbox, the six craft documents, web assets, and `tools/story-skills`
remain intact. Run the link gate, preflight, and full tests before commit.

## Task 3: Create landing pages and move every retained artifact in Obsidian

Create the target landing READMEs with `apply_patch`, then perform these UI move
waves in the worktree-root Obsidian vault. After each wave, inspect `git status`
and verify that unrelated content did not change.

1. Human harness wave:
   - studio `004`-`007`, `009`, `010` -> `creative_harness/craft/`;
   - workroom `411` -> `creative_harness/methods/`.
2. QFUDS Verse knowledge wave:
   - orientation, continuity, world, and density index -> the new world shelf;
   - SAGA `00_bible/` -> `series-bible/`;
   - workroom `412` -> `fiction/research/`.
3. Vector wave:
   - vector-sandbox world -> `fiction/worlds/vector-sandbox/`;
   - Coda -> `fiction/projects/feathersmcgraw-coda/`, with its draft folder
     renamed to `drafts/` in Obsidian.
4. Tool wave:
   - QFUDS Verse `web/` -> `tools/qfuds-verse-web/`.
5. Remove the superseded old fiction landing page after inbound links point to
   the new `fiction/README.md`.

Run the independent link gate after every wave. Any content changes beyond link
destinations require explicit inspection and justification.

## Task 4: Repoint scripts, guards, hooks, and tests

Use tests first for behavior changes.

- Repoint `scripts/fiction_gate.py` from `docs/wiki/fiction` to `fiction/` and
  make project-draft detection follow `projects/*/drafts/`.
- Repoint `scripts/check_web_data_provenance.py` to the retained continuity,
  world, and series-bible shelves and to `tools/qfuds-verse-web/data/`.
- Repoint `scripts/build_doc_graph.py`; update examples in
  `scripts/rename_doc.py`.
- Remove SAGA-only digest and continuity entry points from hooks/Makefile.
- Update or remove obsolete tests, preserving tests for retained behavior.
- Add a structural regression test asserting that prohibited SAGA prose,
  revision, release, and old `docs/wiki/fiction/` roots do not return.
- Keep the initialized `tools/story-skills` submodule untouched.

Run targeted tests, `make preflight`, and `make test`; inspect every changed
script directly before commit.

## Task 5: Rewrite routing authorities and remaining links

Update only routing/path language in:

```text
AGENTS.md
CLAUDE.md
README.md
docs/00_project/qfuds_ko.md
docs/wiki/README.md
docs/wiki/index.md
.agent/workflows/
.agent/templates/fiction/
.agents/skills/fiction-production/SKILL.md
.claude/skills/fiction-production
tools/saga-fiction-studio/skills/
```

The new authority must say:

- content -> `fiction/`;
- human craft/method references -> `creative_harness/`;
- operational workflow/template/skill authority -> existing agent layers;
- web reader -> `tools/qfuds-verse-web/`;
- SAGA project/prose -> Git history only;
- fiction -> never research evidence.

Do not duplicate project research status. Run a repository-wide old-path scan,
the Markdown-link gate, docs validation, preflight, and full tests.

## Task 6: Whole-branch review and handoff

1. Run all repository gates and record exact output.
2. Audit structure and counts against the target layout.
3. Confirm no `docs/wiki/fiction/` file remains and no SAGA prose/project file
   survives under a renamed location.
4. Confirm retained world/reference files differ from the base only where links
   or explicit boundary banners changed.
5. Confirm roadmap, decision log, theory, experiment, and result status are
   unchanged.
6. Run an independent GPT-5.5 xhigh review and a final Fable 5 review of the
   full branch diff. Fix findings, rerun gates, and review again if needed.
7. Present local branch integration choices; do not push or merge without the
   user's explicit choice.

## Recovery

Deleted material remains available at base commit
`bbbcb970bdfb48b7c53ff05b669590653aac5f02` with:

```bash
git show bbbcb970:<path>
```

The abandoned atomization attempt remains addressable by historical commit; it
is intentionally not part of the active structure.
