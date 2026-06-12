"""
CP23: the meV / why-now energy scale = the COSMOLOGICAL CONSTANT PROBLEM.
CP20–CP22 reduced the toy's hand-tuned spec to an irreducible floor of TWO
numbers; CP22 showed a tracker frees the initial conditions but NOT the energy
scale ρ_Λ ≈ (2.3 meV)^4. CP23 asks the honest survey question about that one
surviving number: do the world's KNOWN approaches to "why ~meV / why doesn't the
QFT vacuum energy gravitate" DERIVE it, or do they SELECT / RELOCATE / ASSUME?

STATUS: exploratory sandbox, PARAMETRIZE-not-DERIVE. This is an HONEST SURVEY +
ASSUMPTION/TUNING LEDGER of real, published approaches — NOT a derivation, NOT
evidence, NOT a roadmap change. This CP touches the cosmological constant
problem, the deepest unsolved problem in theoretical physics. NOBODY solves it
here and nobody has solved it anywhere. The deliverable is precisely WHERE each
approach stops: derives / selects / relocates / assumes-cancellation. A confident
fabrication here would be the worst possible outcome — so: hit/fit/select is NOT
a derivation, and the observed meV value is NOT derived by any row below. Genuine
PARTIAL wins are credited honestly (dimensional transmutation makes the SMALLNESS
technically natural) but never overstated. The "050 ceiling" is untouched and
observer mode is untouched. The real check is CLASS/hi_class at Level 3, BLOCKED.

Survey rows (each a ledger entry APPROACH | ASSUMES | DERIVES vs SELECTS/RELOCATES
| verdict), with the numbers that make the problem concrete:
  1. Naive QFT vacuum energy ρ_vac ~ M_cutoff^4 for M_cutoff ∈ {Planck, TeV/SUSY,
     electroweak}; ratio ρ_vac/ρ_Λ_obs → the famous ~10^120 (Planck) and
     ~10^55–10^59 (EW/TeV). This is THE PROBLEM, quantified. category=problem.
  2. Weinberg (1987) anthropic bound: structure must form before Λ-domination ⇒
     ρ_Λ ≲ a few hundred × ρ_m0. Observed ρ_Λ sits ~1.7–2.4 orders BELOW that
     representative cap. Verdict: SELECTS (landscape + observer selection);
     explains the order of magnitude, derives nothing, relocates "why a
     landscape." category=selects.
  3. Dimensional transmutation / technical naturalness: M = M_pl·exp(−c/g²) is
     exponentially small from an O(1) coupling. Exponent c/g² = ln(M_pl/M_DE) ≈
     70. Verdict: the SMALLNESS is technically natural (a REAL partial win,
     credited) BUT (a) it still needs the right O(1) coupling (an input) and
     (b) it addresses a POTENTIAL scale, not the vacuum-energy CC problem
     (ρ_vac ~ M_cutoff^4 is NOT exp-suppressed). Does not solve the actual
     problem. category=partial.
  4. One-liners: SUSY (broken ⇒ wrong scale m_SUSY^4), sequestering / unimodular
     / vacuum-energy-decoupling (Kaloper–Padilla: Λ becomes a global integration
     constant ⇒ does not gravitate, but its VALUE is an unexplained boundary/
     historic average — relocated), swampland / de Sitter conjectures (constrain
     but do not fix the value). category=relocates. Cited where possible; the
     numeric anthropic ceiling is representative (Weinberg 1987, PRL 59, 2607).

Outputs (working dir): cp23_cc_problem.py / .png / .svg / _results.csv
Exploratory; survey + ledger, NOT a solution. hit/select ≠ derivation.
050 + observer untouched; real check = CLASS/hi_class Level 3, BLOCKED.
"""
from __future__ import annotations
import csv
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M

