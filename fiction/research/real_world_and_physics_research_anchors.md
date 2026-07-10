---
doc_id: qfuds_saga_real_world_and_physics_research_anchors_ko
title: QFUDS SAGA 실세계·물리 리서치 앵커 대장 (핍진성 닻)
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_near_future_forecast_panel_method_ko
  - qfuds_saga_reader_accessibility_and_real_world_anchors_ko
next_gate: 근미래 프렐류드(story_design 322)와 in-world 물리(320)의 핍진성 닻으로 인용. 픽션 전용, QFUDS 증거 아님
last_updated: 2026-07-10
---

# QFUDS SAGA 실세계·물리 리서치 앵커 대장 (핍진성 닻)

## 이 문서의 자리

근미래 예측 세계관(로봇→노동→Q-Day)과 in-world 물리·먼 미래 우주론 substrate의 **핍진성
닻**을 신뢰 출처에서 긁어와 중립 톤으로 정리한 대장이다. 08개 리서치 렌즈(근미래 5 + 물리 3)의
결과다. 픽션은 이 자료를 "그럴듯함"의 근거로만 인용하고, 실제 예측·투자·정치 주장으로 쓰지
않는다.

```text
fiction/provenance only
research evidence: no  (QFUDS 물리 support 아님. 이 세계관은 이 자료를 물리적 사실로 주장하지 않는다)
external source claim: 아래 출처표는 신뢰 출처의 중립 인용이며, repo 자산 캐시가 아니다
workflow: Research Asset and Product Workflow 적용
  - 근미래 5종: state=hit_not_cached (WebSearch 스니펫 확인, 여러 원문은 자동 fetch 403, repo 캐시 안 함)
  - 물리 3종: state=hit_not_cached (alphaXiv MCP로 원문 열람, repo 자산 번들 저장은 안 함)
  - 이미 literature/에 있는 물리 논문은 중복 생성 없이 교차참조
  - 2026-07-02 갱신(§A6): 신규 WebSearch 스니펫은 state=hit_not_cached. 단 Gidney 2025
    (arXiv:2505.15917)만 PDF 정식 캐싱 = state=asset_cached, 매니페스트
    [research/assets/gidney_2025_rsa_factoring_noisy_qubits](../../docs/wiki/research/assets/gidney_2025_rsa_factoring_noisy_qubits/README.md)
스타일: em dash 0, "박-" 슬랭 금지, 중립 톤(정치색 배제, 범위·복수추정 병기, contested 플래그)
```

중립 규율: 모든 논쟁적 수치는 **범위와 복수 추정치를 병기**하고, 낙관/비관·정파 프레임이
갈리는 지점은 `contested`로 표시한다. 벤더 자체 발표는 그렇게 표시한다.

---

## PART A. 근미래 실세계 앵커 (2020s-2090s 예측 근거)

### A1. 휴머노이드 로봇·자동화 역량 (state=hit_not_cached)

- **산업용 로봇은 이미 거대·성숙**(비논쟁 배경): IFR World Robotics 2025 = 2024년 운영 대수
  약 466만, 신규 설치 54.2만(4년 연속 50만+). 아시아 74%. 중국 단독 약 202.7만 대·29.5만 설치
  (세계 54%). 이건 "자동화는 이미 어디에나"의 단단한 닻이다.
- **휴머노이드는 '배치됐으나 좁고 불안정'**(논쟁 지대): Figure/BMW Spartanburg 파일럿(단일
  작업, 자체발표 약 1,250시간·부품 9만+), Tesla Optimus의 "2025년 1만 대"는 미달, 약 2hr 배터리,
  MTBF 미공개, 손재주·일반화 한계. Rodney Brooks는 영상학습 손재주를 "순전한 환상"이라 비판;
  낙관론은 "완벽보다 유용성 먼저"로 반박.
