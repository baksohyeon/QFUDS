---
doc_id: research_program
title: QFUDS Research Program
doc_type: overview
stage: "reference"
status: reference
evidence_role: reference
depends_on:
  - project_overview
  - roadmap
next_gate: roadmap is status SSOT; keep Level 2B blocked unless a new physical branch is admitted
last_updated: 2026-06-09
---

# QFUDS Research Program

Working title:

```text
Quantum Foam Unified Dark Sector (QFUDS):
A Speculative Framework for Dark Matter, Dark Energy, and Information Cycling
```

## Abstract Draft

This note explores a speculative cosmological framework in which dark matter and dark energy emerge as two macroscopic phases of a common microscopic quantum-spacetime foam sector. In contrast to the standard LCDM paradigm, where dark matter and dark energy are treated as distinct components, QFUDS asks whether both phenomena could arise from different infrared manifestations of a single quantum foam medium.

In this framework, the clustering phase behaves as an effectively pressureless component characterized by `w ~= 0` and `c_s^2 ~= 0`, reproducing the large-scale structure formation normally attributed to cold dark matter. The residual phase behaves as a slowly relaxing vacuum-pressure component with `w ~= -1`, providing an effective description of cosmic acceleration.

Black holes are interpreted as local information-compression nodes. Black/white-hole remnants, motivated by quantum-gravity tunneling scenarios, are treated as subdominant topological defects within the same foam sector.

The model preserves the Friedmann background dynamics of general relativity while suggesting possible deviations from LCDM in dark-energy evolution, small-scale halo structure, dark-sector clustering behavior, and late-time information correlations associated with black-hole evaporation.

This is a research program and toy framework, not a complete physical theory. The primary objective is to formulate predictions that can be tested against CMB observations, large-scale structure surveys, halo profiles, direct dark matter searches, and future precision measurements of the dark-energy equation of state.

## Why The Center Shifted Away From White Holes

The original idea contained a strong white-hole-universe image. That image is useful creatively, but it is too broad as physics.

The more defensible center is:

```text
dark matter + dark energy
= two effective phases of quantum spacetime foam
```

Black holes and white-hole-like remnants remain in the framework, but as secondary structures:

```text
black holes      -> information-compression nodes
white remnants   -> optional delayed-release defects
remnant density  -> constrained subcomponent
```

This avoids making the whole model depend on the claim that the universe is literally a white hole.

## Model v0.2

The dark sector is split into a unified foam component and an optional remnant component:

```text
rho_dark = rho_QF + rho_rem
```

The foam component is modeled as a unified dark fluid:

```text
rho_QF(a) = rho_QF,0 [(1 - B_s) + B_s a^(-3(1 + alpha))]
```

Interpretation:

```text
(1 - B_s)              -> residual vacuum-pressure behavior
B_s a^(-3(1 + alpha))  -> clustering matter-like behavior
```

Survival conditions:

```text
alpha ~= 0
c_s^2 ~= 0
w_late ~= -1
w_a may be small but nonzero
```

The remnant component is:

```text
rho_rem = integral M f(M) dM
```

It should be treated as subdominant unless its mass function survives microlensing, CMB, and structure-formation bounds.

## The First Observational Constraint

The first constraint is not direct detection. It is structure formation.

The foam must cluster like cold dark matter while also producing a residual pressure like dark energy. That is only possible if the effective sound speed is extremely small:

```text
c_s^2 ~= 0
```

If `c_s^2` is not close to zero, pressure support erases density perturbations and galaxy halos fail to form.

The second immediate constraint is the CMB. Planck already fits LCDM very well. Any QFUDS model that significantly shifts the acoustic peaks, early matter-radiation equality, or lensing spectrum is dead.

The third constraint is the matter power spectrum. A viable model must remain close to LCDM on large scales while allowing only controlled deviations on small halo scales.

## Prediction Set

QFUDS v0.2 predicts or motivates the following tests:

1. Direct WIMP detection may remain null because the dominant dark sector is a collective medium rather than a standard particle species.
2. Dark energy may show weak time evolution:

```text
w(a) = w_0 + w_a(1 - a)
w_0 ~= -1
|w_a| > 0 but small
```

3. The CMB should be nearly LCDM-like.
4. The matter power spectrum should be nearly LCDM-like on large scales.
5. Small galaxy halos may prefer cored profiles over sharp NFW cusps.
6. Baryonic structure and inferred dark structure may show a tighter relation than pure collisionless CDM expects.
7. Black-hole radiation should not be exactly thermal in the full quantum description.
8. If remnants exist, their mass function must be narrow and observationally constrained.

## Cusp-Core Note

The halo-core prediction is not a brand-new observation. It is connected to the known cusp-core problem.

Standard collisionless CDM simulations often produce cuspy inner profiles. Some dwarf and low-surface-brightness galaxies appear more consistent with flatter cores.

QFUDS does not automatically win here. Baryonic feedback can also soften cusps. The useful QFUDS question is narrower:

```text
Can a near-zero-sound-speed foam fluid naturally produce cored small-scale halos
without spoiling CMB and large-scale structure?
```

## Central Black Holes

Nearly all large galaxies appear to host central supermassive black holes. QFUDS should not overclaim this.

Known observational fact:

```text
large galaxies commonly host central supermassive black holes
```

This does not by itself support QFUDS. Standard astrophysics already has candidate formation channels: black-hole mergers, direct collapse, early massive seeds, and accretion inside dark-matter halos.

The conservative formation order is:

```text
quantum foam dark sector
-> dark halo
-> galaxy
-> central supermassive black hole
```

The speculative interpretation is:

```text
black hole = local information-compression node
black hole = possible foam phase-transition site
```

This may become useful if the model predicts changes in halo structure, feedback, or information storage near black holes. Without such predictions, it remains interpretation.

The safe QFUDS position is therefore:

```text
central SMBHs are not proof of QFUDS;
they are possible high-density nodes where the foam-sector interpretation
could become observationally relevant.
```

## Validation Roadmap

Current per-level status lives only in the roadmap:
[docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md).

This document is a reference note for the research framing and idea trail. It
must not be used as the status source. The retained
`dF_coll/dln(a)`/information-production branch has failed physical [Level 1.5](../wiki/glossary/repository_levels.md)
promotion and is demoted to phenomenological interacting-vacuum status. That
rejects only the current retained source relation as a physical derivation; it
does not falsify the broader DM-to-DE phase-transition hypothesis.

## Validation Lineage

The validation path is intentionally staged. The project first checked whether
the two-phase background has a clean LCDM null limit. It then tested whether
named `Gamma(a)` transfer laws already fail at background level. After that,
entropy and information-source scans asked whether any candidate transfer shape
was less arbitrary than a free fitting function. The retained
collapse/information-production shape then became a Level 1.5 physicality
question, not a physical result.

That lineage is historical context only. For the current per-level state, use
the roadmap:
[docs/05_next_steps/000_roadmap.md](../05_next_steps/000_roadmap.md).

Level terminology and level relationships are defined in
[repository_levels.md](../wiki/glossary/repository_levels.md). This section
keeps the historical experiment lineage only.

### Experiment 001: Physically Motivated Gamma(a) Laws

Status:

```text
experiment 001 complete at background-diagnostic level
```

Output:

```text
docs/04_results/010_result_001_gamma_scan.md
qfuds/gamma_laws.py
generalized background integration
viability table for candidate Gamma(a) laws
CSV and PNG output files
```

Result:

```text
constant and ungated growth-driven transfer die early
power-law and horizon-entropy gates behave like ordinary interacting dark energy
collapsed-fraction, black-hole-entropy, and star-formation proxies are worth testing next
```

This does not prove QFUDS novel. It only narrows the next target to low-redshift, physically sourced transfer laws.

### Experiment 002: Entropy And Information Sources

Status:

```text
experiment 002 complete at background-diagnostic level
```

Output:

```text
docs/03_experiments/020_exp_002_entropy_information_gate.md
docs/04_results/020_result_002_entropy_information_gate.md
qfuds/gamma_laws.py
CSV and PNG output files
```

Result:

```text
HBM/KL gravitational entropy fails positivity at the tested amplitude
horizon information reduces to standard horizon/interacting dark energy
black-hole entropy still needs a real mass/accretion history
Press-Schechter information production was the narrow branch retained for
Level 1.5, then demoted after failing physical promotion
```

This still does not prove perturbation stability, CMB viability, matter-power viability, or novelty.

The Press-Schechter/information-production branch was retained because its
source history naturally turns on after nonlinear structure formation and is
less arbitrary than a free `Gamma(a)` curve. That made it worth a hostile
Level 1.5 review. The later demotion means the timing was useful as a proxy, but
the repository still did not derive a physical conversion from phase A into
vacuum-pressure phase B.

For perturbation-level terminology, use
[repository_levels.md](../wiki/glossary/repository_levels.md) and
[010_perturbation_gate.md](../05_next_steps/010_perturbation_gate.md).

### Level 3: CLASS Or CAMB Implementation

Implement QFUDS as a custom dark fluid:

```text
background density
pressure
effective equation of state
sound speed
perturbation equations
```

Default test:

```text
alpha = 0
c_s^2 = 0
remnant fraction = 0
```

This should reproduce the LCDM limit.

### Level 4: CMB Comparison

Compare:

```text
C_l^TT
C_l^TE
C_l^EE
lensing spectrum
```

QFUDS must not visibly damage the acoustic peak structure.

### Level 5: Matter Power Spectrum

Compare:

```text
P(k)
f sigma_8
growth factor
weak-lensing response
```

The model should remain close to LCDM on large scales.

### Level 6: Late-Time Surveys

Test against:

```text
DESI
Euclid
Roman
supernova distances
BAO
weak lensing
```

This is where a small nonzero `w_a` becomes interesting.

## Hardest Questions

1. What is the actual foam equation of motion?
2. Why does `c_s^2 ~= 0` follow from the model instead of being inserted by hand?
3. What symmetry or conservation law fixes `rho_*` as a tiny positive value?
4. Does the model predict a unique relation between dark-energy evolution and growth suppression?
5. Does the remnant sector make any measurable prediction?
6. Can the model beat LCDM without adding enough freedom to fit anything?

## Current Verdict

QFUDS v0.2 is not a theory. It is a research framework.

Its strongest academic core is:

```text
Quantum foam unified dark sector with near-zero effective sound speed.
```

Its weakest parts are:

```text
no microscopic action yet
no derived sound speed yet
no Boltzmann-code implementation yet
no CMB or matter-power fit yet
remnant sector still optional
```

The next real step is not to reopen the retained `Gamma(a)` branch. CLASS or
CAMB remain blocked for physical claims until a new physical branch supplies a
transfer derivation and perturbation prescription. The retained branch may
continue only as explicitly phenomenological interacting-vacuum work.
