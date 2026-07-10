# Fiction migration handoff

Updated: 2026-07-10 15:49 KST

## Goal

Complete the separation described in
[the implementation plan](../../docs/superpowers/plans/2026-07-10-fiction-knowledge-harness-separation.md):

- fiction content under `fiction/`;
- human writing references under `creative_harness/`;
- the QFUDS Verse reader under `tools/qfuds-verse-web/`;
- SAGA production/prose and legacy archives in Git history only;
- no change to QFUDS research status or evidence.

Use ordinary relative Markdown links. Perform every remaining existing-file or
directory move and rename through the repository-root Obsidian vault so Obsidian
updates links. Use `apply_patch` for new files and content/link repairs.

## Git state

- Repository: `/Users/cnai/dev/personal/QFUDS`
- Branch: `codex/fiction-knowledge-harness-separation`
- HEAD before the live move: `e9ba7faa53ac5340081e341723520b02243543bb`
- Recovery base for deleted SAGA material: `bbbcb970bdfb48b7c53ff05b669590653aac5f02`
- Existing branch commits:
  - `51a68ff` Markdown-link checker and tests
  - `d1b88d7` creative-harness landing and craft shelf
  - `e9ba7fa` archive/reference preservation checkpoint

The working tree is intentionally dirty because one large Obsidian move is in
progress. Do not use `git reset`, `git checkout`, or a broad clean operation.

## Completed in the current working tree

The repository-root Obsidian vault moved this whole directory:

```text
docs/wiki/fiction/10_universes/qfuds-verse/
  -> fiction/worlds/qfuds-verse/
```

The destination currently contains 455 files, including 52 Markdown files.
This intentionally carried the world, continuity, Bible, workroom 411/412, and
web-reader assets together so inbound links were updated once by Obsidian.

Obsidian also updated inbound links in at least:

- `creative_harness/craft/006_prose_verisimilitude_audit_checklist_ko.md`
- `creative_harness/craft/007_craft_and_political_theory_research_ko.md`
- `docs/wiki/fiction/01_catalog/001_qfuds_verse_world_density_index_ko.md`

The local ignored `.obsidian/app.json` now contains:

```json
{
  "alwaysUpdateLinks": true,
  "useMarkdownLinks": true,
  "newLinkFormat": "relative",
  "showUnsupportedFiles": true
}
```

No files under `docs/02_theory/`, `docs/03_experiments/`, `docs/04_results/`,
`docs/05_next_steps/`, or `docs/00_project/decision_log.md` differ from the
recovery base at handoff time.

## Current intermediate layout

The following names are temporary and still need Obsidian renames/moves:

```text
fiction/worlds/qfuds-verse/
├── 00_continuity/                  -> continuity/
├── 10_world/                       -> world/
├── 20_series/qfuds-saga/
│   ├── 00_bible/                   -> ../../series-bible/
│   └── 00_workroom/
│       ├── 411_...                 -> creative_harness/methods/
│       └── 412_...                 -> fiction/research/
└── web/                             -> tools/qfuds-verse-web/
```

Do not pre-create `series-bible/README.md`; the retained source README must
occupy that path.

## Next actions in exact order

1. In Obsidian, rename
   `fiction/worlds/qfuds-verse/00_continuity` to `continuity`.
2. In Obsidian, rename
   `fiction/worlds/qfuds-verse/10_world` to `world`.
3. In Obsidian, move
   `fiction/worlds/qfuds-verse/20_series/qfuds-saga/00_bible` to
   `fiction/worlds/qfuds-verse`, then rename it to `series-bible`.
4. In Obsidian, move workroom `411_near_future_forecast_panel_method_ko.md` to
   `creative_harness/methods/`.
5. In Obsidian, move workroom
   `412_real_world_and_physics_research_anchors_ko.md` to `fiction/research/`.
6. In Obsidian, move `fiction/worlds/qfuds-verse/web` to `tools/`, then rename
   it to `qfuds-verse-web`.
   - Verify `.dockerignore` and `.gitignore` afterward. Obsidian may omit hidden
     files during this move. If omitted, recreate both byte-identically with
     `apply_patch`, then remove only the old tracked copies with a narrow command.
7. In Obsidian, move
   `docs/wiki/fiction/01_catalog/001_qfuds_verse_world_density_index_ko.md` to
   `fiction/worlds/qfuds-verse/`.
