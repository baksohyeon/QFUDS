---
name: continuity-pass
description: >
  Recover state and check continuity after a SAGA draft or major revision. Use after
  writing or heavily editing a scene/chapter, or when asked to check for canon
  conflicts. Triggers: "연속성 체크", "캐논 충돌 있나 봐줘", "이번에 뭐 바뀌었어",
  "continuity pass", "chronicler pass", "did this break canon", "update the ledger".
  Extracts new facts, changed character state, opened/closed hooks, and new terms,
  then triages conflicts as confirmed / possible / unknown.
user-invocable: true
---
# Continuity Pass
Run the `continuity` + `chronicler` modes after prose lands. Propose canon updates;
do not canonize by momentum.
SSOT: `.agent/workflows/agentic-fiction-production-workflow.md` (Chronicler Pass,
Truth-State Ledger) and `.agent/templates/fiction/continuity_audit_template.md`,
`chronicler_pass_template.md`, `truth_state_ledger_template.md`.
## Procedure
1. Chronicler recovery — from the new/changed prose, extract:
   - new canon facts (candidate, not yet canon);
   - changed character state (knowledge, position, relationship);
   - opened and closed hooks / dramatic questions;
   - technical terms introduced and their plain-language handles;
   - continuity risks;
   - bible / story_design / revision docs that may need updates.
2. Continuity audit — diff the new material against existing canon (characters,
   timeline, world, terms, field marks). For each finding classify the conflict:
   `confirmed | possible | unknown`. Give the exact source refs on both sides.
3. Truth-state ledger — update what characters know vs what readers know vs what the
   world has institutionally confirmed vs open contradictions.
4. Bilingual alignment — if both KO and EN drafts exist, confirm plot events, field
   marks, character decisions, technical terms, and the research/fiction boundary
   match across languages.
## Output
- a chronicler note (candidate canon deltas, explicitly marked candidate);
- a conflict ledger with severity and confirmed/possible/unknown tags;
- a truth-state update;
- a list of docs needing update, routed via `canon-guardian` (do not edit canon here
  without the guard classification).
## Guardrails
Continuity findings are proposals. Confirmed conflicts must be reported before any
canon edit. Keep records concise and evidence-referenced; do not store long hidden
deliberation. Append, don't overwrite prior state records.
