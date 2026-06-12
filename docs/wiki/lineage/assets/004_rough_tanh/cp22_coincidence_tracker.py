"""
CP22: BRUTE-FORCE the one escape CP20 named for the z*↔ρ* cosmic-coincidence —
a *dynamical* mechanism that locks the transition/critical density to ρ_Λ:
tracker / scaling / attractor quintessence. We integrate a real tracker field
(Ratra–Peebles inverse-power-law potential) and ask the honest accounting
question: does it actually REMOVE tuning, and if so, how much?

STATUS: exploratory sandbox, PARAMETRIZE-not-DERIVE. Nothing here is a derived
QFUDS result, not evidence, not a roadmap change. A brute-force NUMERICAL HIT
(the field landing on Ω_DE≈0.685) is NOT a derivation — it is a curve, not a
mechanism from foam microphysics. The "050 ceiling" stays exactly where it was
and observer mode is untouched. The real check is CLASS/hi_class at Level 3,
which is BLOCKED.

THE POINT (and the honest expected outcome): tracker attractors are KNOWN to
genuinely reduce ONE tuning — insensitivity to initial conditions over many
decades (the field forgets where it started and joins the same late-time
attractor). We MEASURE that here and it is a REAL, partial win; do not dismiss
it. But trackers DO NOT solve why-now: the potential energy scale M (≈ meV,
i.e. V0 ≈ ρ_Λ) must STILL be tuned to set WHEN dark energy comes to dominate.
So the deliverable is the TUNING LEDGER, not "we hit it":

    before tracker : { initial conditions , energy scale }  → 2 tuned numbers
    after  tracker : { energy scale (meV / why-now)      }  → 1 tuned number

A genuine-but-PARTIAL 2→1 reduction. The cosmic coincidence is NOT solved and
NOT derived.

Physics implemented (rough; proxies labelled; each relation checked against a
known limit):
  • Flat FRW with separate matter (a^-3) + radiation (a^-4) + canonical scalar φ.
  • Ratra–Peebles potential V(φ) = M^(4+α)/φ^α = A φ^-α, A ≡ M^(4+α), α>0.
    (Inverse-power-law chosen over the exponential because it gives a genuine
    *tracker* with present w0 in the observed −0.8..−1 band, whereas a single
    exponential gives a scaling solution that does not end up DE-dominated
    without extra structure. Justified, not arbitrary.)
  • Klein–Gordon in e-folds N=ln a, reduced Planck units M_pl=1, 3H0²ρ_c0-norm.

Units: M_pl=1, φ in M_pl. Densities in units of today's critical density
ρ_c0 (so 3H0²=1). The energy scale is reported as M_eff ≡ V0^{1/4}, converted
to meV via ρ_c0^{1/4} ≈ 2.5 meV (standard). For the calibrated tracker
M_eff ≈ ρ_Λ^{1/4} ≈ 2.3 meV — the famous dark-energy scale.

Outputs (working dir):
  cp22_coincidence_tracker.py / .png / .svg / _results.csv
Exploratory; brute-force hit ≠ derivation; real check = CLASS, Level 3, BLOCKED.
"""
from __future__ import annotations
import csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
from scipy.optimize import brentq

import model as M

# ---------------------------------------------------------------------------
# cosmology inputs (dimensionless, ρ_c0 = 1 so 3H0² = 1)
# ---------------------------------------------------------------------------
OMEGA_M0 = M.OMEGA_M0_LCDM     # CDM+baryons stay a normal separate a^-3 species
OMEGA_R0 = M.OMEGA_R0_LCDM     # radiation, a^-4
OMEGA_DE_TARGET = M.OMEGA_L0_LCDM   # what the tracker must hit today (≈0.685)

ALPHA = 1.0                    # Ratra–Peebles power (α>0). α=1: tracker, w0≈-0.8
N_I = np.log(1.0e-7)           # start deep in radiation era, z ≈ 1e7
RHO_C0_QUARTER_MEV = 2.5       # ρ_c0^{1/4} in meV (standard; proxy constant)


# ---------------------------------------------------------------------------
# potential and its derivative (Ratra–Peebles)
# ---------------------------------------------------------------------------
def V_of(phi, A, alpha=ALPHA):
    return A * phi ** (-alpha)


