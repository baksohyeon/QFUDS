---
doc_id: qfuds_saga_first_arc_book1_gsd_phase_brief_ko
title: QFUDS SAGA 1부 Book 1 GSD Phase Brief
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_first_arc_book1_outline_reboot_ko
  - qfuds_saga_first_arc_scene_cards_ko
  - qfuds_saga_first_arc_book1_reboot_korean_primary
  - qfuds_saga_series_production_harness_ko
next_gate: reference only; 029 is canonical 2부 Mara asset under 002 §10 and active origin drafting continues in 117
last_updated: 2026-07-06
---

# QFUDS SAGA 1부 Book 1 GSD Phase Brief

## Cascade Drift Status

이 brief는 029를 1부 Book 1로 완성하려던 legacy completion sprint다. [306 §10](../10_story_design/306_saga_arc_map_multiarc_ko.md)
이후 신규 구조에서는 029가 **2부 Mara 자산**으로 이동 예정이고, active 사엘
origin 원고는 [030](../20_drafts/1.5부/030_origin_arc_sael_korean_primary.md)이다(2026-06-30에
1부→1.5부 강등; 새 1부는 「오르페우스」 122).

따라서 이 문서는 physical cascade 전까지 provenance/reference로 보존한다. 지금은
029 Chapter 6를 이어 쓰지 않는다.

## Phase

- Phase name: QFUDS SAGA 1부 Book 1 Korean-primary completion sprint
- GSD mode: `plan` -> chapter-level `execute` -> manuscript `verify` -> release `migration`
- Applicable workflow:
  [Fiction IP Management Workflow](../../../../../../../../.agent/workflows/fiction-ip-management-workflow.md)
- Authoring baseline date: `2026-06-21`

## Objective

1부 Book 1을 단편집이 아니라 장편 SAGA의 첫 권으로 완성한다. active manuscript는
[029](../20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md) 하나다. 307 outline과
108 scene cards를 기준으로 한국어 primary draft를 먼저 완성하고, 내부 gate를 통과한
뒤 영어 Anglophone independent adaptation, shared continuity check, 사용자
pre-release 확인, polish, `40_release/001_` 승격 순서로 진행한다.

## Reader Support

- English craft terms used: GSD, sprint, deep POV, throughline, field mark,
  incluing, retention gate, release candidate.
- Korean-friendly explanations added: 각 용어는 "실제 집필을 막거나 통과시키는
  작업 기준"으로만 쓴다. 용어 자체가 산문 안에 들어가지는 않는다.
- Bare `TBD` placeholders allowed? `no`

## Concrete Reader Onboarding Gate

이 sprint의 기본 독자는 Bitcoin, AI, 세계사, 철학, 물리를 모르는 일반 독자다.
독자가 배경 지식을 가져오기를 기대하지 않는다. 본문이 직접, 쉽게, 구체적으로
설명해야 한다.

Gate rules:

- Abstract-first opening is blocked. A paragraph may not introduce a new world
  idea before it shows a person, object, institution, or consequence.
- Every hard noun must get an immediate plain-language handle:
  `private key = 비밀 서명 열쇠`, `ledger = 모두가 보는 장부`,
  `data center = 전기와 냉각수를 먹는 서버 공장`.
- 2023-2026 modern anchors must be visible before the far-future abstraction:
  democracy/court, US-China AI/chip rivalry, Iran/Hormuz oil chokepoint,
  tech-platform infrastructure, Bitcoin as property/investment/ideology,
  capitalism/globalization as price-and-supply-chain pressure.
- AI must be treated as a political-economic infrastructure regime, not as a
  chatbot or abstract mind: capital concentration, cloud/GPU/data-center control,
  energy/water/environmental pressure, labor reclassification, democratic
  information integrity, freedom/control ideology, and cognitive offloading must
  be available as scene pressure.
