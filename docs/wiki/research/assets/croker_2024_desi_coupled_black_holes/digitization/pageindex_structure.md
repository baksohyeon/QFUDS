---
doc_id: asset_croker_2024_desi_coupled_black_holes_pageindex_structure
title: "Croker et al. 2024 — PageIndex Structure"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_croker_2024_desi_coupled_black_holes_digitization_index
next_gate: targeted manual extraction before numerical reuse
last_updated: 2026-06-17
---

# Croker et al. 2024 — PageIndex Structure

Source paper: arXiv:2405.12282 (DESI test of dark energy from cosmologically coupled black holes)
[PageIndex](https://github.com/VectifyAI/PageIndex) doc_name: `2405.12282v3.pdf` (20 pages)
Parse quality: `source_text_parse` ([PageIndex](https://github.com/VectifyAI/PageIndex) hierarchical TOC tree + node summaries)
Generated: 2026-06-11 via [PageIndex](https://github.com/VectifyAI/PageIndex) MCP `get_document_structure`.

Derived inspection product. Node summaries are [PageIndex](https://github.com/VectifyAI/PageIndex)-generated; not numerical
digitization or equation provenance. Use page ranges to target `get_page_content`.

## Hierarchical Outline (node_id · pages)

- 0000 · Introduction · p2–5
  - Limitations of w0wa parameterization vs DESI; proposes DE sourced by
    cosmologically coupled black holes (CCBH) formed via stellar collapse that
    convert baryons into DE; links baryon depletion to cosmic SFR.
- 0001 · Theory · p5–6
  - Differential equations for evolution of dark energy, baryon density, and
    expansion; SFRD profiles; collapse-fraction parameter.
- 0002 · Methods · p6–10
  - Governing CCBH expansion ODEs; SFRD models; Bayesian pipeline for collapse
    fraction (Ξ) and baryon density; ~30% baryon conversion; 1.9σ Planck–DESI
    tension that CCBH may reconcile.
- 0003 · Results · p10–11
  - Dynamic nested sampling; CCBH viable vs flat ΛCDM; reconciles early (Planck)
    and late (DESI/SH0ES) tensions; links to missing-baryons problem.
- 0004 · Discussion · p11
  - Higher H0 reduces SH0ES tension; baryon-to-DE conversion; neutrino-mass and
    reionization implications.
  - 0005 · CCBH: Reconciling Dark Energy and Baryon Evolution · p11–14
    (reproduces DESI BAO without early-universe modifications; ~30% present-day
    baryon deficit).
  - 0006 · Bibliography (dark sector, BH physics, surveys) · p14–17
  - 0007 · Bibliography (cosmological models, surveys, astrophysics) · p17–20

## Targeted-extraction pointers

- Governing ODEs (DE, baryon, expansion): nodes 0001–0002 (p5–10).
- Collapse fraction Ξ, baryon conversion %, posteriors: node 0002 (p6–10).
- H0 / tension reconciliation numbers: nodes 0003–0004 (p10–11).
- Best-fit-vs-data and corner plots (figures): see source/extracted figure PDFs.
