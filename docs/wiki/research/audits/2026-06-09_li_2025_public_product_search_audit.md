---
doc_id: audit_2026_06_09_li_2025_public_product_search
title: "2026-06-09 Li 2025 Public Product Search Audit"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - lit_li_2025_desi_dr2_sign_reversal_ide
  - audit_2026_06_09_li_2025_timing_overlap_matrix_plan
next_gate: timing-overlap matrix is only partially executable from public products; author data or digitization protocol required
last_updated: 2026-06-09
record_type: availability_audit
audit_date: 2026-06-09
used_by:
  - li_2025_timing_overlap_matrix
---

# 2026-06-09 Li 2025 Public Product Search Audit

## Audit Objective

Determine whether usable public numerical products already exist for the Li and
Zhang 2025 timing-overlap matrix.

This is an availability audit only. It does not create a new experiment,
perform the timing-overlap analysis, change Exp006, change roadmap status, or
introduce a new physical hypothesis.

## Search Targets

Searched for:

- supplementary materials;
- public repositories;
- GitHub projects;
- Zenodo records;
- OSF records;
- Dataverse records;
- data archives;
- posterior products;
- covariance products;
- numerical `beta(z)` histories;
- PCA mode products;
- MCMC or nested-sampling chains;
- machine-readable reconstruction outputs.

## Sources Checked

| Source | Query or URL | Result |
| --- | --- | --- |
| arXiv abstract page | `https://arxiv.org/abs/2506.18477` | Paper metadata, HTML, PDF, and TeX source links found. |
| arXiv source package | `https://arxiv.org/e-print/2506.18477` | Source bundle found; contains LaTeX, bibliography, style files, and figure PDFs. |
| arXiv source contents | extracted source directory checked with `ls`: `00README.json`, `idenpr.tex`, `idenpr.bib`, `jcappub.sty`, `JHEP.bst`, and seven figure PDFs | No machine-readable `beta(z)` grid, covariance, posterior samples, chains, or PCA mode arrays found. |
| JCAP/IOP article page | DOI `10.1088/1475-7516/2025/12/018` | Article page reachable; no supplemental/data-product hook surfaced in checked HTML. |
| GitHub repository search | exact arXiv ID and exact title | No paper-specific repository found. |
| GitHub CLI repository search | exact arXiv ID, exact title, author/title variants | No paper-specific repository found. |
| GitHub CLI code search | exact arXiv ID, exact title, `fig_reconstruct.pdf`, `fig_pc.pdf beta(z)`, and `CMB+DESI DR2+DESY5 beta(z)` | Hits were absent or arXiv/RAG/citation mirrors only; no reconstruction grid, chain, covariance, or PCA product found. |
| GitHub repository search | `IDECAMB` | Public `liaocrane/IDECAMB` repository found; code infrastructure only. |
| GitHub code search | exact arXiv ID | Unauthenticated GitHub code search unavailable through API; web/domain search did not surface paper-specific code. |
| Zenodo API | exact arXiv ID and exact title | No matching records found. |
| Zenodo API | broad author/DESI and `beta(z)`/DESI DR2 searches | Returned unrelated DESI, same-name-author, or generic dark-energy records; no Li and Zhang 2025 reconstruction product found. |
| OSF API | exact arXiv ID and exact title | No matching files, projects, components, registrations, users, or institutions found. |
| Harvard Dataverse API | exact arXiv ID and exact title | No matching records found. |
| ResearchGate | exact title and arXiv ID pages | Paper/request-full-text pages surfaced; no public machine-readable data product found. |
| ORCID/J-GLOBAL/citation mirrors | exact title and arXiv ID pages | Bibliographic metadata surfaced; no data archive or supplementary product found. |
| General web search | exact title, arXiv ID, GitHub, Zenodo, OSF, data, supplementary, posterior, chains, covariance, author/title variants | Found arXiv, ResearchGate, ORCID/J-GLOBAL/mirror/citation pages; no machine-readable reconstruction product found. |

## Discovered Public Products

