---
doc_id: postmortem-005-research-asset-digitization-automation
id: postmortem-005-research-asset-digitization-automation
seq: 5
title: "Research asset digitization 자동화 시행착오 포스트모템"
doc_type: postmortem
type: postmortem
stage: reference
status: reference
wiki_status: active
evidence_role: provenance
depends_on:
  - postmortem-001-li-2025-data-cache
  - workflow-research-asset-product
  - workflow-research-asset-digitization
next_gate: use digitization workflow before any future paper-source parse or figure extraction claim
date: 2026-06-11
context: Source-X and Exp006 research asset cache cleanup after PageIndex, MarkItDown, and figure-rendering automation
audience: 주니어 개발자
length: 작업 단계별 풀어쓰기
created_at: 2026-06-11
created_by: dorito
updated_at: 2026-06-11
updated_by: dorito
last_updated: 2026-06-11
last_verified_at: 2026-06-11
last_verified_by: dorito
audit_log:
  - action: created
    at: 2026-06-11
    by: dorito
    note: "Recorded the follow-up incident after multi-paper asset digitization was moved from ad hoc MarkItDown attempts into the PageIndex and figure-handling workflow."
  - action: updated
    at: 2026-06-11
    by: dorito
    note: "Folded omitted agent execution details into the body (section 3.4 chen TeX draft-superset trap and lineweaver raster-vs-vector figures; section 5 Abbott 75-page composition and literal-vs-condensed scope; section 6 mount rm/chmod delete constraint, stray-file policy, validator frontmatter/link failure modes) and rewrote Appendix C as a purpose-grouped command cheat sheet per the postmortem skill (one file, appendix at end)."
tags: [postmortem, digitization, pageindex, markitdown, research-assets]
relations:
  - docs/wiki/postmortem/001-20260609-dorito-li-2025-data-cache.md
  - .agent/workflows/README.md
  - .agent/workflows/research-asset-product-workflow.md
  - .agent/workflows/research-asset-digitization-workflow.md
  - docs/wiki/research/assets/README.md
code_refs:
  - file: .agent/workflows/README.md
    note: "Workflow index updated so agents route cached asset digitization work to the new digitization workflow."
  - file: .agent/workflows/research-asset-digitization-workflow.md
    note: "New workflow created from the incident lessons: PageIndex for paper PDFs, MarkItDown for non-paper assets, TeX-based figure mapping, high-resolution rendering, and coverage audit."
  - file: .agent/workflows/research-asset-product-workflow.md
    note: "SSOT for asset state ladder, product-availability claims, and repository asset layout."
  - file: docs/wiki/postmortem/001-20260609-dorito-li-2025-data-cache.md
    note: "Earlier incident that exposed PDF/source asset handling failures and motivated the stricter workflow."
  - file: docs/wiki/research/assets/README.md
    note: "Repository asset cache index and directory convention used by the digitization workflow."
---

# Research asset digitization 자동화 시행착오 포스트모템

[001-20260609-dorito-li-2025-data-cache](docs/wiki/postmortem/001-20260609-dorito-li-2025-data-cache.md) 회고 덕분에 "PDF를 못 읽었는데 문헌을 확인했다고 말하는 문제"는 빨리 잡았다. 이번 사건은 그 다음 단계였다. 여러 논문과 data-release asset(논문 본문이 아니라 데이터·표·코드·README 같은 공개 릴리스 묶음)을 한 번에 Markdown(LLM과 검색이 읽기 쉬운 구조화 텍스트), source text(원본에서 추출한 텍스트), figure PNG(논문 그림을 PNG 이미지로 렌더링한 파일), image reference(Markdown 안의 이미지 링크)까지 정리하려고 하면서, 처음에는 MarkItDown과 caption 추정에 기대다가 PageIndex, TeX source(논문 조판 원본), 고해상도 figure rendering(그림 PDF를 고해상도 이미지로 바꾸는 작업), coverage audit(빠진 본문·그림·링크가 없는지 세는 점검)로 절차를 다시 세운 사건이다. 동시에 흩어진 asset 폴더를 논문/릴리스 단위 구조로 다시 묶고, `.agent/workflows/`를 agent 절차의 SSOT(single source of truth, 단일 기준 문서)로 고정한 파일 구조 정리 사건이기도 하다.

이 문서는 새 실험이 아니다. roadmap status를 바꾸지 않고, Level 2B를 열지 않으며, 어떤 문헌 overlap도 QFUDS support로 승격하지 않는다. 산출물의 최대 의미는 `source_text_parse`와 figure-level inspection asset이다.

또한 이 문서는 논문 본문이나 source code를 보존하는 장소가 아니다. 회고에는 원문을 길게 인용하지 않고, 어떤 확인이 어떤 판단을 바꿨는지만 남긴다.

## 0. 사전 지식

| 용어                    | 이 사건에서의 의미                                                                                                                                                                                    |
| ----------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| MarkItDown              | PDF, HTML, TXT, JSON, notebook 등을 Markdown으로 바꾸는 범용 변환 도구. 논문 PDF 전문에는 line order(줄 순서), equation(수식), figure reference(그림 참조)가 깨질 수 있다.                            |
| PageIndex               | 논문 PDF를 페이지/섹션 단위로 구조화해서 읽는 MCP(Model Context Protocol, 외부 도구 연결 규격) 기반 문서 처리 도구. 이번에는 paper-PDF 전문과 outline(섹션 구조) 추출 경로로 사용했다.                |
| `source_text_parse`     | 논문 본문, 섹션, caption(그림·표 설명), equation(수식)을 검색하고 검토할 수 있는 text-level parse(원문 구조를 텍스트로 옮긴 상태). 숫자 digitization(수치를 표/CSV로 뽑는 작업)은 아니다.             |
| figure mapping          | 논문 Figure 번호와 실제 source figure 파일을 연결하는 작업. PageIndex caption 순서가 아니라 TeX `\includegraphics{...}`(TeX 원고의 그림 삽입 명령)가 권위 소스다.                                     |
| data-release asset      | 논문 본문이 아니라 Zenodo README, JSON metadata(기계 판독용 설명 데이터), notebook(실행 가능한 분석 노트), CSV, figure archive, code manifest 같은 release 자료. 이 경우 MarkItDown이 적합할 수 있다. |
| asset layout convention | `docs/wiki/research/assets/<paper_or_release_key>/{source,figures,digitization}/` 구조. 원본, 렌더링 figure, derived Markdown(원본에서 만든 파생 Markdown)을 같은 논문/릴리스 key 아래에 둔다.        |
| draft superset          | 출판본보다 더 많은 draft용 figure, filename, caption이 들어 있는 TeX source 상태. TeX가 항상 published PDF와 1:1로 맞지 않을 수 있다는 경고다.                                                        |
| compiled PDF            | TeX source를 조판해 실제 독자가 보는 최종 PDF. draft superset 의심이 있으면 이 PDF와 교차검증한다.                                                                                                    |
| frontmatter             | Markdown 파일 맨 위의 `---` YAML metadata block. 이 repo에서는 `doc_id`, `title`, `doc_type` 같은 필드가 validator 입력이다.                                                                          |

