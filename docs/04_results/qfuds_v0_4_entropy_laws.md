# QFUDS v0.4: Entropy-Derived Phase-Transfer Laws

Date: 2026-06-08

## 1. Executive Summary

The v0.4 question is whether the phase-transfer law can be derived as

```math
\Gamma(a)=\lambda {dS\over d\ln a}
```

or

```math
\Gamma(a)=\lambda {dI\over d\ln a}
```

instead of fitted as an arbitrary function.

Hostile verdict:

1. Apparent-horizon entropy is mathematically clean, but it is a background-expansion quantity. It does not derive a dark-energy and structure-formation relation. It reduces to ordinary horizon/interacting dark-energy phenomenology.
2. HBM/KL gravitational entropy is known in the literature, but the simple linear-variance version is too broad in time. In the current two-phase boundary-value model it drives past `rho_B` negative unless the amplitude is so tiny that the signal is effectively irrelevant.
3. Black-hole entropy is real physics, but total cosmic `S_BH(a)` is not available without a black-hole mass function and accretion history. The current v0.3 black-hole law remains a proxy, not a derivation.
4. Nonlinear collapse and information production are the only surviving v0.4 directions. A Press-Schechter-derived `dF_coll/dln a` naturally vanishes in the radiation era and peaks after nonlinear structure formation begins.
5. A strict local relation `Delta f sigma8(z)=F(Delta w(z))` does not exist generically. A nonlocal functional relation does exist after a specific entropy source is fixed. For Press-Schechter information production, a redshift-shape relation can be written without a free shape function, but it still contains a coupling amplitude and a mass-threshold choice unless QFUDS microphysics fixes them.

Recommendation: continue only the collapse/information-production branch. Terminate the broad entropy-language version unless it supplies a real `S(a)` from a mass function or microscopic state count.

## 2. Entropy Candidates

| Candidate | Mathematical entropy | Literature status | Gamma source | Low-z peak? | Radiation-era behavior | Model class |
| --- | --- | --- | --- | --- | --- | --- |
| Total black-hole entropy | `S_BH = sum_i k_B A_i/(4 l_P^2) = sum_i 4 pi k_B G M_i^2/(hbar c)` for Schwarzschild holes | Known: Bekenstein-Hawking area entropy. See Bekenstein 1973 and black-hole mechanics. | `Gamma proportional to dS_BH/dln a`, requiring BH mass and accretion history | Yes, if SMBH growth dominates | Yes, if no primordial BH population dominates | Potentially distinct only if `S_BH(a)` is predicted |
| Gravitational entropy | HBM/KL: `S_HBM(D)=int_D rho ln(rho/<rho>_D) dV`; linear limit `S/V proportional to <delta^2>/2` | Known: Hosoya-Buchert-Morita relative information entropy; CET/Weyl proposals also exist | `Gamma proportional to d(D^2)/dln a` in the implemented weak-contrast proxy | No useful narrow peak; broad late growth | Numerically tiny in radiation era, but active through matter era | Interacting dark energy unless nonlinear entropy closes perturbations |
| Horizon information | Flat apparent horizon: `S_H = k_B A/(4 l_P^2) = pi k_B/(G hbar H^2)` | Known in horizon thermodynamics and holographic dark energy | `Gamma proportional to d(S_H/S_H0)/dln a` | Peaks at low z in the normalized absolute-entropy version | Yes, because `S_H/S_H0 -> 0` as `H -> infinity` | Standard interacting or holographic dark energy |
| Nonlinear collapse entropy | `F_coll(>M,a)=erfc[delta_c/(sqrt(2) sigma_M D(a))]` | Known Press-Schechter collapse statistics | `Gamma proportional to dF_coll/dln a` | Yes, near selected collapse threshold | Yes, exponentially suppressed | Potentially distinct if mass threshold is fixed physically |
| Information production | `I(a)` as information encoded into collapsed structures; minimal computable choice `I proportional to F_coll` | Partly known as KL/relative entropy and halo statistics; not a unique entropy | Same as Press-Schechter `dF_coll/dln a` in this implementation | Yes | Yes | Best v0.4 branch, still incomplete |

