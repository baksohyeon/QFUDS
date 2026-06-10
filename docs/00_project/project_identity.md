---
doc_id: qfuds_project_identity
title: QFUDS Project Identity
doc_type: overview
stage: reference
status: reference
evidence_role: reference
depends_on:
  - project_overview
  - research_program
  - experiment_summary
  - roadmap
next_gate: use roadmap for current status; use success criteria before new branches
last_updated: 2026-06-10
---

# QFUDS Project Identity

## Current Identity

QFUDS is currently best described as a falsification-first design-space
exploration of quantum-foam-inspired dark-sector models.

It is not a validated physical theory. It is not primarily a phenomenological
model. It is a structured attempt to start from an intuition, turn that intuition
into equations and tests, and identify which parts survive contact with known
cosmology.

Current per-level status lives only in the roadmap:
[docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md).

## Accepted Physical-Branch Audit Classification

Current retained-branch classification: Phenomenological IV/IDE; Not Yet A
Physical Model.

This is a retained-branch classification summary, not a definition of the
entire QFUDS research program and not a roadmap status table. Current level,
blockers, and next gates remain governed by
[docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md).

## Project Scope

QFUDS asks whether dark matter and dark energy can be modeled as two effective
macroscopic phases of a common quantum-spacetime foam sector.

The project is allowed to:

1. compare QFUDS-like ideas with LCDM, unified dark fluids, interacting dark
   energy, interacting vacuum, k-essence, holographic dark energy, and compact
   remnant scenarios;
2. implement toy models and proxy scans when their scope is explicit;
3. reject, demote, or narrow ideas when they fail;
4. preserve failed branches as research evidence;
5. define admission rules for future physical branches.

## Non-Goals

The project should not:

1. present QFUDS as a confirmed physical theory;
2. treat the retained `dF_coll/dln(a)` branch as physical after its [Level 1.5](../wiki/glossary/repository_levels.md)
   demotion;
3. reopen the retained branch without new evidence;
4. claim CMB, matter-power, survey-likelihood, or physical perturbation viability
   from background or Level 2A phenomenological results;
5. use black holes, white holes, entropy, quantum foam, or information language
   as labels without equations and failure criteria.

## Three Different Standards

### Design-Space Exploration

Design-space exploration asks:

```text
Which versions of the idea become equations, which fail, which reduce to known
models, and which need new assumptions?
```

This is the primary current identity of QFUDS.

### Phenomenological Model

A phenomenological model asks:

```text
Can a declared transfer law or closure be tested, constrained, and compared with
known interacting dark-sector models?
```

The retained branch may continue only in this sense: as explicitly labeled
interacting-vacuum or interacting-dark-energy phenomenology. That is useful, but
it is not physical QFUDS by itself.

### Physical Theory

A physical theory asks:

```text
What source, stress-energy transfer, phase response, perturbation prescription,
and known-model distinction make the DM-to-DE phase transition real?
```

The repository has not achieved this standard.

## Retained-Branch Failure Boundary

The retained collapse/information-production branch failed as a physical
Level 1.5 derivation because the repository did not derive the source scalar,
physical mass threshold, transfer four-vector, phase-B vacuum-pressure response,
or `delta Q` route from one mechanism.

That failure rejects only the retained `dF_coll/dln(a)` source relation as a
physical derivation. It does not falsify the broader DM-to-DE phase-transition
hypothesis. Future physical branches must satisfy the admission rule in
[success_criteria.md](success_criteria.md) and the roadmap before they can be
treated as physical QFUDS work.

## What We Actually Learned

Ideas rejected by repository evidence:

- constant `Gamma(a)` at the tested amplitude;
- ungated growth-driven transfer at the tested amplitude;
- broad entropy language as a physical derivation;
- the retained `dF_coll/dln(a)` relation as a physical DM-to-DE source.

Ideas downgraded to phenomenology:

- the retained collapse/information-production transfer shape;
- the P1 interacting-vacuum perturbation closure;
- horizon/information routes that reduce to known interacting or holographic dark
  energy behavior.

Ideas still open:

- the broader DM-to-DE phase-transition hypothesis;
- future physical source mechanisms that provide `X`, `Q^nu`, a phase-B
  rationale, a `delta Q` route, and a known-model distinction;
- phenomenological comparison against interacting-vacuum and interacting-dark
  energy model families.

Ideas worth revisiting only with new assumptions or equations:

- cosmologically coupled black holes;
- holographic or horizon-based sources;
- strong-gravity, remnant, Planck-star, white-hole, or baby-universe mechanisms.

The value of the repository so far is therefore not a successful physical
derivation. The value is a reproducible map of which QFUDS-inspired routes fail,
which overlap known cosmology, which survive only phenomenologically, and what a
future physical branch would need to supply.