# ---------------------------------------------------------------------------
# fundamental scales (GeV), and the observed dark-energy scale
# ---------------------------------------------------------------------------
M_PL_GEV = 1.22e19          # full Planck mass  (GeV)
M_PL_RED_GEV = 2.4e18       # reduced Planck mass M_pl/sqrt(8πG) (GeV)
M_TEV_GEV = 1.0e3           # SUSY-breaking proxy ~ TeV (GeV)
M_EW_GEV = 246.0            # electroweak (Higgs vev) scale (GeV)
GEV_PER_MEV = 1.0e-12       # 1 meV = 1e-3 eV = 1e-12 GeV

# ρ_Λ_obs = Ω_Λ · ρ_crit,0, expressed as a (meV)^4 scale, consistent with CP22:
#   ρ_c0^{1/4} ≈ 2.5 meV (standard), so m_DE ≡ ρ_Λ^{1/4} = Ω_Λ^{1/4} · 2.5 meV.
RHO_C0_QUARTER_MEV = 2.5
OMEGA_L = M.OMEGA_L0_LCDM   # 0.685
OMEGA_M = M.OMEGA_M0_LCDM   # 0.315

M_DE_MEV = OMEGA_L ** 0.25 * RHO_C0_QUARTER_MEV     # ≈ 2.27 meV — the DE scale
M_DE_GEV = M_DE_MEV * GEV_PER_MEV
RHO_L_GEV4 = M_DE_GEV ** 4                          # ρ_Λ_obs in GeV^4 = (meV)^4

# representative anthropic ceiling (Weinberg 1987): ρ_Λ ≲ N·ρ_m0, N ~ few hundred
WEINBERG_N_LO, WEINBERG_N_HI = 100.0, 500.0


def rho_vac_over_rho_L(M_cutoff_GeV):
    """Naive QFT vacuum energy ρ_vac ~ M_cutoff^4, as a ratio to observed ρ_Λ."""
    return (M_cutoff_GeV ** 4) / RHO_L_GEV4


def transmutation_exponent(M_pl_GeV, M_target_GeV):
    """c/g² such that M_target = M_pl·exp(−c/g²)  ⇒  c/g² = ln(M_pl/M_target)."""
    return np.log(M_pl_GeV / M_target_GeV)


# ---------------------------------------------------------------------------
# CHECKS: assert known limits/identities before trusting any number
# ---------------------------------------------------------------------------
def _checks():
    # (1) the DE scale really is ~2.3 meV (the famous value)
    assert 2.2 < M_DE_MEV < 2.4, M_DE_MEV
    # (2) Planck vacuum-energy ratio is the famous ~120 orders
    lr_planck = np.log10(rho_vac_over_rho_L(M_PL_GEV))
    assert 118.0 < lr_planck < 126.0, lr_planck
    # (3) transmutation limit: c/g²=0 ⇒ M=M_pl (no suppression); and the exponent
    #     reproduces M_DE: M_pl·exp(−exponent) == M_DE within float tol.
    assert abs(M_PL_RED_GEV * np.exp(-0.0) - M_PL_RED_GEV) < 1e-6 * M_PL_RED_GEV
    expo = transmutation_exponent(M_PL_RED_GEV, M_DE_GEV)
    assert abs(M_PL_RED_GEV * np.exp(-expo) - M_DE_GEV) / M_DE_GEV < 1e-9
    assert 65.0 < expo < 75.0, expo                    # ~70-ish from O(1) coupling
    # (4) Weinberg: observed ρ_Λ/ρ_m0 = Ω_Λ/Ω_m, the well-known O(2) coincidence,
    #     and it must sit BELOW the representative anthropic cap.
    obs_ratio = OMEGA_L / OMEGA_M
    assert 1.5 < obs_ratio < 3.0, obs_ratio
    assert obs_ratio < WEINBERG_N_LO, obs_ratio        # observed below the ceiling
    print(f"checks PASS: m_DE={M_DE_MEV:.2f} meV, log10(rho_Planck/rho_L)="
          f"{lr_planck:.1f}, transmutation exponent={expo:.1f}, "
          f"obs rho_L/rho_m0={obs_ratio:.2f}")


