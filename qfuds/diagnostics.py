from __future__ import annotations

from dataclasses import dataclass

import numpy as np


@dataclass(frozen=True)
class ViabilityReport:
    positive_rho_a: bool
    positive_rho_b: bool
    early_b_max: float
    early_b_safe: bool
    cmb_h_close_max: float
    cmb_close: bool
    matter_domination: bool
    growth_ratio_min: float
    growth_preserved: bool

    @property
    def passes_minimal_checks(self) -> bool:
        return (
            self.positive_rho_a
            and self.positive_rho_b
            and self.early_b_safe
            and self.cmb_close
            and self.matter_domination
            and self.growth_preserved
        )

    def as_dict(self) -> dict[str, float | bool]:
        return {
            "positive_rho_a": self.positive_rho_a,
            "positive_rho_b": self.positive_rho_b,
            "early_b_max": self.early_b_max,
            "early_b_safe": self.early_b_safe,
            "cmb_h_close_max": self.cmb_h_close_max,
            "cmb_close": self.cmb_close,
            "matter_domination": self.matter_domination,
            "growth_ratio_min": self.growth_ratio_min,
            "growth_preserved": self.growth_preserved,
            "passes_minimal_checks": self.passes_minimal_checks,
        }


def add_lcdm_comparison(
    background: dict[str, np.ndarray],
    growth: dict[str, np.ndarray],
    lcdm_background: dict[str, np.ndarray],
    lcdm_growth: dict[str, np.ndarray],
    sigma8_0: float = 0.811,
) -> dict[str, np.ndarray]:
    h_ratio = background["H"] / lcdm_background["H"]
    f_sigma8 = growth["f"] * growth["D"] * sigma8_0
    lcdm_f_sigma8 = lcdm_growth["f"] * lcdm_growth["D"] * sigma8_0
    return {
        "H_over_H_LCDM": h_ratio,
        "f_sigma8": f_sigma8,
        "f_sigma8_LCDM": lcdm_f_sigma8,
        "delta_w_dark": background["w_dark"] - lcdm_background["w_dark"],
        "delta_f_sigma8": f_sigma8 - lcdm_f_sigma8,
    }


def evaluate_viability(
    background: dict[str, np.ndarray],
    growth: dict[str, np.ndarray],
    lcdm_background: dict[str, np.ndarray],
    lcdm_growth: dict[str, np.ndarray],
) -> ViabilityReport:
    a = background["a"]
    early_mask = a <= 1.0e-3
    pre_de_mask = (a >= 1.0e-3) & (a <= 0.5)

    h_ratio = background["H"] / lcdm_background["H"]
    growth_ratio = np.divide(
        growth["D"],
        lcdm_growth["D"],
        out=np.full_like(growth["D"], np.nan),
        where=lcdm_growth["D"] != 0.0,
    )

    early_b_max = float(np.max(background["Omega_Bfoam"][early_mask]))
    cmb_h_close_max = float(np.max(np.abs(h_ratio[early_mask] - 1.0)))
    growth_ratio_min = float(np.nanmin(growth_ratio[pre_de_mask]))
    matter_domination = bool(np.max(background["Omega_clustering"][pre_de_mask]) > 0.45)

    return ViabilityReport(
        positive_rho_a=bool(np.all(background["omega_A"] > 0.0)),
        positive_rho_b=bool(np.all(background["omega_Bfoam"] > 0.0)),
        early_b_max=early_b_max,
        early_b_safe=early_b_max < 0.01,
        cmb_h_close_max=cmb_h_close_max,
        cmb_close=cmb_h_close_max < 0.01,
        matter_domination=matter_domination,
        growth_ratio_min=growth_ratio_min,
        growth_preserved=growth_ratio_min > 0.8,
    )


def classify_gamma_model(model: str, gamma0: float, viability: ViabilityReport) -> str:
    if gamma0 == 0.0:
        return "A. trivial reparameterization of LCDM"
    if not viability.positive_rho_a or not viability.positive_rho_b:
        return "D. unstable or observationally dead"
    if not viability.early_b_safe or not viability.cmb_close or not viability.growth_preserved:
        return "D. unstable or observationally dead"
    if model in {"constant", "powerlaw", "growth_driven"}:
        return "B. standard interacting dark energy"
    if model == "horizon_entropy":
        return "B. standard interacting dark energy"
    if model in {"collapsed_fraction_toy", "black_hole_entropy_proxy", "star_formation_proxy"}:
        return "E. potentially interesting"
    return "C. unified dark fluid equivalent"
