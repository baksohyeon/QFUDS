"""
CP21: BRUTE-FORCE the two escape mechanisms CP20 named for the ξ≈9.5 Mpc scale
— mean-field near-criticality (ξ~|1−T/Tc|^−ν) and Kibble–Zurek freeze-out — and
ask the ONLY question that matters: does hitting the scale REDUCE the count of
fine-tuned numbers (progress toward a derivation) or merely RELOCATE the tuning
into the mechanism's own knobs (no progress)?

STATUS: exploratory sandbox. PARAMETRIZE, NOT DERIVE. Nothing here is derived
foam microphysics; w(a) elsewhere is still a hand-fitted tanh. A brute-force HIT
of ξ≈9.5 Mpc is NOT a derivation — brute force can always hit a single target by
construction. The deliverable is the TUNING LEDGER (inputs-in vs target-out),
not the hit. The 050 ceiling is UNTOUCHED; observer mode is UNTOUCHED; the
roadmap status is UNCHANGED. The real check is CLASS/hi_class (Level 3, BLOCKED);
this script cannot and does not substitute for it.

What CP20 established (built on directly here):
  - data wants ξ ≈ 9.5 Mpc  (from clustering sound speed c_s² = 4.6e-6, c_s≈ξ/d_H)
  - microscopic foam scales are too SMALL by 10^4–10^58
  - the causal/Kibble horizon at z~2 (~4400 Mpc comoving) is too BIG by ~461×
  - the ONLY escape: an EMERGENT tuned-down ξ via near-criticality or KZ quench
CP21 forces those two mechanisms onto the target and reads off the tuning.

Mechanisms (rough; each formula derived/checked against a known limit):
  1. Mean-field criticality:  ξ(T) = ξ0 · |1 − T/Tc|^(−ν) ≡ ξ0 · ε^(−ν)
       ε ≡ |1 − T/Tc| (proximity to the critical point), ν ∈ [0.5, 1].
       Brute-force: solve ε* = (ξ0 / ξ_target)^(1/ν) to HIT ξ_target.
       Limits: ε→1 (far from Tc) ⇒ ξ→ξ0 (micro);  ε→0 (at Tc) ⇒ ξ→∞.
  2. Kibble–Zurek freeze-out:  ξ_KZ = ξ0 · (τ_Q / τ0)^(ν/(1+νz))
       τ_Q = cosmological quench timescale, τ0 = microscopic time, z = dynamic
       exponent ∈ [1, 3]. KZ exponent ν/(1+νz) ∈ (0,1) (sub-linear, by design).
       Brute-force: solve (τ_Q/τ0)* = (ξ_target/ξ0)^((1+νz)/ν) to HIT ξ_target.

Outputs: 2-panel figure (png+svg) + results csv (working dir).
Exploratory; not evidence; real check = CLASS/hi_class (Level 3, BLOCKED).
"""
from __future__ import annotations
import csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M

# ---------------------------------------------------------------------------
# Reuse CP20's calibrated scale ladder verbatim (do not re-derive).
# ---------------------------------------------------------------------------
C_KM_S, H0 = M.C_KM_S, M.H0_CMB
D_H = C_KM_S / H0                       # Hubble distance c/H0 [Mpc]
C2_FIT = 4.6e-6                         # data-fit clustering sound speed (CP7/CP8)
MPC_M = 3.0856775814913673e22          # 1 Mpc in metres


def xi_from_cs2(c2):
    """ξ [Mpc] from c_s² via c_s ≈ ξ/d_H (CP8). Same relation as CP20."""
    return np.sqrt(c2) * D_H


XI_TARGET = xi_from_cs2(C2_FIT)        # ≈ 9.5 Mpc, the data-preferred scale

# microscopic foam ξ0 candidates (metres) → Mpc, same ladder as CP20's micro horn
FOAM_CANDIDATES_M = {
    "Planck length":  1.616e-35,
    "nuclear (1 fm)": 1.0e-15,
    "atomic (1 Å)":   1.0e-10,
    "galaxy (1 kpc)": 3.0857e19,
}
FOAM_XI0_MPC = {name: (L / MPC_M) for name, L in FOAM_CANDIDATES_M.items()}