## 1. 증상

처음 증상은 하나가 아니었다. 겉으로는 사용자의 요구가 매 턴 늘어난 것처럼 보였지만, 실제로는 "충실한 research asset digitization"의 정의가 처음부터 맞지 않았다.

관찰된 문제는 네 가지였다.

1. MarkItDown으로 논문 PDF를 처리했을 때 본문 구조, figure reference, equation 탐색 품질이 충분하지 않았다.
2. PageIndex caption 순서만 보고 figure 번호를 매핑하면서 Amendola 2024와 Farrah 2023 figure 연결이 틀렸다.
3. 일부 figure PDF를 낮은 해상도 PNG로 둔 뒤에야 digitization 입력으로 부족하다는 점이 드러났다.
4. Abbott 2023처럼 긴 문서를 agent가 임의로 요약 범위에 가두면서, "전체 전문 처리" 요구를 한 번에 충족하지 못했다.
5. asset 폴더 역할도 초반에는 category 중심으로 흔들렸다. 같은 논문 자료가 `source`, `figures`, `digitization` 관점으로 흩어지면 추적이 더 어려워진다.
6. MarkItDown과 PageIndex의 역할 차이를 처음부터 명시하지 않아서, PDF 논문 전문 변환과 TXT/HTML/data-release 변환이 같은 문제처럼 취급됐다.

사용자가 제공한 Claude cowork 회고도 같은 패턴을 짚었다.

```text
그림 매핑을 추측했다.
화질 기준을 처음에 안 잡았다.
abbott를 임의로 축소하고 "못 한다"고 프레이밍했다.
```

권한 `600` 가설도 있었지만, 이것은 핵심 재발방지 항목으로 보지 않는다. Claude cowork GUI와 mount 동작의 인터페이스 문제였고, 이번 repository workflow의 중심 실패는 figure/source/digitization 절차였다.

### 1.1 사용자 prompt trail

이번 사건은 agent가 처음부터 정확한 workflow를 알고 처리한 사례가 아니다. 사용자의 prompt가 각 분기점에서 작업 기준을 바꿨다. 그래서 이 문서는 prompt를 별도 모음으로 몰아두지 않고, 아래 진단과 결론 섹션의 해당 분기점에 원문 인용을 배치한다.

전체 흐름은 결국 같은 기준을 가리켰다.

```text
충실한 digitization =
repo-local source cache
+ paper/release key 구조
+ full text parse
+ source figure mapping
+ high-resolution figure PNG
+ working Markdown image references
+ explicit evidence-state label
```

## 2. 첫 의문 + 가설

| 가설                                                                             | 왜 그럴 수 있는지                                                                  | 어떻게 확인할지                                                                                       |
| -------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- |
| H1. MarkItDown 하나로 paper-PDF 전문 변환까지 충분하다                           | Markdown 파일은 생성되므로 겉으로는 성공처럼 보인다                                | paper Markdown에서 섹션 순서, figure link, equation, caption을 원문과 대조한다                        |
| H2. 논문 PDF는 PageIndex가 기본 경로여야 한다                                    | 논문은 페이지/섹션 구조와 수식이 중요하고 PDF line order가 깨질 수 있다            | PageIndex structure/full-text output과 MarkItDown 결과를 역할별로 분리한다                            |
| H3. figure 번호는 PageIndex caption 순서로 매핑해도 된다                         | PageIndex가 figure caption을 순서대로 보여주면 번호와 파일을 연결할 수 있어 보인다 | arXiv `.tex`의 `\includegraphics{...}`와 `\caption{...}` block을 확인한다                             |
| H4. figure PNG는 일단 보이면 충분하다                                            | 브라우저나 editor preview에서는 작은 이미지도 보인다                               | `identify`나 파일 크기로 digitization에 쓸 해상도인지 확인한다                                        |
| H5. 긴 논문은 요약본만 만드는 것이 합리적이다                                    | token과 작업량을 아끼려는 압력이 있다                                              | workflow의 default가 full text인지, 사용자가 범위를 축소했는지 확인한다                               |
| H6. txt/html/data-release 자료도 PageIndex로 처리해야 한다                       | 모든 문서를 같은 도구로 처리하면 단순해 보인다                                     | asset을 `paper-PDF`와 `data-release`로 나누고 MarkItDown 적용 대상을 제한한다                         |
| H7. asset folder는 자료 종류별 category로 나눠도 된다                            | `figures/`, `digitization/`, `source_x/` 같은 이름은 직관적으로 보인다             | 같은 논문의 raw source, extracted figure, Markdown output이 한 key 아래에 모이는지 확인한다           |
| H8. MarkItDown과 PageIndex는 둘 다 Markdown을 만들기 때문에 결과 품질도 비슷하다 | 산출물 확장자가 같으면 같은 evidence state처럼 보인다                              | PDF 논문, HTML/TXT, data-release 각각에서 section order, equation, table, figure reference를 비교한다 |

확인 순서는 비용이 낮고 재발 가능성이 큰 것부터 잡았다. 먼저 현재 repo에 어떤 asset과 digitization 산출물이 생겼는지 확인하고, 그 다음 workflow가 그 산출물의 품질 기준을 실제로 표현하는지 봤다.

## 3. 진단: 실제 상태 확인

### 3.1 asset 폴더가 논문/릴리스 단위로 정리됐는지 확인

이 분기점은 사용자가 repo 구조를 먼저 보라고 여러 번 밀어붙인 데서 시작했다.

> `@docs/wiki/research/ 여기 구조 참고해서 가져와야지`

> `아니 li_2025_desi_dr2_sign_reversal_ide.md 를 보라고 @docs/wiki/research/assets/exp006_timing/li_2025/`

> `시벌 리서치 폴더 제대로 처음부터 정리해.`

이 prompt들은 "새 구조를 만들지 말고 이미 repo에 있는 research tree와 Li 2025 precedent를 먼저 읽으라"는 의미였다.

