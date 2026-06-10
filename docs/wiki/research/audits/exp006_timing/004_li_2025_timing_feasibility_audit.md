---
doc_id: audit_2026_06_09_li_2025_timing_feasibility
title: "2026-06-09 Li 2025 Timing Feasibility Audit"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - lit_li_2025_desi_dr2_sign_reversal_ide
  - audit_2026_06_09_exp006_coverage_expansion
  - result_005_timing_prior_usefulness
  - result_006_literature_timing_support_audit
next_gate: no experiment yet; Li 2025 is feasible only after numerical histories, posterior products, covariance products, or documented digitization
last_updated: 2026-06-09
record_type: feasibility_audit
audit_date: 2026-06-09
used_by:
  - exp_006_coverage_expansion
---

# 2026-06-09 Li 2025 Timing Feasibility Audit

## Audit Objective

Determine whether Li and Zhang 2025 contains enough timing information to
support a meaningful comparison against the retained structure-era timing
profile.

This is a feasibility audit only. It does not create a new experiment, change
the Exp006 conclusion, modify roadmap status, perform posterior recovery, or
introduce a new physical hypothesis.

## Source Boundary

This audit uses the local research cache and existing Exp005/Exp006 results:

- [Li 2025 DESI DR2 Sign-Reversal IDE](../../literature/li_2025_desi_dr2_sign_reversal_ide.md)
- [2026-06-09 Exp006 Coverage Expansion Audit](003_coverage_expansion_audit.md)
- [Result 005: Timing-Prior Usefulness and Redundancy Audit](../../../../04_results/030_result_005_timing_prior_usefulness.md)
- [Result 006: Literature Timing-Support Audit](../../../../04_results/030_result_006_literature_timing_support_audit.md)

## Fixed Retained Timing Target

The retained timing target remains the Exp005 normalized
`information_production` `Gamma(a)` profile:

| Metric | Value |
| --- | ---: |
| peak redshift | `z ~= 2.046` |
| weighted mean redshift | `z ~= 1.746` |
| half-max support | `z ~= 0.259 to 4.632` |
| half-max width | `Delta ln(a) ~= 1.498` |
| `z > 1100` leakage fraction | `0` |
| `z > 10` leakage fraction | `0.000215` |

Only timing overlap is in scope. Amplitude, sign, and physical transfer
interpretation require separate convention handling.

## Li and Zhang Timing Information

Li and Zhang 2025 is a direct DESI-era nonparametric interacting-vacuum timing
target:

| Item | Feasibility relevance |
| --- | --- |
| `Q = beta(a) H rho_de` | Direct interacting-vacuum energy-transfer form, closer to retained P1 than scalar-field CDE proxies. |
| `beta(z)` / `beta(a)` | Primary timing variable for comparison after convention mapping. |
| 20 redshift bins | Finer timing support than the Escamilla table-level node/bin products used in Exp006. |
| Gaussian smoothness prior | Must be treated as part of the reconstruction, not as data-only evidence. |
| sign reversal | Can test whether retained single-pulse timing is compatible, too restrictive, or sign-mismatched. |
| high-redshift deviation from zero | Potentially relevant to the retained peak and high-redshift shoulder. |
| PCA summaries | Can test how many timing modes are data-constrained rather than prior-dominated. |
| DESI DR2, Planck CMB, PantheonPlus, DESY5, Union3 | Modern dataset coverage beyond the original Exp006 Escamilla-centered audit. |

This is the first cached target that can plausibly test whether retained timing
compresses a modern nonparametric IV/IDE reconstruction rather than merely
falling inside broad older table intervals.

## Directly Comparable Quantities

The following quantities are directly comparable after a timing-only mapping:

| Li and Zhang quantity | Retained timing comparison | Current feasibility |
| --- | --- | --- |
| Redshift support of nonzero or weakly nonzero `beta(z)` | Overlap with `z ~= 1.746` weighted mean, `z ~= 2.046` peak, and `z ~= 0.259 to 4.632` half-max support | feasible from figures qualitatively; numerical comparison needs data or digitization |
| Sign-reversal redshift | Whether retained single-pulse support aligns with the positive/negative phase relevant to the chosen convention | feasible qualitatively; convention-sensitive |
| High-redshift positive or nonzero region | Whether retained peak/high-z shoulder is supported, unconstrained, or contradicted | feasible qualitatively; rigorous comparison needs uncertainty bands |
| PCA data-dominated modes | Whether the reconstruction has enough constrained timing structure for compression tests | feasible from paper summaries; mode-shape comparison needs numerical eigenvectors |
| Reconstructed mean curve | Shape RMS/max-error against retained timing and simpler alternatives | requires numerical history or digitized curve |
| 68/95 percent uncertainty bands | Distinguish support from broad compatibility with zero | requires numerical bands, posterior products, covariance products, or reliable digitization |

The following are not directly comparable without extra assumptions:

- `beta(z)` amplitude versus retained `Gamma(a)` amplitude;
- sign interpretation before fixing the transfer convention;
- physical QFUDS source interpretation;
- likelihood-level preference for retained timing over other timing priors.

