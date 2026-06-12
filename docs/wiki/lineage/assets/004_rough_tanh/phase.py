"""
phase.py — QFUDS rough tanh: phase portrait & DESI w0wa context.

STATUS: exploratory sandbox. Phenomenological only. No QFUDS validation claimed.

Produces fig_phase.png (4 panels):
  1. w_Q(a) and w_Q(z): tanh crossover 0→-1 centred at z≈2
  2. Ω_i(a): V1 unified density fractions (baryon, radiation, qfuds)
  3. log ρ_i(a)/ρ_crit,0: matter / radiation / Λ / V2 transitioning component
  4. DESI w0wa overlay: QFUDS tanh vs CPL (w0=-0.7, wa=-1.0) over z∈[0,2.5]
"""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from pathlib import Path

import model as M

# ──────────────────────────────────────────────────────────────────────────────
# Output path
# ──────────────────────────────────────────────────────────────────────────────
OUT = Path(__file__).parent / "fig_phase.png"

# ──────────────────────────────────────────────────────────────────────────────
# Grids
# ──────────────────────────────────────────────────────────────────────────────
N = 120  # points for heavy integrals
a_full = np.linspace(0.05, 1.0, N)
z_full = M.a_to_z(a_full)

# Panel 4 specific: z∈[0, 2.5]
z_desi = np.linspace(0.0, 2.5, 200)
a_desi = M.z_to_a(z_desi)

# ──────────────────────────────────────────────────────────────────────────────
# DESI-CPL parameterisation  w(a) = w0 + wa*(1-a)
# ──────────────────────────────────────────────────────────────────────────────
W0_DESI = -0.7
WA_DESI = -1.0

def w_cpl(a, w0=W0_DESI, wa=WA_DESI):
    return w0 + wa * (1.0 - a)

# ──────────────────────────────────────────────────────────────────────────────
# Numerical values reported to the orchestrator
# ──────────────────────────────────────────────────────────────────────────────
a_z2 = M.z_to_a(2.0)
a_z0 = 1.0

w_Q_z2 = float(M.w_Q(a_z2))
w_Q_z0 = float(M.w_Q(a_z0))
w_CPL_z2 = float(w_cpl(a_z2))
w_CPL_z0 = float(w_cpl(a_z0))

print("=" * 62)
print("QFUDS vs DESI-CPL  w-values  (exploratory)")
print("=" * 62)
print(f"  w_QFUDS  @ z=2 : {w_Q_z2:+.4f}   (a={a_z2:.4f})")
print(f"  w_QFUDS  @ z=0 : {w_Q_z0:+.4f}")
print(f"  w_CPL    @ z=2 : {w_CPL_z2:+.4f}  (w0={W0_DESI}, wa={WA_DESI})")
print(f"  w_CPL    @ z=0 : {w_CPL_z0:+.4f}")
print()
print("Regime comparison:")
print("  QFUDS tanh:  w evolves  0→-1  (matter→DE,  MORE negative over time)")
print("  DESI-CPL:    w evolves -1.7→-0.7  (phantom→quintessence, LESS negative over time)")
print("  At z=2: QFUDS≈-0.53, CPL≈-1.37  |  At z=0: QFUDS=-1.0, CPL=-0.7")
print("  → OPPOSITE direction of evolution; entirely different physical regimes.")
print("=" * 62)

# ──────────────────────────────────────────────────────────────────────────────
# Compute density arrays (slow integrals — cache results)
# ──────────────────────────────────────────────────────────────────────────────
print("Computing rho_Q (V1) …", end=" ", flush=True)
rho_Q = np.array([float(M.rho_Q_over_crit(ai)) for ai in a_full])
print("done")

print("Computing rho_X (V2) …", end=" ", flush=True)
rho_X = np.array([float(M.rho_X_over_crit(ai)) for ai in a_full])
print("done")

print("Computing omega fractions (V1) …", end=" ", flush=True)
fracs = M.omega_fractions_QFUDS(a_full)
print("done")

# Reference densities
rho_baryon = M.OMEGA_B0 * a_full ** -3
rho_rad    = M.OMEGA_R0 * a_full ** -4
rho_matter_lcdm = M.OMEGA_M0_LCDM * a_full ** -3
rho_lambda_lcdm = M.OMEGA_L0_LCDM * np.ones_like(a_full)

# ──────────────────────────────────────────────────────────────────────────────
# w_Q over full a-grid (and corresponding z for left/right axes)
# ──────────────────────────────────────────────────────────────────────────────
w_arr = M.w_Q(a_full)

# w(z) for DESI panel
w_Q_desi  = M.w_Q(a_desi)
w_CPL_arr = w_cpl(a_desi)

# ──────────────────────────────────────────────────────────────────────────────
# Figure setup
# ──────────────────────────────────────────────────────────────────────────────
fig, axes = plt.subplots(2, 2, figsize=(12, 9))
fig.suptitle(
    "QFUDS rough tanh — phase portrait & DESI w0wa context (exploratory)",
    fontsize=13, fontweight="bold", y=0.995
)

