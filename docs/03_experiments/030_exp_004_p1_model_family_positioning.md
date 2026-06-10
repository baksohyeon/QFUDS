---
doc_id: exp_004_p1_model_family_positioning
title: "Experiment 004: Retained P1 Model-Family Positioning and Equivalence Map"
doc_type: experiment
stage: "2"
status: completed
evidence_role: audit
depends_on:
  - qfuds_positioning
  - qfuds_success_criteria
  - qfuds_phenomenological_perturbations
  - result_003_phenomenological_perturbation_closure
next_gate: result_004 model-family classification complete; use roadmap for current status
last_updated: 2026-06-09
---

# Experiment 004: Retained P1 Model-Family Positioning and Equivalence Map

Date: 2026-06-09

## Objective

Classify where the retained P1 phenomenological branch sits in the existing
cosmology landscape.

The primary question is:

```text
Which existing interacting-vacuum or interacting-dark-energy model family best
reproduces retained P1, and at which layer does any difference remain?
```

This is a positioning experiment. It is not a novelty test, a physical
derivation, or a go/no-go test for the whole QFUDS research program.

Equivalence to an existing model family is an allowed and useful outcome. If P1
is equivalent to a known interacting-vacuum or interacting-dark-energy model,
the result should explain what was learned, why that equivalence is
scientifically useful, which parts of the original intuition map onto existing
cosmology, and which parts remain unsupported.

## Hypothesis

Retained P1 is expected to sit closest to interacting-vacuum models with a
time-dependent dark-sector transfer:

```text
Q = Hc Gamma(a) rho_A
```

The retained source-shaped `Gamma(a)` may be equivalent to a time-dependent IDE
or interacting-vacuum coupling at the background and [Level 2A](../wiki/glossary/repository_levels.md) perturbation
levels. Any remaining difference is expected to live in the chosen
parameterization of `Gamma(a)`, not in a physical QFUDS derivation.

The experiment should test this expectation rather than assume it.

## Scope

This experiment tests model-family positioning for the retained P1 branch.

It may establish:

- closest interacting-vacuum or interacting-dark-energy model family;
- exact equivalences at the background, transfer-law, or closure level;
- approximate equivalences to simpler parameterized transfer laws;
- remaining differences between P1 and selected baselines;
- whether remaining differences are physical, phenomenological, or only
  parameterization choices;
- reduction limits to LCDM, constant-coupling IDE, generic time-dependent IDE,
  and interacting vacuum.

It does not establish:

- physical QFUDS derivation;
- microscopic quantum-foam dynamics;
- physical Level 2B perturbation closure;
- CLASS/CAMB viability;
- CMB, matter-power, BAO, supernova, DESI, Euclid, Roman, or likelihood
  viability;
- novelty of QFUDS as a physical theory.

## Baseline Selection

Use baselines that answer the positioning question with the fewest moving parts.

| Baseline | Purpose | Positioning question |
| --- | --- | --- |
| LCDM / zero-transfer control | Confirms the null limit. | Does P1 reduce to LCDM when `Gamma(a) -> 0`? |
| Interacting vacuum in the phase-A/geodesic frame | Closest known family for vacuum-like phase B exchanging energy with CDM-like phase A. | Is P1 exactly an interacting-vacuum model with a chosen `Gamma(a)`? |
| IDE with `Q = Hc xi(a) rho_A` | Generic time-dependent coupling baseline. | Is retained P1 just IDE with `xi(a) = Gamma(a)`? |
| Constant-coupling IDE or interacting vacuum | Standard simple limit. | Does P1 reduce to a constant-coupling model when `Gamma(a)` is constant? |
| Power-law or late-time gated `Gamma(a)` IDE | Simple phenomenological shape baseline. | Can simpler transfer shapes reproduce P1 background and growth behavior? |
| Effective non-interacting dark-energy reconstruction | Background-degeneracy check. | Can P1's background expansion be reproduced by an effective `w(a)` model without interaction? |

Do not use strong-gravity, holographic, black-hole, white-hole, Planck-star, or
baby-universe source ideas as numerical baselines in this experiment. Those are
future physical-source candidates or literature-positioning references, not the
closest P1 phenomenology baselines.

