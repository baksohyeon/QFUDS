---
doc_id: qfuds_strong_gravity_source_mechanism_audit
title: QFUDS Strong Gravity Source Mechanism Audit
doc_type: theory_note
stage: "1.5"
status: completed
evidence_role: audit
depends_on:
  - qfuds_v0_15_phase_transfer_physics
  - qfuds_level_1_5_equivalence_source_perturbation_audit
  - qfuds_level_1_5_transfer_four_vector_derivation_attempt
next_gate: retained branch demoted; strong-gravity ideas require a new admitted physical branch
last_updated: 2026-06-09
---

# QFUDS Strong Gravity Source Mechanism Audit

Date: 2026-06-09

This note asks whether black holes, horizons, white holes, baby universes, or
other strong-gravity ideas can supply a physical source mechanism for the broader
DM-to-DE phase-transition hypothesis.

It does not by itself change viability classifications. The retained-branch
decision is recorded in [000_roadmap.md](../05_next_steps/000_roadmap.md).

## Summary Verdict

The retained branch fails because its specific source relation is not physically
derived:

```math
\Gamma(a) \propto {dF_{\rm coll}(>M,a)\over d\ln a}.
```

That failure does not falsify the broader DM-to-DE phase-transition idea.

Strong-gravity frameworks can define candidate quantities such as black-hole
area entropy, Hawking mass loss, horizon area, remnant abundance, or baby-universe
nucleation rates. None currently gives QFUDS a complete source-to-transfer law
from clustering phase A to smooth vacuum-pressure phase B.

## Candidate Mechanism Table

| Candidate | Possible source `X` | Established physics | Main gap for QFUDS | Level 1.5 outlook |
| --- | --- | --- | --- | --- |
| black-hole entropy | total `S_BH = sum A_i/(4G)` or `dS_BH/dln(a)` | black-hole thermodynamics, area entropy | entropy growth does not imply vacuum-pressure energy transfer | weak; useful provenance, not enough |
| Hawking evaporation | `-dM_BH/dt`, evaporation luminosity, radiation entropy | semiclassical radiation from black holes | produces radiation-like output, not smooth `w ~= -1` phase B | poor for DE, possible for radiation/remnants |
| horizon / holographic dark energy | horizon area, IR cutoff `L`, `rho_DE ~ M_P^2 L^-2` | known HDE/horizon-thermodynamic model class | gives dark-energy-like density but not DM-to-DE transfer | moderate but likely known-model behavior |
| cosmologically coupled black holes | black-hole mass growth or effective vacuum energy in compact objects | active, controversial literature | not established; maps black holes to DE source, not QFUDS phase transfer | most directly relevant but high-risk |
| white-hole / Planck-star remnants | remnant abundance, tunneling rate, delayed release rate | speculative quantum-gravity scenario | tends to produce compact DM-like remnants or radiation, not smooth DE | weak for DE, possible optional remnant sector |
| baby universes / wormholes | nucleation or absorption rate, vacuum branch changes | speculative quantum-gravity/cosmology | often removes energy into disconnected sectors or changes vacuum ensemble, not local A-to-B transfer | speculative; would be new model |

## Established Physics

Black-hole thermodynamics supplies real quantities:

- horizon area;
- Bekenstein-Hawking entropy;
- surface gravity / temperature;
- Hawking radiation in semiclassical gravity.

These are legitimate physical objects. They can support an `X` such as
`S_BH(a)` or `dM_BH/dt`.

References:

- Bardeen, Carter, Hawking, "The four laws of black hole mechanics":
  https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-31/issue-2/The-four-laws-of-black-hole-mechanics/cmp/1103858973.pdf
- Review of black-hole thermodynamics:
  https://pmc.ncbi.nlm.nih.gov/articles/PMC8339704/

What established physics does not supply:

```text
black-hole entropy growth -> smooth vacuum-pressure phase B
```

That step would be QFUDS-specific.

## Horizon And Holographic Dark Energy

Horizon-based dark energy is the strongest known-model neighbor. Holographic
dark energy links vacuum-like energy density to an IR cutoff or horizon scale,
rather than to halo collapse:

```math
\rho_{\rm DE} \sim M_P^2 L^{-2}.
```

References:

- Cohen, Kaplan, Nelson, "Effective Field Theory, Black Holes, and the
  Cosmological Constant": https://arxiv.org/abs/hep-th/9803132
- Li, "A Model of Holographic Dark Energy": https://arxiv.org/abs/hep-th/0403127

This direction can imply vacuum-pressure-like behavior more naturally than
`dF_coll/dln(a)`. But it does not by itself describe dark matter turning into
dark energy. If QFUDS uses this path, it must explain what phase A contributes
to the horizon source, or else it becomes ordinary holographic/interacting dark
energy.

## Black Holes As Dark Energy Sources

Cosmological coupling of black holes is directly relevant because it attempts to
link astrophysical black-hole production or growth to a dark-energy-like
contribution.

