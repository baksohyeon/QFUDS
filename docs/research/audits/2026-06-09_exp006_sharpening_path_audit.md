---
doc_id: audit_2026_06_09_exp006_sharpening_path
title: "2026-06-09 Exp006 Sharpening Path Audit"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_09_exp006_literature_availability
  - result_006_literature_timing_support_audit
next_gate: none; sharpening-path audit only
last_updated: 2026-06-09
record_type: availability_audit
audit_date: 2026-06-09
used_by:
  - exp_006
---

# 2026-06-09 Exp006 Sharpening Path Audit

## Audit Objective

Identify whether Exp006 can be sharpened beyond table-level compatibility
without running a new likelihood analysis, rerunning Exp006, reopening Level
1.5, or introducing a new physical hypothesis.

This audit uses the local research cache as the primary source:

- [Escamilla 2023 Interacting Dark Energy Kernel](../literature/escamilla_2023_interacting_dark_energy_kernel.md)
- [Goh 2023 Tomographic Coupled Dark Energy](../literature/goh_2023_tomographic_coupled_dark_energy.md)
- [Bonilla 2022 Dark Sector Interaction GP](../literature/bonilla_2022_dark_sector_interaction_gp.md)
- [Martinelli 2019 Interacting Vacuum Geodesic CDM](../literature/martinelli_2019_interacting_vacuum_geodesic_cdm.md)
- [Hogg 2020 Vacuum Geodesic CDM Interaction](../literature/hogg_2020_vacuum_geodesic_cdm_interaction.md)
- [Wang 2015 Dark Matter Vacuum Interaction](../literature/wang_2015_dark_sector_interaction_reconstruction.md)
- [2026-06-09 Exp006 Literature Availability Audit](2026-06-09_exp006_literature_availability_audit.md)

It records sharpening paths only. It does not change the Exp006 classification.

## Product Availability

| Paper | Role | Public products found | Public posterior-level products found | Author data likely required |
| --- | --- | --- | --- | --- |
| Escamilla et al. 2023 | primary | tables and functional-posterior figures | no | likely |
| Goh et al. 2023 | secondary proxy | tables and public modified CLASS code | no public chains found | unknown |
| Bonilla et al. 2022 | optional | figures and request-based observational data note | no | likely |
| Martinelli et al. 2019 | historical | tables and figures | no | unknown |
| Hogg et al. 2020 | historical | figures and request-based supporting-data statement | no public products found | yes |
| Wang et al. 2015 | historical | figures | no | unknown |

The direct Exp006 blocker remains the same: the primary Escamilla product has
tables and figures, but no public posterior samples, MCMC chains, covariance
matrices, or numerical reconstructed `Pi_DE(z)` histories were found in the
local cache.

## Sharpening Value By Product

| Product | Expected information gain | Practical feasibility | Audit use |
| --- | --- | --- | --- |
| Escamilla posterior samples or reconstructed `Pi_DE(z)` histories | highest | medium | direct test of timing support beyond broad table intervals |
| Escamilla node covariance matrix or GP functional-posterior numerical grid | high | medium-low | tests whether the `z ~ 2.3` feature is posterior-supported or node-correlation/prior-shaped |
| Escamilla figure digitization with uncertainty protocol | medium | high | approximate curve-level timing audit if author data are unavailable |
| Hogg request-based supporting data | medium | medium | historical vacuum-geodesic CDM comparison; not primary Exp006 evidence |
| Bonilla author data or digitization | low-medium | medium | optional GP comparison; figure-only without data |
| Goh tables/code | low for Exp006 | high | secondary scalar-field CDE proxy only |

## Figure Digitization Feasibility

Figure digitization can recover useful timing information only at qualitative or
semi-quantitative level.

It is acceptable for a sharpening audit if it records:

- exact source figure and paper version;
- axis calibration;
- redshift range and overlap with retained timing support;
- mean curve extraction method;
- uncertainty-band extraction method;
- sign convention notes;
- digitization uncertainty and failure modes.

It is not enough by itself to claim posterior-level support unless the
uncertainty bands can be recovered reliably and the comparison remains direct to
Escamilla's IV/IDE kernel variable.

## Upgrade Requirement

Moving Exp006 from `allowed_but_not_informative` to
`supported_compression_target` would require all of the following:

- a direct IV/IDE product, preferably Escamilla `Pi_DE(z)`, not a scalar-field
  proxy alone;
- nontrivial structure-era support near the retained weighted-mean and peak
  regions;
- uncertainty narrow enough to distinguish retained-like timing from zero
  coupling, late-time-only coupling, and generic smooth or binned timing
  families;
- sign convention compatibility, or explicitly mixed sign support rather than a
  clean opposite-sign preference;
- a documented treatment of the high-redshift shoulder, including whether the
  `z > 2.4` region remains unconstrained.

Broad inclusion inside 95 percent bands is not enough.

## Archive Requirement

The timing-prior branch can be confidently archived if one of these becomes
true:

- Escamilla posterior products or author data are unavailable, and figure
  digitization cannot recover uncertainty well enough for a meaningful timing
  comparison.
- Direct IV/IDE products remain broad, zero-compatible, or unconstrained in the
  retained peak and high-redshift shoulder regions.
- Sharper direct IV/IDE products prefer late-time-only, sign-incompatible, or
  strongly oscillatory histories that make the retained single-pulse timing too
  restrictive.
- A same-data comparison shows retained timing is redundant with simpler
  constant, low-bin tomographic, late-time, or broad smooth-pulse timing
  families.

Archiving this branch would not reject QFUDS broadly. It would only close the
retained timing-prior branch as a useful IV/IDE compression target under the
available literature products.

## Ranked Next Options

| Rank | Option | Feasibility | Expected information gain | Decision value |
| ---: | --- | --- | --- | --- |
| 1 | Request Escamilla posterior samples or numerical reconstructed histories | medium | highest | best route to sharpen or archive |
| 2 | Request Escamilla node covariance or GP numerical grid | medium-low | high | tests whether table nodes can support timing structure |
| 3 | Run a dedicated Escamilla figure-digitization audit | high | medium | useful fallback, but uncertainty-limited |
| 4 | Request Hogg 2020 supporting data | medium | medium | historical comparison; not primary Exp006 target |
| 5 | Request or digitize Bonilla 2022 histories | medium | low-medium | optional direct-adjacent GP comparison |
| 6 | Extend Goh 2023 table/code comparison | high | low | proxy only; cannot promote IV/IDE support |

## Recommendation

The current broad constraints can be narrowed only if stronger numerical
products are obtained. The first practical move is an author-data request for
Escamilla posterior samples, reconstructed `Pi_DE(z)` histories, or covariance
products.

If that fails, the next bounded step is a separate figure-digitization audit.
If digitization cannot recover uncertainty reliably, the branch should be
archived rather than promoted.
