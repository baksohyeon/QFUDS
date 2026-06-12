"""
CP6b: FALSIFICATION — locate where the QFUDS density-driven model differs from ΛCDM.

STATUS: exploratory sandbox. NOT validated. This is a phenomenological model with a
hand-tuned tanh order-parameter and a Jeans-proxy sound-speed treatment (not full
perturbation theory). Do NOT read outputs as confirming or ruling out QFUDS.

Approximate RSD data points are labeled as such and are for directional guidance only.
The c_eff²≈3×10⁻⁵ value from CP5 is the rough S8-fitting knob, not a derived prediction.

Outputs:
  - Printed falsification table to stdout
  - fig_cp6b_falsification.png (panel a: fσ8(z) + data; panel b: w(z) vs DESI-CPL)
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

# ---------------------------------------------------------------------------
# Shared grids and density-driven background (z*=5 → observed transition z≈2)
# ---------------------------------------------------------------------------
A_GRID = dd.A_GRID           # scale factor, 1e-3 → 1 (increasing)
N_GRID = dd.N_GRID           # ln(a), same shape
OM0    = M.OMEGA_M0_V2       # 0.315  (baryons + CDM; same in all models)
OMR    = M.OMEGA_R0

SIGMA8_LCDM  = 0.81          # assumed ΛCDM σ8(z=0) for normalization
A_I          = 1e-3          # ODE initial scale factor
C_EFF2_FIT   = 3e-5          # S8-fitting c_eff² from CP5 (approximate)
C_KM_S       = M.C_KM_S     # 299 792 km/s
H0           = M.H0_CMB      # 67.4 km/s/Mpc
K8           = 0.2           # Mpc⁻¹, representative S8-scale k

print("Building density-driven background (z*=5) ...")
_phi_arr    = dd.relax(z_star=5.0, barrier=2.0, mobility=2.0, lam=3.0)
_w_dens_arr = -_phi_arr
E_DENS      = dd.background_from_w(_w_dens_arr, OM0)
RHO_X_arr   = np.clip(E_DENS**2 - OM0 * A_GRID**-3 - OMR * A_GRID**-4, 1e-30, None)

_lnE_itp    = interp1d(np.log(A_GRID), np.log(E_DENS),    kind="cubic", fill_value="extrapolate")
_lnRhoX_itp = interp1d(np.log(A_GRID), np.log(RHO_X_arr), kind="cubic", fill_value="extrapolate")


def _E_q(a):
    return np.exp(_lnE_itp(np.log(np.clip(a, 1e-6, None))))


def _rhoX(a):
    return np.exp(_lnRhoX_itp(np.log(np.clip(a, 1e-6, None))))


def _dlnE_dN_q(a, h: float = 5e-5) -> float:
    """d ln E / d ln a for QFUDS background (numerical)."""
    la = np.log(np.clip(a, 1e-6, None))
    return (_lnE_itp(la + h) - _lnE_itp(la - h)) / (2.0 * h)


def _eta(a, ceff2: float) -> float:
    """Jeans clustering efficiency on the S8 scale."""
    cs = np.sqrt(ceff2)
    R  = cs * C_KM_S * K8 / (a * H0 * _E_q(a))
    return 1.0 / (1.0 + R**2)


# ---------------------------------------------------------------------------
# Growth ODE solvers (e-folds N = ln a)
# Returns (a_out, D, f) with a_out increasing A_I → 1
# ---------------------------------------------------------------------------
def _grow_qfuds(ceff2: float, n_out: int = 2000):
    """
    Solve growth ODE for QFUDS background with effective sound speed ceff2.
    Clustering source: Ω_m + η·Ω_X  (Jeans proxy, not full perturbation theory).
    """
    n_eval = np.linspace(np.log(A_I), 0.0, n_out)

    def rhs(n, y):
        D, Dp = y
        a     = np.exp(n)
        E2    = _E_q(a)**2
        Om_c  = OM0 * a**-3 / E2 + _eta(a, ceff2) * _rhoX(a) / E2
        Dpp   = -(2.0 + _dlnE_dN_q(a)) * Dp + 1.5 * Om_c * D
        return [Dp, Dpp]

    sol = solve_ivp(rhs, (np.log(A_I), 0.0), [A_I, A_I],
                    t_eval=n_eval, method="LSODA", rtol=1e-8, atol=1e-12)
    a_out = np.exp(sol.t)
    D, Dp = sol.y[0], sol.y[1]
    f     = Dp / D   # f = dlnD/dlna
    return a_out, D, f


def _grow_lcdm(n_out: int = 2000):
    """Solve growth ODE for flat ΛCDM."""
    n_eval = np.linspace(np.log(A_I), 0.0, n_out)

    def _lnEl(lna):
        a = np.exp(lna)
        return 0.5 * np.log(M.OMEGA_M0_LCDM * a**-3 +
                             M.OMEGA_R0_LCDM * a**-4 +
                             M.OMEGA_L0_LCDM)

    def _dlnEl_dN(a, h: float = 5e-5) -> float:
        la = np.log(np.clip(a, 1e-6, None))
        return (_lnEl(la + h) - _lnEl(la - h)) / (2.0 * h)

    def rhs(n, y):
        D, Dp = y
        a  = np.exp(n)
        El2 = (M.OMEGA_M0_LCDM * a**-3 +
               M.OMEGA_R0_LCDM * a**-4 +
               M.OMEGA_L0_LCDM)
        Om  = M.OMEGA_M0_LCDM * a**-3 / El2
        Dpp = -(2.0 + _dlnEl_dN(a)) * Dp + 1.5 * Om * D
        return [Dp, Dpp]

    sol = solve_ivp(rhs, (np.log(A_I), 0.0), [A_I, A_I],
                    t_eval=n_eval, method="LSODA", rtol=1e-8, atol=1e-12)
    a_out = np.exp(sol.t)
    D, Dp = sol.y[0], sol.y[1]
    return a_out, D, Dp / D


def _make_fsig8_itp(a_out, D, f, D0_ref: float, z_max: float = 2.5):
    """
    Build a fσ8(z) interpolator.
    σ8(z=0) for this model = SIGMA8_LCDM * D(z=0) / D0_ref.
    """
    sigma8_0 = SIGMA8_LCDM * D[-1] / D0_ref
    fsig8    = f * (sigma8_0 * D / D[-1])
    z_out    = 1.0 / a_out - 1.0       # decreasing: large-z → 0
    mask     = z_out <= z_max
    # Reverse so z is increasing (required by interp1d)
    z_m  = z_out[mask][::-1]
    fs_m = fsig8[mask][::-1]
    itp  = interp1d(z_m, fs_m, kind="cubic", fill_value="extrapolate")
    return itp, float(sigma8_0)


# ---------------------------------------------------------------------------
# Representative RSD measurements (approximate; NOT for formal inference)
# Sources: 6dFGS, BOSS, eBOSS (published values; list is illustrative)
# ---------------------------------------------------------------------------
RSD_Z   = np.array([0.067, 0.15,  0.38,  0.51,  0.70,  0.85,  1.48])
RSD_FS8 = np.array([0.423, 0.490, 0.497, 0.459, 0.473, 0.315, 0.462])
RSD_ERR = np.array([0.055, 0.150, 0.045, 0.038, 0.041, 0.095, 0.045])


# ---------------------------------------------------------------------------
# Run growth computations
# ---------------------------------------------------------------------------
print("Solving ΛCDM growth ...")
a_l, D_l, f_l = _grow_lcdm()
D0_ref = D_l[-1]                       # ΛCDM D(z=0) — normalization anchor

print("Solving QFUDS growth, c_eff²=3×10⁻⁵  (S8-fit) ...")
a_q, D_q, f_q = _grow_qfuds(C_EFF2_FIT)

print("Solving QFUDS growth, c_eff²=1        (smooth reference) ...")
a_s, D_s, f_s = _grow_qfuds(1.0)

fsig8_l_itp, s8_l0 = _make_fsig8_itp(a_l, D_l, f_l, D0_ref)
fsig8_q_itp, s8_q0 = _make_fsig8_itp(a_q, D_q, f_q, D0_ref)
fsig8_s_itp, s8_s0 = _make_fsig8_itp(a_s, D_s, f_s, D0_ref)

# χ² against representative RSD points
pred_l = fsig8_l_itp(RSD_Z)
pred_q = fsig8_q_itp(RSD_Z)
chi2_l = float(np.sum(((RSD_FS8 - pred_l) / RSD_ERR)**2))
chi2_q = float(np.sum(((RSD_FS8 - pred_q) / RSD_ERR)**2))
ndof   = len(RSD_Z)

print(f"\nσ8(z=0):  ΛCDM={s8_l0:.4f}, QFUDS(3e-5)={s8_q0:.4f}, QFUDS(1)={s8_s0:.4f}")
print(f"fσ8 χ²:   ΛCDM={chi2_l:.2f},  QFUDS(3e-5)={chi2_q:.2f}   (N={ndof} pts, approx data)")

# QFUDS above or below ΛCDM?
print("\nfσ8(z) — ΛCDM vs QFUDS(c_eff²=3e-5):")
for zc in [0.067, 0.38, 0.70, 1.48]:
    fl = float(fsig8_l_itp(zc))
    fq = float(fsig8_q_itp(zc))
    tag = "ABOVE" if fq > fl else "BELOW"
    print(f"  z={zc:.3f}: ΛCDM={fl:.4f}  QFUDS={fq:.4f}  ({tag}, Δ={fq-fl:+.4f})")


# ---------------------------------------------------------------------------
# w(z) comparison: QFUDS (freezing) vs DESI DR2 CPL (thawing)
# ---------------------------------------------------------------------------
Z_GRID_DD = 1.0 / A_GRID - 1.0        # decreasing: large-z → 0
# Reverse to get strictly increasing z for interp1d
_mask_w = Z_GRID_DD <= 3.0
_z_w_rev  = Z_GRID_DD[_mask_w][::-1]
_wq_rev   = _w_dens_arr[_mask_w][::-1]
_w_itp    = interp1d(_z_w_rev, _wq_rev, kind="cubic", fill_value="extrapolate")

# DESI DR2 CPL best-fit (approximate central values, not official)
W0_DESI, WA_DESI = -0.7, -1.0
DW0, DWA         =  0.12,  0.35   # rough 1σ uncertainty


def w_cpl(z):
    a = 1.0 / (1.0 + np.asarray(z, dtype=float))
    return W0_DESI + WA_DESI * (1.0 - a)


def w_cpl_band(z):
    a   = 1.0 / (1.0 + np.asarray(z, dtype=float))
    wc  = W0_DESI + WA_DESI * (1.0 - a)
    sig = np.sqrt(DW0**2 + (DWA * (1.0 - a))**2)
    return wc - sig, wc + sig


print("\nw(z) at key redshifts — QFUDS (freezing) vs DESI-CPL (thawing):")
z_key = [0, 0.5, 1, 2]
for zc in z_key:
    wq = float(_w_itp(zc))
    wd = float(w_cpl(zc))
    print(f"  z={zc}: QFUDS w={wq:.3f},  DESI-CPL w={wd:.3f},  |Δw|={abs(wq-wd):.3f}")

z_scan = np.linspace(0, 2, 500)
dw_scan = np.abs(_w_itp(z_scan) - w_cpl(z_scan))
z_max_dw  = float(z_scan[np.argmax(dw_scan)])
max_dw    = float(dw_scan.max())
print(f"\nMax |Δw(z)| = {max_dw:.3f}  at z = {z_max_dw:.2f}")


# ---------------------------------------------------------------------------
# Falsification table
# ---------------------------------------------------------------------------
SEP = "=" * 95
print("\n" + SEP)
print("FALSIFICATION TABLE  (exploratory — NOT formal constraint)")
print(SEP)
col1, col2, col3, col4 = 22, 24, 25, 24
header = (f"{'Observable':<{col1}} {'Differs from ΛCDM?':<{col2}}"
          f"{'Magnitude / note':<{col3}} {'What would kill the model'}")
print(header)
print("-" * 95)

rows = [
    ("SNe μ(z)",
     "No",
     "<0.02 mag  (CP1 result)",
     "Cannot kill with SNe distances alone"),
    ("BAO D(z)",
     "No (same background)",
     "<0.5%  (same E(z))",
     "Cannot kill with BAO distances alone"),
    (f"fσ8(z) / RSD",
     "Yes — suppressed",
     (f"QFUDS χ²={chi2_q:.1f} vs"
      f" ΛCDM={chi2_l:.1f} (N={ndof})"),
     "Sub-5% fσ8 at z=0.5-1 (DESI+EUCLID)"),
    ("w(z) / DESI w0wa",
     "YES — opposite direction",
     (f"|Δw|≤{max_dw:.2f} (z≈{z_max_dw:.1f}),"
      " freezes vs thaws"),
     "Confirm wa<0 at 3σ — kills freezing model"),
    ("Late ISW",
     "Yes (qualitative)",
     "DE onset earlier; diff sign/amplitude",
     "CMB-galaxy cross-corr (z~0.5-1)"),
]

for obs, diff, mag, kill in rows:
    print(f"{obs:<{col1}} {diff:<{col2}} {mag:<{col3}} {kill}")

print(SEP)
print("VERDICT (on discriminability from ΛCDM):")
print("  Background (μ, BAO): NOT discriminable with current data.")
print(f"  fσ8(z): MARGINALLY discriminable — QFUDS χ²={chi2_q:.1f} vs ΛCDM={chi2_l:.1f}.")
print(f"  w(z): STRONGLY discriminable — max |Δw|={max_dw:.2f} at z={z_max_dw:.1f}.")
print("  MOST VULNERABLE: w(z) direction. Firming up DESI thawing (wa<0) at 3σ kills the model.")
print(SEP)


# ---------------------------------------------------------------------------
# Figure: two panels
# ---------------------------------------------------------------------------
fig, axes = plt.subplots(1, 2, figsize=(14, 5.5))

# --- Panel (a): fσ8(z) ---
ax = axes[0]
z_plt = np.linspace(0.0, 1.65, 300)
ax.plot(z_plt, fsig8_l_itp(z_plt),
        color="tab:blue", lw=2.2, label=f"ΛCDM  (χ²={chi2_l:.1f})")
ax.plot(z_plt, fsig8_q_itp(z_plt),
        color="tab:orange", lw=2.2,
        label=f"QFUDS c_eff²≈3×10⁻⁵, S8-fit  (χ²={chi2_q:.1f})")
ax.plot(z_plt, fsig8_s_itp(z_plt),
        color="tab:green", lw=1.5, ls="--",
        label="QFUDS c_eff²=1  (smooth, reference)")
ax.errorbar(RSD_Z, RSD_FS8, yerr=RSD_ERR,
            fmt="ko", ms=6, capsize=4, zorder=5,
            label="RSD data  (approximate / representative)")
ax.set_xlabel("redshift $z$", fontsize=12)
ax.set_ylabel(r"$f\sigma_8(z)$", fontsize=12)
ax.set_xlim(0, 1.7)
ax.set_ylim(0.15, 0.65)
ax.set_title(
    f"(a) $f\\sigma_8(z)$  —  ΛCDM χ²={chi2_l:.1f},  "
    f"QFUDS(c_eff²≈3×10⁻⁵) χ²={chi2_q:.1f}  (N={ndof})",
    fontsize=9.5)
ax.legend(fontsize=8.5, loc="upper right")
ax.grid(alpha=0.3)
ax.text(0.02, 0.02,
        "Data: approximate / representative only.\nNot for formal inference.",
        transform=ax.transAxes, fontsize=7, color="gray", style="italic")

# --- Panel (b): w(z) ---
ax2 = axes[1]
z_plt2 = np.linspace(0, 2, 400)
ax2.plot(z_plt2, _w_itp(z_plt2),
         color="tab:purple", lw=2.5,
         label="QFUDS density-driven  (FREEZING: w: 0→−1)")
ax2.plot(z_plt2, w_cpl(z_plt2),
         color="tab:red", lw=2.0,
         label=f"DESI DR2 CPL  (THAWING: w₀={W0_DESI}, wₐ={WA_DESI})")
wlo, whi = w_cpl_band(z_plt2)
ax2.fill_between(z_plt2, wlo, whi,
                 color="tab:red", alpha=0.18,
                 label="DESI ±1σ band  (rough approximation)")
ax2.axhline(-1.0, color="gray", ls=":", lw=1.0, label="$w=-1$  (ΛCDM)")
ax2.axvline(z_max_dw, color="k", ls="--", lw=0.9, alpha=0.55,
            label=f"Max |Δw| at z≈{z_max_dw:.1f}  (|Δw|={max_dw:.2f})")
ax2.set_xlabel("redshift $z$", fontsize=12)
ax2.set_ylabel("$w(z)$", fontsize=12)
ax2.set_xlim(0, 2)
ax2.set_ylim(-1.65, 0.25)
ax2.set_title(
    "(b) $w(z)$:  QFUDS freezing  vs  DESI-CPL thawing\n"
    f"Models are in OPPOSITE directions — max |Δw|={max_dw:.2f} at z≈{z_max_dw:.1f}",
    fontsize=9.5)
ax2.legend(fontsize=8.0, loc="lower right")
ax2.grid(alpha=0.3)
ax2.text(0.02, 0.02,
         "DESI band is rough 1σ estimate; not official contour.",
         transform=ax2.transAxes, fontsize=7, color="gray", style="italic")

fig.suptitle(
    "CP6b: Falsification — where QFUDS is discriminable from ΛCDM  "
    "[EXPLORATORY, NOT VALIDATED]",
    fontweight="bold", fontsize=10)
fig.tight_layout()
fig.savefig("fig_cp6b_falsification.png", dpi=130)
print("\nSaved fig_cp6b_falsification.png")
