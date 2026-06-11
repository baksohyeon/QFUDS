# Research Asset and Product Workflow

Use this workflow whenever research work touches an external paper, PDF, arXiv
source bundle, supplementary material, Zenodo/OSF/Dataverse/GitHub asset, figure
PDF, table, code repository, or downloadable archive.

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
| `asset_extracted_not_digitized` | Source, figures, tables, or archive contents were extracted, but numerical digitization or Markdown conversion is not done. |
| `asset_digitized` | Figure/table values were digitized, but may not yet be classified against the research criterion. |
| `asset_cached` | Raw asset and manifest README are stored in the repo. |
| `inspected_no_numerical_product` | Contents were inspected and no machine-readable numerical product was found. |
| `no_asset_found` | PDF/source/supplement/archive/figure/table/code/raw asset checks were run and no relevant asset was found. |
| `inaccessible` | A source appears to exist but access failed or requires unavailable credentials. |

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

Record the source URL, asset type, state, and extraction potential before making
any literature-coverage or data-product claim.

## Step 2: Place Assets Inside The Repository

Use this path pattern:

```text
docs/wiki/research/assets/<topic>/<paper_key>/source/
```

Examples:

```text
docs/wiki/research/assets/black_holes/farrah_2023/source/
docs/wiki/research/assets/entropy/chen_2026/source/
```

If the asset is downloaded, store the original raw asset under `source/`. If it
is extracted, keep extracted files under a clearly named child directory such as
`source/extracted/`.

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

If source/figures/tables are extracted, record
`asset_extracted_not_digitized` until figure/table digitization or Markdown
conversion exists.

Only say `no_asset_found` after the PDF, arXiv HTML/source, supplement,
archive, figure/table, code, and raw-asset checks were actually run.

Only say a QFUDS-ready product was not found after distinguishing raw assets,
extractable products, numerical products, and QFUDS-specific requirements.

## Step 5: Request Markdown Conversion When Text Extraction Is Required

If text extraction is required, do not perform silent extraction and continue.

Instead, create a task request for the user with this exact structure:

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
