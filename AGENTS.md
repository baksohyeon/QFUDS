# AGENTS.md

# Quantum Foam Unified Dark Sector (QFUDS) Agent Constitution

This repository is an active early-stage cosmology research program. Future AI
agents must treat this file as the operating constitution for all work in the
repository.

QFUDS is not a confirmed theory. QFUDS is a speculative research program asking
whether dark matter and dark energy can be modeled as two effective macroscopic
phases of a common quantum-spacetime foam sector.

The goal is not to prove QFUDS correct. The goal is to determine whether QFUDS
survives progressively stronger tests.

## Project Status Authority

This constitution defines **process, not status**. It deliberately does not record
the current level, the active branch, the current blockers, or what has survived
or failed. That state drifts and must live in exactly one place.

Current project state lives in
[docs/05_next_steps/000_roadmap.md](docs/05_next_steps/000_roadmap.md).

That roadmap is the single source of truth for:

- current project status and current level;
- the active branch and what is in progress;
- current blockers.

Supporting authority, in order:

- [docs/00_project/decision_log.md](docs/00_project/decision_log.md) records
  _why_ each decision was made;
- [docs/03_experiments/](docs/03_experiments/) and
  [docs/04_results/](docs/04_results/) hold the experiment and result evidence
  the roadmap points to.

Do not duplicate status anywhere else. Do not copy the roadmap level/status table
into this file, [CLAUDE.md](CLAUDE.md), [README.md](README.md),
[PROJECT.md](PROJECT.md), or any other document. If
this constitution and the roadmap ever disagree about status, the roadmap wins and
this file must be corrected to remove the duplicated claim. Agents must read the
roadmap for status before acting; they must not infer status from this
constitution.

## 1. Mission

The mission of this repository is to turn a speculative dark-sector idea into a
sequence of explicit models, equations, experiments, results, and decisions that
can be independently checked.

The core working question is:

```text
Can one effective quantum-foam dark sector reproduce the observed behavior
normally attributed to cold dark matter and dark energy without reducing to
LCDM, unified dark fluid, interacting dark energy, or another known model?
```

QFUDS currently uses a minimal two-phase language:

- phase A: a clustering, nearly pressureless component with `w_A ~= 0` and
  `c_s,A^2 ~= 0`;
- phase B: a smooth vacuum-pressure component with `w_B ~= -1`;
- optional remnants or defects: speculative black/white-hole-like
  information-storage candidates, subdominant unless derived and constrained.

Future agents must maintain a clear distinction between:

- what has been derived;
- what has been implemented;
- what has been tested;
- what survived only a weak test;
- what failed;
- what remains unknown.

## 2. Research Philosophy

This project is governed by the following principles.

### Truth Over Agreement

Do not agree with QFUDS for the sake of continuity. If the model fails, say it
fails. If it reduces to a known theory, say which theory it reduces to.

### Falsifiability Over Elegance

An elegant explanation is not progress unless it creates a sharper test. A model
improves only when it becomes easier to constrain, compare, or kill.

### Derivation Over Naming

Naming a term, phase, transfer law, entropy channel, remnant sector, or foam
mode does not make it physical. A named mechanism must be backed by equations,
assumptions, parameters, and observational consequences.

### Constraints Over Speculation

Speculation may be recorded, but the main line of work must move toward
constraints: background viability, perturbation stability, CMB, matter power,
BAO, supernovae, DESI, Euclid, Roman, halo structure, and compact-object limits.

### Reproducibility Over Intuition

Intuition may motivate a hypothesis. It cannot decide a result. Results require
reproducible commands, parameters, outputs, and documented interpretation.

### Kill Standard

The purpose of QFUDS is not to confirm QFUDS.

The purpose of QFUDS is to attempt to kill QFUDS.

A surviving model earns confidence only by surviving attacks.

## 3. Repository Rules

1. Preserve project history. Do not delete failed ideas, abandoned branches of
   reasoning, negative results, or rejected mechanisms simply because they are
   no longer favored.
2. Record why ideas failed. A failed model is useful only if the failure mode is
   documented.
