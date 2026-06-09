---
doc_id: qfuds_research_report
title: "Quantum Foam Unified Dark Sector: Research Evaluation"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on: []
next_gate: keep current when model assumptions change
last_updated: 2026-06-08
---

# Quantum Foam Unified Dark Sector: Research Evaluation

Date: 2026-06-08

## 1. Executive Summary

Conceptual origin: QFUDS began as Dorito's information-preservation thought experiment, not as a finished dark-sector theory. The original path was: information has physical cost; black holes should not simply destroy information; white-hole-like remnants could represent a delayed return channel; quantum foam could supply a vacuum medium; dark matter and dark energy might then be two large-scale modes of that medium. The cleaned-up version of that origin is documented in [docs/01_origin/concept_origin.md](../01_origin/concept_origin.md); the current research-program framing is documented in [docs/00_project/research_program.md](../00_project/research_program.md).

Verdict: QFUDS, as stated, is not yet a new theory. It is a research label for a class of already known unified-dark-sector models unless it specifies at least one of the following:

1. a covariant microscopic foam action;
2. a calculable phase-transition or phase-fraction law;
3. a perturbation prescription that differs from CDM plus Lambda while remaining stable;
4. a relic/topological-defect population with a predicted abundance and mass spectrum;
5. an observational signature not absorbed by LCDM, generalized dark fluid, k-essence, scalar-field DM, or interacting dark energy.

The minimal mathematically consistent formulation is a two-phase effective dark fluid in unmodified GR:

```math
T^{\mu\nu}_{\rm dark}=T_A^{\mu\nu}+T_B^{\mu\nu}, \qquad
p_A \simeq 0,\quad c_{s,A}^2\simeq 0,\qquad
p_B=-\rho_B .
```

With no phase transfer, this is exactly LCDM:

```math
\rho_A=\rho_{A0}a^{-3},\qquad \rho_B=\rho_{B0},\qquad
H^2=H_0^2[\Omega_r a^{-4}+\Omega_b a^{-3}+\Omega_A a^{-3}+\Omega_B].
```

With phase transfer,

```math
\frac{d\rho_A}{d\ln a}+3\rho_A=-\Gamma(a)\rho_A,\qquad
\frac{d\rho_B}{d\ln a}=\Gamma(a)\rho_A,
```

QFUDS becomes an interacting dark-sector model with a vacuum component. This is testable, but not automatically novel.

