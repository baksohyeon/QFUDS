# Research Asset and Product Workflow

Use this workflow whenever research work touches an external paper, PDF, arXiv
source bundle, supplementary material, Zenodo/OSF/Dataverse/GitHub asset, figure
PDF, table, code repository, downloadable archive, stable reference website,
or templated/page-family web resource.

This file is the SSOT for literature product recovery and PDF/source/archive
asset handling. It is process-only: it does not change roadmap status, does not
open Level 2B, and does not turn an asset or literature overlap into QFUDS
support.

Reference incident:
[Li & Zhang 2025 data-cache postmortem](../../docs/wiki/postmortem/001-20260609-dorito-li-2025-data-cache.md).

Workflow index: [QFUDS Agent Workflows](README.md).

## Core Rule

Never stop at:

- "PDF exists"
- "source exists"
- "asset exists"
- "no product found"
- "literature checked"

Never keep critical assets only in:

- temporary paths
- local scratch paths
- agent-only working directories

Do not say a product is missing, unavailable, unusable, not found, or not
extractable until this workflow has been applied.

## State Ladder

Use the most specific state that the evidence supports:

| State | Meaning |
| --- | --- |
| `not searched` | No source/product search was attempted. |
| `searched_no_hit` | Search ran and no candidate source was found. |
| `hit_not_cached` | A source was found but no local cache record or asset exists. |
| `asset_available_not_downloaded` | The source exposes an asset, but it has not been retrieved. |
| `asset_downloaded_not_extracted` | The asset is in the repo, but has not been unpacked, parsed, rendered, or inspected. |
| `asset_extracted_not_digitized` | Source, figures, tables, archive contents, or Markdown conversions exist, but numerical digitization or product classification is not done. |
| `asset_digitized` | Figure/table values were digitized, but may not yet be classified against the research criterion. |
| `asset_cached` | Raw asset and manifest README are stored in the repo. |
| `inspected_no_numerical_product` | Contents were inspected and no machine-readable numerical product was found. |
| `no_asset_found` | PDF/source/supplement/archive/figure/table/code/raw asset checks were run and no relevant asset was found. |
| `inaccessible` | A source appears to exist but access failed or requires unavailable credentials. |

Markdown conversion quality must be recorded separately from asset state:

| Quality | Meaning |
| --- | --- |
| `low_fidelity_search_text` | Automated PDF-to-Markdown conversion useful only for rough keyword, section, and citation search. Do not use it as a numerical source. |
| `source_text_parse` | TeX, HTML, XML, or publisher text is parseable enough to inspect equations, captions, and tables against the source. |
| `manual_structured_extract` | A human or agent has curated exact equations, table values, figure values, or section excerpts into a structured file with source locations. |
| `numeric_digitized` | Numerical values have been digitized or extracted with method, units, uncertainty handling, and provenance recorded. |

Allowed extraction-potential classifications:

- `direct_table`
- `figure_digitization_possible`
- `source_tex_parse_possible`
- `zenodo_data_available`
- `code_reproduction_possible`
- `not_extractable`

## Step 1: Record Asset Availability

For every external hit, record whether the source exposes:

- PDF
- arXiv HTML
- arXiv source tar or TeX source
- supplementary material
- Zenodo, OSF, Dataverse, GitHub, or other archive asset
- figure data or figure PDF
- table data
- code repository
- downloadable raw assets
- HTML page families reachable from navigation menus, sitemap-like link lists,
  or templated URL patterns such as `{parameter}.html`
- linked figure/vector products such as PNG, JPG, PDF, SVG, and EPS files

Record the source URL, asset type, state, and extraction potential before making
any literature-coverage or data-product claim.

If the user supplies a URL pattern, a screenshot of a navigation menu, or a page
whose links imply sibling resources, do not cache only the pasted URL. Resolve
the local navigation first, list the inferred page family, and cache the linked
source pages and page-level figure/table products that are in scope. Record the
crawl scope and any skipped off-site links in the asset README or inventory.

## Step 2: Place Assets Inside The Repository

