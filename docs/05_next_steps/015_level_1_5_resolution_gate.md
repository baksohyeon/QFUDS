---
doc_id: level_1_5_resolution_gate
title: Level 1.5 Phase-Transfer Resolution Gate
doc_type: gate
stage: "1.5"
status: in_progress
evidence_role: ssot
depends_on:
  - result_001_5_phase_transfer_physicality
  - result_002_entropy_information_gate
next_gate: resolve physical transfer or explicitly demote to phenomenological interacting vacuum
last_updated: 2026-06-09
---

# Level 1.5 Phase-Transfer Resolution Gate

Date: 2026-06-09

This gate defines what would count as resolving the current phase-transfer
physicality blocker. It does not change project status. Current status remains
in [docs/05_next_steps/000_roadmap.md](000_roadmap.md).

## Question

The retained branch uses a transfer shape tied to nonlinear collapse or
information production:

```math
\Gamma(a) \propto {dF_{\rm coll}(>M,a) \over d\ln a}.
```

Level 1.5 asks whether this is physical QFUDS transfer or only a useful
phenomenological interacting-vacuum source shape.

## Evidence Required For Pass

The branch can be promoted from Level 1.5 to physical Level 2B only if the
repository contains evidence for all of the following before fitting to later
observables:

1. **Derived or justified transfer law**: an equation for the stress-energy
   exchange, or an equivalent coarse-grained conservation law, must state what
   converts phase A into phase B. A label such as entropy, information, collapse,
   or foam is not enough.
2. **Fixed source history before fitting**: `collapse_a` must be replaced by a
   physical mass threshold `M`, or by another fixed threshold with a stated
   physical reason. The threshold must not be chosen after looking at the
   background or perturbation outcome.
3. **Self-consistent source computation**: `dF_coll/dln a` must be recomputed
   using QFUDS growth ingredients, or any imported LCDM collapse approximation
   must be explicitly bounded as a proxy and excluded from physical novelty
   claims.
4. **Parameter decision**: `gamma0` and every remaining free quantity must be
   classified as derived, externally fixed, independently bounded, fitted, or
   phenomenological. A physical pass is not allowed if the transfer amplitude is
   only an unconstrained efficiency.
5. **Perturbation-ready transfer prescription**: the transfer frame, gauge
   assumptions, `delta Q`, and phase-A/phase-B perturbation response must be
   specified well enough to write the Level 2B experiment without inventing new
   physics at that stage.
6. **Known-model comparison**: the branch must be compared against LCDM,
   unified dark fluid, and interacting dark energy. If it is equivalent to a
   known model, the decision must record the equivalence.
7. **Distinct test**: the audit must identify at least one observable, stability
   condition, or falsifiable relation that is not just a free interacting-vacuum
   transfer law.
8. **Reproducible validation artifact**: there must be a derivation document,
   reproducible script output, or analytic check that a hostile reviewer can
   inspect. Documentation structure alone cannot satisfy this criterion.

## Pass Decision

Level 1.5 passes only if the result document can state all of the following:

```text
The retained transfer law is fixed enough to define physical Level 2B
perturbation equations without adding new assumptions there.
```

That statement requires the evidence listed above. A successful background curve
or a completed document set is not enough.

## Evidence Required For Fail Or Demotion

The branch must be rejected as physical QFUDS, or explicitly demoted to
phenomenological interacting vacuum, if the audit finds any of the following:

1. `Gamma(a)` is only a fitted, hand-selected, or post-hoc source function.
2. The source still depends on an implicit `collapse_a` tuning parameter.
3. The source history still uses LCDM growth while claiming QFUDS
   self-consistency.
4. No stress-energy exchange, conservation law, or transfer perturbation
   prescription can be stated.
5. The construction is equivalent to ordinary interacting vacuum without a new
   constraint or observable.
6. Entropy, information, collapse, or foam language has no mathematical role in
   the stress-energy model.

## Fail Decision

Level 1.5 fails as physical QFUDS if the result document must state:

```text
Gamma(a) remains a phenomenological interacting-vacuum transfer law.
```

In that case physical Level 2B remains blocked. A Level 2A-style
phenomenological continuation may still be allowed, but it must not be described
as derived QFUDS physics.

## Allowed Outcomes

There are three acceptable resolutions:

| Outcome | Required evidence | Consequence |
| --- | --- | --- |
| physical pass | derived or justified transfer law, fixed source, self-consistent source computation, parameter decision, perturbation-ready prescription, known-model comparison, distinct test | plan physical Level 2B perturbation experiment |
| demotion | source shape is useful but remains fitted, proxy-based, or equivalent to interacting vacuum | continue only as interacting-vacuum phenomenology; do not make physical QFUDS claims |
| rejection | branch fails a stated physical or mathematical criterion | preserve the failure and choose a new hypothesis only if it creates a sharper test |

## Required Evidence

A Level 1.5 resolution must point to:

- updated theory assumptions;
- experiment definition with predeclared failure criteria;
- code path or analytic derivation;
- output artifacts or derivation record;
- result interpretation;
- decision-log entry;
- experiment-summary row;
- roadmap update.

No background-only output can satisfy this gate by itself.
