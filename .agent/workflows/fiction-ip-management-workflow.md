# Fiction IP Management Workflow

Use this workflow whenever an agent creates, moves, classifies, or extends
fiction material under the repository-root [fiction/](../../fiction/README.md)
vault.

This workflow is process-only. It does not change research evidence or roadmap
status.

Workflow index: [QFUDS Agent Workflows](README.md).

## Core Rule

Manage fiction like an IP studio, not like loose one-off documents.

## Tone And Baseline Rule

Keep fiction-system documents clean and direct.

Do not repeat the full evidence disclaimer in every document. The harness already
defines the boundary. In individual documents, use a short boundary only when it
adds local information, such as an external-source state token or a specific
scope exception.

Avoid grandiose summary prose, decorative metaphors, and repeated manifesto
language in reference documents. Prefer:

- concrete roles over mood labels;
- short definitions over slogans;
- scene-use rules over abstract praise;
- tables/checklists when they reduce ambiguity.

Every new fiction reference, work README, bible, or scene plan must record an
authoring baseline date. Use the date when the document starts, not a floating
"now." When using terms like `ancient`, `modern`, `post-COVID`,
`pre-AGI`, or `future`, explain them relative to that baseline.

The authoring baseline is not automatically story canon. For alternate-history,
far-future, or fully invented worlds, separate:

- author-side baseline: the real-world writing context;
- in-world chronology: calendar, era names, year zero, story year, and internal
  historical labels.

Fully invented worlds should define in-world era IDs instead of forcing
real-world labels such as `post-COVID`.

Author-context may guide clarity and audience assumptions, but do not write
private user identity, location, nationality, job, or personal context into the
story or docs unless the user explicitly asks for it.

## Technical Grounding Rule

Treat scientific and technical terms as load-bearing concepts.

Do not replace terms such as `hash`, `KDF`, `key`, `salt`, `collision`,
`entropy`, `Hawking radiation`, `Page curve`, `island`, `AGI`, or `QFUDS`
with social, legal, religious, or poetic aliases unless the document records a
reason. The default is to preserve the technical term and explain it cleanly.

A fictional alias is allowed only when it represents a story-world institution,
ritual, legal category, propaganda term, translation convention, or character
misunderstanding. It must not hide the underlying technical mechanism.

When a setting changes a technical term, record:

- original technical term;
- preserved term or fictional alias;
- reason for the alias;
- what technical meaning could be lost or distorted;
- where the accurate explanation remains available;
- scene purpose.

If there is no reason, keep the technical term.

## Narrative Frame Rule

Do not reduce narration to only `first person` or `third person`.

Every work bible or substantial scene plan must define the narrative frame:

- who speaks: narrator, editor, archivist, court recorder, memoirist, historian,
  machine, chorus, or anonymous voice;
- who sees: focal character, witness, external camera, institution, archive, or
  rotating focalizers;
- when the telling happens relative to the events;
- what document or performance form carries the story: chronicle, memoir,
  essay, trial record, field report, archive note, letter, transcript,
  recovered file, oral history, direct scene, or mixed form;
- who the implied audience is;
- why the story is being told now;
- what the narrator can know;
- what the narrator may distort, omit, or misunderstand.

For frame narratives, also record how the outer frame changes the meaning of the
inner story.

## Craft Harness Rule

Before creating or revising a work bible, story design, prose draft, or release
candidate, apply
[Creative Writing Craft Harness](../../creative_harness/craft/004_creative_writing_craft_harness_ko.md).

This adds Korean-readable explanations for English craft terms and checks
premise, character, conflict, scene purpose, point of view, dialogue,
worldbuilding, theme, pacing, and revision.

If the user asks for a university, writing-program, workshop, literary-craft, or
formal creative-writing benchmark, also apply
[University Creative Writing Reference Matrix](../../creative_harness/craft/005_university_creative_writing_reference_matrix_ko.md).

## Agentic Production Rule

For active long-form fiction work, apply
[Agentic Fiction Production Workflow](agentic-fiction-production-workflow.md)
after classification and before drafting or revising.

That workflow does not decide canon or routing. It records execution state:
production board, chapter intent card, review wave, chronicler pass, style
packet, and truth-state ledger.

Use it when work touches:

- a chapter, episode, or major scene;
- a multi-step writing sprint;
- prose revision after critique;
- reader-sim or retention feedback;
- continuity recovery after drafting;
- final polish where `humanize` could otherwise hide structural problems.

## Bilingual Draft Sequence Rule

