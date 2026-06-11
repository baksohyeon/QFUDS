---
doc_id: audit_2026_06_09_li_2025_timing_overlap_matrix_plan
title: "2026-06-09 Li 2025 Timing-Overlap Matrix Plan"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_09_li_2025_timing_feasibility
  - lit_li_2025_desi_dr2_sign_reversal_ide
  - result_005_timing_prior_usefulness
  - result_006_literature_timing_support_audit
next_gate: no experiment yet; execute only after data-product search, author data, or digitization protocol
last_updated: 2026-06-11
record_type: execution_plan
audit_date: 2026-06-09
used_by:
  - exp_006_coverage_expansion
---

# 2026-06-09 Li 2025 Timing-Overlap Matrix Plan

## Purpose

Define the exact analysis that would be performed if Li and Zhang 2025 timing
products become available.

This is an execution plan and decision framework only. It does not create a new
experiment, change Exp006, change roadmap status, update the decision log,
perform posterior recovery, or introduce a new physical hypothesis.

## Fixed Scope

The planned analysis asks one timing-only question:

```text
Does the Li and Zhang beta(z) reconstruction contain enough structure-era
timing information to support the retained Exp005 profile as an informative
IV/IDE compression target?
```

It cannot answer:

- whether QFUDS is physically derived;
- whether retained `Gamma(a)` has a physical source;
- whether retained P1 is novel;
- whether the model passes CMB, matter-power, BAO, supernova, DESI, Euclid,
  Roman, or likelihood-level viability;
- whether [Level 2B](../../../glossary/repository_levels.md) should reopen.

## Required Inputs

| Input | Required content | Source or extraction route | Required for |
| --- | --- | --- | --- |
| Retained Exp005 timing fingerprint | peak `z ~= 2.046`, weighted mean `z ~= 1.746`, half-max support `z ~= 0.259 to 4.632`, `z > 10` leakage fraction, normalized retained profile if shape comparison is run | `outputs/exp005_timing_fingerprint.csv`, Result 005, and existing timing-prior code | every comparison |
| Li and Zhang redshift support | bin edges, bin centers, or digitized grid for the 20-bin `beta(z)` reconstruction | paper tables, TeX/source extraction, author data, or digitization | region overlap and shape comparison |
| Sign convention | mapping for `Q = beta(a) H rho_de`, including which sign corresponds to energy flow from CDM to vacuum energy and whether retained `Gamma(a)` sign is compared or ignored | Li and Zhang model section plus local retained P1 convention note | sign compatibility |
| Reconstructed mean `beta(z)` | mean curve or bin means across the plotted/data grid | author data, numerical table, posterior mean, or digitized figure | timing support and normalized shape |
| Uncertainty information | 68/95 percent bands, covariance matrix, posterior samples, chains, or documented digitization uncertainty | posterior/covariance products, author data, or digitization protocol | zero-compatibility and upgrade decision |
| PCA products | first data-dominated mode shapes and coefficients, or enough numerical data to reconstruct them | author data, paper source, or digitized PCA figures | mode compression and prior-shape diagnosis |
| Simpler comparison families | zero coupling, late-time-only support, smooth pulse, low-bin tomography, and retained profile sampled on the same grid | local scripts or a future experiment harness | redundancy test |

No amplitude comparison is allowed unless a separate convention mapping is
documented. The primary comparison is timing support and shape after
normalization.

## Extraction Routes

| Evidence level | Extraction route | Allowed use |
| --- | --- | --- |
| `paper_only_qualitative` | Read paper text, tables, figure captions, and reported PCA summaries. No curve extraction. | coverage and feasibility only |
| `digitized_uncertainty` | Digitize mean curve plus 68/95 percent bands from a named figure version with axis calibration and extraction uncertainty. | semi-quantitative overlap matrix |
| `author_numerical_history` | Use author-provided `beta(z)` grid, bin values, uncertainty bands, or PCA mode arrays. | reproducible overlap and shape comparison |
| `covariance_product` | Use covariance matrix for binned `beta_i` or PCA coefficients. | uncertainty-weighted shape and mode tests |
| `posterior_samples` | Use posterior samples or chains for `beta_i`, PCA coefficients, and cosmological nuisance parameters if supplied. | strongest classification-relevant comparison |

