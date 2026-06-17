---
doc_id: postmortem-014-parser-tool-link-guard-false-positive
id: postmortem-014-parser-tool-link-guard-false-positive
seq: 14
title: "파서 도구 링크와 workflow guard 오탐 회고"
doc_type: postmortem
type: postmortem
stage: reference
status: reference
wiki_status: active
evidence_role: provenance
depends_on:
  - postmortem-013-agent-research-workflow-guard
  - wiki_governance_005_agent_workflow_enforcement_design
next_gate: tool-reference links must not be treated as research-asset claims; keep workflow guard strict for actual source/product claims
date: 2026-06-17
context: PageIndex and MarkItDown repository links were added across QFUDS docs, then agent_workflow_guard.py blocked the commit because tool URLs looked like external research claims
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
    note: "PageIndex/MarkItDown 링크 보강 커밋 20cf49d 직후, workflow guard 오탐과 보정 근거를 기록"
tags: [postmortem, agent-system, workflow-guard, documentation, links]
relations:
  - docs/wiki/postmortem/013-20260617-dorito-agent-research-workflow-guard.md
  - docs/wiki/governance/005_agent_workflow_enforcement_design.md
  - .agent/workflows/research-asset-product-workflow.md
  - .agent/workflows/research-asset-digitization-workflow.md
code_refs:
  - file: scripts/agent_workflow_guard.py
    note: "PageIndex/MarkItDown tool-reference link-only diff와 pre-commit last_updated hunk를 연구 claim 오탐에서 제외"
  - file: docs/wiki/research/assets/eboss_dr16_lya_bao_2020/digitization/markitdown_BAO-only_README.md
    note: "기존 upstream source URL이 있는 변환 산출물에 workflow marker와 asset_cached 상태를 명시"
  - file: .agent/workflows/research-asset-digitization-workflow.md
    note: "PageIndex MCP와 MarkItDown non-paper route의 역할 구분을 링크로 보강"
---

# 파서 도구 링크와 workflow guard 오탐 회고

## 사건 한 줄 요약

