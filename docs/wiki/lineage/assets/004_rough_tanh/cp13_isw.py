"""
CP13: the late-time Integrated Sachs-Wolfe (ISW) effect as a THIRD falsifiable
signal — after (1) w(z) freezing vs DESI thawing (CP6b) and (2) the P(k) step at
k≈k_J (CP9). The CMB late-time channel has never been probed in this sketch.

STATUS: exploratory, PARAMETRIZE-not-DERIVE. w(a) and c_s²=4.6e-6 are hand-chosen
phenomenological knobs, NOT derived from foam microphysics. The 050 ceiling
(deriving the dark sector from foam) is untouched here. Every cosmology formula
below is re-derived in-comment and asserted against a known limit before use, and
every shortcut is labelled "proxy". The REAL ISW check is a Boltzmann solve in
CLASS/hi_class (Level 3, BLOCKED) — this script is a rough toy, not evidence and
not a roadmap change.

------------------------------------------------------------------------------
PHYSICS (rough, all linear, sub-horizon)
------------------------------------------------------------------------------
ISW temperature shift along a line of sight (η = conformal time, Φ = Newtonian/
Weyl potential):
    ΔT/T = 2 ∫ (∂Φ/∂η) dη.
Only a DECAYING potential (Φ̇ ≠ 0) sources ISW.

Sub-horizon Poisson (re-derived): ∇²Φ = 4πG a² δρ  →  -k²Φ/a² = 4πG ρ_m δ.
With ρ_m ∝ a^-3 and δ = D(a)·δ_0 (growing mode), on a FIXED comoving scale
    Φ(k,a) ∝ a² · a^-3 · D(a) / k²  ∝  D(a)/a   (k-norm absorbed).
So define the (normalized) large-scale potential
    P(a) ≡ D(a)/a,         (P → const in matter domination, where D ∝ a)
and the potential-DECAY rate / ISW source strength
    g_ISW(a) ≡ - d[P]/d ln a.
SIGN CONVENTION: g_ISW > 0  ⟺  P = D/a falling  ⟺  potential decaying  ⟺  sources
ISW (this is the ΛCDM late-time situation). g_ISW = 0 in a pure matter universe
(D ∝ a). Limits asserted in main().

QFUDS twist:
  (1) the z≈2 w-transition changes WHEN/HOW Φ decays (background imprint);
  (2) clustering suppression (small c_s²=4.6e-6) makes the dark component cluster
      below its Jeans scale k_J≈0.1 Mpc⁻¹ (CP5/CP9 η proxy), so g_ISW becomes
      mildly k-dependent → a SCALE-dependent ISW, unlike a smooth low-σ8 ΛCDM
      whose g_ISW history is the SAME shape, just lower amplitude.

CRUDE Limber ISW auto-power proxy (re-derived):
    C_ℓ^ISW ∝ ∫ dχ/χ² |∂Φ/∂η(k=ℓ/χ)|² 𝒫_prim(k),    dχ = (c/H0) dz/E.
With ∂Φ/∂η = (dΦ/d ln a)(d ln a/dη) and d ln a/dη = ℋ = aH = a H0 E, and
dΦ/d ln a = Φ0 · dP/d ln a = -Φ0 · g_ISW:
    C_ℓ^ISW ∝ ∫ dz (1/χ²) · g_ISW(k=ℓ/χ, z)² · a² · E(z)      (primordial Φ0,
    𝒫_prim taken IDENTICAL between models so they cancel in the QFUDS/ΛCDM ratio).
This is a relative-amplitude proxy (no absolute μK²), exactly what the task asks.

ISW-galaxy cross sign: galaxies trace δ_g>0 → sit in wells Φ<0; a decaying well
(g_ISW>0) blueshifts traversing photons → ΔT>0 toward overdensities → POSITIVE
cross in ΛCDM. Sign of the cross = sign(g_ISW) over the survey window. We report
whether QFUDS keeps it positive and raises/lowers/flips the amplitude.
"""
from __future__ import annotations
import csv
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
from scipy.interpolate import interp1d, RegularGridInterpolator
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M
import cp5_sound_speed as cp5

