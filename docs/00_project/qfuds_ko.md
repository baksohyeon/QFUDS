---
doc_id: qfuds_korean_overview
title: Quantum Foam Unified Dark Sector (QFUDS)
doc_type: reference
stage: "reference"
status: reference
evidence_role: reference
depends_on:
  - project_overview
next_gate: keep Level 2B blocked; no CMB or matter-power claims
last_updated: 2026-06-11
---

# Quantum Foam Unified Dark Sector (QFUDS)

언어: [English](../../README.md) | Korean

## 암흑물질, 암흑에너지, 정보 순환을 하나로 묶어본다면 어떨까?

### 초록

이 저장소는 암흑물질과 암흑에너지가 같은 미시적 양자 시공간 거품 부문(quantum-spacetime foam sector)의 서로 다른 거시적 상으로 나타날 수 있는지 탐색합니다. 표준 LCDM에서는 암흑물질과 암흑에너지를 서로 다른 성분으로 둡니다. QFUDS는 두 현상이 하나의 양자 거품 매질이 큰 스케일에서 다르게 보인 결과일 수 있는지 묻습니다.

비유하면, 물은 조건에 따라 얼음, 액체 물, 수증기로 보일 수 있습니다. QFUDS는 암흑부문에 대해 비슷한 질문을 던집니다. 하나의 바탕 매질이 어떤 조건에서는 물질처럼 보이고, 다른 조건에서는 진공압처럼 보일 수 있는가?

이 그림에서 뭉치는 상(clustering phase)은 $w \simeq 0$, $c_s^2 \simeq 0$인 거의 압력 없는 성분처럼 행동해야 합니다. 그래야 차가운 암흑물질처럼 구조 형성에 참여할 수 있습니다. 잔여 상(residual phase)은 우주의 가속팽창을 설명하려면 $w \simeq -1$인 느린 진공압 성분처럼 행동해야 합니다. 블랙홀은 QFUDS의 증거로 쓰지 않습니다. 최대한 조심스럽게 말해도, 블랙홀은 QFUDS 언어에서 국소 정보 압축 지점(local information-compression site)으로 붙여볼 수 있는 추측적 라벨일 뿐입니다. 블랙홀/화이트홀 잔여체도 동역학과 제약이 유도되기 전까지는 같은 거품 부문 안의 부차적 위상 결함 후보로만 둡니다.

이 모델은 일반상대론의 프리드만 배경 동역학을 유지합니다. 대신 암흑에너지 변화, 작은 스케일의 은하 헤일로 구조, 암흑부문 뭉침에서 LCDM과 다른 신호가 가능한지 묻습니다. 블랙홀 증발에 대한 언급은 양자중력 동기이지, 이 저장소의 현재 관측 테스트가 아닙니다.

이 프로젝트는 완성된 물리 이론이 아니라 연구 프로그램이자 검증용 장난감 프레임워크입니다.
목적은 제 가설을 실제 테스트에 올려보고, 우주마이크로파배경(CMB), 대규모 구조, 은하 헤일로 밀도 분포, 암흑물질 검출 실험, 암흑에너지 상태방정식 정밀 측정으로 반박 가능한 예측으로 바꾸는 것입니다.

### 기본 변수

상태방정식 변수 $w$는 압력을 에너지 밀도로 나눈 값입니다. $w \simeq 0$이면 물질처럼 희석되고, $w \simeq -1$이면 암흑에너지처럼 행동합니다.

유효 음속 $c_s^2$는 유효 매질이 뭉치려는 변화에 얼마나 강하게 저항하는지를 나타냅니다. QFUDS가 살아남으려면 뭉치는 상에서 $c_s^2 \simeq 0$이어야 합니다.

비유하면, 모래는 쌓여서 더미를 만들 수 있지만 팽팽한 트램펄린은 누르면 다시 밀어냅니다. 은하가 형성될 때 암흑물질 같은 성분은 트램펄린보다 모래에 가까워야 합니다.

### 핵심 가설

암흑물질과 암흑에너지는 근본적으로 분리된 두 물질이 아닐 수 있습니다.
같은 미시적 양자 시공간 거품이 거시적으로 다르게 나타난 두 상일 수 있습니다.

