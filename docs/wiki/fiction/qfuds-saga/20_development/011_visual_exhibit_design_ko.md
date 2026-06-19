---
doc_id: qfuds_saga_visual_exhibit_design_ko
title: QFUDS SAGA Visual Exhibit Design
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_mara_veyr_prologue_english_revision_ko
  - qfuds_saga_post_agi_civilization_history_bilingual_protocol_ko
  - qfuds_saga_agentic_system_ko
next_gate: user reviews whether visual exhibits should enter the episode draft
last_updated: 2026-06-19
---

# QFUDS SAGA Visual Exhibit Design

## Boundary

This is a fiction-system design note.

It does not introduce new research evidence, QFUDS support, validation,
physical-source derivation, or Level 2B admission. The images below are
existing repository assets reused as fictional archive plates, courtroom
exhibits, or visual metaphors.

External-source handling remains governed by
[Research Asset and Product Workflow](../../../../../.agent/workflows/research-asset-product-workflow.md).

Current workflow state:

```text
asset_cached
inspected_no_numerical_product
```

## Principle

The visual language should not say "this proves QFUDS."

It should say:

```text
This is what a future civilization preserved from an early, failed attempt to
ask the universe the right question.
```

The images work best when treated as damaged plates in a legal archive. They are
not diagrams explaining the world to the reader. They are objects that reveal
what the characters inherited, misunderstood, ritualized, and eventually
outgrew.

## Visual Exhibit Candidates

| Asset | Fiction role | Metaphor use | Placement |
| --- | --- | --- | --- |
| `../../../lineage/assets/004_rough_tanh/fig_double_well_explainer.svg` | Exhibit A: the old two-valley myth | A civilization trying to draw grief as a landscape: one valley clusters, one valley thins into pressure, and the ridge between them becomes theology. | Before a chapter about phase A/B mythology. |
| `../../../lineage/assets/004_rough_tanh/fig_phase.png` | Exhibit B: phase plate | Not a proof, but an old map of desire: humans wanted dark matter and dark energy to be two weather patterns in the same invisible atmosphere. | In a Laur Observatory lecture or court appendix. |
| `../../../lineage/assets/004_rough_tanh/fig_state_variable.png` | Exhibit C: forbidden variable | A diagram that looks like a keyhole. Everyone wants to turn it into `X`; the auditor keeps stamping it `not_derived`. | Near the Mara Veyr evidence wall as a warning plate. |
| `../../../lineage/assets/004_rough_tanh/fig_cp6a_ceiling.png` | Exhibit C-2: ceiling plate | Every knob survives cross-examination. The figure becomes a courtroom reminder that tuning can move a problem without solving it. | In a methods appendix or auditor briefing. |
| `../../../lineage/assets/004_rough_tanh/fig_cp21_xi_criticality.png` | Exhibit D: the 10 Mpc temptation | A ruler that became a superstition. Useful as a measurement, dangerous as a destiny. | In a later cosmic-web chapter, not the Mara prologue. |
| `../../../lineage/assets/004_rough_tanh/fig_cp20_ceiling_derivation.png` | Exhibit D-2: the 10 Mpc wound | Too large for microscopic foam, too small for the horizon. A scale that looks like an answer until the audit asks where it came from. | In a lineage lecture or failed-candidate hearing. |
| `../../../lineage/assets/004_rough_tanh/fig_growth.png` | Exhibit E: growth trace | A pulse line from a patient who may never have been alive. Good for showing how retained `Gamma(a)` stayed useful as a timing handle. | In an IV/IDE bridge scene. |
| `../../../lineage/assets/004_rough_tanh/fig_background.png` | Exhibit F: background plate | The old universe drawn as a ledger: not beautiful enough to be a myth, not rigorous enough to be a verdict. | In an archive-wall montage. |
| `../../../lineage/assets/004_rough_tanh/fig_cp14_kill_test.png` | Exhibit G: kill plate | The visual equivalent of a guillotine kept behind glass. It reminds characters that an elegant curve can still die. | In a Constraint Order scene. |
| `../../../lineage/assets/004_rough_tanh/fig_cp12_fluid_frameworks.png` | Exhibit H: classification plate | A toy model placed in known-theory space instead of crowned as new physics. | In a scene where the auditor refuses novelty language. |

## Recommended First Use

Use `fig_state_variable.png` first.

![EXHIBIT Q-17: forbidden variable plate, fiction/provenance only, not research evidence](../../../lineage/assets/004_rough_tanh/fig_state_variable.png)

Reason:

```text
Mara Veyr's case is about whether a person can be reduced to recoverable state.
QFUDS's old failure is about whether a suggestive scale or curve can be promoted
to a physical state variable.
```

That makes the image thematically useful. It can sit on the courtroom wall as an
old cosmology plate, while the legal case asks the same structural question in
human form:

```text
When does a trace become a thing?
When does a reconstruction become a person?
When does a diagram become a claim?
```

## Caption Style

Captions should sound like archival labels, not textbook explanations.

Prefer PNG for GitHub display reliability. Use SVG when zoom or line crispness is
important; `fig_double_well_explainer.svg` is SVG-only.

Good:

```text
EXHIBIT Q-17
EARLY FOAM-SECTOR STATE-VARIABLE SKETCH
ANNOTATION: BEAUTIFUL, UNDEFINED, NOT ADMITTED
```

Bad:

```text
This proves that QFUDS has two phases and explains dark energy.
```

## Prose Integration Pattern

The image should enter as an object in the room.

```text
On the far wall, behind the restored woman's chair, hung an old cosmology plate.
It showed a curve trying to become a law.

Someone had stamped three words across it in red:

BEAUTIFUL.
UNDEFINED.
NOT ADMITTED.
```

Korean translation:

```text
복원된 여자의 의자 뒤, 먼 벽에는 오래된 우주론 plate가 걸려 있었다.
그것은 법칙이 되고 싶어 하는 곡선을 보여 주었다.

누군가 그 위에 붉은 글씨 세 단어를 찍어 두었다.

BEAUTIFUL.
UNDEFINED.
NOT ADMITTED.
```

## Agent Workflow Note

The SAGA writers' room can use sub-agents as logical roles:

| Role | Visual task |
| --- | --- |
| `worldbuilder` | decide whether the exhibit belongs to court, monastery, observatory, or archive culture |
| `science_auditor` | verify the caption does not turn fiction into evidence |
| `style_editor` | make the image feel like part of the scene rather than a pasted diagram |
| `plot_architect` | decide whether the exhibit foreshadows a later reversal |

If an actual Codex/Claude sub-agent tool is available, the main agent may spawn
these as read-only critique agents or disjoint doc-edit workers. If no such tool
is available, the same roles remain a checklist inside the main agent.

## Decision

Recommended next prose pass:

1. Insert only one visual plate into the Mara Veyr prologue revision.
2. Use `fig_state_variable.png` as a courtroom background object.
3. Do not explain the image in narration.
4. Let the caption do the work.
5. Keep all image use fiction/provenance only.
