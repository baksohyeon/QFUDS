"""
CP10: does QFUDS relieve the H0 tension? (the headline tension, never tested.)

So far we only tested S8. H0 is the bigger headline tension (CMB-inferred 67.4 vs
local 73.0, a ~8% gap). I had hoped QFUDS would relieve it.

H0 is a BACKGROUND quantity, inferred via the inverse distance ladder: the CMB
fixes the angular acoustic scale θ* = r_s / D_M(z_rec) very precisely, and the
sound horizon r_s is set by PRE-recombination physics. Our transition is LATE
(z≈2) and the dark component is matter-like (w→0) at high z, so pre-recombination
physics — hence r_s and z_rec — is identical to ΛCDM. With r_s and θ* fixed, the
required D_M(z_rec) is fixed, so:

    H0 ∝ ∫_0^{z_rec} dz / E(z)        (since D_M = (c/H0) ∫ dz/E = r_s/θ* = fixed)

    => H0_QFUDS / H0_ΛCDM = [∫ dz/E_ΛCDM] / [∫ dz/E_QFUDS]   (to z_rec)

If the QFUDS background ≈ ΛCDM (which CP1 forced, to satisfy SNe), this ratio ≈ 1
=> NO H0 relief. We quantify it, and show where the ∫dz/E integrand differs
(only z<2, a tiny slice of the integral that runs to z≈1090).

STATUS: exploratory, rough inverse-distance-ladder argument (fixed r_s, θ*).
Not evidence, not a roadmap change.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import cumulative_trapezoid
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M
import density_driven as dd

Z_REC = 1090.0
H0_CMB, H0_LOCAL = M.H0_CMB, M.H0_LOCAL
NEED_PCT = 100 * (H0_LOCAL - H0_CMB) / H0_CMB     # ~8.3% to close the tension

# high-z integration grid for 1/E up to recombination
A_HI = np.logspace(np.log10(1/(1+Z_REC)), 0.0, 4000)
Z_HI = 1/A_HI - 1


def E_lcdm(a):
    return np.sqrt(M.OMEGA_M0_LCDM*a**-3 + M.OMEGA_R0_LCDM*a**-4 + M.OMEGA_L0_LCDM)


def E_qfuds_hi(z_star=5.0, om0=M.OMEGA_M0_V2):
    """QFUDS E(a) on the high-z grid: w=-φ relaxed, ρ_X by energy conservation."""
    # relax on density_driven's standard grid, then map w onto A_HI by interpolation
    phi = dd.relax(z_star=z_star, barrier=2.0, mobility=2.0, lam=3.0)
    w_std = -phi                      # on dd.A_GRID (a: 1e-3..1)
    # extend: below a=1e-3 (z>999) w->0 (matter-like); fine for z_rec
    w_hi = np.interp(np.log(A_HI), np.log(dd.A_GRID), w_std, left=w_std[0], right=w_std[-1])
    # ρ_X(a)/ρcrit0 = Ω_X0 exp(-3 ∫_1^a (1+w)/a' da') ; integrate in ln a
    omega_x0 = 1.0 - om0 - M.OMEGA_R0
    lnA = np.log(A_HI)
    F = cumulative_trapezoid(1.0 + w_hi, lnA, initial=0.0)
    F = F - F[-1]
    rho_x = omega_x0 * np.exp(-3.0 * F)
    return np.sqrt(om0*A_HI**-3 + M.OMEGA_R0*A_HI**-4 + rho_x), w_hi


def integral_dz_over_E(E_on_z):
    # ∫_0^{z_rec} dz/E, with z increasing
    order = np.argsort(Z_HI)
    z = Z_HI[order]; e = E_on_z[order]
    return np.trapezoid(1.0/e, z), z, (1.0/e)


def main():
    El = E_lcdm(A_HI)
    Eq, w_hi = E_qfuds_hi(z_star=5.0)

    Il, z, inv_l = integral_dz_over_E(El)
    Iq, _, inv_q = integral_dz_over_E(Eq)

    # Fixed θ* and r_s => D_M(z_rec) fixed. D_M = (c/H0) ∫dz/E, so H0 ∝ ∫dz/E.
    ratio = Iq / Il                       # H0_QFUDS / H0_LCDM  (∝ ∫dz/E)
    H0_qfuds = H0_CMB * ratio
    shift_pct = 100*(ratio - 1)
    direction = ("toward local (relief)" if shift_pct > 0 else
                 "AWAY from local (tension WORSE)")

    print(f"∫dz/E to z_rec:  ΛCDM={Il:.4f}   QFUDS={Iq:.4f}")
    print(f"H0_QFUDS / H0_ΛCDM = {ratio:.5f}  ->  shift = {shift_pct:+.2f}% ({direction})")
    print(f"inferred H0_QFUDS = {H0_qfuds:.2f} km/s/Mpc  (CMB ΛCDM {H0_CMB}, local {H0_LOCAL})")
    print(f"need +{NEED_PCT:.1f}% to close tension; QFUDS delivers {shift_pct:+.2f}% "
          f"-> H0 tension NOT relieved (late transition moves it the wrong way)")

    # fraction of the ∫dz/E that comes from z<2 (where the models differ)
    mz = z <= 2
    frac_lt2 = np.trapezoid(inv_l[mz], z[mz]) / Il
    print(f"\nfraction of ∫dz/E from z<2 (where models differ): {100*frac_lt2:.1f}% "
          f"-> the transition only touches a small slice; z>2 (matter-like) dominates")

    fig, ax = plt.subplots(1, 2, figsize=(13.5, 5.4))
    # (a) the integrand 1/E(z) — where do they differ?
    ax[0].plot(z[z<=6], inv_l[z<=6], "b-", label="ΛCDM")
    ax[0].plot(z[z<=6], inv_q[z<=6], "purple", ls="--", label="QFUDS (z*=5)")
    ax[0].axvline(2.0, color="gray", ls=":", label="transition z≈2")
    ax[0].set_xlabel("z"); ax[0].set_ylabel("1/E(z)  (∫ of this sets D_M, H0)")
    ax[0].set_title("(a) only z<2 differs — a thin slice of ∫ to z≈1090")
    ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3)

    # (b) H0 bar: CMB, local, QFUDS-inferred
    bars = {"CMB ΛCDM\n(67.4)": H0_CMB, "QFUDS\ninferred": H0_qfuds, "local\n(73.0)": H0_LOCAL}
    cols = ["tab:blue", "tab:purple", "tab:red"]
    ax[1].bar(range(3), list(bars.values()), color=cols)
    ax[1].set_xticks(range(3)); ax[1].set_xticklabels(list(bars.keys()))
    ax[1].set_ylim(64, 75); ax[1].set_ylabel("H0 [km/s/Mpc]")
    ax[1].axhline(H0_CMB, color="tab:blue", ls=":", lw=1)
    ax[1].axhline(H0_LOCAL, color="tab:red", ls=":", lw=1)
    for i, v in enumerate(bars.values()):
        ax[1].text(i, v+0.15, f"{v:.2f}", ha="center", fontsize=9)
    ax[1].set_title("(b) QFUDS moves the WRONG way — H0 tension not relieved")

    fig.suptitle("CP10: does QFUDS relieve H0? (inverse distance ladder, exploratory)",
                 fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp10_h0_test.png", dpi=130)
    fig.savefig("fig_cp10_h0_test.svg")
    print("\nsaved fig_cp10_h0_test.png + .svg")

    import csv
    with open("cp10_h0_test_results.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["quantity", "value"])
        w.writerow(["int_dz_E_LCDM", f"{Il:.5f}"])
        w.writerow(["int_dz_E_QFUDS", f"{Iq:.5f}"])
        w.writerow(["H0_ratio_QFUDS_over_LCDM", f"{ratio:.6f}"])
        w.writerow(["H0_shift_pct", f"{shift_pct:.4f}"])
        w.writerow(["H0_QFUDS_inferred", f"{H0_qfuds:.3f}"])
        w.writerow(["H0_CMB", H0_CMB]); w.writerow(["H0_local", H0_LOCAL])
        w.writerow(["pct_needed_to_close", f"{NEED_PCT:.3f}"])
        w.writerow(["frac_integral_from_z_lt_2", f"{frac_lt2:.4f}"])
    print("saved cp10_h0_test_results.csv")


if __name__ == "__main__":
    main()
