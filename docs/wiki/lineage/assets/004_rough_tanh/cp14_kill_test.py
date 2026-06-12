"""
CP14: "이미 얼마나 죽었나" — score the two PRE-EXISTING falsifiable directions with
ACTUAL error bars and turn them into a verdict + a rough kill-by-date.

We do NOT invent new signals. We take the two falsifiable hooks already produced
upstream and convert each into a NUMBER WITH AN UNCERTAINTY:

  Part 1 — w(z) direction (CP6b):
      Project OUR density-driven w(z) (relax z*=5, barrier=2, mobility=2, lam=3)
      onto a CPL (w0, wa) point, and ask how many σ that point sits from a
      representative DESI-DR2-LIKE (w0, wa) ellipse — and in WHICH quadrant
      (our FREEZING wa>0 vs DESI THAWING wa<0).

  Part 2 — P(k) step (CP9):
      Take CP9's scale-dependent T(k)=P_QFUDS/P_LCDM step (data-fit ξ≈10 Mpc,
      c_s²=4.6e-6), marginalize an overall amplitude (so a uniform low-σ8 ΛCDM is
      NOT counted as signal), and run a crude Stage-IV weak-lensing Fisher on the
      residual SHAPE to get a rough SNR.

STATUS / HONESTY (read this):
  - Exploratory sandbox. PARAMETRIZE, not DERIVE. The whole w(a) is a hand-fit
    tanh order-parameter relaxation; nothing here is derived from foam
    microphysics. The "050 ceiling" (deriving the dark sector from foam
    microphysics) is UNTOUCHED.
  - This is NOT evidence, NOT a roadmap change.
  - ALL external survey numbers below — the DESI (w0,wa) center & covariance, the
    Euclid/LSST-like f_sky / n_eff / σ_γ — are REPRESENTATIVE / ILLUSTRATIVE
    round numbers chosen to be of the right order. They are NOT a fit to, or a
    quote from, any specific published data release. Do not cite them as such.
  - The Part-2 SNR is an ORDER-OF-MAGNITUDE proxy (single-plane Limber map k→ℓ,
    2D Gaussian mode count, representative shape-noise scale). The absolute SNR is
    uncertain by a factor of a few; only its order of magnitude and the
    amplitude-marginalization sanity check (uniform shift → ~0 shape SNR) are
    robust.
  - The REAL verdict needs a proper joint likelihood against the actual DESI
    chains and a real Stage-IV lensing covariance, run through a Boltzmann code
    (CLASS / hi_class). That is Level 3 and BLOCKED. Everything here is a
    back-of-envelope stand-in for that blocked computation.
"""
from __future__ import annotations

import csv
import numpy as np
from scipy.special import erfinv
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse

import model as M
import density_driven as dd
import cp9_lensing_pk as cp9

# ---------------------------------------------------------------------------
# Sanity on a textbook formula before using it: CPL w(a)=w0+wa(1-a).
# Known limits: w(a=1)=w0 (today), w(a->0)=w0+wa (early). Assert them.
# ---------------------------------------------------------------------------
def w_cpl(a, w0, wa):
    return w0 + wa * (1.0 - a)


assert abs(w_cpl(1.0, -0.9, 0.4) - (-0.9)) < 1e-12, "CPL today limit wrong"
assert abs(w_cpl(0.0, -0.9, 0.4) - (-0.9 + 0.4)) < 1e-12, "CPL early limit wrong"


# ===========================================================================
# PART 1 — w(z) -> CPL (w0, wa) projection, vs a representative DESI ellipse
# ===========================================================================
def our_w_interpolator():
    """OUR density-driven w(a) (relax z*=5,...): same curve used by CP6b/CP11."""
    phi = dd.relax(z_star=5.0, barrier=2.0, mobility=2.0, lam=3.0)
    w = -phi                                   # w_eff(a) on dd.A_GRID (increasing a)
    return dd.A_GRID, w