Current data set the bar high. Planck reports strong consistency with flat six-parameter LCDM and gives representative values \(H_0=67.4\pm0.5\) km/s/Mpc, \(\Omega_m=0.315\pm0.007\), and \(\sigma_8=0.811\pm0.006\) [Planck 2018](https://arxiv.org/abs/1807.06209). DESI DR2 plus CMB and supernovae shows a low-redshift preference for dynamical dark energy and possible phantom crossing, but this is currently a constraint target, not a validation of QFUDS [DESI DR2 guide](https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/), [DESI extended dark energy](https://arxiv.org/abs/2503.14743).

Bottom line: QFUDS survives only in the trivial LCDM limit or as a tightly constrained interacting/unified-dark-fluid model. The black-hole/white-hole remnant component is optional and subdominant; it does not unify the dark sector unless its abundance and coupling to the fluid are derived.

## 2. Literature Mapping

| Model | Similarities | Differences | Does QFUDS reduce to it? | New structure? |
| --- | --- | --- | --- | --- |
| LCDM | Same GR Friedmann background; phase A = CDM; phase B = Lambda. | LCDM has no common foam medium and no phase transfer. | Yes, exactly when \(\Gamma=0\), \(w_A=0\), \(c_{s,A}^2=0\), \(w_B=-1\). | No. Foam wording adds no observable content. |
| Unified Dark Fluid / quartessence | One dark medium produces matter-like and vacuum-like behavior. | QFUDS uses language of two macroscopic phases rather than one barotropic pressure law. | Yes, if total pressure is specified as \(p=p(\rho)\) or an equivalent effective split. | Only if phase fractions are independently measurable or nonbarotropic. |
| Generalized Chaplygin Gas | Interpolates from dust-like era to vacuum-like era with \(p=-A/\rho^\alpha\). | GCG has adiabatic sound speed \(c_s^2=-\alpha w\), often too large at late times. QFUDS demands \(c_s^2\simeq0\) in clustering phase. | Yes for a special barotropic choice. | No, unless QFUDS has entropy perturbations that decouple \(c_s^2\) from \(dp/d\rho\). Source: [Bento et al.](https://arxiv.org/abs/astro-ph/0210375). |
| K-essence unified DM | Purely kinetic scalar models can yield \(\rho=\rho_0+\rho_1a^{-3}\) and \(c_s^2\ll1\). | QFUDS has no scalar action yet. | Yes. The cleanest micro-toy model is Scherrer-type purely kinetic k-essence. Source: [Scherrer 2004](https://arxiv.org/abs/astro-ph/0402316). | No, unless foam microphysics fixes the k-essence function \(P(X)\). |
| Scalar Field / Fuzzy DM | Uses coherent fields/condensates; can form halos and modify small scales. | Fuzzy DM has de Broglie/quantum pressure scale and no dark-energy phase by default. | Partially, if phase A is an ultralight scalar condensate. | Only if phase B emerges from same condensate without tuning. Source: [Hu, Barkana, Gruzinov](https://arxiv.org/abs/astro-ph/0003365). |
| Superfluid DM | Phase language, condensate, phonons, halo-scale phenomenology. | Superfluid DM is usually a galactic phase of dark matter, not a unified dark-energy sector. | Partially for phase A. | Possible if QFUDS predicts a cosmic vacuum-pressure phase from the same condensate. Source: [Berezhiani et al. review](https://arxiv.org/abs/2505.23900). |
| Emergent Gravity | Information/entropy language, horizon thermodynamics, dark phenomenology. | Emergent gravity modifies gravitational response; QFUDS keeps GR intact unless forced. | No, unless QFUDS drops GR and makes dark matter an apparent force. | Not in the conservative GR version. Source: [Verlinde 2016](https://arxiv.org/abs/1611.02269). |
| Loop Quantum Cosmology | Quantum geometry and possible bounce/remnant ideas. | LQC modifies early-universe gravitational dynamics; QFUDS is a late-time dark-sector fluid. | No direct reduction. | Only if foam variables are derived from LQG/LQC states. Source: [Ashtekar overview](https://arxiv.org/abs/0812.0177). |
| White-hole remnant DM | Optional topological defects can behave as cold relics. | Remnants are compact objects, not a smooth vacuum phase. | Phase-defect submodel only. | Not unless QFUDS predicts relic mass spectrum and abundance. Source: [Rovelli and Vidotto](https://arxiv.org/abs/1805.03872). |
| Black-hole to white-hole tunneling | Interprets black holes as information-compression nodes with possible tunneling. | Tunneling models do not generate cosmic acceleration by themselves. | Optional defect dynamics only. Source: [Haggard and Rovelli](https://arxiv.org/abs/1407.0989). | Not for the unified dark sector. |
| Holographic cosmology / HDE | Vacuum pressure tied to horizon/information bounds. | HDE typically sets \(\rho_{\rm DE}\sim M_P^2L^{-2}\); QFUDS has no cutoff prescription. | Possible if phase B is fixed by a holographic IR cutoff. Sources: [Cohen, Kaplan, Nelson](https://arxiv.org/abs/hep-th/9803132), [Li 2004](https://arxiv.org/abs/hep-th/0403127). | Only if foam gives a new cutoff law. |
| Dynamical Dark Energy | Deviations \(w(a)\neq -1\), possible \(w_0w_a\) fits. | QFUDS links dynamics to matter phase transfer. | Yes as interacting or coupled dark energy. | Mild, if transfer is derived and constrained. |
| DESI dark-energy analyses | DESI motivates tests of \(w(z)\) and possible phantom crossing. | DESI does not imply a unified foam. | QFUDS can be fit as a transfer model or effective \(w(z)\). | Only if it predicts DESI-favored behavior before fitting. |

Classification:

- A: Already known in broad form as unified dark fluid/k-essence/interacting dark sector.
- B: Reparameterization in the minimal two-phase version.
- C: Special case of k-essence or coupled vacuum plus CDM if a transfer law is chosen.
- D: Potentially novel only with derived foam microphysics or defect statistics.
- E: Internally inconsistent if it demands a single adiabatic barotropic fluid with \(w\to-1\) and \(c_s^2\to0\) without entropy perturbations or noncanonical dynamics.

## 3. Mathematical Formulation

### Effective action

The least-commitment GR-compatible action is

```math
S=\int d^4x\sqrt{-g}\left[\frac{M_{\rm Pl}^2}{2}R+\mathcal{L}_A+\mathcal{L}_B+\mathcal{L}_{\rm int}\right]+S_b+S_r .
```

For a fully covariant toy model, use a purely kinetic k-essence field:

```math
X=-\frac{1}{2}g^{\mu\nu}\partial_\mu\phi\partial_\nu\phi,\qquad
\mathcal{L}_{\phi}=P(X)=-\rho_\Lambda+\frac{M^4}{2}\left(\frac{X-X_0}{X_0}\right)^2 .
```

Then

```math
T_{\mu\nu}=P_X\partial_\mu\phi\partial_\nu\phi+P g_{\mu\nu},
\qquad
\rho=2XP_X-P,
\qquad
p=P.
```

Writing \(y=(X-X_0)/X_0\),

```math
p=-\rho_\Lambda+\frac{M^4}{2}y^2,\qquad
\rho=\rho_\Lambda+2M^4y+\frac{3M^4}{2}y^2 .
```

Near the kinetic extremum \(y\ll1\), the shift-current equation gives \(y\propto a^{-3}\), so

```math
\rho\simeq \rho_\Lambda+\rho_{m0}a^{-3},\qquad p\simeq-\rho_\Lambda,\qquad
c_s^2=\frac{P_X}{P_X+2XP_{XX}}\simeq\frac{y}{2}.
```

This is mathematically consistent and shows why QFUDS is close to known k-essence unified dark matter.

### Two-phase effective fluid

For computation, the most transparent model is two effective phases:

```math
T_i^{\mu\nu}=(\rho_i+p_i)u_i^\mu u_i^\nu+p_i g^{\mu\nu},
\qquad i=A,B.
```

Set

```math
w_A=0,\quad c_{s,A}^2=0,\qquad w_B=-1,\quad \delta_B=0
```

unless testing deviations.

Allow phase conversion:

```math
\nabla_\mu T_A^{\mu\nu}=Q^\nu,\qquad
\nabla_\mu T_B^{\mu\nu}=-Q^\nu,\qquad
Q^\nu=-Q u^\nu_A .
```

In the homogeneous background, with \(x=\ln a\),

```math
\rho_A'+3\rho_A=-\Gamma(a)\rho_A,\qquad
\rho_B'=\Gamma(a)\rho_A,\qquad
\Gamma(a)=\gamma_0 a^\beta .
```

The Friedmann equation is

```math
H^2(a)=\frac{8\pi G}{3}\left[
\rho_r^0a^{-4}+\rho_b^0a^{-3}+\rho_A(a)+\rho_B(a)
\right].
```

The total dark-sector equation of state is

```math
w_{\rm dark}(a)=\frac{p_A+p_B}{\rho_A+\rho_B}=-\frac{\rho_B}{\rho_A+\rho_B}.
```

The adiabatic sound speed of the combined dark fluid is not generally the physical clustering sound speed. If treated as one adiabatic barotropic fluid,

```math
c_a^2=\frac{p'_{\rm dark}}{\rho'_{\rm dark}},
```

which is dangerous near \(w\to-1\). The model must instead be nonadiabatic or multi-component so that phase A has \(c_{s,A}^2\simeq0\) while phase B remains smooth.

### Perturbations

In Newtonian gauge and subhorizon limit, if phase B is smooth and phase A is CDM-like:

```math
\delta_A'=-\theta_A/H+\text{metric and transfer terms},
\qquad
\theta_A'+\left(1+\frac{H'}{H}\right)\theta_A-k^2\Psi/H=0 .
```

The scale-independent growth approximation used in this repository is

```math
D''+\left[2+\frac{d\ln H}{d\ln a}\right]D'
-\frac{3}{2}\Omega_{\rm cl}(a)D=0,
```

where primes are \(d/d\ln a\) and

```math
\Omega_{\rm cl}(a)=\frac{\rho_b+\rho_A}{\rho_{\rm crit}(a)} .
```

A full Boltzmann implementation must include transfer perturbations:

```math
\delta_A' = -\theta_A + 3\Phi' - \frac{Q}{H\rho_A}(\Phi+\delta_A-\delta_Q),
```

with a clearly specified \(\delta_Q\). This is a hidden assumption in many coupled-fluid models.

### Halo formation

Halo formation requires:

```math
c_{s,A}^2 k^2/a^2 \ll 4\pi G\rho_{\rm cl}
```

on halo scales, or equivalently the Jeans scale must sit below the smallest observed CDM-like structures. If phase A is a scalar/BEC, quantum pressure introduces

```math
k_J(a)\sim a(16\pi G\rho m^2)^{1/4},
```

and Lyman-alpha/halo constraints force the particle mass or effective stiffness into the usual fuzzy-DM bounds.

### Conditions

- \(w\simeq0\): \(\rho_A\gg\rho_B\), \(p_A\simeq0\), phase B dynamically negligible.
- \(w\simeq-1\): \(\rho_B\gg\rho_A\), \(\rho_B'\simeq0\), perturbations in B suppressed.
- \(c_s^2\simeq0\): phase A is dust-like, or k-essence sits near a kinetic extremum with \(P_X/(P_X+2XP_{XX})\ll1\).
- Exact LCDM: \(\Gamma=0\), \(w_A=0\), \(c_{s,A}^2=0\), \(w_B=-1\), \(\delta_B=0\), no anisotropic stress, no remnant abundance affecting expansion.
- Deviations from LCDM: \(\Gamma(a)\neq0\), \(w_B\neq-1\), \(c_{s,A}^2>0\), clustered phase B, nonzero anisotropic stress, topological-defect abundance, or modified gravity.

### Hidden assumptions

1. GR remains valid on cosmological and halo scales.
2. The foam stress tensor is local and covariantly conserved.
3. The phase split is physical, not gauge bookkeeping.
4. Phase A has negligible pressure and viscosity.
5. Phase B is stable against perturbations despite \(w\simeq-1\).
6. The combined fluid is nonadiabatic or multi-component; otherwise sound-speed constraints are severe.
7. Phase transfer does not produce negative \(\rho_B\) at high redshift.
8. Baryons couple only gravitationally.
9. Black/white-hole remnants are subdominant unless separately modeled.
10. No fifth force violates lensing, binary pulsar, gravitational-wave, or equivalence-principle constraints.

## 4. Computational Implementation

Implemented files:

- `qfuds/background.py`
  - `CosmologyParams`: present-day flat cosmological parameters.
  - `QFUDSParams`: \(\gamma_0\), \(\beta\), and \(c_{s,A}^2\).
  - `integrate_background`: RK4 integration of \(\rho_A,\rho_B,H(a),\Omega(a),w(a)\).
- `qfuds/growth.py`
  - `integrate_growth`: solves the GR subhorizon growth equation for smooth phase B.
- `scripts/run_minimal_model.py`
  - CLI runner that writes CSV outputs.
- `outputs/qfuds_gamma0_beta0.csv`
  - exact LCDM-limit numerical output.
- `outputs/qfuds_gamma0.03_beta5.csv`
  - small late-time phase-transfer example with positive phase-B density.

Verified commands:

```bash
python3 scripts/run_minimal_model.py --gamma0 0 --beta 0
python3 scripts/run_minimal_model.py --gamma0 0.03 --beta 5
```

The environment lacked `matplotlib`, so plots were skipped. CSV outputs were produced.

### CLASS integration strategy

For stock CLASS 3.x, the modifications belong in these code surfaces:

- `include/background.h`: add QFUDS parameters and indices for \(\rho_A,\rho_B\).
- `source/input.c`: parse `qfuds_gamma0`, `qfuds_beta`, `qfuds_cs2_a`.
- `source/background.c`: add background initial conditions and derivatives for \(\rho_A,\rho_B\) in `background_derivs`; add contributions to total density and pressure.
- `include/perturbations.h`: add perturbation variables for phase A and optionally phase B.
- `source/perturbations.c`: add continuity/Euler equations for phase A and transfer terms; keep phase B smooth for the minimal case or implement DE-fluid perturbations for \(w_B\neq-1\).
- `explanatory.ini`: document parameters and default `qfuds_gamma0 = 0`.

Minimal first target: implement phase A as an interacting CDM-like species and phase B as vacuum energy with background exchange only. Then compare CMB and matter power spectra against LCDM for \(\gamma_0=0\) to machine precision.

### CAMB integration strategy

For current CAMB-style Fortran/Python workflows, the modifications belong in:

- `model.f90`: add QFUDS parameters to the cosmological parameter type.
- `equations.f90`: add background density evolution and perturbation derivatives.
- `DarkEnergyInterface.f90` or the active dark-energy module in the checkout: add an effective \(w(a)\) or interacting vacuum implementation if using the dark-energy abstraction.
- Python wrapper parameter definitions: expose `qfuds_gamma0`, `qfuds_beta`, `qfuds_cs2_a`.
- Regression tests: verify `gamma0=0` reproduces existing LCDM spectra.

Do not implement QFUDS as only a fitted \(w(a)\) if the claim is unified dark sector; that loses the clustering phase and makes the model just dynamical dark energy.

## 5. Observational Predictions

| Probe | Expected signal | Existing constraints | Survives? |
| --- | --- | --- | --- |
| Planck CMB | Same acoustic peaks in LCDM limit; deviations alter equality, ISW, lensing. | Planck strongly supports base LCDM and tight \(\Omega_ch^2\), \(N_{\rm eff}\), \(\sum m_\nu\). | Only if \(\Gamma\), early dark energy, and sound speed are tiny. |
| BAO | Modified \(H(z)\), \(D_M(z)\), \(D_H(z)\). | DESI DR2 gives precise BAO and hints of evolving DE when combined with other probes. | Possible if QFUDS predicts low-z \(w(z)\) behavior without spoiling CMB. |
| DESI | Phase transfer can mimic \(w_0w_a\) and phantom crossing in effective reconstruction. | DESI extended analysis favors models with phantom crossing but alternatives are not ruled out. | Survives as a fit target, not as evidence. |
| Euclid | Weak lensing and growth-history deviations. | First Euclid weak-lensing demonstrations are appearing; first cosmology results expected in 2027 [Euclid](https://www.euclid-ec.org/euclid-starts-seeing-darkness/). | Strong future test. |
| Weak lensing | Changes \(S_8\), growth rate, lensing power. | Current surveys already constrain clustering amplitude and smooth-DE assumptions. | Survives if growth remains CDM-like. |
| Structure formation | Suppressed or enhanced growth if phase A decays or has pressure. | Lyman-alpha, clusters, galaxy clustering punish large sound speed or late CDM depletion. | Narrow parameter space. |
| Halo profiles | If phase A is superfluid/fuzzy, cores, vortices, phonons, or solitons. | Core-size and Lyman-alpha constraints are model-dependent but severe. | Only with specified particle/medium scale. |
| Rotation curves | Possible MOND-like or cored behavior if phase A has superfluid phonons. | Must still fit clusters and Bullet Cluster-like lensing. | Not predicted by the minimal model. |
| Direct DM detection | Null if purely gravitational foam; possible signal if phase A has particles. | Current null results constrain WIMP-like couplings, not gravitational fluids. | Survives by being hard to detect, but loses particle specificity. |
| Black-hole information | Remnants must not overproduce entropy, gamma rays, microlensing, or merger signatures. | White-hole remnants are speculative and constrained as compact dark relics. | Only as subdominant optional component. |

## 6. Failure Modes

Severity ranking:

1. Critical: no microscopic action or phase law. Without this, QFUDS is terminology over existing models.
2. Critical: single adiabatic unified fluid with \(w\to-1\) generally has non-negligible sound speed and suppresses structure. This killed many simple quartessence models.
3. Critical: phase transfer can make \(\rho_B<0\) at high redshift unless \(\Gamma(a)\) is restricted. The code exposes this directly for some parameter choices.
4. High: exact LCDM limit is too easy. If all successful predictions occur only at \(\Gamma=0\), the model has no new content.
5. High: DESI degeneracy. A fitted \(w(a)\) does not identify foam; many dynamical-DE and interacting-DE models can mimic it.
6. High: black-hole remnant add-on is disconnected from the smooth dark-energy phase unless abundance and coupling are derived.
7. Medium: direct detection evasion is not a prediction.
8. Medium: halo improvements require extra microphysics, usually scalar/superfluid/fuzzy, bringing known constraints.
9. Medium: if GR is modified, gravitational-wave speed and lensing constraints enter immediately.
10. Low: terminology risk. "Quantum foam" is evocative but currently not an observable variable.

Hostile referee summary:

The manuscript would be rejected in its current conceptual form. The proposed unification is already present in generalized dark fluids and k-essence. The terms "foam", "information-compression node", and "phase" are not yet attached to gauge-invariant degrees of freedom or a falsifiable Lagrangian. The only mathematically clean version either reproduces LCDM exactly or becomes a coupled dark-sector model whose parameters must be tightly constrained by existing CMB, BAO, and growth data.

## 7. Novel Contributions

Potentially novel components, if developed:

1. A nonadiabatic two-phase medium where the background acts like unified dark fluid but only phase A clusters. This is not entirely new, but can be packaged cleanly.
2. A derived phase-transfer function \(\Gamma(a,\rho,\mathcal{I})\), where \(\mathcal{I}\) is a real information/entropy scalar rather than metaphor.
3. A joint treatment of smooth phases plus compact black/white-hole remnants with a common topological origin.
4. A prediction that DESI-like low-redshift \(w(z)\) evolution comes with a correlated growth/lensing signature.
5. A foam-derived sound-speed suppression mechanism that avoids Chaplygin-gas oscillations without simply importing k-essence.

Not novel by itself:

- "Dark matter and dark energy are one medium."
- "One component behaves like dust and another like vacuum."
- "Black-hole remnants may be dark matter."
- "Information/holography is related to dark energy."

## 8. Recommended Next Research Steps

1. Decide whether QFUDS is a phenomenological model or a microscopic theory. Do not mix both standards in one claim.
2. Use the implemented two-phase model as the baseline null. Fit only \(\gamma_0,\beta\) first.
3. Enforce viability priors:

```math
\rho_A(a)>0,\quad \rho_B(a)>0,\quad c_{s,A}^2<10^{-6}\ \text{on structure scales},\quad
|\Omega_{\rm early\,B}| \ll 10^{-2}.
```

4. Derive an effective \(w_{\rm eff}(a)\) from \(\Gamma(a)\):

```math
w_{B,\rm eff}=-1-\frac{\Gamma\rho_A}{3\rho_B}.
```

This can cross phantom without a phantom scalar because it is an interacting-vacuum effective equation of state, not a fundamental \(w<-1\) field.

5. Implement a CLASS branch and require:
   - `gamma0=0` matches LCDM CMB and \(P(k)\);
   - nonzero `gamma0` changes BAO/growth in a documented direction;
   - no unstable perturbations.
6. Fit to public likelihoods in this order: background-only BAO/SN, then Planck distance priors, then full Planck/ACT/lensing, then growth.
7. Only after the fluid survives, add remnant defects with parameters:

```math
f_{\rm rem},\quad M_{\rm rem},\quad \frac{dn}{dM},\quad \tau_{\rm tunnel}(M).
```

8. Define one falsifiable QFUDS-specific prediction, for example:

```math
\Delta f\sigma_8(z) = F[\Delta w(z)]
```

with no extra free function. Without this, QFUDS remains a reparameterization.
