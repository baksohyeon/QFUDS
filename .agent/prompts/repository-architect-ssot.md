# Repository Architect: Single Source of Truth Consolidation

One-shot prompt given to Claude Code to fix documentation drift. It does not edit
physics or experiments. It collapses status into a single SSOT (the roadmap),
turns the other files into thin references, and adds a `research_consistency.py`
gate so the one-way authority chain is enforced by code, not by memory.

Authority chain it produces: `CLAUDE.md -> AGENTS.md -> docs/05_next_steps/000_roadmap.md -> docs/00_project/decision_log.md -> docs/03_experiments + docs/04_results`.

## Prompt

````text
ROLE

Act as a repository architect, documentation governance engineer, and scientific reproducibility maintainer.

Do not modify QFUDS physics.
Do not create new experiments.
Do not change scientific conclusions.

Your task is to simplify authority, reduce documentation drift, and enforce repository consistency.

CONTEXT

Recent audits showed:
The repository reached Verdict A after documentation refactors.
However, README.md, PROJECT.md, and AGENTS.md previously drifted away from the roadmap.
The root cause was duplicated sources of truth.

DESIGN GOAL

Establish a strict documentation authority hierarchy.
There must be exactly one source of truth for project status.
All other files must reference it.

REQUIRED AUTHORITY HIERARCHY

Level 1 (SSOT): docs/05_next_steps/000_roadmap.md
  Current project status. Current level. Current active branch. Current blockers.

Level 2: docs/00_project/decision_log.md
  Why decisions were made.

Level 3: docs/03_experiments/ and docs/04_results/
  Evidence.

Level 4: AGENTS.md
  Project constitution. Must not maintain independent project status. Must reference roadmap.

Level 5: CLAUDE.md
  Claude-specific behavior only. Must reference AGENTS.md and roadmap. Must not maintain independent project state.

Level 6: README.md and PROJECT.md
  Human-facing entry points. Must not duplicate roadmap status. Must reference roadmap.

TASK 1

Refactor AGENTS.md.
- AGENTS.md defines process, not status.
- Remove duplicated roadmap state.
- Add explicit section "Project Status Authority":
    Current project state lives in: docs/05_next_steps/000_roadmap.md
    Do not duplicate status elsewhere.

TASK 2

Refactor CLAUDE.md into a thin wrapper. Example structure:
    Project Constitution: See AGENTS.md
    Project Status: See docs/05_next_steps/000_roadmap.md
    Research Decisions: See docs/00_project/decision_log.md
Claude must not maintain independent project status.

TASK 3

Refactor README.md and PROJECT.md.
Remove duplicated status tables. Replace with references:
    Current Status: See roadmap.
    Research History: See decision_log.
    Experiment Evidence: See docs/03_experiments and docs/04_results.

TASK 4

Implement repository consistency enforcement.
Review scripts/validate_docs.py and add a new layer scripts/research_consistency.py.
Checks:
1. Roadmap claims have evidence.
2. Completed experiment levels have: experiment doc, result doc, decision log entry.
3. AGENTS.md does not maintain independent roadmap status.
4. CLAUDE.md does not maintain independent roadmap status.
5. README.md and PROJECT.md do not contradict roadmap.
6. Orphan experiment/result documents are detected.

TASK 5 (optional hook)

If supported by repository tooling, add `make research-audit` or `make preflight`
which runs validate_docs.py and research_consistency.py before major experiment milestones.

OUTPUT

Produce:
1. Documentation Authority Diagram
2. Files Modified
3. Consistency Rules Implemented
4. Hook / Audit Commands Added
5. Remaining Drift Risks

Do not redesign the repository.
Reduce authority duplication.
Make roadmap.md the only project-status source of truth.
````
