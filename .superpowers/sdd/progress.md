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
