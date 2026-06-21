# QFUDS Agent Wiki

This directory is the agent-facing operational wiki for this repository.

Use it for rules that future AI agents must execute: workflow routing, asset
handling, extraction-state classification, guardrails, and repeatable procedure.
Do not rely on `docs/` as the operational authority for agent behavior.

`docs/` stores project knowledge, research records, evidence, and cached assets.
`.agent/` stores how agents must work with those records.

## Authority

1. [AGENTS.md](../AGENTS.md) - project constitution and agent behavior rules.
2. [.agent/workflows/](workflows/README.md) - operational workflow SSOTs.
3. [docs/05_next_steps/000_roadmap.md](../docs/05_next_steps/000_roadmap.md) -
   project status SSOT.
4. [docs/](../docs/) - project knowledge, evidence, research records, and
   cached assets.

If a workflow rule appears both in `.agent/` and `docs/`, the `.agent/` rule is
the operational authority and the `docs/` copy should be reduced to a link or
cache description.

## Agent Workflow Index

- [QFUDS Agent Workflows](workflows/README.md)
- [Documentation Folder Routing Workflow](workflows/documentation-folder-routing-workflow.md)
- [Wiki Maintenance Workflow](workflows/wiki-maintenance-workflow.md)
- [Research Asset and Product Workflow](workflows/research-asset-product-workflow.md)
- [Fiction IP Management Workflow](workflows/fiction-ip-management-workflow.md)
- [Agentic Fiction Production Workflow](workflows/agentic-fiction-production-workflow.md)
- [Fiction Templates](templates/fiction/README.md)

## Routing Rule

Before making any research, literature, data-product, asset, extraction,
coverage, fiction-IP, or postmortem claim, read the relevant workflow under
[workflows/](workflows/README.md).
