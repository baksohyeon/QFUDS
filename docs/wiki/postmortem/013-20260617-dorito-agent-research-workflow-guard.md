---
doc_id: postmortem-013-agent-research-workflow-guard
id: postmortem-013-agent-research-workflow-guard
seq: 13
title: "에이전트 연구 workflow 강제 게이트 회고"
doc_type: postmortem
type: postmortem
stage: reference
status: reference
wiki_status: active
evidence_role: provenance
depends_on:
  - roadmap
  - qfuds_lineage_agentic_research_system_ko
  - wiki_governance_005_agent_workflow_enforcement_design
next_gate: provenance only; workflow guard 유지; NASA/LAMBDA와 BAO cache는 baseline constraint source로만 사용
date: 2026-06-17
context: QFUDS observer-mode 연구에서 NASA/LAMBDA page-family cache와 BAO baseline 논의 중 Research Asset and Product Workflow 적용 누락을 재발 방지 gate로 전환한 작업
audience: 주니어 개발자
length: 작업 단계별 풀어쓰기
created_at: 2026-06-17
created_by: dorito
updated_at: 2026-06-17
updated_by: dorito
last_updated: 2026-06-17
last_verified_at: 2026-06-17
last_verified_by: dorito
audit_log:
  - action: created
    at: 2026-06-17
    by: dorito
    note: "agent research workflow guard 구현과 로컬 pre-commit 설치를 검증한 직후 작성"
tags: [postmortem, agent-system, workflow, research-cache, pre-commit]
relations:
  - docs/wiki/lineage/006_agentic_research_system_ko.md
  - docs/wiki/governance/005_agent_workflow_enforcement_design.md
  - .agent/workflows/README.md
  - .agent/workflows/research-asset-product-workflow.md
  - .agent/workflows/documentation-folder-routing-workflow.md
  - .agent/workflows/wiki-maintenance-workflow.md
code_refs:
  - file: scripts/agent_workflow_guard.py
    note: "staged Markdown에서 외부자료 claim과 workflow state token 누락을 차단"
  - file: scripts/git-hooks/pre-commit
    note: "agent_workflow_guard.py를 pre-commit 순서에 연결"
  - file: Makefile
    note: "make agent-workflow-guard와 make preflight에 workflow guard 연결"
  - file: .agent/hooks/research-workflow-reminder.py
    note: "research-like prompt에서 workflow 적용을 떠올리게 하는 공통 reminder"
  - file: .claude/hooks/remind-research-workflows.sh
    note: "Claude Code용 reminder wrapper"
  - file: .codex/hooks/remind-research-workflows.sh
    note: "Codex용 reminder wrapper"
  - file: AGENTS.md
    note: "외부자료 claim 전에 workflow marker와 state token을 기록해야 한다는 repo 규칙 추가"
  - file: CLAUDE.md
    note: "Claude Code entrypoint에도 같은 research workflow 의무 추가"
---

# 에이전트 연구 workflow 강제 게이트 회고

## 사건 한 줄 요약

NASA/LAMBDA page-family와 BAO baseline constraint를 다루는 조사 흐름에서, 에이전트가
[Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md)를
먼저 다시 확인하지 않고 웹 리서치 판단을 진행했다. 원인은 개별 에이전트 지시와 기억에
의존한 soft rule이었고, 해결은 Codex와 Claude Code 모두가 공유하는 reminder와 git
pre-commit 기반 hard gate를 추가하는 것이었다.

이 회고는 QFUDS 물리 상태를 바꾸지 않는다. NASA/LAMBDA와 BAO cache는 baseline constraint
source일 뿐이고, QFUDS support나 Level 2B admission 근거가 아니다.

## 0. 사전 지식

| 용어 | 뜻 | 이 사건에서 중요한 이유 |
| --- | --- | --- |
| workflow SSOT | 반복 작업 절차의 기준 문서 | QFUDS에서는 [.agent/workflows](../../../.agent/workflows/)가 절차 기준이다. |
| state token | workflow state ladder의 상태 값 | `hit_not_cached`, `asset_cached`, `no_asset_found`처럼 자산 확인 수준을 남긴다. |
| hard gate | 실패하면 커밋이 중단되는 검사 | 사람이 잊어도 repository가 막는다. |
| soft hook | prompt나 tool input에 reminder를 주는 장치 | host 등록 여부와 세션 캐시에 영향을 받으므로 단독 강제력은 약하다. |
| page-family | 같은 URL 패턴과 메뉴에서 이어지는 sibling page 묶음 | NASA/LAMBDA처럼 `{parameters}.html` 패턴이 보이면 pasted URL 하나만 캐시하면 부족하다. |

## 1. 증상

