# Quantum Foam Unified Dark Sector (QFUDS)

Language: English | [Korean](docs/00_project/qfuds_ko.md)

## What if dark matter, dark energy, and information circulation could be tied together?

### Abstract

This repository explores whether dark matter and dark energy could appear as two macroscopic phases of the same microscopic quantum-spacetime foam sector. In standard LCDM, dark matter and dark energy are treated as separate components. QFUDS asks whether both phenomena could instead be different large-scale appearances of one quantum foam medium.

Analogy: water can appear as ice, liquid water, or vapor depending on conditions. QFUDS asks a similar question about the dark sector. Can one underlying medium look like matter under one condition and like vacuum pressure under another?

In this picture, the clustering phase must behave like an almost pressureless component with $w \simeq 0$ and $c_s^2 \simeq 0$. That is how it can participate in structure formation like cold dark matter. The residual phase must behave like a slow vacuum-pressure component with $w \simeq -1$, explaining cosmic acceleration. Black holes are treated as local information-compression nodes, while black/white-hole remnants are kept only as secondary topological-defect candidates inside the same foam sector.

The model preserves the Friedmann background dynamics of general relativity. Instead, it asks whether QFUDS can produce signals that differ from LCDM in dark-energy evolution, small-scale galaxy halo structure, dark-sector clustering, or late-time information correlations associated with black-hole evaporation.

This project is not a complete physical theory. It is a research program and a testable toy framework. The goal is to put the hypothesis under real tests and turn it into falsifiable predictions that can be checked against the cosmic microwave background (CMB), large-scale structure, galaxy halo profiles, dark matter detection experiments, and precision measurements of the dark-energy equation of state.

### Basic Variables

The equation-of-state variable $w$ is pressure divided by energy density. If $w \simeq 0$, the component dilutes like matter. If $w \simeq -1$, it behaves like dark energy.

The effective sound speed $c_s^2$ measures how strongly the effective medium resists clumping. QFUDS survives only if the clustering phase has $c_s^2 \simeq 0$.

Analogy: sand can pile up into a mound, but a stretched trampoline pushes back when pressed. During galaxy formation, a dark-matter-like component must behave more like sand than like a trampoline.

### Core Hypothesis

Dark matter and dark energy may not be fundamentally separate substances.
They may be two macroscopic phases of the same microscopic quantum-spacetime foam.

```text
dark matter  -> clustering foam phase
dark energy  -> residual vacuum-pressure phase
remnants     -> optional defects in the same foam sector
```

Put more simply:

```text
dark matter + dark energy
= two effective phases of quantum spacetime foam
```

Black holes and white-hole-like remnants are secondary. They may be read as information-compression nodes or topological defects, but under the current standard they are far from the core and are not the main topic.

## Why I Came Up With The Hypothesis

### From Information Erasure To A Testable Model

Quantum Foam Unified Dark Sector (QFUDS) started as a toy-framework repository while I was thinking about dark matter, dark energy, and information flow in cosmology.

I wanted to know how far the idea could stay coherent.

I wanted to turn curiosity into equations, constraints, toy code, and falsifiable questions, then actually test the hypothesis.

I read a piece about information thermodynamics.

```text
Original:
Physics has shown that erasing memory necessarily produces heat.
This is the principle proposed by physicist Rolf Landauer. Computation or information generation itself does not necessarily consume energy, but erasing or forgetting one bit of information necessarily releases a certain amount of heat energy into the surroundings.
In other words, the human brain and a hard disk both increase the entropy of the universe and produce physical heat when they "forget" something. Information may not have mass, but information erasure has a thermodynamic price.
The seemingly vague act of "forgetting" is actually paid to the universe as heat and recorded in its bookkeeping.
This is a neuroscience story, a story about the limits of computers, and also a cosmology story.
```

