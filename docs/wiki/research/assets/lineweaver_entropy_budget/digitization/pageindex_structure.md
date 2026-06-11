---
doc_id: asset_lineweaver_entropy_budget_pageindex_structure
title: "Lineweaver — Entropy Budget Chapter — PageIndex Structure"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_lineweaver_entropy_budget_digitization_index
next_gate: targeted manual table extraction before numerical reuse
last_updated: 2026-06-11
---

# Lineweaver — Entropy Budget Chapter — PageIndex Structure

Source: "The Entropy of the Universe and the Maximum Entropy Production Principle"
(Chapter 22, Lineweaver). Source URL:
<https://www.mso.anu.edu.au/~charley/papers/Chapter22Lineweaver.pdf>
PageIndex doc_name: `Chapter22Lineweaver.pdf` (13 pages)
Parse quality: `source_text_parse` (PageIndex hierarchical TOC tree + node summaries)
Generated: 2026-06-11 via PageIndex MCP `get_document_structure`.

Derived inspection product. Node summaries are PageIndex-generated; not numerical
digitization or equation provenance. Use page ranges to target `get_page_content`.

## Hierarchical Outline (node_id · pages)

- 0000 · 22 The Entropy of the Universe and the Maximum Entropy Production Principle · p1
  - 0001 · Abstract · p1
  - 0002 · 22.1 The Entropy of the Observable Universe · p1–3
    - 0003 · 22.1.1 Expansion of the Universe is Isentropic · p3
    - 0004 · 22.1.2 The Entropy Budget of the Universe · p3–4
      (SMBHs are dominant entropy source, then CMB photons, then neutrinos).
  - 0005 · 22.2 The Entropy Gap and the Initial Entropy of the Universe · p4–7
    - 0006 · 22.2.1 Anthropic Reasoning Cannot Rescue Penrose's Model · p7–9
  - 0007 · 22.3 Maximum Entropy Production Principle in Cosmology · p9
    - 0008 · 22.3.1 Entropy Production Around Supermassive Blackholes · p9–12
  - 0009 · References · p12–13

## Targeted-extraction pointers

- Present-day entropy-budget inventory table (the Lane B comparator): node 0004
  (22.1.2, p3–4). This is the table whose values still require manual numeric
  extraction (units + normalization) before numerical reuse.
- Entropy gap discussion: node 0005 (p4–7).
- Note: this cache has no extracted figure files; PageIndex parse is text-tree only.