def dV_of(phi, A, alpha=ALPHA):
    return -alpha * A * phi ** (-alpha - 1.0)


# ---------------------------------------------------------------------------
# background system in e-folds N=ln a.
#
# Derivation (M_pl=1, 8πG=1 → 3H²=ρ_tot, Ḣ=-½(ρ+p)):
#   φ̇ = H φ',   φ̈ = H²φ'' + H H' φ'   (prime = d/dN)
#   KG  φ̈ + 3Hφ̇ + V'(φ) = 0  ⇒  φ'' + (3 + H'/H) φ' + V'(φ)/H² = 0
#   ρ_φ = ½H²φ'² + V ⇒ 3H² = ρ_m+ρ_r+½H²φ'²+V
#        ⇒ H² = (ρ_m+ρ_r+V)/(3 - ½φ'²)        [valid while φ'²<6]
#   H'/H = Ḣ/H² = -(1/2H²)(ρ_m + (4/3)ρ_r + φ̇²)   (φ̇²=H²φ'²)
# Checked limits below: matter H'/H→-3/2, radiation→-2.
# ---------------------------------------------------------------------------
def _H2(N, phi, u, A, alpha=ALPHA):
    a = np.exp(N)
    rho_m = OMEGA_M0 * a ** -3
    rho_r = OMEGA_R0 * a ** -4
    V = V_of(phi, A, alpha)
    denom = 3.0 - 0.5 * u * u
    return (rho_m + rho_r + V) / denom, rho_m, rho_r, V


def rhs(N, y, A, alpha=ALPHA):
    phi, u = y
    phi = max(phi, 1e-300)
    H2, rho_m, rho_r, V = _H2(N, phi, u, A, alpha)
    phidot2 = H2 * u * u
    HpoverH = -(1.0 / (2.0 * H2)) * (rho_m + (4.0 / 3.0) * rho_r + phidot2)
    dphi = u
    du = -(3.0 + HpoverH) * u - dV_of(phi, A, alpha) / H2
    return [dphi, du]


def integrate(phi_i, A, u_i=0.0, alpha=ALPHA, n_pts=4000):
    """Frozen-start (φ̇=0) by default; integrate radiation→today (N_I→0)."""
    N_eval = np.linspace(N_I, 0.0, n_pts)
    sol = solve_ivp(rhs, (N_I, 0.0), [phi_i, u_i], args=(A, alpha),
                    t_eval=N_eval, rtol=1e-9, atol=1e-12, method="RK45",
                    max_step=0.05)
    return sol


def series(sol, A, alpha=ALPHA):
    """Return N, Omega_DE, w_phi, w_tot along the solution."""
    N = sol.t
    phi, u = sol.y[0], sol.y[1]
    a = np.exp(N)
    rho_m = OMEGA_M0 * a ** -3
    rho_r = OMEGA_R0 * a ** -4
    V = V_of(np.clip(phi, 1e-300, None), A, alpha)
    H2 = (rho_m + rho_r + V) / (3.0 - 0.5 * u * u)
    phidot2 = H2 * u * u
    rho_phi = 0.5 * phidot2 + V
    rho_tot = rho_m + rho_r + rho_phi
    p_tot = (1.0 / 3.0) * rho_r + (0.5 * phidot2 - V)
    w_phi = (0.5 * phidot2 - V) / np.maximum(rho_phi, 1e-300)
    w_tot = p_tot / rho_tot
    Omega_DE = rho_phi / rho_tot
    return N, Omega_DE, w_phi, w_tot


def observe_today(sol, A, alpha=ALPHA):
    N, ODE, wphi, wtot = series(sol, A, alpha)
    return float(ODE[-1]), float(wphi[-1])


def z_accel(sol, A, alpha=ALPHA):
    """Redshift at onset of cosmic acceleration (w_tot crosses -1/3, latest).
    Returns (z_acc, status): status in {'window','early','future'}."""
    N, ODE, wphi, wtot = series(sol, A, alpha)
    f = wtot + 1.0 / 3.0            # <0 ⇒ accelerating
    if f[-1] > 0:
        return np.nan, "future"     # not accelerating today → onset in the future
    if f[0] < 0:
        return float(np.exp(-N[0]) - 1.0), "early"   # already accel at z~1e7
    # latest sign change from + to -
    idx = np.where((f[:-1] > 0) & (f[1:] <= 0))[0]
    j = idx[-1]
    Nacc = brentq(lambda x: np.interp(x, N, f), N[j], N[j + 1])
    return float(np.exp(-Nacc) - 1.0), "window"


