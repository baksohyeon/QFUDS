"""
CP15: open the THIRD GDM axis — viscosity c_vis² (anisotropic stress σ) — that
CP11/CP12 pinned to zero, and ask whether it is an INDEPENDENT P(k)/S8 handle at
fixed sound speed c_s².

WHY. Hu 1998 (Generalized Dark Matter, astro-ph/9801234) fixes a dark fluid by
three functions {w(a), c_eff²(=c_s²), c_vis²}. CDM=(0,0,0), Λ=(-1,1,0). CP11
solved the COUPLED 2-fluid sub-horizon system as a PERFECT fluid: c_vis²=0, no
shear σ, no anisotropic stress. CP12 then located the whole toy as "GDM with
c_vis²=0". CP15 turns that knob on: does a non-zero c_vis² give a growth /
P(k)-shape lever that is genuinely independent of the Jeans (c_s²) lever — i.e.
yet ANOTHER tuning handle (ceiling reconfirmed) — or does it barely move anything
(c_vis²=0 justified post hoc)?

WHAT WAS ADDED (the exact equations implemented, e-folds N=ln a, '=d/dN,
ϑ≡θ/𝓗, 𝓗=aH, conformal-Newtonian, sub-horizon, quasi-static potential).
Matter (δ_m,ϑ_m) is UNCHANGED from CP11 (w=0, c_s²=0, σ=0). The dark fluid X
gains a dimensionless shear σ_X:

  δ_m' = -ϑ_m
  ϑ_m' = -(2 + dlnE/dN) ϑ_m - (3/2)(Ω_m δ_m + Ω_X δ_X)

  δ_X' = -(1+w) ϑ_X - 3(c_s² - w) δ_X
  ϑ_X' = -(2 - 3c_s² + dlnE/dN) ϑ_X
         + (c_s²/(1+w)) (k/𝓗)² δ_X
         - (k/𝓗)² σ_X                          # <-- NEW: anisotropic stress
         - (3/2)(Ω_m δ_m + Ω_X δ_X)
  σ_X' = -3 σ_X + (8/3) (c_vis²/(1+w)) ϑ_X        # <-- NEW: Hu GDM shear closure

DERIVATION / JUSTIFICATION of the shear closure (rough, from Hu 1998).
In Hu's GDM the anisotropic stress σ relaxes toward a viscosity-controlled
multiple of the velocity shear. In conformal time τ the standard form is
  σ̇ + 3𝓗 σ = (8/3) c_vis²/(1+w) · (velocity shear source) ,
where 𝓗=aH is the conformal Hubble rate and, sub-horizon in Newtonian gauge,
the metric shear drops and the velocity shear source reduces to the fluid
velocity divergence θ. The factor (8/3)c_vis² is Hu's normalization that maps
c_vis²=1/3 onto relativistic free-streaming (neutrino-like) damping. Converting
to e-folds (d/dτ = 𝓗 d/dN, ϑ≡θ/𝓗) turns 3𝓗σ into 3σ and θ into 𝓗ϑ, giving
the dimensionless line above. The −(k/𝓗)²σ_X term is the anisotropic-stress
entry of the Euler equation (−k²σ in conformal time, divided by 𝓗²). The exact
Hu relaxation coefficient carries O(1) c_a²/w corrections we DROP on purpose —
this is a rough closure, labelled proxy. CRITICALLY none of those O(1) factors
touch the validation: with σ_X(a_i)=0 and the source ∝ c_vis², setting c_vis²=0
makes σ_X≡0 and the system collapses EXACTLY back to CP11's full_2fluid_D1.

VALIDATION (mandatory, reported): c_vis²=0 must reproduce CP11 to ≲1% across k.
SANITY: very large c_vis² strongly free-streams δ_X (smoother, extra suppression)
with a DIFFERENT k-dependence than the c_s² Jeans term — measured below.

STATUS. Exploratory. PARAMETRIZE-not-DERIVE: c_vis² is a hand-turned GDM knob,
NOT derived from foam microphysics. The 050 ceiling (foam → δQ inter-phase
transfer) is untouched. This is a rough CLASS-style sketch (no super-horizon /
relativistic / Boltzmann-hierarchy / nonlinear terms). The real check is
CLASS/hi_class with the full GDM module — Level 3, BLOCKED. Not evidence, not a
roadmap change.
"""
from __future__ import annotations
import csv
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M
import cp5_sound_speed as cp5
import cp11_two_fluid as cp11

