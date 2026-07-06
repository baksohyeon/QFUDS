---
doc_id: repository_levels_glossary
title: Repository Levels Glossary
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - roadmap
  - level_1_5_resolution_gate
  - perturbation_gate
next_gate: link level mentions to this glossary when touching affected documents
last_updated: 2026-07-06
---

# Repository Levels Glossary

## Purpose

This glossary centralizes QFUDS repository level terminology. It is a reference,
not a status authority. Current level status, active branch, and blockers remain
governed by [docs/05_next_steps/000_roadmap.md](../../05_next_steps/000_roadmap.md).

This file uses only repository evidence. Where the repository does not define a
promotion or demotion rule, this file says so instead of inferring one.

## Audit Method

The terminology audit searched the current tree for:

```text
Level 0
Level 1
Level 1.5
Level 2A
Level 2B
```

Primary command:

```bash
rg -n "Level 0|Level 1\\.5|Level 1|Level 2A|Level 2B" docs AGENTS.md README.md PROJECT.md -g "*.md"
```

Generated outputs, code comments, and output archives also contain level terms,
but this glossary treats maintained Markdown as the documentation surface that
needs backlinks.

## Authority Order

Use these authorities in order:

1. [docs/05_next_steps/000_roadmap.md](../../05_next_steps/000_roadmap.md) for
   current status, evidence, and next gate.
2. [docs/05_next_steps/015_level_1_5_resolution_gate.md](../../05_next_steps/015_level_1_5_resolution_gate.md)
   for Level 1.5 pass, fail, demotion, and future-branch admission rules.
3. [docs/05_next_steps/010_perturbation_gate.md](../../05_next_steps/010_perturbation_gate.md)
   for the Level 2A / Level 2B split.
4. [docs/00_project/decision_log.md](../../00_project/decision_log.md) for why
   Level 1.5 was inserted and why Level 2 was split.
5. [PROJECT.md](../../../PROJECT.md) and
   [docs/00_project/research_program.md](../../00_project/research_program.md)
   for historical validation order.

## Level Summary

| Level | Current authoritative definition | Current status source | Promotion criteria | Demotion criteria |
| --- | --- | --- | --- | --- |
| Level 0 | literature position | roadmap | not explicitly defined beyond comparison/currentness | not explicitly defined |
| Level 1 | background validation | roadmap | not explicitly defined beyond completed background validations | later evidence can demote individual outputs to provenance |
| Level 1.5 | retained phase-transfer physicality | roadmap plus Level 1.5 gate | pass only if transfer is fixed enough for physical Level 2B without new assumptions | fail/demote if `Gamma(a)` remains phenomenological interacting-vacuum transfer |
| Level 2A | phenomenological perturbation closure | roadmap plus perturbation gate | allowed when closure is mathematically closed, covariant/gauge-declared, and explicitly phenomenological | killed or narrowed by unstable, ambiguous, or non-predictive closures |
| Level 2B | physical perturbation closure | roadmap plus perturbation gate | allowed only after a physical branch supplies the admission-rule ingredients | remains blocked if Level 1.5 physical promotion fails or no physical branch is admitted |

## Level 0

### Exact Source File

- [PROJECT.md](../../../PROJECT.md)
- [docs/00_project/research_program.md](../../00_project/research_program.md)
- [docs/05_next_steps/000_roadmap.md](../../05_next_steps/000_roadmap.md)

### Exact Quoted Definition

From [PROJECT.md](../../../PROJECT.md):

```text
Level 0: literature position
```

From [docs/00_project/research_program.md](../../00_project/research_program.md):

```text
### Level 0: Literature Position

Goal:

Find out whether QFUDS is just a rephrasing of existing unified dark fluid,
k-essence, scalar-field dark matter, or interacting dark energy models.
```

From [docs/05_next_steps/000_roadmap.md](../../05_next_steps/000_roadmap.md):

```text
| 0 | literature position | completed | [docs/02_theory/900_qfuds_research_report.md](../../02_theory/900_qfuds_research_report.md) | Keep comparison current as model changes |
```

### First Appearance

Current-tree maintained Markdown first appearance:

```text
PROJECT.md:14:Level 0: literature position
```

Git-history cross-check: first observed in commit `b3dc00d` on 2026-06-08.

### Current Authoritative Definition

Current authoritative definition: the roadmap row says Level 0 is `literature
position`.

### Status Meaning

Roadmap status is `completed`. The next gate is to keep comparison current as
model assumptions change.

### Promotion Criteria

No explicit repository-wide promotion criteria for Level 0 were found beyond
the research-program output list:

```text
comparison table
known limits
first kill criteria
```