```text
dark matter  -> 뭉치는 거품 상(clustering foam phase)
dark energy  -> 잔여 진공압 상(residual vacuum-pressure phase)
remnants     -> 같은 거품 부문의 선택적 결함(optional defects)
```

더 간단히 줄여서 설명하면 아래와 같습니다.

```text
암흑물질 + 암흑에너지
= 양자 시공간 거품의 두 유효 상
```

블랙홀과 화이트홀 비슷한 잔여체는 부차적입니다. QFUDS 언어로는 정보 압축 지점이나 위상 결함처럼 읽을 수 있지만, 이것은 확립된 블랙홀 물리나 은하 형성 물리가 아니라 추측적 재해석입니다. 현재 기준으로는 핵심과 거리가 있어 아직 다루지 않는 주제입니다.

## 가설을 세운 계기

### 정보 삭제에서 검증 모델까지

Quantum Foam Unified Dark Sector (QFUDS)는 암흑물질, 암흑에너지, 우주론에서의 정보 흐름을 생각하다가 시작한 장난감 개념의 저장소입니다.

이 아이디어가 어디까지 정합적인지 궁금했습니다.

호기심을 방정식, 제약 조건, 장난감 코드, 반박 가능한 질문으로 바꾸고 가설 검증을 실제로 해보고 싶었습니다.

정보 열역학에 대한 글을 읽었습니다.

```text
동기 부여 원문. 출처 기록으로 보존하며, 기술적 주장으로 쓰지는 않습니다:
『기억을 지울 때, 반드시 열이 발생한다』고 물리학이 증명했습니다.
물리학자 롤프 란다우어가 제창한 원리입니다. 계산을 수행하거나 정보를 생성하는 행위 자체는 에너지를 소모하지 않지만, 1비트의 정보를 지우거나 잊을 때에는 반드시 일정량의 열에너지가 주변으로 방출된다는 것입니다.
즉, 인간의 뇌도 하드디스크도, 무언가를 「잊음」할 때 우주의 엔트로피를 증가시키며, 물리적인 열을 만들어내고 있습니다. 정보에 질량이 있다고 말할 수는 없지만, 정보의 소거에는 열역학적인 대가가 따른다는 뜻입니다.
「잊는다」는 일견 모호해 보이는 현상이, 실은 우주에 열로서 지불되고, 그 장부에 제대로 기록된다는 것입니다.
이는 뇌과학 이야기이자, 컴퓨터의 한계 이야기이며, 우주론 이야기이기도 합니다.
```

보수적으로 읽으면, Landauer 원리는 열적 환경과 결합된 물리계에서 논리적으로 비가역적인 정보 소거에 적용됩니다. 모든 계산이 같은 필연적 비용을 가진다는 뜻도 아니고, 그 자체로 우주론을 함의하는 것도 아닙니다.

비유하면, 파일을 삭제한다고 노트북이 물리 법칙을 무시하는 것은 아닙니다. 노트북은 여전히 에너지를 쓰고 열을 냅니다. 일반적인 Landauer 가정 아래에서 1비트 소거의 이상적 최소 비용은 대략 $k_B T \ln 2$입니다. 긴 원문 흐름은 여기서 반복하지 않고 [concept_origin.md](../01_origin/concept_origin.md)에 보존합니다.

그래서 저는 읽자마자 블랙홀 질문이 자연스럽게 나왔습니다.
정보에 물리적 비용이 있다면, 양자 이론 안에서 블랙홀은 정보를 버리는 단순한 쓰레기통처럼 취급하기 어렵습니다. 이것은 QFUDS의 유도가 아니라 더 날카로운 질문을 만들기 위한 동기입니다.
다음 질문은 정보가 어디에 인코딩되는지, 유니터리한 블랙홀 증발 과정이 복사의 상관관계를 통해 정보를 되돌릴 수 있는지, 그리고 장애물이 정보 파괴인지 해독 복잡도인지입니다.

처음 사고 흐름은 증명이 아니었습니다. 질문은 대략 이렇게 이동했습니다.