Analogy: deleting a file does not make a laptop ignore physics. The machine still uses energy and releases heat. Landauer's principle says that, even in the ideal limit, erasing information has a minimum thermodynamic cost. The longer raw trail is not repeated here; it is preserved in [concept_origin.md](docs/01_origin/concept_origin.md).

That immediately led me to the black-hole question.
If information has a physical cost, a black hole cannot be treated as a simple trash can for information.
The next questions are where the information is encoded, whether Hawking radiation can return it in scrambled form, and whether, from the perspective of quantum-mechanical unitarity, the obstacle is not information destruction but decoding complexity.

The first thought flow was not a proof. The question moved roughly like this:

```text
information erasure has a heat cost
-> this has the same shape as the black-hole information-loss problem
-> Hawking radiation may carry scrambled information
-> recovery is possible in principle but blocked by decoding cost
-> if recovery is possible, ask about the reverse process
-> the reverse process suggests time reversal, CPT, or a white-hole-like counterpart
-> black/white-hole remnants suggest an information-storage sector
-> vacuum or spacetime foam becomes a candidate medium
-> dark matter may be a clustering foam mode
-> dark energy may be residual foam pressure
-> QFUDS: a unified dark-sector toy model
```

The white-hole/reverse-process question was interesting, but beyond a science-fiction-like spark it was too broad and verbose to become a scientifically strict claim.

After checking the branches one by one, the idea converged to one question.

```text
Can one dark sector behave simultaneously
as a clustering component and as a residual vacuum-pressure component?
```

The next validation question moved to $\Gamma(a)$.
If the clustering foam phase transfers into the residual vacuum-pressure phase, can that phase-transfer rate be tied to physical quantities such as structure growth, black-hole entropy, horizon entropy, star formation, or remnant statistics?

Analogy: this is like two water tanks connected by a valve. One tank is the clustering component, and the other is the residual vacuum-pressure component. $\Gamma(a)$ is the valve rule. If the valve is adjusted arbitrarily, that is just tuning. If the valve rule comes from a physical source, it can be tested.

### Divergence, Convergence, Verification

The QFUDS concept came out of repeated dialogue between me and GPT.

```text
raw question
-> explanation
-> follow-up question
-> counterexample or physical constraint
-> broader speculation
-> pruning
-> toy model
-> hostile review
-> code and outputs in this repository
```

In the divergence phase, the idea expanded outward through Landauer, black-hole information, Hawking radiation, Page curve, island ideas, reverse processes, white holes, quantum foam, dark matter, dark energy, the cosmological constant, and worldbuilding.

In the convergence phase, only one repeated question remained.

```text
Can dark matter and dark energy
be treated as two effective modes of the same quantum foam medium?
```

In the verification phase, I stripped away metaphor and placed the idea in front of ordinary cosmology checks.

```text
Does it recover LCDM in the zero-deviation limit?
Can the clustering phase keep c_s^2 near zero?
Does it preserve CMB acoustic peaks?
Does it preserve the matter power spectrum?
Can it produce realistic galaxy halos?
Does the remnant sector pass compact-object constraints?
```

### Pruned Or Preserved Branches

The raw idea mixed several branches.

```text
black holes as information processors
white-hole-like reverse channels
the universe as a white-hole-like release
vacuum fluctuations as sparse dark structure
cosmic acceleration as residual vacuum pressure
```

This repository keeps only the branches that can be turned into variables, equations, and tests. The current research version is this question:

```text
Can a quantum foam unified dark sector
reproduce the observed effects normally explained by dark matter and dark energy?
```

The standard is simple.

```text
Can this idea be made precise enough to be wrong?
```

The detailed raw trail is not repeated in this overview. The source record is preserved in [concept_origin.md](docs/01_origin/concept_origin.md).

## Research Program

I implemented this because I wanted to see how far an initially playful hypothesis could stay coherent.

```text
intuition
-> pruning
-> hypothesis
-> toy equations
-> kill criteria
-> code and future Boltzmann-code validation
```

