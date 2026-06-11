---
doc_id: asset_chen_2026_merger_entropy_budget_digitization_index
title: Chen 2026 Digitization Assets
doc_type: index
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_chen_2026_merger_entropy_budget
next_gate: targeted manual extraction before entropy-history classification
last_updated: 2026-06-11
---

# Chen 2026 Digitization Assets

This folder stores derived inspection products for the Chen, Jani, and Kephart
2026 asset.

The full-text Markdown was regenerated via PageIndex MCP (`source_text_parse`),
replacing the earlier low-fidelity MarkItDown pass. It is a faithful page-by-page
text and LaTeX-equation transcription (including the updated entropy budget
Table 1 and Eqs. 1–16) with figure image links wired to the repo PNG mirrors
under `../figures/extracted/`. It is machine-extracted and not line-for-line
verified (a few Table 1 exponents are flagged in-file as needing a source check),
so it must not be treated as numerical digitization or audited equation provenance.

For entropy-history work, manually extract only the needed equations, tables,
captions, or figure values from the source PDF, TeX, figures, or rendered figure
PNGs, then store the curated output here.

## Records

- [PageIndex full-text extraction](paper_arxiv_2601.13621.md) - faithful
  page-by-page text + LaTeX transcription via PageIndex MCP (`source_text_parse`),
  with working figure image links. Supersedes the prior MarkItDown conversion. - `low_fidelity_search_text`.
- [PageIndex structure](pageindex_structure.md) - hierarchical TOC tree with
  per-node page ranges and summaries, generated via PageIndex MCP
  (`source_text_parse`). Inspection aid for section targeting; not numeric.
- [Merger entropy history recovery extract](chen_2026_merger_entropy_history_recovery_extract.md) -
  manual structured extraction for the retained Source-X Lane B target. It is a
  source-history candidate record, not QFUDS support.
- [Chen Figure 5 numeric digitization CSV](chen_figure5_numeric_digitization.csv) -
  `numeric_digitized` source-history candidate for the Figure 5 blue entropy
  and red entropy-density curves.
- [Chen Figure 5 numeric digitization provenance](chen_figure5_numeric_digitization_provenance.md) -
  calibration, method, landmark checks, missing fields, and status boundary for
  the CSV.
