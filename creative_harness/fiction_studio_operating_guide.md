---
doc_id: fiction_studio_operating_guide_ko
title: 범용 SF 창작 스튜디오 운영 가이드
doc_type: guide
stage: reference
status: completed
evidence_role: reference
depends_on:
  - sf_fiction_studio_spec_ko
  - fiction_creative_writing_craft_harness_ko
  - fiction_zettelkasten_intake_method_ko
next_gate: use the lightest production tier on the next real fiction request
last_updated: 2026-07-11
---

# 범용 SF 창작 스튜디오 운영 가이드

이 문서는 “어디에 넣을까”와 “다음에 무엇을 할까”를 한 번에 찾는 실행 입구다.
작품의 사실은 이 문서에 적지 않는다.

## 가장 짧은 사용법

사용자는 정리하지 않고 말해도 된다.

```text
이거 brain dump야. 원문은 남기고 제텔로 정리해줘.
이 기사 소설에 쓸 만해 보여. 사실과 창작적 비약을 분리해줘.
이 seed를 단편으로 시작하자. 아직 결말은 확정하지 마.
이 장면이 안 읽히는 이유만 진단해줘. 고치지는 마.
이 초고를 구조부터 개정하고 마지막에 한국어 윤문해줘.
```

에이전트는 먼저 `mode`와 `tier`를 정하고, 사용자가 요구하지 않은 canon 승격이나
release를 실행하지 않는다.

## 요청 라우터

| 사용자의 말 | Mode | Tier | 기본 결과 |
| --- | --- | --- | --- |
| 메모, 기사, 생각을 넣어 달라 | curator | Quick | inbox 보존, Zettel/seed 후보, routing report |
| 전제·인물·플롯·결말을 잡아 달라 | architect | Quick 또는 Chapter | story contract, 구조 또는 intent |
| 장면이나 원고를 써 달라 | writer | Quick 또는 Chapter | 승인된 intent에 따른 draft |
| 왜 안 읽히는지 봐 달라 | critic 또는 reader-sim | Chapter | 근거가 있는 workshop response |
| 고쳐 달라 | architect → writer → chronicler → polish | Chapter | revision plan, 개정본, memo |
| 설정 충돌을 찾아 달라 | continuity | Chapter | 충돌과 후보 수정안, 자동 승격 없음 |
| 투고·공개 가능한지 봐 달라 | critic → reader-sim → continuity | Release | 고정 baseline에 묶인 release evidence |

## 폴더 라우터

| 내용 | 위치 | 상태 |
| --- | --- | --- |
| 손대지 않은 입력 | `fiction/inbox/` | raw |
| 작품을 넘어 재사용할 생각 | `fiction/knowledge/notes/` | candidate knowledge |
| Zettel 연결 지도 | `fiction/knowledge/maps/` | working map |
| 작품이 될 조합 | `fiction/knowledge/seeds/` | candidate premise |
| 현실 자료와 검증 메모 | `fiction/research/` | fiction research |
| 특정 세계에서 채택한 사실 | `fiction/worlds/<universe-id>/` | provisional 또는 accepted |
| 작품 계약·설계·현재 상태 | `fiction/projects/<work-id>/README.md` | project authority |
| 독자가 읽는 산문 | `fiction/projects/<work-id>/drafts/` | draft |
| workshop·개정·continuity 증거 | `fiction/projects/<work-id>/reviews/` | review evidence |
| 고정 공개 후보와 공개본 | `fiction/projects/<work-id>/release/` | candidate 또는 published |

## 단계별 최소 산출물

### Quick

의도, 결과, 다음 결정만 남긴다. production board를 만들지 않는다.

### Chapter

1. intent card 또는 README 안의 동등한 intent
2. draft 또는 revision
3. workshop response
4. 필요한 경우 revision plan과 memo
5. continuity/chronicler note
6. 관련 검증

### Release

1. production board와 고정 source baseline
2. intent와 workshop
3. revision plan과 revision memo
4. continuity/chronicler evidence
5. retention gate
6. 최종 검증과 남은 위험

기존 문서가 같은 정보를 충분히 담고 있으면 새 파일을 만들지 않고 링크한다.

## 작품 시작과 작업 순서

새 작품은 `fiction/projects/<work-id>/README.md` 하나와 `drafts/`로 시작한다.
README가 Home Note, work bible, 현재 작업 지도다. 설정이 여러 작품에 공유될 때만
`fiction/worlds/`를 만든다. 장편의 상태 추적 비용이 실제로 커진 뒤에만
`tools/story-skills`를 선택한다.

```text
route -> work contract -> SF substitution test -> intent -> draft -> workshop
-> revision plan -> macro revision -> continuity/chronicler -> target-language polish
-> revision memo -> verify
```

## 사용자 개입 지점

- 어떤 seed를 실제 작품으로 채택할지
- 세계 또는 작품 사실을 accepted로 승격할지
- 상충하는 workshop 의견 중 무엇을 따를지
- 결말·장르 계약·언어·공개 여부를 바꿀지

그 밖의 분류, 링크, 문서 생성, 일관성 검사, 승인된 범위의 개정은 에이전트가
진행할 수 있다.

## 완료 보고와 검증

완료 보고에는 mode와 tier, 변경 파일, review/revision 증거, canon 후보와 승인
상태, 실행한 검증, 남은 위험, 다음 결정 하나만 담는다.

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/check_markdown_link_targets.py creative_harness .agent .agents fiction tools/saga-fiction-studio
python3 scripts/fiction_gate.py
python3 scripts/agent_workflow_guard.py --staged
sh scripts/git-hooks/pre-commit
```
