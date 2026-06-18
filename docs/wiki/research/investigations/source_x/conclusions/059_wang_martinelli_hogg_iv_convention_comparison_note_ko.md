---
doc_id: audit_2026_06_18_wang_martinelli_hogg_iv_convention_comparison_note_ko
title: "2026-06-18 Wang/Martinelli/Hogg IV Convention Comparison Note"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - audit_2026_06_18_wang_2015_iv_equation_extraction_result_ko
  - audit_2026_06_18_martinelli_hogg_iv_geodesic_cdm_same_family_comparison_note_ko
  - asset_wang_2015_dark_matter_vacuum_interaction_equation_extract_20260618
  - asset_martinelli_2019_interacting_vacuum_geodesic_cdm_equation_extract_20260618
  - asset_hogg_2020_vacuum_geodesic_cdm_interaction_equation_extract_20260618
  - roadmap
next_gate: decide whether Tier 1 extraction is sufficient or continue to modern DESI-era comparator targets
last_updated: 2026-06-18
---

# 2026-06-18 Wang/Martinelli/Hogg IV Convention Comparison Note

## Purpose

이 문서는 Wang 2015 `alpha(a)` 계열과 Martinelli/Hogg `q(z)` 계열을
나란히 비교한다.

목적은 retained `Gamma(a)`를 fitting하는 것이 아니다. 목적은 `z ~= 2`
근방의 timing intuition이 실제 IV 문헌에서는 어떤 sign, density factor,
frame, perturbation, RSD observable, prior/PCA, and evidence boundary를
동반하는지 고정하는 것이다.

## Workflow Boundary

This note follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).

No new external source, PDF, posterior product, covariance product, chain,
numerical curve, or product-absence claim is introduced here. This is a
repo-internal comparison of already cached and manually extracted records:

```text
docs/wiki/research/assets/wang_2015_dark_matter_vacuum_interaction/digitization/equation_extraction_20260618.md
docs/wiki/research/assets/martinelli_2019_interacting_vacuum_geodesic_cdm/digitization/equation_extraction_20260618.md
docs/wiki/research/assets/hogg_2020_vacuum_geodesic_cdm_interaction/digitization/equation_extraction_20260618.md
```

Workflow states inherited by this comparison:

```text
asset_cached
asset_extracted_not_digitized
source_text_parse
manual_structured_extract
```

This is not numerical digitization and not QFUDS evidence.

## Convention Matrix

| Field | Wang 2015 | Martinelli 2019 | Hogg 2020 | QFUDS bridge implication |
| --- | --- | --- | --- | --- |
| coupling variable | `alpha(a)` | `q_V(z)` | `q(a)` / `q(z)` | no symbol-level equality |
| raw continuity form | `dot rho_dm + 3H rho_dm = -Q`; `dot V = Q` | same raw form | same raw form | raw `Q` sign can be aligned |
| parameterized `Q` | `3 alpha H rho_dm V / (rho_dm + V)` | `-q_V H V` in FLRW | `-q H V` | density factor differs materially |
| positive dimensionless direction | DM-to-vacuum | vacuum-to-CDM | vacuum-to-CDM | Wang sign is closer to retained positive `Gamma(a)` |
| retained mapping blocker | nonlinear density factor and frame/gauge closure | sign flip and vacuum-density factor | sign flip and inherited perturbation details | all remain comparator-only |
| `Q^mu` frame | parallel to DM four-velocity | parallel to CDM four-velocity after `f^mu=0` | same-family summary | all assume geodesic DM/CDM rather than deriving foam dynamics |
| vacuum perturbation | homogeneous vacuum frame, `delta V=0` | `delta V=0` in selected gauge | inherited from same-family theory | QFUDS has no derived perturbation prescription |
| `delta Q` / perturbation | explicit `delta_dm` equation with `Q(a_i)` term | `delta Q=0` in selected gauge | interaction unperturbed in selected gauge | not interchangeable |
| growth/RSD observable | `f_vartheta sigma_8` replaces simple LCDM growth reading | `f_i = f - Q/(H rho_c)` adjustment | same RSD caution | observational comparison needs model-specific observable |
| reconstruction | 40 scale-factor bins | four-bin / transition histories | 17 bins plus spline/GP | binning is inference machinery |
| prior/PCA | CPZ prior; three data modes; rest prior-dominated | less central in extracted note | CPZ prior and prior-dominance PCA | useful anti-overfit pattern, not physics source |
| evidence boundary | not Bayesian-preferred over LCDM | no QFUDS evidence | weak/no-meaningful evidence language | no validation language |

## What This Clarifies

Wang 2015 is the strongest caution against a too-easy retained `Gamma(a)`
translation:

```text
positive retained Gamma(a) direction ~= positive Wang alpha(a) direction
```

But that is only a sign resemblance. It does not supply equivalence because
Wang uses:

```text
Q = 3 alpha H rho_dm V / (rho_dm + V)
```

while retained mode uses:

```text
Q = mathcalH Gamma(a) rho_A
```

The mapping would need a non-circular derivation of why retained `rho_A` should
stand in for `rho_dm V / (rho_dm + V)`, why the same DM-frame perturbation
closure applies, and why the reconstructed timing is not just inherited from
the 2015 LyaF/RSD tension.

## Non-Circularity Rules

Do not use Wang's `z >= about 2.1` positive `alpha` interval to choose retained
transition timing and then call it foam evidence.

Do not map Wang's CPZ prior length, 40-bin setup, or PCA modes to a QFUDS foam
scale, transition width, or physical source amplitude.

Do not combine Wang sign direction with Martinelli/Hogg density factor unless
an explicit equation states the conversion.

Do not use BAO, LyaF, CMB, SNe, RSD, DES, or SKA references as QFUDS evidence.
They are baseline constraints or data-context explanations for academic IV
models.

## Decision

| Question | Decision |
| --- | --- |
| Does Wang 2015 make retained `Gamma(a)` physically derived? | No. |
| Is Wang sign direction useful? | Yes, as a convention teaching point only. |
| Which family is the perturbation-ready anchor? | Martinelli/Wang both provide perturbation routes; Hogg adds reconstruction guardrails. |
| Which family is closest to retained `Gamma(a)` by sign? | Wang 2015. |
| Which family is closest by density factor? | None; retained `rho_A`, Wang nonlinear `rho_dm V/(rho_dm+V)`, and Martinelli/Hogg `V` differ. |
| What survives? | A stronger academic bridge and a sharper list of missing QFUDS derivations. |

## Next Executable Instruction

Close the Tier 1 extraction pass with a short synthesis note, or continue to
modern DESI-era comparator targets only if the next task needs current
observational context. Do not run retained `Gamma(a)` fitting until sign,
density, Hubble, frame, perturbation, RSD observable, prior/PCA, and evidence
translation rules are frozen.
