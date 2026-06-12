"""
CP4: close the growth/S8 loop for the CP3 density-driven model.

CP1 found the hand-tanh V2 (smooth transition AT z=2) suppressed growth by ~19%
(S8 0.83 -> 0.67), overshooting the observed S8≈0.76. CP3 produced a DIFFERENT
profile that lands the OBSERVED transition at z≈2 but via a density trigger at
z*≈5 plus relaxational lag (sharper, later-completing shape).

Question: does the lagged density-driven transition still lower S8, and does its
sharper/later shape overshoot LESS than CP1's smooth tanh?

Compares three backgrounds, all with the same clustering matter Ω_m0=0.315:
  - ΛCDM
  - CP1 hand-tanh V2      (w = model.w_Q, smooth, transition at z=2)
  - CP3 density-driven     (w from φ relaxed with z*=5 critical density)

Only ordinary matter clusters; the transitioning dark component is smooth.

STATUS: exploratory. Not evidence, not a roadmap change.
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
Z = dd.Z_GRID
OM0 = M.OMEGA_M0_V2          # 0.315 clustering matter (same in all three)
SIGMA8_LCDM = 0.81
A_I = 1e-3


def E_grids():
    w_tanh = M.w_Q(A)
    E_v2 = dd.background_from_w(w_tanh, OM0)
    phi = dd.relax(z_star=5.0, barrier=2.0, mobility=2.0, lam=3.0)
    w_dens = -phi
    E_dens = dd.background_from_w(w_dens, OM0)
    E_lcdm = np.sqrt(M.OMEGA_M0_LCDM * A**-3 + M.OMEGA_R0_LCDM * A**-4 + M.OMEGA_L0_LCDM)
    return {"ΛCDM": E_lcdm, "CP1 hand-tanh V2": E_v2, "CP3 density-driven": E_dens}


def growth(E_on_grid, om0):
    """Solve D'' + (3/a + E'/E)D' - 1.5 Ω_m(a)/a^2 D = 0 on a∈[A_I,1]."""
    a_sorted = A[np.argsort(A)]
    E_sorted = E_on_grid[np.argsort(A)]
    lnE = interp1d(np.log(a_sorted), np.log(E_sorted), kind="cubic",
                   fill_value="extrapolate")

    def E(a):
        return np.exp(lnE(np.log(a)))

    def dlnE_da(a, h=1e-5):
        return (lnE(np.log(a + h)) - lnE(np.log(a - h))) / (2 * h)

    def rhs(a, y):
        D, Dp = y
        Om = om0 * a**-3 / E(a)**2
        Dpp = -(3.0 / a + dlnE_da(a)) * Dp + 1.5 * Om / a**2 * D
        return [Dp, Dpp]

    sol = solve_ivp(rhs, (A_I, 1.0), [A_I, 1.0], t_eval=np.linspace(A_I, 1, 1500),
                    method="LSODA", rtol=1e-8, atol=1e-10)
    a_out, D, Dp = sol.t, sol.y[0], sol.y[1]
    f = a_out * Dp / D                       # f = dlnD/dlna
    return a_out, D, f


def main():
    Es = E_grids()
    out = {}
    for name, E in Es.items():
        a_out, D, f = growth(E, OM0 if name != "ΛCDM" else M.OMEGA_M0_LCDM)
        out[name] = dict(a=a_out, D=D, f=f)

    D1_lcdm = out["ΛCDM"]["D"][-1]
    print("model                  D(1)/D_LCDM(1)   sigma8    S8      ΔS8 vs ΛCDM")
    summary = {}
    for name, r in out.items():
        ratio = r["D"][-1] / D1_lcdm
        om0 = M.OMEGA_M0_LCDM if name == "ΛCDM" else OM0
        sigma8 = SIGMA8_LCDM * ratio
        S8 = sigma8 * np.sqrt(om0 / 0.3)
        summary[name] = dict(ratio=ratio, sigma8=sigma8, S8=S8)
    S8_lcdm = summary["ΛCDM"]["S8"]
    for name, s in summary.items():
        dS8 = s["S8"] - S8_lcdm
        pct = 100 * dS8 / S8_lcdm
        print(f"{name:22s}  {s['ratio']:.4f}          {s['sigma8']:.4f}   "
              f"{s['S8']:.4f}   {dS8:+.4f} ({pct:+.1f}%)")

    print("\nobserved S8 tension sits around 0.76 (vs Planck ΛCDM ~0.83).")
    cp1 = summary["CP1 hand-tanh V2"]["S8"]
    cp3 = summary["CP3 density-driven"]["S8"]
    print(f"CP1 S8 = {cp1:.3f} (overshoots below 0.76), "
          f"CP3 S8 = {cp3:.3f} -> "
          f"{'less' if abs(cp3-0.76) < abs(cp1-0.76) else 'more'} overshoot than CP1")

    # fσ8(z)
    fig, ax = plt.subplots(1, 3, figsize=(16, 5))
    colors = {"ΛCDM": "tab:blue", "CP1 hand-tanh V2": "tab:green",
              "CP3 density-driven": "tab:purple"}
    for name, r in out.items():
        ax[0].plot(r["a"], r["D"] / r["a"], color=colors[name], label=name)
    ax[0].axvline(1/3, color="gray", ls=":", lw=1, label="z=2")
    ax[0].set_xscale("log"); ax[0].set_xlabel("a"); ax[0].set_ylabel("D(a)/a")
    ax[0].set_title("(a) growth suppression"); ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3)

    for name, r in out.items():
        z_out = 1/r["a"] - 1
        ratio = r["D"][-1] / D1_lcdm if name != "ΛCDM" else 1.0
        s8 = SIGMA8_LCDM * (r["D"][-1]/D1_lcdm)
        fsig8 = r["f"] * s8 * r["D"]/r["D"][-1]
        m = z_out <= 2
        ax[1].plot(z_out[m], fsig8[m], color=colors[name], label=name)
    ax[1].set_xlabel("z"); ax[1].set_ylabel("fσ8(z)")
    ax[1].set_title("(b) fσ8(z)"); ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3)

    names = list(summary.keys())
    S8s = [summary[n]["S8"] for n in names]
    ax[2].bar(range(len(names)), S8s, color=[colors[n] for n in names])
    ax[2].axhline(0.76, color="tab:red", ls="--", label="observed S8≈0.76")
    ax[2].axhline(0.83, color="k", ls=":", label="Planck ΛCDM≈0.83")
    ax[2].set_xticks(range(len(names))); ax[2].set_xticklabels(names, rotation=15, fontsize=8)
    ax[2].set_ylabel("S8"); ax[2].set_title("(c) S8 vs observed band")
    ax[2].legend(fontsize=8); ax[2].grid(alpha=0.3, axis="y")

    fig.suptitle("CP4: growth & S8 for the density-driven (lagged) model (exploratory)",
                 fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp4_growth.png", dpi=130)
    fig.savefig("fig_cp4_growth.svg")
    print("saved fig_cp4_growth.png")
    print("saved fig_cp4_growth.svg")

    # --- CSV dump ---
    import csv as _csv
    _csv_path = "cp4_growth_results.csv"
    with open(_csv_path, "w", newline="") as _f:
        _wr = _csv.writer(_f)
        # Table 1: summary sigma8/S8 per model
        _wr.writerow(["# S8 summary table"])
        _wr.writerow(["model", "D_ratio", "sigma8", "S8", "dS8_vs_LCDM"])
        for _name, _s in summary.items():
            _dS8 = _s["S8"] - summary["ΛCDM"]["S8"]
            _wr.writerow([_name, _s["ratio"], _s["sigma8"], _s["S8"], _dS8])
        _wr.writerow([])
        # Table 2: fsigma8(z) curves
        _wr.writerow(["# fsigma8(z) curves"])
        _model_names = list(out.keys())
        _wr.writerow(["z"] + _model_names)
        # build a common z grid (use the shortest a_out)
        _a_ref = out[_model_names[0]]["a"]
        _z_ref = 1 / _a_ref - 1
        _mask_z2 = _z_ref <= 2.0
        _z_out = _z_ref[_mask_z2][::-1]  # increasing z
        for _iz, _zval in enumerate(_z_out):
            _a_val = 1.0 / (1.0 + _zval)
            _row = [_zval]
            for _mn in _model_names:
                _r = out[_mn]
                _a_m = _r["a"]
                _D_m = _r["D"]
                _f_m = _r["f"]
                _D0_m = _r["D"][-1]
                _s8_m = SIGMA8_LCDM * (_D0_m / D1_lcdm)
                _fs8_arr = _f_m * _s8_m * _D_m / _D0_m
                _fs8_val = float(np.interp(_a_val, _a_m, _fs8_arr))
                _row.append(_fs8_val)
            _wr.writerow(_row)
    print(f"saved {_csv_path}")


if __name__ == "__main__":
    main()