```text
정보 삭제에는 열 비용이 있다
-> 블랙홀 정보 손실 문제와 구조가 비슷하다
-> 유니터리한 블랙홀 증발이라면 정보가 상관관계 안에 인코딩되어야 한다
-> 원리상 복구는 가능하지만 해독 비용이 막는다
-> 복구가 가능하다면 역과정을 묻는다
-> 역과정은 시간역전, CPT, 화이트홀 비슷한 대응물을 떠올리게 한다
-> 블랙홀/화이트홀 잔여체는 정보 저장 부문을 암시한다
-> 진공 또는 시공간 거품이 후보 매질이 된다
-> 암흑물질은 뭉치는 거품 모드일 수 있다
-> 암흑에너지는 잔여 거품 압력일 수 있다
-> QFUDS: 통합 암흑부문 장난감 모형
```

화이트홀/역과정 질문은 흥미로웠지만, SF 소설에 가깝고 과학적으로 엄밀한 주장이 되기에는 너무 크고 장황했습니다.

하나씩 짚어가다보니 하나의 질문으로 수렴했습니다.

```text
하나의 암흑부문이
뭉치는 성분과 잔여 진공압 성분으로 동시에 행동할 수 있는가?
```

다음 검증 질문은 $\Gamma(a)$로 이동했습니다.
뭉치는 거품 상이 잔여 진공압 상으로 넘어간다면, 그 전달률을 구조 성장, 블랙홀 엔트로피, 지평선 엔트로피, 별 형성, 잔여체 통계 같은 물리량이나 명시적으로 라벨링된 현상론적 대리 지표에 묶을 수 있는가?

비유하면, 두 물탱크가 연결된 상황입니다. 한쪽 탱크는 뭉치는 성분이고, 다른 탱크는 잔여 진공압 성분입니다. $\Gamma(a)$는 두 탱크 사이의 밸브 규칙입니다. 밸브를 마음대로 조절하면 튜닝이고, 밸브 규칙이 실제 물리량에서 나오면 테스트할 수 있습니다.

### 발산, 수렴, 검증

QFUDS라는 개념은 저와 GPT와의 반복 대화에서 나왔습니다.

```text
날것의 질문
-> 설명
-> 후속 질문
-> 반례 또는 물리 제약
-> 더 넓은 추측
-> 가지치기
-> 장난감 모형
-> 적대적 리뷰
-> 이 저장소의 코드와 출력물
```

발산 단계에서는 Landauer, 블랙홀 정보, 호킹복사, Page curve, island, 역과정, 화이트홀, 양자 거품, 암흑물질, 암흑에너지, 우주상수, 세계관적 상상까지 바깥으로 뻗었습니다.

수렴 단계에서는 반복되는 질문 하나만 남겼습니다.

```text
암흑물질과 암흑에너지를
같은 양자 거품 매질의 두 유효 모드로 볼 수 있는가?
```

검증 단계에서는 은유를 줄이고 기본적인 우주론 검사 앞에 세웠습니다.

```text
무편차 극한에서 LCDM을 회복하는가?
뭉치는 상이 c_s^2를 0에 가깝게 유지할 수 있는가?
CMB 음향 피크를 보존하는가?
물질 파워 스펙트럼을 보존하는가?
현실적인 은하 헤일로를 만들 수 있는가?
잔여체 부문이 조밀 천체 제약을 통과하는가?
```

### 폐기되거나 보존된 가지

날것의 아이디어에는 여러 가지가 섞여 있었습니다.

```text
정보 처리기로서의 블랙홀
화이트홀 비슷한 역방향 통로
화이트홀 비슷한 방출로서의 우주
드문 암흑 구조로서의 진공 요동
잔여 진공압으로서의 우주 가속
```

이 저장소는 변수, 방정식, 테스트로 바꿀 수 있는 가지만 남깁니다. 현재 연구 버전은 다음 질문입니다.

```text
양자 거품 통합 암흑부문이
암흑물질과 암흑에너지로 설명되는 관측 효과를 재현할 수 있는가?
```

기준은 단순합니다.

```text
이 아이디어를 틀릴 수 있을 만큼 정확하게 만들 수 있는가?
```

세부 원문 흐름은 이 개요에서 반복하지 않습니다. 출처 기록은 [concept_origin.md](../01_origin/concept_origin.md)에 보존합니다.

## 연구 프로그램

제가 장난스럽게 떠올린 가설이 어디까지 정합적인지 확인하려고 구현해보았습니다.

