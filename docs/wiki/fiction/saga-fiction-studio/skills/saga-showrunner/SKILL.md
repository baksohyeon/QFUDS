---
name: saga-showrunner
description: >
  Orchestrate a SAGA fiction work session end to end, enforcing the required
  execution order and a production board. Use to start or coordinate a writing sprint
  spanning multiple steps. Triggers: "사가 작업 시작", "이번 챕터 쭉 진행해줘",
  "제작 보드 세팅", "run a saga session", "coordinate this sprint", "plan and draft this
  chapter". Sequences the other skills and never lets drafting, critique, and
  canonization happen in one unlabelled pass.
user-invocable: true
---
# SAGA Showrunner
Entry point and orchestrator. Name the active mode before each decision. One agent
may perform multiple modes, but do not draft, critique, and canonize in the same
unlabelled pass.
SSOT: `.agent/workflows/agentic-fiction-production-workflow.md` (Required Execution
Order, Production Board, Review Wave, Existing Role Preservation) and
`.agent/templates/fiction/saga_production_board_template.md` +
`session_brief_template.md`.
## Required execution order
```
production board -> chapter intent card -> reader onboarding pass -> writer pass
-> critic / reader-sim pass -> continuity pass -> chronicler pass -> verification
```
Short one-off notes may skip the board only if they create no canon, prose,
release-facing revision, or multi-step follow-up.
## Procedure
1. Open or update the Production Board (saga_production_board_template): active unit;
   phase `plan|outline|draft|critique|revise|verify|release`; owner mode; status
   `blocked|in_progress|needs_user|ready_next|done`; failure reason; next action;
   source/output files; approval needed. The board is state, not canon.
2. Map work onto existing SAGA roles (showrunner, worldbuilder, science_auditor,
   plot_architect, character_room, style_editor) — do not invent new role names.
3. Dispatch each phase to the right skill:
   - classification / canon safety -> `canon-guardian`
   - note intake / routing -> `note-curator`
   - intent card + drafting -> `scene-writer`
   - continuity + chronicler recovery -> `continuity-pass`
   - reader comprehension / release gate -> `reader-retention-gate`
4. Enforce the Review Wave order: `foundation scan -> high-severity fix -> re-scan ->
   continuity fix -> voice polish -> release gate`. No line polish before plot/POV/
   continuity failures are fixed. No release without a re-scan record.
5. Do not let two agents edit the same file at once. Record unresolved risks on the
   board. Stop and request the user when a `needs_user` gate is hit.
## Verification
Before commit, run the fiction validation chain (validate_docs, research_consistency,
agent_workflow_guard --staged, fiction_gate --staged, pre-commit) as defined in the
workflow. Never mark a release gate passed without its artifact.