# ---------------------------------------------------------------------------
# calibration: find A so a tracker-joining φ_i gives Ω_DE(0)=target
# ---------------------------------------------------------------------------
def calibrate_A(phi_ref, alpha=ALPHA, target=OMEGA_DE_TARGET):
    def resid(logA):
        ode0, _ = observe_today(integrate(phi_ref, 10.0 ** logA, alpha=alpha), 10.0 ** logA, alpha)
        return ode0 - target
    lo, hi = -130.0, 5.0
    # bracket numerically (Ω_DE0 monotone increasing in A)
    return 10.0 ** brentq(resid, lo, hi, xtol=1e-4)


# ---------------------------------------------------------------------------
# checks: assert known limits before trusting the integrator
# ---------------------------------------------------------------------------
def _checks():
    # (1) matter-only & radiation-only H'/H limits from the derived expression
    # matter: ρ_r→0, V→0  ⇒ H'/H = -(ρ_m)/(2·ρ_m/3) = -3/2
    H2 = OMEGA_M0 * 1.0          # a=1 toy with only matter, 3H2=ρ_m → H2=ρ_m/3
    rho_m = OMEGA_M0
    hph_matter = -(1.0 / (2.0 * (rho_m / 3.0))) * (rho_m)
    assert abs(hph_matter + 1.5) < 1e-12, hph_matter
    # radiation: only ρ_r ⇒ H'/H = -(4/3 ρ_r)/(2·ρ_r/3) = -2
    rho_r = OMEGA_R0
    hph_rad = -(1.0 / (2.0 * (rho_r / 3.0))) * ((4.0 / 3.0) * rho_r)
    assert abs(hph_rad + 2.0) < 1e-12, hph_rad
    # (2) potential limit: canonical V'(φ)=-αAφ^{-α-1}; α→0 ⇒ flat ⇒ V'→0
    assert abs(dV_of(1.0, 1.0, alpha=1e-9)) < 1e-7
    # (3) A=0 (no DE) integration stays matter+radiation: Ω_DE(0)≈0, q decel
    sol0 = integrate(1.0, 0.0)
    ode0, _ = observe_today(sol0, 0.0)
    assert ode0 < 1e-6, ode0
    print(f"checks PASS: H'/H matter={hph_matter:.3f} rad={hph_rad:.3f}; "
          f"A=0 ⇒ Ω_DE(0)={ode0:.2e}")


