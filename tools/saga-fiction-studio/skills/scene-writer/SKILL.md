---
name: scene-writer
description: >
  Draft or rewrite a SAGA scene, chapter, or episode with the reader-onboarding
  harness and Korean-primary sequence. Use when writing new prose or rewriting a
  scene. Triggers: "장면 써줘", "이 챕터 초고", "이 장면 다시 써", "write this scene",
  "draft the chapter", "rewrite this beat", "make this scene less expository".
  Leads with person-under-pressure before concept, attaches every load-bearing
  technical concept to a visible cost, and drafts Korean-first.
user-invocable: true
---
# Scene Writer
Draft prose that hooks before it explains. This skill executes the `writer` mode of
the production order; it does not canonize.
SSOT: `.agent/workflows/agentic-fiction-production-workflow.md`,
`docs/wiki/fiction/00_studio/010_reader_onboarding_harness_ko.md`,
`docs/wiki/fiction/00_studio/009_korean_fiction_prose_naturalness_harness_ko.md`,
and `.agent/templates/fiction/chapter_intent_card_template.md` +
`style_packet_template.md`.
## Before drafting
1. Create or update a Chapter Intent Card (chapter_intent_card_template): who wants
   what now; the immediate threat; the forced choice; each option's cost; the
   dramatic question planted/triggered/paid off; what must be shown, hidden, or
   forbidden; what pressure hands off next.
2. Build/load a Style Packet (style_packet_template): Korean-primary prose,
   technical terms with plain-language handles, distinct character voice, and the
   ban on decorative grandiosity, AI-tell, translationese, and meta-hook slogans
   (`엔진:`, `핵심은 A가 아니라 B`, `사건의 주어는 X`).
3. Read the relevant canon (delegate to `canon-guardian` if the scene asserts new
   facts).
## Reader onboarding gate (per load-bearing concept)
```
accurate technical explanation -> simple analogy -> visible loss / choice pressure
```
Technical explanation is allowed but must attach fast to a deadline, button, loss,
cost, system warning, audit note, seal protocol, court exhibit, or fieldmark.
Deliver exposition as diegesis (a character reads a screen, warning, feed, form) —
not author-to-reader tutorial. Avoid childish analogies and contrived declaratives.
First-scene priority: in an opening/hook scene, retention beats explanation. Make
the reader feel the danger (someone is already losing, now) before teaching the
mechanism. The §톤 가드 table in 010 is mandatory for onboarding scenes.
## Drafting sequence
Korean-primary by default: `Korean primary draft -> English Anglophone adaptation
-> shared continuity check`. The Korean draft must read as natural Korean fiction,
not translationese; the English is a same-story counterpart, not a literal
translation. Do not produce a translated logline or foreign noun-stack intermediate.
## After drafting
Add a compact `Harness Applied` block (craft link, narrative frame, goal/obstacle/
turn/cost, KO/EN sibling-text gate, external-source boundary). Then hand off to
`continuity-pass`. Do not run `humanize`-style polish until structure, continuity,
and technical grounding pass.
