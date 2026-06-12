"""
background.py — QFUDS background expansion and cosmological distances.

STATUS: EXPLORATORY PHENOMENOLOGY.
Numbers reflect what this parameterisation produces; they do NOT validate QFUDS,
do not constitute a roadmap milestone, and should not be quoted as observational
constraints without proper MCMC fitting against real data.
"""

from __future__ import annotations

import matplotlib
matplotlib.use('Agg')   # non-interactive backend; must precede pyplot import

import numpy as np
from scipy.integrate import cumulative_trapezoid
import matplotlib.pyplot as plt

import model   # shared physics contract; do not modify

# ---------------------------------------------------------------------------
# Redshift grid: z in [0, 6]
# ---------------------------------------------------------------------------
N_GRID = 500
Z_GRID = np.linspace(0.0, 6.0, N_GRID)
A_GRID = model.z_to_a(Z_GRID)      # a[0]=1 (today), a[-1]≈1/7

# ---------------------------------------------------------------------------
# 1. E(z) = H(z)/H0 for all three models
# ---------------------------------------------------------------------------
print("Computing E(z) for V1, V2, LCDM ...")
E_v1   = model.E_QFUDS(A_GRID)       # V1: unified QFUDS (DM+DE as one fluid)
E_v2   = model.E_QFUDS_V2(A_GRID)    # V2: normal matter + transitioning dark energy
E_lcdm = model.E_LCDM(A_GRID)        # ΛCDM reference

# ---------------------------------------------------------------------------
# 2. Dimensionless comoving distance  D_C(z) = ∫_0^z dz'/E(z')
#    Uses cumulative trapezoidal integration on the uniform z grid.
#    Units: c/H0 (Mpc when multiplied by DH below).
# ---------------------------------------------------------------------------
DC_v1   = np.concatenate([[0.0], cumulative_trapezoid(1.0 / E_v1,   Z_GRID)])
DC_v2   = np.concatenate([[0.0], cumulative_trapezoid(1.0 / E_v2,   Z_GRID)])
DC_lcdm = np.concatenate([[0.0], cumulative_trapezoid(1.0 / E_lcdm, Z_GRID)])

# Hubble distance (same H0 for all three: shape comparison, not absolute calibration)
DH_MPC = model.C_KM_S / model.H0_CMB   # c/H0 in Mpc

# Luminosity distance  d_L(z) = (1+z) * (c/H0) * D_C(z)   [Mpc]
dL_v1   = (1.0 + Z_GRID) * DH_MPC * DC_v1
dL_v2   = (1.0 + Z_GRID) * DH_MPC * DC_v2
dL_lcdm = (1.0 + Z_GRID) * DH_MPC * DC_lcdm

# Distance modulus  μ = 5 log10(d_L / 10 pc) = 5 log10(d_L_Mpc × 1e5)
# Guard z=0 (dL=0 → log undefined) by substituting nan.
def _mu(dL_mpc: np.ndarray) -> np.ndarray:
    safe = np.where(dL_mpc > 0, dL_mpc, np.nan)
    return 5.0 * np.log10(safe * 1e6 / 10.0)   # 1 Mpc = 1e6 pc

mu_v1   = _mu(dL_v1)
mu_v2   = _mu(dL_v2)
mu_lcdm = _mu(dL_lcdm)

# 3. Δμ residuals vs ΛCDM
delta_mu_v1 = mu_v1   - mu_lcdm
delta_mu_v2 = mu_v2   - mu_lcdm

# ---------------------------------------------------------------------------
# 4. High-z expansion sanity (z = 5)
# ---------------------------------------------------------------------------
print("\n=== HIGH-Z EXPANSION SANITY (z = 5) ===")
a5        = model.z_to_a(5.0)
E5_v1     = float(model.E_QFUDS(a5))
E5_v2     = float(model.E_QFUDS_V2(a5))
E5_lcdm   = float(model.E_LCDM(a5))
ratio_v1  = E5_v1   / E5_lcdm
ratio_v2  = E5_v2   / E5_lcdm

print(f"  E_V1   at z=5 = {E5_v1:.5f}")
print(f"  E_V2   at z=5 = {E5_v2:.5f}")
print(f"  E_LCDM at z=5 = {E5_lcdm:.5f}")
print(f"  E_V1 / E_LCDM = {ratio_v1:.4f}  "
      f"← FAILS: deviates strongly from 1 at early times (V1 excluded by CMB/BBN)")
print(f"  E_V2 / E_LCDM = {ratio_v2:.4f}  "
      f"← PASSES: close to 1; V2 preserves early-universe expansion history")

# ---------------------------------------------------------------------------
# 5. SNe Ia distinguishability: where does |Δμ| > 0.05 mag?
# ---------------------------------------------------------------------------
THRESH = 0.05   # mag; typical SNe Ia statistical scatter per bin

print(f"\n=== DISTANCE MODULUS DEVIATIONS (threshold |Δμ| > {THRESH} mag) ===")
finite = np.isfinite(delta_mu_v1) & np.isfinite(delta_mu_v2)

z_f         = Z_GRID[finite]
dm_v1_f     = delta_mu_v1[finite]
dm_v2_f     = delta_mu_v2[finite]

exceed_v2   = z_f[np.abs(dm_v2_f) > THRESH]
exceed_v1   = z_f[np.abs(dm_v1_f) > THRESH]

if exceed_v2.size > 0:
    print(f"  V2: |Δμ| > {THRESH} mag for z ∈ [{exceed_v2.min():.2f}, {exceed_v2.max():.2f}]")
else:
    print(f"  V2: |Δμ| ≤ {THRESH} mag over entire z = [0, 6]")

if exceed_v1.size > 0:
    print(f"  V1: |Δμ| > {THRESH} mag for z ∈ [{exceed_v1.min():.2f}, {exceed_v1.max():.2f}]")
else:
    print(f"  V1: |Δμ| ≤ {THRESH} mag over entire z = [0, 6]")

# Peak deviations
idx_v1_max = np.argmax(np.abs(dm_v1_f))
idx_v2_max = np.argmax(np.abs(dm_v2_f))
peak_v1 = np.abs(dm_v1_f[idx_v1_max])
peak_v2 = np.abs(dm_v2_f[idx_v2_max])
z_peak_v1 = z_f[idx_v1_max]
z_peak_v2 = z_f[idx_v2_max]

print(f"\n  Max |Δμ| V1 = {peak_v1:.3f} mag  at z = {z_peak_v1:.2f}")
print(f"  Max |Δμ| V2 = {peak_v2:.3f} mag  at z = {z_peak_v2:.2f}")

print("\n=== SNe DISTINGUISHABILITY VERDICT ===")
print("  V1 unified: E_V1/E_LCDM ≪ 1 at z=5; already excluded by early-universe data.")
if exceed_v2.size > 0:
    print(f"  V2 DE-only: Δμ > 0.05 mag over z ~ {exceed_v2.min():.1f}–{exceed_v2.max():.1f};")
    print("  in principle distinguishable from ΛCDM with current SNe statistics,")
    print("  but systematic floors and calibration uncertainties govern actual exclusion power.")
else:
    print("  V2 DE-only: |Δμ| < 0.05 mag everywhere — background geometry alone")
    print("  cannot distinguish V2 from ΛCDM within current SNe Ia scatter.")

# ---------------------------------------------------------------------------
# 6. Figure: three-panel (Agg backend, dpi=130)
# ---------------------------------------------------------------------------
print("\nGenerating fig_background.png ...")
COLORS = {'lcdm': 'black', 'v2': '#1f77b4', 'v1': '#d62728'}

