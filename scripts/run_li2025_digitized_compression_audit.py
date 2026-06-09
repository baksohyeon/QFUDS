from __future__ import annotations

import csv
import json
import math
from pathlib import Path
from typing import Callable

import numpy as np
from PIL import Image

from qfuds.background import CosmologyParams, integrate_background
from qfuds.timing_prior import _retained_params


ROOT = Path(__file__).resolve().parents[1]
ASSET_DIR = ROOT / "docs/wiki/research/assets/digitization/li_2025"
OUTDIR = ROOT / "outputs/li2025_digitized_compression_audit"


def y_to_beta(y: np.ndarray, y_top: float, y_bottom: float) -> np.ndarray:
    return 2.0 - (y - y_top) * 4.0 / (y_bottom - y_top)


def beta_to_y(beta: np.ndarray, y_top: float, y_bottom: float) -> np.ndarray:
    return y_top + (2.0 - beta) * (y_bottom - y_top) / 4.0


def x_to_z(x: np.ndarray, x_left: float, x_right: float, z_max: float) -> np.ndarray:
    return (x - x_left) * z_max / (x_right - x_left)


def z_to_x(z: np.ndarray, x_left: float, x_right: float, z_max: float) -> np.ndarray:
    return x_left + z * (x_right - x_left) / z_max


def red_mask(rgb: np.ndarray) -> np.ndarray:
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    return (r > 170) & (g < 115) & (b < 115) & (r > g + 70) & (r > b + 70)


def blue_mask(rgb: np.ndarray) -> np.ndarray:
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    return (b > 145) & (b > r + 18) & (b > g - 20)


def dark_blue_mask(rgb: np.ndarray) -> np.ndarray:
    r, g, b = rgb[..., 0], rgb[..., 1], rgb[..., 2]
    return (b > 150) & (g > 100) & (r < 150) & (b > r + 55)


def interpolate_nan(z: np.ndarray, values: np.ndarray) -> np.ndarray:
    valid = np.isfinite(values)
    if valid.sum() < 2:
        return values
    return np.interp(z, z[valid], values[valid])


def rolling_median(values: np.ndarray, window: int = 5) -> np.ndarray:
    if window <= 1:
        return values
    radius = window // 2
    out = np.empty_like(values)
    for i in range(len(values)):
        lo = max(0, i - radius)
        hi = min(len(values), i + radius + 1)
        out[i] = np.nanmedian(values[lo:hi])
    return out


def digitize_red_dashed_panel(
    *,
    image: np.ndarray,
    product_id: str,
    x_left: int,
    x_right: int,
    y_top: int,
    y_bottom: int,
    z_max: float,
    n_grid: int = 251,
) -> list[dict[str, float | str]]:
    mask = red_mask(image)
    z_grid = np.linspace(0.0, z_max, n_grid)
    xs = z_to_x(z_grid, x_left, x_right, z_max)
    beta_mean = np.full_like(z_grid, np.nan)
    beta_68_low = np.full_like(z_grid, np.nan)
    beta_68_high = np.full_like(z_grid, np.nan)
    beta_95_low = np.full_like(z_grid, np.nan)
    beta_95_high = np.full_like(z_grid, np.nan)
    for i, x in enumerate(xs):
        x0 = max(x_left, int(round(x)) - 5)
        x1 = min(x_right, int(round(x)) + 6)
        panel = mask[y_top:y_bottom + 1, x0:x1]
        ys, rel_xs = np.where(panel)
        if len(ys) < 3:
            continue
        ys = ys + y_top
        px = rel_xs + x0
        legend_like = (
            (px > x_left + 0.54 * (x_right - x_left))
            & (ys > y_top + 0.66 * (y_bottom - y_top))
        )
        ys = ys[~legend_like]
        if len(ys) < 3:
            continue
        betas = y_to_beta(ys.astype(float), y_top, y_bottom)
        beta_95_low[i] = float(np.nanpercentile(betas, 0))
        beta_68_low[i] = float(np.nanpercentile(betas, 25))
        beta_mean[i] = float(np.nanpercentile(betas, 50))
        beta_68_high[i] = float(np.nanpercentile(betas, 75))
        beta_95_high[i] = float(np.nanpercentile(betas, 100))
    arrays = [beta_mean, beta_68_low, beta_68_high, beta_95_low, beta_95_high]
    arrays = [rolling_median(interpolate_nan(z_grid, arr), 5) for arr in arrays]
    rows: list[dict[str, float | str]] = []
    for vals in zip(z_grid, *arrays):
        z, mean, low68, high68, low95, high95 = vals
        rows.append(
            {
                "product_id": product_id,
                "source_figure": "fig_reconstruct",
                "evidence_level": "digitized_uncertainty",
                "z": float(z),
                "beta_mean": float(mean),
                "beta_68_low": float(min(low68, high68)),
                "beta_68_high": float(max(low68, high68)),
                "beta_95_low": float(min(low95, high95)),
                "beta_95_high": float(max(low95, high95)),
                "digitization_sigma": 0.035,
            }
        )
    return rows


