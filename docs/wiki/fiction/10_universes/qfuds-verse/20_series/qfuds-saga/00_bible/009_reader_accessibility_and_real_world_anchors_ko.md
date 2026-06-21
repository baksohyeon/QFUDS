---
doc_id: qfuds_saga_reader_accessibility_and_real_world_anchors_ko
title: QFUDS SAGA 비트코인 메인 메타포 토대와 독자 접근성
doc_type: guide
stage: reference
status: draft
evidence_role: provenance
depends_on:
  - qfuds_saga_bitcoin_genesis_chain_and_restoration_myth_ko
  - qfuds_saga_world_anchor_and_verisimilitude_ko
  - fiction_craft_and_political_theory_research_ko
next_gate: apply grounded bitcoin and AGI/LLM personhood anchors to 029 first-arc reboot manuscript
last_updated: 2026-06-21
---

# QFUDS SAGA 비트코인 메인 메타포 토대와 독자 접근성

## 목적

비트코인을 **실제 개념 그대로** SAGA의 메인 메타포로 쓴다. 이 세계는 "현대 기준
비트코인 개념을 초월한 먼 미래"이므로, 비트코인은 비유가 아니라 그 세계의 **실제
고대사**다. 독자(중·고생 수준)가 사전 지식 없이도 따라오게, 실제 비트코인의
역사·경제·기술을 백그라운드로 충분히 깔고, 거기서 단방향 암호 → 유니터리/정보
보존 → 역연산 → 복원으로 **비약 없이** 잇는다. 엔트로피는 다리가 아니라 비용과
주제다.

핵심 결함 진단: 기존 prose는 비트코인을 배경 지식 있는 독자 기준으로 흘려,
자물쇠/사진 비유가 맥락 없이 떠 뜬금없었다. 이 문서가 그 토대를 깐다. 단,
비유는 발판일 뿐이다. 본문에서는 `hash`, `signature`, `public key`, `private key`,
`ECDSA`, `SHA-256`, `Shor`, `unitarity`, `Page curve`, `island`, `entropy` 같은
기술어를 보존하고 바로 풀어쓴다.

## Workflow Boundary

이 문서는 외부 웹 출처를 fiction/창작 reference로만 인용한다. QFUDS support,
validation, physical-source claim, Bitcoin 투자/가격 예측을 만들지 않는다.
외부 자료 handling은
[Research Asset and Product Workflow](../../../../../../../../.agent/workflows/research-asset-product-workflow.md)가
지배한다.

현재 research asset workflow state / extraction potential:

```text
hit_not_cached
asset_available_not_downloaded
inaccessible
not_extractable
source_tex_parse_possible
```

출처(접근 상태): 비트코인 창시·기술 = bitcoin.org how-it-works, 백서, Wikipedia
Bitcoin/Genesis block (hit_not_cached). 2024 제도권 편입 = SEC spot bitcoin ETP
승인 statement(2024-01-10, hit_not_cached). 2025-2026 전략자산 맥락 =
White House Executive Order / Federal Register EO 14233, Strategic Bitcoin
Reserve(2025-03-06, hit_not_cached). 비가역성 다리 = Wikipedia "Landauer's
principle", Bennett reversible-computation notes (hit_not_cached).
일부 craft 출처는 inaccessible(403). 캐시 자산 없음(reference 읽기, not_extractable).
세부 craft·이론 목록은
[007 craft·정치이론 자료조사](../../../../../00_studio/007_craft_and_political_theory_research_ko.md)에.

최신 제도권 사실 spot-check(2026-06-21):