| Product | Contains | Timing-overlap use | Evidence level | Sufficient for qualitative comparison | Sufficient for uncertainty-aware comparison | Sufficient for PCA comparison | Sufficient for full classification |
| --- | --- | --- | --- | --- | --- | --- | --- |
| arXiv source bundle | Extracted source directory contains only `00README.json`, `idenpr.tex`, bibliography/style files, and figure PDFs including `fig_reconstruct.pdf`, `fig_pc.pdf`, `fig_evals.pdf`, and robustness figures. | Confirms figure-level products and can support a future digitization protocol. Does not provide numerical histories. | `paper_only_qualitative`; possible input to `digitized_uncertainty` only after a separate protocol | yes | no, not without digitization | no, not without digitizing PCA figures or obtaining arrays | no |
| IOP/JCAP article page | Published article page for DOI `10.1088/1475-7516/2025/12/018` | Confirms publication venue and article access. No checked supplemental file surfaced. | `paper_only_qualitative` | yes | no | no | no |
| `liaocrane/IDECAMB` GitHub repository | Public IDECAMB source code/patch infrastructure, README, CAMB/source files, parameter files, no releases | Could help reproduce a future model implementation if a full pipeline is specified. It is not a Li and Zhang 2025 output product. | code infrastructure only | no for Li timing matrix by itself | no | no | no |
| arXiv/RAG/citation mirrors in GitHub code search | Text copies of abstracts, citation lists, or arXiv feed metadata | Confirms bibliographic spread only. Does not contain reconstruction data. | bibliographic mirror only | no | no | no | no |

## Products Not Found

No public product was found for:

- numerical `beta(z)` mean histories;
- 68 or 95 percent numerical uncertainty bands;
- posterior samples;
- MCMC or PolyChord chains;
- binned `beta_i` covariance matrices;
- PCA eigenvectors or eigenvalue arrays;
- PCA coefficient chains;
- author-provided figure data tables;
- Zenodo, OSF, Dataverse, or GitHub paper-specific data archive.

This is a dated "not found" statement, not proof that the products do not
exist. The second-pass widened search checked exact identifiers, title strings,
author/title variants, figure filenames, archive mirrors, and repository/code
indexes; it still found no Li and Zhang 2025 machine-readable output product.

## Timing-Overlap Matrix Executability

Answer:

```text
partially
```

The timing-overlap matrix can be started only at the paper/source-product level:

- `paper_only_qualitative` rows can be populated from the article and arXiv
  source bundle;
- figure files can serve as inputs to a future digitization protocol;
- the source bundle confirms which figures would need extraction.

The matrix cannot yet be executed at the classification-relevant level because
the currently available public products do not provide numerical histories,
uncertainty arrays, covariance products, posterior samples, chains, or PCA mode
arrays.

Direct extraction of the arXiv source package confirmed this at the file-list
level: the bundle contains figure PDFs and manuscript source files, but no
data-like files such as `.csv`, `.txt`, `.dat`, `.npy`, `.npz`, `.fits`,
chain files, covariance files, or PCA array files.

## Product Use Classification

| Product class | Current availability | Use in matrix |
| --- | --- | --- |
| qualitative comparison | available | Use paper text, source figures, and figure captions to identify relevant regions only. |
| uncertainty-aware comparison | not directly available | Requires digitizing `fig_reconstruct.pdf` uncertainty bands or obtaining numerical histories. |
| PCA comparison | not directly available | Requires digitizing `fig_pc.pdf`/`fig_evals.pdf` or obtaining eigenvectors/eigenvalues/covariance products. |
| full classification | not available | Requires at least uncertainty-bearing digitization; preferably author numerical histories, covariance products, or posterior samples. |

## Recommendation

Do not create the experiment spec yet.

The next action should be one of:

1. request author-provided `beta(z)` histories, uncertainty bands, covariance
   products, PCA mode arrays, or chains;
2. prepare a figure-digitization protocol for `fig_reconstruct.pdf`,
   `fig_pc.pdf`, and `fig_evals.pdf`.

Public search alone did not find products sufficient to move beyond partial
execution.
