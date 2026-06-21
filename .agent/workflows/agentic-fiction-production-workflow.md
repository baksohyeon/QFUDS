# Agentic Fiction Production Workflow

Use this workflow when an agent plans, drafts, critiques, revises, or verifies
fiction prose or series-level fiction production work.

This workflow is process-only. It does not change research evidence, roadmap
status, canon status, or release status by itself.

Workflow index: [QFUDS Agent Workflows](README.md).

## Relationship To Existing Fiction Workflow

[Fiction IP Management Workflow](fiction-ip-management-workflow.md) decides
where fiction material belongs and what kind of record it is.

This workflow decides how an agent executes a bounded fiction production step
after that routing is known.

Use both workflows for active fiction work:

```text
Fiction IP Management Workflow = classify and route
Agentic Fiction Production Workflow = execute, review, recover state
```

## External System Boundary

External AI writing systems may be used only as architecture inspiration unless
the user explicitly approves installation after a separate security review.

For GitHub repositories, MCP servers, Claude Skills, apps, or code assets, apply
[Research Asset and Product Workflow](research-asset-product-workflow.md) before
writing any source, product-availability, cache, extraction, or installation
claim.

Default boundary for the current SAGA harness:

```text
state: hit_not_cached
use: architecture inspiration only
install: no
copy prompts/code: no
```

## Existing Role Preservation

Do not replace work-local role names that already exist in a SAGA workroom.
Map execution modes onto them.

| Existing SAGA role | Production mode it can perform |
| --- | --- |
| `showrunner` | `critic`, `reader-sim`, `continuity` for arc fit and reveal pacing |
| `worldbuilder` | `continuity`, `chronicler` for institutions, costs, rituals, and canon delta |
| `science_auditor` | `critic`, `continuity` for research/fiction boundary and technical grounding |
| `plot_architect` | `writer`, `critic`, `continuity` for scene pressure and turn/cost |
| `character_room` | `writer`, `reader-sim`, `continuity` for desire, voice, and relationship state |
| `style_editor` | `critic`, `reader-sim`, final `polish` only after structure passes |

One agent may perform multiple modes, but must name the active mode before
making decisions. Do not draft, critique, and canonize in the same unlabelled
pass.

## Required Execution Order

For active series prose or major outline work, use this order:

```text
production board
-> chapter intent card
-> reader onboarding pass
-> writer pass
-> critic / reader-sim pass
-> continuity pass
-> chronicler pass
-> verification
```

Short one-off notes may skip the production board only if they do not create
canon, prose, release-facing revision, or multi-step follow-up.

## Production Board

A production board is the current execution state for a work or sprint. It is
not canon. It records:

- active unit;
- phase: `plan | outline | draft | critique | revise | verify | release`;
- owner mode;
- status: `blocked | in_progress | needs_user | ready_next | done`;
- failure reason;
- next action;
- source files and output files;
- approval needed.

Use [.agent/templates/fiction/saga_production_board_template.md](../templates/fiction/saga_production_board_template.md).

## Chapter Intent Card

Before drafting a chapter, large scene, or episode, create or update an intent
card. It must answer:

- who wants what now;
- what immediate threat makes the scene urgent;
- what choice is forced;
- what each option costs;
- which core dramatic question is planted, triggered, or paid off;
- what must be shown, hidden, or forbidden;
- what pressure hands off to the next unit.

Use [.agent/templates/fiction/chapter_intent_card_template.md](../templates/fiction/chapter_intent_card_template.md).

## Reader Onboarding Pass

Before drafting a scene that depends on technical, legal, institutional, or
world-historical concepts, apply
[Fiction Reader Onboarding Harness](../../docs/wiki/fiction/00_studio/010_reader_onboarding_harness_ko.md).

The pass does not ban technical explanation. It requires each load-bearing
concept to pass:

```text
accurate technical explanation -> simple analogy -> visible loss / choice pressure
```

For QFUDS SAGA, the default mode is technothriller plus in-world documents:
technical explanation is allowed, but it must quickly attach to a deadline,
button, loss, cost, system warning, audit note, seal protocol, court exhibit, or
fieldmark.

## Review Wave Protocol

Do not polish while unresolved foundation issues remain.

Use this order:

```text
foundation scan -> high-severity fix -> re-scan -> continuity fix -> voice polish -> release gate
```

Rules:

- do not let multiple agents edit the same file at the same time;
- do not perform line polish before plot/POV/continuity failures are fixed;
- do not release or promote without a re-scan record;
- record unresolved risks in the production board.

Use [.agent/templates/fiction/review_wave_protocol_template.md](../templates/fiction/review_wave_protocol_template.md).

## Chronicler Pass

After a draft or major revision, recover the state that future agents need:

- new canon facts;
- changed character state;
- opened and closed hooks;
- technical terms introduced;
- continuity risks;
- bible/story_design/revision docs that may need updates.

The chronicler pass proposes canon updates. It does not canonize by momentum.

Use [.agent/templates/fiction/chronicler_pass_template.md](../templates/fiction/chronicler_pass_template.md).

## Style Packet

A style packet is a short context packet for active writing. It reduces the need
to reload long craft documents on every pass, but it cannot override them.

It should preserve:

- Korean-primary prose for active SAGA drafts;
- Korean-first drafting for Korean-primary prose, with no translated logline or
  foreign-language noun-stack intermediate;
- technical terms with plain-language handles;
- person-under-pressure before concept explanation;
- distinct character voice;
- no decorative grandiosity, AI-tell, translationese, or meta-hook slogans such
  as `엔진:`, `핵심은 A가 아니라 B`, or `사건의 주어는 X`.

Use [.agent/templates/fiction/style_packet_template.md](../templates/fiction/style_packet_template.md).
For Korean-primary prose, also apply
[Korean Fiction Prose Naturalness Harness](../../docs/wiki/fiction/00_studio/009_korean_fiction_prose_naturalness_harness_ko.md).

## Truth-State Ledger

For long-form fiction, track what characters know, what readers know, what the
world has institutionally confirmed, and what contradictions remain open.

Use [.agent/templates/fiction/truth_state_ledger_template.md](../templates/fiction/truth_state_ledger_template.md).

## Humanize Boundary

`humanize`-style passes are allowed only as final prose polish after structure,
continuity, and technical grounding pass.

Forbidden uses:

- AI detector evasion;
- changing plot facts to sound more human;
- smoothing away technical terms that carry meaning;
- replacing Korean-primary prose with translationese.

## Verification

Before commit, run the same validation chain required by the fiction workflow:

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/agent_workflow_guard.py --staged
python3 scripts/fiction_gate.py --staged
sh scripts/git-hooks/pre-commit
```

Run `make preflight` when the touched scope makes it practical.
