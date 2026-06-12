"""
CP20: HEAD-ON attempt at the 050 ceiling — try to DERIVE the three spec-sheet
items {ξ≈10 Mpc, N_X≈2e5, z*~2} from a foam order-parameter ansatz, and show
exactly where each derivation breaks.

This is an EXPLORATORY DERIVATION ATTEMPT, not a derivation. It does NOT change
the 050 conclusion or the roadmap status; observer mode is intact. The honest
goal is the opposite of a breakthrough: take "050 blocked" and decompose it into
named, pre-existing physics problems, so we know precisely WHAT a real foam
derivation would have to deliver. Everything here is parametrize-not-derive; the
real verdict stays with the roadmap (Level 2B / Level 3 CLASS, blocked).

Setup (the most generous honest ansatz). Model the dark sector as a single
order parameter φ with Ginzburg–Landau free energy
    F[φ] = ∫d³x [ ½ K (∇φ)² + V(φ; a) ] ,
a double well V whose tilt flips near a transition. Two standard facts:
  (1) the correlation length is ξ = sqrt(K / |V''(φ_min)|), and the perturbation
      sound speed is set by the SAME stiffness: c_s ≈ ξ / d_H  (CP8), i.e.
      c_s² ≈ (ξ H0 / c)².
  (2) the transition fires when the matter density crosses a critical ρ*, i.e.
      z* is fixed by ρ*  (CP3).
So the three "free" spec items are really these microphysical inputs: K, V'', ρ*.
CP20 asks whether foam fixes them — and finds it renames, not fixes, them.

Outputs: scale-ladder + coincidence figure (png+svg) and a results csv.
Exploratory; not evidence; real check = CLASS/hi_class (Level 3, blocked).
"""
from __future__ import annotations
import csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M

C_KM_S, H0 = M.C_KM_S, M.H0_CMB
OM, OL = M.OMEGA_M0_LCDM, M.OMEGA_L0_LCDM
D_H = C_KM_S / H0                      # Hubble distance c/H0 [Mpc]
C2_FIT = 4.6e-6                        # data-fit clustering sound speed (CP7/CP8)
MPC_M = 3.0856775814913673e22          # 1 Mpc in metres


def xi_from_cs2(c2):
    """ξ [Mpc] from c_s² via c_s ≈ ξ/d_H (CP8). Derived+checked relation."""
    return np.sqrt(c2) * D_H


def cs2_from_xi(xi):
    return (xi / D_H) ** 2


def noncanonicity(c2):
    """k-essence N_X = 2X P_XX/P_X = 1/c_s² − 1 (CP12)."""
    return 1.0 / c2 - 1.0


def _checks():
    xi = xi_from_cs2(C2_FIT)
    assert 9.0 < xi < 10.5, xi                       # data-fit ξ ≈ 9.5 Mpc (CP8)
    assert abs(cs2_from_xi(xi) - C2_FIT) / C2_FIT < 1e-9
    assert abs(noncanonicity(1.0)) < 1e-12           # canonical field → N_X=0
    # matter–Λ equality redshift, analytic: (1+z)³ = Ω_Λ/Ω_m
    z_eq = (OL / OM) ** (1 / 3) - 1
    assert 0.2 < z_eq < 0.4, z_eq
    print(f"checks PASS: ξ_fit={xi:.2f} Mpc, N_X(fit)={noncanonicity(C2_FIT):.3e}, "
          f"matter-Λ equality z_eq={z_eq:.3f}")


