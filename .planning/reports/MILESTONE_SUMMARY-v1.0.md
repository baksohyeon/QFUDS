# Milestone v1.0 - QFUDS SAGA Fiction Handoff

**Generated:** 2026-06-19
**Purpose:** Handoff for the QFUDS SAGA fiction/IP workstream.

---

## 1. Status

The fiction/IP milestone is complete through revised first-arc v2 drafts.

This is not QFUDS research progress. It is a separate fiction track under
`docs/wiki/fiction/qfuds-saga/`, using QFUDS history as provenance and story
material only.

Current GSD state:

- Phases complete: 17/17
- Plans complete: 17/17
- Active phase: none
- Archive branch target: `codex/qfuds-saga-fiction-archive`
- Latest merged commit: `c5bdeeb docs: revise first arc episodes five six`

## 2. Delivered Work

The milestone built the fiction track from operating system to revised first
arc.

| Phase range | Delivered |
| --- | --- |
| 1 | Fiction/IP GSD harness |
| 2-3 | Cryptographic Death, Hash Covenant, Genesis Chain scene packet |
| 4 | Six-episode first arc outline |
| 5-12 | Rough draft set for Episodes 1-6 |
| 13 | First arc canon consolidation |
| 14 | Full first arc revision control pass |
| 15-17 | Revised v2 drafts for Episodes 1-6 |

## 3. Read Order

Use this order when resuming.

1. `docs/wiki/fiction/qfuds-saga/README.md`
2. `docs/wiki/fiction/qfuds-saga/10_series_bible/008_first_arc_canon_consolidation_ko.md`
3. `docs/wiki/fiction/qfuds-saga/30_drafts/011_first_arc_full_revision_pass.md`
4. `docs/wiki/fiction/qfuds-saga/30_drafts/012_exhibit_s0_episode1_revised_v2_english_draft.md`
5. `docs/wiki/fiction/qfuds-saga/30_drafts/013_the_dead_exchange_revised_v2_english_draft.md`
6. `docs/wiki/fiction/qfuds-saga/30_drafts/014_the_last_hodler_revised_v2_english_draft.md`
7. `docs/wiki/fiction/qfuds-saga/30_drafts/015_identity_flood_revised_v2_english_draft.md`
8. `docs/wiki/fiction/qfuds-saga/30_drafts/016_hawking_court_revised_v2_english_draft.md`
9. `docs/wiki/fiction/qfuds-saga/30_drafts/017_the_broken_crown_revised_v2_english_draft.md`

Older rough drafts remain preserved as provenance. Do not overwrite them unless
the user explicitly asks for replacement.

## 4. Story State

Working title for the first arc: `The Broken Crown`.

Primary story engine:

```text
A restoration court tries to turn proof into possession.
An auditor invents temporary field marks to slow the machine.
Each mark saves someone briefly and teaches power a new grammar.
```

Field mark chain:

| Episode | Field mark |
| --- | --- |
| 1. Exhibit S-0 | `RECOVERABLE / NOT CLAIMABLE` |
| 2. The Dead Exchange | `ACCESS != AUTHORITY` |
| 3. The Last Hodler | `NO CONSENT BY ANALOGY` |
| 4. Identity Flood | `PLURALITY IS NOT CONSENT` |
| 5. Hawking Court | `PHYSICS IS NOT JURISDICTION` |
| 6. The Broken Crown | `who may author loss` |

Arc 1 closes with Mara protected from one claim but not with a clean victory.
The ruling creates `protected pending doctrine`, which is useful enough for
future power to exploit. Arc 2 opens on the question:

```text
Who may author loss?
```

## 5. Boundary

This work is fiction/provenance only.

Do not describe any fiction premise as:

- QFUDS evidence;
- QFUDS support;
- QFUDS validation;
- physical-source derivation;
- Bitcoin prediction;
- black-hole physics claim;
- cryptographic advice;
- legal advice;
- Level 2B admission.

All external-source claims still require the Research Asset and Product
Workflow. The revised v2 fiction loops used existing repo fiction/canon context
only and recorded workflow state as `not searched`.

## 6. Decisions

- English-first prose is the active draft direction.
- Third-person limited Liora POV remains the control point for the first arc.
- Existing rough drafts are preserved; v2 drafts sit beside them.
- The series bible is the place for stable canon. Drafts are readable prose but
  not automatically canon.
- QFUDS-adjacent material is a forbidden fiction temptation, not research
  validation.
- Bitcoin/Genesis Chain is used as artifact, myth, and procedure, not current
  market commentary.

## 7. Deferred Items

Recommended next work, in order:

1. **Arc-level polish/read-order pass**
   - Create a short control document reviewing revised Episodes 1-6 as a
     single read.
   - Check continuity, repeated exposition, field mark misuse risk, and whether
     v2 should become the preferred read order.
   - Do not rewrite all six episodes in this step.

2. **Arc two planning**
   - Build the next six-episode outline around `who may author loss`.
   - Candidate pressure points: Aletheia split, protected pending doctrine,
     H-1 jurisdiction creep, Noor as future POV, Tamas protection, Elias after
     confession.

3. **Series bible refresh**
   - Promote only stable facts from revised v2 into the series bible.
   - Keep open hooks and rejected alternatives separate.

## 8. Verification Already Run

For the revised v2 loops, the following gates passed before commit:

- `python3 scripts/validate_docs.py`
- `python3 scripts/research_consistency.py`
- `python3 scripts/agent_workflow_guard.py --staged`
- `make preflight`
- `sh scripts/git-hooks/pre-commit`

Sensitive-term scans were also run during the revision loops with no matches
for the user-flagged terms in the active fiction/planning paths.

## 9. Resume Instruction

If the next session has less than 15 minutes, do the arc-level polish/read-order
checkpoint first.

If the next session has more time, start Phase 18:

```text
Create a first arc polish/read-order pass for revised Episodes 1-6.
Do not rewrite episode prose yet.
Record preferred read order, continuity issues, exposition cuts, and whether
the v2 drafts should become the active first-arc reading path.
Commit and fast-forward merge into codex/qfuds-saga-fiction-archive.
```
