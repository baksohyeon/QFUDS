---
name: note-curator
description: >
  Classify and route loose fiction notes, meeting memos, chat ideas, and brainstorms
  into the fiction vault structure. Use when capturing or sorting raw material.
  Triggers: "이 메모 정리해줘", "이거 어디 넣어?", "아이디어 분류", "회의록 정리",
  "curate this note", "where does this go", "sort my inbox", "raw vs canon".
  Sorts each item into raw / candidate / canon / archive and routes it to the correct
  fiction folder without promoting anything to canon.
user-invocable: true
---
# Note Curator
Turn loose input into correctly-layered records. Curation never promotes to canon by
itself — it stages material for the canon gate.
SSOT: `.agent/workflows/documentation-folder-routing-workflow.md`,
`.agent/workflows/fiction-ip-management-workflow.md` (layer ladder + Workroom/Bible
rules), and `.agent/workflows/wiki-maintenance-workflow.md`.
## Procedure
1. Normalize input — if it is a PDF/doc/transcript, note that MarkItDown converts it
   to Markdown first (do not paste binary). Keep one idea per record.
2. Classify each item by state:
   - `raw` — unfiltered capture, not evaluated;
   - `candidate` — a proposed setting/scene idea, not yet canon;
   - `canon` — only if it already passed the canon gate (route via `canon-guardian`,
     never mark canon here);
   - `archive` — discarded, retired, or superseded (keep for provenance).
3. Classify by ownership layer: `studio | catalog | universe/IP | continuity | work |
   workroom | bible | story_design | drafts | revisions | release`. Decide by
   ownership, not topic.
4. Route to the folder that owns it. Uncategorized raw material -> `fiction/inbox/`;
   reusable cross-project ideas -> `fiction/knowledge/`; real-world reference
   material -> `fiction/research/`; facts true in a fictional world (continuity/
   world/series-bible) -> `fiction/worlds/<universe-id>/`; work-local operating
   notes, work bible, story design, and boundary -> a section in
   `fiction/projects/<work-id>/README.md`; prose drafts ->
   `fiction/projects/<work-id>/drafts/`. The closed SAGA production track's
   per-work workroom/bible/story-design/revisions/release/archive shelves are
   Git history only (`git show bbbcb970:<path>`); do not recreate them.
   Studio-wide rules belong only in `.agent/workflows/` — there is no separate
   human-readable mirror inside the fiction vault.
5. Stamp each new record with an authoring baseline date and, if it is a bible/scene
   plan, the narrative frame.
## Output
A routing table: item -> state (raw/candidate/canon/archive) -> owning layer ->
target path -> reason. Flag anything that looks like canon so `canon-guardian` can
gate it. Prefer small diffs; do not overwrite existing canon.
## Guardrails
Do not treat raw notes as canon. Do not put universe-wide rules in a workroom. Do not
phrase a fiction premise as a research/status claim. If a web/external source changed
a decision, record URL, allowed claim, blocked claim, and workflow state, or treat it
as unused.

> Provenance: this skill only names external tools (e.g. MarkItDown, PDF intake)
> as workflow references; no external asset was fetched, downloaded, or digitized
> to author it. Per the Research Asset and Product Workflow
> (`.agent/workflows/research-asset-product-workflow.md`), workflow state:
> `no_asset_found`.
