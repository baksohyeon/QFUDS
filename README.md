# Quantum Foam Unified Dark Sector (QFUDS)

Language: English | [Korean](docs/00_project/qfuds_ko.md)

## What if dark matter, dark energy, and information circulation could be tied together?

### Abstract

This repository explores whether dark matter (the unseen mass that makes up most of the universe's matter but gives off no light) and dark energy (the unknown energy driving the universe's accelerating expansion) could appear as two macroscopic phases of the same microscopic quantum-spacetime foam (a hypothetical medium in which spacetime froths at the tiniest scales). In standard LCDM (the current best-fit cosmological model), the two are treated as separate components. QFUDS asks whether both could instead be different large-scale appearances of one quantum foam medium.

Analogy: water can appear as ice, liquid water, or vapor depending on conditions. QFUDS asks a similar question about the dark sector. Can one underlying medium look like matter under one condition and like vacuum pressure under another?

In this picture, the clustering phase must behave like an almost pressureless component (equation of state $w \simeq 0$, effective sound speed $c_s^2 \simeq 0$). That is how it can join structure formation like cold dark matter. The residual phase would have to behave like a slow vacuum-pressure component ($w \simeq -1$) to account for cosmic acceleration. Black holes are not used as evidence for QFUDS. At most they are speculative QFUDS labels for local information-compression sites, while black/white-hole remnants stay secondary topological-defect candidates (loosely, flaws in the weave of spacetime) unless their dynamics and constraints are derived.

The model keeps the Friedmann background dynamics of general relativity (the standard equations for how the universe expands on average). It then asks whether QFUDS can produce signals that differ from LCDM in dark-energy evolution, small-scale galaxy halo structure (a halo is the clump of dark matter wrapping a galaxy), or dark-sector clustering. Any statement about black-hole evaporation is a quantum-gravity motivation, not a current observational test of this repository.

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

Black holes and white-hole-like remnants are secondary. They may be read in QFUDS language as information-compression nodes or topological defects, but this is speculative interpretation rather than established black-hole or galaxy-formation physics. Under the current standard they are far from the core and are not the main topic.

## How To Read This Repository: Two Phases, At Two Different Times

This project has two different layers, and it matters which one you are reading.
They were produced at different stages of the work and do not carry the same
evidential weight.