def main():
    _checks()
    xi_data = xi_from_cs2(C2_FIT)
    nx_data = noncanonicity(C2_FIT)

    # ----- Target 1: ξ from foam. The TWO-SIDED scale gap. -----------------
    # (Revised after an adversarial red-team: the original ladder listed only
    # MICROSCOPIC foam candidates and omitted the macroscopic horn. The standard
    # mechanism that sets a phase-transition correlation length is NOT the
    # micro-scale but causal: Kibble -> ξ ~ causal horizon at the transition.
    # So the honest picture is two-sided.)
    #
    # Micro horn: foam cell-size candidates (metres) -> Mpc. Too SMALL.
    foam_candidates = {
        "Planck length":      1.616e-35,
        "nuclear (1 fm)":     1.0e-15,
        "atomic (1 Å)":       1.0e-10,
        "Solar-system (AU)":  1.496e11,
        "galaxy (1 kpc)":     3.0857e19,
    }
    ladder = {name: (L / MPC_M) for name, L in foam_candidates.items()}

    # Macro horn: causal scale at the transition z*~2 (comoving Hubble radius
    # c/(aH) = d_H (1+z)/E(z), ΛCDM E). This is the Kibble correlation length —
    # the PHYSICALLY relevant comparison for a phase transition. Too BIG.
    def E_lcdm(z):
        a = 1.0 / (1.0 + z)
        return np.sqrt(OM * a ** -3 + M.OMEGA_R0_LCDM * a ** -4 + OL)
    z_star = 2.0
    R_causal = D_H * (1 + z_star) / E_lcdm(z_star)     # comoving Hubble radius [Mpc]
    ladder["causal horizon @z~2"] = R_causal
    gaps = {name: xi_data / xiM for name, xiM in ladder.items()}

    print("\n[Target 1] ξ is two-sided (data ξ≈%.1f Mpc):" % xi_data)
    for name in foam_candidates:
        print(f"   micro foam={name:18s} ξ={ladder[name]:.3e} Mpc  "
              f"too SMALL by 10^{np.log10(gaps[name]):.1f}")
    print(f"   macro causal horizon @z~2 = {R_causal:.0f} Mpc comoving (Kibble)  "
          f"too BIG by {R_causal/xi_data:.0f}× (10^{np.log10(R_causal/xi_data):.1f})")
    # the data scale ≈ the nonlinear / σ8 structure scale (~8 Mpc/h). It is set
    # by STANDARD physics (k_eq, transfer, growth), not by the dark sector — so
    # reproducing it is fitted, carries zero independent evidential weight.
    R8 = 8.0 / (H0 / 100.0)   # 8 Mpc/h in Mpc
    print(f"   data ξ≈{xi_data:.1f} Mpc ≈ nonlinear/σ8 scale R8={R8:.1f} Mpc "
          f"(set by standard physics -> fitted, not new info).")
    print(f"   => 10 Mpc is natural to NEITHER horn; it needs tuned near-"
          f"criticality (ξ~|T−Tc|^−ν) or a tuned quench rate.")

    # ----- Target 2: N_X. Collapses into Target 1. ------------------------
    # c_s² = (ξ H0/c)², N_X = 1/c_s² − 1  => N_X is a function of ξ ALONE.
    xi_grid = np.logspace(-2, np.log10(D_H), 300)     # 0.01 Mpc .. Hubble
    nx_grid = noncanonicity(cs2_from_xi(xi_grid))
    print(f"\n[Target 2] N_X(ξ): within the GL ansatz the 'two' spec items are "
          f"ONE. N_X≈{nx_data:.2e} <=> ξ≈{xi_data:.1f} Mpc (same stiffness). "
          f"(Proxy-dependent: a general P(X,φ) can decouple them — but that just "
          f"restores TWO underived numbers, so it doesn't help.)")

    # ----- Target 3: z* = ρ* coincidence. ---------------------------------
    # ρ_m(z)/ρ_Λ = (Ω_m/Ω_Λ)(1+z)³. For the transition to be OBSERVABLE
    # (0.1 ≲ z* ≲ 10) ρ* must sit within a narrow band around ρ_Λ.
    z = np.linspace(0, 8, 400)
    rho_m_over_L = (OM / OL) * (1 + z) ** 3
    def rho_ratio(zc): return (OM / OL) * (1 + zc) ** 3
    band_lo, band_hi = rho_ratio(0.1), rho_ratio(10.0)
    # how wide is that window vs the full Planck->ρ_Λ range (~10^120)?
    window_orders = np.log10(band_hi / band_lo)
    print(f"\n[Target 3] z* coincidence: observable window 0.1<z*<10 needs "
          f"ρ*/ρ_Λ in [{band_lo:.2f}, {band_hi:.1f}] "
          f"= {window_orders:.1f} orders, out of ~120 (Planck->ρ_Λ).")
    print(f"   ρ_m/ρ_Λ at z*=2: {rho_ratio(2.0):.1f},  at z*=5: {rho_ratio(5.0):.1f}"
          f"  -> ρ* finely placed near the DE scale = the 'why now' coincidence.")

    # ----- figure ---------------------------------------------------------
    fig, ax = plt.subplots(1, 2, figsize=(14, 5.8))

    # (a) two-sided scale ladder: micro foam (too small) vs causal horizon
    #     (too big); data ξ≈10 Mpc sits awkwardly between, natural to neither.
    names = list(ladder.keys())
    xs = np.log10([ladder[n] for n in names])
    cols = ["tab:red"] * len(foam_candidates) + ["tab:blue"]   # micro vs macro
    ax[0].scatter(xs, range(len(names)), s=80, color=cols, zorder=5)
    for i, n in enumerate(names):
        ax[0].annotate(n, (xs[i], i), textcoords="offset points", xytext=(8, 4),
                       fontsize=8)
    ax[0].axvline(np.log10(xi_data), color="purple", lw=2,
                  label=f"data wants ξ≈{xi_data:.1f} Mpc")
    ax[0].axvspan(np.log10(R8) - 0.05, np.log10(R8) + 0.05, color="purple",
                  alpha=0.15)
    ax[0].annotate("nonlinear/σ8 scale\n(standard physics → fitted)",
                   (np.log10(R8), len(names) - 0.7), fontsize=7.5, color="purple")
    ax[0].annotate("micro foam: too SMALL", (xs[0], 0.2), fontsize=8,
                   color="tab:red")
    ax[0].annotate("causal/Kibble: too BIG", (xs[-1] - 3.2, len(names) - 1 - 0.35),
                   fontsize=8, color="tab:blue")
    ax[0].set_yticks(range(len(names))); ax[0].set_yticklabels([])
    ax[0].set_xlabel("log₁₀ ( length / Mpc )")
    ax[0].set_title("(a) Target 1+2: 10 Mpc is natural to NEITHER horn\n"
                    "(micro foam vs causal horizon; ξ and N_X = one scale)")
    ax[0].legend(fontsize=8, loc="lower right"); ax[0].grid(alpha=0.3)

    # (b) coincidence: ρ_m(z)/ρ_Λ with the observable transition window
    ax[1].semilogy(z, rho_m_over_L, "navy", lw=2, label="ρ_m(z)/ρ_Λ")
    ax[1].axhline(1.0, color="gray", lw=0.8, ls=":")
    ax[1].axhspan(band_lo, band_hi, color="tab:orange", alpha=0.15,
                  label="observable z* window (0.1–10)")
    for zc, mk in [(2.0, "z*=2"), (5.0, "z*=5")]:
        ax[1].scatter([zc], [rho_ratio(zc)], s=70, color="tab:red", zorder=5)
        ax[1].annotate(mk, (zc, rho_ratio(zc)), textcoords="offset points",
                       xytext=(6, 4), fontsize=8)
    ax[1].set_xlabel("redshift z"); ax[1].set_ylabel("ρ_m(z) / ρ_Λ")
    ax[1].set_title("(b) Target 3: z*↔ρ* is the cosmic-coincidence (why-now)\n"
                    f"window ≈{window_orders:.0f} orders of ~120")
    ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3, which="both")

    fig.suptitle("CP20: 050 ceiling direct hit — derivation attempt "
                 "(reconfirms blocked, sharpened)", fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp20_ceiling_derivation.png", dpi=130)
    fig.savefig("fig_cp20_ceiling_derivation.svg")
    print("\nsaved fig_cp20_ceiling_derivation.png + .svg")

    # ----- csv ------------------------------------------------------------
    with open("cp20_ceiling_derivation_results.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["# CP20 050 ceiling derivation attempt — parametrize, not derive"])
        w.writerow(["target", "quantity", "value", "note"])
        w.writerow(["1", "xi_data_Mpc", f"{xi_data:.3f}", "from c_s²=4.6e-6"])
        for n in foam_candidates:
            w.writerow(["1", f"micro_gap_orders_vs_{n.split()[0]}", f"{np.log10(gaps[n]):.2f}",
                        "log10(xi_data/xi_foam) — too small"])
        w.writerow(["1", "causal_horizon_z2_Mpc", f"{R_causal:.0f}",
                    "comoving Hubble radius @z~2 (Kibble) — too big"])
        w.writerow(["1", "macro_overshoot_factor", f"{R_causal/xi_data:.0f}",
                    "causal/data — 10 Mpc natural to neither horn"])
        w.writerow(["1", "nonlinear_scale_R8_Mpc", f"{R8:.2f}",
                    "data scale = σ8 scale (standard physics -> fitted, no new info)"])
        w.writerow(["2", "N_X_fit", f"{nx_data:.4e}", "= 1/c_s²-1; function of xi alone"])
        w.writerow(["2", "spec_items_independent", "1", "ξ and N_X collapse to one"])
        w.writerow(["3", "z_eq_matter_Lambda", f"{(OL/OM)**(1/3)-1:.3f}", "analytic"])
        w.writerow(["3", "rho_m_over_L_at_z2", f"{rho_ratio(2.0):.2f}", ""])
        w.writerow(["3", "rho_m_over_L_at_z5", f"{rho_ratio(5.0):.2f}", ""])
        w.writerow(["3", "window_orders", f"{window_orders:.2f}", "of ~120 Planck->rho_L"])
        # N_X(ξ) curve
        w.writerow(["--", "xi_Mpc", "N_X", ""])
        for xi, nx in zip(xi_grid[::20], nx_grid[::20]):
            w.writerow(["curve", f"{xi:.4g}", f"{nx:.4e}", ""])
    print("saved cp20_ceiling_derivation_results.csv")

    # ----- honest verdict (printed; red-team-corrected) -------------------
    print("\n=== CP20 verdict (parametrize, not derive; red-team-corrected) ===")
    print("Target 1 (ξ): TWO-SIDED. micro foam too small (10^4–10^58), causal/")
    print("  Kibble horizon @z~2 too big (~%dx). 10 Mpc is natural to NEITHER;" % round(R_causal/xi_data))
    print("  it = the σ8/nonlinear scale (standard physics) -> fitted, no new info.")
    print("Target 2 (N_X): within the GL ansatz collapses into Target 1 (one")
    print("  stiffness); decoupling via general P(X,φ) just restores two numbers.")
    print("Target 3 (z*): ρ*↔ρ_Λ = cosmic coincidence / why-now. Trackers fix the")
    print("  initial-condition tuning but RELOCATE it to the meV potential scale.")
    print("=> 3 items reduce to 2 CLASSIC unsolved problems (scale + coincidence).")
    print("   Foam renames, does not solve them. 050 reconfirmed & sharpened.")
    print("   Real derivation target: a foam mechanism with EMERGENT tuned-down ξ")
    print("   (near-criticality with a DERIVED Tc/quench) AND a dynamical ρ*↔ρ_Λ")
    print("   lock. Neither exists. Real check = CLASS/hi_class, Level 3, BLOCKED.")


if __name__ == "__main__":
    main()