- **2035 전망의 자릿수 불일치**(논쟁): Goldman - $38B/1.4M대, Morgan Stanley - $5T(2050),
  2차 집계는 $9B-$251B. 방향은 합의, **규모·시점은 크게 불일치.**

| 출처 | URL | 시점 | 핵심 | contested |
| --- | --- | --- | --- | --- |
| IFR World Robotics 2025 | ifr.org/ifr-press-releases | 2025-09 | 466만 운영, 54.2만 설치 | N |
| Figure AI "Production at BMW" | figure.ai/news/production-at-bmw | 2025 | 파일럿 자체발표 수치 | Y(자체) |
| Rodney Brooks blog | rodneybrooks.com/why-todays-humanoids-wont-learn-dexterity | 2025-09 | 손재주 회의 | Y(회의) |
| Goldman Sachs Research | goldmansachs.com/insights | 2024-25 | 약 $38B/1.4M대(2035) | Y(전망) |
| Morgan Stanley | morganstanley.com/insights | 2025 | 약 $5T(2050) | Y(전망) |

**픽션 매핑:** 역량 A/B/C 분기(제한적/젠야타급/롤백)의 근거. "배치됐으나 좁고 불안정"이
2020s-2030s 기본값, "범용 대체"는 2040s+ back-loaded·논쟁 전망으로 그린다.

### A2. 자동화 노동경제 ("노동의 종말"은 논쟁) (state=hit_not_cached)

- 헤드라인 "X% 일자리"는 대부분 **노출(exposure)**이지 소멸이 아니다. IMF(2024): 세계 약 40%
  /선진국 약 60% 노출, 그중 절반은 보강·절반은 대체 압력. Frey-Osborne(2013) 47%(직업 단위) vs
  OECD(2016) 9%(과업 단위) = 방법론 차이(약 5배).
- **주류 컨센서스 = "변형·재분류 + 분배 스트레스"**, 대량 기술실업이 아니다. ILO(2023/2025):
  대체보다 보강, 사무직 최다 노출, 최고노출은 세계고용 3.3%. WEF FoJ 2025: 2030까지 순 +78M
  (창출 170M − 대체 92M, 단 이건 전망).
- 경제학 양극: Autor(재도입 효과, 낙관) vs Acemoglu(생산성 미미+불평등, 회의). **둘 다 "노동의
  종말"을 예측하지 않는다.** Stanford "Canaries"(2025): 최다노출 직군 22-25세 고용 13% 상대감소
  (초입 사다리 효과, 좁고 초기).

| 출처 | URL | 시점 | 핵심 | contested |
| --- | --- | --- | --- | --- |
| IMF Gen-AI SDN/2024/001 | imf.org/.../sdnea2024001.pdf | 2024-01 | 40%/60% 노출, 절반 대체압 | Y(노출≠소멸) |
| OECD (Arntz et al.) 2016 | oecd.org | 2016 | 9%(과업 단위) | Y(Frey 반박) |
| ILO WP96 / WP140 | ilo.org | 2023/2025 | 보강>대체, 최고노출 3.3% | N |
| WEF Future of Jobs 2025 | reports.weforum.org | 2025-01 | 순 +78M(2030) | Y(전망) |
| Acemoglu NBER w32487 | nber.org/papers/w32487 | 2024 | TFP ≤0.66%/10년 | Y(회의 극) |
| Autor NBER w30389 | nber.org/papers/w30389 | 2022 | 고용 60%가 1940년 이후 신직종 | N |
| Stanford "Canaries" | digitaleconomy.stanford.edu | 2025-11 | 초입 22-25세 13%↓ | Y(초기) |

**픽션 매핑:** 캐논의 "재분류(재직·검증·판단 노동으로 이동)"를 그대로 뒷받침. "완전 노동소멸"은
주류 밖 사변이므로 patchwork 변경 쪽에만, 그것도 사변으로 표시.

### A3. AI 역량 예측 + 컴퓨트·반도체 지정학 (state=hit_not_cached)