```text
직관
-> 가지치기
-> 가설
-> 장난감 방정식
-> 폐기 조건
-> 코드와 미래의 볼츠만 코드 검증
```

목표는 QFUDS를 증명하는 것이 아닙니다.
목표는 이 모델을 가장 먼저 죽이는 제약을 찾거나, 살아남는 버전을 LCDM, 통합 암흑 유체, 상호작용 암흑에너지, 스칼라장 암흑물질, 블랙홀/화이트홀 잔여체 모형과 비교할 수 있을 만큼 좁히는 것입니다.

### 주요 문서

- 현재 상태와 단계별 진행: [Roadmap](../05_next_steps/000_roadmap.md)
- 결정 이유: [Decision Log](decision_log.md)
- 실험별 결론: [Experiment Summary](../04_results/000_experiment_summary.md)
- 주장/증거 추적: [Traceability Matrix](traceability_matrix.md)
- [Level 1.5](../wiki/glossary/repository_levels.md) 통과/실패 관문: [Level 1.5 Resolution Gate](../05_next_steps/015_level_1_5_resolution_gate.md)
- 로드맵 한국어 해설: [Roadmap Overview Korean Guide](../05_next_steps/900_roadmap_overview_ko.md)
- 재현 가능한 검사: [Verification Guide](verification_guide.md)
- 문서 무결성 규칙: [Experiment Record Convention](experiment_record_convention.md) 및 [Frontmatter Convention](frontmatter_convention.md)

CMB와 구조 형성 검사를 통과하기 전까지는 강한 물리적 주장으로 읽으면 안 됩니다.

연구 기록은 아래 명령으로 감사합니다.

```bash
python3 scripts/validate_docs.py
python3 scripts/research_consistency.py
python3 scripts/preflight_exp004.py
```

`validate_docs.py`는 메타데이터와 실험/결과 문서의 필수 섹션을 검사합니다.
`research_consistency.py`는 로드맵이 상태 권한 문서로 유지되는지 검사합니다.
`preflight_exp004.py`는 exp_004 계획 전에 exp_003 기록이 일관적인지 검사합니다.

검증 순서는 다음과 같습니다.

```text
문헌상 위치 확인
-> 배경 우주 검증
-> 상 전달 물리성
-> 현상론적 섭동 닫힘
-> 물리적 섭동 방정식
-> CLASS 또는 CAMB 통합
-> CMB 비교
-> 물질 파워 비교
-> DESI / Euclid / Roman 제약
```

비유하면, 이 과정은 다리를 단계별로 시험하는 것과 비슷합니다.
책상 위 작은 모형은 나쁜 설계를 떨어뜨릴 수 있지만, 실제 다리가 바람, 차량, 지진을 버틴다는 증거는 아닙니다.
배경 우주 수준 실험은 나쁜 전달 법칙을 탈락시킬 수 있지만, CMB나 구조 형성 생존성을 주장할 수는 없습니다.

### 현재 작업 가설: 두 상 전달 모형

```text
거의 0에 가까운 음속을 가진 양자 거품 통합 암흑부문
```

더 안전한 공식화는 일반상대론 안의 통합 암흑부문입니다.

$$
\rho_{\rm dark} = \rho_{\rm QF} + \rho_{\rm rem}
$$

$\rho_{\rm QF}$는 양자 거품 통합 암흑 유체입니다. 두 유효 조각을 가집니다.

$$
\rho_{\rm QF}(a) = \rho_{\rm cluster}(a) + \rho_{\rm residual}(a)
$$

뭉치는 조각은 차가운 암흑물질처럼 행동해야 합니다.

$$
\rho_{\rm cluster} \propto a^{-3}, \qquad
w \simeq 0, \qquad
c_s^2 \simeq 0
$$

잔여 조각은 암흑에너지처럼 행동해야 합니다.

$$
\rho_{\rm residual} \simeq \rho_\star, \qquad
w \simeq -1
$$

선택적 잔여체 조각은 다음처럼 씁니다.

$$
\rho_{\rm rem} = \int M f(M)\,dM
$$

실험 001은 뭉치는 상과 잔여 상 사이에 전달률을 추가합니다.

