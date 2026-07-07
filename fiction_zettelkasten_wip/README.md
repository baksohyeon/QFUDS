# fiction_zettelkasten_wip

제텔카스텐 파일럿/소스 큐 작업본을 **SSOT 밖에서** 보존하는 폴더다.

## 성격 / 경계

- **Universe / IP**: qfuds-verse (일부 vector-sandbox 포함). 원 위치는
  `docs/wiki/fiction/` 였다.
- **Canon status**: **비정본 · 작업본(WIP)**. 여기의 어떤 파일도 정본이 아니다.
- **SSOT 경계**: 정본 SSOT는 `docs/wiki/fiction/` 이며 `main` 상태를 유지한다.
  이 폴더는 SSOT가 아니고, 문서/픽션 게이트(validate_docs, fiction_gate 등)의
  스캔 범위(`docs/`, `docs/wiki/fiction*`) 밖에 두기 위해 저장소 루트에 있다.
- **Inherited rules**: 원 위치의 규칙을 참고만 한다. 정본 규정으로 승격하려면
  `.agent/workflows/fiction-ip-management-workflow.md` 절차를 거쳐
  `docs/wiki/fiction/` 로 다시 라우팅해야 한다.
- **Local overrides**: 없음. 내용 편집 없이 원본 그대로 보존만 한다.
- **Fiction / provenance 경계**: 픽션 전제는 QFUDS 연구 근거가 아니다.

## 유래(provenance)

- `codex/fiction-zettelkasten-worldbuilding` 브랜치가 `docs/wiki/fiction/`
  (SSOT)에 직접 추가했던 신규 파일 2,915개를 그대로 옮겨 담은 복제본이다.
- 추출 기준 커밋: `70d6c7d` (main 대비 추가된 파일만, baseline 중복 제외).
- SSOT 원본은 되돌림 커밋으로 `main` 상태로 원복됐다.

## 구성

- `02_zettelkasten/` — 원자적 카드 및 소스 큐 (약 2,896개)
- `01_catalog/` — 파일럿 인덱스 / MoC / 인박스
- `10_universes/` — 유니버스 측 신규 파일