- 스케일링(Epoch/Stanford HAI): 훈련 컴퓨트 연 약 4.4x(약 5-6개월 배가), 비용 약 8개월 배가
  (최대 훈련 2027년 $1B+ 전망), METR 과업 시간지평 약 7개월 배가(최근 약 4개월 가속은 논쟁).
- 전문가 타임라인 **스프레드가 핵심**: 대규모 서베이 HLMI 10% 2027/50% 2047, 전직종 자동화
  50% 2116; 근단기 낙관(일부 2026-27) vs 회의(Marcus 등). 정의 불일치가 격차를 키움.
- 칩 지정학(논쟁·정파 민감): TSMC 최첨단 약 90%+, 수출통제(2022-2025 강화), "sovereign AI" 부상.
  효과성은 CSIS도 양론 병기(지연 vs 우회). 벤더(Nvidia) GPU 수치는 벤더 출처로 표시.

| 출처 | URL | 시점 | 핵심 | contested |
| --- | --- | --- | --- | --- |
| Epoch AI Trends | epoch.ai/trends | 2024-25 | 컴퓨트 - 4.4x/년 | N |
| Stanford HAI AI Index 2025 | hai.stanford.edu/ai-index/2025 | 2025-04 | 컴퓨트 - 5개월 배가 | N |
| METR Long Tasks | metr.org/blog/2025-03-19 | 2025-03 | 시간지평 - 7개월 배가 | Y(방법) |
| AI Impacts 서베이 | arxiv.org/abs/2401.02843 | 2024 | HLMI 50% 2047 | Y(스프레드) |
| CSIS 수출통제 | csis.org | 2024-25 | ≥2세대 격차 목표 | Y(정파) |
| Brookings TSMC | brookings.edu | 2025 | 최첨단 90%+ | Y(지정) |

**픽션 매핑:** 컴퓨트·칩 패권 → 핵심권역 vs 변경 patchwork의 물질 토대. AI 타임라인 스프레드는
작중 인물이 상반된 미래관을 그럴듯하게 대립하는 근거.

### A4. 에너지·데이터센터 + 인구·이주 + UBI (state=hit_not_cached)

- 에너지(IEA Energy and AI 2025): 데이터센터 전력 약 2024년 415-485 TWh → 2030 약 945 TWh
  (세계 약 3%), 2035 시나리오 700-1,700 TWh(자릿수 불확실), 계획 프로젝트 약 20%가 전력망
  병목 위험. **병목이 최공격적 시나리오를 낮춘다.**
- 인구(UN WPP 2024): 세계 인구 2080년대 중반 약 103억 정점 후 감소, 합계출산율 약 2.3(237개국
  중 55%가 대체수준 2.1 미만), 65세+ 2070년대 말 약 22억. 이주가 약 50개국의 감소를 상쇄.
- UBI(파일럿, 정치 민감): Finland(2017-18) 고용효과 미미·웰빙↑(인과 한계), Stockton SEED
  최종 고용효과 비유의(팬데믹 혼입), GiveDirectly Kenya 창업·저축↑·노동 안 줄임. **웰빙엔
  일관, 고용엔 약함·논쟁, 보편성·재정·인플레는 미검증.**

| 출처 | URL | 시점 | 핵심 | contested |
| --- | --- | --- | --- | --- |
| IEA Energy and AI | iea.org/reports/energy-and-ai | 2025-04 | DC 전력 - 945 TWh(2030) | N(전망 범위) |
| UN WPP 2024 | population.un.org/wpp | 2024-07 | 정점 103억(2080s), 출산율 2.3 | N |
| VATT Finland UBI | vatt.fi | 2020-05 | 고용 미미·웰빙↑ | Y(인과) |
| Stanford SEED (CalMatters) | calmatters.org | 2023-04 | 최종 고용효과 비유의 | Y |
| GiveDirectly Kenya | givedirectly.org/2023-ubi-results | 2023-12 | 창업↑·노동 유지 | Y(전이) |

