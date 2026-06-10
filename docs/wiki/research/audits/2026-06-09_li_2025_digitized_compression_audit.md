---
doc_id: audit_2026_06_09_li_2025_digitized_compression
title: "2026-06-09 Li 2025 Digitized Compression Audit"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - audit_2026_06_09_li_2025_timing_overlap_matrix_plan
  - audit_2026_06_09_li_2025_timing_feasibility
  - result_005_timing_prior_usefulness
  - result_006_literature_timing_support_audit
next_gate: no roadmap change; retained timing remains a partial component overlap, not a supported compression target
last_updated: 2026-06-09
record_type: digitized_compression_audit
audit_date: 2026-06-09
---

# 2026-06-09 Li 2025 Digitized Compression Audit

## Audit Objective

Determine whether the retained Exp005 structure-era timing profile provides a
better low-dimensional description of the Li and Zhang 2025 reconstructed
`beta(z)` timing structure than simpler timing families.

This audit does not create a new physical hypothesis, reopen [Level 1.5](../../glossary/repository_levels.md), change
roadmap status, or change Exp004, Exp005, or Exp006 conclusions.

## Execution Boundary

Evidence level:

```text
digitized_uncertainty
```

The audit uses rendered figure products, not author-provided numerical
histories, covariance products, PCA arrays, or posterior samples. The result is
therefore a timing-compression audit, not a likelihood-level classification.

Execution entry point:

```bash
python3 scripts/run_li2025_digitized_compression_audit.py
```

Generated outputs:

```text
outputs/li2025_digitized_compression_audit/digitized_li2025_beta_products.csv
outputs/li2025_digitized_compression_audit/li2025_digitized_compression_metrics.csv
outputs/li2025_digitized_compression_audit/li2025_digitized_compression_summary.json
```

Source figures:

```text
docs/wiki/research/assets/digitization/li_2025/fig_reconstruct.png
docs/wiki/research/assets/digitization/li_2025/fig_bin30.png
docs/wiki/research/assets/digitization/li_2025/fig_zmax.png
```

## Digitized Products

The script digitized:

- `fig_reconstruct`: four DESI DR2 red dashed panel products:
  - `desi_dr2_cmb_desi`;
  - `desi_dr2_pp`;
  - `desi_dr2_desy5`;
  - `desi_dr2_union3`.
- `fig_bin30`: `desy5_bin30` robustness reconstruction.
- `fig_zmax`: `desy5_zmax` high-redshift extension reconstruction.

For each product the extracted table contains:

- redshift grid `z`;
- digitized `beta_mean`;
- digitized 68 percent lower/upper bounds;
- digitized 95 percent lower/upper bounds;
- figure source and digitization uncertainty label.

The `fig_reconstruct` products are less reliable than the robustness products
because the DR2 mean and uncertainty contours are all red dashed curves. The
script therefore treats the central red locus by local percentile extraction.
The robustness figures have a solid red mean and filled uncertainty bands, so
their mean-curve extraction is cleaner.

## Normalized Timing Representations

For every digitized Li and Zhang product, the audit constructs:

```text
signed_history(z) = beta_mean(z) / max(abs(beta_mean))
```

This tests the full sign-reversal structure.

```text
positive_support(z) = max(beta_mean(z), 0) / max(max(beta_mean, 0))
```

This tests only the positive high-redshift component.

```text
evidence_weighted_support(z) = positive_support(z) * nonzero_weight(z)
```

where `nonzero_weight(z)` is approximated from the digitized 68 percent band as
`clip(abs(beta_mean) / sigma_68, 0, 2) / 2`.

The primary compression decision uses `evidence_weighted_support`, because the
retained timing profile is being tested as a support profile, not as a signed
energy-transfer history.

## Comparison Families

The retained profile is fixed from Exp005 and sampled on the Li and Zhang
redshift grid.

Competing timing families are fitted directly to each digitized Li and Zhang
target:

| Family | Timing role | Parameter count |
| --- | --- | ---: |
| zero coupling | null baseline | `0` |
| retained Exp005 timing | fixed structure-era profile | `0` fixed mode / `2` descriptive mode |
| logistic transition | sign/support transition | `2` |
| Gaussian pulse in `ln(a)` | smooth finite pulse | `2` |
| logistic pulse | smooth finite pulse | `2` |
| 3-bin tomography | low-bin flexible support | `3` |
| 5-bin tomography | low-bin flexible support | `5` |

The audit reports both fixed-prior and descriptive penalties for the retained
profile. The decision below uses the stricter descriptive comparison, because
the question is whether retained timing is a better interpretable compression
than other low-dimensional timing descriptions.

## Aggregate Metric Results

Average metrics over all six digitized products:

### Evidence-Weighted Positive Support

| Family | UW RMS | Support overlap | High-z capture | Explained vs zero | AIC-like descriptive |
| --- | ---: | ---: | ---: | ---: | ---: |
| zero coupling | `0.5636` | `0.0000` | `0.0000` | `0.0000` | `62.277` |
| retained Exp005 timing | `0.4836` | `0.4056` | `0.6971` | `0.1664` | `48.057` |
| logistic transition | `0.1043` | `0.8118` | `0.8525` | `0.9516` | `6.377` |
| Gaussian pulse | `0.1099` | `0.8200` | `0.8451` | `0.9429` | `6.716` |
| logistic pulse | `0.1119` | `0.8020` | `0.8447` | `0.9437` | `6.713` |
| 3-bin tomography | `0.2960` | `0.6212` | `0.6957` | `0.6618` | `22.937` |
| 5-bin tomography | `0.1874` | `0.7262` | `0.7643` | `0.8621` | `16.865` |

### Positive Support

| Family | UW RMS | Support overlap | High-z capture | Explained vs zero | AIC-like descriptive |
| --- | ---: | ---: | ---: | ---: | ---: |
| zero coupling | `0.5404` | `0.0000` | `0.0000` | `0.0000` | `76.044` |
| retained Exp005 timing | `0.5034` | `0.4613` | `0.7428` | `-0.0002` | `68.139` |
| logistic transition | `0.0931` | `0.8408` | `0.8791` | `0.9533` | `6.671` |
| Gaussian pulse | `0.1081` | `0.8296` | `0.8591` | `0.9439` | `7.311` |
| logistic pulse | `0.1132` | `0.8145` | `0.8601` | `0.9425` | `7.481` |
| 3-bin tomography | `0.2491` | `0.6777` | `0.7570` | `0.7332` | `22.246` |
| 5-bin tomography | `0.1632` | `0.7714` | `0.8152` | `0.8756` | `17.317` |

### Signed History

| Family | UW RMS | Support overlap | High-z capture | Explained vs zero | AIC-like descriptive |
| --- | ---: | ---: | ---: | ---: | ---: |
| zero coupling | `0.4774` | `0.0000` | `0.0000` | `0.0000` | `452.069` |
| retained Exp005 timing | `0.7733` | `0.4997` | `0.5958` | `-2.2463` | `1133.808` |
| logistic transition | `0.1048` | `0.8008` | `0.8602` | `0.9134` | `31.691` |
| Gaussian pulse | `0.7743` | `0.4865` | `0.5963` | `-2.2651` | `1135.736` |
| logistic pulse | `0.7690` | `0.4894` | `0.5965` | `-2.2174` | `1120.266` |
| 3-bin tomography | `0.3275` | `0.6296` | `0.6888` | `0.2359` | `218.883` |
| 5-bin tomography | `0.2330` | `0.7028` | `0.7370` | `0.5632` | `124.811` |

## Primary DESY5 Robustness Products

The strongest Li and Zhang reconstruction and robustness products are the DESY5
panel and its 30-bin / high-z checks.

Evidence-weighted positive support:

| Product | Family | UW RMS | Support overlap | High-z capture | Explained vs zero | AIC-like descriptive |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| `desi_dr2_desy5` | retained | `0.5110` | `0.3519` | `0.6372` | `-0.0562` | `53.701` |
| `desi_dr2_desy5` | logistic transition | `0.1372` | `0.7424` | `0.7906` | `0.9239` | `7.581` |
| `desi_dr2_desy5` | Gaussian pulse | `0.1503` | `0.7518` | `0.7716` | `0.9086` | `8.300` |
| `desy5_bin30` | retained | `0.4681` | `0.4226` | `0.7913` | `0.3657` | `46.162` |
| `desy5_bin30` | logistic transition | `0.0162` | `0.9581` | `0.9839` | `0.9992` | `4.051` |
| `desy5_bin30` | Gaussian pulse | `0.0199` | `0.9501` | `0.9792` | `0.9989` | `4.076` |
| `desy5_zmax` | retained | `0.3571` | `0.6115` | `0.8170` | `0.7620` | `31.432` |
| `desy5_zmax` | logistic transition | `0.0786` | `0.9067` | `0.9229` | `0.9885` | `5.330` |
| `desy5_zmax` | Gaussian pulse | `0.0589` | `0.9103` | `0.9377` | `0.9935` | `4.745` |

## Interpretation

The retained timing profile does capture a real part of the Li and Zhang
timing structure:

- it overlaps the positive structure-era region;
- it captures a substantial fraction of high-redshift support;
- the `desy5_zmax` robustness product gives the retained profile its strongest
  showing, with high-z capture `0.8170` and explained fraction `0.7620`.

However, the retained profile does not provide the best low-dimensional
compression of the digitized Li and Zhang reconstruction.

The main failure mode is not the peak location. The main failure mode is shape:

- Li and Zhang is a sign-reversing transition-like reconstruction;
- retained Exp005 timing is a finite positive structure-era pulse with a
  nonzero low-redshift tail;
- the retained low-z positive tail mismatches the Li and Zhang low-z negative
  or zero-compatible region;
- fitted logistic transition and smooth pulse families capture the digitized
  support with much lower error and lower complexity-adjusted scores.

The signed-history result is especially hostile to retained timing. Retained
timing is not a signed sign-reversal compressor. It cannot describe the full
Li and Zhang `beta(z)` history without adding assumptions outside Exp005.

## Classification

Classification:

```text
partial_compression
```

Not:

```text
meaningful_compression
supported_compression_target
```

Reason:

```text
Retained timing captures part of the high-z structure-era support, but it does
not explain a meaningful fraction of the Li and Zhang timing structure more
efficiently than competing two-parameter transition or pulse families.
```

This audit also creates pressure toward:

```text
redundant_with_existing_timing_families
```

but does not use that as the terminal classification because the evidence is
still digitized figure evidence, not posterior/covariance evidence. A stronger
redundancy decision would require author numerical products, covariance
matrices, or posterior samples.

## Direct Answer

Question:

```text
Does the retained structure-era timing profile explain a meaningful fraction of
the Li and Zhang timing structure using fewer interpretable timing parameters
than competing timing families?
```

Answer:

```text
No, not under the digitized compression audit.
```

More precise answer:

```text
It explains a partial high-redshift structure-era component, but competing
logistic transition and smooth pulse families explain substantially more of the
digitized Li and Zhang timing structure with the same nominal timing complexity.
```

## What Changed

Changed:

- Li and Zhang 2025 moved from qualitative timing-overlap evidence to a
  digitized compression-audit result.
- The retained timing branch now has quantified partial support capture against
  Li and Zhang figure products.
- The compression question sharpened: the retained profile is not currently the
  best low-dimensional description of the Li and Zhang reconstruction.

Did not change:

- Exp004 remains an IV/IDE phenomenology classification.
- Exp005 remains `potentially_useful_compression_target`.
- Exp006 remains `allowed_but_not_informative`.
- No roadmap status changed.
- No Level 1.5 issue reopened.
- No physical QFUDS hypothesis was introduced.
- No likelihood-level or posterior-level claim was made.

## Recommendation

Do not promote retained timing to `supported_compression_target`.

The next evidence-improving action, if this branch continues, is not a new
physical hypothesis. It is either:

- obtain author numerical histories, covariance products, or posterior samples;
  or
- repeat this compression audit with a documented manual digitization protocol
  and independent extraction check.

Until then, retained timing should be described as:

```text
a partial high-z structure-era component overlap, not a demonstrated
compression target for the Li and Zhang reconstruction.
```
