---
doc_id: qfuds_positioning
title: QFUDS Positioning
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - qfuds_research_report
  - decision_log
  - experiment_summary
  - traceability_matrix
  - roadmap
next_gate: use roadmap for current status; compare new ideas before new branches
last_updated: 2026-06-09
---

# QFUDS Positioning

## Purpose

This document maps QFUDS ideas onto the existing cosmology landscape. It is a
positioning guide, not a status authority. Current status lives in
[docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md).

Classification labels:

- `literature overlap`: already exists in close form in the literature;
- `model-family overlap`: QFUDS can be written as, or compared directly with,
  a known model family;
- `partially supported`: repository evidence supports a limited, scoped claim;
- `requires new assumptions`: not rejected, but needs new equations or inputs;
- `unsupported`: currently speculative in this repository;
- `rejected by repository evidence`: failed a stated repository test or audit.

## Landscape Map

| Idea | Closest literature or model family | Repository status | Evidence gathered | What was learned | Open questions |
| --- | --- | --- | --- | --- | --- |
| DM/DE unification | Unified dark sector, quartessence, k-essence, generalized dark matter | `model-family overlap` | [900_qfuds_research_report.md](../02_theory/900_qfuds_research_report.md), [research_program.md](research_program.md) | The core question is meaningful but not automatically novel; unification must beat known unified-fluid and scalar-field constructions. | What physical degree of freedom makes phase A dust-like while phase B has vacuum pressure? |
| Unified Dark Sector | Unified dark fluid, decomposed dark-sector stress tensor | `literature overlap` | [900_qfuds_research_report.md](../02_theory/900_qfuds_research_report.md), [000_qfuds_v0_2_two_phase_background.md](../02_theory/000_qfuds_v0_2_two_phase_background.md) | QFUDS belongs near existing unified-dark-sector models unless it supplies new microphysics or observables. | Can the phase split be made independently measurable or dynamically derived? |
| Unified Dark Fluid | Generalized Chaplygin gas, generalized dark matter, nonbarotropic unified fluids | `model-family overlap` | [030_qfuds_phenomenological_perturbations.md](../02_theory/030_qfuds_phenomenological_perturbations.md), [900_qfuds_research_report.md](../02_theory/900_qfuds_research_report.md) | A single adiabatic fluid with late vacuum pressure risks excessive sound speed and matter-power failure. | Can QFUDS derive entropy perturbations or a noncanonical action that keeps clustering stable? |
| Interacting Vacuum | Vacuum energy exchanging with CDM-like matter | `model-family overlap` | [015_qfuds_level_1_5_equivalence_source_perturbation_audit.md](../02_theory/015_qfuds_level_1_5_equivalence_source_perturbation_audit.md), [030_result_003_phenomenological_perturbation_closure.md](../04_results/030_result_003_phenomenological_perturbation_closure.md), [030_result_004_p1_model_family_positioning.md](../04_results/030_result_004_p1_model_family_positioning.md) | Exp 004 classifies retained P1 as an exact interacting-vacuum instance with `xi(a)=Gamma(a)` at the background and declared Level 2A P1 closure layers. | Can a future source make the transfer physical rather than chosen? |
| Interacting Dark Energy | Coupled dark-sector models with `Q` or `Q^nu` | `model-family overlap` | [010_result_001_gamma_scan.md](../04_results/010_result_001_gamma_scan.md), [015_qfuds_qnu_necessity_formulation_audit.md](../02_theory/015_qfuds_qnu_necessity_formulation_audit.md), [030_result_004_p1_model_family_positioning.md](../04_results/030_result_004_p1_model_family_positioning.md) | Free or fitted `Gamma(a)` puts QFUDS in ordinary interacting-dark-energy territory; Exp 004 shows retained P1 is a subset of time-dependent IDE under `xi(a)=Gamma(a)`. | What fixed source relation distinguishes a future physical QFUDS branch from a fitted interaction function? |
| Collapse-driven transfer | Press-Schechter collapse history, halo formation proxies | `requires new assumptions` | [020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md), [015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md) | Collapse timing is useful as a low-redshift proxy, but it does not derive conversion into phase B. | What physical threshold, source scalar, and self-consistent QFUDS growth computation define the transfer? |
| Information-production source | Information encoded into collapsed structures, relative entropy, halo statistics | `requires new assumptions` | [020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md), [decision_log.md](decision_log.md) | It was the narrowest experiment 002 route, but it remained proxy-level and later failed physical promotion. | What is the independently defined information measure, and how does it source vacuum pressure? |
| Entropy source | Horizon entropy, HBM/KL gravitational entropy, black-hole entropy | `rejected by repository evidence` for broad entropy language | [020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md), [traceability_matrix.md](traceability_matrix.md) | Horizon entropy overlaps standard horizon/interacting dark energy; broad gravitational entropy failed positivity at tested amplitudes; black-hole entropy lacks mass/accretion history. | Is there a narrower entropy source with units, normalization, and perturbations? |
| Strong-gravity source | Black holes, horizons, remnants, baby-universe dynamics | `requires new assumptions` | [015_qfuds_strong_gravity_source_mechanism_audit.md](../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md) | Strong-gravity ideas are not ruled out as future hypotheses, but none currently supplies the full physical-transfer package. | What source scalar and stress-energy relation connect strong gravity to smooth phase B? |
| Cosmologically coupled black holes | Black-hole mass growth or compact-object vacuum-energy coupling | `unsupported` in this repository | [015_qfuds_strong_gravity_source_mechanism_audit.md](../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md) | This is the most directly relevant strong-gravity family, but it maps black holes to dark energy rather than deriving QFUDS phase transfer. | Can it produce `X`, `Q^nu`, phase-B vacuum pressure, `delta Q`, and a distinction from existing black-hole-coupled dark energy? |
| Holographic dark energy | Horizon/IR cutoff models, horizon thermodynamics | `literature overlap` | [900_qfuds_research_report.md](../02_theory/900_qfuds_research_report.md), [020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md), [015_qfuds_strong_gravity_source_mechanism_audit.md](../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md) | Horizon routes are better at generating vacuum-pressure behavior than DM-to-DE transfer and risk becoming known HDE. | What foam-specific cutoff or transfer law is not already HDE? |
| White-hole / Planck-star / baby-universe ideas | Black-to-white-hole tunneling, remnants, baby universes, wormholes | `unsupported` as dark-energy source | [concept_origin.md](../01_origin/concept_origin.md), [015_qfuds_strong_gravity_source_mechanism_audit.md](../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md), [research_program.md](research_program.md) | These ideas are useful provenance and optional remnant-sector prompts, but they do not currently explain smooth dark energy. | Can they produce a constrained relic abundance, release rate, or stress-energy transfer without replacing the main model with speculation? |