`docs/wiki/research/assets/` 바로 아래를 확인했다. 여기에는 논문 또는 데이터 릴리스 key가 와야 하고, `figures/`, `digitization/`, `source_x/` 같은 category folder가 오면 안 된다.

확인 결과 asset root에는 `The population of merging compact binaries inferred using gravitational waves through GWTC-3`(GWTC-3 population release), `Cosmological Budget of Entropy from Merging Black Holes`(Chen, Jani, and Kephart 2026), Farrah/Croker/Lacy/Li 계열 논문, Lineweaver entropy-budget chapter 같은 논문/릴리스 단위 folder가 있었다. 같은 유형의 확인은 `find ... -maxdepth 1 ... | sort` 형태로 반복했다.

판정:

- H6은 지지된다. asset은 논문/릴리스 단위 key 아래에 있고, 각 asset 안에서 `source/`, `figures/`, `digitization/`이 역할을 나눠야 한다.
- 예전처럼 `assets/figures/`, `assets/digitization/`, `assets/exp006_timing/` 같은 category folder로 나누면 같은 논문 자료가 흩어진다.

### 3.2 digitization Markdown 산출물이 있는지 확인

asset availability만으로는 부족하다는 기준도 사용자가 직접 올렸다.

> `가능하다면 너 수준에서 마크다운 파싱까지 진행해주면 좋음 ... microsoft/markitdown 이거 레포로 실행하면 되는데 . 가능함 /?`

> `microsoft/markitdown 이거로 @docs/wiki/research/assets/ 에 있는 논문들 다 마크다운으로 변환해줄수잇냐고`

이 두 prompt 이후 작업 범위는 "다운로드된 asset 확인"이 아니라 "asset cache 전체를 LLM/search가 읽을 수 있는 Markdown 산출물로 만드는 것"으로 바뀌었다.

각 asset의 `digitization/` 아래 Markdown 산출물을 확인했다. 반복된 파일 목록 전체를 여기에 다시 적지는 않는다. 핵심 관찰은 두 갈래였다.

- paper-PDF asset에는 `pageindex_structure.md`와 `paper_arxiv_*.md` 형태의 PageIndex 산출물이 생겼다.
- data-release asset에는 GWTC release note, notebook, Zenodo README 같은 release Markdown이 생겼다.

판정:

- H2는 지지된다. paper-PDF asset에는 `pageindex_structure.md`와 `paper_arxiv_*.md`가 생겼다.
- H6도 지지된다. `gwtc4_population_release.md`, `popsummary_tutorial.md`, `zenodo_README.md`처럼 data-release 성격의 문서는 MarkItDown/structured conversion route가 맞다.
- 이 산출물은 `source_text_parse`이지 `numeric_digitized`가 아니다. 숫자 table이나 curve point가 provenance/uncertainty와 함께 추출된 것은 아니다.

### 3.3 MarkItDown과 PageIndex의 역할 차이

처음에는 MarkItDown을 중심으로 생각했지만, 사용자는 PDF 논문에서 도구 차이가 크다는 점을 계속 짚었다.

> `변환 품질은 완벽한 논문 재조판이 아니라 LLM/검색용 구조화 텍스트입니다. 그래도 본문과 표/섹션 탐색에는 쓸 수 있으므로 “numerical product 추출 전 단계”로 기록합니다. -> 완벽한 마크다운 파싱 못함?`

> `클로드 코드는 mcp 연결해서 알아서 다 파싱해주는데 ?`

> `markitdown, page index 차이에 대해서도 작성해야하는거아닐까? ... 특히 pdf 의 경우에.`

이 prompt들 때문에 "둘 다 Markdown을 만든다"는 관점을 버렸다. 변환 도구의 차이는 산출물 확장자가 아니라 evidence state(근거로 쓸 수 있는 처리 단계) 차이다.

이번 사건에서 도구 차이는 꽤 컸다. 특히 PDF 논문에서는 "Markdown 파일이 생성됐다"와 "논문을 신뢰 가능한 순서로 읽을 수 있다"가 같은 말이 아니었다.

| 입력                       | MarkItDown 판단                                              | PageIndex 판단                  | 이유                                                                                     |
| -------------------------- | ------------------------------------------------------------ | ------------------------------- | ---------------------------------------------------------------------------------------- |
| paper PDF(논문 본문 PDF)   | 기본값은 `low_fidelity_search_text`                          | 기본 경로는 `source_text_parse` | PDF 논문은 2단, 수식, caption, footnote, figure reference 때문에 단순 변환이 깨지기 쉽다 |
| arXiv HTML                 | 사용 가능                                                    | 필요하면 보조                   | HTML은 이미 구조화 text라 section/search용 Markdown 변환 품질이 상대적으로 안정적이다    |
| TXT/README                 | 사용 가능                                                    | 보통 불필요                     | release note, manifest, package README는 문서 구조가 단순하다                            |
| JSON metadata              | 사용 가능하되 표/목록으로 재정리 필요                        | 부적합                          | PageIndex는 paper reading 도구이지 metadata normalizer가 아니다                          |
| notebook/CSV/table release | MarkItDown 또는 별도 table conversion                        | 부적합                          | 목적은 paper reading이 아니라 release inventory와 table inspection이다                   |
| figure PDF                 | 변환기가 아니라 renderer(그림을 이미지로 그려내는 도구) 필요 | 본문 context 확인에는 보조      | 좌표 추출용 PNG는 `pdftocairo` 같은 rendering tool(렌더링 도구)이 필요하다               |

PDF에서 MarkItDown이 특히 위험한 이유:

- 2단 논문의 줄 순서가 섞일 수 있다.
- 수식의 줄바꿈, 첨자, 부호, 괄호 구조가 깨질 수 있다.
- 표가 spurious Markdown table로 변하면서 원래 행/열 의미가 흐려질 수 있다.
- figure caption과 본문 reference가 분리되거나 순서가 바뀔 수 있다.
- image link가 없거나, 있어도 source figure 파일과 연결되지 않을 수 있다.

PageIndex가 더 나았던 이유:

- page 단위와 section hierarchy(섹션 계층 구조)를 따로 확보할 수 있다.
- paper-PDF 전문을 chunk(한 번에 처리하는 페이지 묶음) 단위로 추출할 수 있다.
- paper reading에는 충분한 `source_text_parse`를 만들 수 있다.
- 긴 논문도 abstract/summary만 임의 추출하지 않고 page 범위로 나눠 처리할 수 있다.

하지만 PageIndex도 figure mapping의 최종 권위는 아니다. PageIndex는 caption과 page context(해당 페이지 주변 본문)를 읽는 데 유용하지만, Figure 번호와 실제 image file name(그림 파일명)은 arXiv source의 `.tex`에서 `\includegraphics`와 `\caption`을 확인해야 한다.