Sources used for literature anchors:

- Bekenstein, "Black Holes and Entropy", Phys. Rev. D 7, 2333, 1973: https://doi.org/10.1103/PhysRevD.7.2333
- Bardeen, Carter, Hawking, "The four laws of black hole mechanics", Commun. Math. Phys. 31, 161, 1973: https://projecteuclid.org/journals/communications-in-mathematical-physics/volume-31/issue-2/The-four-laws-of-black-hole-mechanics/cmp/1103858973.pdf
- Hosoya, Buchert, Morita, "Information Entropy in Cosmology", Phys. Rev. Lett. 92, 141302, 2004: https://arxiv.org/abs/gr-qc/0402076
- Clifton and Ellis, "A Gravitational Entropy Proposal", Class. Quant. Grav. 30, 125009, 2013: https://arxiv.org/abs/1303.5612
- Press and Schechter, "Formation of Galaxies and Clusters of Galaxies by Self-Similar Gravitational Condensation", ApJ 187, 425, 1974: https://adsabs.harvard.edu/pdf/1974ApJ...187..425P
- Madau and Dickinson, "Cosmic Star-Formation History", ARAA 52, 415, 2014: https://doi.org/10.1146/annurev-astro-081811-125615
- Cai and Kim, "First Law of Thermodynamics and Friedmann Equations of FRW Universe", JHEP 0502, 050, 2005: https://arxiv.org/abs/hep-th/0501055
- Cohen, Kaplan, Nelson, "Effective Field Theory, Black Holes, and the Cosmological Constant", PRL 82, 4971, 1999: https://arxiv.org/abs/hep-th/9803132
- Li, "A Model of Holographic Dark Energy", Phys. Lett. B603, 1, 2004: https://arxiv.org/abs/hep-th/0403127

## 3. Mathematical Derivations

The background system remains:

```math
{d\rho_A\over d\ln a}+3\rho_A=-\Gamma(a)\rho_A,
\qquad
{d\rho_B\over d\ln a}=\Gamma(a)\rho_A.
```

For any derived source `X(a)`:

```math
\Gamma(a)=\gamma_0 {dX/d\ln a\over \max(dX/d\ln a)}
```

in the numerical code. This normalization keeps only the derived shape. `gamma0` is still a coupling amplitude, not a shape function.

### Black-Hole Entropy

For nonspinning black holes:

```math
S_BH(a)=\int dM\, {dn_BH\over dM}(M,a)
{4\pi k_B G M^2\over \hbar c}.
```

Then:

```math
\Gamma_BH(a)=\lambda {dS_BH\over d\ln a}.
```

This is physically meaningful but not computable from the current repo. It needs `dn_BH/dM`, mergers, accretion, and possible primordial-BH initial conditions. The existing `black_hole_entropy_proxy` is therefore only a late logistic SMBH-growth proxy.

### HBM/KL Gravitational Entropy

HBM relative entropy on a compact domain `D`:

```math
S_HBM(D)=\int_D \rho \ln{\rho\over <\rho>_D} dV.
```

For `rho=<rho>(1+delta)` and `|delta| << 1`:

```math
S_HBM/V \simeq {<\rho>\over 2}<\delta^2>
\propto D^2(a).
```

The implemented law is:

```math
\Gamma_grav(a)=\gamma_0
{dD^2/d\ln a\over \max(dD^2/d\ln a)}.
```

This is a derivation from a known information measure, but it is not a good QFUDS law. It is active too broadly across matter domination.

### Horizon Information

For a flat FRW apparent horizon `R_A=1/H`:

```math
S_H={k_B A\over 4l_P^2}\propto H^{-2}.
```

