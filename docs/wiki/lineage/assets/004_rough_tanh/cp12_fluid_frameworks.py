"""
CP12: place the rough QFUDS toy inside the established fluid / EFT frameworks.

This checkpoint does NOT add new physics. It only LOCATES the CP1–CP11 toy on
the maps that the literature already drew, so we can name exactly which corner of
fluid-dark-sector theory the toy lives in — and confirm that doing so is pure
PARAMETRIZATION, never DERIVATION. The 050 ceiling (foam→δQ) is untouched.

Frameworks used as coordinate systems (not as endorsements):

  GDM  — Generalized Dark Matter (Hu 1998, astro-ph/9801234).
         A dark fluid is fixed by three functions: w(a), effective sound speed
         c_eff² (rest-frame c_s²), and viscosity c_vis² (anisotropic stress).
         CDM = (w=0, c_s²=0, c_vis²=0).  Λ = (w=-1, c_s²=1, c_vis²=0).
         Our CP11 system used PERFECT-fluid Euler eqs (no shear σ) → c_vis²=0.
         => QFUDS toy = GDM with c_vis²=0, w(a) sliding 0→-1, c_s²≈4.6e-6 const.
         It is a *special case* of GDM, picked by hand — not derived.

  EFT of Dark Energy (hi_class / EFTCAMB; Gleyzes+ 2013, Bellini-Sawicki 2014).
         Linear DE perturbations parametrized by {α_K kineticity, α_B braiding,
         α_M Planck-mass run, α_T tensor speed}. A minimally-coupled k-essence
         (no modified gravity) has α_M=α_T=α_B=0 and only α_K≠0, which sets c_s².
         => QFUDS toy maps to the SIMPLEST non-trivial corner: pure-α_K, no braid.

  EFTofLSS (Baumann+ 2012; Carrasco+ 2012).
         Coarse-graining short modes gives the *matter* fluid an effective sound
         speed / counterterm whose scale is the nonlinear scale, a few–10 Mpc.
         This is the SAME order as the ξ≈10 Mpc that CP8 found hiding in our
         data-fit c_eff². Noted as a scale coincidence (positioning), NOT a claim
         that our c_s² is derived from LSS coarse-graining.

  k-essence (Armendariz-Picon+ 2000).
         A scalar with non-canonical kinetic Lagrangian P(X,φ), X=½(∂φ)². Its
         sound speed is c_s² = P_X / (P_X + 2X P_XX). A canonical field (P=X−V)
         has P_XX=0 → c_s²=1. Reproducing our tiny c_s² needs a strongly
         non-canonical kinetic term; CP12 quantifies how strongly.

Everything below is parametrize-not-derive. Exploratory; not evidence, not a
roadmap change. The real check is CLASS/hi_class (Level 3, blocked).
"""
from __future__ import annotations
import numpy as np
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M
import density_driven as dd

# data-fit clustering sound speed (CP7 best, CP8 ξ≈10 Mpc), constant in the toy
C2_FIT = 4.6e-6
C_VIS2 = 0.0            # CP11 used perfect-fluid Euler eqs → no anisotropic stress

# w(a) of the density-driven model (same curve CP11 used), on a fast interpolator
_w_std = -dd.relax(z_star=5.0, barrier=2.0, mobility=2.0, lam=3.0)
_lnw = interp1d(np.log(dd.A_GRID), _w_std,
                fill_value=(_w_std[0], _w_std[-1]), bounds_error=False)
def w_of(a):
    return float(_lnw(np.log(a)))


def noncanonicity(c_s2):
    """k-essence non-canonicity N_X ≡ 2X P_XX / P_X = 1/c_s² − 1.

    From c_s² = P_X/(P_X + 2X P_XX): invert to N_X. Canonical field → 0.
    """
    return 1.0 / np.asarray(c_s2, dtype=float) - 1.0


def _check_derivations():
    """Hand-check the two relations used, against known limits."""
    # canonical scalar: c_s²=1 → N_X=0
    assert abs(noncanonicity(1.0) - 0.0) < 1e-12
    # round-trip: c_s² = 1/(1+N_X)
    for c2 in (1.0, 1e-2, 4.6e-6, 1e-8):
        nx = noncanonicity(c2)
        c2_back = 1.0 / (1.0 + nx)
        assert abs(c2_back - c2) / c2 < 1e-9, (c2, c2_back)
    # GDM corners
    assert abs(w_of(M.z_to_a(10)) - 0.0) < 0.05   # early: matter-like w≈0
    assert w_of(1.0) < -0.9                        # today: vacuum-like w≈-1
    print("derivation checks: PASS (canonical limit, c_s² round-trip, GDM corners)")