사용자는 NASA/LAMBDA graphic-history URL 패턴과 메뉴 화면을 근거로, 링크를 추론할 수 있고
자료 cache가 중요한 기반 정보라고 지적했다. 핵심 증상은 다음이었다.

- 외부 stable website와 page-family resource를 다루면서 workflow 적용 여부가 먼저 드러나지 않았다.
- "자료가 있다/없다", "cache해야 한다", "baseline constraint로 써야 한다" 같은 claim이
  workflow state 없이 진행될 위험이 있었다.
- Codex와 Claude Code가 각각 다른 prompt/hook 환경을 쓰므로, 한쪽에만 reminder를 넣으면
  같은 누락이 반복될 수 있었다.

직접적인 사용자 확인 문장은 다음과 같은 성격이었다.

```text
웹 리서칭할 때 워크플로우 확실히 했어??
```

이 질문이 맞았다. 당시 누락은 과학 결론 오류가 아니라 운영 절차 오류였다.

## 2. 첫 의문 + 가설

| 가설 | 왜 그럴 수 있는지 | 어떻게 확인할지 |
| --- | --- | --- |
| H1. workflow가 repo에 있지만 agent가 실행 전에 강제로 읽지 않았다. | [AGENTS.md](../../../AGENTS.md)는 workflow 확인을 요구하지만, prompt-time에서 사람이 놓치면 바로 막는 장치가 약했다. | [.agent/workflows/README.md](../../../.agent/workflows/README.md)와 [Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md)를 다시 읽고, 실제 강제 장치가 있는지 확인한다. |
| H2. Claude Code와 Codex hook 등록 방식이 달라 한쪽 reminder만으로는 부족하다. | host별 hook 등록은 다르고, 실행 중인 session은 hook 변경을 즉시 반영하지 않을 수 있다. | `.claude/hooks`, `.codex/hooks`, 사용자 홈의 hook 설정 흔적을 확인한다. |
| H3. commit-time gate가 없어서 workflow marker 누락이 커밋까지 갈 수 있다. | 기존 pre-commit은 docs validation과 research consistency를 보지만, 외부자료 claim의 workflow state token을 직접 보지는 않았다. | [scripts/git-hooks/pre-commit](../../../scripts/git-hooks/pre-commit)과 [Makefile](../../../Makefile)을 읽는다. |
| H4. 너무 넓은 guard를 만들면 governance/index 문서의 일반 설명까지 막는 false positive가 생긴다. | `asset`, `research`, `figure` 같은 단어는 연구 claim이 아니라 폴더 역할 설명에도 나온다. | staged guard를 실제 변경분에 돌려 false positive를 확인하고 범위를 조정한다. |

## 3. 진단: 실제 상태 확인

### 3.1 workflow와 entrypoint 상태

먼저 workflow index와 asset workflow를 확인했다.

```text
rtk sed -n '1,220p' .agent/workflows/README.md
rtk sed -n '1,260p' .agent/workflows/research-asset-product-workflow.md
```

확인 결과, workflow 자체는 이미 충분히 강했다. 특히 stable reference website와 templated
URL pattern도 적용 범위에 들어 있었다. 따라서 H1의 "workflow가 없었다"는 부분은 기각하고,
"workflow를 실행 전에 강제하는 장치가 약했다"는 쪽을 채택했다.

### 3.2 기존 pre-commit 범위

기존 pre-commit은 다음 계열을 돌렸다.

```text
python3 scripts/update_frontmatter_last_updated.py --staged
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/preflight_exp004.py
git diff --check
```

이 검사는 문서 frontmatter, status authority, exp_003 이후 기록 일관성에는 강했다. 하지만
외부자료 claim이 workflow marker와 state token을 포함하는지는 별도로 검사하지 않았다.
따라서 H3은 지지됐다.

### 3.3 첫 guard 실행과 false positive

초기 guard를 staged 변경분에 적용했을 때 false positive가 나왔다.

```text
rtk python3 scripts/agent_workflow_guard.py --staged
```

출력:

```text
agent workflow guard: failed
- docs/wiki/governance/README.md
  - missing Research Asset and Product Workflow marker/link for external-research or product-availability claims
  - missing workflow state token such as asset_cached, hit_not_cached, no_asset_found, or inaccessible

Apply .agent/workflows/research-asset-product-workflow.md and record the workflow state before committing.
```

이 결과는 H4를 지지했다. [docs/wiki/governance/README.md](../governance/README.md)는 외부자료 claim을 한 것이 아니라
폴더 역할을 설명한 문서였다. 그래서 guard를 두 단계로 나눴다.

- `docs/wiki/research/` 아래에서는 `asset`, `figure`, `table`, `data-product` 같은 넓은
  신호도 검사한다.
- 그 밖의 `docs/` 문서에서는 URL, DOI, NASA/LAMBDA, BAO, PDF, source bundle,
  page-family처럼 더 강한 신호만 검사한다.
- `doc_type: index` 문서는 navigation owner이므로 claim owner 검사에서 제외한다.

조정 뒤 같은 staged guard는 통과했다.

```text
agent workflow guard: passed
```

### 3.4 runtime reminder smoke test

공통 reminder는 JSON 출력 계약을 지켜야 하므로 간단한 입력으로 확인했다.

```text
printf '%s' '{"prompt":"NASA LAMBDA BAO 자료 조사하고 캐시해"}' | rtk .agent/hooks/research-workflow-reminder.py
```

출력은 `hookSpecificOutput`와 `additionalContext`를 포함한 JSON이었다.

```json
{"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": "[QFUDS research workflow reminder]\nBefore any external research, literature, data-product, asset, extraction, coverage, or product-availability claim, read .agent/workflows/README.md and apply .agent/workflows/research-asset-product-workflow.md. Record the workflow name/link and the most specific state token (for example hit_not_cached, asset_cached, no_asset_found, or inaccessible) in any resulting research document. NASA/LAMBDA, BAO, paper, PDF, source, and page-family caches are baseline sources only; do not phrase them as QFUDS support."}}
```

이 결과는 H2의 대응으로 충분했다. 단, 이 smoke test는 hook script의 출력 형식만 확인한다.
실제 Codex/Claude Code host가 현재 세션에서 이 wrapper를 등록했는지는 별도 host 설정 문제다.

### 3.5 repository 검증

구현 후 검증은 다음 순서로 통과했다.

```text
rtk python3 scripts/validate_docs.py
```

출력:

```text
docs validation passed
```

```text
rtk python3 scripts/research_consistency.py
```

주요 출력:

```text
CONSISTENCY PASSED: roadmap is the single source of truth; no drift detected
```

```text
rtk make preflight
```

주요 출력:

```text
preflight: all repository audits passed
```

직접 실행은 `rtk` wrapper에서 권한 문제가 있었다.

```text
rtk scripts/git-hooks/pre-commit
```

출력:

```text
[rtk: Permission denied (os error 13)]
```

같은 hook을 shell로 호출해 실제 순서를 검증했다.

```text
rtk sh scripts/git-hooks/pre-commit
```

주요 출력:

```text
agent workflow guard: passed
docs validation passed
CONSISTENCY PASSED: roadmap is the single source of truth; no drift detected
PREFLIGHT PASSED: exp_003 record is consistent
pre-commit: no qfuds/ or tests/ changes -> skipping regression suite (RUN_TESTS=1 to force)
pre-commit: all checks passed
```

마지막으로 로컬 git hook 설치본도 tracked source와 일치시켰다.

```text
rtk make install-git-hooks && rtk cmp -s scripts/git-hooks/pre-commit .git/hooks/pre-commit && echo installed_pre_commit_matches_source
```

출력:

```text
installed .git/hooks/pre-commit
installed_pre_commit_matches_source
```

## 4. 추가 확인

현재 HEAD는 다음 커밋으로 확인됐다.

```text
rtk git log -1 --oneline
```

출력:

```text
42cc2d8 feat: agent research workflow guard for agentic system
```

변경 파일은 다음 범위였다.

```text
A .agent/hooks/research-workflow-reminder.py
A .claude/hooks/remind-research-workflows.sh
A .codex/hooks/README.md
A .codex/hooks/remind-research-workflows.sh
M AGENTS.md
M CLAUDE.md
M Makefile
A docs/wiki/governance/005_agent_workflow_enforcement_design.md
M docs/wiki/governance/README.md
A scripts/agent_workflow_guard.py
M scripts/git-hooks/pre-commit
```

확인하지 않은 것은 다음이다.

- 현재 실행 중인 Codex session이 `.codex/hooks/remind-research-workflows.sh`를 실제 등록했는지.
- 현재 실행 중인 Claude Code session이 `.claude/hooks/remind-research-workflows.sh`를 실제 등록했는지.
- 모든 과거 research 문서에 workflow marker를 일괄 backfill할 필요가 있는지.

강제력은 runtime hook이 아니라 commit gate에 있으므로, 위 미확인은 이번 해결을 막지 않는다.

## 5. 결론 / 해결

선택한 해결은 세 겹 구조였다.