The goal is not to prove QFUDS.
The goal is to find the first constraint that kills the model, or to narrow any surviving version enough to compare it with LCDM, unified dark fluids, interacting dark energy, scalar-field dark matter, and black/white-hole remnant models.

### Key Documents

- Current status and per-stage progress: [Roadmap](docs/05_next_steps/000_roadmap.md)
- Decision reasons: [Decision Log](docs/00_project/decision_log.md)

Until the model survives CMB and structure-formation tests, it should not be read as a strong physical claim.

The validation order is:

```text
literature position
-> background-universe validation
-> phase-transfer physicality
-> phenomenological perturbation closure
-> physical perturbation equations
-> CLASS or CAMB integration
-> CMB comparison
-> matter-power comparison
-> DESI / Euclid / Roman constraints
```

Analogy: this is like testing a bridge in stages.
A small desktop model can reject a bad design, but it does not prove that the real bridge survives wind, traffic, and earthquakes.
Background-level experiments can reject bad transfer laws, but they cannot claim CMB or structure-formation viability.

### Current Working Hypothesis: Two-Phase Transfer Model

```text
quantum foam unified dark sector with near-zero sound speed
```

The safer formulation is a unified dark sector inside ordinary general relativity.

$$
\rho_{\rm dark} = \rho_{\rm QF} + \rho_{\rm rem}
$$

$\rho_{\rm QF}$ is a quantum foam unified dark fluid. It has two effective pieces.

$$
\rho_{\rm QF}(a) = \rho_{\rm cluster}(a) + \rho_{\rm residual}(a)
$$

The clustering piece must behave like cold dark matter.

$$
\rho_{\rm cluster} \propto a^{-3}, \qquad
w \simeq 0, \qquad
c_s^2 \simeq 0
$$

The residual piece must behave like dark energy.

$$
\rho_{\rm residual} \simeq \rho_\star, \qquad
w \simeq -1
$$

The optional remnant piece is written as:

$$
\rho_{\rm rem} = \int M f(M)\,dM
$$

Experiment 001 adds a phase-transfer rate between the clustering phase and the residual phase.

$$
\frac{d\rho_A}{d\ln a} + 3\rho_A = -\Gamma(a)\rho_A
$$

$$
\frac{d\rho_B}{d\ln a} = \Gamma(a)\rho_A
$$

The current test is whether $\Gamma(a)$ can be tied to a physical proxy instead of being a hand-fit function.
Useful validation directions are low-redshift collapse, black-hole entropy, and star-formation proxies.
Constant transfer or ungated growth-based transfer will either fail early or return to ordinary interacting-dark-energy behavior.

Analogy: this is like two connected water tanks. One tank is the clustering phase, and the other is the residual phase. $\Gamma(a)$ is the valve rule. If the valve rule is set arbitrarily, it is just tuning. If the valve rule comes from a physical source, it can be tested.

The remnant term should remain secondary until its mass distribution passes microlensing, CMB, and structure-formation constraints.

### Core Survival Condition

The most important condition is the effective sound speed.

$$
c_s^2 \simeq 0
$$

In plain language:

```text
QFUDS foam may leave pressure that pushes the background universe apart,
but during galaxy formation it must clump like pressureless dust.
```

If the foam is too stiff, pressure erases structure. Then the model dies immediately.

Analogy: dry sand can be piled into a mound. But if you try to make the same mound with an elastic rubber sheet, it keeps pushing back and flattening out. The clustering phase must be sand-like enough for galaxies to form.

### Problems This Model Tries To Address

This model tries to connect three ideas.

1. Unified dark sector: can dark matter and dark energy share the same origin?
2. Coincidence problem: why are the dark matter and dark energy densities comparable in the current universe?
3. Dynamic vacuum energy: can the cosmological constant be a slowly relaxing equilibrium value rather than a fixed number inserted by hand?

### Possible Phenomena If The Model Works

The following are not verified predictions. They are places where the model can be killed.

