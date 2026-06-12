"""
State-variable toy: can a relaxing order parameter φ(a) GENERATE the hand-drawn
w(a)=tanh, instead of us drawing it? (order parameter relaxing in a free energy.)

This is the rigorous form of the user's "invert Navier-Stokes / find the
state variable" instinct. Instead of writing w(a) by hand, we:
  1. define an order parameter φ ∈ [0,1]  (0 = phase A / DM-like, 1 = phase B / DE-like)
  2. give it a double-well free energy F(φ, a) with a tilt h(a) that flips sign
     near a_tr = 0.33 (z≈2)  -> phase A favored early, phase B favored late
  3. relax φ by  dφ/dN = -M ∂F/∂φ   (N = ln a, M = mobility)
  4. read the equation of state OUT:  w_eff(a) = -φ(a)   (w_A=0, w_B=-1)

KEY QUESTION: does φ-dynamics merely reproduce the tanh, or does it add content
the bare tanh cannot have (lag, super-cooling, hysteresis)?

STATUS: exploratory sandbox. F and the tilt h(a) are STILL hand-chosen, so this
does NOT cross the 050 ceiling (h(a) is not derived from foam microphysics). It
only shows the *form* a real state variable would take, and what extra signatures
that form buys. Not evidence, not a roadmap change.
"""
from __future__ import annotations
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

import model as M  # shared contract: a_tr, delta_a, w_Q (the hand-drawn tanh)

A_TR = M.A_TR                 # 0.33  (z≈2)
N_TR = np.log(A_TR)           # transition in e-folds
N_I  = np.log(1e-3)           # start deep in matter era
N_GRID = np.linspace(N_I, 0.0, 2000)


def tilt(N, alpha):
    """h(N): >0 early (favor φ=0, phase A), <0 late (favor φ=1, phase B)."""
    return alpha * (N_TR - N)


def dF_dphi(phi, N, barrier, alpha):
    """∂F/∂φ for F = barrier·φ²(1-φ)²  +  h(N)·(3φ²-2φ³).
    Double-well term keeps φ near 0 or 1; smooth-step tilt biases which well."""
    well = barrier * (2*phi*(1-phi)**2 - 2*phi**2*(1-phi))
    step = tilt(N, alpha) * (6*phi - 6*phi**2)      # d/dφ (3φ²-2φ³)
    return well + step


PHI_SEED = 1e-4    # residual fluctuation seed: a perfect false vacuum (φ=0) is an
                   # exact fixed point, so without a seed the transition NEVER fires
                   # (eternal super-cooling). The seed models tiny foam fluctuations.


def relax_phi(barrier, mobility, alpha, phi0=PHI_SEED):
    """Integrate dφ/dN = -M ∂F/∂φ in the logit variable s=ln(φ/(1-φ)) so that
    φ stays strictly in (0,1) without clipping (clipping the raw state lets the
    early strong tilt drive φ unphysically negative and it never recovers)."""
    s_floor = np.log(phi0 / (1.0 - phi0))   # maintained fluctuation floor

    def rhs(N, y):
        s = y[0]
        phi = 1.0 / (1.0 + np.exp(-s))
        dphi_ds = phi * (1.0 - phi)
        dphi_dN = -mobility * dF_dphi(phi, N, barrier, alpha)
        dsdN = dphi_dN / (dphi_ds + 1e-300)
        # thermal/quantum foam fluctuations hold φ at a minimum floor: don't let
        # the strong early tilt drive φ below the seed (else super-cooling is so
        # deep the late instability has no seed left to grow from).
        if s <= s_floor and dsdN < 0.0:
            dsdN = 0.0
        return [dsdN]
    s0 = s_floor
    sol = solve_ivp(rhs, (N_I, 0.0), [s0], t_eval=N_GRID,
                    method="LSODA", rtol=1e-8, atol=1e-10, max_step=0.02)
    return 1.0 / (1.0 + np.exp(-sol.y[0]))