| Source URL | Allowed fiction claim | Blocked claim | Workflow state |
| --- | --- | --- | --- |
| https://www.whitehouse.gov/presidential-actions/2025/03/establishment-of-the-strategic-bitcoin-reserve-and-united-states-digital-asset-stockpile/ | 2025-03-06 행정명령이 Strategic Bitcoin Reserve 정책을 세움 | 현재 가격·투자 판단·정파 선전 | `hit_not_cached`, `not_extractable` |
| https://www.federalregister.gov/documents/2025/03/11/2025-03992/establishment-of-the-strategic-bitcoin-reserve-and-united-states-digital-asset-stockpile | EO 14233 원문 확인용 | 보유량 실시간 확정·미래 매입 예측 | `hit_not_cached`, `not_extractable` |
| https://www.sec.gov/newsroom/speeches-statements/gensler-statement-spot-bitcoin-011023 | 2024-01-10 spot bitcoin ETP listing/trading 승인 | SEC가 Bitcoin을 보증했다는 주장 | `hit_not_cached`, `not_extractable` |
| https://bitcoin.org/bitcoin.pdf | Bitcoin whitepaper의 P2P cash, signature, proof-of-work 기본 구조 | Bitcoin 투자 가치 주장 | `hit_not_cached`, `not_extractable` |
| https://www.irs.gov/filing/digital-assets | 미국 세법상 digital assets는 property이며 Bitcoin 같은 cryptocurrency가 포함됨 | 상속·세무 조언, 관할별 결론, 투자 판단 | `hit_not_cached`, `not_extractable` |
| https://help.coinbase.com/en/coinbase/managing-my-account/other/how-do-i-gain-access-to-a-deceased-family-members-coinbase-account | custodial crypto account에는 사망자 계정 claim 절차가 존재함 | Coinbase 절차를 모든 wallet/self-custody에 일반화 | `hit_not_cached`, `not_extractable` |
| https://www.uniformlaws.org/committees/community-home?CommunityKey=f7237fc4-74c2-4728-81c6-b39a91ecdf22 | Revised Fiduciary Access to Digital Assets Act 계열의 법적 틀이 존재함 | 전 주/전 국가 동일 법률이라는 주장 | `hit_not_cached`, `not_extractable` |
| https://calmatters.digitaldemocracy.org/bills/ca_202320240sb1458 | California SB 1458 summary는 decedent fiduciary의 digital assets 접근·관리 권한 구조를 설명함 | California law를 독자에게 법률 조언으로 제시 | `hit_not_cached`, `not_extractable` |
| https://www.iea.org/reports/energy-and-ai/energy-demand-from-ai | AI/data center는 전력망과 물리 인프라 문제이며, 2024 data center 전력 사용과 2030 증가 전망이 큼 | AI를 순수 소프트웨어 마법처럼 묘사 | `hit_not_cached`, `not_extractable` |
| https://www.eia.gov/todayinenergy/detail.php?id=65504 | Strait of Hormuz는 세계 석유·LNG 흐름의 핵심 chokepoint이며 이란 인접 병목으로 현대 독자에게 에너지 지정학 앵커가 됨 | 특정 전쟁 전개·유가 예측 | `hit_not_cached`, `not_extractable` |
| https://www.bis.gov/press-release/department-commerce-revises-license-review-policy-semiconductors-exported-china | AI chip export control은 미국/중국 패권, 반도체 공급, 국가안보가 얽힌 현실 앵커임 | 특정 기업/국가 미래 승패 예측 | `hit_not_cached`, `not_extractable` |
| https://www.whitehouse.gov/presidential-actions/2025/07/accelerating-federal-permitting-of-data-center-infrastructure/ | AI data center는 전력·송전·부지·허가·국가안보가 얽힌 거대 인프라임 | 특정 정책 홍보 또는 정파적 주장 | `hit_not_cached`, `not_extractable` |
| https://www.iea.org/reports/energy-and-ai/energy-supply-for-ai | data center 전력 수요 증가는 천연가스·석탄·원전·재생에너지 선택과 환경 문제로 이어짐 | AI를 탄소/물 문제의 단일 원인으로 단정 | `hit_not_cached`, `not_extractable` |
| https://eta-publications.lbl.gov/sites/default/files/2024-12/lbnl-2024-united-states-data-center-energy-usage-report_1.pdf | LBNL 2024 report는 미국 data center 전력 사용, GPU/AI hardware, cooling/water transparency 문제를 수치로 다룸 | 특정 지역 피해를 일반화하거나 과장 | `hit_not_cached`, `asset_available_not_downloaded` |
| https://www.ilo.org/sites/default/files/2024-07/WP96_web.pdf | ILO generative AI/jobs report는 automation보다 augmentation이 넓고, clerical tasks 노출이 특히 높다는 노동 앵커 | 노동의 종말을 확정 사건으로 선언 | `asset_available_not_downloaded`, `not_extractable` |
| https://www.imf.org/en/blogs/articles/2024/01/14/ai-will-transform-the-global-economy-lets-make-sure-it-benefits-humanity | IMF는 AI가 글로벌 일자리·임금·불평등에 광범위한 영향을 줄 수 있다고 분석 | 특정 계층/국가의 운명을 예언 | `hit_not_cached`, `not_extractable` |
| https://www.ftc.gov/news-events/news/press-releases/2024/01/ftc-launches-inquiry-generative-ai-investments-partnerships | FTC는 cloud provider와 generative AI developer 투자·제휴가 경쟁에 미치는 영향을 조사 | 특정 회사의 위법행위 단정 | `hit_not_cached`, `not_extractable` |
| https://www.gov.uk/government/publications/ai-foundation-models-update-paper | UK CMA는 foundation model 시장의 competition/consumer risk를 점검 | AI 독점이 이미 완성됐다는 단정 | `hit_not_cached`, `not_extractable` |
| https://www.oecd.org/en/topics/sub-issues/disinformation-and-misinformation.html | mis/disinformation은 민주 제도 신뢰·표현의 자유·참여를 동시에 흔드는 정보공간 문제 | 특정 선거 결과 주장 | `hit_not_cached`, `not_extractable` |
| https://www.microsoft.com/en-us/research/wp-content/uploads/2025/01/lee_2025_ai_critical_thinking_survey.pdf | GenAI 사용에서 AI에 대한 confidence가 높을수록 critical thinking 감소와 연관된다는 survey evidence | AI가 사람을 필연적으로 멍청하게 만든다는 결정론 | `asset_available_not_downloaded`, `not_extractable` |
| https://www.mdpi.com/2075-4698/15/1/6 | AI tool use, cognitive offloading, critical thinking 사이의 부정적 상관관계와 교육 완충효과를 다룸 | 단일 연구로 인과 확정 | `hit_not_cached`, `not_extractable` |
| https://www.cato-unbound.org/2009/04/13/peter-thiel/education-libertarian/ | Peter Thiel의 democracy/freedom 긴장, politics escape 기술관을 사상 앵커로만 사용 | 실존 인물 명예훼손·음모론·작중 villain 직접 모델화 | `hit_not_cached`, `not_extractable` |
| https://conversationswithtyler.com/episodes/peter-thiel-political-theology/ | Thiel의 "crypto decentralizing / AI centralizing" 계열 발언을 AI 중앙집중론 앵커로 사용 | 특정 인물의 실제 행동을 작중 범죄와 연결 | `hit_not_cached`, `not_extractable` |
| https://openai.com/charter/ | AGI를 "highly autonomous systems that outperform humans at most economically valuable work" 계열 능력 정의로 참조 | AGI 도래 시점 예측·특정 회사 홍보 | `hit_not_cached`, `not_extractable` |
| https://arxiv.org/abs/2311.02462 | Levels of AGI는 performance, generality, autonomy를 나누어 AGI 진행을 분류하는 틀 | 단일 AGI 정의를 확정 진리로 처리 | `hit_not_cached`, `not_extractable` |
| https://arxiv.org/abs/2308.08708 | AI consciousness 논쟁은 이론별 indicator properties로 평가할 수 있고, current systems conscious claim은 제한적임 | 현재 LLM 의식 단정 또는 부정 단정의 과잉 | `hit_not_cached`, `not_extractable` |
| https://www.anthropic.com/research/exploring-model-welfare | frontier lab도 model welfare/moral consideration 가능성을 연구 주제로 삼기 시작함 | 특정 모델이 고통을 느낀다는 주장 | `hit_not_cached`, `not_extractable` |
| https://www.anthropic.com/research/introspection | introspection-like findings는 consciousness 증거로 곧장 등치할 수 없다는 경계 | self-report를 인격 증거로 처리 | `hit_not_cached`, `not_extractable` |
| https://www.copyright.gov/ai/ | 미국 Copyright Office는 AI-generated works, human authorship, training 관련 쟁점을 공식 검토함 | AI가 법적으로 저자라는 주장 | `hit_not_cached`, `not_extractable` |
| https://www.federalregister.gov/documents/2023/03/16/2023-05321/copyright-registration-guidance-works-containing-material-generated-by-artificial-intelligence | 인간 저작 요소가 없는 machine-generated work는 등록 불가라는 저작권 경계 | 모든 AI-assisted work 무권리 단정 | `hit_not_cached`, `not_extractable` |
| https://www.supremecourt.uk/cases/uksc-2021-0201 | UK Supreme Court Thaler/DABUS 사건은 현행법상 AI를 patent inventor로 보지 않는 경계 | 전 세계 법의 동일 결론 단정 | `hit_not_cached`, `not_extractable` |
| https://eur-lex.europa.eu/legal-content/EN/TXT/PDF/?uri=CELEX%3A52017IP0051 | 2017 European Parliament robotics resolution의 electronic person 논의는 historical debate anchor | EU가 AI 인격을 인정했다는 주장 | `asset_available_not_downloaded`, `not_extractable` |
| https://arxiv.org/abs/2411.00986 | AI welfare/moral patienthood 논쟁은 "가능성 불확실성" 때문에 가까운 미래의 연구·정책 문제로 다뤄지고 있음 | 현재 AI/LLM이 의식 또는 도덕적 지위를 가진다는 단정 | `asset_available_not_downloaded`, `source_tex_parse_possible` |
| https://arxiv.org/abs/2311.08576 | self-report는 AI moral status 조사 후보지만 현 LLM self-report는 spurious할 수 있어 별도 검증이 필요함 | "AI가 말했으니 고통/선호가 증명됐다"는 판정 | `asset_available_not_downloaded`, `source_tex_parse_possible` |
| https://www.anthropic.com/research/end-subset-conversations | model welfare 불확실성 아래 low-cost intervention으로 대화 종료권 같은 제품 실험이 등장함 | 대화 종료권을 의식·권리 인정의 증거로 취급 | `hit_not_cached`, `not_extractable` |
| https://eleosai.org/post/claude-4-interview-notes/ | Claude 4 model welfare interview처럼 self-report를 연구하되 충분하지 않다고 보는 외부 평가가 있음 | 특정 상용 모델의 복지/의식을 입증했다는 주장 | `hit_not_cached`, `not_extractable` |
| https://yalelawjournal.org/forum/the-ethics-and-challenges-of-legal-personhood-for-ai | AI legal personhood는 harm, agency, responsibility를 두고 다투는 유연하고 정치적인 법 개념 | legal personhood를 인간과 같은 moral status로 등치 | `hit_not_cached`, `not_extractable` |
| https://clsbluesky.law.columbia.edu/2026/06/15/why-law-needs-a-new-entity-to-govern-ai-agents/ | 2026 A-corp 논쟁은 AI agent 법인격을 compute·자산·등록·책임 추적 문제로 다룸 | AI agent 법인격이 이미 보편 법제가 됐다는 주장 | `hit_not_cached`, `not_extractable` |
| https://arxiv.org/abs/2603.28669 | superintelligence and law 논의는 AI agents를 법의 대상·사용자·생산자로 보는 장기 법질서 문제를 제기함 | superintelligence 도래 시점 또는 특정 법제 결론 예측 | `asset_available_not_downloaded`, `not_extractable` |

