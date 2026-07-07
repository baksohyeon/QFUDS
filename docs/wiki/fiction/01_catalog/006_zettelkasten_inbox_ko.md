---
doc_id: qfuds_verse_zettelkasten_inbox_ko
title: QFUDS Verse 제텔카스텐 아이디어 인박스
doc_type: index
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_verse_zettelkasten_moc_ko
next_gate: convert inbox items only through source-linked zettel cards or chronicler pass
last_updated: 2026-07-07
---

# QFUDS Verse 제텔카스텐 아이디어 인박스

```text
fiction/provenance only
research evidence: no
canon action: capture only
```

## 목적

사용자가 한 번에 덤프하는 세계관·인물·장면·제도 아이디어를 바로 canon으로 밀어 넣지
않고 보류하는 인박스다. 이 문서는 정리 전 임시 보관소이며, 항목 자체는 설정 확정이
아니다.

## 처리 규칙

1. 덤프는 먼저 `raw idea`로 둔다.
2. 기존 문서에서 근거를 찾으면 `source-linked candidate`로 바꾼다.
3. 기존 문서에 없지만 쓸 만하면 story design 또는 chronicler pass 후보로 둔다.
4. canon을 바꾸는 아이디어는 해당 도메인 권위 문서로 보내기 전까지 승격하지 않는다.
5. 모르는 것은 `unknown`으로 둔다. 빈칸을 추정으로 채우지 않는다.

## Capture Queue

| ID | raw idea | status | route | note |
| --- | --- | --- | --- | --- |
| inbox-001 | 사용자가 다음 루프에서 덤프할 새 세계관 아이디어 | empty | pending | 여기에 추가한다 |

## 상태값

| status | 뜻 |
| --- | --- |
| `raw idea` | 아직 출처·위치·canon_state가 없다 |
| `source-linked candidate` | 기존 문서 근거가 있으나 canon 승격은 아니다 |
| `story seed` | 장면 압력으로 쓸 수 있으나 원고에 직접 넣기 전 intent/card 필요 |
| `unknown` | 일부러 보류한다 |
| `routed` | zettel, story design, chronicler pass, bible 중 하나로 이동했다 |

## 사용 가드

이 인박스는 작가의 발화와 새 아이디어를 잃지 않기 위한 장치다. 여기 적힌 문장을
그대로 세계관 사실로 취급하지 않는다.
