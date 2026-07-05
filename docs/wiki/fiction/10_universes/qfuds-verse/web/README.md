# QFUDS Verse — 세계관 코덱스 (web)

QFUDS Verse 유니버스의 3D 딥타임 코덱스. 디자인 프로토타입(Claude Design,
DCLogic/React 런타임)을 **의존성 없는 바닐라 JS 단일 페이지**로 실제 구현한 것.

## 무엇을 하나

- **⟐ 성좌** — 73개 기록을 three.js 3D 그래프로. 게임식 해금: 2008 비트코인 하나에서
  시작 → "판독 완료"를 누르면 인접 신호가 해금. 진행은 localStorage에 저장.
  미해금 노드는 "미확인 신호"로만 보이고, 하단 레일로 시대 점프.
- **≡ 연대기 / ◇ 인물 / ⊞ 체계 / ⌘ 사전** — 정사·후보 기록을 문서 뷰로. 상태 뱃지
  (캐논·후보·제안·미정)로 구분, ⟐ 칩으로 성좌의 해당 노드로 이동.
- **⌬ 아카이브 질의** — 설정 문서 기반 Q&A. 캐논에 없으면 「미정」이라 정직하게 답함.
  **승격 모드**를 켜면 답변 대신 레포 커밋용 `.md` 초안(frontmatter + `depends_on`)을 생성.
- **🌱 시드 보관함** — 대화(세션)를 시드로 저장 → `.md` 내보내기 → 문서 승격 재료로.

## 구조

```
index.html          # 셸 + CSS (엔트리; = "qfuds.html" 디자인 구현)
app.js              # 바닐라 JS 컴포넌트 (three.js 씬 + 5개 뷰 + 질의 + 시드)
data/lore-data.js       # 성좌 노드 + 질의/승격 시스템 프롬프트
data/chronicle-data.js  # 연대기·인물·체계·사전 데이터
vendor/three.min.js # r152 (로컬 벤더링, 오프라인)
fonts/              # IBM Plex Sans KR / Mono woff2 (로컬 셀프호스트)
server.js           # 정적 서빙 + 선택적 /api/query(Gemini 프록시). 의존성 0
Dockerfile          # Dokku가 감지해서 빌드
DEPLOY.md           # 배포 절차 (Dokku / systemd / docker)
```

## 질의(Q&A)는 어디서 되나

`app.js`가 순서대로 시도한다:

1. `window.claude.complete` — Claude Design 미리보기 안. 키 불필요.
2. `POST ./api/query` — 홈서버. `GEMINI_API_KEY` 설정 시 Gemini로 응답.
3. 둘 다 없으면 — "이 환경에선 질의 불가" 친절 안내로 폴백(나머지 기능은 전부 동작).

## 데이터 갱신

세계관 문서가 바뀌면 `data/*.js` 를 갱신하면 된다. 각 항목의 `st`(상태) 뱃지와
`nodes`/`links` 참조만 지키면 성좌·문서 뷰가 자동 반영된다. 출처 문서는 상위
[README](../README.md) 참고.
