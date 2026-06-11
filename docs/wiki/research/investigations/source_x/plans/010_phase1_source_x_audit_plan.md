---
doc_id: audit_2026_06_10_source_x_audit_plan
title: "2026-06-10 Source-X Audit Plan"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - roadmap
  - repository_levels_glossary
  - wiki_governance_004_missing_physics_map
  - wiki_governance_003_blocked_admission_rule_gate
  - wiki_governance_001_physical_branch_summary
  - safe_future_branch_candidates
next_gate: source-x audit only; no roadmap upgrade and no physical Level 2B opening
last_updated: 2026-06-11
---

# 2026-06-10 Source-X Audit Plan

## File Path

Create the Source-X audit plan at:

```text
docs/wiki/research/investigations/source_x/plans/010_phase1_source_x_audit_plan.md
```

This file is the plan for the next audit stage. It is not the audit result and
does not add a new experiment, new theory branch, or roadmap status update.

## Purpose

The Source-X Audit asks:

```text
What physical source scalar X could make Gamma(a) more rigorous, replace it, or
show that it should remain only phenomenological?
```

The audit must identify whether any candidate source scalar `X` can replace,
derive, constrain, or reject the retained prototype timing profile without
treating the current `Gamma(a)` as a physical law.

Do not assume `X` exists. Do not assume current `Gamma(a)` is correct. Do not
assume collapse history is the source.

## Status Boundary

This is an audit task, not a theory-building task.

The Source-X Audit must not:

- open Physical-QFUDS [Level 2B](../../../../glossary/repository_levels.md);
- upgrade the roadmap;
- create a new physical branch;
- prove or rescue the current retained `Gamma(a)`;
- define all QFUDS as IV/IDE;
- use information, entropy, white-hole, remnant, or quantum-foam language as a
  physical source without equations, observables, and stress-energy relation.

Current status remains governed by
[docs/05_next_steps/000_roadmap.md](../../../../../05_next_steps/000_roadmap.md).

## Required Status Wording

Use this wording in the audit where relevant:

```text
Current retained-branch classification:
Phenomenological IV/IDE; Not Yet A Physical Model.

This classification applies to the current retained branch only. It does not define the entire QFUDS research program.

Gamma(a) is a prototype phenomenological transfer profile, not a derived physical law.

The Source-X Audit must not prove Gamma(a). It must determine whether any source X can replace, derive, constrain, or reject it.
```

## Evidence Scan Before External Literature