- AGI/LLM personhood must be split into capability/autonomy, consciousness or
  moral status, and legal personhood/accountability. Do not collapse these into
  "the AI is a person" or "the AI is only a tool" unless a character is making a
  partial claim inside the story.
- The prose must answer "왜 이게 문제인가" inside the scene, not in a later
  appendix.
- Plain-reader test: after any technical paragraph, a reader should be able
  to say who owns what, who can move what, who is harmed, and what changes next.
- Object-level clarity pass: each chapter must contain at least one concrete
  explanation that a general reader can retell without the technical noun.
  Examples: locked notebook for legal title vs access, returned person vs
  returned toy for consent, old box with a name tag for dead-key authority.
- Future-prophecy realism pass: every far-future institution must feel grown
  from a visible 2020s seed: AI-generated evidence, platform/cloud control,
  data-center power and cooling, chip/export politics, digital-asset property,
  estate access, market pricing of uncertainty.
- Transitional-case rule: do not imply Mara/Noor are the first cases ever.
  Restoration disputes, dead-key claims, and estate-access fights are already
  common in the transition. Mara S-0 is important because continuity, damaged
  consent, spouse claim, Genesis-derived access, and market/state interest
  converge into the first public precedent-grade case.
- Exposition containment gate: world-system explanations must be carried by an
  in-scene carrier such as an Aletheia training screen, evidence context packet,
  court notice, market quote board, witness action, or character decision. A
  pure lecture block fails even if the facts are correct.
- Chronology clarity gate: future-historical framing must be explicitly marked
  as future-historical. Do not imply Sael already lives inside the Continuity
  Court era if the prologue event predates Mara by a long interval.
- Legal-label clarity gate: `S-0` must be disambiguated whenever first used in a
  chapter. Mara is the person, Broken Crown is the exhibit, Station S-0 is a
  hearing area, and S-0 is the public precedent docket/case label.
- First-use institutional anchor: if Last Archive speaks in a scene, add a
  one-line in-scene court function before or immediately after the signal so the
  reader knows why everyone freezes without revealing Vera/VERA.

## IP Classification

- Universe/IP: `qfuds-verse`
- Continuity status: active SAGA draft, canon-candidate until release.
- Work id: `qfuds-saga`
- Work format: `series`
- Target folder:
  `00_workroom/` GSD brief -> `20_drafts/029` Korean primary -> English counterpart
  draft -> `30_revisions/` gates -> `40_release/001_` only after user confirmation.
- Time baseline notes:
  - Author-side baseline: 2026-06-21.
  - In-world era: far-future Continuity Court / Waiting City era.
  - `modern Bitcoin`, `2023-2026 AI`, `post-AGI`, `ancient` must be interpreted
    relative to author-side baseline or in-world era explicitly.

## Scope

Allowed outputs:

- Expand 029 Prologue into SAGA-grade opening.
- Draft Chapter 1-6 inside 029 in Korean-primary order.
- Add local continuity notes as the manuscript grows.
- Create English Anglophone adaptation only after Korean draft stabilizes.
- Create shared continuity check and release package after both language paths exist.
- Prepare user pre-release review package before any active `40_release/001_` promotion.

Forbidden outputs:

- Research evidence or roadmap status changes.
- QFUDS support, validation, prediction, legal advice, cryptographic advice, or
  black-hole physics claim.
- Release promotion without user confirmation.
- English-first active prose.
- Draft prose outside the SAGA work README / 20_drafts shelf.
- Canon changes without continuity classification.
- External-source claims without Research Asset and Product Workflow state.
- Undocumented renaming of scientific or technical terms.
- Private user context in docs or story text.

## Source Boundary

이 brief는 새 외부 source table을 직접 보유하지 않는다. Bitcoin/digital-asset
상속·세무·custodial account·fiduciary access, AI infrastructure, AGI, LLM
autonomy/personhood/model-welfare 논쟁에 관한 현실 앵커와 workflow state는
[106 reader accessibility and real-world anchors](../../../10_world/106_reader_accessibility_and_real_world_anchors_ko.md)가
SSOT다. 이 brief와 029는 그 교정만 상속한다.

