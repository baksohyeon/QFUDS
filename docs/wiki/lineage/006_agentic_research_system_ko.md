---
doc_id: qfuds_lineage_agentic_research_system_ko
title: "QFUDS 에이전틱 연구 시스템: 한 사람이 만든 자기교정 AI 연구 하네스의 해부"
doc_type: summary
stage: reference
status: reference
evidence_role: provenance
depends_on:
  - roadmap
  - qfuds_lineage_rough_tanh_thesis_report_ko
next_gate: provenance only; 상태 권위는 roadmap; 운영 규칙 SSOT는 .agent/workflows/; observer mode 무손상
last_updated: 2026-06-13
---

# QFUDS 에이전틱 연구 시스템: 한 사람이 만든 자기교정 AI 연구 하네스의 해부

> **문서 성격 (먼저 읽을 것).** 이 문서는 provenance(출처 기록)이자 회고다.
> QFUDS를 지지하는 증거가 아니고, 로드맵 상태나 050 천장, observer mode를 바꾸지
> 않는다. 운영 규칙의 단일 진실 원천(SSOT)은 이 문서가 아니라 `.agent/workflows/`
> 디렉터리다. 여기서는 그 시스템을 *해부하고 분석*할 뿐, 규칙을 새로 만들지 않는다.

## 한 줄 요약

[004 수치 스케치](004_rough_tanh_numerical_sketch_ko.md)의 거친 tanh 탐색과
[005 논문 보고서](005_rough_tanh_thesis_report_ko.md)가 "물리 결과"라면, 이 글은
그 결과를 가능하게 한 **인프라의 해부**다. 핵심 주장은 단순하다. **이 연구는 손으로
했다면 여기까지 오지 못했다.** 비전문가 한 사람이 24개 체크포인트에 걸쳐 투기적
가설을 끝까지 밀면서도 과대주장으로 미끄러지지 않은 것은, 인식론적 규율을 *코드와
워크플로로 강제하는* 자기교정 AI 연구 하네스(harness) 덕분이다. 그 하네스가 무엇으로
이루어졌는지를 아래에서 한 겹씩 벗겨 본다.

## 1. 시스템 전경

전체는 세 켜로 쌓여 있다. 사람이 여러 AI를 조율하는 맨 위 켜, 무엇을 어디에 두고
무엇을 주장하면 안 되는지를 고정한 운영 거버넌스 켜, 그리고 매 작업을 병렬·적대적으로
돌리고 커밋마다 통과 기준으로 거르는 실행 켜다.

```text
인간 오케스트레이터 (멀티 AI: Claude Code 주 하네스 + Codex·Gemini 교차검토)
  -> 운영 거버넌스 SSOT  (.agent/workflows/ : 라우팅·상태경계·전파·금지단축)
  -> 세션 실행 패턴      (병렬 fan-out + 적대적 검증 + 직렬 통합, worktree 격리)
  -> 결정론적 게이트     (pre-commit hook + scripts/ + Makefile)
  -> append-only 기록    (1 CP = 1 commit, 회고 postmortem)
```

이 구조의 목적은 하나다. **가짜 돌파가 조용히 살아남지 못하게 만드는 것.** 사람이
강하게 밀어붙이는 순간에도 시스템이 자동으로 "재검산 아닌가", "이건 유도가 아니라
매개화 아닌가"를 되묻게 설계됐다.

이 글에서는 이 시스템 전체를 **리서치 에이전트 하네스(Research-Agent Harness)**라고
부른다. 거버넌스로 묶여 스스로를 교정하는, 사실상 에이전트로 꾸린 연구팀이다. 한 사람이
오케스트레이터 겸 PI로 앉고, 탐지·계산·윤문·감사·적대적 리뷰를 각각 다른 에이전트가
맡는다.

## 2. 권위 체인: 무엇이 진실의 원천인가 (SSOT)

이 시스템의 토대는 "무엇이 진실의 원천(SSOT)인가"를 문서로 못박은 것이다. 권위가
충돌할 여지를 없애려고, 역할마다 단 하나의 권위 문서를 정해 계층으로 쌓았다.

