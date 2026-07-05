# QFUDS Verse Codex — 배포 가이드

`docs/wiki/fiction/10_universes/qfuds-verse/web/` 의 자기완결 앱.
성좌(3D)·연대기·인물·체계·사전 + 시드 보관함 + 아카이브 질의.

- **런타임**: 의존성 0개 Node 서버(`server.js`) — 정적 코덱스 서빙 + 선택적 `/api/query`(Gemini 프록시).
- **오프라인**: three.js·IBM Plex 폰트 전부 로컬 벤더링. 인터넷 없이 동작(질의 기능만 키 필요).
- **엔트리**: `index.html` (= "qfuds.html" 디자인의 실제 구현). 서버가 `/` 로 서빙.

로컬 실행:

```bash
cd docs/wiki/fiction/10_universes/qfuds-verse/web
node server.js            # http://localhost:5000
# 질의까지 테스트하려면:
GEMINI_API_KEY=xxxxx node server.js
```

---

## Dokku 배포 (홈서버, `git push dokku main`)

앱이 레포 루트가 아니라 서브디렉터리라, Dokku에 **build-dir**만 알려주면 됩니다.
(레포 전체를 푸시해도 이 폴더만 빌드 컨텍스트로 씀 → 폴더 안 `Dockerfile` 감지.)

```bash
# 1) 앱 생성 + 빌드 디렉터리 지정 (최초 1회)
ssh dorito@100.117.91.34 sudo dokku apps:create qfuds-fiction
ssh dorito@100.117.91.34 sudo dokku builder:set qfuds-fiction build-dir docs/wiki/fiction/10_universes/qfuds-verse/web

# 2) (선택) 질의 켜기 — Gemini 키. 없으면 질의만 비활성, 나머지 전부 동작
ssh dorito@100.117.91.34 sudo dokku config:set qfuds-fiction GEMINI_API_KEY=xxxxx
#   모델 바꾸려면: ... config:set qfuds-fiction GEMINI_MODEL=gemini-2.0-flash

# 3) 리모트 추가 + 배포
git remote add dokku dokku@100.117.91.34:qfuds-fiction   # 이미 있으면 생략
git push dokku main

# 4) 컨테이너 포트(5000)를 호스트 포트로 매핑
ssh dorito@100.117.91.34 sudo dokku ports:set qfuds-fiction http:<PORT>:5000
```

> 키를 절대 레포/커밋에 넣지 않습니다. 서버는 `process.env.GEMINI_API_KEY` 만 읽어요.
> `.env` 는 `.gitignore` 처리돼 있습니다.

### nginx location (homelab-portal 규칙 그대로)

`/etc/nginx/conf.d/00-default-vhost.conf`:

```nginx
location = /qfuds-fiction { return 301 /qfuds-fiction/; }
location /qfuds-fiction/ {
  proxy_pass http://127.0.0.1:<PORT>/;   # 끝 슬래시가 /qfuds-fiction/ 프리픽스를 벗겨줌
  proxy_set_header Host $host;
}
```

```bash
sudo nginx -t && sudo systemctl reload nginx
```

> 앱은 **모든 자산 경로가 상대경로**(`./app.js`, `./api/query` …)라, `/qfuds-fiction/`
> 서브패스 밑에서 그대로 동작합니다. 절대경로(`/app.js`)는 쓰지 않습니다.

### 포털 한 줄

`~/dev/homelab-portal/index.html` 의 `qfuds-fiction/ … soon` 자리를 실제 링크로 바꾸고 `./deploy.sh`.

---

## 대안 (Dokku 안 쓸 때)

같은 `server.js` 가 그대로 돕니다.

```bash
# systemd (최소 풋프린트)
node server.js            # ExecStart=/usr/bin/node server.js, Environment=GEMINI_API_KEY=…, PORT=…

# docker
docker build -t qfuds-codex . && docker run -p 8080:5000 -e GEMINI_API_KEY=xxx qfuds-codex

# 순수 정적(질의 없이)만 원하면 web/ 를 아무 정적 서버로 서빙해도 됩니다
python3 -m http.server 8080   # 질의는 '이 환경에선 불가' 안내로 폴백
```

## 환경변수

| 변수 | 기본값 | 설명 |
| --- | --- | --- |
| `PORT` | `5000` | 리스닝 포트 |
| `GEMINI_API_KEY` | (없음) | 설정 시 아카이브 질의/승격 모드 활성. 미설정 시 정적 + 폴백 안내 |
| `GEMINI_MODEL` | `gemini-2.0-flash` | 질의에 쓰는 Gemini 모델 |

## 튜닝 파라미터 (URL 쿼리)

| 파라미터 | 예 | 효과 |
| --- | --- | --- |
| `?unlockAll=1` | 전체 해금(스포일러 전부 열람) |
| `?autoRotate=0` | 자동 회전 끔 |
| `?starDensity=2000` | 별 밀도(200–3000) |
