# Fiction GSD Phase Brief

## Phase

- Phase name:
- GSD mode: `plan | execute | verify | migration`
- Applicable workflow: `.agent/workflows/fiction-ip-management-workflow.md`
- Authoring baseline date: `YYYY-MM-DD`

## Objective

What concrete fiction/IP work should this phase finish?

## Reader Support

- Unfamiliar terms introduced:
- Target-reader support:
- Blocking placeholders:

## IP Classification

- Universe/IP:
- Continuity status:
- Work id:
- Work format: `series | novel | novella | short | anthology | serial | other`
- Target folder:
- Time baseline notes:

## Scope

Allowed outputs:

- 

Forbidden outputs:

- Research evidence or roadmap status changes.
- Draft prose without a work README.
- Canon changes without continuity classification.
- External-source claims without Fiction Source Intake Workflow state.
- Undocumented renaming of scientific or technical terms.
- Scene or work package without a narrative-frame decision.

## Work-Local Style Rules

- Do not repeat the full evidence disclaimer; state only local boundary
  exceptions or workflow state.
- Draft language and register:
- Voice and form constraints:
- Explain time labels relative to the work's chronology when ambiguity matters.
- Do not write private user context into docs or story text unless explicitly
  authorized.

## Planning Brevity

- Do not repeat the same boundary claim through `truths`, `artifacts`,
  `key_links`, task text, verification, and summary.
- Use `truths` for facts, `artifacts` for files, and `key_links` only for
  non-obvious dependencies.
- Keep summaries short. Use one `Boundary` line unless a local exception needs
  more detail.
- For external tooling issues or maintainer comments, prefer an
  `Issue | Impact | Fix` table over long defensive prose.

## Technical Grounding

- Preserve scientific and technical terms by default.
- If a term is renamed into a fictional, legal, religious, social, or poetic
  alias, record the rationale and the technical meaning that must remain clear.

## Narrative Frame

- Who speaks:
- Who sees / focalizer:
- Telling time:
- Narrative form:
- Implied audience:
- Narrator motive:
- Knowledge limits:
- Distortion risk:

## Required Reads

- `.agent/workflows/fiction-ip-management-workflow.md`
- `.agent/workflows/agentic-fiction-production-workflow.md`
- Relevant universe README:
- Relevant work README:
- Relevant world/design/draft docs:

## Acceptance Criteria

- 

## Verification

Run before commit:

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/check_markdown_link_targets.py creative_harness .agent .agents fiction tools/saga-fiction-studio
python3 scripts/agent_workflow_guard.py --staged
python3 scripts/fiction_gate.py --staged
sh scripts/git-hooks/pre-commit
```

## Handoff

- Commit boundary:
- Next phase:
- User confirmation needed:
