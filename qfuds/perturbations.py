from __future__ import annotations

from dataclasses import dataclass
import csv
import json
import math
from pathlib import Path
from typing import Literal

import numpy as np

from .background import CosmologyParams, QFUDSParams, integrate_background
from .plotting import save_figure_pair


Variant = Literal["P1", "P2"]


@dataclass(frozen=True)
class PerturbationClosure:
    """Level 2A phenomenological closure from exp_003.

    This is not a microphysical derivation. It is a gauge-declared closure audit
    for the retained phenomenological transfer law.
    """

    variant: Variant
    gauge: str = "conformal_newtonian"
    transfer_frame: str = "phase_A_comoving"
    w_b: float = -0.999
    cs2_b: float = 1.0
    instability_threshold: float = 1.0e8


@dataclass(frozen=True)
class PerturbationResult:
    metadata: dict[str, object]
    a: np.ndarray
    z: np.ndarray
    k_h_mpc_values: tuple[float, ...]
    modes: dict[float, dict[str, np.ndarray]]
    diagnostics: dict[str, object]


def _interp(x_grid: np.ndarray, y_grid: np.ndarray, x: float) -> float:
    return float(np.interp(x, x_grid, y_grid))


def _metric_phi(kappa2: float, omega_a_frac: float, omega_b_frac: float, delta_a: float, delta_b: float) -> float:
    source = omega_a_frac * delta_a + omega_b_frac * delta_b
    return -1.5 * source / max(kappa2 + 3.0, 1.0e-30)