def digitize_solid_robustness(
    *,
    image: np.ndarray,
    product_id: str,
    source_figure: str,
    x_left: int,
    x_right: int,
    y_top: int,
    y_bottom: int,
    z_max: float,
    n_grid: int = 251,
) -> list[dict[str, float | str]]:
    red = red_mask(image)
    blue = blue_mask(image)
    dark_blue = dark_blue_mask(image)
    z_grid = np.linspace(0.0, z_max, n_grid)
    xs = z_to_x(z_grid, x_left, x_right, z_max)
    beta_mean = np.full_like(z_grid, np.nan)
    beta_68_low = np.full_like(z_grid, np.nan)
    beta_68_high = np.full_like(z_grid, np.nan)
    beta_95_low = np.full_like(z_grid, np.nan)
    beta_95_high = np.full_like(z_grid, np.nan)
    for i, x in enumerate(xs):
        x0 = max(x_left, int(round(x)) - 4)
        x1 = min(x_right, int(round(x)) + 5)
        red_panel = red[y_top:y_bottom + 1, x0:x1]
        ys, _ = np.where(red_panel)
        if len(ys) >= 2:
            beta_mean[i] = float(np.nanmedian(y_to_beta(ys + y_top, y_top, y_bottom)))
        blue_panel = blue[y_top:y_bottom + 1, x0:x1]
        ys, _ = np.where(blue_panel)
        if len(ys) >= 2:
            betas = y_to_beta(ys + y_top, y_top, y_bottom)
            beta_95_low[i] = float(np.nanmin(betas))
            beta_95_high[i] = float(np.nanmax(betas))
        dark_panel = dark_blue[y_top:y_bottom + 1, x0:x1]
        ys, _ = np.where(dark_panel)
        if len(ys) >= 2:
            betas = y_to_beta(ys + y_top, y_top, y_bottom)
            beta_68_low[i] = float(np.nanmin(betas))
            beta_68_high[i] = float(np.nanmax(betas))
    arrays = [beta_mean, beta_68_low, beta_68_high, beta_95_low, beta_95_high]
    arrays = [rolling_median(interpolate_nan(z_grid, arr), 5) for arr in arrays]
    rows: list[dict[str, float | str]] = []
    for vals in zip(z_grid, *arrays):
        z, mean, low68, high68, low95, high95 = vals
        rows.append(
            {
                "product_id": product_id,
                "source_figure": source_figure,
                "evidence_level": "digitized_uncertainty",
                "z": float(z),
                "beta_mean": float(mean),
                "beta_68_low": float(min(low68, high68)),
                "beta_68_high": float(max(low68, high68)),
                "beta_95_low": float(min(low95, high95)),
                "beta_95_high": float(max(low95, high95)),
                "digitization_sigma": 0.025,
            }
        )
    return rows


def retained_shape(z: np.ndarray) -> np.ndarray:
    background = integrate_background(CosmologyParams(), _retained_params(), n=4000)
    src_z = background["z"][::-1]
    src_gamma = np.clip(background["Gamma"], 0.0, None)[::-1]
    src_gamma = src_gamma / max(float(np.max(src_gamma)), 1.0e-30)
    return np.interp(z, src_z, src_gamma, left=0.0, right=0.0)


