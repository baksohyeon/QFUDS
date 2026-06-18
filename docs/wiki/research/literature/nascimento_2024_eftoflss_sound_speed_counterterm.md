---
doc_id: lit_nascimento_2024_eftoflss_sound_speed_counterterm
title: Nascimento 2024 EFTofLSS Sound Speed Counterterm
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - literature_cache_index
next_gate: none; raw literature cache only
last_updated: 2026-06-18
record_type: literature_record
paper_year: 2024
availability_last_checked: 2026-06-18
used_by:
  - source_x_foam_state_variable_question_result
  - source_x_falsifiability_ledger
---

# Nascimento 2024 EFTofLSS Sound Speed Counterterm

## Workflow Boundary

This literature record follows the
[Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md).
The source was `hit_not_cached` before this record. This record promotes it to
a repository literature record; raw arXiv assets remain
`asset_available_not_downloaded`.

## Bibliographic Metadata

- Paper: "A semi-analytic estimate for the effective sound speed counterterm in
  the EFTofLSS"
- Authors: Caio Nascimento, Drew Jamieson, Matthew McQuinn, Marilena Loverde
- arXiv: [2410.11949](https://arxiv.org/abs/2410.11949)

## Key Equations

- Treats the effective sound-speed counterterm in the Effective Field Theory of
  Large Scale Structure.
- Uses nonlinear structure information and separate-universe methods to estimate
  a nuisance counterterm.

## Coupling Definitions

- No QFUDS dark-sector coupling is defined.
- Candidate relevance is that a galaxy/cosmic-web scale can be absorbed as an
  EFTofLSS cutoff or counterterm calibration.

## Datasets Used

Theory/simulation-calibration paper; no QFUDS product cached here.

## Redshift Coverage

Not a dark-sector source-history product.

## Available Products

- arXiv abstract, PDF, source, and HTML are available.
- Repository raw asset cache was not created in this pass.
- Workflow state for this record: `literature_record_cached`.

## Digitization Requirements

None for 052/053 use unless a later audit needs exact counterterm values or
simulation-calibration details.

## Public Code / Data Links

- arXiv page: <https://arxiv.org/abs/2410.11949>

## QFUDS Relevance

Reference role: EFTofLSS known-model sink for `xi_gal`.

If `xi_gal` only behaves as a smoothing cutoff or counterterm calibration, the
candidate is not QFUDS novelty.

## Use Restrictions

- Do not use EFTofLSS absorption as a QFUDS success claim.
- Do not select `xi_gal` from NASA/BAO/LSS targets and call it physical foam.

## Check History

- 2026-06-18: arXiv metadata checked for the foam-state-variable question pass.
