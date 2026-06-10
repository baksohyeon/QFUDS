---
doc_id: postmortem-001-li-2025-data-cache
id: postmortem-001-li-2025-data-cache
seq: 1
title: "Li & Zhang 2025 데이터 제품 탐색과 캐싱 포스트모템"
doc_type: postmortem
type: postmortem
stage: reference
status: reference
wiki_status: active
evidence_role: reference
depends_on:
  - audit_2026_06_09_li_2025_public_product_search
  - asset_li_2025_desi_dr2_sign_reversal_ide
  - asset_digitization_li_2025_desi_dr2_sign_reversal_ide
next_gate: Li 2025 timing-overlap digitization protocol or author-data request
date: 2026-06-09
context: QFUDS Exp006 후속 Li & Zhang 2025 timing-target availability 조사와 local asset cache 구성
audience: 주니어 개발자
length: 작업 단계별 풀어쓰기
created_at: 2026-06-09
created_by: dorito
updated_at: 2026-06-10
updated_by: dorito
last_updated: 2026-06-10
last_verified_at: 2026-06-10
last_verified_by: dorito
audit_log:
  - action: created
    at: 2026-06-09
    by: dorito
    note: "Li & Zhang 2025 public product search, arXiv source inspection, asset caching, and digitization-image rendering after the Exp006 follow-up analysis."
  - action: updated
    at: 2026-06-09
    by: dorito
    note: "Added epistemic context: why the search mattered, what the Li and Zhang overlap changed, and what it did not prove."
  - action: updated
    at: 2026-06-09
    by: dorito
    note: "Added verbatim user prompt trail because the search direction changed through user judgment, not only agent initiative."
  - action: updated
    at: 2026-06-10
    by: dorito
    note: "Recorded the real resolution: the agent could not reliably parse the paper PDF, so the user produced a complete Markdown rendering of the paper with an external tool, which became the usable text-level artifact."
tags: [postmortem, li-2025, data-products, digitization, exp006]
relations:
  - docs/wiki/research/audits/exp006_timing/006_li_2025_public_product_search_audit.md
  - docs/wiki/research/audits/exp006_timing/005_li_2025_timing_overlap_matrix_plan.md
  - docs/wiki/research/literature/li_2025_desi_dr2_sign_reversal_ide.md
  - docs/wiki/research/assets/figures/li_2025/README.md
  - docs/wiki/research/assets/digitization/li_2025/README.md
  - docs/wiki/research/assets/digitization/li_2025/paper_arxiv_2506.18477v2.md
code_refs:
  - file: docs/wiki/research/audits/exp006_timing/006_li_2025_public_product_search_audit.md
    note: "Public numerical-product availability search record."
  - file: docs/wiki/research/assets/figures/li_2025/README.md
    note: "Cached arXiv source package, extracted source files, and full paper PDF manifest."
  - file: docs/wiki/research/assets/digitization/li_2025/README.md
    note: "High-resolution PNG render manifest for future digitization."
  - file: docs/wiki/research/assets/digitization/li_2025/paper_arxiv_2506.18477v2.md
    note: "User-produced full-paper Markdown rendering; the reliable text-level source after the agent could not parse the paper PDF."
---

# Li & Zhang 2025 데이터 제품 탐색과 캐싱 포스트모템

Li & Zhang 2025가 Exp006 후속 timing target으로 올라온 뒤, 공개 numerical product가 있는지 찾았다. 결론은 "공개 numerical beta(z), covariance, posterior, PCA array는 못 찾았지만, arXiv source bundle 안의 figure PDF와 TeX source를 확인했고, 이를 repo asset cache와 digitization용 고해상도 PNG로 정리했다"이다.

가장 실용적인 마무리는 따로 있었다. 논문 PDF 자체는 agent가 안정적으로 본문을 추출하지 못했다. 그래서 사용자가 별도 도구로 논문 전체를 하나의 완성형 Markdown 문서로 변환했고, 이것이 이후 text-level 분석에 실제로 쓸 수 있는 산출물이 됐다. 즉 이 사건의 진짜 결론은 "agent의 PDF 처리 한계는 인정하고, 사람이 만든 Markdown 변환본을 단일 text source로 삼는다"이다.

이 문서는 새 실험이 아니다. Exp006 결론, roadmap status, [Level 1.5](../glossary/repository_levels.md)는 변경하지 않았다.

이 작업의 실제 의미는 단순한 파일 정리가 아니었다. Exp004, Exp005, Exp006을 지나면서 retained timing branch는 다음 상태에 있었다.

```text
구조 형성 직감
-> Exp004: retained P1은 interacting-vacuum / time-dependent IDE phenomenology
-> Exp005: retained timing은 potential compression target
-> Exp006: allowed_but_not_informative
```

Exp006만 보면 흐름이 닫힐 수 있었다. Escamilla table-level evidence가 애매했기 때문이다. 그런데 사용자가 "DESI/Euclid-era reconstruction literature를 충분히 본 게 맞나?"라고 다시 물으면서 문제가 바뀌었다.

```text
질문 1: 이 직감이 맞는가?
질문 2: 이 직감이 최소한 현대 IDE reconstruction에서 비교 가능한 timing feature와 만나는가?
```

