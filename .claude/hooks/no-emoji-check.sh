#!/bin/bash
# no-emoji-check.sh — PreToolUse hook (Write|Edit): block emojis from being written
# Why: .agent/Memory.md Corrections 행 = "기술 글·문서 작성 시 이모지 금지" (2026-04-27).
# 사용자가 강하게 금지함. 이 hook 가 Write/Edit 의 도구 입력을 검사해 강제.
# 발견 시 텍스트 대안 (안 됨, 금지, 가능, 주의 등) 으로 다시 쓰도록 deny.

set -euo pipefail

INPUT=$(cat)

# Self-skip:
# 1. hook 인프라 파일 (.claude/hooks/*) — hook 본인 코드의 unicode 정의가 본인 검사에 걸려 deadlock
# 2. postmortem 글 (docs/wiki/postmortem/temp/*) — hook 차단 사례를 *메타-인용* 으로 적어야 하는 곳.
#    인용 시 차단 대상 글자가 본문에 들어가는 게 의도된 동작이므로 검사 제외.
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // empty')
case "$FILE_PATH" in
  *.claude/hooks/*) exit 0 ;;
  *.codex/hooks/*) exit 0 ;;
  *docs/wiki/postmortem/temp/*) exit 0 ;;
  *docs/wiki/postmortem/*) exit 0 ;;
esac

# Extract content from Write (.content) or Edit (.new_string) tool inputs.
CONTENT=$(echo "$INPUT" | jq -r '
  .tool_input.content //
  .tool_input.new_string //
  empty
')

if [[ -z "$CONTENT" ]]; then
  exit 0
fi

# Detect emojis. Unicode ranges:
# - U+1F000 to U+1FAFF: 본격 emoji block (얼굴 / 음식 / 동물 등)
# - U+2600  to U+27BF : misc symbols / dingbats (체크 / 경고 / 별 등)
# - U+2B00  to U+2BFF : misc symbols / arrows (블록 사각형 등)
# Excluded on purpose: 화살표 (U+2190-U+21FF), 곱셈 기호 (U+00D7) — 기술 글 자주 씀.
#
# Resolve a working python interpreter (.githooks/pre-commit 와 동일 분기).
# Windows: `python3` 가 MS Store stub 으로 PATH 에 잡히면 GUI installer 가 떠
# hook 가 fail. 진짜 `python` 으로 fallback.
PYTHON3="python3"
if command -v python3 >/dev/null 2>&1; then
  case "$(command -v python3)" in
    */WindowsApps/python3*) PYTHON3="python" ;;
  esac
else
  PYTHON3="python"
fi

# Fail-closed: detector ($PYTHON3) 실패 시 deny — 검사기 못 돌면 이모지가
# 슬쩍 통과할 위험이 있어 안전 차단. stderr 는 임시 파일로 분리 capture 해서
# 사용자에게 원인 보임.
TMPERR=$(mktemp)
trap 'rm -f "$TMPERR"' EXIT

if ! EMOJIS=$(echo "$CONTENT" | "$PYTHON3" -c "
import sys, re
content = sys.stdin.read()
pattern = re.compile('[\U0001F000-\U0001FAFF☀-➿⬀-⯿]')
matches = pattern.findall(content)
if matches:
    seen = []
    for c in matches:
        if c not in seen:
            seen.append(c)
    print(','.join(seen[:5]))
" 2>"$TMPERR"); then
  ERR_MSG=$(cat "$TMPERR")
  jq -n --arg err "$ERR_MSG" '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: ("[Hook] no-emoji-check.sh detector 실행 실패 — 안전 차단 (fail-closed). 원인: " + $err + ". python3/python 가 PATH 에 있는지 / 입력 인코딩 확인.")
    }
  }'
  exit 0
fi

if [[ -n "$EMOJIS" ]]; then
  jq -n --arg emojis "$EMOJIS" '{
    hookSpecificOutput: {
      hookEventName: "PreToolUse",
      permissionDecision: "deny",
      permissionDecisionReason: ("[Hook] 이모지 금지 — 텍스트 대안 사용 (안 됨, 금지, 가능, 주의 등). 발견: " + $emojis)
    }
  }'
fi

exit 0
