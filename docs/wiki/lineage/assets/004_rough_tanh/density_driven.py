"""
CP3: drive the phase transition by a PHYSICAL quantity instead of a hand-drawn
tilt. The order parameter φ should flip because the matter density ρ_m(a) crosses
a critical value ρ*, not because we drew a curve at a_tr.

Landau control:  the A-phase (DM-like) is favored when dense, B-phase (DE-like)
when dilute. So the tilt is set by how far ρ_m sits above/below ρ*:

    h(a) = lambda * ( ρ_m(a)/ρ* - 1 ) = lambda * ( (a*/a)^3 - 1 )

with a* = 1/(1+z*) the scale factor where ρ_m = ρ*. Now the ONLY location knob is
the single physical number z* (i.e. ρ*). The transition redshift is no longer an
input drawn by hand — it is derived from a critical density, and then DELAYED by
the relaxational lag found in CP2.

This narrows the arbitrariness: instead of {a_tr, Δa} we have {z* (physical
critical density), barrier (latent heat), mobility (relaxation rate)}.

KEY OUTPUTS:
  1. z* -> z_obs map: where must the critical density sit so the OBSERVED
     transition (w=-0.5) lands at z≈2 (the retained timing hook)?
  2. feed the resulting numerical w_eff(a) back into the V2 background and check
     whether it still passes the SNe distance test.

STATUS: exploratory. z* is now physical, but ρ* itself and the barrier/mobility
are still chosen — the 050 ceiling (deriving them from foam microphysics) stands.
Not evidence, not a roadmap change.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp, cumulative_trapezoid
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M

N_I = np.log(1e-3)
N_GRID = np.linspace(N_I, 0.0, 2000)
A_GRID = np.exp(N_GRID)
Z_GRID = 1.0 / A_GRID - 1.0
PHI_SEED = 1e-4


def density_tilt(N, a_star, lam):
    """h(a) from the physical density ratio: >0 when denser than ρ* (favor A)."""
    a = np.exp(N)
    return lam * ((a_star / a) ** 3 - 1.0)


def dF_dphi(phi, h, barrier):
    well = barrier * (2*phi*(1-phi)**2 - 2*phi**2*(1-phi))
    step = h * (6*phi - 6*phi**2)
    return well + step


def relax(z_star, barrier, mobility, lam):
    a_star = 1.0 / (1.0 + z_star)
    s_floor = np.log(PHI_SEED / (1 - PHI_SEED))

    def rhs(N, y):
        s = y[0]
        phi = 1.0 / (1.0 + np.exp(-s))
        h = density_tilt(N, a_star, lam)
        dphi_dN = -mobility * dF_dphi(phi, h, barrier)
        dsdN = dphi_dN / (phi * (1 - phi) + 1e-300)
        if s <= s_floor and dsdN < 0.0:
            dsdN = 0.0
        return [dsdN]

    sol = solve_ivp(rhs, (N_I, 0.0), [s_floor], t_eval=N_GRID,
                    method="LSODA", rtol=1e-8, atol=1e-10, max_step=0.02)
    phi = 1.0 / (1.0 + np.exp(-sol.y[0]))
    return phi


def z_obs_of(phi):
    """Observed transition redshift where w_eff = -phi crosses -0.5."""
    w = -phi
    idx = np.argmin(np.abs(w + 0.5))
    return Z_GRID[idx]


def background_from_w(w, omega_m0=M.OMEGA_M0_V2):
    """ρ_X(a)/ρ_crit0 from numerical w via energy conservation, then E(a)."""
    omega_x0 = 1.0 - omega_m0 - M.OMEGA_R0
    # ρ_X(a) = Ω_X0 exp(-3 ∫_1^a (1+w)/a' da').  Integrate in ln a (= N).
    integrand = (1.0 + w)                      # d(ln a) form: ∫(1+w) dN
    # cumulative from a=1 (N=0) backward; build ∫_1^a (1+w) dN over the grid
    F = cumulative_trapezoid(integrand, N_GRID, initial=0.0)
    F = F - F[-1]                              # set reference at N=0 (a=1)
    rho_x = omega_x0 * np.exp(-3.0 * F)
    E = np.sqrt(omega_m0 * A_GRID**-3 + M.OMEGA_R0 * A_GRID**-4 + rho_x)
    return E


def distance_modulus(E):
    # μ(z) = 5 log10(d_L/10pc); d_L = (1+z)(c/H0)∫_0^z dz'/E. Work on increasing z.
    order = np.argsort(Z_GRID)
    z = Z_GRID[order]; e = E[order]
    Dc = cumulative_trapezoid(1.0 / e, z, initial=0.0)
    dL = (1 + z) * (M.C_KM_S / M.H0_CMB) * Dc
    mu = np.full_like(dL, np.nan)
    mask = dL > 0
    mu[mask] = 5 * np.log10(dL[mask] * 1e6 / 10.0)   # Mpc->pc
    return z, mu


def main():
    barrier, mobility, lam = 2.0, 2.0, 3.0

    # ---- 1) scan z*: where does the OBSERVED transition land? ----
    z_stars = [2.0, 2.5, 3.0, 4.0, 5.0]
    rows = []
    phis = {}
    for zs in z_stars:
        phi = relax(zs, barrier, mobility, lam)
        zo = z_obs_of(phi)
        phis[zs] = phi
        rows.append((zs, zo, zs - zo, -phi[-1]))
    print("trigger z*  ->  observed z_obs (w=-0.5)   lag Δz     w(z=0)")
    for zs, zo, lag, w0 in rows:
        print(f"   {zs:4.1f}            {zo:5.2f}              {lag:5.2f}     {w0:+.3f}")

    # pick z* whose observed transition is closest to z=2 (retained hook)
    best = min(rows, key=lambda r: abs(r[1] - 2.0))
    z_star_best = best[0]
    phi_best = phis[z_star_best]
    w_best = -phi_best
    print(f"\nto land observed transition at z~=2, need critical density at "
          f"z* = {z_star_best:.1f}  (observed z_obs = {best[1]:.2f})")

    # ---- 2) feed numerical w back into background, check SNe ----
    E_model = background_from_w(w_best)
    E_lcdm = np.array([float(M.E_LCDM(a)) for a in A_GRID])
    z_mu, mu_model = distance_modulus(E_model)
    _,    mu_lcdm  = distance_modulus(E_lcdm)
    dmu = mu_model - mu_lcdm
    finite = np.isfinite(dmu) & (z_mu <= 6)
    max_dmu = np.nanmax(np.abs(dmu[finite]))
    z_at_max = z_mu[finite][np.nanargmax(np.abs(dmu[finite]))]
    print(f"background check (density-driven w, z*={z_star_best:.1f}): "
          f"max|Δμ| vs ΛCDM over z<6 = {max_dmu:.3f} mag at z={z_at_max:.2f} "
          f"({'distinguishable' if max_dmu>0.05 else 'within SNe scatter'})")

    # ---- figure ----
    fig, ax = plt.subplots(2, 2, figsize=(13, 9))

    # (a) physical density driver h(a) for each z*
    for zs in z_stars:
        a_star = 1/(1+zs)
        h = density_tilt(N_GRID, a_star, lam)
        ax[0,0].plot(A_GRID, h, label=f"z*={zs}")
    ax[0,0].axhline(0, color="k", lw=0.8)
    ax[0,0].set_xscale("log"); ax[0,0].set_ylim(-5, 15)
    ax[0,0].set_xlabel("scale factor a"); ax[0,0].set_ylabel("h(a) = λ((a*/a)³−1)")
    ax[0,0].set_title("(a) physical driver: matter-density tilt"); ax[0,0].legend(fontsize=8)
    ax[0,0].grid(alpha=0.3)

    # (b) w_eff(z) for each z*
    for zs in z_stars:
        ax[0,1].plot(Z_GRID, -phis[zs], label=f"z*={zs}")
    ax[0,1].plot(Z_GRID, M.w_Q(A_GRID), "k--", lw=1.5, label="CP1 hand tanh")
    ax[0,1].axvline(2.0, color="gray", ls=":")
    ax[0,1].set_xlim(0, 5); ax[0,1].set_xlabel("redshift z"); ax[0,1].set_ylabel("w_eff")
    ax[0,1].set_title("(b) w out of density-driven φ"); ax[0,1].legend(fontsize=8)
    ax[0,1].grid(alpha=0.3)

    # (c) z* -> z_obs lag map
    zss = [r[0] for r in rows]; zos = [r[1] for r in rows]
    ax[1,0].plot(zss, zos, "o-", label="observed z_obs")
    ax[1,0].plot(zss, zss, "k--", lw=1, label="no-lag (z_obs=z*)")
    ax[1,0].axhline(2.0, color="tab:red", ls=":", label="retained hook z=2")
    ax[1,0].set_xlabel("trigger z* (critical density)"); ax[1,0].set_ylabel("observed transition z_obs")
    ax[1,0].set_title("(c) lag: trigger must sit EARLIER than observed"); ax[1,0].legend(fontsize=8)
    ax[1,0].grid(alpha=0.3)

    # (d) Δμ(z) of the tuned density-driven model vs ΛCDM
    ax[1,1].fill_between([0,6], -0.05, 0.05, color="gray", alpha=0.2, label="±0.05 mag (SNe)")
    ax[1,1].plot(z_mu[finite], dmu[finite], color="tab:purple",
                 label=f"density-driven w (z*={z_star_best:.0f})")
    ax[1,1].axhline(0, color="k", lw=0.8)
    ax[1,1].set_xlim(0,6); ax[1,1].set_xlabel("redshift z"); ax[1,1].set_ylabel("Δμ vs ΛCDM (mag)")
    ax[1,1].set_title("(d) background distance check"); ax[1,1].legend(fontsize=8)
    ax[1,1].grid(alpha=0.3)

    fig.suptitle("CP3: density-driven transition — trigger from a critical density (exploratory)",
                 fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_density_driven.png", dpi=130)
    fig.savefig("fig_density_driven.svg")
    print("saved fig_density_driven.png")
    print("saved fig_density_driven.svg")

    # --- CSV dump ---
    import csv as _csv
    _csv_path = "density_driven_results.csv"
    with open(_csv_path, "w", newline="") as _f:
        _wr = _csv.writer(_f)
        # Table 1: z_star -> z_obs lag
        _wr.writerow(["# z* -> z_obs lag table"])
        _wr.writerow(["z_star", "z_obs", "lag_dz", "w_at_z0"])
        for _zs, _zo, _lag, _w0 in rows:
            _wr.writerow([_zs, _zo, _lag, _w0])
        _wr.writerow([])
        # Table 2: (a, w_best) curve for the best z*
        _wr.writerow([f"# w_best curve for z_star={z_star_best:.1f} (observed transition at z~2)"])
        _wr.writerow(["a", "z", "w_best"])
        for _i in range(len(A_GRID)):
            _wr.writerow([A_GRID[_i], Z_GRID[_i], w_best[_i]])
    print(f"saved {_csv_path}")


if __name__ == "__main__":
    main()
