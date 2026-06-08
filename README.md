# Quantum Foam Unified Dark Sector (QFUDS)

Language: [English](#quantum-foam-unified-dark-sector-qfuds) | [Korean](docs/qfuds_ko.md)

## Title

Quantum Foam Unified Dark Sector (QFUDS):  
A Speculative Framework for Dark Matter, Dark Energy, and Information Cycling

## Abstract

This repository explores a speculative cosmological framework in which dark matter and dark energy emerge as two macroscopic phases of a common microscopic quantum-spacetime foam sector. In contrast to the standard LCDM paradigm, where dark matter and dark energy are treated as distinct components, QFUDS asks whether both phenomena could arise from different infrared manifestations of a single quantum foam medium.

In this framework, the clustering phase behaves as an effectively pressureless component characterized by `w ~= 0` and `c_s^2 ~= 0`, reproducing the large-scale structure formation normally attributed to cold dark matter. The residual phase behaves as a slowly relaxing vacuum-pressure component with `w ~= -1`, providing an effective description of cosmic acceleration. Black holes are treated as local information-compression nodes, while black/white-hole remnants, motivated by loop quantum gravity tunneling scenarios, remain subdominant topological-defect candidates within the same foam sector.

The model preserves the Friedmann background dynamics of general relativity while suggesting possible deviations from LCDM in the evolution of dark energy, small-scale halo structure, dark-sector clustering behavior, and late-time information correlations associated with black-hole evaporation.

This work should be read as a research program and toy framework, not as a complete physical theory. The primary objective is to turn the original intuition into falsifiable predictions that can be tested against CMB observations, large-scale structure surveys, halo profiles, dark matter detection experiments, and future precision measurements of the dark-energy equation of state.

## Project Note

Quantum Foam Unified Dark Sector (QFUDS) is a speculative toy framework I started while thinking through dark matter, dark energy, and information flow in cosmology.

I did not start with a target theory. I was already interested in information, entropy, black holes, Hawking radiation, quantum mechanics, vacuum structure, and the dark sector. The useful part is the actual reasoning trail: I kept asking whether one topic was the same problem in another language, or whether it forced the next question.

This repository is not a claim that the model is correct. It is a workspace for turning curiosity into equations, constraints, toy code, and falsifiable questions. The writing assumes a technically comfortable reader, so it keeps terms like `unitarity`, `equation of state`, `sound speed`, `CMB`, and `matter power spectrum` when those terms carry the idea better than a softer paraphrase.

## How The Dialogue Became A Repository

QFUDS came out of an iterative dialogue with GPT. The process was not a one-shot prompt that produced a finished theory. It was closer to a technical back-and-forth:

```text
raw question
-> explanation
-> follow-up question
-> counterexample or physical constraint
-> broader speculation
-> pruning
-> toy model
-> adversarial review
-> code and outputs in this repository
```

I used the dialogue to externalize and test the reasoning. First, I pushed the idea outward: Landauer, black-hole information, Hawking radiation, Page curve, islands, reverse process, white holes, quantum foam, dark matter, dark energy, cosmological constant, and SF worldbuilding. Then I pulled it back inward: which part can survive contact with equations?

That pruning changed the center of the project. The early image was:

```text
the universe may be white-hole-like
```

The research version became:

```text
can one dark sector behave as both
a clustering component and a residual vacuum-pressure component?
```

The first adversarial result was useful precisely because it did not flatter the idea. The conservative version either reduces to LCDM or becomes a known interacting/unified dark-sector model. That moved the next question to `Gamma(a)`: if a clustering foam phase transfers into a residual vacuum-pressure phase, can that phase-transfer rate be tied to a physical quantity such as structure growth, black-hole entropy, horizon entropy, star formation, or remnant statistics?

This is why the repository exists. It records the shift from conversational idea expansion to thought experiment, then to a minimal falsifiable model.

## Origin: From Information Erasure To QFUDS

QFUDS did not start as a polished theory. I started from a simple information-thermodynamics trigger:

```text
Erasing information is not free.
Deleting one bit has a minimum thermodynamic cost.
That cost appears as heat in the universe's entropy bookkeeping.
```

My first reaction was not "this gives me a cosmology model." It was closer to:

```text
If erasing information has a thermodynamic cost,
isn't this related to the black-hole information-loss problem?
```

That was the first jump. Landauer made the question about information physical enough to connect to black holes. A black hole is exactly where information, entropy, quantum mechanics, and gravity collide.

From there I asked the next question directly: if information entering a black hole is not simply lost, where is it encoded, and can Hawking radiation return it in a scrambled form? If unitarity says recovery is possible in principle, is the real obstruction destruction, or decoding complexity?

That gave me the raw thought chain. It was not a linear proof. It was a sequence of question jumps:

```text
Landauer: erasing information costs heat
-> black-hole information loss has the same shape
-> Hawking radiation may carry scrambled information
-> recovery is allowed in principle but blocked by decoding cost
-> if recovery exists, ask about a reverse process
-> reverse process suggests time reversal, CPT, or white-hole-like counterpart
-> black/white-hole remnants suggest an information-storage sector
-> vacuum or spacetime foam becomes a candidate medium
-> dark matter may be a clustering foam mode
-> dark energy may be a residual foam pressure
-> QFUDS: a unified dark sector toy model
```

At first, my image was much larger:

```text
What if the universe itself behaves like a giant white-hole-like release?
```

That image was useful as a spark, but it was too broad to be a good scientific claim. As I pruned it, the stronger center became narrower:

```text
Dark matter + dark energy
= two effective phases of quantum spacetime foam.
```

In this framing, dark matter is the clustering phase: the part that behaves almost like pressureless matter and helps form halos. Dark energy is the residual pressure phase: the smooth leftover vacuum behavior that drives accelerated expansion. I keep black holes and white-hole-like remnants as speculative information-flow structures or defect-like remnants, but they are secondary.

## Divergence, Convergence, Verification

The main artifact I want to preserve here is not only the hypothesis. It is the path that produced it: question, next question, branch, pruning, and then pressure from known cosmology.

The first phase was divergence. A small Landauer prompt made me branch into several connected questions. I kept asking whether the same structure was appearing again:

```text
If erased information leaves heat,
then information has physical cost.

If information has physical cost,
then black-hole evaporation cannot be only a disposal story.

If black holes process information,
then a reverse-process or delayed-return channel becomes natural to ask about.

If black holes and vacuum structure are part of one information problem,
then the dark sector might be a large-scale expression of that same structure.
```

That phase was intentionally loose, but the links were specific: black holes raised the information-storage question, Hawking radiation raised the decoding question, time reversal raised the white-hole/CPT question, and the failure to directly detect particle dark matter raised the "maybe this is a collective mode" question.

The important middle step was not simply "black hole, therefore white hole." My thought process passed through reversibility:

```text
If Hawking radiation carries information in a scrambled form,
could an ideal quantum decoder recover it?

If recovery is allowed by unitarity but blocked by complexity,
then the information is not destroyed. It is hidden behind decoding cost.

If a complete time-reversed process existed,
what would play that role physically?
```

That is where the reverse-process question entered for me. I did not treat white holes, black/white-hole remnants, CPT-like symmetry, and replica-wormhole/island ideas as proofs. I treated them as possible answers to a narrower question: if black-hole evaporation is unitary but hard to decode, what physical structure could act like a delayed return channel or information reservoir?

The dark-matter turn came from a separate but connected intuition:

```text
Maybe dark matter is not "matter" in the usual particle sense.
Maybe it is an energy-like collective excitation of vacuum or spacetime foam.
Maybe it is sparse because it comes from the structure of near-empty space,
not from ordinary particles moving through space.
```

The plasma-like language belongs here only as an analogy. I am not claiming dark matter is electromagnetic plasma. The point is collective behavior: a medium can have large-scale modes that are easier to see gravitationally than as individual particles.

The second phase was convergence. After the idea branched too far, I cut the broad image down until one question remained stronger than the rest:

```text
Can dark matter and dark energy be treated as two effective modes
of the same quantum-foam medium?
```

That question is smaller than the original image, but much harder to dodge. It forces the model to say how one sector can look dust-like on structure scales and vacuum-like on cosmic scales.

The third phase was verification pressure. Once I wrote the idea as a dark-sector toy model, it could no longer live on metaphor or aesthetic fit. It had to face ordinary cosmology:

```text
Does it recover LCDM in the zero-deviation limit?
Can the clustering phase keep c_s^2 ~= 0?
Does it preserve CMB acoustic peaks?
Does it preserve the matter power spectrum?
Can it produce realistic halos?
Does any remnant sector survive compact-object constraints?
```

This is why I made the repository. The work is not only to write the idea down. It is to push the idea from curiosity into a form that can be checked, constrained, or killed.

## What Was Pruned

The raw idea had several branches:

```text
black holes as information processors
white-hole-like reverse channels
the universe as a white-hole-like release
vacuum fluctuations as sparse dark structure
cosmic acceleration as residual vacuum pressure
```

This repo keeps the branches that can be translated into variables, equations, and tests. The current research version is not:

```text
The universe is literally a white hole.
```

The current research version is:

```text
Can a quantum-foam unified dark sector reproduce the observed behavior
normally attributed to dark matter and dark energy?
```

The standard here is simple:

```text
Can this be made precise enough to fail?
```

If the answer is no, the idea remains only a story. If the answer is yes, it becomes a toy framework that can be attacked by CMB data, structure formation, halo profiles, and dark-energy measurements.

## Why This Repository Exists

This repository records my move from idea burst to research program:

```text
intuition
-> pruning
-> hypothesis
-> toy equations
-> kill criteria
-> code and future Boltzmann tests
```

The goal is not to prove QFUDS. My goal is to identify the first constraint that kills it, or to make the surviving version narrow enough to compare with LCDM, unified dark fluids, k-essence, interacting dark energy, scalar-field dark matter, and black/white-hole remnant models.

Current status: the project has moved past the first toy-background model into a v0.3 background-transfer diagnostic pass. The repo now tests several physically motivated `Gamma(a)` phase-transfer laws and classifies which ones die immediately. Perturbation equations, CLASS/CAMB integration, CMB power-spectrum comparison, and matter-power comparison are still not complete.

## Current Validation Stage

The project is currently between Level 1 and Level 2: the background model exists, and v0.3 now tests candidate phase-transfer laws, but perturbations are still incomplete.

```text
Level 0: literature position       done in draft form
Level 1: background toy model      implemented
Level 1.5: Gamma(a) transfer laws  v0.3 diagnostic pass complete
Level 2: perturbation equations    not complete
Level 3: CLASS or CAMB integration not started
Level 4: CMB comparison            not started
Level 5: matter power comparison   not started
Level 6: DESI/Euclid/Roman tests   not started
```

QFUDS becomes interesting only after it survives the next numerical checks. v0.3 is still background-level work: it can reject bad transfer laws, but it cannot claim CMB or structure-formation viability yet.

## One-Sentence Thesis

Dark matter and dark energy may not be fundamentally separate substances. They may be two macroscopic phases of the same microscopic quantum-spacetime foam.

```text
dark matter  -> clustering foam phase
dark energy  -> residual vacuum-pressure phase
remnants     -> optional defects in the same foam sector
```

The strongest version of the idea is not "the universe is a white hole." That is too large and too easy to attack.

The stronger version is:

```text
Dark matter + dark energy
= two effective phases of quantum spacetime foam.
```

Black holes and white-hole-like remnants are secondary. They may act as information-compression nodes or topological defects, but they are not the main engine of the model.

## The Thought Flow

The idea started from information, not from dark matter.

```text
Information is physical.
If information cannot simply disappear, what does a black hole do with it?
If a black hole has a time-reversed counterpart, could there be a delayed return channel?
If vacuum foam stores or mediates information, could the dark sector be a large-scale equilibrium of that foam?
```

That produced the first conceptual chain:

```text
information conservation
-> black-hole information problem
-> white-hole-like return channel
-> quantum foam as a medium
-> dark matter as a clustering foam mode
-> dark energy as residual foam pressure
-> black/white-hole remnants as optional defects
```

The jumps are not meant to be proofs. They are changes in the question being asked:

```text
Landauer:
information has physical cost

black-hole information:
if information enters a black hole, where is it encoded?

white-hole-like return:
if black holes have a time-reversed mathematical counterpart,
can the return channel be modeled at least as a remnant or defect?

quantum foam:
if spacetime itself fluctuates microscopically,
could that be the medium carrying the effective dark-sector behavior?

dark matter:
can one long-wavelength foam mode clump with w ~= 0 and c_s^2 ~= 0?

dark energy:
can another large-scale foam mode remain smooth with w ~= -1?

QFUDS:
can both be treated as two effective phases of one dark sector?
```

After pruning the more speculative parts, the useful research question became narrower:

```text
If quantum foam behaves like an effective cosmic medium,
what observational constraint kills it first?
```

## Current Working Hypothesis: The v0.3 Model

The safer formulation is a unified dark sector inside ordinary general relativity.

```text
rho_dark = rho_QF + rho_rem
```

`rho_QF` is a quantum-foam unified dark fluid. It has two effective pieces:

```text
rho_QF(a) = rho_cluster(a) + rho_residual(a)
```

The clustering piece must behave like cold dark matter:

```text
rho_cluster ~ a^-3
w ~= 0
c_s^2 ~= 0
```

The residual piece must behave like dark energy:

```text
rho_residual ~= rho_*
w ~= -1
```

The optional remnant piece is written as:

```text
rho_rem = integral M f(M) dM
```

v0.3 adds a phase-transfer rate between the clustering phase and residual phase:

```text
d rho_A / d ln a + 3 rho_A = -Gamma(a) rho_A
d rho_B / d ln a           =  Gamma(a) rho_A
```

The current test is whether `Gamma(a)` can be tied to a physical proxy instead of being fitted by hand. The most useful toy directions so far are low-redshift collapse, black-hole-entropy, and star-formation proxies. Constant and ungated growth-driven transfer fail early or collapse back into ordinary interacting-dark-energy behavior.

It should stay subdominant unless its mass function survives microlensing, CMB, and structure-formation constraints.

## The Key Survival Condition

The most important condition is the effective sound speed.

```text
c_s^2 ~= 0
```

Plain language:

```text
QFUDS foam may leave a pressure that pushes the universe apart,
but during galaxy formation it must still clump almost like pressureless dust.
```

If the foam is too stiff, pressure erases structure. Then the model dies immediately.

## What The Model Tries To Explain

The model tries to connect three strong ideas:

- Unified dark sector: dark matter and dark energy may share one origin.
- Coincidence problem: the dark matter and dark energy densities are comparable near the present epoch.
- Dynamic vacuum energy: the cosmological constant may be a slowly relaxing equilibrium value, not a fixed number placed by hand.

It does not try to replace general relativity at this stage. The Friedmann background is kept.

## Prediction Candidates

These are not verified predictions. They are places where the model can be killed.

1. Standard WIMP direct detection may keep returning null results.
2. Dark energy may show a small but nonzero time evolution.

```text
w(a) = w_0 + w_a(1 - a)
LCDM:   w_0 = -1, w_a = 0
QFUDS: w_0 ~= -1, |w_a| > 0 but small
```

3. Large-scale structure and the CMB must remain almost LCDM-like.
4. Small galaxy halos may prefer cores over sharp cusps, but this must be separated from baryonic feedback.
5. Dark matter and baryonic structure may show a slightly tighter relation than in pure collisionless CDM.
6. Black-hole evaporation should not be exactly thermal in the full quantum description.
7. If black/white-hole remnants exist, the allowed mass function must be narrow.

The hottest near-term test is probably not white holes. It is whether precision surveys keep supporting `w = -1` or move toward a small nonzero `w_a`.

## First Attacks

A hostile reviewer should attack the model in this order:

1. Can it recover LCDM exactly in the zero-deviation limit?
2. Can the same effective medium produce `w ~= 0` and `w ~= -1` without hand-waving?
3. Why is `c_s^2` near zero?
4. Does it preserve the CMB acoustic peaks?
5. Does it preserve the matter power spectrum?
6. Does it improve anything beyond existing unified dark fluid or k-essence models?
7. Does the remnant sector add real predictions, or only story language?

If these fail, the model is only a vocabulary shift.

## Notes For Non-Scientists

Plain-language notes for the technical terms above:

```text
Information erasure:
Deleting a bit is not just "forgetting." It leaves a heat/entropy cost in
the universe's bookkeeping.

Hawking radiation:
Black holes may leak energy, and possibly information, in an extremely
scrambled form.

Quantum foam:
A speculative picture in which spacetime is not perfectly smooth at the
smallest scales, but has microscopic fluctuations.

Dark matter mode:
The part of the foam that would clump like a wave or medium around galaxies.

Dark energy mode:
The smooth leftover pressure of the same sector, pushing cosmic expansion.

Sound speed:
How stiff the effective medium is. If it is too stiff, it cannot clump into
galaxy halos. QFUDS survives only if the clustering phase is almost dust-like.

White-hole remnant:
A speculative tiny leftover or defect-like object that might store or release
information. It is not established physics and is not the main claim.
```

## Black Holes In This Picture

Black holes are not the central proof of QFUDS.

Observational fact:

```text
Most large galaxies host central supermassive black holes.
```

Examples include the Milky Way's central black hole and the black hole in M87. Their existence is observationally established. Their exact formation route is still an active research question.

The conservative interpretation is:

```text
quantum foam -> dark halo -> galaxy -> central black hole
```

That respects the usual structure-formation picture better than saying black holes create galaxies.

The stronger but still speculative QFUDS question is:

```text
If dark matter is a foam phase,
could central black holes mark special compression or phase-transition sites
inside that foam sector?
```

The speculative QFUDS interpretation proposed by Dorito is:

```text
black hole = local information-compression node
```

or, more boldly:

```text
black hole = possible phase-transition site of the foam sector
```

This is a useful worldbuilding image and a possible research direction, but it is not yet an observational result.

The safe statement is:

```text
QFUDS may reinterpret central black holes as information-compression nodes
within foam-dominated halos, but it does not yet explain why every large
galaxy has one.
```

## Current Status

QFUDS is not a theory yet.

It is a speculative framework with a clearer center than the original white-hole-universe idea:

```text
quantum foam unified dark sector with near-zero sound speed
```

The current v0.3 step is a background-level `Gamma(a)` validation pass. The next meaningful step is not more story. It is perturbations and Boltzmann-code validation:

```text
background equation                    done
Gamma(a) transfer-law diagnostics       v0.3 done
-> perturbation equation
-> CLASS or CAMB implementation
-> CMB comparison
-> matter power spectrum comparison
-> DESI, Euclid, Roman constraints
```

The project becomes physically interesting only if the model survives the first CMB and structure-formation checks.

## Documents

Maintained research documentation:

- `docs/00_project_overview.md`: project goals, status, limitations, roadmap summary, and model genealogy
- `docs/02_theory/qfuds_v0_1.md`: conceptual origin-stage theory note
- `docs/02_theory/qfuds_v0_2.md`: minimal two-phase effective-fluid theory note
- `docs/02_theory/qfuds_v0_3.md`: physically labeled `Gamma(a)` transfer-law theory note
- `docs/03_experiments/exp_000_lcdm_baseline.md`: zero-transfer LCDM control run
- `docs/03_experiments/exp_001_gamma_scan_v03.md`: v0.3 transfer-law scan
- `docs/04_results/result_001_gamma_scan_v03.md`: result interpretation and next target
- `docs/decision_log.md`: chronological decisions with reasons and evidence
- `docs/05_next_steps/roadmap.md`: validation levels, status, and blockers

Historical/source notes:

- `docs/concept_origin.md`: how the raw information-flow idea became the QFUDS question
- `docs/qfuds_ko.md`: Korean explanation of the same origin, pruning, hypothesis, and validation path
- `docs/research_program.md`: abstract, validation roadmap, and kill criteria
- `docs/qfuds_research_report.md`: adversarial literature comparison and mathematical formulation
- `docs/qfuds_v0_3_gamma_laws.md`: v0.3 `Gamma(a)` transfer-law diagnostics and viability table

## Formal Reference Anchors

These links are anchors for the claims and nearby research directions. They do not prove QFUDS.

- [Hawking evaporation and the Landauer Principle](https://arxiv.org/abs/2407.08777)
- [Entanglement Wedge Reconstruction and the Information Paradox](https://arxiv.org/abs/1905.08255)
- [Replica wormholes and the black hole interior](https://arxiv.org/abs/1911.11977)
- [Black hole fireworks: black-to-white-hole tunneling](https://arxiv.org/abs/1407.0989)
- [Small black/white hole stability and dark matter](https://arxiv.org/abs/1805.03872)
- [Planck 2018 cosmological parameters](https://arxiv.org/abs/1807.06209)
- [DESI DR2 results guide](https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/)
- [Unified dark fluid with null sound speed](https://arxiv.org/abs/2509.16155)