LABEL_FS = 9
TICK_FS  = 8
LEGEND_FS = 8

C_QFUDS  = "#2563EB"   # blue
C_CPL    = "#DC2626"   # red
C_BAR    = "#6D28D9"   # purple
C_RAD    = "#D97706"   # amber
C_LCDM_L = "#059669"  # green
C_MATTER = "#374151"   # dark grey
C_V2     = "#0891B2"   # cyan


# ══════════════════════════════════════════════════════════════════════════════
# Panel 1 (top-left): w_Q(a) and dual z-axis
# ══════════════════════════════════════════════════════════════════════════════
ax1 = axes[0, 0]

ax1.plot(a_full, w_arr, color=C_QFUDS, lw=2, label=r"$w_Q(a)$ QFUDS tanh")
ax1.axvline(M.A_TR, color="grey", ls="--", lw=1.2, label=f"$a_{{tr}}={M.A_TR}$ (z≈2)")
ax1.axvspan(M.A_TR - M.DELTA_A, M.A_TR + M.DELTA_A,
            alpha=0.12, color="grey", label=f"$\\Delta a={M.DELTA_A}$ transition width")
ax1.axhline(-1, color="black", ls=":", lw=0.9, label="w = −1 (Λ)")
ax1.axhline( 0, color="black", ls=":", lw=0.9, label="w = 0 (matter)")

ax1.set_xlabel("scale factor $a$", fontsize=LABEL_FS)
ax1.set_ylabel("$w_Q(a)$", fontsize=LABEL_FS)
ax1.set_xlim(0.05, 1.0)
ax1.set_ylim(-1.15, 0.15)
ax1.tick_params(labelsize=TICK_FS)
ax1.legend(fontsize=LEGEND_FS, loc="lower left")
ax1.set_title("Panel 1: Equation of state $w_Q(a)$", fontsize=10)

# Secondary x-axis showing redshift
ax1b = ax1.twiny()
z_ticks = [0, 0.5, 1, 2, 4, 9, 19]
a_ticks = [1.0 / (1 + z) for z in z_ticks]
ax1b.set_xlim(0.05, 1.0)
ax1b.set_xticks(a_ticks)
ax1b.set_xticklabels([str(z) for z in z_ticks], fontsize=TICK_FS)
ax1b.set_xlabel("redshift $z$", fontsize=LABEL_FS)


# ══════════════════════════════════════════════════════════════════════════════
# Panel 2 (top-right): Ω_i(a) V1 stacked area / line
# ══════════════════════════════════════════════════════════════════════════════
ax2 = axes[0, 1]

omega_bar = fracs["baryon"]
omega_rad = fracs["radiation"]
omega_q   = fracs["qfuds"]

ax2.stackplot(a_full,
              omega_rad, omega_bar, omega_q,
              labels=["radiation $\\Omega_r$", "baryons $\\Omega_b$", "QFUDS $\\Omega_Q$"],
              colors=[C_RAD, C_BAR, C_QFUDS],
              alpha=0.75)

ax2.axvline(M.A_TR, color="white", ls="--", lw=1.4)
ax2.text(M.A_TR + 0.015, 0.55, "$a_{tr}$", color="white", fontsize=8, va="center")

ax2.set_xlabel("scale factor $a$", fontsize=LABEL_FS)
ax2.set_ylabel("density fraction $\\Omega_i(a)$", fontsize=LABEL_FS)
ax2.set_xlim(0.05, 1.0)
ax2.set_ylim(0, 1)
ax2.tick_params(labelsize=TICK_FS)
ax2.legend(fontsize=LEGEND_FS, loc="upper left")
ax2.set_title("Panel 2: V1 unified density fractions $\\Omega_i(a)$", fontsize=10)

# annotate QFUDS dual nature
ax2.annotate("matter-like\n(w≈0)", xy=(0.12, 0.35), fontsize=7.5,
             color="white", ha="center", va="center")
ax2.annotate("DE-like\n(w≈−1)", xy=(0.82, 0.55), fontsize=7.5,
             color="white", ha="center", va="center")


# ══════════════════════════════════════════════════════════════════════════════
# Panel 3 (bottom-left): log ρ_i / ρ_crit,0  vs a
# ══════════════════════════════════════════════════════════════════════════════
ax3 = axes[1, 0]

ax3.semilogy(a_full, rho_matter_lcdm,  color=C_MATTER, lw=1.8, ls="-",  label=r"matter $\propto a^{-3}$")
ax3.semilogy(a_full, rho_rad,          color=C_RAD,    lw=1.8, ls="-",  label=r"radiation $\propto a^{-4}$")
ax3.semilogy(a_full, rho_lambda_lcdm,  color=C_LCDM_L, lw=1.8, ls="--", label=r"$\Lambda$ (const)")
ax3.semilogy(a_full, rho_X,            color=C_V2,     lw=2.2, ls="-",  label=r"V2 transitioning $\rho_X$")