Using absolute entropy growth rather than the v0.3 logarithmic derivative:

```math
{d(S_H/S_{H0})\over d\ln a}
= {H_0^2\over H^2}
\left(-2{d\ln H\over d\ln a}\right).
```

Thus:

```math
\Gamma_H(a)=\gamma_0
{(H_0^2/H^2)(-2d\ln H/d\ln a)\over
\max[(H_0^2/H^2)(-2d\ln H/d\ln a)]}.
```

This naturally vanishes in the radiation era because `H0^2/H^2` is tiny. But it is a background horizon law, not a structure-production law.

### Press-Schechter Information Production

For a mass threshold `M`:

```math
F_coll(>M,a)=erfc\left({\nu(a)\over \sqrt{2}}\right),
\qquad
\nu(a)={\delta_c\over \sigma_M D(a)}.
```

Then:

```math
{dF_coll\over d\ln a}
=\sqrt{2\over\pi}\,\nu e^{-\nu^2/2}
{d\ln D\over d\ln a}.
```

The implemented law is:

```math
\Gamma_I(a)=\gamma_0
{dF_coll/d\ln a\over \max(dF_coll/d\ln a)}.
```

This is the cleanest v0.4 candidate because it directly ties phase transfer to nonlinear structure statistics.

## 4. Numerical Results

Implemented:

- `gamma_gravitational_entropy`
- `gamma_information_production`
- `gamma_horizon_information`

Updated files:

- `qfuds/gamma_laws.py`
- `scripts/run_minimal_model.py`
- `qfuds/diagnostics.py`

Generated outputs:

- `outputs/qfuds_gravitational_entropy_gamma0.003_beta0.csv`
- `outputs/qfuds_gravitational_entropy_gamma0.003_beta0.png`
- `outputs/qfuds_information_production_gamma0.02_beta0.csv`
- `outputs/qfuds_information_production_gamma0.02_beta0.png`
- `outputs/qfuds_horizon_information_gamma0.03_beta0.csv`
- `outputs/qfuds_horizon_information_gamma0.03_beta0.png`

Comparison suite:

| Law | gamma0 | peak z | Gamma(a=1e-4) | min rho_B | max early `|H/H_LCDM-1|` | max all `|H/H_LCDM-1|` | Delta f sigma8 z=0 | Delta f sigma8 z=1 | Delta w z=1 |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| collapsed_fraction_toy | 0.03 | 1.86 | 2.28e-19 | 0.386 | 0.00784 | 0.010 | 0.000750 | 0.00147 | 0.00178 |
| black_hole_entropy_proxy | 0.03 | 1.86 | 6.53e-23 | 0.489 | 0.00654 | 0.00838 | 0.000588 | 0.00128 | 0.00115 |
| star_formation_proxy | 0.003 | 1.86 | 3.30e-13 | 0.197 | 0.00106 | 0.00135 | 0.000116 | 0.000177 | 0.000323 |
| gravitational_entropy | 0.003 | 0.0966 | 2.35e-11 | -11.8 | 0.000939 | 0.00120 | 0.000249 | 0.000130 | 0.000737 |
| information_production | 0.02 | 2.05 | 0 | 0.240 | 0.00939 | 0.0120 | 0.00128 | 0.00144 | 0.00375 |
| horizon_information | 0.03 | 0.298 | 8.32e-14 | 0.153 | 0.00901 | 0.0115 | 0.00252 | 0.00133 | 0.00780 |

The HBM/KL `gravitational_entropy` row fails positivity. A sweep showed it needs roughly `gamma0 <= 1e-4` to keep `rho_B>0`, at which point the observable signal is negligible in this toy setup.

## 5. LCDM Comparison

The LCDM limit remains exact at `gamma0=0`.

For surviving v0.4 candidates:

- `information_production` is quiet during radiation domination and peaks near `z ~= 2.05`.
- `horizon_information` is also quiet during radiation domination, but peaks near `z ~= 0.30` because it is driven by horizon-area growth, not collapse.
- `collapsed_fraction_toy`, `black_hole_entropy_proxy`, and `star_formation_proxy` remain the useful v0.3 comparisons because they are low-redshift and structure-gated.

The current `f sigma8` is still a proxy from the smooth-B, clustered-A growth equation. It is not a full Boltzmann result.

## 6. Distinguishing Predictions

Let

```math
w(a)=-{\rho_B\over \rho_A+\rho_B}.
```

Then any measured dark-sector `w(a)` implies a transfer function:

```math
\Gamma_w(a)={-w'(a)+3w(a)[1+w(a)]\over 1+w(a)}.
```

For Press-Schechter information production:

```math
\Gamma_w(a)=\lambda
\sqrt{2\over\pi}\,\nu(a)e^{-\nu^2(a)/2}f(a),
```

with

```math
f(a)={d\ln D\over d\ln a},
\qquad
f\sigma_8(a)=\sigma_{8,0}D(a)f(a).
```

Therefore:

```math
f\sigma_8(a)=
{\sigma_{8,0}D(a)\Gamma_w(a)\over
\lambda\sqrt{2/\pi}\,\nu(a)e^{-\nu^2(a)/2}}.
```

This is the desired structure-DE relation, but only after `lambda`, `sigma_M`, and the perturbation prescription are fixed. Ratios at two redshifts can eliminate `lambda`:

```math
{\Gamma_w(a_1)\over \Gamma_w(a_2)}
=
{\nu_1 e^{-\nu_1^2/2}f(a_1)\over
\nu_2 e^{-\nu_2^2/2}f(a_2)}.
```

That is the cleanest testable v0.4 signature. It is not a local universal `Delta f sigma8(z)=F(Delta w(z))`; it is a nonlocal consistency relation between `w(a)`, collapse statistics, and growth.

## 7. Failure Modes

1. If `Gamma(a)` is any free curve, QFUDS is just interacting dark energy.
2. If the entropy source is horizon area alone, QFUDS is standard horizon/interacting dark-energy phenomenology.
3. If the entropy source is HBM/KL linear variance, the transfer is too broad and can destroy the backward-integrated `rho_B`.
4. If total black-hole entropy is invoked without an actual `dn_BH/dM`, it is a story, not a derivation.
5. If `I(a)` is not defined independently of the desired `Gamma(a)`, the derivation is circular.
6. If phase-B perturbations and transfer perturbations are not specified, `f sigma8` and CMB claims are not physically complete.
7. If the collapse mass threshold is fitted after looking at `w(z)`, the Press-Schechter law becomes another fitting function.

## 8. Most Promising v0.4 Direction

The best surviving direction is:

```math
\Gamma(a)\propto {dF_coll(>M,a)\over d\ln a}
```

or the same law interpreted as information production:

```math
I(a)\propto F_coll(>M,a).
```

This direction is worth continuing because it:

- vanishes in radiation domination,
- peaks after nonlinear structure formation begins,
- connects directly to growth observables,
- gives a falsifiable consistency relation between `w(a)` and `f sigma8(a)`.

The black-hole-entropy branch remains secondary until the repo ingests an actual cosmic black-hole mass/accretion history.

## 9. Recommendation: Continue or Terminate QFUDS

Continue only as a narrow v0.4 interacting-vacuum model with a derived collapse/information-production source. Terminate the broader claim that "entropy production" by itself explains dark energy.

Next technical step:

1. Replace the LCDM-source Press-Schechter approximation with self-consistent QFUDS growth `D(a)`.
2. Choose one physical mass threshold or derive it from foam microphysics.
3. Add transfer perturbations.
4. Fit background `w(a)` and `f sigma8(a)` jointly.
5. Kill the model if the redshift-ratio relation above fails.
