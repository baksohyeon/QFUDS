from __future__ import annotations

from dataclasses import dataclass

import numpy as np

from .gamma_laws import GAMMA_MODELS, evaluate_gamma


@dataclass(frozen=True)
class CosmologyParams:
    """Flat background parameters normalized at a=1."""

    h0: float = 67.4
    omega_b0: float = 0.0493
    omega_r0: float = 9.2e-5
    omega_a0: float = 0.2649
    omega_bfoam0: float = 0.6858


@dataclass(frozen=True)
class QFUDSParams:
    """Phenomenological phase-transfer parameters.

    gamma0 controls energy exchange between clustering phase A and vacuum-like
    phase B. gamma_model selects the dimensionless transfer law. beta controls
    redshift dependence for power-law and gated horizon-entropy laws. gamma0=0
    gives exact LCDM. Positive gamma transfers A -> B.
    """

    gamma0: float = 0.0
    beta: float = 0.0
    cs2_a: float = 0.0
    gamma_model: str = "powerlaw"
    collapse_a: float = 0.35
    collapse_nu: float = 5.0
    growth_index: float = 0.55


def transfer_rate(a: float | np.ndarray, q: QFUDSParams, cosmo: CosmologyParams | None = None) -> float | np.ndarray:
    """Dimensionless d rho / d ln a transfer term."""

    if q.gamma_model not in GAMMA_MODELS:
        raise ValueError(f"Unknown gamma model: {q.gamma_model}")
    if cosmo is None:
        cosmo = CosmologyParams()
    return evaluate_gamma(
        a,
        model=q.gamma_model,
        gamma0=q.gamma0,
        beta=q.beta,
        omega_b0=cosmo.omega_b0,
        omega_r0=cosmo.omega_r0,
        omega_a0=cosmo.omega_a0,
        omega_bfoam0=cosmo.omega_bfoam0,
        collapse_a=q.collapse_a,
        collapse_nu=q.collapse_nu,
        growth_index=q.growth_index,
    )


def _derivs(
    a: float,
    omega_a: float,
    omega_bfoam: float,
    q: QFUDSParams,
    cosmo: CosmologyParams,
) -> tuple[float, float]:
    gamma = float(transfer_rate(a, q, cosmo))
    d_omega_a = -3.0 * omega_a - gamma * omega_a
    d_omega_bfoam = gamma * omega_a
    return d_omega_a, d_omega_bfoam


def integrate_background(
    cosmo: CosmologyParams,
    qfuds: QFUDSParams,
    a_min: float = 1.0e-4,
    a_max: float = 1.0,
    n: int = 1200,
) -> dict[str, np.ndarray]:
    """Integrate the two-phase dark sector backward from a=1.

    The integration variable is x = ln a. Densities are in units of today's
    critical density. The equations are written forward in x, but solved on a
    descending grid from x=0 to x_min so that the supplied present-day values
    are exact boundary data.
    """

    x_desc = np.linspace(np.log(a_max), np.log(a_min), n)
    a_desc = np.exp(x_desc)
    omega_a_desc = np.empty(n)
    omega_bfoam_desc = np.empty(n)
    omega_a_desc[0] = cosmo.omega_a0
    omega_bfoam_desc[0] = cosmo.omega_bfoam0

    for i in range(n - 1):
        x = x_desc[i]
        dx = x_desc[i + 1] - x
        a = float(np.exp(x))
        y_a = float(omega_a_desc[i])
        y_b = float(omega_bfoam_desc[i])

        def f(xi: float, ya: float, yb: float) -> tuple[float, float]:
            return _derivs(float(np.exp(xi)), ya, yb, qfuds, cosmo)

        k1a, k1b = f(x, y_a, y_b)
        k2a, k2b = f(x + 0.5 * dx, y_a + 0.5 * dx * k1a, y_b + 0.5 * dx * k1b)
        k3a, k3b = f(x + 0.5 * dx, y_a + 0.5 * dx * k2a, y_b + 0.5 * dx * k2b)
        k4a, k4b = f(x + dx, y_a + dx * k3a, y_b + dx * k3b)
        omega_a_desc[i + 1] = y_a + dx * (k1a + 2.0 * k2a + 2.0 * k3a + k4a) / 6.0
        omega_bfoam_desc[i + 1] = y_b + dx * (k1b + 2.0 * k2b + 2.0 * k3b + k4b) / 6.0

    order = np.arange(n - 1, -1, -1)
    a = a_desc[order]
    omega_a = omega_a_desc[order]
    omega_bfoam = omega_bfoam_desc[order]
    omega_baryon = cosmo.omega_b0 * a**-3
    omega_rad = cosmo.omega_r0 * a**-4
    e2 = omega_rad + omega_baryon + omega_a + omega_bfoam
    h = cosmo.h0 * np.sqrt(e2)
    omega_total_dark = omega_a + omega_bfoam
    w_dark = -omega_bfoam / omega_total_dark
    w_eff = (omega_rad / 3.0 - omega_bfoam) / e2
    omega_clustering_frac = (omega_baryon + omega_a) / e2
    omega_a_frac = omega_a / e2
    omega_bfoam_frac = omega_bfoam / e2
    gamma = np.asarray(transfer_rate(a, qfuds, cosmo), dtype=float)
    w_bfoam_eff = -1.0 - gamma * omega_a / (3.0 * omega_bfoam)

    return {
        "a": a,
        "z": 1.0 / a - 1.0,
        "H": h,
        "E2": e2,
        "omega_A": omega_a,
        "omega_Bfoam": omega_bfoam,
        "omega_baryon": omega_baryon,
        "omega_radiation": omega_rad,
        "Omega_A": omega_a_frac,
        "Omega_Bfoam": omega_bfoam_frac,
        "Omega_clustering": omega_clustering_frac,
        "w_dark": w_dark,
        "w_Bfoam_eff": w_bfoam_eff,
        "w_eff": w_eff,
        "Gamma": gamma,
    }