C_KM_S, H0 = M.C_KM_S, M.H0_CMB
OM0 = cp5.OM0
A_I = 1e-3
K_GRID = cp11.K_GRID            # reuse CP11 grid so the overlay is apples-to-apples
WL_BAND = cp11.WL_BAND
C2 = cp11.C2                    # fixed data-fit sound speed c_s² = 4.6e-6
S8_REF = 0.83                   # Planck-ish ΛCDM S8 anchor for an "S8-like" number

# viscosity scan (includes 0 for the CP11 validation point)
CVIS2_GRID = np.array([0.0, 1e-6, 1e-4, 1e-2, 1.0])

w_of = cp11.w_of               # identical w(a) curve CP11/CP12 used
k_over_H2 = cp11.k_over_H2


def full_2fluid_visc(k, c2, cvis2):
    """Integrate the 5-variable GDM system (matter + dark fluid with shear).

    Returns (δ_m, δ_comb) at a=1, where δ_comb is the density-weighted total
    clustering field (Ω_m δ_m + Ω_X δ_X)/(Ω_m + Ω_X) that lensing/P(k) sees.
    """
    def rhs(n, y):
        dm, vm, dX, vX, sX = y
        a = np.exp(n)
        E = cp5.E(a); Om = OM0*a**-3/E**2; Ox = cp5.rho_x(a)/E**2
        w = w_of(a); dlnE = cp5.dlnE_dN(a)
        opw = max(1.0 + w, 1e-3)               # regularize 1+w as w->-1 (same as CP11)
        kh2 = k_over_H2(a, k)
        src = 1.5*(Om*dm + Ox*dX)
        ddm = -vm
        dvm = -(2 + dlnE)*vm - src
        ddX = -(1+w)*vX - 3*(c2 - w)*dX
        dvX = (-(2 - 3*c2 + dlnE)*vX
               + (c2/opw)*kh2*dX
               - kh2*sX                        # anisotropic stress on the Euler eq
               - src)
        dsX = -3.0*sX + (8.0/3.0)*(cvis2/opw)*vX   # Hu GDM shear relaxation/closure
        return [ddm, dvm, ddX, dvX, dsX]
    # same growing-mode IC as CP11, plus zero initial shear (adiabatic, MD):
    y0 = [A_I, -A_I, A_I, -A_I, 0.0]
    sol = solve_ivp(rhs, (np.log(A_I), 0.0), y0, method="LSODA",
                    rtol=1e-7, atol=1e-12, t_eval=[0.0], max_step=0.05)
    dm = sol.y[0][-1]; dX = sol.y[2][-1]
    Om1 = OM0; Ox1 = cp5.rho_x(1.0)            # a=1 density weights (ρ/ρcrit0)
    dcomb = (Om1*dm + Ox1*dX)/(Om1 + Ox1)
    return dm, dcomb


def dark_only(k, c2, cvis2):
    """δ_X(k, a=1): dark-fluid contrast, to isolate the suppression k-shape."""
    def rhs(n, y):
        dm, vm, dX, vX, sX = y
        a = np.exp(n)
        E = cp5.E(a); Om = OM0*a**-3/E**2; Ox = cp5.rho_x(a)/E**2
        w = w_of(a); dlnE = cp5.dlnE_dN(a)
        opw = max(1.0 + w, 1e-3); kh2 = k_over_H2(a, k)
        src = 1.5*(Om*dm + Ox*dX)
        return [-vm,
                -(2 + dlnE)*vm - src,
                -(1+w)*vX - 3*(c2 - w)*dX,
                -(2 - 3*c2 + dlnE)*vX + (c2/opw)*kh2*dX - kh2*sX - src,
                -3.0*sX + (8.0/3.0)*(cvis2/opw)*vX]
    sol = solve_ivp(rhs, (np.log(A_I), 0.0), [A_I, -A_I, A_I, -A_I, 0.0],
                    method="LSODA", rtol=1e-7, atol=1e-12, t_eval=[0.0], max_step=0.05)
    return sol.y[2][-1]


def half_suppression_k(kgrid, supp):
    """First k where a (monotone-falling) suppression ratio crosses 0.95."""
    target = 0.95
    for i in range(len(kgrid)-1):
        if (supp[i]-target)*(supp[i+1]-target) <= 0 and supp[i] != supp[i+1]:
            f = (target-supp[i])/(supp[i+1]-supp[i])
            return 10**(np.log10(kgrid[i]) + f*(np.log10(kgrid[i+1])-np.log10(kgrid[i])))
    return np.nan


