"""
CP7: brute-force phenomenological fit. Throw the ambiguous knobs at a grid,
(literature-informed ranges), fit as hard as possible to data, and see how far
the phenomenology can be pushed — i.e. what is the BEST simultaneous fit, and
does it beat ΛCDM or just match it with more parameters?

Free knobs scanned (priors informed by the repo timing work + standard lit):
  z*    ∈ {2,3,4,5,6}     trigger redshift (critical density); retained timing peak ~2
  c_eff²∈ logspace(-7,-2) effective sound speed of the dark component (the S8 lever)
  Ω_m0  ∈ {0.29,0.31,0.33} matter density

Targets (data):
  - fσ8(z): 7 representative RSD points (approximate)
  - S8 weak-lensing prior: 0.76 ± 0.02
  - background gate: max|Δμ(z<2)| vs ΛCDM must stay < 0.10 mag (SNe/BAO consistency)

KEY tension to expose: weak-lensing S8 wants ~0.76 (LOW), but RSD fσ8 prefers the
ΛCDM-ish higher amplitude. Fitting one worsens the other. Brute force shows where
the model settles and what it costs.

STATUS: exploratory. Best-fit knobs are TUNED, not derived; the 050 ceiling and
observer mode stand. Not evidence, not a roadmap change.
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
OM0_DEFAULT = M.OMEGA_M0_V2
OMR = M.OMEGA_R0
SIGMA8_LCDM = 0.81
A_I = 1e-3
C_KM_S, H0, K8 = M.C_KM_S, M.H0_CMB, 0.2

# representative RSD fσ8 data (approximate, label as such)
RSD_Z = np.array([0.067, 0.15, 0.38, 0.51, 0.70, 0.85, 1.48])
RSD_F = np.array([0.423, 0.49, 0.497, 0.459, 0.473, 0.315, 0.462])
RSD_E = np.array([0.055, 0.15, 0.045, 0.038, 0.041, 0.095, 0.045])
S8_OBS, S8_ERR = 0.76, 0.02

# scan grid
ZSTARS = [2.0, 3.0, 4.0, 5.0, 6.0]
CEFF2 = np.logspace(-7, -2, 16)
OM0S = [0.29, 0.31, 0.33]


def lcdm_E(a, om0=M.OMEGA_M0_LCDM):
    return np.sqrt(om0 * a**-3 + M.OMEGA_R0_LCDM * a**-4 + (1 - om0 - M.OMEGA_R0_LCDM))


def growth_D1_and_fsig8(E_interp, dlnE, om0, ceff2, rho_x_interp, z_eval, D1_ref):
    """Solve growth with Ω_clust = Ω_m + η Ω_X; return (sigma8, fσ8 at z_eval)."""
    def eta(a):
        cs = np.sqrt(ceff2)
        R = cs * C_KM_S * K8 / (a * H0 * E_interp(a))
        return 1.0 / (1.0 + R**2)

    def rhs(n, y):
        D, Dp = y; a = np.exp(n)
        Om = om0 * a**-3 / E_interp(a)**2
        Ox = rho_x_interp(a) / E_interp(a)**2
        return [Dp, -(2.0 + dlnE(a)) * Dp + 1.5 * (Om + eta(a) * Ox) * D]

    n_eval = np.log(1.0 / (1.0 + z_eval))
    ns = np.sort(np.concatenate([[np.log(A_I), 0.0], n_eval]))
    sol = solve_ivp(rhs, (np.log(A_I), 0.0), [A_I, A_I], t_eval=ns,
                    method="LSODA", rtol=1e-7, atol=1e-10)
    D = sol.y[0]; Dp = sol.y[1]; n = sol.t
    D1 = np.interp(0.0, n, D)
    sigma8 = SIGMA8_LCDM * D1 / D1_ref
    f = Dp / D                      # f = dlnD/dlna; N=ln a so this is Dp/D (no extra a)
    fsig8 = np.interp(n_eval, n, f * sigma8 * D / D1)
    return sigma8, fsig8


def main():
    # ΛCDM reference growth
    def rhs_l(n, y):
        D, Dp = y; a = np.exp(n)
        El = lcdm_E(a); dl = (np.log(lcdm_E(np.exp(n+1e-5))) - np.log(lcdm_E(np.exp(n-1e-5))))/2e-5
        return [Dp, -(2+dl)*Dp + 1.5*(M.OMEGA_M0_LCDM*a**-3/El**2)*D]
    nl = np.sort(np.concatenate([[np.log(A_I),0.0], np.log(1/(1+RSD_Z))]))
    sl = solve_ivp(rhs_l, (np.log(A_I),0.0), [A_I,A_I], t_eval=nl, method="LSODA", rtol=1e-8, atol=1e-11)
    D1_l = np.interp(0.0, sl.t, sl.y[0])
    fL = sl.y[1]/sl.y[0]            # f = Dp/D in e-folds
    fsig8_l = np.interp(np.log(1/(1+RSD_Z)), sl.t, fL*0.81*sl.y[0]/D1_l)
    chi2_fs_lcdm = np.sum(((fsig8_l - RSD_F)/RSD_E)**2)
    chi2_s8_lcdm = ((0.83 - S8_OBS)/S8_ERR)**2
    print(f"ΛCDM: S8=0.830  χ²_fσ8={chi2_fs_lcdm:.2f}  χ²_S8={chi2_s8_lcdm:.2f}  "
          f"χ²_tot={chi2_fs_lcdm+chi2_s8_lcdm:.2f}")

    # precompute w(a) per z*
    w_by_zstar = {zs: -dd.relax(z_star=zs, barrier=2.0, mobility=2.0, lam=3.0) for zs in ZSTARS}

    best = None
    records = []
    for zs in ZSTARS:
        w = w_by_zstar[zs]
        for om0 in OM0S:
            E = dd.background_from_w(w, om0)
            # background gate
            zc, mu = _dmu(E, om0)
            gate = np.nanmax(np.abs(mu)[zc <= 2])
            lnE = interp1d(np.log(A), np.log(E), kind="cubic", fill_value="extrapolate")
            rhox = E**2 - om0*A**-3 - OMR*A**-4
            lnrx = interp1d(np.log(A), np.log(np.clip(rhox,1e-30,None)), kind="cubic", fill_value="extrapolate")
            Ef = lambda a: np.exp(lnE(np.log(a)))
            dlnE = lambda a: (lnE(np.log(a)+1e-5)-lnE(np.log(a)-1e-5))/2e-5
            rxf = lambda a: np.exp(lnrx(np.log(a)))
            # ΛCDM D1 ref under THIS background is not meaningful; use the global ΛCDM D1_l
            for c2 in CEFF2:
                sigma8, fsig8 = growth_D1_and_fsig8(Ef, dlnE, om0, c2, rxf, RSD_Z, D1_l)
                S8 = sigma8*np.sqrt(om0/0.3)
                chi2_fs = np.sum(((fsig8 - RSD_F)/RSD_E)**2)
                chi2_s8 = ((S8 - S8_OBS)/S8_ERR)**2
                penalty = 1e6 if gate > 0.10 else 0.0
                chi2 = chi2_fs + chi2_s8 + penalty
                records.append((zs, om0, c2, S8, chi2_fs, chi2_s8, chi2, gate))
                if best is None or chi2 < best[6]:
                    best = (zs, om0, c2, S8, chi2_fs, chi2_s8, chi2, gate, fsig8)
    zs,om0,c2,S8,cfs,cs8,ctot,gate,fsig8_best = best
    print(f"\nBEST FIT: z*={zs} Ω_m0={om0} c_eff²={c2:.2e}")
    print(f"  S8={S8:.3f}  χ²_fσ8={cfs:.2f}  χ²_S8={cs8:.2f}  χ²_tot={ctot:.2f}  (gate |Δμ|={gate:.3f})")
    # AIC: ΛCDM ~1 free (Ω_m0); QFUDS adds z*,c_eff²,Ω_m0 -> +3 extra over ΛCDM here
    k_lcdm, k_qfuds = 1, 4
    aic_l = (chi2_fs_lcdm+chi2_s8_lcdm) + 2*k_lcdm
    aic_q = ctot + 2*k_qfuds
    print(f"\nAIC: ΛCDM={aic_l:.2f} (k={k_lcdm}) vs QFUDS best={aic_q:.2f} (k={k_qfuds}) "
          f"-> ΛCDM {'wins' if aic_l<aic_q else 'loses'} by {abs(aic_l-aic_q):.2f}")

    # tension curve: best over (z*,Ω_m0) at each c_eff²
    rec = np.array([(r[2], r[3], r[4], r[6]) for r in records])  # c2,S8,chi2_fs,chi2_tot
    # for each c_eff² take min chi2_fs over z*,Om0
    c2u = np.unique(rec[:,0])
    bestfs = [rec[rec[:,0]==c][:,2].min() for c in c2u]
    s8_at = [rec[rec[:,0]==c][np.argmin(rec[rec[:,0]==c][:,2]),1] for c in c2u]

    fig, ax = plt.subplots(1, 3, figsize=(16, 5))
    ax[0].semilogx(c2u, bestfs, "o-", color="tab:purple", label="QFUDS best χ²_fσ8")
    ax[0].axhline(chi2_fs_lcdm, color="k", ls="--", label=f"ΛCDM χ²_fσ8={chi2_fs_lcdm:.1f}")
    ax[0].set_xlabel("c_eff²"); ax[0].set_ylabel("χ²_fσ8 (7 RSD pts)")
    ax[0].set_title("(a) RSD fit vs sound speed"); ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3)

    ax[1].plot(s8_at, bestfs, "o-", color="tab:purple")
    ax[1].axvline(S8_OBS, color="tab:red", ls="--", label="weak-lensing S8=0.76")
    ax[1].axhline(chi2_fs_lcdm, color="k", ls=":", label="ΛCDM χ²_fσ8")
    ax[1].set_xlabel("S8 (set by c_eff²)"); ax[1].set_ylabel("χ²_fσ8")
    ax[1].set_title("(b) the S8 ↔ fσ8 tug-of-war"); ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3)

    ax[2].errorbar(RSD_Z, RSD_F, yerr=RSD_E, fmt="ko", ms=4, capsize=2, label="RSD (approx)")
    ax[2].plot(RSD_Z, fsig8_l, "b-", label="ΛCDM")
    ax[2].plot(RSD_Z, fsig8_best, "purple", ls="--", label=f"QFUDS best (S8={S8:.2f})")
    ax[2].set_xlabel("z"); ax[2].set_ylabel("fσ8"); ax[2].set_title("(c) best-fit fσ8 vs data")
    ax[2].legend(fontsize=8); ax[2].grid(alpha=0.3)

    fig.suptitle("CP7: brute-force phenomenological fit — how far can tuning push it? (exploratory)",
                 fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp7_brute_fit.png", dpi=130)
    fig.savefig("fig_cp7_brute_fit.svg")
    print("saved fig_cp7_brute_fit.png + .svg")

    # full scan grid -> CSV
    import csv
    with open("cp7_brute_fit_scan.csv", "w", newline="") as fh:
        wcsv = csv.writer(fh)
        wcsv.writerow(["z_star", "omega_m0", "c_eff2", "S8", "chi2_fsigma8",
                       "chi2_S8", "chi2_total", "dmu_gate_mag"])
        for r in records:
            wcsv.writerow([r[0], r[1], f"{r[2]:.6e}", f"{r[3]:.4f}",
                           f"{r[4]:.3f}", f"{r[5]:.3f}", f"{r[6]:.3f}", f"{r[7]:.4f}"])
    # best-fit + ΛCDM comparison summary -> CSV
    with open("cp7_brute_fit_summary.csv", "w", newline="") as fh:
        wcsv = csv.writer(fh)
        wcsv.writerow(["model", "z_star", "omega_m0", "c_eff2", "S8",
                       "chi2_fsigma8", "chi2_S8", "chi2_total", "n_params", "AIC"])
        wcsv.writerow(["LCDM", "-", M.OMEGA_M0_LCDM, "-", "0.830",
                       f"{chi2_fs_lcdm:.3f}", f"{chi2_s8_lcdm:.3f}",
                       f"{chi2_fs_lcdm+chi2_s8_lcdm:.3f}", k_lcdm, f"{aic_l:.3f}"])
        wcsv.writerow(["QFUDS_best", zs, om0, f"{c2:.6e}", f"{S8:.4f}",
                       f"{cfs:.3f}", f"{cs8:.3f}", f"{ctot:.3f}", k_qfuds, f"{aic_q:.3f}"])
    print("saved cp7_brute_fit_scan.csv + cp7_brute_fit_summary.csv")


def _dmu(E, om0):
    from scipy.integrate import cumulative_trapezoid
    z = M.a_to_z(A); order = np.argsort(z); z=z[order]; e=E[order]
    Dc = cumulative_trapezoid(1/e, z, initial=0.0)
    dL = (1+z)*(C_KM_S/H0)*Dc
    El = np.array([float(lcdm_E(a)) for a in A])[order]
    Dcl = cumulative_trapezoid(1/El, z, initial=0.0); dLl=(1+z)*(C_KM_S/H0)*Dcl
    mu = np.where(dL>0, 5*np.log10(np.clip(dL,1e-9,None)*1e5), np.nan)
    mul = np.where(dLl>0, 5*np.log10(np.clip(dLl,1e-9,None)*1e5), np.nan)
    return z, mu-mul


if __name__ == "__main__":
    main()
