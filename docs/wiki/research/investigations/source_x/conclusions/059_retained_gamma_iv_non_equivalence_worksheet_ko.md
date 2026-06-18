---
doc_id: audit_2026_06_18_retained_gamma_iv_non_equivalence_worksheet_ko
title: Retained Gamma IV Non-Equivalence Worksheet
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - qfuds_lineage_gamma_to_academic_iv_bridge_result_ko
  - audit_2026_06_18_tier1_iv_extraction_pass_closeout_ko
  - audit_2026_06_18_martinelli_2019_iv_geodesic_cdm_equation_extraction_ko
  - audit_2026_06_18_hogg_2020_iv_geodesic_cdm_equation_extraction_ko
  - audit_2026_06_18_martinelli_hogg_iv_geodesic_cdm_same_family_comparison_note_ko
  - roadmap
next_gate: candidate source object X definition only; no retained timing fit or baseline-constraint use
last_updated: 2026-06-18
---

# Retained Gamma IV Non-Equivalence Worksheet

## Purpose

This worksheet compares the retained repo-local transfer convention against
the Martinelli/Hogg interacting-vacuum geodesic-CDM family.

It is not a fit. It is not a derivation. It is a stop-rule table.

Target comparison:

```text
Q_retained = H_conf Gamma(a) rho_A
Q_IV       = -q_V H V
```

Every conversion is marked as one of:

```text
defined
assumed
unknown
circular_if_fitted
```

## Workflow Boundary

This worksheet introduces no new external source, new cache, new numerical
product, or product-absence claim. It uses existing Source-X extraction records
only.

External-source handling remains governed by
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).
Inherited workflow states:

```text
asset_cached
asset_extracted_not_digitized
source_text_parse
manual_structured_extract
```

This worksheet is not QFUDS support, validation, novelty, or Level 2B
admission.

## Status Legend

| Status | Meaning |
| --- | --- |
| `defined` | The conversion is fixed by repo convention or extracted paper convention. |
| `assumed` | The conversion could be imposed for a toy comparison, but is not derived. |
| `unknown` | QFUDS has not supplied the required object or equation. |
| `circular_if_fitted` | The conversion becomes circular if chosen after inspecting the same observations used for claimed support. |

## Conversion Worksheet

| Conversion | Required for equivalence | Current status | Reason |
| --- | --- | --- | --- |
| `H_conf` to `H` | Convert conformal-Hubble convention to physical-Hubble convention. | `defined` | This is a convention conversion if scale-factor normalization is specified. |
| raw sign of `Q` | Align retained transfer direction with Martinelli/Hogg raw `Q` and `q_V` signs. | `defined` | The extracted records define `Q = -q_V H V`; sign must be tracked explicitly. |
| `Gamma(a)` to `q_V(a)` | Treat retained timing function as the IV coupling history. | `assumed` | It can be written as a worksheet identity, but no source equation derives it. |
| `rho_A` to CDM `rho_c` | Identify QFUDS phase A with the IV CDM component. | `assumed` | The retained branch behaves CDM-like at background level, but no source object derives equality. |
| phase B to vacuum `V` | Identify QFUDS phase B with interacting vacuum density. | `unknown` | QFUDS has not derived why phase B has vacuum pressure `w ~= -1`. |
| `rho_A / V` ratio | Use the ratio to algebraically map `Gamma(a)` into `q_V(a)`. | `assumed` | The ratio is not a physical source; it is a conversion factor after choosing component identities. |
| `Q^mu` placement | Put transfer along CDM four-velocity. | `unknown` | QFUDS has not derived `Q^mu[X]` or why the CDM/geodesic frame is selected. |
| momentum transfer | Set momentum transfer to zero in the CDM frame. | `unknown` | This is a Martinelli/Hogg model-family closure, not a QFUDS result. |
| vacuum perturbation boundary | Use homogeneous-vacuum or selected-gauge perturbation boundary. | `unknown` | QFUDS has no phase-B perturbation derivation. |
| `delta Q` prescription | Specify perturbation of the interaction. | `unknown` | Retained `Gamma(a)` is background timing only. |
| stability rule | Show perturbations are stable under the chosen closure. | `unknown` | No QFUDS-specific closure or stability proof exists. |
| solver route | Implement the model in CAMB/CLASS-like equations. | `unknown` | A retained timing function alone is not solver-ready. |
| prior/reconstruction guard | Prevent arbitrary timing reconstruction from becoming a source claim. | `defined` | Hogg-style prior/PCA boundary is an audit rule, not QFUDS physics. |
| transition redshift | Choose a `z ~= 2` timing feature. | `circular_if_fitted` | It is circular if selected after looking at the same observations used as support. |
| transition width | Choose the width of the transfer episode. | `circular_if_fitted` | Same risk as transition redshift unless derived before data comparison. |
| amplitude | Choose the strength of transfer. | `circular_if_fitted` | Same risk as transition redshift unless derived before data comparison. |

## Algebraic Worksheet Only

If one forces raw background equality:

```text
Q_retained = Q_IV
```

then:

```text
q_V(a) = - (H_conf / H) Gamma(a) rho_A / V
```

This is useful for checking conventions.

It is not a physical derivation because the hard objects remain missing:

```text
X
Q^mu[X]
phase-B pressure
delta Q
known-model escape equation
```

## Decision

Retained `Gamma(a)` is not equivalent to the Martinelli/Hogg IV/geodesic-CDM
family.

It can be compared to that family as a phenomenological timing worksheet only.
The current conversion table contains too many `assumed`, `unknown`, and
`circular_if_fitted` rows to support any stronger statement.

## Next Executable Instruction

If work continues, choose exactly one missing object and define it before any
data-facing comparison:

```text
X
```

The next checkpoint should ask whether QFUDS can define a source object `X`
that generates `rho_A`, phase-B pressure, and `Q^mu[X]` without selecting
`Gamma(a)`, `q_V(a)`, transition redshift, width, or amplitude from
observational timing.
