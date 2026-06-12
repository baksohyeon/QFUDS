# QFUDS Engineering Prompts

This directory archives reusable design and engineering prompts used to build and
govern this repository. They are process artifacts, not authority. They do not
change roadmap status, open Level 2B, or count as QFUDS evidence.

Most prompts are written in English on purpose. For the same meaning, English
costs fewer LLM tokens than Korean, so prompts stay cheap and leave more room in
context. The methodology writeup is in
[docs/wiki/lineage/006_agentic_research_system_ko.md](../../docs/wiki/lineage/006_agentic_research_system_ko.md).

## Index

| Prompt | Purpose |
| --- | --- |
| [korean-english-workplace-translator.md](korean-english-workplace-translator.md) | Turn messy Korean into practical workplace English, with Korean study notes underneath. Used to draft the other English prompts. |
| [repository-architect-ssot.md](repository-architect-ssot.md) | One-shot architect prompt that consolidated project status into a single SSOT (the roadmap) and added the `research_consistency.py` drift gate. |

The phase-by-phase Source-X audit prompts (plan generation, execution, and the
"do not promote Level 2B / do not invent citations / distinguish cache gap from
evidence gap" guardrails) are not archived here verbatim. Their outputs live under
[docs/wiki/research/investigations/source_x/](../../docs/wiki/research/investigations/source_x/).
