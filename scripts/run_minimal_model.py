from __future__ import annotations

import argparse
import csv
import sys
from pathlib import Path

try:
    import matplotlib.pyplot as plt
except ModuleNotFoundError:  # pragma: no cover - depends on local environment
    plt = None

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from qfuds import (
    GAMMA_MODELS,
    CosmologyParams,
    QFUDSParams,
    add_lcdm_comparison,
    evaluate_viability,
    integrate_background,
    integrate_growth,
)
from qfuds.diagnostics import classify_gamma_model


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the minimal QFUDS two-phase toy model.")
    parser.add_argument("--gamma-model", choices=GAMMA_MODELS, default="powerlaw")
    parser.add_argument("--gamma0", type=float, default=0.0, help="Phase-transfer amplitude. 0 is exact LCDM.")
    parser.add_argument("--beta", type=float, default=0.0, help="Power-law transfer redshift dependence.")
    parser.add_argument("--collapse-a", type=float, default=0.35, help="Toy collapse/BH entropy logistic midpoint.")
    parser.add_argument("--collapse-nu", type=float, default=5.0, help="Toy collapse/BH entropy logistic steepness.")
    parser.add_argument("--all-v03", action="store_true", help="Run the default v0.3 Gamma-law suite.")
    parser.add_argument("--all-v04", action="store_true", help="Run the entropy-derived v0.4 comparison suite.")
    parser.add_argument("--outdir", type=Path, default=Path("outputs"))
    return parser.parse_args()


def _filename_stem(qfuds: QFUDSParams) -> str:
    if qfuds.gamma_model == "powerlaw":
        return f"qfuds_gamma{qfuds.gamma0:g}_beta{qfuds.beta:g}"
    return f"qfuds_{qfuds.gamma_model}_gamma{qfuds.gamma0:g}_beta{qfuds.beta:g}"


def _run_one(cosmo: CosmologyParams, qfuds: QFUDSParams, outdir: Path) -> dict[str, object]:
    background = integrate_background(cosmo, qfuds)
    growth = integrate_growth(background)
    lcdm = integrate_background(cosmo, QFUDSParams(gamma0=0.0, beta=0.0))
    lcdm_growth = integrate_growth(lcdm)
    comparison = add_lcdm_comparison(background, growth, lcdm, lcdm_growth)
    viability = evaluate_viability(background, growth, lcdm, lcdm_growth)

    csv_path = outdir / f"{_filename_stem(qfuds)}.csv"
    with csv_path.open("w", newline="") as handle:
        writer = csv.writer(handle, lineterminator="\n")
        writer.writerow(
            [
                "a",
                "z",
                "Gamma",
                "H_km_s_Mpc",
                "H_over_H_LCDM",
                "rho_A_over_rhocrit0",
                "rho_Bfoam_over_rhocrit0",
                "Omega_A",
                "Omega_Bfoam",
                "Omega_clustering",
                "w_dark",
                "w_Bfoam_eff",
                "w_eff",
                "D",
                "f",
                "f_sigma8_proxy",
                "delta_w_dark_vs_LCDM",
                "delta_f_sigma8_vs_LCDM",
            ]
        )
        for i, a in enumerate(background["a"]):
            writer.writerow(
                [
                    a,
                    background["z"][i],
                    background["Gamma"][i],
                    background["H"][i],
                    comparison["H_over_H_LCDM"][i],
                    background["omega_A"][i],
                    background["omega_Bfoam"][i],
                    background["Omega_A"][i],
                    background["Omega_Bfoam"][i],
                    background["Omega_clustering"][i],
                    background["w_dark"][i],
                    background["w_Bfoam_eff"][i],
                    background["w_eff"][i],
                    growth["D"][i],
                    growth["f"][i],
                    comparison["f_sigma8"][i],
                    comparison["delta_w_dark"][i],
                    comparison["delta_f_sigma8"][i],
                ]
            )

    print(f"Wrote {csv_path}")
    print(f"Classification: {classify_gamma_model(qfuds.gamma_model, qfuds.gamma0, viability)}")
    print(f"Viability: {viability.as_dict()}")

    if plt is None:
        print("Skipped plot: matplotlib is not installed")
        return {"csv": csv_path, "png": None, "viability": viability}

    fig, axes = plt.subplots(2, 2, figsize=(10, 7), constrained_layout=True)
    axes[0, 0].plot(background["a"], comparison["H_over_H_LCDM"])
    axes[0, 0].set(xlabel="a", ylabel="H(a) / H_LCDM(a)", xscale="log")

    axes[0, 1].plot(background["a"], background["Omega_A"], label="Phase A")
    axes[0, 1].plot(background["a"], background["Omega_Bfoam"], label="Phase B")
    axes[0, 1].plot(background["a"], background["Omega_clustering"], label="clustering total")
    axes[0, 1].set(xlabel="a", ylabel="Omega(a)", xscale="log")
    axes[0, 1].legend(frameon=False, fontsize=8)

    axes[1, 0].plot(background["a"], background["w_dark"], label="dark sector")
    axes[1, 0].plot(background["a"], background["w_Bfoam_eff"], label="B effective")
    axes[1, 0].set(xlabel="a", ylabel="w(a)", xscale="log")
    axes[1, 0].legend(frameon=False, fontsize=8)

    axes[1, 1].plot(background["z"], comparison["delta_w_dark"], label="Delta w")
    axes[1, 1].plot(background["z"], comparison["delta_f_sigma8"], label="Delta f sigma8")
    axes[1, 1].set(xlabel="z", ylabel="LCDM difference", xlim=(0, 5))
    axes[1, 1].legend(frameon=False, fontsize=8)

    png_path = outdir / f"{_filename_stem(qfuds)}.png"
    fig.savefig(png_path, dpi=160)
    print(f"Wrote {png_path}")
    return {"csv": csv_path, "png": png_path, "viability": viability}


