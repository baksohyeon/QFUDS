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

from qfuds import CosmologyParams, QFUDSParams, integrate_background, integrate_growth


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the minimal QFUDS two-phase toy model.")
    parser.add_argument("--gamma0", type=float, default=0.0, help="Phase-transfer amplitude. 0 is exact LCDM.")
    parser.add_argument("--beta", type=float, default=0.0, help="Power-law transfer redshift dependence.")
    parser.add_argument("--outdir", type=Path, default=Path("outputs"))
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    args.outdir.mkdir(parents=True, exist_ok=True)

    cosmo = CosmologyParams()
    qfuds = QFUDSParams(gamma0=args.gamma0, beta=args.beta)
    background = integrate_background(cosmo, qfuds)
    growth = integrate_growth(background)

    csv_path = args.outdir / f"qfuds_gamma{args.gamma0:g}_beta{args.beta:g}.csv"
    with csv_path.open("w", newline="") as handle:
        writer = csv.writer(handle)
        writer.writerow(
            [
                "a",
                "z",
                "H_km_s_Mpc",
                "Omega_A",
                "Omega_Bfoam",
                "Omega_clustering",
                "w_dark",
                "w_eff",
                "D",
                "f",
            ]
        )
        for i, a in enumerate(background["a"]):
            writer.writerow(
                [
                    a,
                    background["z"][i],
                    background["H"][i],
                    background["Omega_A"][i],
                    background["Omega_Bfoam"][i],
                    background["Omega_clustering"][i],
                    background["w_dark"][i],
                    background["w_eff"][i],
                    growth["D"][i],
                    growth["f"][i],
                ]
            )

    print(f"Wrote {csv_path}")

    if plt is None:
        print("Skipped plot: matplotlib is not installed")
        return

    fig, axes = plt.subplots(2, 2, figsize=(10, 7), constrained_layout=True)
    axes[0, 0].plot(background["a"], background["H"])
    axes[0, 0].set(xlabel="a", ylabel="H(a) [km/s/Mpc]", xscale="log")

    axes[0, 1].plot(background["a"], background["Omega_A"], label="Phase A")
    axes[0, 1].plot(background["a"], background["Omega_Bfoam"], label="Phase B")
    axes[0, 1].plot(background["a"], background["Omega_clustering"], label="clustering total")
    axes[0, 1].set(xlabel="a", ylabel="Omega(a)", xscale="log")
    axes[0, 1].legend(frameon=False, fontsize=8)

    axes[1, 0].plot(background["a"], background["w_dark"], label="dark sector")
    axes[1, 0].plot(background["a"], background["w_eff"], label="total")
    axes[1, 0].set(xlabel="a", ylabel="w(a)", xscale="log")
    axes[1, 0].legend(frameon=False, fontsize=8)

    axes[1, 1].plot(growth["a"], growth["D"], label="D")
    axes[1, 1].plot(growth["a"], growth["f"], label="f")
    axes[1, 1].set(xlabel="a", ylabel="growth", xscale="log")
    axes[1, 1].legend(frameon=False, fontsize=8)

    png_path = args.outdir / f"qfuds_gamma{args.gamma0:g}_beta{args.beta:g}.png"
    fig.savefig(png_path, dpi=160)
    print(f"Wrote {png_path}")


if __name__ == "__main__":
    main()