For active SAGA prose, the default writing sequence is Korean-primary:

```text
Korean primary draft -> English Anglophone adaptation -> shared continuity check
```

The Korean version is the first reader-facing draft and must read as natural
Korean fiction, not translationese. The English version is a same-story
counterpart written for Anglophone rhythm, idiom, and genre expectations, not a
literal translation. Existing English-first drafts may remain as provenance or
source counterparts, but new active prose should follow the Korean-primary
sequence unless the user explicitly asks otherwise.

Shared continuity checks must keep plot events, field marks, character
decisions, technical terms, and fiction/research boundaries aligned across both
language versions.

Do not cite web references as loose "materials consulted." If a source changes a
workflow, template, checklist, or fiction-system document, the changed document
must record the source URL, allowed claim, blocked claim, and workflow state.
If that record is missing, treat the source as unused.

Before writing or moving fiction, classify the idea by these layers:

```text
studio rule -> catalog entry -> universe/IP -> continuity branch -> work -> bible/design/draft/release
```

Do not decide by topic alone. Decide by ownership:

- `studio`: how agents write, review, verify, and commit fiction.
- `catalog`: what exists, what is active, reading order, status board.
- `universe/IP`: shared fictional world, science-fiction premise, institutions,
  timeline, recurring motifs.
- `continuity`: canon, soft-canon, elseworld, prototype, retired, anthology
  ordering, multiverse policy.
- `work`: a specific series, novel, short story, webtoon-like run, anthology,
  or elseworld branch.
- `workroom`: work-local operating specs, harness notes, approval gates, and
  repeatable review rules that are narrower than global studio policy.
- `bible`: work-local reference sheet for continuity, cast, point of view,
  tone, local rules, and canon constraints.
- `story_design`: outline, arcs, beat sheet, scene list, reveal order.
- `drafts`: prose drafts, language counterparts, and scene tests.
- `revisions`: line-edit plans, continuity-fix passes, and release-prep
  revision controls.
- `release`: cleaned publication/export candidate if one exists.

## Recommended Target Shape

Use this target shape for new fiction work. It reflects the repository-root
fiction vault adopted 2026-07-10; the earlier per-work
studio/catalog/workroom/bible/story-design/revisions/release scaffold under
`docs/wiki/fiction/` is Git history only (`git show bbbcb970:<old-path>`).

```text
fiction/
  inbox/
  knowledge/
  research/
  worlds/
    <universe-id>/
      README.md
      continuity/
      world/
      series-bible/
  projects/
    <work-id>/
      README.md
      drafts/
```

Operational workflow/template/skill authority for fiction stays outside the
vault: `.agent/workflows/`, `.agent/templates/fiction/`,
`.agents/skills/fiction-production/`, and `tools/`. Human craft/method
references stay in `creative_harness/` (`creative_harness/craft/`,
`creative_harness/methods/`).

Within a project, local operating notes, work bible, and story-design/reveal
material live as sections in `README.md`; only prose drafts get their own
`drafts/` subfolder. A shared universe bible lives once in
`worlds/<universe-id>/series-bible/` rather than being duplicated per work.

## Classification Checklist

Before creating a fiction document, answer:

1. Is this a studio rule, catalog entry, universe/IP record, continuity record,
   work record, workroom note, bible note, story design note, prose draft,
   revision, or release candidate?
2. Which universe/IP owns it?
3. Is it canon, soft-canon, elseworld, prototype, retired, or unclassified?
4. Does it inherit shared world rules, or does it introduce a local override?
5. If it introduces a local override, is the override allowed by the continuity
   policy?
6. Is this for a series, novel, short, anthology, webtoon-like run, or
   elseworld branch?
7. Does it need a work README before any bible/design/draft is added?
8. Does it touch external references, papers, PDFs, MCP outputs, assets, or
   source/product claims?
9. Does it accidentally phrase a fiction premise as a research/status claim?
10. What is the authoring baseline date?
11. Is the work same-universe, alternate-history, far-future, fully invented,
    or unknown?
12. What is the in-world chronology if it is not simple same-universe fiction?
13. Are time words such as `ancient`, `current`, `post-COVID`, or `future`
    anchored to the authoring baseline or to an in-world era ID?
14. What is the narrative frame: who speaks, who sees, when, in what form, and
    for which implied audience?
15. Has the craft harness been applied for work bible, story design, prose, or
    release work?
16. Does this task cite university, writing-program, workshop, or craft-web
    references?
17. If yes, has the university reference matrix recorded source state and claim
    boundaries?