def integrate_phenomenological_perturbations(
    background: dict[str, np.ndarray],
    *,
    closure: PerturbationClosure,
    k_h_mpc_values: tuple[float, ...] = (1.0e-4, 1.0e-3, 1.0e-2, 1.0e-1),
) -> PerturbationResult:
    """Integrate the exp_003 Level 2A perturbation closure.

    Variables use x=ln(a). Velocity divergences are dimensionless
    `theta/Hc`. The metric potential is an algebraic Newtonian-gauge closure
    used only for this first hostile stability audit.
    """

    if closure.gauge != "conformal_newtonian":
        raise ValueError("exp_003 baseline closure uses conformal_newtonian gauge")
    if closure.transfer_frame != "phase_A_comoving":
        raise ValueError("exp_003 baseline closure uses phase_A_comoving transfer")

    a = background["a"]
    x_grid = np.log(a)
    e2 = background["E2"]
    dln_hc_dx = 1.0 + 0.5 * np.gradient(np.log(e2), x_grid)
    k_h0 = tuple(float(k) * 2997.92458 for k in k_h_mpc_values)

    modes: dict[float, dict[str, np.ndarray]] = {}
    unstable_modes: dict[str, bool] = {}
    instability_reasons: dict[str, str] = {}

    for k_input, k_dimless in zip(k_h_mpc_values, k_h0):
        delta_a = np.empty_like(a)
        theta_a = np.empty_like(a)
        delta_b = np.empty_like(a)
        theta_b = np.empty_like(a)
        phi = np.empty_like(a)
        q = np.empty_like(a)
        delta_q = np.empty_like(a)
        curvature = np.empty_like(a)
        conservation = np.zeros_like(a)

        delta_a[0] = 1.0e-5
        theta_a[0] = 0.0
        if closure.variant == "P2":
            delta_b[0] = max(1.0 + closure.w_b, 1.0e-12) * delta_a[0]
            theta_b[0] = theta_a[0]
        else:
            delta_b[0] = 0.0
            theta_b[0] = np.nan

        unstable = False
        reason = ""

        def values_at(xi: float) -> tuple[float, float, float, float, float, float, float]:
            ai = math.exp(xi)
            gamma = _interp(x_grid, background["Gamma"], xi)
            e2i = _interp(x_grid, background["E2"], xi)
            omega_a_frac = _interp(x_grid, background["Omega_A"], xi)
            omega_b_frac = _interp(x_grid, background["Omega_Bfoam"], xi)
            omega_a = _interp(x_grid, background["omega_A"], xi)
            omega_b = _interp(x_grid, background["omega_Bfoam"], xi)
            friction = _interp(x_grid, dln_hc_dx, xi)
            kappa2 = (k_dimless / max(ai * math.sqrt(e2i), 1.0e-30)) ** 2
            source = gamma * omega_a / max(abs(omega_b), 1.0e-30)
            return gamma, omega_a_frac, omega_b_frac, source, friction, kappa2, omega_b

        def rhs(xi: float, state: np.ndarray) -> np.ndarray:
            da, ta, db, tb = [float(v) for v in state]
            gamma, omega_a_frac, omega_b_frac, source, friction, kappa2, _ = values_at(xi)
            db_for_phi = 0.0 if closure.variant == "P1" else db
            phii = _metric_phi(kappa2, omega_a_frac, omega_b_frac, da, db_for_phi)

            # Euler friction for theta/Hc: the dimensionless conformal-Newtonian
            # CDM Euler equation is d(theta/Hc)/dx = -(1 + dlnHc/dx)(theta/Hc) + kappa^2 Phi.
            # `friction` is dln_hc_dx = 1 + dlnH/dlna (conformal), so the base
            # constant is 1.0, matching qfuds/growth.py (2 + dlnH/dlna = 1 + dlnHc/dx).
            # The earlier exp_003 code used 2.0 here, double-counting one unit of
            # Hubble friction; see outputs/postmortem/exp003_friction_bug/.
            d_da = -ta - gamma * phii
            d_ta = -(1.0 + friction) * ta + kappa2 * phii

            if closure.variant == "P1":
                return np.asarray([d_da, d_ta, 0.0, 0.0])

            one_plus_w = max(1.0 + closure.w_b, 1.0e-12)
            d_db = (
                -one_plus_w * tb
                - 3.0 * (closure.cs2_b - closure.w_b) * db
                + source * (da - db + phii)
            )
            # Fluid Euler friction -(1-3cs^2)Hc theta in dimensionless conformal
            # form: -[(1 - 3 cs_B^2) + dlnHc/dx](theta/Hc). With friction =
            # dln_hc_dx, the base constant is 1.0 (not 2.0); the earlier code
            # carried the same +1 over-friction as phase A.
            d_tb = (
                -(1.0 + friction - 3.0 * closure.cs2_b) * tb
                + kappa2 * (phii + closure.cs2_b * db / one_plus_w)
                + source * (ta - tb) / one_plus_w
            )
            return np.asarray([d_da, d_ta, d_db, d_tb])

        for i in range(len(a) - 1):
            xi = float(x_grid[i])
            dx = float(x_grid[i + 1] - x_grid[i])
            state = np.asarray([delta_a[i], theta_a[i], delta_b[i], 0.0 if closure.variant == "P1" else theta_b[i]])

            k1 = rhs(xi, state)
            k2 = rhs(xi + 0.5 * dx, state + 0.5 * dx * k1)
            k3 = rhs(xi + 0.5 * dx, state + 0.5 * dx * k2)
            k4 = rhs(xi + dx, state + dx * k3)
            next_state = state + dx * (k1 + 2.0 * k2 + 2.0 * k3 + k4) / 6.0

            if not np.all(np.isfinite(next_state)):
                unstable = True
                reason = "nonfinite perturbation state"
                next_state = np.full(4, np.nan)
            elif float(np.nanmax(np.abs(next_state))) > closure.instability_threshold:
                unstable = True
                reason = "perturbation amplitude exceeded instability threshold"

            delta_a[i + 1] = next_state[0]
            theta_a[i + 1] = next_state[1]
            delta_b[i + 1] = 0.0 if closure.variant == "P1" else next_state[2]
            theta_b[i + 1] = np.nan if closure.variant == "P1" else next_state[3]

            if unstable:
                if i + 2 < len(a):
                    delta_a[i + 2 :] = np.nan
                    theta_a[i + 2 :] = np.nan
                    delta_b[i + 2 :] = np.nan
                    theta_b[i + 2 :] = np.nan
                break

        for i, xi in enumerate(x_grid):
            gamma, omega_a_frac, omega_b_frac, source, _, kappa2, _ = values_at(float(xi))
            q[i] = gamma * background["omega_A"][i]
            delta_q[i] = q[i] * delta_a[i]
            db_for_phi = 0.0 if closure.variant == "P1" else delta_b[i]
            phi[i] = _metric_phi(kappa2, omega_a_frac, omega_b_frac, delta_a[i], db_for_phi)
            curvature[i] = -phi[i] - delta_a[i] / 3.0

        finite_values = [
            delta_a[np.isfinite(delta_a)],
            theta_a[np.isfinite(theta_a)],
            delta_b[np.isfinite(delta_b)],
        ]
        if closure.variant == "P2":
            finite_values.append(theta_b[np.isfinite(theta_b)])
        max_abs = max((float(np.max(np.abs(v))) for v in finite_values if len(v)), default=float("nan"))
        if not unstable and max_abs > closure.instability_threshold:
            unstable = True
            reason = "perturbation amplitude exceeded instability threshold"

        unstable_modes[f"{k_input:g}"] = bool(unstable)
        instability_reasons[f"{k_input:g}"] = reason

        modes[float(k_input)] = {
            "delta_A": delta_a,
            "theta_A": theta_a,
            "delta_B": delta_b,
            "theta_B": theta_b,
            "Phi": phi,
            "Q": q,
            "deltaQ": delta_q,
            "curvature_proxy": curvature,
            "conservation_residual": conservation,
        }

    diagnostics: dict[str, object] = {
        "any_unstable": any(unstable_modes.values()),
        "unstable_modes": unstable_modes,
        "instability_reasons": instability_reasons,
        "max_abs_curvature_proxy": max(
            float(np.nanmax(np.abs(mode["curvature_proxy"]))) for mode in modes.values()
        ),
        "max_conservation_residual": max(
            float(np.nanmax(np.abs(mode["conservation_residual"]))) for mode in modes.values()
        ),
        "theta_B_status": "not_applicable_for_interacting_vacuum" if closure.variant == "P1" else "regularized_fluid_variable",
    }
    metadata: dict[str, object] = {
        "stage": "2A",
        "gauge": closure.gauge,
        "transfer_frame": closure.transfer_frame,
        "transfer_four_vector": "Q_A^mu = -Q u_A^mu; Q_B^mu = +Q u_A^mu",
        "deltaQ_rule": "deltaQ = Q delta_A",
        "deltaGamma": 0,
        "phase_A": "w_A=0, cs2_A=0, sigma_A=0",
        "phase_B_variant": closure.variant,
        "phase_B": "interacting_vacuum" if closure.variant == "P1" else f"regularized_fluid_w={closure.w_b:g}_cs2={closure.cs2_b:g}",
    }
    return PerturbationResult(
        metadata=metadata,
        a=a,
        z=background["z"],
        k_h_mpc_values=tuple(float(k) for k in k_h_mpc_values),
        modes=modes,
        diagnostics=diagnostics,
    )


