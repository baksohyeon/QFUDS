from __future__ import annotations

import csv
from dataclasses import dataclass
import json
import math
from pathlib import Path
from typing import Any, Callable

import numpy as np

from .background import CosmologyParams, QFUDSParams, integrate_background
from .plotting import save_figure_pair


@dataclass(frozen=True)
class TimingFamily:
    family_id: str
    label: str
    parameter_count: int
    family_class: str
    values: np.ndarray
    fit_parameters: dict[str, float]
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


def _normalize_shape(values: np.ndarray) -> np.ndarray:
    clipped = np.clip(values, 0.0, None)
    peak = float(np.max(clipped))
    if peak <= 0.0:
        return np.zeros_like(clipped)
    return clipped / peak


def _logistic_derivative(x: np.ndarray, center: float, width: float) -> np.ndarray:
    t = np.clip((x - center) / max(width, 1.0e-12), -60.0, 60.0)
    f = 1.0 / (1.0 + np.exp(-t))
    return 4.0 * f * (1.0 - f)


def _logistic_transition(x: np.ndarray, center: float, width: float) -> np.ndarray:
    t = np.clip((x - center) / max(width, 1.0e-12), -60.0, 60.0)
    return 1.0 / (1.0 + np.exp(-t))


def _gaussian_ln_a(x: np.ndarray, center: float, width: float) -> np.ndarray:
    return np.exp(-0.5 * ((x - center) / max(width, 1.0e-12)) ** 2)


def _fit_two_parameter_family(
    *,
    x: np.ndarray,
    target: np.ndarray,
    support: np.ndarray,
    centers: np.ndarray,
    widths: np.ndarray,
    builder: Callable[[np.ndarray, float, float], np.ndarray],
) -> tuple[np.ndarray, dict[str, float], float]:
    best_values = np.zeros_like(target)
    best_params = {"center_ln_a": float("nan"), "width_ln_a": float("nan")}
    best_rms = float("inf")
    for center in centers:
        for width in widths:
            values = _normalize_shape(builder(x, float(center), float(width)))
            rms = _rms(values[support] - target[support])
            if rms < best_rms:
                best_rms = rms
                best_values = values
                best_params = {
                    "center_ln_a": float(center),
                    "width_ln_a": float(width),
                    "center_z": float(math.exp(-float(center)) - 1.0),
                }
    return best_values, best_params, best_rms


def _fit_powerlaw(x: np.ndarray, target: np.ndarray, support: np.ndarray) -> tuple[np.ndarray, dict[str, float]]:
    best_values = np.zeros_like(target)
    best_beta = float("nan")
    best_rms = float("inf")
    for beta in np.linspace(-8.0, 8.0, 641):
        values = _normalize_shape(np.exp(beta * x))
        rms = _rms(values[support] - target[support])
        if rms < best_rms:
            best_rms = rms
            best_values = values
            best_beta = float(beta)
    return best_values, {"beta": best_beta}


def _tomographic_bins(x: np.ndarray, target: np.ndarray, support: np.ndarray, n_bins: int) -> tuple[np.ndarray, dict[str, float]]:
    values = np.zeros_like(target)
    x_lo = float(np.min(x[support]))
    x_hi = float(np.max(x[support]))
    edges = np.linspace(x_lo, x_hi, n_bins + 1)
    for i in range(n_bins):
        if i == n_bins - 1:
            mask = (x >= edges[i]) & (x <= edges[i + 1])
        else:
            mask = (x >= edges[i]) & (x < edges[i + 1])
        if np.any(mask):
            values[mask] = float(np.mean(target[mask]))
    return _normalize_shape(values), {
        "n_bins": float(n_bins),
        "min_z": float(math.exp(-x_hi) - 1.0),
        "max_z": float(math.exp(-x_lo) - 1.0),
    }