이번 postmortem은 질문 2로 넘어가는 과정의 기록이다. 결론은 보수적으로 말해도 다음 정도다.

```text
QFUDS 증명 아님.
retained timing의 물리적 유도 아님.
하지만 retained peak z ~= 2.046, weighted mean z ~= 1.746이
Li & Zhang의 DESI-era positive-beta structure-era region과
중간 정도로 겹친다는 문헌 대조 가능성이 생겼다.
```

## 0. 사전 지식

| 용어 | 이 작업에서의 의미 |
| --- | --- |
| numerical product | `beta(z)` mean grid, uncertainty array, covariance matrix, posterior chain, PCA eigenvector/eigenvalue array처럼 바로 계산에 넣을 수 있는 기계 판독 데이터 |
| arXiv source bundle | arXiv의 `e-print` endpoint에서 받는 원고 제출 소스 묶음. TeX, bib, style, figure 파일이 들어갈 수 있다. |
| figure-level product | numerical table은 아니지만, 논문 figure PDF/PNG처럼 digitization으로 값을 추출할 수 있는 자료 |
| timing-overlap matrix | Exp005 retained timing fingerprint와 Li & Zhang `beta(z)` 재건의 redshift support/sign/zero-compatibility를 비교하려는 다음 분석 계획 |

## 1. 증상

처음 문제는 단순했다.

- Li & Zhang 2025가 가장 높은 우선순위 timing target으로 올라왔다.
- 하지만 Exp006을 바로 갱신하거나 새 실험을 만들면 안 됐다.
- 먼저 공개 data product가 실제로 있는지 확인해야 했다.

초기 public search에서는 machine-readable product를 못 찾았다. 그때 사용자 피드백이 들어왔다. 여기서는 요약하면 안 된다. 실제 방향 전환은 사용자의 구체적인 prompt에서 나왔다.

```text
- numerical beta(z) histories;
  - 68/95% uncertainty arrays;
  - posterior samples or chains;
  - covariance matrices;
  - PCA eigenvector/eigenvalue arrays;
  - paper-specific GitHub/Zenodo/OSF/Dataverse data archive. -> 이거 웹 서칭해서 못가져와? 너무 좁게 검색한거아냐? 또
```

그 다음에는 웹 검색이 아니라 파일 실체를 보라는 지시가 들어왔다.

```text
걍 ls 해서 확인해봐;
```

이후 사용자는 "목록만 본 것"과 "실제로 모든 파일을 훑은 것"을 분리했다.

```text
재귀적으로 모든 파일 다 훝어봐.
```

그리고 source bundle 안에 또 다른 archive나 CLI로 못 보는 human-only path가 있을 가능성을 짚었다.

```text
추가적으로 tar 파일같은거 없냐 ? 아니면 cli 상 한계로 못하는거 인간이 직접 해야 접근할 수 있는 경로나 놓친 문서가 잇나?
```

PDF figure의 중요성도 사용자가 먼저 강하게 짚었다.

```text
pdf 가 존나 중요해보이는데. 여기 레포로 이동시키면 내가 마크다운 파일로 뽑아줄까
```

asset 경로도 사용자가 바로잡았다.

```text
docs/research/assets 가 존재함
```

source bundle 구조가 애매해졌을 때도 기준을 다시 잡게 했다.

```text
tar 문서에 있는거 갸 ㅇ 다 가지고 오자.
```

```text
source 는 tar 도 드가야되는거아니녀? 외부 노출된건 뭔기준이여
```

마지막으로 digitization 품질 기준도 사용자가 올렸다.

```text
digitization용 고해상도는 별도 렌더링 도구가
  필요할 수 있습니다. 나머지 figure도 이어서 변환합니다. 고해상도 필요해
```

이 피드백이 핵심이었다. 웹 검색 결과만으로 "없다"고 하면 탐색 누락일 수 있다. 실제 bundle을 받아서 manifest, 압축 내용, 파일 타입, PDF 내부 단서까지 확인해야 했다.

이 장면이 전환점이었다. "검색에서 data repo가 안 보인다"와 "논문 source package에 비교 가능한 figure-level product가 없다"는 서로 다른 말이다. 전자는 웹 탐색 결과이고, 후자는 파일 시스템 증거다. 이 사건에서는 후자까지 내려갔기 때문에 이후 판단이 더 단단해졌다.

### 1.1 사용자 판단이 바꾼 것

이 사건은 agent가 혼자 "좋은 탐색"을 한 사례가 아니다. 사용자가 여러 번 탐색 기준을 올렸고, 그때마다 evidence level이 바뀌었다.