def fit_cpl(a_grid, w_grid, z_lo=0.0, z_hi=1.5, z_pivot=0.5, z_width=0.5):
    """
    Weighted linear least-squares of w(a)=w0+wa(1-a) to OUR w over the DE-relevant
    range z in [z_lo, z_hi]. Weight emphasizes where a DESI-like BAO+SNe set
    constrains w best (broad Gaussian window in z around the CPL pivot z~0.5).
    The weighting is REPRESENTATIVE, not a survey window function.
    Returns (w0, wa) and the sampled (z, w_model, w_fit) for plotting.
    """
    z = 1.0 / a_grid - 1.0
    sel = (z >= z_lo) & (z <= z_hi)
    a = a_grid[sel]
    w = w_grid[sel]
    zz = z[sel]
    weight = np.exp(-0.5 * ((zz - z_pivot) / z_width) ** 2)

    # design matrix X = [1, (1-a)]; solve (Xᵀ W X) p = Xᵀ W w
    X = np.column_stack([np.ones_like(a), (1.0 - a)])
    W = np.diag(weight)
    XtW = X.T @ W
    p = np.linalg.solve(XtW @ X, XtW @ w)
    w0, wa = float(p[0]), float(p[1])
    w_fit = w_cpl(a, w0, wa)
    order = np.argsort(zz)
    return w0, wa, zz[order], w[order], w_fit[order]


def desi_like_cov():
    """
    REPRESENTATIVE / ILLUSTRATIVE DESI-DR2-LIKE (w0,wa) 2D Gaussian.
    NOT a fit to a specific data release — round numbers of the right order,
    capturing the well-known w0-wa anti-correlation and a THAWING (wa<0) center.
    """
    w0c, wac = -0.70, -1.00
    sw0, swa = 0.07, 0.30
    rho = -0.9
    C = np.array([[sw0 ** 2, rho * sw0 * swa],
                  [rho * sw0 * swa, swa ** 2]])
    return np.array([w0c, wac]), C, (sw0, swa, rho)


def chi2_and_sigma(point, center, C):
    """Δχ² = Δᵀ C⁻¹ Δ and several honest 'how far' readings."""
    d = np.asarray(point) - np.asarray(center)
    Cinv = np.linalg.inv(C)
    chi2 = float(d @ Cinv @ d)
    mahalanobis = np.sqrt(chi2)              # joint-σ distance (2 dof)
    cl_2d = 1.0 - np.exp(-chi2 / 2.0)         # CL enclosed for a 2D Gaussian
    cl_2d_clip = min(cl_2d, 1 - 1e-16)
    sigma_1d_equiv = np.sqrt(2.0) * erfinv(cl_2d_clip)  # 1D-Gaussian σ at that CL
    return chi2, mahalanobis, cl_2d, sigma_1d_equiv


def quadrant_label(w0, wa):
    de = "FREEZING (wₐ>0: w was nearer 0 in the past)" if wa > 0 else \
         "THAWING (wₐ<0: w heading toward 0 in the future)"
    cosmo = "phantom-ish (w₀<-1)" if w0 < -1 else "quintessence-ish (w₀>-1)"
    return de, cosmo


# ===========================================================================
# PART 2 — P(k) step shape detectability (crude Stage-IV WL Fisher proxy)
# ===========================================================================
# Representative Euclid/LSST-like setup (ILLUSTRATIVE, not a survey spec).
F_SKY = 0.40
N_EFF_ARCMIN2 = 30.0          # gal / arcmin^2
SIGMA_GAMMA = 0.30            # shape noise per component
K_MAX = 0.20                  # Mpc^-1, linear-ish cutoff
Z_EFF_LENS = 0.7             # representative single-plane lensing distance
C2_FIT = 4.6e-6              # CP9 data-fit c_eff^2 (ξ≈10 Mpc)

ARCMIN_PER_RAD = 180.0 * 60.0 / np.pi   # 3437.75


def comoving_distance_lcdm(z):
    """D_C(z) = (c/H0) ∫_0^z dz'/E_ΛCDM, in Mpc. np.trapezoid (numpy 2.x)."""
    zz = np.linspace(0.0, z, 600)
    a = 1.0 / (1.0 + zz)
    E = np.array([float(M.E_LCDM(ai)) for ai in a])
    integ = np.trapezoid(1.0 / E, zz)
    return (M.C_KM_S / M.H0_CMB) * integ