def _piecewise_linear_reconstruction(
    x: np.ndarray,
    target: np.ndarray,
    support: np.ndarray,
    n_knots: int,
) -> tuple[np.ndarray, dict[str, float]]:
    x_lo = float(np.min(x[support]))
    x_hi = float(np.max(x[support]))
    knots = np.linspace(x_lo, x_hi, n_knots)
    knot_values = np.interp(knots, x, target)
    values = np.interp(x, knots, knot_values, left=0.0, right=0.0)
    return _normalize_shape(values), {"n_knots": float(n_knots)}


def _fingerprint(x: np.ndarray, z: np.ndarray, shape: np.ndarray) -> dict[str, float]:
    weight = np.clip(shape, 0.0, None)
    area = max(_integral(x, weight), 1.0e-30)
    peak_index = int(np.argmax(weight))
    half = 0.5 * float(np.max(weight))
    half_support = weight >= half
    if np.any(half_support):
        z_half = z[half_support]
        x_half = x[half_support]
        half_z_min = float(np.min(z_half))
        half_z_max = float(np.max(z_half))
        width_ln_a = float(np.max(x_half) - np.min(x_half))
    else:
        half_z_min = float("nan")
        half_z_max = float("nan")
        width_ln_a = float("nan")
    mean_x = _integral(x, x * weight) / area
    variance_x = max(_integral(x, (x - mean_x) ** 2 * weight) / area, 0.0)
    sigma_x = math.sqrt(variance_x)
    if sigma_x > 0.0:
        skew_x = _integral(x, ((x - mean_x) / sigma_x) ** 3 * weight) / area
    else:
        skew_x = float("nan")
    return {
        "peak_z": float(z[peak_index]),
        "weighted_mean_z": float(math.exp(-mean_x) - 1.0),
        "arithmetic_weighted_mean_z": float(_integral(x, z * weight) / area),
        "weighted_mean_ln_a": float(mean_x),
        "half_max_z_min": half_z_min,
        "half_max_z_max": half_z_max,
        "half_max_width_ln_a": width_ln_a,
        "skew_ln_a": float(skew_x),
        "z_gt_1100_fraction": float(_integral(x, weight * (z > 1100.0)) / area),
        "z_gt_10_fraction": float(_integral(x, weight * (z > 10.0)) / area),
        "z_lt_1_fraction": float(_integral(x, weight * (z < 1.0)) / area),
        "z_lt_0_5_fraction": float(_integral(x, weight * (z < 0.5)) / area),
    }


def _classification(
    *,
    row: dict[str, Any],
    best_compact_rms: float,
    best_compact_family: str,
) -> str:
    if row["family_id"] == "retained_gamma":
        return "reference"
    compact_match = row["parameter_count"] <= 2 and row["shape_rms_error"] <= 0.05 and row["shape_max_error"] <= 0.15
    flexible_match = row["parameter_count"] > 2 and row["shape_rms_error"] <= 0.05 and row["shape_max_error"] <= 0.15
    if compact_match:
        return "known_compact_timing_family"
    if flexible_match:
        return "flexible_reconstruction_match"
    if row["family_id"] in {"constant", "powerlaw"}:
        return "too_rigid"
    if best_compact_rms <= 0.05 and best_compact_family != row["family_id"]:
        return "redundant_if_used_as_unique_prior"
    return "poor_timing_match"