1. Standard WIMP direct detection may continue to return null results.
2. Dark energy may show small but nonzero time evolution.

$$
w(a) = w_0 + w_a(1-a)
$$

In LCDM, $w_0=-1$ and $w_a=0$. For QFUDS to differ, it needs a small deviation with $w_0 \simeq -1$ and $|w_a|>0$.

3. Large-scale structure and the CMB must remain almost LCDM-like.
4. Small galaxy halos may prefer cores over sharp cusps, but this must be separated from baryonic feedback.
5. Dark matter structure and baryonic structure may show a slightly stronger correlation than in pure collisionless CDM.
6. In a complete quantum description, black-hole evaporation should not be exactly thermal.
7. If black/white-hole remnants exist, their allowed mass distribution must be narrow.

The core of the current test is not white holes.
What matters more is whether precision observations keep supporting $w=-1$, or move toward a small nonzero $w_a$.

### Kill Tests: First Attacks

A hostile reviewer should attack the model in this order.

1. Does it recover LCDM exactly in the zero-deviation limit?
2. Can the same effective medium produce $w \simeq 0$ and $w \simeq -1$ without hand-waving?
3. Why is $c_s^2$ near zero?
4. Does it preserve CMB acoustic peaks?
5. Does it preserve the matter power spectrum?
6. Is it better than existing unified dark fluid or k-essence models?
7. Does the remnant sector add real predictions, or only story language?

If these fail, QFUDS is only a vocabulary shift.

## Black Hole Interpretation: Re-reading, Not Evidence

Black holes are not central evidence for QFUDS.

The observational fact is:

```text
Most large galaxies host central supermassive black holes.
```

The Milky Way's central black hole and M87's black hole are representative examples. Their existence is observationally established. Their exact formation path is still being studied. Standard astrophysical explanations such as mergers, direct collapse, early massive seeds, accretion, and formation inside dark-matter halos still matter.

The conservative interpretation is:

```text
quantum foam -> dark halo -> galaxy -> central black hole
```

This respects the standard structure-formation picture better than saying that black holes create galaxies.

The stronger QFUDS question is:

```text
If dark matter is a foam phase,
could central black holes be special compression sites
or phase-transition sites inside that foam sector?
```

If interpreted from the QFUDS point of view:

```text
black hole = local information-compression node
```

More strongly:

```text
black hole = possible phase-transition site of the foam sector
```

Analogy: in a large city, a major data center may sit near routes where lots of data flows.
But the existence of that data center does not prove that the whole city was created by the network.
Likewise, a central black hole can be read in QFUDS language as a compression point or routing point, but it does not prove QFUDS and does not replace standard black-hole formation physics.

The safe statement is:

```text
QFUDS may reinterpret central black holes as information-compression nodes inside foam-dominated halos, but it does not yet explain why every large galaxy should have one.
```

### Documents

Documentation authority structure:

- [CLAUDE.md](CLAUDE.md) and [AGENTS.md](AGENTS.md) define agent behavior.
- [Roadmap](docs/05_next_steps/000_roadmap.md) is the single source of truth for current status, active gates, and blockers.
- [Decision Log](docs/00_project/decision_log.md) records decision reasons.
- [Experiments](docs/03_experiments/) and [Results](docs/04_results/) store evidence.

Maintained research documents:

- [PROJECT.md](PROJECT.md): documentation control and validation order
- [docs/README.md](docs/README.md): documentation index and folder map
- [overview.md](docs/00_project/overview.md): project goals, limits, and model genealogy
- [decision_log.md](docs/00_project/decision_log.md): chronological decision record with reasons and evidence
- [verification_guide.md](docs/00_project/verification_guide.md): how to rerun and read current validation
- [010_qfuds_v0_1.md](docs/02_theory/010_qfuds_v0_1.md): conceptual origin-stage theory note
- [015_qfuds_v0_15_phase_transfer_physics.md](docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md): phase-transfer physicality audit
- [020_qfuds_v0_2.md](docs/02_theory/020_qfuds_v0_2.md): minimal two-phase effective-fluid theory note
- [030_qfuds_v0_3.md](docs/02_theory/030_qfuds_v0_3.md): physically labeled $\Gamma(a)$ transfer-law theory note
- [040_qfuds_phenomenological_perturbations.md](docs/02_theory/040_qfuds_phenomenological_perturbations.md): phenomenological perturbation closure theory note
- [000_exp_000_lcdm_baseline.md](docs/03_experiments/000_exp_000_lcdm_baseline.md): zero-transfer LCDM control run
- [010_exp_001_gamma_scan.md](docs/03_experiments/010_exp_001_gamma_scan.md): transfer-law scan
- [015_exp_001_5_phase_transfer_physicality.md](docs/03_experiments/015_exp_001_5_phase_transfer_physicality.md): physicality gate
- [020_exp_002_entropy_information_gate.md](docs/03_experiments/020_exp_002_entropy_information_gate.md): entropy/information-source gate
- [030_exp_003_phenomenological_perturbation_closure.md](docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md): perturbation-closure audit
- [000_result_000_lcdm_baseline.md](docs/04_results/000_result_000_lcdm_baseline.md): zero-transfer baseline result
- [010_result_001_gamma_scan.md](docs/04_results/010_result_001_gamma_scan.md): result interpretation and next target
- [015_result_001_5_phase_transfer_physicality.md](docs/04_results/015_result_001_5_phase_transfer_physicality.md): physicality result
- [020_result_002_entropy_information_gate.md](docs/04_results/020_result_002_entropy_information_gate.md): entropy/information-source provenance result
- [030_result_003_phenomenological_perturbation_closure.md](docs/04_results/030_result_003_phenomenological_perturbation_closure.md): perturbation-closure result
- [000_roadmap.md](docs/05_next_steps/000_roadmap.md): validation stages, status, and blockers
- [010_perturbation_gate.md](docs/05_next_steps/010_perturbation_gate.md): perturbation gate

History/source notes:

- [concept_origin.md](docs/01_origin/concept_origin.md): how the raw information-flow idea became the QFUDS question
- [qfuds_ko.md](docs/00_project/qfuds_ko.md): Korean version of this document
- [research_program.md](docs/00_project/research_program.md): abstract, validation roadmap, and kill criteria
- [900_qfuds_research_report.md](docs/02_theory/900_qfuds_research_report.md): adversarial literature comparison and mathematical formulation

### Repository Checks

Validate document frontmatter and cross-links.

```bash
python3 scripts/validate_docs.py        # or: make validate
```

Check repository status-authority consistency.

```bash
python3 scripts/research_consistency.py  # or: make research-audit
```

Run the full preflight audit before major experiment milestones.

```bash
make preflight
```

Run the experiment 004 preflight gate.

```bash
python3 scripts/preflight_exp004.py
```

This gate is documented in [020_exp004_preflight_gate.md](docs/05_next_steps/020_exp004_preflight_gate.md) and can also be run with `make preflight-exp004`.

### Reference Literature

The links below anchor nearby research directions. They do not prove QFUDS.

- [Hawking evaporation and the Landauer Principle](https://arxiv.org/abs/2407.08777)
- [Entanglement Wedge Reconstruction and the Information Paradox](https://arxiv.org/abs/1905.08255)
- [Replica wormholes and the black hole interior](https://arxiv.org/abs/1911.11977)
- [Black hole fireworks: black-to-white-hole tunneling](https://arxiv.org/abs/1407.0989)
- [Small black/white hole stability and dark matter](https://arxiv.org/abs/1805.03872)
- [Planck 2018 cosmological parameters](https://arxiv.org/abs/1807.06209)
- [DESI DR2 results guide](https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/)
- [Unified dark fluid with null sound speed](https://arxiv.org/abs/2509.16155)