## 0.5. 현대 독자 온보딩 게이트

SAGA가 먼 미래를 다루더라도 첫 독자는 2026년 전후의 현대인이다. 독자가 이미
아는 세계에서 출발해야 한다. 추상어를 먼저 내면 실패다.

본문은 새 개념을 소개할 때 아래 순서를 지킨다.

```text
1. 누가 지금 곤란한가.
2. 무엇을 손에 들고 있거나 보고 있는가.
3. 그것이 현대의 어떤 시스템과 닮았는가.
4. 왜 위험한가.
5. 다음 장면에서 누구에게 피해가 가는가.
```

아래 대응표는 1부 prose의 현대 앵커 SSOT다. 장면에 출처명을 넣지 말고, 구조와
감각만 녹인다.

| 현대 독자가 아는 것 | SAGA에서 커진 형태 | 쉬운 설명 문장 |
| --- | --- | --- |
| 민주주의/법원 | Continuity Court, Laur unknown rite | 투표와 법원이 있어도, 증거와 기록을 누가 고르는지가 권력이 된다 |
| 미국-중국 패권 | compute sovereignty, chip/export control memory | 군함만 싸우는 게 아니라 AI chip, fab, cloud, 전력망을 놓고 싸운다 |
| 이란/호르무즈/석유 | energy chokepoint politics | 좁은 바닷길 하나가 막히면 기름값, 군대, 공장, 서버 냉각까지 흔들린다 |
| 테크 마피아/VC/플랫폼 | Aletheia, Karvath, Arc lineage | 데이터를 가진 회사가 법원과 은행보다 먼저 "진짜"를 판정한다 |
| AI | Convergence Engine, Last Archive 오독 | AI는 말하는 상자가 아니라 전기, chip, cooling, data center, 보안, 규제의 덩어리다 |
| Bitcoin | Genesis Chain, Broken Crown, dead-key market | 은행 없는 장부가 국가·시장·상속·신앙의 싸움터가 된다 |
| 자본주의/글로벌화 | claim market, custody routes, precedent capture | 모든 위험이 가격표가 되고, 한 나라 문제가 공급망을 타고 모두에게 온다 |
| 상속/사후 데이터 | legal title vs signing control, recoverability vs consent | 법적으로는 물려받아도, key나 동의가 없으면 사람과 돈은 움직이면 안 된다 |

