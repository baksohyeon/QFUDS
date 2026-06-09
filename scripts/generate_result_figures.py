#!/usr/bin/env python3
"""Generate visual diagnostics used by docs/04_results.

These figures are explanatory views over existing CSV/JSON outputs. They do not
change experiment conclusions and do not introduce new model runs.
"""

from __future__ import annotations

import csv
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import matplotlib.pyplot as plt
import numpy as np

from qfuds.plotting import save_figure_pair


OUT = ROOT / "outputs"
FIG = OUT / "figures"


def _read_csv(path: Path) -> dict[str, np.ndarray]:
    with path.open(newline="") as handle:
        rows = list(csv.DictReader(handle))
    data: dict[str, list[float]] = {}
    for row in rows:
        for key, value in row.items():
            try:
                data.setdefault(key, []).append(float(value))
            except (TypeError, ValueError):
                continue
    return {key: np.asarray(values, dtype=float) for key, values in data.items()}


def _norm(values: np.ndarray) -> np.ndarray:
    peak = max(float(np.nanmax(np.abs(values))), 1.0e-30)
    return values / peak


def result000_lcdm_baseline() -> list[str]:
    data = _read_csv(OUT / "qfuds_gamma0_beta0.csv")
    fig, axes = plt.subplots(1, 2, figsize=(10, 4.2), constrained_layout=True)
    axes[0].plot(data["a"], data["H_over_H_LCDM"])
    axes[0].plot(data["a"], data["Gamma"])
    axes[0].set(xlabel="a", ylabel="control value", xscale="log", title="LCDM-control invariants")
    axes[0].legend(["H/H_LCDM", "Gamma"], frameon=False)
    axes[1].plot(data["a"], data["Omega_A"], label="phase A")
    axes[1].plot(data["a"], data["Omega_Bfoam"], label="phase B")
    axes[1].set(xlabel="a", ylabel="Omega(a)", xscale="log", title="Two-phase bookkeeping")
    axes[1].legend(frameon=False)
    return save_figure_pair(fig, FIG / "result000_lcdm_baseline")


def result001_gamma_scan_summary() -> list[str]:
    models = [
        ("constant", OUT / "qfuds_constant_gamma0.01_beta0.csv", "rejected"),
        ("powerlaw", OUT / "qfuds_gamma0.03_beta5.csv", "survived bg"),
        ("growth", OUT / "qfuds_growth_driven_gamma0.01_beta0.csv", "rejected"),
        ("collapsed", OUT / "qfuds_collapsed_fraction_toy_gamma0.03_beta0.csv", "survived bg"),
        ("horizon", OUT / "qfuds_horizon_entropy_gamma0.03_beta4.csv", "survived bg"),
        ("BH proxy", OUT / "qfuds_black_hole_entropy_proxy_gamma0.03_beta0.csv", "survived bg"),
        ("SFR proxy", OUT / "qfuds_star_formation_proxy_gamma0.003_beta0.csv", "survived bg"),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(12, 4.8), constrained_layout=True)
    labels: list[str] = []
    early_errors: list[float] = []
    min_rho_b: list[float] = []
    colors: list[str] = []
    for label, path, status in models:
        data = _read_csv(path)
        axes[0].plot(data["z"], _norm(data["Gamma"]), label=label)
        early = data["z"] > 1100.0
        labels.append(label)
        early_errors.append(float(np.nanmax(np.abs(data["H_over_H_LCDM"][early] - 1.0))))
        min_rho_b.append(float(np.nanmin(data["rho_Bfoam_over_rhocrit0"])))
        colors.append("#b84a4a" if status == "rejected" else "#2f6f9f")
    axes[0].set(xlabel="z", ylabel="normalized Gamma(a)", xlim=(8.0, 0.0), title="Timing shapes")
    axes[0].legend(frameon=False, fontsize=8)
    x = np.arange(len(labels))
    axes[1].bar(x - 0.18, early_errors, width=0.36, color=colors, label="early |H/H_LCDM-1|")
    axes[1].bar(x + 0.18, np.maximum(-np.asarray(min_rho_b), 0.0), width=0.36, color="#7a7a7a", label="negative rho_B depth")
    axes[1].set_xticks(x, labels, rotation=35, ha="right")
    axes[1].set_yscale("log")
    axes[1].set_ylabel("failure pressure")
    axes[1].set_title("Background-screening pressure")
    axes[1].legend(frameon=False, fontsize=8)
    return save_figure_pair(fig, FIG / "result001_gamma_scan_summary")


def result001_5_physicality_audit() -> list[str]:
    labels = ["source X", "threshold M", "self-consistent growth", "Q^nu", "phase-B pressure", "delta Q"]
    values = np.asarray([[0, 0, 0, 0, 0, 0]], dtype=float)
    fig, ax = plt.subplots(figsize=(10, 2.8), constrained_layout=True)
    image = ax.imshow(values, cmap="Reds_r", vmin=0.0, vmax=1.0, aspect="auto")
    _ = image
    ax.set_xticks(np.arange(len(labels)), labels, rotation=25, ha="right")
    ax.set_yticks([0], ["retained branch"])
    ax.set_title("Level 1.5 physical-promotion ingredients")
    for i, label in enumerate(labels):
        ax.text(i, 0, "missing", ha="center", va="center", color="white", fontsize=10, fontweight="bold")
    return save_figure_pair(fig, FIG / "result001_5_physicality_audit")


def result002_entropy_information_summary() -> list[str]:
    models = [
        ("gravitational entropy", OUT / "qfuds_gravitational_entropy_gamma0.003_beta0.csv", "failed"),
        ("horizon information", OUT / "qfuds_horizon_information_gamma0.03_beta0.csv", "known-model-like"),
        ("information production", OUT / "qfuds_information_production_gamma0.02_beta0.csv", "retained as proxy"),
    ]
    fig, axes = plt.subplots(1, 2, figsize=(11, 4.5), constrained_layout=True)
    labels: list[str] = []
    min_rho_b: list[float] = []
    h_errors: list[float] = []
    for label, path, _ in models:
        data = _read_csv(path)
        axes[0].plot(data["z"], _norm(data["Gamma"]), label=label)
        labels.append(label)
        min_rho_b.append(float(np.nanmin(data["rho_Bfoam_over_rhocrit0"])))
        h_errors.append(float(np.nanmax(np.abs(data["H_over_H_LCDM"] - 1.0))))
    axes[0].set(xlabel="z", ylabel="normalized Gamma(a)", xlim=(8.0, 0.0), title="Source-shape timing")
    axes[0].legend(frameon=False, fontsize=8)
    x = np.arange(len(labels))
    axes[1].bar(x - 0.18, h_errors, width=0.36, label="max |H/H_LCDM-1|")
    axes[1].bar(x + 0.18, np.maximum(-np.asarray(min_rho_b), 0.0), width=0.36, label="negative rho_B depth")
    axes[1].set_xticks(x, labels, rotation=25, ha="right")
    axes[1].set_yscale("log")
    axes[1].set_ylabel("diagnostic pressure")
    axes[1].set_title("Why only one proxy remained")
    axes[1].legend(frameon=False, fontsize=8)
    return save_figure_pair(fig, FIG / "result002_entropy_information_summary")


def main() -> int:
    FIG.mkdir(parents=True, exist_ok=True)
    generated: list[str] = []
    for builder in (
        result000_lcdm_baseline,
        result001_gamma_scan_summary,
        result001_5_physicality_audit,
        result002_entropy_information_summary,
    ):
        generated.extend(builder())
        plt.close("all")
    for path in generated:
        print(path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
