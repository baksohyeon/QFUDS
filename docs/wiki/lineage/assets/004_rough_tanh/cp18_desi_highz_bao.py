"""
CP18: re-aim the CP14 kill test at the redshift window DESI DR2 actually
sharpened — z>2, via the Lyman-α forest BAO.

WHY: CP14 showed our FREEZING w(z) signal HIDES below z≈1.8 (the model is flat
w=-1 there, so it projects onto ΛCDM exactly where DESI's galaxy BAO is
strongest) and only appears at z≳2. DESI DR2's headline NEW strength is exactly
z>2 through the Lyα forest. So instead of a CPL (w0,wa) projection, we compute
the ACTUAL BAO distance observables the model predicts at z>2 and compare them to
ΛCDM at the representative Lyα precision.

WHAT WE COMPUTE (derive + check each formula before use):
  D_M(z) = c ∫_0^z dz'/H(z')         flat comoving transverse distance
  D_H(z) = c/H(z)                     Hubble distance
  D_V(z) = [z · D_M² · D_H]^(1/3)     spherically-averaged BAO distance
  using E_QFUDS_V2(a) and E_LCDM(a) with H0 = 67.4 (CMB-calibrated,
  inverse-distance-ladder value; CP10). Asserts D_M(z→0) → c z / H0.

  r_d: the dark component is matter-like (w→0) BEFORE recombination, so the
  pre-drag physics is identical to ΛCDM (reuse CP10's argument). Hence r_d is
  SHARED between QFUDS and ΛCDM. D_M/r_d and D_H/r_d therefore differ ONLY
  through the late-time E(z) integral — the cleanest possible comparison.

HONESTY / STATUS (read this):
  - Exploratory sandbox. PARAMETRIZE, not DERIVE. The whole w(a) is a hand-fit
    tanh; nothing is derived from foam microphysics. The "050 ceiling"
    (deriving the dark sector from foam microphysics) is UNTOUCHED. Observer
    mode is UNTOUCHED.
  - This is mode-A forecast/positioning, NOT a likelihood. We did NOT ingest any
    DESI data vector or covariance, did NOT run a real likelihood, and store NO
    data tables. The external scalars below are REPRESENTATIVE magnitudes
    SOURCED from the DESI DR2 BAO paper (arXiv:2503.14738), used only to ground
    the precision band — they are not a fit to, or a quote of, the data product.
      * Lyα effective redshift  z_eff ≈ 2.33   (DESI DR2 Lyα sample z∈1.8–4.2)
      * representative Lyα precision: ~1.1% on D_H/r_d, ~1.4% on D_M/r_d
      * sound horizon r_d ≈ 147.05 Mpc   (arXiv:2503.14738, Eq. 2) — illustrative
    Source URL: https://arxiv.org/abs/2503.14738
  - DESI DR2 finds ΛCDM fits the BAO distances WELL on its own; the evolving-w
    hint is from BAO+CMB+SNe COMBINED, and DESI's mild preference is THAWING
    (wa<0). Our model FREEZES — the OPPOSITE direction (CP14). So this test is
    a positioning exercise, not a claim of detection.
  - The REAL verdict needs a proper joint likelihood against the actual DESI
    chains + sound-horizon physics from a Boltzmann code (CLASS / hi_class).
    That is Level 3 and BLOCKED. Everything here is a back-of-envelope stand-in.

Not evidence. Not a roadmap change.
"""
from __future__ import annotations

import csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M

