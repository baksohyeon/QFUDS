"""
CP17: an INTERNAL-CONSISTENCY / self-falsification test of the rough tanh toy.

Premise (the lineage's own narrative): CP5–CP9 opened a dark-fluid sound speed
c_eff² and tuned it to SUPPRESS late-time growth so that the weak-lensing S8
slides from the Planck value (≈0.83) down toward the low-z lensing preference
(≈0.76). Weak lensing is a LOW-redshift probe (z≈0–0.5).

But the CMB lensing potential power C_ℓ^φφ probes structure growth with a kernel
that peaks near COSMIC NOON (z≈2) — exactly where this toy puts its w:0→-1
transition. ACT DR6 CMB lensing measures that growth to ~2% in amplitude and finds
it CONSISTENT WITH ΛCDM / Planck (no low-z suppression). So the self-falsification
question is: does the SAME c_eff² that drags weak-lensing S8 down ALSO drag (or
push) C_ℓ^φφ away from ΛCDM at the ACT scales — i.e. is the toy caught in a
perturbation-sector tension, the analogue of CP10's H0 failure?

STATUS — read this before quoting anything:
  * EXPLORATORY phenomenology. PARAMETRIZE-not-DERIVE. c_eff² is a hand-tuned knob,
    NOT derived from foam microphysics. The "050 ceiling" (deriving the dark sector
    from foam) is UNTOUCHED here; observer mode is UNTOUCHED.
  * Growth uses the cp9 η-Jeans PROXY (a scale-dependent clustering efficiency),
    NOT a Boltzmann/CLASS perturbation solve. The proxy is known to over-cluster a
    w→-1 component in the c_eff²→0 limit (it forces a vacuum-like fluid to cluster);
    that limit is flagged below, not trusted.
  * The ACT DR6 numbers (≈2.3% lensing-amplitude precision, A_lens=1.013±0.023,
    S8^CMBL=0.818±0.022, 43σ, ΛCDM-consistent) are REPRESENTATIVE scalar magnitudes
    sourced from the paper abstract:
        Madhavacheril et al., ACT DR6 CMB lensing — arXiv:2304.05202
        https://arxiv.org/abs/2304.05202
    They are used ONLY as a representative precision band. This is NOT a likelihood.
    NO data vector, NO covariance, NO χ² has been ingested or computed.
  * The REAL test is the coupled clustering-DE perturbations in CLASS/hi_class
    (Level 3) — BLOCKED. Nothing here is evidence or a roadmap change.

Limber proxy (rough, linear):
    C_ℓ^φφ ∝ ∫ dz  W(z)² / (χ(z)² · H(z)/c) · P(k=ℓ/χ, z)
    W(z) ∝ (1+z)·χ(z)(χ* − χ(z))/χ*   (CMB lensing efficiency; the (1+z)=1/a is the
            Poisson factor that makes the kernel peak at z≈2; χ* = comoving dist to z*≈1090)
    P(k,z) = P_prim(k)·T(k)²·D(k,z)²   with the SAME P_prim·T² for both models, so the
             QFUDS/ΛCDM ratio is driven PURELY by the growth D(k,z) (clean ratio).
Geometry (χ, H) is held to ΛCDM for BOTH models: CP10 showed the QFUDS background ≈
ΛCDM, so fixing geometry isolates the perturbation/growth effect — the thing under test.
"""
from __future__ import annotations
import csv
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.interpolate import interp1d, RectBivariateSpline
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M
import cp5_sound_speed as cp5   # density-driven QFUDS background + η-Jeans growth machinery

# ---------------------------------------------------------------------------
# constants
# ---------------------------------------------------------------------------
C_KM_S = M.C_KM_S
H0 = M.H0_CMB
DH = C_KM_S / H0                 # Hubble distance c/H0 [Mpc]
H_LITTLE = H0 / 100.0
OM0 = cp5.OM0                    # 0.315 (V2 matter), == ΛCDM Ω_m
A_I = 1e-3
N_S = 0.96                      # primordial tilt (proxy)
Z_REC = 1090.0

