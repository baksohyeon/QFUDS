from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

import numpy as np

from qfuds import CosmologyParams, QFUDSParams, integrate_background
from qfuds.perturbations import (
    PerturbationClosure,
    integrate_phenomenological_perturbations,
    run_exp003_suite,
)


class Exp003PerturbationTests(unittest.TestCase):
    def setUp(self) -> None:
        self.cosmo = CosmologyParams()
        self.qfuds = QFUDSParams(
            gamma_model="information_production",
            gamma0=0.02,
            collapse_a=0.35,
            collapse_nu=5.0,
        )
        self.background = integrate_background(self.cosmo, self.qfuds, n=240)

    def test_level_2a_closure_returns_required_variables(self) -> None:
        result = integrate_phenomenological_perturbations(
            self.background,
            closure=PerturbationClosure(variant="P2"),
            k_h_mpc_values=(1.0e-3,),
        )

        self.assertEqual(result.metadata["gauge"], "conformal_newtonian")
        self.assertEqual(result.metadata["transfer_frame"], "phase_A_comoving")
        self.assertEqual(result.metadata["deltaQ_rule"], "deltaQ = Q delta_A")

        for key in (
            "delta_A",
            "theta_A",
            "delta_B",
            "theta_B",
            "Phi",
            "Q",
            "deltaQ",
            "curvature_proxy",
            "conservation_residual",
        ):
            self.assertIn(key, result.modes[1.0e-3])
            self.assertEqual(len(result.modes[1.0e-3][key]), len(self.background["a"]))

        np.testing.assert_allclose(
            result.modes[1.0e-3]["deltaQ"],
            result.modes[1.0e-3]["Q"] * result.modes[1.0e-3]["delta_A"],
        )

    def test_exp003_suite_writes_summary_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            outdir = Path(tmp)
            summary = run_exp003_suite(outdir=outdir, n_background=180)

            summary_path = outdir / "exp003_phenomenological_perturbation_summary.json"
            diagnostics_path = outdir / "exp003_stability_diagnostics.csv"
            self.assertTrue(summary_path.exists())
            self.assertTrue(diagnostics_path.exists())
            written = json.loads(summary_path.read_text(encoding="utf-8"))

            self.assertEqual(written["experiment_id"], "exp_003")
            self.assertEqual(summary["experiment_id"], "exp_003")
            self.assertGreaterEqual(len(written["runs"]), 4)
            self.assertTrue((outdir / "exp003_R0_P1_gamma0.csv").exists())
            self.assertTrue((outdir / "exp003_R1_P2_information_production_gamma0.02.csv").exists())
            self.assertTrue((outdir / "figures" / "exp003_stability_summary.png").exists())
            self.assertTrue((outdir / "figures" / "exp003_stability_summary.svg").exists())
            self.assertTrue((outdir / "figures" / "exp003_retained_mode_growth.png").exists())
            self.assertTrue((outdir / "figures" / "exp003_retained_mode_growth.svg").exists())

    def test_regularized_phase_b_closure_records_instability_flags(self) -> None:
        result = integrate_phenomenological_perturbations(
            self.background,
            closure=PerturbationClosure(variant="P2"),
            k_h_mpc_values=(1.0e-4, 1.0e-3, 1.0e-2, 1.0e-1),
        )

        unstable_modes = result.diagnostics["unstable_modes"]
        self.assertIsInstance(unstable_modes, dict)
        self.assertTrue(any(unstable_modes.values()))
        self.assertTrue(result.diagnostics["any_unstable"])


if __name__ == "__main__":
    unittest.main()
