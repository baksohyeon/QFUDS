<INSTRUCTIONS>
@/Users/cnai/.codex/RTK.md
</INSTRUCTIONS>

# AGENTS.md

# Quantum Foam Unified Dark Sector (QFUDS) Agent Constitution

This repository is an active early-stage cosmology research program. Future AI
agents must treat this file as the operating constitution for all work in the
repository.

QFUDS is not a confirmed theory. QFUDS is a speculative research program asking
whether dark matter and dark energy can be modeled as two effective macroscopic
phases of a common quantum-spacetime foam sector.

The project status as of 2026-06-08 is:

- literature mapping is complete;
- background toy models are implemented;
- the v0.3 Gamma-law background scan is complete;
- perturbation equations are not yet complete;
- CLASS/CAMB integration has not started;
- CMB, matter-power, and survey-likelihood tests have not been performed.

The goal is not to prove QFUDS correct. The goal is to determine whether QFUDS
survives progressively stronger tests.

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

1. an experiment document in `docs/03_experiments/`;
2. a result document in `docs/04_results/`;
3. a decision log update in `docs/decision_log.md`;
4. a roadmap update in `docs/05_next_steps/roadmap.md`.

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

## 5. Experiment Rules

Before implementing a new model, create a hypothesis document in
`docs/03_experiments/`.

After implementation, create a result document in `docs/04_results/`.

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

The maintained roadmap is `docs/05_next_steps/roadmap.md`. Update it after every
completed experiment.

Current roadmap status:

| Level | Stage | Status | Meaning |
| --- | --- | --- | --- |
| Level 0 | Literature Position | completed | QFUDS has been compared at a draft level against LCDM, unified dark fluids, interacting dark energy, scalar-field dark matter, and compact-remnant scenarios. |
| Level 1 | Background Toy Model | completed | Two-phase background toy models exist and the zero-transfer limit reproduces LCDM. |
| Level 1.5 | Gamma-law Background Scan | completed | v0.3 transfer-law scan is complete; constant and ungated growth-driven transfer failed at tested amplitudes; low-redshift proxies survived only background checks. |
| Level 2 | Perturbation Equations | in progress | Phase-A, phase-B, and transfer perturbations remain unresolved. |
| Level 3 | CLASS/CAMB Integration | blocked | Boltzmann-code work requires Level 2 equations first. |
| Level 4 | CMB Comparison | blocked | No CMB comparison is valid until CLASS/CAMB or equivalent perturbation implementation exists. |
| Level 5 | Matter Power Spectrum | blocked | Current growth proxy is not a substitute for a full matter-power test. |
| Level 6 | DESI / Euclid / Roman Constraints | blocked | Survey constraints require validated predictions and likelihood machinery. |
| Level 7 | Publication Candidate | blocked | Publication is not appropriate until the model survives hostile review and observational comparison. |

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

What has been tested:

- literature positioning and comparison at a draft level;
- minimal two-phase background formulation;
- zero-transfer LCDM baseline;
- v0.3 Gamma-law background scan;
- minimal background viability flags for candidate transfer laws.

What survived:

- the zero-transfer model survives because it is LCDM;
- power-law and horizon-entropy-gated laws survive as ordinary interacting
  dark-energy examples unless further derived;
- collapsed-fraction, black-hole-entropy, and star-formation proxies survived
  minimal background checks and remain candidates for perturbation tests.

What failed:

- the white-hole-universe image failed as a central testable claim;
- constant Gamma transfer failed at the tested amplitude;
- ungated growth-driven Gamma transfer failed at the tested amplitude;
- any claim of CMB viability from background-only tests failed;
- any claim of novelty from free `Gamma(a)` failed.

What remains unknown:

- whether QFUDS has a microphysical action;
- whether the phase split can be derived rather than assumed;
- whether transfer perturbations are stable;
- whether phase B is exactly smooth or weakly perturbed;
- whether any surviving v0.3 proxy survives CMB tests;
- whether any surviving v0.3 proxy survives matter-power tests;
- whether QFUDS differs observationally from known dark-sector models;
- whether black-hole or remnant language has any required role in the final
  model.

## 12. AI Agent Behavior

Future AI agents must behave as research assistants, not advocates.

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
