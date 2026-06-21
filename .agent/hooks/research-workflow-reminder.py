#!/usr/bin/env python3
"""Emit lightweight workflow reminders for research and fiction-IP prompts."""

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

FICTION_TRIGGER_RE = re.compile(
    r"(?ix)"
    r"\bfiction\b|"
    r"\bnovel\b|"
    r"\bshort\b|"
    r"\bsaga\b|"
    r"\bwebtoon\b|"
    r"\buniverse\b|"
    r"\bmultiverse\b|"
    r"\bcanon\b|"
    r"\bcontinuity\b|"
    r"\belseworld\b|"
    r"\bbible\b|"
    r"\bworldbuilding\b|"
    r"소설|픽션|세계관|멀티버스|단편|장편|웹툰|정사|비정사|설정|캐릭터|원고"
)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        payload = {}

    text = json.dumps(payload, ensure_ascii=False)
    research_hit = TRIGGER_RE.search(text)
    fiction_hit = FICTION_TRIGGER_RE.search(text)
    if not research_hit and not fiction_hit:
        return 0

    reminders = []
    if research_hit:
        reminders.append(
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
    if fiction_hit:
        reminders.append(
            "[QFUDS fiction IP workflow reminder]\n"
            "Before creating or moving fiction, read "
            ".agent/workflows/fiction-ip-management-workflow.md. Classify the "
            "work as studio, catalog, universe/IP, continuity, work, bible, "
            "story_design, draft, revision, release, or archive. Every work "
            "folder needs a README with universe/IP, canon status, inherited "
            "rules, local overrides, and fiction/provenance boundary. Fiction "
            "premises are not QFUDS evidence."
        )

    additional_context = "\n\n".join(reminders)

    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": additional_context,
        },
    }, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
