---
doc_id: asset_lacy_2024_smbh_accretion_coupling_constraints_pageindex_fulltext
title: "Lacy et al. 2024 — PageIndex Full-Text Extraction"
doc_type: reference
stage: reference
status: reference
evidence_role: reference
depends_on:
  - asset_lacy_2024_smbh_accretion_coupling_constraints_digitization_index
next_gate: targeted manual verification before numerical reuse
last_updated: 2026-06-11
---

# Lacy et al. 2024 — PageIndex Full-Text Extraction

Verbatim page-by-page text extraction of arXiv:2312.12344v1 via PageIndex MCP
`get_page_content` (8 pages). Quality: `source_text_parse` — faithful text and
LaTeX-equation extraction, higher fidelity than the MarkItDown conversion, but
machine-extracted and not manually verified line-for-line. Figure image links
resolve to the repo PNG mirrors under `../figures/extracted/`. Mapping:
Figure 1 → `scenario1_revised.png`; Figure 2 → `Salpeter_plot_revised.png`.

---

## Page 1

# Constraints on cosmological coupling from the accretion history of supermassive black holes

Mark Lacy, Athena Engholm, Duncan Farrah, Kiana Ejercito (NRAO)

###### Abstract

Coupling of black hole mass to the cosmic expansion has been suggested as a possible path to understanding the dark energy content of the Universe. We test this hypothesis by comparing the supermassive black hole (SMBH) mass density at $z=0$ to the total mass accreted in AGN since $z=6$, to constrain how much of the SMBH mass density can arise from cosmologically-coupled growth, as opposed to growth by accretion. Using an estimate of the local SMBH mass density of $\approx 1.0\times 10^{6}\,\mathrm{M}_{\odot}\,\mathrm{Mpc}^{-1}$, a radiative accretion efficiency, $\eta$: $0.05<\eta<0.3$, and the observed AGN luminosity density at $z\approx 4$, we constrain the value of the coupling constant between the scale size of the Universe and the black hole mass, $k$, to lie in the range $0<k\lesssim 2$, below the value of $k=3$ needed for black holes to be the source term for dark energy. Initial estimates of the gravitational wave background using pulsar timing arrays, however, favor a higher SMBH mass density at $z=0$. We show that if we adopt such a mass density at $z=0$ of $\approx 7.4\times 10^{6}\,\mathrm{M}_{\odot}\,\mathrm{Mpc}^{-1}$, this makes $k=3$ viable even for low radiative efficiencies, and may exclude non-zero cosmological coupling. We conclude that, although current estimates of the SMBH mass density based on the black hole mass – bulge mass relation probably exclude $k=3$, the possibility remains open that, if the GWB is due to SMBH mergers, $k>2$ is preferred.

Supermassive black holes (1663): Luminosity function (942): Active Galactic Nuclei (16)

## 1 Introduction

### 1.1 The Soltan Argument

There exists an elegant argument for constraining the growth of supermassive black hole (SMBH) mass in galaxies via accretion. Soltan (1982) showed that the integral of the AGN luminosity density over cosmic history gives an estimate of the total accreted mass onto SMBHs, which can be compared to the local mass density of SMBHs to constrain how they grow. This relation, between two independently derived quantities, can give excellent constraints on both AGN physics and the nature of SMBHs themselves. For example, using then available data, Soltan (1982) showed that the history of accreted mass is close to the local SMBH mass density, if a radiative efficiency of $\eta\approx 0.1$ is assumed. This range in $\eta$ is in good agreement with other estimates. Theoretical arguments give a range of $0.05\lesssim\eta\lesssim 0.43$, depending on the spin of the black hole (BH) (Bardeen, 1970; Thorne, 1974). This range is itself in good agreement with most other studies, which find values in the range $0.1\lesssim\eta\lesssim 0.3$ (e.g. Yu & Tremaine, 2002; Elvis et al., 2002; Hopkins et al., 2007; Shankar et al., 2009; Lacy et al., 2015; Zhang & Lu, 2017; Shankar et al., 2020; Shen et al., 2020; Farrah et al., 2022). This consistency argues for the increase in SMBH mass density with cosmic time to be driven by accretion.

### 1.2 Cosmologically-coupled black holes

