---
doc_id: qfuds_saga_revisions_first_second_arc_formal_retention_gate_protocol_ko
title: QFUDS SAGA 1부·2부 정식 reader retention gate protocol
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_revisions_first_second_arc_release_wave_ko
  - qfuds_saga_revisions_reader_feedback_ai_tell_consolidation_ko
  - qfuds_saga_production_board_ko
next_gate: create 012 retention gate run artifact with doc_type gate before any 40_release promotion
last_updated: 2026-06-22
---

# QFUDS SAGA 1부·2부 정식 reader retention gate protocol

## 역할 / 경계

이 문서는 1부 origin([030](../20_drafts/1부/030_origin_arc_sael_korean_primary.md))과
2부 Mara([029](../20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md))를
`40_release/`로 올리기 전에 필요한 **정식 9-persona retention gate 산출물 계약**이다.
이 문서 자체는 실행 결과가 아니라 protocol이다. 실제 실행 결과는 새 run artifact로
남긴다.

Frontmatter 설계:

- 이 문서: `doc_type: guide`, `status: draft`, `evidence_role: provenance`.
  gate를 어떻게 실행할지 정하는 protocol이므로 실행 결과가 아니다.
- 실제 run artifact: `doc_type: gate`, `stage: reference`, `status: in_progress`
  또는 `completed`, `evidence_role: provenance`.
  release 승격을 막거나 허용하는 판정 문서이므로 `guide`가 아니다.

Boundary:

```text
fiction/provenance only
research evidence: no
release promotion: blocked until this artifact is filled
raw private reasoning: do not record
```

## Artifact Rule

Retention feedback은 덮어쓰지 않는다. 실행할 때마다 baseline git commit을 고정하고,
그 baseline에 대한 새 문서를 만든다.

권장 파일명:

```text
012_first_second_arc_retention_gate_run_20260622_c158d31_ko.md
```

초안이 바뀐 뒤 다시 gate를 돌리면 기존 run 문서를 수정하지 않는다. 새 baseline
commit과 blob hash를 잡아 다음 번호의 run 문서를 만든다. 이전 run은 `depends_on`에
걸어 provenance로 남긴다.

## 왜 고쳤나

이전 기록([009](009_first_arc_reader_feedback_and_ai_tell_consolidation_ko.md))은 유용한
진단이었다. 하지만 release gate로 쓰기에는 부족하다. 페르소나별 요약과 개선 계획은
있지만, 정식 gate가 요구해야 할 아래 항목이 한 문서에 잠기지 않았다.

- source draft baseline(commit + file blob hash).
- 페르소나별 stop scene/line.
- 이탈 trigger와 다음 편 진행 의사.
- cross-persona evidence matrix.
- severity가 붙은 issue ledger.
- issue id에서 수정 wave와 changed files로 이어지는 mapping.
- pass/fail 상태값.

따라서 `030/029 정식 9-persona retention gate`는 아직 **통과가 아니라 `not_run`**이다.
앞으로 "전원 완독" 같은 요약은 이 문서의 표가 채워진 뒤에만 쓴다.

## Gate State

```text
gate_id: retention_011_first_second_arc_formal
state: not_run
source_drafts:
  - 20_drafts/1부/030_origin_arc_sael_korean_primary.md
  - 20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md
baseline_commit: c158d3169d6eb6f33af80e26c6cccc8ef1286441
baseline_short: c158d31
baseline_label: docs: polish QFUDS front door
release_target: 40_release/ active manifest, not created
```

Allowed states:

```text
not_run | invalid_no_artifact | ran_failed | ran_passed_with_risks | ran_passed
```

Release promotion is blocked unless the state becomes `ran_passed` or
`ran_passed_with_risks` with explicit accepted residual risks.

## Source Baseline

Feedback은 움직이는 현재 파일이 아니라 아래 baseline ref에 묶는다.

| Source id | Path | Baseline commit | Blob hash |
| --- | --- | --- | --- |
| S030 | `docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/20_drafts/1부/030_origin_arc_sael_korean_primary.md` | `c158d3169d6eb6f33af80e26c6cccc8ef1286441` | `702565433d9c9342b030d1fc6f64dfa6a061c10c` |
| S029 | `docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md` | `c158d3169d6eb6f33af80e26c6cccc8ef1286441` | `c4d40c59c47b0f1b74dcbb71642543487855627d` |

Source ref 형식:

```text
c158d31:<path>#Lx-Ly
```

## Persona Set

| Persona id | Reader profile | What this persona tests | Stop rule |
| --- | --- | --- | --- |
| P1 | 중2 SF 입문 | 기술어 없이도 손실과 선택을 따라가는가 | 첫 실제 혼란 또는 지루함에서 멈춤 |
| P2 | 고2 일반 독자 | 장면 전환과 원인-결과를 따라가는가 | 앞 장면의 결과를 설명 못 하면 멈춤 |
| P3 | 대학생~직장인 일반 | 업무 후 독서 밀도로도 읽히는가 | 인물 목표보다 설정 설명이 커지는 순간 멈춤 |
| P4 | 웹소설 속독 | 다음 화/다음 부 진행 욕구가 생기는가 | 결제/넘김 의사가 사라지는 순간 멈춤 |
| P5 | 까다로운 순문학 | 문장, 리듬, 상투적 결말 문장이 버티는가 | 문장이 작가의 격언으로 들리면 멈춤 |
| P6 | 기술 문외한 | 공개키, 서명, 복원, 사본을 장면 압력으로 이해하는가 | 용어 때문에 장면 비용을 놓치면 멈춤 |
| P7 | 안티-AI 냉소가 | AI식 병렬, 대칭 경구, 설명투가 남았는가 | "AI가 쓴 티"가 누적되는 첫 지점에서 멈춤 |
| P8 | Ted Chiang식 정밀 SF 독자 | 아이디어-윤리-절차가 지적으로 정합한가 | 사고실험이 편의적 장치처럼 보이면 멈춤 |
| P9 | SF 애호가 | 세계관 밀도와 서사 추진력이 같이 살아 있는가 | 설정은 좋은데 장면이 멈추면 멈춤 |

