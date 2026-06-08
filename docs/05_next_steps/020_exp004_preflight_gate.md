---
doc_id: exp004_preflight_gate
title: Experiment 004 Preflight Gate
doc_type: gate
stage: "2"
status: completed
evidence_role: ssot
depends_on:
  - result_003_phenomenological_perturbation_closure
  - roadmap
  - decision_log
next_gate: keep Level 2B blocked; exp_004 may only be planned after this gate passes
last_updated: 2026-06-08
---

# Experiment 004 Preflight Gate

Date: 2026-06-08

This document defines the repository consistency gate that must pass before any
experiment 004 work begins. It is the human-readable companion to the executable
check in `scripts/preflight_exp004.py`. If the two disagree, the script is
authoritative and this document must be corrected.

This gate does not run physics and does not decide whether QFUDS is correct. It
only verifies that the exp_003 research record — theory note, experiment,
result, decision log, roadmap, and outputs — is complete and internally
consistent before the project spends effort on exp_004.

## Why this gate exists

QFUDS is governed by a documentation-first constitution: documentation, not chat
history, is the source of truth, and no experiment is complete until its
experiment doc, result doc, decision-log entry, and roadmap update all exist and
agree. exp_003 (Level 2A phenomenological perturbation closure) also went through
a hostile-verification correction (the phase-A/phase-B Euler friction bug), so
its record spans several files that must stay mutually consistent.

Advancing to exp_004 on top of an inconsistent or partially documented exp_003
would risk:

- building on outputs that no longer exist or were superseded;
- inheriting a scientific conclusion that the decision log never actually
  ratified;
- silently claiming progress (Level 3 / CLASS / CMB / matter-power) that was
  never earned;
- leaving the documentation index out of sync with the real corpus.

The gate makes those failure modes loud and blocking instead of silent.

## What it checks

`scripts/preflight_exp004.py` runs seven cross-document checks:

1. **exp_003 core documents exist** — the theory note
   (`docs/02_theory/040_qfuds_phenomenological_perturbations.md`), the experiment
   (`docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md`),
   and the result
   (`docs/04_results/030_result_003_phenomenological_perturbation_closure.md`)
   are all present.
2. **Postmortem note (if referenced)** — if the result doc or decision log
   references `outputs/postmortem/exp003_friction_bug`, that directory and its
   `README.md` must exist. A referenced but missing postmortem is a blocker.
3. **Decision log has the final exp_003 verdict** — `decision_log.md` records the
   exp_003 outcome (P2 regularized-fluid closure failed, P1 interacting-vacuum
   closure survives as non-novel Level 2A) and the friction-bug correction.
4. **Roadmap reflects Level 2A status** — the roadmap marks Level 2A
   `completed` and keeps Level 2B, CLASS integration, CMB comparison, and matter
   power spectrum `blocked`.
5. **Referenced outputs exist** — every `outputs/*.csv`, `*.json`, or `*.png`
   path cited by the exp_003 documents actually exists on disk.
6. **No premature completion claims** — no document under `docs/` (or the root
   `README.md`) claims Level 3 / CLASS / CAMB / CMB / matter-power completion or
   viability.
7. **Docs index is complete** — `docs/README.md` references every active
   (non-index) Markdown document under `docs/`.

This gate is complementary to `scripts/validate_docs.py`, which validates
per-document frontmatter schema. The preflight gate validates cross-document
state for the exp_003 → exp_004 transition.

## How to run it

There is no `Makefile` in this repository, so run the gate directly:

```bash
python3 scripts/preflight_exp004.py
```

Run the schema validator alongside it:

```bash
python3 scripts/validate_docs.py
```

If a `Makefile` is later added, expose the gate as:

```bash
make preflight-exp004
```

## What failure means

A non-zero exit code means the exp_003 record is not yet consistent enough to
build exp_004 on. The script prints each failing check and a `Blockers` list.
Failure does **not** mean a scientific result is wrong; it means the record is
incomplete or contradictory. Typical causes:

- a referenced output file was moved or deleted;
- the decision log or roadmap was not updated after a correction;
- a new active document was added but never indexed in `docs/README.md`;
- a document started claiming downstream (Level 3+) completion that has not been
  earned.

## What must be fixed before exp_004

Before exp_004 may be planned:

1. `python3 scripts/preflight_exp004.py` must exit `0`.
2. `python3 scripts/validate_docs.py` must exit `0`.
3. Any blocker the gate reports must be resolved by **correcting the record**,
   not by weakening the check. Stale or contradictory documents must be fixed or
   demoted to provenance with honest frontmatter; scientific conclusions must not
   be silently rewritten to make the gate pass.

Passing this gate authorizes only the *planning* of exp_004. It does not lift any
physics blocker: Level 2B, CLASS/CAMB, CMB, matter-power, and survey-likelihood
work remain blocked under the roadmap and the Level 2 perturbation gate.
