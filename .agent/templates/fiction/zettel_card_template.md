# Zettel Card

## Metadata

```yaml
---
doc_id: <unique_doc_id>
title: <H1 title>
doc_type: reference
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - <source_doc_id>
next_gate: review source refs and link into the relevant zettel map before using in story design
last_updated: YYYY-MM-DD
---
```

## Body

````markdown
# <H1 title>

```text
fiction/provenance only
research evidence: no
canon action: none
```

## Statement

One atomic claim, rule, tension, or open question.

## Source Refs

- [source title](relative/path.md#heading): short note on what was extracted.

## Context

Explain only the minimum needed to use the note without reopening every source.

## Links

- [[related zettel title]]
- [related repo doc](relative/path.md)

## Open Questions

- Unknowns that remain unknown. Do not fill with invention.

## Use Guard

This card does not canonize new material. If it changes canon, route the change
through the domain authority document, story design, or chronicler pass.
````

## Rules

- Keep one card to one claim.
- Preserve source meaning. Do not upgrade candidate material to canon.
- Use validator-allowed `doc_type` values only; `note` is not allowed under `docs/`.
- The `title` field must exactly match the first H1.
- Use Markdown links for repo paths.