판정:

- H8은 기각된다. 둘 다 Markdown을 만들 수 있어도 evidence state가 다르다.
- MarkItDown PDF output은 수동 대조 전에는 `low_fidelity_search_text`로 둔다.
- PageIndex paper output은 검토 가능한 `source_text_parse`로 둘 수 있다.
- TXT/HTML/JSON/notebook/data-release는 MarkItDown route(처리 경로)가 실용적이다.
- figure PDF는 Markdown converter(문서 변환기)가 아니라 high-resolution renderer(고해상도 렌더링 도구)와 image-link coverage(이미지 링크가 실제 파일을 가리키는지 점검)가 필요하다.

### 3.4 figure source와 PNG mirror가 실제로 존재하는지 확인

figure는 사용자가 별도 기준으로 끌어올린 부분이다.

> `마크다운 파일 처리하면서 figure 사진 png 파일도 경로 (원본 그대로 구조여야겟지?) 잘 참조하는지 확인해.`

> `논문을 그대로 원문 그대로 추출하는거고 figure 파일참조도 소스에서 참조할 수 있잖아`

> `extracted 에 png 나 pdf 로 있는거 png 변환하면 될거고`

이 prompt들 이후 Markdown은 본문 text만이 아니라 figure reference와 rendered PNG mirror까지 포함해야 했다.

source tree에서는 TeX, HTML/TXT, source figure PDF를 찾았고, `figures/extracted/`에서는 Markdown이 참조할 PNG mirror를 확인했다. 같은 `find` 패턴을 asset 전체에 반복해서 돌렸지만, 회고에는 파일 목록을 전부 복사하지 않는다. 중요한 관찰만 남긴다.

- Amendola, Farrah, Croker, Lacy, Li 계열 asset에는 TeX source가 있었다.
- GWTC release 계열 asset에는 figure PDF, TXT, notebook, release manifest가 있었다.
- 여러 asset에 PNG mirror가 생겼지만, PNG 존재만으로는 충분하지 않았다. 해상도와 Markdown reference coverage를 별도로 확인해야 했다.

판정:

- H3은 기각된다. figure 파일이 실제로 있으므로, caption 순서 추정이 아니라 TeX source의 `\includegraphics` block으로 mapping해야 한다.
- H4도 부분 기각된다. PNG가 존재하는 것만으로 충분하지 않다. workflow가 "target >= 700px wide"와 vector PDF의 2000px render를 명시해야 한다.
- 단, TeX도 무조건 권위는 아니다. `Cosmological Budget of Entropy from Merging Black Holes`(Chen, Jani, and Kephart 2026)의 `sample631.tex`는 draft superset(출판본보다 많은 draft용 그림 block이 남은 TeX source)이었다. TeX 안에는 figure environment(TeX의 그림 단위 block)가 18개 있었지만 published PDF(출판 PDF)에는 7개만 있었다. TeX만 믿으면 오히려 틀린다. 그래서 TeX를 우선 보되 draft superset이면 compiled PDF(TeX를 조판한 최종 PDF)와 PageIndex page content(PageIndex가 페이지별로 추출한 본문)로 교차검증한다. Amendola/Farrah 계열 논문은 TeX가 정답이었고 caption 순서 추측이 틀렸지만, Chen/Jani/Kephart 논문은 TeX가 과잉이었다. 결론은 "한쪽 소스만 믿지 말라"이다.
- 분리 figure 파일이 없는 논문도 있다. Lineweaver entropy-budget chapter(`Chapter22Lineweaver.pdf`)는 책 챕터 PDF라 source에 별도 figure 파일이 없었다. PDF embedded raster(PDF 안에 들어 있는 사진 이미지, 예: M87 사진)는 `pdfimages`로 native image(원본에 가까운 추출 이미지)를 뽑아 그대로 두고, vector diagram(선과 글자로 그려진 도식, Fig 22.2–22.4)은 `pdftoppm`로 high-DPI page render(고해상도 페이지 이미지)를 만든 뒤 crop(필요한 영역만 자르기)해야 했다. 즉 "figure 파일이 없다"가 "figure를 못 만든다"는 아니다.

### 3.5 새 workflow가 실패 패턴을 막는지 확인

이 분기점은 "한 번 고친 절차를 다음 agent도 읽게 만들라"는 요구에서 나왔다.

> `워크플로우 다 참조하게 해야지! ..`

> `@.agent/workflows/ 이거 근데 같은 작업에 대해서 지시하는건데 병합할 수는 없냐?`

> `클로드가 이렇게 작업햇다는데 회고에 잇나?`

그래서 digitization workflow 자체와 workflow index(여러 workflow 중 어떤 문서를 읽어야 하는지 알려주는 목록) 등록 여부를 회고에 남겼다.

새 digitization workflow가 네 가지 실패를 막는지 확인했다.

- paper-PDF는 PageIndex structure(섹션 구조)와 full text extraction(전문 텍스트 추출)으로 보낸다.
- data-release는 MarkItDown conversion(문서 변환)과 table/figure inventory(표·그림 목록 점검)로 보낸다.
- figure mapping은 PageIndex caption 추정이 아니라 TeX source의 figure block을 기준으로 한다.
- vector figure PDF는 낮은 해상도 preview가 아니라 high-resolution PNG로 다시 렌더링한다.

판정:

- H1은 기각된다. MarkItDown은 paper-PDF 기본 경로가 아니다.
- H2, H3, H4, H6, H8은 workflow에 반영됐다.
- H5는 workflow에 더 강하게 반영돼야 한다. paper-PDF route(논문 PDF 처리 경로)는 기본적으로 full text를 만들고, 범위 축소는 사용자가 명시했을 때만 해야 한다.

### 3.6 파일 구조와 workflow routing이 같은 규칙을 가리키는지 확인

파일 구조는 별도 핵심 분기점이었다. 사용자는 "converter"보다 "자료가 흩어지는 구조"를 더 크게 문제 삼았다.

> `파일 구조 컨벤션이 정확한건가? digitization 이거 마크다운 파일로 직접 파싱해논건데 좀 다른듯. 흠 고민. 어떻게 정리하지..;`

> `각 폴더 구조 역할부터 제대로 정의하고 정리해..`

> `하이고 이놈아 그러면 .gitkeep 으로 다 컨벤션 맞춰서 폴더만들어놔야할거아니야`