Use the repository asset-cache layout below. Do not invent new top-level asset
categories without first updating this workflow.

The cache index at
[docs/wiki/research/README.md](../../docs/wiki/research/README.md) describes
the current stored records, but this workflow is the operational SSOT for where
agents place assets.

Repository wiki folder roles are:

- `docs/wiki/governance/`: admission rules, branch gates, consistency checks,
  and missing-physics maps for the repository itself.
- `docs/wiki/lineage/`: idea genealogy and branch dependency provenance.
- `docs/wiki/research/`: external literature records, investigations, cached
  assets, and source/product recovery work.

External papers, PDFs, arXiv source bundles, Zenodo records, figures, tables,
code repositories, and raw assets belong under `docs/wiki/research/`, not under
`governance/` or `lineage/`.

Required asset layout:

```text
docs/wiki/research/assets/
  <paper_or_release_key>/
    source/
    figures/
    digitization/
```

Use these path patterns:

```text
docs/wiki/research/assets/<paper_or_release_key>/source/
docs/wiki/research/assets/<paper_or_release_key>/figures/
docs/wiki/research/assets/<paper_or_release_key>/digitization/
```

Create all three standard child directories for every asset folder. If a
standard directory is empty, add `.gitkeep` so the layout is visible to future
agents and git status does not hide the intended destination.

Examples:

```text
docs/wiki/research/assets/farrah_2023_cosmological_coupling_black_holes/source/
docs/wiki/research/assets/chen_2026_merger_entropy_budget/source/
docs/wiki/research/assets/chen_2026_merger_entropy_budget/digitization/
docs/wiki/research/assets/li_2025_desi_dr2_sign_reversal_ide/
docs/wiki/research/assets/li_2025_desi_dr2_sign_reversal_ide/digitization/
```

If the asset is downloaded, store the original raw asset under `source/`. If it
is extracted, keep extracted files under a clearly named child directory such as
`source/extracted/`.

Use `source/` for external originals and raw products: PDFs, arXiv source
bundles, supplementary archives, Zenodo records or datasets, GitHub metadata
snapshots, code-release manifests, cached HTML pages, and downloadable raw
assets. Use `figures/` inside the same asset directory for figure-level
downloaded, extracted, or rendered assets. Use `digitization/` inside the same
asset directory only for derived conversion or digitization outputs such as
Markdown conversions, link inventories, extracted table drafts, and digitized
CSV/JSON files. Rendered PNG mirrors of figures belong under `figures/`, not
`digitization/`.

Do not create top-level category or audit-chain folders under `assets/`, such as
`assets/figures/`, `assets/digitization/`, `assets/source_x/`, or
`assets/exp006_timing/`. The first child of `assets/` must be a paper or release
key.

The Li and Zhang 2025 cache is the local example of a paper-level asset folder:
[Li 2025 assets](../../docs/wiki/research/assets/li_2025_desi_dr2_sign_reversal_ide/README.md)
and its digitization manifest:
[Li 2025 digitization assets](../../docs/wiki/research/assets/li_2025_desi_dr2_sign_reversal_ide/digitization/README.md).

## Step 3: Create Asset README

Create `README.md` in the asset directory.

The README must contain:

- paper title
- authors
- year
- source URL
- asset type
- why the asset matters
- which audit depends on it
- current asset state
- extraction potential
- known extraction failures or blocked steps
- for web page families, the crawl scope, inferred URL pattern, linked-asset
  inventory path, and any distinction between source-reference tables and
  numerical digitization

The README is the manifest. Do not rely on chat history, temp paths, or an
agent's memory as the only record of the asset.

## Step 4: Inspect Before Claiming Absence

Inspection may include:

- archive manifest
- extracted tree
- file types
- TeX/source text search
- PDF metadata and attachment/URI search
- figure render
- table extraction
- README or data-release manifest review
- code repository README and release inspection
- notebook/script presence check

If assets are visible but not retrieved, record
`asset_available_not_downloaded` and create a product-recovery follow-up.

If assets are downloaded but not unpacked or parsed, record
`asset_downloaded_not_extracted`.

