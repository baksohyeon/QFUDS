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
| Interacting Vacuum | Vacuum energy exchanging with CDM-like matter | `model-family overlap` | [015_qfuds_level_1_5_equivalence_source_perturbation_audit.md](../02_theory/015_qfuds_level_1_5_equivalence_source_perturbation_audit.md), [030_result_003_phenomenological_perturbation_closure.md](../04_results/030_result_003_phenomenological_perturbation_closure.md) | The retained branch is best classified as phenomenological interacting vacuum after Level 1.5. | Can a future source make the transfer physical rather than chosen? |
| Interacting Dark Energy | Coupled dark-sector models with `Q` or `Q^nu` | `model-family overlap` | [010_result_001_gamma_scan.md](../04_results/010_result_001_gamma_scan.md), [015_qfuds_qnu_necessity_formulation_audit.md](../02_theory/015_qfuds_qnu_necessity_formulation_audit.md) | Free or fitted `Gamma(a)` puts QFUDS in ordinary interacting-dark-energy territory. | What fixed source relation distinguishes QFUDS from a fitted interaction function? |
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

The repository has clarified the design space:

1. LCDM is the exact null limit when transfer is absent.
2. Free or early-active transfer laws are not distinctive and can fail quickly.
3. Collapse/information timing is a useful proxy but not a derivation.
4. The retained branch survives only as phenomenological interacting vacuum.
5. A future physical branch must supply equations that distinguish it from the
   model families above.
