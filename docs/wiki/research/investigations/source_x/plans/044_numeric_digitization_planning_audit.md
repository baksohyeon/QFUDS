---
doc_id: audit_2026_06_11_numeric_digitization_planning_audit
title: "2026-06-11 Numeric Digitization Planning Audit"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_black_hole_data_product_audit
  - audit_2026_06_11_product_recovery_candidate_selection_plan
  - audit_2026_06_11_product_recovery_execution_plan
  - audit_2026_06_11_product_recovery_extraction_plan
  - audit_2026_06_11_product_recovery_extraction_result
  - asset_lacy_2024_smbh_density_recovery_extract
  - asset_chen_2026_merger_entropy_history_recovery_extract
  - roadmap
next_gate: approved numeric digitization execution only; no physical admission
last_updated: 2026-06-11
---

# 2026-06-11 Numeric Digitization Planning Audit

## Purpose

This planning audit follows the
[2026-06-11 Product-Recovery Extraction Result](../conclusions/043_product_recovery_extraction_result.md).

The `043` extraction recovered source files, equations, figures, tables,
normalization clues, and entropy-history clues from the selected Lacy and Chen
asset chains. It did not recover a standalone numeric product:

- no standalone `rho_BH(a)` curve;
- no standalone `d rho_BH / dln(a)` curve;
- no standalone `S_BH(a)` curve;
- no standalone `dS_BH / dln(a)` curve.

This document decides whether a future digitization pass can recover usable
curves from already identified assets. It does not digitize, extract new values,
create structured products, or modify asset records.

## Status Boundary

The current blocker remains:

```text
data_product_blocked
```

This is not a `physics_blocked` decision.

Roadmap status remains unchanged.

Physical-QFUDS Level 2B remains blocked.

`Gamma(a)` remains a prototype phenomenological transfer profile.

No physical source is admitted here.

No `Q^nu` is derived here.

No `delta Q` is derived here.

No candidate `X` is derived here.

No QFUDS support claim is made here.

## Authorities

Authority order:

1. [Black-Hole Data Product Audit](../conclusions/040_black_hole_data_product_audit.md)
2. [Product-Recovery Candidate Selection Plan](041_product_recovery_candidate_selection_plan.md)
3. [Product-Recovery Execution Plan](042_product_recovery_execution_plan.md)
4. [Product-Recovery Extraction Result](../conclusions/043_product_recovery_extraction_result.md)

If these records conflict, earlier records in this list win.

## Candidate Evaluation

### Lane A: Lacy Figure 1

Candidate source:
[scenario1_revised.png](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/figures/extracted/scenario1_revised.png).

Source support:
[Lacy density recovery extract](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/digitization/lacy_2024_smbh_density_recovery_extract.md).

Target:
`rho_BH(a)`.

| Check | Evaluation |
| --- | --- |
| Figure quality | Medium. Cached PNG is `1296 x 648`; the figure is readable but split into three panels with several line styles and point markers. |
| Axis readability | Medium. Redshift and log-density axes are visible; panel-specific legends and overlapping curves make automated extraction fragile. |
| Uncertainty visibility | Partial. The Shen et al. uncertainty band and point error bars are visible, but numeric uncertainty bounds are not directly machine-readable from the figure. |
| Digitization feasibility | Medium. Manual curve digitization is possible for selected curves, but panel selection and curve identity must be recorded. |
| Expected recovery accuracy | Medium-low for full curves because multiple curves share panels and line styles; better for approximate comparator curves than for a primary product. |
| Expected product type | Candidate `rho_BH(a)` comparator or source-history curve, not a QFUDS product. |
| Expected missing fields | Covariance, reusable posterior, full normalization route, resolved local-unit conflict, and candidate `X`. |
| Digitization required? | Yes, if a numeric curve is needed from the figure. |
| Equation reconstruction preferable? | Yes. Equation 9 and its input assumptions should be reconstructed first where possible, then Figure 1 should be used as a visual cross-check. |

Decision:
do not recover this first. Use it after the Equation 9 reconstruction route has
been checked.

### Lane A: Lacy Figure 2

Candidate source:
[Salpeter_plot_revised.png](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/figures/extracted/Salpeter_plot_revised.png).

Source support:
[Lacy density recovery extract](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/digitization/lacy_2024_smbh_density_recovery_extract.md).

Target:
constraint support for `d rho_BH / dln(a)`, not a direct history curve.

| Check | Evaluation |
| --- | --- |
| Figure quality | Medium. Cached PNG is `1296 x 504`; three panels and colored exclusion regions are readable. |
| Axis readability | Medium-high for `k` and `log10(t_S / yr)`; not a direct redshift-history axis. |
| Uncertainty visibility | Low for a curve product. It shows exclusion regions and assumptions, not a numeric history uncertainty band. |
| Digitization feasibility | Medium for boundaries and regions; low for recovering `d rho_BH / dln(a)`. |
| Expected recovery accuracy | Medium for approximate exclusion-boundary tracing; low for source-history product recovery. |
| Expected product type | Comparator or constraint map, not a source-history curve. |
| Expected missing fields | Direct redshift coverage, derivative values, source-history normalization, covariance, candidate `X`. |
| Digitization required? | Not required for the next product-recovery step. |
| Equation reconstruction preferable? | Yes. Use the Salpeter-time and Equation 9 support route before any region digitization. |