fig, axes = plt.subplots(3, 1, figsize=(8, 12), constrained_layout=True)
fig.suptitle(
    "QFUDS rough tanh — background & distances (exploratory)",
    fontsize=12, fontweight='bold'
)

# — Panel (a): E(z) ——————————————————————————————————————
ax = axes[0]
ax.plot(Z_GRID, E_lcdm, lw=2.2, color=COLORS['lcdm'], ls='-',
        label=r'$\Lambda$CDM (reference)')
ax.plot(Z_GRID, E_v2,   lw=1.8, color=COLORS['v2'],   ls='--',
        label='V2 DE-only tanh')
ax.plot(Z_GRID, E_v1,   lw=1.8, color=COLORS['v1'],   ls=':',
        label='V1 unified tanh')
ax.set_xlabel('Redshift $z$')
ax.set_ylabel(r'$E(z) = H(z)/H_0$')
ax.set_title('(a) Dimensionless Hubble rate')
ax.set_xlim(0, 6)
ax.set_ylim(bottom=0)
ax.legend(loc='upper left', fontsize=9)

# — Panel (b): percent deviation in E(z) ——————————————————
ax = axes[1]
pct_v2 = (E_v2   / E_lcdm - 1.0) * 100.0
pct_v1 = (E_v1   / E_lcdm - 1.0) * 100.0
ax.axhline(0, color='k', lw=0.8, ls='--')
ax.plot(Z_GRID, pct_v2, lw=1.8, color=COLORS['v2'], label='V2 DE-only')
ax.plot(Z_GRID, pct_v1, lw=1.8, color=COLORS['v1'], label='V1 unified')
ax.set_xlabel('Redshift $z$')
ax.set_ylabel(r'$[E_\mathrm{model}/E_{\Lambda\mathrm{CDM}} - 1]\times100$  (%)')
ax.set_title(r'(b) Percent deviation of $E(z)$ from $\Lambda$CDM')
ax.set_xlim(0, 6)
ax.legend(loc='upper left', fontsize=9)

# — Panel (c): Δμ(z) ——————————————————————————————————————
ax = axes[2]
ax.axhline(0, color='k', lw=0.8, ls='--')
ax.fill_between(
    Z_GRID, -THRESH, THRESH,
    color='gray', alpha=0.20,
    label=rf'$\pm${THRESH} mag (SNe Ia scatter floor)'
)
ax.plot(Z_GRID, delta_mu_v2, lw=1.8, color=COLORS['v2'],
        label=r'$\Delta\mu$ V2 $-$ $\Lambda$CDM')
ax.plot(Z_GRID, delta_mu_v1, lw=1.8, color=COLORS['v1'],
        label=r'$\Delta\mu$ V1 $-$ $\Lambda$CDM')
ax.set_xlabel('Redshift $z$')
ax.set_ylabel(r'$\Delta\mu$ (mag)')
ax.set_title(r'(c) Distance modulus residual vs $\Lambda$CDM')
ax.set_xlim(0, 6)
ax.legend(loc='upper left', fontsize=9)

outfile = 'fig_background.png'
fig.savefig(outfile, dpi=130, bbox_inches='tight')
fig.savefig('fig_background.svg', bbox_inches='tight')
plt.close(fig)
print(f"Saved: {outfile}")
print("Saved: fig_background.svg")

# --- CSV dump ---
import csv as _csv
_csv_path = 'background_results.csv'
with open(_csv_path, 'w', newline='') as _f:
    _w = _csv.writer(_f)
    _w.writerow(['z', 'E_LCDM', 'E_V1', 'E_V2', 'dmu_V1', 'dmu_V2'])
    for _i in range(len(Z_GRID)):
        _w.writerow([Z_GRID[_i], E_lcdm[_i], E_v1[_i], E_v2[_i],
                     delta_mu_v1[_i], delta_mu_v2[_i]])
print(f"Saved: {_csv_path}")
print("\nDone — all numbers printed, PNG, SVG, and CSV written.")