```text
CLAUDE.md      (얇은 진입점: 상태를 들고 있지 않고 아래를 가리키기만 한다)
  -> AGENTS.md  (프로젝트 헌법: 절차와 연구 규칙)
  -> .agent/workflows/  (운영 규칙 SSOT: 반복 절차는 여기를 먼저 본다)
  -> docs/05_next_steps/000_roadmap.md  (상태 SSOT: 현재 레벨·게이트·blocker)
  -> docs/  (지식·증거·연구 기록·캐시 자산)
```

규칙은 단순하고 강하다. 같은 운영 규칙이 `.agent/`와 `docs/`에 둘 다 있으면 `.agent/`
쪽이 권위이고 `docs/` 쪽은 링크로 줄인다. 상태(status)에 대한 주장은 오직 roadmap만
한다. 다른 문서는 "상태는 roadmap을 보라"고 위임할 뿐, 자기 상태를 따로 만들지
않는다. 이 계층 덕분에 "아까 채팅에서 이렇게 정했잖아" 같은 휘발성 기억이 권위를
가로채지 못한다. (이 문서 자체도 그 규율을 따른다. 운영 규칙을 새로 만들지 않고
`.agent/workflows/`를 권위로 가리킬 뿐이다.)

## 3. 층 A: 운영 거버넌스 SSOT (`.agent/workflows/`)

`.agent/` 디렉터리는 사람을 위한 문서(`docs/`)와 에이전트가 따라야 할 운영 규칙을
분리해 담은 *에이전트용 운영 위키*다. ("LLM을 위한 위키"라는 이 패턴 자체는 별도
사이드 프로젝트에서 먼저 실험했고, 이 레포에는 리서치 에이전트 하네스의 거버넌스 층으로
들여왔다.) 연구가 문서·데이터·문헌·자산·산출물에 손대는 *반복 가능한 절차*는 모두 먼저
이 워크플로를 조회하고 따라야 한다. 채팅 기록이나 도구 메모리는 권위가 아니고,
워크플로 디렉터리가 SSOT다. 다섯 개의 워크플로가 서로 다른 국면을 맡는다.

| 워크플로 | 맡는 일 |
| --- | --- |
| `documentation-folder-routing-workflow` | 문서를 기능에 따라 어느 폴더에 둘지, 연구 결과가 roadmap·lineage·governance로 전파될지 결정 |
| `wiki-maintenance-workflow` | wiki 인덱스·레코드 유지, 재사용 가능한 질의 답변 적재 |
| `research-asset-product-workflow` | 외부 논문·PDF·arXiv 소스·보충자료·데이터셋의 *가용성*을 먼저 기록 |
| `research-asset-digitization-workflow` | 캐시한 자산을 Markdown/CSV로 디지털화(구조·전문·그림 추출) |
| `research-investigation-result-routing-workflow` | 산출물을 assets/·plans/·conclusions/로 올바로 분기 |

이 거버넌스가 강제하는 네 규칙이 observer mode를 *구조적으로* 지킨다. (1) 기능 기반
라우팅(주제가 아니라 역할로 배치), (2) 상태 경계(산출물이 존재한다는 이유만으로
roadmap을 갱신하지 않음), (3) 전파 규칙(즉시 갱신할 것과 조건부 갱신할 것을 표로
고정), (4) 금지 단축(연구 산출물로 "QFUDS 지지"나 "Level 2B 적격"을 주장하지 않음).
요지는 한 줄이다. **자산이 존재하는 상태는 물리적으로 적격인 상태가 아니다.**

## 4. 연구 파이프라인: 논문에서 판별까지

사용자가 손으로 했다면 가장 지쳤을 부분, 곧 "논문에서 숫자를 꺼내 우리 곡선과
맞대는" 과정이 워크플로로 자동화돼 있다. 흐름은 이렇다.

