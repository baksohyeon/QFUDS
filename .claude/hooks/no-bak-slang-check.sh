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
  *feedback_korean_no_bak_slang.md) exit 0 ;;
  *MEMORY.md) exit 0 ;;
  *docs/wiki/postmortem/temp/*) exit 0 ;;
  *docs/wiki/postmortem/*) exit 0 ;;
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

# Whitelist: "못을 박-" = 리터럴 못질(망치로 못을 박다). 영어 직역 슬랭이 아니므로 허용.
#   스캔용 사본에서만 그 자리의 "박"을 지워 매치를 막는다(원문은 그대로 저장됨).
#   조사 없는 복합 "못박-"(못박는다 등)은 건드리지 않아 슬랭으로 계속 잡힌다.
CONTENT=$(printf '%s' "$CONTENT" | sed -E 's/못을 박/못을 /g')

# Detect "박-" slang patterns (동사 박다/박히다 활용 + 처박-/들이박- 류 복합).
# 핵심: "박" 이 어절 첫 음절일 때만 슬랭 → `(^|[^가-힣])박` 로 앞 한 글자를
#   "줄 시작 또는 비-한글" 로 강제. 이게 lookbehind 를 순수 ERE 로 흉내낸 것.
# → 도박/압박/박사/대박/반박/수박/호박 등 "박" 이 명사 안에 들어있는 단어는 전부 제외.
#   (예: 도박은 / 압박은 / 도박이다 = 명사+조사, 오탐 방지)
# 순수 grep -oE 만 사용 → macOS BSD grep · Linux/WSL · Windows Git Bash(GNU grep) 모두 동작.
#   (lookbehind/lookahead 가 필요 없어 perl·python·grep -P 의존성 없음.)
# 활용형: 박다/고/지/는(다)/아(서/야/도/라/두/놓/진/졌/버)/어(서/야/도)/은/을/음/
#         으(면/니/려/며/세/러)/았(다/어/고/던/지/네/으)/겠/둔/혀(...)/혔(...)/히(...)/힌/힘.
# 알려진 한계: 박음질(재봉)·박음 명사형은 미세 오탐 가능 — 이 프로젝트(색조) 에선 거의 안 나옴.
# 긴 어미를 앞에 둬 leftmost-longest 안정화 (박는다>박는, 박았다>박았).
# 접두 어절(prefix) 목록: 한글 음절이 앞에 붙는 "박-" 슬랭 복합을 잡으려면 여기에
#   명시해야 한다(`[^가-힣]` 앵커가 한글 앞글자를 막기 때문). 미포함 시 누락됨.
#   못박-(못박는다 등 = 고정/명시로 대체), 갈아박-/쑤셔박-/욱여박-/우겨박-(쑤셔넣기
#   슬랭)을 추가. 명사 박(도박/압박/반박/결박/속박/박사/박수/박자 등)은 prefix에
#   없으므로 여전히 제외된다.
BAK_RE='(^|[^가-힣])(내리|들이|뒤|되|처|쳐|못|갈아|쑤셔|욱여|우겨)?박(는다|는|다|고|지|네|나|아서|아야|아도|아라|아두|아놓|아진|아졌|아버|아|어서|어야|어도|어|은|을|음|으면|으니|으려|으며|으세|으러|았다|았어|았고|았던|았지|았네|았으|았|겠|둔|혀서|혀요|혀있|혀버|혀두|혀놓|혀도|혀야|혀|혔다|혔어|혔고|혔던|혔지|혔|히다|히고|히면|히니|히는|히어|히었|히게|히며|히|힌|힘)'
# grep -oE 매치는 앞 비-한글 1글자를 포함 → sed 로 떼어내고 dedup.
MATCHES=$(printf '%s' "$CONTENT" | grep -oE "$BAK_RE" | sed -E 's/^[^가-힣]+//' || true)
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