$$
\frac{d\rho_A}{d\ln a} + 3\rho_A = -\Gamma(a)\rho_A
$$

$$
\frac{d\rho_B}{d\ln a} = \Gamma(a)\rho_A
$$

현재 테스트는 $\Gamma(a)$를 손으로 맞추는 함수가 아니라 물리적 원천 또는 명시적으로 라벨링된 대리 지표에 묶을 수 있는지입니다.
유용하지만 아직 잠정적인 검증 방향은 저적색편이 붕괴, 블랙홀 엔트로피, 별 형성 대리 지표입니다.
상수 전달이나 제한 없는 성장 기반 전달은 일찍 실패하거나 평범한 상호작용 암흑에너지 거동으로 돌아갈 것입니다.

비유하면, 두 물탱크가 연결된 상황입니다. 한 탱크는 뭉치는 상이고, 다른 탱크는 잔여 상입니다. $\Gamma(a)$는 밸브 규칙입니다. 밸브 규칙을 마음대로 정하면 그냥 튜닝입니다. 밸브 규칙이 물리적 원천에서 나오면 테스트할 수 있습니다.

잔여체 항은 그 질량 분포가 미시중력렌즈, CMB, 구조 형성 제약을 통과하기 전까지 부차적으로 두고 진행할 것입니다.

### 핵심 전제 조건

가장 중요한 조건은 유효 음속입니다.

$$
c_s^2 \simeq 0
$$

쉽게 말하면 다음과 같습니다.

```text
QFUDS 거품은 배경 우주에서는 우주를 밀어내는 압력을 남길 수 있지만,
은하 형성 단계에서는 압력 없는 먼지처럼 뭉쳐야 한다.
```

거품이 너무 뻣뻣하면 압력이 구조 형성을 지워버립니다. 그러면 모델은 즉시 죽습니다.

비유하면, 마른 모래는 쌓아서 더미를 만들 수 있습니다. 하지만 탄성 있는 고무판으로 같은 더미를 만들려고 하면 계속 밀려나서 평평해집니다. 뭉치는 상은 은하가 만들어질 만큼 모래 같아야 합니다.

### 이 모델이 해결하려는 문제

이 모델은 세 가지 생각을 연결하려 합니다.

1. 통합 암흑부문: 암흑물질과 암흑에너지가 같은 기원을 가질 수 있는가
2. 우연성 문제: 왜 현재 우주에서 암흑물질과 암흑에너지 밀도가 비슷한가
3. 동적인 진공에너지: 우주상수가 손으로 넣은 고정 숫자가 아니라 느리게 완화되는 평형값일 수 있는가

### 만약 유효하다면 예측할 수 있는 현상

아래 항목은 검증된 예측이 아닙니다. 모델을 죽일 수 있는 후보 지점이며, 몇몇 항목은 QFUDS만의 고유 신호도 아닙니다.

1. 표준 WIMP 직접 검출은 계속 무검출일 수 있습니다. 하지만 이것만으로 QFUDS가 유리해지는 것은 아닙니다. 직접 검출 신호가 약하거나 숨겨진 비-QFUDS 암흑물질 모형도 많기 때문입니다.
2. 암흑에너지는 작지만 0이 아닌 시간 변화를 보일 수 있습니다.

$$
w(a) = w_0 + w_a(1-a)
$$

LCDM에서는 $w_0=-1$, $w_a=0$입니다. QFUDS가 차이를 만들려면 $w_0 \simeq -1$이면서 $|w_a|>0$인 작은 편차가 필요합니다.

3. 대규모 구조와 CMB는 거의 LCDM처럼 보여야 합니다.
4. 작은 은하 헤일로는 뾰족한 중심부보다 완만한 중심부를 선호할 수 있지만, 보통 물질 되먹임과 구분해야 합니다.
5. 암흑물질 구조와 보통 물질 구조 사이에 순수한 무충돌 CDM보다 약간 더 강한 상관이 남을 수 있습니다. 하지만 QFUDS 고유의 관계식은 아직 유도되지 않았습니다.
6. 완전한 유니터리 양자 서술에서는 최종 블랙홀 증발 상태가 정보가 전혀 없는 순수 열복사로만 기술되면 안 됩니다. 이것은 양자중력의 정합성 기대이지, 관측된 천체물리 신호는 아닙니다.
7. 블랙홀/화이트홀 잔여체가 있다면 허용 가능한 질량 분포는 좁아야 합니다.