8. Move the Vector/Coda wave through Obsidian:
   - move the Coda project to `fiction/projects/feathersmcgraw-coda/`;
   - rename its `20_drafts/` directory to `drafts/`;
   - move Vector Sandbox to `fiction/worlds/vector-sandbox/`;
   - rename its `10_world/` directory to `world/`.
9. Remove the now-empty QFUDS SAGA directory shell and the remaining obsolete
   `docs/wiki/fiction/` content according to the plan. In particular,
   `docs/wiki/fiction/90_archive/` is Git-history-only in the target layout.
10. Repoint scripts, tests, workflows, skills, and landing pages as specified in
    Tasks 4 and 5 of the implementation plan.

## Known link state

Immediately after the whole QFUDS Verse move, this command reported 77 missing
targets:

```bash
python3 scripts/check_markdown_link_targets.py fiction/worlds/qfuds-verse
```

This is not a green state. The set includes:

- expected temporary misses caused by the not-yet-renamed `00_continuity`,
  `10_world`, Bible, workroom, and web paths;
- links to intentionally deleted SAGA story-design, draft, workroom, revision,
  and release files;
- relative links to `.agent/`, `docs/01_origin/`, and the moved craft shelf that
  became too deep after the directory move.

Links to deleted SAGA production documents must not be redirected to unrelated
live documents. Convert them to plain Git-history-only references or remove
navigation entries. A deleted file is recoverable with:

```bash
git show bbbcb970:<old-path>
```

## Recovered inventory facts

- QFUDS world wave: 37 Markdown files; 328 participating local-link
  occurrences; 212 destination strings require changes; 55 outbound misses
  existed before the move.
- Series Bible: 11 retained Markdown files (`README.md`, `201`-`210`), 2,127
  lines; destination has no collision.
- Research anchor `412`: one retained 295-line Markdown file; destination has no
  collision.
- Vector/Coda: six retained Markdown files; no destination collision. Move Coda
  before Vector, then rename `20_drafts` to `drafts`.
- Web-reader and final integration inventories did not complete before the old
  Orca runtime/worktrees disappeared. Reinspect live paths instead of assuming
  those unfinished reports exist.

## Script and authority follow-up

At minimum, inspect and update:

- `scripts/fiction_gate.py`
- `scripts/check_web_data_provenance.py`
- `scripts/build_doc_graph.py`
- `scripts/rename_doc.py`
- `scripts/git-hooks/pre-commit`
- `Makefile`
- `tests/test_web_data_provenance.py`
- a new or recovered `tests/test_fiction_structure.py`
- `AGENTS.md`, `CLAUDE.md`, `README.md`
- `docs/00_project/qfuds_ko.md`
- `docs/wiki/README.md`, `docs/wiki/index.md`
- `.agent/workflows/`, `.agent/templates/fiction/`
- `.agents/skills/fiction-production/SKILL.md`
- `.claude/skills/fiction-production`
- `tools/saga-fiction-studio/skills/`

The final authority language is:

- fiction content -> `fiction/`;
- human craft/method material -> `creative_harness/`;
- operational workflows/templates/skills -> existing agent/tool layers;
- web reader -> `tools/qfuds-verse-web/`;
- SAGA production/prose -> Git history only;
- fiction -> never QFUDS research evidence.

## Verification gates

Run these after every move wave, then all of them before committing:

```bash
python3 scripts/check_markdown_link_targets.py docs/wiki/fiction fiction creative_harness .agent .agents .claude tools
python3 scripts/validate_docs.py
python3 -m unittest discover -s tests
make preflight
make test
git diff --check
```

Also confirm the protected research-status scope remains untouched:

```bash
git diff --name-only bbbcb970 -- \
  docs/02_theory docs/03_experiments docs/04_results docs/05_next_steps \
  docs/00_project/decision_log.md
```

Expected output: empty.

Before staging, inspect the complete rename/delete set with `git status --short`
and ensure `tools/story-skills` remains at its pinned submodule commit.

## Local warning configuration

The Chronicle warning was suppressed in the Orca Codex runtime config by adding
this top-level setting:

```toml
suppress_unstable_features_warning = true
```

File:
`/Users/cnai/Library/Application Support/orca/codex-runtime-home/home/config.toml`

The change takes effect for newly started Codex sessions. It does not disable
Chronicle itself.

## Orchestration state

Two low-token read-only tasks were created for Web-reader inventory and a gap
audit, then marked failed intentionally when the user requested direct handoff.
Their stale terminal handles were no longer live, and they made no authorized
file edits.