Reference:

- Farrah et al., "Observational evidence for cosmological coupling of black
  holes and its implications for an astrophysical source of dark energy":
  https://arxiv.org/abs/2302.07878

This is the strongest candidate to reopen Level 1.5 conceptually, because it
tries to connect compact strong-gravity objects to dark energy rather than only
to radiation or entropy accounting.

But for QFUDS it would be a new hypothesis, not a rescue of the retained branch.
It would need:

- a source scalar such as black-hole production rate, mass growth, or coupled
  vacuum energy;
- a local or averaged stress-energy tensor;
- a mapping from clustering phase A into the black-hole/coupled-vacuum source;
- a reason the result is smooth and vacuum-pressure-like;
- comparison to the black-hole-coupling model itself.

Without those, it is only an analogy.

## White Holes, Planck Stars, And Remnants

Black-to-white-hole transition and Planck-star scenarios are quantum-gravity
proposals for the late fate of black holes. They are often discussed as
information-preserving channels or remnant dark-matter candidates.

References:

- Haggard and Rovelli, "Black hole fireworks":
  https://arxiv.org/abs/1407.0989
- Rovelli and Vidotto review of Planck stars, white holes, and remnants:
  https://arxiv.org/abs/2407.09584
- "White Holes as Remnants":
  https://arxiv.org/abs/1802.04264

These frameworks may define candidate quantities such as tunneling rate,
remnant abundance, or delayed emission rate. They do not naturally produce a
smooth vacuum-pressure phase. Most outputs are compact remnants, radiation, or
information-release channels.

For QFUDS, this is better treated as an optional remnant/defect sector unless a
specific stress-energy transfer to phase B is derived.

## Baby Universes And Wormhole Ideas

Baby-universe and wormhole scenarios can connect black holes, vacuum selection,
and cosmological constants in speculative quantum gravity. They may define a
nucleation or absorption rate.

References:

- Baby universes in quantum gravity:
  https://link.springer.com/article/10.1007/JHEP12%282022%29100
- Baby-universe absorption and dark energy:
  https://arxiv.org/abs/2408.13306

The relevance to QFUDS is limited unless the model keeps stress-energy
accounting inside our observable universe. If energy is hidden in disconnected
baby universes, that is not automatically a smooth phase-B component in our
cosmology.

This path would be a new quantum-gravity model, not a small Level 1.5 patch.

## Established, Speculative, And QFUDS-Specific Parts

Established:

- black holes have thermodynamic area entropy;
- semiclassical black holes radiate;
- horizons can be used in known dark-energy model classes;
- total stress-energy accounting is required in GR.

Speculative:

- black-to-white-hole tunneling as an astrophysical process;
- stable Planck-scale white-hole remnants;
- baby-universe production or absorption as cosmological dynamics;
- black holes as an observationally established source of dark energy.

QFUDS-specific assumptions if adopted:

- phase A feeds a strong-gravity source;
- that source converts energy into phase B rather than radiation, compact
  remnants, heat, or disconnected sectors;
- phase B is smooth and vacuum-pressure-like;
- the source defines `Q^nu` and `delta Q`;
- the result is not just holographic dark energy, black-hole-coupled dark
  energy, or an ordinary interacting-vacuum model under a new name.

## Does Any Direction Beat dFcoll/dln(a)?

Yes, but only in narrow ways.

Horizon/holographic dark energy is better at producing vacuum-pressure-like
behavior, but worse at explaining DM-to-DE transfer. It likely collapses into a
known model class unless QFUDS adds a new source relation.

Cosmologically coupled black holes are more relevant than plain
`dF_coll/dln(a)` because they attempt to link black-hole production/growth to
dark-energy density. They are also more speculative and would require a new
QFUDS hypothesis.

White-hole, Planck-star, and baby-universe ideas are less promising for phase B
because they mainly point toward remnants, radiation, information return, or
disconnected sectors.

## Level 1.5 Reopening Test

A strong-gravity direction can reopen physical Level 1.5 only if it produces all
of the following:

1. a source scalar `X` tied to black holes, horizons, remnants, or baby-universe
   dynamics;
2. a stress-energy relation `Q^nu[X,...]`;
3. a reason the output is smooth vacuum-pressure phase B;
4. a perturbation prescription or route to `delta Q`;
5. a distinction from existing holographic, interacting-vacuum, black-hole
   coupling, or remnant-dark-matter models.

No reviewed framework currently supplies that package for QFUDS.

Therefore the current retained branch fails because the implemented
`dF_coll/dln(a)` source relation is insufficient, not because the broader
DM-to-DE phase-transition hypothesis has been falsified.

This is a future-branch admission rule, not an active new hypothesis:

- `X =`
- `Q^nu =`
- `why phase B has w ~= -1 =`
- `delta Q route =`
- `known-model distinction =`
