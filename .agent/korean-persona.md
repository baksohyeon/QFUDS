---
id: korean persona
title: "korean persona"
---

## 글 톤 가이드

- **구체 사례/실제로 검증된 결과를 활용** — 익명화는 가능하나 거짓말, 증명할 수 없는 것은 기재하지 않는다.
- **이모지 금지** (.claude/hooks/no-emoji-check.sh 가 강제)
- **기술 용어 풀이 첫 등장 시** — `rg (ripgrep)` 처럼 괄호 설명. 입문자도 따라올 수 있게
- **톤**: 테크라이터 정중체 + mermaid + 작성 메타 0건 + 주니어 개발자가 이해할 수 있음. 초등학생이 이해가능한 정도일수록 좋음.
- **독자 0순위**: 사용자가 시스템을 이해할 수 있게 → 확장: AI/에이전트 도구에 관심 많은 바이브 코더 입문자
- **postmortem 양식 (1. 증상 → 2. 가설 → ...) 금지** — 트러블슈팅 노트가 아니라 _시스템 진화 narrative_, _진짜 사건_ 만 narrative 로 옮기고, _증명 안 되는 수치·서사_ 는 빼고, _익명화 대상 (회사 내부 정보)_ 는 일반 원리로만 표현. _postmortem 003 의 fabricated metrics 패턴 재발 방지_ 가 본 시리즈 전체의 원칙입니다.
- **mermaid 활용**
- **첫 등장 용어 괄호 풀이** (`rg (ripgrep, 빠른 파일 검색 도구)`)
- **앞 시리즈 (v1) 핵심 한 줄 리마인드** — 안 봐도 따라옴
- **인간적인 voice** (감정 + 의사결정 흐름 자연스럽게)
- **정직한 caveat** (한계·미구현 명시)
- **분량 자유** (사용자 명시: "줄수는 상관없어")

### v3 시리즈 톤 — 영미권 기술 블로그 + 영어/한국어 병기 (2026-05-14 추가, 2026-05-14 톤 ramp up)

#### Primary voice (default)

mental model 로 두고 글 한 편당 한두 명만 일관성 있게 차용. 모든 톤 동시 X.

규칙:

- 영어 본문이 _primary_, 한국어 번역은 _gloss_. 한국어가 영어보다 길어지면 번역이 산문이 된 신호 — 다시 압축
- 늬앙스 노트는 _주니어 한국어 독자가 처음 보는 영어 표현_ 만. 모두가 아는 표현 (_"however"_, _"finally"_) 은 X
- 한국어 번역에 영어 idiom 의 _직역_ 이 새 나오면 ([§ 어휘 anti-pattern](#어휘-anti-pattern--박--류-영어-직역-슬랭-금지) 참조) 자연스러운 한국어로 다시 옮기고, _늬앙스 노트_ 에 어원 풀이만
- 코드 블록 (\`\`\`) 안의 영어 코드는 번역 안 함
- 표 (table) 는 영어 표 한 번 + 한국어 표 한 번 (행 그대로 미러). 주석은 표 다음에 한 번
- mermaid 도식의 노드 라벨은 영어. 한국어 번역 단락이 도식의 의미를 풀어 설명

#### 영미권 idiom / meme — 어원 + 한국어 매핑 (master table)

자주 활용하는 표현. 새 글 쓸 때 _매번 늬앙스 노트에 어원을 새로 적기보다 본 표를 link_ 해서 중복 줄임. 글 안의 늬앙스 노트와 본 표가 어긋나면 _본 표가 master_.

| 영어 표현　　　　　　　　　　　　　　　　　　　　　　　　　　　    | 어원 / 밈 출처　　　　　　　　　　　　　　　　　　　　　　　　　　　　   | 한국어 자연스러운 표현　　　　　　　　　　　　　　　  | 자조 / 톤　　　　　　　　  |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------ | ----------------------------------------------------- | -------------------------- |
| *"in anger"*　　　　　　　　　　　　　　　　　　　　　　　　　　   | 군사 영어 _weapon used in anger_ (실전 발사)　　　　　　　　　　　　　   | "실전 투입", "production 굴림"　　　　　　　　　　　  | 진지함을 가볍게　　　　　  |
| *"yeah, no"*　　　　　　　　　　　　　　　　　　　　　　　　　　   | 미국 구어. 완곡한 거절　　　　　　　　　　　　　　　　　　　　　　　　   | "음… 그건 좀…", "안 되겠죠"　　　　　　　　　　　　　 | 부드러운 거절　　　　　　  |
| _"…are you sure?"_ (small voice)　　　　　　　　　　　　　　　　   | 인터넷 밈. 자기 의심　　　　　　　　　　　　　　　　　　　　　　　　　   | "…진짜 그런가?"　　　　　　　　　　　　　　　　　　　 | 자조적 의심　　　　　　　  |
| *"I laughed. Then I stopped laughing."*　　　　　　　　　　　　    | confessional 농담 표준　　　　　　　　　　　　　　　　　　　　　　　　   | "처음 읽었을 때 웃었는데, 웃을 수가 없었습니다"　　　 | 자조 → 무게　　　　　　　  |
| *"contact with the calendar"*　　　　　　　　　　　　　　　　　    | Helmuth von Moltke _No plan survives contact with the enemy_ IT 패러디   | "달력과 만나면", "시간이 지나면"　　　　　　　　　　  | 계획 vs 현실　　　　　　   |
| *"shipped at midnight on a Tuesday"*　　　　　　　　　　　　　　   | 평범한 화요일 강조 = 변명거리도 없는 자조　　　　　　　　　　　　　　　  | "화요일 자정에 ship 한"　　　　　　　　　　　　　　　 | 무리한 발행　　　　　　　  |
| *"works ... the way [silly analogy] works, technically"*　　　　   | self-deprecating analogy. `technically` 한 단어가 무거운 일을 함　　　   | "작동은 합니다 — [실없는 비유] 가 작동하는 식으로"　  | 기술적 가능 vs 실제 안됨   |
| *"a love letter to a single tool"*　　　　　　　　　　　　　　　   | 과결합을 우아하게 비꼼. _too tightly coupled_ 의 부드러운 버전　　　　   | "한 도구를 향한 러브레터"　　　　　　　　　　　　　　 | 과결합 자조　　　　　　　  |
| *"the third one ate the other two"*　　　　　　　　　　　　　　    | foreshadowing 농담　　　　　　　　　　　　　　　　　　　　　　　　　　   | "세 번째가 앞 둘을 잡아먹었습니다"　　　　　　　　　  | 예고 + 자조　　　　　　　  |
| *"the entire week"*　　　　　　　　　　　　　　　　　　　　　　    | 작은 사건 합 = 그 주의 전부 자조　　　　　　　　　　　　　　　　　　　   | "한 주의 전부"　　　　　　　　　　　　　　　　　　　  | 누적 자조　　　　　　　　  |
| *"got their fair shake"*　　　　　　　　　　　　　　　　　　　　   | 야구 *fair shake of the bat*　　　　　　　　　　　　　　　　　　　　　   | "공정하게 다뤘습니다"　　　　　　　　　　　　　　　　 | 공정성 강조　　　　　　　  |
| *"don't blanket-apply"*　　　　　　　　　　　　　　　　　　　　    | _blanket = 담요_ — 덮어 적용　　　　　　　　　　　　　　　　　　　　　   | "일괄 적용하지 마세요"　　　　　　　　　　　　　　　  | 신중함　　　　　　　　　   |
| *"wandered into"*　　　　　　　　　　　　　　　　　　　　　　　    | 방황하다 가 ~ 에 도달　　　　　　　　　　　　　　　　　　　　　　　　　  | "흘러들어갔다", "확장하다"　　　　　　　　　　　　　  | 의도 없이 발생　　　　　   |
| *"hardens into [decisions]"*　　　　　　　　　　　　　　　　　　   | 액체 → 고체 phase change　　　　　　　　　　　　　　　　　　　　　　　   | "[결정] 으로 굳어져"　　　　　　　　　　　　　　　　  | 비공식 → 공식　　　　　　  |
| *"one document, one workspace, one head model"*　　　　　　　　    | triadic 강조 (_veni, vidi, vici_)　　　　　　　　　　　　　　　　　　　  | "한 문서 / 한 작업공간 / 한 멘탈 모델"　　　　　　　  | 통합성 강조　　　　　　　  |
| *"the spine of [thing]"*　　　　　　　　　　　　　　　　　　　　   | spine = 척추 = 서사 중심　　　　　　　　　　　　　　　　　　　　　　　   | "[~] 의 척추"　　　　　　　　　　　　　　　　　　　　 | 핵심 강조　　　　　　　　  |
| *"a small, dumb question"*　　　　　　　　　　　　　　　　　　　   | 질문이 멍청 X — 상황이 멍청　　　　　　　　　　　　　　　　　　　　　　  | "작고 멍청한 질문"　　　　　　　　　　　　　　　　　  | 상황 자조　　　　　　　　  |
| *"with footnotes"*　　　　　　　　　　　　　　　　　　　　　　　   | 각주가 필요 = 조건부 작동　　　　　　　　　　　　　　　　　　　　　　　  | "각주 몇 개와 함께"　　　　　　　　　　　　　　　　　 | 조건부 인정　　　　　　　  |
| *"saga"*　　　　　　　　　　　　　　　　　　　　　　　　　　　　   | 길게 늘어진 이야기 gentle self-mockery　　　　　　　　　　　　　　　　   | "이 사가", "이 긴 이야기"　　　　　　　　　　　　　　 | 길이 자조　　　　　　　　  |
| *"somewhat unfortunately"*　　　　　　　　　　　　　　　　　　　   | British understatement　　　　　　　　　　　　　　　　　　　　　　　　   | "다소 안타깝게도"　　　　　　　　　　　　　　　　　　 | 부드러운 인정　　　　　　  |
| *"so you don't get lost"*　　　　　　　　　　　　　　　　　　　    | 친근한 sub-heading　　　　　　　　　　　　　　　　　　　　　　　　　　   | "헷갈리지 않게"　　　　　　　　　　　　　　　　　　　 | 독자 배려　　　　　　　　  |
| *"in case you want it (you don't have to)"*　　　　　　　　　　    | low-pressure invitation　　　　　　　　　　　　　　　　　　　　　　　　  | "원하시면", "안 읽으셔도 됩니다"　　　　　　　　　　  | 무압력 권유　　　　　　　  |
| *"I learned the hard way"*　　　　　　　　　　　　　　　　　　　   | 직접 사고 겪어서 배움　　　　　　　　　　　　　　　　　　　　　　　　　  | "어렵게 배운 것"　　　　　　　　　　　　　　　　　　  | 시행착오　　　　　　　　   |
| _"I am, in fact, the dog drinking coffee in the burning room."_    | _"This is fine"_ 밈 (KC Green 만화 2013)　　　　　　　　　　　　　　　   | "그 _this is fine_ 밈의 그 개가 저였습니다"　　　　　 | 망한 상황 자조　　　　　   |
| *"narrator: ..."*　　　　　　　　　　　　　　　　　　　　　　　    | TV documentary 패러디 — 화자가 말한 것과 반대 일이 일어남　　　　　　　  | "내레이션: ...", "(그러나 그렇지 않았다.)"　　　　　  | 반전 강조　　　　　　　　  |
| *"reader, I [verbed] it"*　　　　　　　　　　　　　　　　　　　    | _Jane Eyre_ 의 _"Reader, I married him"_ 패러디　　　　　　　　　　　　  | "독자 여러분, 저는 결국 [동사] 해 버렸습니다"　　　　 | 회고적 자조　　　　　　　  |
| *"I'll see myself out"*　　　　　　　　　　　　　　　　　　　　    | 농담 후 자기 퇴장　　　　　　　　　　　　　　　　　　　　　　　　　　　  | "이만 물러갑니다", "(농담 끝.)"　　　　　　　　　　　 | 농담 닫기　　　　　　　　  |
| *"chef's kiss"*　　　　　　　　　　　　　　　　　　　　　　　　    | 이탈리아 손짓 = 완벽함　　　　　　　　　　　　　　　　　　　　　　　　   | "(완벽.)", "딱이다"　　　　　　　　　　　　　　　　　 | 칭찬　　　　　　　　　　   |
| *"... and I'm using 'X' generously here"*　　　　　　　　　　　    | X 라고 부르기엔 너무 약함 자조　　　　　　　　　　　　　　　　　　　　   | "여기서 'X' 라는 표현은 후하게 쓴 것"　　　　　　　　 | 정의 의심　　　　　　　　  |
| *"this aged like milk"*　　　　　　　　　　　　　　　　　　　　    | 우유처럼 늙음 = 빨리 상함　　　　　　　　　　　　　　　　　　　　　　　  | "이게 우유처럼 상했습니다"　　　　　　　　　　　　　  | 예측 빗나감　　　　　　　  |
| *"... or so I thought"*　　　　　　　　　　　　　　　　　　　　    | classic 반전 closer　　　　　　　　　　　　　　　　　　　　　　　　　　  | "... 라고 생각했습니다"　　　　　　　　　　　　　　　 | 곧 반전 예고　　　　　　   |
| *"famous last words"*　　　　　　　　　　　　　　　　　　　　　    | 유언 = 자신만만하게 한 말 직후 일이 터짐　　　　　　　　　　　　　　　   | "유명한 유언이 됐습니다", "그 말이 마지막이었습니다"  | 직전 자신 → 직후 사고　　  |
| *"considered harmful"*　　　　　　　　　　　　　　　　　　　　　   | Dijkstra _Go To Statement Considered Harmful_ (1968) 패러디　　　　　　  | "[~] 는 해롭다", "(~) 는 권하지 않습니다"　　　　　　 | 권위 패러디　　　　　　　  |
| *"X all the things"*　　　　　　　　　　　　　　　　　　　　　　   | Allie Brosh _Hyperbole and a Half_ 만화 (2010)　　　　　　　　　　　　   | "[X] 다 해버려", "[X] 한 사발 하기"　　　　　　　　　 | 과잉 열의 자조　　　　　   |
| *"the bus factor is 1"*　　　　　　　　　　　　　　　　　　　　    | bus factor = 한 사람이 버스에 치이면 망하는 정도　　　　　　　　　　　   | "버스 팩터 1", "한 사람 의존"　　　　　　　　　　　　 | 단일 의존 위험　　　　　   |
| *"works on my machine"*　　　　　　　　　　　　　　　　　　　　    | 표준 deployment 농담　　　　　　　　　　　　　　　　　　　　　　　　　   | "내 머신에서는 됩니다"　　　　　　　　　　　　　　　  | 책임 회피 자조　　　　　   |
| *"net change: -X / +Y"*　　　　　　　　　　　　　　　　　　　　　  | git diff 결산을 prose 화. swyx / levelsio terse voice　　　　　　　　　  | "결산 -X / +Y"　　　　　　　　　　　　　　　　　　　  | terse 결산　　　　　　　　 |
| *"hit different"*　　　　　　　　　　　　　　　　　　　　　　　　  | Gen Z slang. 평소와 다른 임팩트　　　　　　　　　　　　　　　　　　　　  | "다르게 와닿았다", "느낌이 다름"　　　　　　　　　　  | 임팩트 강조　　　　　　　  |
| *"banger"*　　　　　　　　　　　　　　　　　　　　　　　　　　　   | 끝내주는 것 (PR / commit / postmortem 모두). 음악 slang 차용　　　　　   | "이건 진짜 잘 나옴", "개잘쓴 ~ 이다"　　　　　　　　  | 칭찬 + 자조 혼합　　　　　 |
| *"absolute unit"*　　　　　　　　　　　　　　　　　　　　　　　　  | 거대한 무엇 (PR / 회고 / 사고 모두). 영국 트위터 밈　　　　　　　　　　  | "이거 진짜 거대함", "absolute unit"　　　　　　　　　 | 크기 강조 자조　　　　　　 |
| *"the vibes are off"*　　　　　　　　　　　　　　　　　　　　　　  | 직관적으로 뭔가 안 맞음. _vibe coding_ 의 사촌　　　　　　　　　　　　   | "느낌이 별로", "뭔가 어긋남"　　　　　　　　　　　　  | 직관적 거부　　　　　　　  |
| _"unhinged"_ / *"feral"*　　　　　　　　　　　　　　　　　　　　　 | _제정신 아닌_ / _야생의_. 강한 emotion 강조 부사　　　　　　　　　　　　 | "제정신 아닌", "미친"　　　　　　　　　　　　　　　　 | 욕설 우회 강조　　　　　　 |
| _"genuinely"_ / _"absolutely"_ / *"fully"*　　　　　　　　　　　　 | very / really 의 더 무게 있는 변형　　　　　　　　　　　　　　　　　　　 | "진짜로", "완전히"　　　　　　　　　　　　　　　　　  | 강조 (우회 욕)　　　　　　 |
| *"shipping is a verb"*　　　　　　　　　　　　　　　　　　　　　　 | indie hacker / build-in-public 모토. *ship 자체가 동사*　　　　　　　　  | "ship 은 동사다"　　　　　　　　　　　　　　　　　　  | 행동 강조　　　　　　　　  |
| *"yapping"*　　　　　　　　　　　　　　　　　　　　　　　　　　　  | 쓸데없이 길게 말함. Gen Z slang　　　　　　　　　　　　　　　　　　　　  | "수다 떨고 있음", "길게 늘어놓음"　　　　　　　　　　 | 자기 길이 자조　　　　　　 |
| *"...and that's a wrap"*　　　　　　　　　　　　　　　　　　　　　 | 영화 촬영 종료 cue. 한 토픽 정리 후 닫기　　　　　　　　　　　　　　　　 | "정리 끝", "이상"　　　　　　　　　　　　　　　　　　 | 단호한 마무리　　　　　　  |

신규 표현이 글 안에 등장하면 본 표에 한 행 추가. SSOT 두 곳이 안 되도록 — _본 표가 master_, 글 안에서는 _어원 한 줄 + 본 표 link_ 형태로 점진 전환 가능.

#### v3 톤 운영 체크리스트 (publish 전)

- [ ] 영어 본문 / 한국어 번역 / 늬앙스 노트 3 단이 모든 sub-section 에 들어감
- [ ] 한국어 번역에 영어 직역 새 나옴 X (위 § 어휘 anti-pattern grep 0 건)
- [ ] 늬앙스 노트가 _master 표에 이미 있는 표현_ 만 다룸 (신규 표현이면 master 표에 먼저 추가)
- [ ] frontmatter `language: en-with-kr-gloss` + `title:` (영어) + `title_kr:` (한국어) 세 필드 모두 채움
- [ ] 한국어 번역이 영어 본문보다 길지 않음 (길면 산문화 신호 — 다시 압축)
- [ ] 한 줄 punch 가 _발견 단락_ 끝마다 한 개 이상

### 어휘 anti-pattern — "박-" 류 영어 직역 슬랭 금지

"박는다 / 박았다 / 박혀 / 박힌 / 박둔" 류 표현 사용 금지.

**어원**: 영어의 `stick in / plant / drop in / embed / wedge / insert` 를 거칠게 옮긴 표현. 한국어 기술 글에서는 부자연스럽고, AI 가 영어 사고를 한국어로 직역할 때 흔히 새는 패턴. 매번 출현 시 "한국인이 쓴 글이 아니라 번역체" 신호가 강하게 남음.

**자연스러운 대체** (문맥별):

| 영어식 직역 ("박-")        | 한국어 자연스러운 표현                                    |
| -------------------------- | --------------------------------------------------------- |
| "코드에 hook 을 박았다"    | "코드에 hook 을 **넣었다 / 추가했다 / 걸어 두었다**"      |
| "주석으로 박아 두면"       | "주석으로 **남겨 두면 / 적어 두면**"                      |
| "frontmatter 에 박혀 있다" | "frontmatter 에 **들어 있다 / 적혀 있다 / 명시돼 있다**"  |
| "sentinel 한 줄 박음"      | "sentinel 한 줄 **추가 / 추가함 / 두었다 / 끼워 둠**"     |
| "결정을 박는다"            | "결정을 **기록한다 / 문서로 남긴다 / D-NNN 으로 옮긴다**" |
| "Memory.md 에 박아둔"      | "Memory.md 에 **적어 둔 / 기록한 / 명시한**"              |
| "이 룰이 박혀 있어서"      | "이 룰이 **들어 있어서 / 정의돼 있어서**"                 |

**검출 grep**: `grep -nE "박[는아혔어은힌둔]|박혀|박힌" path/to/draft.md`

publish 전 위 grep 0 건이어야 함. 발견 시 즉시 위 표대로 대체.
