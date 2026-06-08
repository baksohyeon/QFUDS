#!/bin/bash
# remind-korean-style.sh — UserPromptSubmit hook:
# 매 사용자 turn 시작 시 한국어 어휘 anti-pattern 룰을 system context 에 주입.
# 어시스턴트가 응답 만들기 전에 매번 읽음. 100% 차단은 아니지만 자기검열 빈도 강화.
# Why: file-level 차단 (.claude/hooks/no-bak-slang-check.sh) 만으로는 CLI 응답을 못 잡음.

python3 - <<'PY'
import json

additional_context = """[Korean-style reminder]
한국어 응답·문서 작성 시 "박-" 영어 직역 슬랭 금지.
금지: 박는다 / 박았다 / 박혀 / 박힌 / 박둔 / 박아두.
대체: 넣다 / 추가하다 / 적어두다 / 명시하다 / 들어있다 / 기록하다 / 끼워두다.
응답에 위 패턴이 있으면 조용히 대체어로 고친다. 검증했다는 말은 출력하지 않는다.
상세 매핑 표: .agent/korean-persona.md § 어휘 anti-pattern."""

print(json.dumps({
    "hookSpecificOutput": {
        "hookEventName": "UserPromptSubmit",
        "additionalContext": additional_context,
    },
}, ensure_ascii=False))
PY
