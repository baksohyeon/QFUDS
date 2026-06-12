"""
CP9: confront the correlation length ξ with the weak-lensing P(k) SHAPE.

CP8 said the data-preferred c_eff²≈4.6e-6 hides a correlation length ξ≈10 Mpc.
A clustering dark component with sound speed does NOT suppress structure uniformly
— it clusters on scales below its Jeans scale (k < k_J ≈ 1/ξ) and stays smooth
above it. So it imprints a SCALE-DEPENDENT step on P(k) at k_J, unlike a plain
low-σ8 ΛCDM which suppresses P(k) by the same factor at ALL k.

We solve the scale-dependent linear growth D(k,a) with a k-dependent clustering
efficiency
    η(k,a) = 1 / (1 + (c_s · c · k / (a H))²)
and form the lensing-relevant suppression
    T(k) = [ D_QFUDS(k, a=1) / D_ΛCDM(a=1) ]²   ≈  P_QFUDS(k)/P_ΛCDM(k).

Question: is the QFUDS suppression a SCALE-DEPENDENT step (distinctive, falsifiable
by weak-lensing P(k) shape) or does it mimic a uniform low-σ8 shift?

STATUS: exploratory, rough (Jeans-η proxy growth, no full Boltzmann/CLASS — that
is Level 3, blocked). Not evidence, not a roadmap change.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M
import cp5_sound_speed as cp5

A_I = 1e-3
C_KM_S, H0 = M.C_KM_S, M.H0_CMB
OM0 = cp5.OM0

# wavenumber grid (Mpc^-1); weak-lensing roughly probes ~0.05 .. 1 Mpc^-1
K_GRID = np.logspace(-2.3, 0.3, 30)
WL_BAND = (0.05, 1.0)


def k_jeans(c2, a=1.0, E=1.0):
    """k_J where R=1 today: k_J = a H / (c_s c) [Mpc^-1]."""
    cs = np.sqrt(c2)
    return a * H0 * E / (cs * C_KM_S) if cs > 0 else np.inf


def D1_scaledep(k, c2):
    """growth D(k, a=1) with k-dependent clustering of the dark component."""
    def eta(a):
        cs = np.sqrt(c2)
        R = cs * C_KM_S * k / (a * H0 * cp5.E(a))
        return 1.0 / (1.0 + R**2)
    def rhs(n, y):
        D, Dp = y; a = np.exp(n)
        Om = OM0 * a**-3 / cp5.E(a)**2
        Ox = cp5.rho_x(a) / cp5.E(a)**2
        return [Dp, -(2.0 + cp5.dlnE_dN(a)) * Dp + 1.5 * (Om + eta(a) * Ox) * D]
    sol = solve_ivp(rhs, (np.log(A_I), 0.0), [A_I, A_I], t_eval=[0.0],
                    method="LSODA", rtol=1e-7, atol=1e-11)
    return sol.y[0][-1]


def lcdm_D1():
    def rhs(n, y):
        D, Dp = y; a = np.exp(n)
        El = np.sqrt(M.OMEGA_M0_LCDM*a**-3 + M.OMEGA_R0_LCDM*a**-4 + M.OMEGA_L0_LCDM)
        dl = (np.log(np.sqrt(M.OMEGA_M0_LCDM*np.exp(n+1e-5)**-3+M.OMEGA_R0_LCDM*np.exp(n+1e-5)**-4+M.OMEGA_L0_LCDM))
              - np.log(np.sqrt(M.OMEGA_M0_LCDM*np.exp(n-1e-5)**-3+M.OMEGA_R0_LCDM*np.exp(n-1e-5)**-4+M.OMEGA_L0_LCDM)))/2e-5
        return [Dp, -(2+dl)*Dp + 1.5*(M.OMEGA_M0_LCDM*a**-3/El**2)*D]
    s = solve_ivp(rhs, (np.log(A_I), 0.0), [A_I, A_I], t_eval=[0.0],
                  method="LSODA", rtol=1e-8, atol=1e-11)
    return s.y[0][-1]


def main():
    D1L = lcdm_D1()
    # data-fit c_eff² and two bracketing ξ values
    cases = {
        "ξ≈10 Mpc (data-fit, c_eff²=4.6e-6)": 4.6e-6,
        "ξ≈3 Mpc (c_eff²=5e-7)":             5e-7,
        "ξ≈30 Mpc (c_eff²=5e-5)":            5e-5,
    }
    colors = {list(cases)[0]: "tab:purple", list(cases)[1]: "tab:green", list(cases)[2]: "tab:orange"}

    print("case                                     k_J[Mpc^-1]   T(k=0.02)  T(k=0.3)")
    results = {}
    for name, c2 in cases.items():
        T = np.array([(D1_scaledep(k, c2)/D1L)**2 for k in K_GRID])
        results[name] = T
        kJ = k_jeans(c2)
        T_lo = np.interp(0.02, K_GRID, T); T_hi = np.interp(0.3, K_GRID, T)
        print(f"{name:40s} {kJ:8.3f}     {T_lo:.3f}     {T_hi:.3f}")

    # reference: uniform low-σ8 shift that matches S8=0.76 (scale-independent)
    flat = (0.76/0.83)**2
    print(f"\nreference: uniform low-σ8 (S8 0.83->0.76) suppression = {flat:.3f} at ALL k")
    print("=> QFUDS suppression is SCALE-DEPENDENT (step at k_J); low-σ8 is FLAT. "
          "Weak-lensing P(k) shape across k_J~0.1 distinguishes them.")

    fig, (ax, ax2) = plt.subplots(1, 2, figsize=(15, 5.8))
    # (a) raw P-ratio
    ax.axvspan(WL_BAND[0], WL_BAND[1], color="gray", alpha=0.12,
               label="weak-lensing P(k) sensitivity")
    for name, T in results.items():
        ax.semilogx(K_GRID, T, color=colors[name], lw=2, label=name)
        ax.axvline(k_jeans(cases[name]), color=colors[name], ls=":", lw=1)
    ax.axhline(1.0, color="k", lw=0.7)
    ax.set_xlabel("k  [Mpc⁻¹]"); ax.set_ylabel("P_QFUDS(k) / P_ΛCDM(k)")
    ax.set_title("(a) raw ratio (level is normalization-dependent)")
    ax.legend(fontsize=8, loc="lower left"); ax.grid(alpha=0.3)

    # (b) SHAPE only: normalize each curve to its large-scale (small-k) value,
    # which CMB would pin. Isolates the scale-dependent fingerprint.
    ax2.axvspan(WL_BAND[0], WL_BAND[1], color="gray", alpha=0.12,
                label="weak-lensing P(k) sensitivity")
    for name, T in results.items():
        ax2.semilogx(K_GRID, T/T[0], color=colors[name], lw=2, label=name)
        ax2.axvline(k_jeans(cases[name]), color=colors[name], ls=":", lw=1)
    ax2.axhline(1.0, color="tab:red", ls="--", label="uniform low-σ8 (FLAT = no shape)")
    ax2.set_xlabel("k  [Mpc⁻¹]"); ax2.set_ylabel("shape: P-ratio / (large-scale value)")
    ax2.set_title("(b) scale-dependent fingerprint vs flat low-σ8")
    ax2.legend(fontsize=8, loc="lower left"); ax2.grid(alpha=0.3)

    fig.suptitle("CP9: the foam's weak-lensing P(k) fingerprint — step at k_J≈1/ξ (exploratory)",
                 fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp9_lensing_pk.png", dpi=130)
    fig.savefig("fig_cp9_lensing_pk.svg")
    print("\nsaved fig_cp9_lensing_pk.png + .svg")

    import csv
    with open("cp9_lensing_pk_results.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["k_Mpc^-1"] + [f"T_{n.split('(')[0].strip()}" for n in cases] + ["uniform_lowS8_ref"])
        for i, k in enumerate(K_GRID):
            w.writerow([f"{k:.5g}"] + [f"{results[n][i]:.4f}" for n in cases] + [f"{flat:.4f}"])
    print("saved cp9_lensing_pk_results.csv")


if __name__ == "__main__":
    main()
