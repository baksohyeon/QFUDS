# Roadmap: QFUDS Fiction IP Studio

## Overview

This roadmap tracks the fiction/IP management work needed to turn the QFUDS
fiction track into a usable studio system. It is operational planning only. It
does not modify QFUDS research status, evidence, validation, or Level 2B gates.

## Phases

**Phase Numbering:**
- Integer phases are planned fiction/IP studio work.
- Decimal phases are urgent insertions if a later correction is needed.

- [ ] **Phase 1: Fiction IP GSD Harness** - Make GSD track the fiction IP
  workflow and the first safe execution phase.

## Phase Details

### Phase 1: Fiction IP GSD Harness
**Goal**: Register the fiction/IP studio workflow in GSD and create a first
plan-only checkpoint for story-system execution.
**Depends on**: Existing fiction IP management workflow and GSD planning bridge.
**Requirements**: [FIC-GSD-01, FIC-GSD-02, FIC-GSD-03]
**Success Criteria** (what must be TRUE):
  1. `.planning` exists in the current worktree and does not point at another
     QFUDS checkout.
  2. GSD can create/list/validate the fiction/IP planning phase.
  3. The phase keeps fiction separate from QFUDS research evidence and status.
  4. The next story-design task has a concrete plan gate before drafting.
**Plans**: 1 plan

Plans:
- [ ] 01-01: Create the fiction/IP GSD phase brief and acceptance checklist.

## Progress

**Execution Order:**
Phases execute in numeric order.

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. Fiction IP GSD Harness | 0/1 | Not started | - |