Decision:
do not use as the first digitization target. Keep it as a Lane A consistency and
constraint check.

### Lane A: Equation 9 Support Route

Candidate source:
[AGN_BHgrowth.tex](../../../assets/lacy_2024_smbh_accretion_coupling_constraints/source/extracted/AGN_BHgrowth.tex),
Equation 9 as cited by the `043` extract.

Target:
`rho_BH(a)` reconstruction route.

| Check | Evaluation |
| --- | --- |
| Figure quality | Not applicable. |
| Axis readability | Not applicable. |
| Uncertainty visibility | Partial through named inputs: AGN luminosity density, radiative efficiency, Eddington ratio, and local density assumptions. |
| Digitization feasibility | Not a digitization task. |
| Expected recovery accuracy | Potentially higher than figure tracing if all required input functions and conventions are recoverable from source files. |
| Expected product type | Equation-reconstructed `rho_BH(a)` candidate, still source-history only. |
| Expected missing fields | Input-function machine tables, covariance, resolved local-unit conflict, candidate `X`, QFUDS normalization route. |
| Digitization required? | No. |
| Equation reconstruction preferable? | Yes, for Lane A this should precede Figure 1 digitization. |

Decision:
attempt equation-based reconstruction before Lane A figure digitization, but
only in a later approved task.

### Lane B: Chen Figure 5

Candidate source:
[growth_entropy_gwtc4_only.png](../../../assets/chen_2026_merger_entropy_budget/figures/extracted/growth_entropy_gwtc4_only.png).

Source support:
[Chen merger entropy history recovery extract](../../../assets/chen_2026_merger_entropy_budget/digitization/chen_2026_merger_entropy_history_recovery_extract.md).

Target:
`S_BH(a)` or entropy-density history from merger-generated entropy.

| Check | Evaluation |
| --- | --- |
| Figure quality | High. Cached PNG is `2036 x 1764`; curves, axes, and uncertainty bands are legible. |
| Axis readability | High, with redshift on the bottom axis and lookback time on the top axis. The blue and red curves use separate y axes and must not be mixed. |
| Uncertainty visibility | Medium-high. Shaded uncertainty bands are visible around both curves, but digitized band boundaries would still need explicit method notes. |
| Digitization feasibility | High relative to the other candidates. It contains clear primary curves over `z in [0.01,20]`. |
| Expected recovery accuracy | Medium-high for visual digitization of central curves; medium for uncertainty bands because the bands are translucent and overlap near the peak. |
| Expected product type | Numeric digitized entropy-history candidate: `S_BH(a)` for the blue curve and/or entropy density for the red curve. |
| Expected missing fields | Covariance, source code reproduction route, entropy-to-energy conversion law, QFUDS normalization route, candidate `X`. |
| Digitization required? | Yes, if the goal is a reusable numeric curve. |
| Equation reconstruction preferable? | No for the first pass. Figure digitization is the most direct next recovery step; equation support can be used after the curve is digitized. |

Decision:
recover this first in a future approved digitization task.

### Lane B: Chen Figure 6

Candidate source:
[cumulative_ent_den_gwtc4_only.png](../../../assets/chen_2026_merger_entropy_budget/figures/extracted/cumulative_ent_den_gwtc4_only.png).

Source support:
[Chen merger entropy history recovery extract](../../../assets/chen_2026_merger_entropy_budget/digitization/chen_2026_merger_entropy_history_recovery_extract.md).

Target:
cumulative `S_BH(a)` comparison history.

| Check | Evaluation |
| --- | --- |
| Figure quality | High. Cached PNG is `2353 x 1764`; primary cumulative curve and comparator curves are readable. |
| Axis readability | Medium-high. Axes are legible, but the large legend covers part of the low-redshift plot region. |
| Uncertainty visibility | Medium. The BBH uncertainty band is visible, but comparator bands and overlap complicate extraction. |
| Digitization feasibility | Medium. The main curve can be digitized, but comparison curves and legend overlap increase provenance burden. |
| Expected recovery accuracy | Medium for the main cumulative curve; lower near the covered legend region and overlapping comparator curves. |
| Expected product type | Numeric digitized cumulative entropy comparator, not the first source-history product. |
| Expected missing fields | Covariance, source code reproduction route, entropy-to-energy conversion law, QFUDS normalization route, candidate `X`. |
| Digitization required? | Optional after Figure 5. It is useful as a cumulative cross-check. |
| Equation reconstruction preferable? | No for first recovery; use Figure 5 first, then use Figure 6 to compare cumulative behavior. |

Decision:
keep as second-line Lane B validation or cumulative-history follow-up.

### Lane B: Chen Figure 7

Candidate source:
[cumulative_tot_ent_gwtc4_pbh.png](../../../assets/chen_2026_merger_entropy_budget/figures/extracted/cumulative_tot_ent_gwtc4_pbh.png).

