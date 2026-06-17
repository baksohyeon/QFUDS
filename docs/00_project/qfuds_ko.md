---
doc_id: qfuds_korean_overview
title: Quantum Foam Unified Dark Sector (QFUDS)
doc_type: reference
stage: "reference"
status: reference
evidence_role: reference
depends_on:
  - project_overview
next_gate: keep Level 2B blocked; no CMB or matter-power claims
last_updated: 2026-06-17
---

# Quantum Foam Unified Dark Sector (QFUDS)

언어: [English](../../README.md) | Korean

## 목차

- [한눈에 보기](#한눈에-보기)
- [처음 읽을 곳](#처음-읽을-곳)
- [이 저장소 읽는 법](#이-저장소-읽는-법-하네스-먼저-그다음-두-연구-단계)
- [핵심 산출물](#핵심-산출물-에이전틱-연구-하네스)
- [긴 개요](#긴-개요-암흑물질과-암흑에너지-정보-순환을-하나로-묶어본다면-어떨까)
- [현재 위치](#현재-위치-벽까지-밀어붙여-실제로-알아낸-것)
- [원래 본 줄기](#원래-본-줄기-무엇이-gammaa를-만드는가-그리고-왜-z2인가)
- [후기](#후기-큰-가설은-결국-두-난제로-수렴했습니다)
- [가설을 세운 계기](#가설을-세운-계기)
- [연구 프로그램](#연구-프로그램)
- [블랙홀 해석](#블랙홀-해석-증거가-아닌-재읽기)
- [문서](#문서)
- [저장소 검사](#저장소-검사)
- [참조 문헌](#참조-문헌)

## 한눈에 보기

QFUDS는 확정 이론이 아니라 초기 단계의 우주론 연구 프로그램입니다. 질문은 암흑물질과
암흑에너지가 공통된 양자 시공간 거품 부문의 서로 다른 거시적 상으로 설명될 수 있는지입니다.

이 저장소에서 가장 중요한 산출물은 **에이전틱 연구 하네스**입니다. 워크플로, 캐시,
파서 라우팅, 적대적 검토, 게이트를 묶어 추측성 탐색을 감사 가능한 작업으로 만든
시스템입니다. 그 기록은
[lineage 006](../wiki/lineage/006_agentic_research_system_ko.md)에 있습니다. 물리 문서들은
그 하네스로 읽고, 밀어붙이고, 검토하고, 필요하면 강등한 payload에 가깝습니다.

이 저장소의 목적은 QFUDS를 옹호하는 것이 아닙니다. 아이디어를 검증, 비교, 축소, 또는
폐기할 수 있을 만큼 명시적으로 만드는 것이 목적입니다. 현재 프로젝트 상태는
[로드맵](../05_next_steps/000_roadmap.md)만 말할 수 있습니다.

짧게 말하면 다음과 같습니다.

- 핵심 방법론 산출물은
  [lineage 006](../wiki/lineage/006_agentic_research_system_ko.md)입니다. 에이전틱 연구
  하네스와 운영 시스템 기록입니다.
- 실증으로 뒷받침되는 본 줄기는
  [lineage 003](../wiki/lineage/003_research_flow_plain_language_ko.md)에서 끝납니다.
- 2단계의 거친 탐색 대표 문서는
  [lineage 004](../wiki/lineage/004_rough_tanh_numerical_sketch_ko.md)입니다.
- [lineage 005](../wiki/lineage/005_rough_tanh_thesis_report_ko.md)는 거친 `tanh`
  탐색을 논문 형식으로 압축한 선택적 아카이브입니다. 첫 독해용 문서는 아닙니다.

## 처음 읽을 곳

| 보고 싶은 것 | 읽을 문서 |
| --- | --- |
| 핵심 에이전틱 연구 하네스 | [lineage 006](../wiki/lineage/006_agentic_research_system_ko.md) 및 [.agent/workflows](../../.agent/workflows/README.md) |
| 현재 상태, blocker, 활성 gate | [로드맵](../05_next_steps/000_roadmap.md) |
| 검증된 본 줄기의 쉬운 설명 | [lineage 003](../wiki/lineage/003_research_flow_plain_language_ko.md) |
| 2단계 거친 탐색 대표 기록 | [lineage 004](../wiki/lineage/004_rough_tanh_numerical_sketch_ko.md) |
| 논문형 압축 아카이브 | [lineage 005](../wiki/lineage/005_rough_tanh_thesis_report_ko.md) |
| 영어 개요 | [README.md](../../README.md) |

추천 순서:

```text
lineage 006
로드맵
-> lineage 003
-> lineage 004
-> docs/README.md
```

[lineage 005](../wiki/lineage/005_rough_tanh_thesis_report_ko.md)는 거친 가지를
논문 형식으로 압축해 둔 문서가 필요할 때만 보면 됩니다.

## 이 저장소 읽는 법: 하네스 먼저, 그다음 두 연구 단계

이 프로젝트에는 성격이 다른 세 층이 있습니다. 지금 어느 층을 읽고 있는지에 따라
문장의 무게가 달라집니다. 각 층은 맡은 일이 다르고, 증거로서의 무게도 다릅니다.

**0층: 연구 하네스(핵심 산출물).** 이건 에이전틱 운영 시스템입니다. 워크플로 SSOT,
파서 라우팅, 자산 캐시 상태, 적대적 검토, 회고, 결정론적 게이트가 여기에 속합니다.
기록은 [lineage 006](../wiki/lineage/006_agentic_research_system_ko.md)에 있고, 실제
운영 규칙은 [.agent/workflows](../../.agent/workflows/README.md)에 있습니다. 이 레포에서
재사용 가능한 핵심이 무엇인지 보려면 이 층부터 읽어야 합니다.

**1단계: 제대로 검증한 본 줄기(진짜 실험).** 규칙을 세우고, 시험하고, 실패한 버전은
버리는 방식으로 실제 통과 기준(kill-gate)을 건 부분입니다. 여기서 말하는 주장은 모두
[docs/03_experiments/](../03_experiments/) 안의 번호 붙은 실험으로 뒷받침됩니다.
그 흐름 전체를 쉬운 말로 정리한 끝이
[lineage 003](../wiki/lineage/003_research_flow_plain_language_ko.md)입니다. 아래
[원래 본 줄기](#원래-본-줄기-무엇이-gammaa를-만드는가-그리고-왜-z2인가) 절의
`Gamma(a)` 이야기가 바로 이 단계입니다. 이 저장소에서 딱 하나만 믿겠다면 여기를
믿으면 됩니다. **실증으로 뒷받침되는 기록은 여기, 003에서 끝납니다.**

**2단계: 거칠게 끝까지 밀어본 부분(엄밀함을 내려놓은 구간).** 본 줄기가 벽에 부딪힌
뒤에는 검증 기준을 낮추고 탐색 자체를 끝까지 진행했습니다. 가장 거친 버전 하나,
곧 손으로 그린 `tanh` 전이를 잡고 24개 체크포인트로 밀어붙인 구간입니다. 이건 검증된
결과가 아니라 스케치입니다. 날것의 수치 작업은
[lineage/assets/](../wiki/lineage/assets/)에 모았고, 2단계 대표 탐색 기록은
[lineage 004](../wiki/lineage/004_rough_tanh_numerical_sketch_ko.md)입니다.
[lineage 005](../wiki/lineage/005_rough_tanh_thesis_report_ko.md)는 같은 내용을
논문 형식으로 압축한 선택 문서입니다.
[현재 위치](#현재-위치-벽까지-밀어붙여-실제로-알아낸-것) 절은 이 탐색이 어디까지
갔는지를 정리한 보고입니다. 증명이 아니라, 비전문가가 탐색 결과를 정리한 기록으로
읽어 주세요.

한 줄로: **lineage 006은 재사용 가능한 하네스이고, 1단계는 진짜 시험을 통과한 것(003까지),
2단계는 실패한 구현체를 그래도 벽까지 밀어붙였을 때 나온 것입니다. 대표 기록은 004이고,
005는 선택적으로 읽는 논문형 압축본입니다.**

## 핵심 산출물: 에이전틱 연구 하네스

물리 이야기는 payload에 가깝습니다. 핵심 산출물은 그 결과를 만들고 걸러낸 작업
시스템입니다. 핵심은 일관된 피드백 루프였습니다. AI가 맞는다고 믿은 것이 아니라, AI가
틀릴 수 있다는 전제에서 문헌, 자산, 상태, 검증을 나눠 관리하고, 매번 다시 확인하게 만든
구조입니다. 질문은 GPT와의 대화에서 시작했지만, 저장소 안에서는 워크플로, 로드맵 SSOT,
검증 스크립트, 회고 기록으로 고정했습니다. 덕분에 문헌을 읽고, 데이터를 정리하고,
모르는 것을 분해하는 속도가 크게 올라갔습니다. 전체 기록은
[lineage 006](../wiki/lineage/006_agentic_research_system_ko.md)에 있고, 실제 운영 규칙은
[.agent/workflows](../../.agent/workflows/README.md)에 있으며, 깨진 지점을 어떻게 고쳤는지
남긴 기록은 [회고 폴더](../wiki/postmortem/)에 있습니다.

비서 한 명이라기보다는 운영 규칙이 분명한 작은 연구실에 가깝습니다.

- **요약본이 아니라 진짜 논문을 읽습니다.** PageIndex와 MarkItDown을 MCP로 붙였습니다.
  MCP는 AI 에이전트에 외부 도구를 연결하는 표준 방식입니다. 여기서 중요한 건 단순한
  PDF -> Markdown 변환이 아니라 파서 라우팅이었습니다. 논문 PDF와 arXiv source는
  PageIndex로 구조·페이지·본문을 뽑고, 데이터 릴리스나 매니페스트·표·코드는
  MarkItDown으로 처리했습니다. 그림은 따로 추출했고, Chen Figure 5의 색상별 곡선은
  축 보정까지 거쳐 432줄짜리 CSV 값으로 복원했습니다. 덕분에 제 `Gamma(a)` 곡선을
  다른 논문의 엔트로피 곡선 위에 막연히 포개 본 것이 아니라, 복원한 `S_BH(a)`와
  `entropy_density(a)` 수치와 직접 대조해 볼 수 있었습니다. 이 수치화는 QFUDS 증거가
  아니라 source-history 후보로만 남겼습니다. 파싱하고 검증한 결과는
  [docs/wiki/research/](../wiki/research/)에 쌓여 있습니다. 문헌 메모 약 60건과
  완전히 디지털화한 논문 십수 편(예:
  [Source-X 조사](../wiki/research/investigations/source_x/))이 원본·그림·복원한 숫자와
  함께 보관돼 있습니다.
- **"PDF가 있다"와 "이걸 데이터로 쓸 수 있다"를 구분합니다.** 모든 출처는 11단 사다리에
  올려 둡니다. "아직 안 찾음"부터 "받았지만 안 열어봄", "숫자까지 디지털화해서 바로 쓸 수
  있음"까지요. 이 구분은 받아 둔 파일을 실제로 확인한 자료처럼 취급하는 실수를 막습니다.
  [literature/index.csv](../wiki/research/literature/index.csv) 같은 색인에는
  `product_status`, `digitization_status`, `used_by`, `last_checked` 같은 필드를 두고,
  왜 캐시했는지와 아직 왜 못 쓰는지를 같이 남겼습니다. 그래서 캐시에 없음, 세상에 없음,
  문헌은 있지만 데이터 제품이 없음이 서로 섞이지 않습니다. 토큰과 fetch도 아끼고, 같은
  논문을 두 번 받을 일도 줄어듭니다.
- **검증은 두 겹으로 걸었습니다.** 프롬프트 단계에서는 "테스트를 돌려라", "roadmap
  SSOT를 바꾸지 마라", "타이밍이 닮았다고 증거로 쓰지 마라" 같은 지시를 계속 넣었습니다.
  커밋 단계에서는 git 훅이 `validate_docs.py`, `research_consistency.py`,
  `preflight_exp004.py`를 돌립니다. 여기서 '증거'는 LLM이 납득했다는 뜻이 아니라,
  frontmatter 상태, 필수 섹션, 링크, 출력 파일, 결과 문서와 로드맵 SSOT의 대응처럼 파일로
  확인되는 조건입니다. 코드는 이런 기계적 조건을 검사하고, 물리 해석은 별도 검토로
  남깁니다. 24개 체크포인트 전부 이 관문을 통과한 뒤에야 들어왔습니다.
- **긍정 주장은 따로 깨 봅니다.** "줄였다", "유도했다", "통과했다" 같은 결론을 쓸 때마다
  같은 Codex/AI 작업 안에서 반례와 과대주장을 찾는 검토 패스를 따로 돌렸습니다. 그 뒤
  프롬프트로 다시 테스트를 요구하고, 마지막에는 커밋 훅이 기계 검사를 다시 실행합니다.
  이 검토 과정이 진행 도중 과대주장 세 건을 실제로 잡아냈습니다(기록은
  [lineage 004](../wiki/lineage/004_rough_tanh_numerical_sketch_ko.md)에 있고,
  [lineage 005](../wiki/lineage/005_rough_tanh_thesis_report_ko.md)는 이를 논문형으로 요약합니다).
- **AI 한 대가 아니라 여러 대가 교차로 검토했습니다.** Codex를 주력으로 두고 Claude
  Code와 Gemini를 보조·교차검증으로 붙여서, 한 모델의 사각지대를 다른 모델이 메우게
  했습니다.

이걸 한 문장으로 줄이면 이렇습니다. **이 안전장치들이 있었기에, 비전문가 한 명이 거친
아이디어를 끝까지 밀어붙이면서도 근거 없는 결론을 남기지 않을 수 있었습니다.** 실패는
글로 남고(회고가 그 기록입니다), 긍정 주장은 정해진 관문을 통과해야만 문서에 남습니다.

## 긴 개요: 암흑물질과 암흑에너지, 정보 순환을 하나로 묶어본다면 어떨까?

### 초록

이 저장소는 암흑물질(우주 질량의 대부분을 차지하지만 빛을 내지 않아 직접 보이지 않는 물질)과 암흑에너지(우주의 팽창을 점점 빠르게 만드는 정체불명의 에너지)가, 사실은 같은 미시적 양자 시공간 거품(quantum-spacetime foam, 아주 작은 규모에서 시공간이 부글거린다고 보는 가설적 매질)이 큰 규모에서 서로 다른 모습으로 나타난 것일 수 있는지 탐색합니다. 표준 모형인 LCDM(현재 우주를 가장 잘 설명하는 표준 우주 모형)은 이 둘을 별개의 성분으로 봅니다. 하지만 QFUDS는, 그 둘이 사실은 같은 거품 하나가 규모에 따라 다르게 보인 것일 수도 있다고 여깁니다.

비유하면, 물은 조건에 따라 얼음, 액체 물, 수증기로 보일 수 있습니다. QFUDS는 암흑부문에 대해 비슷한 질문을 던집니다. 하나의 바탕 매질이 어떤 조건에서는 물질처럼 보이고, 다른 조건에서는 진공압처럼 보일 수 있는가?

이 구도에서 뭉치는 상(clustering phase)은 $w \simeq 0$, $c_s^2 \simeq 0$인 거의 압력 없는 성분처럼 행동해야 합니다. 그래야 차가운 암흑물질처럼 구조 형성에 참여할 수 있습니다. 잔여 상(residual phase)은 우주의 가속팽창을 설명하려면 $w \simeq -1$인 느린 진공압 성분처럼 행동해야 합니다. 블랙홀은 QFUDS의 증거로 쓰지 않습니다. 아무리 조심스럽게 말해도, 블랙홀은 QFUDS 언어로 '국소 정보 압축 지점(local information-compression site)'이라 불러볼 수 있는 추측성 이름표일 뿐입니다. 블랙홀이나 화이트홀의 잔여체 역시, 그 동역학과 제약이 제대로 유도되기 전까지는 같은 거품 부문 안의 부차적인 위상 결함(시공간 짜임새에 생긴 흠집 같은 것) 후보로만 둡니다.

이 모델은 일반상대론이 정한 우주 팽창의 기본 틀(프리드만 배경 동역학)을 그대로 지킵니다. 대신 암흑에너지의 시간 변화, 작은 규모의 은하 헤일로(은하를 감싼 암흑물질 덩어리) 구조, 암흑부문의 뭉침에서 LCDM과 다른 신호가 나올 수 있는지를 묻습니다. 블랙홀 증발 이야기는 양자중력에서 나온 동기일 뿐, 이 저장소가 지금 거는 관측 테스트는 아닙니다.

이 프로젝트는 완성된 물리 이론이 아니라 연구 프로그램이자 검증용 장난감 프레임워크입니다.
목적은 제 가설을 실제 검증대 위에 올리는 데 있습니다. 우주마이크로파배경(CMB, 빅뱅의 잔열로 남은 우주 전역의 빛), 대규모 구조, 은하 헤일로 밀도 분포, 암흑물질 검출 실험, 암흑에너지 상태방정식 정밀 측정 같은 실제 관측으로 따져, 틀렸음을 가릴 수 있는 예측으로 다듬어 갑니다.

### 기본 변수

상태방정식 변수 $w$는 압력을 에너지 밀도로 나눈 값입니다. $w \simeq 0$이면 물질처럼 희석되고, $w \simeq -1$이면 암흑에너지처럼 행동합니다.

유효 음속 $c_s^2$는 유효 매질이 뭉치려는 변화에 얼마나 강하게 저항하는지를 나타냅니다. QFUDS가 살아남으려면 뭉치는 상에서 $c_s^2 \simeq 0$이어야 합니다.

비유하면, 모래는 쌓여서 더미를 만들 수 있지만 팽팽한 트램펄린은 누르면 다시 밀어냅니다. 은하가 형성될 때 암흑물질 같은 성분은 트램펄린보다 모래에 가까워야 합니다.

### 핵심 가설

암흑물질과 암흑에너지는 근본적으로 분리된 두 물질이 아닐 수 있습니다.
같은 미시적 양자 시공간 거품이 거시적으로 다르게 나타난 두 상일 수 있습니다.

```text
dark matter  -> 뭉치는 거품 상(clustering foam phase)
dark energy  -> 잔여 진공압 상(residual vacuum-pressure phase)
remnants     -> 같은 거품 부문의 선택적 결함(optional defects)
```

더 간단히 줄여서 설명하면 아래와 같습니다.

```text
암흑물질 + 암흑에너지
= 양자 시공간 거품의 두 유효 상
```

블랙홀과 화이트홀 비슷한 잔여체는 부차적입니다. QFUDS 언어로는 정보 압축 지점이나 위상 결함처럼 읽어볼 수 있지만, 이것은 확립된 블랙홀 물리나 은하 형성 물리가 아니라 추측에 가까운 다시 읽기일 뿐입니다. 지금 기준으로는 핵심에서 거리가 있어 아직 다루지 않는 주제입니다.

## 현재 위치: 벽까지 밀어붙여 실제로 알아낸 것

*2단계: 거칠게 밀어붙인 부분. 통과 기준을 건 실험이 아니라 현상론적 스케치입니다.*

위에 적은 개념은 출발점일 뿐 결과가 아닙니다. 지금까지 가장 끝까지 밀어붙인 시도는
구체적인 한 버전, 곧 통합 암흑부문의 상태방정식(압력과 밀도의 비 $w$)을 '거친 `tanh`
전이'($w$가 부드러운 S자 곡선을 따라 한 값에서 다른 값으로 서서히 갈아타는 방식)로 놓고,
24개의 작은 체크포인트로 쪼개 한계까지 끌고 간 작업입니다. 그 기록이
[거친 `tanh` 수치 스케치](../wiki/lineage/004_rough_tanh_numerical_sketch_ko.md)에
담겨 있습니다. 이 작업의 의의는 새 우주론을 발견한 데 있지 않고, 24개 체크포인트로
이 아이디어가 어디까지 통하고 어디서 왜 막히는지를 기록한 데 있습니다. 더 형식적인
[논문 형식 보고서](../wiki/lineage/005_rough_tanh_thesis_report_ko.md)는 같은 내용을
압축한 선택 문서이며, 처음 읽을 때는 004가 더 직접적인 입구입니다.
프로젝트는 지금 **관측자 모드**(observer mode, 새 가설을 더 밀지 않고 외부 관측
결과를 기다리는 상태)이고, 현재 상태를 알려주는 단 하나의 기준 문서는
[로드맵](../05_next_steps/000_roadmap.md)입니다.

![효과적 수준에서는 작동합니다: V2 변형의 배경 팽창과 거리지수는 Ia형 초신성 산포 바닥(±0.05 mag) 안에서 ΛCDM을 따라가고, 완전 통합 V1 변형은 고적색편이에서 깨집니다.](../wiki/lineage/assets/004_rough_tanh/fig_background.png)

이 지도는 세 층위로 읽힙니다.

- **효과적 수준(겉으로 맞춰보는 단계): 작동은 하지만 이기지는 못합니다.** 보통 물질을
  따로 떼어낸 변형(V2)은 우주의 팽창 역사를 초신성 데이터로 봤을 때 ΛCDM과 구별이 안
  될 만큼 똑같이 재현합니다(거리 차이가 $|\Delta\mu| < 0.02$ mag, 즉 초신성 밝기 오차 안에
  숨을 정도). 여기에 아주 작은 유효 음속(단일 $S_8$ CP5 교차값은
  $c_{\rm eff}^2 \approx 2.9\times10^{-5}$, 이후 CP7의 거친 격자 최적값은
  $4.6\times10^{-6}$)을 넣으면 구조가 자라난 정도($S_8$)가 관측값
  $S_8 \approx 0.76$ 쪽으로 내려옵니다.
  그러나 이게 ΛCDM보다 나은 것은 아닙니다. 적합이 좋아 보이는 까닭은 그저 $S_8$를
  낮췄기 때문이고($S_8$를 낮추는 모델이라면 무엇이든 똑같이 좋아집니다), 손으로 맞춰야
  할 값이 하나 더 늘며, 허블 상수 긴장($H_0$ 긴장, 가까운 우주와 먼 우주가 알려주는
  팽창 속도가 8%쯤 어긋나는 문제)은 오히려 *더 나빠집니다*.
- **반증 가능 수준(틀렸음을 증명할 수 있는 단계): 진짜 과학적 가치는 여기 있습니다.**
  배경(우주의 평균 팽창)에서는 ΛCDM과 똑같아 숨어버리니, 이 모델이 가치를 가지려면
  ΛCDM과 *갈라지는* 지점이 있어야 합니다. 다행히 깨끗하게 갈라지는 신호가 셋 남습니다.
  (1) 약중력렌즈(멀리 있는 은하 빛이 중간 물질의 중력에 휘는 정도로 물질 분포를 재는
  방법)로 본 물질 분포 곡선에 특정 크기 근처에서 계단처럼 꺾이는 자국이 생기고
  ($k_J \approx 0.1\,\mathrm{Mpc}^{-1}$), (2) 후기 ISW(우주배경복사 빛이 거대구조를 지나며 받는 미세한
  에너지 변화)가 크기에 따라 기울어지며, (3) 구조가 자라는 속도를 나타내는 지수
  ($\gamma_{\rm eff}(k)$)가 크기에 따라 달라집니다. 차세대 망원경 Euclid급 관측이라면 이 신호들을
  $\sim\!24\sigma$(통계적으로 사실상 확실하다고 볼 만큼 강한 수준)로 잡아낼 수 있습니다.
- **근본 수준(왜 그런지를 제일원리에서 끌어내는 단계): 천장에 부딪힙니다.** 데이터가
  원하는 값들을 미시 거품 구조에서 *유도*하려 하면 막힙니다. 데이터는 상관길이
  $\xi \approx 10$ Mpc(미시적 거품 크기가 아니라 은하들이 이루는 거대구조 크기)와 임계밀도
  부근에서 일어나는 전이($\rho_* \approx \rho_\Lambda$)를 원합니다. 이 값들을 어떤 메커니즘으로 억지로
  만들어내려 하면, 손으로 맞춰야 하는 양이 줄지 않고 *자리만 옮겨갈* 뿐입니다. 결국 두
  숫자는 각각 **우주상수 문제**(왜 진공에너지가 이렇게까지 작은가)와 **계층/스케일
  문제**(왜 하필 이 크기인가)로 되돌아갑니다. 이 천장은 이 아이디어만의 실패가 아니라,
  시간에 따라 변하는 암흑에너지를 다루는 *모든* 모델이 똑같이 부딪히는 벽입니다.

![천장을 한 장으로: 데이터가 원하는 상관길이 ξ≈9.5 Mpc는 미시 거품 크기에도, 빛이 닿을 수 있는 한계(인과 지평)에도 자연스럽지 않다. 게다가 전이가 일어나는 밀도는 '왜 하필 지금이냐(why-now)'를 따지는, 약 3자릿수(~3 order) 폭의 좁은 창 안에 들어앉는다. 결국 스케일 문제와 why-now 문제로 귀결된다.](../wiki/lineage/assets/004_rough_tanh/fig_cp20_ceiling_derivation.png)

이야기로만 끝나지 않고 확인된 항목도 둘 있습니다. 하나는
tracker-attractor(처음 조건을 아무렇게나 줘도 시간이 지나면 같은 결말로 빨려드는
성질)인데, 시작값을 손으로 맞춰야 하는 범위를 약 15.7 decade(10의 15.7제곱, 그러니까
매우 넓은 범위) 줄입니다. 이 작업 전체에서 부분적으로 확인된 항목입니다. 다른 하나는,
"내가 뭘 놓쳤지?" 하고 떠올린 서로 다른 직관 셋이 각자
알아서 약 25년치 기존 연구(카멜레온 차폐, LTB 보이드, Buchert 평균화)와 똑같은 곳에
도착했다는 사실입니다. 이는 그 천장이 제 방식 하나가 만들어낸 착시가 아니라 실제로
존재한다는 방증입니다.

방법론적으로는 에이전트 기반 운영 절차를 사용했습니다. 규칙을 한곳에 모아
관리하는 구조(거버넌스 SSOT)에, 여러 작업을 동시에 돌리고(병렬) 나온 결과를 일부러
반박해 보고(적대적 검토) 정해진 통과 기준으로 거르는(결정론적 게이트) 장치를 붙였습니다.
목적은 지원되지 않은 긍정 주장이 문서에 남지 않게 하는 것이었습니다.

위의 숫자들은 모두 거친 근사(rough proxy, 정밀 계산이 아니라 경향만 보는 어림셈)에서
나온 값입니다. 제대로 검증하려면 전문 우주론 계산 코드(Boltzmann code, CLASS/hi_class)가
필요한데, 지금은 그 단계가 막혀(blocked) 있습니다. 그러니 여기 어떤 것도 확정된 물리적
주장이 아닙니다. 체크포인트별 전체 기록은
[거친 `tanh` 수치 스케치](../wiki/lineage/004_rough_tanh_numerical_sketch_ko.md)에,
압축된 논문형 종합은
[논문 형식 보고서](../wiki/lineage/005_rough_tanh_thesis_report_ko.md)에,
지금까지 얻은 교훈은 [What We Actually Learned](project_identity.md)에 정리해 두었습니다.

## 원래 본 줄기: 무엇이 Gamma(a)를 만드는가, 그리고 왜 z≈2인가

*1단계: 제대로 검증한 본 줄기. 아래 단계 하나하나가
[docs/03_experiments/](../03_experiments/)의 통과 기준을 건 실험이고,
[lineage 003](../wiki/lineage/003_research_flow_plain_language_ko.md)에 정리돼
있습니다. 이 프로젝트에서 실증으로 뒷받침되는 부분이고, 시간상으로도 먼저였습니다.*

위의 'rough tanh' 이야기보다 먼저 시작한 본 줄기가 있습니다. 출발점은 블랙홀 정보
역설이었습니다. *정보가 진짜 안 사라진다면 어디로 가는가?* 거기서 'Landauer → 블랙홀
정보 → 화이트홀 → 양자 거품 → 암흑물질/암흑에너지'로 자신만만하게 이어 붙였고,
망상으로 끝내기 싫어 전이함수 Gamma(a)(암흑물질처럼 뭉치는 쪽에서 암흑에너지처럼 남는
쪽으로 얼마나 넘어가는지를 정하는 밸브 같은 함수)를 세워 실험을 쌓았습니다.

실험은 이렇게 흘렀습니다.

- **exp_000**: Gamma=0이면 표준 LCDM으로 돌아가는지부터 확인(대조군).
- **exp_001**: 여러 Gamma 법칙 스캔. 너무 활발하거나 제멋대로 튀는 전달 법칙은 탈락.
- **exp_001.5**: "이게 진짜 물리 source에서 나왔나?" 감사. 유지된 Gamma는 *물리적
  유도에 실패*.
- **exp_002**: 엔트로피/정보 source로 밀 수 있나? 넓은 엔트로피 언어는 죽고, 정보 생산
  모양은 provenance로만 남음.
- **exp_003**: 섭동 닫힘. P2는 죽고 P1만 현상론으로 생존.
- **exp_004**: 모델 족보 확인. 여기서 결정적 결과가 나왔습니다. 내 P1은 새 우주론이
  아니라 기존 상호작용 진공(IV)·상호작용 암흑에너지(IDE) 안에 떨어지는 놈이었습니다.
  "새 이론을 만들었다"가 아니라 "기존 IDE/IV와 비교 가능한 형태로 떨어졌다"가 맞습니다.
- **exp_005–006**: 그럼 내 Gamma의 timing이 그냥 예쁜 곡선이냐, 실제 IDE 복원을
  압축하는 prior냐? 답은 물리 source도 새 모델도 아님. 단, 유지된 Gamma의 peak가 z≈2
  근처였고, Escamilla 2023과 DESI DR2 기반 복원(Li & Zhang 2025 등)에서도 z≈1–2에
  feature가 자꾸 나옵니다. 다만 데이터가 넓고 약해서 "배제는 안 되지만 지지도 못 함
  (allowed but not informative)".

디지털화 압축 감사까지 해보니, 내가 만든 Gamma 함수는 *최적 압축 family가
아니었습니다*. 더 단순한 transition/Gaussian/pulse가 복원을 더 잘 설명했습니다. 즉 내
구현체는 졌습니다. 그런데 그 함수가 *가리키던 시기* z≈2 자체는 계속 살아남았습니다.

왜 하필 z≈2인가? 이때가 별 생성·은하 성장·퀘이사·블랙홀 성장이 모두 활발한 우주의
전성기, Cosmic Noon(우주 전성기)입니다. 더 중요한 점은 기존 학계도 여기서 멈춘다는
데 있습니다. "feature는 보인다. 그런데 왜인지는 모른다." 표준 ΛCDM은 암흑물질↔암흑에너지
상호작용을 0으로 두니, 이 질문 자체를 다루지 않습니다.

쉬운 비유로 옮기면 이렇습니다. 처음엔 "여름에 아이스크림이 왜 많이 팔리지? 더위?
관광객? 방학?"을 물었는데, 찾아보니 학계가 이미 비슷한 답들을 해뒀더군요(블랙홀
엔트로피·CCBH·IDE 등). 그래서 방향을 틀었습니다. "개별 원인 말고, *도시 전체의
활동량*이 반영된 지표 아닐까?" 관점은 좋았습니다. 그런데 바로 다음 질문에서
막혔습니다. **"그 도시 전체 활동량을 *무엇으로 측정*하는데?"** 전력 사용량? 유동인구?
결제량? 그걸 나타낼 숫자가 없었습니다. 아이디어는 있는데 온도계가 없는 상태였습니다.

이게 지금 QFUDS의 정확한 위치입니다. 원인 후보를 모르는 단계가 아니라, **상태변수
(state variable, 그 거시 상태를 나타내는 측정 가능한 양)를 아직 정의하지 못한
단계**입니다. 실제로 이건 로드맵의 공식 blocker이기도 합니다. 거품 부문에서 순환 없이
정의되는 상태변수가 아직 없습니다.

처음 블랙홀 정보 역설("보존된 정보가 어디로 가나")에서 출발했는데, 끝에 남은 질문도
"보존돼야 할 무언가가 *언제*(z≈2) 흘러가나, 그리고 그걸 *셀 수 있는 양*은 무엇이냐"
였습니다. 출발한 입구로 다시 나온 셈입니다.

현재 결론은 이렇습니다. 아직 답은 없습니다. Gamma(a)는 전체 가설이 아니라 첫
프로토타입 구현체였고, 그 프로토타입은 실패했습니다. 남은 부분은 "구조 형성
시기와 암흑부문 상호작용 타이밍이 관련 있을 수 있다"는 가능성입니다. 이 질문은
현재 레포 안에서도 아직 닫히지 않았습니다. 상태
권위는 여전히 [로드맵](../05_next_steps/000_roadmap.md)이고, 프로젝트는 observer
mode입니다. 이 강등은 큰 가설(암흑물질↔암흑에너지 상전이)의 폐기가 아니라, 그것을
설명하려던 메커니즘 하나의 폐기에 가깝습니다.

## 후기: 큰 가설은 결국 두 난제로 수렴했습니다

처음에는 큰 이론처럼 보였지만, 끝까지 밀어붙이고 나니 결국 현대 물리학이 아직 못 푼
두 가지 난제로 수렴했습니다. 며칠간의 결론을 먼저 적자면 이렇습니다.

> **[과학적 난제]**
> 1. **왜 암흑에너지의 스케일이 하필 meV(밀리전자볼트, 아주 작은 에너지 단위)인가?**
>    이 질문은 곧장 우주상수 문제(진공에너지가 이론값보다 어마어마하게 작은 이유를
>    못 푸는 문제)로 이어집니다.
> 2. **진공에너지를 셀 때 어느 크기에서 자를(cutoff) 것인가?** 저는 양자 세계(아주
>    작은 미시 영역)에서 출발해 추론했는데, 정작 데이터가 요구하는 거리 기준이 플랑크
>    스케일(상상하기 힘들 만큼 작은 미시 길이)인지, 지평 스케일(빛이 닿을 수 있는
>    우주의 한계 크기)인지, 아니면 은하들이 모여 이루는 cosmic-web 스케일인지가
>    분명치 않습니다.

"왜"까지는 끝내 알 수 없었습니다. 당연한 일입니다. 이 둘이 바로 현대 물리학이 아직 못
푼 난제라서, 애초에 물리적으로 깔끔하게 유도해 낼 수가 없으니까요.

정리하면 이렇습니다.

시작은 질문 하나였습니다. *블랙홀에 빨려 들어간 정보가 정말로 사라지지 않는다면, 그
정보는 대체 어디에 남는 걸까?* 여기서 생각이 번졌습니다. 진공이나 시공간 거품 같은
어떤 매질이 있어서, 어떤 조건에서는 암흑물질처럼 뭉치고 어떤 조건에서는 암흑에너지처럼
우주를 밀어내는 건 아닐까? 이름도 제법 그럴듯하게 붙였습니다. 바로 **QFUDS (Quantum
Foam Unified Dark Sector)**입니다. 물이 조건에 따라 얼음, 액체, 수증기로 모습을 바꾸듯,
하나의 암흑부문이 어떤 조건에서는 뭉치는 상(상태방정식 $w \approx 0$, 유효 음속 $c_s^2 \approx 0$인 상태로,
그래야 차가운 암흑물질처럼 구조를 만드는 데 참여합니다)으로, 다른 조건에서는 잔여
진공압 상($w \approx -1$인 상태로, 그래야 우주의 가속팽창을 설명합니다)으로 보일 수 있느냐는
물음이었습니다.

곧 정직한 한계에 부딪혔습니다. 이건 잘해야 *현상론*(왜 그런지는 모른 채 관측에 맞는
식만 세우는 단계)이고, 물리적으로 유도(derive, 제일원리에서 식을 끌어내는 것)할 수는
없었습니다. 게다가 새롭지도 않았습니다. 비슷한 접근을 하던 학파가 이미 같은 계산을
해두고 같은 자리에서 멈춰 있었거든요. 아쉬웠지만 이렇게 마음먹었습니다. "엄밀함을
지켜야 하는 과학자라면 여기서 멈추겠지만, 나는 그런 제약이 없으니 비과학적이어도 끝까지
가 보자." 그래서 동적 우주론에 필요한 성질을 얻으려고, 표준모형이 미묘하게 안 맞는
지점을 겨냥해 경향성을 살피며 brute-force(가능한 값을 무식하게 다 넣어보며 맞추는
방식)로 끼워 맞춰 나갔습니다.

그 결과, 최적해(데이터에 가장 잘 맞는 값의 조합)가 나왔습니다.

- **$c_{\rm eff}^2 \approx 4.6\times10^{-6}$**: 유효 음속을 제곱한 값입니다. 쉽게 말하면 이 암흑부문이 구조
  형성에서 얼마나 잘 퍼지는지(혹은 반대로 얼마나 잘 뭉치는지)를 조절하는 변수입니다.
- **상관길이 $\xi \approx 9.5$–$10$ Mpc**: 거품의 한 부분이 다른 부분에 영향을 미치는 유효 거리
  눈금입니다. 1 Mpc가 약 326만 광년이니, 10 Mpc는 은하 하나의 내부가 아니라 cosmic
  web, 곧 우주 거대구조 크기에 해당합니다.

| 상관길이 $\xi$ | $c_{\rm eff}^2$ | $S_8$ |
| --- | --- | --- |
| 미시 거품 ($\xi \le 1$ Mpc) | $\to 0$ ($5\times10^{-8}$ 이하) | **0.95 (너무 높음)** |
| 구조 스케일 ($\xi \approx 10$ Mpc) | $\approx 5\times10^{-6}$ | 0.82 |
| **데이터 fit ($c_{\rm eff}^2 = 4.6\times10^{-6}$)** | **$\to\ \xi \approx 9.5$ Mpc** | $\approx 0.78$–$0.82$ |
| Hubble ($\xi \approx c/H_0$) | $\approx 1$ | 0.68 (오버슈트) |

![뒤집힌 순간: 관측 S8을 재현하는 상관길이는 제가 기대한 미시 거품 스케일이 아니라 ξ≈10 Mpc(거대구조 스케일)이었습니다.](../wiki/lineage/assets/004_rough_tanh/fig_cp8_ceff2_derivation.png)

논문을 하나하나 크로스체킹(여러 논문을 서로 대조해 확인)해 보니, 자랑스럽게 말해도 될
만한 지점이 있었습니다. brute-force로 짚어낸 스케일과 파라미터 언어가 학계가 이미
다뤄 온 문제 영역과 같은 자리로 들어간 것입니다. 증명도 아니고 새 이론이라는 주장도
아니지만, 올바른 문제 스케일에 실제로 수렴한 것은 맞았습니다. 의미는 있었지만, 동시에
예상 밖이었습니다. 제가 기대한 건 "양자 거품의 아주 작은 단위, 플랑크 스케일"이었는데
프록시 적합이 가리킨 건 은하를 훌쩍 넘어선 거대구조 스케일이었으니까요. (물론 이게
물리적 증명은 아닙니다. 위의 두 난제 때문에 애초에 유도 자체가 불가능합니다.)

그래서 "내가 너무 미시·양자 스케일에만 갇혀서 본 게 아닐까" 하는 의심이 들었습니다.
진공에너지를 플랑크 스케일에서 자르지 말고, 은하·구조 스케일에서 coarse-graining(자잘한
디테일은 뭉뚱그리고 큰 단위로 평균 내서 보는 것)을 해야 하는 건 아닐까 싶었죠. 문헌을
더 뒤져 보니 1990년대부터 지금까지 이미 다 해본 길이었습니다. HDE, EFTofLSS, IR
cutoff, coarse-graining, running vacuum, Buchert averaging, LTB void, screening
같은 흐름이 모두 그런 선례입니다. 심지어 비선형 $\sim\!10$ Mpc 스케일을 암흑부문의 coarse-graining
기준으로 쓰는 접근까지 이미 논문에 나와 있었습니다.

이 모델이 완전히 숨어 버리지는 않는다는 점이 흥미롭습니다. 우주의 평균 팽창
(배경)에서는 ΛCDM과 구별이 안 되지만, 구조(은하들이 뭉친 모양)에는 흔적을 남깁니다.
물질 분포 곡선 $P(k)$의 계단 자국, ISW가 크기에 따라 기울어지는 모양, 구조 성장 지수가
크기에 따라 흐르는 현상이 그 흔적입니다. 즉 배경에서는 숨지만 구조에서는 들킬 수 있는
유형이라, Euclid급 관측이라면 잡아낼 수도 있는 반증 신호까지 나온 셈입니다.

다만 한 가지는 분명히 해두고 싶습니다. 이건 QFUDS가 옳다고 증명한 기록이 아닙니다.
비전문가가 brute-force로 밀어붙이다가 결국 현대 우주론의 미해결 난제에 가닿은 과정을
적은 기록에 가깝습니다.

출발점은 원래 관심이 많던 정보·열역학·블랙홀 질문이었습니다. 정보 삭제에는 열 비용이
따른다는 컴퓨터 과학과 물리학의 연결고리를 보고, it from bit, 블랙홀 정보 문제,
암흑부문까지 질문이 번졌습니다. GPT와 여러 차례 묻고 답하며 사고실험을 해 보다가, 실제로
어디까지 맞고 어디서 막히는지 확인해 보고 싶어졌습니다. 개발자 입장에서는 AI와 함께라면
문헌 조사, 자료 정리, 수치 검산, 실패 기록까지 하나의 리서치 파이프라인으로 묶을 수
있겠다는 판단이 있었습니다.

그래서 이 작업은 그냥 챗봇과 수다 떨듯 진행한 것이 아닙니다. 이 레포 안에서 5일 동안
에이전트 하네스와 일종의 연구 메모리 시스템을 같이 만들며 굴렸습니다. 논문 캐시, 자산
상태표, 워크플로 정의, 실험·결과 기록, 검증 스크립트를 한 묶음으로 두고, 내가 아는 것과
모르는 것, 아직 모르는 줄도 몰랐던 구멍을 계속 분리했습니다. 결과적으로 물리 이론을
증명한 것은 아니지만, 빠르게 배우고 틀린 결론을 걸러내는 시스템으로는 성공적이었습니다.

학계 흐름은 넓게 훑되, 실제 레퍼런스할 데이터는 논문과 1차 출처만 기준으로 삼았습니다.
유튜브, 위키피디아, 영문 위키피디아는 근거로 쓰지 않았습니다. 논문을 찾고, PDF와 arXiv
원본을 받고, 그림 자료를 뜯어내고, Markdown으로 바꾸고, 그래프에서 숫자를 다시 읽어내고
(digitization, 그림 속 곡선을 수치 데이터로 복원하는 작업), CSV로 뽑았습니다. Chen
Figure 5의 색상별 곡선은 축 보정까지 거쳐 432줄짜리 CSV 값으로 복원했고, 제 전이함수
$\Gamma(a)$를 복원한 `S_BH(a)`와 `entropy_density(a)` 수치와 대조했습니다. 여기에 "이미
알려진 모델과 무엇이 다른지"(known-model distinction) 판별, 중복 fetch를 줄이는 캐싱,
상태별 검증 게이트까지 붙였습니다.

결국 가장 크게 남은 것은 "이런 식으로도 배울 수 있구나"라는 깨달음이었습니다. 정리하면
다섯 가지가 남습니다.

1. 현대 우주론의 미해결 난제로 수렴하는 과정을 brute-force로 재현했습니다.
2. 그것이 우연이 아니라, 실제로 학계가 걸어온 길과 겹쳤습니다. 제가 손으로 뽑은
   값이 같은 자리에 놓였고, 접근하는 사고의 흐름도 비슷했으며, 결과적으로 1990년대부터
   오늘날까지의 계보를 따라가 확인한 셈이 되었습니다.
3. 며칠간의 탐색 결과가 학계가 수십 년 다뤄온 실제 스케일 위에 놓였다는 점은
   개인적으로도 큰 성과였고, 영광스러운 확인이었습니다.
4. AI 하네스(앞서 말한, 직접 짠 에이전트 연구 시스템)만으로 비전문가가 여기까지
   도달할 수 있다는 사실 자체가 놀라웠습니다.
5. 이 모든 과정을 직접 만든 에이전트 시스템으로 5일 만에 끝까지 실행했다는 점도
   개인적으로 큰 성과입니다.

관련 DESI·Euclid(우주 거대구조를 정밀하게 관측하는 차세대 프로젝트들) 후속 공개 자료가
이 rough-tanh 가지의 다음 외부 검산 지점입니다. 그 자료가 실제 likelihood 계산으로
이어지기 전까지는 더 강한 결과를 주장하지 않고 observer mode에 두는 것이 맞습니다.

## 가설을 세운 계기

### 정보 삭제에서 검증 모델까지

Quantum Foam Unified Dark Sector (QFUDS)는 암흑물질, 암흑에너지와 우주론에서 정보가 어떻게 흐르는지를 고민하다 시작한 장난감 개념 저장소입니다.

이 아이디어가 어디까지 정합적인지 궁금했습니다.

호기심을 방정식, 제약 조건, 장난감 코드, 반박 가능한 질문으로 바꾸고 가설 검증을 실제로 해보고 싶었습니다.

정보 열역학에 대한 글을 읽었습니다.

```text
동기 부여 원문. 출처 기록으로 보존하며, 기술적 주장으로 쓰지는 않습니다:
『기억을 지울 때, 반드시 열이 발생한다』고 물리학이 증명했습니다.
물리학자 롤프 란다우어가 제창한 원리입니다. 계산을 수행하거나 정보를 생성하는 행위 자체는 에너지를 소모하지 않지만, 1비트의 정보를 지우거나 잊을 때에는 반드시 일정량의 열에너지가 주변으로 방출된다는 것입니다.
즉, 인간의 뇌도 하드디스크도, 무언가를 「잊음」할 때 우주의 엔트로피를 증가시키며, 물리적인 열을 만들어내고 있습니다. 정보에 질량이 있다고 말할 수는 없지만, 정보의 소거에는 열역학적인 대가가 따른다는 뜻입니다.
「잊는다」는 일견 모호해 보이는 현상이, 실은 우주에 열로서 지불되고, 그 장부에 제대로 기록된다는 것입니다.
이는 뇌과학 이야기이자, 컴퓨터의 한계 이야기이며, 우주론 이야기이기도 합니다.
```

조심스럽게 읽으면 이렇습니다. Landauer 원리는 열과 주고받는 물리계에서 논리적으로 되돌릴 수 없는 정보 삭제에만 적용됩니다. 모든 계산에 똑같이 피할 수 없는 비용이 드는 것도 아니고, 이 원리 하나가 곧바로 우주론을 뜻하지도 않습니다.

비유하면, 파일을 삭제한다고 노트북이 물리 법칙을 무시하는 것은 아닙니다. 노트북은 여전히 에너지를 쓰고 열을 냅니다. 일반적인 Landauer 가정 아래에서 1비트 소거의 이상적 최소 비용은 대략 $k_B T \ln 2$입니다. 긴 원문 흐름은 여기서 반복하지 않고 [concept_origin.md](../01_origin/concept_origin.md)에 보존합니다.

그래서 저는 읽자마자 블랙홀 질문이 자연스럽게 나왔습니다.
정보에 물리적 비용이 있다면, 양자 이론 안에서 블랙홀은 정보를 버리는 단순한 쓰레기통처럼 취급하기 어렵습니다. 이것은 QFUDS의 유도가 아니라 더 날카로운 질문을 만들기 위한 동기입니다.
그다음 질문은 이렇게 갈라집니다. 정보는 어디에 새겨지는가? 유니터리한(정보가 보존되는) 블랙홀 증발이라면, 빠져나온 복사들 사이의 상관관계 속에 정보가 숨어 되돌아올 수 있는가? 그리고 진짜 장벽은 정보가 파괴되는 것인가, 아니면 단지 해독이 너무 복잡한 것인가?

처음 사고 흐름은 증명이 아니었습니다. 질문은 대략 이렇게 이동했습니다.

```text
정보 삭제에는 열 비용이 있다
-> 블랙홀 정보 손실 문제와 구조가 비슷하다
-> 유니터리한 블랙홀 증발이라면 정보가 상관관계 안에 인코딩되어야 한다
-> 원리상 복구는 가능하지만 해독 비용이 막는다
-> 복구가 가능하다면 역과정을 묻는다
-> 역과정은 시간역전, CPT, 화이트홀 비슷한 대응물을 떠올리게 한다
-> 블랙홀/화이트홀 잔여체는 정보 저장 부문을 암시한다
-> 진공 또는 시공간 거품이 후보 매질이 된다
-> 암흑물질은 뭉치는 거품 모드일 수 있다
-> 암흑에너지는 잔여 거품 압력일 수 있다
-> QFUDS: 통합 암흑부문 장난감 모형
```

화이트홀/역과정 질문은 흥미로웠지만, SF 소설에 가깝고 과학적으로 엄밀한 주장이 되기에는 너무 크고 장황했습니다.

하나씩 짚어가다보니 하나의 질문으로 수렴했습니다.

```text
하나의 암흑부문이
뭉치는 성분과 잔여 진공압 성분으로 동시에 행동할 수 있는가?
```

다음 검증 질문은 $\Gamma(a)$로 이동했습니다.
뭉치는 거품 상이 잔여 진공압 상으로 넘어간다면, 그 전달률을 구조 성장, 블랙홀 엔트로피, 지평선 엔트로피, 별 형성, 잔여체 통계 같은 실제 물리량에, 또는 출처를 분명히 밝힌 대용 지표(proxy)에 묶을 수 있는가?

비유하면, 두 물탱크가 연결된 상황입니다. 한쪽 탱크는 뭉치는 성분이고, 다른 탱크는 잔여 진공압 성분입니다. $\Gamma(a)$는 두 탱크 사이의 밸브 규칙입니다. 밸브를 마음대로 조절하면 튜닝이고, 밸브 규칙이 실제 물리량에서 나오면 테스트할 수 있습니다.

### 발산, 수렴, 검증

QFUDS라는 개념은 제가 GPT와 주고받은 반복 대화에서 나왔습니다.

```text
날것의 질문
-> 설명
-> 후속 질문
-> 반례 또는 물리 제약
-> 더 넓은 추측
-> 가지치기
-> 장난감 모형
-> 적대적 리뷰
-> 이 저장소의 코드와 출력물
```

발산 단계에서는 Landauer, 블랙홀 정보, 호킹복사, Page curve와 island(둘 다 블랙홀 정보 역설을 풀려고 나온 개념), 역과정, 화이트홀, 양자 거품, 암흑물질, 암흑에너지, 우주상수, 세계관 수준의 상상까지 사방으로 뻗어 나갔습니다.

수렴 단계에서는 반복되는 질문 하나만 남겼습니다.

```text
암흑물질과 암흑에너지를
같은 양자 거품 매질의 두 유효 모드로 볼 수 있는가?
```

검증 단계에서는 은유를 줄이고 기본적인 우주론 검사 앞에 세웠습니다.

```text
무편차 극한에서 LCDM을 회복하는가?
뭉치는 상이 c_s^2를 0에 가깝게 유지할 수 있는가?
CMB 음향 피크를 보존하는가?
물질 파워 스펙트럼을 보존하는가?
현실적인 은하 헤일로를 만들 수 있는가?
잔여체 부문이 조밀 천체 제약을 통과하는가?
```

### 폐기되거나 보존된 가지

날것의 아이디어에는 여러 가지가 섞여 있었습니다.

```text
정보 처리기로서의 블랙홀
화이트홀 비슷한 역방향 통로
화이트홀 비슷한 방출로서의 우주
드문 암흑 구조로서의 진공 요동
잔여 진공압으로서의 우주 가속
```

이 저장소는 변수, 방정식, 테스트로 바꿀 수 있는 가지만 남깁니다. 현재 연구 버전은 다음 질문입니다.

```text
양자 거품 통합 암흑부문이
암흑물질과 암흑에너지로 설명되는 관측 효과를 재현할 수 있는가?
```

기준은 단순합니다.

```text
이 아이디어를 틀릴 수 있을 만큼 정확하게 만들 수 있는가?
```

세부 원문 흐름은 이 개요에서 반복하지 않습니다. 출처 기록은 [concept_origin.md](../01_origin/concept_origin.md)에 보존합니다.

어떤 가지가 살아남았고, 어떤 가지가 동기 수준으로만 내려앉았고, 어떤 가지가 레포 증거 때문에 버려졌는지, 그 현재 감사 상태는 [concept_survival_audit.md](concept_survival_audit.md)에서 확인할 수 있습니다(Source-X의 known-model-distinction 결과와 관측자 모드 전환까지 포함합니다). 상태(status)의 단일 진실 원천은 여전히 [Roadmap](../05_next_steps/000_roadmap.md)입니다.

## 연구 프로그램

제가 장난스럽게 떠올린 가설이 어디까지 정합적인지 확인하려고 구현해보았습니다.

```text
직관
-> 가지치기
-> 가설
-> 장난감 방정식
-> 폐기 조건
-> 코드와 미래의 볼츠만 코드 검증
```

목표는 QFUDS를 증명하는 것이 아닙니다.
목표는 이 모델을 가장 먼저 죽이는 제약을 찾거나, 살아남는 버전을 LCDM, 통합 암흑 유체, 상호작용 암흑에너지, 스칼라장 암흑물질, 블랙홀/화이트홀 잔여체 모형과 비교할 수 있을 만큼 좁히는 데 있습니다.

### 주요 문서

- 현재 상태와 단계별 진행: [Roadmap](../05_next_steps/000_roadmap.md)
- 결정 이유: [Decision Log](decision_log.md)
- 실험별 결론: [Experiment Summary](../04_results/000_experiment_summary.md)
- 주장/증거 추적: [Traceability Matrix](traceability_matrix.md)
- [Level 1.5](../wiki/glossary/repository_levels.md) 통과/실패 관문: [Level 1.5 Resolution Gate](../05_next_steps/015_level_1_5_resolution_gate.md)
- 로드맵 한국어 해설: [Roadmap Overview Korean Guide](../05_next_steps/900_roadmap_overview_ko.md)
- 재현 가능한 검사: [Verification Guide](verification_guide.md)
- 문서 무결성 규칙: [Experiment Record Convention](experiment_record_convention.md) 및 [Frontmatter Convention](frontmatter_convention.md)

CMB와 구조 형성 검사를 통과하기 전까지는 강한 물리적 주장으로 읽으면 안 됩니다.

연구 기록은 아래 명령으로 감사합니다.

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/preflight_exp004.py
```

`validate_docs.py`는 메타데이터와 실험/결과 문서의 필수 섹션을 검사합니다.
`research_consistency.py`는 로드맵이 상태 권한 문서로 유지되는지 검사합니다.
`preflight_exp004.py`는 exp_004 계획 전에 exp_003 기록이 일관적인지 검사합니다.

검증 순서는 다음과 같습니다.

```text
문헌상 위치 확인
-> 배경 우주 검증
-> 상 전달 물리성
-> 현상론적 섭동 닫힘
-> 물리적 섭동 방정식
-> CLASS 또는 CAMB 통합
-> CMB 비교
-> 물질 파워 비교
-> DESI / Euclid / Roman 제약
```

비유하면, 이 과정은 다리를 단계별로 시험하는 것과 비슷합니다.
책상 위 작은 모형은 나쁜 설계를 떨어뜨릴 수 있지만, 실제 다리가 바람, 차량, 지진을 버틴다는 증거는 아닙니다.
배경 우주 수준 실험은 나쁜 전달 법칙을 탈락시킬 수 있지만, CMB나 구조 형성 생존성을 주장할 수는 없습니다.

### 두 상 전달 모형 (유지된 가지, 현재는 현상론으로 강등됨)

> 이것은 원래의 작업 가설이었습니다. 이후 현상론적 상호작용 진공(interacting
> vacuum) 지위로 강등됐고, 프로젝트는 관측자 모드입니다(위의 [현재 위치](#현재-위치-벽까지-밀어붙여-실제로-알아낸-것)와
> [로드맵](../05_next_steps/000_roadmap.md) 참조). 아래는 현재의 물리적 주장이
> 아니라 모델 정의로서 보존합니다.

```text
거의 0에 가까운 음속을 가진 양자 거품 통합 암흑부문
```

더 안전한 공식화는 일반상대론 안의 통합 암흑부문입니다.

$$
\rho_{\rm dark} = \rho_{\rm QF} + \rho_{\rm rem}
$$

$\rho_{\rm QF}$는 양자 거품 통합 암흑 유체입니다. 두 유효 조각을 가집니다.

$$
\rho_{\rm QF}(a) = \rho_{\rm cluster}(a) + \rho_{\rm residual}(a)
$$

뭉치는 조각은 차가운 암흑물질처럼 행동해야 합니다.

$$
\rho_{\rm cluster} \propto a^{-3}, \qquad
w \simeq 0, \qquad
c_s^2 \simeq 0
$$

잔여 조각은 암흑에너지처럼 행동해야 합니다.

$$
\rho_{\rm residual} \simeq \rho_\star, \qquad
w \simeq -1
$$

선택적 잔여체 조각은 다음처럼 씁니다.

$$
\rho_{\rm rem} = \int M f(M)\,dM
$$

실험 001은 뭉치는 상과 잔여 상 사이에 전달률을 추가합니다.

$$
\frac{d\rho_A}{d\ln a} + 3\rho_A = -\Gamma(a)\rho_A
$$

$$
\frac{d\rho_B}{d\ln a} = \Gamma(a)\rho_A
$$

이 가지에는 $\Gamma(a)$를 손으로 맞추는 함수가 아니라, 실제 물리적 원천이나 출처를 분명히 밝힌 대용 지표(proxy)에 묶을 수 있느냐는 시험이 걸려 있었습니다. 물리적 유도로서는 그 기준을 넘지 못했고, 지금은 출처를 명시한 현상론으로만 살아남습니다.
유용하지만 아직 잠정적인 검증 방향은 저적색편이 붕괴(가까운 우주, 즉 비교적 최근 시점에서 구조가 무너지는 정도), 블랙홀 엔트로피, 별 형성 대용 지표입니다.
전달률을 상수로 두거나, 제동 없이 구조 성장에만 비례시키는 방식은 일찍 무너지거나, 결국 평범한 상호작용 암흑에너지와 똑같은 거동으로 되돌아갑니다.

비유하면, 두 물탱크가 연결된 상황입니다. 한 탱크는 뭉치는 상이고, 다른 탱크는 잔여 상입니다. $\Gamma(a)$는 밸브 규칙입니다. 밸브 규칙을 마음대로 정하면 그냥 튜닝입니다. 밸브 규칙이 물리적 원천에서 나오면 테스트할 수 있습니다.

잔여체 항은 그 질량 분포가 미시중력렌즈, CMB, 구조 형성 제약을 통과하기 전까지 부차적으로 두고 진행합니다.

### 핵심 전제 조건

가장 중요한 조건은 유효 음속입니다.

$$
c_s^2 \simeq 0
$$

쉽게 말하면 다음과 같습니다.

```text
QFUDS 거품은 배경 우주에서는 우주를 밀어내는 압력을 남길 수 있지만,
은하 형성 단계에서는 압력 없는 먼지처럼 뭉쳐야 한다.
```

거품이 너무 뻣뻣하면 압력이 구조 형성을 지워버립니다. 그러면 모델은 즉시 죽습니다.

비유하면, 마른 모래는 쌓아서 더미를 만들 수 있습니다. 하지만 탄성 있는 고무판으로 같은 더미를 만들려고 하면 계속 밀려나서 평평해집니다. 뭉치는 상은 은하가 만들어질 만큼 모래 같아야 합니다.

### 이 모델이 해결하려는 문제

이 모델은 세 가지 생각을 연결하려 합니다.

1. 통합 암흑부문: 암흑물질과 암흑에너지가 같은 기원을 가질 수 있는가
2. 우연성 문제: 왜 현재 우주에서 암흑물질과 암흑에너지 밀도가 비슷한가
3. 동적인 진공에너지: 우주상수가 손으로 끼워 넣은 고정 숫자가 아니라, 시간이 지나며 천천히 제자리를 찾아가는 평형값일 수 있는가

### 만약 유효하다면 예측할 수 있는 현상

아래 항목은 검증된 예측이 아닙니다. 모델을 죽일 수 있는 후보 지점이며, 몇몇 항목은 QFUDS만의 고유 신호도 아닙니다.

1. 표준 WIMP 직접 검출은 계속 무검출일 수 있습니다. 하지만 이것만으로 QFUDS가 유리해지는 것은 아닙니다. 직접 검출 신호가 약하거나 숨겨진 비-QFUDS 암흑물질 모형도 많기 때문입니다.
2. 암흑에너지는 작지만 0이 아닌 시간 변화를 보일 수 있습니다.

$$
w(a) = w_0 + w_a(1-a)
$$

LCDM에서는 $w_0=-1$, $w_a=0$입니다. QFUDS가 차이를 만들려면 $w_0 \simeq -1$이면서 $|w_a|>0$인 작은 편차가 필요합니다.

3. 대규모 구조와 CMB는 거의 LCDM처럼 보여야 합니다.
4. 작은 은하 헤일로는 뾰족한 중심부보다 완만한 중심부를 선호할 수 있지만, 보통 물질 되먹임(baryonic feedback, 별·초신성·가스가 내놓은 에너지가 거꾸로 구조 형성에 영향을 주는 것)과 구분해야 합니다.
5. 암흑물질 구조와 보통 물질 구조 사이에 순수한 무충돌 CDM보다 약간 더 강한 상관이 남을 수 있습니다. 하지만 QFUDS 고유의 관계식은 아직 유도되지 않았습니다.
6. 정보가 온전히 보존되는(유니터리한) 양자 서술이 옳다면, 블랙홀이 다 증발한 마지막 상태가 정보라곤 하나도 없는 순수 열복사로만 설명돼서는 안 됩니다. 이것은 양자중력이라면 이래야 한다는 정합성 기대이지, 관측된 천체물리 신호는 아닙니다.
7. 블랙홀/화이트홀 잔여체가 있다면 허용 가능한 질량 분포는 좁아야 합니다.

현재 검증하려는 테스트의 핵심은 화이트홀이 아닙니다.
정밀 관측이 계속 $w=-1$을 지지하는지, 아니면 작은 0이 아닌 $w_a$ 쪽으로 움직이는지가 더 중요합니다.

### 폐기 테스트: 먼저 공격해야 할 지점

적대적인 리뷰어라면 이 순서로 공격합니다.

1. 무편차 극한에서 LCDM을 정확히 회복하는가?
2. 같은 유효 매질이 $w \simeq 0$과 $w \simeq -1$을 얼버무리는 설명 없이 만들어 낼 수 있는가?
3. 왜 $c_s^2$가 0에 가까운가?
4. CMB 음향 피크를 보존하는가?
5. 물질 파워 스펙트럼을 보존하는가?
6. 기존 통합 암흑 유체나 k-에센스 모형보다 나은 것이 있는가?
7. 잔여체 부문은 실제 예측을 추가하는가, 아니면 이야기용 언어인가?

여기서 실패하면 QFUDS는 이름만 바꾼 용어 교체입니다.

## 블랙홀 해석: 증거가 아닌 재읽기

블랙홀은 QFUDS의 중심 증거가 아닙니다.

관측 기준선은 다음과 같습니다.

```text
많은 대질량 은하, 특히 중심 팽대부를 가진 은하는 중심에 대질량 블랙홀을 가진다.
```

우리 은하 중심 블랙홀과 M87의 블랙홀이 대표적인 예입니다. 존재 자체는 별 궤도 동역학과 사건지평선 스케일 영상으로 관측적으로 확립되어 있습니다. 다만 정확한 형성 경로는 여전히 연구 중입니다. 씨앗 블랙홀 형성, 가스 강착, 은하와 블랙홀 병합, 직접 붕괴, 조밀한 항성계 동역학, 암흑물질 헤일로 안의 형성 같은 표준 천체물리 설명은 여전히 중요합니다.

표준 구조 형성 순서는 다음에 더 가깝습니다.

```text
원시 밀도 요동
-> 차가운 암흑물질 헤일로
-> 가스 냉각, 별 형성, 은하
-> 중심 대질량 블랙홀 씨앗과 강착/병합 성장
```

이것은 블랙홀이 은하를 만든다는 말과 다릅니다. 블랙홀은 특히 활동은하핵 되먹임(AGN feedback, 블랙홀이 뿜는 에너지가 숙주 은하의 별 형성에 거꾸로 영향을 주는 것)을 통해 숙주 은하에 영향을 줄 수 있지만, 표준 시나리오에서 은하 형성의 일반적인 출발점은 아닙니다.

QFUDS는 다른 질문을 던질 수 있습니다.

```text
암흑 헤일로가 유효 거품 상이라면,
중심 블랙홀은 그 상의 특수한 고밀도,
고엔트로피, 높은 정보 밀도 영역을 추적하는가?
```

첫 번째 조건은 QFUDS 가정이지 표준 결과가 아닙니다. 표준 우주론은 다음을 말하지 않습니다.

```text
양자 거품 -> 암흑 헤일로
```

QFUDS가 더 강하게 묻는 질문은 다음과 같습니다.

```text
암흑물질이 거품 상이라면,
중심 블랙홀은 그 거품 부문 안의
특수한 압축 지점이나 상전이 지점일 수 있는가?
```

만약 QFUDS 관점으로 해석한다면 다음과 같습니다.

```text
black hole = 가능한 국소 정보 압축 지점
```

더 강하게 말하면:

```text
black hole = 거품 부문의 추측적 상전이 후보 지점
```

이것은 확립된 블랙홀 물리가 아닙니다. 기존 문헌에도 "블랙홀 상전이"라는 표현은 있지만, 보통 반-드 지터(AdS, 진공에너지가 음수인 가상의 시공간) 공간이나 확장된 블랙홀 열역학에서 다루는 Hawking-Page 전이(온도에 따라 블랙홀이 생겼다 사라졌다 하는 일종의 상전이) 같은 것을 가리킵니다. 그것이 관측된 은하 중심 블랙홀을 양자 거품 암흑부문의 상전이 지점이라고 본다는 뜻은 아닙니다.

비유하면, 큰 도시에는 보통 데이터가 많이 오가는 경로 근처에 큰 데이터 센터가 있을 수 있습니다. 하지만 데이터 센터가 있다고 해서 도시 전체가 그 네트워크 때문에 생겼다는 증거는 아닙니다. 마찬가지로 중심 블랙홀은 QFUDS 언어로 압축 지점이나 경로 지점처럼 읽을 수 있지만, QFUDS를 증명하지는 않으며 표준 블랙홀 형성 물리를 대체하지도 않습니다.

안전한 문장은 다음 정도입니다.

```text
QFUDS는 중심 블랙홀을 거품이 지배하는 헤일로 안의 가능한 정보 압축 지점으로 재해석할 수 있지만, 이것은 추측이며 많은 대질량 은하가 왜 중심 블랙홀을 가지는지는 아직 설명하지 못합니다.
```

### 문서

문서 권한 구조:

- [CLAUDE.md](../../CLAUDE.md)와 [AGENTS.md](../../AGENTS.md)는 에이전트 행동을 정의합니다.
- [Roadmap](../05_next_steps/000_roadmap.md)은 현재 상태, 활성 관문, 막힌 지점의 단일 진실 공급원입니다.
- [Decision Log](decision_log.md)는 결정 이유를 기록합니다.
- [Experiments](../03_experiments/)와 [Results](../04_results/)는 증거를 보관합니다.

유지되는 연구 문서:

- [PROJECT.md](../../PROJECT.md): 문서 관리와 검증 순서
- [docs/README.md](../README.md): 문서 색인과 폴더 지도
- [overview.md](overview.md): 프로젝트 목표, 한계, 모델 계보
- [project_identity.md](project_identity.md): 현재 프로젝트 정체성, 범위, 비목표, 유지-가지 분류, "What We Actually Learned"
- [success_criteria.md](success_criteria.md): 최소/중간/강한 성공 기준과 물리-가지 admission rule
- [qfuds_positioning.md](qfuds_positioning.md): QFUDS 아이디어를 기존 우주론 모델군과 대조
- [concept_survival_audit.md](concept_survival_audit.md): 원래 직관을 현재 증거와 대조한 감사. 강등(demotion)된 가지와 아직 열려 있는 후보를 정리
- [decision_log.md](decision_log.md): 이유와 증거가 포함된 시간순 결정 기록
- [verification_guide.md](verification_guide.md): 현재 검증을 다시 실행하고 읽는 방법
- [frontmatter_convention.md](frontmatter_convention.md): 표준 메타데이터 스키마
- [experiment_record_convention.md](experiment_record_convention.md): 실험/결과 섹션 규칙, 요약 정책, postmortem 정책
- [traceability_matrix.md](traceability_matrix.md): 양방향 주장/증거 추적 색인
- [000_qfuds_v0_1_conceptual_origin.md](../02_theory/000_qfuds_v0_1_conceptual_origin.md): 개념 기원 단계 이론 노트
- [000_qfuds_v0_2_two_phase_background.md](../02_theory/000_qfuds_v0_2_two_phase_background.md): 최소 두 상 유효 유체 이론 노트
- [010_qfuds_v0_3_gamma_laws.md](../02_theory/010_qfuds_v0_3_gamma_laws.md): 물리적 의미를 명시한 $\Gamma(a)$ 전달 법칙 이론 노트
- [015_qfuds_v0_15_phase_transfer_physics.md](../02_theory/015_qfuds_v0_15_phase_transfer_physics.md): 상 전달 물리성 감사
- [030_qfuds_phenomenological_perturbations.md](../02_theory/030_qfuds_phenomenological_perturbations.md): 현상론적 섭동 닫힘 이론 노트
- [000_exp_000_lcdm_baseline.md](../03_experiments/000_exp_000_lcdm_baseline.md): 무전달 LCDM 대조군 실행
- [010_exp_001_gamma_scan.md](../03_experiments/010_exp_001_gamma_scan.md): 전달 법칙 스캔
- [015_exp_001_5_phase_transfer_physicality.md](../03_experiments/015_exp_001_5_phase_transfer_physicality.md): 물리성 관문
- [020_exp_002_entropy_information_gate.md](../03_experiments/020_exp_002_entropy_information_gate.md): 엔트로피/정보원 관문
- [030_exp_003_phenomenological_perturbation_closure.md](../03_experiments/030_exp_003_phenomenological_perturbation_closure.md): 섭동 닫힘 감사
- [030_exp_004_p1_model_family_positioning.md](../03_experiments/030_exp_004_p1_model_family_positioning.md): 유지된 P1의 모델군 위치 감사
- [030_exp_005_timing_prior_usefulness.md](../03_experiments/030_exp_005_timing_prior_usefulness.md): 타이밍 prior 유용성 감사
- [030_exp_006_literature_timing_support_audit.md](../03_experiments/030_exp_006_literature_timing_support_audit.md): 문헌 타이밍 겹침 감사
- [000_result_000_lcdm_baseline.md](../04_results/000_result_000_lcdm_baseline.md): 무전달 기준 결과
- [010_result_001_gamma_scan.md](../04_results/010_result_001_gamma_scan.md): 결과 해석과 다음 표적
- [015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md): 물리성 결과
- [020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md): 엔트로피/정보원 provenance 결과
- [030_result_003_phenomenological_perturbation_closure.md](../04_results/030_result_003_phenomenological_perturbation_closure.md): 섭동 닫힘 결과
- [030_result_004_p1_model_family_positioning.md](../04_results/030_result_004_p1_model_family_positioning.md): 유지된 P1은 상호작용 진공/시간 의존 IDE 사례이지 새 물리 가지가 아님
- [030_result_005_timing_prior_usefulness.md](../04_results/030_result_005_timing_prior_usefulness.md): 유지된 타이밍은 prior-compression 표적으로만 유용함
- [030_result_006_literature_timing_support_audit.md](../04_results/030_result_006_literature_timing_support_audit.md): 문헌 타이밍 겹침은 가능하지만 source derivation은 아님
- [000_experiment_summary.md](../04_results/000_experiment_summary.md): 가벼운 실험별 결론 요약과 postmortem 현황
- [000_roadmap.md](../05_next_steps/000_roadmap.md): 검증 단계, 상태, 막힌 지점
- [010_perturbation_gate.md](../05_next_steps/010_perturbation_gate.md): 섭동 관문
- [015_level_1_5_resolution_gate.md](../05_next_steps/015_level_1_5_resolution_gate.md): Level 1.5 통과, 실패, demotion의 증거 기준
- [030_exp003_record_consistency_gate.md](../05_next_steps/030_exp003_record_consistency_gate.md): Level 2A 섭동 닫힘 기록 일관성 관문

핵심 하네스 기록:

- [006_agentic_research_system_ko.md](../wiki/lineage/006_agentic_research_system_ko.md): 핵심 에이전틱 연구 하네스 기록. 문서·상태 경계, 워크플로 라우팅, 자산 캐시 상태 사다리, PageIndex/MarkItDown MCP, 적대적 검토 패스, 결정론적 깃훅 게이트, 회고 피드백 루프
- [.agent/workflows](../../.agent/workflows/README.md): 이후 에이전트가 따라야 하는 실행 워크플로 SSOT

역사/출처 노트:

- [004_rough_tanh_numerical_sketch_ko.md](../wiki/lineage/004_rough_tanh_numerical_sketch_ko.md): 2단계 대표 문서. 24개 체크포인트 거친 `tanh` 수치 탐색 로그
- [005_rough_tanh_thesis_report_ko.md](../wiki/lineage/005_rough_tanh_thesis_report_ko.md): 선택적으로 읽는 논문 형식 압축본. 효과적 적합, 반증 가능 신호, 이론적 천장을 종합
- [Source-X 조사 색인](../wiki/research/investigations/source_x/README.md): Source-X plans 041-050, Chen Figure 5 수치화, known-model distinction, observer-mode 라우팅, foam-sector feasibility closeout
- [Blocked Admission Rule Gate](../wiki/governance/003_blocked_admission_rule_gate.md): 다섯 항목 physical-branch admission gate
- [Missing Physics Map](../wiki/governance/004_missing_physics_map.md): 물리 가지를 열기 전에 비어 있는 수학 객체 지도
- [concept_origin.md](../01_origin/concept_origin.md): 날것의 정보 흐름 아이디어가 QFUDS 질문이 된 과정
- [README.md](../../README.md): 이 문서의 영어판
- [research_program.md](research_program.md): 초록, 검증 로드맵, 폐기 조건
- [900_qfuds_research_report.md](../02_theory/900_qfuds_research_report.md): 적대적 문헌 비교와 수학적 공식화

### 저장소 검사

문서 frontmatter와 교차 링크를 검증합니다.

```bash
python3 scripts/validate_docs.py        # 또는: make validate
```

저장소 상태 권한 일관성을 검사합니다.

```bash
python3 scripts/research_consistency.py  # 또는: make research-audit
```

주요 실험 마일스톤 전에 전체 preflight 감사를 실행합니다.

```bash
make preflight
```

커밋 전에 같은 문서/회귀 검사를 강제하고 싶다면 로컬 git pre-commit hook을 설치합니다.

```bash
make install-git-hooks
```

이 hook은 검증을 실행하기 전에 staged Markdown frontmatter의 `last_updated`
날짜도 자동으로 갱신합니다.

experiment 004 preflight gate를 실행합니다.

```bash
python3 scripts/preflight_exp004.py
```

이 관문은 [030_exp003_record_consistency_gate.md](../05_next_steps/030_exp003_record_consistency_gate.md)에 문서화되어 있으며 `make preflight-exp004`로도 실행됩니다.

### 참조 문헌

아래 링크들은 결이 비슷한 참조 문헌입니다. QFUDS를 증명하지는 않습니다.

- [Hawking evaporation and the Landauer Principle](https://arxiv.org/abs/2407.08777)
- [Landauer Principle Stands up to Quantum Test](https://physics.aps.org/articles/v11/49)
- [Entanglement Wedge Reconstruction and the Information Paradox](https://arxiv.org/abs/1905.08255)
- [Replica wormholes and the black hole interior](https://arxiv.org/abs/1911.11977)
- [Black hole fireworks: black-to-white-hole tunneling](https://arxiv.org/abs/1407.0989)
- [Small black/white hole stability and dark matter](https://arxiv.org/abs/1805.03872)
- [The Thermodynamics of Black Holes](https://link.springer.com/article/10.12942/lrr-2001-6)
- [Coevolution (Or Not) of Supermassive Black Holes and Host Galaxies](https://arxiv.org/abs/1304.7762)
- [The origins of massive black holes](https://www.nature.com/articles/s42254-021-00364-9)
- [Formation of Supermassive Black Hole Seeds](https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/formation-of-supermassive-black-hole-seeds/DA9F246C7A0C6C1C0E057CCBF40220F6)
- [First M87 Event Horizon Telescope Results IV](https://arxiv.org/abs/1906.11241)
- [First Sagittarius A* Event Horizon Telescope Results III](https://arxiv.org/abs/2311.09479)
- [Cold dark matter: Controversies on small scales](https://pmc.ncbi.nlm.nih.gov/articles/PMC4603506/)
- [Direct Detection of Dark Matter: A Critical Review](https://www.mdpi.com/2073-8994/16/2/201)
- [Planck 2018 cosmological parameters](https://arxiv.org/abs/1807.06209)
- [DESI DR2 results guide](https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/)
- [Unified dark fluid with null sound speed](https://arxiv.org/abs/2509.16155)
