---
doc_id: lit_li_2025_desi_dr2_sign_reversal_ide
title: Li 2025 DESI DR2 Sign-Reversal IDE
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

# Li 2025 DESI DR2 Sign-Reversal IDE

## Bibliographic Metadata

- Paper: "Cosmic sign-reversal: non-parametric reconstruction of interacting
  dark energy with DESI DR2"
- Authors: Yun-He Li, Xin Zhang
- arXiv: [2506.18477](https://arxiv.org/abs/2506.18477)
- DOI: [10.1088/1475-7516/2025/12/018](https://doi.org/10.1088/1475-7516/2025/12/018)
- Venue: JCAP

## Key Equations

- Studies vacuum energy with `w = -1` interacting with cold dark matter.
- Uses a non-parametric reconstruction of a redshift-dependent coupling
  function.
- The energy-transfer form is reported as `Q = beta(a) H rho_de`.

## Coupling Definitions

- Primary cache variable: `beta(z)` or equivalently `beta(a)`.
- The reconstruction discretizes `beta(z)` into 20 redshift bins and uses a
  Gaussian smoothness prior.

## Datasets Used

- DESI DR2 BAO.
- Planck CMB.
- PantheonPlus.
- DESY5.
- Union3.

## Redshift Coverage

- The reconstruction uses 20 redshift bins.
- Principal-component figures shown in the paper cover low-to-intermediate
  redshifts relevant to DESI-era timing audits.

## Available Products

- Tables: yes.
- Posterior samples: not found in the checked public sources.
- MCMC chains: not found in the checked public sources.
- Covariance matrices: not found in the checked public sources.
- Reconstructed histories: figures.
- Figures: yes.
- PCA summaries: yes, reported in the paper.
- arXiv source bundle: yes; contains LaTeX and figure PDFs, but no numerical
  `beta(z)` histories, covariance products, posterior samples, chains, or PCA
  mode arrays were found in the source package during the 2026-06-09 product
  search.

## Digitization Requirements

Digitization or author-provided reconstruction products would be required for a
curve-level timing comparison. Table and figure products are enough only for a
coverage audit.

## Public Code / Data Links

- arXiv page provides PDF, HTML, and TeX source links.
- Public IDECAMB code infrastructure exists at
  [liaocrane/IDECAMB](https://github.com/liaocrane/IDECAMB), but it is not a
  Li and Zhang 2025 output-product repository.
- No public posterior-product, covariance-product, chain, numerical-history, or
  PCA-product repository was found during the 2026-06-09 product search.

## QFUDS Relevance

Reference role: high-priority missing DESI-era nonparametric IV/IDE timing
coverage.

This record does not state that retained timing is supported.

## Use Restrictions

- Treat the Gaussian smoothness prior as part of the reconstruction method.
- Do not compare `beta(z)` directly to retained `Gamma(a)` without a convention
  and timing-only mapping.
- Do not use figure-level curves as numerical evidence without a digitization
  protocol.

## Check History

- 2026-06-09: arXiv page and public search checked for bibliographic metadata,
  paper products, and public posterior-product availability.
- 2026-06-09: dedicated public product search checked arXiv source, JCAP/IOP,
  GitHub, Zenodo, OSF, Dataverse, and general web search. Result: timing-overlap
  matrix is only partially executable from current public products; author data
  or figure digitization is required for uncertainty-aware comparison.