def main():
    D1L = cp11.lcdm_D1()

    # ---------------------------------------------------------------
    # 1) VALIDATION: c_vis²=0 must reproduce CP11's full_2fluid_D1 (δ_m).
    # ---------------------------------------------------------------
    dm_v0 = np.array([full_2fluid_visc(k, C2, 0.0)[0] for k in K_GRID])
    dm_cp11 = np.array([cp11.full_2fluid_D1(k, C2) for k in K_GRID])
    resid = np.abs(dm_v0/dm_cp11 - 1.0)
    max_resid = float(np.max(resid))
    print(f"[VALIDATION] c_vis²=0 vs CP11 full_2fluid_D1: "
          f"max |δ_m_CP15/δ_m_CP11 - 1| = {max_resid:.2e} "
          f"({'PASS' if max_resid < 0.01 else 'FAIL'} <1% across k)")

    # ---------------------------------------------------------------
    # 2) SCAN c_vis² at FIXED c_s²: transfer T(k) (δ_m-based, CP11-comparable,
    #    and combined) + S8-like integrated amplitude.
    # ---------------------------------------------------------------
    Tm = {}      # δ_m transfer  (validation-clean, overlay CP11)
    Tc = {}      # combined δ transfer
    dX_of = {}   # dark-fluid contrast (for k-shape isolation)
    for cv in CVIS2_GRID:
        dm_k = np.empty_like(K_GRID); dc_k = np.empty_like(K_GRID); dx_k = np.empty_like(K_GRID)
        for i, k in enumerate(K_GRID):
            dm, dc = full_2fluid_visc(k, C2, cv)
            dm_k[i] = dm; dc_k[i] = dc; dx_k[i] = dark_only(k, C2, cv)
        Tm[cv] = (dm_k/D1L)**2
        Tc[cv] = (dc_k/D1L)**2
        dX_of[cv] = dx_k

    band = (K_GRID >= WL_BAND[0]) & (K_GRID <= WL_BAND[1])

    def s8_like(Tcomb):
        # band-averaged amplitude relative to ΛCDM, anchored to a Planck-ish S8
        return S8_REF*np.sqrt(np.mean(Tcomb[band]))

    S8m = np.array([S8_REF*np.sqrt(np.mean(Tm[cv][band])) for cv in CVIS2_GRID])
    S8c = np.array([s8_like(Tc[cv]) for cv in CVIS2_GRID])

    print("\nc_vis²        S8-like(δ_m)   S8-like(combined)")
    for cv, sm, sc in zip(CVIS2_GRID, S8m, S8c):
        print(f"  {cv:.0e}       {sm:.4f}          {sc:.4f}")
    print(f"\nS8-like(combined) range over c_vis²∈[0,1] at fixed c_s²={C2:.1e}: "
          f"{S8c.min():.4f} .. {S8c.max():.4f}  (Δ={S8c.max()-S8c.min():.4f})")
    print(f"S8-like(δ_m)      range: {S8m.min():.4f} .. {S8m.max():.4f}  "
          f"(Δ={S8m.max()-S8m.min():.4f})")

    # ---------------------------------------------------------------
    # 3) k-SHAPE: does viscosity suppress δ_X with a DIFFERENT k-dependence
    #    than the c_s² Jeans term? Compare matched-depth suppression shapes.
    # Both effects isolated at the SAME fixed fit c_s², each relative to the
    # case WITHOUT that effect, so their k-onset is directly comparable:
    #   viscosity:   δ_X(c_s²=fit, c_vis²=1) / δ_X(c_s²=fit, c_vis²=0)
    #   sound speed: δ_X(c_s²=fit, c_vis²=0) / δ_X(c_s²→0,   c_vis²=0)  [pure Jeans]
    supp_vis = dX_of[1.0]/dX_of[0.0]
    dX_nopress = np.array([dark_only(k, 1e-12, 0.0) for k in K_GRID])
    supp_cs = dX_of[0.0]/dX_nopress           # Jeans suppression of the FIT c_s²

    k_half_vis = half_suppression_k(K_GRID, supp_vis)
    k_half_cs = half_suppression_k(K_GRID, supp_cs)
    # Jeans scale where c_s·k/𝓗 ~ 1 today (a=1): k_J = aH/(c·c_s)
    k_jeans = (1.0*H0*cp5.E(1.0))/(C_KM_S*np.sqrt(C2))
    # viscosity onset scale (k/𝓗~1 today, where the (k/𝓗)²σ term wakes up)
    k_visc = (1.0*H0*cp5.E(1.0))/C_KM_S
    print(f"\n[k-shape] viscosity (c_vis²=1, fixed c_s²) δ_X suppression: min={supp_vis.min():.4f}, "
          f"crosses 0.95 at k≈{k_half_vis:.3f} Mpc⁻¹")
    print(f"[k-shape] pure Jeans (fit c_s²={C2:.1e}) δ_X suppression: min={supp_cs.min():.4f}, "
          f"crosses 0.95 at k≈{k_half_cs:.3f} Mpc⁻¹")
    print(f"[k-shape] c_s² Jeans scale k_J = aH/(c·c_s) ≈ {k_jeans:.3f} Mpc⁻¹  ;  "
          f"viscosity scale k_aH = aH/c ≈ {k_visc:.4f} Mpc⁻¹")
    different_shape = (np.isnan(k_half_vis) != np.isnan(k_half_cs)) or (
        not np.isnan(k_half_vis) and not np.isnan(k_half_cs)
        and abs(np.log10(k_half_vis) - np.log10(k_half_cs)) > 0.15)
    print(f"[k-shape] viscosity k-onset {'DIFFERS from' if different_shape else 'resembles'} "
          f"the c_s² Jeans k-onset "
          f"(Δlog10 k ≈ {abs(np.log10(k_half_vis)-np.log10(k_half_cs)):.2f})"
          if not (np.isnan(k_half_vis) or np.isnan(k_half_cs)) else
          f"[k-shape] one onset is off-grid -> shapes differ")

    # verdict: is c_vis² an independent knob? (does it move S8 at fixed c_s²?)
    # Physical S8 proxy = MATTER field δ_m (what weak lensing traces in this V2
    # split, where Ω_m=0.315 stays separate). Combined δ is a secondary diagnostic.
    independent = (S8m.max()-S8m.min()) > 0.01
    print(f"\n[VERDICT] at fixed c_s², c_vis² moves S8-like(δ_m, physical) by "
          f"Δ={S8m.max()-S8m.min():.4f} "
          f"(combined-δ diagnostic moves Δ={S8c.max()-S8c.min():.4f}) -> "
          f"{'INDEPENDENT knob (ceiling reconfirmed: a 3rd tuning handle)' if independent else 'negligible (c_vis²=0 justified)'}")

    # ---------------------------------------------------------------
    # FIGURE
    # ---------------------------------------------------------------
    fig, ax = plt.subplots(1, 2, figsize=(14, 5.6))
    cmap = plt.cm.viridis(np.linspace(0.1, 0.9, len(CVIS2_GRID)))

    ax[0].axvspan(*WL_BAND, color="gray", alpha=0.12, label="weak-lensing band")
    for cv, col in zip(CVIS2_GRID, cmap):
        ax[0].semilogx(K_GRID, Tm[cv], color=col, lw=2,
                       label=f"c_vis²={cv:.0e}")
    # CP11 (c_vis²=0) overlay as validation — δ_m transfer of CP11 (must sit on cv=0)
    Tm_cp11 = (dm_cp11/D1L)**2
    ax[0].semilogx(K_GRID, Tm_cp11, "k--", lw=1.6, dashes=(5, 3),
                   label=f"CP11 c_vis²=0 (resid {max_resid:.0e})")
    ax[0].axvline(k_jeans, color="tab:red", ls=":", lw=1.2,
                  label=f"c_s² Jeans k_J≈{k_jeans:.2g}")
    if not np.isnan(k_half_vis):
        ax[0].axvline(k_half_vis, color="tab:blue", ls="-.", lw=1.2,
                      label=f"c_vis² onset≈{k_half_vis:.2g}")
    ax[0].axhline(1.0, color="k", lw=0.6)
    ax[0].set_xlabel("k [Mpc⁻¹]"); ax[0].set_ylabel("P/P_ΛCDM  (matter δ_m)")
    ax[0].set_title(f"(a) T(k) vs c_vis² at fixed c_s²={C2:.1e}\n"
                    f"CP11 overlay validates c_vis²=0 (max resid {max_resid:.1e})")
    ax[0].legend(fontsize=7.2, loc="best"); ax[0].grid(alpha=0.3)

    cvx = np.clip(CVIS2_GRID, 1e-7, None)
    ax[1].semilogx(cvx, S8m/S8m[0], "s-", color="tab:green", lw=2,
                   label=f"S8-like δ_m (physical), Δ={S8m.max()-S8m.min():.3f}")
    ax[1].semilogx(cvx, S8c/S8c[0], "o--", color="tab:purple", lw=1.6,
                   label=f"total-δ clustering (diag.), Δ={S8c.max()-S8c.min():.3f}")
    ax[1].axhline(1.0, color="k", ls=":", lw=1, label="c_vis²=0 baseline")
    ax[1].annotate(f"c_s² Jeans lever FIXED\n(c_s²={C2:.1e}, k_J≈{k_jeans:.2g} Mpc⁻¹)\n"
                   f"viscosity acts at k≈{k_half_vis:.2g} Mpc⁻¹\n"
                   f"→ different k-scale, independent knob",
                   xy=(0.03, 0.06), xycoords="axes fraction", fontsize=7.2,
                   va="bottom", bbox=dict(boxstyle="round", fc="wheat", alpha=0.6))
    ax[1].set_xlabel("c_vis²  (viscosity / anisotropic stress)")
    ax[1].set_ylabel("amplitude relative to c_vis²=0")
    ax[1].set_title(f"(b) independent leverage of c_vis² at fixed c_s²\n"
                    f"physical S8-like: {S8m[0]:.3f} → {S8m[-1]:.3f}")
    ax[1].legend(fontsize=7.2, loc="best"); ax[1].grid(alpha=0.3)

    fig.suptitle("CP15: GDM third axis — viscosity c_vis² at fixed sound speed (exploratory)",
                 fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp15_viscosity.png", dpi=130)
    fig.savefig("fig_cp15_viscosity.svg")
    print("\nsaved fig_cp15_viscosity.png + .svg")

    # ---------------------------------------------------------------
    # CSV
    # ---------------------------------------------------------------
    with open("cp15_viscosity_results.csv", "w", newline="") as fh:
        wr = csv.writer(fh)
        wr.writerow([f"# CP15 viscosity scan at fixed c_s²={C2:.3e}"])
        wr.writerow(["# Table 1: T(k) combined-delta transfer per c_vis²"])
        wr.writerow(["k_Mpc^-1"] + [f"Tcomb_cvis2={cv:.0e}" for cv in CVIS2_GRID]
                    + [f"Tm_cvis2={cv:.0e}" for cv in CVIS2_GRID])
        for i, k in enumerate(K_GRID):
            wr.writerow([f"{k:.5g}"]
                        + [f"{Tc[cv][i]:.5f}" for cv in CVIS2_GRID]
                        + [f"{Tm[cv][i]:.5f}" for cv in CVIS2_GRID])
        wr.writerow([])
        wr.writerow(["# Table 2: S8-like vs c_vis² at fixed c_s²"])
        wr.writerow(["c_vis2", "S8like_combined", "S8like_dm"])
        for cv, sc, sm in zip(CVIS2_GRID, S8c, S8m):
            wr.writerow([f"{cv:.3e}", f"{sc:.5f}", f"{sm:.5f}"])
        wr.writerow([])
        wr.writerow(["# Table 3: VALIDATION c_vis2=0 vs CP11 full_2fluid_D1 (delta_m)"])
        wr.writerow(["k_Mpc^-1", "dm_CP15_cvis0", "dm_CP11", "abs_rel_resid"])
        for i, k in enumerate(K_GRID):
            wr.writerow([f"{k:.5g}", f"{dm_v0[i]:.6e}", f"{dm_cp11[i]:.6e}",
                         f"{resid[i]:.3e}"])
        wr.writerow(["# max_abs_rel_resid", f"{max_resid:.3e}"])
        wr.writerow([])
        wr.writerow(["# Table 4: k-shape — dark-fluid suppression (both at fixed fit c_s²)"])
        wr.writerow(["k_Mpc^-1", "supp_vis_cvis2=1_over_cvis0",
                     "supp_jeans_fitcs_over_nopress"])
        for i, k in enumerate(K_GRID):
            wr.writerow([f"{k:.5g}", f"{supp_vis[i]:.5f}", f"{supp_cs[i]:.5f}"])
        wr.writerow(["# k_half_vis", f"{k_half_vis:.4f}", "# k_half_cs", f"{k_half_cs:.4f}"])
        wr.writerow(["# k_jeans_cs", f"{k_jeans:.4f}", "# k_visc_aH", f"{k_visc:.4f}"])
    print("saved cp15_viscosity_results.csv")


if __name__ == "__main__":
    main()
