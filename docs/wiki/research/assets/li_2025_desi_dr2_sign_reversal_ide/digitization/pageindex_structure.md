---
doc_id: asset_li_2025_desi_dr2_sign_reversal_ide_pageindex_structure
title: "Li & Zhang 2025 — PageIndex Structure"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_li_2025_desi_dr2_sign_reversal_ide_digitization_index
next_gate: targeted manual extraction before numerical reuse
last_updated: 2026-06-17
---

# Li & Zhang 2025 — PageIndex Structure

Source paper: arXiv:2506.18477v2 (DESI DR2 non-parametric sign-reversal IDE reconstruction)
[PageIndex](https://github.com/VectifyAI/PageIndex) doc_name: `paper_arxiv_2506.18477v2.pdf` (20 pages; ingested 2026-06-09)
Parse quality: `source_text_parse` ([PageIndex](https://github.com/VectifyAI/PageIndex) hierarchical TOC tree + node summaries)
Generated: 2026-06-11 via [PageIndex](https://github.com/VectifyAI/PageIndex) MCP `get_document_structure`.

Derived inspection product. Node summaries are [PageIndex](https://github.com/VectifyAI/PageIndex)-generated; not numerical
digitization or equation provenance. Use page ranges to target `get_page_content`.
Figure PDFs (fig_reconstruct, fig_pc, fig_evals, fig_bin30, fig_zmax,
fig_mock_lcdm, fig_bayes_data) are individually ingested in [PageIndex](https://github.com/VectifyAI/PageIndex) and mirrored
under `figures/extracted/`.

## Hierarchical Outline (node_id · pages)

- 0000 · Introduction · p2–3
  - Motivates Interacting Dark Energy (IDE) vs ΛCDM under H0 tension and DESI
    dynamical-DE preference; proposes model-independent non-parametric
    reconstruction of vacuum–CDM coupling.
- 0001 · The model · p3–5
  - Background equations; degeneracy between dynamical DE and IDE; extended
    parameterized post-Friedmann (ePPF) perturbations; Bayesian Gaussian-smoothness
    prior on β(a).
- 0002 · The reconstruction method · p5–6
  - Gaussian prior + CPZ correlation function; "floating" average; synthetic-data
    validation; Cobaya, PolyChord, IDECAMB; CMB + BAO datasets and priors.
- 0003 · Data and results · p6–10
  - Sign change in β(z) over time; no H0 resolution but moderate S8 alleviation;
    Δχ²_MAP and Bayesian evidence prefer IDE over ΛCDM; PCA → three data-constrained
    degrees of freedom.
- 0004 · Conclusion · p10–12
  - β(z) fits better than ΛCDM; sign-reversal in energy transfer; degenerate with
    CPL in expansion but differs in S8 growth.
- 0005 · Appendix: Validation with Synthetic Data · p12–13
- 0006 · Appendix: Robustness of the Reconstruction · p13–20
  - Null-signal recovery from ΛCDM mocks; robustness to binning/redshift; 118-ref
    bibliography.

## Targeted-extraction pointers

- β(z) reconstruction (sign-reversal): node 0003 (p6–10); figure fig_reconstruct.
- PCA / three DOF: node 0003; figures fig_pc (eigenvectors), fig_evals (inverse eigenvalues).
- Bayes factor / Δχ²: node 0003; figure fig_bayes_data.
- Robustness (30-bin, extended-z, mock-ΛCDM): node 0006; figures fig_bin30, fig_zmax, fig_mock_lcdm.
