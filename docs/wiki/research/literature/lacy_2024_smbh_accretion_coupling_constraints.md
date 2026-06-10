---
doc_id: lit_lacy_2024_smbh_accretion_coupling_constraints
title: Lacy 2024 SMBH Accretion Coupling Constraints
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

# Lacy 2024 SMBH Accretion Coupling Constraints

## Bibliographic Metadata

- Paper: "Constraints on cosmological coupling from the accretion history of
  supermassive black holes"
- Authors: Mark Lacy, Athena Engholm, Duncan Farrah, Kiana Ejercito
- arXiv: [2312.12344](https://arxiv.org/abs/2312.12344)
- DOI: [10.3847/2041-8213/ad1b5f](https://doi.org/10.3847/2041-8213/ad1b5f)
- Venue: Astrophysical Journal Letters

## Short Summary

Lacy et al. use the accretion history of supermassive black holes to constrain
cosmological coupling strength, finding bounds below the strong `k = 3`
dark-energy-source case under the reported assumptions. For QFUDS this is an
accretion-history constraint comparator. It is not a QFUDS source history or an
admission-rule completion.

## Key Equations

- Tests black-hole mass coupling to cosmic expansion using SMBH mass density at
  `z=0` and accreted AGN mass since `z=6`.
- Constrains the coupling index `k`; the abstract reports `0 < k <~ 2` under a
  local SMBH mass-density estimate, below `k = 3` needed for black holes to be
  the dark-energy source term.

## Coupling Definitions

- Primary cache variable: cosmological coupling index `k`.
- Accretion history is used as a constraint on how much SMBH mass can arise
  from non-accretion cosmological coupling.

## Datasets Used

- Local SMBH mass density.
- AGN luminosity density to `z ~= 6`.
- Radiative accretion efficiency range.
- PTA gravitational-wave-background mass-density estimates considered as an
  alternate case.

## Redshift Coverage

- AGN accretion-history comparison to `z ~= 6`.

## Available Products

- Tables/figures: paper products available.
- Posterior samples/chains/covariances: not found in this quick cache pass.
- Public code/data repository: not found in this quick cache pass.

## Digitization Requirements

Useful as a qualitative and semi-quantitative constraint record. Reproducing
the constraints requires extracting paper values or obtaining author products.

## Public Code / Data Links

- arXiv abstract/PDF/HTML/source: <https://arxiv.org/abs/2312.12344>
- Journal DOI: <https://doi.org/10.3847/2041-8213/ad1b5f>

## QFUDS Relevance

Reference role: accretion-history constraint comparator for black-hole mass
growth as a source lane.

It does not supply QFUDS `Q^nu`, phase-B pressure rationale, or `delta Q`.

## Use Restrictions

- Use as a constraint on CCBH-like source assumptions, not as QFUDS evidence.
- Do not map `k` bounds into QFUDS without a specific QFUDS black-hole source
  model.

## Check History

- 2026-06-10: arXiv metadata and abstract checked for coverage audit.