Before proposing new external literature work, scan the existing repository
evidence anchors listed in [Required Evidence Anchors](#required-evidence-anchors).

The audit must reuse existing literature notes as anchors. It must not duplicate
existing literature tables, paper summaries, or dated availability audits.

If a needed literature family is already represented in
[docs/wiki/research/literature/index.csv](../../../literature/index.csv), route through
that cache record. If a needed external source is absent, record the missing
source as a gap instead of inventing a file or conclusion.

## Candidate X Lanes

The audit must include at least the six lanes below. Each lane must fill every
field in [Per-Lane Audit Template](#per-lane-audit-template).

### Lane 1: Collapse-History Source

Audit whether collapse history can define a source scalar rather than only a
timing proxy.

Minimum candidates:

- `dF_coll / dln(a)`;
- halo formation;
- nonlinear structure formation.

Required boundary: collapse timing is not enough. This lane must test whether
the source can be defined without circularly importing the retained `Gamma(a)`
and whether it can explain transfer into smooth phase B.

### Lane 2: Black-Hole-Coupled Source

Audit whether black-hole production, growth, or entropy histories can define a
candidate `X`.

Minimum candidates:

- black-hole production history;
- black-hole mass growth;
- black-hole entropy proxy.

Required boundary: black-hole information storage, entropy growth, or compact
object abundance does not by itself imply vacuum-pressure phase B.

### Lane 3: Horizon / HDE Source

Audit whether a horizon or holographic route can replace the retained timing
profile, or whether it reduces QFUDS to a known model family.

Minimum candidates:

- horizon-scale energy density;
- IR cutoff relation;
- reduction to known HDE or interacting vacuum.

Required boundary: this is a reduction test, not a novelty claim. If the lane is
standard HDE or interacting vacuum with QFUDS labels, record that failure.

### Lane 4: Causal-Set / Stochastic Lambda Source

Audit causal-set or stochastic-Lambda behavior as an adjacent dark-energy
comparison only.

Minimum candidates:

- Lambda fluctuation;
- causal-set volume scaling;
- comparison only, not adoption.

Required boundary: this lane is not a DM-to-DE phase-transfer branch unless it
also supplies `X`, `Q^nu`, phase-B rationale, `delta Q`, and known-model
distinction.

### Lane 5: Remnant-Sector Source

Audit remnants as compact-object, defect-sector, or DM-only candidates unless a
vacuum-pressure route is actually derived.

Minimum candidates:

- Planck remnants;
- white-hole remnants;
- DM-only audit unless a vacuum-pressure route is derived.

Required boundary: do not use remnants as a dark-energy source without a smooth
`w ~= -1` stress-energy relation.

### Lane 6: Information / Entropy Source

Audit whether information or entropy production can become a physical source
only if it supplies equations, observables, and stress-energy relation.

Minimum candidates:

- Landauer;
- information production;
- entropy production.

Required boundary: reject information or entropy language as a physical source
unless it defines source units, normalization, transfer law, observables, and
phase-B stress-energy.

## Per-Lane Audit Template

For each candidate lane, the Source-X Audit must fill all fields below:

```text
source definition
units
normalization
required data or literature source
relation to Gamma(a)
relation to Q^nu
whether it can explain phase B having w ~= -1
whether it can define delta Q
closest known model family
expected failure mode
what would count as progress
what would not be enough
```

The audit must state `unknown` for missing fields rather than filling gaps with
analogy or naming.

## Audit Criteria

A candidate `X` is meaningful only if it can be evaluated against the five
blocked admission-rule items:

```text
X =
Q^nu =
why phase B has w ~= -1 =
delta Q route =
known-model distinction =
```

The audit must ask whether the lane can:

- define a scalar or source history with units and normalization;
- relate that source to the background transfer without circular use of
  retained `Gamma(a)`;
- supply or point toward a covariant transfer relation `Q^nu`;
- explain why the receiving component behaves as smooth vacuum-pressure phase B;
- define a perturbation route for `delta Q`;
- distinguish itself from LCDM, unified dark fluid, IV/IDE, HDE,
  black-hole-coupled DE, remnant DM, or causal-set Lambda;
- produce a falsifiable observable, failure condition, or reproducible next
  audit step.

## Failure Criteria

Reject or demote a lane if it only supplies:

- a visually similar timing curve;
- a renamed `Gamma(a)`;
- broad entropy, information, foam, black-hole, or white-hole language;
- a conservation-compatible `Q^nu` ansatz with no physical source;
- collapse history copied from standard growth without self-consistency;
- compact remnants, radiation, heat, or disconnected sectors instead of smooth
  phase-B vacuum pressure;
- known HDE, IV/IDE, causal-set Lambda, or remnant-DM behavior with no distinct
  QFUDS prediction;
- no route to `delta Q` or perturbation stability testing.

## What Counts As Progress

Progress means the audit identifies at least one lane that can supply a sharper,
testable next step without opening Level 2B.

Examples of progress:

- a candidate `X` with declared units, normalization, and data source;
- a clear reason a lane fails one of the five admission-rule items;
- a reduction result showing the lane is a known model family;
- a reproducible follow-up audit or experiment proposal with predeclared failure
  criteria;
- a decision that current `Gamma(a)` should remain phenomenological, be
  replaced, be constrained, or be discarded.

## What Is Not Enough

The following do not count as progress:

- saying a source "looks like" retained `Gamma(a)`;
- treating current `Gamma(a)` as the target law to prove;
- treating background-only timing overlap as physical derivation;
- using external literature as support without matching variables, units, and
  model family;
- duplicating literature-cache summaries instead of referencing them;
- moving a speculative lane into theory or roadmap status before it satisfies
  the admission rule.

## Required Evidence Anchors

Scan these repository files before adding new literature work:

- [docs/05_next_steps/000_roadmap.md](../../../../../05_next_steps/000_roadmap.md)
- [docs/wiki/glossary/repository_levels.md](../../../../glossary/repository_levels.md)
- [docs/wiki/governance/004_missing_physics_map.md](../../../../governance/004_missing_physics_map.md)
- [docs/wiki/governance/003_blocked_admission_rule_gate.md](../../../../governance/003_blocked_admission_rule_gate.md)
- [docs/wiki/governance/001_physical_branch_admission_summary.md](../../../../governance/001_physical_branch_admission_summary.md)
- [docs/05_next_steps/010_safe_future_branch_candidates.md](../../../../../05_next_steps/010_safe_future_branch_candidates.md)
- [docs/04_results/015_result_001_5_phase_transfer_physicality.md](../../../../../04_results/015_result_001_5_phase_transfer_physicality.md)
- [docs/04_results/030_result_005_timing_prior_usefulness.md](../../../../../04_results/030_result_005_timing_prior_usefulness.md)
- [docs/04_results/030_result_006_literature_timing_support_audit.md](../../../../../04_results/030_result_006_literature_timing_support_audit.md)
- [docs/02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md](../../../../../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md)
- [docs/02_theory/015_qfuds_level_1_5_transfer_four_vector_derivation_attempt.md](../../../../../02_theory/015_qfuds_level_1_5_transfer_four_vector_derivation_attempt.md)
- [docs/wiki/lineage/001_qfuds_genealogy.md](../../../../lineage/001_qfuds_genealogy.md)
- [docs/wiki/lineage/002_branch_graph.md](../../../../lineage/002_branch_graph.md)
- [docs/wiki/research/literature/README.md](../../../literature/README.md)
- [docs/wiki/research/literature/index.csv](../../../literature/index.csv)
- [docs/wiki/research/investigations/](./)

## Missing References

No checked requested evidence anchor is missing.

The target file
[docs/wiki/research/investigations/source_x/plans/010_phase1_source_x_audit_plan.md](010_phase1_source_x_audit_plan.md)
is intentionally new.

## Confirmations

- Roadmap remains SSOT for current status:
  [docs/05_next_steps/000_roadmap.md](../../../../../05_next_steps/000_roadmap.md).
- `repository_levels.md` remains SSOT for level terminology:
  [docs/wiki/glossary/repository_levels.md](../../../../glossary/repository_levels.md).
- `004_missing_physics_map.md` remains SSOT for missing admission-rule items:
  [docs/wiki/governance/004_missing_physics_map.md](../../../../governance/004_missing_physics_map.md).
- No roadmap upgrade is made by this plan.
- No Level 2B opening is made by this plan.
- No new physical branch is created by this plan.
- No `Gamma(a)` proof attempt is made by this plan.
- Existing literature docs are reused as anchors.
- No duplicated literature summary is added.

## Verification

After creating or editing this file, run:

```bash
rtk python3 scripts/validate_docs.py
rtk git diff --check
```
