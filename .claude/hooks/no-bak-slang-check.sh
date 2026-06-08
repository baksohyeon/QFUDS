#!/bin/bash
# no-bak-slang-check.sh — PreToolUse hook (Write|Edit):
# 한국어 마크다운에서 "박-" 영어 직역 슬랭 (embed/stick-in/insert 류) 차단.
# Why: .agent/korean-persona.md § 어휘 anti-pattern. 한국어 기술 글의 번역체 신호 강함.
# 사용자가 강하게 거슬려 함. 발견 시 deny → 대체 어휘 (넣다 / 추가하다 / 적어두다 /
# 명시하다 / 들어있다 / 기록하다 / 끼워두다) 로 재작성.

set -euo pipefail

INPUT=$(cat)

# Self-skip — hook 본인 / anti-pattern 정의 문서 / 한국어 사전 파일 / postmortem 은 검사 제외
# (이유: 정의 자체에 슬랭 단어가 예시로 등장. self-deadlock 방지.
#  postmortem 은 hook 차단 사례를 *메타-인용* 으로 적어야 하는 곳.)
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
case "$FILE_PATH" in
  *.claude/hooks/*) exit 0 ;;
  *.codex/hooks/*) exit 0 ;;
  *.agent/korean-persona.md) exit 0 ;;
  *MEMORY.md) exit 0 ;;
esac

# 검사 대상 파일 확장자 (한국어 마크다운만)
case "$FILE_PATH" in
  *.md|*.txt|*.mdx) ;;
  *) exit 0 ;;
esac

# Write 의 .content 또는 Edit 의 .new_string 추출
CONTENT=$(echo "$INPUT" | jq -r '
  .tool_input.content //
  .tool_input.new_string //
  empty
')

[ -z "$CONTENT" ] && exit 0

# Detect "박-" slang patterns
# - 박는다 / 박는 (현재형)
# - 박았다 / 박았 / 박았어 (과거형)
# - 박혔어 / 박혔다 (과거 수동)
# - 박은 (관형사형)
# - 박힌 / 박혀 (수동 관형형/연결형)
# - 박둔 / 박아두 (보존형)
MATCHES=$(echo "$CONTENT" | grep -oE "박[는아혔어은힌둔]|박혀|박힌|박아두" || true)
MATCHES=$(echo "$MATCHES" | sort -u | head -5 | tr '\n' ',' | sed 's/,$//')

if [ -n "$MATCHES" ]; then
  jq -n --arg matches "$MATCHES" '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: ("[Hook] \"박-\" 영어 직역 슬랭 금지 (.agent/korean-persona.md § 어휘 anti-pattern). 대체: 넣다 / 추가하다 / 적어두다 / 명시하다 / 들어있다 / 기록하다 / 끼워두다. 발견: " + $matches)
    }
  }'
fi

exit 0
