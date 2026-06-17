#!/usr/bin/env python3
"""Emit a lightweight workflow reminder for research-like agent prompts."""

from __future__ import annotations

import json
import re
import sys


TRIGGER_RE = re.compile(
    r"(?ix)"
    r"\bresearch\b|"
    r"\bliterature\b|"
    r"\bweb\b|"
    r"\bbrowse\b|"
    r"\bsearch\b|"
    r"\bpaper\b|"
    r"\barxiv\b|"
    r"\bpdf\b|"
    r"\bsource\b|"
    r"\basset\b|"
    r"\bcache\b|"
    r"\bdigitiz(?:e|ation)\b|"
    r"\bnasa\b|"
    r"\blambda\b|"
    r"\bbao\b|"
    r"\bdesi\b|"
    r"\beboss\b|"
    r"\bzenodo\b|"
    r"\bgithub\b|"
    r"리서치|조사|검색|논문|자료|출처|캐시|워크플로우"
)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        payload = {}

    text = json.dumps(payload, ensure_ascii=False)
    if not TRIGGER_RE.search(text):
        return 0

    additional_context = (
        "[QFUDS research workflow reminder]\n"
        "Before any external research, literature, data-product, asset, "
        "extraction, coverage, or product-availability claim, read "
        ".agent/workflows/README.md and apply "
        ".agent/workflows/research-asset-product-workflow.md. Record the "
        "workflow name/link and the most specific state token "
        "(for example hit_not_cached, asset_cached, no_asset_found, or "
        "inaccessible) in any resulting research document. NASA/LAMBDA, BAO, "
        "paper, PDF, source, and page-family caches are baseline sources only; "
        "do not phrase them as QFUDS support."
    )

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": additional_context,
        },
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