| 사용자 prompt | 바뀐 작업 | 바뀐 판단 |
| --- | --- | --- |
| `너무 좁게 검색한거아냐?` | exact search에서 broad external archive/code search로 확장 | "못 찾음"의 근거가 좁은 검색에 갇히지 않게 됨 |
| `걍 ls 해서 확인해봐;` | arXiv source bundle을 실제 추출하고 파일 목록 확인 | 웹 검색 결과가 아니라 source package manifest로 판단하게 됨 |
| `재귀적으로 모든 파일 다 훝어봐.` | 파일 타입, text source, PDF 문자열까지 확인 | hidden/nested data product 가능성을 더 좁힘 |
| `tar 파일같은거 없냐?` | nested archive/data-like extension 확인 | source bundle 안의 추가 archive 가능성을 배제 |
| `pdf 가 존나 중요해보이는데` | figure PDF를 단순 부속물이 아니라 product로 분류 | numerical product는 없어도 digitization route가 생김 |
| `docs/research/assets 가 존재함` | 잘못 만든 literature-local asset path 대신 repo asset tree 사용 | cache 위치가 repo convention에 맞게 정리됨 |
| `source 는 tar 도 드가야되는거아니녀?` | tar 원본과 extracted source를 같은 `source/` 기준 아래 재배치 | asset 구조 기준이 명확해짐 |
| `고해상도 필요해` | `sips` 저해상도 PNG에서 `qlmanage -t -s 2400` 렌더로 전환 | digitization에 쓸 수 있는 품질의 PNG가 생김 |

이 prompt trail이 없었으면 결과는 훨씬 약했을 가능성이 높다.

```text
가능했던 약한 결론:
web search에서 public data 못 찾음.

실제로 도달한 결론:
public numerical product는 못 찾았지만,
arXiv source bundle의 figure-level products를 확인했고,
repo-local cache와 high-resolution digitization images까지 확보했다.
```

## 2. 첫 의문 + 가설

| 가설 | 왜 그럴 수 있는지 | 어떻게 확인할지 |
| --- | --- | --- |
| H1. arXiv source bundle 안에 numerical data가 숨어 있다 | 논문 figure를 그린 원본 `.dat`, `.csv`, `.npy`가 같이 제출되는 경우가 있다 | arXiv `e-print`를 받고 `tar` manifest, extracted tree, file type을 확인한다 |
| H2. source bundle에는 figure PDF만 있고 numerical data는 없다 | 많은 arXiv 제출은 TeX와 final figure PDF만 포함한다 | `ls`, `file`, `rg`로 data-like 확장자와 repository/data availability 문구를 확인한다 |
| H3. PDF 내부에 attachment나 URI가 있다 | PDF는 embedded file, URI annotation, metadata를 가질 수 있다 | `strings`로 `/EmbeddedFiles`, `/Filespec`, `/URI`, archive URL 패턴을 검색한다 |
| H4. publisher page나 arXivLabs가 별도 code/data link를 제공한다 | arXiv page의 Code/Data tab, publisher supplement hook이 있을 수 있다 | arXiv HTML과 JCAP/IOP HTML에서 supplement/data/code hook을 확인한다 |
| H5. GitHub/Zenodo/OSF/Dataverse 등에 paper-specific archive가 있다 | 저자가 별도 repository나 archive record를 만들었을 수 있다 | exact title, arXiv ID, figure filename, author/title variants로 넓혀 검색한다 |

검증 순서는 비용이 낮고 신호가 큰 것부터 잡았다. 먼저 arXiv source bundle 자체를 확인하고, 그 다음 외부 archive/search를 넓혔다.

## 3. 진단: 실제 상태 확인

### 3.1 arXiv source bundle manifest 확인

먼저 source package를 내려받아 압축 manifest를 확인했다.

```bash
rtk tar -tzvf /private/tmp/qfuds_2506_18477_src.tar
```

핵심 출력:

```text
-rw-r--r--  0 root   root      215 Dec 11 21:38 00README.json
-rw-rw-r--  0 root   root    91881 Jun  9  2025 fig_bayes_data.pdf
-rw-rw-r--  0 root   root   103779 Aug 25  2025 fig_bin30.pdf
-rw-rw-r--  0 root   root   160915 Jun 15  2025 fig_evals.pdf
-rw-rw-r--  0 root   root   103268 Aug 25  2025 fig_mock_lcdm.pdf
-rw-rw-r--  0 root   root   161931 Jun 15  2025 fig_pc.pdf
-rw-rw-r--  0 root   root   172298 Jun  9  2025 fig_reconstruct.pdf
-rw-rw-r--  0 root   root   103703 Sep 17  2025 fig_zmax.pdf
-rw-rw-r--  0 root   root   103728 Sep 26  2025 idenpr.bib
-rw-rw-r--  0 root   root    43618 Dec 11 21:33 idenpr.tex
-rw-rw-r--  0 root   root    11222 Dec  5  2018 jcappub.sty
-rw-rw-r--  0 root   root    20428 Jun 12  2023 JHEP.bst
```

판정:

- H1은 약해졌다. manifest에 `.csv`, `.dat`, `.npy`, `.npz`, chain, covariance 파일이 없었다.
- H2가 강해졌다. bundle은 TeX, bibliography/style, figure PDF 중심이었다.

### 3.2 추출본을 실제로 `ls`로 확인

압축 manifest만 믿지 않고 실제 추출 디렉터리도 확인했다.

```bash
rtk ls -lha /private/tmp/qfuds_2506_18477_src
```

핵심 출력:

```text
00README.json  215B
JHEP.bst  19.9K
fig_bayes_data.pdf  89.7K
fig_bin30.pdf  101.3K
fig_evals.pdf  157.1K
fig_mock_lcdm.pdf  100.8K
fig_pc.pdf  158.1K
fig_reconstruct.pdf  168.3K
fig_zmax.pdf  101.3K
idenpr.bib  101.3K
idenpr.tex  42.6K
jcappub.sty  11.0K
```

