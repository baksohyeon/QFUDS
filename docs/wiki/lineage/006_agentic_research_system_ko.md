---
doc_id: qfuds_lineage_agentic_research_system_ko
title: "QFUDS 에이전트 기반 연구 운영 절차 기록"
doc_type: summary
stage: reference
status: reference
evidence_role: provenance
depends_on:
  - roadmap
  - qfuds_lineage_rough_tanh_thesis_report_ko
next_gate: provenance only; 상태 기준은 roadmap; 운영 규칙 SSOT는 .agent/workflows/; observer mode 무손상
last_updated: 2026-06-17
---

# QFUDS 에이전트 기반 연구 운영 절차 기록

> **문서 성격 (먼저 읽을 것).** 이 문서는 provenance(출처 기록, "어떻게 여기까지
> 왔는지 남기는 기록")이자 회고입니다. QFUDS를 지지하는 증거가 아니며, 로드맵 상태나
> 050 천장, observer mode(새 물리 가지를 더 밀지 않고 관측과 문헌을 지켜보는 상태)를
> 바꾸지 않습니다. 운영 규칙의 단일 진실 원천(SSOT, 기준 문서가 하나라는 뜻)은 이 문서가 아니라
> [.agent/workflows](../../../.agent/workflows/)입니다. 이 문서는 그 시스템을
> 설명할 뿐, 새 운영 규칙을 만들지 않습니다.

## 요약과 읽는 순서

[004 수치 스케치](004_rough_tanh_numerical_sketch_ko.md)와
[005 논문 보고서](005_rough_tanh_thesis_report_ko.md)는 1단계의 엄격한 실험이 한계에 부딪힌 뒤, 손으로 그린 `tanh` 전이를 24개 체크포인트로 끝까지 밀어본 2단계 현상론 스케치입니다. 이 문서는 그 물리 스케치 자체가 아니라, 그 작업에 사용된 문서화,
검증, 회고 절차를 정리합니다. 초점은 물리 결론의 강도가 아니라, 문헌 조사, 자산 캐시,
수치 추출, 검증, 실패 기록을 저장소 안에서 어떻게 연결했는지에 있습니다.
여기서 자산 캐시는 논문 PDF, 그림, 데이터 파일을 다시 찾지 않아도 되게 저장해 둔 것을
뜻하고, 수치 추출은 그림 속 곡선이나 표를 CSV 같은 숫자 파일로 옮기는 일을 뜻합니다.

이 시스템은 AI가 맞을 것이라고 믿고 만든 장치가 아닙니다. 반대로 AI가 틀릴 수 있고,
사용자의 기대에 맞춰 과장할 수 있으며, 캐시에 없는 자료를 세상에 없는 자료로 착각할 수
있다는 전제에서 출발했습니다. 그래서 상태 기준, 문헌 자산, 검증 스크립트, 회고, 적대적
검토를 서로 분리했습니다. 이 레포에는 대화 내용뿐 아니라, 그 대화를 문서, 코드, 검증
절차로 옮긴 작업 기록이 남아 있습니다.

이 글은 먼저 전체 구조를 짚고, 그 다음 상태 기준점, 운영 워크플로, 문헌 자산 파이프라인,
실행 루프, 검증 게이트, 회고 규율 순서로 내려갑니다. 이 문서에서 말하는 운영 절차는
AI에게 더 많은 자유를 주기 위한 것이 아니라, 성급한 긍정 판단이나 논리 점프를 줄이기
위해 문서와 코드에 제한을 둔 방식입니다.

## 1. 전체 구조: 다섯 역할

전체 시스템은 다섯 역할로 나뉩니다.

| 층 | 담당 | 실제 장치 |
| --- | --- | --- |
| 질문 조율 | 사람이 질문, 범위, 금지 조건, 검토 기준을 정합니다. | Codex 주력, Claude Code·Gemini 보조 검토 |
| 운영 규칙 | 무엇을 어디에 두고 무엇을 주장하면 안 되는지 고정합니다. | 운영 워크플로 |
| 실행 루프 | 독립 작업은 병렬로 진행하고, 공유 파일은 직렬로 통합합니다. | 병렬 fan-out(일을 여러 갈래로 나눔), worktree 격리(작업 공간 분리), 원자적 커밋(한 번에 한 묶음만 기록) |
| 검토 루프 | 긍정 주장마다 반례와 과대주장을 먼저 찾습니다. | 적대적 검토 프롬프트, known-model distinction(이미 알려진 모델과 같은지 비교) 확인 |
| 결정론적 게이트 | 파일 조건을 코드로 검사하고 실패하면 커밋을 중단합니다. | 문서 검증기, 커밋 게이트, 회귀 테스트 |

이 구조가 막으려 한 실패 모드는 다섯 가지입니다.

- **상태 드리프트:** 문서마다 현재 상태를 다르게 말하는 문제입니다. 예를 들어 [README.md](../../../README.md), [AGENTS.md](../../../AGENTS.md),
  [로드맵](../../05_next_steps/000_roadmap.md)이 서로 다른 상태를 말하는 문제입니다.
- **캐시 false-negative:** 로컬 캐시에 없다는 이유로 문헌 자체가 없다고 말하는 문제입니다. 쉽게 말하면
  "내 서랍에 없으니 세상에도 없다"고 착각하는 경우입니다.
- **파서 오판:** PDF가 Markdown으로 변환됐다는 이유로 논문을 충분히 확인했다고 보는
  문제입니다.
- **긍정 주장 과대화:** 타이밍이나 곡선 모양이 닮았다는 이유로 물리 증거처럼 쓰는
  문제입니다.
- **회고 없는 실패:** 막힌 지점을 기록하지 않아 다음 세션이 같은 실수를 반복하는
  문제입니다.

이 문서에서는 이 묶음을 에이전트 운영 절차라고 부릅니다. 여기서 절차란 AI가 할 일을
규칙, 파일, 검증 스크립트, 커밋 단위로 제한해 둔 구조를 뜻합니다.

## 2. 상태 기준점과 세션 메모리

이 구조의 출발점은 "어떤 파일이 어떤 판단을 책임지는가"를 분리한 데 있습니다. 목적은
관리 체계를 크게 만드는 것이 아니라, AI가 어디까지 말할 수 있고 어디서 멈춰야 하는지를
파일 구조로 제한하는 것이었습니다.

[AGENTS.md](../../../AGENTS.md)는 프로젝트를 대표하는 선언문이라기보다 AI 행동 규율에
가깝습니다. 이 파일은 QFUDS가 확정 이론이 아니며, 목적은 QFUDS를 보호하는 것이 아니라
더 강한 테스트를 견디는지 확인하는 것이라고 명시합니다. 즉 AI가 사용자의 기대에 맞춰
과도하게 칭찬하거나, 약한 결과를 강한 물리 결론으로 끌어올리거나, 이름 붙이기를 유도처럼
말하지 않도록 제한하는 기준입니다.

이 규율은 문체보다 판단 기준에 가깝습니다. AI가 "그럴듯하다"는 이유로 모델을
살려 두거나, 실험 범위를 넘어선 주장을 하지 않도록 합니다. 예를 들어
background-only 결과(우주의 전체 팽창만 본 결과)는 perturbation stability(작은 밀도 흔들림이
안정한지), CMB viability(우주배경복사 관측과 맞는지), matter-power viability(은하 분포
크기별 통계와 맞는지)로
읽히면 안 됩니다. 문헌에서 비슷한 timing이나 곡선 모양을 찾았다고 해서 QFUDS support로
올릴 수도 없습니다. `derived`, `implemented`, `tested`, `survived`, `failed`, `unknown`을
구분하라는 규칙도 같은 목적입니다. AI가 연구 보조자로서 할 수 있는 말과 아직 못 하는 말을
분리해 둔 것입니다.

이런 규칙을 사람이 매번 말로 다시 지시하면 세션마다 흔들립니다. 그래서 [AGENTS.md](../../../AGENTS.md)에
반복 규율을 고정했습니다. 그 결과 새 에이전트는 먼저 "QFUDS를 증명하는 것이 아니라
죽일 수 있는지 확인한다"는 기준에서 출발합니다. 이 기준은 이후의 문헌 조사, 수치화,
결과 해석이 사용자의 기대나 모델의 호의적 해석 쪽으로 기우는 것을 줄이기 위한 것입니다.

[CLAUDE.md](../../../CLAUDE.md)는 별도 상태나 별도 연구 규칙을 들고 있지 않습니다.
Claude 계열 도구가 들어오면 먼저 [AGENTS.md](../../../AGENTS.md)를 읽고,
현재 상태는 [로드맵](../../05_next_steps/000_roadmap.md)을 보게 하는 진입 문서입니다.
Codex 작업에서는 [AGENTS.md](../../../AGENTS.md)가 레포 단위 작업 규율로 들어오므로,
Claude와 Codex가 서로 다른 시작 규칙을 들고 작업하지 않게 됩니다. 관리해야 할 규칙을
여러 파일에 흩뿌리지 않고, 같은 규율과 같은 로드맵을 바라보게 한 구조입니다.

초기 구조의 문제는 "상태를 아는 문서가 너무 많다"였습니다. [README.md](../../../README.md),
[PROJECT.md](../../../PROJECT.md), [AGENTS.md](../../../AGENTS.md),
[CLAUDE.md](../../../CLAUDE.md)가 현재 레벨이나 완료 여부를 조금씩 반복해서 말하면,
어느 문서를 먼저 읽었는지에 따라 에이전트가 서로 다른 상태에서 출발할 수 있었습니다.
그래서 문제를 "문서를 더 친절하게 쓰기"가 아니라 "상태를 말하는 파일을 하나로 줄이고,
나머지는 그 파일을 가리키게 만들기"로 정의했습니다.

정리 방식은 다음과 같습니다. 현재 레벨, blocker(지금 막힌 지점), 다음 gate(다음에 통과해야
하는 관문)는
[로드맵](../../05_next_steps/000_roadmap.md)만 말합니다. 반복 운영 절차는
[.agent/workflows](../../../.agent/workflows/)로 분리했습니다. workflow는 "작업할 때 어떤
순서로 확인할지 적어 둔 절차서"입니다. 사람이 읽는 연구 기록과
증거는 [docs](../../) 아래에 둡니다. 그리고
[scripts/research_consistency.py](../../../scripts/research_consistency.py)가 이 구조를
다시 검사합니다. 로드맵이 인용한 실험·결과·decision log 근거가 실제 파일로 있는지
확인하고, [README.md](../../../README.md), [PROJECT.md](../../../PROJECT.md),
[AGENTS.md](../../../AGENTS.md), [CLAUDE.md](../../../CLAUDE.md)가 독립적인 레벨·상태
줄을 만들면 실패시킵니다.

따라서 이 구조는 문서 정리와 검증 규칙을 함께 둔 형태입니다. "AI가 어디를 읽고,
어떤 기준으로 답하고, 작업 후 무엇으로 검산되는가"를 한 방향으로 묶었습니다. 진입점은
[AGENTS.md](../../../AGENTS.md)와 [CLAUDE.md](../../../CLAUDE.md)로 정리하고, 현재 상태는
[로드맵](../../05_next_steps/000_roadmap.md)에만 두고, 절차는
[.agent/workflows](../../../.agent/workflows/)로 보내고, 마지막에는
[scripts/research_consistency.py](../../../scripts/research_consistency.py)가 상태 불일치를 잡습니다.
AI의 판단을 신뢰해서 만든 구조가 아니라, AI 판단이 흐트러질 때 파일과 코드가 다시 좁혀
주도록 만든 구조입니다.

이 구조에서 AI는 [AGENTS.md](../../../AGENTS.md)에서
과학적 태도와 금지선을 읽고, [로드맵](../../05_next_steps/000_roadmap.md)에서 현재 상태를
확인하고, [.agent/workflows](../../../.agent/workflows/)에서 절차를 찾습니다. 작업 뒤에는
검증 코드가 그 구조를 다시 점검합니다. 세션 메모리는 채팅 로그가 아니라 **문서 구조와
그 구조를 검사하는 코드**에 남습니다.

## 3. 운영 워크플로

[.agent/workflows](../../../.agent/workflows/)는 반복 가능한 절차를 다섯 개 워크플로로 나눕니다.
워크플로는 요리 순서표처럼, 작업을 시작하기 전에 무엇을 먼저 확인하고 어디에 결과를
남길지 정한 문서입니다.

| 워크플로 | 맡는 일 |
| --- | --- |
| [documentation-folder-routing-workflow](../../../.agent/workflows/documentation-folder-routing-workflow.md) | 문서를 기능에 따라 어느 폴더에 둘지, 연구 결과가 roadmap·lineage·governance로 전파될지 결정합니다. |
| [wiki-maintenance-workflow](../../../.agent/workflows/wiki-maintenance-workflow.md) | wiki 인덱스·레코드 유지, 재사용 가능한 질의 답변 적재, 위키 상태 점검을 담당합니다. |
| [research-asset-product-workflow](../../../.agent/workflows/research-asset-product-workflow.md) | 외부 논문·PDF·arXiv 소스·보충자료·데이터셋의 가용성과 제품 상태를 먼저 기록합니다. |
| [research-asset-digitization-workflow](../../../.agent/workflows/research-asset-digitization-workflow.md) | 캐시한 자산을 Markdown, 그림, CSV 후보로 디지털화하는 절차를 정의합니다. |
| [research-investigation-result-routing-workflow](../../../.agent/workflows/research-investigation-result-routing-workflow.md) | 산출물을 assets, plans, conclusions로 나누고 blocker 상태를 결론 문서에 남깁니다. |

이 워크플로는 체크리스트보다 선후 관계에 가깝습니다.
데이터·문헌 연구에서는 산출물 유무, 추출 완료, 커버리지 충분성을 말하기 전에
[research-asset-product-workflow](../../../.agent/workflows/research-asset-product-workflow.md)를
적용해야 합니다. 위키 인덱스나 디렉터리 구조를 바꾸기 전에는
[wiki-maintenance-workflow](../../../.agent/workflows/wiki-maintenance-workflow.md)와
[documentation-folder-routing-workflow](../../../.agent/workflows/documentation-folder-routing-workflow.md)를
확인해야 합니다. 자산을 디지털화해 산출물을 만들면
[research-investigation-result-routing-workflow](../../../.agent/workflows/research-investigation-result-routing-workflow.md)를
통해 그 산출물이 무엇을 바꾸었고 무엇을 바꾸지 않았는지 결론 문서에 남겨야 합니다.

이 절차가 유지하는 경계는 다음 문장입니다.

```text
자산이 존재하는 상태는 물리적으로 적격인 상태가 아닙니다.
```

예를 들어 Chen Figure 5 CSV가 존재해도 그것만으로 candidate `X`(전이를 일으키는 실제 물리 대상),
`Q^nu`(에너지·운동량이 어떻게 오가는지 쓰는 수식), `delta Q`(그 오고감이 흔들릴 때의 변화),
Level 2B, QFUDS support가 생기지 않습니다. CSV는 자산 제품이고, 물리 입장은 별도의
입장 규칙을 통과해야 합니다. 이 차이를 문서 배치와 검증 절차가 계속 유지합니다.

폴더 구조도 주제가 아니라 역할로 나뉩니다.

| 위치 | 역할 |
| --- | --- |
| [docs/00_project](../../00_project/) | 프로젝트 정체성, 결정 기록, 규약, frontmatter convention |
| [docs/01_origin](../../01_origin/) | 아이디어 출처와 초기 역사 |
| [docs/02_theory](../../02_theory/) | 이론 노트, 모델 버전, 문헌상 위치 |
| [docs/03_experiments](../../03_experiments/) | 재현 가능한 실험 정의 |
| [docs/04_results](../../04_results/) | 결과, 진단, 적대적 결론 |
| [docs/05_next_steps](../../05_next_steps/) | 로드맵과 다음 gate |
| [docs/wiki/governance](../governance/) | admission rule, 가지 gate, missing-physics map |
| [docs/wiki/lineage](../lineage/) | 아이디어 계보, 가지 의존, 강등 provenance |
| [docs/wiki/research](../research/) | 외부 문헌, 조사, 캐시 자산 |
| [docs/wiki/postmortem](../postmortem/) | 회고와 재발 방지 기록 |
| [.agent/workflows](../../../.agent/workflows/) | 운영 규칙 SSOT |
| [scripts](../../../scripts/), [tests](../../../tests/), [outputs](../../../outputs/), [qfuds](../../../qfuds/) | 검증 코드, 회귀 테스트, 산출물, 모델 코드 |

이 문서도 같은 규칙을 따릅니다. 에이전트 시스템 자체를 설명하지만, 운영 규칙을 새로
만드는 문서가 아니라 아이디어 계보와 작업 provenance를 정리하는 문서이므로
[docs/wiki/lineage](../)에 놓입니다.

## 4. 문헌 자산 파이프라인

주요 구현 내용은 문헌 탐색을 자산 상태, 파싱 품질, 수치 추출, 결과 라우팅으로 나누어
기록한 것입니다.
파싱은 PDF나 데이터 파일을 컴퓨터가 읽을 수 있는 글과 구조로 바꾸는 일이고, 라우팅은
결과를 맞는 폴더와 맞는 문서로 보내는 일입니다.

```text
문헌 후보 탐색
  -> 캐시 상태 기록
  -> 원본 PDF / arXiv source / figure / release asset 보관
  -> PageIndex·MarkItDown 파서 라우팅
  -> figure 추출과 TeX 기반 매핑
  -> 수치화 또는 구조화 추출
  -> Source-X 결론 문서에 blocker 상태 기록
```

### 4.1 캐시 상태 사다리

[Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md)는
"있다/없다"를 한 줄로 끝내지 않습니다. 자산 상태를
다음처럼 가장 구체적인 상태로 기록합니다.

| 상태 | 의미 |
| --- | --- |
| `not searched` | 아직 검색하지 않았습니다. |
| `searched_no_hit` | 검색했지만 후보 출처를 찾지 못했습니다. |
| `hit_not_cached` | 출처는 찾았지만 로컬 캐시가 없습니다. |
| `asset_available_not_downloaded` | 받을 수 있는 자산이 있지만 아직 받지 않았습니다. |
| `asset_downloaded_not_extracted` | 저장소에 있지만 풀거나 파싱하지 않았습니다. |
| `asset_extracted_not_digitized` | 원문·그림·표는 추출했지만 수치화하지 않았습니다. |
| `asset_digitized` | 그림·표 값을 디지털화했지만 연구 기준에 맞춰 판정하지 않았습니다. |
| `asset_cached` | 원본 자산과 매니페스트가 저장소에 보관돼 있습니다. |
| `inspected_no_numerical_product` | 확인했지만 기계적으로 재사용 가능한 수치 제품은 없었습니다. |
| `no_asset_found` | PDF, source, supplement, archive, table, code까지 확인한 뒤 관련 자산을 찾지 못했습니다. |
| `inaccessible` | 출처는 보이지만 접근하지 못했습니다. |

이 상태 사다리는 토큰과 fetch를 아끼는 캐시 전략이기도 하지만, 별도 역할은
false-negative를 줄이는 데 있습니다. **캐시에 없음**, **검색어가 좁아서 못 찾음**,
**문헌은 있지만 데이터 제품이 없음**, **문헌 자체가 없음**은 서로 다른 상태입니다. 이
구분이 없으면 RAG나 리서치 봇은 "내가 못 찾음"을 "세상에 없음"으로 잘못 말하기 쉽습니다.

### 4.2 PageIndex와 MarkItDown의 역할 분리

문서 파이프라인은 단순한 `PDF -> Markdown` 변환이 아니었습니다. 입력 종류에 따라
파서를 다르게 골랐습니다.

| 입력 | 기본 경로 | 이유 |
| --- | --- | --- |
| 논문 PDF | PageIndex | 페이지, 섹션, 수식, caption 구조가 중요합니다. |
| arXiv source / TeX | TeX 직접 확인 | Figure 번호와 원본 그림 파일 매핑의 ground truth입니다. |
| Zenodo README, JSON, release note | MarkItDown | 논문 본문이 아니라 매니페스트·표·코드 설명을 Markdown으로 바꾸는 데 적합합니다. |
| figure PDF / PNG | Poppler·ImageMagick | 수치화를 위해 고해상도 PNG를 렌더링해야 합니다. |

PageIndex는 논문 PDF를 페이지와 섹션 단위로 읽기 위한 MCP 도구입니다. MCP는 AI가 외부
도구를 호출할 수 있게 이어 주는 연결 방식입니다. [Research Asset Digitization Workflow](../../../.agent/workflows/research-asset-digitization-workflow.md)는
먼저 이미 적재된 문서를 `browse_documents`로 확인하고, 없으면 `process_document`로
적재한 뒤, `get_document_structure`로 섹션 구조를 받고 `get_page_content`로 페이지별
본문을 가져오라고 정합니다. MarkItDown은 데이터 릴리스, README, JSON, notebook처럼
논문 본문이 아닌 매니페스트성 자료를 Markdown 글로 바꾸는 데 더 적합했습니다.

[회고 005: 연구 자산 디지털화 자동화](../postmortem/005-20260611-dorito-research-asset-digitization-automation.md)는
이 분리를 만든 사건 기록입니다. 그 회고는 MarkItDown으로 논문 PDF 전문을 처리하면
2단 레이아웃, 수식, figure reference, caption 순서가 깨질 수 있다고 정리합니다.
반대로 PageIndex는 페이지·섹션 구조와 본문 chunk를 안정적으로 가져오는 데 유리했습니다.
다만 PageIndex도 figure 번호와 원본 파일명을 확정하는 최종 기준은 아니었습니다. 회고 005는
PageIndex caption 순서로 Amendola/Farrah figure mapping을 추정했다가 틀렸고,
arXiv TeX의 `\includegraphics`와 `\caption` block으로 교정했다고 기록합니다. Chen 논문처럼
TeX가 출판본보다 figure block을 더 많이 가진 draft superset일 때는 compiled PDF와 PageIndex
page context로 다시 대조해야 했습니다.

Figure 매핑도 별도 무결성 문제였습니다. PageIndex caption 순서만 믿으면 실제 Figure 번호와
파일명이 어긋날 수 있습니다. 그래서 arXiv TeX의 `\includegraphics`와 `\caption`을
ground truth로 삼고, source figure 수, 추출 PNG 수, 문서 안 참조 수를 대조했습니다. 저해상도
그림은 digitization 입력으로 부족하므로 고해상도 렌더링 기준도 세웠습니다.

### 4.3 Source-X plans 41~49 사례

Source-X는 "QFUDS의 물리 원인이 될 수 있는 외부 후보를 찾아보자"는 조사 이름입니다.
plans 41~49는 그 조사에서 실행한 작은 작업 묶음입니다. 여기서 구분할 점은
"숫자를 뽑았다"가 아니라 "숫자를 뽑았지만 물리 증거로 승격하지 않았다"입니다.

1. **후보 선정 (plan 041).** 캐시한 논문 중 먼저 수치화할 후보를 골랐습니다. 엔트로피
   쪽은 Chen 2026 병합 엔트로피 논문, 밀도 쪽은 Lacy 2024 블랙홀 논문이 선택됐습니다.
   이 선택은 QFUDS 지지가 아니라 수치 산출물 후보 선정이었습니다.
2. **구조화 추출 (plan 042-043).** 표, 식, 그림을 사람이 검토할 수 있게 정리했습니다.
   이 단계의 상태는 여전히 `data_product_blocked`였습니다.
3. **수치화 (plan 044-046).** Chen Figure 5의 색상별 곡선을 분리하고, 축 보정까지 거쳐
   432줄짜리 CSV(`numeric_digitized`)로 복원했습니다. CSV에는 `z`, `a`, `ln_a`, value,
   curve id, band role, provenance가 기록됐습니다. 이 결과는
   [046 결과](../research/investigations/source_x/conclusions/046_chen_figure5_numeric_digitization_result.md)에
   남아 있습니다.
4. **`Gamma(a)` 대조 (plan 047).** `Gamma(a)`는 1단계 실험에서 남은 현상론 전이함수입니다.
   팽창 변수 `a`에 따라 암흑부문 전이가 언제 강해지는지 나타내는 곡선입니다. 047은 Chen의
   `S_BH(a)`와 `entropy_density(a)`를 이 곡선과 모양 수준에서만 대조했습니다. 일부
   timing-shape 유사성은 있었지만, peak가 더 이르고 late tail이 약했습니다. 따라서 이는
   QFUDS 증거가 아니라 제한된 comparator 기록입니다.
5. **known-model distinction (plan 048).** 다음으로 이 경로가 이미 알려진 모델을 다른 이름으로
   부른 것인지 확인했습니다. 비교 대상은 엔트로피 DE, horizon entropy,
   CCBH, IV/IDE, running vacuum, emergent-DE, structure-activation 계열과 구별되는지
   물었습니다. 답은 "아직 아니다"였습니다.
6. **observer mode 라우팅 (plan 049-050).** observer mode는 새 물리 가지를 열지 않고
   기다리며 관찰하는 상태입니다. 049는 Level 2B 입장 조건을 다시 물었고,
   다섯 항목이 모두 막혀 있음을 확인했습니다. 050은 forward route도 아직 최소 수학 객체가
   없어 `Gamma(a)` 유도가 불가능하다고 정리했습니다.

이 사례는 산출물 생성과 상태 경계 분리를 함께 기록한 예입니다. 파이프라인은 논문에서
CSV까지 산출물을 만들었지만, 상태 경계는 그 산출물을 물리 증거로 승격하지 않도록
유지했습니다.

### 4.4 baseline reference cache와 kill-map

Source-X가 observer mode로 닫힌 뒤에는 질문이 바뀌었습니다. "무엇이 QFUDS를 지지하는가"가
아니라, "앞으로 어떤 물리 가지가 나오더라도 먼저 맞아야 하는 표준 관측 문턱은 무엇인가"를
분리해야 했습니다. 그래서 [baseline_reference 조사](../research/investigations/baseline_reference/README.md)는
NASA/LAMBDA와 BAO 자료를 QFUDS evidence가 아니라 **baseline constraint source**로 라우팅했습니다.

이때도 같은 workflow가 적용됐습니다. [NASA/LAMBDA Graphic History cache closeout](../research/investigations/baseline_reference/conclusions/001_nasa_lambda_graphic_history_cache_closeout.md)은
[NASA/LAMBDA Graphic History 자산](../research/assets/nasa_lambda_graphic_history/README.md)을
`asset_cached`로 닫았습니다. 로컬 캐시는 20개 HTML page, 90개 figure/vector asset, 106개
page-level link record, 57개 data-reference row를 갖습니다. 하지만 이 숫자는 "자료를 실제로
가져왔다"는 운영 상태이지, 수치 likelihood나 QFUDS 지지 근거가 아닙니다.

그 다음 [effective foam assumption ledger 결과](../research/investigations/baseline_reference/conclusions/002_effective_foam_assumption_ledger_result.md)는
`xi ~= 10 Mpc`, transition width, amplitude를 데이터 확인 뒤에 고르면 순환논리라고 못박았습니다.
`xi`는 아직 물리적으로 유도된 길이가 아닙니다. 입력값인지, 출력값인지, 단순 coarse-grained
scale인지도 아직 확정되지 않았습니다. geometry side 수정인지 stress-energy side 수정인지도
분리해서 먼저 정해야 합니다.

마지막으로 [NASA + BAO baseline constraint map](../research/investigations/baseline_reference/conclusions/003_nasa_bao_baseline_constraint_map.md)은
NASA/LAMBDA의 CMB, `n_s`, 우주 나이, `tau`, `Omega_m`, `Omega_b h^2`, `Omega_c h^2`,
`sigma8`, `H0`, supernova 축과 DESI/eBOSS Ly-alpha BAO의 `z ~= 2.33` geometry 값을
kill-map으로 정리했습니다. retained timing이 할 수 있는 일은 좁습니다. `z ~= 2` 근처의
현상론적 timing fingerprint가 고적색편이 BAO 측정 영역과 닿는지 보는 정도입니다. retained
`Gamma(a)`는 여전히 IV/IDE comparator이고, `D_M/r_d`, `D_H/r_d`, CMB, matter power,
survey likelihood를 계산하지 못합니다.

따라서 baseline_reference 체인의 운영 결론은 다음입니다.

```text
NASA/LAMBDA와 BAO cache는 QFUDS evidence가 아니라 QFUDS가 맞아야 할 kill constraint입니다.
kill constraint를 보기 전에 xi, width, amplitude를 고르면 그 경로는 중단합니다.
```

## 5. 실행 방식: 병렬 작업, 검토, 직렬 통합

한 세션의 실행 패턴은 다음과 같습니다.

- **Append-only 기록.** append-only는 지우고 다시 쓰지 않고 아래에 계속 덧붙이는 방식입니다.
  각 체크포인트는 기존 기록을 지우지 않고 `CPn` 섹션, 스크립트,
  그림, CSV, 결론을 덧붙입니다.
- **원자적 커밋.** 하나의 체크포인트는 가능하면 하나의 커밋으로 묶습니다. 계산, 출력,
  문서 결론이 서로 떨어지지 않게 하기 위한 규칙입니다.
- **병렬 fan-out.** 서로 독립적인 계산이나 조사 작업은 병렬로 나눕니다. ISW, kill-test,
  점성, ceiling mechanism처럼 독립성이 있는 작업이 여기에 해당합니다.
- **직렬 통합.** 공유 파일, CP 번호, lineage 문서 append, git 커밋은 메인 에이전트가
  직렬로 통합합니다. 파일 충돌이 예상되는 작업은 git worktree로 격리합니다.
- **적대적 검토.** 긍정 주장에는 반례와 과대주장을 찾는 별도 검토 패스를 붙입니다.

여기서 적대적 검토는 특정 상주 에이전트 이름이 아닙니다. 결론을 바로 확정하지 않고,
같은 AI 작업 안에서 잠시 "이 결과를 깨려는 리뷰어" 역할을 가정하게 한 절차입니다. 예를
들어 "이 결론이 단순히 ΛCDM, IV/IDE, running vacuum 같은 기존 계열을 다른 이름으로
부른 것은 아닌가", "증거 파일이 실제로 있는가", "이 문장을 읽으면 Level 2B를 연 것처럼
보이지 않는가", "로드맵 상태를 바꿀 근거가 있는가"를 다시 묻게 했습니다.

이 절차가 필요한 이유는 긍정 결론이 가장 쉽게 과장되기 때문입니다. "유사하다"는 말은
금방 "지지한다"로 바뀌고, "현상론적으로 닫혔다"는 말은 금방 "물리적으로 유도됐다"로
읽힐 수 있습니다. 그래서 검토 패스는 결론을 좋게 다듬는 단계가 아니라, 결론의 강도를
낮출 이유를 먼저 찾는 단계였습니다. 특히 다음 네 가지를 반복해서 확인했습니다.

- **동일성 질문:** 이 결과가 LCDM, unified dark fluid, IV/IDE, running vacuum, entropic
  dark energy 같은 기존 계열로 흡수되는가?
- **증거 질문:** 결과 문서, 실험 문서, 출력 파일, decision log, 로드맵 근거가 실제로
  존재하는가?
- **범위 질문:** background-only, proxy scan, source comparison 같은 약한 작업을
  perturbation, CMB, matter-power 검증처럼 말하고 있지 않은가?
- **상태 질문:** 이 문장이 roadmap update, Level 2B admission, candidate `X`, `Q^nu`,
  `delta Q` 도출처럼 읽히지 않는가?

검토 방식도 단순했습니다. 먼저 메인 작업이 결론 초안을 만들고, 그 다음 같은 세션에서
적대적 리뷰어 역할을 가정한 프롬프트로 결론을 다시 읽습니다. 이때 리뷰어 역할은 "좋은
표현을 찾아라"가 아니라 "이 결론을 기각하거나 낮춰야 할 이유를 찾아라"에 가깝습니다.
그 결과 과한 문장이 나오면 `support`, `derive`, `survive`, `pass` 같은 말을 더 좁은
표현으로 바꾸고, 필요한 경우 `provenance`, `comparator`, `blocked`, `not admitted`,
`unknown` 같은 상태로 낮췄습니다.

이 검토는 프롬프트만으로 끝나지 않았습니다. 검토 뒤에는
[scripts/validate_docs.py](../../../scripts/validate_docs.py),
[scripts/research_consistency.py](../../../scripts/research_consistency.py),
[scripts/preflight_exp004.py](../../../scripts/preflight_exp004.py), `git diff --check`를
돌려서 문서 형식, 상태 기준, 실험 기록, 공백 오류를 확인했습니다. 즉 적대적 검토는
"비판적으로 생각해 봤다"는 태도가 아니라, 반례 질문과 결정론적 검사를 한 세트로 묶은
운영 절차였습니다.

이 검토는 긍정 주장에 더 엄격하게 적용했습니다. 부정 결과나 제자리 결과는 과대주장 위험이
작지만, "줄였다", "유도했다", "통과했다" 같은 표현은 곧바로 물리 주장처럼 읽힐 수
있습니다. 그래서 긍정 문장에는 "무엇을 통과했는가", "어떤 강도의 테스트인가", "어디까지
아직 unknown인가"를 붙여 다시 봤습니다. [005 §2.4](005_rough_tanh_thesis_report_ko.md)는
이 과정에서 과대주장 세 건을 실제로 잡아낸 기록입니다.

실행 프롬프트에도 같은 규칙을 반복해서 넣었습니다. "roadmap SSOT를 지켜라", "Level 2B를
열지 마라", "타이밍 겹침을 증거로 치지 마라", "인용을 지어내지 마라", "캐시 공백과 실제
증거 공백을 구분하라" 같은 지시가 계속 들어갔습니다. 그래서 안전장치는 프롬프트의 역할
지정, 적대적 검토 질문, 코드 검증의 세 겹으로 작동했습니다.

이 절차의 역할은 검토 질문을 반복 가능하게 만드는 데 있었습니다. AI에게 "더 비판적으로
봐라"라고만 말하면 결과가 흔들립니다. 반대로 어떤 질문을 해야 하는지, 어떤 상태 승격을
막아야 하는지, 어떤 파일이 없으면 실패인지 정해 두면 같은 검토를 다시 수행할 수 있습니다.
이 문서에서 말하는 적대적 검토는 이 반복 가능한 검토 역할입니다.

## 6. 검증 게이트: 커밋 단계 검사

이 시스템에서 검증은 권장 체크리스트가 아닙니다. 커밋 경로에 자동으로 걸린 검사입니다.
사람이 마지막에 다음 명령을 직접 실행해 확인할 수도 있지만, 같은 순서가 git pre-commit 훅에도
들어 있습니다.

```text
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/agent_workflow_guard.py --staged
python3 scripts/preflight_exp004.py
git diff --check
```

[scripts/git-hooks/pre-commit](../../../scripts/git-hooks/pre-commit)이 저장소에 보관된 표준 훅이고,
로컬 git이 실제로 실행하는 설치본은 [.git/hooks/pre-commit](../../../.git/hooks/pre-commit)입니다.
훅은 `set -eu`로 시작합니다. 그래서 중간 명령 하나라도 0이 아닌 종료 코드를 반환하거나, 정의되지
않은 변수를 사용하면 shell이 즉시 멈추고 커밋이 실패합니다. 종료 코드는 프로그램이 끝나며
"문제 없음" 또는 "문제 있음"을 알려 주는 숫자입니다. 이 때문에 검증 스크립트는 단순한
리포트 생성기가 아니라 커밋 여부에 영향을 주는 검사기입니다.

검사 장치는 두 층으로 나뉩니다.

- **하드 검사.** Python 검증기와 git pre-commit 훅이 실제 파일을 검사합니다. 실패하면
  커밋이 중단됩니다.
- **소프트 제한.** [AGENTS.md](../../../AGENTS.md), 실행 프롬프트, 한국어 스타일 리마인더
  훅이 모델의 행동을 제한합니다. 다만 모델이 따르지 않으면 깨질 수 있습니다.

문서·상태 정합성은 하드 검사에 둡니다. 상태 기준이 roadmap 하나인지, 완료 주장에 근거
문서가 있는지, 실험·결과 문서가 짝을 이루는지, frontmatter가 맞는지는 스크립트가 검사합니다.
여기서 "증거"는 LLM이 납득했다는 뜻이 아닙니다. frontmatter, 필수 섹션, 링크, 출력 파일,
결과 문서, 로드맵 SSOT와의 대응처럼 파일로 확인되는 조건을 뜻합니다.

[scripts/git-hooks/pre-commit](../../../scripts/git-hooks/pre-commit)은 다음 순서로 검사합니다.

```text
staged Markdown 문서의 last_updated 자동 갱신
  -> staged 연구 문서의 외부자료 workflow marker와 state token 검사
  -> 문서 frontmatter, H1, 링크, 실험·결과 문서 형식 검사
  -> 로드맵 SSOT와 독립 상태 주장 불일치 검사
  -> exp_003 이후 기록 정합성 및 성급한 물리 완료 주장 검사
  -> 공백 오류 검사
  -> qfuds 또는 tests 변경 시 수치 회귀 테스트
```

[scripts/update_frontmatter_last_updated.py](../../../scripts/update_frontmatter_last_updated.py)는
pre-commit에서 제일 먼저 실행됩니다. 이 스크립트는 staged 상태의 Markdown 파일만 대상으로
잡고, 파일에 YAML frontmatter와 `last_updated` 필드가 있을 때만 날짜를 오늘로 바꿉니다.
staged는 "이번 커밋에 넣겠다고 골라 둔 상태"입니다. YAML frontmatter는 문서 맨 위에 붙는
이름표 묶음입니다. 부분 staging 된 파일은 거부합니다. 같은 파일에 staged 변경과 unstaged 변경이 섞여 있으면
자동 수정이 사용자의 의도와 다른 조각까지 섞어 넣을 수 있기 때문입니다. 날짜를 바꾼 뒤에는
해당 파일을 다시 `git add`해서 실제 커밋 대상도 갱신합니다. 원자료 성격의 일부 source 자산은
업스트림 스냅샷일 수 있으므로 건너뜁니다.

[scripts/validate_docs.py](../../../scripts/validate_docs.py)는 문서 하나하나의 구조를 검사합니다.
모든 Markdown 문서에서 YAML frontmatter를 파싱하고, 필수 필드인 `doc_id`, `title`, `doc_type`,
`stage`, `status`, `evidence_role`, `depends_on`, `next_gate`, `last_updated`가 있는지 확인합니다.
`doc_type`, `stage`, `status`, `evidence_role`은 코드 안의 허용 목록과 비교합니다. 본문의 첫 H1은
frontmatter의 `title`과 같아야 합니다. H1은 Markdown에서 `# 제목`으로 쓰는 가장 큰 제목입니다.
`doc_id`는 저장소 안에서 중복될 수 없습니다. 실험 문서와
결과 문서에는 목적, 가설, 범위, 실패 기준, 출력, 결정 같은 필수 절이 있어야 합니다. 활성 stage
문서 폴더에서는 파일명이 `000_`, `010_`, `015_`, `020_`, `030_`, `040_`, `900_` 같은 정렬 prefix를
가져야 합니다.

같은 스크립트는 링크 형식도 검사합니다. 본문에서 실제로 존재하는 Markdown 파일 경로가 그냥
텍스트로 노출되면 실패시키고, 클릭 가능한 Markdown 링크로 쓰게 합니다. 예를 들어 이 문서가
[frontmatter 규약](../../00_project/frontmatter_convention.md)을 설명할 때 경로를 일반 텍스트로
박아 두면 실패합니다. 문서가 독립적으로 읽혀야 한다는 요구를 코드로 옮긴 것입니다. 독자는
설명을 읽다가 근거 파일로 바로 이동할 수 있어야 하고, 검증기는 그 최소 형식을 확인합니다.

[scripts/research_consistency.py](../../../scripts/research_consistency.py)는 문서 사이의 상태 불일치를
잡습니다. 이 스크립트는 [로드맵](../../05_next_steps/000_roadmap.md)을 상태 SSOT로 보고, 로드맵이
인용한 [docs](../../), [outputs](../../../outputs/), [tests](../../../tests/),
[qfuds](../../../qfuds/), [scripts](../../../scripts/) 경로가 실제로 존재하는지 검사합니다. 완료된
experiment/result 쌍이 [decision log](../../00_project/decision_log.md)에 기록됐는지도 확인합니다.
또 [AGENTS.md](../../../AGENTS.md), [CLAUDE.md](../../../CLAUDE.md),
[README.md](../../../README.md), [PROJECT.md](../../../PROJECT.md),
[overview](../../00_project/overview.md)가 로드맵을 참조하는지 보면서, 이 문서들이 별도의 상태표가
되지 않게 합니다. 본문에서 `Level`과 `completed`, `blocked`, `active`, `current` 같은 상태 단어가
한 줄에 묶여 독립 상태 선언처럼 보이면 오류로 잡습니다. 결론은 단순합니다. 현재 레벨과 blocker는
로드맵만 말할 수 있고, 다른 문서는 그 위치를 가리킬 수만 있습니다.

[scripts/preflight_exp004.py](../../../scripts/preflight_exp004.py)는 이름과 달리 새 물리 계산을 돌리는
스크립트가 아닙니다. exp_003 이후 기록이 서로 맞는지 확인하는 연구 기록 게이트입니다.
[exp_003 이론 문서](../../02_theory/030_qfuds_phenomenological_perturbations.md),
[exp_003 실험 문서](../../03_experiments/030_exp_003_phenomenological_perturbation_closure.md),
[exp_003 결과 문서](../../04_results/030_result_003_phenomenological_perturbation_closure.md),
[decision log](../../00_project/decision_log.md), [로드맵](../../05_next_steps/000_roadmap.md),
[docs index](../../README.md), [outputs](../../../outputs/) 참조가 서로 맞는지 확인합니다.
구체적으로는 exp_003의 P2 fail, P1 survival, friction correction, Level 2A 완료, Level 2B 이후
blocker가 결정 문서와 로드맵에 같이 남아 있는지 봅니다. 반대로 Level 3, CLASS, CMB, matter-power
완료처럼 아직 허용되지 않은 강한 주장이 문서에 나오면 정규식으로 오류 처리합니다. 즉 이 스크립트는
수치 결과를 새로 만드는 코드가 아니라, 수치 결과와 문서 결론이 서로 다른 방향으로 새는 것을
검사하는 코드입니다.

[scripts/agent_workflow_guard.py](../../../scripts/agent_workflow_guard.py)는 2026-06-17에
추가된 연구 workflow 강제 게이트입니다. 이 스크립트는 staged Markdown 문서에서 URL,
arXiv, DOI, NASA/LAMBDA, BAO, DESI/eBOSS, PDF, source bundle, downloadable asset,
page-family resource, product-availability claim 같은 신호를 찾습니다. 그런 신호가 있으면
문서 안에 [Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md)
표시와 state token이 함께 있어야 합니다. state token은 `hit_not_cached`,
`asset_available_not_downloaded`, `asset_cached`, `inspected_no_numerical_product`,
`no_asset_found`, `inaccessible`처럼 workflow state ladder에서 온 값입니다.

이 게이트가 막으려는 오류는 간단합니다. 에이전트가 외부 웹이나 논문을 본 뒤
"자료 없음", "제품 없음", "캐시 완료", "coverage 확인"이라고 말하면서도 실제로 어떤
workflow 상태까지 갔는지 남기지 않는 경우입니다. 예를 들어 NASA/LAMBDA page-family
URL을 열어 sibling page와 figure/table asset을 추론할 수 있는데, 그 추론 범위와 캐시 상태를
문서에 남기지 않으면 다음 세션은 "못 찾은 것"과 "없는 것"을 구분할 수 없습니다. 그래서
이제 외부자료 claim은 state token 없이 커밋되지 않습니다.

이 변경은 운영 규칙을 한 단계 올린 것입니다. 이전에는
[.agent/workflows](../../../.agent/workflows/)를 읽으라는 규칙이 AGENTS/CLAUDE 진입 문서와
프롬프트에 주로 의존했습니다. 지금은 같은 규칙이
[AGENTS.md](../../../AGENTS.md), [CLAUDE.md](../../../CLAUDE.md),
[Agent Workflow Enforcement Design](../governance/005_agent_workflow_enforcement_design.md),
[scripts/git-hooks/pre-commit](../../../scripts/git-hooks/pre-commit), [Makefile](../../../Makefile)에
연결됩니다. 따라서 Codex와 Claude Code가 서로 다른 prompt context에서 시작해도, staged
문서가 workflow marker와 state token을 빠뜨리면 같은 commit gate에서 멈춥니다.

`git diff --check`는 연구 의미를 해석하지 않습니다. trailing whitespace, conflict marker, 잘못된
공백 같은 패치 품질 문제를 잡습니다. 하지만 pre-commit 안에 함께 들어 있으므로, 이런 기계적
오류도 커밋을 중단시킵니다.

회귀 테스트는 항상 돌리지 않습니다. [회고 006: 느린 pre-commit 훅](../postmortem/006-20260611-dorito-precommit-regression-test-scope.md)에서
측정한 결과, 문서 검증 스크립트는 매우 빠르고 실제 병목은 수치 회귀 테스트였습니다. 그래서
문서만 고치는 커밋에서는 회귀 테스트를 건너뛰고, [qfuds](../../../qfuds/)나
[tests](../../../tests/)가 바뀌었을 때만 전체 테스트를 돌리도록 경로 범위 게이트를
만들었습니다. 실제 구현은 [scripts/git-hooks/pre-commit](../../../scripts/git-hooks/pre-commit)에
있습니다. 훅은 `git diff --cached --name-only --diff-filter=ACMR`로 staged 경로 목록을 얻고,
그 목록이 [qfuds](../../../qfuds/) 또는 [tests](../../../tests/)로 시작하거나 `RUN_TESTS=1`이 설정된 경우에만
`python3 -m unittest discover -s tests -p 'test_*.py'`를 실행합니다.

여기까지가 하드 게이트입니다. 이 경로에는 LLM 호출이 없습니다. Python 스크립트와 shell
조건문이 파일 상태를 검사할 뿐입니다.

LLM 쪽 개입은 별도 soft hook으로 분리돼 있습니다. [remind-korean-style.sh](../../../.claude/hooks/remind-korean-style.sh)는
사용자 turn 시작 때 한국어 문체 리마인더를 모델 context에 추가합니다.
[no-bak-slang-check.sh](../../../.claude/hooks/no-bak-slang-check.sh)와
[no-emoji-check.sh](../../../.claude/hooks/no-emoji-check.sh)는 쓰기 직전의 tool input을
검사해서 금지 표현이나 이모지를 발견하면 차단합니다. 이 훅들은 모델 행동을 유도하거나
쓰기 입력을 제한하는 장치이지, QFUDS 물리 결론을 판정하는 장치가 아닙니다. 물리·문서 상태
판정은 위의 pre-commit 게이트와 Python 검증기에 남아 있습니다.

연구 workflow용 soft hook도 같은 원칙입니다.
[research-workflow-reminder.py](../../../.agent/hooks/research-workflow-reminder.py)는 prompt에
research, literature, paper, arXiv, PDF, source, asset, cache, NASA, BAO 같은 신호가 있으면
workflow 적용을 떠올리게 하는 `UserPromptSubmit` reminder를 냅니다. Claude Code wrapper는
[remind-research-workflows.sh](../../../.claude/hooks/remind-research-workflows.sh)에 있고,
Codex wrapper는 [remind-research-workflows.sh](../../../.codex/hooks/remind-research-workflows.sh)에
있습니다. 다만 hook 등록은 host마다 다르므로, 이 reminder는 편의 장치입니다. 재발 방지의
강제력은 [scripts/agent_workflow_guard.py](../../../scripts/agent_workflow_guard.py)와
pre-commit gate에 있습니다.

이 구조는 사용자 기대에 맞춘 동조와 논리 점프를 줄이기 위해 사용됐습니다.
[AGENTS.md](../../../AGENTS.md)의 첫 원칙은 "동의보다 진실"입니다. 검증 게이트는 그
원칙을 파일 조건으로 옮깁니다. 에이전트가 "성공"이라고 쓰더라도, 증거 파일과 상태
기준이 맞지 않으면 커밋은 통과하지 못합니다.

## 7. 역할 분담

이 시스템은 단일 챗봇과의 대화가 아닙니다. 그렇다고 계획자, 작성자, 검토자가 코드상
클래스로 정의돼 있는 것도 아닙니다. 역할은 작업 모드로 나뉩니다.

- **사람 조율자.** 질문을 정하고, 범위를 좁히고, 금지 조건을 걸고, 결과를
  검토합니다. 특히 "로드맵 상태를 바꾸지 마라", "Level 2B를 열지 마라", "테스트를
  돌려라" 같은 지시가 반복적으로 들어갔습니다.
- **메인 에이전트.** 플랜을 만들고, 파일을 읽고, 작업을 쪼개고, 결과를 통합합니다.
- **작업 에이전트 패스.** 계산, 디지털화, 문서 윤문, 커버리지 감사처럼 독립적인 작업을
  맡습니다.
- **검토 패스.** 적대적 리뷰어를 가정하고 긍정 주장을 깨는 질문을 던집니다. known-model
  distinction과 상태 경계도 이때 다시 확인합니다.
- **결정론적 게이트.** 마지막에는 스크립트가 통과 여부를 판정합니다.

여러 AI도 함께 썼습니다. Codex를 주력으로 두고 Claude Code와 Gemini를 보조·교차검증에
사용했습니다. 모델 이름 자체보다, 한 모델의 누락 가능성을 다른 모델과 검증 게이트로
확인한 점이 중요했습니다.

프롬프트도 별도 산출물로 관리했습니다. 단계별 플랜, 실행 프롬프트, 영어 프롬프트,
한국어-영어 workplace 번역 프롬프트를 설계했습니다. 영어를 쓴 것은 단순 취향이 아니라
토큰 효율과 논문·코드 문맥 때문이었습니다. 코드, 로그, 스택트레이스, 경로, 식별자는
번역하지 않도록 규칙을 두었습니다. 대표 프롬프트는
[.agent/prompts](../../../.agent/prompts/README.md)에 보관돼 있습니다.

따라서 검토자는 특정 사람이나 상주 에이전트가 아닙니다. "이 결론을 반박하려면 어디를
봐야 하는가"를 묻는 프롬프트 패스와, 실제 파일 조건을 확인하는 결정론적 스크립트를 합친
역할입니다. 그래서 결과를 옹호하는 방향으로 기울 여지가 줄어듭니다.

## 8. 회고 규율

주요 사건마다 회고를 append-only로 남겼습니다. 회고는
[docs/wiki/postmortem](../postmortem/)에 쌓입니다. 회고의 목적은 감상문이 아니라
재발 방지입니다. 무엇이 잘못됐는지, 어떤 가설을 세웠는지, 무엇을 측정했는지, 어떤 규칙이
생겼는지를 남깁니다.

회고 작성도 표준화했습니다. [postmortem skill](../../../.agents/skills/postmortem/SKILL.md)은
시퀀스 번호, YAML frontmatter, `audit_log`, `relations`, `code_refs`를 요구합니다. 즉
회고도 그냥 작성하지 않고, 나중에 검색·검증·참조할 수 있는 형태로 남깁니다.

| seq | 주제 |
| --- | --- |
| 001 | [Li 2025 데이터 캐시](../postmortem/001-20260609-dorito-li-2025-data-cache.md) |
| 002 | [IV/IDE 타이밍 체크포인트](../postmortem/002-20260609-dorito-iv-ide-timing-checkpoint.md) |
| 003 | [QFUDS 스코프 강등 회고](../postmortem/003-20260610-dorito-qfuds-scope-demotion-retrospective.md) |
| 004 | [Source-X 데이터 산출물 감사](../postmortem/004-20260610-dorito-source-x-data-product-audit.md) |
| 005 | [연구 자산 디지털화 자동화](../postmortem/005-20260611-dorito-research-asset-digitization-automation.md) |
| 006 | [pre-commit 회귀 테스트 스코프](../postmortem/006-20260611-dorito-precommit-regression-test-scope.md) |
| 007 | [Source-X 산출물 라우팅 워크플로](../postmortem/007-20260611-dorito-source-x-product-routing-workflow.md) |
| 008 | [Source-X 진행 체크포인트](../postmortem/008-20260611-dorito-source-x-progress-checkpoint.md) |
| 009 | [QFUDS observer mode 종결 회고](../postmortem/009-20260611-dorito-qfuds-observer-mode-closing-retro.md) |
| 010 | [rough tanh lineage 하강 회고](../postmortem/010-20260612-dorito-rough-tanh-lineage-descent-retro.md) |
| 011 | [rough tanh lineage 자연 닫힘 회고](../postmortem/011-20260612-dorito-rough-tanh-lineage-natural-closing-retro.md) |
| 012 | [QFUDS 수식 검산과 문서 정합성 감사 회고](../postmortem/012-20260613-dorito-qfuds-math-doc-audit.md) |
| 013 | [에이전트 연구 workflow 강제 게이트 회고](../postmortem/013-20260617-dorito-agent-research-workflow-guard.md) |

회고는 이후 워크플로와 스크립트 변경의 근거로 사용됐습니다. 001은 PDF/source asset을 캐시하지 않은 채 문헌을 확인했다고
말하는 문제를 잡았고, 005는 PageIndex와 MarkItDown의 역할 차이, TeX 기반 figure mapping,
고해상도 rendering 기준을 정리했습니다. 006은 pre-commit 병목을 측정해 경로 범위 테스트
전략으로 바꿨습니다. 이 기록들이 이후 [.agent/workflows](../../../.agent/workflows/)와
[scripts](../../../scripts/)로 굳어졌습니다.

## 9. 무엇이 검증됐고 무엇이 아닌가

이 문서가 다루는 것은 물리 발견이 아니라 운영 방식입니다. 여기서 확인된 것은
"QFUDS가 맞다"가 아니라, 검증되지 않은 아이디어를 문헌 자산, 수치 제품, 상태 경계,
known-model distinction, baseline constraint, 회고로 나누어 다룬 방식입니다. 특히
baseline_reference 체인은 NASA/LAMBDA와 BAO 자료를 관측 문턱으로 정리하되, 그 문턱을
QFUDS support로 쓰지 않도록 막았습니다.

반대로 다음은 검증되지 않았습니다.

- foam sector(이 프로젝트가 가정한 미시적인 거품 부문)가 실제 물리적 암흑부문 source라는
  점은 검증되지 않았습니다.
- Chen Figure 5가 `Gamma(a)`(암흑부문 전이가 시간에 따라 얼마나 강한지 나타내는 함수)의
  물리 원인이라는 점은 검증되지 않았습니다.
- `Q^nu`, `delta Q`, candidate `X`는 도출되지 않았습니다.
- `xi ~= 10 Mpc`는 물리적으로 유도되지 않았고, 입력인지 출력인지도 확정되지 않았습니다.
- Level 2B admission(물리 섭동 단계로 들어가는 입장 허가)은 열리지 않았습니다.
- CMB, matter power, survey likelihood 검증은 완료되지 않았습니다.
- NASA+BAO baseline map은 likelihood 구현이 아니며, `D_M/r_d`, `D_H/r_d`, CMB, matter
  power를 계산하는 QFUDS 모델을 만들지 않았습니다.

[049 Level 2B 입장 적격성 검토](../research/investigations/source_x/conclusions/049_level2b_eligibility_review_and_observer_mode.md)와
[050 foam-sector-to-Gamma 유도 가능성 결과](../research/investigations/source_x/conclusions/050_foam_sector_to_gamma_derivation_feasibility_result.md)도
이 경계를 유지합니다. 049는 현재 black-hole entropy / Chen-Gamma lane이 candidate `X`,
`Q^nu`, phase-B `w ~= -1` 근거, `delta Q` route, known-model distinction을 모두
채우지 못했으므로 Level 2B에 부적격하다고 판정하고 observer mode로 라우팅한 문서입니다.
050은 별도 질문을 다룹니다. retained `Gamma(a)`에서 뒤로 추정하는 길이 아니라, foam sector
상태 변수에서 출발해 `Gamma(a)` 같은 전이 profile을 앞으로 유도할 수 있는지 보았고,
foam-sector state variable, phase A/B 계산 정의, 대체 transition object, 최소 방정식 세트가
아직 없다고 정리했습니다. [Source-X 조사 인덱스](../research/investigations/source_x/README.md)는
049와 050을 읽는 순서와 두 문서가 Level 2B를 열지 않는다는 경계를 함께 설명합니다. 이 문서는
그 상태를 바꾸지 않습니다.

[effective foam assumption ledger](../research/investigations/baseline_reference/conclusions/002_effective_foam_assumption_ledger_result.md)와
[NASA + BAO baseline constraint map](../research/investigations/baseline_reference/conclusions/003_nasa_bao_baseline_constraint_map.md)도
같은 결론을 유지합니다. 전자는 `xi`, width, amplitude를 관측 뒤에 고르는 경로를
순환논리로 중단시키고, 후자는 NASA/LAMBDA와 DESI/eBOSS Ly-alpha BAO를 관측 kill-map으로만
사용합니다. 두 문서 모두 Level 2B를 열지 않고, retained timing을 물리 QFUDS로 승격하지 않습니다.

이 문서의 결론은 다음으로 제한됩니다.

```text
이 프로젝트의 물리 결론은 아직 막혀 있습니다.
이 프로젝트의 운영 절차는 막힌 지점을 문서와 검증 절차로 분류했습니다.
```

## 부록: 참조

- 운영 규칙 SSOT: [.agent/workflows](../../../.agent/workflows/)
- 결정론적 게이트: [scripts/git-hooks/pre-commit](../../../scripts/git-hooks/pre-commit),
  [Makefile](../../../Makefile), [scripts/agent_workflow_guard.py](../../../scripts/agent_workflow_guard.py),
  [scripts](../../../scripts/)
- 문서 검증 코드: [scripts/validate_docs.py](../../../scripts/validate_docs.py),
  [scripts/research_consistency.py](../../../scripts/research_consistency.py),
  [scripts/preflight_exp004.py](../../../scripts/preflight_exp004.py)
- LLM soft hook: [.claude/hooks/remind-korean-style.sh](../../../.claude/hooks/remind-korean-style.sh),
  [.claude/hooks/no-bak-slang-check.sh](../../../.claude/hooks/no-bak-slang-check.sh),
  [.claude/hooks/no-emoji-check.sh](../../../.claude/hooks/no-emoji-check.sh),
  [.agent/hooks/research-workflow-reminder.py](../../../.agent/hooks/research-workflow-reminder.py)
- workflow enforcement 설계: [Agent Workflow Enforcement Design](../governance/005_agent_workflow_enforcement_design.md)
- 회고 로그: [docs/wiki/postmortem](../postmortem/)
- Source-X plans: [docs/wiki/research/investigations/source_x/plans](../research/investigations/source_x/plans/)
- Source-X conclusions: [docs/wiki/research/investigations/source_x/conclusions](../research/investigations/source_x/conclusions/)
- baseline reference 조사: [docs/wiki/research/investigations/baseline_reference](../research/investigations/baseline_reference/)
- NASA/LAMBDA cache: [docs/wiki/research/assets/nasa_lambda_graphic_history](../research/assets/nasa_lambda_graphic_history/)
- NASA+BAO kill-map: [003 NASA + BAO baseline constraint map](../research/investigations/baseline_reference/conclusions/003_nasa_bao_baseline_constraint_map.md)
- 이 시스템이 만든 결과: [004 수치 스케치](004_rough_tanh_numerical_sketch_ko.md),
  [005 논문 보고서](005_rough_tanh_thesis_report_ko.md)