# ---------------------------------------------------------------------------
# Representative external scalars — SOURCED from arXiv:2503.14738 (DESI DR2 BAO)
# These GROUND the comparison band. NOT a likelihood, NO covariance ingested.
# ---------------------------------------------------------------------------
DESI_URL = "https://arxiv.org/abs/2503.14738"
Z_EFF_LYA = 2.33          # DESI DR2 Lyα forest effective redshift (sample z∈1.8–4.2)
LYA_Z_LO, LYA_Z_HI = 1.8, 4.2     # DESI DR2 Lyα sample redshift range (shaded window)
R_D_MPC = 147.05          # sound horizon at drag epoch, Mpc (Eq. 2) — illustrative, SHARED
SIG_DH_PCT = 1.1          # representative Lyα precision on D_H/r_d (%)
SIG_DM_PCT = 1.4          # representative Lyα precision on D_M/r_d (%)

H0 = M.H0_CMB             # 67.4 km/s/Mpc — CMB / inverse-distance-ladder (CP10)
C = M.C_KM_S              # km/s
HUBBLE_DIST = C / H0      # c/H0 in Mpc (D_H today)


# ---------------------------------------------------------------------------
# Distance formulae — DERIVE/CHECK a known limit before use.
#   D_C(z) = (c/H0) ∫_0^z dz'/E(z')   ; flat => D_M = D_C (transverse comoving).
#   Limit: as z->0, E->1 so D_M -> (c/H0) z.  (asserted in main)
#   D_H(z) = c/H(z) = (c/H0)/E(z).     ; Limit: D_H(0) = c/H0.
#   D_V(z) = [z D_M² D_H]^(1/3).       ; spherically-averaged BAO scale.
# ---------------------------------------------------------------------------
def E_of_z(z, E_of_a):
    """Evaluate a model E(a) on a redshift array (a = 1/(1+z))."""
    a = 1.0 / (1.0 + np.asarray(z, dtype=float))
    return np.array([float(E_of_a(ai)) for ai in a])


def comoving_DM(z_grid, E_vals):
    """D_M(z) [Mpc] = (c/H0) ∫_0^z dz'/E, flat. z_grid must start at 0 & ascend."""
    from scipy.integrate import cumulative_trapezoid
    inv_E = 1.0 / E_vals
    integ = cumulative_trapezoid(inv_E, z_grid, initial=0.0)
    return HUBBLE_DIST * integ


def hubble_DH(E_vals):
    """D_H(z) [Mpc] = (c/H0)/E(z)."""
    return HUBBLE_DIST / E_vals


def DV(z_grid, DM, DH):
    """D_V(z) = [z D_M² D_H]^(1/3) [Mpc]. (z=0 -> 0, handled by grid)."""
    return np.cbrt(z_grid * DM**2 * DH)


