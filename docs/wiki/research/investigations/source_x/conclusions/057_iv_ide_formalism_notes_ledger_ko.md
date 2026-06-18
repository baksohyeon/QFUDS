---
doc_id: audit_2026_06_18_iv_ide_formalism_notes_ledger_ko
title: "2026-06-18 IV/IDE Formalism Notes Ledger"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - audit_2026_06_18_iv_ide_formalism_study_map_ko
  - audit_2026_06_18_academic_derivation_bridge_ko
  - postmortem-015-bruteforce-gamma-method-retrospective
  - qfuds_phenomenological_perturbations
  - result_003_phenomenological_perturbation_closure
  - result_004_p1_model_family_positioning
  - result_006_literature_timing_support_audit
  - qfuds_qnu_necessity_formulation_audit
  - roadmap
next_gate: paper-by-paper IV/IDE equation extraction only; no physical-QFUDS admission
last_updated: 2026-06-18
---

# 2026-06-18 IV/IDE Formalism Notes Ledger

## Purpose

이 문서는 [IV/IDE Formalism Study Map](056_iv_ide_formalism_study_map_ko.md)의
첫 실행 장부다.

목적은 QFUDS를 새 이론으로 보존하는 것이 아니라, retained `Gamma(a)`가
학계 IV/IDE formalism의 어느 슬롯까지 들어가고 어디서 멈추는지 분리하는
것이다.

```text
retained Gamma(a) = phenomenological interaction-history comparator
physical QFUDS source = not derived
Level 2B = closed
```

## Workflow Boundary

This ledger follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md)
as a source-state boundary.

No new external source, PDF, page family, cache, digitization, posterior product,
or product-absence claim is introduced here. This ledger only reclassifies
repository-owned records and the source states already recorded there.

Inherited workflow states:

| Source family | Inherited workflow state | Boundary |
| --- | --- | --- |
| Retained P1/P2 perturbation records | repository result/theory records | not external product evidence |
| Exp006 timing audit | table-level products only | no likelihood, Boltzmann run, curve fit, or posterior product |
| Escamilla 2023 and Martinelli 2019 literature records | `literature_record_cached`; raw assets remain `asset_available_not_downloaded` | convention targets, not numerical histories for QFUDS |
| Li 2025 sign-reversal IDE record | cached source/digitization records inherited from owning audit | timing-compression and convention reference only |
| NASA/LAMBDA, BAO, CMB, LSS constraints | baseline constraints only | not used to choose `Gamma(a)`, amplitude, width, transition redshift, or source scale |

Subagents were used only as read-only scouts. The main writer integrated their
findings into this single ledger.

## Short Conclusion

The honest translation is narrow.

```math
Q = H \Gamma(a)\rho_A
```

or, in conformal-time notation,

```math
Q = \mathcal{H}\Gamma(a)\rho_A.
```

That is a usable background interaction-history slot. It is not a physical
source law.

The next missing academic objects are:

```text
X
Q^mu[X, ...]
transfer frame rule
phase-B pressure prescription
source-side delta Q
stability prescription
Boltzmann-ready equation set
known-model escape equation
```

Until those exist, retained `Gamma(a)` can teach IV/IDE notation and model
comparison. It cannot reopen physical-QFUDS admission.

## Layer Ledger