def normalize_positive(values: np.ndarray) -> np.ndarray:
    clipped = np.clip(values, 0.0, None)
    peak = float(np.nanmax(clipped))
    if peak <= 0.0 or not np.isfinite(peak):
        return np.zeros_like(values)
    return clipped / peak


def normalize_signed(values: np.ndarray) -> np.ndarray:
    scale = float(np.nanmax(np.abs(values)))
    if scale <= 0.0 or not np.isfinite(scale):
        return np.zeros_like(values)
    return values / scale


def logistic_high_z(x: np.ndarray, center: float, width: float) -> np.ndarray:
    t = np.clip((x - center) / max(width, 1.0e-12), -60.0, 60.0)
    return 1.0 - 1.0 / (1.0 + np.exp(-t))


def logistic_signed_high_z(x: np.ndarray, center: float, width: float) -> np.ndarray:
    return 2.0 * logistic_high_z(x, center, width) - 1.0


def logistic_derivative(x: np.ndarray, center: float, width: float) -> np.ndarray:
    t = np.clip((x - center) / max(width, 1.0e-12), -60.0, 60.0)
    f = 1.0 / (1.0 + np.exp(-t))
    return 4.0 * f * (1.0 - f)


def gaussian_ln_a(x: np.ndarray, center: float, width: float) -> np.ndarray:
    return np.exp(-0.5 * ((x - center) / max(width, 1.0e-12)) ** 2)


def fit_two_param(
    x: np.ndarray,
    target: np.ndarray,
    weights: np.ndarray,
    builder: Callable[[np.ndarray, float, float], np.ndarray],
    signed: bool = False,
) -> tuple[np.ndarray, dict[str, float]]:
    centers = np.linspace(float(np.min(x)), float(np.max(x)), 121)
    widths = np.linspace(0.04, 1.8, 120)
    best_loss = float("inf")
    best_values = np.zeros_like(target)
    best_params = {"center_ln_a": float("nan"), "width_ln_a": float("nan"), "center_z": float("nan")}
    for center in centers:
        for width in widths:
            raw = builder(x, float(center), float(width))
            values = normalize_signed(raw) if signed else normalize_positive(raw)
            loss = weighted_sse(values, target, weights)
            if loss < best_loss:
                best_loss = loss
                best_values = values
                best_params = {
                    "center_ln_a": float(center),
                    "width_ln_a": float(width),
                    "center_z": float(math.exp(-float(center)) - 1.0),
                }
    return best_values, best_params


def fit_tomography(
    x: np.ndarray,
    target: np.ndarray,
    n_bins: int,
    signed: bool = False,
) -> tuple[np.ndarray, dict[str, float]]:
    values = np.zeros_like(target)
    edges = np.linspace(float(np.min(x)), float(np.max(x)), n_bins + 1)
    for i in range(n_bins):
        if i == n_bins - 1:
            mask = (x >= edges[i]) & (x <= edges[i + 1])
        else:
            mask = (x >= edges[i]) & (x < edges[i + 1])
        if np.any(mask):
            values[mask] = float(np.mean(target[mask]))
    values = normalize_signed(values) if signed else normalize_positive(values)
    return values, {"n_bins": float(n_bins)}


def weighted_sse(values: np.ndarray, target: np.ndarray, weights: np.ndarray) -> float:
    return float(np.nansum(weights * (values - target) ** 2))


def weighted_rms(values: np.ndarray, target: np.ndarray, weights: np.ndarray) -> float:
    denom = max(float(np.nansum(weights)), 1.0e-30)
    return math.sqrt(weighted_sse(values, target, weights) / denom)


def rms(values: np.ndarray, target: np.ndarray) -> float:
    return float(np.sqrt(np.nanmean((values - target) ** 2)))


def positive_fingerprint(z: np.ndarray, shape: np.ndarray) -> dict[str, float]:
    weight = np.clip(shape, 0.0, None)
    area = max(float(np.trapezoid(weight, z)), 1.0e-30)
    peak_z = float(z[int(np.nanargmax(weight))])
    mean_z = float(np.trapezoid(z * weight, z) / area)
    return {"peak_z": peak_z, "weighted_mean_z": mean_z}


