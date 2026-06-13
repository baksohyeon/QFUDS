"""
CP16: the growth-index γ fingerprint — is QFUDS clustering-DE degenerate with
modified gravity in the standard growth diagnostic?

The growth rate f(a) ≡ dlnD/dlna is famously fit by

        f(a) = Ω_m(a)^γ

with γ ≈ 0.55 for ΛCDM/GR (Wang & Steinhardt 1998; Linder 2005). Modified-gravity
backgrounds shift γ: f(R) gravity → γ ≈ 0.42 (enhanced growth), DGP → γ ≈ 0.68
(suppressed growth). γ is therefore a compact "fingerprint" of how a model grows
structure relative to GR at a given background Ω_m(a).

QUESTION: when the QFUDS dark fluid only PARTIALLY clusters (small c_s², η Jeans
suppression), does it imprint an effective γ(z) that looks like ΛCDM, like MG, or
like neither — i.e. is QFUDS DEGENERATE with MG in this diagnostic, or
DISTINGUISHABLE?

WHAT IS COMPUTED
  1. Linear growth D(a), f(a)=D'/D (N=ln a, ' = d/dN) for:
        (i)  ΛCDM (standard GR growth — sanity-checked to reproduce γ≈0.55),
        (ii) QFUDS V2-class clustering-DE: the density-driven background of
             CP5/CP11 (cp5.E, cp5.rho_x) with the η Jeans clustering suppression
             at the data-fit c_s² = 4.6e-6. Source term uses the effective
             clustering fraction Ω_clust = Ω_m + η(a,k) Ω_X.
  2. EFFECTIVE growth index inverted as γ_eff(a) = ln f(a) / ln Ω_m(a), where
     Ω_m(a) is the ORDINARY clustering-matter fraction Ω_m0 a⁻³/E² (the quantity
     an observer reads off the background — they do NOT know η Ω_X is secretly
     clustering). This is the standard observational diagnostic, so any deviation
     from 0.55 is exactly the "fingerprint".
  3. Compare γ_eff(z) and γ_eff(z=0) to ΛCDM 0.55, f(R) 0.42, DGP 0.68; report
     whether QFUDS sits INSIDE the MG band (degenerate) or OUTSIDE
     (distinguishable), and whether γ_eff is SCALE-DEPENDENT (itself a
     distinguishing feature, since standard γ is scale-independent).

SCALE: primary curve at the S8 scale k = 0.2 Mpc⁻¹ (= cp5.K8). η = 1/(1+R²) with
R = c_s·c·k/(aH) clusters the dark fluid on LARGE scales (small k, η→1) and keeps
it smooth on SMALL scales (large k, η→0) — so γ_eff is k-dependent and we report
the spread across k explicitly.

PARAMETRIZE-not-DERIVE: w(a), c_s², and the Jeans η are PHENOMENOLOGICAL knobs.
Nothing here is derived from foam microphysics — the "050 ceiling" (deriving the
dark sector, including δQ transfer and the true c_eff², from the foam sector)
STANDS UNTOUCHED. This is a rough toy answering "how far does it go, as a curve."
NOT a derived theory, NOT evidence, NOT a roadmap change. The η Jeans factor is a
proxy for the real sub-horizon pressure (CP11 showed it tracks the full 2-fluid
to a few percent over the WL band, but it is still a proxy). The REAL growth-index
check is the coupled clustering-DE perturbations in CLASS/hi_class — that is
Level 3 and BLOCKED.
"""
from __future__ import annotations
import csv
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M
import density_driven as dd          # noqa: F401  (kept for provenance/parity)
import cp5_sound_speed as cp5

# --------------------------------------------------------------------------- #
# constants / knobs
# --------------------------------------------------------------------------- #
C_KM_S = M.C_KM_S
H0 = M.H0_CMB
A_I = 1e-3
C2 = 4.6e-6                  # data-fit c_eff² (same as CP11)
K_S8 = 0.2                  # Mpc⁻¹, representative S8 scale (= cp5.K8)
K_SCAN = [0.01, 0.05, 0.2, 0.5, 1.0]    # for the scale-dependence report

OM0 = cp5.OM0               # 0.315 ordinary clustering matter (V2)
OML_M = M.OMEGA_M0_LCDM
OML_R = M.OMEGA_R0_LCDM
OML_L = M.OMEGA_L0_LCDM

# literature growth-index anchors
GAMMA_LCDM = 0.55
GAMMA_FR = 0.42            # f(R) gravity (enhanced growth)
GAMMA_DGP = 0.68          # DGP braneworld (suppressed growth)


# --------------------------------------------------------------------------- #
# ΛCDM background + growth (the GR reference)
# --------------------------------------------------------------------------- #
def E_lcdm(a):
    return np.sqrt(OML_M * a ** -3 + OML_R * a ** -4 + OML_L)