## Method

Compare retained P1 against the selected baselines layer by layer.

### Layer 1: Background Equivalence

Compare:

- `H(a) / H_LCDM - 1`;
- `rho_A(a)`;
- `rho_B(a)`;
- total dark-sector density;
- effective background equation of state;
- early-time dark-energy or phase-B fraction;
- integrated transferred fraction.

Classify background behavior as:

- exact equivalence;
- approximate equivalence within predeclared tolerance;
- distinguishable background trajectory;
- failed background consistency.

### Layer 2: Transfer-Law Equivalence

Compare:

- retained `Gamma(a)` shape;
- generic `xi(a)` reconstruction where `Q = Hc xi(a) rho_A`;
- constant-coupling approximation;
- power-law or gated approximation;
- transfer peak location, width, amplitude, and low-redshift support.

Determine whether P1's retained source shape contributes a constraint beyond
choosing a time-dependent coupling function.

### Layer 3: Perturbation-Closure Equivalence

Compare P1's declared Level 2A closure with standard interacting-vacuum and IDE
closure choices:

```text
Q_A^mu = -Q u_A^mu
Q_B^mu = +Q u_A^mu
deltaQ = Q delta_A
deltaGamma = 0
phase B: interacting vacuum
```

Classify whether the closure is:

- standard interacting vacuum in the phase-A frame;
- a known IDE closure with different notation;
- a phenomenological closure choice not fixed by microphysics;
- physically distinct from the baseline closures.

### Layer 4: Observable Diagnostics

Compare:

- `delta_A(a,k)`;
- relative growth suppression or enhancement versus LCDM;
- matter-era growth slope;
- scale dependence across the tested `k` grid;
- metric-potential proxy behavior where available;
- stability flags;
- sensitivity to coupling amplitude and transfer-shape parameters.

The experiment should identify whether any observable difference survives after
matching simpler IDE or interacting-vacuum baselines.

## Runs

This specification does not run the experiment. Before execution, implement or
identify a deterministic command that produces the required outputs below.

The planned comparison set is:

```text
R0: LCDM / Gamma(a) = 0
R1: retained P1 Gamma(a) with documented retained parameters
R2: interacting vacuum with xi(a) = retained Gamma(a)
R3: IDE with xi(a) = retained Gamma(a)
R4: constant-coupling IDE or interacting vacuum matched to P1 by integrated transfer
R5: power-law or late-time gated Gamma(a) matched to P1 by transfer timing and amplitude
R6: effective non-interacting w(a) reconstruction matched to P1 background expansion
```

If the existing code cannot represent one of these baselines without changing
the model assumptions, record that limitation in the result document rather than
silently substituting another comparison.

## Diagnostics

The result must report diagnostics in four groups:

1. Background diagnostics: expansion, densities, effective equation of state,
   and transferred fraction.
2. Transfer diagnostics: coupling function, peak timing, support, amplitude,
   and reconstruction error.
3. Perturbation diagnostics: growth, scale dependence, stability, and closure
   matching.
4. Interpretation diagnostics: whether differences are exact, approximate,
   physical, phenomenological, or only parameterization choices.

Use the following classification vocabulary:

| Classification | Meaning |
| --- | --- |
| `exact_equivalence` | Same equations or same predictions under an explicit mapping. |
| `approximate_equivalence` | Predictions can be matched within tolerance by a baseline model. |
| `background_degenerate` | Expansion history matches, but perturbation behavior may differ. |
| `closure_equivalent` | Perturbation prescription matches a known IDE or interacting-vacuum closure. |
| `parameterization_difference` | Difference comes only from the chosen `Gamma(a)` shape or fitting basis. |
| `phenomenological_difference` | Difference changes testable behavior but is not physically derived. |
| `physical_difference` | Difference follows from a derived source, transfer four-vector, or microphysical closure. |
| `unresolved` | Existing implementation or diagnostics cannot decide the classification. |

For this experiment, `physical_difference` should be used only if the result
points to an already documented derivation. The retained P1 branch currently has
no accepted physical derivation.