**Phase 1: the rigorous thread (the real experiments).** This is the part that was
put through explicit kill-gates: define a rule, test it, and reject the versions
that fail. Claims in this layer are backed by numbered experiments in
[docs/03_experiments/](docs/03_experiments/). The plain-language account ends at
[lineage 003](docs/wiki/lineage/003_research_flow_plain_language_ko.md), and it
corresponds to the `Gamma(a)` story below under
[The Main Thread](#the-main-thread-what-makes-gammaa-and-why-z2). If you only rely
on one part of this repository, rely on this layer. **The empirical record stops
at 003.**

**Phase 2: the rough push (exploratory sketches).** After the rigorous thread hit
its wall, I relaxed the standard and pushed one deliberately rough version as far
as it would go: a hand-drawn `tanh` transition checked across 24 checkpoints.
These are sketches, not validated results. The raw numerical work is collected in
[lineage/assets/](docs/wiki/lineage/assets/), and it is written up
phenomenologically in
[lineage 004](docs/wiki/lineage/004_rough_tanh_numerical_sketch_ko.md) and
[lineage 005](docs/wiki/lineage/005_rough_tanh_thesis_report_ko.md).
The [Where This Stands](#where-this-stands-what-pushing-the-idea-to-the-wall-found)
section just below is the honest report of how far that rough push reached. Read
it as an organized exploration by a non-specialist, not as proof.

In one line: **Phase 1 is what survived real tests (up to 003); Phase 2 is what
happened when I pushed a failing idea to its visible limits (004 to 005).**

## Where This Stands: What Pushing the Idea to the Wall Found

*Phase 2: the rough push. Phenomenological sketches (lineage 004 to 005), not
gated experiments.*

The conceptual program above is the starting point, not the result. The most
complete attempt so far took one concrete version: a rough `tanh`
equation-of-state transition for a unified dark sector (the equation of state $w$
slides smoothly along an S-shaped curve from one value to another). I pushed it
all the way to its limits across 24 atomic checkpoints. That record is the
[rough-`tanh` lineage report](docs/wiki/lineage/005_rough_tanh_thesis_report_ko.md)
(Korean). Its contribution is a systematic *map* of how far the idea reaches and
where it is blocked, not a discovery of new cosmology. The project is currently
in **observer mode** (no longer pushing new hypotheses, just waiting on external
observations); the single source of truth for status remains the
[Roadmap](docs/05_next_steps/000_roadmap.md).

![It works at the effective level: the V2 variant's background expansion and distance modulus track LCDM to within the Type Ia supernova scatter floor (±0.05 mag), while the fully unified V1 variant breaks at high redshift.](docs/wiki/lineage/assets/004_rough_tanh/fig_background.png)

The map reads on three levels:

- **Effective level: it works, but it does not win.** With ordinary matter held
  separate (variant V2), the background expansion is indistinguishable from LCDM
  in supernovae ($|\Delta\mu| < 0.02$ mag, within the brightness scatter of Type Ia
  supernovae), and a tiny effective sound speed ($c_{\rm eff}^2 \approx 3\times10^{-5}$, so small the
  dark sector barely spreads and mostly clumps) pulls the structure-growth
  amplitude $S_8$ down to the observed $S_8 \approx 0.76$. But this is not better than
  LCDM: the apparent fit win is just the generic effect of lowering $S_8$, it costs
  one more hand-tuned knob, and the $H_0$ tension (the roughly 8% disagreement between
  nearby and distant measures of the expansion rate) gets *worse*, not better.
- **Falsifiable level: where the science actually is.** Because it hides in the
  background, the model's only scientific value is where it *diverges* from LCDM.
  It leaves three clean falsifiable signatures: a scale-dependent step in the
  weak-lensing matter power spectrum (weak lensing reads the matter map from how
  foreground gravity bends the light of distant galaxies; the step sits at
  $k_J \approx 0.1\,\mathrm{Mpc}^{-1}$), a scale-dependent tilt in the late ISW signal (the faint
  energy shift CMB photons pick up while crossing large-scale structure), and a
  running growth index $\gamma_{\rm eff}(k)$ (the exponent for how fast structure grows). A
  representative Euclid-class tomographic forecast detects these at $\sim\!24\sigma$
  (statistically as good as certain), within reach of next-generation surveys.
- **Fundamental level: the ceiling.** Trying to *derive* the parameters the data
  wants from a microscopic foam structure fails. The data prefer a correlation
  length $\xi \approx 10$ Mpc (a large-scale-structure scale, not a microscopic foam
  scale) and a transition near a critical density $\rho_* \approx \rho_\Lambda$. Forcing these from
  a mechanism does not reduce the tuning; it relocates it, and the two numbers
  reduce to the **cosmological-constant problem** (why the vacuum energy is so
  absurdly small) and the **hierarchy/scale problem** (why this particular size).
  This ceiling is not a failure unique to this idea; it is the wall
  every dynamical-dark-energy model shares.

![The ceiling in one picture: the correlation length the data wants (ξ ≈ 9.5 Mpc) is natural to neither the microscopic foam scale nor the causal horizon, and the transition density sits inside the ~3-orders cosmic-coincidence window. In other words, the scale problem and the why-now problem.](docs/wiki/lineage/assets/004_rough_tanh/fig_cp20_ceiling_derivation.png)

Two findings survive as genuine, narrow gains rather than story language: a
tracker-attractor mechanism (any starting value gets pulled to the same outcome
over time) that removes about 15.7 decades (factors of ten, an enormous range) of
initial-condition tuning, the one real partial win, and the observation that three independent
"what did I miss?" intuitions each re-discovered, on their own, about 25 years of
existing literature (chameleon screening, LTB voids, Buchert averaging), which
corroborates that the ceiling is real rather than an artifact of one approach.

The exploration also used an agent-based operating procedure: workflow SSOT,
parallel work, adversarial review, and deterministic gates. The purpose was to
reduce the chance that an unsupported positive claim would pass unchecked while
the speculative branch was pushed to its recorded limit.

Every number above comes from a rough proxy; rigorous validation requires a
Boltzmann code (a full cosmology solver such as CLASS/hi_class) and is currently
blocked. Nothing here is a
confirmed physical claim. See the
[thesis-style report](docs/wiki/lineage/005_rough_tanh_thesis_report_ko.md) for
the full checkpoint-by-checkpoint record, and
[What We Actually Learned](docs/00_project/project_identity.md) for the standing
lessons.

## The Main Thread: What Makes Gamma(a), and Why z≈2?

*Phase 1: the rigorous thread. Every step below is a gated experiment in
[docs/03_experiments/](docs/03_experiments/), summarized in
[lineage 003](docs/wiki/lineage/003_research_flow_plain_language_ko.md). This is
the empirically grounded part of the project, and it came first.*

Before the rough-`tanh` story above, there was an earlier, main thread. It began
with the black-hole information paradox: *if information really isn't destroyed,
where does it go?* From there the chain ran, confidently, `Landauer ->
black-hole information -> white hole -> quantum foam -> dark matter / dark
energy`. To keep it from staying a daydream, I built a transfer function
`Gamma(a)` (a valve that sets how much of the clustering, dark-matter-like phase
converts into the leftover, dark-energy-like phase) and stacked experiments.

How it went:

- **exp_000**: confirm that `Gamma=0` returns to standard LCDM (control).
- **exp_001**: scan transfer laws; over-active or unconstrained ones die.
- **exp_001.5**: audit "does this come from a real physical source?" The retained
  `Gamma` fails physical derivation.
- **exp_002**: entropy/information as a source. Broad entropy language dies; the
  information-production shape survives only as provenance.
- **exp_003**: perturbation closure. P2 dies; only P1 survives, phenomenologically.
- **exp_004**: model genealogy. The decisive result: my P1 is not a new cosmology
  but a special case inside existing interacting-vacuum (IV) / interacting-dark-energy
  (IDE). Not "I built a new theory," but "it landed in a form comparable to known
  IDE/IV."
- **exp_005–006**: is my `Gamma` timing just a pretty curve, or a prior that
  compresses real IDE reconstructions? Answer: not a physical source, not a new
  model. But the retained `Gamma` peaks near z≈2, and IV/IDE reconstructions
  (Escamilla 2023; DESI DR2-era work like Li & Zhang 2025) keep showing a feature
  around z≈1–2. The data is wide and weak, so it is "allowed but not informative."

A digitized compression audit went further: my `Gamma` was not the optimal
compression family; simpler transition/Gaussian/pulse shapes fit the
reconstructions better. My implementation lost. Yet the *epoch* it pointed at,
z≈2, kept surviving.

Why z≈2? That is Cosmic Noon, when star formation, galaxy growth, quasars, and
black-hole growth all peak. The funny part: the literature also stops here. "There
is a feature; we do not know why." Standard LCDM sets the dark-matter-to-dark-energy
interaction to zero, so it never asks the question at all.

In plain terms: I first asked "why does ice cream sell more in summer? heat?
tourists? school break?" and found the field had already tried those (black-hole
entropy, CCBH, IDE). So I changed the angle: "maybe it is not any single cause,
but an index of the whole city's activity." Good angle. Then the next question
blocked me: **"what do you actually measure that city-wide activity with?"** Power
use? foot traffic? card spending? There was no number for it. I had the idea but
no thermometer.

That is exactly where QFUDS stands: not a stage of not knowing the candidate
cause, but a stage of **not yet having defined a state variable** (a measurable
quantity for that macroscopic state). This is, literally, a roadmap blocker: no
non-circular foam-sector state variable exists yet.

I started from the black-hole information paradox ("where does conserved
information go?"), and the question left at the end had the same shape: *when*
(z≈2) does the conserved thing flow, and *what measurable quantity* counts it? I
came back out the door I went in.

The honest bottom line: I have no answer yet. `Gamma(a)` was a first prototype,
not the whole hypothesis, and that prototype lost. What survives is the core
intuition that *structure-formation timing and dark-sector interaction timing may
be related.* The most striking part is that the question I happened to chase is
one nobody can cleanly answer yet. Status authority remains the
[Roadmap](docs/05_next_steps/000_roadmap.md); the project is in observer mode.
This demotion is not a falsification of the broad dark-matter-to-dark-energy
transition hypothesis, only the retirement of one mechanism meant to explain it.

## Afterword: A Grand-Sounding Theory That Converged on Two Open Problems

I proposed a grand-sounding theory, and after pushing it all the way through, it
converged onto two of modern physics' unsolved problems. The conclusion of these
few days, stated up front:

> **The two open problems**
> 1. **Why is the dark-energy scale exactly meV (a tiny energy unit, the
>    milli-electronvolt)?** This leads straight into the cosmological-constant
>    problem (why the vacuum energy is so absurdly small).
> 2. **Where should the vacuum-energy cutoff be set?** I reasoned from the quantum
>    side, but what distance scale does it actually require: the Planck scale
>    (impossibly small), the horizon scale (the size of the observable universe),
>    or the galaxy / cosmic-web scale?

I never reached the "why." Of course not: these two *are* modern physics' open
problems, which is exactly why none of this can be derived from first principles.

Here is how it went.

It started with a single question: *if information that falls into a black hole
really isn't destroyed, where does it end up?* That led to the idea that some
medium, vacuum or spacetime foam, might clump like dark matter under some
conditions and push the universe apart like dark energy under others, and I gave it a
suitably grand name: **QFUDS (Quantum Foam Unified Dark Sector)**. Just as water
appears as ice, liquid, or vapor depending on conditions, could one dark sector
look like a clustering phase ($w \approx 0$, $c_s^2 \approx 0$, so it joins structure
formation like cold dark matter) in one regime and a residual vacuum-pressure
phase ($w \approx -1$, so it drives acceleration) in another?

I hit the honest limit quickly: at best this is *phenomenological* (it fits the
data without explaining why), and it cannot be *derived* from first principles. It
was not even new: schools of thought with
a similar approach had already run the same calculation and stopped at the same
place. It was disappointing, but I reasoned that a scientist bound by rigor would
stop here, and that I was not, so I could push it through even if it became
unscientific. To get the properties a dynamical-dark-energy model needs, I
brute-forced a fit (just trying values until they land) toward the places where
the standard model is subtly off, watching the trends as I went.

And then an optimum actually appeared.

- **$c_{\rm eff}^2 \approx 4.6\times10^{-6}$**: the effective sound speed squared. In plain terms,
  the knob that sets how readily this dark sector spreads out versus how readily
  it clumps during structure formation.
- **correlation length $\xi \approx 9.5$–$10$ Mpc**: the effective distance over which its
  parts influence one another. Since 1 Mpc is about 3.26 million light-years,
  10 Mpc is not the inside of a single galaxy but the scale of the cosmic web,
  the realm of large-scale structure.

| Correlation length $\xi$ | $c_{\rm eff}^2$ | $S_8$ |
| --- | --- | --- |
| microscopic foam ($\xi \le 1$ Mpc) | $\to 0$ ($\le 5\times10^{-8}$) | **0.95 (too high)** |
| structure scale ($\xi \approx 10$ Mpc) | $\approx 5\times10^{-6}$ | 0.82 |
| **data fit ($c_{\rm eff}^2 = 4.6\times10^{-6}$)** | **$\to\ \xi \approx 9.5$ Mpc** | $\approx 0.78$–$0.82$ |
| Hubble ($\xi \approx c/H_0$) | $\approx 1$ | 0.68 (overshoot) |

![The moment it flipped: the correlation length that reproduces the observed S8 is ξ ≈ 10 Mpc (a large-scale-structure scale), not the microscopic foam scale I expected.](docs/wiki/lineage/assets/004_rough_tanh/fig_cp8_ceff2_derivation.png)

Cross-checking the literature, I found that the values I had brute-forced actually
matched the ones the field works with. It was an honor and a shock at once,
because what I had expected was the *very small, Planck-scale* unit of a "quantum
foam," and what the data pointed to was a scale beyond galaxies, in large-scale
structure. (None of this is a physical proof, of course; the two open problems
above make a derivation impossible from the start.)

It made me ask whether I had been trapped in the micro/quantum picture, and
whether vacuum energy should not be cut at the Planck scale but coarse-grained
(averaged over the fine detail) at the galaxy/structure scale instead. Digging further, I found this road had been
travelled from the 1990s to today. Obvious in hindsight, and quietly funny in the
moment. This is what standing on the shoulders of giants feels like: holographic
dark energy, EFTofLSS, IR cutoffs, coarse-graining, running vacuum, Buchert
averaging, LTB voids, screening. Even the specific move of using the roughly 10 Mpc
nonlinear scale as a coarse-graining cutoff for the dark sector was already in the
papers.

What is interesting is that the model does not vanish entirely. It is
indistinguishable from LCDM in the background, but it leaves fingerprints in
structure: a step in $P(k)$, a scale-dependent tilt in the ISW signal, a running
growth index. It hides in the background and can be caught in structure; a
falsifiable signal that a Euclid-class survey could actually detect fell out of
it.

One thing I want to state plainly: this is not a record of proving QFUDS. It is
closer to a record of a non-specialist brute-forcing the path that converges onto
modern cosmology's open problems.

The starting point was a set of questions I already cared about: information,
thermodynamics, and black holes. The link between information erasure and heat
led naturally to `it from bit`, the black-hole information problem, and then the
dark sector. After several GPT conversations and thought experiments, I wanted
to know where the idea actually held together and where it failed. As a
developer, I also had a practical hunch: with AI, literature search, asset
management, numerical checks, and failure records could be tied into one
research pipeline.

So this was not just a chatbot conversation. Inside this repository I spent 5
days building and running an agent-based operating procedure: paper caches,
asset-status tables, workflow definitions, experiment/result records, and
validation scripts. The system kept separating what I knew, what I did not know,
and what I did not yet know I was missing. It did not prove the physics; it
provided a way to record the search and filter unsupported conclusions.

I used broad searches to understand the field, but I only used primary sources
for reference data and numerical comparison. YouTube, Wikipedia, and even
English Wikipedia were not evidence sources. The pipeline searched papers,
pulled PDFs and arXiv source, extracted figures, converted documents, digitized
plots into CSVs, and compared my transfer function $\Gamma(a)$ against recovered
`S_BH(a)` and `entropy_density(a)` values from Chen Figure 5. It also automated
known-model distinction, reduced duplicate fetches through caching, and attached
validation gates to each status claim.

The operational summary is:

1. The brute-force exploration reached the same unsolved-problem region that
   appears in the cosmology literature.
2. Several hand-built values and intuitions overlapped with existing literature
   paths from the 1990s to today.
3. The result remains a rough proxy record, not a validated physical model.
4. The agent-based workflow helped keep literature, assets, status, validation,
   and failure records separate.
5. The process is kept as a methodology record alongside the physical negative
   results.

The relevant DESI/Euclid data (from next-generation surveys that map large-scale
structure in detail) won't be released until this October. Until then, there is
nothing more to do but wait.

## How This Was Built: Agent-Based Research Operations

The physics above is only part of the story. The other part is the system used to
produce and check the work. The repository used a consistent feedback loop. I did not
assume the AI was right; I assumed it could be wrong, could overstate results,
and could confuse "not in cache" with "does not exist." So the repository split
literature, assets, status, validation, and retrospectives into separate layers
and made each pass check the others. The workflow record is in
[lineage 006](docs/wiki/lineage/006_agentic_research_system_ko.md); the incident
records are in the
[postmortems folder](docs/wiki/postmortem/) (11 of them).

The setup is divided into explicit operating rules:

- **It reads real papers, not summaries.** PageIndex and MarkItDown were attached
  through MCP, the standard way to connect external tools to an AI agent. The
  important part was not a generic `PDF -> Markdown` conversion, but parser
  routing. Paper PDFs and arXiv source went through PageIndex for structure,
  pages, and body text; data releases, manifests, tables, and code-like records
  went through MarkItDown. Figures were extracted separately. Chen Figure 5 was
  digitized by separating the colored curves, calibrating the axes, and
  recovering a 432-row CSV. This provided a numeric comparison between my
  `Gamma(a)` curve and recovered `S_BH(a)` / `entropy_density(a)` values, not
  just a visual comparison. This remained a source-history candidate, not QFUDS
  evidence. The parsed-and-checked results live in
  [docs/wiki/research/](docs/wiki/research/): about 60 literature notes and a
  dozen fully digitized papers (see the
  [Source-X investigation](docs/wiki/research/investigations/source_x/)), each
  kept with its source, its figures, and its recovered numbers.
- **It knows the difference between "I have the PDF" and "I can actually use this
  as data."** Every source sits on an 11-rung ladder, from "never searched" to
  "downloaded but never opened" to "numbers digitized and ready to use." This
  blocks a common research failure mode: treating a downloaded file as if it had
  actually been checked. The
  [literature index](docs/wiki/research/literature/index.csv) records fields like
  `product_status`, `digitization_status`, `used_by`, and `last_checked`, so "not
  in cache," "not found in the world," and "paper exists but no usable data
  product exists" do not collapse into the same state. The cache saves tokens and
  fetches, and it avoids downloading the same paper twice.
- **Validation is applied in two layers.** At the prompt layer, I repeatedly
  forced instructions such as "run the tests," "do not change the roadmap SSOT,"
  and "do not treat timing resemblance as evidence." At the commit layer, git
  hooks run `validate_docs.py`, `research_consistency.py`, and
  `preflight_exp004.py`. Here "evidence" does not mean that an LLM found the
  claim plausible. It means file-backed conditions: frontmatter status, required
  sections, links, output files, result documents, and consistency with the
  roadmap SSOT. All 24 checkpoints had to clear these gates before they were
  recorded.
- **Positive claims get a separate review pass.** When a sentence says "reduced,"
  "derived," or "passed," the same Codex/AI workflow runs an adversarial review
  pass looking for counterexamples and overclaims. Then the prompt asks for tests
  again, and the commit hook runs the mechanical checks. This process flagged
  three overclaims mid-flight (recorded in
  [lineage 005](docs/wiki/lineage/005_rough_tanh_thesis_report_ko.md)).
- **More than one AI checked the work.** I ran Codex as the lead, with Claude Code
  and Gemini as backups and cross-checkers, so one model's omissions could be checked
  by another.

The point is methodological: the repository records how a speculative branch was
pushed while unsupported conclusions were checked against documented gates.
Failures are written down in postmortems, and positive claims must pass the same
documented gates as the rest of the repository.

## Why I Came Up With The Hypothesis

### From Information Erasure To A Testable Model

Quantum Foam Unified Dark Sector (QFUDS) started as a toy-framework repository while I was thinking about dark matter, dark energy, and information flow in cosmology.

I wanted to know how far the idea could stay coherent.

I wanted to turn curiosity into equations, constraints, toy code, and falsifiable questions, then actually test the hypothesis.

I read a piece about information thermodynamics.

```text
Original motivating text, kept as provenance rather than as a technical claim:
Physics has shown that erasing memory necessarily produces heat.
This is the principle proposed by physicist Rolf Landauer. Computation or information generation itself does not necessarily consume energy, but erasing or forgetting one bit of information necessarily releases a certain amount of heat energy into the surroundings.
In other words, the human brain and a hard disk both increase the entropy of the universe and produce physical heat when they "forget" something. Information may not have mass, but information erasure has a thermodynamic price.
The seemingly vague act of "forgetting" is actually paid to the universe as heat and recorded in its bookkeeping.
This is a neuroscience story, a story about the limits of computers, and also a cosmology story.
```

Conservative reading: Landauer's principle applies to logically irreversible erasure (deletions you cannot undo, like overwriting a bit) in a physical system coupled to a thermal environment (one that can exchange heat with its surroundings). It does not mean that every act of computation has the same unavoidable cost, and it does not by itself imply cosmology.

Analogy: deleting a file does not make a laptop ignore physics. The machine still uses energy and releases heat. In the ideal limit, erasing one bit has a minimum thermodynamic cost of order $k_B T \ln 2$ under the usual Landauer assumptions. The longer raw trail is not repeated here; it is preserved in [concept_origin.md](docs/01_origin/concept_origin.md).

That immediately led me to the black-hole question.
If information has a physical cost, a black hole should not be treated as a simple trash can in a quantum theory. This is a motivation for asking sharper questions, not a derivation of QFUDS.
The next questions: where is the information encoded; could a unitary evaporation (one that preserves information rather than destroying it) hand it back through correlations hidden in the radiation; and is the real obstacle that information is destroyed, or just that decoding it is hopelessly complex?

The first thought flow was not a proof. The question moved roughly like this:

```text
information erasure has a heat cost
-> this has the same shape as the black-hole information-loss problem
-> unitary black-hole evaporation would require information to be encoded in correlations
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
If the clustering foam phase transfers into the residual vacuum-pressure phase, can that phase-transfer rate be tied to physical quantities or controlled phenomenological proxies such as structure growth, black-hole entropy, horizon entropy, star formation, or remnant statistics?

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

For the current audited status of which branches survived, were demoted to motivation, or were killed against repository evidence, including the Source-X known-model-distinction outcome and the move to observer mode, see [concept_survival_audit.md](docs/00_project/concept_survival_audit.md). The [Roadmap](docs/05_next_steps/000_roadmap.md) remains the single source of truth for status.

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
- Experiment outcomes: [Experiment Summary](docs/04_results/000_experiment_summary.md)
- Claim/evidence traceability: [Traceability Matrix](docs/00_project/traceability_matrix.md)
- [Level 1.5](docs/wiki/glossary/repository_levels.md) pass/fail gate: [Level 1.5 Resolution Gate](docs/05_next_steps/015_level_1_5_resolution_gate.md)
- Reproducible checks: [Verification Guide](docs/00_project/verification_guide.md)
- Documentation integrity rules: [Experiment Record Convention](docs/00_project/experiment_record_convention.md) and [Frontmatter Convention](docs/00_project/frontmatter_convention.md)

Until the model survives CMB and structure-formation tests, it should not be read as a strong physical claim.

To audit the research record from the command line:

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/preflight_exp004.py
```

`validate_docs.py` checks metadata and required experiment/result sections.
`research_consistency.py` checks that the roadmap remains the status authority.
`preflight_exp004.py` checks exp_003 record consistency. It does not authorize
new retained-branch experiments.

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

### Two-Phase Transfer Model (Retained Branch, Now Demoted to Phenomenology)

> This was the original working hypothesis. It has since been demoted to
> phenomenological interacting-vacuum status, and the project is in observer
> mode (see [Where This Stands](#where-this-stands-what-pushing-the-idea-to-the-wall-found)
> and the [Roadmap](docs/05_next_steps/000_roadmap.md)). It is kept below as the
> model definition, not as a current physical claim.

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

The test this branch was held to was whether $\Gamma(a)$ can be tied to a real physical source, or to an explicitly labeled proxy (a stand-in quantity whose origin is stated up front), instead of being a hand-fit function. It did not pass that bar as a physical derivation and now survives only as labeled phenomenology.
Useful but still provisional validation directions are low-redshift collapse (how structure breaks down in the nearby, recent universe), black-hole entropy, and star-formation proxies.
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
3. Dynamic vacuum energy: can the cosmological constant be a slowly relaxing equilibrium value (a number that settles into place over time) rather than a fixed number inserted by hand?

### Possible Phenomena If The Model Works

The following are not verified predictions. They are candidate kill surfaces, and several are not unique to QFUDS.

1. Standard WIMP (Weakly Interacting Massive Particle, the long-favored dark-matter candidate) direct detection may continue to return null results. This would not by itself favor QFUDS, because many non-QFUDS dark-matter models also predict weak or hidden direct-detection signals.
2. Dark energy may show small but nonzero time evolution.

$$
w(a) = w_0 + w_a(1-a)
$$

In LCDM, $w_0=-1$ and $w_a=0$. For QFUDS to differ, it needs a small deviation with $w_0 \simeq -1$ and $|w_a|>0$.

3. Large-scale structure and the CMB must remain almost LCDM-like.
4. Small galaxy halos may prefer flat cores over sharp central spikes (cusps), but this must be separated from baryonic feedback (ordinary matter, stars and supernovae, pushing back on the structure).
5. Dark matter structure and ordinary (baryonic) matter structure may show a slightly stronger correlation than in pure collisionless CDM (cold dark matter that interacts only through gravity), but no such QFUDS-specific relation has been derived yet.
6. In a complete unitary (information-preserving) quantum description, the final black-hole evaporation state should not be describable as purely information-free thermal radiation. This is a quantum-gravity consistency expectation, not an observed astrophysical signal.
7. If black/white-hole remnants exist, their allowed mass distribution must be narrow.

The core of the current test is not white holes.
What matters more is whether precision observations keep supporting $w=-1$, or move toward a small nonzero $w_a$.

### Kill Tests: First Attacks

A hostile reviewer should attack the model in this order.

1. Does it recover LCDM exactly in the zero-deviation limit?
2. Can the same effective medium produce $w \simeq 0$ and $w \simeq -1$ without hand-waving (vague, unproven arm-waving)?
3. Why is $c_s^2$ near zero?
4. Does it preserve CMB acoustic peaks?
5. Does it preserve the matter power spectrum?
6. Is it better than existing unified dark fluid or k-essence models?
7. Does the remnant sector add real predictions, or only story language?

If these fail, QFUDS is only a vocabulary shift.

## Black Hole Interpretation: Re-reading, Not Evidence

Black holes are not central evidence for QFUDS.

The observational baseline is:

```text
Many massive galaxies, especially galaxies with central bulges, host central massive black holes.
```

The Milky Way's central black hole and M87's black hole are representative examples. Their existence is observationally established through stellar dynamics and event-horizon-scale imaging. Their exact formation paths are still being studied. Standard astrophysical explanations such as seed formation, gas accretion, galaxy and black-hole mergers, direct collapse, dense stellar dynamics, and formation inside dark-matter halos still matter.

The standard structure-formation order is closer to:

```text
primordial density perturbations
-> cold dark matter halos
-> gas cooling, star formation, and galaxies
-> central massive black-hole seeds plus accretion and mergers
```

This is not the same as saying that black holes create galaxies. Black holes can affect their host galaxies through feedback, especially active galactic nuclei (AGN, where a black hole's energetic output reaches back to influence its galaxy's star formation), but they are not the general starting point of galaxy formation in the standard picture.

QFUDS may ask a different question:

```text
if dark halos are an effective foam phase,
could central black holes trace special high-density,
high-entropy, or high-information regions of that phase?
```

The first clause is a QFUDS assumption, not a standard result. Standard cosmology does not say:

```text
quantum foam -> dark halo
```

The stronger QFUDS question is:

```text
If dark matter is a foam phase,
could central black holes be special compression sites
or phase-transition sites inside that foam sector?
```

If interpreted from the QFUDS point of view:

```text
black hole = possible local information-compression node
```

More strongly:

```text
black hole = speculative candidate phase-transition site of the foam sector
```

This is not established black-hole physics. "Black-hole phase transition" is an existing phrase in black-hole thermodynamics, especially in anti-de Sitter (AdS, an imaginary spacetime with negative vacuum energy) or extended-thermodynamics settings, but that literature does not mean that observed galactic-center black holes are phase-transition sites of a quantum-foam dark sector.

Analogy: in a large city, a major data center may sit near routes where lots of data flows. But the existence of that data center does not prove that the whole city was created by the network. Likewise, a central black hole can be read in QFUDS language as a compression point or routing point, but it does not prove QFUDS and does not replace standard black-hole formation physics.

The safe statement is:

```text
QFUDS may reinterpret central black holes as possible information-compression nodes inside foam-dominated halos, but this is speculative and does not yet explain why many massive galaxies host central black holes.
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
- [project_identity.md](docs/00_project/project_identity.md): current project identity, scope, non-goals, retained-branch classification, and "What We Actually Learned"
- [success_criteria.md](docs/00_project/success_criteria.md): minimum/moderate/strong success criteria and the physical-branch admission rule
- [qfuds_positioning.md](docs/00_project/qfuds_positioning.md): QFUDS ideas mapped against existing cosmology model families
- [concept_survival_audit.md](docs/00_project/concept_survival_audit.md): original intuition mapped against current evidence, demotions, and open candidates
- [decision_log.md](docs/00_project/decision_log.md): chronological decision record with reasons and evidence
- [verification_guide.md](docs/00_project/verification_guide.md): how to rerun and read current validation
- [frontmatter_convention.md](docs/00_project/frontmatter_convention.md): canonical metadata schema
- [experiment_record_convention.md](docs/00_project/experiment_record_convention.md): experiment/result section rules, summary policy, and postmortem policy
- [traceability_matrix.md](docs/00_project/traceability_matrix.md): bidirectional claim/evidence traceability index
- [000_qfuds_v0_1_conceptual_origin.md](docs/02_theory/000_qfuds_v0_1_conceptual_origin.md): conceptual origin-stage theory note
- [000_qfuds_v0_2_two_phase_background.md](docs/02_theory/000_qfuds_v0_2_two_phase_background.md): minimal two-phase effective-fluid theory note
- [010_qfuds_v0_3_gamma_laws.md](docs/02_theory/010_qfuds_v0_3_gamma_laws.md): physically labeled $\Gamma(a)$ transfer-law theory note
- [015_qfuds_v0_15_phase_transfer_physics.md](docs/02_theory/015_qfuds_v0_15_phase_transfer_physics.md): phase-transfer physicality audit
- [030_qfuds_phenomenological_perturbations.md](docs/02_theory/030_qfuds_phenomenological_perturbations.md): phenomenological perturbation closure theory note
- [000_exp_000_lcdm_baseline.md](docs/03_experiments/000_exp_000_lcdm_baseline.md): zero-transfer LCDM control run
- [010_exp_001_gamma_scan.md](docs/03_experiments/010_exp_001_gamma_scan.md): transfer-law scan
- [015_exp_001_5_phase_transfer_physicality.md](docs/03_experiments/015_exp_001_5_phase_transfer_physicality.md): physicality gate
- [020_exp_002_entropy_information_gate.md](docs/03_experiments/020_exp_002_entropy_information_gate.md): entropy/information-source gate
- [030_exp_003_phenomenological_perturbation_closure.md](docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md): perturbation-closure audit
- [030_exp_004_p1_model_family_positioning.md](docs/03_experiments/030_exp_004_p1_model_family_positioning.md): retained P1 model-family positioning audit
- [030_exp_005_timing_prior_usefulness.md](docs/03_experiments/030_exp_005_timing_prior_usefulness.md): timing-prior usefulness audit
- [030_exp_006_literature_timing_support_audit.md](docs/03_experiments/030_exp_006_literature_timing_support_audit.md): literature timing-support audit
- [000_result_000_lcdm_baseline.md](docs/04_results/000_result_000_lcdm_baseline.md): zero-transfer baseline result
- [010_result_001_gamma_scan.md](docs/04_results/010_result_001_gamma_scan.md): result interpretation and next target
- [015_result_001_5_phase_transfer_physicality.md](docs/04_results/015_result_001_5_phase_transfer_physicality.md): physicality result
- [020_result_002_entropy_information_gate.md](docs/04_results/020_result_002_entropy_information_gate.md): entropy/information-source provenance result
- [030_result_003_phenomenological_perturbation_closure.md](docs/04_results/030_result_003_phenomenological_perturbation_closure.md): perturbation-closure result
- [030_result_004_p1_model_family_positioning.md](docs/04_results/030_result_004_p1_model_family_positioning.md): retained P1 is an interacting-vacuum/time-dependent IDE instance, not a new physical branch
- [030_result_005_timing_prior_usefulness.md](docs/04_results/030_result_005_timing_prior_usefulness.md): retained timing is useful only as a prior-compression target
- [030_result_006_literature_timing_support_audit.md](docs/04_results/030_result_006_literature_timing_support_audit.md): literature timing overlap is allowed but not a source derivation
- [000_experiment_summary.md](docs/04_results/000_experiment_summary.md): lightweight experiment conclusions and postmortem coverage
- [000_roadmap.md](docs/05_next_steps/000_roadmap.md): validation stages, status, and blockers
- [010_perturbation_gate.md](docs/05_next_steps/010_perturbation_gate.md): perturbation gate
- [015_level_1_5_resolution_gate.md](docs/05_next_steps/015_level_1_5_resolution_gate.md): evidence criteria for Level 1.5 pass, fail, or demotion
- [030_exp003_record_consistency_gate.md](docs/05_next_steps/030_exp003_record_consistency_gate.md): record-consistency gate for the Level 2A perturbation closure

History/source notes:

- [004_rough_tanh_numerical_sketch_ko.md](docs/wiki/lineage/004_rough_tanh_numerical_sketch_ko.md): the 24-checkpoint rough-`tanh` numerical exploration log (Korean)
- [005_rough_tanh_thesis_report_ko.md](docs/wiki/lineage/005_rough_tanh_thesis_report_ko.md): thesis-style synthesis of the rough-`tanh` lineage covering effective fit, falsifiable signatures, and the theoretical ceiling (Korean)
- [006_agentic_research_system_ko.md](docs/wiki/lineage/006_agentic_research_system_ko.md): agent-based research operations record: document/status boundaries, workflow routing, asset cache states, PageIndex/MarkItDown MCP, adversarial review passes, and deterministic git-hook gates (Korean)
- [Source-X investigation index](docs/wiki/research/investigations/source_x/README.md): Source-X plans 041-050, Chen Figure 5 digitization, known-model distinction, observer-mode routing, and foam-sector feasibility closeout
- [Blocked Admission Rule Gate](docs/wiki/governance/003_blocked_admission_rule_gate.md): five-item physical-branch admission gate
- [Missing Physics Map](docs/wiki/governance/004_missing_physics_map.md): missing mathematical objects before a physical branch can open
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

Install the local git pre-commit hook if you want commits to enforce the same
documentation and regression checks:

```bash
make install-git-hooks
```

The hook also updates staged Markdown frontmatter `last_updated` dates before
running validation.

Run the experiment 004 preflight gate.

```bash
python3 scripts/preflight_exp004.py
```

This gate is documented in [030_exp003_record_consistency_gate.md](docs/05_next_steps/030_exp003_record_consistency_gate.md) and can also be run with `make preflight-exp004`.

### Reference Literature

The links below anchor nearby research directions. They do not prove QFUDS.

- [Hawking evaporation and the Landauer Principle](https://arxiv.org/abs/2407.08777)
- [Landauer Principle Stands up to Quantum Test](https://physics.aps.org/articles/v11/49)
- [Entanglement Wedge Reconstruction and the Information Paradox](https://arxiv.org/abs/1905.08255)
- [Replica wormholes and the black hole interior](https://arxiv.org/abs/1911.11977)
- [Black hole fireworks: black-to-white-hole tunneling](https://arxiv.org/abs/1407.0989)
- [Small black/white hole stability and dark matter](https://arxiv.org/abs/1805.03872)
- [The Thermodynamics of Black Holes](https://link.springer.com/article/10.12942/lrr-2001-6)
- [Coevolution (Or Not) of Supermassive Black Holes and Host Galaxies](https://arxiv.org/abs/1304.7762)
- [The origins of massive black holes](https://www.nature.com/articles/s42254-021-00364-9)
- [Formation of Supermassive Black Hole Seeds](https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/formation-of-supermassive-black-hole-seeds/DA9F246C7A0C6C1C0E057CCBF40220F6)
- [First M87 Event Horizon Telescope Results IV](https://arxiv.org/abs/1906.11241)
- [First Sagittarius A* Event Horizon Telescope Results III](https://arxiv.org/abs/2311.09479)
- [Cold dark matter: Controversies on small scales](https://pmc.ncbi.nlm.nih.gov/articles/PMC4603506/)
- [Direct Detection of Dark Matter: A Critical Review](https://www.mdpi.com/2073-8994/16/2/201)
- [Planck 2018 cosmological parameters](https://arxiv.org/abs/1807.06209)
- [DESI DR2 results guide](https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/)
- [Unified dark fluid with null sound speed](https://arxiv.org/abs/2509.16155)