```text
논문/자산 가용성 기록  (URL·타입·상태·추출 가능성 먼저 적는다)
  -> 디지털화          (PageIndex 구조·전문 추출 + MarkItDown 변환 + 고해상 figure 추출)
  -> 표본/수치 추출     (CSV로 뽑는다)
  -> 비교              (디지털화한 Chen entropy 곡선과 전이함수 Γ(a)를 맞댄다)
  -> known-model 판별   (이미 알려진 모델과 무엇이 다른지 자동 대조)
  -> 라우팅            (산출물은 assets/, 판단은 conclusions/, 가지 변화는 lineage/)
```

**캐시 히트와 미스를 섬세하게 구분하는 상태 사다리.** "있다/없다"로 끝내지 않으려고,
자산의 상태를 11단계 사다리로 못박았다. 검색을 안 했는지(`not searched`), 검색했지만
못 찾았는지(`searched_no_hit`), 출처는 찾았지만 아직 로컬 캐시가 없는지
(`hit_not_cached`, 곧 캐시 미스), 받았지만 안 풀었는지(`asset_downloaded_not_extracted`),
그림·표는 뽑았지만 아직 수치로 디지털화 안 했는지(`asset_extracted_not_digitized`),
원자료와 매니페스트까지 저장됐는지(`asset_cached`, 곧 캐시 히트)를 *가장 구체적인
상태*로 기록한다. Markdown 변환 품질도 따로 기록한다. 키워드 검색용 저충실
(`low_fidelity_search_text`)부터 출처 파싱 가능(`source_text_parse`), 사람이 큐레이션한
(`manual_structured_extract`), 우도까지 가능한(`numeric_digitized`) 등급으로 나눈다.
이 사다리가 "PDF가 존재한다"를 "데이터로 쓸 수 있다"로 잘못 승격시키는 미끄러짐을
막고, 같은 논문을 다시 받지 않도록 캐시 히트를 명시한다.

**PageIndex·MarkItDown MCP로 추출을 자동화.** 논문 본문·구조 추출은 PageIndex MCP
서버로 한다. `browse_documents`로 이미 적재한 문서를 다시 올리지 않게 막고,
`process_document`로 적재하며, `get_document_structure`로 계층 목차를, `get_page_content`로
본문을 페이지 단위로 가져온다. 매니페스트·표·코드만 있는 데이터 릴리스는 MarkItDown으로
Markdown으로 변환하고, 그림은 Poppler·ImageMagick으로 추출한다. API 키는 절대 커밋하지
않고 환경변수나 로컬 MCP 설정에만 둔다.

핵심은 순서의 강제다. 본문에 "이 논문이 매장했다" 같은 확정형 문장을 적기 *전에*
먼저 자산 상태(다운로드 여부·추출 가능성)를 기록하게 한다. 이 순서를 어겼다가 사후
복구한 사건이 [회고 005](../postmortem/005-20260611-dorito-research-asset-digitization-automation.md)와
[회고 011](../postmortem/011-20260612-dorito-rough-tanh-lineage-natural-closing-retro.md)에
남아 있다. 논문을 다시 찾을 때 비용을 아끼는 캐싱은 [회고 001](../postmortem/001-20260609-dorito-li-2025-data-cache.md)에서
시작됐다.

## 5. 층 B: 세션 실행 패턴 (병렬·적대적·결정론적)

거버넌스 안에서 한 세션은 다음 패턴으로 돈다.

- **Append-only + 원자적 커밋.** 각 체크포인트는 독립 스크립트, 그림, 수치(csv),
  문서 섹션을 커밋 하나로 묶는다(1 CP = 1 commit). 이전 결론을 덮지 않고 아래로 쌓는다.
- **병렬 fan-out + 직렬 통합.** 서로 독립인 계산(ISW, kill-test, 점성, 천장 메커니즘
  등)은 다수 하위 에이전트로 *병렬 spawn*되고, 공유 자원(문서 append, CP 번호, git)은
  충돌과 번호 경합을 피하려 메인 에이전트가 *직렬*로 통합한다. 파일을 동시에 고치는
  작업은 git **worktree**로 격리해 서로 밟지 않게 한다.