## Classification Rules

Apply these rules before writing the final positioning statement.

### R2 and R3 Relationship

`R2` and `R3` are not independent numerical baselines unless `R3` defines a
distinct IDE closure.

The baseline labels mean:

| Run | Meaning | Independent of P1? |
| --- | --- | --- |
| `R2` | Interacting vacuum with `xi(a) = Gamma(a)` and the P1 vacuum closure. | No. This is the expected exact mapping if the equations match. |
| `R3` | Generic IDE with `xi(a) = Gamma(a)`. | No, unless it introduces a non-vacuum phase-B equation of state, sound speed, velocity variable, `deltaQ` rule, or momentum-transfer frame. |

Therefore the result may classify retained P1 as both:

```text
exact interacting-vacuum instance
subset of generic time-dependent IDE under xi(a) = Gamma(a)
```

but it must not treat `R2` and `R3` as separable numerical evidence unless the
implemented `R3` closure is explicitly different from P1.

### Quantitative Equivalence Thresholds

Use the same sampled `a` grid and tested `k` grid for all implemented baselines.
Report both maximum absolute error and root-mean-square error for each
diagnostic.

Classify a baseline as approximately equivalent only if it satisfies all
applicable thresholds:

| Diagnostic group | Quantity | Approximate-equivalence threshold |
| --- | --- | --- |
| Transfer shape | normalized `Gamma(a)` | RMS error <= 5% and max error <= 15% over the interval where retained P1 has non-negligible support |
| Background expansion | `H(a) / H_P1(a) - 1` | max absolute error <= 0.5% for `a >= 1e-3` |
| Dark-sector densities | `rho_A(a)`, `rho_B(a)` relative to P1 | max relative error <= 2% where the denominator is nonzero |
| Effective equation of state | `w_dark(a)` or reconstructed `w(a)` | max absolute error <= 0.02 for `a >= 1e-3` |
| Perturbation growth | `delta_A(a,k)` relative to P1 | RMS relative error <= 5% for each tested finite mode |
| Growth-rate proxy | matter-era growth slope or `f(a)` | max absolute error <= 0.05 over the reported matter-era window |
| Stability | instability flags | same stable/unstable classification for every implemented tested mode |

If a diagnostic cannot be computed for a baseline, classify that layer as
`unresolved`, not equivalent. If a baseline matches background diagnostics but
fails perturbation diagnostics, classify it as `background_degenerate`, not
fully equivalent.

### Distinct-Phenomenology Boundary

`phenomenological_difference` or `partially_distinct_phenomenology` may be used
only for differences that survive the thresholds above inside the declared
Level 2A closure:

```text
conformal Newtonian gauge
phase-A-comoving transfer
Q_A^mu = -Q u_A^mu
Q_B^mu = +Q u_A^mu
deltaQ = Q delta_A
deltaGamma = 0
phase B: interacting vacuum
```

This classification does not imply physical QFUDS distinction. It means only
that retained P1 behaves differently from the implemented baselines under the
current phenomenological closure. A physical distinction still requires the
future-branch admission ingredients: source `X`, `Q^nu`, phase-B vacuum-pressure
rationale, `delta Q` route, and known-model distinction.

### Closure and Frame Mapping

The result must include a closure/frame-mapping table. Use this minimum table
even when some rows are analytic or unresolved rather than numerically
implemented:

| Comparison | Transfer frame | Phase-B treatment | `deltaQ` / perturbative transfer | Required classification |
| --- | --- | --- | --- | --- |
| P1 retained closure | phase-A-comoving | exact interacting vacuum | `deltaQ = Q delta_A`, `deltaGamma = 0` | implemented baseline |
| Geodesic-CDM interacting vacuum | CDM/phase-A frame | interacting vacuum | map to published interacting-vacuum convention if possible | exact, equivalent, or unresolved |
| Generic time-dependent IDE | must be declared | vacuum or non-vacuum DE must be declared | `deltaQ` and momentum transfer must be declared | equivalent only if closure matches; otherwise unresolved or distinct within Level 2A |
| Alternate momentum-transfer frame | non-phase-A frame | declared by baseline | frame-dependent `deltaQ` route must be declared | unresolved unless implemented |
| Effective non-interacting `w(a)` reconstruction | none | non-interacting effective dark energy | no physical transfer perturbation | background-degenerate only |