def _decision(summary_rows: list[dict[str, Any]]) -> dict[str, Any]:
    compact = [
        row
        for row in summary_rows
        if row["family_id"] != "retained_gamma" and row["parameter_count"] <= 2
    ]
    flexible = [
        row
        for row in summary_rows
        if row["family_id"] != "retained_gamma" and row["parameter_count"] > 2
    ]
    best_compact = min(compact, key=lambda row: row["shape_rms_error"])
    best_flexible = min(flexible, key=lambda row: row["shape_rms_error"])
    compact_ok = best_compact["shape_rms_error"] <= 0.05 and best_compact["shape_max_error"] <= 0.15
    flexible_ok = best_flexible["shape_rms_error"] <= 0.05 and best_flexible["shape_max_error"] <= 0.15

    if compact_ok:
        verdict = "redundant_as_unique_shape_but_useful_as_interpretable_prior"
        interpretation = (
            "A standard compact pulse family reproduces the retained timing shape. "
            "The retained profile should not be claimed as a distinct timing family, "
            "but it can still be used as an interpretable low-dimensional prior."
        )
    elif flexible_ok:
        verdict = "potentially_useful_compression_target"
        interpretation = (
            "Flexible reconstructions can reproduce the timing shape but compact "
            "families do not. The retained profile may be useful as a compression "
            "target if future reconstructions prefer similar support."
        )
    else:
        verdict = "not_supported_as_timing_prior"
        interpretation = (
            "Neither compact nor flexible reference families matched the retained "
            "shape under the predeclared timing-only metrics."
        )

    return {
        "verdict": verdict,
        "interpretation": interpretation,
        "best_compact_family": best_compact["family_id"],
        "best_compact_shape_rms_error": best_compact["shape_rms_error"],
        "best_compact_shape_max_error": best_compact["shape_max_error"],
        "best_flexible_family": best_flexible["family_id"],
        "best_flexible_shape_rms_error": best_flexible["shape_rms_error"],
        "best_flexible_shape_max_error": best_flexible["shape_max_error"],
        "physical_claim_supported": False,
        "roadmap_status_change": False,
    }


def _write_visualizations(
    outdir: Path,
    z: np.ndarray,
    families: list[TimingFamily],
    rows: list[dict[str, Any]],
) -> list[str]:
    try:
        import matplotlib.pyplot as plt
    except ModuleNotFoundError:
        return []

    outputs: list[str] = []
    selected = {
        "retained_gamma",
        "constant",
        "powerlaw",
        "logistic_derivative",
        "gaussian_ln_a",
        "piecewise_linear_8_knots",
    }
    fig, ax = plt.subplots(figsize=(9, 5), constrained_layout=True)
    for family in families:
        if family.family_id not in selected:
            continue
        linewidth = 2.4 if family.family_id == "retained_gamma" else 1.5
        ax.plot(z, family.values, label=family.label, linewidth=linewidth)
    ax.set(xlabel="z", ylabel="normalized timing shape", title="Exp 005 retained timing prior vs reference families", xlim=(8.0, 0.0), ylim=(-0.03, 1.08))
    ax.legend(frameon=False, fontsize=8)
    figures_dir = outdir / "figures"
    outputs.extend(save_figure_pair(fig, figures_dir / "exp005_timing_family_shapes"))
    plt.close(fig)

    plot_rows = [row for row in rows if row["family_id"] != "retained_gamma"]
    labels = [str(row["family_id"]).replace("_", "\n") for row in plot_rows]
    rms = [float(row["shape_rms_error"]) for row in plot_rows]
    max_errors = [float(row["shape_max_error"]) for row in plot_rows]
    x = np.arange(len(plot_rows))
    width = 0.35
    fig, ax = plt.subplots(figsize=(10, 4.8), constrained_layout=True)
    ax.bar(x - width / 2, rms, width=width, label="RMS error")
    ax.bar(x + width / 2, max_errors, width=width, label="max error")
    ax.axhline(0.05, color="#2b2b2b", linestyle="--", linewidth=1.0, label="RMS threshold")
    ax.axhline(0.15, color="#6b6b6b", linestyle=":", linewidth=1.0, label="max threshold")
    ax.set_xticks(x, labels)
    ax.set_ylabel("normalized shape error")
    ax.set_title("Exp 005 timing-family error thresholds")
    ax.legend(frameon=False)
    outputs.extend(save_figure_pair(fig, figures_dir / "exp005_timing_family_errors"))
    plt.close(fig)
    return outputs