현재 검증하려는 테스트의 핵심은 화이트홀이 아닙니다.
정밀 관측이 계속 $w=-1$을 지지하는지, 아니면 작은 0이 아닌 $w_a$ 쪽으로 움직이는지가 더 중요합니다.

### 폐기 테스트: 먼저 공격해야 할 지점

적대적인 리뷰어라면 이 순서로 공격할 것입니다.

1. 무편차 극한에서 LCDM을 정확히 회복하는가?
2. 같은 유효 매질이 $w \simeq 0$과 $w \simeq -1$을 손흔들기식 설명 없이 만들 수 있는가?
3. 왜 $c_s^2$가 0에 가까운가?
4. CMB 음향 피크를 보존하는가?
5. 물질 파워 스펙트럼을 보존하는가?
6. 기존 통합 암흑 유체나 k-에센스 모형보다 나은 것이 있는가?
7. 잔여체 부문은 실제 예측을 추가하는가, 아니면 이야기용 언어인가?

여기서 실패하면 QFUDS는 이름만 바꾼 용어 교체입니다.

## 블랙홀 해석: 증거가 아닌 재읽기

블랙홀은 QFUDS의 중심 증거가 아닙니다.

관측 기준선은 다음과 같습니다.

```text
많은 대질량 은하, 특히 중심 팽대부를 가진 은하는 중심에 대질량 블랙홀을 가진다.
```

우리 은하 중심 블랙홀과 M87의 블랙홀이 대표적인 예입니다. 존재 자체는 별 궤도 동역학과 사건지평선 스케일 영상으로 관측적으로 확립되어 있습니다. 다만 정확한 형성 경로는 여전히 연구 중입니다. 씨앗 블랙홀 형성, 가스 강착, 은하와 블랙홀 병합, 직접 붕괴, 조밀한 항성계 동역학, 암흑물질 헤일로 안의 형성 같은 표준 천체물리 설명은 여전히 중요합니다.

표준 구조 형성 순서는 다음에 더 가깝습니다.

```text
원시 밀도 요동
-> 차가운 암흑물질 헤일로
-> 가스 냉각, 별 형성, 은하
-> 중심 대질량 블랙홀 씨앗과 강착/병합 성장
```

이것은 블랙홀이 은하를 만든다는 말과 다릅니다. 블랙홀은 특히 활동은하핵 피드백을 통해 숙주 은하에 영향을 줄 수 있지만, 표준 그림에서 은하 형성의 일반적인 출발점은 아닙니다.

QFUDS는 다른 질문을 던질 수 있습니다.

```text
암흑 헤일로가 유효 거품 상이라면,
중심 블랙홀은 그 상의 특수한 고밀도,
고엔트로피, 높은 정보 밀도 영역을 추적하는가?
```

첫 번째 조건은 QFUDS 가정이지 표준 결과가 아닙니다. 표준 우주론은 다음을 말하지 않습니다.

```text
양자 거품 -> 암흑 헤일로
```

QFUDS가 더 강하게 묻는 질문은 다음과 같습니다.

```text
암흑물질이 거품 상이라면,
중심 블랙홀은 그 거품 부문 안의
특수한 압축 지점이나 상전이 지점일 수 있는가?
```

만약 QFUDS 관점으로 해석한다면 다음과 같습니다.

```text
black hole = 가능한 국소 정보 압축 지점
```

더 강하게 말하면:

```text
black hole = 거품 부문의 추측적 상전이 후보 지점
```

이것은 확립된 블랙홀 물리가 아닙니다. 기존 문헌에도 "블랙홀 상전이"라는 표현은 있지만, 보통 반-드 지터(AdS) 공간이나 확장된 블랙홀 열역학 문맥의 Hawking-Page 전이 등을 뜻합니다. 그것이 관측된 은하 중심 블랙홀이 양자 거품 암흑부문의 상전이 지점이라는 뜻은 아닙니다.

