---
doc_id: asset_lineweaver_entropy_budget_chapter
title: "Lineweaver Entropy Budget Chapter Asset"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - audit_2026_06_10_black_hole_data_product_audit
next_gate: inspect Markdown conversion and extract table values before using the entropy inventory numerically
last_updated: 2026-06-11
---

# Lineweaver Entropy Budget Chapter Asset

Local access copy for the Lineweaver entropy-budget chapter PDF.

Source URL: <https://www.mso.anu.edu.au/~charley/papers/Chapter22Lineweaver.pdf>

## Asset Manifest

```text
source/chapter22_lineweaver.pdf
digitization/chapter22_lineweaver.md
```

Asset type: PDF chapter, MarkItDown Markdown conversion.

Current asset state: `asset_extracted_not_digitized`; PDF converted to
Markdown, but table values not extracted into a numerical product.

Extraction potential: `direct_table`, `figure_digitization_possible`.

## Why This Asset Matters

The chapter provides a present-day entropy-budget table useful as a Lane B
inventory comparator.

This asset is not QFUDS evidence and does not define a redshift-dependent
`S_BH(a)`, `dS_BH/dln(a)`, entropy-to-energy conversion law, or `Q^nu`.

## Dependent Audit

[2026-06-10 Black-Hole Data Product Audit](../../../governance/source_x/conclusions/040_black_hole_data_product_audit.md)
depends on this asset cache before treating the entropy inventory as only a
prose citation.

## Known Limitations

The PDF now has a MarkItDown Markdown conversion for text inspection, plus a
PageIndex hierarchical structure parse (`source_text_parse`,
[pageindex_structure.md](digitization/pageindex_structure.md)) that locates the
22.1.2 entropy-budget table on p3-4. Neither is numerical digitization; table
values, units, and
normalization text still need explicit extraction before this asset can be used
numerically.

The MarkItDown conversion has no local figure references because this cache does
not include extracted chapter figure files.