For several decades it has been recognized that BHs with non-singular interiors (including 'dark energy'-like interiors) may have exteriors identical to BHs with interior singularities (e.g. Gliner, 1966; Dymnikova, 1992; Faraoni & Jacques, 2007; Beltracchi & Gondolo, 2019; Cadoni et al., 2023a). Recently, however, it was realized that the masses of non-singular BHs could be affected by the cosmic expansion (Croker & Weiner, 2019). Indeed, in a recent paper, Cadoni et al. (2023b) show that such

## Page 2

a coupling is necessary in General Relativity (GR) if BHs do not contain singularities. Thus the detection of a non-zero cosmological coupling would have important implications for our understanding of BHs.

The mass coupling between BHs and the cosmic expansion can be parameterized via:

$M_{\bullet}(a)=M_{\bullet}(a_{i})\left(\frac{a}{a_{i}}\right)^{k}$ (1)

(Croker et al., 2020, 2021) in which $M_{\bullet}(a)$ and $M_{\bullet}(a_{i})$ are the BH mass at some later and earlier times respectively, $a$ and $a_{i}$ are the scale factors at those times ($a=(1+z)^{-1}$ at redshift $z$), and $k$ is the cosmological coupling strength, with $-3\leq k\leq 3$ from a causality constraint.

Croker and Weiner (2019) show that the value of $k$ is related to the equation of state of the medium internal to the BH. Expressing the equation of state as $p=w\rho$, where $p$ is the pressure and $\rho$ the density, Croker et al. (2021) show that $k=-3w$. Thus, for vacuum energy where $p=-\rho$, $k=3$. In this case, the mass density of BHs is conserved as the Universe expands: their number density decreases with $a^{-3}$ but their mass increases as $a^{3}$ and so BHs could account for the cosmological constant (Croker and Weiner, 2019; Farrah et al., 2023a) (see also [Prescod-Weinstein et al. 2009], for an alternative way BHs could be the origin of dark energy). In contrast, GR solutions for non-singular BHs prefer $k=1$ (Cadoni et al., 2023b). In this case, the BH mass growth would not compensate for cosmological dilution of their density, so they would not contribute to dark energy.

Observationally, the evidence is mixed. Farrah et al. (2023b, a) find, based on an analysis of SMBH versus host galaxy masses out to $z\approx 2$, that a value of $k\approx 3$ is suggested and $k=0$ can be ruled out at $\approx 3\sigma$. On the other hand, Lei et al. (2023) argue, based on a much smaller sample of AGN at $z>4.5$ with much lower stellar masses, that $k=3$ can be ruled out at $\approx 2\sigma$. For stellar mass black holes, Gao and Li (2023) argue that cosmological coupling of black holes can explain the distribution of compact object masses in low mass X-ray binaries, in particular the "mass gap" between the highest mass neutron stars and lowest mass BHs. However, Rodriguez (2023a) disfavor coupling based on observations of a BH binary in the globular cluster NGC 3201 and Andrae and El-Badry (2023) argue that two BH binaries found by Gaia are likely to have formed with BH masses that were too small if $k=3$. Also, Ghodla et al. (2023) argue that $k=3$ would result in too many BH mergers compared to observations from gravitational wave detectors.

### 1.3 Scope of this paper

As the observational picture seems far from settled, we decided to investigate an independent constraint on BH growth. For cosmologically-coupled mass growth of BHs to be viable, the mass increase must fit within the constraint provided by the Soltan argument - that is, the local SMBH mass density must accommodate both the mass increase due to accretion, and the mass increase due to cosmological coupling. In this paper, we examine whether cosmologically-coupled BH growth can be accommodated within the constraints from the Soltan argument, and, if so, what constraints this can set on the value of $k$. We adopt the latest measures of both the AGN luminosity function (LF) over cosmic history, and of the local SMBH mass density, and explore values for the cosmological coupling strength in the range $0<k<3$. We discuss uncertainties on our results arising from uncertainties in both $\eta$ and the Eddington ratio $\lambda$. §2 presents our methods and §3 our sources of data. §4 presents our results and §5 discusses these results in the context of uncertainties on observed parameters. §6 summarizes our conclusions. We assume a cosmology with $H_{0}=70\,\mathrm{kms^{-1}Mpc}$, $\Omega_{\mathrm{M}}=0.3$ and $\Omega_{\Lambda}=0.7$.

## 2 Methods

### 2.1 Generalization of the Soltan Argument for cosmologically-coupled black holes

The SMBH mass and luminosity are connected for each AGN through

$L=\eta\dot{M}_{\mathrm{acc}}c^{2},$ (2)

