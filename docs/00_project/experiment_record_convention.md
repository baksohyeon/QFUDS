---
doc_id: experiment_record_convention
title: QFUDS Experiment Record Convention
doc_type: guide
stage: "1.5"
status: in_progress
evidence_role: ssot
depends_on:
  - frontmatter_convention
  - verification_guide
next_gate: keep Level 2B blocked; use this convention for exp_004 planning
last_updated: 2026-06-09
---

# QFUDS Experiment Record Convention

Date: 2026-06-09

This document defines the minimum research record for every QFUDS experiment.
It complements the frontmatter schema in
[docs/00_project/frontmatter_convention.md](frontmatter_convention.md) and the executable validator in
`scripts/validate_docs.py`.

## Record Chain

Every experiment should have this chain:

```text
theory note or prior result
-> experiment specification
-> code / command / parameters
-> output artifacts
-> result interpretation
-> decision-log entry
-> roadmap update
-> experiment-summary update
```

The roadmap remains the single source of truth for current project status. The
summary document records experiment outcomes, not the current active level.

## Required Experiment Sections

Every document with `doc_type: experiment` must expose these sections:

- `Objective`: what question is being tested.
- `Hypothesis`: what should happen before looking at the result.
- `Scope`: what the experiment can and cannot establish.
- `Method` or `Execution`: command, code path, or process.
- `Parameters` or `Runs`: fixed values, model branch, grid, priors, or variants.
- `Outputs` or `Required Outputs`: files that make the result reproducible.
- `Failure Criteria`: what would kill or narrow the hypothesis.
- `Decision` or `Decision Rule`: how the result will be classified.

These headings are not decoration. They are the audit surface that prevents a
later agent from turning a weak test into a stronger claim.

## Required Result Sections

Every document with `doc_type: result` must expose these sections:

- `Scope`: the strongest claim the result is allowed to support.
- `Evidence` or `Outputs`: generated files, commands, code paths, or inspected
  artifacts.
- `Decision`: what survived, failed, was demoted, or remains unknown.
- `Next Gate`, `Next Test`, or `What Became The Next Target`: the next
  constraint that must be satisfied.

Result documents should also include a plain-language verdict near the top, but
the required sections above are the minimum machine-checkable structure.

## Lightweight Summaries

After every result, update:

```text
docs/04_results/000_experiment_summary.md
```

The summary should list:

- experiment ID;
- scope;
- hypothesis or target;
- primary command or evidence;
- verdict;
- epistemic classification;
- next gate.

This is the answer to "what have we learned so far?" It must not replace the
roadmap's status table.

## Postmortem Policy

Not every result needs a full postmortem. A normal negative result is already
captured in its result document and decision log.

Create a postmortem when any of the following happens:

- a code bug changes diagnostics or conclusions;
- an output artifact is superseded but must be preserved;
- a result is reclassified after hostile review;
- a validation command was wrong or incomplete;
- a document made a claim stronger than the evidence allowed.

Postmortems should record:

- trigger;
- root cause;
- affected files and outputs;
- old conclusion;
- corrected conclusion;
- remaining risk;
- verification command.

Archived postmortems may live under `outputs/postmortem/` when they primarily
preserve generated artifacts. If a postmortem becomes part of the maintained
research record, mirror or move the narrative into `docs/` with
`doc_type: postmortem`.

## Integrity Checks

Run these before treating documentation as current:

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/preflight_exp004.py
```

`validate_docs.py` checks frontmatter and required sections.
`research_consistency.py` checks cross-document status authority.
`preflight_exp004.py` checks the exp_003 to exp_004 transition record.
