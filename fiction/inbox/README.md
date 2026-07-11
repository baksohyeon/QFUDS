# Inbox

문장 조각, 질문, 이미지, 꿈, 음성 메모, 기사 링크처럼 아직 분류하지 않은
원재료를 잠시 둔다. 사용자는 정리하지 않은 채 넣어도 된다.

가장 간단한 사용법:

```text
"오, 이거 소설에 쓸 만한 기사 같다. fiction/inbox에 넣고 정리해줘."
"이 생각 brain dump 할게. 후보와 확정을 섞지 말고 분류해줘."
"이 메모에서 재사용 가능한 생각만 Zettel로 증류해줘."
```

에이전트는 원문을 바로 canon이나 원고로 바꾸지 않는다.

```text
capture
-> source/provenance 확인
-> 재사용 가능한 생각은 knowledge
-> 현실 자료는 research
-> 특정 세계의 채택 사실은 worlds의 candidate
-> 특정 작품의 장면·플롯은 projects의 candidate
-> 가치가 없으면 폐기 제안
```

원문은 기본 보존하고 `SRC-YYYYMMDD-<slug>` source id를 붙인다. 처리 결과와
파생 Zettel은 이 id와 원문 경로를 링크한다. 웹 기사나 외부 자료는 URL, allowed
anchor, blocked claim, workflow state를 먼저 기록한다. 삭제나 archive는 사용자
승인 뒤에만 한다. Inbox는 장기 저장소가 아니지만 자동 폐기 큐도 아니다.
