---
doc_id: concept_survival_audit
title: QFUDS Concept Survival Audit
doc_type: summary
stage: "2"
status: completed
evidence_role: audit
depends_on:
  - concept_origin
  - qfuds_project_identity
  - qfuds_positioning
  - result_001_5_phase_transfer_physicality
  - result_004_p1_model_family_positioning
  - result_005_timing_prior_usefulness
  - result_006_literature_timing_support_audit
  - audit_2026_06_11_known_model_distinction_audit_result
  - audit_2026_06_12_foam_sector_to_gamma_derivation_feasibility_result
next_gate: observer mode; no physical branch without X, Q^nu, phase-B rationale, delta Q, and known-model distinction
last_updated: 2026-06-12
---

# QFUDS Concept Survival Audit

Date: 2026-06-12

This note maps the original QFUDS intuition against the current repository
evidence. It is a handoff audit, not a status authority. Current level, active
blockers, and roadmap status live only in
[docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md).

The original intuition can be summarized as:

```text
information compression
-> structure formation
-> black-hole / high-entropy sites
-> dark-sector dynamic-equilibrium shift
-> z ~= 2 interaction feature
```

The repository has not validated that chain as physics. It has partly preserved
one narrower timing intuition:

```text
structure-era activity may be related to dark-sector interaction timing.
```

## Classification Key

This audit uses the requested labels:

- `rejected`
- `demoted to motivation`
- `retained as phenomenological intuition`
- `retained as timing feature`
- `retained as candidate source mechanism`
- `still open but unsupported`
- `blocked until X, Q^nu, delta Q, or physical source exists`

## Concept Map

| Original concept | Current classification | What survived | What failed or remains missing | Primary evidence |
| --- | --- | --- | --- | --- |
| information preservation / Landauer motivation | demoted to motivation | The origin trail remains useful for explaining why information, entropy, black holes, and dark-sector questions were connected. | Landauer does not derive a cosmological source, transfer law, vacuum pressure, or perturbation closure. | [concept_origin.md](../01_origin/concept_origin.md), [020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md) |
| black-hole information compression | retained as candidate source mechanism | Black-hole entropy, mass growth, and high-entropy compact objects remain possible future `X` candidates. | No repository equation maps black-hole information compression into smooth phase-B vacuum pressure. No black-hole mass/accretion history is accepted as a QFUDS source. | [015_qfuds_strong_gravity_source_mechanism_audit.md](../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md), [020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md) |
| black-hole / white-hole / remnant intuition | demoted to motivation; retained as candidate source mechanism only for future branches | Remnants and white-hole-like ideas remain provenance and optional defect-sector prompts. | They are not a current source for dark energy and do not define `Q^nu`, `delta Q`, relic abundance, release rate, or stress-energy transfer. | [concept_origin.md](../01_origin/concept_origin.md), [015_qfuds_strong_gravity_source_mechanism_audit.md](../02_theory/015_qfuds_strong_gravity_source_mechanism_audit.md) |
| quantum-foam dark-sector medium | still open but unsupported | It remains the model language for asking whether DM and DE are two effective macroscopic phases of one spacetime-foam sector. | No microscopic foam degree of freedom, action, stress tensor, perturbation prescription, or known-model distinction has been derived. | [project_identity.md](project_identity.md), [qfuds_positioning.md](qfuds_positioning.md), [000_roadmap.md](../05_next_steps/000_roadmap.md) |
| DM/DE two-effective-phase idea | retained as phenomenological intuition | Phase A and phase B bookkeeping gives a valid LCDM null limit and a useful interacting-vacuum decomposition. | It is not yet a physical unification theory. Retained P1 maps into interacting vacuum / time-dependent IDE under `xi(a)=Gamma(a)`. | [000_result_000_lcdm_baseline.md](../04_results/000_result_000_lcdm_baseline.md), [030_result_004_p1_model_family_positioning.md](../04_results/030_result_004_p1_model_family_positioning.md) |
| dynamic-equilibrium intuition | still open but unsupported; blocked until X, Q^nu, delta Q, or physical source exists | The idea that a dark-sector equilibrium could shift during structure formation remains a candidate hypothesis. | It is not yet a testable model. The repository has no state variable, equilibrium condition, source law, transfer four-vector, phase-B response, perturbation route, or failure criteria for it. | [015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md), [000_roadmap.md](../05_next_steps/000_roadmap.md) |
| structure-era timing | retained as timing feature | The strongest surviving core is the timing idea: the relevant interaction support may sit in the structure era rather than radiation domination or only at very late time. | Timing alone is not a source derivation, not novelty, and not observational viability. | [030_result_005_timing_prior_usefulness.md](../04_results/030_result_005_timing_prior_usefulness.md), [030_result_006_literature_timing_support_audit.md](../04_results/030_result_006_literature_timing_support_audit.md) |
| retained `Gamma(a)` | retained as phenomenological intuition; prototype implementation only | It is a useful first implementation of a source-shaped transfer profile and a [Level 2A](../wiki/glossary/repository_levels.md) interacting-vacuum closure. | It failed physical Level 1.5 promotion and is not the full QFUDS hypothesis. It is not a derived source, not an independent model family, and not currently the optimal compression family in the digitized audit output. | [015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md), [030_result_004_p1_model_family_positioning.md](../04_results/030_result_004_p1_model_family_positioning.md), `outputs/li2025_digitized_compression_audit/li2025_digitized_compression_summary.json` |
| `z ~= 1.7-2.1` DESI-era timing feature | retained as timing feature | Retained timing has peak redshift `z ~= 2.046` and weighted mean `z ~= 1.746`; inspected table-level literature products allow overlap with this region. | The cause of the feature is not known. Exp006 says table-level support is allowed but not informative, and the digitized compression output says retained timing captures only a partial high-z structure-era component. | [030_result_005_timing_prior_usefulness.md](../04_results/030_result_005_timing_prior_usefulness.md), [030_result_006_literature_timing_support_audit.md](../04_results/030_result_006_literature_timing_support_audit.md), `outputs/li2025_digitized_compression_audit/li2025_digitized_compression_summary.json` |

