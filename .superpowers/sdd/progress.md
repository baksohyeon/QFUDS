# Fiction separation SDD progress

Planning: complete (`task_32deba06eafc`, Fable 5 report + coordinator-corrected implementation plan)
Inventory: complete (`task_5c1ceafcaf87`, report `.superpowers/sdd/luna-inventory-report.md`, read-only scope verified)
User decisions applied: root `fiction/`; visible `creative_harness/`; no atomization import; all moves through Obsidian; `tools/story-skills` preserved.
Execution Task 1: complete at `51a68ff` (Markdown-link gate, 9 targeted tests, 98 total tests).
Review Task 1: Haiku specification PASS; Sonnet requested two fixes; fixes completed and Haiku recheck APPROVED.
Execution Task 2: documentation migration active. The Notion deep-research
separation is being applied first: human creative-writing harness documents are
moving into `creative_harness/craft/` through Obsidian so Markdown links are
updated by the vault. Code gates and test refinements are paused until the
document routing is stable.
User reconfirmation 2026-07-10 (later session): keep the binding plan on all
three open points — craft stays outside the vault in `creative_harness/`, no
number prefixes inside `fiction/`, and `90_archive` is deleted from the active
tree (Git history only), overriding the interim preserve commit `e9ba7fa`.
Additionally adopted for landing pages: world-note `state:
provisional/accepted/retired`, hand-curated project `HOME.md` (no auto
dashboards), and the five inbox routing questions in `fiction/README.md`.
Stash integration note: the previous session left its whole-directory Obsidian
move (docs/wiki/fiction/10_universes/qfuds-verse -> fiction/worlds/qfuds-verse,
455 renames) plus HANDOFF.md in stash "WIP temp". The stash surfaced during the
first Task 2 commit attempt and was reconciled with the Task 2 edits: de-links
survived the renames, over-deep ../ prefixes in moved files were shortened,
wiki index/lineage/landing routing was re-applied, and the provenance guard
gained mid-migration path candidates. Remaining moves follow HANDOFF.md steps
1-8 (renames, 411/412, density index, vector/coda, web).
Execution Task 2 completion: `90_archive` deleted (38 files), saga-digest Make
target and pre-commit digest hook removed, 62 links to deleted SAGA/story/
release/workroom targets de-linked to plain text with Git-history markers,
moved-craft links repointed to `creative_harness/`, stale relative links inside
`creative_harness/` repaired, and `check_web_data_provenance.py` reworked
(retained shelves resolve at legacy or fiction-vault paths; closed shelves are
history-only). Gates at this boundary: link gate, validate_docs,
research_consistency, fiction_gate, web-data guard, preflight, unittest all
passing (51 tests; earlier SAGA-subject tests were removed with their
subjects).
Task 2: complete (commits e9ba7fa..c68b116, gates green: link/validate/consistency/fiction/provenance/preflight/51 tests, protected scope untouched)
Task 3: complete (user-performed Obsidian waves: continuity/world/series-bible renames, 411->creative_harness/methods, 412->fiction/research, density index->worlds/qfuds-verse, web->tools/qfuds-verse-web with dotfiles, coda->fiction/projects with drafts/, vector-sandbox->fiction/worlds with world/; 32 link repoints + 3 de-links; old wiki fiction landing deleted; gates green)
Task 3b: complete (inbox routing questions in fiction/README, world-note state rule provisional/accepted/retired in worlds/README, hand-curated HOME.md principle in projects/README)
Task 4: complete (commit dc0162b, review Approved; Minor for final review: (1) fiction_gate is_active_draft keyword-matching exempts coda drafts from soft agentic-marker checks beyond what the README override licenses [pre-existing], (2) build_doc_graph LAYER_RULES bare-word fragments are collision-prone)
Task 5: complete (commit 7e892af, review Approved; Important carried: .planning/** historical GSD logs keep bare pre-migration paths — final review to judge; the two fiction/worlds stray mentions fixed by coordinator [104 Next Task reframed as git-history record]; README:21 is already historical prose, README:89 already a git-show citation)