| Formalism layer | Academic question | Current QFUDS fill | Missing item | Stop condition | Next safe action |
| --- | --- | --- | --- | --- | --- |
| Model taxonomy | Which known model family absorbs the behavior first? | Retained P1 sits in interacting-vacuum / time-dependent IDE phenomenology. | A source equation that escapes IV/IDE, effective `w(a)`, unified fluid, running vacuum, backreaction, or modified gravity sinks. | Stop if the branch is fully describable as known IV/IDE with no new equation. | Compare paper-by-paper model assumptions before naming novelty. |
| Background `Q` | What scalar transfer history is being used? | `Q = H Gamma(a) rho_A`; positive `Q` moves energy from phase A to phase B in local convention. | Time variable, sign, density factor, dimensions for every literature comparison. | Stop if only a fitted or chosen `Gamma(a)` curve exists. | Build a convention map before any fit. |
| Density convention | Which density multiplies the coupling? | Local map uses `rho_A`; academic papers may use `rho_c`, `rho_de`, kernels, or other variables. | Translation rule between `Gamma(a)`, `xi(a)`, `beta(a)`, `Pi_DE`, `q_V`, or reconstructed kernels. | Stop if symbols are compared without density and sign translation. | Extract exact equations from each paper. |
| Covariant transfer | What is `Q^mu`? | Level 2A used a phase-A-frame closure. | Physical covariant source law and transfer-frame rule. | Stop if only background `Q` is defined. | Separate DM-frame, DE-frame, total-frame, and source-derived choices. |
| Perturbation closure | What are `delta Q`, `delta Gamma`, momentum transfer, gauge, pressure, and sound speed? | P1 uses `deltaQ = Q delta_A`, `deltaGamma = 0` as ansatz. | Source-side perturbation derivation and gauge/frame consistency. | Stop before CMB/LSS claims if perturbations are copied only for stability. | Study IV/IDE closure and instability literature. |
| Phase-B prescription | Is B vacuum, near-vacuum fluid, scalar field, or effective component? | P1 exact interacting vacuum; P2 near-vacuum fluid failed retained amplitude. | Physical pressure route for phase B. | Stop treating P2 as viable at retained amplitude. | Keep P1 as comparator; retire P2 unless new preregistered model is built. |
| Stability | Does the closure avoid known IDE instabilities? | P1 stable only in local algebraic Newtonian audit; P2 failed. | Superhorizon/early-time stability and, if used, PPF prescription. | Stop saying P1 passed superhorizon stability. | Read stability papers before solver claims. |
| Solver readiness | Can this enter CLASS/CAMB or likelihood code? | No. | Full background and perturbation equations, initial conditions, gauge rules, numerical interface. | Stop before Boltzmann, CMB, matter-power, or survey-likelihood claims. | Make a solver-readiness checklist only. |
| Observational products | What data product can constrain it? | Exp006 is table-level and timing-compression only. | Posterior samples, covariance/PCA arrays, author numerical histories, or likelihood implementation. | Stop using table overlap as an informative prior. | Treat NASA/BAO/CMB/LSS as kill constraints after equations are frozen. |

## Background Convention Map

The repository-local background convention is:

```math
\rho_A' + 3\mathcal{H}\rho_A = -Q,
\qquad
\rho_B' + 3\mathcal{H}(1+w_B)\rho_B = +Q,
```

with:

```math
Q = \mathcal{H}\Gamma(a)\rho_A.
```

In this convention, positive `Q` transfers energy from the phase-A/CDM-like
sector to the phase-B/vacuum-like sector.

| Item | Current status | Academic requirement | Stop condition |
| --- | --- | --- | --- |
| Background scalar `Q` | Writable as `H Gamma(a) rho_A` or `Hc Gamma(a) rho_A`. | Define time convention, sign, density factor, and dimensions. | Stop if only a fitted/chosen `Gamma(a)` exists. |
| Sign convention | Positive `Q` reduces `rho_A` and increases `rho_B`. | State which direction positive coupling means in each paper. | Stop if sign cannot be mapped across variables. |
| Density factor | Local map uses `rho_A`. | Record whether a source uses `rho_c`, `rho_de`, total density, or a reconstructed kernel. | Stop if a density factor is assumed without source support. |
| Literature variable | Examples include `Pi_DE`, `q_V`, and `beta(a)`. | Translate before comparing shape or timing. | Stop if treating symbols as directly equivalent. |
| Inference boundary | Phenomenological comparator only. | Need source variable, derived transfer law, pressure route, and constraints. | Stop before physical-origin or novelty claims. |

Li-type `Q = beta(a) H rho_de`, Escamilla-type `Pi_DE(z)`, and
Martinelli-type `q_V(z)` are convention targets. They are not interchangeable
numerical histories until sign, density factor, time variable, and normalization
are mapped.

## `Q^mu` And Frame Matrix

Academic IV/IDE work needs the split stress-energy bookkeeping:

```math
\nabla_\mu T_A^{\mu\nu}=-Q^\nu,
\qquad
\nabla_\mu T_B^{\mu\nu}=+Q^\nu.
```

The scalar `Q` is only a background projection of `Q^nu`.