**픽션 매핑:** 데이터센터 전력 병목 = 계급·지리 분화의 물질 근거. 고령화·저출생·이주 = 돌봄
노동·역량 분기 A(돌봄이 피난처)의 근거. UBI = patchwork 변경의 "붕괴+UBI 실패" 톤(주류 밖
사변으로 표시).

### A5. 양자 위협·PQC + 딥페이크·검증경제 (Q-Day 근거) (state=hit_not_cached)

- PQC(문서화된 정책): NIST FIPS 203/204/205(ML-KEM/ML-DSA/SLH-DSA, 2024-08 확정), NSA CNSA
  2.0 마감 2027-2035, HNDL("지금 수집·나중 복호")은 널리 수용. **CRQC 도래 시점은 극도로
  불확실**(약 2030-2035 무게, 10-30년 이견). "Q-Day"는 일정이 아니라 명명.
- 딥페이크·출처증명: C2PA(2021-, 서명된 provenance) 표준이 소셜 재압축에 **벗겨짐**(RAND도
  "개방 생태계에선 비현실적"). 딥페이크 급증(Sumsub 2년 약 40배, Entrust "5분마다 1건" 등
  벤더별 방법 상이=directional). **Arup $25M 딥페이크 CFO 영상 사기(2024)** = 단단한 실사건 닻.
- 검증경제: Truepic 등 "진본성 서비스"가 유료 신뢰 층으로 판매 → 진본성 有/無 계급의 실모델.

| 출처 | URL | 시점 | 핵심 | contested |
| --- | --- | --- | --- | --- |
| NIST PQC (CSA) | cloudsecurityalliance.org | 2024-08 | FIPS 203/204/205 확정 | N |
| NSA CNSA 2.0 (QuSecure) | qusecure.com | 2024-26 | 2027-2035 마감 | N(정책) |
| Palo Alto "What is Q-Day" | paloaltonetworks.com/cyberpedia/what-is-q-day | - | CRQC 약 5-15년, 무게 2030-35 | Y(시점) |
| C2PA / RAND | c2pa.org; truescreen.io | 2021-25 | 소셜서 provenance 벗겨짐 | N |
| CNN Arup 딥페이크 | cnn.com/2024/05/16 | 2024-05 | $25M 딥페이크 사기 | N |

**픽션 매핑:** Q-Day(양자가 서명 붕괴)와 검증경제(Aletheia)의 직접 근거. C2PA 취약성 = "The
Soft Editing"(위조 완벽화)의 현실 메커니즘. Arup 사건 = 근미래 딥페이크 재난의 단단한 닻.
단, 작중 Q-Day 날짜는 극적 허구이며 실제 CRQC 시점 예측이 아님을 유지한다.

### A6. 2026-07-02 갱신: 인식 위기는 이미 현재진행형 (state=asset_cached / hit_not_cached)

A5의 딥페이크·Q-Day 닻은 2025년 데이터였다. 2026-07-02 WebSearch 재확인 결과,
2026년 상반기 현재 세 영역(전쟁·금융·사법신원)이 모두 이미 라이브다. 근미래 인식 위기는
예측이 아니라 현재 상태이며, 픽션의 단일 파국 기둥은 이 기준선 위에 놓는다. 아래는 신뢰
출처 중립 인용이고, 정파색이 갈리는 지점은 contested로 표시한다. 벤더 자체 수치도 그렇게
표시한다.

- **전쟁 위조(라이브):** 2026-02-28 미국·이스라엘의 대이란 군사행동 이후 AI 가짜 홍수.
  텔아비브 피격 가짜 영상, "네타냐후 사망·AI 딥페이크 등장" 허위, 조작 사상자, 게임 영상의
  실전 둔갑. 생성은 수 분, 검증은 느린 수동. 이 비대칭이 핵심이다.