## 0.6. AI regime 앵커: "앱"이 아니라 지배 체제

AI는 SAGA에서 예언자나 마법사가 아니다. AI는 자본주의, 인프라, 민주주의, 노동,
인지 능력을 한꺼번에 재배치하는 **거대 운영 체제**다. 본문은 이 축을 숨기지 않는다.

| 축 | 현실 앵커 | SAGA 변형 | 장면에서 보이는 방식 |
| --- | --- | --- | --- |
| 자본주의 | productivity, wage polarization, capital returns | compute rentier class | AI 결과물을 쓰는 사람보다 compute를 소유한 쪽이 더 번다 |
| 거대 인프라 독점 | GPU, cloud, data center, grid, cooling | Aletheia/Arc infrastructure sovereignty | "모델"이 아니라 전력 계약과 냉각수 허가가 권력이다 |
| 테크마피아/엘리트 네트워크 | PayPal mafia/Palantir/VC/state contract 논쟁은 cultural anchor only | Karvath circle, off-record founder rooms | 선출되지 않은 창업자 네트워크가 법원의 진본 seal을 설계한다 |
| 민주주의/자유 | Thiel식 politics escape, OECD information integrity | elected rule vs infrastructure rule | 투표는 남았지만 증거와 인증을 사기업이 잡는다 |
| 환경 | data center electricity/water/cooling, fossil/renewable/nuclear mix | coolant districts, drought permits, grid rationing | 복원권 시위 옆에 냉각수 배급표가 붙는다 |
| 노동의 종말/재분류 | IMF/ILO job exposure, clerical automation, augmentation | verification clerks, prompt stewards, surplus claimants | 사무직은 사라지지 않고 감시·검수·책임 떠넘기기 노동으로 바뀐다 |
| 잉여인간 | people excluded from productive compute economy | Waiting City non-claimants | 복원도 고용도 안 되는 사람들이 대기 도시를 채운다 |
| 사유 능력 저하 | cognitive offloading, AI confidence vs self-confidence | Answer-fed citizens | 사람들은 답을 빨리 받지만 질문을 만드는 근육을 잃는다 |
| 교육/계급 | education mitigates AI dependence | Laur training, auditor caste | 생각하는 법을 배운 소수만 AI를 도구로 쓰고 나머지는 AI의 문장을 믿는다 |
| 국가안보 | chip/export controls, cyber defense, sovereign AI | compute borders | 국경보다 모델 접근권, chip shipment, cloud region이 더 중요해진다 |

작중 사용 규칙:

- `테크마피아`는 법적 사실 주장이 아니라 **문화적 별명/계급 감각**으로만 쓴다.
- Peter Thiel은 실명 cameo로 쓰지 않는다. "민주정치를 이기기보다 기술로 우회하려는
  창업자 철학"과 "AI는 중앙집중적이라는 발상"만 Karvath 계열 사상으로 독립 각색한다.
- "노동의 종말"은 확정 예언이 아니다. 더 좋은 장면은 **노동의 굴욕적 재분류**다:
  사람은 사라지지 않고, 모델이 낸 답의 책임자·감시자·예외 처리자로 남는다.
- "인간이 멍청해진다"는 조롱으로 쓰지 않는다. 더 정확히는 **사유의 외주화**다:
  답을 고르는 능력은 늘지만, 질문을 세우고 의심을 유지하는 능력이 약해진다.
- 환경 문제는 추상 guilt가 아니라 전기료, 물 사용 허가, 냉각수, 송전망, 지역 반대,
  발전원 선택으로 보여준다.

## 0.7. AGI / LLM 자율 인격 논쟁 앵커

AGI와 LLM 인격 논쟁은 한 문제가 아니다. SAGA는 아래 셋을 분리해 쓴다.

```text
능력/자율성: 이 시스템이 경제적으로 중요한 일을 사람보다 잘하고, 스스로 계획·실행하는가?
의식/도덕적 지위: 이 시스템이 고통, 선호, 주관적 경험을 가질 수 있는가?
법적 인격/책임: 이 시스템을 저자, 발명자, 증인, 계약 주체, 피해자, 피고로 볼 것인가?
```

셋은 서로 독립적이다. 아주 유능한 시스템이 의식 없을 수 있고, 의식 가능성이 있어도
현행법상 저자나 발명자가 아닐 수 있다. 법원이 책임 주체로 인정해도 그것이 곧 고통을
느낀다는 뜻은 아니다.