The minimum classification-relevant level is `digitized_uncertainty`. The
preferred level is `author_numerical_history`, `covariance_product`, or
`posterior_samples`.

## Matrix Rows

The timing-overlap matrix should contain one row per Li and Zhang bin, grid
segment, or PCA-supported redshift interval.

Required columns:

| Column | Meaning |
| --- | --- |
| `source_product` | figure, table, author file, covariance product, or posterior chain |
| `evidence_level` | one of the evidence levels above |
| `z_min`, `z_max`, `z_center` | Li and Zhang redshift support |
| `beta_mean` | reconstructed mean or bin mean |
| `beta_68_low`, `beta_68_high` | 68 percent interval, if available |
| `beta_95_low`, `beta_95_high` | 95 percent interval, if available |
| `digitization_sigma` | extraction uncertainty, if digitized |
| `retained_region` | low tail, weighted-mean region, peak region, high-z shoulder, outside support |
| `retained_weight` | retained normalized profile averaged over this bin or segment |
| `sign_status` | compatible, opposite, mixed, convention_pending, or not_comparable |
| `zero_status` | excludes_zero, weakly_nonzero, zero_compatible, unconstrained, or unknown |
| `support_status` | data_supported, prior_shaped, broad_compatible, unconstrained, sign_incompatible, or not_comparable |
| `notes` | convention, figure, or extraction caveats |

## Required Comparison Outputs

### Region Overlap

Report overlap with:

- retained weighted mean region: centered on `z ~= 1.746`;
- retained peak region: centered on `z ~= 2.046`;
- retained half-max support: `z ~= 0.259 to 4.632`;
- low-redshift tail: `z < 1`;
- high-redshift shoulder: `z > 2.4`, flagged separately because Exp006 could
  not test this region with Escamilla table products.

For each region, classify:

- sign compatibility;
- zero compatibility;
- whether support is data-supported, prior-shaped, broad-compatible, or
  unconstrained.

### Shape Comparison

If a mean curve and uncertainty are available:

1. Sample retained timing and all comparison families on the Li and Zhang grid.
2. Normalize timing shapes to compare support, not amplitude.
3. Compute unweighted and uncertainty-weighted metrics:

```text
rms_error
max_error
weighted_region_overlap
peak_offset_delta_z
weighted_mean_offset_delta_z
half_max_support_intersection_fraction
high_z_support_fraction
late_time_support_fraction
```

4. Compare retained timing against:

- zero coupling;
- late-time-only support;
- broad smooth pulse;
- Gaussian pulse in `ln(a)`;
- logistic transition-rate pulse;
- low-bin tomography;
- Li and Zhang data-dominated PCA reconstruction, if available.

The retained profile is useful only if it is informative relative to these
simpler alternatives.

### PCA Compression Check

If PCA mode shapes or covariance products are available:

- project the retained normalized profile onto the data-dominated PCA modes;
- project the simpler alternatives onto the same modes;
- compare how much data-constrained variance each profile captures;
- flag retained timing as prior-shaped if its apparent agreement lives mainly
  in modes that Li and Zhang identify as prior-dominated.

## Decision Boundaries

### `supported_compression_target`

Use only if all are true:

- evidence level is at least `digitized_uncertainty`;
- retained weighted-mean and peak regions overlap nonzero or weakly nonzero
  `beta(z)` support;
- the relevant support is not solely prior-shaped;
- zero coupling, late-time-only timing, and broad generic smooth-pulse timing
  are distinguishable from the retained-like support in the same data product;
- sign is compatible, mixed, or explicitly convention-mapped rather than
  cleanly opposite;
- high-redshift shoulder is either supported or honestly shown to be irrelevant
  to the Li and Zhang constrained range;
- retained timing performs at least as well as simpler pulse/tomographic
  alternatives on RMS/max-error or PCA-projection metrics;
- the result remains a phenomenological timing-prior claim only.

Sufficient upgrade result:

```text
Li and Zhang beta(z), with uncertainty, shows data-supported structure-era
coupling around z ~= 1.7-2.1; zero and late-time-only histories are disfavored
or materially worse in that region; retained timing matches the constrained
support at least as well as simpler smooth-pulse and low-bin alternatives under
the same grid, uncertainty, and sign convention.
```

