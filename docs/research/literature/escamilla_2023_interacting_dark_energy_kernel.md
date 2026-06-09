---
doc_id: lit_escamilla_2023_interacting_dark_energy_kernel
title: Escamilla 2023 Interacting Dark Energy Kernel
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-09
record_type: literature_record
paper_year: 2023
availability_last_checked: 2026-06-09
used_by:
  - exp_006
---

# Escamilla 2023 Interacting Dark Energy Kernel

## Bibliographic Metadata

- Paper: "Model-independent reconstruction of the Interacting Dark Energy
  Kernel: Binned and Gaussian process"
- Authors: Luis A. Escamilla, Ozgur Akarsu, Eleonora Di Valentino, J. Alberto
  Vazquez
- arXiv: [2305.16290](https://arxiv.org/abs/2305.16290)
- DOI: [10.1088/1475-7516/2023/11/051](https://doi.org/10.1088/1475-7516/2023/11/051)
- Venue: JCAP

## Key Equations

- Reconstructs an interacting dark energy kernel in a model-independent
  framework.
- Uses Gaussian-process and binned reconstructions.
- Table products report constraints on `Pi_1...Pi_5`.

## Coupling Definitions

- Primary variable for the Exp006 cache: `Pi_DE(z)`.
- The paper convention also uses `Pi_DM = -Pi_DE`.
- The related re-escalation function `I_Q(z)` is used for visualization in the
  paper, but Exp006 used `Pi_DE(z)` table products.

## Datasets Used

- BAO.
- Pantheon+ supernovae.
- Cosmic chronometers.

## Redshift Coverage

- GP nodes include `z = 0.0, 0.75, 1.5, 2.25, 3.0`.
- Binned reconstruction uses redshift bins with `Delta z = 0.6`.
- The high-redshift region is weakly constrained in the reported products.

## Available Products

- Tables: yes.
- Posterior samples: not found in the checked public sources.
- MCMC chains: not found in the checked public sources.
- Covariance matrices: not found in the checked public sources.
- Reconstructed histories: shown as figures; no public numerical history found.
- Figures: yes.

## Digitization Requirements

Figure digitization is optional if the goal is a qualitative timing audit.
Digitization is required if a future audit needs curve-level support from the
functional posterior figures.

## Public Code / Data Links

- arXiv page provides PDF and TeX source.
- No public posterior-product repository was found during the 2026-06-09 check.

## QFUDS Relevance

Reference role: primary phenomenological IV/IDE timing target for Exp006.

This record does not state that QFUDS or retained `Gamma(a)` is supported.

## Use Restrictions

- Use as a direct IV/IDE literature target.
- Do not treat broad table-level compatibility as preference.
- Do not infer posterior-level timing support without posterior samples,
  numerical histories, or documented digitization.

## Check History

- 2026-06-09: arXiv page, paper source, and Exp006 source notes checked for
  table products and public posterior products.