def ell_noise_scale(chi_eff):
    """
    Representative multipole where weak-lensing shape noise ≈ signal per mode
    for the given (n_eff, σ_γ). White convergence noise N_ℓ = σ_γ²/n̄ (n̄ in
    sr^-1); a representative Stage-IV lensing signal makes N/C ≈ 1 near ℓ≈700.
    We anchor ℓ_noise to that scale and model N/C(ℓ) ≈ (ℓ/ℓ_noise)². This ties
    the noise term to the quoted survey numbers but is REPRESENTATIVE, not a
    computed C_ℓ^κκ.
    """
    n_sr = N_EFF_ARCMIN2 * ARCMIN_PER_RAD ** 2          # gal / sr
    N_white = SIGMA_GAMMA ** 2 / n_sr                    # ~2.5e-10 sr
    # representative Stage-IV convergence signal at the pivot (illustrative):
    C_pivot = 3.0e-10
    ell_pivot = 700.0
    # N/C = 1 where (ℓ/ℓ_noise)^2 = 1; calibrate ℓ_noise s.t. N/C(ℓ_pivot)=N_white/C_pivot
    nc_pivot = N_white / C_pivot
    ell_noise = ell_pivot / np.sqrt(max(nc_pivot, 1e-6))
    return ell_noise, N_white


def stage4_shape_snr(k, T, chi_eff, ell_noise):
    """
    Crude 2D-Gaussian Fisher on the amplitude-marginalized shape residual of the
    ratio R(k)=P_QFUDS/P_LCDM ≈ T(k), mapped k->ℓ=k·χ_eff (single-plane Limber).

      σ_R(k)/R = sqrt(2 / N_modes) · (1 + (ℓ/ℓ_noise)²)     [Knox-style]
      N_modes  = f_sky · (2ℓ+1) · Δℓ                         [2D annulus]
      Â        = Σ (T/σ²) / Σ (1/σ²)                          [marginalized amp]
      SNR²     = Σ [(T-Â)/σ_R]²                               [residual shape]

    Returns dict with per-k arrays and totals.
    """
    ell = k * chi_eff
    # Δℓ from log-k bin widths: Δk_i ≈ k_i·Δln k ; Δℓ = χ_eff·Δk
    dlnk = np.gradient(np.log(k))
    dk = k * dlnk
    d_ell = chi_eff * np.abs(dk)
    N_modes = F_SKY * (2.0 * ell + 1.0) * d_ell
    sig_cv = np.sqrt(2.0 / N_modes)                     # cosmic-variance rel. err
    noise_factor = 1.0 + (ell / ell_noise) ** 2
    sigma_R = sig_cv * noise_factor                     # relative error on R(k)

    inv_var = 1.0 / sigma_R ** 2
    A_hat = np.sum(T * inv_var) / np.sum(inv_var)        # best-fit uniform amp
    resid = T - A_hat                                    # detectable SHAPE
    snr_k = resid / sigma_R                              # per-k contribution
    snr_tot = float(np.sqrt(np.sum(snr_k ** 2)))
    return {
        "ell": ell, "sigma_R": sigma_R, "A_hat": float(A_hat),
        "resid": resid, "snr_k": snr_k, "snr_tot": snr_tot,
        "N_modes": N_modes,
    }


# ===========================================================================
# MAIN
# ===========================================================================
def main():
    print("=" * 74)
    print("CP14: scoring the two falsifiable hooks with error bars (exploratory)")
    print("All survey numbers are REPRESENTATIVE/ILLUSTRATIVE, not a release fit.")
    print("=" * 74)

    # ---------------- PART 1 ----------------
    print("\n--- Part 1: w(z) -> CPL (w0,wa) vs representative DESI ellipse ---")
    a_grid, w_grid = our_w_interpolator()

    # KEY honesty point: the CPL projection is fit-range sensitive because our
    # z*=5 transition is a SHARP step at z≈2, while CPL is a smooth ramp.
    #   (A) DESI low-z sweet spot z∈[0,1.5]: our model is FLAT at w=-1 there, so
    #       it projects onto ΛCDM (-1,0) — observationally hidden where DESI is
    #       strongest.
    #   (B) DESI full BAO reach z∈[0,2.3] (incl. Lyα): the step enters the window
    #       and the projection becomes mildly FREEZING (w0≲-1, wa>0). This is the
    #       apples-to-apples range matching how DESI fits its own (w0,wa).
    w0_lo, wa_lo, _, _, _ = fit_cpl(a_grid, w_grid, z_lo=0.0, z_hi=1.5,
                                    z_pivot=0.5, z_width=0.5)
    w0, wa, z_s, w_model_s, w_fit_s = fit_cpl(a_grid, w_grid, z_lo=0.0, z_hi=2.3,
                                              z_pivot=0.7, z_width=1.2)
    print(f"OUR density-driven w(z) projected onto CPL:")
    print(f"   (A) DESI low-z sweet spot z∈[0,1.5]: (w0,wa)=({w0_lo:+.3f},{wa_lo:+.3f})"
          f"  -> sits ON ΛCDM (model is flat w=-1 below z~1.8)")
    print(f"   (B) DESI full BAO reach  z∈[0,2.3]: (w0,wa)=({w0:+.3f},{wa:+.3f})"
          f"  -> the genuine projection (step enters window)")
    de_lab, cosmo_lab = quadrant_label(w0, wa)
    print(f"   quadrant of (B): {de_lab}; {cosmo_lab}")
    print(f"   CAVEAT: (w0,wa) is fit-range dependent (sharp step vs smooth CPL);"
          f" treat as indicative, not a unique projection.")

    center, C, (sw0, swa, rho) = desi_like_cov()
    print(f"representative DESI-like center (w0,wa)=({center[0]:+.2f},{center[1]:+.2f}), "
          f"σ=({sw0},{swa}), ρ={rho}  [ILLUSTRATIVE]")

    chi2_q, mah_q, cl_q, s1d_q = chi2_and_sigma([w0, wa], center, C)
    print(f"OUR (B) point vs DESI-like:  Δχ²={chi2_q:.1f}  "
          f"-> {mah_q:.1f}σ (joint, 2 dof), "
          f"CL={100*cl_q:.3f}%  (≈{s1d_q:.1f}σ 1D-equivalent)")

    chi2_a, mah_a, cl_a, s1d_a = chi2_and_sigma([w0_lo, wa_lo], center, C)
    print(f"OUR (A) point vs DESI-like:  Δχ²={chi2_a:.1f}  -> {mah_a:.1f}σ "
          f"(identical to ΛCDM — it IS ΛCDM in the low-z window)")

    lcdm_pt = [-1.0, 0.0]
    chi2_l, mah_l, cl_l, s1d_l = chi2_and_sigma(lcdm_pt, center, C)
    print(f"ΛCDM (-1,0) vs DESI-like: Δχ²={chi2_l:.1f}  "
          f"-> {mah_l:.1f}σ (joint), CL={100*cl_l:.2f}%")
    print(f"   NOTE: this illustrative ellipse is tight enough that even ΛCDM sits "
          f"~{mah_l:.0f}σ off — i.e. these representative error bars are aggressive;"
          f" treat the absolute σ with caution (real check = CLASS, BLOCKED).")

    # ---------------- PART 2 ----------------
    print("\n--- Part 2: CP9 P(k) step shape SNR (crude Stage-IV WL proxy) ---")
    chi_eff = comoving_distance_lcdm(Z_EFF_LENS)
    ell_noise, N_white = ell_noise_scale(chi_eff)
    print(f"map k->ℓ at χ_eff(z={Z_EFF_LENS})≈{chi_eff:.0f} Mpc; "
          f"k_max={K_MAX} -> ℓ_max≈{K_MAX*chi_eff:.0f}; "
          f"representative ℓ_noise≈{ell_noise:.0f}")

    # k grid up to k_max; reuse CP9's scale-dependent growth for T(k)
    k = np.logspace(-2.0, np.log10(K_MAX), 24)
    D1L = cp9.lcdm_D1()
    T = np.array([(cp9.D1_scaledep(ki, C2_FIT) / D1L) ** 2 for ki in k])
    kJ = cp9.k_jeans(C2_FIT)
    print(f"CP9 step: k_J≈{kJ:.3f} Mpc^-1 (c_s²={C2_FIT}); "
          f"T(k_min)={T[0]:.3f}, T(k_max)={T[-1]:.3f}")

    res = stage4_shape_snr(k, T, chi_eff, ell_noise)
    print(f"after marginalizing overall amplitude (Â={res['A_hat']:.3f}):")
    print(f"   shape residual SNR (Stage-IV-like) ≈ {res['snr_tot']:.1f}σ "
          f"[ORDER-OF-MAGNITUDE proxy]")

    # sanity: a UNIFORM amplitude shift (no step) must give ~0 shape SNR
    T_uniform = np.full_like(k, 0.90)
    res_uniform = stage4_shape_snr(k, T_uniform, chi_eff, ell_noise)
    print(f"sanity — uniform low-σ8 shift (flat T=0.90): "
          f"shape SNR = {res_uniform['snr_tot']:.2e}σ  (≈0 expected: a pure "
          f"amplitude shift carries NO shape information)")

    # ---------------- FIGURE ----------------
    fig, (axL, axR) = plt.subplots(1, 2, figsize=(15, 6.2))

    # (a) (w0,wa) plane
    eigval, eigvec = np.linalg.eigh(C)
    angle = np.degrees(np.arctan2(eigvec[1, 0], eigvec[0, 0]))
    for nsig, alpha in [(1, 0.30), (2, 0.15)]:
        width, height = 2 * nsig * np.sqrt(eigval)
        axL.add_patch(Ellipse(center, width, height, angle=angle,
                              facecolor="tab:blue", alpha=alpha,
                              edgecolor="tab:blue", lw=1.2,
                              label=f"DESI-like {nsig}σ (illustrative)"))
    axL.plot(*center, "o", color="tab:blue", ms=7, label="DESI-like center (thawing)")
    axL.plot(-1, 0, "ks", ms=8,
             label=f"ΛCDM (-1,0)  [{mah_l:.0f}σ; = our z<1.5 projection]")
    axL.plot(w0, wa, "*", color="tab:red", ms=18,
             label=f"OUR QFUDS, z∈[0,2.3] ({w0:+.2f}, {wa:+.2f})")
    axL.annotate(f"{mah_q:.0f}σ off\n(freezing vs\nthawing)",
                 xy=(w0, wa), xytext=(w0 + 0.05, wa - 0.55),
                 fontsize=10, color="tab:red", ha="left",
                 arrowprops=dict(arrowstyle="->", color="tab:red", lw=1.3))
    axL.axhline(0, color="gray", lw=0.8, ls=":")
    axL.axvline(-1, color="gray", lw=0.8, ls=":")
    axL.set_xlabel("$w_0$", fontsize=12)
    axL.set_ylabel("$w_a$", fontsize=12)
    axL.set_title("(a) CPL plane: our freezing point vs representative DESI ellipse")
    axL.legend(fontsize=8, loc="upper right")
    axL.grid(alpha=0.3)

    # (b) P(k) shape residual + error band + SNR
    band_lo = res["resid"] - res["sigma_R"]
    band_hi = res["resid"] + res["sigma_R"]
    axR.axhline(0.0, color="k", lw=0.8)
    axR.fill_between(k, band_lo, band_hi, color="tab:purple", alpha=0.20,
                     label="Stage-IV-like ±1σ per-k (crude proxy)")
    axR.semilogx(k, res["resid"], "o-", color="tab:purple", lw=2,
                 label="QFUDS shape residual  T(k) − Â")
    axR.axvline(kJ, color="tab:green", ls=":", lw=1.4, label=f"k_J≈{kJ:.2f} (step)")
    axR.semilogx(k, res_uniform["resid"], "x--", color="gray", lw=1.2,
                 label="uniform low-σ8 (residual ≈ 0)")
    axR.set_xlabel("k  [Mpc⁻¹]", fontsize=12)
    axR.set_ylabel("amplitude-marginalized shape residual", fontsize=12)
    axR.set_title(f"(b) P(k) step shape SNR ≈ {res['snr_tot']:.0f}σ  (order-of-magnitude)")
    axR.legend(fontsize=8, loc="lower left")
    axR.grid(alpha=0.3)

    fig.suptitle("CP14: how dead is it already? — two falsifiable hooks scored "
                 "(exploratory; survey numbers illustrative)", fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp14_kill_test.png", dpi=130)
    fig.savefig("fig_cp14_kill_test.svg")
    print("\nsaved fig_cp14_kill_test.png + .svg")

    # ---------------- CSV ----------------
    with open("cp14_kill_test_results.csv", "w", newline="") as fh:
        wtr = csv.writer(fh)
        wtr.writerow(["# CP14 kill test — exploratory; survey numbers ILLUSTRATIVE, "
                      "not a release fit; real verdict = CLASS, Level 3, BLOCKED"])
        wtr.writerow([])
        wtr.writerow(["# Part 1: w(z)->CPL projection and distances"])
        wtr.writerow(["quantity", "w0", "wa"])
        wtr.writerow(["our_QFUDS_CPL_z0to2.3_PRIMARY", f"{w0:.4f}", f"{wa:.4f}"])
        wtr.writerow(["our_QFUDS_CPL_z0to1.5_lowz", f"{w0_lo:.4f}", f"{wa_lo:.4f}"])
        wtr.writerow(["DESI_like_center_ILLUSTRATIVE", f"{center[0]:.4f}", f"{center[1]:.4f}"])
        wtr.writerow(["LCDM_reference", "-1.0", "0.0"])
        wtr.writerow([])
        wtr.writerow(["point", "delta_chi2", "mahalanobis_sigma_2dof",
                      "CL_2D_percent", "sigma_1D_equiv"])
        wtr.writerow(["our_QFUDS_z0to2.3", f"{chi2_q:.3f}", f"{mah_q:.3f}",
                      f"{100*cl_q:.4f}", f"{s1d_q:.3f}"])
        wtr.writerow(["our_QFUDS_z0to1.5", f"{chi2_a:.3f}", f"{mah_a:.3f}",
                      f"{100*cl_a:.4f}", f"{s1d_a:.3f}"])
        wtr.writerow(["LCDM", f"{chi2_l:.3f}", f"{mah_l:.3f}",
                      f"{100*cl_l:.4f}", f"{s1d_l:.3f}"])
        wtr.writerow(["# DESI-like cov", f"sw0={sw0}", f"swa={swa}", f"rho={rho}"])
        wtr.writerow([])
        wtr.writerow(["# Part 2: P(k) step shape SNR (crude Stage-IV WL proxy)"])
        wtr.writerow([f"# f_sky={F_SKY}, n_eff={N_EFF_ARCMIN2}/arcmin^2, "
                      f"sigma_gamma={SIGMA_GAMMA}, k_max={K_MAX}, "
                      f"chi_eff={chi_eff:.1f} Mpc, ell_noise={ell_noise:.0f}, "
                      f"c_s2={C2_FIT}, A_hat={res['A_hat']:.4f}"])
        wtr.writerow(["k_Mpc^-1", "ell", "T_ratio", "shape_residual",
                      "sigma_R", "snr_per_k", "snr2_cumulative"])
        snr2_cum = 0.0
        for i in range(len(k)):
            snr2_cum += res["snr_k"][i] ** 2
            wtr.writerow([f"{k[i]:.5g}", f"{res['ell'][i]:.1f}", f"{T[i]:.5f}",
                          f"{res['resid'][i]:+.5f}", f"{res['sigma_R'][i]:.5f}",
                          f"{res['snr_k'][i]:+.4f}", f"{np.sqrt(snr2_cum):.4f}"])
        wtr.writerow(["TOTAL_SNR", "", "", "", "", "", f"{res['snr_tot']:.4f}"])
        wtr.writerow(["SANITY_uniform_shift_SNR", "", "", "", "", "",
                      f"{res_uniform['snr_tot']:.3e}"])
    print("saved cp14_kill_test_results.csv")

    # ---------------- VERDICT ----------------
    print("\n" + "=" * 74)
    print("VERDICT (representative numbers — real check is CLASS, Level 3, BLOCKED):")
    print(f"  w(z): OUR ({w0:+.2f},{wa:+.2f}) is FREEZING (wa>0); representative DESI")
    print(f"        center is THAWING (wa<0). Opposite quadrant, {mah_q:.0f}σ away.")
    print(f"        -> already strongly disfavored IF the illustrative DESI holds.")
    print(f"  P(k): step shape detectable at ≈{res['snr_tot']:.0f}σ by a Stage-IV-like")
    print(f"        lensing survey (order-of-magnitude); a uniform shift gives ~0.")
    print(f"        -> a clean, near-future kill/confirm handle (this decade).")
    print("=" * 74)


if __name__ == "__main__":
    main()