### `allowed_but_not_informative`

Use if:

- retained support overlaps the Li and Zhang mean curve or broad bands; but
- zero coupling remains allowed in the weighted-mean or peak regions; or
- uncertainty is too broad to distinguish retained timing from simpler
  alternatives; or
- only qualitative paper-level overlap is available.

This preserves the current Exp006-style outcome.

### `redundant_with_existing_timing_families`

Use if:

- Li and Zhang support is real enough to compare; but
- a simpler timing family, such as late-time-only, Gaussian/logistic pulse, or
  low-bin tomography, matches the constrained support as well as or better than
  retained timing; and
- retained timing adds no clear compression value under the same evidence
  product.

This would not disfavor IV/IDE timing; it would disfavor retaining this named
profile as a useful prior.

### `disfavored_aesthetic_only`

Use if:

- Li and Zhang excludes or strongly disfavors retained-like structure-era
  support near `z ~= 1.746` and `z ~= 2.046`; or
- the sign convention is cleanly opposite in the retained support region; or
- the only apparent overlap is created by the Gaussian smoothness prior rather
  than data-dominated modes; or
- the reconstruction prefers a strongly sign-reversing or oscillatory history
  that a retained single-pulse profile would suppress.

This would close or archive the retained timing-prior branch as a useful Li and
Zhang compression target. It would not reject QFUDS broadly.

### `inconclusive_due_to_data_limitations`

Use if:

- only paper-level qualitative information is available;
- digitization cannot recover uncertainty bands reliably;
- redshift axes, sign convention, or figure uncertainty are ambiguous;
- posterior/covariance products are unavailable and the figure bands are too
  broad or unclear;
- the conclusion depends on high-redshift regions not constrained by Li and
  Zhang.

This is preferred over positive wording when the evidence cannot separate
support from compatibility.

## What Results Would Change

| Result | Would change | Would not change |
| --- | --- | --- |
| `supported_compression_target` | Retained timing can be used as an informative phenomenological IV/IDE prior candidate in a later experiment. | No physical QFUDS validation, no Level 2B reopening, no novelty claim, no roadmap level change by itself. |
| `allowed_but_not_informative` | Confirms that Li and Zhang does not yet sharpen Exp006 enough. | Does not archive retained timing; does not promote it. |
| `redundant_with_existing_timing_families` | Retained timing loses priority as a named prior if simpler families compress Li and Zhang equally well. | Does not rule out IV/IDE, P1 phenomenology, or future physical branches. |
| `disfavored_aesthetic_only` | Retained timing-prior branch should be archived for Li and Zhang-style timing compression. | Does not reject QFUDS broadly or the broader dark-sector phase-transition question. |
| `inconclusive_due_to_data_limitations` | Blocks classification movement until better products exist. | Does not imply support or exclusion. |

## Exact Analysis If Data Arrive

If Li and Zhang data products became available tomorrow:

1. Archive the raw products under `docs/wiki/research/assets/` with source, date,
   checksum if available, and product type.
2. Record whether the product is author data, covariance, posterior samples,
   chains, or digitization output.
3. Convert the Li and Zhang redshift support to a common `z` grid.
4. Sample retained Exp005 timing on the same grid.
5. Sample simpler comparison families on the same grid.
6. Apply the documented `Q = beta(a) H rho_de` sign convention.
7. Build the overlap matrix with mean, uncertainty, zero-status, sign-status,
   and retained-region labels.
8. Compute normalized shape metrics and uncertainty-weighted metrics.
9. If PCA products are present, project retained and simpler alternatives onto
   data-dominated modes.
10. Assign one of the five decision categories above.

## Recommended Next Step

Recommended order:

1. Public data/code search.
2. Author data request if no public numerical histories, covariance products,
   or chains are found.
3. Figure digitization protocol if author/public products are unavailable or
   delayed.
4. Direct experiment-spec creation only after one of the above yields a usable
   numerical or uncertainty-bearing product.

Do not create the experiment spec first. Without data products or a digitization
protocol, the experiment would only restate the feasibility audit and would not
be able to move the classification responsibly.
