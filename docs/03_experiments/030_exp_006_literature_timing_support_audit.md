---
doc_id: exp_006_literature_timing_support_audit
title: "Experiment 006: Literature Timing-Support Audit"
doc_type: experiment
stage: "2"
status: completed
evidence_role: audit
depends_on:
  - result_005_timing_prior_usefulness
  - result_004_p1_model_family_positioning
next_gate: result 006 classifies retained timing as allowed but not informative at table level
last_updated: 2026-06-09
---

# Experiment 006: Literature Timing-Support Audit

Date: 2026-06-09

## Objective

Test whether the retained structure-era `Gamma(a)` timing profile has coarse
support in published reconstructed or tomographic IV/IDE coupling histories.

The roadmap question is:

```text
Before using retained Gamma(a) as a prior, check whether actual IV/IDE
reconstructed or tomographic coupling histories have compatible timing support.
```

This experiment is a table-level audit only. It asks whether published
reconstructions allow or weakly prefer coupling support near the retained timing
window. It does not refit data and does not digitize figures unless a target is
explicitly reclassified as feasible before execution.

## Hypothesis

The retained profile remains useful as a phenomenological IV/IDE compression
target if actual reconstructed or tomographic literature products allow
structure-era support near the retained timing fingerprint:

| Retained timing metric | Value from result 005 |
| --- | ---: |
| peak redshift | `z ~= 2.046` |
| weighted mean redshift | `z ~= 1.746` |
| half-max support | `z ~= 0.259 to 4.632` |
| half-max width | `Delta ln(a) ~= 1.498` |
| `z > 1100` leakage fraction | `0` |

The working hypothesis is deliberately weak:

```text
retained timing may be compatible with current IV/IDE timing reconstructions
and may be worth testing later as a compression prior.
```

The hypothesis is not:

```text
data prefer QFUDS timing.
```

## Scope

This experiment can change conclusions about:

- whether retained timing should remain on the phenomenological IV/IDE track as
  a candidate compression prior;
- whether a future likelihood-level prior test is worth designing;
- whether Escamilla et al. 2023 provides enough table-level evidence to justify
  a more detailed posterior-product or author-data request;
- whether Goh et al. 2023 is useful as a secondary scalar-field CDE timing
  proxy;
- whether Bonilla et al. 2022 should remain optional because usable coupling
  products are not available without data request or digitization.

This experiment cannot change conclusions about:

- physical QFUDS validity;
- the retained branch's failed [Level 1.5](../wiki/glossary/repository_levels.md) physical promotion;
- physical Level 2B readiness;
- existence of a physical `Q^nu`, source field `X`, or phase-B vacuum-pressure
  derivation;
- novelty of P1 or retained `Gamma(a)` as a distinct physical model family;
- CMB, matter-power, BAO, supernova, DESI, Euclid, Roman, or likelihood-level
  viability;
- the sign or amplitude viability of retained `Gamma(a)`;
- any roadmap level/status table entry.

The only permitted conclusion is about timing-prior usefulness inside known
phenomenological IV/IDE or adjacent CDE model classes.

## Method

Use only numerical values reported in paper tables and text.

Primary target:

- Escamilla et al. 2023, "Model-independent reconstruction of the interacting
  dark energy kernel: Binned and Gaussian process."

Secondary proxy target:

- Goh et al. 2023, "Constraining constant and tomographic coupled dark energy
  with low-redshift and high-redshift probes."

Optional target:

- Bonilla et al. 2022, "Reconstruction of the dark sectors' interaction: A
  model-independent inference and forecast from GW standard sirens."

Bonilla et al. 2022 must remain optional unless one of these is true before
execution:

- reconstructed coupling-history numerical products are obtained from the
  authors or a public source;
- figure digitization is explicitly accepted as part of the audit scope;
- a table-level surrogate is identified that captures timing support beyond
  quoted `delta(z=0)` values.

Do not fit amplitudes. Do not normalize and compare full curves unless numerical
curves or posterior samples become available. For this specification, compare
only:

- reported coupling variable;
- redshift support;
- bin or node placement;
- reported mean, best-fit, uncertainty, upper limit, or unconstrained status;
- whether the retained peak and half-max support overlap constrained,
  weakly constrained, unconstrained, or absent literature regions;
- whether sign information, if available, is compatible, opposite, mixed, or not
  comparable.

## Parameters

Use the retained timing fingerprint from result 005 as the fixed comparison
target. No new QFUDS parameters are introduced.

Primary comparison mapping:

| Paper | Variable | Timing product | Use in Exp006 |
| --- | --- | --- | --- |
| Escamilla et al. 2023 | `Pi_DE(z)` with `Pi_DM = -Pi_DE`; also `I_Q(z)` for visualization | GP nodes at `z = [0.0, 0.75, 1.5, 2.25, 3.0]`; binned amplitudes with `Delta z = 0.6`; table constraints for `Pi_1...Pi_5` | Primary table-level IV/IDE kernel timing audit |
| Goh et al. 2023 | scalar-field CDE coupling strength `beta(z)` | 7-bin edges `{0,1,2,5,100,500,1000}` and 4-bin low-z edges `{0,0.5,1,2}` with table constraints | Secondary proxy only; not a direct vacuum-transfer variable |
| Bonilla et al. 2022 | `delta(z)=q(1+z)^-6`, `q=Q/H0^3` | GP-reconstructed coupling function, mainly shown as figures; some present-day values in text | Optional only if numerical products or acceptable digitization exist |

Escamilla-specific timing bins:

| Region | Relation to retained timing | Audit note |
| --- | --- | --- |
| `z < 0.6` or node `z = 0` | late tail and low-redshift shoulder | Useful for checking whether literature support is only late-time |
| `0.6 <= z < 1.2` or node `z = 0.75` | inside retained half-max support | Secondary support region |
| `1.2 <= z < 1.8` or node `z = 1.5` | near retained weighted mean | Key support region |
| `1.8 <= z < 2.4` or node `z = 2.25` | near retained peak | Key support region |
| `z > 2.4` or node `z = 3.0` | retained high-z shoulder, but literature data weak | Must be flagged if unconstrained |

Goh-specific timing bins:

| Binning | Relation to retained timing | Audit note |
| --- | --- | --- |
| 7-bin `1 < z < 2` | near retained weighted mean | Secondary proxy region |
| 7-bin `2 < z < 5` | contains retained peak and high-z shoulder | Secondary proxy region |
| 4-bin `1 < z < 2` and `z > 2` | lower-resolution low-z proxy | Useful only for late-time probe comparison |

## Outputs

This specification does not create outputs yet.

Required outputs if the experiment is later executed:

```text
outputs/exp006_literature_target_feasibility.csv
outputs/exp006_literature_timing_support_matrix.csv
outputs/exp006_literature_classification.json
```

Required result document after execution:

```text
docs/04_results/030_result_006_literature_timing_support_audit.md
```

The result must record the exact paper versions, source URLs or DOIs, and whether
each row came from a numerical table, text quote, author-provided data, or figure
digitization.

## Failure Criteria

The audit fails or becomes unresolved if:

1. it uses toy timing families instead of published IV/IDE or CDE literature
   products;
2. it treats Goh et al. 2023 as a direct interacting-vacuum transfer target
   rather than a scalar-field CDE proxy;
3. it treats Bonilla et al. 2022 figure-only information as numerical evidence
   without declaring digitization uncertainty;
4. it compares amplitudes without a documented convention mapping;
5. it removes amplitude and sign, then claims physical support;
6. it treats broad or unconstrained posterior regions as positive support;
7. it ignores that Escamilla et al. 2023 reports weak or absent constraints in
   the high-redshift region where the retained half-max tail extends;
8. it interprets compatibility with `Pi_DE = 0`, `beta = 0`, or
   sign-indefinite intervals as evidence that data prefer retained timing;
9. it changes roadmap level/status conclusions.

If any of these occur, classify the experiment as `inconclusive due to data
limitations` or `unresolved`, and do not update the roadmap beyond recording the
failed audit if the experiment was actually executed.

## Decision

Allowed classifications:

| Classification | Required condition | Meaning |
| --- | --- | --- |
| `supported_compression_target` | Escamilla table-level support overlaps the retained weighted-mean and peak regions, the relevant bins/nodes are constrained or weakly preferred rather than purely unconstrained, sign is compatible or mixed rather than clearly opposite, and Goh does not contradict the broad timing support as a secondary proxy. | Retained timing remains worth testing as a low-dimensional IV/IDE compression prior. This is not a data preference for QFUDS. |
| `allowed_but_not_informative` | Retained timing lies inside broad allowed intervals, but those intervals also allow zero coupling, opposite timing, or many alternative histories. | Current literature does not exclude retained timing, but compatibility is mostly lack of constraining power. |
| `redundant_with_existing_timing_families` | Literature tables support only timing structures already captured by simpler constant, low-bin tomographic, late-time, or broad smooth-pulse families, with no distinctive structure-era value for retained timing. | Retained timing is unnecessary as a named prior even if not excluded. |
| `disfavored_aesthetic_only` | Escamilla or another direct IV/IDE target constrains the structure-era peak region against retained-like support, prefers only late-time coupling, clearly prefers opposite sign in the relevant region, or leaves retained timing supported only by prior-shaped smoothing. | Retained timing should not be used as an IV/IDE prior-compression target under current evidence. |
| `inconclusive_due_to_data_limitations` | The primary region is unconstrained, table values are insufficient, redshift domains do not overlap the retained support, posterior products are unavailable, or the conclusion would depend on figure digitization not yet accepted. | Exp006 cannot answer the roadmap question with current literature products. |

Decision hierarchy:

1. Prefer `inconclusive_due_to_data_limitations` over a positive or negative
   claim when the evidence is dominated by missing posterior products,
   unconstrained high-redshift bins, or figure-only curves.
2. Prefer `allowed_but_not_informative` over `supported_compression_target` when
   retained timing is merely inside broad 95% regions.
3. Use `supported_compression_target` only if the primary Escamilla table-level
   evidence has meaningful overlap with retained structure-era support and does
   not depend on ignored sign or amplitude problems.
4. Use `disfavored_aesthetic_only` only for a direct IV/IDE conflict, not for
   the secondary Goh proxy alone.

Any final decision must keep this wording boundary:

```text
Exp006 can say whether retained timing is a plausible phenomenological
compression target for published IV/IDE coupling histories.
```

It must not say:

```text
Exp006 supports QFUDS physics, source derivation, novelty, or observational
viability.
```

## References

- L. A. Escamilla, O. Akarsu, E. Di Valentino, and J. A. Vazquez,
  "Model-independent reconstruction of the interacting dark energy kernel:
  Binned and Gaussian process," JCAP 11 (2023) 051,
  `arXiv:2305.16290`.
- L. W. K. Goh, A. Gomez-Valent, V. Pettorino, and M. Kilbinger,
  "Constraining constant and tomographic coupled dark energy with low-redshift
  and high-redshift probes," Phys. Rev. D 107 (2023) 083503,
  `arXiv:2211.13588`.
- A. Bonilla, S. Kumar, R. C. Nunes, and S. Pan, "Reconstruction of the dark
  sectors' interaction: A model-independent inference and forecast from GW
  standard sirens," MNRAS 512 (2022) 4231-4238, `arXiv:2102.06149`.
