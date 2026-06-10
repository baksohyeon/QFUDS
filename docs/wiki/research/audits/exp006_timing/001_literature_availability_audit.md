---
doc_id: audit_2026_06_09_exp006_literature_availability
title: "2026-06-09 Exp006 Literature Availability Audit"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - research_audit_index
  - literature_cache_index
next_gate: none; availability audit only
last_updated: 2026-06-09
record_type: availability_audit
audit_date: 2026-06-09
used_by:
  - exp_006
---

# 2026-06-09 Exp006 Literature Availability Audit

## Audit Objective

Record dated availability checks for literature products relevant to Exp006 and
nearby IV/IDE reconstruction papers.

This audit records search state only. It does not change Exp006, the roadmap,
or any QFUDS research conclusion.

## Papers Checked

| Paper | Cache record | Availability state |
| --- | --- | --- |
| Escamilla et al. 2023 | [Escamilla 2023 Interacting Dark Energy Kernel](../../literature/escamilla_2023_interacting_dark_energy_kernel.md) | tables and figures found; public posterior products not found |
| Goh et al. 2023 | [Goh 2023 Tomographic Coupled Dark Energy](../../literature/goh_2023_tomographic_coupled_dark_energy.md) | tables and public code found; public chains not found |
| Bonilla et al. 2022 | [Bonilla 2022 Dark Sector Interaction GP](../../literature/bonilla_2022_dark_sector_interaction_gp.md) | figures found; table-level timing history not found |
| Martinelli et al. 2019 | [Martinelli 2019 Interacting Vacuum Geodesic CDM](../../literature/martinelli_2019_interacting_vacuum_geodesic_cdm.md) | tables and figures found; public posterior products not found |
| Hogg et al. 2020 | [Hogg 2020 Vacuum Geodesic CDM Interaction](../../literature/hogg_2020_vacuum_geodesic_cdm_interaction.md) | figures found; supporting data request statement found |
| Wang et al. 2015 | [Wang 2015 Dark Matter Vacuum Interaction](../../literature/wang_2015_dark_sector_interaction_reconstruction.md) | figures found; public posterior products not found |

## Search Inputs

Representative searches:

```text
Escamilla 2023 Model-independent reconstruction interacting dark energy kernel arXiv DOI data availability
Goh 2023 Constraining constant and tomographic coupled dark energy arXiv GitHub
Bonilla 2022 Reconstruction dark sectors interaction model-independent inference forecast standard sirens arXiv data availability
Martinelli 2019 interacting vacuum geodesic CDM reconstruction arXiv data availability
Hogg 2020 latest evidence for a late time vacuum geodesic CDM interaction arXiv data availability
Wang 2015 model-independent reconstruction dark sector interaction arXiv
```

## Sources Checked

- arXiv article pages and available TeX source links.
- Journal or institutional data-availability pages when surfaced.
- GitHub search for public code or reconstruction products.
- Existing Exp006 source notes and table-level outputs.

## Products Found

- Escamilla et al. 2023: paper tables and functional-posterior figures.
- Goh et al. 2023: paper tables and public modified CLASS code.
- Bonilla et al. 2022: paper figures and request-based observational data note.
- Martinelli et al. 2019: paper tables and figures.
- Hogg et al. 2020: paper figures and request-based supporting-data statement.
- Wang et al. 2015: paper figures.

## Products Not Found

The 2026-06-09 check did not find public posterior samples, MCMC chains,
covariance matrices, or numerical reconstructed coupling histories for the
primary Exp006 Escamilla target.

This is a dated "not found" statement, not proof that the products do not exist.

## Author Data Requirement

- Escamilla et al. 2023: likely required for posterior-level comparison.
- Bonilla et al. 2022: likely required unless figure digitization is accepted.
- Hogg et al. 2020: explicitly request-based according to the checked data
  availability statement.

## Digitization Feasibility

Digitization is feasible for qualitative timing extraction from plotted
functional posteriors, but it would require a separate protocol for:

- source figure version;
- axis calibration;
- uncertainty-band extraction;
- redshift-domain overlap;
- sign convention notes.

Digitized figures should be stored under `docs/wiki/research/assets/digitization/`
only after a digitization audit is explicitly approved.

## Staleness Risk

Availability results are stale-prone. Before a future experiment classification
uses a "not found" claim, rerun the availability check or contact authors.

## Follow-Up Actions

- If Exp006 sharpening continues, prioritize author-provided Escamilla posterior
  products or numerical reconstructed histories.
- If author data is unavailable, design a separate figure-digitization audit
  before making curve-level claims.