[PageIndex](https://github.com/VectifyAI/PageIndex)와 [MarkItDown](https://github.com/microsoft/markitdown)
언급을 저장소 문서 전체에서 링크로 바꾸자, `agent_workflow_guard.py`가 도구 GitHub URL을
외부 연구 자산 claim으로 오탐해 커밋을 막았다. 해결은 도구 레퍼런스 링크만 바꾸는 staged
diff를 예외 처리하되, 실제 연구 자산 문서의 source/product claim에는 workflow marker와
state token 요구를 그대로 유지하는 것이었다.

## 0. 사전 지식

| 용어 | 뜻 | 이 사건에서 중요한 이유 |
| --- | --- | --- |
| tool-reference link | 도구 설명을 위해 붙인 프로젝트 링크 | PageIndex와 MarkItDown GitHub 링크는 논문, 데이터셋, source product가 아니다. |
| external-research claim | 외부 논문, PDF, source, 데이터, coverage, asset 상태에 대한 주장 | 이 claim은 [Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md) marker와 state token이 필요하다. |
| state token | workflow state ladder의 상태 값 | `asset_cached`, `hit_not_cached`, `no_asset_found` 같은 값으로 자산 확인 수준을 남긴다. |
| pre-commit `last_updated` | 커밋 직전 staged Markdown의 날짜를 자동 갱신하는 훅 단계 | link-only diff였던 파일에 `last_updated:` hunk가 추가되어 예외 판정이 다시 깨졌다. |

핵심 구분은 간단하다.

```text
PageIndex/MarkItDown 도구 링크 = 도구 설명
NASA/LAMBDA, BAO, arXiv, DOI, source bundle 링크 = 연구 자산 또는 source claim 후보
```

둘 다 URL이지만 같은 의미가 아니다. guard는 URL 문자열만 보면 둘을 구분하지 못한다.

## 1. 증상

전체 문서에서 `PageIndex`와 `MarkItDown` 언급에 GitHub 링크를 붙인 뒤, staged guard가 실패했다.
대표 증상은 다음과 같았다.

```text
agent workflow guard: failed
- docs/00_project/qfuds_ko.md
  - missing Research Asset and Product Workflow marker/link for external-research or product-availability claims
  - missing workflow state token such as asset_cached, hit_not_cached, no_asset_found, or inaccessible
- docs/wiki/lineage/003_research_flow_plain_language_ko.md
  - missing Research Asset and Product Workflow marker/link for external-research or product-availability claims
  - missing workflow state token such as asset_cached, hit_not_cached, no_asset_found, or inaccessible
...
Apply .agent/workflows/research-asset-product-workflow.md and record the workflow state before committing.
```

이 실패는 실제로 새 NASA/LAMBDA, BAO, arXiv source claim을 추가해서 생긴 것이 아니었다.
문서 안의 파서 도구 이름을 다음처럼 링크로 바꾼 결과였다.

```text
PageIndex -> [PageIndex](https://github.com/VectifyAI/PageIndex)
MarkItDown -> [MarkItDown](https://github.com/microsoft/markitdown)
```

하지만 guard는 `https?://`와 `github`를 외부 연구 신호로 잡고 있었다.

## 2. 첫 의문 + 가설

| 가설 | 왜 그럴 수 있는지 | 어떻게 확인할지 |
| --- | --- | --- |
| H1. 실제 연구 자산 claim이 새로 추가됐다 | 링크를 전체 문서에 넣으면서 연구 source URL도 새로 만들었을 수 있다 | `git diff --cached --stat`, 실패 파일 diff를 본다 |
| H2. guard가 도구 GitHub 링크를 연구 source link로 오탐했다 | `STRICT_EXTERNAL_RESEARCH_RE`가 `https?://`와 `github`를 모두 잡는다 | `scripts/agent_workflow_guard.py`의 정규식을 읽는다 |
| H3. generated digitization 문서까지 바꾼 것이 문제다 | asset digitization 문서에는 원래 source URL과 `BAO` 같은 단어가 많다 | 실패 파일 목록과 `docs/wiki/research/assets/...` 범위를 대조한다 |
| H4. pre-commit의 `last_updated` 자동 갱신이 link-only 예외를 깨뜨렸다 | pre-commit은 guard 전에 `last_updated`를 바꾼다 | `scripts/git-hooks/pre-commit` 실행 출력과 staged diff를 본다 |
| H5. guard를 끄는 것이 빠른 해결이다 | 링크 보강 커밋만 통과시키려면 가장 쉬워 보인다 | 013 회고와 005 governance의 hard gate 목적과 비교한다 |

## 3. 진단: 실제 상태 확인

### 3.1 변경 범위 확인

명령:

```bash
rtk git diff --cached --stat
```

출력 요약:

```text
83 files changed, 341 insertions(+), 270 deletions(-)
```

해석:

- 변경 범위가 넓었다.
- 대부분은 `PageIndex` 또는 `MarkItDown` 일반 언급을 GitHub 링크로 바꾸는 문서 변경이었다.
- H1은 일부만 가능했다. 실제 새 연구 결과를 추가한 것은 아니지만, asset/digitization 문서에는 기존 외부 source URL이 이미 많아서 guard가 파일 전체를 다시 검사하면 실패할 수 있었다.

### 3.2 guard 정규식 확인

명령:

```bash
rtk sed -n '1,230p' scripts/agent_workflow_guard.py
```

확인한 코드:

```python
STRICT_EXTERNAL_RESEARCH_RE = re.compile(
    r"(?ix)"
    r"https?://|"
    r"\barxiv\b|"
    r"\bdoi\b|"
    r"\bnasa\b|"
    r"\blambda\b|"
    r"\bdesi\b|"
    r"\beboss\b|"
    r"\bbao\b|"
    r"\bzenodo\b|"
    r"\bosf\b|"
    r"\bdataverse\b|"
    r"\bgithub\b|"
    r"\bpdf\b|"
    ...
)
```

해석:

- H2는 지지된다.
- 도구 문서 링크도 `https://github.com/...`이므로 strict external research signal에 걸린다.
- 이 정규식 자체가 틀린 것은 아니다. 실제 연구 source가 GitHub release, code repo, archive인 경우도 있기 때문이다.

### 3.3 staged guard 실패 재현

명령:

```bash
rtk python3 scripts/agent_workflow_guard.py --staged
```

초기 실패 요약:

```text
agent workflow guard: failed
- docs/00_project/qfuds_ko.md
  - missing Research Asset and Product Workflow marker/link for external-research or product-availability claims
  - missing workflow state token such as asset_cached, hit_not_cached, no_asset_found, or inaccessible
...
```

해석:

- H3도 지지된다.
- guard는 staged 파일 전체를 읽는다. 링크 보강처럼 작고 기계적인 변경이어도, 파일 안에 기존
  `PDF`, `asset`, `BAO`, external URL이 있으면 workflow marker/state token 누락으로 걸릴 수 있다.
- 이 동작은 신규 연구 claim 차단에는 보수적이지만, 도구 링크 보강 같은 maintenance commit에는 과했다.

### 3.4 pre-commit에서 `last_updated` hunk가 추가됨

명령:

```bash
rtk sh scripts/git-hooks/pre-commit
```

출력 일부:

```text
pre-commit: running QFUDS documentation and regression checks
frontmatter last_updated: updated
  docs/wiki/lineage/003_research_flow_plain_language_ko.md
  docs/wiki/postmortem/005-20260611-dorito-research-asset-digitization-automation.md
  docs/wiki/research/assets/abbott_2023_gwtc3_population_merging_compact_binaries/README.md
  ...
agent workflow guard: failed
- docs/wiki/lineage/003_research_flow_plain_language_ko.md
  - missing Research Asset and Product Workflow marker/link for external-research or product-availability claims
```

해석:

- H4는 지지된다.
- 처음에는 "도구 링크 치환만 포함한 diff"를 예외 처리하면 충분해 보였다.
- 하지만 pre-commit은 guard 전에 `last_updated:`를 자동 변경한다.
- 따라서 staged diff는 더 이상 순수 link-only diff가 아니었고, 예외 조건에 `last_updated:` 전용 hunk를 허용해야 했다.

### 3.5 최종 검증

수정 후 pre-commit 전체를 다시 실행했다.

명령:

```bash
rtk sh scripts/git-hooks/pre-commit
```

출력 요약:

```text
agent workflow guard: passed
docs validation passed
CONSISTENCY PASSED: roadmap is the single source of truth; no drift detected
PREFLIGHT PASSED: exp_003 record is consistent
pre-commit: no qfuds/ or tests/ changes -> skipping regression suite (RUN_TESTS=1 to force)
pre-commit: all checks passed
```

해석:

- 최종 보정은 현재 커밋 경로에서 동작했다.
- full regression suite는 실행되지 않았다. `qfuds/` 또는 `tests/` 변경이 아니었고, pre-commit 정책에 따라 문서 변경에서는 건너뛰었다.
- 이 사건은 물리 계산이나 QFUDS status와 무관하다.

## 4. 추가 확인

커밋 결과:

```text
20cf49d docs: link parser tool references
```

이 커밋에서 관련 핵심 변경은 두 가지다.

| 파일 | 변경 | 이유 |
| --- | --- | --- |
| [scripts/agent_workflow_guard.py](../../../scripts/agent_workflow_guard.py) | `TOOL_REFERENCE_LINKS`, `staged_change_is_only_tool_reference_links`, `last_updated:` hunk 허용 추가 | 도구 링크 보강을 연구 source claim으로 오탐하지 않기 위해 |
| [markitdown_BAO-only_README.md](../research/assets/eboss_dr16_lya_bao_2020/digitization/markitdown_BAO-only_README.md) | workflow marker와 `asset_cached` 상태 추가 | 이 파일은 실제 upstream source URL을 포함하므로 예외 처리보다 명시적 상태 기록이 맞음 |

## 5. 결론 / 해결

선택한 해결:

- PageIndex/MarkItDown GitHub 링크만 도구 레퍼런스로 allowlist 처리했다.
- allowlist는 staged diff가 도구 링크 치환과 `last_updated:` 자동 갱신만 포함할 때만 작동하게 했다.
- 실제 source/product URL이 있는 `markitdown_BAO-only_README.md`에는 [Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md) marker와 `asset_cached` state token을 직접 추가했다.

고르지 않은 대안:

| 대안 | 왜 고르지 않았나 |
| --- | --- |
| `https?://`나 `github`를 guard 신호에서 제거 | GitHub release, code repo, data archive가 실제 연구 자산인 경우를 놓친다. |
| 이번 커밋에서 guard를 우회 | 013에서 만든 hard gate의 목적을 바로 약화한다. |
| 모든 기존 asset 문서에 workflow marker를 대량 추가 | 이번 사건의 직접 원인은 도구 링크 보강이다. 대량 보강은 별도 감사 작업으로 분리하는 것이 낫다. |
| PageIndex/MarkItDown을 링크하지 않음 | 독자가 도구 출처로 이동할 수 없어 문서 품질 요구를 만족하지 못한다. |

현재 남은 한계:

- guard는 여전히 정규식 기반이다. 문장 의미를 깊게 해석하지 않는다.
- 이번 보정은 PageIndex/MarkItDown 두 도구 링크만 대상으로 한다.
- 다른 도구 URL을 대량 링크화할 때는 같은 방식의 allowlist가 필요한지 별도 판단해야 한다.

## 6. 재발 방지 / 운영 메모

- 도구 링크와 연구 자산 링크를 분리한다.
- guard 예외는 "파일 이름" 기준이 아니라 "staged diff의 의미" 기준으로 둔다.
- pre-commit에서 자동 변경되는 `last_updated:` hunk를 고려한다.
- 실제 source/product URL이 들어간 문서는 가능하면 workflow marker와 state token을 직접 남긴다.
- guard를 넓게 끄기보다, 오탐 범위를 좁게 설명 가능한 형태로 줄인다.

다음에 비슷한 일이 생기면 먼저 다음 질문을 던진다.

```text
이 URL은 도구 출처인가, 연구 source/product claim인가?
이 변경은 새 claim인가, 기존 용어의 링크화인가?
pre-commit 자동 변경이 staged diff에 추가됐는가?
```

## 7. 타임라인

- 2026-06-17: PageIndex/MarkItDown 언급을 전체 Markdown 문서에서 GitHub 링크로 보강.
- 2026-06-17: `agent_workflow_guard.py --staged`가 다수 문서에서 workflow marker/state token 누락으로 실패.
- 2026-06-17: guard의 `https?://`와 `github` 정규식이 도구 링크도 잡는다는 점 확인.
- 2026-06-17: PageIndex/MarkItDown tool-reference link-only diff 예외 추가.
- 2026-06-17: pre-commit의 `last_updated:` 자동 갱신이 link-only 예외를 깨뜨리는 점 확인.
- 2026-06-17: `last_updated:` hunk 허용과 `markitdown_BAO-only_README.md` workflow marker 보강.
- 2026-06-17: pre-commit 전체 통과 후 `20cf49d` 커밋 생성.

## 부록 A — 디버깅 명령어 모음

### 변경 범위 보기

```bash
rtk git diff --cached --stat
rtk git status --short
```

`git diff --cached --stat`은 staged 변경의 파일 수와 줄 수를 요약한다. 이 사건에서는 링크 보강이
넓은 문서 범위에 걸쳐 있다는 점을 확인했다. `git status --short`는 staged/unstaged 상태를 짧게
보여준다. 중간에 parent thread와 stage 상태가 섞였을 때, 이 명령으로 index가 비어 있거나
다른 파일이 staged된 상황을 확인했다.

### guard 직접 실행

```bash
rtk python3 scripts/agent_workflow_guard.py --staged
```

이 명령은 commit 전에 staged Markdown만 대상으로 external research claim과 workflow marker/state
token 누락을 검사한다. 이 사건에서는 도구 링크가 `github` URL이라는 이유로 실패하는 것을 재현했다.

### pre-commit 전체 실행

```bash
rtk sh scripts/git-hooks/pre-commit
```

repo 표준 pre-commit 순서를 그대로 실행한다. `last_updated` 자동 갱신, workflow guard,
문서 검증, roadmap consistency, exp_003 preflight, 공백 검사 순서가 함께 돈다. 이 사건에서는
`last_updated:` hunk가 guard 예외 조건에 영향을 준다는 점을 확인했다.

### guard 코드 읽기

```bash
rtk sed -n '1,230p' scripts/agent_workflow_guard.py
```

`sed -n '1,230p'`는 파일의 1~230줄만 출력한다. 이 사건에서는 `STRICT_EXTERNAL_RESEARCH_RE`가
`https?://`와 `github`를 모두 잡는다는 점을 확인했다.

### 특정 파일 diff 보기

```bash
rtk git diff --cached -- docs/wiki/research/assets/eboss_dr16_lya_bao_2020/digitization/markitdown_BAO-only_README.md
```

`-- <path>` 뒤에 파일을 주면 그 파일의 staged diff만 본다. 이 사건에서는
`markitdown_BAO-only_README.md`가 단순 도구 링크 외에 기존 upstream source URL을 포함하고 있어,
예외 처리보다 workflow marker/state token을 직접 남기는 편이 맞다고 판단했다.

이런 부류의 문제는 보통 이 순서로 푼다.

```text
실패 메시지 확인
-> staged diff 범위 확인
-> guard 정규식과 실패 파일을 대조
-> 실제 claim이면 workflow marker/state token 추가
-> 도구 링크 오탐이면 좁은 예외 추가
-> pre-commit 전체 재실행
```
