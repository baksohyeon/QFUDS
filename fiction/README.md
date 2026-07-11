# Fiction knowledge vault

이 선반은 QFUDS 연구 증거가 아닌 창작 지식만 보관한다.

## 구조

- [Inbox](inbox/README.md): 아직 분류하지 않은 원재료
- [Knowledge / Zettelkasten](knowledge/README.md): 작품을 넘어 재사용할 수 있는 생각, 구조 지도, story seed
- [Research](research/README.md): 핍진성을 위한 현실 자료와 이해
- [Worlds](worlds/README.md): 허구 세계에서 현재 참으로 채택한 사실
- [Projects](projects/README.md): 특정 작품의 설계와 원고

Zettelkasten은 생각을 발산하고, 세계 문서는 채택한 사실을 기억하며, 프로젝트는
선택한 생각을 장면과 원고 순서로 수렴한다. 지식 선반은 자동 원자화 큐가 아니다.

정리되지 않은 입력은 그대로 [Inbox](inbox/README.md)에 넣고 `brain dump로
처리해줘`라고 지시할 수 있다. 에이전트는 raw→Zettel→seed→project 후보를 나누며,
사용자의 중간 수정과 promotion 결정을 기다린다.

## Inbox 라우팅 질문

Inbox는 장기 저장소가 아니다. 각 항목을 다음 질문으로 판별해 이동하거나
버린다.

1. 다른 작품에서도 쓸 생각인가? → `knowledge/`
2. 실제 세계에 대한 조사인가? → `research/`
3. 특정 허구 세계에서 참인 사실인가? → `worlds/`
4. 특정 작품의 플롯·인물·장면인가? → `projects/`
5. 어디에도 해당하지 않는가? → 사용자가 삭제 또는 archive를 승인할 때까지 inbox 보존

## 경계

창작 운영 하네스는 [creative_harness](../creative_harness/README.md)와
`.agent/`, `.agents/`, `tools/`에 있다. 픽션 문서는 QFUDS 물리 연구의
근거가 아니다.

## 이행 기록

2026-07-10에 SAGA 원고·초고·리비전·릴리스·레거시 아카이브를 활성 트리에서
제거했다. 복구가 필요하면 Git 이력의 기준 커밋을 사용한다.