def dlnE_lcdm_dN(a, h=1e-5):
    return (np.log(E_lcdm(np.exp(np.log(a) + h)))
            - np.log(E_lcdm(np.exp(np.log(a) - h)))) / (2 * h)


def Om_lcdm(a):
    return OML_M * a ** -3 / E_lcdm(a) ** 2


def growth_lcdm(n_grid):
    """Solve D'' + (2 + dlnE/dN) D' - 1.5 Ω_m D = 0 in e-folds; GR source."""
    def rhs(n, y):
        D, Dp = y
        a = np.exp(n)
        return [Dp, -(2.0 + dlnE_lcdm_dN(a)) * Dp + 1.5 * Om_lcdm(a) * D]
    sol = solve_ivp(rhs, (n_grid[0], n_grid[-1]), [A_I, A_I], t_eval=n_grid,
                    method="LSODA", rtol=1e-9, atol=1e-12)
    a = np.exp(sol.t)
    D, Dp = sol.y[0], sol.y[1]
    return a, D, Dp


# --------------------------------------------------------------------------- #
# QFUDS clustering-DE background + growth (η Jeans suppression)
# --------------------------------------------------------------------------- #
def eta(a, c2, k):
    """Jeans clustering efficiency at wavenumber k: η→1 (clusters) for small k,
    η→0 (smooth) for large k. R = c_s·c·k/(aH)."""
    R = np.sqrt(c2) * C_KM_S * k / (a * H0 * cp5.E(a))
    return 1.0 / (1.0 + R ** 2)


def Om_qfuds(a):
    """Ordinary clustering-matter fraction in the QFUDS background (what an
    observer reads from the expansion history; η Ω_X is NOT included here)."""
    return OM0 * a ** -3 / cp5.E(a) ** 2


def growth_qfuds(n_grid, c2, k):
    """Same growth ODE but the SOURCE uses Ω_clust = Ω_m + η(a,k) Ω_X."""
    def rhs(n, y):
        D, Dp = y
        a = np.exp(n)
        E = cp5.E(a)
        Om = OM0 * a ** -3 / E ** 2
        Ox = cp5.rho_x(a) / E ** 2
        Om_clust = Om + eta(a, c2, k) * Ox
        return [Dp, -(2.0 + cp5.dlnE_dN(a)) * Dp + 1.5 * Om_clust * D]
    sol = solve_ivp(rhs, (n_grid[0], n_grid[-1]), [A_I, A_I], t_eval=n_grid,
                    method="LSODA", rtol=1e-9, atol=1e-12)
    a = np.exp(sol.t)
    D, Dp = sol.y[0], sol.y[1]
    return a, D, Dp


# --------------------------------------------------------------------------- #
def gamma_eff(f, Om):
    """γ_eff = ln f / ln Ω_m  (f = Ω_m^γ inverted)."""
    return np.log(f) / np.log(Om)


def gamma_eff_scale_curves(n_grid, c2, k_values, a_reference):
    """Return γ_eff(a_reference) curves for each k in ``k_values``.

    The plot x-axis is redshift, but γ_eff is computed on a scale-factor grid.
    Keep this interpolation explicitly in ``a`` so the scale-dependence band is
    not accidentally sampled with redshift values.
    """
    a_reference = np.asarray(a_reference, dtype=float)
    curves = []
    for k in k_values:
        ak, Dk, Dpk = growth_qfuds(n_grid, c2, k)
        gk = gamma_eff(Dpk / Dk, Om_qfuds(ak))
        curves.append(np.interp(a_reference, ak, gk))
    return np.asarray(curves)