- **금융 위조(라이브):** 딥페이크 사기 누적 약 $2.19B(2025년에만 약 $1.65B). 투자 사기
  (유명인 딥페이크) 약 52%, CEO 사칭 송금 약 25%. 딥페이크 시도 12개월 새 약 +94%.
  GenAI 사기 2027년 연 약 $40B 전망(전망치).
- **사법·신원(라이브):** Mendones v. Cushman & Wakefield(2025-09)에서 딥페이크 영상 증거로
  소송 종료 제재. 판사들이 증거 추정을 가중 검증 쪽으로 이동. 신원확인 시도의 약 58%가
  딥페이크에 뚫림(벤더 방법 상이, directional).
- **법제화:** EU AI Act 50조 AI 생성·조작 콘텐츠 표시 의무가 2026-08-02 발효. 미국 Digital
  Authenticity and Provenance Act(2025). C2PA는 소셜 재압축에 벗겨지며 "역사는 증명하나
  진실은 증명 못 함"으로 구조적 불충분.
- **Q-Day 가속(contested):** Gidney 2025가 RSA-2048을 100만 미만 노이지 큐빗·1주 미만으로
  추정(2019년 2천만 큐빗에서 하향). Cloudflare가 완전 PQC 목표를 2029로 당김. 전 IBM
  수석과학자는 3-4년(개인 견해). 주류 무게는 여전히 2030년대 이후이고, 작동하는 코드깨기
  기계는 아직 없다. 실질 위협은 HNDL(수집 후 복호)이며 그래서 지금 PQC 이주가 진행된다.

| 출처 | URL | 시점 | 핵심 | contested |
| --- | --- | --- | --- | --- |
| Euronews Iran AI fakes | euronews.com/next/2026/03/30 | 2026-03 | 대이란전 딥페이크 홍수 | N(사건) |
| OECD.AI incident | oecd.ai/en/incidents/2026-03-04-c056 | 2026-03 | 중동분쟁 딥페이크 | N(사건) |
| Surfshark deepfake fraud | surfshark.com/research/chart/deepfake-fraud-countries | 2026 | 누적 약 $2.19B | Y(집계) |
| Fortune AI fraud 2026 | fortune.com/2026/01/13 | 2026-01 | $12.5B 사기, 기업 60% 증가 | Y(전망) |
| Thomson Reuters courts | thomsonreuters.com/en-us/posts/ai-in-courts | 2026 | 증거 추정 가중검증 이동 | N |
| Kennedys 86% fake | kennedyslaw.com/en/thought-leadership 2026 | 2026 | 신원확인 약 58% 뚫림 | Y(벤더) |
| EyeSift C2PA / EU AI Act 50 | eyesift.com/ai-image-detection-2026-c2pa | 2026 | 50조 2026-08 발효 | N(정책) |
| Gidney 2025 (asset_cached) | arxiv.org/abs/2505.15917 | 2025-05 | RSA-2048 <1M 큐빗 | Y(이론 추정) |
| The Quantum Insider | thequantuminsider.com/2026/03/31 | 2026-03 | Q-Day 타임라인 재작성 | Y(시점) |
| Benzinga ex-IBM | benzinga.com/Opinion/26/07/60224860 | 2026-07 | Q-Day 3-4년 | Y(개인) |

**픽션 매핑:** 인식 위기는 이미 현재진행형(COVID 비유의 MERS 국면, 사회가 흡수·정상화
중)이다. 그래서 근미래 아크의 단일 파국 기둥(125 위기 1 계열)은 "현재 기준선을 넘는" 임계
사건으로 설계한다. 가짜가 흐리는 수준(현재)이 아니라 실제 방아쇠를 당기는 수준(픽션)이다.
EU AI Act 8월 발효는 작중 검증 의무 제도의 현실 씨앗으로 쓴다. Q-Day는 125의 먼 미래·
소프트·contested 유지가 2026 가속에도 여전히 정당하다(작동 기계 미존재, 주류 2030s+, 시점
극불확실). 두-위기 분리는 불변이다. Gidney 2025 원문은 정식 캐싱했고(state=asset_cached),
나머지 2026 스니펫은 hit_not_cached다.