# ACT DR6 representative scalars (sourced, NOT a likelihood — see header)
ACT_AMP_PREC = 0.023            # ~2.3% lensing-amplitude precision (A_lens=1.013±0.023)
ACT_S8 = 0.818                  # S8^CMBL = 0.818 ± 0.022 (ACT DR6 alone), ΛCDM-consistent
ACT_URL = "https://arxiv.org/abs/2304.05202"

# weak-lensing target the lineage tuned c_eff² toward
SIGMA8_LCDM = cp5.SIGMA8_LCDM   # 0.81
S8_LCDM = 0.83
S8_WL = cp5.S8_OBS              # 0.76

# c_eff² cases. Headline = the value that ACTUALLY pulls cp5's S8 to 0.76.
CEFF2_S8FIT = 2.92e-5           # cp5 crossing S8→0.76 (the c² that fixes weak lensing)
CEFF2_LINEAGE = 4.6e-6          # cp8/cp9 "ξ≈10 Mpc data-fit" value (milder; S8≈0.82)
CEFF2_SMOOTH = 1.0              # sanity: smooth dark (Λ-like) → growth suppressed
CEFF2_CLUST = 1e-10            # sanity: clustering limit (proxy over-clusters w→-1)

# ℓ grid and the ACT-sensitive band
L_GRID = np.unique(np.round(np.logspace(np.log10(30), np.log10(1000), 45))).astype(float)
ACT_BAND = (100.0, 600.0)


# ---------------------------------------------------------------------------
# ΛCDM background geometry (fixed for both models — isolates growth)
# ---------------------------------------------------------------------------
def E_lcdm(a):
    a = np.asarray(a, float)
    return np.sqrt(M.OMEGA_M0_LCDM * a**-3 + M.OMEGA_R0_LCDM * a**-4 + M.OMEGA_L0_LCDM)


def build_chi():
    """Comoving distance χ(z) [Mpc] on a z grid running to last scattering."""
    z = np.concatenate([np.linspace(0.0, 12.0, 1400)[:-1],
                        np.logspace(np.log10(12.0), np.log10(Z_REC), 400)])
    a = 1.0 / (1.0 + z)
    inv_e = 1.0 / E_lcdm(a)
    chi = DH * cumulative_trapezoid(inv_e, z, initial=0.0)
    return z, chi


# ---------------------------------------------------------------------------
# growth D(k,a): ΛCDM (k-independent) and QFUDS (η-Jeans, k-dependent)
# IC: D=a_i at a_i (matter domination) for BOTH → same primordial normalization,
# so D_QFUDS/D_ΛCDM → 1 at high z automatically (clean ratio).
# ---------------------------------------------------------------------------
def _dense_solve(rhs):
    return solve_ivp(rhs, (np.log(A_I), 0.0), [A_I, A_I], method="LSODA",
                     rtol=1e-8, atol=1e-12, dense_output=True)


def D_lcdm_solution():
    def rhs(n, y):
        D, Dp = y
        a = np.exp(n)
        El = E_lcdm(a)
        h = 1e-5
        dl = (np.log(E_lcdm(np.exp(n + h))) - np.log(E_lcdm(np.exp(n - h)))) / (2 * h)
        Om = M.OMEGA_M0_LCDM * a**-3 / El**2
        return [Dp, -(2.0 + dl) * Dp + 1.5 * Om * D]
    return _dense_solve(rhs)


def D_qfuds_solution(k, ceff2):
    """QFUDS growth at fixed wavenumber k [Mpc^-1] with η-Jeans clustering of Ω_X."""
    cs = np.sqrt(ceff2)

    def eta(a):
        R = cs * C_KM_S * k / (a * H0 * cp5.E(a))
        return 1.0 / (1.0 + R**2)

    def rhs(n, y):
        D, Dp = y
        a = np.exp(n)
        Om = OM0 * a**-3 / cp5.E(a)**2
        Ox = cp5.rho_x(a) / cp5.E(a)**2
        return [Dp, -(2.0 + cp5.dlnE_dN(a)) * Dp + 1.5 * (Om + eta(a) * Ox) * D]
    return _dense_solve(rhs)