def main():
    a = np.exp(N_GRID)
    z = 1.0 / a - 1.0

    # hand-drawn reference: w_tanh(a) -> equivalent φ_tanh = -w = (DM->DE fraction)
    w_tanh = M.w_Q(a)
    phi_tanh = -w_tanh                      # 0 -> 1 across a_tr

    alpha = 6.0                             # tilt steepness (drives the trigger)
    cases = {
        "fast relax, low barrier":  dict(barrier=2.0,  mobility=4.0,  c="tab:green"),
        "slow relax (lag)":         dict(barrier=2.0,  mobility=0.6,  c="tab:orange"),
        "high barrier (supercool)": dict(barrier=12.0, mobility=1.2,  c="tab:red"),
    }

    results = {}
    for name, p in cases.items():
        phi = relax_phi(p["barrier"], p["mobility"], alpha)
        w_eff = -phi
        # effective transition redshift = where w_eff crosses -0.5
        idx = np.argmin(np.abs(w_eff + 0.5))
        results[name] = dict(phi=phi, w=w_eff, z_tr=z[idx], **p)

    z_tr_tanh = z[np.argmin(np.abs(w_tanh + 0.5))]

    # ---- report ----
    print(f"hand-drawn tanh: effective z_transition (w=-0.5) = {z_tr_tanh:.3f}")
    for name, r in results.items():
        print(f"  {name:28s}: z_tr = {r['z_tr']:.3f}  "
              f"(lag Δz vs tanh = {r['z_tr']-z_tr_tanh:+.3f})  "
              f"w(z=0) = {r['w'][-1]:+.4f}")

    # ---- figure ----
    fig, ax = plt.subplots(1, 2, figsize=(13, 5.2))
    ax[0].plot(a, phi_tanh, "k--", lw=2, label="hand-drawn tanh (φ=-w)")
    for name, r in results.items():
        ax[0].plot(a, r["phi"], color=r["c"], lw=2, label=f"φ relaxed: {name}")
    ax[0].axvline(A_TR, color="gray", ls=":", lw=1)
    ax[0].set_xscale("log"); ax[0].set_xlabel("scale factor a")
    ax[0].set_ylabel("order parameter φ(a)  (0=A/DM, 1=B/DE)")
    ax[0].set_title("(a) φ relaxed from an equation vs the drawn curve")
    ax[0].legend(fontsize=8); ax[0].grid(alpha=0.3)

    ax[1].plot(z, w_tanh, "k--", lw=2, label="hand-drawn tanh w(a)")
    for name, r in results.items():
        ax[1].plot(z, r["w"], color=r["c"], lw=2, label=f"w_eff: {name}")
    ax[1].axvline(2.0, color="gray", ls=":", lw=1, label="z=2")
    ax[1].set_xlim(0, 5); ax[1].set_xlabel("redshift z")
    ax[1].set_ylabel("w_eff(z) = -φ(z)")
    ax[1].set_title("(b) equation of state OUT of φ-dynamics")
    ax[1].legend(fontsize=8); ax[1].grid(alpha=0.3)

    fig.suptitle("State-variable toy — does φ generate w(a)? (exploratory)",
                 fontweight="bold")
    fig.tight_layout()
    fig.savefig("fig_state_variable.png", dpi=130)
    fig.savefig("fig_state_variable.svg")
    print("saved fig_state_variable.png")
    print("saved fig_state_variable.svg")

    # --- CSV dump ---
    import csv as _csv
    _csv_path = "state_variable_results.csv"
    with open(_csv_path, "w", newline="") as _f:
        _wr = _csv.writer(_f)
        # columns: a, z, w_tanh (reference), then phi and w_eff for each case
        _case_names = list(results.keys())
        _header = ["a", "z", "w_tanh"]
        for _cn in _case_names:
            _header += [f"phi_{_cn}", f"w_eff_{_cn}"]
        _wr.writerow(_header)
        for _i in range(len(a)):
            _row = [a[_i], z[_i], w_tanh[_i]]
            for _cn in _case_names:
                _row += [results[_cn]["phi"][_i], results[_cn]["w"][_i]]
            _wr.writerow(_row)
    print(f"saved {_csv_path}")


if __name__ == "__main__":
    main()