| Transfer choice | Current QFUDS status | What it means | Ledger decision |
| --- | --- | --- | --- |
| `Q^mu` parallel to phase-A / DM velocity | Level 2A P1 used this as declared closure. | Momentum transfer vanishes in the phase-A frame. | Comparator allowed; physical frame rule not derived. |
| `Q^mu` parallel to phase-B / DE velocity | Not implemented. | Different momentum transfer and perturbation equations. | Open literature comparison only. |
| `Q^mu` parallel to total dark-sector velocity | Not implemented. | Another closure class with different stability behavior. | Open literature comparison only. |
| Source-derived covariant vector | Missing. | Would require a physical source variable `X`. | Required before physical-QFUDS admission. |
| Background scalar only | Current retained `Gamma(a)` level. | Enough for background translation, not perturbations. | Stop before perturbation or CMB claims. |

## Perturbation And Stability Ledger

The Level 2A phenomenological closure used:

```text
gauge = conformal Newtonian
frame = phase-A-comoving
Q_A^mu = -Q u_A^mu
Q_B^mu = +Q u_A^mu
deltaQ = Q delta_A
deltaGamma = 0
```

This is a closure ansatz. It is not a source derivation.

| Item | Current ledger state | Boundary |
| --- | --- | --- |
| `Q` | `Hc Gamma(a) rho_A`; writable background transfer. | Not derived from `X`. |
| `Q^nu` | Declared in phase-A frame for P1. | Missing physical source law. |
| Gauge | Conformal Newtonian for the audit. | Not a general gauge-proof source model. |
| `deltaQ` | `Q delta_A`. | Ansatz only. |
| `deltaGamma` | `0`. | Gauge-fixed phenomenological choice, not source physics. |
| Phase B P1 | Interacting vacuum. | Stable only in local algebraic audit; known IV form. |
| Phase B P2 | Near-vacuum fluid with `w_B=-0.999`. | Failed retained amplitude across tested `k`. |
| Conservation residual | Not independently computed under algebraic metric closure. | Placeholder-style diagnostics cannot be upgraded to physics validation. |
| PPF fallback | Possible phenomenological stabilization class. | Not QFUDS novelty unless derived. |

Exact stop conditions:

- Stop any physical-QFUDS or Level 2B claim unless `X`, `Q^nu`, phase-B
  pressure rationale, source-side `delta Q`, and known-model distinction are
  supplied.
- Stop perturbation integration for any background with `rho_B <= 0`.
- Stop amplitude escalation at the first background or perturbation failure; do
  not retune after seeing failures.
- Stop treating P2 as viable at retained amplitude.
- Stop saying P1 passed superhorizon stability; the algebraic Newtonian closure
  did not test that.
- Stop before CMB, matter-power, survey-likelihood, or CLASS/CAMB claims.

## Product And Solver Readiness

This ledger is not a solver plan.

| Readiness item | Required before stronger claim | Current state |
| --- | --- | --- |
| Equation readiness | background equations, `Q^mu`, perturbation equations, pressure/sound-speed prescription, initial conditions | incomplete |
| Stability readiness | known IDE instability checks, superhorizon behavior, PPF decision if needed | incomplete |
| Product readiness | author numerical histories, covariance/PCA arrays, posterior samples, likelihood implementation, or digitized uncertainty products | mostly absent or limited by owning records |
| Boltzmann readiness | CLASS/CAMB-compatible equation set and validation tests | absent |
| Observational readiness | frozen equations before NASA/BAO/CMB/LSS kill constraints | blocked until equations are frozen |

NASA/LAMBDA, BAO, CMB, and LSS constraints should come after the formalism is
fixed. If observations are used first to select transition scale, width,
amplitude, or source timing, the route fails by circularity.

## Decision

| Question | Decision |
| --- | --- |
| Can retained `Gamma(a)` be translated into academic language? | Yes, as a background IV/IDE interaction-history comparator. |
| Does it derive a physical QFUDS source? | No. |
| Does P1 become new physics? | No. It remains phase-A-frame interacting-vacuum phenomenology unless a source law is derived. |
| Does P2 remain viable? | No at retained amplitude. |
| Can this justify NASA/BAO/CMB/LSS comparison now? | No. Those remain kill constraints after equations are frozen. |
| What is the useful value? | It marks exactly where the non-scientist brute-force `Gamma(a)` intuition enters real IV/IDE formalism and where it stops. |

## Next Executable Instruction

Create a paper-by-paper IV/IDE equation extraction plan. For each paper, extract
only the exact source-term convention, density factor, sign convention,
`Q^mu`/frame choice, perturbation prescription, and stated stability rule. Do
not fit `Gamma(a)`, do not select a transition scale, and do not use
NASA/LAMBDA, BAO, CMB, or LSS constraints until the equation set is frozen.
