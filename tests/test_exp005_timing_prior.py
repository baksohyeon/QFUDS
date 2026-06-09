from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from qfuds import run_exp005_timing_prior_audit


class Exp005TimingPriorTests(unittest.TestCase):
    def test_exp005_suite_writes_timing_prior_outputs(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            outdir = Path(tmp)
            summary = run_exp005_timing_prior_audit(outdir=outdir, n_background=220)

            summary_path = outdir / "exp005_timing_prior_summary.json"
            self.assertTrue(summary_path.exists())
            written = json.loads(summary_path.read_text(encoding="utf-8"))

            self.assertEqual(summary["experiment_id"], "exp_005")
            self.assertEqual(written["scope"], "phenomenological IV/IDE timing-prior analysis only")
            self.assertTrue((outdir / "exp005_timing_family_comparison.csv").exists())
            self.assertTrue((outdir / "exp005_timing_fingerprint.csv").exists())
            self.assertTrue((outdir / "exp005_timing_prior_criteria.csv").exists())
            self.assertTrue((outdir / "figures" / "exp005_timing_family_shapes.png").exists())
            self.assertTrue((outdir / "figures" / "exp005_timing_family_shapes.svg").exists())
            self.assertTrue((outdir / "figures" / "exp005_timing_family_errors.png").exists())
            self.assertTrue((outdir / "figures" / "exp005_timing_family_errors.svg").exists())

    def test_exp005_keeps_physical_claims_false(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            summary = run_exp005_timing_prior_audit(outdir=Path(tmp), n_background=220)

            self.assertFalse(summary["decision"]["physical_claim_supported"])
            self.assertFalse(summary["decision"]["roadmap_status_change"])
            self.assertIn(
                summary["decision"]["verdict"],
                {
                    "redundant_as_unique_shape_but_useful_as_interpretable_prior",
                    "potentially_useful_compression_target",
                    "not_supported_as_timing_prior",
                },
            )

    def test_exp005_compares_required_timing_families(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            summary = run_exp005_timing_prior_audit(outdir=Path(tmp), n_background=220)

            families = {row["family_id"] for row in summary["family_comparison"]}
            self.assertTrue(
                {
                    "constant",
                    "powerlaw",
                    "logistic_transition",
                    "logistic_derivative",
                    "tomographic_3_bins",
                    "tomographic_5_bins",
                    "piecewise_linear_8_knots",
                }.issubset(families)
            )


if __name__ == "__main__":
    unittest.main()
