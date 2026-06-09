from __future__ import annotations

import csv
from dataclasses import dataclass
import json
import math
from pathlib import Path
from typing import Any

import numpy as np

from .background import CosmologyParams, QFUDSParams, integrate_background
from .growth import integrate_growth
from .perturbations import (
    PerturbationClosure,
    PerturbationResult,
    integrate_phenomenological_perturbations,
)


K_VALUES: tuple[float, ...] = (1.0e-4, 1.0e-3, 1.0e-2, 1.0e-1)


@dataclass(frozen=True)
class Exp004Run:
    run_id: str
    label: str
    qfuds: QFUDSParams | None
    status: str
    note: str


def _retained_params() -> QFUDSParams:
    return QFUDSParams(
        gamma_model="information_production",
        gamma0=0.02,
        collapse_a=0.35,
        collapse_nu=5.0,
    )


def _integral(x: np.ndarray, y: np.ndarray) -> float:
    return float(np.trapezoid(y, x))


def _safe_rel_diff(candidate: np.ndarray, reference: np.ndarray) -> np.ndarray:
    denom = np.where(np.abs(reference) > 1.0e-30, np.abs(reference), np.nan)
    return (candidate - reference) / denom


def _rms(values: np.ndarray) -> float:
    finite = values[np.isfinite(values)]
    if len(finite) == 0:
        return float("nan")
    return float(np.sqrt(np.mean(finite * finite)))


def _max_abs(values: np.ndarray) -> float:
    finite = values[np.isfinite(values)]
    if len(finite) == 0:
        return float("nan")
    return float(np.max(np.abs(finite)))


def _fit_constant_gamma(p1: dict[str, np.ndarray]) -> float:
    x = np.log(p1["a"])
    gamma = p1["Gamma"]
    return max(_integral(x, gamma) / max(float(x[-1] - x[0]), 1.0e-30), 0.0)


def _fit_powerlaw_gamma(p1: dict[str, np.ndarray]) -> tuple[float, float]:
    a = p1["a"]
    gamma = p1["Gamma"]
    max_gamma = float(np.max(gamma))
    support = gamma > max(max_gamma * 1.0e-3, 1.0e-30)
    x = np.log(a[support])
    y = np.log(gamma[support])
    if len(x) < 2:
        return max_gamma, 0.0
    beta, log_gamma0 = np.polyfit(x, y, 1)
    return float(math.exp(log_gamma0)), float(beta)


def _effective_w_reconstruction(
    cosmo: CosmologyParams,
    p1: dict[str, np.ndarray],
) -> dict[str, np.ndarray]:
    a = p1["a"]
    matter = (cosmo.omega_b0 + cosmo.omega_a0) * a**-3
    radiation = cosmo.omega_r0 * a**-4
    rho_de = p1["E2"] - matter - radiation
    positive = rho_de > 0.0
    w = np.full_like(a, np.nan)
    if np.any(positive):
        dlnrho_dln_a = np.gradient(np.log(np.clip(rho_de, 1.0e-300, None)), np.log(a))
        w = -1.0 - dlnrho_dln_a / 3.0
    return {
        "a": a,
        "z": p1["z"],
        "rho_de_eff": rho_de,
        "w_eff_de": w,
        "positive_rho_de_eff": np.asarray(positive, dtype=bool),
    }


def _write_background_csv(
    path: Path,
    background: dict[str, np.ndarray],
    growth: dict[str, np.ndarray],
) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(
            [
                "a",
                "z",
                "Gamma",
                "H",
                "rho_A",
                "rho_B",
                "Omega_A",
                "Omega_B",
                "w_dark",
                "w_B_eff",
                "D",
                "f",
            ]
        )
        for i, ai in enumerate(background["a"]):
            writer.writerow(
                [
                    ai,
                    background["z"][i],
                    background["Gamma"][i],
                    background["H"][i],
                    background["omega_A"][i],
                    background["omega_Bfoam"][i],
                    background["Omega_A"][i],
                    background["Omega_Bfoam"][i],
                    background["w_dark"][i],
                    background["w_Bfoam_eff"][i],
                    growth["D"][i],
                    growth["f"][i],
                ]
            )


