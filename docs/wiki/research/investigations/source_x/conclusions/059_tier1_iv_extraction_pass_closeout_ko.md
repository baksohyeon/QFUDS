---
doc_id: audit_2026_06_18_tier1_iv_extraction_pass_closeout_ko
title: Tier 1 IV Extraction Pass Closeout
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - plan_2026_06_18_paper_by_paper_iv_ide_equation_extraction_ko
  - audit_2026_06_18_li_2025_iv_ide_equation_extraction_ko
  - audit_2026_06_18_escamilla_2023_iv_ide_kernel_equation_extraction_ko
  - audit_2026_06_18_li_escamilla_iv_ide_convention_comparison_note_ko
  - audit_2026_06_18_martinelli_2019_iv_geodesic_cdm_equation_extraction_ko
  - audit_2026_06_18_hogg_2020_iv_geodesic_cdm_equation_extraction_ko
  - audit_2026_06_18_martinelli_hogg_iv_geodesic_cdm_same_family_comparison_note_ko
  - audit_2026_06_18_wang_2015_iv_equation_extraction_ko
  - audit_2026_06_18_wang_martinelli_hogg_iv_convention_comparison_note_ko
  - roadmap
next_gate: optional Tier 2 modern comparator extraction only if current observational-context comparison is explicitly needed
last_updated: 2026-06-18
---

# Tier 1 IV Extraction Pass Closeout

## Purpose

This note closes the Tier 1 paper-by-paper IV/IDE extraction pass that followed
the academic derivation bridge. It does not create a new QFUDS theory branch.

The goal is narrower:

- record what the retained `Gamma(a)` intuition can now be translated into;
- record what it still cannot supply;
- prevent a jump from timing resemblance to physical source language;
- decide whether more extraction is needed before the next conceptual step.

## Workflow Boundary

This closeout is an internal synthesis over existing Source-X records. It does
not introduce a new external source, new numerical product, or new
observational claim.

External-source handling remains governed by
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).
The inherited workflow states for the records summarized here are:

- `asset_cached`
- `asset_extracted_not_digitized`
- `source_text_parse`
- `manual_structured_extract`

These states mean the academic source terms and conventions were extracted for
audit use. They do not mean that QFUDS has evidence, validation, or Level 2B
admission.

## Short Closeout

Tier 1 is sufficient for the current bridge question.

The retained `Gamma(a)` can now be described honestly as a phenomenological
timing fingerprint that resembles a class of interacting-vacuum /
interacting-dark-energy source histories. It is not yet a physical QFUDS
derivation because it still lacks:

- a source object `X`;
- a derived covariant transfer vector `Q^mu[X]`;
- a reason phase B has `w ~= -1`;
- a perturbation prescription tied to the source;
- a novelty escape from known IV/IDE or interacting-vacuum models.

Do not run a retained-timing fit, NASA/BAO/CMB/LSS interpretation, or Level 2B
admission step from Tier 1 alone.

## Tier 1 Matrix

| Record | What it contributed | Useful bridge | Hard boundary |
| --- | --- | --- | --- |
| Li 2025 | DESI-era IV/IDE route with `Q = beta H rho_de`, frame language, and ePPF-style perturbation machinery. | Shows where real papers move from background `Q` to `Q^mu`, perturbations, and constraints. | Comparator only. It does not derive a QFUDS source or phase-B pressure. |
| Escamilla 2023 | Background-kernel language with `Pi_DE`, `I_Q`, and explicit sign/normalization conventions. | Shows how a time-dependent interaction kernel can be written without claiming a microphysical source. | Background-only for this bridge. It cannot be used as perturbation closure. |
| Martinelli 2019 | Interacting vacuum with geodesic CDM, `Q = -qHV`, a CDM-frame transfer choice, perturbations, and CAMB route. | Best Tier 1 formalism anchor for a perturbation-ready interacting-vacuum comparator. | The same machinery is a known-model sink unless QFUDS derives a distinct source. |
| Hogg 2020 | Same geodesic-CDM family plus binned reconstruction, CPZ correlation prior, PCA checks, and weak-evidence boundary. | Best Tier 1 non-circularity lesson: reconstruction needs priors and prior-dominance checks. | Reconstructed timing cannot be rebranded as source physics. |
| Wang 2015 | Historical `alpha(a)` interaction with nonlinear density factor, DM-frame closure, RSD/LyaF tension boundary, and PCA. | Sign-closer to retained positive `Gamma(a)` in one convention, but with a different density factor. | Similar sign does not establish equivalence or physical origin. |

## Translation Rules Frozen

These rules are the usable output of Tier 1:

1. `Gamma(a)` is a timing comparator, not a source derivation.
2. A scalar background rate is not enough. A physical model needs `Q^mu`, frame
   choice, perturbation equations, stability handling, and solver route.
3. Sign comparisons must always name the paper convention. Positive `Gamma(a)`
   cannot be compared across records without the density continuity equation.
4. Density factors matter. `rho_de`, `rho_dm`, `V`, and nonlinear
   `rho_dm V / (rho_dm + V)` forms are not interchangeable.
5. Reconstructed interaction histories are not physical origins. They are
   inference objects unless a source equation generates them.
6. Observational products are kill constraints or comparator context, not
   QFUDS evidence.
7. If `xi`, width, amplitude, or transition redshift are chosen after looking at
   the same observations used for support, the branch fails as circular.

## What QFUDS Still Misses

| Missing object | Why Tier 1 did not solve it | Stop condition |
| --- | --- | --- |
| `X` | The extracted papers define interaction forms or reconstruction spaces, not a QFUDS foam-sector state object. | Stop before source language. |
| `Q^mu[X]` | Tier 1 shows how papers choose transfer vectors, but QFUDS has not derived one from `X`. | Stop before perturbation or solver claims. |
| Phase-B pressure | None of the extracted records explains why a QFUDS phase has `w ~= -1`. | Stop before dark-energy physical-origin claims. |
| Perturbation closure | Martinelli/Hogg/Wang show closure choices, but they are model-family choices. | Stop before CMB/LSS viability claims. |
| Novelty equation | All usable routes currently sit inside known IV/IDE or interacting-vacuum machinery. | Stop before novelty language. |

## Tier 2 Decision

Do not automatically start Tier 2.

Tier 2 modern DESI-era parameterized extraction is useful only if the next
question explicitly needs current observational-context comparison. It is not
needed to answer the present bridge question, because Tier 1 already shows the
main academic gap:

```text
retained Gamma(a) -> phenomenological interaction history
retained Gamma(a) != derived Q^mu[X], pressure, perturbations, or novelty
```

If Tier 2 is opened later, it must be a separate comparator-extraction task, not
a QFUDS validation step.

## Decision

The paper-by-paper bridge reached a stable checkpoint:

- keep retained `Gamma(a)` as a phenomenological IV/IDE timing comparator;
- use Martinelli/Hogg/Wang/Li/Escamilla as formalism-learning anchors;
- do not claim physical QFUDS support;
- do not open Level 2B;
- do not use NASA/BAO/CMB/LSS products as model interpretation until a source
  object and non-circular equation route exist.

## Next Executable Instruction

If work continues, write a small learning checkpoint that maps one selected
academic equation family into a clean "what a real derivation would require"
template: background continuity equation, covariant transfer vector, frame
choice, perturbation variables, stability condition, and exact place where
retained `Gamma(a)` stops.
