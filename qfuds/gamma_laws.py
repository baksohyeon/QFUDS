from __future__ import annotations

from functools import lru_cache
from typing import Literal

import numpy as np

GammaModel = Literal[
    "constant",
    "powerlaw",
    "growth_driven",
    "collapsed_fraction_toy",
    "horizon_entropy",
    "black_hole_entropy_proxy",
    "star_formation_proxy",
]

GAMMA_MODELS: tuple[str, ...] = (
    "constant",
    "powerlaw",
    "growth_driven",
    "collapsed_fraction_toy",
    "horizon_entropy",
    "black_hole_entropy_proxy",
    "star_formation_proxy",
)


def _as_array(a: float | np.ndarray) -> np.ndarray:
    return np.asarray(a, dtype=float)


def _return_shape(a: float | np.ndarray, values: np.ndarray) -> float | np.ndarray:
    if np.isscalar(a):
        return float(values)
    return values


def lcdm_e2(
    a: float | np.ndarray,
    omega_b0: float,
    omega_r0: float,
    omega_a0: float,
    omega_bfoam0: float,
) -> float | np.ndarray:
    scale = _as_array(a)
    e2 = omega_r0 * scale**-4 + (omega_b0 + omega_a0) * scale**-3 + omega_bfoam0
    return _return_shape(a, e2)


def lcdm_omega_m(
    a: float | np.ndarray,
    omega_b0: float,
    omega_r0: float,
    omega_a0: float,
    omega_bfoam0: float,
) -> float | np.ndarray:
    scale = _as_array(a)
    e2 = np.asarray(lcdm_e2(scale, omega_b0, omega_r0, omega_a0, omega_bfoam0))
    omega_m = (omega_b0 + omega_a0) * scale**-3 / e2
    return _return_shape(a, omega_m)


def lcdm_dlnh_dln_a(
    a: float | np.ndarray,
    omega_b0: float,
    omega_r0: float,
    omega_a0: float,
    omega_bfoam0: float,
) -> float | np.ndarray:
    scale = _as_array(a)
    e2 = np.asarray(lcdm_e2(scale, omega_b0, omega_r0, omega_a0, omega_bfoam0))
    de2 = -4.0 * omega_r0 * scale**-4 - 3.0 * (omega_b0 + omega_a0) * scale**-3
    dlnh = 0.5 * de2 / e2
    return _return_shape(a, dlnh)


def gamma_constant(a: float | np.ndarray, gamma0: float) -> float | np.ndarray:
    scale = _as_array(a)
    values = np.full_like(scale, gamma0, dtype=float)
    return _return_shape(a, values)


def gamma_powerlaw(a: float | np.ndarray, gamma0: float, beta: float) -> float | np.ndarray:
    scale = _as_array(a)
    values = gamma0 * scale**beta
    return _return_shape(a, values)


def gamma_growth_driven(
    a: float | np.ndarray,
    gamma0: float,
    omega_b0: float,
    omega_r0: float,
    omega_a0: float,
    omega_bfoam0: float,
    growth_index: float = 0.55,
) -> float | np.ndarray:
    """Toy law proportional to LCDM f=dlnD/dlna ~= Omega_m(a)^growth_index."""

    omega_m = np.asarray(lcdm_omega_m(a, omega_b0, omega_r0, omega_a0, omega_bfoam0))
    values = gamma0 * omega_m**growth_index
    return _return_shape(a, values)


def gamma_collapsed_fraction_toy(
    a: float | np.ndarray,
    gamma0: float,
    collapse_a: float,
    collapse_nu: float,
) -> float | np.ndarray:
    """Toy law proportional to d f_coll / d ln a for a logistic collapsed fraction."""

    scale = _as_array(a)
    fraction = 1.0 / (1.0 + (collapse_a / scale) ** collapse_nu)
    derivative = collapse_nu * fraction * (1.0 - fraction)
    values = gamma0 * derivative / max(collapse_nu / 4.0, 1.0e-12)
    return _return_shape(a, values)


def gamma_horizon_entropy(
    a: float | np.ndarray,
    gamma0: float,
    beta: float,
    omega_b0: float,
    omega_r0: float,
    omega_a0: float,
    omega_bfoam0: float,
) -> float | np.ndarray:
    """Toy law tied to d ln S_H / d ln a for S_H proportional to H^-2.

    The optional a^beta gate is kept explicit because the ungated horizon-entropy
    derivative is nonzero in the radiation and matter eras.
    """

    scale = _as_array(a)
    dln_entropy = -2.0 * np.asarray(
        lcdm_dlnh_dln_a(scale, omega_b0, omega_r0, omega_a0, omega_bfoam0)
    )
    values = gamma0 * np.clip(dln_entropy / 4.0, 0.0, None) * scale**beta
    return _return_shape(a, values)


def gamma_black_hole_entropy_proxy(
    a: float | np.ndarray,
    gamma0: float,
    collapse_a: float,
    collapse_nu: float,
) -> float | np.ndarray:
    """Toy law for dS_BH/dln a using a late logistic SMBH-entropy proxy."""

    return gamma_collapsed_fraction_toy(a, gamma0, collapse_a, collapse_nu)


def _madau_dickinson_shape(a: np.ndarray) -> np.ndarray:
    z_plus_1 = 1.0 / a
    return z_plus_1**2.7 / (1.0 + (z_plus_1 / 2.9) ** 5.6)


@lru_cache(maxsize=1)
def _star_formation_proxy_norm() -> float:
    grid = np.geomspace(1.0e-4, 1.0, 4000)
    return float(np.max(_madau_dickinson_shape(grid)))


def gamma_star_formation_proxy(a: float | np.ndarray, gamma0: float) -> float | np.ndarray:
    """Toy law tied to empirical cosmic SFR shape, normalized to max=gamma0."""

    scale = _as_array(a)
    values = gamma0 * _madau_dickinson_shape(scale) / _star_formation_proxy_norm()
    return _return_shape(a, values)


def evaluate_gamma(
    a: float | np.ndarray,
    *,
    model: str,
    gamma0: float,
    beta: float,
    omega_b0: float,
    omega_r0: float,
    omega_a0: float,
    omega_bfoam0: float,
    collapse_a: float,
    collapse_nu: float,
    growth_index: float,
) -> float | np.ndarray:
    if model == "constant":
        return gamma_constant(a, gamma0)
    if model == "powerlaw":
        return gamma_powerlaw(a, gamma0, beta)
    if model == "growth_driven":
        return gamma_growth_driven(
            a, gamma0, omega_b0, omega_r0, omega_a0, omega_bfoam0, growth_index
        )
    if model == "collapsed_fraction_toy":
        return gamma_collapsed_fraction_toy(a, gamma0, collapse_a, collapse_nu)
    if model == "horizon_entropy":
        return gamma_horizon_entropy(
            a, gamma0, beta, omega_b0, omega_r0, omega_a0, omega_bfoam0
        )
    if model == "black_hole_entropy_proxy":
        return gamma_black_hole_entropy_proxy(a, gamma0, collapse_a, collapse_nu)
    if model == "star_formation_proxy":
        return gamma_star_formation_proxy(a, gamma0)
    raise ValueError(f"Unknown gamma model: {model}")
