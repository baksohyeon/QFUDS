"""
CP11: replace the η Jeans PROXY (CP5/CP9) with the actual coupled 2-fluid
sub-horizon perturbation system, and check how far the proxy deviated.

The real system (Ma & Bertschinger 1995, conformal-Newtonian gauge, sub-horizon,
quasi-static potential) for matter (w=0, c_s²=0) + dark fluid X (w(a), c_s²),
coupled only through the Poisson potential, in e-folds N=ln a (' = d/dN), with
ϑ ≡ θ/𝓗 (dimensionless velocity divergence) and 𝓗=aH:

  δ_m' = -ϑ_m
  ϑ_m' = -(2 + dlnE/dN) ϑ_m - (3/2)(Ω_m δ_m + Ω_X δ_X)

  δ_X' = -(1+w) ϑ_X - 3(c_s² - w) δ_X
  ϑ_X' = -(2 - 3c_s² + dlnE/dN) ϑ_X
         + (c_s²/(1+w)) (k/𝓗)² δ_X
         - (3/2)(Ω_m δ_m + Ω_X δ_X)

The (k/𝓗)² c_s² term is the Jeans pressure that smooths δ_X above its sound
horizon — exactly what the η-proxy mimicked with η=1/(1+R²). Here it is exact.

Limits (sanity): c_s²→0 -> δ_X tracks δ_m (full clustering); c_s²→1 -> δ_X
pressure-oscillates to ~0 (smooth). Both checked below.

This is the rough "CLASS-style" calculation for the PHENOMENOLOGICAL fluid (no
super-horizon/relativistic terms, no nonlinear, no Boltzmann hierarchy). The
physical-QFUDS version would need the DERIVED δQ transfer between phases — that
is the 050 ceiling. Exploratory; not evidence, not a roadmap change.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M
import density_driven as dd
import cp5_sound_speed as cp5

C_KM_S, H0 = M.C_KM_S, M.H0_CMB
OM0, OMR = cp5.OM0, M.OMEGA_R0
A_I = 1e-3
K_GRID = np.logspace(-2.3, 0.3, 22)        # Mpc^-1
WL_BAND = (0.05, 1.0)
C2 = 4.6e-6                                  # data-fit c_eff²

# w(a) of the density-driven model, on a fast interpolator
_w_std = -dd.relax(z_star=5.0, barrier=2.0, mobility=2.0, lam=3.0)
_lnw = interp1d(np.log(dd.A_GRID), _w_std, fill_value=(_w_std[0], _w_std[-1]), bounds_error=False)
def w_of(a): return float(_lnw(np.log(a)))


def k_over_H2(a, k):
    """(k/𝓗)² with 𝓗 = aH; dimensionless via c."""
    return (C_KM_S * k / (a * H0 * cp5.E(a)))**2


def full_2fluid_D1(k, c2):
    """Integrate the 4-variable system; return matter δ_m(k, a=1)."""
    def rhs(n, y):
        dm, vm, dX, vX = y
        a = np.exp(n)
        E = cp5.E(a); Om = OM0*a**-3/E**2; Ox = cp5.rho_x(a)/E**2
        w = w_of(a); dlnE = cp5.dlnE_dN(a)
        opw = max(1.0 + w, 1e-3)          # regularize 1+w as w->-1 (vacuum-like, smooth)
        src = 1.5*(Om*dm + Ox*dX)
        ddm = -vm
        dvm = -(2 + dlnE)*vm - src
        ddX = -(1+w)*vX - 3*(c2 - w)*dX
        dvX = (-(2 - 3*c2 + dlnE)*vX
               + (c2/opw)*k_over_H2(a, k)*dX
               - src)
        return [ddm, dvm, ddX, dvX]
    # matter-dominated growing-mode IC: δ∝a => δ'=δ => ϑ=-δ ; X is matter-like early
    y0 = [A_I, -A_I, A_I, -A_I]
    sol = solve_ivp(rhs, (np.log(A_I), 0.0), y0, method="LSODA",
                    rtol=1e-7, atol=1e-12, t_eval=[0.0], max_step=0.05)
    return sol.y[0][-1]


def proxy_D1(k, c2):
    """CP9 η-proxy: single growth eq with Ω_clust = Ω_m + η(k,a) Ω_X."""
    def eta(a):
        R = np.sqrt(c2)*C_KM_S*k/(a*H0*cp5.E(a))
        return 1.0/(1.0+R**2)
    def rhs(n, y):
        D, Dp = y; a = np.exp(n)
        Om = OM0*a**-3/cp5.E(a)**2; Ox = cp5.rho_x(a)/cp5.E(a)**2
        return [Dp, -(2+cp5.dlnE_dN(a))*Dp + 1.5*(Om+eta(a)*Ox)*D]
    sol = solve_ivp(rhs, (np.log(A_I), 0.0), [A_I, A_I], method="LSODA",
                    rtol=1e-7, atol=1e-11, t_eval=[0.0])
    return sol.y[0][-1]


def lcdm_D1():
    def rhs(n, y):
        D, Dp = y; a = np.exp(n)
        El = np.sqrt(M.OMEGA_M0_LCDM*a**-3+M.OMEGA_R0_LCDM*a**-4+M.OMEGA_L0_LCDM)
        dl = (np.log(np.sqrt(M.OMEGA_M0_LCDM*np.exp(n+1e-5)**-3+M.OMEGA_R0_LCDM*np.exp(n+1e-5)**-4+M.OMEGA_L0_LCDM))
              - np.log(np.sqrt(M.OMEGA_M0_LCDM*np.exp(n-1e-5)**-3+M.OMEGA_R0_LCDM*np.exp(n-1e-5)**-4+M.OMEGA_L0_LCDM)))/2e-5
        return [Dp, -(2+dl)*Dp + 1.5*(M.OMEGA_M0_LCDM*a**-3/El**2)*D]
    s = solve_ivp(rhs, (np.log(A_I), 0.0), [A_I, A_I], method="LSODA",
                  rtol=1e-8, atol=1e-11, t_eval=[0.0])
    return s.y[0][-1]


def main():
    D1L = lcdm_D1()

    # --- sanity: limits at a representative k ---
    k0 = 0.2
    dm_clust = full_2fluid_D1(k0, 1e-9)    # c_s²→0: should cluster (large δ_m)
    dm_smooth = full_2fluid_D1(k0, 1.0)    # c_s²→1: smooth dark -> less growth
    print(f"limit check at k={k0}: δ_m(c_s²→0)/δ_m(c_s²=1) = "
          f"{dm_clust/dm_smooth:.3f}  (>1 expected: clustering boosts growth)")

    T_full, T_prox = [], []
    for k in K_GRID:
        T_full.append((full_2fluid_D1(k, C2)/D1L)**2)
        T_prox.append((proxy_D1(k, C2)/D1L)**2)
    T_full = np.array(T_full); T_prox = np.array(T_prox)

    # normalize both to large-scale (small-k) value -> shape comparison
    Sf = T_full/T_full[0]; Sp = T_prox/T_prox[0]
    band = (K_GRID >= WL_BAND[0]) & (K_GRID <= WL_BAND[1])
    max_dev = np.max(np.abs(Sf[band]-Sp[band]))
    print(f"\nshape (normalized) max |proxy - full| over WL band = {max_dev:.3f} "
          f"({100*max_dev:.1f}% of large-scale power)")
    print(f"raw T_full/T_proxy over WL band: "
          f"{np.min(T_full[band]/T_prox[band]):.3f} .. {np.max(T_full[band]/T_prox[band]):.3f}")

    fig, ax = plt.subplots(1, 2, figsize=(14, 5.6))
    ax[0].axvspan(*WL_BAND, color="gray", alpha=0.12, label="weak-lensing band")
    ax[0].semilogx(K_GRID, T_full, "purple", lw=2, label="full 2-fluid")
    ax[0].semilogx(K_GRID, T_prox, "tab:green", ls="--", lw=2, label="η Jeans proxy (CP9)")
    ax[0].axhline(1.0, color="k", lw=0.7)
    ax[0].set_xlabel("k [Mpc⁻¹]"); ax[0].set_ylabel("P/P_ΛCDM (raw)")
    ax[0].set_title("(a) full 2-fluid vs proxy — raw"); ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3)

    ax[1].axvspan(*WL_BAND, color="gray", alpha=0.12, label="weak-lensing band")
    ax[1].semilogx(K_GRID, Sf, "purple", lw=2, label="full 2-fluid (shape)")
    ax[1].semilogx(K_GRID, Sp, "tab:green", ls="--", lw=2, label="η proxy (shape)")
    ax[1].set_xlabel("k [Mpc⁻¹]"); ax[1].set_ylabel("shape: T(k)/T(k→0)")
    ax[1].set_title(f"(b) shape match — max dev {100*max_dev:.1f}% over WL band")
    ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3)

    fig.suptitle("CP11: η proxy vs full 2-fluid perturbations (exploratory)", fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp11_two_fluid.png", dpi=130)
    fig.savefig("fig_cp11_two_fluid.svg")
    print("\nsaved fig_cp11_two_fluid.png + .svg")

    import csv
    with open("cp11_two_fluid_results.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["k_Mpc^-1", "T_full", "T_proxy", "shape_full", "shape_proxy"])
        for i, k in enumerate(K_GRID):
            w.writerow([f"{k:.5g}", f"{T_full[i]:.4f}", f"{T_prox[i]:.4f}",
                        f"{Sf[i]:.4f}", f"{Sp[i]:.4f}"])
    print("saved cp11_two_fluid_results.csv")


if __name__ == "__main__":
    main()