18. Are English craft terms and abbreviations explained for Korean readers?
19. Does this introduce or rename a scientific or technical concept?
20. If yes, what is the recorded rationale and what technical meaning is
    preserved?
21. What validation and commit boundary will close this step?

## Work README Contract

Every work folder must have a README before drafts are added.

The README must state:

- universe/IP;
- format: series, novel, short, anthology, webtoon-like run, or elseworld;
- canon status;
- authoring baseline date;
- inherited continuity/world/science-boundary documents;
- local overrides;
- workroom/bible/design/draft/revision/release paths;
- local boundary exceptions, if any.

Use [.agent/templates/fiction/work_readme_template.md](../templates/fiction/work_readme_template.md).

## Workroom Rule

Record local operating procedure for a single work — agent harness notes,
approval gates, sub-agent role definitions, local workflow exceptions, or
repeatable review rules for that work only — as a section in the work's
`README.md` under `fiction/projects/<work-id>/`. The dedicated `00_workroom/`
subfolder was part of the closed SAGA production track (Git history only,
`git show bbbcb970:<path>`); new work does not recreate it.

Do not put universe-wide studio rules in a work's README. Global fiction/IP
rules belong in `.agent/workflows/`; there is no separate human-readable
mirror inside the fiction vault.

## Harness Applied Block

Every active prose draft, release-facing revision plan, or release candidate
must include a compact `Harness Applied` block near the boundary/intent section.
The block records:

- craft harness link;
- narrative frame;
- scene or revision goal/obstacle/turn/cost;
- Korean-primary / English Anglophone sibling-text gate;
- external-source or research-asset workflow boundary.

Legacy drafts may omit this block when preserved unchanged for provenance, but
any new revision of those drafts must add it before the draft is promoted.

## Bible Rule

`bible` is a continuity-reference term, not a folder every work needs.

Shared continuity for a universe lives in
`fiction/worlds/<universe-id>/series-bible/` (the qfuds-verse universe keeps
its bible there). A work with no shared-bible need records its own continuity
reference as a "Work Bible" section in the work's `README.md` under
`fiction/projects/<work-id>/`, covering:

- cast and relationships;
- point of view and voice;
- setting subset used by the work;
- local timeline;
- local motifs;
- local science-fiction limits;
- what the work inherits from the universe;
- what the work overrides.

Do not use `bible` for:

- prose drafts;
- loose brainstorms;
- whole-repo fiction system rules;
- research evidence;
- external-source cache records.

The per-work `00_bible/` subfolder was part of the closed SAGA production
track (Git history only, `git show bbbcb970:<path>`).

## Universe Inheritance Rule

Do not make every work a new universe by default.

Default behavior:

```text
new idea -> existing universe/IP -> work-local README -> inherited rules + local overrides
```

Create a new universe only when the idea changes the shared premise enough that
inheritance would be misleading. Examples:

- different physics premise;
- incompatible timeline;
- incompatible institutions or history;
- different genre contract so strong that shared canon would confuse readers;
- explicit multiverse branch that needs its own continuity policy.

If a work borrows only some motifs from a universe, classify it as `elseworld`
or create a new universe. Do not write "loosely QFUDS-ish" without a continuity
classification.

## GSD Planning Integration

GSD planning may manage execution phases, but it must not replace this
classification workflow.

Use this split:

```text
Fiction IP Management Workflow = where the idea belongs and what it is
GSD planning = how to execute a bounded phase of work
```

Use GSD planning for:

- migrating an existing fiction folder into the IP structure;
- creating a catalog or universe scaffold;
- building a new series/short/anthology work package;
- planning a multi-step writing sprint;
- coordinating review, revision, verification, commit, and handoff.

Do not use GSD planning for:

- deciding canon by momentum;
- skipping the universe/IP and continuity classification;
- adding drafts before a work README exists;
- treating a phase plan as fiction canon;
- turning fiction premises into research/status claims.

Every fiction-related GSD phase must state:

- applicable workflow: this workflow;
- universe/IP or `none yet`;
- continuity status;
- target work folder;
- allowed outputs;
- forbidden outputs;
- acceptance criteria;
- verification commands.

Use [.agent/templates/fiction/gsd_phase_brief_template.md](../templates/fiction/gsd_phase_brief_template.md)
when drafting a GSD phase for fiction work.

## Reader Retention Test (Release Gate)

Before any fiction work (short or series) is promoted to release, run a reader
retention test. This is a formal gate, not optional polish: prose can pass
AI-tell and naturalness audits and still lose readers (this happened on the
QFUDS SAGA first arc).