If source, figures, tables, or Markdown conversions are extracted, record
`asset_extracted_not_digitized` until figure/table digitization or numerical
product classification exists.

Only say `no_asset_found` after the PDF, arXiv HTML/source, supplement,
archive, figure/table, code, and raw-asset checks were actually run.

Only say a QFUDS-ready product was not found after distinguishing raw assets,
extractable products, numerical products, and QFUDS-specific requirements.

## Step 5: Convert Or Request Markdown When Text Extraction Is Required

If text extraction is required, first try to create a repository-local Markdown
conversion when a safe converter is available. Preferred command:

```text
uvx --from 'markitdown[all]' markitdown <input.pdf> > <asset_dir>/digitization/<output>.md
```

Record the command or tool, the input PDF, the output Markdown path, conversion
quality, and any conversion warnings in the asset README, digitization README, or
dependent audit. A Markdown conversion is still only a derived inspection asset;
it is not numerical digitization and is not QFUDS-ready evidence.

Default [MarkItDown](https://github.com/microsoft/markitdown) PDF conversions must be treated as
`low_fidelity_search_text` unless manually checked against the source. This is
especially important for two-column papers, equations, tables, captions, and
figures. Broken line order, spurious Markdown tables, merged words, missing
minus signs, and lost equation structure are expected failure modes.

Do not ask the user to manually extract an entire paper by default. Ask for
targeted manual extraction only when a specific audit needs exact equations,
tables, figure values, captions, or source sections. Store the curated output in
the same `digitization/` directory with a filename that names the extracted
product, for example `table_1_entropy_budget.csv`,
`figure_1_beta_history_points.csv`, or `equation_source_terms.md`.

After Markdown conversion, check image references:

- If the Markdown contains `![...](...)` links, every target must resolve
  relative to the Markdown file unless the link is an intentional external URL.
- If the converter emits no image links, record that explicitly. Do not imply
  the figures were embedded.
- Preserve original figure files in their upstream/extracted layout under the
  same asset directory, usually `source/extracted/`.
- Store rendered PNG mirrors and copied figure files under `figures/`, usually
  `figures/extracted/`. Do not store figure mirrors under `digitization/`.

If conversion fails, the output is unusable, or the environment cannot run the
converter, do not perform silent extraction and continue.

Instead, either perform targeted manual extraction yourself from the repository
source assets, or create a task request for the user with this exact structure:

```text
Markdown conversion required.

Input asset:
<repo path>

Recommended output:
<repo path>

Reason:
<why the audit needs it>

Needed sections:
<figures/tables/text>

Blocked audit:
<which audit is waiting for it>
```

If agent PDF parsing fails, record the failure explicitly. Do not hide the
failure behind a weaker phrase such as "no data found" or "literature checked".

## Step 6: Promote Only After Evidence Exists

Only after the needed asset is cached, extracted, digitized, converted to
Markdown, or otherwise inspected may the paper be promoted into the matching
evidence state.

Before Markdown conversion, do not classify an unread PDF as `literature fully
checked`.

Before digitization, do not classify a figure-level asset as a numerical
product.

Before code execution or manifest inspection, do not classify a code repository
or archive as reproducible evidence.

## Required Wording

Use:

- "asset exists, not downloaded"
- "asset exists, not extracted"
- "figure-level product exists"
- "QFUDS-ready product not found"
- "not extractable from checked assets"

Do not use:

- "no product" when a PDF, source bundle, figure, table, archive, Zenodo record,
  or code repository exists.
- "recorded gap only" for a downloadable asset.
- "supports QFUDS" for an availability or overlap finding.

## Forbidden

Never:

- treat PDF existence as evidence extraction
- treat unread PDF as a literature miss
- store critical assets only in temporary locations
- hide extraction failures
- claim coverage completeness while assets remain unprocessed
- present an availability finding as QFUDS support

## Verification

After documentation changes, run:

```bash
rtk python3 scripts/validate_docs.py
rtk python3 scripts/research_consistency.py
rtk git diff --check
```
