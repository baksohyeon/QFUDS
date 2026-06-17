---
doc_id: audit_2026_06_17_foam_state_variable_placement_selection_matrix
title: "2026-06-17 Foam State Variable and Placement Selection Matrix"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - audit_2026_06_17_effective_foam_assumption_ledger_result
  - audit_2026_06_17_nasa_bao_baseline_constraint_map
  - wiki_governance_004_missing_physics_map
  - audit_2026_06_12_foam_sector_to_gamma_derivation_feasibility_result
  - roadmap
next_gate: define one candidate state variable and placement as a plan-only theory-definition checkpoint before model-facing NASA or BAO interpretation
last_updated: 2026-06-17
---

# 2026-06-17 Foam State Variable and Placement Selection Matrix

## Purpose

This document proposes and rejects candidate foam-sector state variables and
equation-side placements before any NASA/LAMBDA or BAO baseline constraint is
used for model-facing interpretation.

It is a selection matrix only.

It is not a derivation.

It is not an experiment result.

It does not claim QFUDS support.

It does not open Physical-QFUDS Level 2B.

It does not use NASA/LAMBDA, DESI, eBOSS, BAO, LSS, or retained timing targets
to choose `xi`, transition width, transition redshift, or amplitude.

## Workflow Application

This document uses the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md)
for the external baseline-source boundary inherited from the baseline-reference
chain.

Referenced source states:

- NASA/LAMBDA Graphic History: `asset_cached`;
- DESI DR2 Ly-alpha BAO: `asset_extracted_not_digitized` with `direct_table`
  products;
- eBOSS DR16 Ly-alpha BAO: `asset_cached` with `direct_table` products.

These states are baseline-source states only. They are not QFUDS evidence.

## Boundary

The current retained `Gamma(a)` remains a phenomenological IV/IDE comparator.
It cannot be reused as the physical foam-sector source.

The NASA + BAO baseline map remains a kill-map only. It can state what a future
model would have to pass. It cannot select the model variables.

The first non-circular step must be:

```text
choose a candidate state variable and equation-side placement
-> define the required equation and kill condition
-> only then compare to NASA/LAMBDA or BAO thresholds
```

## Verdict Labels

| Label | Meaning |
| --- | --- |
| `reject_now` | Reject as a current route; it is circular, undefined, or only a renamed known model. |
| `defer_until_equation` | Keep as a possible route only if a concrete equation and units are supplied first. |
| `candidate_for_next_definition` | Least-bad next target for a plan-only definition attempt, not accepted physics. |
| `downstream_only` | May appear only after a state variable and placement are defined. |
| `baseline_only` | Usable only as external constraint context, not model evidence. |

## Selection Metrics

| Metric | Pass condition | Fail condition |
| --- | --- | --- |
| State variable clarity | Variable has units, domain, normalization, and evolution target. | Variable is just `foam`, `xi`, `Gamma(a)`, or analogy language. |
| Non-circular scale rule | `xi`, width, redshift, and amplitude are fixed or derived before target comparison. | Values are chosen after looking at NASA/LAMBDA, BAO, LSS, or retained timing. |
| Equation-side placement | Route chooses geometry side, stress-energy side, or interaction source with consistency conditions. | Route switches sides to evade constraints. |
| Conservation consistency | Geometry route preserves Bianchi consistency, or stress-energy route states conservation/transfer. | Conservation is assumed by wording. |
| Phase-B rationale | Explains why the receiver behaves like smooth `w ~= -1` stress-energy. | Calls information, entropy, or foam vacuum-like without stress tensor or equation of state. |
| Perturbation route | Names the future `delta X`, `delta T_mu_nu`, or `delta Q^nu` requirement. | Claims CMB, matter-power, or clustering viability from background timing. |
| Known-model distinction | States the closest sink before novelty language. | Renames LCDM+EFTofLSS, backreaction, running vacuum, screened modified gravity, or IV/IDE. |
| Kill condition | Gives a predeclared way to stop. | Leaves every failure repairable by retuning width or amplitude. |

## State Variable Candidate Matrix

