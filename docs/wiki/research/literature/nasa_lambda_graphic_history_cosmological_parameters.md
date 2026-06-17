---
doc_id: lit_nasa_lambda_graphic_history_cosmological_parameters
title: NASA LAMBDA Graphic History Cosmological Parameters
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - research_cache_index
next_gate: numeric plot digitization only if exact historical parameter values are needed
last_updated: 2026-06-17
---

# NASA LAMBDA Graphic History Cosmological Parameters

## Bibliographic Metadata

- Source: NASA LAMBDA, "Graphic History to Cosmology".
- Source URL:
  <https://lambda.gsfc.nasa.gov/resources/graphic_history/index.html>
- Parameter page:
  <https://lambda.gsfc.nasa.gov/resources/graphic_history/parameters.html>
- Data-reference page:
  <https://lambda.gsfc.nasa.gov/resources/graphic_history/data_ref.html>
- References page:
  <https://lambda.gsfc.nasa.gov/resources/graphic_history/more_ref.html>
- Source owner shown in HTML metadata: NASA GSFC LAMBDA.
- Cache:
  [NASA LAMBDA Graphic History Assets](../assets/nasa_lambda_graphic_history/README.md).

## Workflow Application

- Workflow:
  [Research Asset and Product Workflow](../../../../.agent/workflows/research-asset-product-workflow.md).
- Source type: stable NASA LAMBDA reference website and page-family cache.
- Asset state: `asset_cached`.
- Derived product state: `manual_structured_extract` for the data-reference
  matrix only.
- Extraction potential: `direct_table`, `figure_digitization_possible`.
- Evidence role: baseline LambdaCDM/observational-parameter source coverage;
  not QFUDS support.

## Key Equations

The page family is primarily an explanatory and historical reference. The
Hubble-constant page states the standard flat/curved LambdaCDM expansion form
in terms of `H(z)`, `H0`, `Omega_m`, `Omega_Lambda`, and `Omega_k`.

This cache does not introduce QFUDS equations.

## Coupling Definitions

None. The source is a LambdaCDM and observational-parameter reference, not an
interacting-dark-sector model.

## Datasets Used

The LAMBDA `data_ref.html` page maps literature/data references to graphical
history plots for:

- scalar index `n_s`;
- universe age `t0`;
- optical depth to reionization `tau`;
- Hubble constant `H0`;
- matter density `Omega_m`;
- baryonic density `Omega_b h^2`;
- CDM density `Omega_c h^2`;
- matter clustering `sigma8`.

The extracted local matrix is
[data_reference_matrix.csv](../assets/nasa_lambda_graphic_history/digitization/data_reference_matrix.csv).

## Redshift Coverage

This is not a single redshift reconstruction product. It is a reference page
family spanning CMB, supernovae, galaxies/quasars, intensity mapping,
LambdaCDM theory, power spectrum, and historical one-dimensional parameter
constraints.

## Available Products

- Cached HTML page family: `asset_cached`.
- Linked PNG/JPG/PDF/SVG/EPS figure products: `asset_cached`.
- Data-reference matrix: `manual_structured_extract`.
- Numerical parameter-history points: not digitized.

## Digitization Requirements

If a future audit needs exact plotted values, use the cached SVG/PDF/EPS assets
where available and create a separate provenance file stating:

- source figure;
- axis mapping;
- units and parameter definition;
- extraction method;
- uncertainty handling;
- rows copied from the LAMBDA data-reference matrix.

Until then, use the cache for background/source coverage only.

## Public Code / Data Links

- LAMBDA data portal: <https://lambda.gsfc.nasa.gov/product/>
- Graphic History page family:
  <https://lambda.gsfc.nasa.gov/resources/graphic_history/>
- Local link inventory:
  [link_inventory.tsv](../assets/nasa_lambda_graphic_history/digitization/link_inventory.tsv).

## QFUDS Relevance

This source is important baseline context. It helps prevent omissions in
standard-parameter, CMB, Hubble-tension, and historical-observation framing.

It does not support QFUDS. It does not supply a physical transfer law,
candidate `X`, `Q^nu`, `delta Q`, or known-model distinction.

## Use Restrictions

- Do not cite this as evidence for QFUDS.
- Do not treat the graphical histories as numerical data unless a future
  digitization product records exact extraction provenance.
- Do not treat the LAMBDA educational/reference synthesis as a substitute for
  primary paper or likelihood products when a formal experiment needs
  numerical constraints.

## Check History

- 2026-06-17: Cached 20 HTML pages, downloaded 90 linked figure/vector assets,
  and extracted the 57-row data-reference matrix.
- 2026-06-17: Re-opened live NASA LAMBDA landing, parameter, and
  data-reference pages; local cache includes the 2025 data-reference rows and
  remains `asset_cached`, with plotted numerical values still not digitized.