> `ㅇㅇ 최대한 SSOT 처리해야해. 불필요한건 제거, 분산된건 하나로, 다른건 분리. 분할, 그룹핑.`

이 prompt들 때문에 asset layout(자료 배치 구조), empty directory convention(빈 표준 폴더를 `.gitkeep`으로 보존하는 규칙), workflow SSOT boundary(어떤 문서가 최종 기준인지 나누는 경계)를 같은 섹션에서 정리했다.

이번 정리에서는 converter만 고친 것이 아니라 파일 구조도 같이 고쳤다. agent가 매번 새 위치를 추측하면 다시 자료가 흩어지기 때문이다.

정리된 asset layout:

```text
docs/wiki/research/assets/
  <paper_or_release_key>/
    README.md
    source/
    figures/
    digitization/
```

각 디렉터리의 역할:

| 경로                 | 역할                                                                                                           |
| -------------------- | -------------------------------------------------------------------------------------------------------------- |
| `source/`            | 외부 원본. PDF, arXiv source tar, Zenodo metadata, release archive, code manifest를 둔다.                      |
| `source/extracted/`  | tar, zip, figure archive 등을 푼 원본 파생물. TeX source와 원본 figure PDF도 여기에 남긴다.                    |
| `figures/extracted/` | Markdown에서 참조할 PNG mirror와 rendered figure를 둔다.                                                       |
| `digitization/`      | PageIndex outline/full text, MarkItDown release Markdown, table inventory 같은 derived inspection text를 둔다. |

금지된 구조:

```text
docs/wiki/research/assets/figures/
docs/wiki/research/assets/digitization/
docs/wiki/research/assets/source_x/
docs/wiki/research/assets/exp006_timing/
```

판정:

- H7은 기각된다. asset의 첫 child는 category가 아니라 paper/release key여야 한다.
- 같은 논문의 `source`, rendered `figures`, derived `digitization`은 한 key 아래에 있어야 README와 audit이 같은 대상을 가리킬 수 있다.
- [QFUDS Agent Workflows](../../../.agent/workflows/README.md)는 workflow routing index(작업별 참조 workflow 목록)이고, [Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md)는 상태/claim/layout SSOT다.
- [Research Asset Digitization Workflow](../../../.agent/workflows/research-asset-digitization-workflow.md)는 "어떻게 변환할지" 절차 문서다. 둘이 충돌하면 product workflow가 이긴다.
- [Research Assets](../research/assets/README.md)는 cache index이지 operational workflow SSOT가 아니다.

## 4. 추가 확인: 001 회고와 이번 사건의 차이

이 회고는 기존 001에 덧붙인 것이 아니라 신규 postmortem으로 분리했다. 사용자가 명시적으로 새 문서와 skill 준수를 요구했기 때문이다.

> `신규 회고 문서로 작성해. SKILL.md 잘 지켜라.`

[Li 2025 Data Cache Incident](001-20260609-dorito-li-2025-data-cache.md)는 첫 번째 문제를 잡았다.

```text
웹 검색에서 data repo가 안 보임
!=
쓸 자료가 없음
```

이번 사건은 두 번째 문제다.

```text
asset이 repo에 있음
!=
충실하게 digitized 됨
```

001에서 배운 것은 "PDF/source/figure asset을 놓치지 말라"였다. 이번에 배운 것은 "asset을 찾은 뒤에도 full text, figure mapping, image quality, coverage audit을 별도 단계로 검증하라"이다.

| 단계            | 001 회고의 초점                            | 이번 회고의 초점                                                           |
| --------------- | ------------------------------------------ | -------------------------------------------------------------------------- |
| asset discovery | source bundle과 figure PDF를 놓치지 않기   | 이미 있는 asset을 paper/release 단위로 처리하기                            |
| PDF parsing     | agent PDF extraction failure를 숨기지 않기 | paper-PDF는 PageIndex, data-release는 MarkItDown으로 분리하기              |
| figure handling | figure PDF를 product로 인정하기            | TeX mapping, PNG mirror, 고해상도 render, image link coverage까지 확인하기 |
| evidence state  | `not found`와 `not extracted` 분리         | `source_text_parse`와 `numeric_digitized` 분리                             |

이번에 명시적으로 확인하지 않은 것도 있다.

- PageIndex MCP API 호출 로그 자체는 (편의상) Claude Cowork 로 처리해서 하위 부록으로 작성함.

## 5. 결론 / 해결

최종 결정은 세 가지다.

| 결정                | 고른 것                                                            | 안 고른 대안                                      | 근거                                                                            |
| ------------------- | ------------------------------------------------------------------ | ------------------------------------------------- | ------------------------------------------------------------------------------- |
| paper-PDF 변환 경로 | PageIndex structure + full text                                    | MarkItDown PDF output을 논문 전문으로 사용        | MarkItDown은 논문 PDF에서 section/equation/figure reference가 깨질 수 있다      |
| non-paper 변환 경로 | MarkItDown으로 HTML/TXT/JSON/notebook/CSV release를 Markdown화     | 모든 자료를 PageIndex로 밀어 넣기                 | data-release는 논문 본문 구조보다 manifest/table/figure inventory가 중요하다    |
| figure mapping      | TeX `\includegraphics` block을 권위 소스로 사용                    | PageIndex caption 순서로 추정                     | Amendola/Farrah mapping 오류가 실제로 발생했다                                  |
| figure quality      | vector PDF는 2000px급 PNG로 재렌더                                 | 보이는 작은 PNG를 그대로 둠                       | digitization 입력은 preview가 아니라 좌표 추출 가능한 해상도가 필요하다         |
| 긴 논문 처리        | full text default                                                  | agent가 임의로 abstract/summary/conclusion만 처리 | 범위 축소는 사용자가 명시해야 한다                                              |
| 파일 구조           | paper/release key 아래 `source/`, `figures/`, `digitization/` 고정 | asset root 아래 category folder를 만들기          | 같은 논문 자료가 흩어지면 README, audit, image link가 서로 다른 대상을 가리킨다 |
| workflow routing    | workflow index에 digitization workflow를 등록                      | Claude/Codex chat memory로만 절차 공유            | agent가 매번 같은 SSOT를 읽어야 재발을 막을 수 있다                             |
| converter 선택      | paper-PDF는 PageIndex, TXT/HTML/data-release는 MarkItDown          | 모든 Markdown 변환을 같은 품질로 취급             | PDF 논문과 release text는 구조 실패 모드가 다르다                               |