| 선택 | 고른 이유 | 안 고른 대안 |
| --- | --- | --- |
| [AGENTS.md](../../../AGENTS.md)와 [CLAUDE.md](../../../CLAUDE.md)에 workflow state 기록 의무를 추가 | agent entrypoint에서 같은 규칙을 읽게 한다. | chat instruction에만 남기기. 세션이 바뀌면 사라진다. |
| `.agent/hooks/research-workflow-reminder.py`를 공통 구현으로 두고 Codex/Claude wrapper를 얇게 둠 | 구현은 공유하고 host별 등록 차이는 wrapper로 분리한다. | Codex와 Claude hook 로직을 따로 복사. drift가 생긴다. |
| `scripts/agent_workflow_guard.py --staged`를 pre-commit과 `make preflight`에 연결 | 사람이 놓쳐도 커밋이 멈춘다. | reminder hook만 사용. host 등록 누락과 session cache에 취약하다. |
| [Agent Workflow Enforcement Design](../governance/005_agent_workflow_enforcement_design.md)을 governance에 기록 | 운영 규칙이 왜 생겼는지 repo 안에서 추적할 수 있다. | 코드만 추가. 다음 사람이 왜 있는지 모른다. |

핵심 판단은 다음이다.

```text
workflow 누락은 LLM 태도 문제가 아니라 시스템 경계 문제다.
따라서 prompt reminder가 아니라 commit gate가 최종 방어선이어야 한다.
```

## 6. 재발 방지 / 운영 메모

- 외부자료 claim이 들어간 staged Markdown은 workflow marker와 state token 없이는 커밋되지 않는다.
- NASA/LAMBDA, BAO, DESI/eBOSS, paper, PDF, source, page-family cache는 baseline source로만 기록한다.
- "no product found", "literature checked", "coverage complete" 같은 absence claim은 state ladder 없이 쓰지 않는다.
- runtime reminder는 편의 장치다. host별 hook 등록이 빠져도 pre-commit gate는 남아야 한다.
- guard false positive가 생기면 workflow 규칙을 낮추지 말고, claim owner, path scope,
  signal strength를 조정한다.

## 7. 타임라인

- 2026-06-17: NASA/LAMBDA graphic-history page-family와 BAO baseline 논의 중 workflow 적용 누락 지적.
- 2026-06-17: [Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md)를 다시 확인하고, stable website/page-family도 적용 범위임을 확인.
- 2026-06-17: Codex/Claude 공통 reminder와 `scripts/agent_workflow_guard.py` 설계.
- 2026-06-17: 첫 staged guard에서 governance README false positive 확인.
- 2026-06-17: research folder와 일반 docs의 signal strength를 분리하고 index 문서를 제외해
  false positive 조정.
- 2026-06-17: validation, research consistency, preflight, pre-commit 순서 검증.
- 2026-06-17: 로컬 `.git/hooks/pre-commit` 설치본을 tracked source와 일치시킴.
- 2026-06-17: `42cc2d8` 커밋으로 guard 작업 기록.

## 부록 X - 디버깅 명령어 모음

### 문서와 workflow 확인

```text
rtk sed -n '1,220p' .agent/workflows/README.md
rtk sed -n '1,260p' .agent/workflows/research-asset-product-workflow.md
```

`sed -n 'A,Bp'`는 파일의 A번째 줄부터 B번째 줄까지만 출력한다. 이 사건에서는 workflow
적용 범위와 state ladder를 확인하려고 썼다.

### staged guard 확인

```text
rtk python3 scripts/agent_workflow_guard.py --staged
```

`--staged`는 이번 커밋에 들어갈 파일만 검사한다. 이 사건에서는 guard가 실제 커밋 대상
문서에서 workflow marker와 state token 누락을 잡는지 확인했다.

### hook JSON smoke test

```text
printf '%s' '{"prompt":"NASA LAMBDA BAO 자료 조사하고 캐시해"}' | rtk .agent/hooks/research-workflow-reminder.py
```

`printf`는 작은 입력을 그대로 만들어 표준입력으로 넘긴다. 이 사건에서는 hook이 raw text가
아니라 JSON을 출력하는지 확인했다.

### repo 검증

```text
rtk python3 scripts/validate_docs.py
rtk python3 scripts/research_consistency.py
rtk make preflight
rtk git diff --check
```

이 묶음은 문서 frontmatter, status authority, exp_003 기록, 공백 오류를 확인한다. 이런
부류의 문제는 먼저 좁은 guard를 단독 실행하고, 그 다음 전체 preflight로 넓혀 확인하는
순서가 좋다.

### pre-commit 설치 확인

```text
rtk make install-git-hooks
rtk cmp -s scripts/git-hooks/pre-commit .git/hooks/pre-commit
```

`cmp -s`는 두 파일이 같은지 조용히 비교한다. 이 사건에서는 tracked hook source와 로컬
`.git/hooks/pre-commit` 설치본이 같은지 확인했다.
