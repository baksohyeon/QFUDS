---
doc_id: lit_tsedrik_2025_boss_des_y3_dark_scattering
title: Tsedrik 2025 BOSS DES Y3 Dark Scattering
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-09
record_type: literature_record
paper_year: 2025
availability_last_checked: 2026-06-09
used_by:
  - exp_006_coverage_expansion
---

# Tsedrik 2025 BOSS DES Y3 Dark Scattering

## Bibliographic Metadata

- Paper: "Interacting dark energy constraints from the full-shape analyses of
  BOSS DR12 and DES Year 3 measurements"
- Authors: M. Tsedrik, S. Lee, K. Markovic, P. Carrilho, A. Pourtsidou, C.
  Moretti, B. Bose, E. Huff, A. Robertson, P. L. Taylor, J. Zuntz
- arXiv: [2502.03390](https://arxiv.org/abs/2502.03390)
- DOI: [10.1093/mnrasl/slaf055](https://doi.org/10.1093/mnrasl/slaf055)
- Venue: Monthly Notices of the Royal Astronomical Society: Letters

## Key Equations

- Studies Dark Scattering, an interacting dark energy model with pure momentum
  exchange between dark energy and dark matter.
- Uses growth-sensitive probes rather than a background-only timing
  reconstruction.

## Coupling Definitions

- Primary cache variable: Dark Scattering interaction parameters.
- This is a momentum-exchange IDE family, not a vacuum-energy transfer kernel.

## Datasets Used

- DES Y3 `3x2pt` measurements.
- BOSS DR12 full-shape galaxy power spectrum multipoles plus BAO.
- External BAO measurements.
- Planck PR4 for comparison.

## Redshift Coverage

- Timing coverage is encoded through growth-sensitive low- and intermediate-
  redshift probes, not through a reconstructed redshift-dependent coupling
  curve.

## Available Products

- Tables: yes.
- Posterior samples: not found in the checked public sources.
- MCMC chains: not found in the checked public sources.
- Covariance matrices: input data products are public for BOSS/DES families,
  but paper-specific posterior covariance was not found.
- Reconstructed histories: not applicable.
- Figures: yes.
- Public likelihood/data link: BOSS full-shape likelihood data link surfaced in
  the journal page.

## Digitization Requirements

Digitization is not the main route for this paper. Its value is as
growth-sensitive IDE coverage, not as a reconstructed timing-history source.

## Public Code / Data Links

- arXiv page provides PDF, HTML, and TeX source links.
- Journal page references public BOSS full-shape likelihood data:
  [full_shape_likelihoods data](https://github.com/oliverphilcox/full_shape_likelihoods/tree/main/data)

## QFUDS Relevance

Reference role: high-priority growth-sensitive IDE coverage adjacent to retained
structure-era timing.

This record does not provide direct support for retained timing.

## Use Restrictions

- Do not treat momentum exchange as equivalent to energy-transfer timing.
- Use only to check whether structure-growth-sensitive IDE constraints should
  be included in later coverage.

## Check History

- 2026-06-09: arXiv page, journal metadata, and public data-link references
  checked.
