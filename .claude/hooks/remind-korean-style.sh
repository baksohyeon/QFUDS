#!/bin/bash
# remind-korean-style.sh — UserPromptSubmit hook:
# 매 사용자 turn 시작 시 한국어 어휘 anti-pattern 룰을 system context 에 주입.
# 어시스턴트가 응답 만들기 전에 매번 읽음. 쓰기 차단이 아니라 문체 reminder 로만 작동.

python3 - <<'PY'
import json

additional_context = """[Korean-style reminder]
한국어 응답·문서·소설 작성 시 "박는다/박았다/박혀 있다"를 영어식 stick/embed/insert 만능 직역어로 남발하지 않는다.
기술·절차 문맥 대체: 넣다 / 추가하다 / 적어두다 / 명시하다 / 들어있다 / 기록하다 / 끼워두다.
소설 문맥에서는 실제 못질, 말뚝, 충돌, 신체 동작, 의도적 강한 비유의 박다 / 박았다 / 박혀 / 박힌은 허용한다.
검증했다는 말은 출력하지 않는다. 상세 매핑 표: .agent/korean-persona.md § 어휘 anti-pattern."""

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": additional_context,
    },
}, ensure_ascii=False))
PY
