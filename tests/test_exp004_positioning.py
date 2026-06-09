from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from qfuds import run_exp004_suite


class Exp004PositioningTests(unittest.TestCase):
    def test_exp004_suite_writes_positioning_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            outdir = Path(tmp)
            summary = run_exp004_suite(outdir=outdir, n_background=180)

            summary_path = outdir / "exp004_positioning_summary.json"
            self.assertTrue(summary_path.exists())
            written = json.loads(summary_path.read_text(encoding="utf-8"))

            self.assertEqual(summary["experiment_id"], "exp_004")
            self.assertEqual(written["classification"]["primary_outcome"], "exact_interacting_vacuum_instance")
            self.assertTrue((outdir / "exp004_baseline_comparison.csv").exists())
            self.assertTrue((outdir / "exp004_background_equivalence.csv").exists())
            self.assertTrue((outdir / "exp004_transfer_reconstruction.csv").exists())
            self.assertTrue((outdir / "exp004_closure_frame_mapping.csv").exists())
            self.assertTrue((outdir / "exp004_reduction_limits.csv").exists())
            self.assertTrue((outdir / "exp004_R1_background_growth.csv").exists())
            self.assertTrue((outdir / "exp004_R1_p1_perturbations.csv").exists())
            self.assertTrue((outdir / "exp004_R6_effective_w_reconstruction.csv").exists())

    def test_r2_is_exact_mapping_and_r3_is_analytic_subset(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            summary = run_exp004_suite(outdir=Path(tmp), n_background=180)

            rows = {row["run_id"]: row for row in summary["baseline_comparison"]}
            self.assertEqual(rows["R2"]["classification"], "exact_equivalence")
            self.assertEqual(rows["R3"]["classification"], "generic_IDE_subset_mapping")
            self.assertEqual(rows["R3"]["status"], "analytic_subset_mapping")


if __name__ == "__main__":
    unittest.main()