def main():
    _checks()

    # ----- Row 1: naive QFT vacuum energy — THE PROBLEM, quantified ---------
    cutoffs = {
        "Planck (1.22e19 GeV)": M_PL_GEV,
        "SUSY/TeV (1e3 GeV)":   M_TEV_GEV,
        "electroweak (246 GeV)": M_EW_GEV,
    }
    ratios = {name: rho_vac_over_rho_L(Mc) for name, Mc in cutoffs.items()}
    log_ratios = {name: np.log10(r) for name, r in ratios.items()}
    print(f"\n[Row 1] naive QFT vacuum energy ρ_vac ~ M_cutoff^4 vs observed "
          f"ρ_Λ=({M_DE_MEV:.2f} meV)^4:")
    for name in cutoffs:
        print(f"   M_cutoff={name:22s} ρ_vac/ρ_Λ = 10^{log_ratios[name]:.1f}")
    print(f"   => the famous ~10^{log_ratios['Planck (1.22e19 GeV)']:.0f} (Planck) "
          f"and ~10^{log_ratios['SUSY/TeV (1e3 GeV)']:.0f} (TeV) discrepancy. "
          f"category=PROBLEM (this is the CC problem itself).")

    # ----- Row 2: Weinberg anthropic bound — SELECTS -----------------------
    obs_ratio = OMEGA_L / OMEGA_M                          # ρ_Λ/ρ_m0 observed ≈ 2.17
    orders_below_lo = np.log10(WEINBERG_N_LO / obs_ratio)  # how far below N=100 cap
    orders_below_hi = np.log10(WEINBERG_N_HI / obs_ratio)  # how far below N=500 cap
    print(f"\n[Row 2] Weinberg (1987) anthropic ceiling ρ_Λ ≲ "
          f"{WEINBERG_N_LO:.0f}–{WEINBERG_N_HI:.0f}·ρ_m0 (structure must form):")
    print(f"   observed ρ_Λ/ρ_m0 = Ω_Λ/Ω_m = {obs_ratio:.2f}; sits "
          f"{orders_below_lo:.2f}–{orders_below_hi:.2f} orders BELOW the cap.")
    print(f"   => SELECTS (multiverse + observer selection): explains the order of "
          f"magnitude, derives nothing, relocates to 'why a landscape'.")

    # ----- Row 3: dimensional transmutation — PARTIAL (smallness natural) ---
    expo_red = transmutation_exponent(M_PL_RED_GEV, M_DE_GEV)   # ~69
    expo_full = transmutation_exponent(M_PL_GEV, M_DE_GEV)      # ~71
    print(f"\n[Row 3] dimensional transmutation M = M_pl·exp(−c/g²):")
    print(f"   exponent c/g² = ln(M_pl/M_DE) = {expo_red:.1f} (reduced M_pl) / "
          f"{expo_full:.1f} (full M_pl) from an O(1) coupling.")
    print(f"   => SMALLNESS technically natural (REAL partial win). BUT needs the "
          f"right O(1) coupling (input) AND addresses a POTENTIAL scale, not the "
          f"vacuum-energy CC problem (ρ_vac~M_cutoff^4 is NOT exp-suppressed). "
          f"category=PARTIAL; does not solve the actual problem.")

    # ----- Row 4: one-line ledger rows — RELOCATE / wrong scale ------------
    oneliners = [
        ("SUSY (broken)",
         "exact SUSY ⇒ ρ_vac=0; but SUSY is broken at m_SUSY≳TeV",
         "relocates", "broken SUSY gives ρ_vac~m_SUSY^4 — wrong by ~10^59"),
        ("sequestering / unimodular (Kaloper–Padilla)",
         "Λ promoted to a global integration constant; decouples vacuum energy",
         "relocates", "Λ no longer gravitates, but its VALUE = unexplained "
                      "boundary/historic-average input"),
        ("swampland / de Sitter conjectures",
         "consistency of EFT in quantum gravity (string landscape)",
         "relocates", "constrains the value/dynamics, does NOT fix the meV scale"),
    ]
    print(f"\n[Row 4] one-liners (assume/survive):")
    for name, ass, cat, note in oneliners:
        print(f"   {name:42s} [{cat}] {note}")

    # ----- assemble the ledger (category in {problem,selects,partial,relocates})
    ledger = [
        ("Naive QFT vacuum energy", "problem",
         f"10^{log_ratios['Planck (1.22e19 GeV)']:.0f} (Planck) / "
         f"10^{log_ratios['SUSY/TeV (1e3 GeV)']:.0f} (TeV)",
         "ρ_vac~M_cutoff^4: this IS the CC problem, quantified"),
        ("Weinberg anthropic bound", "selects",
         f"obs {orders_below_lo:.1f}-{orders_below_hi:.1f} orders below cap",
         "SELECTS via landscape+observer; relocates to 'why a landscape'"),
        ("Dimensional transmutation", "partial",
         f"exponent c/g^2 = {expo_red:.0f}",
         "smallness technically natural (REAL partial); needs O(1) input + "
         "is a POTENTIAL scale, not vacuum-energy CC"),
        ("SUSY (broken)", "relocates", "~10^59 off",
         "exact SUSY ρ_vac=0, but broken SUSY ⇒ wrong scale m_SUSY^4"),
        ("Sequestering / unimodular", "relocates", "Λ = integration const",
         "decouples vacuum energy; VALUE = unexplained boundary input"),
        ("Swampland / dS conjectures", "relocates", "constraint only",
         "constrains, does not fix the meV value"),
    ]

    # =====================================================================
    # FIGURE (2 panels)
    # =====================================================================
    cat_color = {"problem": "tab:red", "selects": "tab:purple",
                 "partial": "tab:green", "relocates": "tab:orange"}

    fig, ax = plt.subplots(1, 2, figsize=(15.5, 6.4))

    # (a) energy-density ladder: log10(ρ/ρ_Λ_obs). QFT cutoffs tower ~56–123
    #     orders above; the Weinberg anthropic ceiling sits just ~2 orders above
    #     observed ρ_Λ (at 0), which is the whole point: observed is just under
    #     the anthropic cap but ~120 orders under the naive QFT estimate.
    rungs = [
        ("ρ_vac(Planck)",      log_ratios["Planck (1.22e19 GeV)"], "tab:red"),
        ("ρ_vac(SUSY/TeV)",    log_ratios["SUSY/TeV (1e3 GeV)"],   "tab:red"),
        ("ρ_vac(electroweak)", log_ratios["electroweak (246 GeV)"], "tab:red"),
        ("Weinberg cap (×500)", np.log10(WEINBERG_N_HI * (OMEGA_M / OMEGA_L)),
         "tab:purple"),
        ("Weinberg cap (×100)", np.log10(WEINBERG_N_LO * (OMEGA_M / OMEGA_L)),
         "tab:purple"),
        ("ρ_Λ observed", 0.0, "navy"),
    ]
    ys = np.arange(len(rungs))[::-1]
    for (name, val, col), y in zip(rungs, ys):
        ax[0].barh(y, val, color=col, alpha=0.75, height=0.6, zorder=3)
        ax[0].annotate(f"{name}: 10^{val:.1f}" if val >= 1 else f"{name}: 10^0",
                       (max(val, 0) + 1.5, y), va="center", fontsize=8.5)
    # bracket the ~120-order problem
    lp = log_ratios["Planck (1.22e19 GeV)"]
    ax[0].annotate("", xy=(lp, ys[0] + 0.45), xytext=(lp, ys[-1] - 0.45),
                   arrowprops=dict(arrowstyle="<->", color="gray", lw=1.2))
    ax[0].annotate(f"the\n~{lp:.0f}-order\nCC problem", (lp - 8, np.mean(ys)),
                   fontsize=9, color="gray", ha="right")
    # zoom inset note: observed sits just under the anthropic cap
    ax[0].annotate("observed ρ_Λ sits just\nUNDER the anthropic cap\n"
                   "(~2 orders), but ~120\nunder the QFT estimate",
                   xy=(0, ys[-1]), xytext=(40, ys[-1] + 0.1), fontsize=8,
                   color="navy",
                   arrowprops=dict(arrowstyle="->", color="navy", lw=1))
    ax[0].set_yticks(ys)
    ax[0].set_yticklabels([r[0] for r in rungs], fontsize=8)
    ax[0].set_xlabel("log₁₀ ( ρ / ρ_Λ,observed )")
    ax[0].set_xlim(-5, 150)
    ax[0].set_title("(a) the scale ladder: QFT vacuum energy vs observed ρ_Λ\n"
                    f"ρ_vac~M⁴ towers ~10^{lp:.0f} (Planck) / "
                    f"10^{log_ratios['SUSY/TeV (1e3 GeV)']:.0f} (TeV) above; "
                    "anthropic cap just above ρ_Λ", fontsize=9.5)
    ax[0].grid(alpha=0.3, axis="x")

    # (b) the assumption ledger: one row per approach, colored by category,
    #     verdict text + the key number; transmutation exponent marked.
    n = len(ledger)
    ax[1].set_xlim(0, 10)
    ax[1].set_ylim(-0.5, n - 0.5)
    ax[1].axis("off")
    cat_label = {"problem": "PROBLEM", "selects": "SELECTS",
                 "partial": "PARTIAL-natural", "relocates": "RELOCATES"}
    for i, (name, cat, key, note) in enumerate(ledger):
        y = n - 1 - i
        col = cat_color[cat]
        ax[1].barh(y, 2.4, left=0.0, color=col, alpha=0.8, height=0.72, zorder=2)
        ax[1].annotate(cat_label[cat], (1.2, y), va="center", ha="center",
                       fontsize=8.5, color="white", fontweight="bold")
        ax[1].annotate(name, (2.7, y + 0.16), va="center", fontsize=9,
                       fontweight="bold")
        ax[1].annotate(f"[{key}]  {note}", (2.7, y - 0.18), va="center",
                       fontsize=7.3, color="0.25")
    ax[1].annotate("exponent ≈70 ⇒ smallness natural,\nbut O(1) input + "
                   "wrong target (potential, not vacuum)",
                   (2.7, n - 1 - 2 - 0.42), fontsize=6.8, color="darkgreen")
    ax[1].set_title("(b) assumption / tuning ledger — nobody DERIVES the meV value\n"
                    "derives ✗  |  selects (anthropic)  |  partial-natural "
                    "(transmutation)  |  relocates", fontsize=9.5)

    fig.suptitle("CP23: the meV / why-now scale = the cosmological constant "
                 "problem — best approaches SELECT / RELOCATE / partially-"
                 "NATURALIZE, none DERIVE\n(exploratory; CC problem is unsolved "
                 "— survey + ledger, not a solution; hit/select ≠ derivation; "
                 "050 + observer untouched; real check = CLASS, BLOCKED)",
                 fontweight="bold", fontsize=10)
    fig.tight_layout(rect=(0, 0, 1, 0.93))
    fig.savefig("fig_cp23_cc_problem.png", dpi=130)
    fig.savefig("fig_cp23_cc_problem.svg")
    print("\nsaved fig_cp23_cc_problem.png + .svg")

    # =====================================================================
    # CSV
    # =====================================================================
    with open("cp23_cc_problem_results.csv", "w", newline="") as fh:
        w = csv.writer(fh)
        w.writerow(["# CP23 cosmological constant problem — survey + ledger; "
                    "parametrize-not-derive; hit/select != derivation; "
                    "050+observer untouched; real check CLASS Level3 BLOCKED"])
        w.writerow(["# observed dark-energy scale m_DE = Omega_L^0.25 * 2.5 meV "
                    "= %.3f meV ; rho_L = (%.3f meV)^4" % (M_DE_MEV, M_DE_MEV)])
        w.writerow([])
        w.writerow(["approach", "key_number", "category", "note"])
        # Row 1 — the problem, one line per cutoff
        for name in cutoffs:
            w.writerow([f"Naive QFT vacuum (M_cutoff={name})",
                        f"rho_vac/rho_L=1e{log_ratios[name]:.1f}", "problem",
                        "rho_vac~M_cutoff^4; this IS the CC problem quantified"])
        # Row 2 — Weinberg anthropic
        w.writerow(["Weinberg anthropic bound",
                    f"obs {orders_below_lo:.2f}-{orders_below_hi:.2f} orders below "
                    f"cap (N=100-500)", "selects",
                    "Weinberg 1987 PRL 59 2607 (representative); SELECTS via "
                    "landscape+observer; relocates to 'why a landscape'"])
        w.writerow(["  obs rho_L/rho_m0", f"{obs_ratio:.3f}", "selects",
                    "Omega_L/Omega_m, the O(2) why-now coincidence"])
        # Row 3 — transmutation
        w.writerow(["Dimensional transmutation",
                    f"exponent c/g^2={expo_red:.1f} (reduced) / {expo_full:.1f} "
                    f"(full M_pl)", "partial",
                    "smallness technically natural (REAL partial win); needs O(1) "
                    "coupling input + addresses POTENTIAL scale, not vacuum-energy CC"])
        # Row 4 — one-liners
        for name, ass, cat, note in oneliners:
            w.writerow([name, "(qualitative)", cat, note])
        w.writerow([])
        w.writerow(["## VERDICT"])
        w.writerow(["meV_value_derived_by_any_row", "NO",
                    "nobody derives the meV/why-now scale"])
        w.writerow(["net", "select/relocate/partial-natural", "hit/select != "
                    "derivation; QFUDS inherits this unsolved CC problem; 050 + "
                    "observer untouched; real check = CLASS Level3 BLOCKED"])
    print("saved cp23_cc_problem_results.csv")

    # =====================================================================
    # honest verdict (printed)
    # =====================================================================
    print("\n=== CP23 verdict (survey + ledger; hit/select != derivation) ===")
    print(f"Row 1 (QFT vacuum): ρ_vac~M^4 is ~10^{lp:.0f} (Planck) / "
          f"10^{log_ratios['SUSY/TeV (1e3 GeV)']:.0f} (TeV) too big = the CC problem.")
    print(f"Row 2 (Weinberg): anthropic cap ~{WEINBERG_N_LO:.0f}-{WEINBERG_N_HI:.0f}·"
          f"ρ_m0; observed sits ~{orders_below_lo:.1f}-{orders_below_hi:.1f} orders "
          f"under it. SELECTS, derives nothing, relocates to 'why a landscape'.")
    print(f"Row 3 (transmutation): exponent ~{expo_red:.0f} makes the SMALLNESS "
          f"technically natural (real partial win), but needs an O(1) coupling and "
          f"targets a POTENTIAL scale, not the vacuum-energy CC. Not a solution.")
    print("Row 4: SUSY (broken ⇒ wrong scale), sequestering/unimodular (Λ → "
          "integration constant ⇒ value relocated), swampland (constrains only).")
    print("=> NOBODY derives meV. Approaches select / relocate / partially-"
          "naturalize. This is the cosmological constant problem; QFUDS inherits")
    print("   it exactly as ΛCDM does. hit/select != derivation. 050 untouched,")
    print("   observer mode untouched. Real check = CLASS/hi_class Level 3 BLOCKED.")


if __name__ == "__main__":
    main()
