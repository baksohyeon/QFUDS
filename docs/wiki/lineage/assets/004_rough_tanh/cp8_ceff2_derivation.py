"""
CP8: rough DERIVATION attempt for c_eff² (instead of dialing it).

CP5-CP7 dialed c_eff² to fit S8 (best ≈ 4.6e-6). Here we ask: does any
first-principles handle PRODUCE that value, or does the foam premise give
something else?

Physical handle — correlation length ξ of the order parameter.
Add a gradient term to the free energy: F = ∫ [ (κ/2)(∇φ)² + V(φ) ].
The field smooths fluctuations below its correlation length ξ = sqrt(κ/V''),
and the perturbation sound speed is set by the same stiffness:

    c_eff  ≈  ξ / d_H        (sound horizon ~ correlation length; d_H = c/H0)
    c_eff² ≈  (ξ H0 / c)²

So c_eff² is NOT a free number — it is fixed once you say how big the foam's
correlation length is. Three natural regimes:

    microscopic "quantum foam"  ξ ≪ 1 Mpc      -> c_eff² → 0   (clusters like CDM)
    structure scale             ξ ~ 10 Mpc                     (cosmic-web scale)
    Hubble scale                ξ ~ c/H0 ~ 4400 Mpc -> c_eff² ~ 1 (smooth)

We compute the S8 each regime gives (reusing the CP5 growth machinery) and check
whether the data-preferred c_eff² corresponds to a foam-natural ξ.

STATUS: exploratory, order-of-magnitude. ξ↔c_eff² is a rough sound-horizon
mapping, not a real derivation from foam microphysics (that is the 050 ceiling).
Not evidence, not a roadmap change.
"""
from __future__ import annotations
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M
import cp5_sound_speed as cp5   # reuse S8_of_ceff2 (module-level setup runs once)

D_H = M.C_KM_S / M.H0_CMB          # Hubble distance c/H0 in Mpc ≈ 4448 Mpc
C2_FIT = 4.6e-6                    # CP7 best-fit c_eff²


def xi_of_ceff2(c2):
    """comoving correlation/Jeans length implied by c_eff²:  ξ ≈ c_s · d_H [Mpc]."""
    return np.sqrt(c2) * D_H


def ceff2_of_xi(xi_mpc):
    return (xi_mpc / D_H) ** 2