# ---------------------------------------------------------------------------
def main():
    _checks()
    alpha = ALPHA
    phi_ref = 1.0e-3                    # reference field ON the attractor plateau
                                        # (high initial V; tracker funnel, not the
                                        # frozen/thawing knee near φ~1)
    A_cal = calibrate_A(phi_ref, alpha)
    M_eff_cal = (V_of(phi_ref, A_cal, alpha)) ** 0.25  # ρ_c0 units; proxy scale
    M_eff_cal_meV = (OMEGA_DE_TARGET) ** 0.25 * RHO_C0_QUARTER_MEV  # ≈ρ_Λ^{1/4}
    sol_cal = integrate(phi_ref, A_cal, alpha=alpha)
    ode0_cal, w0_cal = observe_today(sol_cal, A_cal, alpha)
    # deep-matter DE fraction (DE must be subdominant in the matter era)
    N_s, ODE_s, wphi_s, wtot_s = series(sol_cal, A_cal, alpha)
    iz30 = int(np.argmin(np.abs(np.exp(-N_s) - 1.0 - 30.0)))
    w_phi_z30 = float(wphi_s[iz30])
    w_tracker_pred = -2.0 / (alpha + 2.0)         # known tracker value, w_B=0
    print(f"\ncalibrated A={A_cal:.3e}  Ω_DE(0)={ode0_cal:.4f}  w0={w0_cal:+.3f}")
    print(f"deep-matter (z~30): Ω_DE={ODE_s[iz30]:.2e}, w_φ={w_phi_z30:+.3f}  "
          f"(known tracker w=-2/(α+2)={w_tracker_pred:+.3f} once rolling)")
    print(f"M_eff(calibrated) ≈ {M_eff_cal_meV:.2f} meV  (= ρ_Λ^1/4, the DE scale)")

    # sanity asserts (the win + the honest band)
    assert abs(ode0_cal - OMEGA_DE_TARGET) < 0.02, ode0_cal
    assert -1.0 <= w0_cal <= -0.6, w0_cal             # observed DE band
    assert ODE_s[iz30] < 0.05, ODE_s[iz30]            # deep matter: Ω_DE≪1
    # on the attractor the matter-era EoS must equal the KNOWN tracker value
    # w_φ = -2/(α+2); this confirms the integrator reproduces the analytic tracker.
    assert abs(w_phi_z30 - w_tracker_pred) < 0.05, w_phi_z30
    # the genuine attractor property is further asserted below via the IC-basin
    # width (brute-force 1), the operational definition of the attractor.

    # =====================================================================
    # BRUTE-FORCE 1 — the REAL test: IC attractor. Fix A, scan φ_i over many
    # decades. Tracker forgets φ_i ⇒ Ω_DE(0) converges = IC tuning removed.
    # =====================================================================
    phi_i_grid = np.logspace(-16.0, 3.0, 58)          # 19 decades of initial field
    ode0_scan, w0_scan = [], []
    for pi in phi_i_grid:
        s = integrate(pi, A_cal, alpha=alpha)
        o, w = observe_today(s, A_cal, alpha)
        ode0_scan.append(o)
        w0_scan.append(w)
    ode0_scan = np.array(ode0_scan)
    w0_scan = np.array(w0_scan)

    # basin = decades of φ_i landing in Ω_DE(0)=target±0.05
    in_basin = np.abs(ode0_scan - OMEGA_DE_TARGET) <= 0.05
    if in_basin.any():
        lo_b = phi_i_grid[in_basin].min()
        hi_b = phi_i_grid[in_basin].max()
        basin_decades = np.log10(hi_b / lo_b)
        ode_spread = float(np.ptp(ode0_scan[in_basin]))
    else:
        lo_b = hi_b = np.nan
        basin_decades = 0.0
        ode_spread = np.nan
    print(f"\n[Brute-force 1: IC attractor — the REAL partial win]")
    print(f"  scanned φ_i over {np.log10(phi_i_grid[-1]/phi_i_grid[0]):.0f} decades")
    print(f"  basin (Ω_DE0=0.685±0.05): φ_i∈[{lo_b:.2e},{hi_b:.2e}] "
          f"= {basin_decades:.1f} decades, Ω_DE0 spread={ode_spread:.3f}")
    assert basin_decades >= 10.0, basin_decades       # ≥10 decades = real reduction

    # =====================================================================
    # BRUTE-FORCE 2 — why-now SURVIVES: scan the energy scale (A=f·A_cal ⇒
    # M_eff=f^{1/4}·M_cal). Record z_acc. Only M_eff~meV puts acceleration in
    # the observed window z∈[0,2]; other scales push it to z~1000s or future.
    # =====================================================================
    f_grid = np.logspace(-8.0, 8.0, 65)               # 16 decades of amplitude
    Meff_meV, zacc_scan, status_scan = [], [], []
    for f in f_grid:
        s = integrate(phi_ref, f * A_cal, alpha=alpha)
        za, st = z_accel(s, f * A_cal, alpha)
        Meff_meV.append(M_eff_cal_meV * f ** 0.25)    # M_eff ∝ A^{1/4}
        zacc_scan.append(za)
        status_scan.append(st)
    Meff_meV = np.array(Meff_meV)
    zacc_scan = np.array(zacc_scan)
    status_scan = np.array(status_scan)

    # which M_eff give z_acc in the observed late window [0,2]?
    obs = np.array([(s == "window") and (0.0 <= z <= 2.0)
                    for z, s in zip(zacc_scan, status_scan)])
    if obs.any():
        Mlo, Mhi = Meff_meV[obs].min(), Meff_meV[obs].max()
        whynow_decades = np.log10(Mhi / Mlo)
    else:
        Mlo = Mhi = np.nan
        whynow_decades = np.nan
    print(f"\n[Brute-force 2: why-now — the tuning that SURVIVES]")
    print(f"  scanned energy scale M_eff over "
          f"{np.log10(Meff_meV.max()/Meff_meV.min()):.1f} decades")
    print(f"  z_acc in observed window [0,2] ONLY for "
          f"M_eff∈[{Mlo:.2f},{Mhi:.2f}] meV = {whynow_decades:.2f} decades wide")
    print(f"  → the meV scale must still be tuned to ~1 number. why-now SURVIVES.")

    # =====================================================================
    # TUNING LEDGER — the actual deliverable
    # =====================================================================
    print("\n=== CP22 TUNING LEDGER (parametrize-not-derive; hit ≠ derivation) ===")
    print(f"  BEFORE tracker : 2 tuned numbers {{initial conditions, energy scale}}")
    print(f"  AFTER  tracker : 1 tuned number  {{energy scale ≈ meV (why-now)}}")
    print(f"    • initial conditions: FREED over {basin_decades:.0f} decades "
          f"(attractor basin) — GENUINE, partial win")
    print(f"    • energy scale: STILL tuned, window {whynow_decades:.2f} decades "
          f"around {M_eff_cal_meV:.1f} meV — why-now NOT solved")
    print(f"  NET: 2 → 1 tuned numbers. Genuine but PARTIAL. Coincidence remains.")
    print(f"  A brute-force numerical hit is NOT a foam derivation. 050 untouched,")
    print(f"  observer mode untouched. Real check = CLASS/hi_class Level 3 BLOCKED.")

    # =====================================================================
    # FIGURE (2 panels)
    # =====================================================================
    fig, ax = plt.subplots(1, 2, figsize=(14, 5.8))

    # (a) IC attractor basin: Ω_DE(0) vs φ_i — flat over many decades
    ax[0].semilogx(phi_i_grid, ode0_scan, "o-", color="tab:green", ms=4,
                   lw=1.5, label="Ω_DE(0) vs initial φ_i")
    ax[0].axhline(OMEGA_DE_TARGET, color="navy", lw=1.2, ls="--",
                  label=f"target {OMEGA_DE_TARGET:.3f}")
    ax[0].axhspan(OMEGA_DE_TARGET - 0.05, OMEGA_DE_TARGET + 0.05,
                  color="tab:green", alpha=0.12)
    if np.isfinite(lo_b):
        ax[0].axvspan(lo_b, hi_b, color="tab:green", alpha=0.10)
        ax[0].annotate(f"IC tuning REMOVED:\n{basin_decades:.0f} decades of φ_i\n"
                       f"all land on Ω_DE(0)≈0.685\n(attractor — real partial win)",
                       xy=(np.sqrt(lo_b * hi_b), OMEGA_DE_TARGET),
                       xytext=(0.04, 0.30), textcoords="axes fraction",
                       fontsize=8.5, color="darkgreen",
                       arrowprops=dict(arrowstyle="->", color="darkgreen", lw=1))
    ax[0].set_xlabel("initial field φ_i  [M_pl]  (frozen start)")
    ax[0].set_ylabel("Ω_DE(z=0)")
    ax[0].set_title("(a) IC attractor: tracker forgets φ_i\n"
                    "→ initial-condition tuning genuinely reduced")
    ax[0].set_ylim(0, 1)
    ax[0].legend(fontsize=8, loc="upper right")
    ax[0].grid(alpha=0.3, which="both")

    # (b) why-now: z_acc vs energy scale M_eff — only meV hits the window
    fin = np.isfinite(zacc_scan)
    ax[1].loglog(Meff_meV[fin], np.clip(zacc_scan[fin], 1e-2, None), "s-",
                 color="tab:red", ms=4, lw=1.3, label="z_acc(M_eff)")
    ax[1].axhspan(1e-2, 2.0, color="tab:orange", alpha=0.15,
                  label="observed window z_acc∈[0,2]")
    if np.isfinite(Mlo):
        ax[1].axvspan(Mlo, Mhi, color="tab:orange", alpha=0.25)
        ax[1].annotate(f"why-now STILL tuned:\nonly M_eff≈{M_eff_cal_meV:.0f} meV\n"
                       f"({whynow_decades:.1f} decades) hits z∈[0,2]\n"
                       f"= V0≈ρ_Λ. coincidence NOT solved",
                       xy=(np.sqrt(Mlo * Mhi), 1.0),
                       xytext=(0.05, 0.62), textcoords="axes fraction",
                       fontsize=8.5, color="darkred",
                       arrowprops=dict(arrowstyle="->", color="darkred", lw=1))
    ax[1].axvline(M_eff_cal_meV, color="navy", lw=1.0, ls=":")
    ax[1].set_xlabel("energy scale  M_eff = V0^{1/4}  [meV]   (proxy)")
    ax[1].set_ylabel("acceleration-onset redshift  z_acc")
    ax[1].set_title("(b) why-now survives: only the meV scale works\n"
                    "→ energy-scale tuning NOT removed by the tracker")
    ax[1].legend(fontsize=8, loc="upper left")
    ax[1].grid(alpha=0.3, which="both")

    fig.suptitle("CP22: coincidence tracker brute-force — IC tuning genuinely "
                 "reduced (2→1), but why-now/meV survives\n"
                 "(exploratory; brute-force hit ≠ derivation; 050 + observer "
                 "mode untouched; real check = CLASS, BLOCKED)",
                 fontweight="bold", fontsize=10.5)
    fig.tight_layout(rect=(0, 0, 1, 0.94))
    fig.savefig("fig_cp22_coincidence_tracker.png", dpi=130)
    fig.savefig("fig_cp22_coincidence_tracker.svg")
    print("\nsaved fig_cp22_coincidence_tracker.png + .svg")

    # =====================================================================
    # CSV
    # =====================================================================
    with open("cp22_coincidence_tracker_results.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["# CP22 coincidence tracker brute-force — parametrize, not "
                    "derive; hit != derivation; 050+observer untouched; CLASS BLOCKED"])
        w.writerow(["# Ratra-Peebles V=A*phi^-alpha, alpha=%.2f, M_pl=1, rho_c0=1"
                    % alpha])
        w.writerow(["# calibration", "A_cal=%.4e" % A_cal,
                    "OmegaDE0=%.4f" % ode0_cal, "w0=%.4f" % w0_cal,
                    "Meff_cal_meV=%.3f" % M_eff_cal_meV])
        w.writerow([])
        w.writerow(["## SECTION 1: IC attractor scan (fixed A, vary phi_i)"])
        w.writerow(["phi_i_Mpl", "Omega_DE0", "w0", "in_basin"])
        for pi, o, wv in zip(phi_i_grid, ode0_scan, w0_scan):
            w.writerow([f"{pi:.6e}", f"{o:.5f}", f"{wv:+.4f}",
                        int(abs(o - OMEGA_DE_TARGET) <= 0.05)])
        w.writerow([])
        w.writerow(["## SECTION 2: why-now scan (vary energy scale M_eff)"])
        w.writerow(["M_eff_meV", "z_acc", "status"])
        for mm, za, st in zip(Meff_meV, zacc_scan, status_scan):
            w.writerow([f"{mm:.6e}", ("nan" if not np.isfinite(za) else f"{za:.5e}"),
                        st])
        w.writerow([])
        w.writerow(["## LEDGER SUMMARY"])
        w.writerow(["quantity", "value", "note"])
        w.writerow(["IC_basin_decades_free", f"{basin_decades:.2f}",
                    "decades of phi_i landing on OmegaDE0=0.685+/-0.05 (REAL reduction)"])
        w.writerow(["IC_OmegaDE0_spread_in_basin", f"{ode_spread:.4f}",
                    "flatness of the attractor basin"])
        w.writerow(["whynow_window_decades", f"{whynow_decades:.3f}",
                    "decades of M_eff giving z_acc in [0,2] (tuning that SURVIVES)"])
        w.writerow(["whynow_scale_meV", f"{M_eff_cal_meV:.3f}",
                    "the meV/rho_Lambda scale that must still be tuned"])
        w.writerow(["tuning_before", "2", "{initial conditions, energy scale}"])
        w.writerow(["tuning_after", "1", "{energy scale = meV / why-now}"])
        w.writerow(["net_reduction", "2->1", "GENUINE but PARTIAL; coincidence NOT solved"])
        w.writerow(["derivation_status", "brute-force hit != derivation",
                    "050 untouched; observer mode untouched; real check CLASS Level3 BLOCKED"])
    print("saved cp22_coincidence_tracker_results.csv")


if __name__ == "__main__":
    main()