def _write_perturbation_csv(path: Path, result: PerturbationResult) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(
            [
                "a",
                "z",
                "k_h_Mpc",
                "delta_A",
                "theta_A",
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
                        mode["Phi"][i],
                        mode["Q"][i],
                        mode["deltaQ"][i],
                        mode["curvature_proxy"][i],
                        mode["conservation_residual"][i],
                    ]
                )


def _write_effective_w_csv(path: Path, reconstruction: dict[str, np.ndarray]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(["a", "z", "rho_de_eff", "w_eff_de", "positive_rho_de_eff"])
        for i, ai in enumerate(reconstruction["a"]):
            writer.writerow(
                [
                    ai,
                    reconstruction["z"][i],
                    reconstruction["rho_de_eff"][i],
                    reconstruction["w_eff_de"][i],
                    bool(reconstruction["positive_rho_de_eff"][i]),
                ]
            )


def _gamma_shape_metrics(candidate: dict[str, np.ndarray], p1: dict[str, np.ndarray]) -> dict[str, float]:
    p1_gamma = p1["Gamma"]
    cand_gamma = candidate["Gamma"]
    max_gamma = max(float(np.max(p1_gamma)), 1.0e-30)
    support = p1_gamma > max_gamma * 1.0e-3
    p1_norm = p1_gamma[support] / max_gamma
    cand_norm = cand_gamma[support] / max_gamma
    diff = cand_norm - p1_norm
    return {
        "gamma_rms_error": _rms(diff),
        "gamma_max_error": _max_abs(diff),
    }


def _background_metrics(candidate: dict[str, np.ndarray], p1: dict[str, np.ndarray]) -> dict[str, float]:
    mask = p1["a"] >= 1.0e-3
    rho_a_rel = _safe_rel_diff(candidate["omega_A"], p1["omega_A"])
    rho_b_rel = _safe_rel_diff(candidate["omega_Bfoam"], p1["omega_Bfoam"])
    return {
        "h_max_abs_error": _max_abs(candidate["H"][mask] / p1["H"][mask] - 1.0),
        "rho_a_max_rel_error": _max_abs(rho_a_rel),
        "rho_b_max_rel_error": _max_abs(rho_b_rel),
        "w_dark_max_abs_error": _max_abs(candidate["w_dark"][mask] - p1["w_dark"][mask]),
    }


def _growth_metrics(candidate: dict[str, np.ndarray], p1: dict[str, np.ndarray]) -> dict[str, float]:
    mask = (p1["a"] >= 0.02) & (p1["a"] <= 0.5)
    return {
        "f_max_abs_error": _max_abs(candidate["f"][mask] - p1["f"][mask]),
    }


def _perturbation_metrics(candidate: PerturbationResult, p1: PerturbationResult) -> dict[str, float | bool]:
    rms_by_mode: list[float] = []
    for k in K_VALUES:
        cand_delta = candidate.modes[k]["delta_A"]
        p1_delta = p1.modes[k]["delta_A"]
        rel = _safe_rel_diff(cand_delta, p1_delta)
        rms_by_mode.append(_rms(rel))
    return {
        "delta_a_rms_rel_error_max_over_k": max(rms_by_mode),
        "same_stability_flags": candidate.diagnostics["unstable_modes"] == p1.diagnostics["unstable_modes"],
        "any_unstable": bool(candidate.diagnostics["any_unstable"]),
    }


def _classify_metrics(metrics: dict[str, Any], *, has_perturbations: bool) -> str:
    if metrics.get("exact_mapping"):
        return "exact_equivalence"
    background_ok = (
        metrics.get("h_max_abs_error", float("inf")) <= 0.005
        and metrics.get("rho_a_max_rel_error", float("inf")) <= 0.02
        and metrics.get("rho_b_max_rel_error", float("inf")) <= 0.02
        and metrics.get("w_dark_max_abs_error", float("inf")) <= 0.02
    )
    transfer_ok = (
        metrics.get("gamma_rms_error", float("inf")) <= 0.05
        and metrics.get("gamma_max_error", float("inf")) <= 0.15
    )
    growth_ok = metrics.get("f_max_abs_error", float("inf")) <= 0.05
    if not has_perturbations:
        return "background_degenerate" if background_ok else "unresolved"
    perturbation_ok = (
        metrics.get("delta_a_rms_rel_error_max_over_k", float("inf")) <= 0.05
        and bool(metrics.get("same_stability_flags", False))
    )
    if background_ok and transfer_ok and growth_ok and perturbation_ok:
        return "approximate_equivalence"
    if background_ok and not perturbation_ok:
        return "background_degenerate"
    if not transfer_ok and not background_ok:
        return "parameterization_difference"
    return "phenomenological_difference"


def run_exp004_suite(
    *,
    outdir: Path = Path("outputs"),
    n_background: int = 1200,
) -> dict[str, Any]:
    """Run Exp 004 model-family positioning diagnostics.

    This executes the approved Level 2A comparison design. It does not introduce
    a new physical branch or change the declared P1 closure.
    """

    outdir.mkdir(parents=True, exist_ok=True)
    cosmo = CosmologyParams()

    p1_params = _retained_params()
    p1_background = integrate_background(cosmo, p1_params, n=n_background)
    p1_growth = integrate_growth(p1_background)

    constant_gamma = _fit_constant_gamma(p1_background)
    powerlaw_gamma0, powerlaw_beta = _fit_powerlaw_gamma(p1_background)

    runs = [
        Exp004Run(
            "R0",
            "LCDM / Gamma(a)=0",
            QFUDSParams(gamma_model="information_production", gamma0=0.0, collapse_a=0.35, collapse_nu=5.0),
            "implemented",
            "LCDM null limit.",
        ),
        Exp004Run("R1", "retained P1", p1_params, "implemented", "Retained P1 reference."),
        Exp004Run(
            "R2",
            "interacting vacuum with xi(a)=Gamma(a)",
            p1_params,
            "implemented_exact_mapping",
            "Same background and Level 2A P1 vacuum closure as retained P1.",
        ),
        Exp004Run(
            "R3",
            "generic time-dependent IDE with xi(a)=Gamma(a)",
            None,
            "analytic_subset_mapping",
            "Not an independent numerical baseline without a distinct IDE closure.",
        ),
        Exp004Run(
            "R4",
            "constant-coupling IDE/interacting vacuum matched by integrated transfer",
            QFUDSParams(gamma_model="constant", gamma0=constant_gamma),
            "implemented",
            f"constant gamma0={constant_gamma:.12g} matched to retained P1 integrated transfer.",
        ),
        Exp004Run(
            "R5",
            "power-law Gamma(a) matched by least-squares transfer shape",
            QFUDSParams(gamma_model="powerlaw", gamma0=powerlaw_gamma0, beta=powerlaw_beta),
            "implemented",
            f"powerlaw gamma0={powerlaw_gamma0:.12g}, beta={powerlaw_beta:.12g} fit over retained P1 support.",
        ),
        Exp004Run(
            "R6",
            "effective non-interacting w(a) reconstruction",
            None,
            "background_reconstruction",
            "Matches P1 background expansion by construction; no transfer perturbations.",
        ),
    ]

    backgrounds: dict[str, dict[str, np.ndarray]] = {}
    growths: dict[str, dict[str, np.ndarray]] = {}
    perturbations: dict[str, PerturbationResult] = {}

    for run in runs:
        if run.qfuds is None:
            continue
        background = integrate_background(cosmo, run.qfuds, n=n_background)
        growth = integrate_growth(background)
        perturbation = integrate_phenomenological_perturbations(
            background,
            closure=PerturbationClosure(variant="P1"),
            k_h_mpc_values=K_VALUES,
        )
        backgrounds[run.run_id] = background
        growths[run.run_id] = growth
        perturbations[run.run_id] = perturbation
        stem = f"exp004_{run.run_id}"
        _write_background_csv(outdir / f"{stem}_background_growth.csv", background, growth)
        _write_perturbation_csv(outdir / f"{stem}_p1_perturbations.csv", perturbation)

    reconstruction = _effective_w_reconstruction(cosmo, p1_background)
    _write_effective_w_csv(outdir / "exp004_R6_effective_w_reconstruction.csv", reconstruction)

    p1_perturbation = perturbations["R1"]
    baseline_rows: list[dict[str, Any]] = []
    background_rows: list[dict[str, Any]] = []
    transfer_rows: list[dict[str, Any]] = []

    for run in runs:
        row: dict[str, Any] = {
            "run_id": run.run_id,
            "label": run.label,
            "status": run.status,
            "note": run.note,
        }
        if run.run_id == "R3":
            row.update(
                {
                    "classification": "generic_IDE_subset_mapping",
                    "exact_mapping": True,
                    "has_perturbations": False,
                }
            )
            baseline_rows.append(row)
            continue
        if run.run_id == "R6":
            h_error = _max_abs(reconstruction["rho_de_eff"] + (cosmo.omega_b0 + cosmo.omega_a0) * p1_background["a"] ** -3 + cosmo.omega_r0 * p1_background["a"] ** -4 - p1_background["E2"])
            row.update(
                {
                    "classification": "background_degenerate",
                    "exact_mapping": True,
                    "has_perturbations": False,
                    "background_reconstruction_max_abs_e2_error": h_error,
                    "positive_rho_de_eff_all": bool(np.all(reconstruction["positive_rho_de_eff"])),
                }
            )
            baseline_rows.append(row)
            continue

        background = backgrounds[run.run_id]
        growth = growths[run.run_id]
        metrics: dict[str, Any] = {}
        metrics.update(_gamma_shape_metrics(background, p1_background))
        metrics.update(_background_metrics(background, p1_background))
        metrics.update(_growth_metrics(growth, p1_growth))
        metrics.update(_perturbation_metrics(perturbations[run.run_id], p1_perturbation))
        metrics["exact_mapping"] = run.run_id in {"R1", "R2"}
        classification = "exact_equivalence" if metrics["exact_mapping"] else _classify_metrics(metrics, has_perturbations=True)
        row.update(metrics)
        row["classification"] = classification
        row["has_perturbations"] = True
        baseline_rows.append(row)
        background_rows.append({k: row[k] for k in row if k in {"run_id", "label", "classification", "h_max_abs_error", "rho_a_max_rel_error", "rho_b_max_rel_error", "w_dark_max_abs_error", "f_max_abs_error", "delta_a_rms_rel_error_max_over_k", "same_stability_flags", "any_unstable"}})
        transfer_rows.append({k: row[k] for k in row if k in {"run_id", "label", "classification", "gamma_rms_error", "gamma_max_error"}})

    closure_rows = [
        {
            "comparison": "P1 retained closure",
            "transfer_frame": "phase-A-comoving",
            "phase_b_treatment": "exact interacting vacuum",
            "deltaq_transfer": "deltaQ = Q delta_A; deltaGamma = 0",
            "classification": "implemented baseline",
        },
        {
            "comparison": "Geodesic-CDM interacting vacuum",
            "transfer_frame": "CDM/phase-A frame",
            "phase_b_treatment": "interacting vacuum",
            "deltaq_transfer": "maps to the declared P1 phase-A-frame closure at this audit level",
            "classification": "closure_equivalent within Level 2A",
        },
        {
            "comparison": "Generic time-dependent IDE",
            "transfer_frame": "must be declared",
            "phase_b_treatment": "vacuum or non-vacuum DE must be declared",
            "deltaq_transfer": "not independent unless a distinct closure is supplied",
            "classification": "generic_IDE_subset_mapping",
        },
        {
            "comparison": "Alternate momentum-transfer frame",
            "transfer_frame": "non-phase-A frame",
            "phase_b_treatment": "declared by baseline",
            "deltaq_transfer": "not implemented",
            "classification": "unresolved",
        },
        {
            "comparison": "Effective non-interacting w(a) reconstruction",
            "transfer_frame": "none",
            "phase_b_treatment": "non-interacting effective dark energy",
            "deltaq_transfer": "no physical transfer perturbation",
            "classification": "background_degenerate only",
        },
    ]

    reduction_rows = [
        {"limit": "Gamma(a) -> 0", "classification": "LCDM null limit", "evidence": "R0"},
        {"limit": "Gamma(a) = const", "classification": "constant-coupling IDE/interacting-vacuum limit; not approximately equivalent to retained P1 at matched integrated transfer", "evidence": "R4"},
        {"limit": "arbitrary Gamma(a)", "classification": "generic time-dependent IDE/interacting-vacuum model", "evidence": "R3 analytic mapping"},
        {"limit": "xi(a) = Gamma(a)", "classification": "direct interacting-vacuum/IDE subset mapping", "evidence": "R2/R3"},
        {"limit": "w_B = -1 with transfer along u_A^mu", "classification": "interacting vacuum in phase-A/geodesic frame", "evidence": "P1 closure"},
        {"limit": "background-only H(a) matching", "classification": "effective non-interacting w(a) degeneracy at background level", "evidence": "R6"},
    ]

    def write_rows(path: Path, rows: list[dict[str, Any]]) -> None:
        fields = sorted({key for row in rows for key in row})
        with path.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(rows)

    write_rows(outdir / "exp004_baseline_comparison.csv", baseline_rows)
    write_rows(outdir / "exp004_background_equivalence.csv", background_rows)
    write_rows(outdir / "exp004_transfer_reconstruction.csv", transfer_rows)
    write_rows(outdir / "exp004_closure_frame_mapping.csv", closure_rows)
    write_rows(outdir / "exp004_reduction_limits.csv", reduction_rows)

    summary = {
        "experiment_id": "exp_004",
        "title": "Retained P1 Model-Family Positioning and Equivalence Map",
        "classification": {
            "closest_model_family": "interacting vacuum; subset of time-dependent IDE",
            "primary_outcome": "exact_interacting_vacuum_instance",
            "secondary_outcome": "generic_IDE_equivalent under xi(a)=Gamma(a)",
            "remaining_differences": "parameterization-only for the retained source-shaped Gamma(a) within Level 2A; alternate frames unresolved",
            "physical_difference": False,
        },
        "fit_parameters": {
            "R4_constant_gamma0": constant_gamma,
            "R5_powerlaw_gamma0": powerlaw_gamma0,
            "R5_powerlaw_beta": powerlaw_beta,
        },
        "baseline_comparison": baseline_rows,
        "closure_frame_mapping": closure_rows,
        "reduction_limits": reduction_rows,
        "outputs": [
            "outputs/exp004_baseline_comparison.csv",
            "outputs/exp004_background_equivalence.csv",
            "outputs/exp004_transfer_reconstruction.csv",
            "outputs/exp004_closure_frame_mapping.csv",
            "outputs/exp004_reduction_limits.csv",
            "outputs/exp004_positioning_summary.json",
            "outputs/exp004_R6_effective_w_reconstruction.csv",
        ]
        + [
            f"outputs/exp004_{run.run_id}_background_growth.csv"
            for run in runs
            if run.qfuds is not None
        ]
        + [
            f"outputs/exp004_{run.run_id}_p1_perturbations.csv"
            for run in runs
            if run.qfuds is not None
        ],
    }
    summary_path = outdir / "exp004_positioning_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2, sort_keys=True), encoding="utf-8")
    return summary
