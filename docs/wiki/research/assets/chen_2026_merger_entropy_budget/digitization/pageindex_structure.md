---
doc_id: asset_chen_2026_merger_entropy_budget_pageindex_structure
title: "Chen et al. 2026 — PageIndex Structure"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_chen_2026_merger_entropy_budget_digitization_index
next_gate: targeted manual extraction before entropy-history classification
last_updated: 2026-06-17
---

# Chen et al. 2026 — PageIndex Structure

Source paper: arXiv:2601.13621 (BBH merger contribution to the cosmological entropy budget)
[PageIndex](https://github.com/VectifyAI/PageIndex) doc_name: `2601.13621v1.pdf` (15 pages)
Parse quality: `source_text_parse` ([PageIndex](https://github.com/VectifyAI/PageIndex) hierarchical TOC tree + node summaries)
Generated: 2026-06-11 via [PageIndex](https://github.com/VectifyAI/PageIndex) MCP `get_document_structure`.

Derived inspection product. Node summaries are [PageIndex](https://github.com/VectifyAI/PageIndex)-generated; not numerical
digitization or equation provenance. Use page ranges to target `get_page_content`.

## Hierarchical Outline (node_id · pages)

- 0000 · Introduction · p1–2
  - Updates the cosmological entropy budget with GW observations of BH mergers in
    the 5–300 M☉ range; Bekenstein–Hawking entropy; claims merger entropy can
    exceed CMB entropy at z~12; notes PBH thermodynamic impact.
- 0001 · Methods · p2
  - PISN mass gap; Bekenstein–Hawking formula; Salpeter IMF for progenitor number
    densities across mass regimes.
  - 0002 · Entropy for Stellar Black Holes · p2–3 (SEVN evolution code).
  - 0003 · Entropy for Merging Binary Black Holes · p3–4 (LVK data + numerical
    relativity; Monte Carlo; redshift-dependent merger rates; entropy density).
  - 0004 · Entropy Budget for Primordial Black Holes · p4–5 (Power-Law+Peak model;
    NR surrogate fits; updated comparative entropy-budget table).
  - 0005 · Cosmological Density Parameters · p5–6 (PBH log-normal mass dist;
    density parameters Ω for initial mass, GW energy, post-merger remnants).
- 0006 · Results · p6
  - 0007 · Entropy Budget for Stellar Black Holes · p6–7 (PISN-gap remnants
    dominate; entropy ∝ mass²; no significant z-correlation in per-merger entropy).
  - 0008 · Entropy Budget for Merging Black Holes · p7–9 (peak at z≈4.55;
    thermodynamic crossover at z≈12.6 where merger entropy surpasses CMB).
- 0009 · Cosmological Implications · p9
  - 0010 · The Thermodynamic Crossover at Cosmic Dawn · p9
  - 0011 · Constraints from the Dark Ages: The PBH Floor · p9–10
  - 0012 · Cosmological Density Parameters & Thermodynamic Asymmetry · p10–11
    (mergers energetically inefficient but entropically dominant).
  - 0013 · Volume-normalized Retrospective Entropy Density · p11–12 (peak z≈4.33;
    crossover z≈0.55 vs relic radiation).
- 0014 · Conclusion · p12
- 0015 · Acknowledgement + references · p12–15 (Hawking area theorem applied to
  GWTC-4 data).

## Targeted-extraction pointers

- Updated entropy-budget comparative table: node 0004 (p4–5) and node 0008 (p7–9).
- Density parameters Ω (mass, GW energy, remnants): nodes 0005, 0007, 0012.
- Crossover redshifts (z≈12.6, z≈4.55, z≈4.33, z≈0.55): nodes 0008, 0013.
