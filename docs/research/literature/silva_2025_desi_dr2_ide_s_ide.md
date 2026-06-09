---
doc_id: lit_silva_2025_desi_dr2_ide_s_ide
title: Silva 2025 DESI DR2 IDE and S-IDE
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

# Silva 2025 DESI DR2 IDE and S-IDE

## Bibliographic Metadata

- Paper: "New constraints on interacting dark energy from DESI DR2 BAO
  observations"
- Authors: Emanuelly Silva, Miguel A. Sabogal, Mateus Scherer, Rafael C.
  Nunes, Eleonora Di Valentino, Suresh Kumar
- arXiv: [2503.23225](https://arxiv.org/abs/2503.23225)
- DOI: [10.1103/qqc6-76z4](https://doi.org/10.1103/qqc6-76z4)
- Venue: Physical Review D

## Key Equations

- Constrains traditional IDE and sign-switching interacting dark energy
  (`S-IDE`) frameworks.
- Uses DESI DR2 BAO to update constraints on coupling parameters.

## Coupling Definitions

- Primary cache variable: coupling parameter in traditional IDE and `S-IDE`
  parameterizations.
- The paper is useful for sign-switching timing coverage, not for a fully
  nonparametric coupling history.

## Datasets Used

- DESI DR2 BAO over `0.295 <= z <= 2.330`.
- Supernova samples including PantheonPlus variants.
- Additional data combinations described in the paper.

## Redshift Coverage

- DESI DR2 BAO measurements cover `0.295 <= z <= 2.330`.
- The `S-IDE` framework provides sign-switching timing information through its
  transition behavior rather than through a freely reconstructed curve.

## Available Products

- Tables: yes.
- Posterior samples: not found in the checked public sources.
- MCMC chains: not found in the checked public sources.
- Covariance matrices: not found in the checked public sources.
- Reconstructed histories: not applicable; parameterized model constraints.
- Figures: yes.
- Public code: a modified CLASS IDE repository was surfaced by public code
  search.

## Digitization Requirements

Digitization is not required for the paper's table-level constraints. It would
not replace posterior samples for timing-support classification.

## Public Code / Data Links

- arXiv page provides PDF, HTML, and TeX source links.
- Public code search surfaced [msabogal/CLASS_IDE](https://github.com/msabogal/CLASS_IDE)
  as a modified CLASS implementation used with this paper family.

## QFUDS Relevance

Reference role: high-priority missing DESI-era sign-switching IDE coverage.

This record does not classify retained timing.

## Use Restrictions

- Use as sign-switching and DESI-era parameterized IDE coverage.
- Do not treat `S-IDE` as a nonparametric timing reconstruction.
- Do not change Exp006 without a separate experiment/result update.

## Check History

- 2026-06-09: arXiv page, article metadata, and public code search checked.
