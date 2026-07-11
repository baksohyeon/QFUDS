---
doc_id: fiction_zettelkasten_intake_method_ko
title: Zettelkasten 기반 fiction intake 방법
doc_type: guide
stage: reference
status: completed
evidence_role: reference
depends_on:
  - sf_fiction_studio_spec_ko
next_gate: process one real brain dump through capture, distill, connect, seed, and project promotion
last_updated: 2026-07-11
---

# Zettelkasten 기반 fiction intake 방법

## 목적

사용자가 정리되지 않은 생각, 기사, 문장 조각을 넣으면 에이전트가 후보와 확정을
섞지 않고 창작 시스템으로 조립한다. 사용자는 중간 단계의 Zettel, seed, project
map을 직접 고치고 채택할 수 있어야 한다.

## 구조 원리

```text
Zettelkasten: 작품을 초월해 생각을 분해·연결하며 발산
World / Series Bible: 특정 세계에서 채택한 사실을 기억
Project: 선택한 생각을 장면과 원고 순서로 수렴
```

제텔카스텐에 canon과 원고를 전부 넣지 않는다. 세계 Bible을 아이디어 공장으로
쓰지 않는다. project가 원본 Zettel을 링크하며, 원본을 복사하거나 이동하지 않는다.

## 입력 계약

사용자는 다음처럼 최소한으로 지시할 수 있다.

```text
이거 brain dump야. fiction inbox에 넣고 생각 단위로 증류해줘.
이 기사 SF에 쓸 만해 보여. 출처 확인하고 재사용 아이디어와 작품 후보를 나눠줘.
이 Zettel들을 연결해서 story seed 세 개만 만들어줘. canon으로 확정하지 마.
이 seed를 실제 단편 project로 승격하자. README 작업 지도를 만들어줘.
```

## 처리 순서

### 1. Capture

원문과 출처를 source id와 함께 보존한다. 기사, PDF, 웹 페이지는 Fiction Source
Intake Workflow를 적용해 URL, source state, allowed anchor, blocked claim을
기록한다. QFUDS 연구 주장을 만들 때만 별도의 연구 workflow를 실행한다.

### 2. Distill

원문에서 재사용 가능한 생각을 한 논지씩 자기 말로 쓴다.

```yaml
---
type: zettel
kind: idea | question | pattern | principle | technique | observation
created: YYYY-MM-DD
source-ids: []
related-notes: []
related-projects: []
---
```

노트 길이가 아니라 독립적으로 다시 쓸 수 있는 사고 단위인지 본다.

### 3. Connect

비슷한 노트뿐 아니라 긴장을 만드는 노트와 연결한다. 링크 옆에 관계와 이유를 쓴다.

```text
supports | contradicts | extends | causes | exemplifies | transforms
```

### 4. Form a story seed

여러 Zettel 사이에 인물과 갈등이 생겼을 때만 seed를 만든다.

필수 항목:

- premise candidate
- source Zettels
- possible conflict
- speculative change와 예상 비용
- unknowns
- promotion blocker

### 5. Promote to project

사용자가 실제로 쓸 작품으로 채택했을 때 `fiction/projects/<work-id>/README.md`를
만든다. README는 자동 대시보드가 아니라 작가가 직접 배열하는 Home Note다.

최소 항목:

- premise, form, genre, target reader
- inherited world 또는 standalone
- source Zettels / research
- central conflict와 ending hypothesis
- open questions
- current next action 하나

### 6. Linearize

아이디어를 독자가 읽을 순서로 장면화한다. 짧은 작품은 README의 scene list와
`drafts/`만으로 충분하다. 장편에서 실제 관리 비용이 생기면 `tools/story-skills`의
chapter, scene, continuity schema를 선택형으로 도입한다.

## 최소 자동화 원칙

- 세 번 이상 반복해서 귀찮았던 작업만 자동화한다.
- Graph는 관계 진단 도구이지 작품 구조의 증거가 아니다.
- Canvas는 작업대다. 중요한 결정은 Markdown에 확정한다.
- Obsidian Bases는 properties 기반 목록이 필요할 때만 쓴다.
- 플러그인을 제거해도 Markdown과 파일 순서가 의미를 유지해야 한다.
- 자동 분류가 사용자의 채택 결정을 대신하지 않는다.

## Source Boundary

사용자 제공 조사문은 2026-07-10 기준 작가 사례, Obsidian, Zettelkasten 자료의
종합 메모로 제공됐다. 이번 작업에서 원문의 모든 외부 사례를 독립 재검증하지는
않았으므로 작가별 세부 폴더 구조를 현재 사실로 재인용하지 않는다.

직접 확인한 자료:

| Source | Allowed use | Blocked use | State |
| --- | --- | --- | --- |
| [Obsidian Vault](https://obsidian.md/help/vault) | vault가 로컬 폴더이며 여러 vault를 둘 수 있다는 기본 구조 | 특정 fiction 폴더 구조의 보증 | `hit_not_cached` |
| [Obsidian Bases](https://obsidian.md/help/bases) | Markdown properties를 정렬·필터·편집하는 core plugin | 자동 대시보드가 창작 품질을 높인다는 주장 | `hit_not_cached` |
| [Obsidian Backlinks](https://obsidian.md/help/plugins/backlinks) | linked / unlinked mentions로 사용처를 역추적 | 링크가 관계 의미를 자동 설명한다는 주장 | `hit_not_cached` |
| [Obsidian Graph](https://obsidian.md/help/plugins/graph) | 내부 링크 관계 시각화와 orphan 진단 | 아름다운 graph가 명확한 소설 구조라는 주장 | `hit_not_cached` |
| [Obsidian Canvas](https://obsidian.md/help/plugins/canvas) | 노트·자료·웹을 2D 공간에 배치하고 관계 label 사용 | text card만으로 최종 SSOT를 대체 | `hit_not_cached` |
| [Zettelkasten Method for Fiction](https://zettelkasten.de/fiction/) · [story tools](https://zettelkasten.de/posts/zettelkasten-fiction-writing-part-3-tools-analysing-story/) | fiction 분석·생성을 돕는 thinking tool과 story tool 구조 | 유일하거나 정통인 fiction workflow 주장 | `hit_not_cached` |

사용자 제공 조사문의 허용 용도는 `Zettelkasten / World Bible / Project` 분리와
과잉 자동화 경계의 설계 입력이다. 개별 작가의 현재 작업 방식이나 Obsidian
플러그인 성능을 검증한 사실로 재사용하지 않는다.