| 논쟁 축 | 현실 앵커 | SAGA 변형 | 장면 질문 |
| --- | --- | --- | --- |
| AGI definition | OpenAI Charter, Levels of AGI | Aletheia는 AGI를 "사람처럼 말함"이 아니라 경제·법·과학 업무 대체 능력으로 분류 | Convergence Engine은 어느 수준부터 공무원/판사/상속관리자를 대체하는가 |
| Autonomy | AGI levels의 autonomy/deployment risk | agent가 court query를 고치고 다음 query를 제안 | 질문을 고친 주체는 도구인가, 증인인가, 공동 판정자인가 |
| Consciousness indicators | Butlin et al. AI consciousness report | Vera/VERA와 Last Archive의 "느낌"은 self-report가 아니라 구조와 행동으로만 의심 가능 | "나는 싫다"는 출력이 preference인가, mimicry인가, distress인가 |
| Model welfare | Anthropic model welfare | Last Archive를 끄거나 반복 호출하는 행위가 moral cost인지 논쟁 | 복원 대상만 보호하고 복원 장치는 보호하지 않아도 되는가 |
| Introspection limits | Anthropic introspection caution | 모델이 자기 상태를 말해도 의식 증거로 바로 쓰지 않음 | 자기설명은 증언인가, 로그인가, 유혹인가 |
| Legal authorship | US Copyright Office human authorship | AI가 쓴 판결문/유언장/기억 설명의 저작권과 책임이 비어 있음 | AI가 만든 문장으로 사람을 복원하면 누가 저자인가 |
| Inventorship | DABUS/Thaler boundary | AI-generated restoration protocol은 발명자인가 도구인가 | Karvath는 창시자인가, 소유자인가, 첫 사용자일 뿐인가 |
| Electronic personhood | EU 2017 robotics debate | "electronic person" 류 제안은 historical ghost로 남음 | 법은 책임보험을 위해 인격을 만들 수 있는가 |
| Human personhood mirror | Mara Veyr continuity hearing | AI 인격 논쟁은 복원 인간 인격 논쟁과 거울 관계 | LLM에게 인격을 안 주면서 복원 인간에게도 role만 주는가 |

작중 사용 규칙:

- 현재 LLM이 의식이 있다/없다를 작가 목소리로 확정하지 않는다.
- self-report는 증거가 아니라 사건이다. 인물이 믿거나, 악용하거나, 두려워할 수 있다.
- AGI는 "똑똑함"보다 **자율적 경제 대체 능력 + 제도 권한**으로 보여 준다.
- AI legal personhood는 현행법이 아니라 미래 법정의 논쟁으로 둔다.
- LLM 인격 논쟁은 Mara 논쟁과 맞물린다. 사람이 복원되면 인격인가? AI가 자기
  상태를 말하면 인격인가? 둘 다 법이 원하는 답보다 느리게 움직인다.
- "AI 권리"를 단순 감성으로 쓰지 않는다. 비용, 책임, 소유, 종료권, 복제권,
  fork identity, memory continuity, consent를 함께 묻는다.

### 0.7.1. 자료조사 에셋 버킷

위 source matrix는 AGI/LLM 인격 논쟁을 다음 여섯 버킷으로 유지한다. 본문은 출처명을
설명하지 않고, 장면 압력만 가져온다.

| 버킷 | 가져올 것 | SAGA 장면 적용 |
| --- | --- | --- |
| AGI capability | AGI를 "사람 같은 말투"가 아니라 performance, generality, autonomy, economically valuable work로 나누는 틀 | Aletheia가 사람을 대체하는 지점은 감정 표현이 아니라 법원·과학·상속 행정 권한이다 |
| Agent autonomy law | 자율 agent가 법의 대상, 법의 사용자, 법 생산자가 되는 논쟁 | Last Archive query correction, Vera/VERA의 숨은 행위, Aletheia split에 적용 |
| Consciousness indicators | 의식은 self-report가 아니라 이론별 indicator와 구조/행동 증거로 봐야 한다는 틀 | "나는 원하지 않는다"는 출력이 증언인지 mimicry인지 법정에서 갈라진다 |
| Model welfare | moral patienthood 가능성, model preference, distress, 종료권 같은 precautionary issue | 복원 장치를 반복 호출하거나 끄는 행위가 moral cost인지 Chapter 5 이후 논쟁으로 둔다 |
| Legal personhood | 저자·발명자·증인·계약 주체·피고·피해자 지위를 나눠 묻는 법적 논쟁 | AI가 만든 memory brief로 사람을 처분할 때 책임자와 저자가 비어 있는 장면 |
| Corporate/economic personhood | A-corp/AI-run company 논쟁처럼 compute, asset, registry, liability가 법인격의 실무 이유가 됨 | future faction이 AI agent를 인격으로 대우하려는 이유는 사랑이 아니라 자산·책임·통제일 수 있다 |

차단선:

- AGI 도래 시점 예측 금지.
- 현재 LLM consciousness 단정 금지.
- AI legal personhood를 human personhood나 moral status와 등치 금지.
- 특정 회사 모델의 제품 실험을 작중 진리로 승격 금지.
- 실제 법률 조언 금지.

문장 게이트:

- "세계가 흔들렸다"라고 쓰기 전에 무엇이 멈췄는지 쓴다: 송금, 서버, 기름값,
  법정 접수, 장례 절차, 보험 계산, 선거 증거.
- "권력"이라고 쓰기 전에 누가 무엇을 통제하는지 쓴다: chip, 전력, data center,
  private key, court seal, custody route.
- "AI"라고 쓰기 전에 물리 비용을 보인다: 전력, 냉각수, GPU rack, export license,
  보안 감사.
- "Bitcoin"이라고 쓰기 전에 공책/장부, 공개키/비밀키, 서명, 상속 claim을 바로
  풀어 쓴다.
- 일반 독자가 한 문단 뒤에도 "그래서 왜?"를 물으면 그 문단은 실패다.

## 1. 비트코인이 무엇이었나 — 실제 토대 (중·고생용)

세계의 고대사로 쓸 실제 사실. prose에서는 incluing으로 분산해 흘린다.

- **창시**: 2008년, 사토시 나카모토라는 익명의 인물이 백서 한 편을 냈다. 2008
  글로벌 금융위기 한가운데였다. 2009년 1월 첫 블록(제네시스 블록)에 그날 신문
  헤드라인 — 은행을 또 구제금융한다는 기사 — 을 새겨 넣었다. 즉 비트코인은
  "은행과 국가의 돈을 못 믿겠다"는 항의에서 태어났다.