- Spawn several reader-persona subagents with distinct profiles (예: 중학생,
  고등학생, 대학생~직장인 일반, 웹소설 속독, 까다로운 순문학, 기술 문외한,
  안티-AI 냉소가, Ted Chiang식 정밀·절제, SF 애호가). 다양성이 핵심이다.
- 각 페르소나는 release 원고를 읽고, 흥미가 진짜로 끊기는 지점에서 멈춘다.
  보고: 이탈 지점(장면·줄)과 트리거, 편별 몰입 점수, 다음 편 진행 여부,
  끝까지 끌고 간 훅.
- 집계해 공통 이탈 지점을 고치고, 페르소나가 목표 리텐션(사실상 끝까지)에
  도달할 때까지 반복한다. 통과 전에는 release 금지.
- 실행 결과와 판정을 작품 README(`fiction/projects/<work-id>/README.md`)의
  해당 섹션에 기록한다. 과거 SAGA `30_revisions/`, `00_workroom/` 경로는
  closed shelf로 Git 이력에서만 확인한다(`git show bbbcb970:<path>`).

### Required Retention Gate Artifact

A retention gate without a written artifact is invalid. Do not record
"9-persona pass", "all completed", or "release gate passed" unless the work has
a revision document based on
[reader_retention_gate_template.md](../templates/fiction/reader_retention_gate_template.md).
The run artifact must use `doc_type: gate`. A protocol or planning document may
use `doc_type: guide`, but it cannot itself count as the completed retention
gate.

The artifact must include:

- gate id, source draft files, baseline commit/date, per-file blob hash, and
  target release shelf;
- persona roster and why each persona exists;
- reading units pinned as `baseline commit:path#Lx-Ly`;
- one result sheet per persona, including exact baseline stop source ref, stop
  trigger, immersion score, clarity score, next-unit intent, strongest hook, and
  weakest moment;
- cross-persona evidence matrix;
- issue ledger with severity, evidence personas, baseline source ref, proposed fix,
  owner mode, and status;
- revision mapping from issue id to changed files and fix commit/blob;
- pass/fail decision using only these states:

```text
not_run | invalid_no_artifact | ran_failed | ran_passed_with_risks | ran_passed
```

Release promotion is blocked when the gate state is `not_run`,
`invalid_no_artifact`, or `ran_failed`.

Pass requires:

- every persona result sheet exists;
- no release-blocking `S0` issue remains open;
- every repeated `S1` issue is fixed or explicitly deferred with rationale;
- every applied fix links to a revision wave and changed files;
- every feedback item is tied to the reviewed git baseline, not the moving
  current file;
- the production board records the gate id, decision, and residual risks.

Retention gate run artifacts are immutable. If the draft changes after a run,
create a new run document for the new baseline and link the older run through
`depends_on`. Do not overwrite prior persona feedback.

Do not store raw private reasoning or long hidden deliberation. Store concise
reader-facing observations, evidence references, and actionable issue records.

## External Source Boundary

If fiction work touches external paper, web reference, PDF, code repository,
MCP, asset, image, source, extraction, cache, or product-availability claims,
also apply [Research Asset and Product Workflow](research-asset-product-workflow.md).

Every resulting fiction document must record:

- workflow marker/link;
- most specific workflow state token;
- a short local boundary statement for how the source is used.

### External Tool and Code Adoption (fiction only)

Rule relaxed 2026-06-30 (user decision). The earlier "inspiration-only; no
install or prompt/code copy" prohibition is lifted **for fiction work only**.
External AI writing tools, MCP servers, prompts, and code may be adopted or
adapted for fiction, under these conditions:

- check and respect the source license before copying; record the license;
- record source URL, license, allowed claim, blocked claim, and workflow state
  in the changed fiction document (this rule + Research Asset and Product
  Workflow);
- vet MCP servers/tools for security (prompt injection, excess permissions) and
  scope them to the fiction repo/vault before installing;
- adopt on the fiction side only — never copy external material into QFUDS
  research evidence, theory, or results. The research/fiction boundary is not
  lifted;
- prefer adapting external material to this project's structure (shelves,
  Korean-primary, gates) over replacing the governance wholesale.

## Validation

Before commit, run:

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/agent_workflow_guard.py --staged
python3 scripts/fiction_gate.py --staged
make preflight
sh scripts/git-hooks/pre-commit
```

For fiction restructuring, also run a local link/state smoke check over
`fiction/` when practical.