def main():
    _check_derivations()

    # ---- QFUDS trajectory across redshift in GDM coordinates -----------------
    z_grid = np.linspace(0.0, 6.0, 121)
    a_grid = M.z_to_a(z_grid)
    w_traj = np.array([w_of(a) for a in a_grid])
    c2_traj = np.full_like(w_traj, C2_FIT)        # constant in the toy
    nx_fit = float(noncanonicity(C2_FIT))

    print(f"\nQFUDS toy located as: GDM(w(a):0→{w_traj[0]:+.2f}, "
          f"c_s²={C2_FIT:.1e}, c_vis²={C_VIS2:.0f})")
    print(f"k-essence non-canonicity at fit c_s²: 2X·P_XX/P_X = 1/c_s²−1 "
          f"= {nx_fit:.3e}  (canonical field = 0)")
    print(f"  → kinetic term must be ~{nx_fit:.0e}× more non-linear in X "
          f"than a canonical scalar.")

    # ---- reference points in the (w, c_s²) plane -----------------------------
    refs = {
        "CDM (w=0, c_s²→0)":          (0.0, 1e-9, "o", "tab:blue"),
        "Λ / vacuum (w=-1, c_s²=1)":  (-1.0, 1.0, "*", "k"),
        "quintessence (canonical)":   (-0.8, 1.0, "s", "tab:green"),
    }

    # k-essence non-canonicity curve over c_s²
    c2_axis = np.logspace(-8, 0, 200)
    nx_axis = noncanonicity(c2_axis)

    # ---- figure --------------------------------------------------------------
    fig, ax = plt.subplots(1, 2, figsize=(14, 5.8))

    # (a) GDM (w, c_s²) plane with QFUDS trajectory colored by z
    sc = ax[0].scatter(w_traj, c2_traj, c=z_grid, cmap="viridis",
                        s=22, zorder=5, label="QFUDS toy w(a) @ c_s²=4.6e-6")
    cb = fig.colorbar(sc, ax=ax[0]); cb.set_label("redshift z")
    ax[0].annotate("today\n(w→-1)", (w_traj[0], C2_FIT), textcoords="offset points",
                   xytext=(8, 14), fontsize=8, color="purple")
    ax[0].annotate("early\n(w→0)", (w_traj[-1], C2_FIT), textcoords="offset points",
                   xytext=(-30, 14), fontsize=8, color="purple")
    for name, (w, c2, mk, col) in refs.items():
        ax[0].scatter([w], [c2], marker=mk, s=160, color=col,
                      edgecolor="white", zorder=6, label=name)
    ax[0].axhspan(1e-9, 1e-7, color="tab:red", alpha=0.07)
    ax[0].text(-0.05, 2e-8, "micro-foam ξ≪Mpc → c_s²→0\n(CP8: S8 wrong way)",
               fontsize=7.5, color="tab:red")
    ax[0].set_yscale("log"); ax[0].set_ylim(1e-9, 3.0)
    ax[0].set_xlim(0.15, -1.15)                    # w from 0 (early) to -1 (late)
    ax[0].set_xlabel("equation of state  w"); ax[0].set_ylabel("sound speed  c_s²")
    ax[0].set_title("(a) GDM plane — QFUDS = c_vis²=0 special case")
    ax[0].legend(fontsize=7, loc="lower left"); ax[0].grid(alpha=0.3, which="both")

    # (b) k-essence non-canonicity vs c_s²
    ax[1].loglog(c2_axis, nx_axis, "navy", lw=2, label="2X·P_XX/P_X = 1/c_s² − 1")
    ax[1].scatter([C2_FIT], [nx_fit], s=140, color="purple", zorder=6,
                  label=f"QFUDS fit: c_s²={C2_FIT:.1e} → {nx_fit:.1e}")
    ax[1].scatter([1.0], [1e-3], marker="s", s=120, color="tab:green", zorder=6,
                  label="canonical scalar: c_s²=1 → 0")
    ax[1].axhline(1.0, color="gray", lw=0.7, ls=":")
    ax[1].text(1.3e-8, 1.4, "canonical (N_X=1) line", fontsize=7, color="gray")
    ax[1].set_xlabel("clustering sound speed  c_s²")
    ax[1].set_ylabel("k-essence non-canonicity  N_X = 2X·P_XX/P_X")
    ax[1].set_title("(b) how non-canonical the kinetic term must be")
    ax[1].legend(fontsize=8, loc="upper right"); ax[1].grid(alpha=0.3, which="both")

    fig.suptitle("CP12: locating the QFUDS toy in fluid/EFT frameworks "
                 "(parametrize, not derive)", fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp12_fluid_frameworks.png", dpi=130)
    fig.savefig("fig_cp12_fluid_frameworks.svg")
    print("\nsaved fig_cp12_fluid_frameworks.png + .svg")

    # ---- framework mapping table (printed; positioning summary) --------------
    print("\nframework placement (coordinate, not derivation):")
    rows = [
        ("GDM (Hu 1998)",      "w(a):0→-1, c_s²=4.6e-6, c_vis²=0",
         "special case, c_vis²=0 (perfect fluid)"),
        ("EFT of DE",          "α_K≠0; α_B=α_M=α_T=0",
         "simplest corner: minimally-coupled k-essence, no braiding"),
        ("EFTofLSS",           "c_s(eff) scale ≈ ξ ≈ 10 Mpc (CP8)",
         "scale coincidence only; not derived from coarse-graining"),
        ("k-essence",          f"N_X = 2X·P_XX/P_X = {nx_fit:.2e}",
         "~5 orders from canonical → strongly non-canonical kinetic term"),
    ]
    for fw, coord, note in rows:
        print(f"  {fw:18s} | {coord:34s} | {note}")

    # ---- csv -----------------------------------------------------------------
    import csv
    with open("cp12_fluid_frameworks_results.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["z", "a", "w", "c_s2", "c_vis2", "noncanonicity_NX"])
        for i, z in enumerate(z_grid):
            w.writerow([f"{z:.4f}", f"{a_grid[i]:.5f}", f"{w_traj[i]:+.5f}",
                        f"{C2_FIT:.3e}", f"{C_VIS2:.1f}", f"{nx_fit:.5e}"])
    print("saved cp12_fluid_frameworks_results.csv")


if __name__ == "__main__":
    main()
