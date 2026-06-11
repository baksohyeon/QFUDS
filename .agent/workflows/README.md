# QFUDS Agent Workflows

This directory is the operational workflow SSOT for QFUDS agents.

Before any repeatable research, data, literature, asset, documentation, or
postmortem procedure, agents must check this index and follow every applicable
workflow. Do not rely on chat history or tool memory as the workflow authority.

These workflows are process-only. They do not change roadmap status, open Level
2B, or turn literature overlap into QFUDS support.

`docs/` stores project records and cached assets. Workflow rules belong here. If
an operational rule is duplicated in `docs/`, treat this workflow directory as
the authority and reduce the `docs/` copy to a link or descriptive cache index.

## Workflow Index

| Workflow | Use when |
| --- | --- |
| [Wiki Maintenance Workflow](wiki-maintenance-workflow.md) | Maintaining `docs/wiki/`, ingesting new wiki records, filing reusable query answers, updating wiki indexes, or linting wiki health. |
| [Research Asset and Product Workflow](research-asset-product-workflow.md) | Research work touches an external paper, PDF, arXiv source bundle, supplementary material, Zenodo/OSF/Dataverse/GitHub asset, figure PDF, table, code repository, downloadable archive, or any product-availability claim. |

## Required Routing

For data/literature research, apply
[Research Asset and Product Workflow](research-asset-product-workflow.md) before
any product-availability, product-missing, extraction-completeness, or
coverage-completeness claim.

For wiki maintenance, apply
[Wiki Maintenance Workflow](wiki-maintenance-workflow.md) before changing
`docs/wiki/index.md` or the wiki directory structure.

If multiple workflows apply, follow all of them. If workflows appear to conflict,
use the more conservative rule and record the conflict in the audit or
postmortem.
