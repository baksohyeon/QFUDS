---
name: postmortem
description: Write a junior-friendly incident or postmortem note in Korean with evidence, hypotheses, and decision rationale. Use when the user asks for a postmortem, incident write-up, RCA doc, 사건 정리, 포스트모템, or to document how debugging went.
user-invocable: true
argument-hint: "[optional path or PR #]"
---

## When to use

- After debugging: capture **what broke**, **how you verified**, **what you ruled out**, **why you chose the fix**.
- Audience: **주니어 개발자** — short prerequisite blocks, no inference jumps.
- Default output language: **Korean** prose; keep code paths, log lines, GitHub/CI names, and YAML keys as in the real system (English is fine).

## Before writing

1. Collect from the session (and repo): symptom, environment, PR/issue numbers, commands run, relevant file paths.
2. **Do not invent** PR numbers, job URLs, or log lines. Use placeholders like `PR #___` or `<run-url>` if unknown.
3. **Output path** — 두 옵션:
   - **영구 자료** (디폴트): `docs/wiki/postmortem/NNN-YYYYMMDD-<author>-<slug>.md`
   - **draft staging** (긴 회고 작성 중 보호): `docs/wiki/postmortem/temp/<slug>.md` — 검토 후 영구 위치로 이동
4. **파일명 컨벤션** (영구 위치만):
   - `NNN` — 3 자리 zero-pad sequence. `ls docs/wiki/postmortem/ | grep -oE '^[0-9]{3}' | sort -n | tail -1` 의 다음 번호. (sentinel 도입 시 README claim-pointer 따름)
   - `YYYYMMDD` — 사건 *발생일* (created_at 동일). 8 자리.
   - `<author>` — git author 핸들 (소문자). 다중 작업자 환경에서 추적용.
   - `<slug>` — 영문 kebab-case, 짧고 식별 가능. 한국어 제목은 frontmatter `title` 에 넣고 slug 는 영문.
5. **두 hook 자동 skip** — `docs/wiki/postmortem/temp/*` + `docs/wiki/postmortem/*` 안에서는 emoji / 한국어 슬랭 차단 hook 가 self-skip. 즉 hook 차단 사례를 *메타-인용* 으로 자유롭게 적을 수 있음.

## Required YAML frontmatter

영구 위치 (`docs/wiki/postmortem/`) 의 wiki 표준:

```yaml
---
id: postmortem-NNN-<slug>
seq: <N>
title: "<짧은 한글 제목>"
type: postmortem
date: YYYY-MM-DD
context: <어떤 작업 흐름 중인지 — sprint 이름 / plan 단계 / blog episode / PR # / 브랜치 / 서비스 / 배포 단계 중 적용 가능한 것, 한 줄>
audience: 주니어 개발자
length: 작업 단계별 풀어쓰기
created_at: YYYY-MM-DD
created_by: <author>
updated_at: YYYY-MM-DD
updated_by: <author>
last_verified_at: YYYY-MM-DD
last_verified_by: <author>
audit_log:
  - action: created
    at: YYYY-MM-DD
    by: <author>
    note: "<한 줄 — 어떤 작업 직후 작성됐는지>"
status: active
tags: [postmortem, <도메인 키워드 2~4 개>]
relations:
  - <관련 D-NNN ADR 경로>            # 결정 로그 cross-link
  - <관련 sprint plan / 워크플로우 경로>   # 작업 흐름 cross-link
  - <관련 blog 글 경로>               # 회고 narrative cross-link
code_refs:
  - file: <변경된 코드 경로>
    note: "<무엇 / 왜>"
---
```

draft staging (`docs/wiki/postmortem/temp/`) 은 위 frontmatter 의 *부분 집합* 으로 가능 — 영구 이동 시 보강.

