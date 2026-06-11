# Research Asset Digitization Workflow

Use this workflow to convert a cached research asset under
`docs/wiki/research/assets/<key>/` into Markdown: structure outline, full text,
and figures.

This file is the operational procedure for *how* to digitize. The state ladder,
quality classifications, asset layout, and product-claim rules remain governed by
the [Research Asset and Product Workflow](research-asset-product-workflow.md)
(SSOT). When this file and the SSOT disagree, the SSOT wins.

Workflow index: [QFUDS Agent Workflows](README.md).

This workflow is process-only. It does not change roadmap status or turn a parse
into QFUDS evidence. The highest state it produces is `source_text_parse`. It
does not perform `manual_structured_extract` or `numeric_digitized`.

## Prerequisites: PageIndex MCP

Paper full-text and structure extraction require the PageIndex MCP server.

- Cowork: add the PageIndex connector in Settings (one click).
- Claude Code / Codex: register the same PageIndex API key in the MCP server
  config JSON.
- Never commit the API key. Keep it in environment variables or local MCP
  config only; ensure it is git-ignored.
- Tools used: `process_document`, `get_document_structure`, `get_page_content`,
  `browse_documents` (and `get_document_image` only for inspection — do not write
  base64 into files).

MarkItDown is required for non-paper (data-release) assets:
`pip install 'markitdown[all]' --break-system-packages`.

Poppler and ImageMagick are required for figures: `pdftocairo`, `pdftoppm`,
`pdfimages`, `convert`, `identify`.

## Phase 0: Orientation (read-only)

Read the SSOT and the target asset records before acting:
[research-asset-product-workflow.md](research-asset-product-workflow.md),
`docs/wiki/research/assets/README.md`, and the target asset's `README.md` and
`digitization/README.md`. Confirm the verification scripts exist:
`scripts/validate_docs.py` and `scripts/research_consistency.py`.

## Phase 1: Inventory and Triage

List each asset folder's `source/`, `source/extracted/`, `figures/extracted/`,
and `digitization/` contents. Classify the asset as:

- `paper-PDF` — a paper manuscript/body exists (PDF or arXiv source).
- `data-release` — only manifests, tables, figures, code, or notebooks exist; no
  manuscript body.

Pick the output route from the classification:

- `paper-PDF` -> PageIndex structure + full text (Phases 2-4).
- `data-release` -> MarkItDown conversion + table/figure inventory (Phase 5).

## Phase 2: Ingest and Structure (PageIndex)

Call `browse_documents` first to avoid re-uploading already-ingested documents.
Ingest any missing paper with `process_document` (arXiv PDF URL or the asset's
source URL). Pull the hierarchical outline with `get_document_structure` and
write it to `digitization/pageindex_structure.md`. Classify the parse as
`source_text_parse` (not numeric).

## Phase 3: Full-Text Extraction

Call `get_page_content` in page chunks (about 6-8 pages; responses over ~50KB are
persisted to a temp file, so prefer smaller inline chunks). Write
`digitization/paper_<id>.md` (or the existing source-named file) page by page
with `## Page N` markers, preserving LaTeX equations verbatim. This output
*replaces* any low-fidelity MarkItDown conversion of the same paper.

For large papers, build the file incrementally with a quoted bash heredoc
(`cat >> file <<'EOF' ... EOF`) so the growing file is not re-read and `$` and
backtick characters are not expanded.

Do not re-type large numerical tables. Reference them to the data-release
document where they are already cached as CSV-to-Markdown.

## Phase 4: Figure Handling

Authoritative mapping. Parse each `\begin{figure} ... \includegraphics{} ...
\caption{} ... \end{figure}` block in the arXiv `.tex` source to obtain the exact
figure-number-to-file mapping. Do not guess from captions. If the `.tex` is a
draft superset, reconcile against the figures that actually appear in the
compiled PDF (via PageIndex page content).

Coverage audit. For each asset compare the count of source figure PDFs, the count
of PNG mirrors under `figures/extracted/`, and the count of figures referenced in
the Markdown. Every paper figure should be referenced.

High resolution. Re-render vector figure PDFs at high resolution, overwriting any
low-resolution PNG:

```text
pdftocairo -png -singlefile -scale-to 2000 <fig>.pdf <fig>
```

Keep author-provided native PNGs as-is (do not upscale). If a paper has no
separate figure files (for example a scanned book chapter), extract embedded
raster figures with `pdfimages -png`, and capture vector figures by rendering the
page at high DPI and cropping:

```text
pdftoppm -r 600 -png <page> in.pdf /tmp/pg
convert /tmp/pg-<page>.png -crop WxH+X+Y +repage -trim out.png
```

Write Markdown image links with the relative path `../figures/extracted/...` and
include the figure caption.

## Phase 5: Non-Paper Assets (MarkItDown)

Unpack archives, then convert text/HTML/JSON/notebook/CSV sources to Markdown with
`markitdown`. Assemble a data-release document containing: the release notes, the
numerical tables (CSV-to-Markdown), and a figure inventory with working image
links. Render any vector figure PDFs to PNG as in Phase 4.

## Phase 6: Manifests

Create or update `digitization/README.md` (index) with a record line per output.
Add a one-line pointer in the asset root `README.md` to the new document. Write
references to other `.md` files as Markdown links, not as backticked paths, so the
link-hygiene check does not flag them.

State recording. The conversion is `source_text_parse`. The asset state stays
`asset_extracted_not_digitized` unless real numeric digitization (units,
provenance, uncertainty) is performed.

## Phase 7: Verification (required)

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
git diff --check
```

Also confirm: every Markdown image link resolves, referenced figures are not
low-resolution (target >= 700px wide), no broken `.md` cross-links, and no stray
or temp files remain.

## Cross-Cutting Rules

- Naming: name the product, e.g. `pageindex_structure.md`,
  `paper_<arxivid>.md`, `gwtc<n>_population_release.md`, `zenodo_record.md`.
- Mount constraints: bash `rm` and `chmod` are blocked on the mount. Use the
  cowork file-delete tool (after approval) to remove stray files. File mode `600`
  does not block rendering because the files are owned by the user.
- Quality ladder: `low_fidelity_search_text` (default MarkItDown) <
  `source_text_parse` (PageIndex or verified conversion) <
  `manual_structured_extract` < `numeric_digitized`. This workflow promotes only
  to `source_text_parse`.
- Do not claim "no product", "missing", or "not extractable" until the PDF,
  arXiv source/HTML, supplement, archive, figure/table, and code checks have
  actually been run, per the SSOT.