def main():
    n_grid = np.linspace(np.log(A_I), 0.0, 1600)

    a_l, D_l, Dp_l = growth_lcdm(n_grid)
    a_q, D_q, Dp_q = growth_qfuds(n_grid, C2, K_S8)

    f_l = Dp_l / D_l
    f_q = Dp_q / D_q
    Oml = Om_lcdm(a_l)
    Omq = Om_qfuds(a_q)
    z = 1.0 / a_l - 1.0       # a_l == a_q (same n_grid)

    g_l = gamma_eff(f_l, Oml)
    g_q = gamma_eff(f_q, Omq)

    # ----- pull z=0 values -----
    def at_z0(arr):
        return float(np.interp(1.0, a_l, arr))   # a ascending
    f_l0, f_q0 = at_z0(f_l), at_z0(f_q)
    g_l0, g_q0 = at_z0(g_l), at_z0(g_q)
    Omq0 = at_z0(Omq)

    print("=" * 64)
    print("CP16 growth-index fingerprint (exploratory)")
    print("=" * 64)
    print(f"  f_LCDM(z=0)      = {f_l0:.4f}   Ω_m,LCDM(0)={OML_M:.3f}")
    print(f"  f_QFUDS(z=0)     = {f_q0:.4f}   Ω_m,QFUDS(0)={Omq0:.3f} (k={K_S8})")
    print(f"  γ_LCDM(z=0)      = {g_l0:.4f}   (literature 0.55)")
    print(f"  γ_eff,QFUDS(z=0) = {g_q0:.4f}   (k={K_S8} Mpc⁻¹, S8 scale)")

    # ----- MG band placement -----
    band_lo, band_hi = min(GAMMA_FR, GAMMA_DGP), max(GAMMA_FR, GAMMA_DGP)
    inside_band = band_lo <= g_q0 <= band_hi
    verdict = ("INSIDE the MG band → DEGENERATE with modified gravity"
               if inside_band else
               "OUTSIDE the MG band → DISTINGUISHABLE from f(R)/DGP")
    near = min((("ΛCDM", GAMMA_LCDM), ("f(R)", GAMMA_FR), ("DGP", GAMMA_DGP)),
               key=lambda t: abs(t[1] - g_q0))
    print(f"  MG band [{band_lo:.2f},{band_hi:.2f}]: γ_eff,QFUDS(0)={g_q0:.3f} "
          f"→ {verdict}")
    print(f"  closest literature anchor: {near[0]} (γ={near[1]})")

    # ----- scale dependence of γ_eff(z=0) across k -----
    print("\n  scale-dependence of γ_eff(z=0):")
    g_q0_by_k = {}
    for k in K_SCAN:
        ak, Dk, Dpk = growth_qfuds(n_grid, C2, k)
        fk = Dpk / Dk
        gk = gamma_eff(fk, Om_qfuds(ak))
        gk0 = float(np.interp(1.0, ak, gk))
        g_q0_by_k[k] = gk0
        print(f"     k={k:>5} Mpc⁻¹  η(z=0)={float(eta(1.0, C2, k)):.3f}  "
              f"γ_eff(0)={gk0:.4f}")
    g_spread = max(g_q0_by_k.values()) - min(g_q0_by_k.values())
    print(f"  γ_eff(z=0) spread over k∈[{K_SCAN[0]},{K_SCAN[-1]}]: "
          f"Δγ={g_spread:.3f}  "
          f"({'SCALE-DEPENDENT (extra MG-distinguishing feature)' if g_spread > 0.01 else 'nearly scale-independent'})")

    # ----- sanity asserts -----
    # (1) ΛCDM γ(z=0) ≈ 0.55
    assert abs(g_l0 - 0.55) <= 0.02, f"ΛCDM γ(z=0)={g_l0:.4f} not ≈0.55±0.02"
    # (2) deep matter domination: f→1 and Ω_m→1 (use z≈99, a=0.01, post-radiation)
    a_md = 0.01
    f_l_md = float(np.interp(a_md, a_l, f_l))
    f_q_md = float(np.interp(a_md, a_q, f_q))
    Om_l_md = Om_lcdm(a_md)
    Om_q_md = Om_qfuds(a_md)
    assert 0.97 <= f_l_md <= 1.01, f"f_LCDM(z=99)={f_l_md:.4f} not ≈1"
    assert 0.97 <= f_q_md <= 1.01, f"f_QFUDS(z=99)={f_q_md:.4f} not ≈1"
    assert Om_l_md > 0.95, f"Ω_m,LCDM(z=99)={Om_l_md:.4f} not →1"
    # QFUDS Ω_m plateaus ~0.91 (NOT 1): the density-driven dark fluid is only
    # asymptotically matter-like (w→0 with residual amplitude) and radiation
    # erodes it deeper in z — a real feature, so the floor is looser here.
    assert Om_q_md > 0.88, f"Ω_m,QFUDS(z=99)={Om_q_md:.4f} not clearly matter-dominated"
    print(f"\n  SANITY OK: γ_LCDM(0)={g_l0:.3f}≈0.55 | "
          f"matter-dom (z=99) f_LCDM={f_l_md:.3f} f_QFUDS={f_q_md:.3f}→1 | "
          f"Ω_m,LCDM={Om_l_md:.3f}→1, Ω_m,QFUDS={Om_q_md:.3f} (plateau ~0.91, "
          f"residual dark fluid mildly matter-like)")

    # ----------------------------------------------------------------- figure
    fig, ax = plt.subplots(1, 2, figsize=(14, 5.6))

    # (a) f(a) vs z
    zm = (z >= 0) & (z <= 5)
    ax[0].plot(z[zm], f_l[zm], color="tab:blue", lw=2, label="ΛCDM (GR)")
    ax[0].plot(z[zm], f_q[zm], color="tab:purple", lw=2,
               label=f"QFUDS clustering-DE (c_s²={C2:.1e}, k={K_S8})")
    ax[0].axvline(2.0, color="gray", ls=":", lw=1, label="transition z≈2")
    ax[0].set_xlabel("redshift z")
    ax[0].set_ylabel("growth rate  f(a) = dlnD/dlna")
    ax[0].set_title("(a) growth rate f(z)")
    ax[0].legend(fontsize=8)
    ax[0].grid(alpha=0.3)

    # (b) γ_eff(z) with MG band
    gm = (z >= 0) & (z <= 3) & (Omq < 0.985) & (Oml < 0.985)
    ax[1].axhspan(band_lo, band_hi, color="tab:orange", alpha=0.12,
                  label="modified-gravity band")
    ax[1].axhline(GAMMA_LCDM, color="tab:blue", ls="--", lw=1.3,
                  label="ΛCDM/GR γ=0.55")
    ax[1].axhline(GAMMA_FR, color="tab:green", ls="-.", lw=1.2,
                  label="f(R) γ=0.42")
    ax[1].axhline(GAMMA_DGP, color="tab:red", ls="-.", lw=1.2,
                  label="DGP γ=0.68")
    ax[1].plot(z[gm], g_l[gm], color="tab:blue", lw=1.2, alpha=0.7,
               label="γ_eff ΛCDM (sanity)")
    ax[1].plot(z[gm], g_q[gm], color="tab:purple", lw=2.2,
               label=f"γ_eff QFUDS (k={K_S8})")
    # scale-dependence band: shade min..max over K_SCAN at each z
    gk_curves = gamma_eff_scale_curves(n_grid, C2, K_SCAN, a_l)
    ax[1].fill_between(z[gm], gk_curves[:, gm].min(axis=0),
                       gk_curves[:, gm].max(axis=0),
                       color="tab:purple", alpha=0.15,
                       label=f"QFUDS k∈[{K_SCAN[0]},{K_SCAN[-1]}] spread")
    ax[1].scatter([0], [g_q0], color="tab:purple", zorder=5, s=40)
    ax[1].set_xlabel("redshift z")
    ax[1].set_ylabel("effective growth index  γ_eff = ln f / ln Ω_m")
    ax[1].set_title("(b) γ_eff(z) vs ΛCDM / MG band")
    ax[1].set_ylim(0.30, 0.85)
    ax[1].legend(fontsize=7.5, loc="upper right")
    ax[1].grid(alpha=0.3)

    fig.suptitle("CP16: growth-index γ fingerprint — QFUDS vs ΛCDM / modified gravity (exploratory)",
                 fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp16_growth_index.png", dpi=130)
    fig.savefig("fig_cp16_growth_index.svg")
    print("\nsaved fig_cp16_growth_index.png + .svg")

    # ----------------------------------------------------------------- CSV
    z_out = np.concatenate([np.linspace(0.0, 2.0, 21),
                            np.linspace(2.2, 5.0, 15)])
    with open("cp16_growth_index_results.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["# CP16 growth-index fingerprint (exploratory; proxy; "
                    "050 ceiling untouched; real check = CLASS, blocked)"])
        w.writerow([f"# c_eff2={C2}, k_S8={K_S8} Mpc^-1; "
                    f"Omega_m_a = QFUDS ordinary-matter fraction Om0 a^-3/E^2"])
        w.writerow([f"# gamma_eff_QFUDS(z=0)={g_q0:.4f}, gamma_LCDM(z=0)={g_l0:.4f}, "
                    f"MG band [{band_lo},{band_hi}] -> {'INSIDE/degenerate' if inside_band else 'OUTSIDE/distinguishable'}"])
        w.writerow(["z", "Omega_m_a", "f_LCDM", "f_QFUDS",
                    "gamma_eff_QFUDS", "gamma_LCDM"])
        for zz in z_out:
            aa = 1.0 / (1.0 + zz)
            row = [f"{zz:.4f}",
                   f"{float(np.interp(aa, a_q, Omq)):.5f}",
                   f"{float(np.interp(aa, a_l, f_l)):.5f}",
                   f"{float(np.interp(aa, a_q, f_q)):.5f}",
                   f"{float(np.interp(aa, a_q, g_q)):.5f}",
                   f"{float(np.interp(aa, a_l, g_l)):.5f}"]
            w.writerow(row)
        w.writerow([])
        w.writerow(["# gamma_eff_QFUDS(z=0) scale dependence"])
        w.writerow(["k_Mpc^-1", "eta_z0", "gamma_eff_z0"])
        for k in K_SCAN:
            w.writerow([k, f"{float(eta(1.0, C2, k)):.4f}",
                        f"{g_q0_by_k[k]:.5f}"])
    print("saved cp16_growth_index_results.csv")


if __name__ == "__main__":
    main()