### Demotion Criteria

No explicit Level 0 demotion criteria were found.

## Level 1

### Exact Source File

- [PROJECT.md](../../../PROJECT.md)
- [docs/00_project/research_program.md](../../00_project/research_program.md)
- [docs/05_next_steps/000_roadmap.md](../../05_next_steps/000_roadmap.md)

### Exact Quoted Definition

From [PROJECT.md](../../../PROJECT.md):

```text
Level 1: background toy model
```

From [PROJECT.md](../../../PROJECT.md):

```text
Level 1 contains three background validations:

exp_000: zero-transfer LCDM baseline
exp_001: Gamma-law background scan
exp_002: entropy / information-source background gate
```

From [docs/00_project/research_program.md](../../00_project/research_program.md):

```text
### Level 1: Background Cosmology
```

From [docs/05_next_steps/000_roadmap.md](../../05_next_steps/000_roadmap.md):

```text
| 1 | background validation | completed | [docs/04_results/000_result_000_lcdm_baseline.md](../../04_results/000_result_000_lcdm_baseline.md), [docs/04_results/010_result_001_gamma_scan.md](../../04_results/010_result_001_gamma_scan.md), [docs/04_results/020_result_002_entropy_information_gate.md](../../04_results/020_result_002_entropy_information_gate.md), `outputs/`, `tests/test_gamma_v03.py` | Treat experiment 002 as provenance; audit only the retained collapse/information-production shape |
```

### First Appearance

Current-tree maintained Markdown first appearance:

```text
PROJECT.md:15:Level 1: background toy model
```

Search note: [README.md](../../../README.md) contains `Level 1.5` before
[PROJECT.md](../../../PROJECT.md) in a broad `Level 1` text search, so
exact-token searches for `Level 1` must exclude `Level 1.5` when auditing
Level 1.

Git-history cross-check: first observed in commit `b3dc00d` on 2026-06-08.

### Current Authoritative Definition

Current authoritative definition: the roadmap row says Level 1 is `background
validation`.

### Status Meaning

Roadmap status is `completed`. The roadmap says experiment 002 must be treated
as provenance and only the retained collapse/information-production shape should
be audited.

### Promotion Criteria

No explicit repository-wide promotion criteria for Level 1 were found beyond
the completion of the listed background validations.

### Demotion Criteria

No explicit Level 1 demotion rule was found. The repository does define a
demotion outcome for an individual Level 1 result: experiment 002 is provenance,
not current physical evidence.

## Level 1.5

### Exact Source File

- [docs/05_next_steps/000_roadmap.md](../../05_next_steps/000_roadmap.md)
- [docs/05_next_steps/015_level_1_5_resolution_gate.md](../../05_next_steps/015_level_1_5_resolution_gate.md)
- [docs/00_project/decision_log.md](../../00_project/decision_log.md)
- [docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md](../../02_theory/015_qfuds_v0_15_phase_transfer_physics.md)

### Exact Quoted Definition

From [docs/05_next_steps/000_roadmap.md](../../05_next_steps/000_roadmap.md):

```text
| 1.5 | retained phase-transfer physicality | completed for retained branch | [docs/02_theory/015_qfuds_level_1_5_equivalence_source_perturbation_audit.md](../../02_theory/015_qfuds_level_1_5_equivalence_source_perturbation_audit.md), [docs/02_theory/015_qfuds_level_1_5_transfer_four_vector_derivation_attempt.md](../../02_theory/015_qfuds_level_1_5_transfer_four_vector_derivation_attempt.md), [docs/04_results/015_result_001_5_phase_transfer_physicality.md](../../04_results/015_result_001_5_phase_transfer_physicality.md), `qfuds/gamma_laws.py` | Retained branch demoted to phenomenological interacting vacuum; future physical branches must pass the admission rule before reopening Level 1.5 or Level 2B |
```

From [docs/05_next_steps/015_level_1_5_resolution_gate.md](../../05_next_steps/015_level_1_5_resolution_gate.md):

```text
Level 1.5 asks whether this is physical QFUDS transfer or only a useful
phenomenological interacting-vacuum source shape.
```

From [docs/00_project/decision_log.md](../../00_project/decision_log.md):

```text
Insert Level 1.5, phase transfer physicality, before perturbation closure.
```

### First Appearance

Current-tree maintained Markdown first appearance:

```text
PROJECT.md:16:QFUDS v0.15 / Level 1.5: phase transfer physicality
```

Git-history cross-check: first observed in commit `6840282` on 2026-06-08.

### Current Authoritative Definition