If alternate frames are not implemented, the result must say so explicitly. It
must not infer frame independence from a single phase-A-frame run.

## Reduction Limits

The result must explicitly assess these limits:

| Limit | Expected classification |
| --- | --- |
| `Gamma(a) -> 0` | LCDM null limit. |
| `Gamma(a) = const` | Constant-coupling IDE or interacting-vacuum limit. |
| arbitrary `Gamma(a)` | Generic time-dependent IDE or interacting-vacuum model. |
| `xi(a) = Gamma(a)` | Direct mapping to IDE or interacting vacuum with the same transfer history. |
| `w_B = -1` with transfer along `u_A^mu` | Interacting vacuum in the phase-A/geodesic frame. |
| background-only `H(a)` matching | Effective non-interacting `w(a)` degeneracy. |

If a limit cannot be tested numerically, the result must state whether the
mapping is algebraic, approximate, or untested.

## Required Outputs

The experiment result must include:

- a baseline-comparison table;
- a background-equivalence table;
- a transfer-law reconstruction table;
- a perturbation-closure comparison table;
- growth or stability diagnostics for each implemented baseline;
- a reduction-limit table;
- transfer-shape and baseline-error visual diagnostics in PNG and SVG under
  `outputs/figures/`;
- a final positioning statement.

The final positioning statement should use this form:

```text
Retained P1 is best classified as [model family].
It is exactly equivalent to [baseline/limit] at [layer].
It is approximately equivalent to [baseline] for [diagnostic].
Its remaining differences are [physical / phenomenological / parameterization-only / unresolved].
This equivalence is scientifically useful because [landscape connection / reusable baseline / falsification boundary].
The original QFUDS intuition that survived is [surviving content].
The original QFUDS intuition that did not survive is [non-surviving content].
```

## Failure Criteria

Because this is a positioning experiment, equivalence to an existing model
family is not a failure.

The experiment fails only if it cannot produce a trustworthy classification.
Failure conditions are:

1. no explicit baseline mapping is tested or documented;
2. exact and approximate equivalence are not distinguished;
3. background, transfer-law, and perturbation-closure layers are mixed together;
4. parameterization differences are described as physical differences;
5. physical-QFUDS claims are made without a documented source, `Q^nu`, phase-B
   vacuum-pressure rationale, and `delta Q` route;
6. result prose treats equivalence to IDE or interacting vacuum as a negative
   result rather than a positioning result;
7. diagnostics are too weak to support the final positioning statement.

If any failure condition occurs, the correct result classification is
`unresolved`, not `P1 failed`.

## Decision

The decision produced by this experiment is a model-family classification, not a
go/no-go verdict.

Allowed final classifications are:

| Outcome | Meaning |
| --- | --- |
| `exact_interacting_vacuum_instance` | P1 is an interacting-vacuum model with a specified `Gamma(a)`. |
| `generic_IDE_equivalent` | P1 is time-dependent IDE under the mapping `xi(a) = Gamma(a)`. |
| `background_degenerate_perturbatively_distinct` | Background matches a known family, but perturbation closure or growth behavior differs. |
| `parameterization_variant_only` | P1 differs only by the chosen transfer-function basis. |
| `partially_distinct_phenomenology` | P1 is close to IDE or interacting vacuum but imposes a constrained, testable transfer history. |
| `unresolved` | Available diagnostics cannot support a stable positioning statement. |

After the result is interpreted, update the result document, experiment summary,
decision log, traceability matrix, and roadmap only as required by the repository
workflow. The roadmap remains the single source of truth for current project
status.

## Required Result Document

When executed, this experiment should produce:

```text
docs/04_results/030_result_004_p1_model_family_positioning.md
```

No result exists yet. This specification only defines the question, baselines,
diagnostics, reduction limits, outputs, and classification rule.