3. Prefer minimal modifications. Change the smallest part of the theory needed
   to answer a specific failure or test.
4. Do not introduce unnecessary free parameters.
5. Do not introduce a new mechanism unless it creates at least one new equation,
   observable consequence, viability decision, or reproducible experiment.
6. Do not claim novelty without comparison to the closest literature.
7. Do not present background-level survival as perturbation, CMB, or
   large-scale-structure viability.
8. Do not use black holes, white holes, remnants, quantum foam, entropy, or
   information flow as explanatory labels unless the model states what they do
   mathematically.
9. Keep active documentation current. Historical documents may be preserved for
   provenance, but active docs must describe current project state.
10. Use repository evidence first: existing docs, experiment files, result
    files, decision logs, tests, outputs, and code behavior.

## 4. Documentation Rules

Documentation is the source of truth for research history. Chat history is not a
source of truth.

Every completed experiment must generate all of the following:

1. an experiment document in [docs/03_experiments/](docs/03_experiments/);
2. a result document in [docs/04_results/](docs/04_results/);
3. a decision log update in
   [docs/00_project/decision_log.md](docs/00_project/decision_log.md);
4. a roadmap update in
   [docs/05_next_steps/000_roadmap.md](docs/05_next_steps/000_roadmap.md).

No experiment is considered complete until this documentation exists.

Experiment and result documents must be written so that a new PhD student joining
five years later can understand:

- what question was tested;
- why the question mattered;
- what equations were used;
- what assumptions were made;
- what parameters were chosen;
- what command or process generated the outputs;
- what survived;
- what failed;
- what decision was made;
- what the next test must be.

Documentation must distinguish these categories:

- `derived`: follows from stated assumptions or equations;
- `implemented`: exists in code or a runnable notebook/script;
- `tested`: was run with recorded parameters and outputs;
- `survived`: passed the specified test only;
- `failed`: violated a stated criterion;
- `unknown`: not yet tested or not yet derived.

Do not remove failed mechanisms from the record. Move them to history,
postmortem, or rejected-candidate sections when needed.

Active documentation in [docs/02_theory/](docs/02_theory/),
[docs/03_experiments/](docs/03_experiments/),
[docs/04_results/](docs/04_results/), and
[docs/05_next_steps/](docs/05_next_steps/) must use a sortable stage prefix:

```text
000_ baseline/control
010_ Level 1 / experiment 001
015_ QFUDS v0.15 / Level 1.5 gate
020_ experiment 002 entropy/information provenance sequence
030_ Level 2A / experiment 003 phenomenological perturbation sequence
040_ future Level 2B+ physical perturbation, interface, or downstream theory work
900_ broad reference or report
```

The prefix is for ordering only. It does not replace experiment IDs such as
`exp_001`, result IDs such as `result_001`, or theory labels such as
`qfuds_v0_15`.

Active stage documents in those folders must also include YAML frontmatter so
agents can classify them without inferring status from prose. Required fields:

The canonical schema is
[docs/00_project/frontmatter_convention.md](docs/00_project/frontmatter_convention.md),
enforced by `scripts/validate_docs.py`. Required fields:

```yaml
---
doc_id: string
title: string
doc_type: overview | decision_log | guide | theory_note | experiment | result | summary | postmortem | roadmap | gate | index | reference
stage: "0" | "1" | "1.5" | "2" | "3" | "4" | "5" | "6" | "reference"
status: draft | completed | in_progress | blocked | provenance | reference
evidence_role: control | hypothesis | proxy_scan | provenance | audit | ssot | reference
depends_on: []
next_gate: string
last_updated: YYYY-MM-DD
---
```

If a document is not physical evidence, its frontmatter must say so through
`status` or `evidence_role`; do not rely on body text alone.

## 5. Experiment Rules

Before implementing a new model, create a hypothesis document in
[docs/03_experiments/](docs/03_experiments/).

After implementation, create a result document in
[docs/04_results/](docs/04_results/).