# Reference a^-3 dashed guide for V2
# Normalise at a=0.05 to show the peel-away
a_guide = np.linspace(0.05, M.A_TR, 50)
rho_X_0 = float(M.rho_X_over_crit(a_full[0]))
rho_guide = rho_X_0 * (a_full[0] / a_guide) ** 3
ax3.semilogy(a_guide, rho_guide, color=C_V2, lw=1.1, ls=":", alpha=0.6,
             label=r"V2 extrapolated $a^{-3}$ guide")

ax3.axvline(M.A_TR, color="grey", ls="--", lw=1.2)
ax3.text(M.A_TR + 0.015, 2e-2, "$a_{tr}$", color="grey", fontsize=8)

ax3.set_xlabel("scale factor $a$", fontsize=LABEL_FS)
ax3.set_ylabel(r"$\rho_i(a)\,/\,\rho_{\rm crit,0}$", fontsize=LABEL_FS)
ax3.set_xlim(0.05, 1.0)
ax3.set_ylim(1e-4, 1e3)
ax3.tick_params(labelsize=TICK_FS)
ax3.legend(fontsize=LEGEND_FS, loc="upper right")
ax3.set_title("Panel 3: Density evolution — peel-away near $a_{tr}$", fontsize=10)


# ══════════════════════════════════════════════════════════════════════════════
# Panel 4 (bottom-right): DESI w0wa overlay over z∈[0, 2.5]
# ══════════════════════════════════════════════════════════════════════════════
ax4 = axes[1, 1]

ax4.plot(z_desi, w_Q_desi,  color=C_QFUDS, lw=2.2, label="QFUDS tanh $w_Q(z)$")
ax4.plot(z_desi, w_CPL_arr, color=C_CPL,   lw=2.2, ls="--",
         label=f"DESI-CPL $w_0={W0_DESI}$, $w_a={WA_DESI}$")

# Mark z=2 values
ax4.scatter([2.0], [w_Q_z2],   color=C_QFUDS, zorder=5, s=50)
ax4.scatter([2.0], [w_CPL_z2], color=C_CPL,   zorder=5, s=50)
ax4.annotate(f"QFUDS: {w_Q_z2:+.2f}", xy=(2.0, w_Q_z2),
             xytext=(2.15, w_Q_z2 + 0.12), fontsize=7.5, color=C_QFUDS,
             arrowprops=dict(arrowstyle="-", color=C_QFUDS, lw=0.8))
ax4.annotate(f"CPL: {w_CPL_z2:+.2f}", xy=(2.0, w_CPL_z2),
             xytext=(2.15, w_CPL_z2 - 0.12), fontsize=7.5, color=C_CPL,
             arrowprops=dict(arrowstyle="-", color=C_CPL, lw=0.8))

# Mark z=0 values
ax4.scatter([0.0], [w_Q_z0],   color=C_QFUDS, zorder=5, s=50, marker="D")
ax4.scatter([0.0], [w_CPL_z0], color=C_CPL,   zorder=5, s=50, marker="D")

ax4.axhline(-1, color="black", ls=":", lw=0.9, label="w = −1")
ax4.axhline( 0, color="black", ls=":", lw=0.9, label="w = 0")
ax4.axvline( 2, color="grey",  ls="--", lw=0.9, alpha=0.6)
ax4.text(2.05, 0.05, "z=2", fontsize=7.5, color="grey")

ax4.set_xlabel("redshift $z$", fontsize=LABEL_FS)
ax4.set_ylabel("$w(z)$", fontsize=LABEL_FS)
ax4.set_xlim(0, 2.5)
ax4.set_ylim(-2.0, 0.25)
ax4.tick_params(labelsize=TICK_FS)
ax4.legend(fontsize=LEGEND_FS, loc="lower right")
ax4.set_title("Panel 4: QFUDS vs DESI-CPL $w(z)$  (exploratory; NOT a fit)", fontsize=10)

# Honest note
ax4.text(0.02, 0.04,
         "Note: opposite sign of evolution.\n"
         "QFUDS: 0→−1 (freezing from matter).\n"
         "CPL: −1.7→−0.7 (thawing from phantom).\n"
         "These are DIFFERENT regimes.",
         transform=ax4.transAxes, fontsize=7, color="black",
         va="bottom", ha="left",
         bbox=dict(boxstyle="round,pad=0.3", fc="lightyellow", ec="grey", alpha=0.85))


# ──────────────────────────────────────────────────────────────────────────────
# Final layout & save
# ──────────────────────────────────────────────────────────────────────────────
fig.tight_layout(rect=[0, 0, 1, 0.97])
fig.savefig(OUT, dpi=130, bbox_inches="tight")
print(f"\nSaved: {OUT}  ({OUT.stat().st_size // 1024} kB)")
