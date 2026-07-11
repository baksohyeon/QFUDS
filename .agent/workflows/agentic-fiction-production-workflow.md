# Agentic Fiction Production Workflow

Use this workflow after fiction material is classified and routed. It governs how an
agent plans, drafts, critiques, revises, verifies, and closes a bounded unit.

## Outcome

Produce readable fiction while keeping creative judgment, canon, continuity,
research, and release evidence distinct.

## Modes

- `curator`: capture and distill raw material
- `architect`: premise, causality, structure, scenes, ending
- `writer`: draft prose
- `critic`: diagnose text against the work contract
- `reader-sim`: report comprehension, expectation, and dropout
- `continuity`: compare facts, chronology, knowledge, and promises
- `chronicler`: recover candidate deltas
- `polish`: target-language sentence pass after higher-order work

Name mode changes. One agent may perform several modes, but should not silently move
from writing to canon approval.

## Risk-Based Tiers

| Tier | Use | Required artifacts |
| --- | --- | --- |
| Quick | brain dump, Zettel, seed, micro-exercise, isolated scene test | intent, output, next decision |
| Chapter | chapter, major scene, substantial rewrite | intent card, draft/revision, focused review, continuity/chronicler note |
| Release | complete short, submission or release candidate | board, baseline, workshop, revision plan, revision memo, continuity, retention gate |

Do not let process documentation outweigh the prose without a stated reason.

## Production Loop

```text
work contract
-> speculative premise and consequence check
-> intent
-> draft
-> author-centered workshop
-> revision plan
-> macro revision
-> continuity/chronicler recovery
-> prose polish
-> revision memo
-> verification
```

Quick work may stop after any useful stage. Chapter and release work may reuse an
existing artifact rather than duplicating it.

## Intent

Before drafting a major unit, state:

- reader promise and unit function;
- scene type;
- POV anchor and knowledge limit;
- speculative rule, limit, and cost active here;
- starting state and required ending change;
- information to reveal, delay, or forbid;
- next-unit pressure.

For a dramatic scene, add current want, resistance, tactics, and choice. Reflective,
observational, documentary, or connective units use their own minimum contract from
the craft harness.

## Workshop

Writer supplies:

- intent under 100 words;
- target reader;
- 1-3 questions;
- deliberate choices not currently open for revision;
- current revision stage.

Reviewer replies:

```text
observation -> reader effect -> evidence ref -> question -> optional suggestion
```

Use `workshop_response_template.md` when the review needs a file artifact.

Separate micro-workshop from manuscript workshop. Conflicting feedback is resolved
against the work contract and text evidence, not by vote.

## Revision

Do not polish while foundation issues remain.

```text
premise/reader contract
-> causality/chronology/POV knowledge
-> scene function and order
-> exposition/onboarding
-> paragraph and rhythm
-> sentence and read-aloud
```

Use `revision_plan_template.md` before editing and `revision_memo_template.md` after.
Record applied, rejected, and deferred feedback. The writer retains the decision.

## Continuity And Chronicler

After substantial prose changes, recover:

- candidate canon facts;
- character physical, emotional, relational, and knowledge-state changes;
- opened, transformed, paid, denied, or forgotten promises;
- technical terms and world rules introduced;
- chronology and POV risks;
- files that may need promotion or repair.

Continuity findings propose changes. Promotion follows the IP workflow.

## Polish

Polish is target-language and work-profile specific. It preserves plot facts,
character voice, narrative frame, register, names, numbers, and direct quotations.

For Korean prose, use the span-based S1/S2/S3 module. Do not use a detector score as
a release gate or rewrite undetected prose merely to sound less machine-generated.
Stop when changes exceed the agreed scope or risk changing meaning.

## Reader Retention

Release-facing work needs an immutable gate artifact tied to a commit and blob hash.
Store it under:

```text
fiction/projects/<work-id>/reviews/retention/
```

Personas report exact stop point, trigger, immersion, clarity, next-unit intent,
strongest hook, and weakest moment. Release is blocked by missing artifacts, open
release-blocking issues, or feedback tied to a moving source.

Retention is evidence about a target audience, not universal literary truth.

## Release Procedure

1. Finish structural revision and commit the source draft as a baseline.
2. Create a candidate under `release/candidates/` without changing its prose.
3. Record baseline commit and blob in the board, retention gate, continuity audit,
   and release checklist.
4. If any fix changes prose, the old evidence remains provenance; commit the fix and
   rerun affected gates against a new baseline.
5. After every release-blocking item is closed, copy the passed candidate unchanged
   to `release/published/`, update the work README, and verify the two blobs match.

Use `release_checklist_template.md`. A release decision cannot refer to an uncommitted
or subsequently edited source.

## Parallel Agents

Parallelize reading, research, and non-overlapping review roles. Never let two agents
edit the same file concurrently. A master agent merges findings against the work
contract and records conflicts rather than averaging them away.

## Verification

Run the validation chain defined in the IP workflow. For release work, also verify
that intent, workshop, revision plan, revision memo, continuity, and retention
artifacts point to the same source baseline.
