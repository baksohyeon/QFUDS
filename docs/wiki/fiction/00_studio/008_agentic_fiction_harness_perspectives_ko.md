---
doc_id: agentic_fiction_harness_perspectives_ko
title: 에이전틱 픽션 하네스 4관점 정리
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - fiction_ip_management_system_ko
  - fiction_gsd_harness_operator_guide_ko
next_gate: keep in sync with fiction-ip-management-workflow updates
last_updated: 2026-06-21
---

# 에이전틱 픽션 하네스 4관점 정리

이 문서는 QFUDS 픽션 제작 시스템을 네 관점에서 설명한다. 같은 하네스를
**에이전트·작가·독자·협업**이 각각 어떻게 보는지 분리해 두면, 새 세션이나
새 사람이 자기 위치에서 무엇을 보고 무엇을 해야 하는지 바로 안다.

전체 규칙의 단일 출처는
[Fiction IP Management Workflow](../../../.agent/workflows/fiction-ip-management-workflow.md)
이고, 이 문서는 그 규칙을 관점별로 풀어 쓴 안내서다. 충돌하면 워크플로우가 이긴다.

## 0. 한 장의 그림

```text
세계(IP)            qfuds-verse
  └ 작품(시리즈)     qfuds-saga
       ├ 00_workroom    작가실 운영 규칙·하네스
       ├ 00_bible       설정 기준서(세계·인물·과학 경계)
       ├ 10_story_design 기획·아웃라인·반전 설계
       ├ 20_drafts      편집 가능한 원본 원고(SSOT)
       ├ 30_revisions   퇴고·release 통제 계획
       └ 40_release     통과된 release manifest/export
```

핵심 한 줄: **20_drafts가 원본이고, 40_release는 release가 통과됐을 때만 manifest/export를 둔다.**
수기 조립 원고를 계속 유지하지 않는다.

## 1. 에이전트 관점 (무엇이 자동으로 막히나)

에이전트는 규칙을 "기억"하지 않는다. 규칙은 코드와 훅으로 강제된다.

- **하드 게이트 (커밋 차단).** `scripts/fiction_gate.py --staged`가 pre-commit에
  연결돼 있다. 독자용 산문에서 em dash(한·영)와 민감한 사회·정치 주제 용어가
  발견되면 커밋이 막힌다.
- **소프트 게이트 (작성 시점).** `.claude/settings.json`의 PreToolUse 훅이 이모지·
  특정 한국어 비속어가 든 Write/Edit를 거부하고, UserPromptSubmit 훅이 한국어
  문체 규칙과 리서치 워크플로우를 매 턴 상기시킨다.
- **검증 에이전트.** `ai-tell-detector`, `naturalness-reviewer`,
  `content-fidelity-auditor`가 release 전 AI 티·자연스러움·의미 보존을 감사한다.
- **집필 전 프리플라이트.** `00_workroom/005`가 "반복 인물 시트 없으면 집필 금지",
  "선언된 POV·연재 스레드·앙상블 연계" 같은 시리즈 게이트를 둔다.

에이전트가 할 일: 워크플로우를 먼저 읽고, 게이트를 우회하지 말고, 막히면 규칙에
맞게 고친다. 게이트가 막는 것은 결함이 아니라 설계다.

## 2. 작가(사용자) 관점 (내 아이디어가 어디 사는가)

작가는 "내가 준 생각이 어디 들어갔고, 무엇을 보면 되는지"만 알면 된다.

- **읽고 싶다** -> 각 SAGA README의 current reading path를 본다. reboot 중이면
  `20_drafts`의 prototype 읽기 순서가 우선이다.
- **설정을 알고 싶다** -> `00_bible/`(010 인과 스파인, 016 인물부터).
- **기획·전개를 보고 싶다** -> `10_story_design/`.
- **내 아이디어가 어디 갔나** -> `00_workroom/006` 추적 원장.
- **무엇을 어디에 두나** -> 이 README의 라우팅 표와 승격 규칙.

작가가 새 아이디어를 줄 때: 브레인스토밍은 `10_story_design`, 굳어진 세계 사실은
`00_bible`, 실제 장면은 `20_drafts`로 간다. 어느 서랍인지 모르면 `00_workroom/006`과
README 라우팅 표를 본다.

## 3. 독자 관점 (완성본만 본다)

독자에게 보이는 것은 통과된 `40_release` 산출물뿐이다. release가 아직 없거나
reboot 중이면 독자용 active release가 없다고 표시하고, prototype은 작업장 경로로
분리한다.

- `40_release/001`-`099`는 active release manifest/export로 예약한다.
- `40_release/900`-`999`는 archived/provenance release metadata로만 쓴다.
- 독자 체감 품질은 **리텐션 테스트**로 측정한다. 다양한 독자 페르소나가 "흥미가
  유지되는 동안만" 읽고 이탈 지점을 보고하며, 공통 이탈 원인을 고친 뒤 다시
  돌린다. 이 테스트 통과가 release의 조건이다(release 게이트).

## 4. 협업 관점 (소스와 빌드를 헷갈리지 않기)

여러 세션·여러 에이전트가 같은 작품을 건드릴 때의 규칙.

- **원본은 하나다.** 원고를 고칠 때는 항상 `20_drafts`를 고친다. release shelf의
  export 산출물은 직접 고치지 않는다.
- **release 생성.** 드래프트가 release gate를 통과했을 때만 `40_release`에
  manifest/export를 만든다. generated manuscript가 필요하면 source hash와 생성 절차를
  함께 남긴다.
- **canon 충돌은 bible이 기준.** 드래프트가 설정과 어긋나면 bible(`00_bible`)을
  기준으로 맞추거나, bible을 의도적으로 갱신한다. 어느 쪽인지 명시한다.
- **추적성.** 작가 입력의 출처는 `00_workroom/006`이 보관한다. 새 입력이 들어오면
  그 표를 갱신한다.

## 왜 이렇게까지 하나

단편 한 편은 머릿속 규칙으로도 됐다. 시리즈로 가자 같은 규칙이 매번 지켜지지 않아
세계관 구멍·균질한 인물 목소리·반복 구조·AI 티가 누적됐다. 원인은 도구가 없어서가
아니라 도구가 강제되지 않아서였다. 그래서 규칙을 훅과 게이트로 옮겨 사람이 잊어도
시스템이 막게 했다. 이 문서는 그 시스템을 관점별로 읽는 지도다.