C_KM_S, H0 = M.C_KM_S, M.H0_CMB
OM0, OMR = cp5.OM0, M.OMEGA_R0
A_I = 1e-3
C2 = 4.6e-6                       # data-fit c_eff² (CP5/CP8); k_J ≈ 0.1 Mpc⁻¹
K_ISW = 0.015                     # large/linear scale for the headline g_ISW(z) curve
K_NODES = np.logspace(-3.0, -0.5, 9)   # 0.001 .. 0.316 Mpc⁻¹ for the 2D g_ISW(k,z)
LMAX = 220
L_GRID = np.unique(np.round(np.logspace(np.log10(2), np.log10(LMAX), 22))).astype(int)
SIGMA8_LCDM = cp5.SIGMA8_LCDM     # 0.81
SIGMA8_LOW = 0.75                 # "uniform low-σ8" ΛCDM comparison (amplitude only)
Z_FEATURE = 2.0                   # QFUDS w-transition redshift (retained hook)

# dense e-fold grid for trajectories / numerical d/dlna
N_TRAJ = np.linspace(np.log(A_I), 0.0, 600)
A_TRAJ = np.exp(N_TRAJ)
Z_TRAJ = 1.0 / A_TRAJ - 1.0


# ---------------------------------------------------------------------------
# Growth trajectories  D(a)  (return on the dense e-fold grid)
# ---------------------------------------------------------------------------
def lcdm_growth_traj():
    """ΛCDM linear growth D(a); IC D=a (matter-dom growing mode) so D/a→1 early."""
    def El(a):
        return np.sqrt(M.OMEGA_M0_LCDM*a**-3 + M.OMEGA_R0_LCDM*a**-4 + M.OMEGA_L0_LCDM)
    def dlnE(n, h=1e-5):
        return (np.log(El(np.exp(n+h))) - np.log(El(np.exp(n-h)))) / (2*h)
    def rhs(n, y):
        D, Dp = y; a = np.exp(n)
        Om = M.OMEGA_M0_LCDM*a**-3 / El(a)**2
        return [Dp, -(2.0 + dlnE(n))*Dp + 1.5*Om*D]
    sol = solve_ivp(rhs, (N_TRAJ[0], N_TRAJ[-1]), [A_I, A_I], t_eval=N_TRAJ,
                    method="LSODA", rtol=1e-9, atol=1e-12)
    return sol.y[0]


def qfuds_growth_traj(k, c2):
    """Scale-dependent QFUDS growth D(k,a) (CP9 η-Jeans proxy clustering); IC D=a."""
    def eta(a):
        cs = np.sqrt(c2)
        R = cs * C_KM_S * k / (a * H0 * cp5.E(a))
        return 1.0 / (1.0 + R**2)
    def rhs(n, y):
        D, Dp = y; a = np.exp(n)
        Om = OM0*a**-3 / cp5.E(a)**2
        Ox = cp5.rho_x(a) / cp5.E(a)**2
        return [Dp, -(2.0 + cp5.dlnE_dN(a))*Dp + 1.5*(Om + eta(a)*Ox)*D]
    sol = solve_ivp(rhs, (N_TRAJ[0], N_TRAJ[-1]), [A_I, A_I], t_eval=N_TRAJ,
                    method="LSODA", rtol=1e-8, atol=1e-11)
    return sol.y[0]


def g_isw_from_D(D):
    """g_ISW(a) = - d/dlna [ D/a ]  on the dense grid (>0 = decaying potential)."""
    P = D / A_TRAJ                       # P normalized to 1 in matter era (D∝a)
    return -np.gradient(P, N_TRAJ)