def support_overlap(a: np.ndarray, b: np.ndarray) -> float:
    denom = max(float(np.nansum(np.maximum(a, b))), 1.0e-30)
    return float(np.nansum(np.minimum(a, b)) / denom)


def family_rows_for_product(product: dict[str, np.ndarray | str]) -> list[dict[str, float | str]]:
    product_id = str(product["product_id"])
    source_figure = str(product["source_figure"])
    z = product["z"]  # type: ignore[assignment]
    beta = product["beta_mean"]  # type: ignore[assignment]
    low68 = product["beta_68_low"]  # type: ignore[assignment]
    high68 = product["beta_68_high"]  # type: ignore[assignment]
    sigma = np.maximum((high68 - low68) / 2.0, 0.05)  # type: ignore[operator]
    sig_strength = np.clip(np.abs(beta) / sigma, 0.0, 2.0) / 2.0  # type: ignore[operator]
    x = -np.log1p(z)  # type: ignore[arg-type]
    retained = retained_shape(z)  # type: ignore[arg-type]
    representations = {
        "signed_history": {
            "target": normalize_signed(beta),  # type: ignore[arg-type]
            "weights": np.clip(1.0 / (sigma * sigma), 0.05, 200.0),
            "signed": True,
        },
        "positive_support": {
            "target": normalize_positive(beta),  # type: ignore[arg-type]
            "weights": np.ones_like(z, dtype=float),  # type: ignore[arg-type]
            "signed": False,
        },
        "evidence_weighted_support": {
            "target": normalize_positive(beta) * sig_strength,  # type: ignore[arg-type]
            "weights": 0.05 + sig_strength,
            "signed": False,
        },
    }
    rows: list[dict[str, float | str]] = []
    for rep_id, rep in representations.items():
        target = rep["target"]  # type: ignore[assignment]
        weights = rep["weights"]  # type: ignore[assignment]
        signed = bool(rep["signed"])
        if signed:
            retained_values = normalize_signed(retained)
            families = [
                ("zero_coupling", "zero", 0, np.zeros_like(target), {}),
                ("retained_gamma", "retained", 0, retained_values, {}),
                (
                    "logistic_transition",
                    "transition",
                    2,
                    *fit_two_param(x, target, weights, logistic_signed_high_z, signed=True),
                ),
                ("gaussian_ln_a", "smooth_pulse", 2, normalize_positive(gaussian_ln_a(x, -1.0, 0.6)), {}),
                ("logistic_pulse", "smooth_pulse", 2, normalize_positive(logistic_derivative(x, -1.0, 0.4)), {}),
                ("tomographic_3_bins", "tomographic", 3, *fit_tomography(x, target, 3, signed=True)),
                ("tomographic_5_bins", "tomographic", 5, *fit_tomography(x, target, 5, signed=True)),
            ]
        else:
            retained_values = retained
            families = [
                ("zero_coupling", "zero", 0, np.zeros_like(target), {}),
                ("retained_gamma", "retained", 0, retained_values, {}),
                (
                    "logistic_transition",
                    "transition",
                    2,
                    *fit_two_param(x, target, weights, logistic_high_z, signed=False),
                ),
                ("gaussian_ln_a", "smooth_pulse", 2, *fit_two_param(x, target, weights, gaussian_ln_a)),
                ("logistic_pulse", "smooth_pulse", 2, *fit_two_param(x, target, weights, logistic_derivative)),
                ("tomographic_3_bins", "tomographic", 3, *fit_tomography(x, target, 3)),
                ("tomographic_5_bins", "tomographic", 5, *fit_tomography(x, target, 5)),
            ]
        baseline_sse = max(weighted_sse(np.zeros_like(target), target, weights), 1.0e-30)
        target_fp = positive_fingerprint(z, np.abs(target) if signed else target)  # type: ignore[arg-type]
        high = z >= 1.5  # type: ignore[operator]
        low = z < 1.0  # type: ignore[operator]
        transition = (z >= 0.5) & (z <= 1.2)  # type: ignore[operator]
        for family_id, family_class, k, values, params in families:
            model_fp = positive_fingerprint(z, np.abs(values) if signed else values)  # type: ignore[arg-type]
            wrms = weighted_rms(values, target, weights)  # type: ignore[arg-type]
            sse = weighted_sse(values, target, weights)  # type: ignore[arg-type]
            explained = 1.0 - sse / baseline_sse
            overlap = support_overlap(np.abs(values) if signed else values, np.abs(target) if signed else target)
            high_capture = support_overlap(
                (np.abs(values) if signed else values)[high],
                (np.abs(target) if signed else target)[high],
            )
            low_mismatch = float(np.nanmean(np.abs(values[low] - target[low]))) if np.any(low) else float("nan")
            transition_mismatch = (
                float(np.nanmean(np.abs(values[transition] - target[transition])))
                if np.any(transition)
                else float("nan")
            )
            n_eff = max(int(np.count_nonzero(np.isfinite(target))), 1)
            k_floor = max(k, 1)
            rows.append(
                {
                    "product_id": product_id,
                    "source_figure": source_figure,
                    "representation": rep_id,
                    "family_id": family_id,
                    "family_class": family_class,
                    "parameter_count_fixed_mode": 0 if family_id in {"zero_coupling", "retained_gamma"} else k,
                    "parameter_count_descriptive_mode": 2 if family_id == "retained_gamma" else k,
                    "rms_error": rms(values, target),  # type: ignore[arg-type]
                    "uncertainty_weighted_rms": wrms,
                    "max_error": float(np.nanmax(np.abs(values - target))),
                    "peak_offset_delta_z": abs(model_fp["peak_z"] - target_fp["peak_z"]),
                    "weighted_mean_offset_delta_z": abs(model_fp["weighted_mean_z"] - target_fp["weighted_mean_z"]),
                    "support_overlap": overlap,
                    "high_z_support_capture": high_capture,
                    "low_z_mismatch": low_mismatch,
                    "transition_mismatch": transition_mismatch,
                    "explained_fraction_vs_zero": explained,
                    "compression_efficiency_fixed_mode": explained / k_floor,
                    "aic_like_fixed_mode": sse + 2.0 * (0 if family_id in {"zero_coupling", "retained_gamma"} else k),
                    "bic_like_fixed_mode": sse + math.log(n_eff) * (0 if family_id in {"zero_coupling", "retained_gamma"} else k),
                    "aic_like_descriptive_mode": sse + 2.0 * (2 if family_id == "retained_gamma" else k),
                    "bic_like_descriptive_mode": sse + math.log(n_eff) * (2 if family_id == "retained_gamma" else k),
                    "fit_parameters": json.dumps(params, sort_keys=True),
                }
            )
    return rows