# ---------------------------------------------------------------------------
# Mechanism 1: mean-field near-criticality
# ---------------------------------------------------------------------------
def xi_criticality(eps, xi0, nu):
    """ξ = ξ0 · ε^(−ν). ε ≡ |1 − T/Tc| proximity to the critical point."""
    return xi0 * np.asarray(eps, dtype=float) ** (-nu)


def eps_required(xi0, xi_target, nu):
    """Solve ξ0·ε^(−ν) = ξ_target  ⇒  ε* = (ξ0/ξ_target)^(1/ν)."""
    return (xi0 / xi_target) ** (1.0 / nu)


def sensitivity_criticality(nu):
    """d ln ξ / d ln ε  for ξ = ξ0 ε^(−ν)  =  −ν   (analytic, ε-independent)."""
    return -nu


# ---------------------------------------------------------------------------
# Mechanism 2: Kibble–Zurek freeze-out
# ---------------------------------------------------------------------------
def kz_exponent(nu, zdyn):
    """KZ scaling exponent ν/(1+νz). Lies in (0,1) for ν>0, z≥1."""
    return nu / (1.0 + nu * zdyn)


def xi_kz(tauQ_over_tau0, xi0, nu, zdyn):
    """ξ_KZ = ξ0 · (τ_Q/τ0)^(ν/(1+νz))."""
    return xi0 * np.asarray(tauQ_over_tau0, dtype=float) ** kz_exponent(nu, zdyn)


def tauQ_required(xi0, xi_target, nu, zdyn):
    """Solve ξ0·(τ_Q/τ0)^μ = ξ_target  ⇒  (τ_Q/τ0)* = (ξ_target/ξ0)^(1/μ),
    with μ = ν/(1+νz), i.e. exponent (1+νz)/ν."""
    return (xi_target / xi0) ** (1.0 / kz_exponent(nu, zdyn))


def sensitivity_kz(nu, zdyn):
    """d ln ξ / d ln(τ_Q/τ0) for ξ_KZ = μ = ν/(1+νz)  (analytic)."""
    return kz_exponent(nu, zdyn)


# ---------------------------------------------------------------------------
# Derive/CHECK every formula against a known limit BEFORE use.
# ---------------------------------------------------------------------------
def _checks():
    # ξ_target reproduces CP20's data scale
    assert 9.0 < XI_TARGET < 10.5, XI_TARGET

    xi0 = FOAM_XI0_MPC["galaxy (1 kpc)"]   # a finite, visible scale for limit tests
    nu = 1.0

    # Limit A: far from Tc (ε→1) ⇒ ξ→ξ0 (micro). Exact at ε=1.
    assert abs(xi_criticality(1.0, xi0, nu) - xi0) < 1e-30 * max(xi0, 1e-30)

    # Limit B: at Tc (ε→0) ⇒ ξ→∞ (diverges). Monotone blow-up.
    assert xi_criticality(1e-60, xi0, nu) > 1e50

    # Round-trip: the solved ε* must reproduce ξ_target.
    for name, x0 in FOAM_XI0_MPC.items():
        for nv in (0.5, 1.0):
            eps = eps_required(x0, XI_TARGET, nv)
            assert np.isclose(xi_criticality(eps, x0, nv), XI_TARGET, rtol=1e-9), name

    # KZ exponent must sit in (0,1) for all (ν,z) in range (sub-linear by design).
    for nv in (0.5, 1.0):
        for zd in (1, 2, 3):
            mu = kz_exponent(nv, zd)
            assert 0.0 < mu < 1.0, (nv, zd, mu)

    # KZ round-trip: solved (τ_Q/τ0)* reproduces ξ_target.
    for name, x0 in FOAM_XI0_MPC.items():
        for nv in (0.5, 1.0):
            for zd in (1, 2, 3):
                r = tauQ_required(x0, XI_TARGET, nv, zd)
                assert np.isclose(xi_kz(r, x0, nv, zd), XI_TARGET, rtol=1e-6), name

    # Sensitivity: numeric central difference vs analytic (criticality & KZ).
    eps0 = eps_required(xi0, XI_TARGET, nu)
    h = 1e-4
    num = (np.log(xi_criticality(eps0 * np.exp(h), xi0, nu))
           - np.log(xi_criticality(eps0 * np.exp(-h), xi0, nu))) / (2 * h)
    assert np.isclose(num, sensitivity_criticality(nu), rtol=1e-5), num
    r0 = tauQ_required(xi0, XI_TARGET, nu, 2)
    numk = (np.log(xi_kz(r0 * np.exp(h), xi0, nu, 2))
            - np.log(xi_kz(r0 * np.exp(-h), xi0, nu, 2))) / (2 * h)
    assert np.isclose(numk, sensitivity_kz(nu, 2), rtol=1e-5), numk

    print(f"checks PASS: ξ_target={XI_TARGET:.2f} Mpc; "
          f"crit limits ξ(ε=1)=ξ0, ξ(ε→0)→∞; "
          f"KZ exponent∈(0,1); round-trips & sensitivities verified.")