## SAGA-Grade Draft Standard

This sprint rejects "thin prologue" output. A chapter is not considered drafted
unless it has enough scale, conflict, and world pressure to function as a SAGA
installment.

| Unit | Hard floor | Target range | Must carry |
| --- | --- | --- | --- |
| Prologue | 6,000 Korean characters | 8,000-12,000 Korean characters | Aletheia/Karvath/Arc, Bitcoin/ECDSA collapse, restoration seed, Mara hook |
| Chapter 1 | 6,000 Korean characters | 8,000-15,000 Korean characters | Liora, Mara, Elias, Pell, Court procedure, `RECOVERABLE / NOT CLAIMABLE` |
| Chapter 2-6 | 6,000 Korean characters each | 8,000-15,000 Korean characters each | each chapter's field mark, causal damage, next hook |
| Book 1 Korean primary | no short-story bundle | 60,000-90,000 Korean characters as working target | one Mara-centered Book 1 arc |

Character count is a floor, not a quality metric. A scene can still fail if it is
long but static, expository, generic, or detached from the 108 scene cards.

Reader-comprehension correction:

- The Prologue must not imply that Bitcoin lacked inheritance law or estate
  handling. Digital assets can be property, custodial accounts can have decedent
  claim procedures, and fiduciary-access legal frameworks exist.
- The dramatic fault line is **legal title / inheritance claim** versus
  **technical private-key signing control**.
- First-page reader test: a non-technical reader should be able to summarize the
  premise as "the asset was legally inherited, but nobody could sign with the
  lost key until Aletheia's system reversed the signing barrier."
- If the chapter reads like fossil archaeology or legal discovery of Bitcoin,
  revise before continuing.
- If the chapter reads like abstract SF philosophy before it explains the modern
  systems being extrapolated, revise before continuing.
- Applied correction in 029: Prologue-Chapter 2 now includes an explicit
  "what this world is" ladder: restoration law asks continuity, claim, and
  consent; Aletheia arose because editable evidence made verification expensive;
  Bitcoin split legal title from private-key signing control; Broken Crown turns
  that split into restoration; Mara and Noor show why access, memory, and names
  still cannot create consent. The pass adds object-level analogies and anchors
  the far future in 2020s AI/evidence/infrastructure realities. It also clarifies
  that S-0 is a public precedent-grade convergence case, not the first dispute
  of its kind. Follow-up revision moved broad explanations into scene carriers,
  clarified the Sael/Mara chronology, separated S-0 docket/station/person/exhibit
  labels, added the key-recovery -> record-recovery -> restoration bridge, and
  anchored Last Archive before its first direct intervention.

## Tone Rules

- Natural Korean fiction first. English terms remain only when they are proper
  nouns, field marks, technical terms, or deliberate institutional artifacts.
- Direct technical explanation is allowed. Do not hide physics or cryptography
  behind ornamental metaphor.
- No grandiose filler. If a paragraph does not move plot, pressure, character,
  technical grounding, or atmosphere, cut it.
- No generic "engine" when the local object is Aletheia Systems, the Arc, or
  Convergence Engine.
- No abstract AI mysticism. Show racks, chips, cooling, export licenses, labor
  displacement, evidence dependence, or institutional incentives before giving an
  AI-philosophy sentence.
- The reader should feel a large world pressing on a specific person, not read a
  wiki lecture.
- Scene first, summary second. A market board, court notice, training packet,
  physical object, or character choice should appear before any paragraph that
  generalizes the setting.

## Technical Grounding

Preserve these terms directly when the scene needs them:

- Bitcoin, Satoshi, Genesis block, SHA-256, ECDSA, public key, private key,
  signature, ledger, custody route.