Source support:
[Chen merger entropy history recovery extract](../../../assets/chen_2026_merger_entropy_budget/digitization/chen_2026_merger_entropy_history_recovery_extract.md).

Target:
retrospective entropy-density history.

| Check | Evaluation |
| --- | --- |
| Figure quality | High. Cached PNG is `2957 x 1771`; the main curve and comparator curves are readable. |
| Axis readability | Medium-high. Redshift and lookback-time axes are legible; interpretation is less direct because the plotted quantity is retrospective density. |
| Uncertainty visibility | Medium. The main uncertainty band is visible but overlaps with comparator regions. |
| Digitization feasibility | Medium-high for the main black-hole curve; medium for uncertainty bands. |
| Expected recovery accuracy | Medium for the central curve; lower for uncertainty envelope and intersections. |
| Expected product type | Numeric digitized retrospective entropy-density candidate, not standalone `S_BH(a)`. |
| Expected missing fields | Entropy-to-energy conversion law, physical density interpretation, covariance, QFUDS normalization route, candidate `X`. |
| Digitization required? | Optional after Figure 5 if the retrospective density definition is needed. |
| Equation reconstruction preferable? | Equation 16 should be used as the interpretation guardrail, but figure digitization remains the practical recovery method for the plotted curve. |

Decision:
valuable follow-up target, but not first because the retrospective-density
definition adds interpretation risk.

### Lane B: Equation 16 Support Route

Candidate source:
[sample631.tex](../../../assets/chen_2026_merger_entropy_budget/source/extracted/sample631.tex),
Equation 16 as cited by the `043` extract.

Target:
retrospective entropy-density definition.

| Check | Evaluation |
| --- | --- |
| Figure quality | Not applicable. |
| Axis readability | Not applicable. |
| Uncertainty visibility | Partial through Figure 7 text and peak uncertainties. |
| Digitization feasibility | Not a digitization task. |
| Expected recovery accuracy | Useful for interpreting Figure 7, but insufficient alone without the underlying cumulative entropy and comoving-volume inputs. |
| Expected product type | Equation support and normalization check for retrospective entropy density. |
| Expected missing fields | Underlying source arrays, covariance, entropy-to-energy conversion law, QFUDS normalization route, candidate `X`. |
| Digitization required? | No for the equation itself. |
| Equation reconstruction preferable? | Preferable only as an interpretation check after Figure 5; not preferable as the first recovery method. |

Decision:
use Equation 16 as support for later Figure 7 work, not as the first recovery
target.

## Required Decision

First curve to recover:

```text
Chen Figure 5: growth_entropy_gwtc4_only.png
```

Recommended first product:

```text
numeric_digitized source-history candidate for the Figure 5 blue entropy curve
S_BH(a), with the red entropy-density curve recorded separately if digitized
```

Lane priority:

```text
Lane B before Lane A
```

Method priority:

```text
1. Digitize Chen Figure 5 central curve and visible uncertainty band.
2. Record redshift, a = 1 / (1 + z), ln(a), entropy units, axis mapping,
   curve color, y-axis side, and digitization uncertainty.
3. Keep Chen Table 1 and Figure 5 text values as normalization checks.
4. Use Chen Figure 6 and Figure 7 only as follow-up validation targets.
5. For Lane A, attempt Equation 9 input reconstruction before Figure 1
   digitization.
```

Equation-based reconstruction should be attempted before figure digitization for
Lane A only. For Lane B, Figure 5 digitization is the more direct first recovery
route because the plotted curve is already a redshift-history product.

## Expected Risks

- Chen Figure 5 has two y axes; the future digitization must keep blue entropy
  and red entropy density as separate quantities.
- Figure-derived products will remain `numeric_digitized`, not source-code
  reproduced.
- Visible uncertainty bands do not provide covariance.
- No candidate `X` boundary is defined by digitizing these figures.
- No entropy-to-energy conversion law is supplied by Chen Figure 5.
- Lacy Figure 1 may tempt direct tracing, but the unresolved local-unit conflict
  and Equation 9 input dependence make equation reconstruction the safer first
  Lane A route.

## Expected Value

Chen Figure 5 is the highest-value first target because it is the clearest
already-cached redshift-history curve in the retained black-hole lanes. A future
digitization could convert the current `manual_structured_extract` into a
`numeric_digitized` source-history candidate.

That would improve the data-product state but would not, by itself, admit a
physical source into QFUDS.

## Readiness For Future Execution

Ready for a future numeric digitization execution task only if that task is
explicitly approved.

Future execution must write any numeric digitization output under the relevant
asset directory, for example:

```text
docs/wiki/research/assets/chen_2026_merger_entropy_budget/digitization/
```

This `044` plan does not create that output.

## Final Decision

Proceed next, if approved, with Lane B numeric digitization of Chen Figure 5.

Do not proceed to physical admission, `Q^nu`, `delta Q`, or Level 2B from this
planning audit.

The black-hole lane remains:

```text
data_product_blocked
```
