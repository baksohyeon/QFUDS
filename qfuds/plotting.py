from __future__ import annotations

import os
from pathlib import Path
import tempfile
from typing import Any

os.environ.setdefault("MPLBACKEND", "Agg")
_cache_root = Path(tempfile.gettempdir()) / "qfuds-cache"
_cache_root.mkdir(parents=True, exist_ok=True)
(_cache_root / "matplotlib").mkdir(parents=True, exist_ok=True)
(_cache_root / "fontconfig").mkdir(parents=True, exist_ok=True)
os.environ.setdefault("MPLCONFIGDIR", str(_cache_root / "matplotlib"))
os.environ.setdefault("XDG_CACHE_HOME", str(_cache_root))


def save_figure_pair(fig: Any, stem: Path) -> list[str]:
    """Save one figure as PNG and SVG, returning repo-style output paths."""

    png_path = stem.with_suffix(".png")
    svg_path = stem.with_suffix(".svg")
    png_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(png_path, dpi=160)
    fig.savefig(svg_path)
    if png_path.parent.name == "figures":
        return [f"outputs/figures/{png_path.name}", f"outputs/figures/{svg_path.name}"]
    return [f"outputs/{png_path.name}", f"outputs/{svg_path.name}"]