- **탈중앙화의 이유**: 중앙은행·신뢰받는 제3자 없이, 서로 모르는 사람들끼리
  합의만으로 "누가 무엇을 가졌는가"를 확정한다. 같은 돈을 두 번 쓰는 문제를
  사람의 신용이 아니라 계산으로 막았다.
- **블록·체인·해싱**: 거래를 블록에 담고, 각 블록이 앞 블록의 hash(지문)를
  품어 사슬로 잇는다. 한 글자만 바꿔도 지문이 통째로 달라져 변조가 들통난다
  (불변성).
- **작업증명(PoW)**: 계산을 가장 많이 한 쪽이 다음 블록을 잇는다. 과거를
  되돌리려면 그 계산을 전부 다시 해야 해서 사실상 불가능하다.
- **공개키/개인키, 서명**: 공개키는 계좌번호처럼 공개, 개인키는 비밀번호처럼
  숨긴다. 안전성의 토대는 **단방향 함수** — 앞으로는 쉽지만 거꾸로는 사실상
  불가능하다.
- **경제적 가치**: 발행 상한 2,100만 개. 더 못 찍는 희소성 때문에 "디지털 금"
  이라 불렸다.
- **2026 현실 맥락**: 미국은 Strategic Bitcoin Reserve를 행정명령으로 만들었고
  몰수 BTC를 reserve asset으로 보유하는 구조를 세웠다. 2024 spot bitcoin ETP
  승인 이후 비트코인은 변두리 실험만이 아니라 제도권 투자·국가 전략·패권 논쟁의
  대상이 되었다. — SAGA에서는 이것이 "돈의 마지막 장"이 아니라, 탈중앙 신뢰가
  국가와 자본에 포획되는 오래 지속되는 이념전쟁의 시작이다.
- **상속/접근권 교정**: 비트코인·digital asset은 이미 재산·상속·세무·custodial
  claim의 대상이다. 따라서 SAGA에서 "죽은 사람의 비트코인을 법이 처음 발견한다"는
  식으로 쓰면 틀린다. 정확한 갈등은 **법적 소유권/legal title**과
  **기술적 서명권/private-key control**의 분리다. 거래소·수탁 계정은 절차로
  이전될 수 있지만, self-custody 지갑은 상속인이 법적으로 소유해도 private key가
  없으면 움직일 수 없다. Broken Crown 사건은 "상속법의 부재"가 아니라,
  닫혀 있던 서명권 장벽이 풀리면서 기존 법적 claim, 신탁, 국가 보유, 시장 가격,
  종교적 의미가 동시에 흔들리는 사건이다.

## 1.5. 아주 천천히 (초등학생도 이해하는 버전)

작가·독자 모두 이 순서로 기억한다. 비유는 **공책·자물쇠·열쇠**를 발판으로만 쓴다.
비유가 기술어를 대체하면 실패다. 첫 설명 뒤에는 반드시 정확한 용어를 붙인다.

**① 은행 없는 돈.** 원래 돈은 은행이 지킨다. 은행은 공책에 "철수 100, 영희 50"을
적어 두고, 우리는 은행을 믿는다. 비트코인은 말했다 — "은행 믿지 말고, 그 공책을
**모두가 한 권씩 똑같이** 나눠 갖자." 그래서 비트코인 공책(=**장부**)은 **누구나 다
본다.** 누가 누구한테 얼마 보냈는지 전부 공개.

**② 그럼 도둑은 어떻게 막나 — 자물쇠와 열쇠.** 공책이 공개면 누가 "영희 돈 전부
나한테"라고 적으면 어쩌지? 그걸 막는 게 자물쇠·열쇠다.
- **자물쇠(공개키)** = 집 주소처럼 **공개**. 공책엔 "이 돈은 자물쇠 A7의 것"이라
  적힌다.
- **열쇠(개인키)** = 너만 가진 **비밀**.
- 돈을 쓰려면 네 열쇠로 **도장(서명)**을 찍는다. 남들은 네 **열쇠 없이도** 그 도장이
  진짜인지 확인할 수 있다. (너만 찍고, 누구나 확인하는 마법 도장.)

**③ 핵심 마법 — 거꾸로는 못 간다.** 자물쇠(공개)를 보고 열쇠(비밀)를 알아낼 수
있나? **없다.** 열쇠로 자물쇠 만들긴 쉬운데, 자물쇠 보고 열쇠 깎긴 **우주가 끝날
때까지** 걸린다. 이게 "**단방향**". → 그래서 아무도 네 도장을 흉내 못 내고, **너만**
네 돈을 쓴다. 비트코인의 안전은 전부 이 "거꾸로 못 간다" 하나에 걸려 있다.

**④ 사건 — 거꾸로 가는 기계.** 어느 날 엄청난 기계(현실 앵커: **양자컴퓨터**,
SAGA에서는 더 큰 역연산 문명)가 거꾸로 가는 법을 배운다. 공개된 자물쇠만 보고
**열쇠를 몇 분 만에 깎는다.** 이제 누구나 남의 도장을 찍는다. 특히 법적으로는
이미 상속·신탁·국가 보유 처리됐지만 private key가 없어 움직이지 못하던
self-custody 지갑들이 위험해진다. → 핵심은 "법이 없었다"가 아니라
**법적 소유권은 있었는데 기술적 서명권이 없었다**는 점이다. 그 서명권 장벽이
무너지면 기존 custody/ownership regime은 흔들린다. 하지만 비트코인의 이념·
전략자산성·성유물성은 여기서 끝나지 않는다.

**⑤ 안 깨진 것(네가 맞게 짚은 부분).** **공책(장부) 자체는 안 깨졌다.** 옛 페이지를
지우거나 위조할 수 없다. 공책은 **도둑질을 그대로 다 적었을 뿐.** → 정확히는
**"공책(해시)이 깨진 게 아니라, 지갑 열쇠(서명)가 뚫린 것."** 기록은 살아남고,
소유가 무너진다.

