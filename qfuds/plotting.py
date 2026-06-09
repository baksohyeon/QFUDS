from __future__ import annotations

from pathlib import Path
from typing import Any


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