**`relations:` 활용 가이드** — *어떤 작업 하다가 발생했나* 의 cross-link 를 모두 여기에:
- 관련 D-NNN 결정 로그 (`docs/wiki/decisions/D-NNN.md`)
- 관련 sprint plan (`.planning/sprints/<name>/PLAN.md` 또는 `temp/sprints/<name>/PLAN.md`)
- 관련 워크플로우 (`.agent/workflows/<name>.md`)
- 관련 blog 글 (`docs/blog/posts/<YYYY-MM-DD>-*.md`)
- 관련 슬래시 (`.claude/commands/<name>.md`)

`context` 한 줄 + `relations:` 의 cross-link 둘이 합쳐서 *어떤 작업 흐름이 사건의 trigger 였나* 명시.

## Body — section order

1. **사건 한 줄 요약** — cause and effect in one or two sentences.
2. **0. 사전 지식** — only concepts needed to read the rest (small tables or diagrams). Omit if truly obvious.
3. **1. 증상** — what was seen (quoted errors, check names, screenshots described).
4. **2. 첫 의문 + 가설** — table: `가설 | 왜 그럴 수 있는지 | 어떻게 확인할지` with ids `H1`, `H2`, … Order verification **cheapest / highest signal first**.
5. **3. 진단: 실제 상태 확인** — commands run plus **verbatim** output (trim only noise). For each result, state which hypothesis is **supported or rejected** and why.
6. **4. (선택) 추가 확인** — only if needed; same evidence bar.
7. **5. 결론 / 해결** — what was done or recommended; **tradeoffs** if any.
8. **6. 재발 방지 / 운영 메모** — checklist, doc or CI follow-up, or explicit “none — by design.”
9. **7. 타임라인** — short chronological bullets.
10. **부록 (선택, 조건부)** — 본문 흐름을 끊지 않도록 *맨 뒤* 에 모은다. 아래 조건에 해당하면 추가:
    - **부록 X — 디버깅 명령어 모음 (cheat sheet)**: 셸/CLI 명령(리눅스 유틸, `npm`/`jq`/`mise`/`gh`/`docker` 등)으로 진단했다면 **필수**. 본문 진단 섹션에 흩어진 명령을 *목적별로* 한곳에 모아, 주니어가 그대로 복사·응용할 수 있게 한다. 각 명령마다 두 가지를 같이 적는다: (1) *그 명령이 일반적으로 무슨 일을 하는지* (도구/플래그 설명), (2) *이 사건에서 무엇을 보려고 썼고 출력에서 무엇을 읽었는지*. 끝에 "이런 부류의 문제는 보통 이 순서로 푼다" 류의 응용 팁 한 줄.
    - **부록 Y — 도메인 개념 완전 해설**: 사건 이해에 특정 도메인 지식(예: npm 패키징, DNS, OAuth flow, DB 인덱스)이 결정적이었다면, 본문엔 최소만 두고 깊은 해설은 부록으로 분리. 주니어 기준 "왜 이게 함정이 되는가" 까지.

## Writing rules

- **Observation → interpretation → next step.** No gaps in the reasoning chain.
- Prefer **primary sources** (workflow YAML, `gh` output, API responses) over memory.
- State explicitly what was **not** verified.
- **명령어는 본문에선 흐름대로, 부록에선 목적별로 모은다.** 진단 섹션 안에선 추론 순서대로 명령을 보여주되, 같은 명령들을 부록 cheat sheet 에 한 번 더 *재사용 가능한 형태* 로 정리한다 (중복이 아니라 두 독자층 — 사건을 따라 읽는 사람 vs 명령만 빌리러 온 사람 — 을 위한 것).
- **결정마다 근거를 적는다.** 해결 섹션에 "고른 것 / 안 고른 대안 / 근거" 를 표나 줄로 명시 — 주니어가 "왜 A 가 아니라 B" 를 재현할 수 있게.
- No blame; name **systems and interfaces**.
- Define non-obvious acronyms once.

## Output contract

- Deliver **one** Markdown file unless the user asked for more.
- Do not add unrelated refactors or extra documentation files.

## Pairing with other workflows

- If the incident started with `/investigate` or graph-first rules, **keep the same evidence standard** here: commands and outputs win over paraphrase.