파일 타입도 확인했다.

```bash
rtk file /private/tmp/qfuds_2506_18477_src/*
```

핵심 출력:

```text
00README.json:       JSON data
fig_reconstruct.pdf: PDF document, version 1.4, 1 pages
fig_pc.pdf:          PDF document, version 1.4, 1 pages
fig_evals.pdf:       PDF document, version 1.4, 1 pages
idenpr.bib:          Unicode text, UTF-8 text
idenpr.tex:          LaTeX 2e document text, ASCII text
jcappub.sty:         LaTeX document text, ASCII text
```

판정:

- 추출 디렉터리에도 숨은 하위 디렉터리나 data-like file은 없었다.
- 하지만 figure PDF는 충분히 의미 있는 asset이었다. 특히 `fig_reconstruct.pdf`, `fig_pc.pdf`, `fig_evals.pdf`가 timing-overlap에 직접 연결된다.

### 3.3 TeX source에서 data availability 단서 확인

다음은 TeX와 bib 내부에서 repository, supplement, data availability 문구를 찾았다.

```bash
rtk rg -n "(Data|data|Code|code|availability|Supplement|repository|github|Zenodo|OSF|Dataverse|figshare|archive|Ancillary)" /private/tmp/qfuds_2506_18477_src/idenpr.tex
```

확인된 것은 주로 논문 본문 내용이었다.

```text
Figure 1. Reconstructed evolution history of beta(z) ...
DESI DR2-based results ... lower reconstruction uncertainties in the redshift range 0.3 < z < 2.5.
```

판정:

- TeX 본문에서 별도 public data repository 문구는 확인되지 않았다.
- 대신 timing 분석에 중요한 본문 단서가 확보됐다: sign reversal, high-z positive beta, DR2 uncertainty reduction, robustness appendix.

### 3.4 PDF 내부 attachment/URI 단서 확인

PDF 안에 embedded file이나 외부 URL annotation이 있을 가능성도 확인했다.

```bash
rtk strings /private/tmp/qfuds_2506_18477_src/fig_reconstruct.pdf \
  /private/tmp/qfuds_2506_18477_src/fig_pc.pdf \
  /private/tmp/qfuds_2506_18477_src/fig_evals.pdf \
  /private/tmp/qfuds_2506_18477_src/fig_bin30.pdf \
  /private/tmp/qfuds_2506_18477_src/fig_zmax.pdf \
  /private/tmp/qfuds_2506_18477_src/fig_bayes_data.pdf \
  /private/tmp/qfuds_2506_18477_src/fig_mock_lcdm.pdf \
  | rg -n "(/EmbeddedFiles|/Filespec|/FileAttachment|/URI|github|zenodo|osf|dataverse|csv|dat|npy|chain|cov|posterior|Matplotlib)"
```

핵심 출력:

```text
<< /Creator (Matplotlib v3.8.4, https://matplotlib.org)
/Producer (Matplotlib pdf backend v3.8.4)
```

판정:

- H3은 기각했다. PDF들은 Matplotlib PDF로 보였고, embedded file이나 data URL 단서는 없었다.
- 다만 Matplotlib source figure PDF이므로 고해상도 rasterization과 digitization 입력으로는 유용했다.

### 3.5 외부 archive/search 확인

외부 검색은 audit 문서에 정리했다. 핵심 결과는 다음이다.

| 경로 | 판정 |
| --- | --- |
| GitHub exact arXiv ID/title/code search | paper-specific data repo 없음 |
| Zenodo exact/broad search | Li & Zhang reconstruction product 없음 |
| OSF exact search | 없음 |
| Harvard Dataverse exact search | 없음 |
| JCAP/IOP HTML | checked HTML에서 supplement/data hook 없음 |
| ResearchGate/ORCID/J-GLOBAL/citation mirrors | bibliographic metadata만 확인 |

판정:

- H5는 현재 공개 경로 기준으로 기각했다.
- 단, "없다"가 아니라 "현재 확인 가능한 public product를 찾지 못했다"로 기록했다. 나중에 저자 제공 자료나 비공개 archive가 나올 수 있기 때문이다.

## 4. 추가 확인: cache와 digitization 준비

자료가 numerical product는 아니더라도, figure-level product는 다음 분석의 입력이 된다. 그래서 local cache를 만들었다.

```text
docs/wiki/research/assets/figures/li_2025/
```

현재 구조:

```text
README.md
paper_arxiv_2506.18477v2.pdf
source/arxiv_source_2506.18477v2.tar.gz
source/extracted/00README.json
source/extracted/JHEP.bst
source/extracted/fig_bayes_data.pdf
source/extracted/fig_bin30.pdf
source/extracted/fig_evals.pdf
source/extracted/fig_mock_lcdm.pdf
source/extracted/fig_pc.pdf
source/extracted/fig_reconstruct.pdf
source/extracted/fig_zmax.pdf
source/extracted/idenpr.bib
source/extracted/idenpr.tex
source/extracted/jcappub.sty
```

그 다음 digitization용 PNG도 만들었다.

