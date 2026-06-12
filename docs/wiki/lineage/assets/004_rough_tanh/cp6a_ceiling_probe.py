"""
CP6a: Ceiling probe — do the tuned knobs collapse to one foam scale?

PURPOSE: Quantify (not resolve) the 050 ceiling.
  (1) A canonical scalar order parameter has c_eff²=1 by construction. Contrast
      with the CP5 result that S8≈0.76 requires c_eff²≈3e-5. Compute the S8
      each gives and the gap in orders of magnitude.
  (2) Test the single-scale hypothesis: if z* (critical density ρ*) is the ONE
      foam scale, do barrier and mobility collapse to specific natural values, or
      stay free? Produce an explicit knob count before vs after.

HONEST EXPECTED OUTCOME: the knobs do NOT collapse. c_eff²≈3e-5 is ~4.5 orders
below canonical and requires an independently tuned non-canonical kinetic term.
This re-confirms and QUANTIFIES the 050 ceiling.

STATUS: exploratory sandbox. Not evidence, not a roadmap change.
"""
from __future__ import annotations

import numpy as np
from scipy.integrate import solve_ivp
from scipy.interpolate import interp1d
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

import model as M
import density_driven as dd

# ---------------------------------------------------------------------------
# Reuse the CP5/CP3 background:  z*=5 → observed transition at z≈2
# ---------------------------------------------------------------------------
A = dd.A_GRID
N = dd.N_GRID
OM0 = M.OMEGA_M0_V2
OMR = M.OMEGA_R0
SIGMA8_LCDM = 0.81
S8_OBS = 0.76
A_I = 1e-3

C_KM_S = M.C_KM_S    # 299792 km/s
H0 = M.H0_CMB        # 67.4 km/s/Mpc
K8 = 0.2             # Mpc^-1, representative S8-scale wavenumber

_phi = dd.relax(z_star=5.0, barrier=2.0, mobility=2.0, lam=3.0)
_w = -_phi
E_DENS = dd.background_from_w(_w, OM0)
RHO_X = E_DENS**2 - OM0 * A**-3 - OMR * A**-4

lnE_spl = interp1d(np.log(A), np.log(E_DENS), kind="cubic", fill_value="extrapolate")
ln_rhox_spl = interp1d(np.log(A), np.log(np.clip(RHO_X, 1e-30, None)),
                       kind="cubic", fill_value="extrapolate")


def _E(a):       return np.exp(lnE_spl(np.log(a)))
def _rho_x(a):   return np.exp(ln_rhox_spl(np.log(a)))
def _dlnE_dN(a, h=1e-5):
    return (lnE_spl(np.log(a) + h) - lnE_spl(np.log(a) - h)) / (2 * h)


def eta(a: float, ceff2: float) -> float:
    """Jeans suppression factor (CP5 proxy): 1 = full clustering, 0 = smooth."""
    cs = np.sqrt(ceff2)
    R = cs * C_KM_S * K8 / (a * H0 * _E(a))
    return 1.0 / (1.0 + R**2)


def D1_growth(ceff2: float) -> float:
    """D(a=1) via linear growth ODE with effective Ω_clust = Ω_m + η Ω_X."""
    def rhs(n: float, y: list) -> list:
        D, Dp = y
        a = np.exp(n)
        Om = OM0 * a**-3 / _E(a)**2
        Ox = _rho_x(a) / _E(a)**2
        Om_clust = Om + eta(a, ceff2) * Ox
        Dpp = -(2.0 + _dlnE_dN(a)) * Dp + 1.5 * Om_clust * D
        return [Dp, Dpp]
    n0 = np.log(A_I)
    sol = solve_ivp(rhs, (n0, 0.0), [A_I, A_I],
                    t_eval=np.linspace(n0, 0.0, 1200),
                    method="LSODA", rtol=1e-8, atol=1e-12)
    return float(sol.y[0][-1])


