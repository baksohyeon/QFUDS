---
doc_id: asset_nasa_lambda_graphic_history
title: NASA LAMBDA Graphic History Assets
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - research_cache_index
next_gate: numeric plot digitization only if an audit needs source values from the history plots
last_updated: 2026-06-17
---

# NASA LAMBDA Graphic History Assets

Local cache for the NASA LAMBDA "Graphic History to Cosmology" page family.

This is a foundational reference cache for standard cosmological-parameter
context, historical measurement provenance, and baseline LambdaCDM comparison
language. It is not QFUDS evidence, does not change roadmap status, and does not
open Level 2B.

## Source

- Landing page:
  <https://lambda.gsfc.nasa.gov/resources/graphic_history/index.html>
- User-visible parameter page pattern:
  `https://lambda.gsfc.nasa.gov/resources/graphic_history/{page}.html`
- Cached crawl date: 2026-06-17.
- Source owner shown in HTML metadata: NASA GSFC LAMBDA.
- Content attribution in pages: NASA / LAMBDA Archive Team.

## Cached Page Family

The crawl followed the tertiary navigation menu exposed by
`parameters.html`, including non-obvious filenames such as `galaxiQ.html`,
`scalarI.html`, `taureionzation.html`, `matterd.html`, `fluctsize.html`,
`hubb_const.html`, and `more_ref.html`.

Cached HTML pages:

- `source/html/page_list.txt` - 20 cached page stems.
- `source/html/*.html` - raw local HTML copies for the full Graphic History
  menu family.

## Files

- `source/html/` - raw HTML pages.
- `figures/graphic_history_images/` - 88 linked Graphic History figure,
  vector, and PDF assets.
- `figures/lambda_graphics_images/` - 2 linked LAMBDA graphics assets referenced
  from the power-spectrum page.
- [Link inventory](digitization/link_inventory.tsv) - source page, raw link,
  resolved URL, local path, and download status for every linked figure/vector
  asset found in the cached HTML.
- [Download queue](digitization/download_queue.tsv) - unique URL to local-path
  map used for this crawl.
- [Data reference matrix](digitization/data_reference_matrix.csv) - source
  extraction of the LAMBDA `data_ref.html` table.

## Current Asset State

- Asset state: `asset_cached`.
- Derived product state: `manual_structured_extract` for the data-reference
  matrix only.
- Extraction potential: `direct_table`, `figure_digitization_possible`.
- Markdown conversion quality: not applicable; source HTML was cached directly.

All 90 linked figure/vector URLs discovered in the cached page family were
downloaded. The source does not expose an obvious machine-readable CSV of the
plotted numerical parameter histories. The plots are available as PNG/PDF/SVG
and, for several parameter plots, EPS.

## Recovered Quantities

The `data_ref.html` table was extracted into
`digitization/data_reference_matrix.csv`. It maps 57 labeled literature/data
sources to parameter-history plots:

- `n_s`
- `t0`
- `tau`
- `H0`
- `Omega_m`
- `Omega_b h^2`
- `Omega_c h^2`
- `sigma8`

This matrix records which cited source contributes to which plotted parameter.
It does not contain the plotted numerical values themselves.

## Known Limits

- Figure/vector files are cached, but plot-point digitization has not been
  performed.
- The data-reference matrix is provenance metadata, not a numerical likelihood,
  posterior product, or cosmological-parameter table.
- This cache does not supply candidate `X`, `Q^nu`, `delta Q`, a foam-sector
  state variable, a physical transfer law, or known-model distinction.
- This cache can improve baseline-literature coverage and citation hygiene, but
  it does not support or validate QFUDS.
