---
doc_id: <work>_retention_gate_run_<YYYYMMDD>_<baseline-shortsha>
title: <Work> Retention Gate Run <YYYY-MM-DD> <baseline-shortsha>
doc_type: gate
stage: reference
status: in_progress
evidence_role: provenance
depends_on:
  - <retention_gate_protocol_or_previous_run_doc_id>
next_gate: complete persona sheets, issue ledger, decision, and verification before release promotion
last_updated: 2026-06-22
---

# <Work> Retention Gate Run <YYYY-MM-DD> <baseline-shortsha>

## Frontmatter Rules

Use this frontmatter for actual retention gate **run artifacts** under `docs/`.
Protocol/specification documents may use `doc_type: guide`, but a run that can
block or permit release must use `doc_type: gate`.

Field choices:

- `doc_type: gate` because this artifact records a formal pass/fail gate.
- `stage: reference` because fiction release gates are not QFUDS research levels.
- `status: in_progress` while sheets are being filled, `completed` after a
  final decision, or `blocked` if the run cannot finish.
- `evidence_role: provenance` because fiction feedback is process provenance,
  not research evidence.
- `depends_on` must include the protocol document and, for reruns, the previous
  gate run artifact.

## Metadata

- Work id:
- Gate id:
- Scope:
- Source draft(s):
- Baseline commit/date:
- Gate owner mode: `reader-sim` + `critic` + `chronicler`
- Production board:
- Revision shelf output:
- Release target:

## Immutable Run Rule

This document is a gate run artifact, not a rolling scratchpad. Do not overwrite
a completed gate run when the draft changes. Create a new gate document for each
new baseline.

Recommended naming:

```text
30_revisions/<NNN>_<work>_retention_gate_run_<YYYYMMDD>_<baseline-shortsha>.md
```

If feedback is re-run after edits, record the previous run in `depends_on` and
create a new run artifact. The prior artifact remains provenance.

## Boundary

```text
fiction/provenance only
research evidence: no
release promotion without this artifact: no
raw private reasoning: do not record
```

## Source Baseline

Each reviewed draft must be pinned to a git commit and blob hash. Feedback
without a source baseline is not actionable.

Commands:

```bash
git rev-parse HEAD
git rev-parse HEAD:<path>
```

| Source id | Path | Baseline commit | Blob hash | Notes |
| --- | --- | --- | --- | --- |
| S1 | TBD | TBD | TBD | TBD |

## Persona Set

| Persona id | Reader profile | What this persona tests | Stop rule |
| --- | --- | --- | --- |
| P1 | TBD | TBD | stop at the first real loss of interest or confusion that would make this reader quit |

## Reading Units

Use `baseline commit:path#Lx-Ly` for every unit. Line numbers are interpreted at
the baseline commit, not after later edits.

| Unit id | Source ref | Blob hash | Role in release | Expected hook |
| --- | --- | --- | --- | --- |
| U1 | TBD | TBD | TBD | TBD |

## Persona Result Sheets

Every persona must fill one row per reading unit. Do not summarize the gate as
"all passed" unless this table exists.

`Stop source ref` must use the same baseline reference form as the reading
units. If the persona completes the unit, write `completed` and still record the
weakest moment source ref when possible.

| Persona | Unit | Completed? | Stop source ref | Stop trigger | Immersion score 1-10 | Clarity score 1-10 | Next-unit intent | Strongest hook | Weakest moment source ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Cross-Persona Evidence Matrix

| Unit | Median immersion | Lowest immersion persona | Common stop trigger | Repeated confusion | Strong hook consensus |
| --- | --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | TBD | TBD |

## Issue Ledger

Severity:

- `S0`: release-blocking dropout or continuity break.
- `S1`: repeated confusion, boredom, or AI-tell across 3+ personas.
- `S2`: local weakness across 1-2 personas.
- `S3`: taste note or optional polish.

| Issue id | Severity | Evidence personas | Source ref | Failure mode | Proposed fix | Owner mode | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RET-001 | TBD | TBD | TBD | TBD | TBD | TBD | `open | fixed | deferred | rejected` |

## Decision

Gate state:

```text
not_run | invalid_no_artifact | ran_failed | ran_passed_with_risks | ran_passed
```

Pass requires:

- every persona result sheet is filled;
- no `S0` remains open;
- every `S1` is either fixed or explicitly deferred with rationale;
- revision wave links every fixed issue to changed files;
- every issue links to a baseline source ref;
- production board records the gate id and decision.

Decision:

```text
TBD
```

## Revision Mapping

| Issue id | Fix wave/doc | Baseline source ref | Changed files | Fix commit/blob | Verification | Residual risk |
| --- | --- | --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Verification

Required before this gate can support release promotion:

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/agent_workflow_guard.py --staged
python3 scripts/fiction_gate.py --staged
sh scripts/git-hooks/pre-commit
```