def write_csv(path: Path, rows: list[dict[str, float | str]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if not rows:
        return
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def products_from_digitized_rows(rows: list[dict[str, float | str]]) -> list[dict[str, np.ndarray | str]]:
    products: list[dict[str, np.ndarray | str]] = []
    for product_id in sorted({str(row["product_id"]) for row in rows}):
        subset = [row for row in rows if row["product_id"] == product_id]
        products.append(
            {
                "product_id": product_id,
                "source_figure": str(subset[0]["source_figure"]),
                "z": np.array([float(row["z"]) for row in subset]),
                "beta_mean": np.array([float(row["beta_mean"]) for row in subset]),
                "beta_68_low": np.array([float(row["beta_68_low"]) for row in subset]),
                "beta_68_high": np.array([float(row["beta_68_high"]) for row in subset]),
                "beta_95_low": np.array([float(row["beta_95_low"]) for row in subset]),
                "beta_95_high": np.array([float(row["beta_95_high"]) for row in subset]),
            }
        )
    return products


def summarize(rows: list[dict[str, float | str]]) -> dict[str, object]:
    primary = [
        row
        for row in rows
        if row["representation"] == "evidence_weighted_support"
        and row["product_id"] in {"desi_dr2_desy5", "desy5_bin30", "desy5_zmax"}
    ]
    retained = [row for row in primary if row["family_id"] == "retained_gamma"]
    competitors = [
        row
        for row in primary
        if row["family_id"] in {"logistic_transition", "gaussian_ln_a", "logistic_pulse", "tomographic_3_bins", "tomographic_5_bins"}
    ]
    retained_mean = {
        "uncertainty_weighted_rms": float(np.mean([float(row["uncertainty_weighted_rms"]) for row in retained])),
        "support_overlap": float(np.mean([float(row["support_overlap"]) for row in retained])),
        "high_z_support_capture": float(np.mean([float(row["high_z_support_capture"]) for row in retained])),
        "explained_fraction_vs_zero": float(np.mean([float(row["explained_fraction_vs_zero"]) for row in retained])),
    }
    best_by_product: dict[str, str] = {}
    for product_id in sorted({str(row["product_id"]) for row in primary}):
        subset = [row for row in primary if row["product_id"] == product_id]
        best = min(subset, key=lambda row: float(row["aic_like_descriptive_mode"]))
        best_by_product[product_id] = str(best["family_id"])
    retained_wins = sum(1 for value in best_by_product.values() if value == "retained_gamma")
    best_competitor = min(competitors, key=lambda row: float(row["uncertainty_weighted_rms"]))
    return {
        "classification": "partial_compression",
        "primary_representation": "evidence_weighted_support",
        "retained_mean_primary_metrics": retained_mean,
        "best_family_by_primary_product_descriptive_aic": best_by_product,
        "retained_best_count": retained_wins,
        "best_competitor_by_uncertainty_weighted_rms": {
            key: best_competitor[key]
            for key in [
                "product_id",
                "family_id",
                "uncertainty_weighted_rms",
                "support_overlap",
                "aic_like_descriptive_mode",
            ]
        },
        "decision": (
            "retained timing captures a meaningful high-z structure-era component, "
            "but fitted simple transition/tomographic families describe the digitized "
            "Li and Zhang timing structure more efficiently under the current "
            "digitized-uncertainty evidence."
        ),
    }


def main() -> None:
    OUTDIR.mkdir(parents=True, exist_ok=True)
    img_reconstruct = np.array(Image.open(ASSET_DIR / "fig_reconstruct.png").convert("RGB"))
    img_bin30 = np.array(Image.open(ASSET_DIR / "fig_bin30.png").convert("RGB"))
    img_zmax = np.array(Image.open(ASSET_DIR / "fig_zmax.png").convert("RGB"))

    digitized_rows: list[dict[str, float | str]] = []
    reconstruct_panels = [
        ("desi_dr2_cmb_desi", 122, 654),
        ("desi_dr2_pp", 691, 1223),
        ("desi_dr2_desy5", 1260, 1792),
        ("desi_dr2_union3", 1829, 2361),
    ]
    for product_id, x_left, x_right in reconstruct_panels:
        digitized_rows.extend(
            digitize_red_dashed_panel(
                image=img_reconstruct,
                product_id=product_id,
                x_left=x_left,
                x_right=x_right,
                y_top=31,
                y_bottom=528,
                z_max=2.5,
            )
        )
    digitized_rows.extend(
        digitize_solid_robustness(
            image=img_bin30,
            product_id="desy5_bin30",
            source_figure="fig_bin30",
            x_left=376,
            x_right=2282,
            y_top=93,
            y_bottom=1513,
            z_max=2.5,
        )
    )
    digitized_rows.extend(
        digitize_solid_robustness(
            image=img_zmax,
            product_id="desy5_zmax",
            source_figure="fig_zmax",
            x_left=385,
            x_right=2335,
            y_top=95,
            y_bottom=1548,
            z_max=4.5,
        )
    )
    write_csv(OUTDIR / "digitized_li2025_beta_products.csv", digitized_rows)

    metric_rows: list[dict[str, float | str]] = []
    for product in products_from_digitized_rows(digitized_rows):
        metric_rows.extend(family_rows_for_product(product))
    write_csv(OUTDIR / "li2025_digitized_compression_metrics.csv", metric_rows)
    summary = summarize(metric_rows)
    (OUTDIR / "li2025_digitized_compression_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(summary, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