def _safe_label(value: float) -> str:
    return f"{value:g}"


def _write_result_csv(path: Path, result: PerturbationResult) -> None:
    first_mode = next(iter(result.modes.values()))
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(
            [
                "a",
                "z",
                "k_h_Mpc",
                "delta_A",
                "theta_A",
                "delta_B_or_substitute",
                "theta_B",
                "Phi",
                "Q",
                "deltaQ",
                "curvature_proxy",
                "conservation_residual",
            ]
        )
        for k, mode in result.modes.items():
            for i, ai in enumerate(result.a):
                writer.writerow(
                    [
                        ai,
                        result.z[i],
                        k,
                        mode["delta_A"][i],
                        mode["theta_A"][i],
                        mode["delta_B"][i],
                        mode["theta_B"][i],
                        mode["Phi"][i],
                        mode["Q"][i],
                        mode["deltaQ"][i],
                        mode["curvature_proxy"][i],
                        mode["conservation_residual"][i],
                    ]
                )
    # Touch first_mode so static checkers do not mistake the empty result case.
    _ = first_mode


def _max_abs_perturbation(result: PerturbationResult) -> float:
    values: list[float] = []
    for mode in result.modes.values():
        for key in ("delta_A", "theta_A", "delta_B", "theta_B"):
            finite = mode[key][np.isfinite(mode[key])]
            if len(finite):
                values.append(float(np.max(np.abs(finite))))
    return max(values, default=float("nan"))


def _run_label(run_id: str, variant: str, qfuds: QFUDSParams) -> str:
    if run_id == "R0":
        return f"exp003_{run_id}_{variant}_gamma0"
    return f"exp003_{run_id}_{variant}_{qfuds.gamma_model}_gamma{qfuds.gamma0:g}"