비유하면, 큰 도시에는 보통 데이터가 많이 오가는 경로 근처에 큰 데이터 센터가 있을 수 있습니다. 하지만 데이터 센터가 있다고 해서 도시 전체가 그 네트워크 때문에 생겼다는 증거는 아닙니다. 마찬가지로 중심 블랙홀은 QFUDS 언어로 압축 지점이나 경로 지점처럼 읽을 수 있지만, QFUDS를 증명하지는 않으며 표준 블랙홀 형성 물리를 대체하지도 않습니다.

안전한 문장은 다음 정도입니다.

```text
QFUDS는 중심 블랙홀을 거품이 지배하는 헤일로 안의 가능한 정보 압축 지점으로 재해석할 수 있지만, 이것은 추측이며 많은 대질량 은하가 왜 중심 블랙홀을 가지는지는 아직 설명하지 못합니다.
```

### 문서

문서 권한 구조:

- [CLAUDE.md](../../CLAUDE.md)와 [AGENTS.md](../../AGENTS.md)는 에이전트 행동을 정의합니다.
- [Roadmap](../05_next_steps/000_roadmap.md)은 현재 상태, 활성 관문, 막힌 지점의 단일 진실 공급원입니다.
- [Decision Log](decision_log.md)는 결정 이유를 기록합니다.
- [Experiments](../03_experiments/)와 [Results](../04_results/)는 증거를 보관합니다.

유지되는 연구 문서:

- [PROJECT.md](../../PROJECT.md): 문서 관리와 검증 순서
- [docs/README.md](../README.md): 문서 색인과 폴더 지도
- [overview.md](overview.md): 프로젝트 목표, 한계, 모델 계보
- [decision_log.md](decision_log.md): 이유와 증거가 포함된 시간순 결정 기록
- [verification_guide.md](verification_guide.md): 현재 검증을 다시 실행하고 읽는 방법
- [frontmatter_convention.md](frontmatter_convention.md): 표준 메타데이터 스키마
- [experiment_record_convention.md](experiment_record_convention.md): 실험/결과 섹션 규칙, 요약 정책, postmortem 정책
- [traceability_matrix.md](traceability_matrix.md): 양방향 주장/증거 추적 색인
- [000_qfuds_v0_1_conceptual_origin.md](../02_theory/000_qfuds_v0_1_conceptual_origin.md): 개념 기원 단계 이론 노트
- [000_qfuds_v0_2_two_phase_background.md](../02_theory/000_qfuds_v0_2_two_phase_background.md): 최소 두 상 유효 유체 이론 노트
- [010_qfuds_v0_3_gamma_laws.md](../02_theory/010_qfuds_v0_3_gamma_laws.md): 물리적으로 라벨링된 $\Gamma(a)$ 전달 법칙 이론 노트
- [015_qfuds_v0_15_phase_transfer_physics.md](../02_theory/015_qfuds_v0_15_phase_transfer_physics.md): 상 전달 물리성 감사
- [030_qfuds_phenomenological_perturbations.md](../02_theory/030_qfuds_phenomenological_perturbations.md): 현상론적 섭동 닫힘 이론 노트
- [000_exp_000_lcdm_baseline.md](../03_experiments/000_exp_000_lcdm_baseline.md): 무전달 LCDM 대조군 실행
- [010_exp_001_gamma_scan.md](../03_experiments/010_exp_001_gamma_scan.md): 전달 법칙 스캔
- [015_exp_001_5_phase_transfer_physicality.md](../03_experiments/015_exp_001_5_phase_transfer_physicality.md): 물리성 관문
- [020_exp_002_entropy_information_gate.md](../03_experiments/020_exp_002_entropy_information_gate.md): 엔트로피/정보원 관문
- [030_exp_003_phenomenological_perturbation_closure.md](../03_experiments/030_exp_003_phenomenological_perturbation_closure.md): 섭동 닫힘 감사
- [000_result_000_lcdm_baseline.md](../04_results/000_result_000_lcdm_baseline.md): 무전달 기준 결과
- [010_result_001_gamma_scan.md](../04_results/010_result_001_gamma_scan.md): 결과 해석과 다음 표적
- [015_result_001_5_phase_transfer_physicality.md](../04_results/015_result_001_5_phase_transfer_physicality.md): 물리성 결과
- [020_result_002_entropy_information_gate.md](../04_results/020_result_002_entropy_information_gate.md): 엔트로피/정보원 provenance 결과
- [030_result_003_phenomenological_perturbation_closure.md](../04_results/030_result_003_phenomenological_perturbation_closure.md): 섭동 닫힘 결과
- [000_experiment_summary.md](../04_results/000_experiment_summary.md): 가벼운 실험별 결론 요약과 postmortem 현황
- [000_roadmap.md](../05_next_steps/000_roadmap.md): 검증 단계, 상태, 막힌 지점
- [010_perturbation_gate.md](../05_next_steps/010_perturbation_gate.md): 섭동 관문
- [015_level_1_5_resolution_gate.md](../05_next_steps/015_level_1_5_resolution_gate.md): Level 1.5 통과, 실패, demotion의 증거 기준

역사/출처 노트:

- [concept_origin.md](../01_origin/concept_origin.md): 날것의 정보 흐름 아이디어가 QFUDS 질문이 된 과정
- [README.md](../../README.md): 이 문서의 영어판
- [research_program.md](research_program.md): 초록, 검증 로드맵, 폐기 조건
- [900_qfuds_research_report.md](../02_theory/900_qfuds_research_report.md): 적대적 문헌 비교와 수학적 공식화

### 저장소 검사

문서 frontmatter와 교차 링크를 검증합니다.

```bash
python3 scripts/validate_docs.py        # 또는: make validate
```

저장소 상태 권한 일관성을 검사합니다.

```bash
python3 scripts/research_consistency.py  # 또는: make research-audit
```

주요 실험 마일스톤 전에 전체 preflight 감사를 실행합니다.

```bash
make preflight
```

커밋 전에 같은 문서/회귀 검사를 강제하고 싶다면 로컬 git pre-commit hook을 설치합니다.

```bash
make install-git-hooks
```

이 hook은 검증을 실행하기 전에 staged Markdown frontmatter의 `last_updated`
날짜도 자동으로 갱신합니다.

experiment 004 preflight gate를 실행합니다.

```bash
python3 scripts/preflight_exp004.py
```

이 관문은 [030_exp003_record_consistency_gate.md](../05_next_steps/030_exp003_record_consistency_gate.md)에 문서화되어 있으며 `make preflight-exp004`로도 실행됩니다.

### 참조 문헌

아래 링크들은 결이 비슷한 참조 문헌입니다. QFUDS를 증명하지는 않습니다.

- [Hawking evaporation and the Landauer Principle](https://arxiv.org/abs/2407.08777)
- [Landauer Principle Stands up to Quantum Test](https://physics.aps.org/articles/v11/49)
- [Entanglement Wedge Reconstruction and the Information Paradox](https://arxiv.org/abs/1905.08255)
- [Replica wormholes and the black hole interior](https://arxiv.org/abs/1911.11977)
- [Black hole fireworks: black-to-white-hole tunneling](https://arxiv.org/abs/1407.0989)
- [Small black/white hole stability and dark matter](https://arxiv.org/abs/1805.03872)
- [The Thermodynamics of Black Holes](https://link.springer.com/article/10.12942/lrr-2001-6)
- [Coevolution (Or Not) of Supermassive Black Holes and Host Galaxies](https://arxiv.org/abs/1304.7762)
- [The origins of massive black holes](https://www.nature.com/articles/s42254-021-00364-9)
- [Formation of Supermassive Black Hole Seeds](https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/formation-of-supermassive-black-hole-seeds/DA9F246C7A0C6C1C0E057CCBF40220F6)
- [First M87 Event Horizon Telescope Results IV](https://arxiv.org/abs/1906.11241)
- [First Sagittarius A* Event Horizon Telescope Results III](https://arxiv.org/abs/2311.09479)
- [Cold dark matter: Controversies on small scales](https://pmc.ncbi.nlm.nih.gov/articles/PMC4603506/)
- [Direct Detection of Dark Matter: A Critical Review](https://www.mdpi.com/2073-8994/16/2/201)
- [Planck 2018 cosmological parameters](https://arxiv.org/abs/1807.06209)
- [DESI DR2 results guide](https://www.desi.lbl.gov/2025/03/19/desi-dr2-results-march-19-guide/)
- [Unified dark fluid with null sound speed](https://arxiv.org/abs/2509.16155)
