from __future__ import annotations

import importlib
import sys
import unittest
from contextlib import contextmanager
from pathlib import Path

import numpy as np


ASSET_DIR = (
    Path(__file__).resolve().parents[1]
    / "docs"
    / "wiki"
    / "lineage"
    / "assets"
    / "004_rough_tanh"
)
LINEAGE_MODULES = (
    "model",
    "density_driven",
    "cp5_sound_speed",
    "cp16_growth_index",
)


@contextmanager
def rough_tanh_import_context():
    old_path = list(sys.path)
    old_modules = {
        name: sys.modules[name]
        for name in LINEAGE_MODULES
        if name in sys.modules
    }
    sys.path.insert(0, str(ASSET_DIR))
    for name in LINEAGE_MODULES:
        sys.modules.pop(name, None)
    try:
        yield
    finally:
        for name in LINEAGE_MODULES:
            sys.modules.pop(name, None)
        sys.modules.update(old_modules)
        sys.path[:] = old_path


class RoughTanhLineageAssetTests(unittest.TestCase):
    def test_shared_model_normalizations_and_limits(self) -> None:
        with rough_tanh_import_context():
            model = importlib.import_module("model")

            self.assertAlmostEqual(
                model.OMEGA_B0 + model.OMEGA_R0 + model.OMEGA_Q0,
                1.0,
                places=14,
            )
            self.assertAlmostEqual(
                model.OMEGA_M0_LCDM + model.OMEGA_R0_LCDM + model.OMEGA_L0_LCDM,
                1.0,
                places=14,
            )
            self.assertAlmostEqual(
                model.OMEGA_M0_V2 + model.OMEGA_R0 + model.OMEGA_X0_V2,
                1.0,
                places=14,
            )
            self.assertAlmostEqual(float(model.E_LCDM(1.0)), 1.0, places=14)
            self.assertAlmostEqual(float(model.E_QFUDS(1.0)), 1.0, places=14)
            self.assertAlmostEqual(float(model.E_QFUDS_V2(1.0)), 1.0, places=14)
            self.assertGreater(float(model.w_Q(1.0e-3)), -1.0e-5)
            self.assertLess(float(model.w_Q(1.0)), -0.99999)
            self.assertAlmostEqual(
                float(model.rho_X_over_crit(1.0)),
                model.OMEGA_X0_V2,
                places=14,
            )

    def test_density_driven_background_matches_constant_w_limits(self) -> None:
        with rough_tanh_import_context():
            model = importlib.import_module("model")
            density_driven = importlib.import_module("density_driven")

            a = density_driven.A_GRID
            omega_m0 = model.OMEGA_M0_V2
            omega_x0 = 1.0 - omega_m0 - model.OMEGA_R0

            E_vacuum = density_driven.background_from_w(
                np.full_like(a, -1.0),
                omega_m0=omega_m0,
            )
            expected_vacuum_e2 = (
                omega_m0 * a**-3
                + model.OMEGA_R0 * a**-4
                + omega_x0
            )
            np.testing.assert_allclose(
                E_vacuum**2,
                expected_vacuum_e2,
                rtol=2.0e-12,
                atol=2.0e-12,
            )

            E_matterlike = density_driven.background_from_w(
                np.zeros_like(a),
                omega_m0=omega_m0,
            )
            expected_matterlike_e2 = (
                (omega_m0 + omega_x0) * a**-3
                + model.OMEGA_R0 * a**-4
            )
            np.testing.assert_allclose(
                E_matterlike**2,
                expected_matterlike_e2,
                rtol=3.0e-12,
                atol=1.0e-8,
            )

    def test_cp16_scale_dependence_band_interpolates_on_scale_factor(self) -> None:
        with rough_tanh_import_context():
            cp16 = importlib.import_module("cp16_growth_index")

            n_grid = np.linspace(np.log(cp16.A_I), 0.0, 120)
            a_reference = np.array([0.25, 0.5, 1.0])
            k_values = [0.05, 0.2]
            curves = cp16.gamma_eff_scale_curves(
                n_grid,
                cp16.C2,
                k_values,
                a_reference,
            )

            self.assertEqual(curves.shape, (len(k_values), len(a_reference)))
            ak, Dk, Dpk = cp16.growth_qfuds(n_grid, cp16.C2, k_values[0])
            direct = np.interp(
                a_reference,
                ak,
                cp16.gamma_eff(Dpk / Dk, cp16.Om_qfuds(ak)),
            )
            np.testing.assert_allclose(curves[0], direct, rtol=1.0e-12, atol=1.0e-12)


if __name__ == "__main__":
    unittest.main()