---

## PART B. 딥피직스 substrate 앵커 (in-world 물리·먼 미래 우주론) (state=hit_not_cached)

이미 `docs/wiki/research/literature/`에 있는 논문은 중복 생성하지 않고 교차참조한다.
alphaXiv MCP로 원문 열람; repo 자산 번들 저장은 안 함.

### B1. 정보 보존·유니터리 + 창발 시공간 (114 substrate)

- **주류**: 블랙홀 정보역설의 현행 해답 = 정보 보존·Page curve 복원(quantum extremal
  surface·island·replica wormhole). 유니터리 = 정보보존·일대일 가역 진화이며 **실용 복원 아님**
  (Hayden-Preskill scrambling). 114의 "정보 보존이되 실용 복원 불가"·복원=재구성과 정합.
- **주류(도메인 한정)**: 홀로그래피·AdS/CFT·Ryu-Takayanagi(얽힘엔트로피=면적).
- **사변**: "우리 우주 시공간이 얽힘에서 완전 창발"(Van Raamsdonk), ER=EPR(Maldacena-Susskind).
  in-world에선 사실, 실세계에선 사변으로 격리.

| 논문 | ref | 플래그 |
| --- | --- | --- |
| Almheiri 외, Entropy of Hawking Radiation (review) | arXiv:2006.06872 | 주류 |
| Hayden-Preskill, Black holes as mirrors | arXiv:0708.4025 | 주류(가정 有) |
| Almheiri-Mahajan-Maldacena-Zhao, Page curve | arXiv:1908.10996 | 주류 |
| Ryu-Takayanagi | hep-th/0603001 | 주류(AdS/CFT) |
| Van Raamsdonk, Building spacetime | arXiv:1005.3035 | 사변 |
| Maldacena-Susskind, ER=EPR | arXiv:1306.0533 | 사변 |
| (교차참조) literature/almheiri_2021_entropy_hawking_radiation.md | - | 기존 캐시 |

### B2. 로런츠 대칭(근본 vs 창발)·시간 화살·텔레포테이션 (114 substrate)

- **주류**: 로런츠 불변은 초정밀 검증(Δc/c ≲ 10^-17). 불변 속도는 시공간 대칭의 성질이지
  빛이 특별해서가 아님. 시간 화살 = 법칙이 아니라 **낮은 엔트로피 초기조건**(Past Hypothesis,
  Penrose Weyl). 텔레포테이션 = 원본 파괴 후 재구성(사본 아님, 노클로닝 위반 아님), **114·113의
  복원=사본·재구성 근거의 정론.**
- **사변**: 로런츠 대칭이 이산 substrate(QCA 격자)에서 창발(Mlodinow-Brun 2025, 격자간격 ≲
  플랑크 수배). "시공간=계산 격자"의 respectable 앵커.

| 논문 | ref | 플래그 |
| --- | --- | --- |
| Jacobson-Liberati-Mattingly, LV bounds | hep-ph/0407370 | 주류 |
| Bennett 외, Quantum teleportation | PRL 70,1895 (1993) | 정론 |
| Wootters-Zurek / Dieks, No-cloning | Nature 299,802 / PLA 92A,271 (1982) | 정론 |
| Al-Khalili-Chen, Arrow of time / EPH | arXiv:2405.03418 | 주류틀+신제안 |
| Mlodinow-Brun, QCA lattice bounds | arXiv:2506.20136 | 사변 |

### B3. 화이트홀 바운스·잔해·우주상수 (White Hole 스레드·003·DM↔DE)

