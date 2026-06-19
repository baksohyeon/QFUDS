# Fiction GSD Phase Brief

## Phase

- Phase name:
- GSD mode: `plan | execute | verify | migration`
- Applicable workflow: `.agent/workflows/fiction-ip-management-workflow.md`
- Authoring baseline date: `YYYY-MM-DD`

## Objective

What concrete fiction/IP work should this phase finish?

## Reader Support

- English craft terms used:
- Korean-friendly explanations added:
- Bare `TBD` placeholders allowed? `yes | no`

## IP Classification

- Universe/IP:
- Continuity status:
- Work id:
- Work format: `series | novel | short | anthology | webtoon | elseworld`
- Target folder:
- Time baseline notes:

## Scope

Allowed outputs:

- 

Forbidden outputs:

- Research evidence or roadmap status changes.
- Draft prose without a work README.
- Canon changes without continuity classification.
- External-source claims without Research Asset and Product Workflow state.
- Undocumented renaming of scientific or technical terms.
- Scene or work package without a narrative-frame decision.

## Tone Rules

- Do not repeat the full evidence disclaimer; state only local boundary
  exceptions or workflow state.
- Keep reference prose clean and direct.
- Explain `ancient`, `modern`, `post-COVID`, `pre-AGI`, and `future` relative
  to the authoring baseline date.
- Do not write private user context into docs or story text unless explicitly
  authorized.

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