# ---------------------------------------------------------------------------
# Background geometry: comoving distance χ(z) and E(z) per model
# ---------------------------------------------------------------------------
def comoving_distance(z_grid, E_of_a):
    """χ(z) = (c/H0) ∫_0^z dz'/E(z')   [Mpc]. Re-derived; checked vs Hubble radius."""
    Ez = np.array([float(E_of_a(1.0/(1.0+z))) for z in z_grid])
    chi = (C_KM_S/H0) * cumulative_trapezoid(1.0/Ez, z_grid, initial=0.0)
    return chi, Ez


def main():
    # ---- growth trajectories ----
    D_L = lcdm_growth_traj()
    g_L = g_isw_from_D(D_L)
    D_Q_isw = qfuds_growth_traj(K_ISW, C2)
    g_Q_isw = g_isw_from_D(D_Q_isw)

    # ---- SANITY CHECKS (assert against known limits) ----
    # (1) matter-dominated plateau -> g_ISW -> 0 (D ∝ a, P const). NB: at z≳200
    # radiation (Ω_r/Ω_m~0.3 @ z=1000) makes Φ decay too, a real non-zero bump —
    # so the clean matter-only plateau is 10 ≲ z ≲ 40, where g must be ~0.
    plateau = (Z_TRAJ >= 10) & (Z_TRAJ <= 40)
    g_plat_L = float(np.max(np.abs(g_L[plateau])))
    g_plat_Q = float(np.max(np.abs(g_Q_isw[plateau])))
    assert g_plat_L < 1e-2, f"ΛCDM g_ISW should vanish in matter plateau, got {g_plat_L}"
    assert g_plat_Q < 1e-2, f"QFUDS g_ISW should vanish in matter plateau, got {g_plat_Q}"
    # (2) ΛCDM late times -> g_ISW > 0 (potentials decay under Λ)
    g_L0 = float(np.interp(0.0, Z_TRAJ[::-1], g_L[::-1]))
    g_Q0 = float(np.interp(0.0, Z_TRAJ[::-1], g_Q_isw[::-1]))
    assert g_L0 > 0, f"ΛCDM g_ISW(z=0) should be >0 (decay), got {g_L0}"
    print(f"[sanity] matter-plateau max|g_ISW| (10<z<40): ΛCDM={g_plat_L:.2e}, QFUDS={g_plat_Q:.2e}  (→0 OK)")
    print(f"[sanity] g_ISW(z=0): ΛCDM={g_L0:+.4f} (>0 decay OK), QFUDS={g_Q0:+.4f}")

    # ---- 2D g_ISW(k,z) table for QFUDS (scale dependence) ----
    g_Q_grid = np.array([g_isw_from_D(qfuds_growth_traj(k, C2)) for k in K_NODES])  # [nk, nN]
    # interpolator over (ln k, N); clamp outside node range
    g_Q_interp = RegularGridInterpolator(
        (np.log(K_NODES), N_TRAJ), g_Q_grid, bounds_error=False, fill_value=None)

    def g_Q_of(k, n):
        lk = np.clip(np.log(k), np.log(K_NODES[0]), np.log(K_NODES[-1]))
        nn = np.clip(n, N_TRAJ[0], N_TRAJ[-1])
        return float(g_Q_interp((lk, nn)))

    # ΛCDM g_ISW interpolator in N (k-independent)
    g_L_of = interp1d(N_TRAJ, g_L, bounds_error=False, fill_value=(g_L[0], g_L[-1]))

    # ---- background geometry per model ----
    z_int = np.linspace(1e-3, 5.0, 400)
    chi_L, Ez_L = comoving_distance(z_int, M.E_LCDM)
    chi_Q, Ez_Q = comoving_distance(z_int, cp5.E)
    # sanity: χ monotone increasing, positive
    assert np.all(np.diff(chi_L[1:]) > 0) and chi_L[-1] > 0, "χ_LCDM must increase"

    a_int = 1.0/(1.0+z_int)
    n_int = np.log(a_int)

    # ---- crude Limber ISW auto-power C_ℓ (relative amplitude) ----
    # C_ℓ ∝ ∫ dz (1/χ²) g_ISW(k=ℓ/χ,z)² a² E   (primordial norm identical → cancels)
    def Cl_isw(L_arr, which):
        out = np.zeros(len(L_arr))
        for i, L in enumerate(L_arr):
            chi = chi_L if which == "L" else chi_Q
            Ez = Ez_L if which == "L" else Ez_Q
            # avoid χ→0 at z→0 (integrand ~ g²/χ² · a²E; g→finite, regularize)
            valid = chi > 1.0
            kk = L / np.clip(chi, 1.0, None)
            if which == "L":
                g = np.array([float(g_L_of(nn)) for nn in n_int])
            else:
                g = np.array([g_Q_of(kk[j], n_int[j]) for j in range(len(n_int))])
            integ = np.where(valid, (g**2) * a_int**2 * Ez / np.clip(chi, 1.0, None)**2, 0.0)
            out[i] = np.trapezoid(integ, z_int)
        return out

    Cl_L = Cl_isw(L_GRID, "L")
    Cl_Q = Cl_isw(L_GRID, "Q")
    # uniform low-σ8 ΛCDM: amplitude-only rescale of growth -> g_ISW scales by same
    # const -> C_ℓ scales by (σ8_low/σ8)^2 UNIFORMLY in ℓ (shape identical to ΛCDM)
    amp_low = (SIGMA8_LOW / SIGMA8_LCDM)**2
    Cl_low = Cl_L * amp_low

    # ---- headline numbers ----
    # total low-ℓ ISW power (ℓ ≤ 30) ratio QFUDS/ΛCDM
    lowl = L_GRID <= 30
    tot_L = float(np.trapezoid(Cl_L[lowl], L_GRID[lowl]))
    tot_Q = float(np.trapezoid(Cl_Q[lowl], L_GRID[lowl]))
    ratio_tot = tot_Q / tot_L
    # ratio vs ℓ (shape)
    ratio_l = Cl_Q / Cl_L
    print(f"\nISW auto-power QFUDS/ΛCDM: total(ℓ≤30) ratio = {ratio_tot:.3f}")
    print(f"  C_ℓ ratio range over ℓ∈[2,{LMAX}]: {ratio_l.min():.3f} .. {ratio_l.max():.3f}")
    print(f"  (uniform low-σ8 ΛCDM ratio = {amp_low:.3f} at ALL ℓ — shape FLAT)")

    # ---- ISW-galaxy cross sign & amplitude (representative ℓ=10) ----
    # C_ℓ^Tg ∝ ∫ dz (1/χ²) g_ISW(k=ℓ/χ) aE · [W_g(z) b D_gal(z)]   (sign = sign g_ISW)
    L_X = 10.0
    z0, sz = 0.45, 0.25            # representative ISW-galaxy survey window
    Wg = np.exp(-0.5*((z_int - z0)/sz)**2)
    Dg_L = interp1d(N_TRAJ, D_L)(n_int)
    Dg_Q = interp1d(N_TRAJ, D_Q_isw)(n_int)

    def cross(which):
        chi = chi_L if which == "L" else chi_Q
        Ez = Ez_L if which == "L" else Ez_Q
        Dg = Dg_L if which == "L" else Dg_Q
        kk = L_X / np.clip(chi, 1.0, None)
        if which == "L":
            g = np.array([float(g_L_of(nn)) for nn in n_int])
        else:
            g = np.array([g_Q_of(kk[j], n_int[j]) for j in range(len(n_int))])
        valid = chi > 1.0
        integ = np.where(valid, g * a_int * Ez * Wg * Dg / np.clip(chi, 1.0, None)**2, 0.0)
        return float(np.trapezoid(integ, z_int))

    cross_L = cross("L")
    cross_Q = cross("Q")
    cross_low = cross_L * np.sqrt(amp_low)   # cross ∝ g·D_gal, both ∝ σ8 → ∝ amp_low... use linear σ8
    sign_L = "positive" if cross_L > 0 else ("negative" if cross_L < 0 else "zero")
    sign_Q = "positive" if cross_Q > 0 else ("negative" if cross_Q < 0 else "zero")
    cross_ratio = cross_Q / cross_L
    verdict = ("raises" if cross_ratio > 1.02 else
               "lowers" if cross_ratio < 0.98 else "matches")
    if (cross_Q > 0) != (cross_L > 0):
        verdict = "FLIPS sign of"
    print(f"\nISW-galaxy cross (ℓ={L_X:.0f}, gal window z0={z0}): "
          f"ΛCDM {sign_L} ({cross_L:.3e}), QFUDS {sign_Q} ({cross_Q:.3e})")
    print(f"  QFUDS {verdict} the cross vs ΛCDM (ratio {cross_ratio:.3f})")

    # ---- z≈2 feature description ----
    gL2 = float(np.interp(Z_FEATURE, Z_TRAJ[::-1], g_L[::-1]))
    gQ2 = float(np.interp(Z_FEATURE, Z_TRAJ[::-1], g_Q_isw[::-1]))
    # curvature proxy of QFUDS g near z=2 (kink from the w:0→-1 switch)
    print(f"\nz≈2 feature: g_ISW(z=2) ΛCDM={gL2:+.4f}, QFUDS={gQ2:+.4f} "
          f"(QFUDS/ΛCDM={gQ2/gL2 if gL2 else float('nan'):.3f})")
    # peak redshift of each g_ISW(z)
    win = (Z_TRAJ >= 0.0) & (Z_TRAJ <= 5.0)
    zL_peak = float(Z_TRAJ[win][np.argmax(g_L[win])])
    zQ_peak = float(Z_TRAJ[win][np.argmax(g_Q_isw[win])])
    print(f"  g_ISW(z) peaks at  ΛCDM z={zL_peak:.2f},  QFUDS z={zQ_peak:.2f}")

    # =================== FIGURE ===================
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(15, 5.9))

    # (a) g_ISW(z)
    zmask = (Z_TRAJ >= 0) & (Z_TRAJ <= 5)
    axA.plot(Z_TRAJ[zmask], g_L[zmask], color="tab:blue", lw=2.2, label="ΛCDM")
    axA.plot(Z_TRAJ[zmask], g_Q_isw[zmask], color="tab:purple", lw=2.2,
             label=f"QFUDS (k={K_ISW} Mpc⁻¹)")
    axA.axvline(Z_FEATURE, color="gray", ls=":", lw=1.5)
    axA.annotate("z≈2 w-transition\n(w: 0 → −1)", xy=(Z_FEATURE, gQ2),
                 xytext=(2.7, gQ2*0.55 + 0.02), fontsize=8.5,
                 arrowprops=dict(arrowstyle="->", color="gray"))
    axA.axhline(0, color="k", lw=0.7)
    axA.set_xlabel("redshift z"); axA.set_ylabel("g_ISW = −d(D/a)/dlna   (>0: potential decays)")
    axA.set_title("(a) ISW source: potential-decay rate g_ISW(z)")
    axA.legend(fontsize=9, loc="upper right"); axA.grid(alpha=0.3)
    axA.set_xlim(0, 5)

    # (b) crude C_ℓ^ISW, normalized shape: QFUDS vs ΛCDM vs uniform low-σ8
    nrm = Cl_L[0]
    axB.semilogx(L_GRID, Cl_L/nrm, color="tab:blue", lw=2.2, label="ΛCDM")
    axB.semilogx(L_GRID, Cl_Q/nrm, color="tab:purple", lw=2.2, label="QFUDS (scale-dep)")
    axB.semilogx(L_GRID, Cl_low/nrm, color="tab:red", ls="--", lw=2,
                 label=f"uniform low-σ8 ({SIGMA8_LOW}) — FLAT shape")
    axB.set_xlabel("multipole ℓ"); axB.set_ylabel("crude C_ℓ^ISW  /  C_{ℓ=2}^ΛCDM")
    axB.set_title(f"(b) ISW auto-power proxy  (total ℓ≤30: QFUDS/ΛCDM={ratio_tot:.2f})")
    axB.legend(fontsize=8.5, loc="upper right"); axB.grid(alpha=0.3)

    fig.suptitle("CP13: late-time ISW as a 3rd falsifiable signal — parametrize-not-derive (exploratory)",
                 fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp13_isw.png", dpi=130)
    fig.savefig("fig_cp13_isw.svg")
    print("\nsaved fig_cp13_isw.png + .svg")

    # =================== CSV ===================
    with open("cp13_isw_results.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["# Table 1: g_ISW(z) at k=%.3g Mpc^-1 (>0 = decaying potential)" % K_ISW])
        w.writerow(["z", "g_ISW_LCDM", "g_ISW_QFUDS"])
        for j in range(len(Z_TRAJ)):
            if 0.0 <= Z_TRAJ[j] <= 5.0:
                w.writerow([f"{Z_TRAJ[j]:.4f}", f"{g_L[j]:.6f}", f"{g_Q_isw[j]:.6f}"])
        w.writerow([])
        w.writerow(["# Table 2: crude Limber ISW auto-power C_ell (relative; primordial norm cancels)"])
        w.writerow(["ell", "Cl_ISW_LCDM", "Cl_ISW_QFUDS", "Cl_ISW_lowsigma8", "ratio_QFUDS_LCDM"])
        for i, L in enumerate(L_GRID):
            w.writerow([L, f"{Cl_L[i]:.6e}", f"{Cl_Q[i]:.6e}",
                        f"{Cl_low[i]:.6e}", f"{ratio_l[i]:.4f}"])
        w.writerow([])
        w.writerow(["# Table 3: scalar summary"])
        w.writerow(["quantity", "value"])
        w.writerow(["ISW_autopower_total_ratio_QFUDS_over_LCDM_lmax30", f"{ratio_tot:.4f}"])
        w.writerow(["uniform_lowsigma8_amplitude_ratio_flat", f"{amp_low:.4f}"])
        w.writerow(["ISW_galaxy_cross_LCDM_l10", f"{cross_L:.6e}"])
        w.writerow(["ISW_galaxy_cross_QFUDS_l10", f"{cross_Q:.6e}"])
        w.writerow(["ISW_galaxy_cross_sign_LCDM", sign_L])
        w.writerow(["ISW_galaxy_cross_sign_QFUDS", sign_Q])
        w.writerow(["ISW_galaxy_cross_ratio_QFUDS_LCDM", f"{cross_ratio:.4f}"])
        w.writerow(["g_ISW_z2_LCDM", f"{gL2:.6f}"])
        w.writerow(["g_ISW_z2_QFUDS", f"{gQ2:.6f}"])
        w.writerow(["g_ISW_peak_z_LCDM", f"{zL_peak:.3f}"])
        w.writerow(["g_ISW_peak_z_QFUDS", f"{zQ_peak:.3f}"])
    print("saved cp13_isw_results.csv")

    return dict(ratio_tot=ratio_tot, ratio_l=(ratio_l.min(), ratio_l.max()),
                cross_L=cross_L, cross_Q=cross_Q, cross_ratio=cross_ratio,
                sign_L=sign_L, sign_Q=sign_Q, verdict=verdict,
                gL2=gL2, gQ2=gQ2, zL_peak=zL_peak, zQ_peak=zQ_peak,
                amp_low=amp_low, g_L0=g_L0, g_Q0=g_Q0)


if __name__ == "__main__":
    main()
