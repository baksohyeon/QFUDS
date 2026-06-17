---
doc_id: wiki_governance_005_agent_workflow_enforcement_design
title: Agent Workflow Enforcement Design
doc_type: gate
stage: reference
status: completed
evidence_role: audit
depends_on:
  - wiki_governance_index
  - qfuds_agent_workflows
next_gate: keep agent_workflow_guard.py in pre-commit before external research commits
last_updated: 2026-06-17
---

# Agent Workflow Enforcement Design

## Context

The failure mode is procedural, not scientific: an agent can perform web or
literature research and then forget to apply the repository workflow before
making a product-availability, cache, extraction, or coverage claim.

Prompt instructions alone are insufficient because Codex, Claude Code, and
other agent hosts use different runtime hook systems. The repository therefore
needs one common enforcement layer that is independent of the agent host.

The authoritative workflow remains
[Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md).
This governance record does not replace it. It defines how agents are forced to
surface that workflow in repository changes.

## Decision

Use a three-layer enforcement system.

| Layer | Mechanism | Scope | Enforcement strength |
| --- | --- | --- | --- |
| Repository policy | [AGENTS.md](../../../AGENTS.md) and [CLAUDE.md](../../../CLAUDE.md) require workflow application before external research claims. | Codex, Claude Code, and any future agent reading repository entry points. | Human-readable rule. |
| Runtime reminder | `.agent/hooks/research-workflow-reminder.py`, with Claude and Codex wrappers, injects a short reminder when the prompt looks like research, literature, source, asset, NASA/LAMBDA, BAO, or cache work. | Host sessions where hooks are locally registered. | Soft guard; prevents common omission before work starts. |
| Commit gate | `scripts/agent_workflow_guard.py --staged`, wired into `scripts/git-hooks/pre-commit` and `make preflight`. | Staged Markdown under `docs/`. | Hard guard; blocks commits that make external-research or product claims without workflow evidence. |

The hard guard checks staged Markdown for external research signals such as
URLs, arXiv, DOI, NASA/LAMBDA, BAO, DESI/eBOSS, PDF, source bundles,
downloadable assets, figures, tables, page-family resources, or
product-availability language.

When a staged document contains those signals, it must also contain both:

- the workflow marker or link:
  [Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md)
  or
  `Research Asset and Product Workflow`;
- a state token from the workflow state ladder, such as `hit_not_cached`,
  `asset_available_not_downloaded`, `asset_cached`,
  `inspected_no_numerical_product`, `no_asset_found`, or `inaccessible`.

This makes a missing workflow application visible at commit time without trying
to infer whether the scientific interpretation is correct.

## Options Considered

| Option | Result | Reason |
| --- | --- | --- |
| Prompt rule only | Rejected | It depends on agent memory and does not fail closed. |
| Claude/Codex hooks only | Rejected as sole mechanism | Hook registration is host-specific and may be cached or absent in a session. |
| Pre-commit gate only | Accepted but incomplete | It blocks bad commits but catches the problem after work has already started. |
| Hybrid reminder plus pre-commit gate | Chosen | The reminder reduces omissions early, while the repository gate provides agent-independent enforcement. |

## Required Behavior

Before any agent writes a research document that touches an external paper,
PDF, arXiv source, supplement, NASA/LAMBDA page family, BAO/DESI/eBOSS data
source, Zenodo/OSF/Dataverse/GitHub asset, figure, table, code repository,
stable website, or product-availability claim, the agent must:

1. read [QFUDS Agent Workflows](../../../.agent/workflows/README.md);
2. apply
   [Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md);
3. record the workflow name or link in the resulting document;
4. record the most specific workflow state token;
5. avoid QFUDS support, validation, or Level 2B-opening language unless the
   roadmap and evidence chain independently authorize it.

NASA/LAMBDA and BAO caches remain baseline constraint sources. They are not
QFUDS evidence by themselves.

## Failure Conditions

The commit must fail when a staged Markdown document makes an external research
or product-availability claim but omits the workflow marker or omits a state
token.

The commit must also fail when an absence claim such as "no product found",
"not extractable", "literature checked", or "coverage complete" is present
without the workflow state ladder.

The gate does not certify correctness. It only confirms that the workflow state
was made explicit enough for review.

## Consequences

This design deliberately creates friction. A research document cannot casually
say that a product is missing, a source was checked, a page family was cached,
or an asset is unavailable without recording the workflow state.

The runtime hook cannot be treated as sufficient enforcement. Codex and Claude
Code may require local hook registration and fresh sessions after hook changes.
The tracked wrappers exist so both hosts can share the same reminder logic, but
the repository-level commit gate remains the durable enforcement point.

## Action Items

- Keep `scripts/agent_workflow_guard.py --staged` wired into
  `scripts/git-hooks/pre-commit`.
- Keep `make preflight` running the same guard so staged research documents can
  be audited before commit.
- When adding a new workflow state or accepted marker, update
  `scripts/agent_workflow_guard.py` and the workflow SSOT together.
- If a future agent host is added, create a thin wrapper that calls
  `.agent/hooks/research-workflow-reminder.py`; do not fork the reminder logic.