- **주류(문제로서)**: 우주상수 문제 = 진공에너지 이론값이 관측값보다 약 10^120 크다, **미해결
  위기**(Weinberg 1989, Bousso 2012, Burgess 2013). 암흑에너지 ≈ 진공에너지·w≈-1이 보수적 기본.
- **프런티어**: 블랙-화이트홀 바운스·Planck star·화이트홀 잔해(LQG; Rovelli-Vidotto,
  Haggard-Rovelli). **바운스의 유니터리성은 증명 안 됨, 정합 논증만**(Bianchi 외 2018, 미해결
  항 잔존). 화이트홀 잔해 암흑물질은 **Barrau 2021이 강하게 제약**(표준 인플레서 배제).
- **프런티어**: 상호작용 암흑부문(IDE)·동적 암흑에너지(DESI DR2 이후) = 활발하나 비컨센서스.

| 논문 | ref | 플래그 |
| --- | --- | --- |
| Bousso, CC problem/dark energy/landscape | arXiv:1203.0307 | 주류(문제)+사변(landscape) |
| Rovelli-Vidotto, Planck stars | arXiv:1401.6562 | 프런티어 |
| Bianchi 외, White holes as remnants | arXiv:1802.04264 | 프런티어(유니터리 미증명) |
| (교차참조) literature/barrau_2021_white_hole_remnant_constraints.md | arXiv:2101.01949 | 기존 캐시(제약 논문) |
| (교차참조) literature/burgess_2013_naturalness_dark_energy.md | arXiv:1309.4133 | 기존 캐시 |
| (교차참조) literature/figueruelo_2026_desi_dr2_linear_nonlinear_ide.md | - | 기존 캐시(IDE) |
| (교차참조) literature/croker_2024_desi_coupled_black_holes.md | - | 기존 캐시 |
| (교차참조) literature/buchert_2007_dark_energy_from_structure.md | - | 기존 캐시(구조형성) |

**픽션 매핑(경계 절대):** White Hole Equilibrium·화이트홀-블랙홀 정보 순환·DM↔DE 상호작용·
구조형성=정보증가는 **작중 사변**으로만. 실세계에선 (a) 바운스 유니터리성 미증명, (b) 우주상수
"평형"은 미해결 위기이지 풀린 균형 아님, (c) 화이트홀 잔해 DM은 제약됨, (d) IDE의 "z≈1-2 왜"는
열린 질문. 이 넷은 극적 긴장의 정당한 소재이되, **QFUDS 물리 support로 승격 금지**(roadmap·
status 불변). Population III 최초별 → 금속 시딩 → 구조 형성 = 국소 복잡도(정보) 증가는 표준
천체물리이나, "그것이 DM↔DE 상호작용의 원인"은 사용자도 명시한 미검증 후보 가설이다.

---

## PART C. 사용법 규칙

1. 픽션 본문은 위 앵커를 **incluing**(장면·대사·유물로 흘리기)으로만 쓰고 강의하지 않는다.
2. 논쟁 수치는 범위·복수추정으로 제시하고, 인물이 상반된 해석을 갖게 해 정파색을 중화한다.
3. 실사건(Arup 등)·표준(NIST·IFR·IMF)은 단단한 닻, 벤더·전망·프런티어는 그렇게 표시.
4. 물리 substrate는 114·003·White Hole 스레드에서 in-world 사변으로만. QFUDS 연구 status·
   roadmap을 절대 건드리지 않는다.

## Boundary

```text
fiction/provenance only
research evidence: no (QFUDS support 아님)
external source claim: 신뢰 출처 중립 인용, repo 자산 캐시 아님(hit_not_cached)
```

이 대장은 근미래 프렐류드(story_design 322)와 in-world 물리(320)의 핍진성 닻이다. 실제 예측·
투자·정치 주장이 아니며, 물리 substrate는 작중 사변으로만 쓰고 QFUDS 물리 증거로 승격하지
않는다. 이미 literature/에 있는 논문은 교차참조로 갈음한다.