| Candidate | Meaning | Placement pressure | Closest known-model sink | Required equation before use | Current verdict |
| --- | --- | --- | --- | --- | --- |
| `xi ~= 10 Mpc` by itself | A length scale only | none | LCDM+EFTofLSS, halo-model smoothing, screened modified gravity | Definition as correlation length, cutoff, smoothing scale, or derived state property | `reject_now`; a length is not a state variable. |
| `X(x,a)` scalar foam order parameter | Coarse-grained local foam phase/order density | stress-energy first, unless geometry action is supplied | unified dark fluid, scalar-field DE, running vacuum | Evolution law for `X`, units, normalization, mapping to density/pressure or source | `candidate_for_next_definition` only. |
| `f_B(x,a)` phase-B volume or occupation fraction | Fraction of effective foam sector in vacuum-like phase B | stress-energy | unified dark fluid, IV/IDE, effective `w(a)` | Equation for `f_B`, relation to `rho_A`, `rho_B`, `p_B`, and conservation | `candidate_for_next_definition` only, but high known-model risk. |
| `C_X(r,a)` or `xi_X(a)` from a two-point function | Correlation function and derived correlation length of `X` | downstream of `X` | EFTofLSS, halo-model coarse graining | Two-point function, threshold definition for `xi_X`, evolution, and test split | `defer_until_equation`; cannot be first. |
| `lambda_F(x,a)` hazard or transition rate | Local rate for A-to-B conversion | interaction source | IV/IDE | Derivation from `X` or `f_B`, positivity, sign convention, background limit | `downstream_only`; circular if fitted to retained `Gamma(a)`. |
| `s_F(x,a)` entropy or information density | Coarse-grained entropy/information proxy | stress-energy only if stress tensor exists | entropic DE, HDE, black-hole entropy DE | Stress tensor or thermodynamic relation giving `rho`, `p`, and transfer | `reject_now` as current route; analogy is insufficient. |
| `B_D(a)` backreaction/averaging scalar | Domain-dependent inhomogeneity correction | geometry | backreaction | Averaging scheme, modified expansion equation, conservation relation | `defer_until_equation`; otherwise it is standard backreaction language. |
| `Delta G_mu_nu[X]` metric-side correction | Foam correction to Einstein geometry | geometry | modified gravity, screened gravity | Modified field equation, Bianchi identity handling, lensing/growth prediction | `defer_until_equation`; too unconstrained now. |
| `Q_foam^nu` as primitive source | Direct covariant transfer vector | interaction source | IV/IDE | Source variable underneath `Q^nu`, momentum-transfer frame, perturbation `delta Q^nu` | `reject_now` if primitive; `downstream_only` after `X` exists. |

## Placement Matrix

| Placement | What it would mean | Required consistency object | Advantage | Current blocker | Verdict |
| --- | --- | --- | --- | --- | --- |
| Geometry side | Modify the left side of Einstein's equation with foam-effective geometry. | Modified field equation plus Bianchi-compatible conservation relation. | Directly addresses spacetime/foam language. | No action, field equation, averaging scheme, or conservation closure. | `defer_until_equation`. |
| Stress-energy side | Treat foam as an effective dark-sector component or phase mixture. | Effective `T_mu_nu`, `rho`, `p`, equation of state, sound speed, and conservation or transfer law. | Forces concrete density/pressure and perturbation questions early. | Phase-B `w ~= -1`, sound speed, and perturbation route are missing. | `candidate_for_next_definition`, not accepted physics. |
| Interaction-source side | Treat foam as a source controlling energy exchange between A and B. | Non-fitted `Q^nu[X,...]`, frame choice, background limit, and `delta Q^nu`. | Connects to retained IV/IDE comparator language. | Collapses into IV/IDE if `Gamma(a)` is reused. | `downstream_only`. |
| Effective `w(a)` side | Treat the effect as reconstructed background expansion. | Background equation of state only. | Easy to compare at background level. | Too degenerate; no source, perturbations, or novelty. | `reject_now` for physical QFUDS. |
| Mixed side | Switch between geometry and stress-energy wording. | None unless formal equivalence map is supplied. | Rhetorically flexible. | Hides constraints and can evade failures. | `reject_now`. |

## Least-Bad Next Definition Target

If a next plan-only checkpoint is authorized, the least-bad target is:

```text
stress-energy-side scalar phase/order variable:
X(x,a) or f_B(x,a)
```

This is not because it is likely correct. It is least-bad because it forces the
missing objects into the open:

- `rho_F[X]`;
- `p_F[X]` or phase-B equation of state;
- conservation or transfer relation;
- perturbation placeholder `delta X` or `delta T_mu_nu`;
- known-model reduction test against unified dark fluid, running vacuum, and
  IV/IDE.

The geometry-side route should not be selected first unless the next document
can state a modified field equation or averaging equation. Otherwise it will
only rename backreaction or modified gravity.

The interaction-source route should not be selected first because it invites
reusing retained `Gamma(a)`. It can only come after `X` or `f_B` exists.

## Rejection Rules

Reject a candidate immediately if it does any of the following:

1. treats `xi ~= 10 Mpc` as a state variable;
2. chooses `xi`, transition width, transition redshift, or amplitude from
   NASA/LAMBDA, BAO, LSS, or retained timing and then calls that choice a foam
   source;
3. uses retained `Gamma(a)` as the physical source;
4. claims geometry-side modification without a Bianchi-compatible consistency
   statement;
5. claims stress-energy-side physics without `T_mu_nu`, equation of state, and
   sound-speed or perturbation requirements;
6. claims phase B has `w ~= -1` because it is foam, entropy, information, or
   vacuum-like by label;
7. claims known-model distinction without first naming the closest known-model
   sink.

## Decision

No candidate is accepted as physical QFUDS.

The next executable checkpoint, if opened, should be a plan-only theory
definition attempt for a stress-energy-side scalar order/phase variable
`X(x,a)` or `f_B(x,a)`.

NASA/LAMBDA and BAO remain blocked from model-facing interpretation until that
definition exists.

## Status Boundary Closeout

Candidate `X`: proposed only as a next-definition target, not supplied.

`Q^nu`: no.

Phase-B `w ~= -1` rationale: no.

`delta Q`: no.

Known-model distinction: no.

QFUDS support: no.

Roadmap status change: no.

Physical-QFUDS Level 2B change: no.