## Available Products

Current cache state:

| Product | Availability | Feasibility use |
| --- | --- | --- |
| Paper tables | found | parameter/data summary and limited feasibility routing |
| Figures | found | qualitative timing overlap and possible digitization source |
| PCA summaries | found | identifies whether a few timing modes carry the reconstruction signal |
| Reconstructed histories | figures only | usable only after digitization or author data |
| Public posterior samples | not found | missing for rigorous posterior-level comparison |
| MCMC or nested-sampling chains | not found | missing for likelihood/posterior replay |
| Covariance matrices | not found | missing for uncertainty-weighted timing comparison |
| Numerical `beta(z)` grid or mode vectors | not found | missing for reproducible curve-level comparison |

A published-material-only audit can assess qualitative overlap. It cannot
establish that retained timing is supported rather than merely compatible.

## Published-Material-Only Assessment

Published material is enough to answer:

- Li and Zhang is a relevant direct IV/IDE timing target.
- The timing product is meaningfully richer than the original Exp006 Escamilla
  table-level product.
- Retained structure-era support overlaps the type of redshift region Li and
  Zhang is designed to reconstruct.
- A later comparison is worth executing if numerical products or a documented
  digitization route are available.

Published material is not enough to answer:

- whether retained timing beats zero coupling;
- whether retained timing beats late-time-only coupling;
- whether retained timing beats generic smooth-pulse or low-bin timing
  families;
- whether sign-reversal timing makes retained single-pulse timing too
  restrictive;
- whether the high-redshift shoulder is data-supported or prior-shaped.

## Digitization Sufficiency

Digitization would be sufficient for a bounded, intermediate analysis if it
captures:

- the source figure version;
- redshift-axis calibration;
- reconstructed mean `beta(z)`;
- 68 and 95 percent uncertainty bands;
- sign convention notes;
- the redshift range covering retained weighted mean, peak, and shoulder;
- extraction uncertainty and failure modes.

Digitization would be enough to classify qualitative or semi-quantitative timing
overlap. It would not by itself support a likelihood-level or posterior-level
promotion unless the uncertainty bands are reliable enough to distinguish
retained-like support from zero, late-time-only, and generic smooth timing
families.

## Posterior Or Covariance Requirement

Posterior samples, covariance products, or author-provided numerical histories
are required for a rigorous comparison.

They are required because the decision boundary is not simple overlap. The
comparison must test whether retained timing is informative relative to:

- zero coupling;
- late-time-only coupling;
- a broad smooth pulse;
- low-bin tomography;
- the data-dominated PCA modes reported by Li and Zhang;
- sign-reversal histories that may not be compressible by a single retained
  pulse.

Without posterior or covariance information, a curve-level comparison risks
treating a prior-smoothed mean curve as stronger evidence than it is.

## Potential Classification Impact

Answer:

```text
yes, conditionally
```

A Li and Zhang comparison realistically has the power to move the retained
timing branch from:

```text
allowed_but_not_informative
```

toward:

```text
supported_compression_target
```

but only if it uses uncertainty-bearing numerical products or a documented
digitization that recovers uncertainty bands well enough for model-family
comparison.

The reason is that Li and Zhang is a direct modern nonparametric IV/IDE timing
target, not only additional literature coverage. Its 20-bin `beta(z)`
reconstruction, sign-reversal behavior, high-redshift deviation, and PCA
summaries are exactly the type of timing structure Exp006 lacked.

The current public-cache products are not enough to move the classification on
their own. They justify a comparison; they do not yet supply a result.

## Smallest Executable Analysis

The smallest next executable analysis is a Li and Zhang timing-overlap matrix,
not a new physical hypothesis.

Inputs:

- retained Exp005 timing fingerprint;
- Li and Zhang redshift bins or digitized redshift grid;
- sign convention note for `Q = beta(a) H rho_de`;
- published or digitized mean `beta(z)`;
- published, digitized, covariance-derived, or posterior-derived uncertainty
  bands.

Outputs:

- overlap of Li and Zhang timing support with retained weighted mean, peak, and
  half-max support;
- classification of each retained region as supported, zero-compatible,
  sign-incompatible, unconstrained, or not comparable;
- RMS/max-error comparison between normalized Li and Zhang timing support,
  retained timing, and simpler pulse/tomographic timing families;
- explicit flag for whether the comparison used paper-only facts,
  digitization, author data, covariance products, or posterior products.

Minimum useful version:

```text
paper-plus-digitization timing-overlap matrix with uncertainty-band extraction
```

Best rigorous version:

```text
posterior/covariance timing-compression test against retained, smooth-pulse,
low-bin tomographic, late-time-only, and zero-coupling families
```

## Recommendation

Proceed with Li and Zhang before opening a new experiment only if the next step
is framed as data-product acquisition or digitization feasibility.

Do not promote retained timing from `allowed_but_not_informative` using the
published paper summary alone. The comparison becomes classification-relevant
only after numerical histories, posterior/covariance products, or documented
uncertainty-bearing digitization exist.