- Aletheia Systems, Adrian Karvath, the Arc, Convergence Engine, Last Archive.
- recoverability, irreversibility, continuity threshold, consent file, field mark.
- Hawking radiation, Page curve, island, unitarity, entropy, QFUDS forbidden lattice.
- AGI levels, autonomy, model welfare, AI consciousness indicators, electronic
  personhood, human authorship/inventorship boundary.

Aliases are allowed only as in-world legal or institutional language. If a chapter
adds an alias, record the original technical term and the meaning that must not
be lost.

## Narrative Frame

- Who speaks: restrained third-person narrator.
- Who sees / focalizer: Prologue Sael; Chapter 1 Liora; later chapters per 108
  scene cards.
- Telling time: direct scene, close to the event.
- Narrative form: direct prose with occasional field-mark/code-block artifacts.
- Implied audience: general Korean SF reader, no assumed Bitcoin or physics expertise.
- Narrator motive: make institutions, technologies, and grief collide through
  concrete scenes.
- Knowledge limits: no Vera/VERA core reveal in Book 1 opening; Last Archive stays
  misreadable as awe/fault until later.
- Distortion risk: lecture, slogan, and prophecy-like narration can make the SAGA
  feel smaller. Scene pressure must carry meaning before summary does.

## Required Reads

- [Fiction IP Management Workflow](../../../../../../../../.agent/workflows/fiction-ip-management-workflow.md)
- [Documentation Folder Routing Workflow](../../../../../../../../.agent/workflows/documentation-folder-routing-workflow.md)
- [Wiki Maintenance Workflow](../../../../../../../../.agent/workflows/wiki-maintenance-workflow.md)
- [QFUDS SAGA README](../README.md)
- [307 Book 1 outline](../10_story_design/307_first_arc_book1_outline_reboot_ko.md)
- [308 scene cards](../10_story_design/308_first_arc_scene_cards_ko.md)
- [030 active origin manuscript](../20_drafts/1.5부/030_origin_arc_sael_korean_primary.md) (1.5부 사엘 origin; 1부→1.5부 강등 2026-06-30)
- [029 Mara reboot asset](../20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md) (canonical 2부 after 306 §10)
- [Reader accessibility and real-world anchors](../../../10_world/106_reader_accessibility_and_real_world_anchors_ko.md)
- [Last Archive origin and reversal causality](../../../10_world/107_last_archive_origin_and_reversal_causality_ko.md)
- [Bitcoin stature / ideology / deep-time](../../../10_world/110_bitcoin_stature_ideology_deeptime_ko.md)
- [Character ensemble voices](../00_bible/205_character_ensemble_voices_relationships_ko.md)

## Acceptance Criteria

- 029 Prologue reaches at least 6,000 Korean characters and functions as a full
  SAGA opening, not a short setup note.
- Chapter 1-6 are drafted in 029 with each chapter meeting the hard floor and
  108 scene-card requirements.
- Korean primary draft comes before any new English counterpart.
- No active release before user pre-release review and confirmation.
- User pre-release package includes read order, known risks, unresolved choices,
  and concrete polish candidates.
- Release promotion creates `40_release/001_` only after Korean primary, English
  adaptation, shared continuity check, release-facing revision gate, and user
  confirmation.

## Verification

Run before commit:

```bash
python3 scripts/fiction_gate.py
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/agent_workflow_guard.py --staged
git diff --check
make preflight
sh scripts/git-hooks/pre-commit
```

## Handoff

- Commit boundary:
  - Phase brief + Prologue expansion can land together.
  - After that, each chapter draft should land in its own commit or tight pair of
    chapter + continuity notes.
- Next phase: hold this sprint until physical cascade. Active origin drafting
  continues in 117 B2.
- User confirmation needed:
  - Not needed for each drafting sprint unless a new canon decision appears.
  - Required before `40_release/001_` active release promotion.