def _default_v03_suite(args: argparse.Namespace) -> list[QFUDSParams]:
    return [
        QFUDSParams(gamma_model="constant", gamma0=0.01, beta=0.0),
        QFUDSParams(gamma_model="powerlaw", gamma0=0.03, beta=5.0),
        QFUDSParams(gamma_model="growth_driven", gamma0=0.01, beta=0.0),
        QFUDSParams(
            gamma_model="collapsed_fraction_toy",
            gamma0=0.03,
            beta=0.0,
            collapse_a=args.collapse_a,
            collapse_nu=args.collapse_nu,
        ),
        QFUDSParams(gamma_model="horizon_entropy", gamma0=0.03, beta=4.0),
        QFUDSParams(
            gamma_model="black_hole_entropy_proxy",
            gamma0=0.03,
            beta=0.0,
            collapse_a=0.35,
            collapse_nu=6.0,
        ),
        QFUDSParams(gamma_model="star_formation_proxy", gamma0=0.003, beta=0.0),
    ]


def _default_v04_suite(args: argparse.Namespace) -> list[QFUDSParams]:
    return [
        QFUDSParams(
            gamma_model="collapsed_fraction_toy",
            gamma0=0.03,
            beta=0.0,
            collapse_a=args.collapse_a,
            collapse_nu=args.collapse_nu,
        ),
        QFUDSParams(
            gamma_model="black_hole_entropy_proxy",
            gamma0=0.03,
            beta=0.0,
            collapse_a=0.35,
            collapse_nu=6.0,
        ),
        QFUDSParams(gamma_model="star_formation_proxy", gamma0=0.003, beta=0.0),
        QFUDSParams(gamma_model="gravitational_entropy", gamma0=0.003, beta=0.0),
        QFUDSParams(
            gamma_model="information_production",
            gamma0=0.02,
            beta=0.0,
            collapse_a=args.collapse_a,
            collapse_nu=args.collapse_nu,
        ),
        QFUDSParams(gamma_model="horizon_information", gamma0=0.03, beta=0.0),
    ]


def main() -> None:
    args = parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    cosmo = CosmologyParams()
    if args.all_v03:
        for qfuds in _default_v03_suite(args):
            _run_one(cosmo, qfuds, args.outdir)
        return
    if args.all_v04:
        for qfuds in _default_v04_suite(args):
            _run_one(cosmo, qfuds, args.outdir)
        return

    qfuds = QFUDSParams(
        gamma0=args.gamma0,
        beta=args.beta,
        gamma_model=args.gamma_model,
        collapse_a=args.collapse_a,
        collapse_nu=args.collapse_nu,
    )
    _run_one(cosmo, qfuds, args.outdir)


if __name__ == "__main__":
    main()