Current authoritative definition: Level 1.5 is the retained phase-transfer
physicality gate. For the retained branch, it is completed as a physical
promotion failure and demotion to phenomenological interacting vacuum.

### Status Meaning

Roadmap status is `completed for retained branch`. It does not mean physical
QFUDS passed.

### Promotion Criteria

From [docs/05_next_steps/015_level_1_5_resolution_gate.md](../../05_next_steps/015_level_1_5_resolution_gate.md):

```text
The branch can be promoted from Level 1.5 to physical Level 2B only if the
repository contains evidence for all of the following before fitting to later
observables:
```

The same section lists: derived or justified transfer law, fixed source history,
self-consistent source computation, parameter decision, perturbation-ready
transfer prescription, known-model comparison, distinct test, and reproducible
validation artifact.

Pass statement required by the gate:

```text
The retained transfer law is fixed enough to define physical Level 2B
perturbation equations without adding new assumptions there.
```

### Demotion Criteria

From [docs/05_next_steps/015_level_1_5_resolution_gate.md](../../05_next_steps/015_level_1_5_resolution_gate.md):

```text
Level 1.5 fails as physical QFUDS if the result document must state:

Gamma(a) remains a phenomenological interacting-vacuum transfer law.
```

## Level 2A

### Exact Source File

- [docs/05_next_steps/000_roadmap.md](../../05_next_steps/000_roadmap.md)
- [docs/05_next_steps/010_perturbation_gate.md](../../05_next_steps/010_perturbation_gate.md)
- [docs/02_theory/030_qfuds_phenomenological_perturbations.md](../../02_theory/030_qfuds_phenomenological_perturbations.md)
- [docs/00_project/decision_log.md](../../00_project/decision_log.md)

### Exact Quoted Definition

From [docs/05_next_steps/000_roadmap.md](../../05_next_steps/000_roadmap.md):

```text
| 2A | phenomenological perturbation closure | completed | [docs/02_theory/030_qfuds_phenomenological_perturbations.md](../../02_theory/030_qfuds_phenomenological_perturbations.md), [docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md](../../03_experiments/030_exp_003_phenomenological_perturbation_closure.md), [docs/04_results/030_result_003_phenomenological_perturbation_closure.md](../../04_results/030_result_003_phenomenological_perturbation_closure.md), `outputs/exp003_stability_diagnostics.csv` | P2 failed at retained amplitude; P1 survives only as phenomenological interacting vacuum |
```

From [docs/02_theory/030_qfuds_phenomenological_perturbations.md](../../02_theory/030_qfuds_phenomenological_perturbations.md):

```text
Therefore QFUDS may enter Level 2A:

phenomenological perturbation closure
```

From [docs/05_next_steps/010_perturbation_gate.md](../../05_next_steps/010_perturbation_gate.md):

```text
Level 2A may test whether the current branch is even mathematically usable.
Level 2A may not claim microphysics, novelty, CMB viability, matter-power
viability, or survey-likelihood viability.
```

### First Appearance

Current-tree maintained Markdown first appearance:

```text
PROJECT.md:17:Level 2A: phenomenological perturbation closure
```

Git-history cross-check: first observed in commit `e2e2b73` on 2026-06-08.

### Current Authoritative Definition

Current authoritative definition: Level 2A is a completed phenomenological
perturbation closure level. P1 survives only phenomenologically; P2 failed at
retained amplitude.

### Status Meaning

Roadmap status is `completed`. This means the declared phenomenological closure
audit was completed, not that physical QFUDS perturbations were derived.

### Promotion Criteria

From [docs/05_next_steps/010_perturbation_gate.md](../../05_next_steps/010_perturbation_gate.md):

```text
Phenomenological perturbation closure may begin as Level 2A if the closure is
covariant, gauge-declared, and explicitly labeled as phenomenological.
```

### Demotion Criteria

No separate Level 2A demotion rule was found. The gate gives kill/narrowing
criteria for the branch:

```text
Terminate or narrow the surviving branch if:
```

The listed criteria include gauge ambiguity, instability, phase-B clustering
that breaks vacuum-pressure interpretation, excessive growth changes, reduction
to standard interacting dark energy without a new fixed source relation, and a
failed redshift-ratio relation.

## Level 2B

### Exact Source File

- [docs/05_next_steps/000_roadmap.md](../../05_next_steps/000_roadmap.md)
- [docs/05_next_steps/010_perturbation_gate.md](../../05_next_steps/010_perturbation_gate.md)
- [docs/02_theory/030_qfuds_phenomenological_perturbations.md](../../02_theory/030_qfuds_phenomenological_perturbations.md)
- [docs/00_project/research_program.md](../../00_project/research_program.md)

### Exact Quoted Definition