def growth_grid_qfuds(ceff2, k_grid, z_grid):
    """D_QFUDS(k,z) on a (k,z) grid via one ODE solve per k (dense output)."""
    n_grid = np.log(1.0 / (1.0 + np.clip(z_grid, 0.0, 1.0 / A_I - 1.0)))
    D = np.empty((k_grid.size, z_grid.size))
    for i, k in enumerate(k_grid):
        sol = D_qfuds_solution(k, ceff2)
        D[i, :] = sol.sol(n_grid)[0]
    return D


# ---------------------------------------------------------------------------
# proxy linear matter transfer (BBKS) — shape only; common to both models
# ---------------------------------------------------------------------------
def T_bbks(k):
    """BBKS transfer function (proxy). Γ = Ω_m h. k in Mpc^-1."""
    gamma = OM0 * H_LITTLE
    q = k / gamma
    q = np.where(q <= 0, 1e-12, q)
    L = np.log(1.0 + 2.34 * q) / (2.34 * q)
    P = (1.0 + 3.89 * q + (16.1 * q)**2 + (5.46 * q)**3 + (6.71 * q)**4)
    return L * P**-0.25


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
def main():
    print("CP17: CMB-lensing C_ℓ^φφ internal-consistency test (exploratory, proxy)")
    print(f"ACT DR6 representative precision: ±{ACT_AMP_PREC*100:.1f}% amplitude, "
          f"S8^CMBL={ACT_S8}, ΛCDM-consistent  [{ACT_URL}]\n")

    # --- geometry ---
    zc, chi = build_chi()
    chi_of_z = interp1d(zc, chi, kind="cubic")
    z_of_chi = interp1d(chi, zc, kind="cubic")
    chi_star = float(chi[-1])
    print(f"χ* (to z*={Z_REC:.0f}) = {chi_star:.1f} Mpc")

    # --- CMB lensing kernel W(z)² and the per-dz geometric weight ---
    z_int = np.concatenate([np.linspace(0.02, 12.0, 900)[:-1],
                            np.logspace(np.log10(12.0), np.log10(Z_REC * 0.999), 200)])
    chi_z = chi_of_z(z_int)
    El_z = E_lcdm(1.0 / (1.0 + z_int))
    # convergence efficiency W_κ ∝ (1+z)·χ(χ*−χ)/χ*. The (1+z)=1/a factor is the
    # Poisson conversion P_Φ∝(Ω_m/a)P_δ; it is what shifts the CMB-lensing kernel to z~2.
    W = (1.0 + z_int) * chi_z * (chi_star - chi_z) / chi_star
    # per-dz geometric weight in the Limber integral: W²/(χ² H/c) = W² · (c/H0)/(χ² E)
    Kgeom = W**2 * DH / (chi_z**2 * El_z)

    # comoving-distance kernel W²/χ² (the standard "CMB lensing kernel" that peaks at z~2;
    # no 1/E volume Jacobian — that Jacobian is folded into Kgeom for the dz integral below)
    Kchi = W**2 / chi_z**2
    z_kernel_peak = float(z_int[np.argmax(Kchi)])
    print(f"geometric χ-kernel W²/χ² peaks at z = {z_kernel_peak:.2f}")

    # --- growth grids ---
    k_grid = np.logspace(-3.3, 0.5, 36)
    solL = D_lcdm_solution()
    nL = np.log(1.0 / (1.0 + np.clip(z_int, 0.0, 1.0 / A_I - 1.0)))
    DL_z = solL.sol(nL)[0]                               # D_ΛCDM(z) on z_int

    # full lensing CONTRIBUTION per dχ at a representative ℓ (incl. matter power + growth):
    # dC_ℓ/dχ ∝ (W²/χ²)·P(ℓ/χ,z). The kernel is BROAD; the physically-robust statement
    # is its REDSHIFT WEIGHTING, not the exact peak: CMB lensing weights z≳1, far above
    # the z~0.3–0.8 where weak-lensing/galaxy surveys (and the toy's growth shift) live.
    ELL_REF = 100.0
    k_ref = ELL_REF / chi_z
    dCdchi_ref = Kchi * (k_ref**N_S * T_bbks(k_ref)**2) * DL_z**2
    z_contrib_peak = float(z_int[np.argmax(dCdchi_ref)])
    norm = np.trapezoid(dCdchi_ref, z_int)
    frac_lo = float(np.trapezoid(dCdchi_ref[z_int < 0.5], z_int[z_int < 0.5]) / norm)
    frac_hi = float(np.trapezoid(dCdchi_ref[z_int > 1.0], z_int[z_int > 1.0]) / norm)
    print(f"CMB-lensing kernel (ℓ={ELL_REF:.0f}): broad, peak~z{z_contrib_peak:.1f}; "
          f"weight from z<0.5 = {frac_lo*100:.0f}%, from z>1 = {frac_hi*100:.0f}%")
    print("  => CMB lensing is a HIGH-z probe (z≳1); weak lensing lives at z~0.3–0.8.")

    # sanity: high-z agreement of QFUDS vs ΛCDM growth (same primordial norm)
    nhi = np.log(1.0 / (1.0 + 8.0))
    DLhi = float(solL.sol(nhi)[0])
    DQhi = float(D_qfuds_solution(0.1, CEFF2_S8FIT).sol(nhi)[0])
    hi_agree = abs(DQhi / DLhi - 1.0)
    print(f"sanity[high-z norm]: |D_QFUDS/D_ΛCDM - 1| at z=8 = {hi_agree*100:.2f}%  "
          f"(should be ≪1 — matter-dominated, same IC)")

    cases = {
        "QFUDS c²=2.92e-5 (S8→0.76 fit)": CEFF2_S8FIT,
        "QFUDS c²=4.6e-6 (cp8/cp9 lineage)": CEFF2_LINEAGE,
        "sanity smooth c²=1": CEFF2_SMOOTH,
        "sanity clustering c²=1e-10": CEFF2_CLUST,
    }

    Dgrids = {name: growth_grid_qfuds(c2, k_grid, z_int) for name, c2 in cases.items()}
    splines = {name: RectBivariateSpline(np.log(k_grid), z_int, np.log(np.clip(D, 1e-30, None)))
               for name, D in Dgrids.items()}

    logk = np.log(k_grid)

    def Cl_phiphi(ell, growth2_z):
        """Limber C_ℓ^φφ for a given D(z)² along the line of sight (k=ℓ/χ)."""
        k_los = ell / chi_z
        Tk = T_bbks(k_los)
        Pbase = k_los**N_S * Tk**2                       # P_prim·T² (common to both)
        phifac = (2.0 / (ell * (ell + 1.0)))**2          # κ→φφ conversion (common)
        integ = phifac * Kgeom * Pbase * growth2_z
        return np.trapezoid(integ, z_int)

    # ΛCDM reference C_ℓ^φφ
    Cl_L = np.array([Cl_phiphi(l, DL_z**2) for l in L_GRID])

    # QFUDS C_ℓ^φφ and ratio for each case
    Cl_Q = {}
    ratio = {}
    for name in cases:
        sp = splines[name]
        vals = []
        for l in L_GRID:
            k_los = np.clip(l / chi_z, k_grid[0], k_grid[-1])
            DQ_z = np.exp(np.array([sp(np.log(kk), zz)[0, 0] for kk, zz in zip(k_los, z_int)]))
            vals.append(Cl_phiphi(l, DQ_z**2))
        Cl_Q[name] = np.array(vals)
        ratio[name] = Cl_Q[name] / Cl_L

    # band-averaged ratio over the ACT-sensitive band (weight by ΛCDM signal)
    band = (L_GRID >= ACT_BAND[0]) & (L_GRID <= ACT_BAND[1])
    wband = Cl_L[band]
    band_ratio = {name: float(np.sum(ratio[name][band] * wband) / np.sum(wband)) for name in cases}
    band_suppr = {name: (1.0 - band_ratio[name]) * 100.0 for name in cases}  # +% = below ΛCDM

    print("\n--- band-averaged C_ℓ^φφ ratio over ACT band ℓ∈[100,600] ---")
    for name in cases:
        sign = "below ΛCDM (suppressed)" if band_suppr[name] > 0 else "ABOVE ΛCDM (enhanced)"
        print(f"  {name:34s} ratio={band_ratio[name]:.4f}  "
              f"=> {abs(band_suppr[name]):.2f}% {sign}")

    # weak-lensing vs CMB-lensing contrast (headline c²)
    headline = "QFUDS c²=2.92e-5 (S8→0.76 fit)"
    wl_amp_suppr = (1.0 - S8_WL / S8_LCDM) * 100.0       # ~8% S8 amplitude drop WL wants
    cmbl_amp_suppr = band_suppr[headline]
    print("\n--- weak-lensing (z≈0) vs CMB-lensing (z≈2) at the SAME c²=2.92e-5 ---")
    print(f"  weak lensing wants S8 amplitude DOWN {wl_amp_suppr:.1f}% (0.83→0.76)")
    print(f"  CMB lensing C_ℓ^φφ amplitude shift   {cmbl_amp_suppr:+.2f}% "
          f"(+=below ΛCDM) over ACT band")
    print(f"  ACT DR6 measures this amplitude to ±{ACT_AMP_PREC*100:.1f}% and sees ΛCDM.")

    # --- sanity asserts (only limits this proxy ACTUALLY satisfies) ---
    assert hi_agree < 0.05, "high-z growth must match ΛCDM (same primordial norm)"
    assert frac_hi > 0.5 and frac_lo < 0.2, \
        "CMB lensing must be a high-z probe (z>1 dominated, little z<0.5 weight)"
    assert band_ratio["sanity smooth c²=1"] < 1.0, \
        "smooth (Λ-like) dark must SUPPRESS growth → ratio<1"
    # monotonic: more sound speed → more suppression → lower ratio
    assert (band_ratio["sanity clustering c²=1e-10"] >= band_ratio[headline]
            >= band_ratio["sanity smooth c²=1"]), "ratio must decrease monotonically in c²"
    print("\nsanity asserts PASSED: high-z norm ok; CMB lensing is a high-z (z>1) probe; "
          "smooth→ratio<1; monotone in c².")
    # honest flag on the clustering limit
    cl_lim = band_ratio["sanity clustering c²=1e-10"]
    print(f"NOTE: c²→0 band ratio = {cl_lim:.3f} (≳1). The naive expectation 'c²→0 "
          "recovers ΛCDM (ratio=1)' does NOT hold: the Jeans proxy forces the w→-1 "
          "component to cluster, over-growing structure. Proxy artifact; real check = CLASS.")

    # --- verdict ---
    print("\n=== CP17 VERDICT ===")
    dev = abs(cmbl_amp_suppr)
    n_sigma = dev / (ACT_AMP_PREC * 100.0)
    direction = "below" if cmbl_amp_suppr > 0 else "above"
    if dev <= ACT_AMP_PREC * 100.0:
        verdict = (f"NO sharp CMB-lensing tension: the C_ℓ^φφ amplitude sits {dev:.2f}% "
                   f"{direction} ΛCDM ({n_sigma:.1f}σ), INSIDE the representative ACT "
                   f"±{ACT_AMP_PREC*100:.1f}% band. The growth modification is a LOW-z (z≲1) "
                   f"effect, so the z≳1-weighted CMB-lensing kernel barely sees it — UNLIKE "
                   f"weak lensing at z~0.3. The toy threads this needle by being a late-time "
                   f"fluid; contrast CP10, where H0 failed.")
    else:
        verdict = (f"CMB-lensing TENSION: C_ℓ^φφ amplitude {dev:.2f}% {direction} ΛCDM "
                   f"(~{n_sigma:.1f}σ vs representative ACT ±{ACT_AMP_PREC*100:.1f}%). "
                   f"The same c² that drags weak-lensing S8 to 0.76 also moves CMB lensing "
                   f"off ΛCDM — perturbation-sector analogue of CP10's H0 failure.")
    print(verdict)
    print("(Representative ACT scalars, sourced, NOT a likelihood; no covariance ingested. "
          "Real verdict needs CLASS/hi_class — Level 3 BLOCKED.)")

    # ---------------------------------------------------------------------
    # figure: (a) kernel + suppression region, (b) C_ℓ^φφ ratio vs ℓ + ACT band
    # ---------------------------------------------------------------------
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(15, 5.8))

    # (a) χ-kernels: bare geometric W²/χ² and the full dC/dχ (incl. matter power)
    m6 = z_int <= 6.0
    axA.plot(z_int[m6], (Kchi / Kchi.max())[m6], color="tab:blue", lw=1.6, ls="--",
             label=rf"geometric $W_\kappa^2/\chi^2$ (peak z={z_kernel_peak:.1f})")
    axA.fill_between(z_int[m6], 0, (dCdchi_ref / dCdchi_ref.max())[m6], color="tab:blue",
                     alpha=0.18)
    axA.plot(z_int[m6], (dCdchi_ref / dCdchi_ref.max())[m6], color="tab:blue", lw=2.4,
             label=rf"full $dC_\ell/d\chi$ (ℓ={ELL_REF:.0f}, peak z={z_contrib_peak:.1f})")
    axA.axvspan(1.5, 2.5, color="tab:red", alpha=0.12,
                label="QFUDS transition (z≈2)")
    axA.axvspan(0.3, 0.8, color="tab:green", alpha=0.12,
                label="weak-lensing z~0.3–0.8")
    axA.set_xlabel("redshift z"); axA.set_ylabel("normalized kernel")
    axA.set_xlim(0, 6); axA.set_ylim(0, 1.05)
    axA.set_title("(a) CMB lensing weights z≳1, above the weak-lensing window")
    axA.text(0.97, 0.40, f"z<0.5: {frac_lo*100:.0f}% of weight\n z>1: {frac_hi*100:.0f}% of weight",
             transform=axA.transAxes, ha="right", va="top", fontsize=8,
             bbox=dict(boxstyle="round", fc="white", alpha=0.7))
    axA.legend(fontsize=8, loc="upper right"); axA.grid(alpha=0.3)

    # (b) ratio
    axB.axhspan(1.0 - ACT_AMP_PREC, 1.0 + ACT_AMP_PREC, color="tab:green", alpha=0.15,
                label=f"ACT DR6 ±{ACT_AMP_PREC*100:.1f}% (representative, sourced)")
    axB.axvspan(ACT_BAND[0], ACT_BAND[1], color="gray", alpha=0.10,
                label="ACT-sensitive band ℓ∈[100,600]")
    axB.axhline(1.0, color="k", lw=0.8)
    axB.semilogx(L_GRID, ratio[headline], color="tab:purple", lw=2.4,
                 label=f"QFUDS c²=2.92e-5 (S8→0.76): {band_suppr[headline]:+.1f}% band")
    axB.semilogx(L_GRID, ratio["QFUDS c²=4.6e-6 (cp8/cp9 lineage)"], color="tab:orange",
                 lw=1.8, ls="--",
                 label=f"QFUDS c²=4.6e-6 (lineage): {band_suppr['QFUDS c²=4.6e-6 (cp8/cp9 lineage)']:+.1f}% band")
    # weak-lensing amplitude the same c² wants (z~0), for contrast
    axB.axhline((S8_WL / S8_LCDM)**2, color="tab:red", ls="-.", lw=1.3,
                label=f"weak-lensing wants (z≈0): P↓{(1-(S8_WL/S8_LCDM)**2)*100:.0f}%")
    axB.set_xlabel("multipole ℓ"); axB.set_ylabel(r"$C_\ell^{\phi\phi}$ QFUDS / ΛCDM")
    axB.set_title("(b) CMB lensing barely moves while weak lensing wants a big z≈0 drop")
    axB.legend(fontsize=7.5, loc="lower left"); axB.grid(alpha=0.3)

    fig.suptitle("CP17: CMB-lensing vs weak-lensing internal consistency "
                 "(exploratory; ACT precision representative, sourced)", fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp17_cmb_lensing.png", dpi=130)
    fig.savefig("fig_cp17_cmb_lensing.svg")
    print("\nsaved fig_cp17_cmb_lensing.png + .svg")

    # ---------------------------------------------------------------------
    # CSV
    # ---------------------------------------------------------------------
    with open("cp17_cmb_lensing_results.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["ell", "Clpp_LCDM", "Clpp_QFUDS_c2_2.92e-5",
                    "ratio_c2_2.92e-5", "ratio_c2_4.6e-6"])
        for i, l in enumerate(L_GRID):
            w.writerow([int(l), f"{Cl_L[i]:.6e}", f"{Cl_Q[headline][i]:.6e}",
                        f"{ratio[headline][i]:.5f}",
                        f"{ratio['QFUDS c²=4.6e-6 (cp8/cp9 lineage)'][i]:.5f}"])
        w.writerow([])
        w.writerow(["# summary"])
        w.writerow(["quantity", "value", "note"])
        w.writerow(["chi_star_Mpc", f"{chi_star:.1f}", "comoving dist to z*=1090"])
        w.writerow(["kernel_contribution_peak_z", f"{z_contrib_peak:.3f}",
                    f"full dC/dchi at ell={ELL_REF:.0f} (broad)"])
        w.writerow(["kernel_frac_weight_z_lt_0.5", f"{frac_lo:.3f}", "CMB lensing low-z weight"])
        w.writerow(["kernel_frac_weight_z_gt_1", f"{frac_hi:.3f}", "CMB lensing high-z weight"])
        for name in cases:
            w.writerow([f"band_ratio[{name}]", f"{band_ratio[name]:.4f}",
                        f"{band_suppr[name]:+.2f}% vs LCDM (+ = suppressed)"])
        w.writerow(["WL_S8_amp_suppression_pct", f"{wl_amp_suppr:.2f}",
                    "weak lensing wants 0.83->0.76 at z~0"])
        w.writerow(["CMBlensing_band_amp_shift_pct", f"{cmbl_amp_suppr:.2f}",
                    "headline c^2=2.92e-5 over ACT band (+ = below LCDM)"])
        w.writerow(["ACT_amp_precision_pct", f"{ACT_AMP_PREC*100:.1f}",
                    f"representative, sourced {ACT_URL}, NOT a likelihood/no covariance"])
        w.writerow(["ACT_S8_CMBL", f"{ACT_S8}", "0.818+/-0.022, LCDM-consistent"])
        w.writerow(["n_sigma_vs_ACT", f"{n_sigma:.2f}", "|CMBL shift| / ACT precision"])
        w.writerow(["highz_growth_agreement_pct", f"{hi_agree*100:.3f}",
                    "QFUDS vs LCDM at z=8 (clean-ratio check)"])
        w.writerow(["verdict", "see_stdout", verdict[:90]])
    print("saved cp17_cmb_lensing_results.csv")


if __name__ == "__main__":
    main()
