from __future__ import annotations

import unittest

import numpy as np

from qfuds import (
    GAMMA_MODELS,
    CosmologyParams,
    QFUDSParams,
    add_lcdm_comparison,
    evaluate_viability,
    integrate_background,
    integrate_growth,
)


class GammaV03Tests(unittest.TestCase):
    def setUp(self) -> None:
        self.cosmo = CosmologyParams()
        self.lcdm = integrate_background(self.cosmo, QFUDSParams(gamma0=0.0), n=300)
        self.lcdm_growth = integrate_growth(self.lcdm)

    def test_gamma_zero_reproduces_lcdm_powerlaw_path(self) -> None:
        other = integrate_background(
            self.cosmo,
            QFUDSParams(gamma_model="powerlaw", gamma0=0.0, beta=5.0),
            n=300,
        )
        np.testing.assert_allclose(other["omega_A"], self.lcdm["omega_A"])
        np.testing.assert_allclose(other["omega_Bfoam"], self.lcdm["omega_Bfoam"])
        np.testing.assert_allclose(other["H"], self.lcdm["H"])

    def test_each_gamma_model_returns_finite_aligned_arrays(self) -> None:
        for model in GAMMA_MODELS:
            with self.subTest(model=model):
                qfuds = QFUDSParams(gamma_model=model, gamma0=0.01, beta=4.0)
                background = integrate_background(self.cosmo, qfuds, n=300)
                growth = integrate_growth(background)
                comparison = add_lcdm_comparison(
                    background, growth, self.lcdm, self.lcdm_growth
                )
                expected_len = len(background["a"])

                for values in background.values():
                    self.assertEqual(len(values), expected_len)
                    self.assertTrue(np.all(np.isfinite(values)))
                for values in growth.values():
                    self.assertEqual(len(values), expected_len)
                    self.assertTrue(np.all(np.isfinite(values)))
                for values in comparison.values():
                    self.assertEqual(len(values), expected_len)
                    self.assertTrue(np.all(np.isfinite(values)))

    def test_viability_flags_are_explicit_booleans(self) -> None:
        background = integrate_background(
            self.cosmo,
            QFUDSParams(gamma_model="collapsed_fraction_toy", gamma0=0.04),
            n=300,
        )
        growth = integrate_growth(background)
        report = evaluate_viability(background, growth, self.lcdm, self.lcdm_growth)
        report_dict = report.as_dict()

        for key in (
            "positive_rho_a",
            "positive_rho_b",
            "early_b_safe",
            "cmb_close",
            "matter_domination",
            "growth_preserved",
            "passes_minimal_checks",
        ):
            self.assertIsInstance(report_dict[key], bool)

    def test_positive_density_check_detects_invalid_parameter_choice(self) -> None:
        background = integrate_background(
            self.cosmo,
            QFUDSParams(gamma_model="constant", gamma0=0.5),
            n=300,
        )
        growth = integrate_growth(background)
        report = evaluate_viability(background, growth, self.lcdm, self.lcdm_growth)
        self.assertFalse(report.positive_rho_b)


if __name__ == "__main__":
    unittest.main()
