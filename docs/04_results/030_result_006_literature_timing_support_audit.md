---
doc_id: result_006_literature_timing_support_audit
title: "Result 006: Literature Timing-Support Audit"
doc_type: result
stage: "2"
status: completed
evidence_role: audit
depends_on:
  - exp_006_literature_timing_support_audit
  - result_005_timing_prior_usefulness
next_gate: retained timing is allowed but not informative at table level; no prior use without stronger posterior products
last_updated: 2026-06-09
---

# Result 006: Literature Timing-Support Audit

Date: 2026-06-09

## Executive Verdict

Exp006 classifies retained structure-era timing as:

```text
allowed_but_not_informative
```

Escamilla et al. 2023 is sufficient for a coarse table-level primary audit. It
does overlap the retained structure-era window, including the retained weighted
mean and peak regions. But the overlap is weak evidence only: the relevant
table-level constraints are broad, zero-compatible, or explicitly
unconstrained.

This means retained timing is not excluded by the inspected literature products,
but the table products do not support using it as an informative IV/IDE prior.

## Scope

This was a coarse, table-level timing-support audit only.

It establishes:

- Escamilla et al. 2023 is usable as the primary table-level IV/IDE kernel
  comparison target;
- Goh et al. 2023 is usable only as a secondary scalar-field CDE proxy;
- Bonilla et al. 2022 remains optional because the inspected products do not
  provide table-level coupling histories;
- retained timing is allowed by current table-level products, but not
  informatively supported.

It does not establish:

- physical QFUDS validation;
- a physical source for retained `Gamma(a)`;
- a new `Q^nu`;
- physical Level 2B readiness;
- CMB, matter-power, BAO, supernova, DESI, Euclid, Roman, or likelihood
  viability;
- novelty of QFUDS, P1, or retained `Gamma(a)`;
- sign or amplitude viability of retained `Gamma(a)`.

## Evidence

No likelihood run, Boltzmann run, curve fit, or figure digitization was
performed.

Primary outputs:

```text
outputs/exp006_literature_target_feasibility.csv
outputs/exp006_literature_timing_support_matrix.csv
outputs/exp006_literature_classification.json
```

Inspected source products:

| Paper | Role | Product used |
| --- | --- | --- |
| Escamilla et al. 2023 | primary | paper text and Table 3 constraints for `Pi_1...Pi_5` |
| Goh et al. 2023 | secondary proxy | paper tables for 7-bin and 4-bin tomographic `beta_i` constraints |
| Bonilla et al. 2022 | optional | paper text and figures only; no table-level timing history used |

## Primary Target: Escamilla 2023

Escamilla et al. reconstruct the dimensionless interaction kernel
`Pi_DE(z)`, with `Pi_DM = -Pi_DE`, using both GP and binned approaches.

The useful table-level comparisons are:

| Product | Retained timing region | Reported value | Audit interpretation |
| --- | --- | ---: | --- |
| GP, `w=-1`, `z=1.5` | near retained weighted mean | `Pi_3=-0.29 (1.04)` | broad and zero-compatible |
| GP, `w=-1`, `z=2.25` | near retained peak | `Pi_4=0.93 (5.34)` | broad and zero-compatible |
| GP, `w0` free, `z=1.5` | near retained weighted mean | `Pi_3=-0.22 (1.14)` | broad and zero-compatible |
| GP, `w0` free, `z=2.25` | near retained peak | `Pi_4=5.35 (5.82)` | weak structure-era feature, still broad |
| GP, both cases, `z=3.0` | retained high-z shoulder | `Pi_5 unconstr.` | cannot test high-z shoulder |
| binned, both cases, retained peak and high-z shoulder | `z >= 1.8` | `Pi_4`, `Pi_5` unconstr. | cannot resolve retained peak/tail with binned table product |

The paper text also reports an oscillatory-like GP behavior, with a more
prominent maximum around `z ~ 2.3`. That is relevant because it overlaps the
retained peak near `z ~= 2.046`. It is not enough to classify retained timing as
a supported compression target, because the table constraints remain broad and
the high-redshift shoulder is unconstrained.

## Secondary Proxy: Goh 2023

Goh et al. constrain scalar-field CDE `beta(z)`, not an interacting-vacuum
transfer kernel. Exp006 therefore treats it only as an adjacent timing proxy.

The relevant table-level proxy bins are:

| Product | Retained timing region | Reported value | Audit interpretation |
| --- | --- | ---: | --- |
| 7-bin, `1 < z < 2`, Planck+ACT1800+SPT+BSC | near retained weighted mean | `beta_2 < 0.124` | allowed, not preferred |
| 7-bin, `2 < z < 5`, Planck+ACT1800+SPT+BSC | contains retained peak | `beta_3 < 0.094` | allowed, not preferred |
| 7-bin, `2 < z < 5`, plus RSD | contains retained peak | `beta_3=0.064 (-0.023,+0.018)` | secondary proxy activity, not direct IV evidence |
| 4-bin, `1 < z < 2`, 3x2pt | near retained weighted mean | `beta_3=0.016 (-0.010,+0.007)` | small proxy activity |
| 4-bin, `z > 2`, 3x2pt | retained peak/tail coarsely | `beta_4=0.015 (-0.011,+0.006)` | too coarse to resolve retained timing |

Goh does not contradict the Escamilla-based classification. It also cannot
promote retained timing to a supported IV/IDE prior, because `beta(z)` is a
scalar-field CDE coupling proxy.

## Optional Target: Bonilla 2022

Bonilla et al. reconstruct `delta(z)=q(1+z)^-6`, with `q=Q/H0^3`, and is
scientifically relevant to the same broad question. It was not used for the
Exp006 classification because the inspected paper/source did not provide
table-level coupling histories or posterior products. Using it for timing
support would require author-provided data or explicit figure digitization.

## Decision

The predeclared classification is:

```text
allowed_but_not_informative
```

Why this is not `supported_compression_target`:

- Escamilla overlaps the retained weighted-mean and peak regions, but the
  relevant table constraints are broad and zero-compatible.
- The binned Escamilla product leaves the retained peak and high-z shoulder
  unconstrained.
- `Pi_5` is unconstrained in all Escamilla cases, so the retained high-z
  shoulder cannot be tested.
- Goh is useful only as a secondary proxy and cannot promote the conclusion.

Why this is not `inconclusive_due_to_data_limitations`:

- Escamilla provides enough table-level information to answer the coarse audit
  question.
- The answer is not "no information"; it is "allowed, but too weak to be
  informative."

Why this is not `disfavored_aesthetic_only`:

- No direct table-level IV/IDE conflict with retained structure-era support was
  found.
- The retained peak region is weakly allowed in the Escamilla GP product.

Why this is not `redundant_with_existing_timing_families`:

- Exp006 did not find table-level evidence that the literature support reduces
  specifically to constant, low-bin tomographic, late-time, or broad smooth
  pulse families.
- The available products are too coarse to establish redundancy.

## Next Gate

Do not use retained timing as an informative IV/IDE prior from Exp006 alone.

The next gate, if this phenomenological branch continues, is one of:

- obtain posterior samples or author-provided reconstructed coupling histories
  for Escamilla et al. 2023;
- perform an explicitly documented figure-digitization audit with uncertainty
  bounds;
- design a likelihood-level prior test where retained timing is compared
  against simpler timing families and flexible reconstructions under the same
  data model.

Until one of those exists, the retained timing status is:

```text
allowed by current table-level literature products, but not informative enough
to justify prior use.
```