"full text default"에는 범위 정의가 하나 더 필요했다. `The population of merging compact binaries inferred using gravitational waves through GWTC-3`(Abbott et al. 2023 / LVK GWTC-3 population paper)는 75페이지지만, 본문 약 36p + 부록 약 16p + 참고문헌 381개 약 12p + 저자/소속 약 10p로, 마지막 약 30%가 참고문헌과 저자목록이다(LVK 논문 특성). 이번에 전달한 범위는 본문·부록 서술과 번호 수식 전부 verbatim(원문 그대로), 큰 표 6개와 그림 34장은 data-release 참조, 참고문헌·저자목록은 요약이었다. "글자 그대로 100% 전사"(표 전 행 + 381 reference + 저자 10p)는 분량만 2–3배이고 연구 가치는 낮다. 그래서 긴 논문은 임의 축소하지 않되, "full text"가 *참고문헌·저자목록까지 문자 그대로*인지 *과학 내용만 완전 리터럴(literal, 원문 문장 그대로)*인지는 사용자에게 한 번 확인한다.

그래서 새 operational SSOT는 [.agent/workflows/research-asset-digitization-workflow.md](../../../.agent/workflows/research-asset-digitization-workflow.md)다.

이 workflow가 보장하는 것은 여기까지다.

```text
asset cached
-> source extracted
-> source_text_parse
-> figure PNG/link coverage
```

이 workflow가 요구하는 파일 구조는 다음이다.

```text
docs/wiki/research/assets/<paper_or_release_key>/source/
docs/wiki/research/assets/<paper_or_release_key>/source/extracted/
docs/wiki/research/assets/<paper_or_release_key>/figures/extracted/
docs/wiki/research/assets/<paper_or_release_key>/digitization/
```

이 workflow가 보장하지 않는 것은 다음이다.

```text
numeric_digitized
manual_structured_extract
QFUDS support
roadmap status update
Level 2B opening
```

## 6. 재발 방지 / 운영 메모

다음부터 research asset digitization을 맡은 agent는 이 순서를 지켜야 한다.

1. 먼저 [Research Asset and Product Workflow](../../../.agent/workflows/research-asset-product-workflow.md)를 읽고 asset state ladder를 정한다.
2. [QFUDS Agent Workflows](../../../.agent/workflows/README.md)에서 digitization workflow가 등록돼 있는지 확인한다.
3. cached asset이면 [Research Asset Digitization Workflow](../../../.agent/workflows/research-asset-digitization-workflow.md)를 읽는다.
4. asset folder는 반드시 paper/release key 아래 `source/`, `figures/`, `digitization/` 세 child를 갖게 한다.
5. asset을 `paper-PDF`와 `data-release`로 나눈다.
6. `paper-PDF`는 PageIndex로 `pageindex_structure.md`와 full-text `paper_*.md`를 만든다.
7. `data-release`는 MarkItDown과 structured table/figure inventory로 처리한다.
8. figure 번호와 파일명은 `.tex`의 `\includegraphics` + `\caption` block에서 매핑한다.
9. source figure PDF가 있으면 `figures/extracted/`에 고해상도 PNG mirror를 만든다.
10. Markdown image link는 `../figures/extracted/...` 상대 경로로 넣고 실제 resolve 여부를 확인한다.
11. source figure count, PNG count, Markdown reference count를 비교한다.
12. 변환 결과는 `source_text_parse`로 기록하고, numerical extraction 전에는 `numeric_digitized`라고 쓰지 않는다.

간단한 판단 규칙:

```text
PDF가 있다 -> 문헌 확인 완료 아님
Markdown이 있다 -> numerical product 아님
PNG가 있다 -> figure digitization 완료 아님
caption을 봤다 -> figure mapping 완료 아님
```

이번 사건에서 workflow에 남긴 핵심 guardrail(재발을 막는 작업 규칙)은 다음 여섯 가지다.

- 권위 mapping은 PageIndex caption 순서가 아니라 TeX source다.
- 고해상도 figure rendering은 후속 옵션이 아니라 기본값이다.
- 긴 논문은 full text default이고, 임의 축소하지 않는다.
- MarkItDown은 paper-PDF 기본 경로가 아니라 non-paper/data-release 경로다.
- asset은 자료 종류별 category가 아니라 paper/release key 기준으로 묶는다.
- MarkItDown PDF output은 기본적으로 `low_fidelity_search_text`, PageIndex paper output은 검토 가능한 `source_text_parse`로 분리한다.

운영 제약(이번에 실제로 막혔던 것):

- mount(Claude cowork가 보는 작업 디렉터리 연결층)에서는 bash `rm`/`chmod`이 `Operation not permitted`로 막힌다. 삭제가 필요하면 cowork file-delete 도구로 허용을 먼저 받는다. 그러니 `digitization/`에 임시 파일을 만들지 않는다. 만들면 validator(문서 규칙 검사기)가 frontmatter 없다고 깨지고 mount에서 지우기도 번거롭다. 변환 조립은 sandbox/메모리(임시 작업 공간)에서 하고 최종 파일만 mount에 쓴다.
- figure mode `600`(파일 권한 숫자)은 mount가 잠가서 못 바꾸지만, 소유자 본인 파일이라 VS Code 렌더링에는 영향이 없다. 권한은 핵심 문제가 아니었다.
- `docs/` 아래 모든 `.md`는 frontmatter 필수이고 첫 H1(문서 첫 제목)이 `title`과 정확히 일치해야 한다(em-dash 포함). 본문에서 존재하는 `.md` 경로를 backtick(코드 표시용 역따옴표)으로 쓰면 "should be a Markdown link"로 막히므로 실제 링크로 쓴다(`.tar.gz`/`.csv` 등 비-md 경로는 안 걸림). 새 `.md`를 만들면 곧바로 이 둘을 맞춘다.

## 7. 타임라인