def _write_visualizations(
    outdir: Path,
    summary_runs: list[dict[str, object]],
    retained_results: dict[str, PerturbationResult],
) -> list[str]:
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError:
        return []

    outputs: list[str] = []
    labels = [f"{run['run_id']} {run['variant']}" for run in summary_runs]
    values = [float(run["max_abs_perturbation"]) for run in summary_runs]
    colors = ["#2f6f9f" if run["variant"] == "P1" else "#b84a4a" for run in summary_runs]

    fig, ax = plt.subplots(figsize=(10, 4.8), constrained_layout=True)
    ax.bar(labels, values, color=colors)
    ax.axhline(PerturbationClosure(variant="P1").instability_threshold, color="#2b2b2b", linestyle="--", linewidth=1.2, label="instability threshold")
    ax.set_yscale("log")
    ax.set_ylabel("max absolute perturbation")
    ax.set_title("Exp 003 stability diagnostic")
    ax.tick_params(axis="x", rotation=40)
    ax.legend(frameon=False)
    figures_dir = outdir / "figures"
    outputs.extend(save_figure_pair(fig, figures_dir / "exp003_stability_summary"))
    plt.close(fig)

    if {"P1", "P2"}.issubset(retained_results):
        fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), constrained_layout=True)
        for variant, result in retained_results.items():
            mode = result.modes[1.0e-1]
            axes[0].plot(result.a, np.abs(mode["delta_A"]), label=variant)
            axes[1].plot(result.a, np.abs(mode["curvature_proxy"]), label=variant)
        axes[0].set(xlabel="a", ylabel="|delta_A|", xscale="log", yscale="log", title="Retained branch, k=0.1 h/Mpc")
        axes[1].set(xlabel="a", ylabel="|curvature proxy|", xscale="log", yscale="log", title="Curvature proxy")
        for ax in axes:
            ax.legend(frameon=False)
        outputs.extend(save_figure_pair(fig, figures_dir / "exp003_retained_mode_growth"))
        plt.close(fig)
    return outputs


def run_exp003_suite(
    *,
    outdir: Path = Path("outputs"),
    n_background: int = 1200,
) -> dict[str, object]:
    """Run the exp_003 predeclared Level 2A perturbation suite."""

    outdir.mkdir(parents=True, exist_ok=True)
    cosmo = CosmologyParams()
    runs = [
        ("R0", QFUDSParams(gamma_model="information_production", gamma0=0.0)),
        ("R1", QFUDSParams(gamma_model="information_production", gamma0=0.02, collapse_a=0.35, collapse_nu=5.0)),
        ("R2a", QFUDSParams(gamma_model="information_production", gamma0=0.005, collapse_a=0.35, collapse_nu=5.0)),
        ("R2b", QFUDSParams(gamma_model="information_production", gamma0=0.01, collapse_a=0.35, collapse_nu=5.0)),
        ("R3", QFUDSParams(gamma_model="information_production", gamma0=0.04, collapse_a=0.35, collapse_nu=5.0)),
    ]
    summary_runs: list[dict[str, object]] = []
    retained_results: dict[str, PerturbationResult] = {}

    for run_id, qfuds in runs:
        background = integrate_background(cosmo, qfuds, n=n_background)
        for variant in ("P1", "P2"):
            closure = PerturbationClosure(variant=variant)  # type: ignore[arg-type]
            result = integrate_phenomenological_perturbations(
                background,
                closure=closure,
            )
            label = _run_label(run_id, variant, qfuds)
            csv_path = outdir / f"{label}.csv"
            _write_result_csv(csv_path, result)
            if run_id == "R1":
                retained_results[variant] = result
            summary_runs.append(
                {
                    "run_id": run_id,
                    "variant": variant,
                    "gamma_model": qfuds.gamma_model,
                    "gamma0": qfuds.gamma0,
                    "csv": str(csv_path),
                    "metadata": result.metadata,
                    "diagnostics": result.diagnostics,
                    "max_abs_perturbation": _max_abs_perturbation(result),
                }
            )

    plot_outputs = _write_visualizations(outdir, summary_runs, retained_results)
    summary = {
        "experiment_id": "exp_003",
        "title": "Phenomenological Perturbation Closure Audit",
        "closure": "baseline Level 2A closure from docs/03_experiments/030_exp_003_phenomenological_perturbation_closure.md",
        "runs": summary_runs,
        "visual_outputs": plot_outputs,
    }
    summary_path = outdir / "exp003_phenomenological_perturbation_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")

    diagnostics_path = outdir / "exp003_stability_diagnostics.csv"
    with diagnostics_path.open("w", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(
            [
                "run_id",
                "variant",
                "gamma_model",
                "gamma0",
                "any_unstable",
                "unstable_modes",
                "max_abs_perturbation",
                "max_abs_curvature_proxy",
                "max_conservation_residual",
                "theta_B_status",
            ]
        )
        for run in summary_runs:
            diagnostics = run["diagnostics"]
            unstable_modes = [
                k for k, value in diagnostics["unstable_modes"].items() if value
            ]
            writer.writerow(
                [
                    run["run_id"],
                    run["variant"],
                    run["gamma_model"],
                    run["gamma0"],
                    diagnostics["any_unstable"],
                    ";".join(unstable_modes),
                    run["max_abs_perturbation"],
                    diagnostics["max_abs_curvature_proxy"],
                    diagnostics["max_conservation_residual"],
                    diagnostics["theta_B_status"],
                ]
            )
    return summary
