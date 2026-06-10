---
doc_id: lit_lei_2024_jwst_black_holes_dark_energy_test
title: Lei 2024 JWST Black Holes Dark Energy Test
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-10
record_type: literature_record
paper_year: 2024
availability_last_checked: 2026-06-10
used_by:
  - source_x_black_hole_coupled_source_audit
---

# Lei 2024 JWST Black Holes Dark Energy Test

## Bibliographic Metadata

- Paper: "Black holes as the source of dark energy: a stringent test with
  high-redshift JWST AGNs"
- Authors: Lei Lei, Lei Zu, Guan-Wen Yuan, Zhao-Qiang Shen, Yi-Ying Wang,
  Yuan-Zhu Wang, Zhen-Bo Su, Wen-ke Ren, Shao-Peng Tang, Hao Zhou, Chi Zhang,
  Zhi-Ping Jin, Lei Feng, Yi-Zhong Fan, Da-Ming Wei
- arXiv: [2305.03408](https://arxiv.org/abs/2305.03408)
- DOI: [10.1007/s11433-023-2233-2](https://doi.org/10.1007/s11433-023-2233-2)
- Venue: Science China Physics, Mechanics & Astronomy 67, 229811 (2024)

## Short Summary

Lei et al. test the black-holes-as-dark-energy interpretation against
high-redshift JWST AGN host and black-hole mass estimates. The record is useful
for QFUDS only as a constraint comparator on strong black-hole cosmological
coupling. It does not provide a QFUDS source term, covariant transfer vector,
phase-B pressure derivation, or perturbation prescription.

## Key Equations

- Tests cosmological coupling with coupling index near `k = 3`.
- Compares high-redshift AGN host and black-hole masses against mass growth
  expected under the dark-energy-source hypothesis.

## Coupling Definitions

- Primary cache variable: cosmological coupling index `k`, especially `k = 3`.
- The test uses `M_star` and `M_BH` consistency for high-redshift JWST AGNs.

## Datasets Used

- JWST NIRSpec-/NIRCam-resolved AGNs and quasars.
- Three early-type host galaxies at `z ~ 4.5--7` are highlighted in the arXiv
  abstract.

## Redshift Coverage

- Main test range: `z ~ 4.5--7`.

## Available Products

- Tables: paper reports tables.
- Posterior samples: not found in this quick 2026-06-10 source check.
- MCMC chains: not found in this quick 2026-06-10 source check.
- Covariance matrices: not found in this quick 2026-06-10 source check.
- Figures: paper figures available through arXiv/PDF/HTML.
- Public code/data repository: not found in the quick source check.

## Digitization Requirements

The paper can be used qualitatively as a high-redshift constraint record. Any
numerical reuse of its mass-redshift comparisons would require table extraction
or author products.

## Public Code / Data Links

- arXiv abstract/PDF/HTML/source: <https://arxiv.org/abs/2305.03408>
- Journal DOI: <https://doi.org/10.1007/s11433-023-2233-2>

## QFUDS Relevance

Reference role: constraint comparator for the black-hole-coupled source lane.

The paper is relevant because it tests a central black-hole-as-dark-energy
coupling value at high redshift. It does not supply a QFUDS source equation,
QFUDS stress-energy transfer, or a phase-B perturbation prescription.

## Use Restrictions

- Use as a constraint/comparator, not as QFUDS evidence.
- Do not generalize the reported high-redshift tension to all black-hole source
  ideas without a model-specific mapping.

## Check History

- 2026-06-10: arXiv abstract, DOI metadata, and availability links checked for
  black-hole-coupled source audit caching.
