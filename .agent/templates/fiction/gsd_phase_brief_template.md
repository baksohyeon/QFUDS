# Fiction GSD Phase Brief

## Phase

- Phase name:
- GSD mode: `plan | execute | verify | migration`
- Applicable workflow: `.agent/workflows/fiction-ip-management-workflow.md`

## Objective

What concrete fiction/IP work should this phase finish?

## IP Classification

- Universe/IP:
- Continuity status:
- Work id:
- Work format: `series | novel | short | anthology | webtoon | elseworld`
- Target folder:

## Scope

Allowed outputs:

- 

Forbidden outputs:

- QFUDS evidence, support, validation, or Level 2B admission.
- Draft prose without a work README.
- Canon changes without continuity classification.
- External-source claims without Research Asset and Product Workflow state.

## Required Reads

- `.agent/workflows/fiction-ip-management-workflow.md`
- `.agent/workflows/documentation-folder-routing-workflow.md`
- `.agent/workflows/wiki-maintenance-workflow.md`
- Relevant universe README:
- Relevant work README:
- Relevant bible/design/draft docs:

## Acceptance Criteria

- 

## Verification

Run before commit:

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/agent_workflow_guard.py --staged
make preflight
sh scripts/git-hooks/pre-commit
```

## Handoff

- Commit boundary:
- Next phase:
- User confirmation needed:

