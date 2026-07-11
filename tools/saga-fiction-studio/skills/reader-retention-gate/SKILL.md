---
name: reader-retention-gate
description: >
  Run the reader-comprehension and retention gate before promoting SAGA fiction to
  release. Use to check whether readers actually keep reading, or before a release.
  Triggers: "독자 이탈 체크", "리텐션 게이트", "이거 끝까지 읽혀?", "reader comprehension pass",
  "retention gate", "will readers drop off", "release gate", "proper-noun overload".
  Checks proper-noun density, proposition overload, exposition-before-stakes, and
  first-scene hook; optionally spawns reader-persona subagents; writes a gate artifact.
user-invocable: true
---
# Reader Retention Gate
A formal release gate, not optional polish. Prose can pass AI-tell and naturalness
audits and still lose readers. A gate without a written artifact is invalid.
SSOT: `.agent/workflows/fiction-ip-management-workflow.md` (Reader Retention Test +
Required Retention Gate Artifact), `agentic-fiction-production-workflow.md` (Reader
Retention Gate Artifact), and
`.agent/templates/fiction/reader_retention_gate_template.md` +
`reader_retention_gate` / `creative_harness/craft/reader_onboarding_harness.md`.
## Fast comprehension scan (always)
Check the draft for: proper-noun overload; proposition/declarative overload;
explanation placed before stakes; weak first-scene hook (mechanism taught before
danger is felt); tutorialized exposition; childish onboarding analogies. Report each
hit with an exact source ref and a concrete fix.
## Full persona gate (before release)
1. Pin reading units as `baseline commit:path#Lx-Ly` with `git rev-parse` blob
   hashes. Feedback ties to the reviewed baseline, not the moving current file.
2. Spawn several distinct reader personas (예: 중학생, 고등학생, 대학생~직장인, 웹소설
   속독, 까다로운 순문학, 기술 문외한, 안티-AI 냉소가, Ted Chiang식 정밀, SF 애호가).
   Diversity is the point.
3. Each persona reads and stops where interest genuinely breaks. Record: exact stop
   ref, stop trigger, immersion + clarity scores, next-unit intent, strongest hook,
   weakest moment.
4. Build the cross-persona evidence matrix and an issue ledger (severity, evidence
   personas, baseline ref, proposed fix, owner mode, status).
5. Write the gate artifact using the template with `doc_type: gate`. Record decision
   as one of: `not_run | invalid_no_artifact | ran_failed | ran_passed_with_risks |
   ran_passed`.
## Gate rule
Release is blocked when state is `not_run`, `invalid_no_artifact`, or `ran_failed`.
Pass requires every persona sheet present, no open release-blocking S0, repeated S1s
fixed or explicitly deferred, and each fix linked to a revision wave. Run artifacts
are immutable — a changed draft gets a NEW run linked via `depends_on`.
