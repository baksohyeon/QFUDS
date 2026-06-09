---
doc_id: frontmatter_convention
title: QFUDS Frontmatter Schema Convention
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on: []
next_gate: none; canonical schema reference
last_updated: 2026-06-09
---

# QFUDS Frontmatter Schema Convention

Date: 2026-06-08

This document is the single source of truth (SSOT) for the YAML frontmatter
schema used by every maintained Markdown document under `docs/`. It is the
human-readable companion to the executable check in `scripts/validate_docs.py`.
When this document and the validator disagree, the validator is authoritative and
this document must be corrected to match it.

[PROJECT.md](../../PROJECT.md) and [AGENTS.md](../../AGENTS.md) describe the same
schema for convenience; both defer to this file and to
`scripts/validate_docs.py`.

## Where it applies

Every `*.md` file under `docs/` (recursively) must begin with valid frontmatter.
The validator walks `docs/**/*.md`. Files outside `docs/` (for example
`outputs/postmortem/*/README.md`) are not validated, but should still carry
frontmatter when they are part of the research record.

## Required fields

All nine fields are required on every validated document, in this schema:

```yaml
---
doc_id: string
title: string
doc_type: overview | decision_log | guide | theory_note | experiment | result | summary | postmortem | roadmap | gate | index | reference
stage: "0" | "1" | "1.5" | "2" | "3" | "4" | "5" | "6" | reference
status: draft | completed | in_progress | blocked | provenance | reference
evidence_role: control | hypothesis | proxy_scan | provenance | audit | ssot | reference
depends_on: []
next_gate: string
last_updated: YYYY-MM-DD
---
```

## Allowed values

These enumerations match `scripts/validate_docs.py` exactly.

| Field | Allowed values |
| --- | --- |
| `doc_type` | `overview`, `decision_log`, `guide`, `theory_note`, `experiment`, `result`, `summary`, `postmortem`, `roadmap`, `gate`, `index`, `reference` |
| `stage` | `0`, `1`, `1.5`, `2`, `3`, `4`, `5`, `6`, `reference` |
| `status` | `draft`, `completed`, `in_progress`, `blocked`, `provenance`, `reference` |
| `evidence_role` | `control`, `hypothesis`, `proxy_scan`, `provenance`, `audit`, `ssot`, `reference` |

`doc_id`, `title`, `next_gate`, and `last_updated` are free-form strings;
`depends_on` is a YAML list.

## Rules enforced by the validator

1. **Frontmatter present and terminated.** The file must start with `---\n` and
   contain a closing `\n---\n`.
2. **All required fields present.** Missing any of the nine fields fails.
3. **Enumerated fields use allowed values.** See the table above.
4. **Quote colons.** Any scalar value that itself contains a colon (`:`) must be
   quoted, e.g. `title: "Result 003: Phenomenological Perturbation Closure Audit"`.
5. **H1 matches `title`.** The first `# ` heading in the body must equal the
   `title` field character-for-character.
6. **Unique `doc_id`.** No two documents may share a `doc_id`.
7. **Provenance/reference honesty.** If `status` is `provenance` or `reference`,
   then `evidence_role` must also be `provenance` or `reference`. A document that
   is not physical evidence must say so through metadata, not body text alone.
8. **Sortable filename prefix in active stage dirs.** Files in `docs/02_theory/`,
   `docs/03_experiments/`, `docs/04_results/`, and `docs/05_next_steps/` (except
   [README.md](README.md)) must start with one of the prefixes `000_`, `010_`, `015_`,
   `020_`, `030_`, `040_`, `900_`.
9. **Experiment/result section coverage.** Experiment documents must expose
   objective, hypothesis, scope, outputs, failure criteria, and decision
   sections. Result documents must expose scope, evidence or outputs, decision,
   and next-gate sections. The detailed convention is
   [docs/00_project/experiment_record_convention.md](experiment_record_convention.md).

## Stage prefix meaning

The numeric filename prefix is a sort key only. It does not replace experiment
IDs (`exp_001`), result IDs (`result_001`), or theory labels (`qfuds_v0_15`).

```text
000_ baseline/control
010_ Level 1 / experiment 001
015_ QFUDS v0.15 / Level 1.5 gate
020_ experiment 002
030_ later experiment/result sequence (e.g. exp_003)
040_ Level 2 theory work
040_ Level 3+ theory or interface work when the roadmap unblocks it
900_ broad reference or report
```

## Choosing `status` vs `evidence_role`

- `status` describes lifecycle: is the document `draft`, `in_progress`,
  `completed`, `blocked`, demoted to `provenance`, or a static `reference`?
- `evidence_role` describes epistemic weight: is it a `control`, a `hypothesis`,
  a `proxy_scan`, demoted `provenance`, an `audit`, the `ssot` for some decision,
  or a neutral `reference`?

A background scan demoted after a stronger test should be `status: provenance`
and `evidence_role: provenance`, never left implying it is current evidence.

## How to apply and verify

Run the validator before committing documentation changes:

```bash
python3 scripts/validate_docs.py
```

Exit code `0` and `docs validation passed` means the corpus conforms to this
convention. Any other output lists the offending file and rule.