```bash
qlmanage -t -s 2400 -o /private/tmp/qfuds_li2025_ql_all \
  docs/wiki/research/assets/figures/li_2025/source/extracted/fig_reconstruct.pdf \
  docs/wiki/research/assets/figures/li_2025/source/extracted/fig_bayes_data.pdf \
  docs/wiki/research/assets/figures/li_2025/source/extracted/fig_evals.pdf \
  docs/wiki/research/assets/figures/li_2025/source/extracted/fig_pc.pdf \
  docs/wiki/research/assets/figures/li_2025/source/extracted/fig_mock_lcdm.pdf \
  docs/wiki/research/assets/figures/li_2025/source/extracted/fig_bin30.pdf \
  docs/wiki/research/assets/figures/li_2025/source/extracted/fig_zmax.pdf
```

핵심 출력:

```text
fig_reconstruct.pdf produced one thumbnail
fig_bayes_data.pdf produced one thumbnail
fig_bin30.pdf produced one thumbnail
fig_mock_lcdm.pdf produced one thumbnail
fig_pc.pdf produced one thumbnail
fig_zmax.pdf produced one thumbnail
fig_evals.pdf produced one thumbnail
Done producing thumbnails
```

출력 이미지 확인:

```bash
rtk file docs/wiki/research/assets/digitization/li_2025/*.png
```

핵심 출력:

```text
fig_bayes_data.png:  PNG image data, 2400 x 1920
fig_bin30.png:       PNG image data, 2400 x 1782
fig_evals.png:       PNG image data, 2400 x 1789
fig_mock_lcdm.png:   PNG image data, 2400 x 1782
fig_pc.png:          PNG image data, 2400 x 1753
fig_reconstruct.png: PNG image data, 2400 x 619
fig_zmax.png:        PNG image data, 2400 x 1823
```

판정:

- 공개 numerical product는 못 찾았지만, future digitization protocol에 쓸 수 있는 local figure cache는 확보했다.
- 이 덕분에 이후 qualitative timing-overlap analysis를 repo-local evidence만으로 수행할 수 있었다.

### 4.1 PDF 처리 한계와 Markdown 변환본

여기서 한 가지 한계가 분명했다. figure PDF는 digitization 입력으로 정리했지만, 논문 본문 PDF(`paper_arxiv_2506.18477v2.pdf`) 자체는 agent가 안정적으로 텍스트를 추출하지 못했다. `strings`나 부분 텍스트로는 단서를 잡을 수 있었지만, 본문 전체를 신뢰할 수 있는 순서와 수식으로 읽어내는 데는 실패했다.

이 한계는 agent 쪽에서 우회하지 않았다. 대신 사용자가 별도 도구로 논문 전체를 하나의 완성형 Markdown 문서로 변환했다.

```text
docs/wiki/research/assets/digitization/li_2025/paper_arxiv_2506.18477v2.md
```

- 810줄 규모의 full-paper Markdown 변환본이다.
- frontmatter는 `asset_markdown_li_2025_desi_dr2_sign_reversal_ide`로 묶여 있고, `asset_li_2025_desi_dr2_sign_reversal_ide` literature node에 depends_on으로 연결된다.
- 이후 timing-overlap 분석에서 본문 caption, dataset 조합, robustness 설명을 인용할 때 PDF가 아니라 이 Markdown을 단일 text source로 쓴다.

판정:

- agent의 PDF 본문 추출 한계는 우회 대상이 아니라 기록 대상이다.
- 신뢰할 수 있는 text-level source는 사람이 만든 Markdown 변환본이고, 이것이 figure cache/PNG와 함께 이 사건의 실질적 산출물이다.

| 자료 | 누가 만들었나 | 역할 |
| --- | --- | --- |
| `paper_arxiv_2506.18477v2.pdf` | arXiv 원본 | 보관용 원본. agent 본문 추출은 신뢰 불가 |
| `paper_arxiv_2506.18477v2.md` | 사용자 (외부 도구) | text-level 분석의 단일 source |
| `source/extracted/*.pdf` figure | arXiv source bundle | digitization 입력 |
| `digitization/li_2025/*.png` | `qlmanage -t -s 2400` | 고해상도 digitization 이미지 |

### 4.2 회고: 왜 `ls`가 연구 판단을 바꿨나

`ls` 자체가 대단한 명령이라서가 아니다. 중요한 것은 판단의 근거가 바뀐 점이다.

| 단계 | 판단 근거 | 위험 |
| --- | --- | --- |
| 웹 검색만 한 상태 | 검색 결과에 data repo가 안 보임 | archive/source bundle 안의 figure product를 놓칠 수 있음 |
| arXiv source manifest 확인 | 제출 source package의 실제 파일 목록 | numerical product 부재를 더 강하게 말할 수 있음 |
| extracted `ls` 확인 | 로컬 파일 시스템의 실제 추출 결과 | nested directory나 숨은 source file 누락 가능성을 줄임 |
| PDF/TeX 내부 검색 | figure와 원고 자체의 metadata/text | figure-level product와 timing 문구를 evidence로 분리 가능 |

이 순서 덕분에 결론이 이렇게 정밀해졌다.

```text
틀린 결론:
Li & Zhang에는 쓸 자료가 없다.

정확한 결론:
Li & Zhang에는 classification-level numerical product는 공개되어 있지 않다.
하지만 timing comparison의 다음 단계에 필요한 figure-level product는 있다.
```