def D1_lcdm() -> float:
    """ΛCDM reference D(a=1)."""
    def rhs_l(n: float, y: list) -> list:
        D, Dp = y
        a = np.exp(n)
        El = np.sqrt(M.OMEGA_M0_LCDM * a**-3 + M.OMEGA_R0_LCDM * a**-4 + M.OMEGA_L0_LCDM)
        h = 1e-5
        dl = (np.log(np.sqrt(M.OMEGA_M0_LCDM * np.exp(n + h)**-3
                              + M.OMEGA_R0_LCDM * np.exp(n + h)**-4 + M.OMEGA_L0_LCDM))
              - np.log(np.sqrt(M.OMEGA_M0_LCDM * np.exp(n - h)**-3
                               + M.OMEGA_R0_LCDM * np.exp(n - h)**-4 + M.OMEGA_L0_LCDM))) / (2 * h)
        Om = M.OMEGA_M0_LCDM * a**-3 / El**2
        return [Dp, -(2 + dl) * Dp + 1.5 * Om * D]
    sol = solve_ivp(rhs_l, (np.log(A_I), 0.0), [A_I, A_I],
                    t_eval=[0.0], method="LSODA", rtol=1e-8, atol=1e-12)
    return float(sol.y[0][-1])


def S8_from_D1(D1: float, D1_ref: float) -> float:
    sigma8 = SIGMA8_LCDM * D1 / D1_ref
    return sigma8 * np.sqrt(OM0 / 0.3)


# ---------------------------------------------------------------------------
# Knob-count analysis (purely logical, no computation)
# ---------------------------------------------------------------------------
KNOBS_BEFORE = [
    ("z*",      "trigger density / transition location"),
    ("Δa",      "transition width (phenomenological in CP1;\n"
                "  emergent in CP3 via barrier+M+lam)"),
    ("barrier", "Landau latent heat coefficient"),
    ("M",       "mobility / relaxation rate"),
    ("c_eff²",  "sound speed (kinetic structure)"),
]
# After fixing z* as the one foam scale:
KNOBS_AFTER = [
    ("z*",      "retained as THE foam energy scale"),
    ("barrier", "dimensionless Landau ratio — NOT fixed by z*"),
    ("M",       "dimensionless relaxation rate — NOT fixed by z*"),
    ("lam",     "dimensionless density coupling — NOT fixed by z*"),
    ("c_eff²",  "kinetic structure — completely independent of z*"),
]
# Δa is subsumed by z* in CP3 dynamics (1 collapse), but lam is now explicit.
# Net: 5 before → 5 after.  The single-scale assumption provides no reduction.