def main():
    # data-preferred value -> implied correlation length
    xi_fit = xi_of_ceff2(C2_FIT)
    print(f"d_H = c/H0 = {D_H:.0f} Mpc")
    print(f"data-preferred c_eff² = {C2_FIT:.1e}  ->  implied ξ = {xi_fit:.1f} Mpc "
          f"(cosmic-web / S8 scale)")

    # three foam regimes -> c_eff² -> S8
    regimes = [
        ("microscopic foam ξ=1 kpc", 1e-3),
        ("ξ=0.1 Mpc",                1e-1),
        ("ξ=1 Mpc",                  1.0),
        ("structure ξ=10 Mpc",       10.0),
        ("data-fit ξ≈9.9 Mpc",       xi_fit),
        ("ξ=100 Mpc",                100.0),
        ("Hubble ξ=c/H0",            D_H),
    ]
    print("\nregime                     ξ[Mpc]     c_eff²        S8")
    rows = []
    for name, xi in regimes:
        c2 = min(ceff2_of_xi(xi), 1.0)
        D1 = cp5.S8_of_ceff2(max(c2, 1e-12))
        sigma8 = cp5.SIGMA8_LCDM * D1 / _D1_lcdm
        S8 = sigma8 * np.sqrt(cp5.OM0 / 0.3)
        rows.append((name, xi, c2, S8))
        print(f"{name:26s} {xi:9.3g}  {c2:11.3e}  {S8:.3f}")

    print("\nVERDICT:")
    print("  microscopic 'quantum foam' (ξ << Mpc) -> c_eff²→0 -> S8 too HIGH (~0.95).")
    print("  Hubble-scale ξ -> c_eff²~1 -> S8 too LOW (~0.68, overshoot).")
    print(f"  data needs ξ ≈ {xi_fit:.0f} Mpc = cosmic-web scale, which is NOT foam-like.")
    print("  => a natural foam correlation length does NOT reproduce the fit. 050 stands.")

    # smooth S8(ξ) curve
    xi_grid = np.logspace(-3, np.log10(D_H), 40)        # 1 kpc .. Hubble
    S8_grid = []
    for xi in xi_grid:
        c2 = min(ceff2_of_xi(xi), 1.0)
        D1 = cp5.S8_of_ceff2(max(c2, 1e-12))
        S8_grid.append(cp5.SIGMA8_LCDM * D1 / _D1_lcdm * np.sqrt(cp5.OM0/0.3))
    S8_grid = np.array(S8_grid)

    fig, ax = plt.subplots(figsize=(9, 5.5))
    ax.semilogx(xi_grid, S8_grid, "-", color="tab:purple", lw=2, label="S8(ξ)")
    ax.axhline(0.76, color="tab:red", ls="--", label="observed S8≈0.76")
    ax.axhline(0.83, color="k", ls=":", label="Planck ΛCDM≈0.83")
    ax.axvline(xi_fit, color="tab:green", ls="-.", label=f"data-fit ξ≈{xi_fit:.0f} Mpc")
    ax.axvspan(1e-3, 1.0, color="tab:blue", alpha=0.12)
    ax.text(3e-3, 0.70, "microscopic\n'foam' regime\n(ξ≪Mpc)\nS8 too high",
            fontsize=8, color="tab:blue")
    ax.axvspan(1e3, D_H, color="tab:orange", alpha=0.12)
    ax.text(1.3e3, 0.92, "Hubble-scale\nS8 overshoots low", fontsize=8, color="tab:orange")
    ax.set_xlabel("foam order-parameter correlation length ξ  [Mpc]")
    ax.set_ylabel("S8 produced")
    ax.set_title("CP8: which correlation length reproduces S8? (rough derivation, exploratory)")
    ax.legend(fontsize=8); ax.grid(alpha=0.3)
    fig.tight_layout()
    fig.savefig("fig_cp8_ceff2_derivation.png", dpi=130)
    fig.savefig("fig_cp8_ceff2_derivation.svg")
    print("\nsaved fig_cp8_ceff2_derivation.png + .svg")

    import csv
    with open("cp8_ceff2_derivation_results.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["# d_H_Mpc", f"{D_H:.3f}", "c_eff2_fit", C2_FIT, "xi_fit_Mpc", f"{xi_fit:.3f}"])
        w.writerow(["xi_Mpc", "c_eff2", "S8"])
        for xi, c2v, s8v in zip(xi_grid, [min(ceff2_of_xi(x),1.0) for x in xi_grid], S8_grid):
            w.writerow([f"{xi:.5g}", f"{c2v:.5e}", f"{s8v:.4f}"])
    print("saved cp8_ceff2_derivation_results.csv")


# ΛCDM growth normalization (compute once)
from scipy.integrate import solve_ivp
def _lcdm_D1():
    def rhs(n, y):
        D, Dp = y; a = np.exp(n)
        El = np.sqrt(M.OMEGA_M0_LCDM*a**-3 + M.OMEGA_R0_LCDM*a**-4 + M.OMEGA_L0_LCDM)
        dl = (np.log(np.sqrt(M.OMEGA_M0_LCDM*np.exp(n+1e-5)**-3+M.OMEGA_R0_LCDM*np.exp(n+1e-5)**-4+M.OMEGA_L0_LCDM))
              - np.log(np.sqrt(M.OMEGA_M0_LCDM*np.exp(n-1e-5)**-3+M.OMEGA_R0_LCDM*np.exp(n-1e-5)**-4+M.OMEGA_L0_LCDM)))/2e-5
        return [Dp, -(2+dl)*Dp + 1.5*(M.OMEGA_M0_LCDM*a**-3/El**2)*D]
    s = solve_ivp(rhs, (np.log(1e-3), 0.0), [1e-3, 1e-3], t_eval=[0.0],
                  method="LSODA", rtol=1e-8, atol=1e-11)
    return s.y[0][-1]

_D1_lcdm = _lcdm_D1()

if __name__ == "__main__":
    main()