- **적대적 검증(비대칭).** 모든 *positive* 주장(줄였다·유도했다·통과했다)은 커밋 전에
  적대적 리뷰어 에이전트의 반박을 거친다. 부정·제자리 결과는 안전 방향이라 가볍게,
  긍정 주장만 빡세게 검증한다. 실제로 잡아낸 사례가 [005 §2.4](005_rough_tanh_thesis_report_ko.md)에
  세 건 기록돼 있다. 천장 분해 초안의 상관길이 사다리가 미시 쪽으로 편향된 것을
  red-team이 거시 지평을 빠뜨렸다고 지적해 교정했고, tracker attractor의 "진짜 부분
  승리"를 적분기가 해석적 상태방정식을 재현하는지 독립 재실행으로 검증했으며,
  우주상수 문제를 환각 최대 위험 지점으로 분류해 "유도했다" 결과가 나오면 즉시 가짜로
  플래그하게 가드를 걸었다.
- **인식론적 가드레일 4종.** parametrize ≠ derive(매개화는 유도가 아니다),
  brute-force hit ≠ derivation(끼워맞춤 적중은 유도가 아니다), representative ≠
  likelihood(대표값은 실제 우도가 아니다), rough proxy(진짜 검증은 Boltzmann 코드).

## 6. 결정론적 게이트: 과학적 규율을 코드로 강제

가장 단단한 안전장치는 사람의 의지가 아니라 훅이다. `scripts/git-hooks/pre-commit`이
매 커밋에서 다음을 순서대로 강제한다.

```text
frontmatter last_updated 자동 갱신
  -> validate_docs.py        (메타데이터·H1 일치·고유 doc_id 검사)
  -> research_consistency.py (로드맵이 상태 권위인지, 독립 상태 주장 없는지)
  -> preflight_exp004.py     (실험 기록 정합성 게이트)
  -> git diff --check        (공백 오류)
  -> (qfuds/ 또는 tests/ 변경 시에만) 회귀 테스트 전체
```

회귀 테스트를 문서 전용 커밋에서 건너뛰어 속도를 지키는 스코프 결정은
[회고 006](../postmortem/006-20260611-dorito-precommit-regression-test-scope.md)에
근거가 남아 있다. 같은 게이트를 `Makefile`(`make preflight`)과 `scripts/`로도 돌릴 수
있다. rough tanh lineage의 전 24개 체크포인트가 이 게이트를 통과했고, 그래서 "미성숙
완료 주장"이 디렉터리·인덱스 차원에서 자동 차단됐다.

게이트는 커밋 시점에서 끝나지 않는다. 에이전트가 글을 *쓰는 순간*에도 Claude Code 훅이
돈다. `.claude/hooks/`의 세 훅이 그것이다. `remind-korean-style.sh`(UserPromptSubmit)는
매 turn 시작에 한국어 어휘 anti-pattern 규칙을 컨텍스트에 주입하고, `no-bak-slang-check.sh`와
`no-emoji-check.sh`(PreToolUse Write·Edit)는 한국어 직역 슬랭과 이모지를 파일에 쓰기
*직전에* 차단한다. 규칙의 출처는 `.agent/`의 korean-persona 어휘 anti-pattern 표다.
영리한 부분은 self-skip이다. 훅이 자기 정의 파일과 회고(차단 사례를 메타 인용해야 하는
곳)에서는 스스로 비켜서 데드락을 피한다. 즉 문체 규율마저 사람의 기억이 아니라 훅으로
강제되고, 그 훅조차 자기 예외를 안다.

## 7. 인간 + 멀티 AI 오케스트레이션

이 시스템은 단일 챗봇과의 대화가 아니다. 연구자가 한 일은 다음과 같다.

- **프롬프트 엔지니어링으로 역할 분리.** 탐지·윤문·감사·리뷰처럼 책임을 나눠 에이전트를
  설계했다.
