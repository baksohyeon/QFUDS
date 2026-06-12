"""
CP5: open the effective sound speed c_eff² of the transitioning dark component.

CP4 showed the S8 overshoot (S8≈0.68 vs observed ≈0.76) is structural in the
transition SHAPE, and pointed at the real lever: c_eff². A smooth component
(c_eff²≈1, doesn't cluster) over-suppresses growth; a clustering one (c_eff²≈0)
behaves like matter and would not suppress. The truth is in between.

ROUGH PROXY (not full perturbation theory): a fluid mode is pressure-supported
above its sound horizon, k·c_s > aH. So at the S8 scale k_8 the dark component
clusters with a Jeans efficiency

    η(a) = 1 / (1 + R(a)²),   R(a) = c_s · c · k_8 / (a · H0 · E(a)),  c_s=√c_eff²

η→1 (clusters like matter) when c_s is tiny; η→0 (smooth) when c_s≈1. The growth
source then uses an effective clustering fraction Ω_clust = Ω_m + η·Ω_X.

NOTE: this is a transparent Jeans proxy to show the TREND and locate the c_eff²
that would fit S8. The rigorous calculation is the coupled clustering-DE
perturbations in CLASS — that is Level 3 and BLOCKED. Finding a fitting c_eff² is
adding a tuned knob (exactly 003's "c_eff²=0 is an unresolved condition"), not a
derivation. Exploratory; not evidence, not a roadmap change.
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

A = dd.A_GRID
N = dd.N_GRID
OM0 = M.OMEGA_M0_V2
OMR = M.OMEGA_R0
SIGMA8_LCDM = 0.81
S8_OBS = 0.76
A_I = 1e-3

C_KM_S = M.C_KM_S          # 299792 km/s
H0 = M.H0_CMB              # 67.4 km/s/Mpc
K8 = 0.2                   # Mpc^-1, representative S8-scale wavenumber

# density-driven background (z*=5, lands observed transition at z≈2)
_phi = dd.relax(z_star=5.0, barrier=2.0, mobility=2.0, lam=3.0)
_w = -_phi
E_DENS = dd.background_from_w(_w, OM0)
RHO_X = E_DENS**2 - OM0 * A**-3 - OMR * A**-4     # transitioning component density

lnE = interp1d(np.log(A), np.log(E_DENS), kind="cubic", fill_value="extrapolate")
ln_rhox = interp1d(np.log(A), np.log(np.clip(RHO_X, 1e-30, None)),
                   kind="cubic", fill_value="extrapolate")


def E(a):       return np.exp(lnE(np.log(a)))
def rho_x(a):   return np.exp(ln_rhox(np.log(a)))
def dlnE_dN(a, h=1e-5):
    return (lnE(np.log(a) + h) - lnE(np.log(a) - h)) / (2 * h)


def eta(a, ceff2):
    cs = np.sqrt(ceff2)
    R = cs * C_KM_S * K8 / (a * H0 * E(a))
    return 1.0 / (1.0 + R**2)


def S8_of_ceff2(ceff2):
    """Solve growth in e-folds with effective clustering Ω_clust = Ω_m + η Ω_X."""
    def rhs(n, y):
        D, Dp = y                       # ' = d/dN
        a = np.exp(n)
        Om = OM0 * a**-3 / E(a)**2
        Ox = rho_x(a) / E(a)**2
        Om_clust = Om + eta(a, ceff2) * Ox
        Dpp = -(2.0 + dlnE_dN(a)) * Dp + 1.5 * Om_clust * D
        return [Dp, Dpp]
    n0, n1 = np.log(A_I), 0.0
    sol = solve_ivp(rhs, (n0, n1), [A_I, A_I], t_eval=np.linspace(n0, n1, 1200),
                    method="LSODA", rtol=1e-8, atol=1e-12)
    return sol.y[0][-1]


def main():
    # reference: ΛCDM growth (standard, η irrelevant)
    def rhs_lcdm(n, y):
        D, Dp = y; a = np.exp(n)
        El = np.sqrt(M.OMEGA_M0_LCDM*a**-3 + M.OMEGA_R0_LCDM*a**-4 + M.OMEGA_L0_LCDM)
        dl = (np.log(np.sqrt(M.OMEGA_M0_LCDM*np.exp(n+1e-5)**-3+M.OMEGA_R0_LCDM*np.exp(n+1e-5)**-4+M.OMEGA_L0_LCDM))
              - np.log(np.sqrt(M.OMEGA_M0_LCDM*np.exp(n-1e-5)**-3+M.OMEGA_R0_LCDM*np.exp(n-1e-5)**-4+M.OMEGA_L0_LCDM)))/(2e-5)
        Om = M.OMEGA_M0_LCDM*a**-3/El**2
        return [Dp, -(2+dl)*Dp + 1.5*Om*D]
    sol_l = solve_ivp(rhs_lcdm, (np.log(A_I), 0.0), [A_I, A_I],
                      t_eval=[0.0], method="LSODA", rtol=1e-8, atol=1e-12)
    D1_lcdm = sol_l.y[0][-1]

    ceff2_grid = np.logspace(-8, 0, 25)
    S8s = []
    for c2 in ceff2_grid:
        D1 = S8_of_ceff2(c2)
        sigma8 = SIGMA8_LCDM * D1 / D1_lcdm
        S8 = sigma8 * np.sqrt(OM0 / 0.3)
        S8s.append(S8)
    S8s = np.array(S8s)

    print("c_eff²       S8")
    for c2, s8 in zip(ceff2_grid, S8s):
        print(f"  {c2:.2e}   {s8:.4f}")

    # find c_eff² where S8 crosses observed 0.76 (S8 decreases as c_eff² grows)
    cross = None
    for i in range(len(S8s) - 1):
        if (S8s[i] - S8_OBS) * (S8s[i+1] - S8_OBS) <= 0:
            # log-linear interp
            f = (S8_OBS - S8s[i]) / (S8s[i+1] - S8s[i])
            cross = 10 ** (np.log10(ceff2_grid[i]) + f*(np.log10(ceff2_grid[i+1])-np.log10(ceff2_grid[i])))
            break
    print(f"\nS8 range over c_eff²∈[1e-8,1]: {S8s.min():.3f} .. {S8s.max():.3f}")
    if cross is not None:
        print(f"S8 = {S8_OBS} reached at c_eff² ≈ {cross:.2e}  "
              f"(an extreme fine-tune; tiny sound speed required)")
    else:
        print(f"S8 = {S8_OBS} NOT reachable in scanned range "
              f"(observed band sits outside [{S8s.min():.3f},{S8s.max():.3f}])")

    fig, ax = plt.subplots(1, 2, figsize=(13, 5.2))
    ax[0].semilogx(ceff2_grid, S8s, "o-", color="tab:purple", label="density-driven model")
    ax[0].axhline(0.83, color="k", ls=":", label="Planck ΛCDM ≈ 0.83")
    ax[0].axhline(S8_OBS, color="tab:red", ls="--", label="observed S8 ≈ 0.76")
    if cross is not None:
        ax[0].axvline(cross, color="tab:green", ls="-.", label=f"fit c_eff²≈{cross:.1e}")
    ax[0].set_xlabel("c_eff²  (sound speed² of dark component)")
    ax[0].set_ylabel("S8"); ax[0].set_title("(a) S8 vs sound speed")
    ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3)

    # η(a) for a few c_eff² to show what clusters
    for c2 in [1.0, 1e-4, 1e-6, 1e-8]:
        ax[1].plot(1/A - 1, [eta(ai, c2) for ai in A], label=f"c_eff²={c2:.0e}")
    ax[1].set_xlim(0, 5); ax[1].set_xlabel("z"); ax[1].set_ylabel("η = clustering efficiency")
    ax[1].set_title("(b) how much of Ω_X clusters at the S8 scale")
    ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3)

    fig.suptitle("CP5: opening c_eff² — can the dark component cluster enough to fit S8? (exploratory)",
                 fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp5_sound_speed.png", dpi=130)
    print("saved fig_cp5_sound_speed.png")


if __name__ == "__main__":
    main()