where $L$ is the bolometric luminosity of the AGN, $\eta$ is the radiative efficiency, and $\dot{M}_{\mathrm{acc}}$ is the mass accretion rate of the BH. Mass/energy that is not radiated is accreted onto the BH, so the rate of mass increase of the BH, $\dot{M}_{\bullet}=(1-\eta)L_{\mathrm{bol}}/(\eta c^{2})$.

In the absence of cosmological coupling (and ignoring the mass density of any high redshift seed population, which we assume to be negligible throughout this paper, the mass density in SMBHs today is equal to the integral of the AGN luminosity density, $U(z)$ over Cosmic Time, modulated by $\eta$:

$\rho_{\bullet}(0)=\int_{0}^{\infty}\left(\frac{1-\eta}{\eta}\right)\frac{U(z)}{c^{2}}\frac{\mathrm{d}t}{\mathrm{d}z}\mathrm{d}z,$ (3)

where $U$

## Page 3

$U(z) = \int_{\mathrm{L_{min}}}^{\mathrm{L_{max}}}L\frac{\partial\phi(L,z)}{\partial(\mathrm{log_{10}}L)}\,\mathrm{d}(\mathrm{log_{10}}L)$ (4)
$= \frac{1}{\mathrm{ln}10}\int_{\mathrm{L_{min}}}^{\mathrm{L_{max}}}\frac{\partial\phi(L,z)}{\partial(\mathrm{log_{10}}L)}\,\mathrm{d}L,$ (5)

$\frac{\partial\phi(L,z)}{\partial(\mathrm{log_{10}}L)}$ is the bolometric luminosity function of AGN and

$\frac{\mathrm{d}t}{\mathrm{d}z}=\frac{-1}{(1+z)H(z)},$ (6)

where

$H(z)=H_{0}\sqrt{(1+z)^{3}\Omega_{\mathrm{m}}+\Omega_{\Lambda}}\ ,$ (7)

and $H_{0}$ is the Hubble Constant at the current epoch. If, in addition, BH mass is increasing with the scale factor of the Universe as per Equation 1, then the contribution to the BH mass density at redshift $z^{\prime}$, $\delta\rho_{\bullet}(z^{\prime})$, to that at redshift $z$ is

$\delta\rho_{\bullet}(z)(1+z)^{k}=\delta\rho_{\bullet}(z^{\prime})(1+z^{\prime})^{k}$ (8)

and the version of Equation 3 with cosmologically-coupled BHs is thus:

$\rho_{\bullet}(z)=\frac{1}{(1+z)^{k}}\int_{\infty}^{z}\left(\frac{1-\eta}{\eta}\right)\frac{U(z^{\prime})(1+z^{\prime})^{k-1}}{H(z^{\prime})c^{2}}\,\mathrm{d}z^{\prime}$ (9)

### 2.2 Constraints from the AGN luminosity function at high redshifts

The high redshift AGN luminosity function also provides a constraint on SMBH growth. If the growth of SMBHs by accretion at high redshifts is too slow, there is insufficient mass density in SMBHs to power the observed AGN luminosity density at early times ($z\gtrsim 2$), when a large fraction of the SMBH population was actively accreting. We relate the luminosity density in AGN to the mass density in SMBHs via a mean Eddington ratio, $\lambda=L/L_{\mathrm{Edd}}$, where $L_{\mathrm{Edd}}$ is the Eddington luminosity. (We note that both this analysis and the Soltan analysis above could be made more constraining by considering the observed distribution of SMBH masses and AGN luminosities and using a continuity-equation approach (e.g. Raimundo et al., 2012; Tucci & Volonteri, 2017). However, given the uncertainties in our understanding of the possible mass/luminosity dependencies of variables such as $\lambda$ and $\eta$, and uncertainties in the exact forms of the mass and luminosity functions and SMBH merger histories, we retain an integral approach for this study.)

## 3 Data

Two measurements are needed to use the formalism in §2. First is a measurement of the local SMBH mass density. Second is a measure of the accretion history of SMBHs since the first quasars, via a bolometric AGN luminosity function. We describe both these sources of data in this section.

### 3.1 The local mass density of SMBHs

Graham & Driver (2007, hereafter GD07) compared several estimates of the local SMBH mass density available in the literature at the time (see Figure 1, left-hand panel). These were derived from the SMBH mass – bulge velocity dispersion ($M_{\bullet}-\sigma$) and the SMBH mass – bulge mass ($M_{\bullet}-M_{\mathrm{bulge}}$) relations, and adjusted to a common $H_{0}=70\mathrm{kms^{-1}Mpc^{-1}}$. GD07 determined a local SMBH mass density in the range 4.4-5.9 $\times 10^{5}M_{\odot}\mathrm{Mpc^{-3}}$. Subsequently, Kormendy & Ho (2013) presented a recalibration of the $M_{\bullet}-\sigma$ and $M_{\bullet}-M_{\mathrm{bulge}}$ relations by excluding pseudobulges and galaxy-galaxy mergers from the fitting procedure. This resulted in an increase of the $M_{\bullet}/M_{\mathrm{bulge}}$ ratio from $\approx 0.2\%$ to $\approx 0.5\%$. Thus, the SMBH mass density calculated from a stellar mass function and the Kormendy & Ho (2013) $M_{\bullet}-M_{\mathrm{bulge}}$ relation results in a local SMBH mass density substantially higher than the Graham & Driver (2007) estimate (we note also that the work of McConnell & Ma (2013) also suggests a relatively high normalization, $\approx 0.3\%$, however, to be conservative, we adopt the higher Kormendy & Ho (2013) normalization). Furthermore, the difference in the shapes of the stellar mass functions for disks and bulges means that the assumption of a single bulge fraction independent of stellar mass is not strictly correct.

We therefore construct an updated range for the local SMBH mass density as follows. We use the study of Thanjavur et al. (2016), who split the stellar mass function into spheroid and disk components. Using their spheroid mass function and the $M_{\bullet}-M_{\mathrm{bulge}}$ relation of Kormendy & Ho (2013) results in an estimate of $\rho_{\bullet}(0)=1.0\times 10^{6}M_{\odot}\mathrm{Mpc^{-3}}$, higher than that of Graham & Driver (2007), but lower than that obtained by assuming a fixed bulge fraction and using an all-galaxy stellar mass function.

The uncertainty in this estimate is substantial. It may be too low – there is evidence that a significant fraction of SMBH mass may be missed by using spheroid mass of velocity dispersion as a proxy. For example, Voggel et al. (2019) argue for the existence of a population of 'stripped' galaxy nuclei in the haloes of giant ellipticals. These objects have modest stellar masses, but can harbor SMBHs of up to $\sim 10^{7}\mathrm{M_{\odot}}$. Voggel et al. (2019) further

## Page 4

argue that this population may increase the total SMBH mass density by up to $\sim 30\%$. At high velocity dispersions (or equivalently, high stellar masses) the $M_{\bullet}-\sigma$ relation may also be biased low, as there are several examples of 'overmassive' SMBHs for their hosts (e.g. Dullo et al., 2021; Nightingale et al., 2023). Another plausible source of error is ejected SMBHs (Postman et al., 2012; Chu et al., 2023). Conversely, it is possible our estimate is too high. Selection biases (Schulze and Wisotzki, 2011; Shankar et al., 2016) could lead to an overestimate of the SMBH mass density by a factor $\approx 3$, though the existence of this bias has not been confirmed observationally. Also, the spheroid mass function still includes pseudobulges, which, as Kormendy and Ho (2013) emphasize, typically fall below the $M_{\bullet}-M_{\rm bulge}$ relation (Hopkins et al., 2008, though pseudobulges are typically less massive than classical bulges, making up $\lesssim 10\%$ of the stellar mass density in spheroids). It is beyond the scope of this paper to synthesize these disparate results into a firm range for $\rho_{\bullet}$. However, a maximum value of $\approx 1.6\times 10^{6}\rm M_{\odot}Mpc^{-1}$ does not appear to be ruled out (assuming $\approx 30\%$ of the mass density is stripped and $\approx 30\%$ ejected), and a minimum value of $3\times 10^{5}\rm M_{\odot}Mpc^{-1}$ also seems plausible, based on the most extreme estimates of bias. We therefore adopt an estimate and range of $\log_{10}(\rho_{\bullet}(0)/\rm M_{\odot}Mpc^{-1})=6.0^{+0.2}_{-0.5}$ based on the $M_{\bullet}-M_{\rm bulge}$ relation.

Finally, we note that the recent detection of a gravitational wave background (GWB) by pulsar timing arrays, if ascribed purely to the mergers of SMBHs, results in a much higher SMBH mass density estimate than those discussed above. Using the results of Agazie et al. (2023) we find that the peaks of their posterior distributions of the most relevant parameters from the fits based on their Phenom+Astro priors (the galaxy stellar mass function characteristic density and cutoff mass, the $M_{\bullet}/M_{\rm bulge}$ ratio, and the logarithmic width of the $M_{\bullet}/M_{\rm bulge}$ distribution) lead to an estimate of $7.4\times 10^{6}M_{\odot}\rm Mpc^{-3}$. Using the posterior distribution of $\rho_{\bullet}$ constructed from their Monte-Carlo simulations results in a $95\%$ confidence range of $2-1400\times 10^{6}M_{\odot}\rm Mpc^{-3}$ and an average of $\approx 1\times 10^{8}M_{\odot}\rm Mpc^{-3}$ (we note also that Casey-Clyde et al., 2022, found a similar result using the earlier 12.5 yr NanoGrav data release). Given the large uncertainties in the SMBH merger estimates it is probably too early to be concerned with the tension between the GWB versus the $M_{\bullet}-M_{\rm bulge}$ relation (see Afzal et al., 2023, for a discussion of the strength of the tension between the SMBH binary model and the measured GWB in the context of new physics), nevertheless we consider the implications of a GWB-based estimate of $\rho_{\bullet}(0)=7.4\times 10^{6}M_{\odot}\rm Mpc^{-3}$ in our analysis as well.

### 3.2 The bolometric AGN luminosity function

To compute the comoving AGN luminosity density, we need an estimate of the bolometric AGN luminosity function as a function of redshift. Integrating under this luminosity function as a function of redshift then gives the comoving AGN luminosity density. To perform this calculation, we adopt the Shen et al. (2020) (their "global fit B") luminosity function (Equation 10), which agrees well with, but is somewhat more refined than other estimates (e.g. Hopkins et al., 2007; Lacy et al., 2015; Runburg et al., 2022):

$\frac{\partial\phi(L,z)}{\partial(\log_{10}L)}=\frac{\phi(z)^{*}}{((L/L(z)^{*})^{\gamma_{1}(z)}+(L/L(z)^{*})^{\gamma_{2}(z)})},$ (10)

where the redshift dependencies of $\phi^{*}$, $L^{*}$, $\gamma_{1}$ and $\gamma_{2}$ are detailed in Shen et al. (2020).

## 4 Results

Figure 1 (middle and right panels) plots the SMBH mass densities from §3.1 with the result of integrating Equation 9 from $z=6$ to $z=0$ for fixed $\eta$ values of $0.1$ and $0.3$ (Thorne, 1974). We show curves for $k=0$ (no cosmological coupling), $k=1$ (e.g. the exact solutions of Faraoni and Jacques, 2007) and $k=3$ (Farrah et al., 2023a). This indicates that, if we assume the GD07 value for the local SMBH mass density and $\langle\eta\rangle\simeq 0.3$, then an upper limit can be set of $k\lesssim 2$. Alternatively, using the GWB value for the local SMBH mass density, then a non-zero value of $k$ is required for any reasonable value of $\eta$.

To generalize this argument, we note that, for a given value of $k$, $\eta$ can uniquely determined by matching the observed local black hole mass density, so if we assume a value of the Eddington ratio, $\lambda$ between the minimum value needed to explain the AGN luminosity function at high redshift (assuming all SMBHs are actively-accreting) and $\lambda=1$ then we can define an allowed region in AGN accretion parameter space as a function of $k$. In Figure 2, we use the Salpeter time:

$t_{S}=4\times 10^{8}\frac{\eta}{\lambda(1-\eta)}\ \rm yr$ (11)

as a proxy for accretion rate as a function of $\eta$, and plot $k$ vs $t_{S}$ to define an allowed region of parameter space in which quasars can (on average) lie (assuming no evolution in the mean $\eta$ or $\lambda$ and that the increase in the SMBH mass density is dominated by accretion). Here, a similar result is seen. With the GD07 local density we constrain $k$ to $<2$, with our derived density range then $0<k<3$ can (just) be accommodated (though only with very high values of $\eta\approx 0.55$ and $\lambda\approx 1$), but with

## Page 5

BLACK HOLE COUPLING & ACCRETION HISTORY

![Figure 1 — k constraints vs local SMBH mass density](../figures/extracted/scenario1_revised.png)
Figure 1. Middle and right panels: constraints on the value of the cosmological coupling strength $k$ (Equation 1) based on comparing the growth of SMBH density via accretion to the local density of SMBHs. Middle: assuming $\eta = 0.1$ (which agrees well with the GD07 estimate of $\rho_{\bullet}(0)$ if $k = 0$) and right: $\eta = 0.3$, the maximum theoretical value for a maximally-spinning BH (Thorne 1974). In both, the red triangle and error bar represents our estimate of the local SMBH mass density from the $M_{\bullet} - M_{\mathrm{bulge}}$ relation and the blue square and error bar (which extends well above the plotted range) the preliminary estimate from the GWB, as discussed in §3.2. Also in both, the black lines represent the minimum mass density in SMBHs needed to account for the observed luminosity function for different mean values of $\lambda$ and the cyan-solid, magenta-dotted and red-dashed lines the growth in BH mass density for different values of $k$ assuming the AGN luminosity function of Shen et al. (2020). The shaded region around the $k = 0$ (cyan-solid) line corresponds to the uncertainty in Shen et al. (2020). Far left: a compilation of estimates of the local mass density in black holes from the literature: S04: Shankar et al. (2004), M04: Marconi et al. (2004), H07: Hopkins et al. (2007), G07: Graham et al. (2007), GD07: Graham & Driver (2007), YL08: Yu & Lu (2008), S09: Shankar et al. (2009), with the cyan shaded area indicating the range of uncertainty at $z = 0$ for the Shen et al. (2020) luminosity function, assuming $\eta = 0.1$.

the GWB local density range then an approximate lower limit can be set of $k > 2$, assuming standard accretion disk dominated growth.

# 5. DISCUSSION

Conventional assumptions about SMBH accretion, combined with estimates of the local SMBH mass density based on the $M_{\bullet} - M_{\mathrm{bulge}}$ relation, imply an allowed range of $0 < k \lesssim 2$ (Figure 2). This range is in slight tension ($\sim 90\%$ confidence interval) with the results in Farrah et al. (2023a), though it is consistent with some of the recent constraints discussed in §1.2 (e.g. Lei et al. 2023; Rodriguez 2023b; Andrae & El-Badry 2023; Ghodla et al. 2023).

Our constraints on $k$ from the Soltan argument are, however, dependent on four variables: the local SMBH mass density, the integrated luminosity density from the AGN luminosity function and the mean values of $\lambda$ and $\eta$, which regulate the total accretion derived from integrating the AGN luminosity function. We first briefly review the uncertainties on the luminosity density, $\eta$ and $\lambda$ (the uncertainties on the local SMBH density are discussed in §3.1), before discussing the effect of these uncertainties on our limit on $k$.

# 5.1. Uncertainties in the luminosity density

The bolometric luminosity function of AGN is still uncertain, but most of the uncertainty lies at the faint end at high redshifts, whereas the dominant contribution to the luminosity density arises around the break in the luminosity function, where AGN surveys are relatively complete.

As briefly discussed in §3.2, we adopt the luminosity function of Shen et al. (2020), however, if, for example, we use the mid-infrared luminosity function of Glikman et al. (2018) and convert to the bolometric luminosity

## Page 6

LACY, ET AL.

![Figure 2 — allowed k vs Salpeter time](../figures/extracted/Salpeter_plot_revised.png)
Figure 2. The allowed values of the cosmological coupling strength $k$ (Equation 1) and the Salpeter time (Equation 11) $t_S$ for quasars assuming accretion-dominated growth of the supermassive black hole density. Left: assuming the GD07 estimate of $\rho_{\bullet}(0)$, middle assuming the best estimate from this paper and right assuming the value from the peaks of the GWB posterior fits. The hatched blue regions represent the parameter space where the Salpeter time is too long to grow enough black holes at $z = 4$ to explain the observed luminosity function and the red regions are those where the Eddington ratio needs to exceed unity to do this. The yellow hatched regions are excluded based on the plausible range of $0.05 < \eta < 0.3$.

function using the prescription of Lacy et al. (2015) we recover a black hole mass density $60\%$ higher than that from the Shen et al. (2020) luminosity function. (Using this value would be even more constraining on the value of $k$.) Based on this small difference between two independently-derived luminosity density estimates we believe that the uncertainties from the AGN luminosity function, although not negligible, are smaller than those from the local black hole mass density.

# 5.2. Uncertainties in accretion efficiency

The typical accretion efficiency of an SMBH is poorly constrained (e.g. Raimundo et al. 2012). The canonical value of $\eta \approx 0.1$ (e.g. Soltan 1982) is not measured directly, but obtained by matching early estimates of accretion luminosity to local SMBH mass density. The theoretical limit is thought to be $\eta \approx 0.3$ (Thorne 1974). Observational estimates of $\eta$ vary from $\lesssim 0.1$ to potentially $>0.5$ (e.g. Trakhtenbrot 2014; Jana et al. 2021; Farrah et al. 2022; Lai et al. 2023). Several factors are thought to affect $\eta$; for example, magnetized discs may have $\eta > 0.3$ (Avara et al. 2016; Kinch et al. 2021), but there is no consensus on how these factors interrelate. For Figure 2 we have assumed the conventional range of $0.05 < \eta < 0.3$, but a larger range is certainly not excluded. We note though that high values of $\eta$ reduce the available time for black hole growth by accretion in the early Universe, which is already problematic (e.g. Bañados et al. 2018).

# 5.3. Uncertainties in Eddington ratio

Directly observed Eddington ratios in quasars are consistent with $\lambda \sim 0.05$, with a broad tail towards higher Eddington ratios (e.g. Farrah et al. 2023b). This ratio may however be biased low. Most SMBH mass is likely accreted in obscured phases (Martínez-Sansigre et al. 2005) during which Eddington ratios can be higher (Teng et al. 2014; Farrah et al. 2022). Furthermore, quasar surveys may find AGN whose SMBH masses and Eddington ratios are biased low and high, respectively (e.g. Shen et al. 2008).

# 6. CONCLUSIONS

By analysing the growth of the mass density in SMBHs via accretion we show that high values of cosmological coupling ($k \approx 3$) needed by Farrah et al. (2023a) to account for dark energy via BHs is disfavored if conventional assumptions regarding the local SMBH mass density and accretion mechanisms are made. However, we cannot rule out scenarios in which $k = 3$ is possible, and indeed, recent estimates of the GWB from pulsar timing arrays favor a much higher mass density of SMBHs than estimates based on the $M_{\bullet} - M_{\mathrm{bulge}}$ relation and would comfortably allow $k = 3$ (Figure 2, right panel). Better constraints on the local mass function

## Page 7

of SMBHs are thus essential both to our understanding of the GWB and for more reliably constraining any cosmological coupling of black holes.

We are grateful to L.Z. Kelley and the NANOGrav team for supplying the data from their simulations of supermassive black hole merger statistics. The National Radio Astronomy Observatory is a facility of the National Science Foundation operated under cooperative agreement by Associated Universities, Inc.

## References (page 7)

- Afzal, A., Agazie, G., Anumarlapudi, A., et al. 2023, ApJL, 951, L11, doi: 10.3847/2041-8213/acdc91
- Agazie, G., Anumarlapudi, A., Archibald, A. M., et al. 2023, arXiv:2306.16220
- Andrae, R., & El-Badry, K. 2023, A&A, 673, L10
- Avara, M. J., McKinney, J. C., & Reynolds, C. S. 2016, MNRAS, 462, 636
- Bañados, E., Venemans, B. P., Mazzucchelli, C., et al. 2018, Nature, 553, 473
- Bardeen, J. M. 1970, Nature, 226, 64
- Beltracchi, P., & Gondolo, P. 2019, PhRvD, 99, 044037
- Cadoni, M., Murgia, R., Pitzalis, M., & Sanna, A. P. 2023a, arXiv:2309.16444
- Cadoni, M., Sanna, A. P., Pitzalis, M., et al. 2023b, JCAP, 2023, 007
- Casey-Clyde, J. A., Mingarelli, C. M. F., Greene, J. E., et al. 2022, ApJ, 924, 93
- Chu, A., Boldrini, P., & Silk, J. 2023, MNRAS, 522, 948
- Croker, K. S., Nishimura, K. A., & Farrah, D. 2020, ApJ, 889, 115
- Croker, K. S., & Weiner, J. L. 2019, ApJ, 882, 19
- Croker, K. S., Zevin, M., Farrah, D., Nishimura, K. A., & Tarlé, G. 2021, ApJL, 921, L22
- Dullo, B. T., Gil de Paz, A., & Knapen, J. H. 2021, ApJ, 908, 134
- Dymnikova, I. 1992, General Relativity and Gravitation, 24, 235
- Elvis, M., Risaliti, G., & Zamorani, G. 2002, ApJL, 565, L75
- Faraoni, V., & Jacques, A. 2007, PhRvD, 76, 063510
- Farrah, D., Efstathiou, A., Afonso, J., et al. 2022, MNRAS, 513, 4770
- Farrah, D., Croker, K. S., Zevin, M., et al. 2023a, ApJL, 944, L31
- Farrah, D., Petty, S., Croker, K. S., et al. 2023b, ApJ, 943, 133
- Gao, S.-J., & Li, X.-D. 2023, ApJ, 956, 128
- Ghodla, S., Easther, R., Briel, M. M., & Eldridge, J. J. 2023, The Open Journal of Astrophysics, 6, 25
- Glikman, E., Lacy, M., LaMassa, S., et al. 2018, ApJ, 861, 37
- Gliner, E. B. 1966, Soviet Journal of Experimental and Theoretical Physics, 22, 378
- Graham, A. W., & Driver, S. P. 2007, MNRAS, 380, L15
- Graham, A. W., Driver, S. P., Allen, P. D., & Liske, J. 2007, MNRAS, 378, 198
- Hopkins, P. F., Hernquist, L., Cox, T. J., & Kereš, D. 2008, ApJS, 175, 356
- Hopkins, P. F., Richards, G. T., & Hernquist, L. 2007, ApJ, 654, 731
- Jana, A., Naik, S., Chatterjee, D., & Jaisawal, G. K. 2021, MNRAS, 507, 4779
- Kinch, B. E., Schnittman, J. D., Noble, S. C., Kallman, T. R., & Krolik, J. H. 2021, ApJ, 922, 270
- Kormendy, J., & Ho, L. C. 2013, ARA&A, 51, 511
- Lacy, M., Ridgway, S. E., Sajina, A., et al. 2015, ApJ, 802, 102
- Lai, S., Wolf, C., Onken, C. A., & Bian, F. 2023, MNRAS, 521, 3682

## Page 8

## References (page 8, continued)

- Lei, L., Zu, L., Yuan, G.-W., et al. 2023, arXiv:2305.03408
- Marconi, A., Risaliti, G., Gilli, R., et al. 2004, MNRAS, 351, 169
- Martínez-Sansigre, A., Rawlings, S., Lacy, M., et al. 2005, Nature, 436, 666
- McConnell, N. J., & Ma, C.-P. 2013, ApJ, 764, 184
- Nightingale, J. W., Smith, R. J., He, Q., et al. 2023, MNRAS, 521, 3298
- Postman, M., Lauer, T. R., Donahue, M., et al. 2012, ApJ, 756, 159
- Prescod-Weinstein, C., Afshordi, N., & Balogh, M. L. 2009, PhRvD, 80, 043513
- Raimundo, S. I., Fabian, A. C., Vasudevan, R. V., Gandhi, P., & Wu, J. 2012, MNRAS, 419, 2529
- Rodriguez, C. L. 2023a, ApJL, 947, L12
- Rodriguez, C. L. 2023b, ApJL, 947, L12
- Runburg, J., Farrah, D., Sajina, A., et al. 2022, ApJ, 924, 133
- Schulze, A., & Wisotzki, L. 2011, A&A, 535, A87
- Shankar, F., Weinberg, D. H., & Miralda-Escudé, J. 2009, ApJ, 690, 20
- Shankar, F., Bernardi, M., Sheth, R. K., et al. 2016, MNRAS, 460, 3119
- Shankar, F., Weinberg, D. H., Marsden, C., et al. 2020, MNRAS, 493, 1500
- Shen, X., Hopkins, P. F., Faucher-Giguère, C.-A., et al. 2020, MNRAS, 495, 3252
- Shen, Y., Greene, J. E., Strauss, M. A., Richards, G. T., & Schneider, D. P. 2008, ApJ, 680, 169
- Soltan, A. 1982, MNRAS, 200, 115
- Teng, S. H., Brandt, W. N., Harrison, F. A., et al. 2014, ApJ, 785, 19
- Thanjavur, K., Simard, L., Bluck, A. F. L., & Mendel, T. 2016, MNRAS, 459, 44
- Thorne, K. S. 1974, ApJ, 191, 507
- Trakhtenbrot, B. 2014, ApJL, 789, L9
- Tucci, M., & Volonteri, M. 2017, A&A, 600, A64
- Voggel, K. T., Seth, A. C., Baumgardt, H., et al. 2019, ApJ, 871, 159
- Yu, Q., & Lu, Y. 2008, ApJ, 689, 732
- Yu, Q., & Tremaine, S. 2002, MNRAS, 335, 965
- Zhang, X., & Lu, Y. 2017, Science China Physics, Mechanics, and Astronomy, 60, 109511
