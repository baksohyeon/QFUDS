from __future__ import annotations

import numpy as np


def _interp(x_grid: np.ndarray, y_grid: np.ndarray, x: float) -> float:
    return float(np.interp(x, x_grid, y_grid))


def integrate_growth(background: dict[str, np.ndarray], n: int | None = None) -> dict[str, np.ndarray]:
    """Integrate scale-independent linear growth for clustered matter.

    This is the standard sub-horizon GR growth equation with smooth vacuum-like
    phase B. It is valid only for cs_A^2 approximately zero and no phase-B
    perturbations:

    D_xx + [2 + d ln H / d ln a] D_x - 3 Omega_clustering(a) D / 2 = 0.
    """

    a_bg = background["a"]
    x_bg = np.log(a_bg)
    e2_bg = background["E2"]
    omega_cl_bg = background["Omega_clustering"]
    dlnh_dx_bg = 0.5 * np.gradient(np.log(e2_bg), x_bg)

    if n is None:
        n = len(a_bg)
    x = np.linspace(float(x_bg[0]), float(x_bg[-1]), n)
    a = np.exp(x)
    y = np.empty((n, 2))
    y[0, 0] = a[0]
    y[0, 1] = a[0]

    def rhs(xi: float, d: float, u: float) -> tuple[float, float]:
        omega_cl = _interp(x_bg, omega_cl_bg, xi)
        friction = 2.0 + _interp(x_bg, dlnh_dx_bg, xi)
        return u, 1.5 * omega_cl * d - friction * u

    for i in range(n - 1):
        dx = x[i + 1] - x[i]
        d, u = float(y[i, 0]), float(y[i, 1])
        k1d, k1u = rhs(float(x[i]), d, u)
        k2d, k2u = rhs(float(x[i] + 0.5 * dx), d + 0.5 * dx * k1d, u + 0.5 * dx * k1u)
        k3d, k3u = rhs(float(x[i] + 0.5 * dx), d + 0.5 * dx * k2d, u + 0.5 * dx * k2u)
        k4d, k4u = rhs(float(x[i] + dx), d + dx * k3d, u + dx * k3u)
        y[i + 1, 0] = d + dx * (k1d + 2.0 * k2d + 2.0 * k3d + k4d) / 6.0
        y[i + 1, 1] = u + dx * (k1u + 2.0 * k2u + 2.0 * k3u + k4u) / 6.0

    growth = y[:, 0] / y[-1, 0]
    rate = y[:, 1] / y[:, 0]
    return {"a": a, "z": 1.0 / a - 1.0, "D": growth, "f": rate}