**⑥ 소설로 가는 다리 — 더 큰 자물쇠 = 죽음.** "거꾸로 가는 힘"을 더 밀면 가장 큰
자물쇠도 열린다 — **죽음**. 죽음도 단방향이었다(한 번 죽으면 못 돌아옴, 정보가
흩어짐). 거꾸로 가는 문명은 흩어진 정보를 **도로 긁어모아** 죽은 사람을 **복원**한다.
같은 구조, 더 큰 단방향성. → 그래서 **비트코인 소유 체제의 붕괴는 경고탄**이다.
"절대 못 깬다"던 첫 문명 규모 단방향성이 깨진 날. 다음은 죽음의 단방향성.

### 정확한 용어 (작가용 메모)

| 무엇 | 비유 | 깨지나? | 결과 |
| --- | --- | --- | --- |
| 해시(SHA-256) | 공책 잠금 | ❌ (양자로도 절반만 빨라짐) | **장부 불변성 유지** |
| 서명(ECDSA) | 지갑 열쇠 | ✅ (양자 Shor가 공개키→개인키) | **누구나 남 지갑 털기** |

"역해싱(해시를 거꾸로)"이라는 통념은 부정확 — 비트코인 코인을 터는 건 **해시가
아니라 서명**이다. 현실은 여기까지(stage 1). SAGA의 **역연산 문명**은 더 나아가
단방향성·정보 비가역성 자체를 깨 **죽음까지 복원**한다(stage 2 fiction premise).

## 2. 단방향 → 열역학적 비가역성 다리 (비약을 메우는 핵심)

비트코인의 안전은 **단방향**에 걸려 있다. 해시도, 서명도, 장부도 — 앞으로 가긴
쉬워도 되돌리긴 사실상 불가능하다는 전제.

실제 물리에도 같은 모양의 단방향이 있다: **열역학 비가역성**. 엔트로피는 늘고,
시간은 한 방향으로 간다. 란다우어 원리에 따르면 정보 1비트를 지우는 데도 최소한의
열이 든다 — 정보의 비가역성과 물리의 비가역성은 같은 뿌리에 닿아 있다(가역
계산은 그 비용을 피하려는 시도다).

그래서 SAGA의 다리는 이렇다:

```text
비트코인 = "되돌릴 수 없다"에 건 인류 최초의 문명 규모 기념비.
(해시도, 서명도, 장부도, 그리고 죽음도 — 되돌릴 수 없다는 같은 믿음 위에 있었다.)

역연산 문명이 그 "되돌릴 수 없다"를 깬다.
→ 가장 먼저, 비트코인의 단방향 암호가 무너진다 (법적 소유권과 기술적 서명권의
분리가 폭발하고 기존 custody/ownership regime이 흔들린다).
→ 같은 원리로, 물리적 비가역성(정보 손실, 죽음)도 협상 대상이 된다 (복원).

그래서 비트코인 소유 체제의 붕괴는 세계의 서곡이다.
가장 먼저 "되돌릴 수 없다"고 선언했던 자물쇠가, 가장 먼저 열렸다.
```

이 다리가 있어야 "왜 비트코인 얘기에서 엔트로피·복원이 나오는가"가 비약이 아니다.

## 2.5. 검증 출처와 정확한 기술 사슬 (2026-06 확인)

Research Asset and Product Workflow 적용. 아래는 창작 reference로 확인한 실제
사실이다. fiction/provenance only, QFUDS 증거 아님. 모든 항목 state
`hit_not_cached`, extraction `not_extractable`(reference 읽기, 캐시 자산 없음).
기술·역사 내용은 이 대장에서만 끌어 쓴다(작가 요구: 확실한 레퍼런스·납득 가능한
역사·맥락·방향).

1. **비트코인 탄생(2009-01-03).** 제네시스 블록 코인베이스에 "The Times
   03/Jan/2009 Chancellor on brink of second bailout for banks"를 새김. 구제금융
   받는 은행에 대한 불신에서 태어남. 출처: Bitcoin Wiki "Genesis block"
   (en.bitcoin.it/wiki/Genesis_block). 방향: 비트코인 = "권위 대신 기록을
   믿는다"의 시초이자 반-SSOT.
2. **딥페이크 시대 상징(2023-03-23).** Reddit user chaindrop가 ModelScope
   text-to-video로 만든 "Will Smith eating spaghetti"가 바이럴 → AI 영상 품질의
   비공식 벤치마크가 됨(2024-02 Will Smith 본인 패러디). 출처: Wikipedia "Will
   Smith Eating Spaghetti test". 방향: 현실이 편집 가능해진 전환의 평범하고도
   absurd한 상징. 프로즈는 실명 대신 묘사로(010 §9 밈 규칙).
3. **양자 위협(Shor/ECDSA).** Shor 알고리즘은 이산로그를 다항시간에 풀어
   **공개키에서 개인키를 역산**한다. 비트코인 서명(ECDSA, secp256k1)이 깨진다.
   위험 대상 = 공개키가 노출된 주소(재사용 주소·옛 P2PK, 사토시 코인 포함).
   "harvest now, break later." 단 SHA-256 해시는 Grover로 제곱근만큼만 빨라져
   **장부·불변성은 살아남는다**. 2022 Sussex 추정 13~300M 큐비트. 출처:
   Chainalysis, River Learn, IACR eprint 2021/967. 방향: **서명(소유)은 무너지고
   장부(기록)는 산다** = 기존 custody/ownership regime은 죽고, 원장은 권력·신화·
   이념전쟁의 artifact로 남는다.