## Original-Hypothesis Status Snapshot

This table compares the original "one foam medium, two effective dark-sector
phases" intuition against the current roadmap and the latest Source-X
feasibility result.

| Status label | Repository-state answer | Evidence boundary |
| --- | --- | --- |
| verified | The LCDM null limit and the basic two-phase background bookkeeping are verified as implementation scaffolding. `Gamma(a)=0` recovers the control path, and nonzero transfer profiles can be run as toy backgrounds. | This verifies the scaffold, not physical QFUDS. |
| confirmed | The retained timing fingerprint is confirmed as a repository feature: the prototype has support near the structure era, with peak timing around `z ~= 2`. | This confirms timing in the prototype, not its physical cause. |
| rejected | Constant transfer, ungated growth-driven transfer at tested amplitudes, the retained collapse/information-production source relation as a physical derivation, P2 at retained amplitude, and the Chen-Gamma / black-hole entropy known-model distinction claim are rejected or blocked by audits. | These are branch-level decisions, not a rejection of the whole QFUDS question. |
| discarded | White-hole-universe imagery, Landauer-as-cosmology, broad entropy language, generic remnant language, and generic foam language are discarded as explanatory evidence. | They remain provenance or motivation only unless made into equations and observables. |
| deferred | The original foam-sector route is deferred. The 050 feasibility result finds no non-circular foam-sector state variable, calculable phase definitions, replacement transition object, or foam-sector equation set. | It is unsupported before derivation, not killed by a failed derivation. |

## Nearest Literature Neighbors

This section records similarity to existing research lines. It is not repository
evidence for QFUDS and does not promote any concept above the classifications in
the table above.