# ---------------------------------------------------------------------------
def main():
    _checks()
    print(f"\nξ_target (data-preferred) = {XI_TARGET:.3f} Mpc  (c_s²={C2_FIT:.1e})\n")

    rows = []   # for csv + ledger

    # ---- Mechanism 1: criticality — required proximity ε ------------------
    print("[M1] mean-field criticality  ξ = ξ0·ε^(−ν),  solve ε* to hit target:")
    for name, xi0 in FOAM_XI0_MPC.items():
        for nu in (0.5, 1.0):
            eps = eps_required(xi0, XI_TARGET, nu)
            orders = np.log10(eps)             # negative; |orders| = fine-tuning
            sens = sensitivity_criticality(nu)
            print(f"   ξ0={name:16s} ν={nu:>3}: ε*={eps:.3e}  "
                  f"(must sit 10^{orders:.1f} from Tc)  dlnξ/dlnε={sens:+.2f}")
            rows.append({
                "mechanism": "criticality", "xi0_Mpc": xi0, "nu": nu, "z": "",
                "required_tuning": eps, "orders_of_tuning": orders,
                "sensitivity": sens,
                "verdict": "RELOCATED: 1 tuned input (ε) -> 1 target (ξ)",
            })

    # ---- Mechanism 2: Kibble–Zurek — required quench ratio τ_Q/τ0 ---------
    print("\n[M2] Kibble–Zurek  ξ = ξ0·(τ_Q/τ0)^(ν/(1+νz)),  solve τ_Q/τ0 to hit:")
    for name, xi0 in FOAM_XI0_MPC.items():
        for nu in (0.5, 1.0):
            for zd in (1, 2, 3):
                r = tauQ_required(xi0, XI_TARGET, nu, zd)
                orders = np.log10(r)           # positive & huge
                sens = sensitivity_kz(nu, zd)
                print(f"   ξ0={name:16s} ν={nu} z={zd}: τ_Q/τ0={r:.3e}  "
                      f"(quench slow by 10^{orders:.1f}×)  "
                      f"dlnξ/dln(τ_Q/τ0)={sens:.3f}")
                rows.append({
                    "mechanism": "kibble_zurek", "xi0_Mpc": xi0, "nu": nu, "z": zd,
                    "required_tuning": r, "orders_of_tuning": orders,
                    "sensitivity": sens,
                    "verdict": "RELOCATED: 1 tuned input (τ_Q/τ0) -> 1 target (ξ)",
                })

    # ---- TUNING LEDGER: inputs-in vs target-out ---------------------------
    # Both mechanisms are 1-tuned-input -> 1-target maps. Count of fine-tuned
    # numbers does NOT drop (was: ξ unexplained; now: ε OR τ_Q/τ0 unexplained,
    # PLUS ν, z, ξ0, PLUS the meta-tuning "why near-critical / why this quench").
    print("\n[LEDGER] tuned-input count IN vs target OUT:")
    print("   pre-CP21:  1 unexplained number (ξ≈9.5 Mpc).")
    print("   criticality: supply ε (knife-edge proximity) + ν + ξ0; still 1 OUT.")
    print("                => count NOT reduced; tuning RELOCATED into ε.")
    print("   kibble-zurek: supply τ_Q/τ0 (huge) + ν + z + ξ0; still 1 OUT.")
    print("                => count NOT reduced; tuning RELOCATED into τ_Q/τ0.")
    print("   META-tuning (both): WHY does the dark sector sit at/near a 2nd-order")
    print("   critical point (or undergo a slow cosmological quench) AT ALL? That")
    print("   proximity is itself an unexplained input — a tuning ON TOP of ε/τ_Q.")

    # representative (Planck-scale ξ0) headline numbers for the ledger panel
    eps_planck_nu1 = eps_required(FOAM_XI0_MPC["Planck length"], XI_TARGET, 1.0)
    eps_planck_nu05 = eps_required(FOAM_XI0_MPC["Planck length"], XI_TARGET, 0.5)
    r_planck = tauQ_required(FOAM_XI0_MPC["Planck length"], XI_TARGET, 1.0, 2)

    # ---- figure -----------------------------------------------------------
    fig, ax = plt.subplots(1, 2, figsize=(14, 5.8))

    # (a) ξ vs proximity ε (log-log). Curves per foam ξ0 (ν=1 solid, 0.5 dashed),
    #     ξ_target line, tuned solutions ε* marked. Shows ξ slides from micro (ε=1)
    #     up to the target only by pushing ε to absurdly small (knife-edge) values.
    eps_grid = np.logspace(-120, 0, 600)
    colors = {"Planck length": "tab:red", "nuclear (1 fm)": "tab:orange",
              "atomic (1 Å)": "tab:green", "galaxy (1 kpc)": "tab:blue"}
    for name, xi0 in FOAM_XI0_MPC.items():
        c = colors[name]
        ax[0].plot(eps_grid, xi_criticality(eps_grid, xi0, 1.0), color=c, lw=1.6,
                   label=f"{name} (ν=1)")
        ax[0].plot(eps_grid, xi_criticality(eps_grid, xi0, 0.5), color=c, lw=1.0,
                   ls="--", alpha=0.7)
        eps_s = eps_required(xi0, XI_TARGET, 1.0)
        ax[0].scatter([eps_s], [XI_TARGET], s=55, color=c, zorder=6,
                      edgecolor="k", linewidth=0.5)
    ax[0].axhline(XI_TARGET, color="purple", lw=2,
                  label=f"data wants ξ≈{XI_TARGET:.1f} Mpc")
    ax[0].axvline(1.0, color="gray", lw=0.8, ls=":")
    ax[0].annotate("ε=1: far from Tc\n(ξ→ξ0, micro)", (1.0, 1e-30), fontsize=7,
                   color="gray", ha="right")
    ax[0].annotate("ε→0: AT Tc (ξ→∞)\nknife-edge proximity = the tuning",
                   (1e-110, 1e30), fontsize=7.5, color="purple")
    ax[0].set_xscale("log"); ax[0].set_yscale("log")
    ax[0].set_xlim(1e-120, 3)
    ax[0].set_ylim(1e-60, 1e40)
    ax[0].set_xlabel("proximity to critical point  ε = |1 − T/Tc|")
    ax[0].set_ylabel("correlation length ξ [Mpc]")
    ax[0].set_title("(a) M1 criticality: ξ0·ε^(−ν) CAN reach 9.5 Mpc —\n"
                    "only by tuning ε down 10^59–10^117 (brute-force ≠ derivation)")
    ax[0].legend(fontsize=6.5, loc="lower left"); ax[0].grid(alpha=0.3, which="both")

    # (b) tuning ledger: orders of fine-tuning required per mechanism × foam ξ0.
    #     Bars = |log10(required input)|. The verdict text: relocated, not reduced.
    labels, vals, bcols = [], [], []
    for name, xi0 in FOAM_XI0_MPC.items():
        labels.append(f"M1 crit\n{name.split()[0]}\nν=1")
        vals.append(abs(np.log10(eps_required(xi0, XI_TARGET, 1.0))))
        bcols.append("tab:purple")
    for name, xi0 in FOAM_XI0_MPC.items():
        labels.append(f"M2 KZ\n{name.split()[0]}\nν=1,z=2")
        vals.append(abs(np.log10(tauQ_required(xi0, XI_TARGET, 1.0, 2))))
        bcols.append("teal")
    ypos = np.arange(len(labels))
    ax[1].barh(ypos, vals, color=bcols, alpha=0.85, edgecolor="k", linewidth=0.4)
    for i, v in enumerate(vals):
        ax[1].text(v + 2, i, f"10^{v:.0f}", va="center", fontsize=7.5)
    ax[1].set_yticks(ypos); ax[1].set_yticklabels(labels, fontsize=6.8)
    ax[1].invert_yaxis()
    ax[1].set_xlabel("orders of fine-tuning required in the input "
                     "(|log₁₀ ε|  or  log₁₀ τ_Q/τ0)")
    ax[1].set_title("(b) TUNING LEDGER — RELOCATED, not REDUCED\n"
                    "1 tuned input (ε or τ_Q/τ0) → 1 target (ξ); count unchanged")
    ax[1].grid(alpha=0.3, axis="x")
    ax[1].text(0.98, 0.03,
               "verdict: brute-force HITS ξ but only by\n"
               "supplying a fine-tuned ε / τ_Q INPUT.\n"
               "knobs RELOCATED, not REDUCED.\n"
               "+ meta-tuning: why near-critical at all?",
               transform=ax[1].transAxes, fontsize=7.2, ha="right", va="bottom",
               bbox=dict(boxstyle="round", fc="wheat", alpha=0.85))

    fig.suptitle("CP21: ξ near-criticality / Kibble–Zurek brute-force "
                 "(exploratory; brute-force hit ≠ derivation)", fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_cp21_xi_criticality.png", dpi=130)
    fig.savefig("fig_cp21_xi_criticality.svg")
    print("\nsaved fig_cp21_xi_criticality.png + .svg")

    # ---- csv --------------------------------------------------------------
    with open("cp21_xi_criticality_results.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["# CP21 ξ near-criticality / Kibble-Zurek brute-force — "
                    "parametrize, not derive; brute-force hit != derivation"])
        w.writerow(["# xi_target_Mpc", f"{XI_TARGET:.4f}",
                    "data-preferred scale from c_s²=4.6e-6 (CP8/CP20)"])
        w.writerow(["mechanism", "xi0_Mpc", "nu", "z",
                    "required_tuning", "orders_of_tuning", "sensitivity", "verdict"])
        for r in rows:
            w.writerow([r["mechanism"], f"{r['xi0_Mpc']:.4e}", r["nu"], r["z"],
                        f"{r['required_tuning']:.4e}", f"{r['orders_of_tuning']:.3f}",
                        f"{r['sensitivity']:.4f}", r["verdict"]])
    print("saved cp21_xi_criticality_results.csv")

    # ---- honest verdict (printed) -----------------------------------------
    print("\n=== CP21 verdict (parametrize, not derive; brute-force ≠ derivation) ===")
    print(f"Both mechanisms CAN hit ξ≈{XI_TARGET:.1f} Mpc — trivially, by construction.")
    print(f"M1 criticality: to reach it from a Planck-scale ξ0 the proximity must be")
    print(f"  ε≈{eps_planck_nu1:.1e} (ν=1) … {eps_planck_nu05:.1e} (ν=0.5): the system")
    print(f"  must sit 10^59–10^117 away from Tc — an absurd knife-edge proximity INPUT.")
    print(f"  Response sensitivity dlnξ/dlnε=−ν is only O(1), so the tuning is in the")
    print(f"  VALUE of ε (its smallness), not the slope.")
    print(f"M2 Kibble–Zurek: τ_Q/τ0≈{r_planck:.1e} (Planck ξ0, ν=1,z=2): the cosmological")
    print(f"  quench must be slower than micro by ~10^175 (10^116 already at z=1).")
    print(f"  Its exponent ν/(1+νz)∈(0,1)")
    print(f"  makes the RESPONSE milder (sensitivity ~0.33), BUT the required central")
    print(f"  value is still an enormous supplied INPUT, not an output.")
    print(f"LEDGER: each mechanism is a 1-tuned-input → 1-target map. The count of")
    print(f"  unexplained numbers does NOT drop: ξ's tuning is RELOCATED into ε (or")
    print(f"  τ_Q/τ0), and ν, z, ξ0 are added. Plus META-tuning: why near a 2nd-order")
    print(f"  point / slow quench at all? => RELOCATED, NOT REDUCED. No derivation.")
    print(f"050 ceiling UNTOUCHED; observer mode UNTOUCHED; roadmap UNCHANGED.")
    print(f"Real check = CLASS/hi_class (Level 3), BLOCKED. This script is not it.")


if __name__ == "__main__":
    main()