def main() -> None:
    print("CP6a: ceiling probe — do the knobs collapse to one foam scale?")
    print("=" * 65)

    # ------------------------------------------------------------------ #
    # 1.  Sound-speed gap: canonical vs required                           #
    # ------------------------------------------------------------------ #
    print("\n[1] SOUND SPEED: canonical scalar c_eff²=1 vs CP5-required")

    D1_ref = D1_lcdm()

    CEFF2_CANONICAL = 1.0     # canonical scalar: c_s² = 1 exactly
    CEFF2_REQUIRED  = 3.0e-5  # CP5 estimate; will refine below

    D1_can = D1_growth(CEFF2_CANONICAL)
    S8_can = S8_from_D1(D1_can, D1_ref)

    D1_req = D1_growth(CEFF2_REQUIRED)
    S8_req = S8_from_D1(D1_req, D1_ref)

    gap_orders = np.log10(CEFF2_CANONICAL / CEFF2_REQUIRED)

    print(f"  canonical  c_eff²=1.0  → S8 = {S8_can:.4f}  "
          f"({'above' if S8_can > S8_OBS else 'below'} observed {S8_OBS})")
    print(f"  required   c_eff²=3e-5 → S8 = {S8_req:.4f}  (CP5 target)")
    print(f"  gap:       {gap_orders:.1f} orders of magnitude in c_eff²")
    print()
    print("  Physical meaning: a CANONICAL scalar order parameter (L=X-V)")
    print("  has c_eff²=1 by the Christopherson-Malik theorem.  Achieving")
    print("  c_eff²≈3e-5 requires a non-canonical k-essence kinetic term")
    print("  K(X) with 2X·K_XX >> K_X — itself an independent fine-tune.")

    # Scan the S8(c_eff²) curve and find crossing
    ceff2_grid = np.logspace(-8, 0, 30)
    S8s = []
    for c2 in ceff2_grid:
        S8s.append(S8_from_D1(D1_growth(c2), D1_ref))
    S8s = np.array(S8s)

    cross = None
    for i in range(len(S8s) - 1):
        if (S8s[i] - S8_OBS) * (S8s[i + 1] - S8_OBS) <= 0:
            f = (S8_OBS - S8s[i]) / (S8s[i + 1] - S8s[i])
            cross = 10 ** (np.log10(ceff2_grid[i])
                           + f * (np.log10(ceff2_grid[i + 1]) - np.log10(ceff2_grid[i])))
            break

    if cross is not None:
        CEFF2_REQUIRED = cross
        D1_req = D1_growth(CEFF2_REQUIRED)
        S8_req = S8_from_D1(D1_req, D1_ref)
        gap_orders = np.log10(CEFF2_CANONICAL / CEFF2_REQUIRED)
        print(f"\n  Curve-interpolated crossing: c_eff² = {cross:.2e}  → S8 = {S8_req:.4f}")
        print(f"  Refined gap: {gap_orders:.1f} orders of magnitude")

    # ------------------------------------------------------------------ #
    # 2.  Knob-count: single-scale collapse check                          #
    # ------------------------------------------------------------------ #
    print("\n[2] KNOB COUNT: before vs after the single-scale (z*) assumption")
    print()
    print("  BEFORE  —  5 independently tuned parameters:")
    for k, desc in KNOBS_BEFORE:
        print(f"    {k:<10s}  {desc}")
    print()
    print("  SINGLE-SCALE ASSUMPTION: ρ* (i.e. z*) is the one foam scale.")
    print("  In Landau theory, the energy scale ρ* sets the transition location.")
    print("  But the dimensionless Landau coefficients {barrier, M, lam} are")
    print("  ratios of microscopic Hamiltonian parameters — they are NOT forced")
    print("  to specific values by knowing ρ*.  And c_eff² lives in the kinetic")
    print("  sector, entirely separate from the potential / location sector.")
    print()
    print("  AFTER   —  surviving free parameters:")
    for k, desc in KNOBS_AFTER:
        print(f"    {k:<10s}  {desc}")
    print()
    print("  Collapse accounting:")
    print("    Δa  (CP1 phenomenological width)  →  subsumed by z*+dynamics (CP3)")
    print("    barrier, M, lam, c_eff²           →  all REMAIN independent")
    print()
    print("  Net reduction: 1 knob (Δa → emergent), but lam is now explicit.")
    print("  Total: 5 before → 5 after.  Single-scale gives ZERO prediction power.")

    # ------------------------------------------------------------------ #
    # 3.  Verdict                                                          #
    # ------------------------------------------------------------------ #
    print("\n[3] VERDICT")
    print(f"  c_eff²(canonical) = 1.0  → S8 = {S8_can:.3f}")
    print(f"  c_eff²(required)  = {CEFF2_REQUIRED:.2e}  → S8 = {S8_req:.3f}")
    print(f"  Gap: {gap_orders:.1f} orders of magnitude; no foam mechanism bridges this.")
    print("  Knob count: 5 before, 5 after — single-scale collapses nothing new.")
    print("  CP6a does NOT cross the 050 ceiling.")

    # ------------------------------------------------------------------ #
    # 4.  Figure                                                           #
    # ------------------------------------------------------------------ #
    fig = plt.figure(figsize=(13.5, 5.8))
    gs = gridspec.GridSpec(1, 2, width_ratios=[2.3, 1.4], wspace=0.36)

    # --- Panel (a): S8 vs c_eff² ---
    ax = fig.add_subplot(gs[0])

    ax.semilogx(ceff2_grid, S8s, "o-", color="tab:purple", lw=1.8, ms=4,
                label="QFUDS density-driven (CP5 Jeans proxy)")
    ax.axhline(0.83, color="k", ls=":", lw=1.1, label="Planck ΛCDM S8 ≈ 0.83")
    ax.axhline(S8_OBS, color="tab:red", ls="--", lw=1.4, label=f"observed S8 ≈ {S8_OBS}")

    # Mark canonical point
    ax.plot(CEFF2_CANONICAL, S8_can, "s", color="tab:orange", ms=11, zorder=6)
    ax.annotate(
        f"canonical scalar\nc_eff²=1\nS8={S8_can:.3f}",
        xy=(CEFF2_CANONICAL, S8_can),
        xytext=(0.003, S8_can + 0.025),
        fontsize=8, color="tab:orange", fontweight="bold",
        arrowprops=dict(arrowstyle="->", color="tab:orange", lw=1.2),
    )

    # Mark required point
    ax.plot(CEFF2_REQUIRED, S8_req, "D", color="tab:green", ms=11, zorder=6)
    ax.annotate(
        f"S8-required\nc_eff²≈{CEFF2_REQUIRED:.1e}\nS8={S8_req:.3f}",
        xy=(CEFF2_REQUIRED, S8_req),
        xytext=(CEFF2_REQUIRED * 60, S8_req - 0.045),
        fontsize=8, color="tab:green", fontweight="bold",
        arrowprops=dict(arrowstyle="->", color="tab:green", lw=1.2),
    )

    # Gap annotation: double-headed arrow at y=0.705
    y_gap = 0.705
    ax.annotate(
        "",
        xy=(CEFF2_CANONICAL, y_gap),
        xytext=(CEFF2_REQUIRED, y_gap),
        arrowprops=dict(arrowstyle="<->", color="dimgray", lw=1.6),
    )
    x_mid = np.sqrt(CEFF2_REQUIRED * CEFF2_CANONICAL)
    ax.text(x_mid, y_gap + 0.007,
            f"~{gap_orders:.1f} orders of magnitude\n(canonical → required c_eff²)",
            ha="center", va="bottom", fontsize=8.5, color="dimgray",
            style="italic",
            bbox=dict(boxstyle="round,pad=0.2", facecolor="lightyellow", alpha=0.85))

    ax.set_xlabel("c_eff²  (effective sound speed² of dark component)", fontsize=10)
    ax.set_ylabel("S8", fontsize=10)
    ax.set_title("(a) S8 vs c_eff²: canonical scalar vs S8-required value",
                 fontweight="bold", fontsize=10)
    ax.legend(fontsize=8, loc="lower right")
    ax.grid(alpha=0.3)
    ax.set_ylim(0.67, 0.90)
    ax.set_xlim(1e-8, 3.0)

    # --- Panel (b): Knob count ---
    ax2 = fig.add_subplot(gs[1])
    ax2.axis("off")

    def txt(ax_obj, x, y, s, **kw):
        ax_obj.text(x, y, s, transform=ax_obj.transAxes, va="top", **kw)

    txt(ax2, 0.5, 0.98, "KNOB COUNT (CP6a)", ha="center",
        fontsize=10, fontweight="bold")

    txt(ax2, 0.03, 0.88, "BEFORE  (5 tuned):", ha="left",
        fontsize=9, fontweight="bold", color="tab:red")
    before_lines = [
        "  z*      — trigger density (ρ*)",
        "  Δa      — transition width",
        "  barrier — Landau latent heat",
        "  M       — relaxation rate",
        "  c_eff²  — sound speed",
    ]
    for i, line in enumerate(before_lines):
        txt(ax2, 0.03, 0.80 - i * 0.085, line, ha="left",
            fontsize=8, color="tab:red")

    txt(ax2, 0.03, 0.37, "AFTER single-scale z*  (5 tuned):", ha="left",
        fontsize=9, fontweight="bold", color="tab:blue")
    after_items = [
        ("z*",      "scale reference  [retained]",  "tab:gray"),
        ("barrier", "dimensionless ratio  [FREE]",   "tab:blue"),
        ("M",       "dimensionless ratio  [FREE]",   "tab:blue"),
        ("lam",     "density coupling   [FREE]",     "tab:blue"),
        ("c_eff²",  "kinetic sector  [INDEPENDENT]", "darkred"),
    ]
    for i, (k, desc, col) in enumerate(after_items):
        txt(ax2, 0.03, 0.29 - i * 0.082,
            f"  {k:<8s}— {desc}", ha="left", fontsize=8, color=col)

    # Summary box
    ax2.text(0.5, 0.03,
             "5 → 5 :  no knobs collapse under\n"
             "the single-scale assumption.\n"
             f"c_eff²≈{CEFF2_REQUIRED:.0e} needs {gap_orders:.1f} OOM of\n"
             "extra tuning vs canonical.\n"
             "050 CEILING: NOT CROSSED",
             transform=ax2.transAxes,
             ha="center", va="bottom", fontsize=8,
             color="darkred", fontweight="bold",
             bbox=dict(boxstyle="round,pad=0.4",
                       facecolor="mistyrose", edgecolor="darkred", alpha=0.9))

    # --- Suptitle ---
    fig.suptitle(
        "CP6a: ceiling probe — foam-scale collapse check  "
        "(exploratory; 050 ceiling NOT crossed)",
        fontweight="bold", fontsize=10,
    )

    fig.savefig("fig_cp6a_ceiling.png", dpi=130, bbox_inches="tight")
    print("\nsaved fig_cp6a_ceiling.png")


if __name__ == "__main__":
    main()