이 차이가 크다. 첫 번째 결론이면 Li & Zhang branch를 접게 된다. 두 번째 결론이면 digitization protocol이나 author-data request로 넘어갈 수 있다.

## 5. 결론 / 해결

최종 결론은 세 단계다.

| 질문 | 결론 | 근거 |
| --- | --- | --- |
| Li & Zhang public numerical product가 이미 있는가? | 현재 확인 가능한 범위에서는 없음 | arXiv source, GitHub, Zenodo, OSF, Dataverse, publisher page 확인 |
| timing-overlap matrix를 즉시 full classification으로 실행할 수 있는가? | 아니오 | numerical beta(z), uncertainty array, covariance, posterior, PCA array 부재 |
| 다음 단계에 쓸 local evidence는 확보했는가? | 예 | TeX, figure PDFs, full paper PDF, 사용자가 만든 full-paper Markdown 변환본, high-resolution PNG cache 확보 |
| 논문 본문을 신뢰 가능한 text로 읽을 수 있는가? | 예, 단 PDF가 아니라 Markdown으로 | agent의 PDF 본문 추출은 실패했고, 사용자가 외부 도구로 만든 Markdown이 단일 text source |

중요한 결정:

- `public product availability`는 `partially`로 둔다.
- Exp006의 `allowed_but_not_informative` 결론은 변경하지 않는다.
- 새 실험은 만들지 않는다.
- Li & Zhang은 계속 highest-priority timing target으로 유지하되, 다음 단계는 digitization protocol 또는 author-data request다.

안 고른 대안:

| 대안 | 왜 안 골랐나 |
| --- | --- |
| 검색 결과만 보고 "no public data"로 끝내기 | arXiv source bundle 내부 figure PDF를 놓칠 수 있었다 |
| figure PDF를 바로 분석 결과로 승격하기 | numerical uncertainty/covariance가 아니므로 classification-level evidence가 아니다 |
| Exp006 결론을 즉시 상향하기 | 아직 retained timing이 simpler alternatives보다 낫다는 수치 비교가 없다 |
| roadmap status를 바꾸기 | asset cache와 qualitative overlap은 roadmap-level result가 아니다 |

### 5.1 연구적으로 바뀐 것과 안 바뀐 것

이번 작업으로 바뀐 것은 "retained timing이 맞다"가 아니다. 바뀐 것은 질문의 수준이다.

작업 전 상태:

```text
구조 형성 시기 intuition이 IDE/DESI reconstruction literature와 실제로 만나는지 불명확함.
Exp006은 allowed_but_not_informative.
Escamilla table-level evidence만으로는 timing branch를 지지하기 어려움.
```

작업 후 상태:

```text
Li & Zhang 2025에서 sign-reversal beta(z) reconstruction을 확인.
논문은 high-z positive beta와 DR2의 0.3 < z < 2.5 uncertainty reduction을 보고.
Figure 1과 robustness Figure 6은 z ~= 1.7-2.1 부근 positive-beta region을 보여줌.
이 구간은 Exp005 retained weighted mean z ~= 1.746, peak z ~= 2.046과 겹침.
```

그래서 이 작업은 다음과 같이 분류한다.

| 항목 | 판정 |
| --- | --- |
| QFUDS physical support | 아님 |
| retained timing physical derivation | 아님 |
| Exp006 conclusion update | 아님 |
| DESI-era IDE reconstruction과의 timing-region overlap | 있음, 현재는 moderate |
| supported_compression_target 승격 | 아직 아님 |
| 다음 실행 가능한 방향 | digitized uncertainty 또는 author numerical products 기반 timing-overlap matrix |

이게 중요한 이유는 "직감"이 바로 "증명"으로 뛴 게 아니라, 중간에 검증 가능한 연구 질문으로 바뀌었기 때문이다.

```text
직감:
구조 형성 시기에 뭔가 있다.

문헌 대조 가능한 질문:
DESI-era nonparametric/sign-reversal IDE reconstruction에서
retained timing peak/weighted-mean 부근에 data-supported beta(z) structure가 있는가?
```

이 전환이 이번 작업의 가장 큰 성과다.

## 6. 재발 방지 / 운영 메모

비슷한 논문-data 탐색은 다음 순서로 해야 한다.

1. 논문 본문/abstract만 읽지 말고 arXiv `e-print` source bundle을 받는다.
2. `tar` manifest와 extracted `ls`를 둘 다 확인한다.
3. data-like 확장자만 찾지 말고 figure PDF도 product로 분류한다.
4. PDF 내부 attachment/URI 단서를 확인한다.
5. GitHub/Zenodo/OSF/Dataverse는 exact ID, exact title, figure filename, author/title variants로 나눠 찾는다.
6. "없다"는 말 대신 "현재 확인 가능한 public product를 찾지 못했다"로 쓴다.
7. numerical product가 없으면 figure cache와 digitization-ready PNG를 repo에 남긴다.
8. 논문 본문 PDF의 text 추출이 agent에서 불안정하면 우회하지 말고 한계로 기록한다. 신뢰 가능한 text source가 필요하면 사람이 만든 full-paper Markdown 변환본을 단일 source로 삼고 repo에 남긴다.

명시적으로 아직 안 한 것:

- posterior recovery는 하지 않았다.
- covariance reconstruction은 하지 않았다.
- figure digitization으로 numeric beta(z) table을 만들지는 않았다.
- timing-overlap matrix를 새 experiment로 실행하지 않았다.
- roadmap, decision log, Exp006 result는 변경하지 않았다.

## 7. 타임라인

- Li & Zhang 2025가 Exp006 coverage expansion 이후 highest-priority timing target으로 지정됐다.
- timing-feasibility audit에서 "yes, conditionally"로 판정했다.
- timing-overlap matrix plan을 작성했다.
- public product search에서 GitHub, Zenodo, OSF, Dataverse, publisher page를 확인했다.
- 사용자가 `너무 좁게 검색한거아냐?`라고 지적하면서 exact search를 넘어 broader archive/code search로 확장했다.
- 사용자가 `걍 ls 해서 확인해봐;`라고 지시하면서 arXiv source bundle을 다운로드하고 실제 파일 목록을 확인했다.
- 사용자가 `재귀적으로 모든 파일 다 훝어봐.`라고 지시하면서 `tar`, `ls`, `file`, `rg`, `strings`로 source tree와 PDF 내부 단서를 확인했다.
- 사용자가 `tar 파일같은거 없냐?`라고 지적하면서 nested archive/data-like file 가능성을 별도로 확인했다.
- numerical product는 찾지 못했지만 figure PDFs와 TeX source를 확인했다.
- 사용자가 `pdf 가 존나 중요해보이는데`라고 짚으면서 figure PDF를 future digitization input으로 분류했다.
- `docs/wiki/research/assets/figures/li_2025/`에 source bundle, extracted files, full paper PDF를 캐싱했다.
- 사용자가 `docs/research/assets 가 존재함`과 `source 는 tar 도 드가야되는거아니녀?`라고 지적하면서 asset tree 구조를 repo convention에 맞게 재정리했다.
- 사용자가 `고해상도 필요해`라고 지적하면서 낮은 해상도 변환을 버리고 `qlmanage -t -s 2400` 고해상도 렌더로 전환했다.
- `docs/wiki/research/assets/digitization/li_2025/`에 고해상도 PNG 7개와 figure map을 추가했다.
- 논문 본문 PDF는 agent가 안정적으로 추출하지 못했다. 사용자가 별도 도구로 논문 전체를 `paper_arxiv_2506.18477v2.md`(810줄) 완성형 Markdown으로 변환해 text-level 단일 source로 확보했다.
- Li & Zhang reconstruction과 Exp005 retained timing profile의 qualitative overlap을 분석했다.
- 회고상 핵심 판단을 정리했다: 이 작업은 QFUDS 지지가 아니라, retained structure-era timing intuition이 DESI-era IDE reconstruction feature와 비교 가능한 질문으로 올라간 사건이다.

## 부록 A — 디버깅 명령어 모음

### arXiv source bundle manifest 보기

```bash
rtk tar -tzvf /private/tmp/qfuds_2506_18477_src.tar
```

일반 의미:

- `tar -t`는 archive 안의 파일 목록을 출력한다.
- `-z`는 gzip 압축을 처리한다.
- `-v`는 크기와 timestamp까지 자세히 보여준다.
- `-f`는 대상 archive 파일을 지정한다.

이 사건에서 본 것:

- `.csv`, `.dat`, `.npy`, `.npz`, chain, covariance 파일이 있는지 확인했다.
- 결과는 TeX, bib/style, figure PDF 중심이었다.

### 실제 추출 디렉터리 확인

```bash
rtk ls -lha /private/tmp/qfuds_2506_18477_src
```

일반 의미:

- `ls`는 디렉터리 파일 목록을 보여준다.
- `-l`은 자세한 목록, `-h`는 사람이 읽기 쉬운 크기, `-a`는 숨김 파일 포함이다.

이 사건에서 본 것:

- archive manifest와 실제 추출 결과가 같은지 확인했다.
- 숨은 data directory가 없다는 판단을 강화했다.

### 파일 타입 확인

```bash
rtk file /private/tmp/qfuds_2506_18477_src/*
```

일반 의미:

- `file`은 확장자만 보지 않고 파일 magic/header를 보고 타입을 추정한다.

이 사건에서 본 것:

- figure 파일들이 PDF document인지 확인했다.
- TeX source와 JSON README가 텍스트로 읽을 수 있음을 확인했다.

### 텍스트 source에서 단서 찾기

```bash
rtk rg -n "(Data|data|Code|code|availability|Supplement|repository|github|Zenodo|OSF|Dataverse|figshare|archive|Ancillary)" /private/tmp/qfuds_2506_18477_src/idenpr.tex
```

일반 의미:

- `rg`는 빠른 텍스트 검색 도구다.
- `-n`은 줄 번호를 같이 출력한다.

이 사건에서 본 것:

- 별도 data availability나 repository 문구가 있는지 찾았다.
- 명시적인 public data hook은 못 찾았고, 대신 Figure 1/6의 timing 관련 문구를 확인했다.

### PDF 내부 단서 찾기

```bash
rtk strings /private/tmp/qfuds_2506_18477_src/fig_reconstruct.pdf \
  /private/tmp/qfuds_2506_18477_src/fig_pc.pdf \
  /private/tmp/qfuds_2506_18477_src/fig_evals.pdf \
  | rg -n "(/EmbeddedFiles|/Filespec|/URI|github|zenodo|csv|dat|npy|chain|cov|posterior|Matplotlib)"
```

