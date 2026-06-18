---
doc_id: audit_2026_06_18_martinelli_hogg_iv_geodesic_cdm_same_family_comparison_note_ko
title: "2026-06-18 Martinelli/Hogg IV/Geodesic-CDM Same-Family Comparison Note"
doc_type: reference
stage: reference
status: completed
evidence_role: audit
depends_on:
  - audit_2026_06_18_martinelli_2019_iv_geodesic_cdm_equation_extraction_result_ko
  - audit_2026_06_18_hogg_2020_iv_geodesic_cdm_equation_extraction_result_ko
  - asset_martinelli_2019_interacting_vacuum_geodesic_cdm_equation_extract_20260618
  - asset_hogg_2020_vacuum_geodesic_cdm_interaction_equation_extract_20260618
  - roadmap
next_gate: decide whether Wang 2015 should be cached/extracted as the next historical IV convention target
last_updated: 2026-06-18
---

# 2026-06-18 Martinelli/Hogg IV/Geodesic-CDM Same-Family Comparison Note

## Purpose

이 문서는 Martinelli 2019와 Hogg 2020을 같은 vacuum-geodesic CDM 계열로
비교한다.

목적은 retained `Gamma(a)`를 fitting하는 것이 아니다. 목적은 실제
interacting-vacuum 문헌이 같은 물리 세팅을 공유하더라도, 하나는 상세
perturbation-ready formalism을 전개하고 다른 하나는 17-bin reconstruction
and prior-control problem으로 확장한다는 점을 분리하는 것이다.

## Workflow Boundary

This note follows the
[Research Asset and Product Workflow](../../../../../../.agent/workflows/research-asset-product-workflow.md).

No new external source, PDF, posterior product, covariance product, chain,
numerical curve, or product-absence claim is introduced here. This is a
repo-internal comparison of already cached and manually extracted records:

```text
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

## Same-Family Matrix

| Field | Martinelli 2019 | Hogg 2020 | QFUDS bridge implication |
| --- | --- | --- | --- |
| `model_class` | interacting vacuum / geodesic CDM | interacting vacuum / geodesic CDM | same academic family, not a QFUDS source |
| `background_Q_raw` | `dot rho_c + 3H rho_c = -Q`; `dot V = Q` | same raw continuity form | retained `Gamma(a)` still needs sign and density translation |
| `parameterized_Q` | `Q = -q_V Theta V / 3`; FLRW `Q = -q_V H V` | `Q = -qHV` | same vacuum-density coupling up to notation |
| `positive_dimensionless_direction` | positive `q_V` means vacuum-to-CDM | positive `q` means vacuum-to-CDM | opposite to retained positive `Gamma(a)` direction |
| `density_factor` | vacuum density `V` | vacuum density `V` | not retained `rho_A` |
| `Q_mu_frame` | covariant `Q^mu`, CDM-frame pure energy exchange | summarized as `Q^mu = Q u^mu + f^mu`, with `f^mu = 0` | QFUDS lacks a derived transfer vector |
| `momentum_transfer` | zero in CDM frame | zero in CDM frame | geodesic CDM is an assumption, not a foam derivation |
| `gauge` | synchronous gauge comoving with CDM | synchronous CDM-comoving gauge stated | copied gauge closure would be post-hoc without QFUDS equations |
| `delta_Q` | `delta Q = 0` in selected gauge | interaction unperturbed in selected gauge, details inherited | Hogg relies on same-family formalism rather than restating all equations |
| `solver_route` | modified CAMB plus CosmoMC | modified CAMB plus CosmoMC; GetDist and MCEvidence for postprocessing | perturbation-ready comparator, not Level 2B admission |
| `reconstruction_scope` | constant, transition, seeded-vacuum, and four-bin histories | 17-bin reconstruction with spline and GP | Hogg is the stronger anti-overfit teaching example |
| `prior_control` | limited relative to Hogg | CPZ correlation prior, `N_eff`, prior strength, PCA prior-dominance check | useful non-circularity pattern |
| `model_selection` | likelihood constraints and tension discussion | Bayes factor and data-only `Delta chi^2` boundary | no validation language |
| `product_status` | no machine-readable `q_V(z)` posterior history created by extraction | no machine-readable `q(z)` posterior history created by extraction | no timing fit should be run from these notes |
| `stop_status` | `continue_to_perturbation_extract` | `continue_to_perturbation_extract`, with perturbations inherited by reference | same-family comparison is allowed; QFUDS admission is not |

## What Hogg Adds Over Martinelli

Hogg 2020 is not a new QFUDS source. Its value for the current repo is
methodological:

| Hogg object | Why it matters | Stop rule |
| --- | --- | --- |
| 17 `q_i` bins | shows how an academic paper makes a flexible interaction history explicit | do not rename bins as foam transition structure |
| CPZ correlation prior | suppresses rapid oscillations and reduces binning bias | do not treat prior smoothness as physical derivation |
| `N > N_eff` rule | chooses enough bins relative to correlation length | do not map `a_c` to `xi_gal` or a QFUDS scale |
| prior-only PCA comparison | checks whether the prior washes out the data | useful audit harness pattern only |
| Bayes factor and data-only `Delta chi^2` | separates weak hints from meaningful model preference | no support/validation wording |
| BAO/SNe tension statement | records that late-time interaction does not resolve `H_0` under those data choices | baseline constraint only |

## What QFUDS Was Missing

The retained `Gamma(a)` work stopped at a useful shape intuition. Martinelli and
Hogg show the missing academic objects:

1. define `Q` with sign, density factor, and Hubble normalization;
2. embed `Q` into a covariant `Q^mu`;
3. choose the transfer frame and momentum-exchange rule;
4. state the gauge and perturbation closure;
5. implement a solver route before using CMB/LSS/BAO constraints;
6. define prior and binning safeguards before interpreting reconstructed
   interaction histories;
7. separate model-selection language from visual curve similarity.

That means the safe interpretation is:

```text
retained Gamma(a) = phenomenological timing comparator
Martinelli/Hogg q(z) = academic IV/geodesic-CDM coupling reconstruction
QFUDS physical source = still not derived
```

## Non-Circularity Rules

Do not use Martinelli or Hogg to choose a retained `Gamma(a)` amplitude, width,
transition redshift, or foam scale and then claim the result as QFUDS source
support.

Do not use Hogg's CPZ correlation length, 17-bin setup, spline, GP kernel, or
PCA result as a physical foam-sector derivation.

Do not treat BAO, CMB, SNe, RSD, DES, Lyman-alpha, or SKA mentions in Hogg as
QFUDS evidence. They are baseline constraints or future probes for academic
interacting dark-sector models.

## Decision

| Question | Decision |
| --- | --- |
| Are Martinelli 2019 and Hogg 2020 the same academic family? | Yes: vacuum-geodesic CDM interaction with CDM-frame no-momentum-transfer closure. |
| Which paper is the better perturbation/formalism anchor? | Martinelli 2019. |
| Which paper is the better reconstruction/non-circularity teaching target? | Hogg 2020. |
| Does either paper supply QFUDS source object `X`? | No. |
| Does either paper validate retained `Gamma(a)`? | No. |
| What survives for QFUDS? | A disciplined bridge into known IV/geodesic-CDM formalism, not an independent theory claim. |

## Next Executable Instruction

Decide whether to cache/source-extract Wang 2015 as the next historical
interacting-vacuum convention target. If yes, apply the same workflow:
source-state record first, exact equation extraction second, convention
comparison third. Do not run retained `Gamma(a)` fitting or NASA/BAO/CMB/LSS
interpretation before the convention map is complete.