From [docs/05_next_steps/000_roadmap.md](../../05_next_steps/000_roadmap.md):

```text
| 2B | physical perturbation closure | blocked | retained branch failed Level 1.5 physical promotion | Requires a new physical-QFUDS branch that first provides `X`, `Q^nu`, phase-B vacuum-pressure rationale, `delta Q`, and known-model distinction |
```

From [docs/02_theory/030_qfuds_phenomenological_perturbations.md](../../02_theory/030_qfuds_phenomenological_perturbations.md):

```text
QFUDS may not enter Level 2B:

physical perturbation closure

until Level 1.5 resolves the physical meaning of `Gamma(a)`.
```

From [docs/00_project/research_program.md](../../00_project/research_program.md):

```text
Level 2B requires a physical transfer derivation, including the source, transfer
frame, phase-B response, and perturbation route.
```

### First Appearance

Current-tree maintained Markdown first appearance:

```text
PROJECT.md:18:Level 2B: physical perturbation equations
```

Git-history cross-check: first observed in commit `e2e2b73` on 2026-06-08.

### Current Authoritative Definition

Current authoritative definition: Level 2B is blocked physical perturbation
closure. It requires a new admitted physical branch before work can begin.

### Status Meaning

Roadmap status is `blocked`. The retained branch failed Level 1.5 physical
promotion.

### Promotion Criteria

From [docs/05_next_steps/000_roadmap.md](../../05_next_steps/000_roadmap.md):

```text
Requires a new physical-QFUDS branch that first provides `X`, `Q^nu`, phase-B vacuum-pressure rationale, `delta Q`, and known-model distinction
```

From [docs/05_next_steps/010_perturbation_gate.md](../../05_next_steps/010_perturbation_gate.md):

```text
Open a new physical-QFUDS branch only after it provides `X`, `Q^nu`, a
reason phase B has `w ~= -1`, a `delta Q` route, and a known-model
distinction.
```

### Demotion Criteria

No Level 2B demotion rule was found because Level 2B is not open. The current
rule is blocking, not demotion.

## Relationship Between Levels

The evidence-backed validation order is:

```text
Level 0 literature position
-> Level 1 background validation
-> Level 1.5 retained phase-transfer physicality
-> Level 2A phenomenological perturbation closure
-> Level 2B physical perturbation closure
```

Important boundaries:

- Level 0 and Level 1 are completed filters, not observational validation.
- Level 1.5 decides whether a retained or future transfer branch is physical
  enough to support physical perturbation work.
- Level 2A may proceed as phenomenology without Level 1.5 physical success, but
  it cannot claim microphysics, novelty, CMB viability, matter-power viability,
  or survey-likelihood viability.
- Level 2B cannot proceed from the retained branch. It requires a new physical
  branch that satisfies the admission rule.

## Undefined Usages Found

Strictly, every pre-existing level mention was underdefined before this glossary
because the repository had no single level-terminology reference. More specific
gaps:

- Level 0: no explicit promotion or demotion criteria found.
- Level 1: no explicit repository-wide promotion or demotion criteria found;
  individual Level 1 outputs can be demoted to provenance.
- Level 1.5: well defined, but many documents mention it without linking to the
  gate or roadmap.
- Level 2A: well defined across the roadmap, perturbation gate, and theory note,
  but many documents require roadmap knowledge to know current status.
- Level 2B: well defined as blocked, but many mentions rely on knowing the
  admission rule from the roadmap or gate.

## Circular References Found

No strict definitional cycle was found. The risk is distributed authority:

- [PROJECT.md](../../../PROJECT.md) gives validation order while deferring
  current status to the roadmap.
- The roadmap defines current level status while pointing to evidence docs.
- The Level 1.5 gate defines pass/fail criteria while also deferring current
  status to the roadmap.
- The Level 2 perturbation gate defines the Level 2A/2B split while deferring
  physical-branch admission to Level 1.5 and the roadmap.

This is not circular if readers follow the authority order above. It becomes
confusing when a document mentions a level without linking to this glossary or
to the relevant gate.

## Terminology Requiring Roadmap Knowledge

These phrases require roadmap knowledge unless linked to this glossary:

- `current level`
- `Level 1.5 promotion`
- `failed Level 1.5 physical promotion`
- `Level 2A phenomenology`
- `physical Level 2B`
- `Level 2B remains blocked`
- `Level 3+ physical claims`

## Backlink Rule

Every maintained document that mentions `Level 0`, `Level 1`, `Level 1.5`,
`Level 2A`, or `Level 2B` should link the first substantive mention to this
glossary. Repeated mentions in the same document do not need repeated links.