- **병렬 에이전트 spawn과 worktree 격리.** 독립 작업을 동시에 띄우고, 파일 충돌은
  worktree로 분리했다.
- **여러 AI의 교차검토.** Claude Code를 주 연구 하네스로 두고, Codex와 Gemini를
  보조·교차검증에 활용했다. 한 모델의 약점을 다른 모델이 메우게 했다.
- **테스트로 버그를 잡아냄.** 수치 회귀 테스트가 실험 코드를 기록된 출력과 대조해,
  사람 눈이 놓친 어긋남을 잡았다.
- **적대적 리뷰어로 엄격한 과학 규율 유지.** 긍정 주장마다 반대 검증을 붙여, 투기적
  탐색을 끝까지 밀면서도 정직성을 지켰다. 최종 검수자 역할까지 에이전트가 맡았다.

## 8. 회고 규율

굵직한 사건마다 회고를 append-only로 남겨 같은 실수를 반복하지 않게 했다. 회고는
`docs/wiki/postmortem/`에 쌓인다. 그리고 이 회고들은 손으로 쓴 게 아니라 내가 만든
회고 스킬(`.agents/skills/postmortem/`)이 생성한다. 스킬은 시퀀스 번호를 자동 채번하고,
주니어 개발자 눈높이의 한국어 산문과 엄격한 YAML frontmatter(`audit_log`·`relations`·
`code_refs` 포함)를 강제하며, 위 스타일 훅이 회고에서 self-skip한다는 점까지 알고
동작한다. 회고를 쓰는 행위 자체가 표준화된 도구로 묶여 있는 셈이다.

| seq | 주제 |
| --- | --- |
| 001 | Li 2025 데이터 캐시 |
| 002 | IV/IDE 타이밍 체크포인트 |
| 003 | QFUDS 스코프 강등 회고 |
| 004 | Source-X 데이터 산출물 감사 |
| 005 | 연구 자산 디지털화 자동화 |
| 006 | pre-commit 회귀 테스트 스코프 |
| 007 | Source-X 산출물 라우팅 워크플로 |
| 008 | Source-X 진행 체크포인트 |
| 009 | QFUDS observer mode 종결 회고 |
| 010 | rough tanh lineage 하강 회고 |
| 011 | rough tanh lineage 자연 닫힘 회고 |

## 9. 무엇이 검증됐고 무엇이 아닌가

분명히 해 둘 것이 있다. 이 시스템의 기여는 *방법론*이다. [005 논문 보고서](005_rough_tanh_thesis_report_ko.md)가
물리 분석과 나란히 내세우는 두 번째 기여, 곧 "운영 거버넌스 SSOT와 병렬·적대적·
결정론적 실행 패턴을 결합한 자기교정 연구 하네스가, 투기적 가설을 끝까지 밀면서도
가짜 돌파를 구조적으로 차단하고 정직한 결론에 도달하게 했다"는 점을 이 문서가 해부한
것이다.

그러나 **이 인프라의 존재가 QFUDS를 지지하지는 않는다.** 정교한 시스템으로 도달한
결론이라 해서 결론의 물리적 무게가 커지는 것은 아니다. 상태의 단일 진실 원천은 여전히
[로드맵](../../05_next_steps/000_roadmap.md)이고, 프로젝트는 observer mode 그대로이며,
050 천장은 무손상이다. 이 글은 "어떻게 정직하게 여기까지 왔는가"의 기록이지, "결론이
옳다"의 증거가 아니다.

## 부록: 참조

- 운영 규칙 SSOT: `.agent/workflows/`(5개 워크플로)와 `.agent/` 에이전트 위키
- 결정론적 게이트: `scripts/git-hooks/pre-commit`, `Makefile`(`make preflight`), `scripts/`
- 회고 로그: [`docs/wiki/postmortem/`](../postmortem/)
- 이 시스템이 만든 결과: [004 수치 스케치](004_rough_tanh_numerical_sketch_ko.md),
  [005 논문 보고서](005_rough_tanh_thesis_report_ko.md)