일반 의미:

- `strings`는 binary 파일 안에서 사람이 읽을 수 있는 문자열만 뽑는다.
- PDF 내부 metadata, URI, embedded file 관련 키워드를 빠르게 확인할 수 있다.

이 사건에서 본 것:

- embedded data file이나 repository URL 단서는 없었다.
- Matplotlib PDF backend로 생성된 figure라는 단서는 있었다.

### PDF를 digitization용 PNG로 렌더링

```bash
qlmanage -t -s 2400 -o /private/tmp/qfuds_li2025_ql_all \
  docs/wiki/research/assets/figures/li_2025/source/extracted/fig_reconstruct.pdf
```

일반 의미:

- macOS `qlmanage -t`는 Quick Look thumbnail을 생성한다.
- `-s 2400`은 출력 폭/스케일을 크게 잡아 고해상도 PNG를 만든다.
- `-o`는 출력 디렉터리를 지정한다.

이 사건에서 본 것:

- `sips` 기본 변환은 낮은 해상도였다.
- `qlmanage -t -s 2400`은 digitization에 더 적합한 2400px wide PNG를 만들었다.

응용 팁:

- 논문 data product 탐색은 `metadata search -> source bundle -> extracted files -> PDF internals -> external archives -> local cache` 순서가 안전하다. 중간에 "없다"고 단정하면 figure-level product를 놓치기 쉽다.

## 부록 B — 왜 figure PDF도 중요한가

numerical product가 없으면 비교를 포기해야 하는 것은 아니다. 다만 증거 수준을 낮춰야 한다.

| 자료 | 가능한 일 | 불가능한 일 |
| --- | --- | --- |
| figure PDF | 축, sign region, transition region, rough uncertainty band 확인 | covariance-aware classification |
| high-resolution PNG | WebPlotDigitizer류 도구로 mean/band digitization | 원저자 posterior 복원 |
| TeX caption/body | figure 의미, dataset 조합, robustness 설명 확인 | numerical beta_i 재현 |
| posterior/covariance/chains | uncertainty-aware timing-overlap matrix | 공개되지 않으면 사용 불가 |

이번 작업의 핵심은 "숫자 파일이 없으니 끝"이 아니었다. 정확한 판정은 다음이다.

```text
classification-level numerical product는 없다.
하지만 figure-level product는 있고, digitization-ready cache까지 만들 수 있다.
```

그래서 Li & Zhang 2025는 여전히 다음 timing-overlap 분석의 최우선 target으로 남는다.

## 부록 C — 이번 사건의 연구 교훈

이 사건은 "논문 하나를 더 찾았다"보다 크고, "새 물리학을 찾았다"보다 작다. 정확히는 검증 가능한 질문의 해상도가 올라간 사건이다.

처음에는 다음에 가까웠다.

```text
구조 형성 시기가 수상하다.
```

이 문장은 연구 질문으로는 너무 약하다. 어떤 이론 family와 비교하는지, 어떤 observable timing과 연결되는지, 어떤 문헌이 반례나 지지 후보인지가 없다.

Exp004 이후에는 질문이 조금 좁아졌다.

```text
retained P1은 IDE/IV phenomenology로 읽을 수 있는가?
```

Exp005 이후에는 timing prior 문제가 생겼다.

```text
retained timing profile은 known IV/IDE coupling histories를 압축하는 후보가 될 수 있는가?
```

Exp006 이후에는 한 번 멈췄다.

```text
Escamilla table-level comparison으로는 allowed_but_not_informative.
```

여기서 끝냈으면 "직감은 흥미롭지만 문헌 대조에서 애매함"으로 정리됐을 수 있다. 하지만 coverage question을 다시 던지면서 다음 질문으로 바뀌었다.

```text
Escamilla만 본 것이 충분한가?
DESI-era nonparametric/sign-switching IDE reconstruction은 같은 timing region을 가리키는가?
```

Li & Zhang 2025가 중요해진 이유가 여기에 있다. 이 논문은 retained timing과 같은 물리적 가정을 하지 않는다. 오히려 known IDE framework 안에서 DESI DR2, CMB, SNIa를 사용해 beta(z)를 non-parametric하게 재건한다. 그래서 겹침이 보이면 최소한 다음 말은 할 수 있다.

```text
retained structure-era timing intuition은
완전히 독립적인 DESI-era IDE reconstruction에서 보이는
structure-era positive-beta region과 비교할 수 있다.
```

아직 말하면 안 되는 것도 분명하다.

```text
Li & Zhang이 QFUDS를 지지한다.
retained timing이 물리적으로 유도됐다.
retained timing이 simpler timing family보다 낫다.
Exp006 결론을 바꿔야 한다.
```

현재 말할 수 있는 가장 강한 문장은 이것이다.

```text
Li & Zhang 2025는 retained timing branch를 폐기하기보다
digitized uncertainty 또는 author data로 더 날카롭게 비교할 이유를 제공한다.
```

이 정도가 좋은 연구 상태다. 과장하지 않고, 닫지도 않고, 다음에 무엇을 측정해야 하는지 분명해졌다.