## Positioning Summary

QFUDS currently sits closest to interacting-vacuum, interacting-dark-energy, and
unified-dark-sector model families. Its original quantum-foam language remains a
motivation, not an established physical derivation.

## Exp 004 Interpretation

Experiment 004 changes the project interpretation from "the retained branch may
be near interacting vacuum" to a sharper statement:

```text
retained P1 is an exact interacting-vacuum instance, and a subset of
time-dependent interacting dark energy, when xi(a)=Gamma(a).
```

This is useful because it means the original intuition did not float outside
known cosmology. It mapped into an existing dark-sector model family with
well-defined comparison machinery. It also means the retained branch is not a
new physical theory by itself.

Repository-level implications:

| Category | Interpretation after Exp 004 |
| --- | --- |
| Supported by repository evidence | The two-phase bookkeeping has a valid LCDM null limit; retained P1 can be written and integrated as a Level 2A interacting-vacuum closure; Exp 004 maps P1 exactly to interacting vacuum under `xi(a)=Gamma(a)`. |
| Supported only phenomenologically | The retained collapse/information-production `Gamma(a)` shape remains a useful late, structure-timed transfer parameterization. It can guide interacting-vacuum / IDE phenomenology, but it is not a source derivation. |
| Reduced to known cosmology | Retained P1 reduces to interacting vacuum and time-dependent IDE. Background expansion can also be reconstructed by an effective non-interacting `w(a)`, so background behavior alone does not define a distinct QFUDS class. |
| Still speculative | A physical quantum-foam or strong-gravity source for DM-to-DE phase transfer; a derived `Q^nu`; a phase-B vacuum-pressure rationale; a physical `delta Q` route; and a known-model distinction for future branches. |

What should be believed differently:

Before Exp 004, it was still possible to describe retained P1 as a QFUDS-shaped
phenomenological branch whose precise literature location needed clarification.
After Exp 004, retained P1 should be believed to be ordinary
interacting-vacuum / time-dependent IDE phenomenology with a particular
source-shaped coupling. That is not a failure of the research program; it is a
successful positioning result.

What mapped successfully:

- the intuition that a dark-sector transfer can connect a clustering component
  and a vacuum-like component;
- the late, structure-timed transfer shape as a phenomenological `Gamma(a)`;
- the phase-A plus phase-B language as an interacting-vacuum decomposition;
- the Level 2A P1 perturbation closure as a known-style interacting-vacuum
  closure.

What collapsed into known model families:

- retained P1 at the background and declared Level 2A closure layers collapses
  into interacting vacuum;
- retained P1 as a broader class collapses into time-dependent IDE under
  `xi(a)=Gamma(a)`;
- simple changes of transfer-shape basis are parameterization differences, not
  new physical model classes;
- background-only expansion matching collapses into effective `w(a)`
  reconstruction and is not enough to distinguish QFUDS.

What is now resolved:

- retained P1's closest model family is interacting vacuum;
- retained P1 is not an independent physical QFUDS derivation;
- equivalence to IDE/interacting vacuum is a positioning result, not a negative
  result;
- a future physical branch cannot inherit retained P1's source relation as
  already derived.

What should be retired for the retained branch:

- claims that retained collapse/information production physically derives
  DM-to-DE conversion;
- claims that retained P1 is novel because of its two-phase naming;
- claims that the retained branch is distinguishable from interacting vacuum or
  IDE without a new source equation or closure;
- claims based on background behavior alone as evidence of physical QFUDS.

What remains open for future physical branches:

- whether a new source `X` can generate a non-ad hoc transfer;
- whether that source can supply `Q^nu`, a phase-B vacuum-pressure rationale,
  and a physical `delta Q` route;
- whether a future physical branch can avoid reduction to LCDM, unified dark
  fluid, interacting vacuum, IDE, holographic dark energy, or remnant dark
  matter;
- whether any future branch can produce observational consequences beyond known
  model-family parameterizations.

The repository has clarified the design space:

1. LCDM is the exact null limit when transfer is absent.
2. Free or early-active transfer laws are not distinctive and can fail quickly.
3. Collapse/information timing is a useful proxy but not a derivation.
4. The retained branch is exactly positioned as interacting-vacuum /
   time-dependent IDE phenomenology, not physical QFUDS.
5. A future physical branch must supply equations that distinguish it from the
   model families above.