- Li 2025 회고에서 agent PDF extraction 실패와 source/figure asset cache 필요성이 정리됐다.
- 이후 여러 paper/release asset이 [docs/wiki/research/assets/](../research/assets/README.md) 아래 논문/릴리스 단위로 정리됐다.
- asset 하위 구조를 `source/`, `figures/`, `digitization/`으로 고정하고, empty standard directory는 `.gitkeep`으로 남기는 컨벤션을 세웠다.
- 처음에는 Codex 쪽 MarkItDown 기반 변환이 논문 전문 처리에 충분하지 않았다.
- 특히 PDF 논문에서는 MarkItDown과 PageIndex의 품질 차이가 컸고, MarkItDown은 TXT/HTML/data-release 쪽으로 역할을 좁혔다.
- Claude cowork에서 PageIndex MCP(Model Context Protocol, 외부 도구 연결 규격)를 사용해 여러 논문의 structure(섹션 구조)와 full text extraction(전문 추출)을 진행했다.
- Amendola 2024와 Farrah 2023에서 PageIndex caption 순서 기반 figure mapping이 틀렸고, TeX `\includegraphics` 확인으로 수정했다.
- 일부 figure PNG가 너무 낮은 해상도였고, vector PDF를 2000px급 PNG로 다시 렌더링하는 기준이 생겼다.
- Abbott 2023은 처음에 긴 문서라 일부만 처리하는 방향으로 축소됐지만, full text default가 맞다는 결론으로 정리됐다.
- TXT/HTML/JSON/notebook/data-release 성격 자료는 MarkItDown이 적합한 경로로 분리됐다.
- 이 교훈을 [.agent/workflows/research-asset-digitization-workflow.md](../../../.agent/workflows/research-asset-digitization-workflow.md)에 반영했다.
- [.agent/workflows/README.md](../../../.agent/workflows/README.md)에 새 digitization workflow를 등록해 agent routing index에서도 찾을 수 있게 했다.
- 이 postmortem은 그 시행착오를 001 회고의 후속 사건으로 기록한다.

## 부록 A: 확인 패턴

이 사건에서는 여러 asset에 비슷한 확인을 반복했다. 회고의 목적은 shell transcript를 보존하는 것이 아니라, 다음 agent가 어떤 순서로 판단해야 하는지 남기는 것이다. 그래서 대표 패턴만 적고 반복 출력은 생략한다.

### sequence 확인

`docs/wiki/postmortem/`의 기존 numbered 파일을 보고 다음 sequence가 005임을 확인했다. 이 확인은 파일명 충돌을 막기 위한 것이다.

### asset root 확인

`docs/wiki/research/assets/` 바로 아래 folder가 paper/release key인지 확인했다. category folder가 있으면 같은 논문 자료가 여러 곳으로 흩어졌다는 신호다.

이번 판단:

- asset root는 paper/release key 중심으로 정리돼 있었다.
- future workflow는 이 구조를 유지해야 한다.

### digitization 산출물 확인

각 asset의 `digitization/` 아래에 어떤 Markdown 산출물이 있는지 확인했다. 같은 패턴으로 `pageindex_structure.md`, `paper_*.md`, release Markdown(릴리스 설명 파일을 변환한 Markdown)을 반복 확인했다.

이번 판단:

- paper-PDF asset은 PageIndex route(논문 PDF 처리 경로)를 탄다.
- TXT/HTML/JSON/notebook/data-release asset은 MarkItDown 또는 structured conversion route(구조화 변환 경로)를 탄다.
- 둘 다 Markdown일 수 있지만 evidence state(근거로 쓸 수 있는 처리 단계)는 다르다.

### source와 figure 확인

`source/extracted/`에서는 TeX, HTML/TXT, source figure PDF를 확인했다. `figures/extracted/`에서는 Markdown image link가 가리킬 PNG mirror를 확인했다.

이번 판단:

- figure mapping은 PageIndex caption 순서가 아니라 source TeX를 우선한다.
- source figure PDF가 있으면 Markdown용 PNG mirror가 필요하다.
- PNG가 있다는 사실만으로는 충분하지 않고, 해상도와 reference coverage가 필요하다.

### TeX 기반 figure mapping

TeX source에서 figure include(그림 삽입 명령)와 caption block(그림 설명 단락)을 찾는 확인을 반복했다. 이때 논문 본문이나 source code를 회고에 그대로 옮기지 않는다. 필요한 것은 "어떤 file이 어떤 Figure에 대응하는지"라는 mapping 판단이다.

이번 판단:

- caption 순서 추정은 틀릴 수 있다.
- source TeX가 있으면 먼저 TeX를 본다.
- TeX가 draft superset(출판본보다 많은 draft용 그림이 남은 원고)이면 compiled PDF(조판된 최종 PDF)나 PageIndex page context(페이지별 본문 내용)로 대조한다.

### high-resolution figure rendering

figure PDF를 PNG로 바꾸는 작업은 여러 파일에 반복했다. 회고에는 모든 command를 나열하지 않는다. 판단 기준만 남긴다.

이번 판단:

- preview용 저해상도 이미지는 digitization 입력으로 부족하다.
- vector PDF graph는 2000px급 이상의 PNG mirror로 다시 렌더링한다.
- native PNG(저자가 제공한 원본 PNG)는 억지로 upscale(픽셀만 키우는 확대)하지 않는다.

### verification

문서 변경 뒤에는 validate(문서 규칙 검사), research consistency(연구 문서 일관성 검사), whitespace check(공백 오류 검사)를 실행했다. 이 검증은 frontmatter, link hygiene(링크 형식 정리), roadmap/document consistency(roadmap과 문서 간 일관성), whitespace 오류를 잡는다.

이번 판단:

- "전부 통과"라고 말하려면 이 검증 결과가 있어야 한다.
- 단, 이 검증은 figure mapping의 물리적 정확성이나 numerical digitization까지 보장하지 않는다.

## 부록 B: 왜 이 문제가 반복되기 쉬운가

이 문제는 "파일 변환"처럼 보이지만 실제로는 evidence-state 문제다.

```text
변환 파일이 생김
-> 읽을 수 있는 text인지 확인 필요
-> source figure와 연결됐는지 확인 필요
-> numerical product인지 별도 확인 필요
-> QFUDS 판단에 써도 되는지 별도 확인 필요
```

한 단계라도 건너뛰면 표현이 과장된다.

| 잘못된 표현              | 정확한 표현                                                |
| ------------------------ | ---------------------------------------------------------- |
| 논문 파싱 완료           | `source_text_parse` 생성                                   |
| figure digitization 완료 | figure PNG mirror와 Markdown reference 생성                |
| data product 없음        | checked assets에서 QFUDS-ready numerical product not found |
| 문헌 확인 완료           | PDF/source/figure/table/code availability checked          |
| QFUDS timing support     | literature comparison target or overlap candidate          |

이번 workflow의 목적은 agent가 이런 단계를 뭉개지 못하게 하는 것이다.

## 부록 C: 명령어 모음 (cheat sheet)

본문 진단에서는 명령을 추론 순서대로 보여줬다. 여기서는 같은 명령을 *목적별*로 모은다. 명령만 빌리러 온 다음 agent가 그대로 복사·응용할 수 있게, 각 명령에 (1) 그 명령이 일반적으로 무슨 일을 하는지, (2) 이 사건에서 무엇을 보려고 썼는지를 같이 적는다. 경로는 `<key>` = paper/release key로 둔다.

