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
| [Documentation Folder Routing Workflow](documentation-folder-routing-workflow.md) | Creating, moving, classifying, or cross-linking repository documentation and deciding whether research work should propagate into roadmap, lineage, governance, postmortem, or result docs. |
| [Wiki Maintenance Workflow](wiki-maintenance-workflow.md) | Maintaining `docs/wiki/`, ingesting new wiki records, filing reusable query answers, updating wiki indexes, or linting wiki health. |
| [Research Asset and Product Workflow](research-asset-product-workflow.md) | Research work touches an external paper, PDF, arXiv source bundle, supplementary material, Zenodo/OSF/Dataverse/GitHub asset, figure PDF, table, code repository, downloadable archive, or any product-availability claim. |
| [Research Asset Digitization Workflow](research-asset-digitization-workflow.md) | Converting a cached asset under `docs/wiki/research/assets/` into Markdown: PageIndex structure/full-text extraction, MarkItDown conversion of data releases, and high-resolution figure extraction/mapping. |
| [Research Investigation Result Routing Workflow](research-investigation-result-routing-workflow.md) | A research investigation creates, changes, judges, or routes an asset-level product and needs the correct split between `assets/`, `plans/`, `conclusions/`, and indexes. |

## Required Routing

For data/literature research, apply
[Research Asset and Product Workflow](research-asset-product-workflow.md) before
any product-availability, product-missing, extraction-completeness, or
coverage-completeness claim.

For wiki maintenance, apply
[Wiki Maintenance Workflow](wiki-maintenance-workflow.md) before changing
`docs/wiki/index.md` or the wiki directory structure.

For documentation placement and propagation decisions, apply
[Documentation Folder Routing Workflow](documentation-folder-routing-workflow.md)
before moving docs across `docs/`, `docs/wiki/`, or `.agent/workflows/`.

For any extraction or digitization that creates an asset-level product, apply
[Research Investigation Result Routing Workflow](research-investigation-result-routing-workflow.md)
so the matching investigation conclusion records the result and blocker state.

If multiple workflows apply, follow all of them. If workflows appear to conflict,
use the more conservative rule and record the conflict in the audit or
postmortem.
