---
name: fiction-production
description: Execute QFUDS fiction writing, critique, revision, chronicler, and release-prep work using the local agentic fiction production harness. Use when the user asks to write, revise, review, outline, continue, or operationalize QFUDS SAGA fiction.
user-invocable: true
argument-hint: "[optional work/unit/file]"
---

## Required Reading Order

Before changing fiction files, read:

1. `docs/05_next_steps/000_roadmap.md` for current research posture.
2. `.agent/workflows/fiction-ip-management-workflow.md` for routing and boundary.
3. `.agent/workflows/agentic-fiction-production-workflow.md` for production order.
4. `docs/wiki/fiction/00_studio/009_korean_fiction_prose_naturalness_harness_ko.md`
   for Korean-primary prose or polish.
5. `docs/wiki/fiction/00_studio/010_reader_onboarding_harness_ko.md`
   for scenes that depend on technical, legal, institutional, or world-historical concepts.
6. The relevant work README and workroom production board. When you need the
   story itself (premise, world rules, cast, the five dramatic questions, or the
   restoration mechanism), read the SAGA reader orientation first:
   `docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/10_story_design/023_first_arc_reader_orientation_world_and_cast_ko.md`.
7. The chapter intent card, if the task touches prose or a chapter/episode plan.
8. Relevant bible, story_design, draft, and revision docs.

## Execution Modes

Name the active mode before making decisions:

- `writer`: draft or rewrite prose from an approved intent card.
- `critic`: identify structural, POV, pacing, and technical-grounding failures.
- `reader-sim`: report where a target reader loses interest or clarity.
- `continuity`: check canon, chronology, knowledge state, field marks, and terms.
- `chronicler`: recover deltas after drafting or revision.
- `polish`: final language pass only after structure and continuity pass.

## Non-Negotiables

- Fiction is not QFUDS research evidence. (This boundary is NOT lifted.)
- External AI writing tools, MCP servers, prompts, and code MAY be adopted or
  adapted for fiction work (rule relaxed 2026-06-30, user decision), under these
  conditions:
  - check and respect the source license before copying; record it;
  - record source URL, license, allowed claim, blocked claim, and workflow state
    in the changed fiction document (IP workflow source rule + Research Asset and
    Product Workflow);
  - vet MCP servers/tools for security (prompt injection, excess permissions)
    and scope them to the fiction repo/vault before installing;
  - fiction side only — never copy external material into QFUDS research
    evidence, theory, or results;
  - prefer adapting to this project's structure (shelves, Korean-primary, gates)
    over replacing the governance wholesale.
- Korean-primary active SAGA prose comes before English adaptation unless the user explicitly overrides it.
- Draft Korean prose as Korean sentences first. Do not generate a translated
  logline or foreign-language noun stack and then render it into Korean.
- Preserve technical terms when they carry meaning; explain them in-scene.
- `humanize` is final polish only. Do not use it for AI detector evasion or to hide weak structure.
- Do not canonize by momentum. Proposed canon changes go through a chronicler pass and the appropriate bible/story_design/revision destination.

## Output Contract

For prose or major outline work, leave behind:

- updated production board state;
- chapter intent card or explicit note that an existing card was reused;
- reader onboarding note when the scene depends on unfamiliar concepts;
- review wave result for substantial revisions;
- chronicler pass after drafting or revision;
- validation commands run and any residual risk.
