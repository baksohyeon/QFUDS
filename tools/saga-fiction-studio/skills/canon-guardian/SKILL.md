---
name: canon-guardian
description: >
  Guard SAGA/web-novel canon before any edit. Use before creating, moving, editing,
  or extending fiction material under the repository-root fiction/ vault — bible,
  world, timeline, terms, character sheets, continuity records, or anything that
  could become canon.
  Triggers: "정본 수정", "이거 캐논 맞아?", "설정 바꿔줘", "이 문서 옮겨줘", "add this to the bible",
  "edit canon", "is this canon", "update the timeline/world/character". Classifies the
  change, reads the related canon first, and reports conflict risk BEFORE editing.
user-invocable: true
---
# Canon Guardian
Manage fiction like an IP studio, not loose documents. This skill runs BEFORE any
canon-touching edit. It never canonizes by momentum.
SSOT (read the relevant one, do not restate it here):
`.agent/workflows/fiction-ip-management-workflow.md` and
`.agent/workflows/documentation-folder-routing-workflow.md`.
## When to run
Run before any create/move/edit/extend on `fiction/`, especially
`worlds/<universe-id>/series-bible/`, `worlds/<universe-id>/world/`,
`worlds/<universe-id>/continuity/`, timeline, terms, or character docs, or a
project's "Work Bible" section in `fiction/projects/<work-id>/README.md`.
Short one-off notes that create no canon may skip this.
## Procedure
1. Classify the change by ownership, not topic, using the layer ladder:
   `studio -> catalog -> universe/IP -> continuity -> work -> workroom -> bible ->
   story_design -> drafts -> revisions -> release`. State which layer owns it.
2. Answer the Classification Checklist in the IP-management workflow (canon status:
   canon / soft-canon / elseworld / prototype / retired / unclassified; universe
   owner; inherited rules vs local override; authoring baseline date; narrative
   frame if a bible/scene plan).
3. Read the related canon FIRST — before editing — for every entity the change
   touches: relevant character sheets, timeline files, world/institution docs,
   term definitions, and continuity records. Use `.agent/templates/fiction/` sheets
   (character_sheet, work_bible, universe_readme) as the shape.
4. Report conflict risk BEFORE writing anything. Separate every claim into:
   `confirmed canon | candidate idea | interpretation | discarded/archive`.
   Never present a candidate as canon.
5. Enforce routing: canon lives only in its owning folder; drafts never go in
   `series-bible/`; universe-wide rules never go in a project's "Work Bible"
   section. Use `fiction/worlds/<universe-id>/series-bible/` for shared universe
   canon and `fiction/projects/<work-id>/` (README sections + `drafts/`) for
   work-local material; the closed SAGA production track's per-work
   bible/story-design/drafts/revisions/release/archive shelves are Git history
   only (`git show bbbcb970:<path>`).
6. If a work folder has no README, block bible/design/draft additions until a work
   README exists (Work README Contract).
7. Preserve load-bearing technical terms (hash, KDF, key, entropy, Page curve, AGI,
   QFUDS…). A fictional alias is allowed only with a recorded rationale.
## Output
- the layer classification and canon status;
- the related canon you read and any conflict, tagged confirmed / possible / unknown;
- a go / fix-first recommendation;
- only after the user confirms, make the edit as small a diff as possible.
## Guardrails
Do not decide canon by momentum. Do not skip the universe/continuity classification.
Do not add drafts before a work README exists. Prefer small diffs. Hand off to
`continuity-pass` after the edit lands.