def run_exp005_timing_prior_audit(
    *,
    outdir: Path = Path("outputs"),
    n_background: int = 1200,
) -> dict[str, Any]:
    """Run a timing-only prior usefulness audit for retained Gamma(a).

    This is a phenomenological IV/IDE timing analysis. It compares normalized
    timing shapes only; it does not compare amplitudes or derive a source.
    """

    outdir.mkdir(parents=True, exist_ok=True)
    cosmo = CosmologyParams()
    retained = integrate_background(cosmo, _retained_params(), n=n_background)
    x = np.log(retained["a"])
    z = retained["z"]
    target = _normalize_shape(retained["Gamma"])
    support = target > 1.0e-3
    center_guess = float(x[int(np.argmax(target))])
    center_grid = np.linspace(center_guess - 1.5, center_guess + 1.5, 121)
    width_grid = np.linspace(0.08, 1.8, 121)

    powerlaw, powerlaw_params = _fit_powerlaw(x, target, support)
    transition, transition_params, _ = _fit_two_parameter_family(
        x=x,
        target=target,
        support=support,
        centers=center_grid,
        widths=width_grid,
        builder=_logistic_transition,
    )
    logistic_rate, logistic_rate_params, _ = _fit_two_parameter_family(
        x=x,
        target=target,
        support=support,
        centers=center_grid,
        widths=width_grid,
        builder=_logistic_derivative,
    )
    gaussian, gaussian_params, _ = _fit_two_parameter_family(
        x=x,
        target=target,
        support=support,
        centers=center_grid,
        widths=width_grid,
        builder=_gaussian_ln_a,
    )
    tomo3, tomo3_params = _tomographic_bins(x, target, support, 3)
    tomo5, tomo5_params = _tomographic_bins(x, target, support, 5)
    reconstruction8, reconstruction8_params = _piecewise_linear_reconstruction(
        x, target, support, 8
    )

    families = [
        TimingFamily(
            "retained_gamma",
            "retained normalized Gamma(a)",
            2,
            "reference",
            target,
            {"collapse_a": 0.35, "collapse_nu": 5.0},
            "Reference timing prior from retained information-production branch.",
        ),
        TimingFamily(
            "constant",
            "constant coupling",
            0,
            "rigid",
            np.ones_like(target),
            {},
            "No timing localization.",
        ),
        TimingFamily(
            "powerlaw",
            "power-law coupling",
            1,
            "rigid",
            powerlaw,
            powerlaw_params,
            "Best normalized power-law timing shape.",
        ),
        TimingFamily(
            "logistic_transition",
            "logistic transition",
            2,
            "transition",
            transition,
            transition_params,
            "Best cumulative logistic transition, not its derivative.",
        ),
        TimingFamily(
            "logistic_derivative",
            "logistic transition-rate pulse",
            2,
            "smooth_pulse",
            logistic_rate,
            logistic_rate_params,
            "Best finite-duration logistic transition-rate pulse.",
        ),
        TimingFamily(
            "gaussian_ln_a",
            "Gaussian pulse in ln(a)",
            2,
            "smooth_pulse",
            gaussian,
            gaussian_params,
            "Best symmetric smooth pulse in ln(a).",
        ),
        TimingFamily(
            "tomographic_3_bins",
            "three-bin tomographic timing",
            3,
            "tomographic",
            tomo3,
            tomo3_params,
            "Piecewise-constant reconstruction over retained support.",
        ),
        TimingFamily(
            "tomographic_5_bins",
            "five-bin tomographic timing",
            5,
            "tomographic",
            tomo5,
            tomo5_params,
            "Piecewise-constant reconstruction over retained support.",
        ),
        TimingFamily(
            "piecewise_linear_8_knots",
            "eight-knot nonparametric proxy",
            8,
            "nonparametric_proxy",
            reconstruction8,
            reconstruction8_params,
            "Flexible timing reconstruction proxy; not a physical model.",
        ),
    ]

    best_compact_rms = min(
        _rms(family.values[support] - target[support])
        for family in families
        if family.family_id != "retained_gamma" and family.parameter_count <= 2
    )
    best_compact_family = min(
        (
            family
            for family in families
            if family.family_id != "retained_gamma" and family.parameter_count <= 2
        ),
        key=lambda family: _rms(family.values[support] - target[support]),
    ).family_id

    rows: list[dict[str, Any]] = []
    fingerprint_rows: list[dict[str, Any]] = []
    for family in families:
        diff = family.values[support] - target[support]
        metrics = {
            "shape_rms_error": _rms(diff),
            "shape_max_error": _max_abs(diff),
        }
        fp = _fingerprint(x, z, family.values)
        row: dict[str, Any] = {
            "family_id": family.family_id,
            "label": family.label,
            "family_class": family.family_class,
            "parameter_count": family.parameter_count,
            "note": family.note,
            **metrics,
            **fp,
            **{f"fit_{key}": value for key, value in family.fit_parameters.items()},
        }
        row["classification"] = _classification(
            row=row,
            best_compact_rms=best_compact_rms,
            best_compact_family=best_compact_family,
        )
        rows.append(row)
        fingerprint_rows.append(
            {
                key: row[key]
                for key in (
                    "family_id",
                    "peak_z",
                    "weighted_mean_z",
                    "half_max_z_min",
                    "half_max_z_max",
                    "half_max_width_ln_a",
                    "skew_ln_a",
                    "z_gt_1100_fraction",
                    "z_gt_10_fraction",
                    "z_lt_1_fraction",
                    "z_lt_0_5_fraction",
                )
            }
        )

    decision = _decision(rows)
    criteria_rows = [
        {
            "criterion": "parameter_reduction",
            "matters_because": "The possible value is compact timing structure between rigid and arbitrary coupling histories.",
            "measurement": "parameter_count versus shape_rms_error and shape_max_error",
            "pass_signal": "few parameters reproduce the timing support within thresholds",
        },
        {
            "criterion": "early_leakage_suppression",
            "matters_because": "Early coupling risks CMB-era contamination and strong early-universe constraints.",
            "measurement": "z_gt_1100_fraction and z_gt_10_fraction",
            "pass_signal": "fractions remain negligible for the retained prior and matched family",
        },
        {
            "criterion": "interpretability",
            "matters_because": "A timing prior is useful only if its parameters map to peak, width, support, and tails.",
            "measurement": "peak_z, weighted_mean_z, half-max support, skew_ln_a",
            "pass_signal": "parameters can be stated before amplitude fitting",
        },
        {
            "criterion": "redundancy",
            "matters_because": "A prior is not unique if standard timing families reproduce it with equal or fewer assumptions.",
            "measurement": "best compact family errors and classification",
            "pass_signal": "retained prior is labeled as reusable prior, not new timing family, when compact matches exist",
        },
    ]

    def write_rows(path: Path, data: list[dict[str, Any]]) -> None:
        fields = sorted({key for row in data for key in row})
        with path.open("w", newline="") as handle:
            writer = csv.DictWriter(handle, fieldnames=fields, lineterminator="\n")
            writer.writeheader()
            writer.writerows(data)

    write_rows(outdir / "exp005_timing_family_comparison.csv", rows)
    write_rows(outdir / "exp005_timing_fingerprint.csv", fingerprint_rows)
    write_rows(outdir / "exp005_timing_prior_criteria.csv", criteria_rows)
    plot_outputs = _write_visualizations(outdir, z, families, rows)

    summary = {
        "experiment_id": "exp_005",
        "title": "Timing-Prior Usefulness and Redundancy Audit",
        "scope": "phenomenological IV/IDE timing-prior analysis only",
        "normalization": "all timing families normalized to max(shape)=1; amplitudes are not compared",
        "decision": decision,
        "retained_fingerprint": next(
            row for row in fingerprint_rows if row["family_id"] == "retained_gamma"
        ),
        "family_comparison": rows,
        "criteria": criteria_rows,
        "for_argument": "The retained profile supplies a compact, interpretable, low-leakage structure-era timing prior for IV/IDE coupling searches.",
        "against_argument": "Without a source derivation, and if standard pulse families reproduce the shape, the retained profile is not a distinct timing family.",
        "outputs": [
            "outputs/exp005_timing_prior_summary.json",
            "outputs/exp005_timing_family_comparison.csv",
            "outputs/exp005_timing_fingerprint.csv",
            "outputs/exp005_timing_prior_criteria.csv",
        ]
        + plot_outputs,
        "visual_outputs": plot_outputs,
    }
    (outdir / "exp005_timing_prior_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True),
        encoding="utf-8",
    )
    return summary