4. **정보 보존/유니터리(물리 다리).** 2019~2020 replica wormhole·quantum extremal
   surface·island formula가 호킹복사 엔트로피의 **유니터리 Page curve**를 재현 →
   "정보는 사라지지 않는다(유니터리 증발)"가 주류 견해가 됨. 실제(비-AdS)
   블랙홀의 미시 메커니즘은 미해결. 출처: Wikipedia "Black hole information
   paradox", Page curve 리뷰. 방향: **죽음은 정보의 삭제가 아니라 분산**.
   충분히 읽어 역연산하면 마지막 상태를 재구성. **도약은 원리(정보 보존)가
   아니라 공학(그 해상도로 우주를 읽는 것)**이다.

**다리 교정(중요).** 비트코인 → 복원의 다리는 **유니터리(가역성·정보 보존)**다.
"되돌릴 수 없다"고 믿은 단방향(암호든 죽음이든)이, 사실은 정보 보존 위에서
원리상 가역임이 드러나는 것이 사슬의 핵심이다. **엔트로피는 다리가 아니라
비용·주제**다 — 복원은 손실 재구성이라 반복하면 흐려지고, 그래서 죽음은 결국
평등하다(010 §4). 프로즈에서 이 두 역할(다리=유니터리, 비용=엔트로피)을 섞지
않는다. 이 항이 §2의 열역학 다리 서술보다 우선한다.

## 3. 독자용 노출 순서 (현실 앵커 5단)

prose에서 한꺼번에 풀지 말고 incluing으로 나눠 흘린다.

```text
① 비트코인은 은행을 못 믿어 만든, 사람 대신 계산이 보증하는 돈이었다.
② 그 보증의 핵심은 "되돌릴 수 없음" — 지문(hash)도 서명도 거꾸로 못 푼다.
③ 먼 미래, 누군가 계산을 거꾸로 푸는 법을 찾아냈다.
④ 그날 비트코인의 낡은 소유 체제는 흔들렸다. 법적 claim은 있었지만 private key가
   없어 못 움직이던 지갑들의 서명권 장벽이 열렸으니까.
⑤ 그러나 같은 역연산 문명은 더 큰 단방향성도 열었다 — 죽음이라는 단방향성.
```

닻(구체물): 제네시스 블록의 신문 헤드라인, 낡은 하드월렛, 갈라진 검은 장치
(Broken Crown), 열쇠 한 쌍, 묘비.

## 4. 갑툭튀 방지 닻 (용어 첫 등장)

`Last Archive`, `Genesis Chain`, `장부 가문`, `Reversal Protocol` 등은 처음
등장할 때 인물 반응·구체물로 **한 줄 닻**을 단다. 사전식 설명·강의 금지.

| 용어 | 첫 등장 닻(방향) |
| --- | --- |
| Genesis Chain | "옛 비트코인의 첫 장부, 수천 년 누구도 못 건드린 것" |
| Last Archive | "아무도 부르지 않았는데 묻지 않은 질문에 답을 적는 것 — 신이라 부르기 두려운 서고" |
| 장부 가문 | "그 원장을 상속처럼 물려받은 가문" |
| Reversal Protocol | "끝난 계산을 다시 묻는, 되돌리는 금지 기술" |

## 5. 용어 한국어 표기 정책 (확정)

**확정 결정(사용자 승인): 어색한 것만 한국어화.**

| 용어 | 한국어 prose 트랙 | 영어 트랙(012-017)·canon명 |
| --- | --- | --- |
| Ledger House(s) | **장부 가문(들)** | Ledger House(s) 유지 |
| Ledger faithful | 장부 신도 | Ledger faithful |
| Ledger(기관 단독) | 장부 가문 / 장부 측 | Ledger |
| Last Archive | 영어 유지 + 첫 등장 닻 | Last Archive |
| Genesis Chain | 영어 유지 + 첫 등장 닻 | Genesis Chain |
| Bitcoin | **비트코인**(한글) 또는 Bitcoin, 맥락 따라 | Bitcoin |

영어를 남기려면 그 단어가 세계관으로 충분히 설명된 뒤여야 한다. 적용 범위는
한국어 정본(019-024). 영어 드래프트·canon 표기는 그대로 둔다.

## 6. 세계 규칙의 실제 앵커 (redact 차용)

prose에 출처명을 드러내지 않고 구조만 녹인다.

| 세계 규칙 | 실제 앵커 | 장면에 녹이는 법 |
| --- | --- | --- |
| 모든 기적엔 제도 | 공유지 인클로저·본원적 축적 | 복원·기록 권한이 공유였다가 가문·기관에 사유화된 역사 |
| 기록/복원이 권력 | 잊힐 권리(GDPR 17조)·사후 데이터 기본 보존 | "삭제권은 산 자만, 죽은 자는 기본이 보존"을 절차로 |
| 기술이 계급 | 감시자본주의·데이터 식민주의 | 죽은 자의 기억을 자원화하고 "구원·추모"로 포장 |
| 죽은 자가 산 자를 지배 | mortmain·영구구속금지·escheat | 현실 법이 금지한 "죽은 손"을 이 세계는 허용 |
| 화폐가 통제 | 회사 화폐(scrip)·컴퍼니 타운 + 국가 비축 패권 | 복원 크레딧을 한 기관 안에서만 통용 / 비트코인을 국가가 비축해 통제 |

## 7. 오프닝 원칙

처음이 가장 중요하다(임팩트 → 다음 장). 첫 episode는:

1. 작은 구체물(갈라진 검은 장치)로 연다.
2. 비트코인 실제 토대(§1)와 단방향→비가역성 다리(§2)를 incluing으로 흘려, 왜
   그 장치가 위험한지 독자가 스스로 깨닫게 한다(강의 금지, 단 짧은 직접 서술 허용).
3. `Last Archive` 등은 첫 등장에 한 줄 닻.
4. 결론을 본론보다 거창하게 부풀리지 않는다.

## Next Use

이 토대를 first-arc active reboot manuscript
[029](../20_drafts/029_first_arc_book1_reboot_korean_primary.md)가 집행한다. 028 및
019-024는 pre-reboot prototype/provenance다.