def main():
    print("=" * 76)
    print("CP18: QFUDS BAO distances at z>2 (Lyα window) vs ΛCDM — exploratory")
    print(f"External scalars REPRESENTATIVE, sourced from {DESI_URL}")
    print("NOT a likelihood; NO covariance ingested. Real verdict = CLASS (BLOCKED).")
    print("=" * 76)

    # ---- redshift grid: fine, 0 -> 3 (covers the Lyα window up to z_eff & beyond)
    z = np.linspace(0.0, 3.0, 601)

    # ---- E(z) for both cosmologies (H0 = 67.4 shared; SNe-pinned background, CP1)
    E_lcdm = E_of_z(z, M.E_LCDM)
    E_qfuds = E_of_z(z, M.E_QFUDS_V2)

    # ---- distances
    DM_lcdm = comoving_DM(z, E_lcdm)
    DM_qfuds = comoving_DM(z, E_qfuds)
    DH_lcdm = hubble_DH(E_lcdm)
    DH_qfuds = hubble_DH(E_qfuds)
    DV_lcdm = DV(z, DM_lcdm, DH_lcdm)
    DV_qfuds = DV(z, DM_qfuds, DH_qfuds)

    # ---- SANITY 1: D_M(z->0) -> c z / H0 (E->1). At finite z[1] there is an
    #      O(z) correction (E>1 from matter), so tolerance scales with z[1].
    z_small = z[1]
    dm_small_pred = HUBBLE_DIST * z_small
    tol1 = 5.0 * z_small  # first-order correction bound (~few % of c z/H0 at z[1])
    assert abs(DM_lcdm[1] - dm_small_pred) / dm_small_pred < tol1, \
        "D_M(z->0) -> c z/H0 limit FAILED (ΛCDM)"
    assert abs(DM_qfuds[1] - dm_small_pred) / dm_small_pred < tol1, \
        "D_M(z->0) -> c z/H0 limit FAILED (QFUDS)"
    # ---- SANITY 2: D_H(0) = c/H0 exactly (E(0)=1).
    assert abs(DH_lcdm[0] - HUBBLE_DIST) / HUBBLE_DIST < 1e-9, "D_H(0)=c/H0 FAILED (ΛCDM)"
    assert abs(DH_qfuds[0] - HUBBLE_DIST) / HUBBLE_DIST < 1e-9, "D_H(0)=c/H0 FAILED (QFUDS)"
    # ---- SANITY 3: z->0 background is ΛCDM (CP1 SNe-pinned). pct diff -> 0 at low z.
    with np.errstate(invalid="ignore", divide="ignore"):
        pct_DM = 100.0 * (DM_qfuds - DM_lcdm) / DM_lcdm
    pct_DH = 100.0 * (DH_qfuds - DH_lcdm) / DH_lcdm
    pct_DM[0] = 0.0  # 0/0 at z=0 (D_M(0)=0); limit is 0 since both -> c z/H0
    assert abs(pct_DH[0]) < 1e-9, "z->0 must reduce to ΛCDM (D_H) — FAILED"
    assert abs(pct_DM[1]) < 0.5, "z->0 must reduce to ΛCDM (D_M) — FAILED"
    print("\nsanity: D_M->cz/H0, D_H(0)=c/H0, z->0 => ΛCDM   [all asserts passed]")

    # ---- observables in BAO units (r_d SHARED — CP10: matter-like before drag)
    DM_over_rd_lcdm = DM_lcdm / R_D_MPC
    DM_over_rd_qfuds = DM_qfuds / R_D_MPC
    DH_over_rd_lcdm = DH_lcdm / R_D_MPC
    DH_over_rd_qfuds = DH_qfuds / R_D_MPC

    # ---- evaluate at the sourced Lyα effective redshift z_eff
    def at_zeff(arr):
        return float(np.interp(Z_EFF_LYA, z, arr))

    pdm_zeff = at_zeff(pct_DM)
    pdh_zeff = at_zeff(pct_DH)
    DMrd_l, DMrd_q = at_zeff(DM_over_rd_lcdm), at_zeff(DM_over_rd_qfuds)
    DHrd_l, DHrd_q = at_zeff(DH_over_rd_lcdm), at_zeff(DH_over_rd_qfuds)

    print(f"\n--- at z_eff = {Z_EFF_LYA} (sourced Lyα effective redshift) ---")
    print(f"  D_M/r_d :  ΛCDM={DMrd_l:7.3f}   QFUDS={DMrd_q:7.3f}   "
          f"Δ={pdm_zeff:+.2f}%   (rep. Lyα precision ±{SIG_DM_PCT}%)")
    print(f"  D_H/r_d :  ΛCDM={DHrd_l:7.3f}   QFUDS={DHrd_q:7.3f}   "
          f"Δ={pdh_zeff:+.2f}%   (rep. Lyα precision ±{SIG_DH_PCT}%)")

    # ---- verdict: within or beyond the representative Lyα precision?
    def verdict(pct, sig):
        return "BEYOND (testable)" if abs(pct) > sig else "WITHIN (hidden)"

    v_dm = verdict(pdm_zeff, SIG_DM_PCT)
    v_dh = verdict(pdh_zeff, SIG_DH_PCT)
    n_dm = abs(pdm_zeff) / SIG_DM_PCT
    n_dh = abs(pdh_zeff) / SIG_DH_PCT
    print(f"\n  D_M/r_d: |Δ|/σ_rep = {n_dm:.2f}  -> {v_dm}")
    print(f"  D_H/r_d: |Δ|/σ_rep = {n_dh:.2f}  -> {v_dh}")
    print(f"  direction: QFUDS H(z) slightly HIGHER at mid-z (late w:0->-1 leaves "
          f"the dark\n             component matter-like longer) -> D_H, D_M shrink. "
          f"This is FREEZING,\n             the OPPOSITE of DESI's mild THAWING "
          f"preference (CP14).")

    # ---- FIGURE (2 panels) ------------------------------------------------
    fig, (axA, axB) = plt.subplots(1, 2, figsize=(15, 6.2))
    lya_kw = dict(color="goldenrod", alpha=0.13)

    # (a) D_M/r_d and D_H/r_d vs z, with Lyα window + representative error bars
    axA.axvspan(LYA_Z_LO, min(LYA_Z_HI, z[-1]), label="DESI DR2 Lyα window (z∈1.8–4.2)",
                **lya_kw)
    axA.plot(z, DM_over_rd_lcdm, "b-", lw=2, label="$D_M/r_d$  ΛCDM")
    axA.plot(z, DM_over_rd_qfuds, "b--", lw=2, label="$D_M/r_d$  QFUDS")
    axA.plot(z, DH_over_rd_lcdm, color="tab:red", lw=2, label="$D_H/r_d$  ΛCDM")
    axA.plot(z, DH_over_rd_qfuds, color="tab:red", lw=2, ls="--",
             label="$D_H/r_d$  QFUDS")
    # representative Lyα error bars at z_eff (NOT a data point — illustrative)
    axA.errorbar(Z_EFF_LYA, DMrd_l, yerr=DMrd_l * SIG_DM_PCT / 100.0, fmt="o",
                 color="navy", ms=6, capsize=4,
                 label=f"rep. ±{SIG_DM_PCT}% (D_M/r_d @ z_eff)")
    axA.errorbar(Z_EFF_LYA, DHrd_l, yerr=DHrd_l * SIG_DH_PCT / 100.0, fmt="s",
                 color="darkred", ms=6, capsize=4,
                 label=f"rep. ±{SIG_DH_PCT}% (D_H/r_d @ z_eff)")
    axA.axvline(Z_EFF_LYA, color="gray", ls=":", lw=1)
    axA.set_xlabel("redshift  z", fontsize=12)
    axA.set_ylabel("BAO distance / $r_d$", fontsize=12)
    axA.set_title("(a) $D_M/r_d$ & $D_H/r_d$: QFUDS vs ΛCDM  ($r_d$ shared, CP10)")
    axA.legend(fontsize=8, loc="center left")
    axA.grid(alpha=0.3)

    # (b) % difference vs z, with representative DESI-DR2 precision bands
    axB.axvspan(LYA_Z_LO, min(LYA_Z_HI, z[-1]), **lya_kw)
    axB.axhline(0.0, color="k", lw=0.8)
    axB.fill_between(z, -SIG_DM_PCT, SIG_DM_PCT, color="b", alpha=0.10,
                     label=f"rep. Lyα ±{SIG_DM_PCT}% (D_M/r_d)")
    axB.fill_between(z, -SIG_DH_PCT, SIG_DH_PCT, color="tab:red", alpha=0.08,
                     label=f"rep. Lyα ±{SIG_DH_PCT}% (D_H/r_d)")
    axB.plot(z, pct_DM, "b-", lw=2, label="Δ $D_M/r_d$  (QFUDS−ΛCDM)")
    axB.plot(z, pct_DH, color="tab:red", lw=2, label="Δ $D_H/r_d$  (QFUDS−ΛCDM)")
    axB.axvline(Z_EFF_LYA, color="gray", ls=":", lw=1)
    axB.plot(Z_EFF_LYA, pdm_zeff, "bo", ms=7)
    axB.plot(Z_EFF_LYA, pdh_zeff, "s", color="tab:red", ms=7)
    axB.annotate(f"z_eff={Z_EFF_LYA}\nΔD_M={pdm_zeff:+.2f}% ({v_dm.split()[0]})\n"
                 f"ΔD_H={pdh_zeff:+.2f}% ({v_dh.split()[0]})",
                 xy=(Z_EFF_LYA, pdm_zeff), xytext=(0.55, 0.20),
                 textcoords="axes fraction", fontsize=9,
                 arrowprops=dict(arrowstyle="->", color="gray"))
    axB.set_xlabel("redshift  z", fontsize=12)
    axB.set_ylabel("% difference  (QFUDS − ΛCDM)", fontsize=12)
    axB.set_title("(b) % difference vs representative DESI-DR2 Lyα precision band")
    axB.legend(fontsize=8, loc="lower left")
    axB.grid(alpha=0.3)

    fig.suptitle("CP18: QFUDS BAO distances in DESI DR2's z>2 Lyα window "
                 "(exploratory; DESI precision representative, sourced)",
                 fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp18_desi_highz_bao.png", dpi=130)
    fig.savefig("fig_cp18_desi_highz_bao.svg")
    print("\nsaved fig_cp18_desi_highz_bao.png + .svg")

    # ---- CSV --------------------------------------------------------------
    with open("cp18_desi_highz_bao_results.csv", "w", newline="") as fh:
        wtr = csv.writer(fh)
        wtr.writerow(["# CP18 DESI z>2 BAO — exploratory; external scalars "
                      "REPRESENTATIVE, sourced from arXiv:2503.14738"])
        wtr.writerow([f"# NOT a likelihood; NO covariance ingested. r_d={R_D_MPC} Mpc "
                      f"SHARED (CP10). H0={H0}. z_eff={Z_EFF_LYA}."])
        wtr.writerow([f"# rep. Lyα precision: D_M/r_d ±{SIG_DM_PCT}%, "
                      f"D_H/r_d ±{SIG_DH_PCT}%. Real verdict = CLASS, Level 3, BLOCKED."])
        wtr.writerow(["z", "DM_over_rd_LCDM", "DM_over_rd_QFUDS",
                      "DH_over_rd_LCDM", "DH_over_rd_QFUDS",
                      "pct_diff_DM", "pct_diff_DH"])
        for i in range(len(z)):
            wtr.writerow([f"{z[i]:.4f}",
                          f"{DM_over_rd_lcdm[i]:.5f}", f"{DM_over_rd_qfuds[i]:.5f}",
                          f"{DH_over_rd_lcdm[i]:.5f}", f"{DH_over_rd_qfuds[i]:.5f}",
                          f"{pct_DM[i]:+.5f}", f"{pct_DH[i]:+.5f}"])
    print("saved cp18_desi_highz_bao_results.csv")

    # ---- VERDICT ----------------------------------------------------------
    print("\n" + "=" * 76)
    print("VERDICT (representative numbers — real check is CLASS, Level 3, BLOCKED):")
    print(f"  At DESI's sharpened z_eff={Z_EFF_LYA}:")
    print(f"    D_M/r_d differs {pdm_zeff:+.2f}%  -> {v_dm} (vs ±{SIG_DM_PCT}% rep.)")
    print(f"    D_H/r_d differs {pdh_zeff:+.2f}%  -> {v_dh} (vs ±{SIG_DH_PCT}% rep.)")
    print(f"  Sign: QFUDS H(z) slightly higher mid-z (FREEZING) = OPPOSITE of DESI's")
    print(f"        mild THAWING preference; and DESI finds ΛCDM fits BAO well alone.")
    print(f"  050 ceiling + observer mode UNTOUCHED. r_d shared (CP10).")
    print("=" * 76)


if __name__ == "__main__":
    main()