## Reading Units

| Unit id | Source ref | Blob hash | Role in release | Expected hook |
| --- | --- | --- | --- | --- |
| U1 | `c158d31:docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/20_drafts/1부/030_origin_arc_sael_korean_primary.md#L153-L256` | `702565433d9c9342b030d1fc6f64dfa6a061c10c` | 1부 origin hook + Aletheia entry | "나는 보낸 적 없다"와 검증실 십육 도 |
| U2 | `c158d31:docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/20_drafts/1부/030_origin_arc_sael_korean_primary.md#L257-L450` | `702565433d9c9342b030d1fc6f64dfa6a061c10c` | Broken Crown mechanism + first ratification | 공개키 역산, 중지 실패, 한 사람 구하기 |
| U3 | `c158d31:docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/20_drafts/1부/030_origin_arc_sael_korean_primary.md#L451-L653` | `702565433d9c9342b030d1fc6f64dfa6a061c10c` | standard-authoring cost + Mara handoff | 사엘 도장이 선례가 되고 사람 복원 청구로 번짐 |
| U4 | `c158d31:docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md#L126-L1436` | `c4d40c59c47b0f1b74dcbb71642543487855627d` | 2부 Mara entry + court stakes | 복원은 사본인가, 누가 청구하는가 |
| U5 | `c158d31:docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md#L1437-L2245` | `c4d40c59c47b0f1b74dcbb71642543487855627d` | public myth + Identity Flood | 분파 압력, HashDoS, 가장 사람 같은 장면 |
| U6 | `c158d31:docs/wiki/fiction/10_universes/qfuds-verse/20_series/qfuds-saga/20_drafts/2부/029_first_arc_book1_reboot_korean_primary.md#L2246-L3060` | `c4d40c59c47b0f1b74dcbb71642543487855627d` | Hawking Court + protected pending | QFUDS rejected courtroom argument, `who may author loss` |

## Persona Result Sheets

정식 실행 시 모든 칸을 채운다. 이 표가 비어 있으면 gate는 통과할 수 없다.

| Persona | Unit | Completed? | Stop source ref | Stop trigger | Immersion 1-10 | Clarity 1-10 | Next-unit intent | Strongest hook | Weakest moment source ref |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| P1 | U1 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| P1 | U2 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| P1 | U3 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| P1 | U4 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| P1 | U5 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| P1 | U6 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| P2 | U1-U6 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| P3 | U1-U6 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| P4 | U1-U6 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| P5 | U1-U6 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| P6 | U1-U6 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| P7 | U1-U6 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| P8 | U1-U6 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |
| P9 | U1-U6 | TBD | TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Cross-Persona Evidence Matrix

| Unit | Median immersion | Lowest immersion persona | Common stop trigger | Repeated confusion | Strong hook consensus |
| --- | --- | --- | --- | --- | --- |
| U1 | TBD | TBD | TBD | TBD | TBD |
| U2 | TBD | TBD | TBD | TBD | TBD |
| U3 | TBD | TBD | TBD | TBD | TBD |
| U4 | TBD | TBD | TBD | TBD | TBD |
| U5 | TBD | TBD | TBD | TBD | TBD |
| U6 | TBD | TBD | TBD | TBD | TBD |

## Issue Ledger

Severity:

- `S0`: release-blocking dropout or continuity break.
- `S1`: repeated confusion, boredom, or AI-tell across 3+ personas.
- `S2`: local weakness across 1-2 personas.
- `S3`: taste note or optional polish.

| Issue id | Severity | Evidence personas | Source ref | Failure mode | Proposed fix | Owner mode | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| RET-011-001 | TBD | TBD | TBD | TBD | TBD | TBD | open |

## Decision Rule

Pass requires:

- every persona result sheet exists;
- no `S0` issue remains open;
- every `S1` issue is fixed or explicitly deferred with rationale;
- every applied fix links to a revision wave and changed files;
- every feedback item links to a baseline source ref;
- production board records this gate id, decision, and residual risks.

Decision:

```text
not_run
```

## Revision Mapping

| Issue id | Fix wave/doc | Baseline source ref | Changed files | Fix commit/blob | Verification | Residual risk |
| --- | --- | --- | --- | --- | --- | --- |
| TBD | TBD | TBD | TBD | TBD | TBD | TBD |

## Verification

Required after filling or changing this gate:

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/agent_workflow_guard.py --staged
python3 scripts/fiction_gate.py --staged
sh scripts/git-hooks/pre-commit
```