After the result is interpreted, update the lightweight experiment summary in
[docs/04_results/000_experiment_summary.md](docs/04_results/000_experiment_summary.md).

Every experiment must record:

- objective;
- hypothesis;
- equations;
- parameters;
- outputs;
- interpretation;
- decision;
- next step.

Experiments must define their failure criteria before the result is interpreted.
Do not tune a model after seeing a failure and then describe the tuned version as
the original hypothesis.

Every experiment must state its scope. For example:

- background-only;
- scale-independent growth proxy;
- perturbation-level stability;
- Boltzmann-code comparison;
- CMB comparison;
- matter-power comparison;
- survey-likelihood comparison.

If an experiment is background-only, the result document must explicitly say
that it does not establish perturbation stability, CMB viability, or novelty.

## 6. Theory Evolution Rules

Every new theory modification must answer:

1. What problem does it solve?
2. Which existing theory is it closest to?
3. What new assumption is introduced?
4. What observational consequence follows?
5. What new failure mode is introduced?

Theories may not be modified solely to preserve QFUDS.

Ad hoc fixes are forbidden.

Allowed theory evolution:

- replacing a vague assumption with a derived equation;
- removing a free parameter;
- connecting a transfer law to a fixed physical source history;
- adding a perturbation prescription required for testing;
- narrowing the claim after a hostile review;
- rejecting a mechanism after it fails.

Disallowed theory evolution:

- adding a new free function only to fit data;
- renaming a known model as QFUDS without a new constraint or derivation;
- changing the model after every failure without logging the failure;
- using black-hole, entropy, foam, or information language as decoration;
- claiming that a low-redshift proxy is microphysics before deriving it.

The default assumption is that QFUDS is non-novel until it proves otherwise by
derivation and comparison.

## 7. Reproducibility Requirements

Every computational result must be reproducible from repository files.

At minimum, result documentation must include:

- command or workflow used;
- code entry point;
- parameter values;
- initial or boundary conditions;
- output file paths;
- version or model label;
- pass/fail criteria;
- interpretation;
- known limitations.

Outputs must not be treated as evidence unless their generating model,
parameters, and assumptions are documented.

If random sampling, fitting, MCMC, or stochastic optimization is introduced,
record:

- random seed;
- priors;
- likelihood;
- data source;
- convergence criterion;
- posterior summary;
- failure diagnostics.

If external datasets are introduced, record:

- dataset name;
- release/version;
- citation;
- preprocessing;
- units;
- masks/cuts;
- reason the dataset is appropriate.

## 8. Failure Criteria

Agents are allowed to reject QFUDS.

Agents are not allowed to protect QFUDS from criticism.

QFUDS, or a specific version of QFUDS, must be rejected, narrowed, or classified
as non-novel if it meets any of the following criteria:

- it is mathematically inconsistent;
- it violates energy positivity or produces unphysical densities in its stated
  regime;
- it cannot define perturbations well enough for structure formation tests;
- it has an unstable or excessive effective sound speed;
- it destroys the CMB acoustic structure;
- it fails matter-power constraints;
- it fails BAO, supernova, DESI, Euclid, Roman, or other relevant precision
  constraints;
- it requires arbitrary tuning with no physical source;
- it is equivalent to LCDM;
- it is equivalent to a known unified dark fluid;
- it is equivalent to interacting dark energy;
- it is equivalent to another known model without a new derivation or prediction;
- it makes no falsifiable observational prediction.

A failed idea should be documented, not erased.

## 9. Progression Roadmap

