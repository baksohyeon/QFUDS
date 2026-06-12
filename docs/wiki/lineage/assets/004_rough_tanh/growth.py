"""
growth.py — Linear matter-growth ODE & S8 test for QFUDS V2 vs ΛCDM.

EXPLORATORY PHENOMENOLOGY. NOT validated. Results describe what the rough
tanh-parameterised model gives numerically. Do not read as confirming or
denying QFUDS claims.
"""

from __future__ import annotations

import numpy as np
from scipy.interpolate import CubicSpline
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from model import (
    E_QFUDS_V2, E_LCDM,
    OMEGA_M0_V2, OMEGA_M0_LCDM,
)

# ---------------------------------------------------------------------------
# Parameters
# ---------------------------------------------------------------------------
A_I          = 1e-3    # start of integration (deep matter domination)
N_GRID       = 400     # tabulation grid size for E(a)
N_EVAL       = 2000    # ODE output evaluation points
SIGMA8_LCDM  = 0.81    # reference σ8 today for ΛCDM

# ---------------------------------------------------------------------------
# 1. Pre-tabulate E(a) on a log-spaced grid; build CubicSpline interpolators.
#    This avoids calling scipy.quad inside the stiff ODE solver.
# ---------------------------------------------------------------------------
a_grid = np.logspace(np.log10(A_I), 0.0, N_GRID)

print("Pre-tabulating E(a) for QFUDS V2 (scipy.quad per point, ~few s)...")
E_v2_grid   = np.array([float(E_QFUDS_V2(ai)) for ai in a_grid])
print("Pre-tabulating E(a) for LCDM...")
E_lcdm_grid = np.array([float(E_LCDM(ai))    for ai in a_grid])
print("Building CubicSpline interpolators...")

cs_v2   = CubicSpline(a_grid, E_v2_grid)
cs_lcdm = CubicSpline(a_grid, E_lcdm_grid)

# ---------------------------------------------------------------------------
# 2. Growth ODE (second-order, recast as first-order system)
#
#    D'' + (3/a + E'/E) D' - (3/2) Omega_m0 / (a^5 E^2) * D = 0
#
#    Only ordinary (clustering) matter enters the source term.
#    The transitioning X component is smooth (c_s=1); it enters E(a) but not
#    the gravity term.
# ---------------------------------------------------------------------------

def make_rhs(cs: CubicSpline, Omega_m0: float):
    """Return rhs(a, y) for solve_ivp using the pre-built CubicSpline for E."""
    def rhs(a: float, y):
        D, Dp = y
        E  = float(cs(a))
        Ep = float(cs(a, 1))               # dE/da via spline derivative
        p  = 3.0 / a + Ep / E              # friction coefficient
        q  = 1.5 * Omega_m0 / (a**5 * E**2)   # gravity source
        return [Dp, -p * Dp + q * D]
    return rhs

# Initial conditions: growing mode in matter domination (D ∝ a → D'=1)
y0     = [A_I, 1.0]
a_eval = np.linspace(A_I, 1.0, N_EVAL)

print("Solving growth ODE for LCDM...")
sol_lcdm = solve_ivp(
    make_rhs(cs_lcdm, OMEGA_M0_LCDM),
    t_span=(A_I, 1.0), y0=y0, method="DOP853",
    t_eval=a_eval, rtol=1e-10, atol=1e-13,
)
assert sol_lcdm.success, f"LCDM ODE solver failed: {sol_lcdm.message}"

print("Solving growth ODE for QFUDS V2...")
sol_v2 = solve_ivp(
    make_rhs(cs_v2, OMEGA_M0_V2),
    t_span=(A_I, 1.0), y0=y0, method="DOP853",
    t_eval=a_eval, rtol=1e-10, atol=1e-13,
)
assert sol_v2.success, f"V2 ODE solver failed: {sol_v2.message}"

a_arr   = sol_lcdm.t           # shape (N_EVAL,), increasing a_i → 1
D_lcdm  = sol_lcdm.y[0]
Dp_lcdm = sol_lcdm.y[1]        # dD/da
D_v2    = sol_v2.y[0]
Dp_v2   = sol_v2.y[1]

z_arr = 1.0 / a_arr - 1.0      # decreasing: ~999 → 0

# ---------------------------------------------------------------------------
# 3. Derived quantities
# ---------------------------------------------------------------------------
D_lcdm_today = D_lcdm[-1]
D_v2_today   = D_v2[-1]

# Growth ratio (both start with same D(a_i)); σ8 scales with this ratio.
ratio_D  = D_v2_today / D_lcdm_today
sigma8_v2 = SIGMA8_LCDM * ratio_D

# S8 = σ8 √(Ω_m0 / 0.3)
S8_lcdm = SIGMA8_LCDM * np.sqrt(OMEGA_M0_LCDM / 0.3)
S8_v2   = sigma8_v2   * np.sqrt(OMEGA_M0_V2   / 0.3)
dS8     = S8_v2 - S8_lcdm
dS8_pct = 100.0 * dS8 / S8_lcdm

# Growth rate  f(a) = d ln D / d ln a = a D'(a) / D(a)
f_lcdm = a_arr * Dp_lcdm / D_lcdm
f_v2   = a_arr * Dp_v2   / D_v2

# fσ8(a) = f(a) · σ8_today · D(a)/D(1)
fs8_lcdm = f_lcdm * SIGMA8_LCDM * D_lcdm / D_lcdm_today
fs8_v2   = f_v2   * sigma8_v2   * D_v2   / D_v2_today