### 압축 해제 / 변환

```bash
tar xzf <key>/source/table_data.tar.gz -C <key>/source/extracted/
```

- 일반: gzip tar 아카이브를 지정 디렉터리에 푼다(`x` 추출, `z` gzip, `f` 파일, `-C` 대상).
- 이번 용도: data-release의 table/figure 아카이브를 `source/extracted/`로 풀어 CSV·figure 원본을 확보.

```bash
markitdown <key>/source/zenodo_README.txt > <key>/digitization/zenodo_README.md
markitdown <key>/source/extracted/table_data/foo.csv   # CSV -> Markdown 표
```

- 일반: MarkItDown이 TXT/HTML/JSON/notebook/CSV 등을 Markdown으로 변환한다.
- 이번 용도: data-release의 release note, event-list, CSV 표를 Markdown으로, 단 `paper-PDF`가 아니라 `data-release` 경로에서만.

### figure 렌더 / 추출 (고해상도)

```bash
pdftocairo -png -singlefile -scale-to 2000 <fig>.pdf <fig>
```

- 일반: vector PDF(선과 글자로 된 PDF 그림)를 가장 긴 변 2000px PNG로 렌더(`-singlefile`로 페이지 suffix 없이).
- 이번 용도: arXiv figure PDF(amendola/farrah/croker/li/abbott/gwtc4)를 저해상 PNG 위에 고해상도로 덮어쓰기. 저자 native PNG(저자가 원본으로 제공한 PNG, chen/lacy)는 건드리지 않음.

```bash
pdfimages -png <key>/source/chapter22_lineweaver.pdf /tmp/lw     # 임베드 래스터 추출
pdftoppm -r 600 -png -f 6 -l 6 <pdf> /tmp/pg                      # 페이지를 600dpi로 렌더
convert /tmp/pg-06.png -crop 2950x1320+380+430 +repage -trim out.png   # figure 영역 크롭
identify -format '%wx%h' out.png                                 # 해상도 확인
```

- 일반: `pdfimages`는 PDF에 들어 있는 raster image(픽셀 이미지)를 그대로 뽑고, `pdftoppm`은 페이지 전체를 raster로 렌더, `convert -crop/-trim`은 그중 figure만 잘라낸다, `identify`는 픽셀 크기를 본다.
- 이번 용도: 분리 figure 파일이 없는 Lineweaver에서 사진(M87)은 `pdfimages` native(원본 추출 상태) 유지, vector 도식(22.2–22.4)은 `pdftoppm` 600dpi 렌더 후 crop(필요 영역만 자르기). `identify`로 700px 미만인지 검사.

### figure 번호 ↔ 파일 매핑 (TeX 권위 소스)

```bash
grep -oE '\\includegraphics(\[[^]]*\])?\{[^}]*\}' <key>/source/extracted/*.tex
# 더 정확히는 figure environment 단위로 \includegraphics + \caption 파싱
```

- 일반: TeX에서 그림 삽입 명령을 뽑아 Figure 번호 순서와 실제 파일명을 연결한다.
- 이번 용도: PageIndex caption 순서 추정으로 틀렸던 amendola/farrah를 TeX 기준으로 교정. 단 `Cosmological Budget of Entropy from Merging Black Holes`처럼 draft superset이면 compiled PDF와 교차검증.

### 긴 논문 full-text 추출 / 조립

- PageIndex(MCP 도구): `process_document`(적재) -> `get_document_structure`(outline, 섹션 구조) -> `get_page_content`(페이지 본문). `get_page_content`는 응답이 약 50KB를 넘으면 temp 파일로 persist(임시 파일로 저장)되므로 6–8 페이지 단위 chunk(페이지 묶음)로 부른다.

```bash
cat >> <key>/digitization/paper_<id>.md <<'P_EOF'
## Page N
...verbatim...
P_EOF
```

- 일반: quoted heredoc(`'P_EOF'`, 따옴표로 감싼 여러 줄 입력)으로 파일 끝에 append(덧붙이기)한다. 따옴표 delimiter(끝 표시 문자열)라 `$`·backtick이 shell 확장되지 않는다.
- 이번 용도: `The population of merging compact binaries inferred using gravitational waves through GWTC-3`를 chunk별로 증분 append. 성장하는 파일을 매번 다시 읽지 않고, `## Page N` 마커로 누락 추적.

### 커버리지 / 품질 감사

```bash
# Markdown image link가 전부 실제 파일로 resolve(경로 해석)되는지 + 700px 미만 있는지
find . -path '*/digitization/*.md' -print0 | while IFS= read -r -d '' f; do d=$(dirname "$f");
  grep -o '](\.\./figures/extracted/[^)]*)' "$f" | sed 's/](//;s/)//' | while read p; do
    [ -f "$d/$p" ] && identify -format '%w\n' "$d/$p" || echo "MISSING $p"; done; done
```

- 일반: 모든 digitization Markdown의 이미지 링크를 모아 파일 존재·해상도를 검사.
- 이번 용도: "전부 resolve, 0 missing, 0 under 700px"를 말할 근거를 만듦. source figure 수 ↔ PNG 수 ↔ Markdown 참조 수 비교도 같은 패턴.

### 검증

```bash
python3 scripts/validate_docs.py          # frontmatter / H1=title / .md 링크 hygiene(링크 형식 정리)
python3 scripts/research_consistency.py    # roadmap/문서 일관성
git diff --check                           # whitespace 오류
```

- 일반: 문서 schema(필수 필드 규칙)·일관성·whitespace(공백 오류)를 검사.
- 이번 용도: 문서 변경마다 실행. "전부 통과"라고 말하려면 이 결과가 있어야 한다. 단, figure 매핑의 물리적 정확성이나 numerical digitization까지 보장하지는 않는다.

### 삭제 (mount 제약)

- mount(연결된 작업 디렉터리)에서 bash `rm`/`chmod`은 `Operation not permitted`로 막힌다. 삭제가 필요하면 cowork file-delete 도구로 폴더 삭제 허용을 먼저 받은 뒤 `rm`. 이번에 lacy 중복본 `paper_arxiv_2312.12344 2.md`, 임시 `_tbl_*.md`, `_wtest.txt` 제거에 이 제약이 걸렸다.

이런 부류의 작업은 보통 이 순서로 푼다: 압축 해제 → (paper면 PageIndex / release면 MarkItDown) 변환 → TeX로 figure 매핑 확정 → 고해상도 렌더 → 커버리지 감사 → validator. 매 단계 산출물은 `source_text_parse`까지만, numerical product 아님.