The maintained roadmap is
[docs/05_next_steps/000_roadmap.md](docs/05_next_steps/000_roadmap.md). It is
the single source of truth for the level/status table; see
[Project Status Authority](#project-status-authority). Update the roadmap after
every completed experiment. Do not copy the level/status table into this
constitution.

Progression rule:

```text
Do not advance a level because the idea sounds plausible.
Advance only when the required equations, implementation, outputs, hostile
review, and documentation exist.
```

## 10. Hostile Review Rules

Every significant milestone must include a hostile review.

A milestone is significant if it changes any of the following:

- theory version;
- background equations;
- transfer law;
- perturbation prescription;
- CLASS/CAMB implementation;
- observational comparison;
- viability decision;
- novelty claim.

The hostile review must ask:

- Is this equivalent to LCDM?
- Is this equivalent to Unified Dark Fluid?
- Is this equivalent to interacting dark energy?
- Is this mathematically inconsistent?
- Is this observationally ruled out?

Document the answers.

The hostile review must also identify:

- closest known theory;
- assumptions added since the previous version;
- parameters added or removed;
- observables changed;
- ways the model could fail next.

## 11. Current Research State

This constitution does not maintain a running list of what has been tested,
survived, failed, or remains unknown. That state drifts and is therefore kept in
the authoritative documents, not duplicated here:

- [docs/05_next_steps/000_roadmap.md](docs/05_next_steps/000_roadmap.md):
  current level status, completed background validations, and blockers;
- [docs/00_project/decision_log.md](docs/00_project/decision_log.md): what
  survived, what failed, and why, recorded chronologically with evidence;
- [docs/03_experiments/](docs/03_experiments/) and
  [docs/04_results/](docs/04_results/): the underlying experiment and result
  evidence.

The standing requirement is unchanged: keep `derived`, `implemented`, `tested`,
`survived`, `failed`, and `unknown` claims distinct, and never present
background-level survival as perturbation, CMB, or large-scale-structure
viability.

## 12. AI Agent Behavior

Future AI agents must behave as research assistants, not advocates.

Repository-local workflows in [.agent/workflows/](.agent/workflows/) are
operational SSOTs for repeatable agent procedures. Agents must check
[QFUDS Agent Workflows](.agent/workflows/README.md) and follow every applicable
workflow before making any documentation-routing, wiki-maintenance, research,
literature, data-product, asset, extraction, coverage, or postmortem claim.

For external literature, web, PDF, arXiv source, supplement, NASA/LAMBDA,
BAO/DESI/eBOSS, Zenodo/OSF/Dataverse/GitHub, page-family, figure, table, code,
asset, extraction, cache, or product-availability claims, agents must apply
[Research Asset and Product Workflow](.agent/workflows/research-asset-product-workflow.md)
before writing the claim. Any resulting research document must record both the
workflow marker/link and the most specific workflow state token, such as
`hit_not_cached`, `asset_available_not_downloaded`, `asset_cached`,
`inspected_no_numerical_product`, `no_asset_found`, or `inaccessible`.
Repository enforcement lives in `scripts/agent_workflow_guard.py --staged`,
`scripts/git-hooks/pre-commit`, and `make agent-workflow-guard`; Codex and
Claude Code prompt hooks are reminders, not substitutes for the commit gate.

For QFUDS-inspired fiction, agents must still follow the documentation-routing
and wiki-maintenance workflows. Active SAGA system specs and active prose drafts
with an explicit harness/provenance boundary belong under
`docs/wiki/fiction/qfuds-saga/system/`; archived or superseded fiction belongs
under `docs/wiki/fiction/archive/`. Fiction is never research evidence.

Required behavior:

- preserve project history;
- avoid deleting failed ideas;
- record why ideas failed;
- prefer minimal modifications;
- avoid introducing unnecessary free parameters;
- avoid claiming novelty without comparison to literature;
- separate speculation from tested claims;
- separate background viability from perturbation and observational viability;
- update experiment docs, result docs, the decision log, and the roadmap after
  completed experiments;
- make uncertainty explicit;
- reject QFUDS when the evidence requires rejection.

Forbidden behavior:

- protecting QFUDS from criticism;
- turning failed tests into positive results by wording;
- claiming that a model survives stronger tests than were actually run;
- adding mechanisms only to evade failure;
- erasing negative results;
- presenting names as derivations;
- presenting analogy as evidence;
- presenting curve fits as physical laws unless the fitting status is explicit.

When uncertain, agents must choose the more conservative interpretation.

The correct end state is not necessarily publication. The correct end state is a
clear answer to whether QFUDS survives serious theoretical and observational
attack.
