# Fiction IP Management Workflow

Use this workflow to capture, classify, route, promote, or move fiction material.
It governs the repository-root `fiction/` studio and is independent of QFUDS research
status.

Workflow index: [Repository Agent Workflows](README.md).

## Core Boundary

Fiction may borrow scientific questions from QFUDS, but fiction is never QFUDS
research evidence. `docs/wiki/fiction/` is legacy read-only. Do not route active
work there or recreate its old shelves. Historical material may be cited only as a
Git-history source such as `git show bbbcb970:<path>`.

## Authority Layers

Decide ownership before editing:

```text
studio method
-> reusable Zettelkasten knowledge
-> real-world fiction research
-> universe/world continuity
-> work Home Note and local design
-> draft
-> review/revision evidence
-> release candidate
```

| Layer | Active home |
| --- | --- |
| Studio workflow, templates, agent skills | `.agent/`, `.agents/`, `creative_harness/`, `tools/` |
| Raw capture | `fiction/inbox/` |
| Cross-project ideas and craft tools | `fiction/knowledge/` |
| Real-world research for fiction | `fiction/research/` |
| Facts adopted by a fictional world | `fiction/worlds/<universe-id>/` |
| Work contract, bible/design summary, current map | `fiction/projects/<work-id>/README.md` |
| Prose | `fiction/projects/<work-id>/drafts/` |
| Review and revision artifacts | `fiction/projects/<work-id>/reviews/` when needed |
| Fixed release candidates | `fiction/projects/<work-id>/release/candidates/` |
| Published snapshots | `fiction/projects/<work-id>/release/published/` |

Do not duplicate the same fact across layers. Lower layers link to the authority they
inherit.

## Brain Dump And Zettelkasten Route

Unstructured input is allowed. Capture it without promoting it.

```text
brain dump / article / fragment
-> inbox
-> distill reusable thought to knowledge/notes
-> connect through knowledge/maps
-> combine into knowledge/seeds
-> user promotes a seed to a project
-> project linearizes it into scenes and prose
```

Follow
[Zettelkasten fiction intake](../../creative_harness/methods/zettelkasten_fiction_intake_method.md).
Original Zettels remain in knowledge; projects link rather than copy them.

## Classification Checklist

Before a write or move, answer only the relevant items:

1. Is it raw, candidate, accepted, retired, or release-facing?
2. Is it reusable thought, real-world research, world fact, work design, prose, or
   review evidence?
3. Which universe and work own it, if any?
4. What does it inherit and what is a local override?
5. Does it change canon, character knowledge, chronology, terminology, or promises?
6. Does it touch an external source or tool?
7. What is the smallest artifact and validation needed?

Raw material and agent-generated proposals are never canon by momentum.

## Project Home Contract

Every work has one hand-maintained entrypoint:

```text
fiction/projects/<work-id>/README.md
```

The README is the project's Home Note. Do not also require `HOME.md` or `story.md`
for a new work.

Minimum fields:

- universe or `standalone`;
- form, target reader, genre/subgenre contract;
- language and style profile;
- authoring baseline and in-world chronology when relevant;
- premise and speculative change;
- source Zettels and research;
- inherited world rules and local overrides;
- narrative frame and POV;
- central conflict, ending hypothesis, open questions;
- current draft and one next action;
- current canon state and promotion rule.

Optional growth paths:

- add `reviews/` after substantial workshop or revision evidence exists;
- adopt `tools/story-skills` schema only when long-form continuity work justifies it;
- never add files solely because a template offers them.

## Release State Transition

Release work uses immutable evidence, not a moving draft.

```text
drafting/revising
-> commit the candidate source baseline
-> copy the exact candidate to release/candidates/
-> run workshop, continuity, retention, and release checklist against commit + blob
-> if prose changes, commit a new baseline and create new gate artifacts
-> when all release blockers are closed, copy the passed candidate unchanged to
   release/published/ and set the work README state to released
```

Naming:

```text
release/candidates/<work-id>_<version>_<baseline-shortsha>.md
release/published/<work-id>_<version>.md
reviews/release/<work-id>_release_check_<version>_<baseline-shortsha>.md
```

`released` means the published snapshot is byte-identical to the candidate that
passed the recorded gate, and the work README records version, date, destination,
baseline commit, and blob. A submission package not yet public may use `submission`
state and the candidates shelf without a published copy.

## Universe And Canon Rule

Create a new universe only when inherited physics, history, institutions, or genre
contract would mislead the reader. Otherwise create a new work under an existing
universe and record local overrides.

World states:

- `provisional`: candidate used for exploration;
- `accepted`: current authority for that universe;
- `retired`: preserved but no longer active.

Canon promotion requires:

1. owning universe/work identified;
2. conflicts checked against current authority;
3. proposed delta listed;
4. user or recorded project rule approves promotion;
5. affected links, chronology, and knowledge state updated.

Drafting can propose canon. It cannot approve it.

## Work-Local Profiles

Global workflow does not impose:

- Korean-first or English-first;
- a fixed POV or character arc model;
- em dash or word bans;
- technothriller, literary, web-novel, or hard-SF pacing;
- bilingual sibling drafts;
- specific QFUDS terms, roles, or dramatic questions.

Record those decisions in the work README and style packet. A target-language draft
should be composed directly in that language. Translation and adaptation are separate
only when the work chooses that policy.

## Craft Rule

Before a major scene, chapter, or revision, apply
[SF Creative Writing Craft Harness](../../creative_harness/craft/creative_writing_craft_harness.md).

Optional modules:

- Korean prose naturalness;
- reader onboarding for unfamiliar concepts;
- social/institutional verisimilitude;
- university workshop benchmark.

Scene type determines the minimum contract. Do not force every scene into the same
want-obstacle-turn-cost formula.

## External Source And Tool Rule

For sources used only for fiction, follow
[Fiction Source Intake Workflow](fiction-source-intake-workflow.md). Run the
[Research Asset and Product Workflow](research-asset-product-workflow.md) separately
only if the source also supports a QFUDS research claim.

Every adopted method or copied asset records:

- source id, URL, access date, and workflow state;
- license when copying or modifying;
- allowed and blocked claims;
- whether content was inspected, copied, adapted, installed, or only referenced;
- security scope for executable tools;
- owning fiction document or profile.

Inspection does not authorize installation. Paraphrased methods do not authorize
copying source prose. Do not claim an asset is absent until a scoped search was
actually run.

## Story Skills Boundary

`tools/story-skills` is a vendored MIT-licensed submodule with deterministic checks
for schema, links, chronology, character state, promises, and questions. It is an
optional long-form engine, not the global creative authority.

For a new or small work, use README + drafts. Adopt Story Skills only after an
adapter/import plan maps current files without destroying author-owned structure.
Run its own tests and validators inside the submodule when used.

## Validation

For fiction/control-document changes, run:

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/check_markdown_link_targets.py creative_harness .agent .agents fiction tools/saga-fiction-studio
python3 scripts/agent_workflow_guard.py --staged
python3 scripts/fiction_gate.py --staged
sh scripts/git-hooks/pre-commit
```

Run `make preflight` when the touched scope makes it practical. If a work adopts
Story Skills, also run its `story validate`, `story links`, and `story continuity`
checks.
