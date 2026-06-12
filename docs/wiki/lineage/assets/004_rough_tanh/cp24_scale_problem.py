"""
CP24: the SCALE PROBLEM — an honest survey + ledger of every candidate origin
for the dark-sector correlation length ξ ≈ 9.5–10 Mpc that the data wants
(CP8/CP20/CP21), showing each one is circular / relocated / wrong-size.

STATUS: exploratory sandbox. PARAMETRIZE, NOT DERIVE. This is a rough toy, NOT a
derived theory, NOT evidence, NOT a roadmap change. w(a) elsewhere is still a
hand-fitted tanh. Nothing here derives 10 Mpc from foam — and the deliverable is
the explicit demonstration that NOTHING does. The 050 ceiling is UNTOUCHED;
observer mode is UNTOUCHED; the roadmap status is UNCHANGED. The real check is
CLASS/hi_class (Level 3, BLOCKED); this script cannot and does not substitute.

MAXIMUM-HONESTY GUARDRAIL (the point of this CP):
  ξ ≈ 10 Mpc is the SECOND irreducible number (after c_s²/N_X). CP24 does NOT
  derive it. It surveys the standard candidate origins of a ~10 Mpc length and
  reads off, for each, WHERE it stops:
    - standard-cosmology scales (k_eq^-1, r_d, R8, horizon): the only one ξ lands
      ON is R8, the nonlinear/σ8 scale — and R8 is fixed by STANDARD physics
      (Ω_m h², primordial spectrum, transfer), so a dark sector reproducing it
      makes NO independent prediction. CIRCULAR, zero evidential weight.
      "Matches ≠ derives."
    - dimensional transmutation L = L_0·exp(+c/g²): RELOCATES the tuning into the
      coupling g (like CP21's ε). Genuine partial credit — it converts a ~58-order
      length tuning into a ~sub-percent coupling tuning (exponential map) — but it
      is still an input and does not PICK 10 Mpc over any other scale.
    - dark-fluid Jeans length λ_J = c_s/H: equals ξ only BY CONSTRUCTION, because
      it is built from c_s² — the very quantity CP8 was trying to explain.
      CIRCULAR with CP8.
  If anything below reads as "this derives 10 Mpc from foam" it is a hallucination
  and must be deleted. The verdict is: QFUDS inherits the standard hierarchy /
  scale problem; no candidate derives the scale.

Outputs (working dir, exact names):
  fig_cp24_scale_problem.png (dpi=130) + .svg, cp24_scale_problem_results.csv
Conventions: numpy 2.4 (np.trapezoid), matplotlib Agg. Formulas derived/CHECKed
against known limits (assert). External numbers labelled representative/cited.
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
# Reuse CP20/CP21 calibration verbatim (do not re-derive the dark-sector scale).
# ---------------------------------------------------------------------------
C_KM_S, H0 = M.C_KM_S, M.H0_CMB
H_LITTLE = H0 / 100.0                    # dimensionless h
OM, OR, OL = M.OMEGA_M0_LCDM, M.OMEGA_R0_LCDM, M.OMEGA_L0_LCDM
OMBH2 = M.OMEGA_B0 * H_LITTLE ** 2       # physical baryon density (for context)
OMMH2 = OM * H_LITTLE ** 2               # physical matter density
D_H = C_KM_S / H0                        # Hubble distance c/H0 [Mpc]
C2_FIT = 4.6e-6                          # data-fit clustering sound speed (CP7/CP8)
MPC_M = 3.0856775814913673e22           # 1 Mpc in metres
L_PLANCK_M = 1.616255e-35               # Planck length [m]
L_DARKCONF_M = 1.973269804e-16          # ~1 GeV^-1 (ħc/GeV) dark-confinement proxy [m]


def xi_from_cs2(c2: float) -> float:
    """ξ [Mpc] from c_s² via c_s ≈ ξ/d_H (CP8). Derived+checked relation."""
    return np.sqrt(c2) * D_H


XI_TARGET = xi_from_cs2(C2_FIT)          # ≈ 9.5 Mpc, the data-preferred scale


# ---------------------------------------------------------------------------
# Standard-cosmology scales (each DERIVED from standard inputs, then compared).
# ---------------------------------------------------------------------------
def E_lcdm(z: float) -> float:
    """ΛCDM dimensionless Hubble rate E(z)=H/H0 (same as CP20)."""
    a = 1.0 / (1.0 + z)
    return np.sqrt(OM * a ** -3 + OR * a ** -4 + OL)


def k_eq_inv_Mpc() -> tuple[float, float, float]:
    """Comoving 1/k_eq, the horizon scale at matter–radiation equality.

    DERIVATION (standard). Equality: Ω_m a_eq^-3 = Ω_r a_eq^-4 ⇒ a_eq = Ω_r/Ω_m.
    Comoving k_eq = a_eq H(a_eq)/c. At equality H_eq = H0·sqrt(2 Ω_m a_eq^-3), so
        k_eq = (H0/c)·Ω_m·sqrt(2/Ω_r)   [Mpc^-1].
    Returns (z_eq, k_eq, 1/k_eq).
    """
    a_eq = OR / OM
    z_eq = 1.0 / a_eq - 1.0
    k_eq = (H0 / C_KM_S) * OM * np.sqrt(2.0 / OR)   # Mpc^-1, comoving
    return z_eq, k_eq, 1.0 / k_eq


def causal_horizon_z2_Mpc(z_star: float = 2.0) -> float:
    """Comoving Hubble radius c/(aH) at z* (the Kibble scale, CP20). ~4400 Mpc."""
    return D_H * (1.0 + z_star) / E_lcdm(z_star)


def jeans_comoving_Mpc(c2: float, z_star: float = 2.0) -> tuple[float, float, float]:
    """Dark-fluid Jeans length λ_J = c_s/H, comoving, at z*.

    c_s = sqrt(c2)·c (km/s). Proper λ_J = c_s/H(z*); comoving = ×(1+z*).
    KEY (the circularity, flagged): c_s = sqrt(c2)·c and ξ = sqrt(c2)·d_H, so
    c_s = ξ·H0. Hence λ_J,com = ξ·(1+z*)/E(z*) — i.e. it REDUCES to ξ by
    construction (it is built from c_s², the CP8 fit). Returns
    (c_s_km_s, lambda_J_proper, lambda_J_comoving).
    """
    c_s = np.sqrt(c2) * C_KM_S                       # km/s
    H_z = H0 * E_lcdm(z_star)                         # km/s/Mpc
    lam_proper = c_s / H_z                            # Mpc proper
    lam_com = lam_proper * (1.0 + z_star)             # Mpc comoving
    return c_s, lam_proper, lam_com


# ---------------------------------------------------------------------------
# Dimensional transmutation: L = L_0 · exp(+c/g²). Read off the exponent.
# ---------------------------------------------------------------------------
def transmutation_exponent(L0_m: float, L_target_Mpc: float) -> float:
    """Exponent E = c/g² needed so L_0·exp(E) = L_target. E = ln(L_target/L_0)."""
    L_target_m = L_target_Mpc * MPC_M
    return float(np.log(L_target_m / L0_m))


def coupling_precision_for_factor(exponent: float, factor: float) -> float:
    """How tightly must g be tuned to land within `factor` of the target?

    L = L_0·exp(c/g²) ⇒ d ln L/d ln g = −2(c/g²) = −2·exponent. To stay within
    Δln L = ln(factor): |Δln g| = ln(factor)/(2·exponent). Returns that fractional
    precision on g (the relocated tuning). Smaller = tighter.
    """
    return np.log(factor) / (2.0 * exponent)


# ---------------------------------------------------------------------------
# CHECKS (assert known limits / ballparks; flag the built-in circularity).
# ---------------------------------------------------------------------------
def _checks() -> None:
    assert 9.0 < XI_TARGET < 10.5, XI_TARGET            # data-fit ξ≈9.5 Mpc (CP8)

    z_eq, k_eq, k_eq_inv = k_eq_inv_Mpc()
    # equality redshift in the known ballpark (~3400) and 1/k_eq in tens–150 Mpc
    assert 2500 < z_eq < 4000, z_eq
    assert 30.0 < k_eq_inv < 150.0, k_eq_inv
    # cross-check against the textbook fitting form k_eq ≈ 0.073 Ω_m h² Mpc^-1
    k_eq_fit = 0.073 * OMMH2
    assert abs(k_eq - k_eq_fit) / k_eq_fit < 0.15, (k_eq, k_eq_fit)

    R8 = 8.0 / H_LITTLE
    assert 11.0 < R8 < 13.0, R8                          # nonlinear/σ8 scale ≈12 Mpc

    R_caus = causal_horizon_z2_Mpc()
    assert 4000 < R_caus < 5000, R_caus                  # ~4400 Mpc (CP20)

    # CIRCULARITY CHECK (flagged): λ_J,com must equal ξ·(1+z*)/E(z*) to machine
    # precision — i.e. the Jeans scale reduces to ξ BY CONSTRUCTION (built from c_s²).
    _, _, lam_com = jeans_comoving_Mpc(C2_FIT)
    expected = XI_TARGET * (1.0 + 2.0) / E_lcdm(2.0)
    assert abs(lam_com - expected) / expected < 1e-9, (lam_com, expected)
    assert 8.0 < lam_com < 11.0, lam_com                 # lands on ξ (circular)

    print(f"checks PASS: ξ_target={XI_TARGET:.2f} Mpc | z_eq={z_eq:.0f}, "
          f"1/k_eq={k_eq_inv:.1f} Mpc (fit {1/k_eq_fit:.1f}) | R8={R8:.2f} | "
          f"horizon@z2={R_caus:.0f} | λ_J,com={lam_com:.2f}≈ξ (CIRCULAR by construction)")


# ---------------------------------------------------------------------------
def main() -> None:
    _checks()

    z_eq, k_eq, k_eq_inv = k_eq_inv_Mpc()
    R8 = 8.0 / H_LITTLE                                  # nonlinear/σ8 scale [Mpc]
    R_caus = causal_horizon_z2_Mpc()                    # comoving horizon @z~2
    c_s, lam_proper, lam_com = jeans_comoving_Mpc(C2_FIT)
    R_DRAG = 147.09          # representative/cited: Planck 2018 (Aghanim+ 2020), Mpc

    # transmutation exponents from a micro L_0 up to 10 Mpc
    exp_planck = transmutation_exponent(L_PLANCK_M, 10.0)
    exp_darkconf = transmutation_exponent(L_DARKCONF_M, 10.0)
    # relocated coupling precision to land within a factor of 2 of 10 Mpc
    prec_planck = coupling_precision_for_factor(exp_planck, 2.0)

    # ---- ledger: ORIGIN | scale | vs ξ | category | note -----------------
    ledger = [
        # name, scale_Mpc, category, note
        ("matter–radiation equality  1/k_eq", k_eq_inv, "wrong-size",
         f"horizon @ z_eq≈{z_eq:.0f}, set by Ω_m h²; ~{k_eq_inv/XI_TARGET:.0f}× too big, not ξ"),
        ("sound horizon at drag  r_d", R_DRAG, "wrong-size",
         "representative (Planck2018, cited); ~15× too big, not ξ"),
        ("nonlinear / σ8 scale  R8=8/h", R8, "circular",
         "ξ LANDS here, but R8 is fixed by STANDARD physics (Ω_m h², P(k), transfer) "
         "→ matching it = zero independent evidence"),
        ("dark-fluid Jeans  λ_J=c_s/H @z*=2", lam_com, "circular",
         "= ξ·(1+z*)/E(z*) BY CONSTRUCTION; built from c_s² (the CP8 fit) → circular"),
        ("causal/Kibble horizon @z~2", R_caus, "wrong-size",
         f"comoving Hubble radius; {R_caus/XI_TARGET:.0f}× too big (CP20/CP21)"),
        ("dimensional transmutation  L0·exp(c/g²)", 10.0, "relocated",
         f"reaches 10 Mpc only by choosing g (exp≈{exp_planck:.0f} from Planck L0); "
         f"relocates tuning, does not pick 10 Mpc"),
    ]

    print(f"\nξ target (data)         : {XI_TARGET:.2f} Mpc  (c_s²={C2_FIT:.1e})")
    print("\n--- scale ledger (ORIGIN | scale[Mpc] | scale/ξ | category) ---")
    for name, scale, cat, _note in ledger:
        print(f"  {name:42s} {scale:9.2f}  {scale/XI_TARGET:7.2f}×  {cat}")

    print(f"\n[transmutation] L = L_0·exp(+c/g²) up to 10 Mpc:")
    print(f"  from Planck length  L0={L_PLANCK_M:.3e} m : exponent c/g² = "
          f"ln(L_t/L0) = {exp_planck:.1f}")
    print(f"  from ~GeV^-1 (dark conf) L0={L_DARKCONF_M:.3e} m: exponent = "
          f"{exp_darkconf:.1f}")
    print(f"  PARTIAL CREDIT (honest): the exponential map converts a "
          f"~10^{exp_planck/np.log(10):.0f} length tuning into a coupling tuning;")
    print(f"  to land within ×2 of 10 Mpc, g must be set to ~{prec_planck*100:.2f}% "
          f"(d lnL/d lng = −2·exp = {-2*exp_planck:.0f}).")
    print(f"  => a real reduction of tuning, BUT still an input and it does NOT "
          f"select 10 Mpc over any other scale. RELOCATED (cf. CP21 ε).")

    # ---- figure ----------------------------------------------------------
    fig, ax = plt.subplots(1, 2, figsize=(14.5, 6.0))

    # (a) number line of comoving scales; ξ marked; R8 band highlighted.
    bar_items = [
        ("1/k_eq", k_eq_inv, "tab:gray"),
        ("r_d", R_DRAG, "tab:gray"),
        ("R8 (σ8)", R8, "tab:green"),
        ("λ_J", lam_com, "tab:orange"),
        ("horizon @z~2", R_caus, "tab:blue"),
    ]
    names = [b[0] for b in bar_items]
    xs = np.log10([b[1] for b in bar_items])
    cols = [b[2] for b in bar_items]
    ax[0].scatter(xs, range(len(names)), s=110, color=cols, zorder=5,
                  edgecolor="k", linewidth=0.5)
    for i, (n, val, _c) in enumerate(bar_items):
        ax[0].annotate(f"{n} = {val:.0f} Mpc" if val > 50 else f"{n} = {val:.1f} Mpc",
                       (xs[i], i), textcoords="offset points", xytext=(9, 3),
                       fontsize=8.5)
    ax[0].axvline(np.log10(XI_TARGET), color="purple", lw=2.2,
                  label=f"data wants ξ≈{XI_TARGET:.1f} Mpc")
    ax[0].axvspan(np.log10(R8) - 0.04, np.log10(R8) + 0.04, color="purple",
                  alpha=0.13)
    ax[0].annotate("ξ sits ON R8\n(σ8 scale = standard physics\n→ matching = CIRCULAR)",
                   (np.log10(XI_TARGET), len(names) - 0.55), fontsize=8,
                   color="purple", ha="center")
    ax[0].annotate("← too small", (np.log10(XI_TARGET) - 0.55, -0.45), fontsize=8,
                   color="gray")
    ax[0].annotate("too big →", (np.log10(R_caus) - 0.7, -0.45), fontsize=8,
                   color="gray")
    ax[0].set_yticks(range(len(names)))
    ax[0].set_yticklabels([])
    ax[0].set_ylim(-0.8, len(names) + 0.3)
    ax[0].set_xlabel("log₁₀ ( comoving length / Mpc )")
    ax[0].set_title("(a) standard scales vs ξ: ξ lands only on R8\n"
                    "(nonlinear/σ8 scale, set by standard physics)")
    ax[0].legend(fontsize=8.5, loc="lower right")
    ax[0].grid(alpha=0.3)

    # (b) origin ledger: each candidate + verdict, transmutation exponent marked.
    cat_color = {"circular": "tab:red", "relocated": "tab:orange",
                 "wrong-size": "tab:blue", "derive": "tab:green"}
    ax[1].axis("off")
    ax[1].set_title("(b) origin ledger — none DERIVES 10 Mpc")
    y = 0.96
    ax[1].text(0.0, y, "ORIGIN", fontsize=9, fontweight="bold")
    ax[1].text(0.62, y, "scale/ξ", fontsize=9, fontweight="bold")
    ax[1].text(0.80, y, "verdict", fontsize=9, fontweight="bold")
    y -= 0.05
    ax[1].plot([0, 1.0], [y, y], color="k", lw=0.7)
    for name, scale, cat, _note in ledger:
        y -= 0.135
        short = name.split("  ")[0]
        sub = name.split("  ")[1] if "  " in name else ""
        ax[1].text(0.0, y + 0.02, short, fontsize=8.5)
        if sub:
            ax[1].text(0.0, y - 0.03, sub, fontsize=7, color="dimgray")
        ax[1].text(0.62, y + 0.01, f"{scale/XI_TARGET:.2f}×", fontsize=8.5)
        ax[1].text(0.80, y + 0.01, cat, fontsize=8.5, fontweight="bold",
                   color=cat_color[cat])
    y -= 0.16
    ax[1].plot([0, 1.0], [y + 0.06, y + 0.06], color="k", lw=0.5, alpha=0.4)
    ax[1].text(0.0, y, "transmutation L=L₀·exp(c/g²):", fontsize=8.5,
               fontweight="bold")
    y -= 0.05
    ax[1].text(0.0, y, f"  exponent c/g² ≈ {exp_planck:.0f} (Planck L₀) / "
                       f"{exp_darkconf:.0f} (GeV⁻¹ L₀)", fontsize=8)
    y -= 0.045
    ax[1].text(0.0, y, f"  → converts ~10^{exp_planck/np.log(10):.0f} length tuning "
                       f"into ~{prec_planck*100:.1f}% coupling tuning;", fontsize=8)
    y -= 0.045
    ax[1].text(0.0, y, "  real reduction (partial credit) but still an input; "
                       "does not PICK 10 Mpc.", fontsize=8)
    ax[1].set_xlim(0, 1.0)
    ax[1].set_ylim(0, 1.0)

    fig.suptitle("CP24: the dark-sector scale ξ≈10 Mpc — survey + ledger "
                 "(exploratory; the scale is not derived)", fontweight="bold")
    fig.tight_layout(rect=(0, 0, 1, 0.96))
    fig.savefig("fig_cp24_scale_problem.png", dpi=130)
    fig.savefig("fig_cp24_scale_problem.svg")
    print("\nsaved fig_cp24_scale_problem.png + .svg")

    # ---- csv -------------------------------------------------------------
    with open("cp24_scale_problem_results.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["# CP24 scale problem — survey + ledger (parametrize, not derive)"])
        w.writerow(["# xi_target_Mpc", f"{XI_TARGET:.4f}", "from c_s²=4.6e-6 (CP8)"])
        w.writerow(["origin", "scale_Mpc", "ratio_to_xi", "category", "note"])
        for name, scale, cat, note in ledger:
            w.writerow([name, f"{scale:.4f}", f"{scale/XI_TARGET:.4f}", cat, note])
        # transmutation detail rows
        w.writerow(["transmutation_exponent_Planck", f"{exp_planck:.4f}", "",
                    "relocated", "c/g² = ln(10Mpc/L_Planck)"])
        w.writerow(["transmutation_exponent_GeVinv", f"{exp_darkconf:.4f}", "",
                    "relocated", "c/g² = ln(10Mpc/(1 GeV^-1))"])
        w.writerow(["transmutation_coupling_precision_x2", f"{prec_planck:.6f}", "",
                    "relocated", "fractional |Δln g| to stay within ×2 of 10 Mpc"])
        # context constants
        w.writerow(["z_eq", f"{z_eq:.2f}", "", "context", "matter–radiation equality redshift"])
        w.writerow(["Omega_m_h2", f"{OMMH2:.4f}", "", "context", "fixes k_eq & R8 (standard)"])
    print("saved cp24_scale_problem_results.csv")

    # ---- honest verdict (printed) ---------------------------------------
    print("\n=== CP24 verdict (parametrize, not derive; max-honesty) ===")
    print(f"ξ≈{XI_TARGET:.1f} Mpc lands ON R8={R8:.1f} (the nonlinear/σ8 scale). R8 is")
    print("  fixed by STANDARD physics (Ω_m h², primordial spectrum, transfer), NOT by")
    print("  the dark sector → reproducing it is CIRCULAR, zero evidential weight.")
    print("  'Matches ≠ derives.' It is NOT k_eq^-1 (~95 Mpc), r_d (~147), or the")
    print(f"  z~2 horizon (~{R_caus:.0f} Mpc, {R_caus/XI_TARGET:.0f}× too big).")
    print("  Dimensional transmutation RELOCATES the tuning into the coupling g")
    print("  (partial credit: exp map softens it to a sub-percent coupling tuning,")
    print("  but still an input and does not pick 10 Mpc). The dark-fluid Jeans scale")
    print("  equals ξ only BY CONSTRUCTION (built from c_s², the CP8 fit) → CIRCULAR.")
    print("  No candidate DERIVES 10 Mpc. QFUDS inherits the standard hierarchy/scale")
    print("  problem. 050 ceiling + observer mode UNTOUCHED; real check = CLASS, BLOCKED.")


if __name__ == "__main__":
    main()
