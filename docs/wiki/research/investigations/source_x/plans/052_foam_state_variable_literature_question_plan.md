---
doc_id: audit_2026_06_17_foam_state_variable_literature_question_plan
title: "2026-06-17 Foam-State Variable Literature Question Plan"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_12_foam_sector_to_gamma_derivation_feasibility_result
  - audit_2026_06_12_effective_phase_fraction_scaffold
  - audit_2026_06_17_effective_foam_assumption_ledger_result
  - qfuds_positioning
  - literature_cache_index
  - roadmap
next_gate: execute candidate-variable question audit before selecting xi
last_updated: 2026-06-17
---

# 2026-06-17 Foam-State Variable Literature Question Plan

## Purpose

This plan answers the follow-up implied by the effective foam assumption ledger:

```text
If QFUDS has no foam-sector state-variable definition yet, what existing
academic variables should be tested or asked about before inventing one?
```

This is a question plan, not a model result.

It does not define candidate `X`.

It does not derive `Q^nu`.

It does not derive `delta Q`.

It does not claim QFUDS support.

It does not treat `xi ~= 10 Mpc` as a derived physical scale.

It does not use NASA/LAMBDA or BAO products as QFUDS evidence.

It does not open Physical-QFUDS Level 2B.

## Workflow Application

This plan follows the
[Research Asset and Product Workflow](../../../../../.agent/workflows/research-asset-product-workflow.md).

The web pass in this plan is a candidate-source scoping pass only. It does not
claim that any external asset is QFUDS-ready, missing, unavailable, or
exhaustively inspected.

Use these states:

| State | Meaning in this plan |
| --- | --- |
| `literature_record_cached` | A repository literature record already exists. |
| `reference_hit_cached_in_index` | The literature index already records the source as a reference-only hit. |
| `hit_not_cached` | A source was found in the web pass, but no local asset record was created. |

Any `hit_not_cached` source must be cached under `docs/wiki/research/assets/`
or promoted to a literature record before it can support a later product,
availability, or absence claim.

## Candidate Variable Shortlist

| Candidate variable family | Concrete variable to ask about | Why it is relevant | First reduction risk | Required answer before reuse |
| --- | --- | --- | --- | --- |
| Backreaction / averaged geometry | Buchert `Q_D`, averaged curvature deviation `W_D`, domain scale `D`, morphon field | Structure formation can be represented through averaged geometry variables. | Backreaction cosmology / morphon scalar field | Can `xi` be an averaging-domain scale with a closure condition, or is it only domain-choice bookkeeping? |
| EFTofLSS / coarse graining | Smoothing cutoff `Lambda`, nonlinear scale `k_NL^-1`, effective stress tensor, effective sound speed counterterm | A galaxy/cosmic-web scale near several Mpc can easily be an EFT cutoff or nuisance scale. | LCDM+EFTofLSS | Is `xi ~= 10 Mpc` distinguishable from an EFT cutoff or counterterm calibration? |
| Running vacuum / holographic vacuum | `rho_vac(H, dot H)`, `nu_eff`, IR cutoff `L` | Phase B vacuum-pressure behavior may reduce to existing dynamical-vacuum families. | Running vacuum / HDE | What foam-specific variable changes vacuum density beyond known RVM/HDE forms? |
| Screened modified gravity | scalar field `phi`, mass `m(a)`, coupling `beta(a)`, Compton scale `m^-1` | A finite effective length can be a screening or fifth-force range. | Screened modified gravity | Is `xi` a force/screening length, and if so what lensing/growth split follows? |
| Spacetime-foam correlation | foam correlation length, effective foam field, topology-change density | This is closest in wording to QFUDS, but it is speculative and not automatically cosmology-ready. | spacetime-foam dark energy, topological DE, HDE-like vacuum | Can it provide units, stress tensor, equation of state, and observational target before fitting? |
| Causal-set / stochastic Lambda | fluctuating `Lambda(t)`, spacetime volume fluctuation scale | Gives a discrete-spacetime route to dark-energy fluctuation without QFUDS phase transfer. | stochastic dark energy / causal-set Lambda | Can it produce phase A plus phase B, or only a fluctuating vacuum term? |
| Internal phase-fraction scaffold | effective `f_B(a)`, transition center `a_tr`, width `sigma` | Already in repo as a weak analytic scaffold that avoids `Gamma(a)`. | effective `w(a)` reconstruction | Can `f_B` be tied to an external variable above rather than chosen as a fit function? |

## Workflow-Compliant Source State