| Neighbor line | Why it is close | Boundary for QFUDS |
| --- | --- | --- |
| vacuum-energy self-tuning / sequestering | Kaloper-Padilla-style vacuum energy sequestering asks whether vacuum energy can be prevented from gravitating in the naive way, and whether the observed effective cosmological constant can be fixed by global constraints or cosmic history. This is the closest neighbor to the intuition that `Lambda` could be an effective dynamic-equilibrium value rather than a fixed inserted number. | It is a known cosmological-constant-problem framework, not a QFUDS derivation. A QFUDS dynamic-equilibrium branch would still need `X`, `Q^nu`, a phase-B vacuum-pressure rationale, `delta Q`, and a known-model distinction. |
| thermodynamic / information-theoretic gravity | Jacobson derives Einstein's equation as a thermodynamic equation of state, and Verlinde's emergent-gravity proposal links dark-gravity effects to de Sitter entropy, information, and dark energy. This overlaps the intuition that dark matter might be a collective spacetime or vacuum effect rather than an ordinary particle. | These works do not supply the QFUDS two-phase transfer law. They are motivation and comparison targets unless QFUDS derives its own stress tensor, source, and perturbations. |
| Planck-star, white-hole-remnant, and remnant-dark-matter scenarios | Rovelli/Vidotto-style black-to-white-hole and Planck-mass remnant work overlaps the black-hole / white-hole / information-storage part of the origin trail. | These scenarios mainly point to compact remnants or dark-matter subcomponents, not smooth phase-B vacuum pressure. In QFUDS they remain optional candidate mechanisms until an abundance, mass function, source term, and stress-energy transfer are derived. |
| DESI-era evolving-dark-energy and IV/IDE literature | DESI DR2 strengthens the observational motivation to test whether dark energy is exactly constant, while IV/IDE reconstructions provide timing products that can be compared with retained structure-era timing. | This is not a QFUDS validation. Current repository status remains that retained timing is allowed but not informative at table level, and the digitized compression audit leaves retained timing as partial compression rather than the best family. |

The closest current reading order is:

```text
vacuum energy sequestering / self-tuning
-> thermodynamic or information-theoretic gravity
-> emergent-gravity dark-sector effects
-> Planck-star / white-hole-remnant dark-matter candidates
```

This sequence resembles the original thought trail, but no cited line supplies
the full QFUDS chain:

```text
Landauer / information preservation
-> black-hole / white-hole information cycle
-> vacuum residual
-> small positive Lambda
-> structure-era dark-sector interaction feature
```

Reference anchors:

- Kaloper and Padilla, [Sequestering the Standard Model Vacuum Energy](https://link.aps.org/doi/10.1103/PhysRevLett.112.091304)
- Kaloper and Padilla, [Vacuum energy sequestering: The framework and its cosmological consequences](https://arxiv.org/abs/1406.0711)
- Jacobson, [Thermodynamics of Spacetime: The Einstein Equation of State](https://arxiv.org/abs/gr-qc/9504004)
- Verlinde, [Emergent Gravity and the Dark Universe](https://arxiv.org/abs/1611.02269)
- Rovelli and Vidotto, [Planck stars, White Holes, Remnants and Planck-mass quasi-particles](https://arxiv.org/abs/2407.09584)
- Christodoulou and Rovelli, [Small black/white hole stability and dark matter](https://arxiv.org/abs/1805.03872)
- DESI Collaboration, [DESI DR2 Results: March 19 Guide](https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/)
- DESI Collaboration, [DESI DR2 results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints](https://arxiv.org/abs/2503.14738)

## What Survived?

The parts that survived are narrow:

1. A two-effective-phase dark-sector bookkeeping language remains useful.
2. The retained P1 branch can be written as Level 2A interacting-vacuum /
   time-dependent IDE phenomenology.
3. The structure-era timing intuition survived as a phenomenological timing
   feature.
4. The `z ~= 1.7-2.1` region remains a real timing fingerprint of the retained
   profile and is not ruled out by the inspected table-level products.
5. Black holes, remnants, and strong-gravity quantities remain possible future
   source candidates only if they become equations.

The core surviving idea is not:

```text
retained Gamma(a) physically derives QFUDS.
```

The core surviving idea is:

```text
dark-sector interaction timing may be related to the structure-formation era.
```

## What Was Killed?

Exp004-Exp006 and the digitized compression audit killed or narrowed these
stronger claims:

1. Retained P1 is not an independent physical QFUDS model family. Exp004 maps it
   exactly into interacting vacuum / time-dependent IDE at the declared Level 2A
   P1 closure layer.
2. The retained collapse/information-production source relation is not a
   physical derivation. Level 1.5 demoted it to phenomenological interacting
   vacuum.
3. Retained `Gamma(a)` is not currently justified as an informative IV/IDE prior
   from table-level literature products. Exp006 classifies it as
   `allowed_but_not_informative`.
4. The digitized compression output does not select retained `Gamma(a)` as the
   best compression family: `retained_best_count = 0` and
   `classification = partial_compression`.
5. Broad entropy language was killed as an explanatory source unless a specific
   `S(a)`, normalization, stress-energy relation, and perturbation route are
   supplied.

The digitized audit does not kill the broader structure-era timing intuition.
Its decision says retained timing captures a meaningful high-z structure-era
component, while simpler fitted transition or tomographic families describe the
digitized timing structure more efficiently under the current evidence.

## What Was Never Tested?

These parts of the original chain have not been tested as QFUDS physics:

1. information compression as the actual dark-sector source;
2. black holes as phase-boundary conditions for a dark-sector transition;
3. white-hole or remnant channels as a stress-energy source for phase B;
4. quantum foam as a microscopic medium with a derived action or stress tensor;
5. dynamic equilibrium as a state equation that generates `Q(z)`;
6. a physical explanation for why the interaction feature should peak near
   `z ~= 2`;
7. CMB, matter-power, BAO, supernova, DESI, Euclid, Roman, or likelihood-level
   viability of a physical QFUDS branch.

## Was `Gamma(a)` Only A First Prototype?

Yes.

Retained `Gamma(a)` was the first prototype implementation of the broader
intuition, not the full hypothesis. It encoded one candidate story:

```text
structure collapse / information production
-> phase-A to phase-B transfer timing
```

That prototype lost as physical QFUDS. It also lost, in the current digitized
compression output, as the best compression family. Those failures do not prove
that the original dynamic-equilibrium intuition is false. They prove only that
the implemented retained source relation and retained timing shape do not carry
the stronger claims.

## Dynamic-Equilibrium Candidate

A Dynamic-Equilibrium QFUDS hypothesis should be separated from retained
`Gamma(a)`. It is not yet a current branch.

To become testable, it would need at minimum:

1. a state variable or source scalar `X(a)` that represents the equilibrium
   shift;
2. a derived transfer relation `Q^nu[X,...]`;
3. a reason phase B has `w ~= -1` rather than radiation, heat, compact remnants,
   or ordinary fluid pressure;
4. a perturbation route for `delta Q`;
5. a prediction for the timing, sign, and amplitude of `Q(z)` before fitting
   data;
6. a declared failure criterion;
7. a known-model distinction from LCDM, unified dark fluid, interacting vacuum,
   IDE, holographic dark energy, black-hole-coupled dark energy, and remnant
   dark matter.

Until those exist, dynamic equilibrium is:

```text
still open but unsupported;
blocked until X, Q^nu, delta Q, or physical source exists.
```

## Strongest Statement Today

The strongest statement supported by the repository today is:

```text
QFUDS has not been validated as physical theory. The retained branch is
phenomenological interacting-vacuum / time-dependent IDE, but the original
structure-era timing intuition remains alive as a weak, non-physical timing
feature: retained timing peaks near z ~= 2 and captures part of a high-z
structure-era component, though current table-level and digitized evidence do
not make it an informative or optimal prior.
```

## Strongest Statement We Cannot Make

The repository still cannot say:

```text
information compression, black holes, quantum foam, or dynamic equilibrium
physically causes the observed dark-sector interaction timing.
```

It also cannot say:

```text
QFUDS is novel, physically derived, perturbatively complete, CMB viable,
matter-power viable, DESI/Euclid/Roman viable, or observationally preferred.
```

## Project Convergence Arc (2026-06-08 to 2026-06-12)

This section records the higher-altitude arc of the project so the survival map
above is read in context. It is narrative, not a status authority. Current
status lives only in
[000_roadmap.md](../05_next_steps/000_roadmap.md).

### Timeline

The repository spans about five days.

```text
2026-06-08 Mon  repository opens; prose theory, origin trail, v0.1-v0.3 notes
2026-06-09 Tue  background validation and verification-record hardening
2026-06-10 Wed  Source-X audit opens; black-hole lane, literature cache
2026-06-11 Thu  040 data-product audit -> 043 extraction -> 046 Chen Figure 5
                digitization -> 047 Gamma shape comparison -> 048 known-model
                distinction -> 049 eligibility review and observer mode
2026-06-12 Fri  050 foam-sector-to-Gamma forward-route feasibility result:
                minimum mathematical objects missing, no Level 2B opening
```

The Source-X `040-050` sprint, from data-product audit to the known-model
distinction, observer-mode routing, and forward-route feasibility closeout,
landed across two days.

### Methodology arc

The discipline level rose in four stages, independent of the physics content:

1. Prose theory and origin trail. The idea is held in words only, with no
   verification device.
2. Experiments and results (`exp_000` to `exp_006`). The idea is forced into a
   LCDM null limit, a transfer scan, a physicality gate, an entropy gate, a
   perturbation closure, and a model-family positioning. This is where retained
   `Gamma(a)` was demoted from physics to phenomenological interacting vacuum.
3. Governance and SSOT. The roadmap becomes the single status authority,
   frontmatter and validation scripts are added, and the repository starts
   policing its own over-claims.
4. Source-X investigation. The chain hunts for a physical source `X` (black-hole
   entropy history, Chen merger entropy) that could ground retained `Gamma(a)`,
   and ends at a numeric comparator with no admitted physical source.

### Source-X outcome (040-050)

The Source-X chain did not break `data_product_blocked`. It moved the blocker
forward and made it precise:

```text
literature exists
-> manual structured extract exists (043)
-> Chen Figure 5 numeric digitization exists (046)
-> qualitative Gamma shape comparison done (047); red entropy density is the
   closest timing comparator, but peaks earlier and has a shorter tail
-> known-model distinction blocked (048); the lane is not distinguished from
   entropy-DE, horizon entropy, black-hole-entropy DE, CCBH, IV/IDE, running
   vacuum, emergent DE, or structure-activation families
-> Level 2B ineligible; routed to observer mode (049)
-> forward foam-sector route audited (050); no state variable, calculable phase
   definitions, replacement transition object, or foam-sector equation set yet
```

See the
[Known-Model Distinction Audit Result](../wiki/research/investigations/source_x/conclusions/048_known_model_distinction_audit_result.md),
[Level 2B Admission Eligibility Review and Observer-Mode Routing](../wiki/research/investigations/source_x/conclusions/049_level2b_eligibility_review_and_observer_mode.md),
and the
[Foam-Sector-to-Gamma Derivation Feasibility Result](../wiki/research/investigations/source_x/conclusions/050_foam_sector_to_gamma_derivation_feasibility_result.md).

### Reading of the outcome

The result is best read as audit success, not model success or model failure:

```text
not QFUDS success
not QFUDS failure
QFUDS audit success
```

What the five days bought is a precise location of the idea: where it overlaps
already-researched territory, how much is reducible to existing families, and
where the unsolved-physics boundary begins. The five blocked admission items
(`X`, `Q^nu`, phase-B `w ~= -1` rationale, `delta Q`, known-model distinction)
are close to open problems of modern cosmology, so the lane reached a real
research frontier rather than a self-made wall.

The single most accurate closing sentence for the `040-049` chain is:

> The intuition that an important transition sat near the structure-formation
> era (`z ~= 2`) is retained, but its explanatory candidates already exist as
> several research lines (CCBH, entropic DE, IDE, running vacuum, emergent DE),
> and current evidence cannot select one of them or assert new physics.

The single most accurate closing sentence after `050` is:

> The original foam-sector direction remains the right form of the question,
> but current repository evidence cannot yet attempt that derivation because the
> minimum mathematical objects have not been supplied.

The original divergence (Landauer, white holes, foam) narrowed to one surviving
question that the major surveys and competing dark-energy programs are already
working on: why did something transition near cosmic high noon? That is the
basis for the observer-mode posture recorded in `049`.

## Handoff Rule

Future work should not rescue retained `Gamma(a)` by wording. If the original
intuition is continued, it should be continued as a new Dynamic-Equilibrium
candidate with its own `X`, `Q^nu`, phase-B rationale, `delta Q`, known-model
comparison, and failure criteria. Retained `Gamma(a)` may be referenced as the
first prototype that clarified what failed and what timing feature remained.