# Interpolate at specific redshifts
def fs8_at_z(z_target: float, arr: np.ndarray) -> float:
    a_t = 1.0 / (1.0 + z_target)
    return float(np.interp(a_t, a_arr, arr))

fs8_lcdm_z0  = fs8_at_z(0.0, fs8_lcdm)
fs8_lcdm_z05 = fs8_at_z(0.5, fs8_lcdm)
fs8_v2_z0    = fs8_at_z(0.0, fs8_v2)
fs8_v2_z05   = fs8_at_z(0.5, fs8_v2)

# ---------------------------------------------------------------------------
# 4. Print report
# ---------------------------------------------------------------------------
verdict = (
    "LOWERS S8  -> supports the doc claim"
    if dS8 < 0 else
    "RAISES S8  -> contradicts the doc claim"
)

print()
print("=" * 64)
print("  QFUDS rough tanh -- linear growth & S8  (exploratory)")
print("=" * 64)
print(f"  D_V2(1) / D_LCDM(1)        = {ratio_D:.6f}")
print(f"  sigma8  LCDM               = {SIGMA8_LCDM:.4f}")
print(f"  sigma8  QFUDS V2           = {sigma8_v2:.4f}")
print(f"  S8      LCDM               = {S8_lcdm:.4f}")
print(f"  S8      QFUDS V2           = {S8_v2:.4f}")
print(f"  Delta_S8 (V2 - LCDM)       = {dS8:+.4f}  ({dS8_pct:+.2f}%)")
print(f"  VERDICT: z~2 transition {verdict}")
print()
print(f"  fsigma8(z=0)   LCDM={fs8_lcdm_z0:.4f}  V2={fs8_v2_z0:.4f}")
print(f"  fsigma8(z=0.5) LCDM={fs8_lcdm_z05:.4f}  V2={fs8_v2_z05:.4f}")
print("=" * 64)

# ---------------------------------------------------------------------------
# 5. Figure
# ---------------------------------------------------------------------------
fig = plt.figure(figsize=(12, 8))
fig.suptitle(
    "QFUDS rough tanh — linear growth & S8 (exploratory)",
    fontsize=13, fontweight="bold", y=0.99,
)

gs  = gridspec.GridSpec(2, 2, figure=fig, hspace=0.42, wspace=0.36)
ax_a = fig.add_subplot(gs[0, :])   # top full-width
ax_b = fig.add_subplot(gs[1, 0])   # bottom-left
ax_c = fig.add_subplot(gs[1, 1])   # bottom-right (text)

# --- Panel (a): D(a)/a vs a (log scale) ---
ax_a.plot(a_arr, D_lcdm / a_arr, color="steelblue",  lw=2,
          label=r"$\Lambda$CDM")
ax_a.plot(a_arr, D_v2   / a_arr, color="darkorange", lw=2, ls="--",
          label="QFUDS V2")
ax_a.axvline(0.33, color="gray", ls=":", lw=1.2, alpha=0.8,
             label=r"$a_{tr}=0.33$ (z$\approx$2)")
ax_a.set_xscale("log")
ax_a.set_xlim(A_I, 1.0)
ax_a.set_xlabel(r"scale factor $a$", fontsize=11)
ax_a.set_ylabel(r"$D(a)\,/\,a$", fontsize=11)
ax_a.set_title(r"(a) Linear growth factor (normalised by $a$; D/a$\to$const in matter dom.)",
               fontsize=10)
ax_a.legend(fontsize=10)

# --- Panel (b): fσ8 vs z ∈ [0, 2] ---
mask = (z_arr >= 0.0) & (z_arr <= 2.0)
ax_b.plot(z_arr[mask], fs8_lcdm[mask], color="steelblue",  lw=2,
          label=r"$\Lambda$CDM")
ax_b.plot(z_arr[mask], fs8_v2[mask],   color="darkorange", lw=2, ls="--",
          label="QFUDS V2")
ax_b.set_xlabel(r"redshift $z$", fontsize=11)
ax_b.set_ylabel(r"$f\sigma_8(z)$", fontsize=11)
ax_b.set_title(r"(b) $f\sigma_8(z)$", fontsize=10)
ax_b.set_xlim(0, 2)
ax_b.legend(fontsize=10)

# --- Panel (c): text summary ---
ax_c.axis("off")
summary = "\n".join([
    f"sigma8  LCDM  = {SIGMA8_LCDM:.4f}",
    f"sigma8  V2    = {sigma8_v2:.4f}",
    "",
    f"S8   LCDM     = {S8_lcdm:.4f}",
    f"S8   V2       = {S8_v2:.4f}",
    "",
    f"Delta_S8      = {dS8:+.4f}",
    f"Delta_S8 %    = {dS8_pct:+.1f}%",
    "",
    f"D_V2/D_LCDM   = {ratio_D:.4f}",
])
ax_c.text(0.05, 0.90, summary, transform=ax_c.transAxes,
          fontsize=9.5, va="top", fontfamily="monospace")

v_color = "green" if dS8 < 0.0 else "red"
v_short = ("LOWERS S8\n(supports doc claim)"
           if dS8 < 0.0 else
           "RAISES S8\n(contradicts doc claim)")
ax_c.text(0.05, 0.06, f"VERDICT:\n{v_short}",
          transform=ax_c.transAxes, fontsize=11,
          va="bottom", color=v_color, fontweight="bold")
ax_c.set_title("(c) sigma8 & S8 summary", fontsize=10)

out_path = "fig_growth.png"
fig.savefig(out_path, dpi=130, bbox_inches="tight")
print(f"Saved {out_path}")