| Anchor | Variable family | Source URL | Asset/product state | Extraction potential | Allowed use here |
| --- | --- | --- | --- | --- | --- |
| Buchert 2007 local record | backreaction | [0707.2153](https://arxiv.org/abs/0707.2153) | `literature_record_cached` | not assessed in this plan | comparator question only |
| Lapi 2025 local record | structure-emergent dark energy | [2502.05823](https://arxiv.org/abs/2502.05823) | `literature_record_cached` | not assessed in this plan | comparator question only |
| Sola 2021 local record | running vacuum | [2102.12758](https://arxiv.org/abs/2102.12758) | `literature_record_cached` | not assessed in this plan | comparator question only |
| EFTofLSS sound-speed counterterm hit | EFTofLSS | [2410.11949](https://arxiv.org/abs/2410.11949) | `hit_not_cached` | `source_tex_parse_possible`; not performed | ask whether `xi` is an EFT cutoff/counterterm proxy |
| Screened modified gravity hit | screened modified gravity | [1203.4812](https://arxiv.org/abs/1203.4812) | `hit_not_cached` | `source_tex_parse_possible`; not performed | ask whether `xi` is a screening length |
| Spacetime-foam correlation hit | spacetime foam | [2507.15881](https://arxiv.org/abs/2507.15881) | `hit_not_cached` | `source_tex_parse_possible`; not performed | ask whether a foam correlation variable is defined |
| Causal-set Lambda hit | stochastic Lambda | [1703.06265](https://arxiv.org/abs/1703.06265) | `hit_not_cached` | `source_tex_parse_possible`; not performed | ask whether this supplies only vacuum fluctuation |
| Causal-set discreteness hit | stochastic Lambda | [2304.03819](https://arxiv.org/html/2304.03819v2) | `hit_not_cached` | `arXiv HTML`; not converted or cached | ask whether volume fluctuation can be a state variable |
| Reference-only local index hits | HDE / screening / LSS | literature `index.csv` reference-only rows | `reference_hit_cached_in_index` | not assessed in this plan | priority hints only |

This table is not a product-availability audit. It only records enough source
state to avoid treating a web hit as a cached or inspected product.

## Questions To Ask Before Picking `xi`

These are the questions to ask a literature pass, collaborator, or subject
expert. A future audit should record answers source-by-source.

1. Is there a recognized covariant state variable that can play the role of a
   foam correlation length on galaxy or cosmic-web scales?
2. If the proposed variable is a length, is it a physical correlation length,
   a smoothing scale, a screening length, a Compton wavelength, or an averaging
   domain?
3. Does the variable live on the geometry side, stress-energy side, or in an
   interaction/source term?
4. Does the variable already belong to backreaction, EFTofLSS, running vacuum,
   screened modified gravity, stochastic Lambda, or HDE?
5. Can it produce both a clustering phase A and a smooth vacuum-pressure phase
   B, or does it only describe one side?
6. What equation determines its time evolution before observational fitting?
7. What observable would kill it before `xi`, width, or amplitude are tuned?
8. Does it provide `Q^nu` and `delta Q`, or only background behavior?
9. If `xi ~= 10 Mpc` is used, what independent reason fixes that value?
10. What would make the proposal non-circular under a split between calibration
    data and test data?

## Working Recommendation

The first candidate to test should not be the most QFUDS-sounding one. It should
be the most dangerous known-model sink:

```text
xi ~= 10 Mpc as EFTofLSS / nonlinear coarse-graining scale
```

Reason: if this absorbs the idea, QFUDS should not spend effort dressing it as
foam physics. If it does not absorb the idea, the next strongest checks are
backreaction/domain averaging and screened-modified-gravity length scales.

Only after those sinks fail should a speculative spacetime-foam correlation
variable be considered.

## Stop Conditions

Stop and keep the lane in observer mode if:

- the candidate variable is only a renamed `Gamma(a)`;
- `xi` is chosen from the same NASA/BAO/LSS targets later used as support;
- the candidate produces only an effective `w(a)` background;
- the candidate has no equation of motion or closure condition;
- the candidate does not say whether it is geometry-side, stress-energy-side,
  or interaction-side;
- the candidate cannot state how phase B gets `w ~= -1`;
- the candidate is already fully absorbed by EFTofLSS, backreaction, running
  vacuum, screened modified gravity, IV/IDE, HDE, or stochastic Lambda.

## Output Required For The Next Audit

The next executable audit should produce a source-by-source table:

| Column | Required content |
| --- | --- |
| `candidate_variable` | The variable proposed by the literature or expert answer. |
| `source_family` | Backreaction, EFTofLSS, running vacuum, screened MG, spacetime foam, causal set, or internal scaffold. |
| `workflow_state` | `literature_record_cached`, `reference_hit_cached_in_index`, `hit_not_cached`, or later asset state. |
| `equation_side` | Geometry, stress-energy, interaction, or unassigned. |
| `xi_mapping` | Whether `xi` maps to a physical length, cutoff, domain, screening scale, or no mapping. |
| `phase_A_route` | Whether clustering/matter-like behavior is supplied. |
| `phase_B_route` | Whether vacuum-pressure behavior is supplied. |
| `known_model_sink` | Which known model absorbs the candidate first. |
| `non_circularity_status` | Independent, calibrated, fitted, circular, or unknown. |
| `ask_or_drop` | Ask deeper, use as comparator, or drop as absorbed. |

## Status Boundary

This plan changes no physical-admission item.

Candidate `X`: no.

`Q^nu`: no.

Phase-B `w ~= -1` rationale: no.

`delta Q`: no.

Known-model distinction: no.

QFUDS support: no.

Roadmap status change: no.

Physical-QFUDS Level 2B change: no.
