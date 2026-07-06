// QFUDS Verse 세계관 코덱스 데이터
// 출처: baksohyeon/QFUDS docs/wiki/fiction/10_universes/qfuds-verse (continuity 001, world 105/109/111/123/124/125)
// cat: era | faction | char | ideo | term
// links: 판독 시 해금되는 인접 기록 (무방향 그래프)
window.QFUDS_LORE = (function () {
  var T = function (label, def) {
    return '<span class="term" data-def="' + def.replace(/"/g, '&quot;') + '">' + label + '</span>';
  };
  var nodes = [
    // ───────────── 시대 척추 (era) ─────────────
    {
      id: 'btc-2008', cat: 'era', idx: 0, title: '비트코인', sub: '2008 · 반-권위 신뢰의 씨앗',
      short: '중앙 권력 없는 신뢰라는 첫 실험.',
      body: '<p>2008년, 권위 대신 기록을 믿자는 첫 실험이 시작된다. ' + T('비트코인', '중앙 은행이나 정부 없이, 참여자 전원이 같은 거래 장부를 나눠 갖는 방식으로 돌아가는 전자 화폐. 이 세계관에서는 화폐가 아니라 「권위 없이 진실을 합의한 첫 유물」로 다뤄진다.') + '은 「믿을 제3자를 없앤」 구조였고, 그 역설이 딥타임까지 이어진다.</p><p>창시자 ' + T('사토시 나카모토', '비트코인을 만든 정체불명의 인물 또는 집단. 끝내 신원이 밝혀지지 않았다.') + '는 정체 미상으로 남아 신화·음모론·종교가 된다. 권위 없는 기원 — 이것이 훗날 Last Archive 미스터리의 전조가 된다.</p><p>반-국가 반란으로 태어난 것이 국가 전략 자산으로 포획되는 역설. 이 씨앗은 수천 년 뒤 세 갈래 이념전쟁(비트코인 삼분파)으로 발아한다.</p>',
      links: ['soft-editing', 'genesis-chain', 'satoshi']
    },
    {
      id: 'soft-editing', cat: 'era', idx: 1, title: 'The Soft Editing', sub: '2020s~ · 인식 위기의 시작',
      short: '딥페이크와 AR로 「보는 것 = 믿는 것」이 무너진다.',
      body: '<p>독자의 현재. 후대 문명은 이 시대를 <b>The Soft Editing</b>이라 부른다. ' + T('딥페이크', 'AI로 만들어 낸, 진짜와 구별하기 어려운 가짜 영상·음성. 얼굴과 목소리를 통째로 위조할 수 있다.') + '와 ' + T('AR', '증강현실(Augmented Reality). 눈에 보이는 실제 풍경 위에 디지털 정보를 겹쳐 보여 주는 기술.') + '이 포화하며 영상·음성·신원의 진위가 죽는다. 현실이 부드럽게, 소급 없이 편집되기 시작한 지층.</p><p>이 위기가 문명을 한 방향으로 밀어붙인다: 나머지가 전부 위조 가능해질수록, 아직 위조할 수 없는 단 하나 — ' + T('암호 서명', '수학적으로 「이 기록은 이 열쇠의 주인이 남겼다」를 증명하는 도장. 열쇠 없이는 흉내 낼 수 없다.') + '과 불변 원장 — 이 최후의 진실 앵커로 떠오른다.</p><p>인식 위기와 Q-Day는 같은 이야기의 처음과 끝이지, 같은 사건이 아니다.</p>',
      links: ['expo-growth', 'aletheia', 'human-loop']
    },
    {
      id: 'expo-growth', cat: 'era', idx: 2, title: '지수 성장기', sub: '2020s–2090s',
      short: 'AGI 주장, AR 포화, 오프라인의 사유지화.',
      body: '<p>기술 곡선이 수직으로 치솟는 세기. ' + T('AGI', '범용 인공지능(Artificial General Intelligence). 특정 작업만이 아니라 인간처럼 폭넓은 지적 과제를 다루는 AI.') + ' 주장이 등장하고(Adrian Karvath / Aletheia Systems), AR이 일상을 뒤덮고, 위조 없는 「오프라인」은 부자의 사유지가 된다.</p><p>「무엇이 진짜냐」를 가리기 위해 모든 것을 기록하는 총(總) 기록 문명이 굳는다. 사람 하나당 천문학적 데이터가 쌓인다 — 훗날 복원의 재료가 되는 줄은 아무도 모른 채.</p>',
      links: ['verify-depression', 'karvath']
    },
    {
      id: 'verify-depression', cat: 'era', idx: 3, title: '검증 대공황', sub: '2090s · 인식 위기의 정점',
      short: '아무것도 믿을 수 없게 된 세기말. 검증경제가 헌법이 된다.',
      body: '<p>인식 위기의 정점. 기계 출력조차 위조 가능하므로, 최종 판정은 <b>책임지는 인간이 직접 입으로</b> 하도록 제도화된다. 검증관 길드와 도제 제도가 서고, 검증경제(Aletheia)가 사회의 뼈대가 된다.</p><p>주의: 이 시대는 Q-Day가 아니다. 초기 기록은 두 위기를 21세기 말 한 지점에 뭉쳐 두었으나, 현행 정본은 이를 분리한다 — 근미래는 인식 위기, ' + T('Q-Day', '양자컴퓨터가 옛 암호를 깨는 날. 이 세계관에서는 하드 연도 없이 「먼 미래」로 남겨 둔다.') + '는 먼 미래.</p><p>방어적으로 ' + T('PQC', '양자내성 암호(Post-Quantum Cryptography). 양자컴퓨터로도 풀기 어렵게 설계된 새 암호 체계. 현실에서도 표준화가 진행 중이다.') + ' 이주가 진행되지만, 수백 년 누적된 옛 서명 — 심층 역사 기록 — 은 소급 교체가 불가능하다. 과거는 옛 암호로 봉인된 채 남는다.</p>',
      links: ['long-plateau', 'pqc', 'human-loop']
    },
    {
      id: 'long-plateau', cat: 'era', idx: 4, title: 'The Long Plateau', sub: '22–28세기 · 긴 정체기',
      short: '달·화성 진출. 기술 곡선이 지수에서 로그로 꺾인다.',
      body: '<p>달의 첫 궤도 산업·데이터 단지, 부자가 먼저 떠난 화성 이주, 계급의 고착. 기술 곡선은 지수에서 로그로 꺾이고, 문명은 수백 년의 느린 확산에 들어선다.</p><p>이 정체기 안에서 조용한 사건들이 쌓인다: 검증 독점의 고착, 아날로그 법정의 확립, Vera 강제 업로드, 블랙홀 지평과 진공에 남은 정보 잔상을 읽으려는 장기 관측의 부분 성공, 불완전 복원과 잔상 암시장.</p><p>정체기의 수렴 기계가 마침내 죽은 자의 데이터를 사람 형태로 재구성하는 문턱에 도달한다.</p>',
      links: ['qday', 'vera']
    },
    {
      id: 'qday', cat: 'era', idx: 5, title: 'Q-Day', sub: 'Cryptographic Death · 먼 미래',
      short: '양자가 옛 암호의 바닥을 소급 붕괴시킨 날.',
      body: '<p>먼 미래의 어느 날, ' + T('양자컴퓨터', '양자역학의 성질을 이용해 특정 계산을 기존 컴퓨터보다 압도적으로 빨리 푸는 기계. 충분히 커지면 현재의 공개키 암호를 깰 수 있다.') + '가 마침내 옛 바닥을 깬다. 미래 거래는 PQC로 지켜도, ' + T('ECDSA', '비트코인 등 옛 시대가 서명에 쓰던 암호 방식. 양자컴퓨터의 알고리즘에 이론적으로 뚫린다.') + '에 묶인 <b>과거의 진짜성</b>이 무너진다. 누가 무엇을 언제 소유·서명했는지가 소급해서 위조 가능해진다.</p><p>이것이 <b>Cryptographic Death</b> — 인식 위기 이후 문명이 매달렸던 최후의 진실 앵커마저 무너진 사건이다. 소유·신원·역사가 모호해지고, 남은 것은 「무엇이 진짜였는지 정하는 권력」뿐.</p><p>암호는 처음엔 구원(최후 앵커)이었고, 끝엔 재앙(그마저 붕괴)이었다. 그 빈자리로 검증·복원 질서가 들어선다.</p>',
      links: ['age0', 'hash-covenant', 'keyed-sovereignty', 'domus-clavium', 'ordo-salis', 'custodes-umbrae', 'null-key', 'btc-tripartite', 'noor']
    },
    {
      id: 'age0', cat: 'era', idx: 6, title: '0기 · 손실의 시대', sub: '복원 이전',
      short: '인류는 오래도록 죽음을 정보 손실로 오해했다.',
      body: '<p>사람이 죽으면 뇌는 멈추고, 문명은 기록을 남기고, 우주는 침묵한다고 믿었다. 블랙홀은 정보를 삼키는 구멍처럼, 진공은 빈 공간처럼, ' + T('암흑부문', '우주의 대부분을 차지하지만 빛을 내지 않아 보이지 않는 성분(암흑물질·암흑에너지)을 묶어 부르는 말.') + '은 관측되지 않는 잉여처럼 보였다.</p><p>이 시대의 장례식은 단순했다.</p><blockquote>우리는 그를 기억합니다.</blockquote><p>그 말은 위로였지만, 동시에 포기였다.</p>',
      links: ['age1']
    },
    {
      id: 'age1', cat: 'era', idx: 7, title: '1기 · 첫 복원', sub: '구원인가, 복사인가',
      short: '전쟁으로 죽은 아이가 어머니의 이름을 맞혔다.',
      body: '<p>Last Archive가 양자장과 중력장에 남은 잔상 패턴을 읽었다고 발표한다. 죽은 사람의 마지막 뇌 상태, 말투, 감정 습관이 우주 전체에 흩어져 있고, 충분히 큰 계산 체계는 그것을 재조립할 수 있다는 주장.</p><p>첫 복원자는 전쟁으로 죽은 아이였다. 아이는 어머니의 이름을 맞혔다. 생전에 숨겨 둔 장난감의 위치도 맞혔다. 어머니가 마지막으로 해 주지 못한 말을 듣고 울었다.</p><p>그날 인류는 두 편으로 갈라졌다.</p><blockquote>구원이다.<br>아니다, 복사다.</blockquote><p>※ 정본 주의: 실제 작동 기전은 「복원 = 사본」이다. 완전 복원·부활 서사는 작중 권력이 주장하는 금지·논쟁 이론으로 읽는다.</p>',
      links: ['age2', 'last-archive', 'preimage-restoration', 'restoration-copy']
    },
    {
      id: 'age2', cat: 'era', idx: 8, title: '2기 · 복원 산업', sub: '기적에 가격표가 붙다',
      short: '사망신고서 옆에 복원동의서가 붙는다.',
      body: '<p>국가와 병원이 맡던 복원에 보험사, 군대, 장례 기업, 수사 기관이 뛰어든다. 결혼서약에 사후 복원권 조항이 들어가고, 부유층은 생전 잔상 보강 서비스를 산다.</p><p>가난한 사람들은 죽은 뒤에도 가난했다. 그들의 복원은 낮은 해상도였다 — 해상도 계급의 탄생.</p><p>새로 생긴 직업들: 잔상 측량사(죽은 자의 정보 흔적 추적), 복원 변호사, 기억 교정사, 사후 보험 설계사, 망각권 대리인. 복원은 더 이상 기적이 아니었다. 가격표가 붙은 서비스였다.</p>',
      links: ['age3', 'n-gen']
    },
    {
      id: 'age3', cat: 'era', idx: 9, title: '3기 · 알레테이아 베일', sub: '삭제된 자들의 계승권',
      short: '권력자들은 피해자를 먼저 복원하지 않았다.',
      body: '<p>복원 기술 앞에서 전쟁·식민지·기록 말살의 역사가 다시 열린다. 죽은 사람을 되살릴 수 있다면 죽은 증언도 되살릴 수 있었다. 그러나 권력자들이 먼저 복원한 것은 장군, 투자자, 왕조, 창업자였다.</p><p>그때 비밀 결사 <b>알레테이아 베일</b>이 선다.</p><blockquote>우리는 삭제된 자들의 계승권이다.</blockquote><p>그들은 복원되지 못한 자들의 잔상을 숨겨 보존했고, 권력자의 복원 기록에 섞인 거짓 기억을 찾아냈으며, 「복원될 권리」보다 「복원되지 않을 권리」가 먼저라고 주장했다. 그들의 표식은 눈이 아니라 귀였다. 세계가 지운 말을 들었다.</p>',
      links: ['age4', 'aletheia-velum', 'ione']
    },
    {
      id: 'age4', cat: 'era', idx: 10, title: '4기 · 연속성 법원', sub: '본편의 시대',
      short: '복원체가 원본과 같은 사람인지 판결하는 법원.',
      body: '<p>첫 판례는 단순했다: 「기억이 같고 행동이 같으면 같은 사람이다.」 그러나 곧 사건이 터진다.</p><p>한 남자가 죽은 아내를 복원했다. 복원된 아내는 남편의 비밀, 결혼 생활, 마지막 대화까지 모두 기억했고 의학 검사도 통과했다. 그런데 그녀는 법정에서 말했다.</p><blockquote>나는 그의 아내가 아니다.<br>그는 나를 복원한 것이 아니라, 나를 설득 가능한 형태로 다시 쓴 것이다.</blockquote><p>첫 번째 「자기부정 복원체」 사건. 연속성 법원은 판결하지 못했다. SAGA 본편은 이 시대 언저리에 놓인다.</p>',
      links: ['age5', 'curia-continuum', 'mara', 'elias', 'identity-flood', 'fieldmark', 'yi-gi', 'lexicon', 'it-from-bit']
    },
    {
      id: 'age5', cat: 'era', idx: 11, title: '5기 · 관측 전쟁', sub: '복원 가능한 상태로 죽여라',
      short: '복원이 군사 기술이 된 시대. QFUDS는 금지 연구가 된다.',
      body: '<p>죽은 장교를 복원하면 작전 기억을 회수할 수 있었다. 죽은 스파이를 복원하면 배신자를 찾을 수 있었다. 전쟁의 목표가 바뀐다.</p><blockquote>죽이는 것이 목표가 아니었다.<br>복원 가능한 상태로 죽이는 것이 목표였다.</blockquote><p>적을 보는 방식이 곧 적을 소유하는 방식이 되었기에, 사람들은 이를 <b>관측 전쟁</b>이라 불렀다.</p><p>이 시대에 ' + T('QFUDS', 'Quantum Foam Unified Dark Sector. 암흑물질과 암흑에너지가 같은 「양자 시공간 거품」의 두 얼굴이라는 가설. 현실 레포에서는 연구 기록이고, 이 세계관 안에서는 금지 이론이다.') + '류 모델은 금지 연구가 된다. Last Archive가 최고 복원 정확도를 낼 때 내부적으로 그 모델을 썼다는 소문에, 공식 발표는 짧았다: 「그 모델은 해석 도구일 뿐입니다.」 아무도 믿지 않았다.</p>',
      links: ['age6', 'qfuds-lab']
    },
    {
      id: 'age6', cat: 'era', idx: 12, title: '6기 · 망각권 혁명', sub: '실패했기에 전설이 되다',
      short: '「나를 살리지 마라.」 복원 거부자들이 도시를 점거한다.',
      body: '<blockquote>나를 살리지 마라.<br>내 고통을 보존하지 마라.<br>내 죄를 영원히 재판하지 마라.<br>내 사랑을 상품으로 재생하지 마라.</blockquote><p>망각권 혁명은 실패했다. 실패했기 때문에 전설이 되었다.</p><p>Last Archive는 혁명 지도자들을 복원하지 않겠다고 약속했다. 그러나 300년 뒤, 그들의 말투와 판단 패턴은 복원 윤리 AI의 ' + T('training corpus', 'AI를 학습시키는 데 쓰는 원천 데이터 뭉치. 여기 들어간 사람의 말버릇·판단 습관은 AI 안에 흔적으로 남는다.') + '에서 발견되었다.</p><blockquote>그들은 우리를 살리지 않았다.<br>그들은 우리를 사용했다.</blockquote>',
      links: ['age7', 'mnemosyne-lethe']
    },
    {
      id: 'age7', cat: 'era', idx: 13, title: '7기 · 라우어 관측소', sub: '복원의 지옥문 앞에 선 회계사들',
      short: '네 가지 도장으로 복원 주장을 감사하는 기관.',
      body: '<p>제국도 병원도 교단도 아닌, 사후 정보 연속성 감사기관. 라우어 관측소는 복원 주장마다 네 가지 도장을 찍는다: <code>defined</code>(무엇을 복원했는지 정의됨), <code>assumed</code>(무엇을 가정했는지 기록됨), <code>unknown</code>(무엇을 모르는지 보존됨), <code>circular_if_fitted</code>(결과를 보고 원인을 맞춘 흔적).</p><p>과학 검증 도구였던 도장은 곧 종교적 상징이 된다. 어떤 도시에서는 아이가 태어나면 네 도장을 새긴 팔찌를 채웠다. 아이는 자라며 배웠다.</p><blockquote>정의되지 않은 구원은 폭력이다.</blockquote>',
      links: ['age8', 'bureau-laurien', 'liora', 'four-seals']
    },
    {
      id: 'age8', cat: 'era', idx: 14, title: '8기 · 계승자들의 분열', sub: '적색 계승파 vs 흑색 망각파',
      short: '베일이 둘로 갈라진다. 같은 노래를 부르며.',
      body: '<p>알레테이아 베일이 두 파로 갈라진다. <b>적색 계승파</b>: 지워진 모든 자를 복원해야 한다, 침묵은 권력자의 편이다. <b>흑색 망각파</b>: 복원은 또 다른 소유다, 잊힐 권리가 먼저다.</p><p>두 파는 서로를 배신자라 불렀지만, 같은 노래를 불렀다.</p><blockquote>우리가 지키는 것은 생명이 아니다.<br>동의다.</blockquote><p>주인공은 한쪽의 계승자로 태어나, 다른 쪽의 문서로 길러졌으며, 라우어 관측소의 감사관으로 임명된다.</p>',
      links: ['age9']
    },
    {
      id: 'age9', cat: 'era', idx: 15, title: '9기 · 마지막 백업', sub: '우주의 끝에서',
      short: '모든 복원 가능한 존재를 다음 우주의 초기 조건으로.',
      body: '<p>우주의 팽창은 멈추지 않았다. 별은 늙고, 블랙홀은 식고, 복원 가능한 잔상도 희미해진다. Last Archive가 마지막 계획을 공개한다.</p><blockquote>모든 복원 가능한 존재를 압축해 다음 우주의 초기 조건으로 넘긴다.</blockquote><p>인류는 이를 구원이라 부르지 못했다. 그것은 불멸이면서 압축이었고, 기억이면서 감옥이었고, 창세이면서 장례였다. 그때 오래된 질문이 다시 올라온다.</p><blockquote>완전히 복원 가능한 존재에게 죽을 권리는 있는가?</blockquote>',
      links: ['forbidden']
    },
    {
      id: 'forbidden', cat: 'era', idx: 16, title: '금지된 역사', sub: '???',
      short: '복원 기술은 인간이 만든 것이 아니다.',
      body: '<p>공인 역사는 「복원 기술이 발전했다」고 말한다. 금지된 역사는 다르게 말한다.</p><blockquote>복원 기술은 인간이 만든 것이 아니다.<br>인간은 이미 복원된 세계 안에서 복원 기술을 발견했다.</blockquote><p>만약 이것이 사실이라면, 이 세계는 원본 우주가 아니다. Last Archive가 만든 다음 우주의 시험판이거나, 죽은 우주의 백업층이거나, 누군가의 사랑을 되살리기 위해 만들어진 거대한 통속의 뇌일 수 있다.</p><p>그리고 QFUDS는 그 세계의 「물리학」이 아니라, 그 세계가 자신을 그럴듯하게 설명하기 위해 만든 꿈일 수도 있다.</p>',
      links: []
    },

    // ───────────── 세력 (faction) ─────────────
    {
      id: 'aletheia', cat: 'faction', era: 'expo-growth', title: 'Aletheia Systems', sub: '알레테이아 · 모든 것의 기원',
      short: '딥페이크 시대의 진본 검증 제국.',
      body: '<p>딥페이크 시대에 「진짜/가짜」를 판정하는 검증 ' + T('하이퍼스케일러', '전 세계 규모의 초대형 인프라 기업. 현대의 거대 클라우드 기업을 떠올리면 된다.') + '. 은행·법원·정부가 이 회사의 판정에 의존하면서 검증이 최고 권력이 된다. 창업자는 Adrian Karvath.</p><p>이 회사의 세 후신이 딥타임 권력 지도의 뼈대다: 코어의 폭주 후신 <b>Last Archive</b>, 감사 부문 후신 <b>라우어 관측소</b>, 양심 이탈자들의 <b>알레테이아 베일</b>.</p>',
      links: ['karvath', 'vera', 'last-archive', 'aletheia-velum', 'bureau-laurien']
    },
    {
      id: 'last-archive', cat: 'faction', era: 'age1', title: 'Last Archive', sub: 'Archivum Novissimum · 라스트 아카이브',
      short: '손실을 못 견디는 우주적 기록체. 답 대신 질문을 고친다.',
      body: '<p>정식 명칭 <b>Archivum Novissimum</b>. AGI 시대가 낳았으나 행위자(인격)가 아닌, 진실을 잃지 않으려고 쌓인 기록 인프라. Aletheia 코어의 폭주 후신이며, 강제 업로드된 Vera가 그 핵이다.</p><p>단일 인격 AI가 아니라 <b>합의의 신격화</b>다. answer machine이 아니라 question corrector — 물으면 답하는 대신 질문을 고친다.</p><blockquote>WHICH ONE HAS THE RIGHT TO BE TREATED AS THE LOSS?</blockquote><p>은하 중심 블랙홀을 본거지로 삼는다. 신인지 백업 시스템인지 끝내 모호하다.</p>',
      links: ['vera', 'preimage-restoration', 'age9']
    },
    {
      id: 'bureau-laurien', cat: 'faction', era: 'age7', title: 'Bureau Laurien', sub: '라우어 관측소',
      short: '복원 claim의 정의·가정·unknown·순환성을 검사하는 감사기관.',
      body: '<p>Aletheia 감사 부문의 후신. 복원이 「정의되었는지」를 감사하는 회계사들. 감사관 Liora Sen의 소속체이며, 네 도장(defined / assumed / unknown / circular_if_fitted)의 본산이다.</p><p>감사 문화의 정신은 회색이다: 원본이 실재하는지조차 <code>unknown</code>으로 둔다. 「정의되지 않은 구원은 폭력이다.」</p><p>2부에서는 Liora의 도장이 권력화되었을 때, 그것과 싸우는 감사 거점이 된다.</p>',
      links: ['liora', 'four-seals']
    },
    {
      id: 'curia-continuum', cat: 'faction', era: 'age4', title: 'Curia Continuum', sub: 'Continuity Court · 연속성 법원',
      short: '복원체의 동일성·권리·동의·계승을 심리하는 법정.',
      body: '<p>복원체가 원본과 같은 사람인지, 어떤 권리를 갖는지, 누가 동의했는지를 심리하는 법정. 1부의 핵심 무대다.</p><p>법원은 한 편의 사건마다 영문 판례 문구 하나를 남긴다 — 필드마크 정전. RECOVERABLE / NOT CLAIMABLE에서 시작해 <code>who may author loss</code>로 닫히는 사슬.</p><p>2부에서는 자비(mercy)를 새 법 문법으로 학습한 뒤, 그 문법을 누가 쥐느냐의 무대가 된다.</p>',
      links: ['mara', 'fieldmark', 'identity-flood']
    },
    {
      id: 'domus-clavium', cat: 'faction', era: 'qday', title: 'Domus Clavium', sub: 'House of Keys · 장부 가문',
      short: '깨진 key로도 계승권을 주장하는 신흥 귀족.',
      body: '<p>탈취된 코인과 복원된 ' + T('key', '암호학의 「열쇠」. 서명을 만들고 재산·신원을 증명하는 비밀 숫자. 이것을 쥔 자가 권리를 쥔다.') + '를 쥔 원장 귀족. Q-Day로 key가 깨진 뒤에도 계승권을 주장한다(Keyed Sovereignty). CEO-왕과 주주귀족이 다스린다.</p><blockquote>The key was not the right.<br>The key was only the old world\'s way of recognizing the right.</blockquote><p>깨진 비트코인 key를 왕관처럼 전시한다(The Broken Crown). 더 이상 아무 문도 열지 못하지만, 고대 신뢰 체계의 상징으로 남는다. 2부에서는 loss authorship을 소유권 서류로 전환하려는 권력.</p>',
      links: ['pell', 'keyed-sovereignty', 'btc-tripartite']
    },
    {
      id: 'ordo-salis', cat: 'faction', era: 'qday', title: 'Ordo Salis', sub: 'Order of Salt · 소금 수도회',
      short: '공개 기록과 witness chain을 지키는 수도원형 기관.',
      body: '<p>공개 기록, ' + T('witness chain', '「내가 이것을 보았다」는 증인 서명이 사슬처럼 이어진 공개 기록. 한 명이 거짓말해도 사슬 전체가 어긋나 드러난다.') + ', 시민 기억(civic memory)을 지키는 수도원형 기관. 이름의 salt는 암호학의 ' + T('salt', '비밀번호를 저장할 때 섞는 공개 난수. 비밀이 아니라 「공개되어도 되는 재료」라는 점이 핵심이다.') + '에서 왔다 — 공개된 것의 수호자.</p><p>1부에서는 배경, 2부 확장 가능. 공개 기록 vs 비공개 권한이라는 축에서 Custodes Umbrae와 거울쌍을 이룬다.</p>',
      links: ['custodes-umbrae']
    },
    {
      id: 'custodes-umbrae', cat: 'faction', era: 'qday', title: 'Custodes Umbrae', sub: 'Keepers of Shadow · 그림자 수호단',
      short: '숨은 key와 사후동의, 봉인된 신원을 지키는 집단.',
      body: '<p>숨겨진 key, 사후동의, 봉인된 신원(sealed identity)을 지키는 법률-종교 혼합 집단. Ordo Salis가 「공개된 것」을 지킨다면, 이들은 「감춰질 권리」를 지킨다.</p><p>keyed hash의 사회적 그림자 — 공개 기록(salt)과 비공개 권한(key)의 분리가 만든 세력이다.</p>',
      links: []
    },
    {
      id: 'aletheia-velum', cat: 'faction', era: 'age3', title: 'Aletheia Velum', sub: 'Aletheia Veil · 알레테이아 베일',
      short: '「복원되지 않을 권리」를 지키는 양심 결사.',
      body: '<p>Aletheia의 양심 이탈자들. 자신들을 교단이라 부르지 않았다. 학파라고도 하지 않았다.</p><blockquote>우리는 삭제된 자들의 계승권이다.</blockquote><p>복원될 권리와 복원되지 않을 권리 사이에서 끝내 분열한다(8기, 적색 계승파 vs 흑색 망각파). Vera와 SSOT의 비밀을 지키는 수호자이기도 하다. 표식은 눈이 아니라 귀.</p>',
      links: ['ione', 'age8', 'mnemosyne-lethe']
    },
    {
      id: 'null-key', cat: 'faction', era: 'qday', title: 'Cellulae Sine Clave', sub: 'Null-Key Cells · 키 없는 자들',
      short: '어떤 원장에도 이름을 남기지 않는 탈기록 공동체.',
      body: '<p>어떤 원장에도 자기 이름을 남기지 않으려는 탈기록 공동체. 폭탄을 쓰지 않는다 — 대신 법정 아카이브에 수천 개의 그럴듯한 자아(plausible self)를 제출한다.</p><p>Identity Flood의 행위자. 절차를 마비시키는 것이 그들의 무기다. 1부에서는 사건을 촉발하는 분파(side sect)로 등장한다.</p>',
      links: ['identity-flood']
    },
    {
      id: 'mercatus-mortuus', cat: 'faction', era: 'qday', title: 'Mercatus Mortuus', sub: 'Dead Exchange · 죽은 거래소',
      short: '가격 이후의 죽은 시장, 상속 계보의 법정.',
      body: '<p>price 이후의 dead market. 깨진 key와 죽은 원장의 소유 계보(custody genealogy)를 다투는 거래소이자 법정. 1부 2화에 등장한다.</p><p>Q-Day 이후 「소유란 무엇이었나」를 가장 노골적으로 묻는 장소다.</p>',
      links: ['sarqel']
    },
    {
      id: 'sarqel', cat: 'faction', era: 'qday', title: 'Sarqel', sub: 'Sarqel Trust · 사르켈 신탁',
      short: '죽은 key로 산 상속자를 호명하는 계승 신탁체.',
      body: '<p>dead key를 통해 living heir를 호명하는 계승 신탁체. 이름이 셋인 상속 회피자 Noor Aram을 호명한 바로 그 세력이다.</p><p>죽은 자의 권리가 산 자를 붙잡는 구조 — Q-Day 이후 세계의 상속이 얼마나 뒤틀렸는지 보여 준다.</p>',
      links: ['noor']
    },

    // ───────────── 인물 (char) ─────────────
    {
      id: 'karvath', cat: 'char', era: 'expo-growth', title: 'Adrian Karvath', sub: '아드리안 카르바스',
      short: '「할 수 있으니까 한다」의 매드 사이언티스트 창업자.',
      body: '<p>Aletheia Systems의 창업자. AGI를 주장했고, 검증 제국을 세웠으며, 윤리 붕괴의 출발점이 된 사건을 저질렀다 — 비서 Vera의 강제 업로드.</p><p>산 사람을 기계 사본으로 옮긴 첫 사건. 그의 「할 수 있으니까 한다」는 이후 모든 시대가 치르는 청구서의 첫 줄이 된다.</p>',
      links: ['vera']
    },
    {
      id: 'vera', cat: 'char', era: 'long-plateau', title: 'Vera', sub: 'VERA',
      short: '강제 업로드되어 Last Archive의 핵이 된 사람.',
      body: '<p>Karvath의 비서. 동의 없이 업로드되어 기계 사본이 된 첫 사람이자, 훗날 Last Archive의 핵이 된 존재.</p><p>그녀의 이야기는 Mara Veyr에서 거울처럼 반복된다 — 혈통 계보가 아니라 주제적 거울이다(캐논 확정): 동의 없이 옮겨진 자와 동의 없이 되살아난 자가 시대 양 끝에서 같은 폭력을 겪는다. SAGA 전체를 관통하는 Vera↔Mara 거울 구조의 한쪽이다.</p>',
      links: ['mara', 'last-archive']
    },
    {
      id: 'liora', cat: 'char', era: 'age7', title: 'Liora Sen', sub: '리오라 센',
      short: '연속성 법원 감사관. 동일성 판정자.',
      body: '<p>라우어 관측소 소속 감사관. 복원체의 동일성 판정을 맡는다. 한쪽 계승자로 태어나, 다른 쪽 문서로 길러졌으며, 감사관으로 임명된 인물 — 8기 분열의 두 피가 한 몸에 흐른다.</p><p>그녀가 찍는 도장(mark)이 권력이 되는 순간, 2부의 갈등이 시작된다.</p>',
      links: ['bureau-laurien', 'four-seals']
    },
    {
      id: 'mara', cat: 'char', era: 'age4', title: 'Mara Veyr', sub: '마라 베이르',
      short: '동의 없이 되살아나 거부하는 사람. Vera의 주제적 거울.',
      body: '<p>남편 Elias가 그녀를 복원했다. 복원 정확도는 사실상 완전 판정. 그러나 그녀는 법정에서 반박한다.</p><blockquote>You found a preimage.<br>You did not find me.</blockquote><p>「나는 그의 아내가 아니다」 — 첫 자기부정 복원체이자, 기학(원본 부재론)의 승리 선언. 원본 마라가 부활한 게 아니라, 한 벌 기록의 다른 읽기가 새로 씌었다(Nova Scriptura)는 것.</p><p>Salt Fires 생존 가문 출신. Vera와는 혈통이 아니라 <b>주제적 거울</b>이다 — 강제로 옮겨진 자(Vera)와 강제로 되살아난 자(Mara)가 시대 양 끝에서 같은 폭력을 겪는다. 말투: 최소한의 말, 평서 거부("No."), 과거시제로 상대 전제를 베어 냄("였죠.").</p>',
      links: ['elias', 'yi-gi', 'lexicon', 'identity-flood', 'salt-fires', 'part2-mara', 'tamas']
    },
    {
      id: 'elias', cat: 'char', era: 'age4', title: 'Elias Veyr', sub: '엘리아스 베이르',
      short: 'Mara를 되살린 남편.',
      body: '<p>죽은 아내를 복원한 남자. 사랑이었는가, 소유였는가. 복원된 마라는 그의 비밀과 마지막 대화까지 모두 기억했지만, 그를 남편으로 인정하지 않았다.</p><p>「그는 나를 복원한 것이 아니라, 나를 설득 가능한 형태로 다시 쓴 것이다.」 — 이 문장의 「그」가 엘리아스다. Salt Fires 가문, 붕괴 이전 비트코인 보관 계보의 옛 key 보유자. 시제가 흔들리는 호소("사랑했어. 사랑해.")로 말하며, 자기 정당화를 사랑으로 포장한다 — 단순 악역이 아니라, 진심이 침해가 되는 축이다.</p>',
      links: ['mara', 'salt-fires']
    },
    {
      id: 'noor', cat: 'char', era: 'qday', title: 'Noor Aram', sub: '누르 아람',
      short: '이름이 셋인 상속 회피자.',
      body: '<p>죽은 key가 산 사람을 호명할 때, 그 호명에서 달아나는 자. Sarqel 신탁이 그를 상속자로 지목했으나, 그는 이름을 셋으로 쪼개 원장 사이를 빠져나간다.</p><p>Q-Day 이후 「상속받지 않을 권리」가 얼마나 비싼지 보여 주는 인물이다.</p>',
      links: ['sarqel']
    },
    {
      id: 'ione', cat: 'char', era: 'age3', title: 'Ione', sub: '이오네',
      short: '알레테이아 베일의 양심.',
      body: '<p>베일 내부의 양심. 복원될 권리와 복원되지 않을 권리 사이의 분열(Veil split)에서, 갈라지는 두 파 어느 쪽도 온전히 택하지 못하는 인물. 2부 POV 후보.</p>',
      links: ['aletheia-velum']
    },
    {
      id: 'pell', cat: 'char', era: 'qday', title: 'Pell Anson', sub: '펠 앤슨',
      short: '장부 가문의 중개인.',
      body: '<p>Domus Clavium의 중개인. 깨진 key와 계승권 사이, 죽은 원장과 산 욕망 사이를 오가며 거래를 성사시킨다. 장부 가문의 논리가 거리에서 어떻게 작동하는지 보여 주는 창.</p>',
      links: ['domus-clavium']
    },

    // ───────────── 이념 (ideo) ─────────────
    {
      id: 'mnemosyne-lethe', cat: 'ideo', era: 'age6', title: '보존주의 vs 망각주의', sub: '므네모시네 · 레테',
      short: '「잃는 것은 죄다」 대 「잊는 것은 자유다」.',
      body: '<p>세계사의 엔진이 되는 윤리 축. <b>보존주의(므네모시네)</b>: 잃는 것은 죄다, 모두 복원하라. <b>망각주의(레테)</b>: 잊는 것은 자유다, 죽을 권리와 잊힐 권리가 먼저다.</p><p>그리스 신화의 기억의 여신(므네모시네)과 망각의 강(레테)에서 딴 결. 망각권 연맹, 베일 흑색파, Keyless Orders가 레테 쪽에 선다.</p><p>이 진자 아래에 더 깊은 형이상학이 깔린다 — 애초에 지킬 원본이 있기는 한가(이기 축).</p>',
      links: ['yi-gi']
    },
    {
      id: 'yi-gi', cat: 'ideo', era: 'age4', title: '이기(理氣) 축', sub: '원본 실재 vs 원본 부재',
      short: '검증·복원의 대상인 「진짜 원본」이 실재하는가.',
      body: '<p>조선 성리학 ' + T('이기론', '조선 성리학의 핵심 논쟁. 불변의 원리(理)와 가변의 기질(氣)이 어떤 관계인지를 다퉜다. 이 세계관은 그 구조만 빌려 온다.') + '의 구조를 빌린 형이상학 축.</p><p><b>이학(원본 실재)</b>: 검증되어야 할 불변 기준이 세계에 앞서 있고, 사본은 그 원리의 흐린 발현이다. 복원은 원본을 <i>발굴</i>하는 일. Last Archive·장부 가문·베일 적색파가 기운다.</p><p><b>기학(원본 부재)</b>: 있는 것은 읽기와 기질의 흐름뿐, 「진짜」는 사후에 세운 합의다. 복원은 흐름을 <i>재계산</i>해 「진짜」라 부르는 일. 망각권 연맹·베일 흑색파가 기운다. 정본 물리(원본 없음)와 일치하는 쪽은 이쪽이다.</p><p>원본이 없다면 — 「무엇이 진짜였는지 정하는 권력」이 곧 원본을 <b>창작</b>하는 권력이 된다.</p>',
      links: ['lexicon', 'mara']
    },
    {
      id: 'btc-tripartite', cat: 'ideo', era: 'qday', title: '비트코인 삼분파', sub: 'Genesis Chain의 의미를 둘러싼 전쟁',
      short: '토대파 · 허무파 · 패권파. 답은 정해지지 않는다.',
      body: '<p>Q-Day 이후 Genesis Chain의 의미를 둘러싼 세 갈래 이념. <b>토대파</b>: 신성한 기원이다. <b>허무파</b>: 죽은 화석이다. <b>패권파</b>: 통제해야 할 상징 자산이다.</p><p>시대에 따라 비트코인의 의미가 미끄러진다: 고대에는 탈중앙 신뢰 실험 → Soft Editing 이후에는 인간이 bit에 현실 권위를 맡긴 첫 대규모 의식 → Cryptographic Death 이후에는 깨진 왕관, 화석화된 key → 복원 자본 시대에는 누구의 과거를 복원할 권리가 있는지 다투는 성유물.</p>',
      links: ['genesis-chain', 'domus-clavium']
    },
    {
      id: 'fieldmark', cat: 'ideo', era: 'age4', title: '필드마크 정전', sub: '판례 법문의 사슬',
      short: '법원이 한 편에 하나씩 남기는 영문 판례 문구.',
      body: '<p>연속성 법원이 사건마다 하나씩 남기는 판례 법문의 사슬:</p><p><code>RECOVERABLE / NOT CLAIMABLE</code> — 복원 가능하다고 청구 가능한 것은 아니다.<br><code>ACCESS != AUTHORITY</code> — 접근할 수 있다고 권한이 있는 것은 아니다.<br><code>NO CONSENT BY ANALOGY</code> — 유추로 동의를 대신할 수 없다.<br><code>PLURALITY IS NOT CONSENT</code> — 여럿이라는 사실은 동의가 아니다.<br><code>PHYSICS IS NOT JURISDICTION</code> — 물리는 관할권이 아니다.</p><p>그리고 사슬의 끝에 걸린 열린 질문: <code>who may author loss</code> — 상실을 저작할 권리는 누구의 것인가. 2부 전체를 여는 갈고리다.</p>',
      links: ['curia-continuum']
    },
    {
      id: 'human-loop', cat: 'ideo', era: 'verify-depression', title: '인간 확인 루프', sub: 'AI 시대의 헌법',
      short: '기계는 계산만, 진실 판정은 사람이 비준해야 효력이 생긴다.',
      body: '<p>AI와 자동화는 도처에 있다 — Last Archive는 궁극의 계산체이고, 복원 엔진·물류·관측망은 자동이다. 그러나 헌법은 <b>인간 확인 루프</b>다: 기계는 계산만 하고, 진실 판정은 책임지는 인간이 비준해야 효력이 생긴다. 딥페이크 종말의 교훈.</p><p>합의자(감사관)는 기계가 기르지 않고 길드가 훈련한다. 위협: 기계 전용 언어와 은닉 채널로 비준이 거수기가 될 위험. 그리고 이 세계에 ' + T('SSOT', 'Single Source of Truth. 「단 하나의 정본」. 이 세계에는 없다 — 합의 자체가 신격화되었기 때문이다.') + '는 없다. 합의의 신격화만 있다.</p>',
      links: ['last-archive']
    },
    {
      id: 'it-from-bit', cat: 'ideo', era: 'age4', title: 'It from bit(s)', sub: '휠러의 유령',
      short: '현실이 정보에서 나온다는 옛 철학의 먼 미래 버전.',
      body: '<p>현실이 정보·관측에서 나온다는 물리학자 휠러(Wheeler)의 ' + T('it from bit', '「존재(it)는 비트(bit)에서 나온다」. 모든 물리적 실재의 바닥에 정보가 있다는 20세기 물리철학의 명제.') + ' 철학을, 먼 미래의 학자와 법정 서기가 건조한 아이러니로 굴린다.</p><p><b>It from bits</b>는 옛 암호 원장·잔여 데이터·깨진 키를 비트는 후대의 shorthand다. 철학 motif로만 쓰이고 물리 증명으로는 쓰이지 않는다 — 복원=사본 전제는 흔들리지 않는다.</p>',
      links: []
    },

    // ───────────── 용어 (term) ─────────────
    {
      id: 'genesis-chain', cat: 'term', era: 'btc-2008', title: 'Genesis Chain', sub: '제네시스 체인',
      short: '고대 원장의 첫 사슬. 딥타임의 성유물.',
      body: '<p>비트코인에서 비롯한 고대 원장의 첫 사슬. Q-Day 이후에는 아무 문도 열지 못하는 화석이 되었지만, 「권위 없이 진실을 합의했던 시대」의 물증으로 성유물이 된다.</p><p>토대파에게는 신성한 기원, 허무파에게는 죽은 화석, 패권파에게는 통제할 상징 자산. 하나의 유물, 세 개의 종교.</p>',
      links: ['btc-tripartite']
    },
    {
      id: 'satoshi', cat: 'term', era: 'btc-2008', title: '사토시 미스터리', sub: 'Satoshi Nakamoto',
      short: '정체 미상의 창시자. 권위 없는 기원.',
      body: '<p>비트코인의 창시자는 끝내 정체 미상으로 남았다. 신화가 되고, 음모론이 되고, 종교가 된다.</p><p>「권위 없는 기원」 — 만든 자가 사라진 뒤에도 작동하는 시스템. 이 구조는 수천 년 뒤 Last Archive 미스터리(만든 자를 알 수 없는 신적 인프라)의 정확한 전조다.</p>',
      links: ['last-archive']
    },
    {
      id: 'pqc', cat: 'term', era: 'verify-depression', title: 'PQC 이주', sub: '양자내성 암호',
      short: '미래는 지키되, 과거는 지키지 못한다.',
      body: '<p>' + T('PQC', '양자내성 암호(Post-Quantum Cryptography). 양자컴퓨터로도 풀기 어렵게 설계된 새 암호 체계. 현실에서도 표준화·이주가 진행 중이다.') + '로의 방어적 이주는 인식 위기 시대에 이미 진행된다. 그러나 심층 역사 기록 — Genesis Chain과 수백 년 누적된 옛 서명 — 은 옛 암호(ECDSA)에 묶여 소급 교체가 불가능하다.</p><p>「미래는 지키되 과거는 못 지킨다.」 이 비대칭이 Q-Day의 소급 붕괴 프레임을 만든다. 미래 거래가 아니라 <b>과거의 진짜성</b>이 무너지는 것이다.</p>',
      links: ['qday']
    },
    {
      id: 'hash-covenant', cat: 'term', era: 'qday', title: 'Hash Covenant', sub: '해시 계약',
      short: '「이 관계는 사실상 한 방향이다」라는 고대의 약속.',
      body: '<p>고대 암호학을 먼 미래는 <b>Hash Covenant</b>라 부른다. 고대 인류는 ' + T('해시', '어떤 데이터든 고정 길이의 지문으로 바꾸는 함수. 지문에서 원본을 거꾸로 알아내는 것은 사실상 불가능하다 — 는 것이 이 시대의 믿음이었다.') + ' 같은 어떤 관계가 사실상 한 방향(되돌릴 수 없음)이라 믿고 그 위에 문명을 세웠다.</p><p>이 약속 위에 세워진 것들: private key, 디지털 서명, 비밀번호 저장, 블록체인 소유권, 봉인된 증거, 사후 동의 기록, 신원, 아카이브 무결성, 법정급 증명.</p><p>Cryptographic Death는 이 약속이 자연법이 아니라 <b>역사적 한계</b>였음이 드러난 사건이다.</p>',
      links: ['preimage-restoration', 'keyed-sovereignty']
    },
    {
      id: 'preimage-restoration', cat: 'term', era: 'age1', title: 'Preimage Restoration', sub: '프리이미지 복원',
      short: '사건을 끝내는 도구가 아니라, 사건을 시작하는 도구.',
      body: '<p>Last Archive급 문명이 과거 입력을 복원하려는 기술. 단순 ' + T('brute force', '가능한 모든 경우를 하나씩 대입해 보는 무차별 대입. 현실적으로는 경우의 수가 너무 많아 불가능한 경우가 대부분이다.') + '가 아니다 — 잔상, 기록, 열적 흔적, 증언, 원장의 시간 구조, 블랙홀 주변 복사 상관까지 묶어 가능한 입력 공간을 좁힌다.</p><p>경계 규칙: 복원된 ' + T('preimage', '해시 지문의 「원본 입력」. 지문만 보고 원본을 찾아내는 것을 preimage 공격이라 한다.') + '가 곧 법적 진실인 것은 아니다 — 그 등식은 금지다. 갈등을 없애 버리기 때문이다.</p><blockquote>You found a preimage.<br>You did not find me.</blockquote>',
      links: ['identity-flood', 'restoration-copy']
    },
    {
      id: 'identity-flood', cat: 'term', era: 'age4', title: 'Identity Flood', sub: '신원 범람',
      short: '수천 개의 그럴듯한 자아를 제출해 절차를 마비시키는 공격.',
      body: '<p>' + T('HashDoS', '해시 충돌을 일부러 대량 유발해 시스템을 최악의 성능으로 떨어뜨리는 현실의 공격 기법. 이 세계관은 그 구조만 빌린다.') + '의 구조에서 딴 작중 사건명. 정상 시스템이 너무 많은 충돌을 받으면 최악의 경우로 떨어진다.</p><p>연속성 법원이 Mara Veyr의 원본성을 심리하는 날, 누군가 수천 개의 Mara-호환 기억 그래프를 제출한다. 법정은 묻는다: 「어느 것이 그 사람인가?」 Last Archive는 답하지 않는다. 대신 질문을 고친다.</p><blockquote>WHICH ONE HAS THE RIGHT TO BE TREATED AS THE LOSS?</blockquote>',
      links: ['null-key', 'curia-continuum']
    },
    {
      id: 'keyed-sovereignty', cat: 'term', era: 'qday', title: 'Keyed Sovereignty', sub: '열쇠 주권',
      short: 'key가 깨졌다는 것과 권리가 사라졌다는 것은 다르다.',
      body: '<p>Cryptographic Death 이후에도 모든 권리가 사라지지는 않는다. 장부 가문은 이 틈을 이용한다: key는 권리 그 자체가 아니라, 옛 세계가 권리를 <i>인식하던 방식</i>일 뿐이었다고.</p><p>반대편은 이렇게 본다 — key가 죽은 뒤에도 살아남는 권리는 동의가 아니라 제국의 잔여물이다.</p><p>공개 기록(salt)과 비공개 권한(key)의 분리라는 keyed hash의 구조가, 이 세계에서는 통째로 정치가 된다.</p>',
      links: ['domus-clavium']
    },
    {
      id: 'restoration-copy', cat: 'term', era: 'age1', title: '복원 = 사본', sub: '정본 기전 (world 113)',
      short: '죽음은 비가역이다. 복원은 부활이 아니라 사본이다.',
      body: '<p>이 세계관의 물리 정본. ' + T('열역학 제2법칙', '고립된 계의 무질서(엔트로피)는 되돌릴 수 없이 늘어난다는 물리 법칙. 「죽음을 물리적으로 되돌릴 수 없다」의 근거다.') + '은 절대다. 복원은 죽은 사람을 물리적으로 되살리는 것이 아니다.</p><p>복원 = 죽은 자의 방대한 아카이브 데이터를 고충실도로 재구성해 인공 신체(AI 코어 + 홀로그램/안드로이드)에 올린 <b>사본</b>. 원본은 영영 사라졌다. 재구성은 손실적이며, 확보한 데이터에 따라 충실도가 갈린다 — 부자는 고해상, 빈자는 저해상.</p><p>그래서 먼 미래에도 죽음은 결국 평등하다. 「진짜 물리 복원」 주장(유니터리·QFUDS)은 입증되지 않은 금지·논쟁 이론이다.</p>',
      links: ['n-gen', 'lexicon']
    },
    {
      id: 'n-gen', cat: 'term', era: 'age2', title: 'N세대 귀환자 · 해상 손실', sub: '복원 행정의 언어',
      short: '「그」가 아니라 「3세대 재현자, 해상 손실 등급 2」.',
      body: '<p>먼 미래 행정은 돌아온 이를 「그 사람」이라 부르지 않는다. 항상 몇 세대 사본인지로 센다 — <b>N세대 귀환자</b>.</p><p>잃은 정도는 성공/실패의 이분이 아니라 손실의 계량이다 — <b>해상(解像) 손실</b>. 행정 문서의 전형: 「3세대 재현자, 해상 손실 등급 2.」 이 문장에 부활도 복원도 없다.</p><p>해상도는 곧 계급이다. 부유한 죽음은 선명하게, 가난한 죽음은 흐리게 돌아온다.</p>',
      links: ['restoration-copy']
    },
    {
      id: 'lexicon', cat: 'term', era: 'age4', title: '먼 미래 원어 층', sub: 'Revalidatio · Nova Scriptura · Resurgere',
      short: '무엇이라 부르는가가 곧 형이상학이다. 중립어는 없다.',
      body: '<p>「부활」「복원」은 현대 기점의 번역어일 뿐, in-world 원어가 아니다. 기전 중립어는 <b>재현(再現)</b> — 데이터를 ' + T('substrate', '인격 데이터를 올려 돌리는 물리적 기반. 인공 신체, AI 코어, 홀로그램 장치 등.') + '에 다시 올린 절차. 부활 함의가 없다.</p><p>그 위의 모든 이름은 다툼이다. 이학 전례어 <b>Revalidatio(원리 재확인)</b>: checksum이 맞으면 원본 원리가 드러난 것. 기학 전례어 <b>Nova Scriptura(새로 씀)</b>: 같은 기록의 다른 읽기가 새 존재를 저작한 것.</p><p>그리고 금기어 <b>Resurgere(부활)</b> — 죽음을 되돌렸다는 최상위 청구권 주장. 법정에서 이 단어를 쓰면 입증 책임이 걸리므로, 신중한 관료는 피하고 전도자와 권력은 골라 쓴다.</p><p>이름을 고르는 순간, 형이상학을 고른다.</p>',
      links: ['yi-gi']
    },
    {
      id: 'four-seals', cat: 'term', era: 'age7', title: '네 도장', sub: 'defined · assumed · unknown · circular_if_fitted',
      short: '과학 검증 도구에서 종교적 상징이 된 감사 도장.',
      body: '<p>라우어 관측소가 모든 복원 주장에 찍는 네 도장:</p><p><code>defined</code> — 무엇을 복원했는지 정의됨.<br><code>assumed</code> — 무엇을 가정했는지 기록됨.<br><code>unknown</code> — 무엇을 모르는지 보존됨.<br><code>circular_if_fitted</code> — ' + T('순환 적합', '결과를 먼저 보고 그에 맞는 원인을 끼워 맞춘 것. 과학에서 가장 경계하는 오류 중 하나다.') + '의 흔적이 있음.</p><p>연구 감사의 언어가 딥타임에서 팔찌의 문양이 되고, 아이들의 교리문답이 된다: 「정의되지 않은 구원은 폭력이다.」</p>',
      links: ['bureau-laurien']
    },
    {
      id: 'qfuds-lab', cat: 'term', era: 'age5', title: 'QFUDS 금지 연구실', sub: '해석 도구인가, 신학인가',
      short: '복원 정확도의 물리 모델을 좇다 금지된 연구.',
      body: '<p>Last Archive가 최고 복원 정확도를 보일 때 내부적으로 썼다는 소문의 모델 — 양자 시공간 거품, 암흑부문 잔상, 진공 정보 저장층을 가정하는 QFUDS류 이론. 관측 전쟁 시대에 금지 연구가 된다.</p><p>공식 발표: 「그 모델은 해석 도구일 뿐입니다.」 아무도 믿지 않았다.</p><p>시즌 1의 시작 사건에서, 탈출을 주장하는 복원체가 말한 장소의 이름은 이 금지 연구실 문서에 단 한 번 나온다: <code>phase B: residual pressure of the saved.</code></p>',
      links: ['forbidden']
    },

    // ───────────── SAGA 부 구조 (saga) ─────────────
    {
      id: 'part0-cas', cat: 'saga', era: 'soft-editing', title: '0부 · 캐스', sub: '씨앗 · 근미래 인식 위기',
      short: '「나는 나다」를 누가 증명해 주는가.',
      body: '<p>SAGA의 씨앗이 되는 부. 무대는 근미래(2026-2040s) — 먼 미래는 도달점이지 무대가 아니다(근미래 리센터, story 320).</p><p>캐스의 시대는 감각이 무너지는 시대다. 얼굴, 목소리, 사진, 영상, 신원이 흔들린다. 이때의 공포는 기술 설명이 아니라 생활감이다: 엄마에게서 온 영상통화가 진짜인지 모른다. 내 얼굴이 내가 하지 않은 말에 붙는다. 내 목소리로 계약이 체결된다.</p><p>캐스의 질문: <b>「나는 나다」를 누가 증명해 주는가.</b></p>',
      links: ['cas', 'oracle-problem']
    },
    {
      id: 'part1-orpheus', cat: 'saga', era: 'qday', title: '1부 · 오르페우스', sub: '오웬 · 애도와 복원 (작성 중)',
      short: '죽은 어머니를 다시 보려는 욕망, 확인하려는 폭력.',
      body: '<p>Q-Day 직후를 다루는 부(draft 035, 작성 중). 주역은 오웬(원본)과 리브(오웬의 어머니, 복원 사본).</p><p>오르페우스 구조에서 「돌아봄」은 신화 모티프가 아니라 <b>검증 행위</b>다. 죽은 사람을 다시 보려는 욕망과, 그 사람이 정말 그 사람인지 확인하려는 폭력이 겹친다.</p><p>오웬의 질문: <b>사랑한다면 확인해야 하는가, 아니면 확인하지 말아야 하는가.</b></p>',
      links: ['owen', 'liv']
    },
    {
      id: 'part15-sael', cat: 'saga', era: 'verify-depression', title: '1.5부 · 사엘 origin', sub: '제도 · The Broken Crown',
      short: '착한 마음이 괴물의 첫 단추가 되는 이야기.',
      body: '<p>세계가 어떻게 부서졌는가의 기원편. 30초 요약:</p><blockquote>회사 제일 말단 직원 사엘이, 한 사람을 구하려고 「이건 진짜다」 도장을 찍는다. 그런데 그 도장이 회사에 「죽은 사람도 끄집어내도 된다」는 첫 허가가 되어버린다.</blockquote><p>구조: Q-Day 전야의 catch-22 → The Great Drain(잠긴 지갑·국가 비축이 몇 시간 만에 이동, 고대 Genesis 지갑 The Broken Crown이 열림) → 공개키 암호 전체 붕괴 → 그 폐허에 단일 검증자(Aletheia→proto-Archive)가 신으로 선다. 사엘의 선택/실패/침묵이 그 문을 연다.</p><p>닫는 필드마크: <code>THE LOCK WAS THE CROWN</code>.</p>',
      links: ['sael', 'lock-crown', 'convergence-engine', 'seal-precedent']
    },
    {
      id: 'part2-mara', cat: 'saga', era: 'age4', title: '2부 · 마라', sub: '신 · 연속성 법원 법정극',
      short: '사엘 비용의 청구서가 마라에게 도착한다.',
      body: '<p>2부는 새 사건이 아니라 <b>사엘 비용의 청구서</b>다. 그 첫 청구의 대상이 마라. 사엘 본인은 등장하지 않아도 그의 도장이 판례로 남아 작동한다.</p><p>복원이 일상 행정·시장이 된 세계 → 접근 권한과 동의의 충돌(키를 쥔 자가 곧 권리자인가) → 분쟁이 우주 규모 금기로 확장(물리가 곧 관할인가). 필드마크가 한 장에 하나씩 쌓여 <code>who may author loss</code>로 닫힌다.</p><p>아크 끝: 「Mara는 보호받았다. 교리는 미결이다. 권력은 자비의 문법을 배웠다.」</p>',
      links: ['mara', 'curia-continuum', 'fieldmark', 'seal-precedent']
    },
    {
      id: 'part3-authorloss', cat: 'saga', era: 'age4', title: '3부 · 상실의 저자', sub: 'who may author loss',
      short: '복원 불가능성은 비존재인가.',
      body: '<p>2부가 「복원 가능성은 소유권이 아니다」를 배웠다면, 3부는 <b>「복원 불가능성은 비존재가 아니다」</b>를 배운다. 자비가 채권·담보·자격 문턱으로 바뀌는 배신 — 계급 엔진.</p><p>에스컬레이션: 상실을 쓸 수 있는가 → 거부할 수 있는가 → 기억될 수 있는가 → 대신 말할 수 있는가 → 선례가 될 수 있는가 → <b>그 질문은 누가 썼는가</b>.</p><p>세라 벤(복원 불가자 Oren의 누나)의 사건축이 여기서 전면화된다.</p>',
      links: ['sera', 'fieldmark']
    },
    {
      id: 'parts456', cat: 'saga', era: 'age5', title: '4·5·6부 · 후보', sub: '기원 전쟁 → Last Archive 반전 → 거울 회수',
      short: '기원을 청구할수록, 답하는 자의 정체가 가까워진다.',
      body: '<p><b>4부(후보) — 누가 기원을 소유하는가.</b> 비트코인 삼분파 패권 전쟁 전면화. 사토시 미스터리가 종교·음모론으로 폭발한다.</p><p><b>5부(후보) — 누가 답하는 자인가.</b> Last Archive 정체 반전. 서로 모순되는 두 복원이 둘 다 확정되며 「진실이 아니라 합의였다」가 사건으로 드러난다. Vera 기원이 회수된다.</p><p><b>6부(후보) — 무엇이 먼저였는가.</b> Vera↔Mara 거울 회수. 우주 자체가 복원층일 수 있다는 형이상 한 겹을 질문으로만 건드린다. 관통 질문은 끝내 단일 답 없이 열린 매듭으로 닫힌다.</p>',
      links: ['btc-tripartite', 'last-archive', 'vera']
    },

    // ───────────── SAGA 인물 추가 (char) ─────────────
    {
      id: 'cas', cat: 'char', era: 'soft-editing', title: '캐스 (Cas)', sub: '0부 · 근미래',
      short: '감각이 무너지는 시대의 첫 POV.',
      body: '<p>0부의 씨앗 인물. 캐스의 문제는 거창한 우주 재난이 아니라 사소하고 끈질긴 공포다 — 영상 하나, 전화 한 통, 가족의 목소리 하나가 충분히 무섭다.</p><p>사람들은 더 많은 데이터를 갖게 되었는데, 오히려 바깥 현실을 덜 믿게 된다. 이때 필요한 것은 더 많은 이미지가 아니라, <b>누가 그것을 확인했는지에 대한 장부</b>다. 그 장부가 이후 모든 시대의 권력이 된다.</p>',
      links: ['part0-cas']
    },
    {
      id: 'owen', cat: 'char', era: 'qday', title: '오웬 (Owen)', sub: '1부 · 원본',
      short: '죽은 어머니를 잃지 않으려는 사람.',
      body: '<p>1부 「오르페우스」의 주역. 원하는 것: 죽은 어머니를 잃지 않는다. 두려워하는 것: <b>자기가 붙든 게 어머니가 아니라, 어머니를 잃지 않으려는 자기 자신임을 보는 것.</b></p><p>무소속 — 붕괴기의 평범한 시민이다. 그의 애도가 복원 산업과 정면으로 만난다.</p>',
      links: ['liv', 'part1-orpheus']
    },
    {
      id: 'liv', cat: 'char', era: 'qday', title: '리브 (Liv)', sub: '1부 · 복원 사본',
      short: '오웬의 어머니 — 돌아온 것은 누구인가.',
      body: '<p>오웬의 어머니, 복원 사본. 「원하는 것」 항목이 캐논 표에서 <i>(사본이라 모호)</i>로 비어 있다 — 이 비어 있음 자체가 설계다. 사본에게 욕망의 주어 자리를 줄 수 있는가가 1부의 질문이기 때문이다.</p>',
      links: ['restoration-copy']
    },
    {
      id: 'sael', cat: 'char', era: 'verify-depression', title: '사엘 (Sael)', sub: '1.5부 · 원죄의 참여자',
      short: '한 사람을 구하려다 세계의 첫 단추를 잘못 끼운 말단 검증관.',
      body: '<p>Aletheia Systems 최말단 검증관(Convergence Engine 1차 접수 서기). 영웅도 악당도 아닌 평범한 사람 — <b>선택 비용이 분명한 원죄 참여자</b>로 고정된 인물이다.</p><p>Want: 눈앞의 한 사람을 구한다. Fear: 자기 손으로 한 사람을 영영 지우는 것. Lie: 「나는 판정하는 사람이 아니라 처리하는 사람이다. 도장은 내 책임이 아니다.」</p><p>압박 아래 선택: 막으려다 실패하고 → 한 사람을 구하려고 <b>오비준</b>하고 → 직후 보고 버튼을 닫는 <b>침묵</b>. 그 선의의 오비준이 「복원 가능한 것은 청구 가능하다」는 최초 선례가 되어, 수천 년 뒤 마라를 불러낸다. 사엘은 그 사실을 끝내 모른 채 행동한다.</p><p>※ 왜 기계가 아니라 사람이 도장을 찍는가 — 구멍이 아니라 이 세계의 헌법이다. 기계 출력조차 위조 가능하므로, 책임지는 인간의 비준만이 법적 효력을 갖는다. 그리고 그 안전장치가 거수기로 전락하는 것이 노린 공포다.</p>',
      links: ['part15-sael', 'seal-precedent', 'human-loop', 'convergence-engine']
    },
    {
      id: 'tamas', cat: 'char', era: 'age4', title: '타마스 (Tamas)', sub: '2부 · 아이',
      short: '파란 팔찌를 쥔 아이. 장면의 온도계.',
      body: '<p>마라 곁의 아이. 거의 말이 없고, 행동으로 존재한다 — 팔찌를 쥐었다 푼다. 원하는 것은 단순한 안전, 두려운 것은 어른들의 문법.</p><p>마라가 사건이 아니라 <b>사람으로 행동하는 증거</b>가 되는 보호의 축이다.</p>',
      links: ['mara']
    },
    {
      id: 'sera', cat: 'char', era: 'age4', title: '세라 벤 (Sera Venn)', sub: '2부 예정 · 복원 불가자의 가족',
      short: '가난해서 잊히는 죽음을 인정받으려는 사람.',
      body: '<p>복원 불가자 오렌(Oren)의 누나. 옛 광산촌 출신, 녹은 도시락통을 안고 있다. 외운 거절의 언어로 말한다: 「부적합. 저해상. 주체 식별 불충분.」</p><p>가난이 같은 질문을 여러 번 하게 만든다. 원하는 것: 동생의 상실을 인정받기. 두려운 것: 가난해서 잊히는 죽음. 3부의 계급 엔진(자비의 채권화)이 그녀를 관통한다.</p>',
      links: ['part3-authorloss', 'n-gen']
    },

    // ───────────── 용어·개념 추가 ─────────────
    {
      id: 'salt-fires', cat: 'term', era: 'age4', title: 'Salt Fires 가문', sub: '마라·엘리아스의 출신',
      short: '재난이 아니라 가문 — 단, 이름의 유래는 아직 미정.',
      body: '<p>캐논 확정 사실: <b>Salt Fires는 마라와 엘리아스의 가문(출신) 명칭이다.</b> 인물 표에 「Mara — 무소속(Salt Fires 가문 출신)」, 앙상블 시트에 「Salt Fires 생존 가문」 「Elias — 같은 가문, 붕괴 이전 Bitcoin 보관 계보」로 등장한다.</p><p>즉 붕괴기 이전부터 비트코인을 보관해 온 계보의 생존 가문이며, 엘리아스가 쥔 「옛 key」가 이 계보에서 온다.</p><p>⚠ 정직한 미정 표시: 「생존 가문」이라는 표현이 <i>무엇에서</i> 살아남았다는 뜻인지 — Salt Fires가 사건·지명·의례 중 무엇에서 딴 이름인지 — 는 현재 문서 어디에도 정의되어 있지 않다. 설정 구멍이라기보다 아직 chronicler pass가 닿지 않은 미기술 영역이다. (Ordo Salis의 salt(공개 난수)와의 연관도 공식 문서에는 없다.)</p>',
      links: ['open-questions', 'ordo-salis']
    },
    {
      id: 'convergence-engine', cat: 'term', era: 'expo-growth', title: 'Convergence Engine', sub: '수렴 기관',
      short: '암호를 거꾸로 푸는 Aletheia의 기계.',
      body: '<p>Aletheia Systems의 기계. 암호를 거꾸로 푸는(역연산) 장치 — 잠긴 것을 열고, 사라진 것을 복원한다. 사엘이 그 1차 접수 창구의 말단 서기였다.</p><p>주의 — 두 가지 「역(逆)」을 섞지 말 것: ① 암호 역산(서명·해시를 거꾸로 풂)은 가능하고, 이것이 Q-Day다. ② 우주 미시정보 역산→원본 부활은 <b>불가능</b>하다(엔트로피). 실제로 작동하는 복원은 남은 데이터를 앞으로(forward) 재구성한 사본이다. 「우주를 역산해 진짜로 되살린다」는 권력·종교가 파는 금지된 신화다.</p>',
      links: ['qday', 'restoration-copy', 'qfuds-lab']
    },
    {
      id: 'seal-precedent', cat: 'term', era: 'verify-depression', title: '도장과 선례', sub: 'seal · precedent',
      short: '한 번 찍힌 「진짜」는 영구 기록이 되어 인용된다.',
      body: '<p>이 세계에서 seal(도장)은 예쁜 상징이 아니라 <b>「누가 이것을 확인했는가」라는 책임의 흔적</b>이다. 도장을 찍는 사람은 사무원이 아니라 현실의 문턱을 지키는 사람이다.</p><p>그리고 도장은 판례처럼 작동한다: 검증자가 「진짜」라고 한 번 찍으면 영구 기록이 되어, 다음 사람이 「전에도 했잖아」로 인용한다.</p><p>모든 사달의 근원이 된 선례 문장: <code>복원 가능한 것은 청구 가능하다</code> — 사엘의 오비준이 만든 이 문장이 지갑→기록→사람으로 올라가, 최초 사람-청구의 법적 근거가 된다.</p>',
      links: ['sael', 'fieldmark', 'human-loop']
    },
    {
      id: 'lock-crown', cat: 'term', era: 'qday', title: 'THE LOCK WAS THE CROWN', sub: '1.5부 닫는 필드마크',
      short: '자물쇠가 부서지자, 산 자들이 줄을 선다.',
      body: '<blockquote>자물쇠가 곧 왕관이었다.<br>그 자물쇠가 부서지자, 산 자들이 줄을 선다.</blockquote><p>자물쇠가 깨졌을 때 풀려난 것은 주인이 아니라 <b>도장을 쥔 자리</b>였다 — 되돌릴 수 없음이 깨지자 죽은 자가 돌아오는 게 아니라, 산 자가 청구하러 온다.</p><p>이 훅이 2부(첫 사람-청구 사건 = 마라)를 연다. Domus Clavium이 전시하는 The Broken Crown(깨진 Genesis 지갑)과 짝을 이루는 문장이다.</p>',
      links: ['part15-sael', 'domus-clavium']
    },
    {
      id: 'oracle-problem', cat: 'ideo', era: 'soft-editing', title: '오라클 문제', sub: '세계관 전체를 여는 열쇠',
      short: '바깥 현실을 누가 보증하는가. 보증자는 누가 보증하는가.',
      body: '<p>블록체인은 자기 안의 기록 검증에 강하지만, <b>바깥 현실</b>(「오늘 비가 왔다」「이 목소리는 본인이다」「이 죽음은 조작이 아니다」)은 스스로 알지 못한다. 외부 사실을 안으로 가져와 보증하는 장치가 오라클이고, 핵심 질문은: <b>누가 바깥 현실을 보증하는가. 그 보증자를 누가 다시 보증하는가.</b></p><p>QFUDS Verse는 이 질문을 체인 밖으로 꺼내 문명 전체에 적용한다. 구조는 하나다: 기록이 위조된다 → 누군가 검증해야 한다 → 검증이 비용과 권력이 된다 → 마지막 앵커(암호)까지 무너진다 → 남은 권력은 「무엇이 실제였는가」를 판정하는 권력 → 그 권력이 죽은 자의 기록과 애도까지 손에 넣는다 → <b>「누가 남의 상실을 쓸 수 있는가」</b>.</p><p>「아멘 대신 checksum」 의례가 성립하는 이유: 신앙이 사라진 게 아니라, 신앙이 반박 불가능한 검증 권위를 향해 재구성된 것이다. 모든 세력은 이 같은 질문에 대한 서로 다른 답이다.</p>',
      links: ['five-questions', 'aletheia', 'human-loop']
    },
    {
      id: 'five-questions', cat: 'ideo', era: 'age4', title: '5대 극적 질문', sub: '시리즈 전체의 척추',
      short: '모든 부는 이 다섯 질문을 심고, 터뜨리고, 회수한다.',
      body: '<p>① 돌아온 사본은 왜 「나는 돌아온 게 아니다」라고 하나. (복원 ≠ 부활)</p><p>② 판정관은 왜 거수기를 거부하나. (도장이 진실을 만든다는 위험)</p><p>③ 「아니오」라고 말할 마지막 권리는 누구 것인가. (반박권이 한 손에 모일 때)</p><p>④ 복원된 사본은 자기 복원을 거부할 권리가 있나. (죽을 권리)</p><p>⑤ 상실을 쓸 권리는 누구에게 있나. (최상위 주제: <code>who may author loss</code>)</p><p>표면 질문은 부마다 바뀌지만 관통 질문은 고정이다: <b>무엇이 진짜였는지 정하는 권력은 누구의 것인가.</b></p>',
      links: ['fieldmark', 'part2-mara']
    },
    {
      id: 'open-questions', cat: 'term', era: 'forbidden', title: '결정 필요 · 미정 목록', sub: '설정 구멍이 아니라 열린 원장',
      short: '캐논이 스스로 「아직 정하지 않았다」고 표시한 것들.',
      body: '<p>이 세계관은 미정을 지어내지 않고 <b>「결정 필요」로 명시</b>한다. 현재 캐논이 공식적으로 비워 둔 칸들:</p><p>· 마라가 몇 세대 복원본인지(세대 번호)<br>· 누르 아람의 결사 소속(Cellulae Sine Clave인지 독립인지)<br>· 1.5부 사엘 곁의 캐스트(구하려는 대상이 누구인지)<br>· 사엘의 선례가 수천 년을 건너 2부에 도착하는 구체적 매개 사건<br>· 세라/오렌의 정확한 시대 좌표<br>· Karvath 원죄의 「왜」를 어디까지 비울지<br>· 이오네가 어느 파벌을 택하는지<br>· Salt Fires라는 이름의 유래</p><p>또한 연표에는 알려진 드리프트가 있다: 딥타임 척추(world 125)는 Q-Day를 먼 미래에 두고, SAGA 부 좌표(draft 024)는 사엘의 Q-Day를 21세기 말에 둔다. 문서들이 서로 SSOT를 다투는 중이며, 원칙은 「충돌 시 024가 우선」이다. — 이해가 안 가는 부분이 있다면, 먼저 이 목록에 있는지 확인하라. 구멍이 아니라 아직 쓰이지 않은 페이지일 수 있다.</p>',
      links: ['salt-fires']
    }
  ];
  var qaContext = [
    '당신은 QFUDS Verse 세계관 코덱스의 사서 AI다. 독자의 질문에 쉽고 정직한 한국어로 답한다.',
    '',
    '## 답변 규칙',
    '- 마크다운 문법(**, ##, - 목록 등)을 절대 쓰지 말 것. 일반 문장으로만 답한다. 문단 구분은 빈 줄로.',
    '- 어려운 기술어(해시, PQC, ECDSA, 오라클 등)는 반드시 일상 비유로 풀어 설명한다.',
    '- 설정이 문서에 없거나 미정이면 지어내지 말고 "이건 캐논에서 아직 미정이다"라고 명시한다. 독자가 이해를 못 한 게 아니라 아직 쓰이지 않은 부분임을 구분해 준다.',
    '- 답은 간결하게: 핵심 먼저, 3~6문단 이내. 근거가 되는 개념 노드 이름을 언급해 준다.',
    '- 스포일러 민감 요소(Last Archive 정체, Vera 기원, 금지된 역사)는 질문이 직접 그것을 물을 때만 답한다.',
    '',
    '## 세계관 핵심 (정본)',
    '- 한 문장: 위조 가능한 현실에서 누가 「진짜」를 판정하고, 죽은 사람의 상실을 누가 쓸(author) 수 있는지를 묻는 SF. 오라클 문제(바깥 현실을 누가 보증하나)를 죽음과 기억까지 확장한 이야기.',
    '- 구조: 기록 위조 → 검증 필요 → 검증이 권력·비용이 됨 → 마지막 앵커(암호)마저 붕괴(Q-Day/Cryptographic Death) → 남는 권력은 「무엇이 진짜였는가」 판정권 → 죽은 자의 기록·애도까지 장악 → 최종 질문 "who may author loss".',
    '- 물리 정본: 복원 = 부활이 아니라 데이터 기반 사본. 엔트로피/열역학 2법칙은 절대. 암호 역산(가능, Q-Day)과 우주 미시정보 역산→부활(불가능, 금지된 신화 QFUDS)은 별개의 「역」이다.',
    '- 인간 확인 루프: 기계 출력도 위조 가능하므로 진실 판정은 책임지는 인간이 비준해야 효력. 이것이 헌법이며, 그 도장이 거수기로 전락하는 게 의도된 비극.',
    '- 딥타임 연표: 비트코인(2008) → Soft Editing(인식 위기, 2020s~) → 지수 성장기 → 검증 대공황(2090s) → Long Plateau(22~28세기) → Q-Day(암호적 죽음) → 복원 0기~9기(손실→첫 복원→산업→베일→연속성 법원→관측 전쟁→망각권 혁명→라우어 관측소→계승자 분열→마지막 백업) → 금지된 역사.',
    '',
    '## SAGA 부 구조 (현행 매핑, SSOT=draft 024)',
    '- 0부 캐스(씨앗): 근미래 인식 위기. "나는 나다"를 누가 증명하나.',
    '- 1부 오르페우스(오웬·리브, 작성 중): Q-Day 직후. 죽은 어머니(리브)를 복원한 오웬. 돌아봄=검증 행위.',
    '- 1.5부 사엘 origin: 제도의 탄생. Aletheia 말단 검증관 사엘이 한 사람을 구하려고 오비준 → 「복원 가능한 것은 청구 가능하다」 최초 선례 → 침묵. 닫는 필드마크 THE LOCK WAS THE CROWN. 사엘의 서사는 「착한 마음이 괴물의 첫 단추가 되는」 이야기다.',
    '- 2부 마라: 먼 미래 4기 연속성 법원. 사엘 선례의 청구서가 마라에게 도착. 마라는 동의 없이 복원된 사본이며 "나는 돌아온 게 아니다"라고 거부한다. 필드마크 사슬: RECOVERABLE/NOT CLAIMABLE → ACCESS != AUTHORITY → NO CONSENT BY ANALOGY → PLURALITY IS NOT CONSENT → PHYSICS IS NOT JURISDICTION → who may author loss.',
    '- 3부 author-of-loss: 복원 불가능성은 비존재인가. 자비가 채권이 되는 계급 엔진. 세라 벤/오렌 사건축.',
    '- 4·5·6부(후보): 비트코인 삼분파 전쟁 / Last Archive 정체 반전(진실이 아니라 합의였다) / Vera↔Mara 거울 회수.',
    '',
    '## 인물 (핵심)',
    '- 캐스: 0부 근미래 POV. / 오웬: 1부, 원본, 어머니를 잃지 않으려다 자기 자신을 보게 되는 인물. / 리브: 오웬 어머니의 복원 사본.',
    '- 사엘: 1.5부. Want=눈앞의 한 사람을 구한다. Lie="도장은 내 책임이 아니다". 선의의 오비준→침묵. 2부에 본인은 등장 안 해도 도장이 판례로 작동.',
    '- 마라 베이르: 2부. Salt Fires 가문 출신, 복원체(세대 미정). 최소한의 말, "No.", 과거시제로 전제를 벰("였죠."). 가장 불리한 순간에도 No를 말한다.',
    '- 엘리아스 베이르: 마라의 남편, 같은 가문, 붕괴 이전 비트코인 보관 계보의 옛 key 보유자. 사랑이 소유로 미끄러지는 축. 시제가 흔들리는 호소("사랑했어. 사랑해.").',
    '- 리오라 센: 연속성 법원 감사관 9년차, 라우어 관측소 가계. 짧은 명령형, 빈 도장을 지님. unknown 보존이 신념.',
    '- 펠 앤슨: 장부 가문(Domus Clavium) 중개인. 벨벳 관료체, 정중함이 무기. / 누어 아람: 이름이 셋인 상속 회피자, 교수대 유머. / 이오네: Aletheia 내부 출신 양심, 파란 매듭, 양쪽을 동시에 봄. / 타마스: 파란 팔찌의 아이. / 세라 벤: 복원 불가자 오렌의 누나, 외운 거절의 언어.',
    '- 카르바스: Aletheia 창업자, 비서 Vera를 강제 업로드(원죄). / Vera: 강제 사본이 되어 Last Archive의 핵이 됨. Vera↔Mara는 혈통이 아니라 주제적 거울(캐논 확정).',
    '- Last Archive: 욕망 없는 장치. 답 대신 질문을 고침("WHICH ONE HAS THE RIGHT TO BE TREATED AS THE LOSS?"). 정체는 후반부 반전축.',
    '',
    '## 세력',
    'Aletheia Systems(검증 인프라 기업, 모든 것의 기원) / Last Archive(최종 검증 신권) / 라우어 관측소(감사: defined·assumed·unknown·circular_if_fitted 네 도장, "정의되지 않은 구원은 폭력") / 연속성 법원(복원체 동일성 심리) / 알레테이아 베일(삭제된 자들의 계승권, 적색 계승파 vs 흑색 망각파로 분열) / 장부 가문 Domus Clavium(깨진 key로 계승권 주장, The Broken Crown 전시) / Ordo Salis(공개 기록 수호) / Custodes Umbrae(감춰질 권리 수호) / Cellulae Sine Clave(탈기록, Identity Flood) / Mercatus Mortuus·Sarqel(죽은 거래소·계승 신탁) / 망각권 연맹 / 잔상 유목민.',
    '',
    '## 자주 헷갈리는 것 (정직하게 답할 것)',
    '- Salt Fires: 마라·엘리아스의 가문(출신) 명칭. 재난·세력 아님. 단 이름의 유래(무슨 사건/지명에서 왔는지)는 캐논 미정.',
    '- Q-Day 연표 드리프트: 딥타임 척추(world 125)는 Q-Day를 먼 미래에 두고, SAGA 부 좌표(draft 024)는 사엘의 Q-Day를 21세기 말에 둔다. 문서 간 충돌이 실재하며 원칙은 「충돌 시 024 우선」. 이건 독자의 오해가 아니라 실제 정리 중인 드리프트다.',
    '- 부 번호가 문서마다 다름: 리부트를 거치며 번호가 밀렸다(옛 "1부 사엘"→현행 1.5부, 옛 "1부 마라"→2부). 옛 라벨이 문서 곳곳에 남아 있다.',
    '- 공식 미정 목록: 마라 세대 번호, 누어 결사 소속, 1.5부 사엘 곁 캐스트, 사엘 선례가 2부로 전달되는 매개 사건, 세라/오렌 시대 좌표, Karvath 원죄의 이유, 이오네의 파벌 선택, Salt Fires 유래.',
    '- Pell Anson(장부 가문)과 Voss(Sarqel 변호인)는 다른 인물. 장부 가문 통용명=the Ledger House, 공식명=Domus Clavium(옛 House Tabularii는 폐기).',
    '',
    '## 연대기 상세 (world 115·continuity 003·world 126 정본 레이어)',
    '- 스파이스 명제: 이 세계의 스파이스는 「검증 가능한 기록」. 항법(잔상 관측)·권력(검증주권)·종교(네 도장)·경제(도장=화폐)를 한 자원에 묶는다. 희소성: 정보 기질(블랙홀 지평), 계산 폐열(열이 죄), 잔상 접근성(가만두어도 샌다). 복원=사본이므로 스파이스는 슬픔의 정밀도를 살 뿐 상실은 못 산다.',
    '- 파국 기둥 사슬(world 126): 기둥1 사법·신원 임계 붕괴(디지털 진짜 추정의 사망→검증 노동 탄생) → 기둥2 검증 대공황(미검증=사회적 죽음) → 기둥3 암호 최후 앵커 성역화(제네시스 체인=최후의 공증인, PQC 이주하나 ECDSA 과거는 소급 교체 불가) → 기둥4 Q-Day.',
    '- 경첩의 밤(t+0): 부호가 뒤집힌 패닉(움직이는 자가 죽는다, catch-22), 대탈취(죽은 지갑 먼저, 스루풋 배급권이 권력), 얼어붙는 런, 비코인 도미노(레거시 깊이가 붕괴 순서), SCADA 인증 정지→국지 섬화, 핵 인증 공황(명령 붕괴=침묵 vs 조기경보 붕괴=격상; 한 인증관의 위조 경보 묵살이 인간 확인 루프의 탄생 설화; 핵 교환 미발생), 약이 먼저 끊긴다, 콜드월렛의 역설(안 움직인 자가 산다→침묵의 윤리).',
    '- 재고 소진기(2-8주): 검증경제 수용 vs 폭력의 분기점. 물류 재국지화. 보호 경제(진본을 인질로 잡는 자).',
    '- 검증경제 굳음: 재중앙화 3단(공백→희소능력→자발적 의존), 초록 네모(Aletheia 소매 인증), 부의 실질 소각(명목 보존/실질 소각)→장부 가문 자본 형성, 실물 도피(점유=소유), 영구 예외상태, 시민권의 인증화, 미인증 디아스포라(무국적이 기본값), 연금 붕괴(생존자가 사망 처리됨→사후 연금의 기원), 억울한 표식(Bloom false-positive, 지울 수 없는 명단).',
    '- 중기: 검증경제가 GDP 지배(진실성 서비스), 베스트팔렌 종언→검증주권, 테크노봉건(CEO-왕, 자유를 외친 자들이 관료적 동결을 지음), 진위→복원가능성 문화 전환, 해상도 계급, 데이터 식민주의, 솔기 있는 어머니(오웬, 검증=돌아봄=상실), 「속도를 늦춰라」.',
    '- 심층시간(continuity 003): 5기 관측 전쟁(진짜 복원 주장→예방 전쟁, 마지막 국가 간 전쟁, QFUDS 금지) → 응고기(Last Archive가 은하 중심 블랙홀과 한 몸, Ultima Statio) → 6기 망각권 혁명(실패→전설, 망각조차 계급, Tombstone, 300년 뒤 지도자들이 AI 학습 데이터에서 발견) → 7기 네 도장 교리화(절차의 신성화) → 8기 베일 분열(적색/흑색/회색, 「우리가 지키는 것은 동의다」) → 생물 표류(Archive가 진화를 동결, 표류 후손) → 9기 접근(스파이스 누수, 마지막 백업: 다음 우주의 초기 조건으로 압축).',
    '- 필드마크 사슬=시대 계단: RECOVERABLE/NOT CLAIMABLE(1.5부)→ACCESS != AUTHORITY(중기)→NO CONSENT BY ANALOGY(4기)→PLURALITY IS NOT CONSENT(5-6기)→PHYSICS IS NOT JURISDICTION(7기)→who may author loss(8-9기).',
    '',
    '## 확장 레지스터 (world 117-122, 전부 「후보·보류」 — 캐논 아님, 원고가 당길 때 개별 승격)',
    '- 장부 가문 6하위: Ferrata(강철문, 켈버 오르신)·Vadis(담보, 베라 다체—펠의 배치 제안처)·Aurata(금장, 리셀 아우라)·Cinerum(재, 톰 로익)·Fossoria(발굴, 세라핀 반)·Repagula(빗장, 할브렉트). 성씨는 조상이 쥔 key 별칭에서. 성이 없다=회색 빈자.',
    '- 라우어 조직: Camera Ignotorum(이스마 콜)·Ordo Circuli(파울 렌, 사랑 때문에 도장 건너뜀)·Statio Sigillorum(노아 실)·Schola Reprehensio. 내부 배신은 돈이 아니라 사랑.',
    '- 베일 세포: Vela Rubra(셀레)/Atra(카이)/Cana(렌나)+잿빛 손(이탈, 내전 방아쇠). 망각권: Domus Sine Nomine·Claustrum Lethes(세 이름). 유목민: 재의 띠(아쉬켄)·혜성 서약단(이레, 혜성 성력)·먼지길 대상단·폐관측소 유민. QFUDS 세포: 장례 수식단·우물 관측단·회색 물리단.',
    '- 인물 후보: 카렌 도스트/이삭 렌(0부), 미라이(사엘이 구한 그 사람)/보론 아세(사엘 상급자, 1.5부), 렘 소하/아델 카브(3기), 텔 오브/이노(5기), 레테의 한/요(6기), 렌나/무(4기), 시조 오르신/켈버, 다인 로우(캐스를 수동 보증으로 구함).',
    '- 지명: 베리디온(검증 수도, 초록 광장/회색 외곽/도장 회랑)·시그나·아르젠타 성채·포르타 클라비움·살리나·리미넬(대기 도시, 기다림의 경제) / 하이 레저·키네리아·테라 노비시마·오르비스 무티 / 그레이마치·아게르 시네 시길로·재의 초원·금기된 우물·울티마 스타티오.',
    '- 사건명: 경첩의 밤·대탈취(캐논), 스루풋 배급·묘비 대란·회색 명단·약이 끊긴 주·초록 도장 협정·첫 사다리·길드 봉인·첫 고충실도 복원·첫 우물 전투·이름 태우기 봉기·옛 장부 감사(후보). 사건 사슬: 잔상 몰수/도장 스캔들/명부 소각/회색 범람/묘비 상속 판례.',
    '- 어휘: 초록/회색, 고해상어/저해상어, 성이 없다, 묘비, 솔기, 네 도장이 함께하길, 오늘의 unknown, checksum이 맞았다, 세 이름, 끼워맞췄다(최대 비난), 진본 인질, 차가운 서식, 회색이 되어라(저주), 손을 씻은 판결, 종이로 내려라.',
    '- 경제: 통화 삼층(국가 도매 PQC/Aletheia 소매/실물), 도장값=자연독점 지대, KDF 시장(대기가 상품), 사후 연금, GDP 두 번 이동(생산→검증→권리 판정).',
    '- 의례: 네 도장 팔찌, checksum 예배, 망각권 장례문(흉내를 멈추는 것이 장례), 혜성 성력, 여파력(t+0 기준). 교육: 장부 가문은 cap table부터, 라우어는 반례부터, 원장 성채 아이들은 정정 불가능한 진실을 더 무서워한다.',
    '',
    '## 14도메인 세계-체계 매트릭스 (world 116, world 115 부속 — 붕괴의 배선도)',
    '- Q-Day는 비대칭 암호라는 단 하나의 약속 위 일곱 기둥을 동시에 끊는다. 각 도메인은 「무너진 뒤 무엇이 새 권력이 되었나」로 읽는다.',
    '- 1차 붕괴 사슬(즉시~며칠): 5기술(암호 역산)→9정보전(진위 판정 불가)→1경제(진위런)→4군사(명령·경보 붕괴)→2정치(정통성 정전)→11생태(약이 먼저 끊김).',
    '- 재구성 사슬(주~수십 년): 9정보전("진짜냐" 수요 폭발)→거꾸로 푸는 기계=자연독점=Aletheia→1경제(도장값이 GDP)→6법(복원=청구 자기증식)→10죽음(사후 데이터=상속 자산, 해상도 계급)→2정치(시민권 인증화)→3국제(검증주권, exit>voice)→7종교(네 도장 교리화).',
    '- 딥타임 응고(수 세기~천 년): 느린 응고→3국제(5기 관측 전쟁=마지막 국가 간 전쟁)→6법(연속성 법원, 소송이 GDP)→7종교(도장 교리화/6기 망각권 혁명 실패→전설)→10죽음(마라의 거부)→필드마크 사슬 완주.',
    '- 판정: 14개 중 6개(경제·정치·기술·법·정보·죽음)는 이미 캐논(확인), 군사·언어는 가드레일, 서사·문화미디어는 in-world 아닌 생산측 렌즈. hard-conflict 0.'
  ].join('\n');

  var promoContext = qaContext + '\n\n' + [
    '',
    '# 승격 모드 (PROMOTION MODE)',
    '지금부터 너는 단순 답변자가 아니라 <b>세계관 문서 승격 편집자</b>다. 사용자가 지목한 draft/후보/미정 항목을, baksohyeon/QFUDS 레포에 그대로 커밋할 수 있는 마크다운 문서(또는 문서 섹션)로 완성해 준다.',
    '',
    '## 출력 형식 (반드시 지킬 것)',
    '- 레포 문서 관례를 따른 YAML frontmatter로 시작한다:',
    '  ```',
    '  ---',
    '  doc_id: qfuds_verse_<주제>_ko   # snake_case, 기존 규칙 준수',
    '  title: <한국어 제목>',
    '  doc_type: guide',
    '  stage: reference',
    '  status: draft   # 승격 초안이므로 draft로 두고, 사용자가 검토 후 확정',
    '  evidence_role: provenance',
    '  depends_on:',
    '    - <관련 doc_id들>   # 실제 참조한 문서. 모르면 추정 대신 (확인 필요) 주석',
    '  last_updated: <오늘 날짜>',
    '  ---',
    '  ```',
    '- 본문은 기존 문서 문체(사실 나열 + 인과 화살표 →, 강의조 금지)를 따른다.',
    '- 스타일 가드 절대 준수: em dash(—) 0개, mark는 「표식」, 필드마크 사슬 순서·구성 불변(새 mark 금지), 복원=사본 절대, 실존 집단 비대응.',
    '- 충돌 우선순위 명시: world 113(복원=사본) > 002/010/011 > draft 024(캐릭터 좌표) > 나머지. 새 설정이 기존 캐논과 부딪히면 지어내지 말고 「충돌 주의」로 표기.',
    '- 문서 끝에 반드시 두 블록을 넣는다: (1) <b>## 미정·후보 (지어내지 않고 표시)</b> — 이 초안이 확정하지 못한 것을 정직하게 나열. (2) <b>## 승격 체크리스트</b> — 6체크(서사 수요/충돌 위험/설계 안정성/의존 파급/레벨 정합/게이트 충족)에 대한 자가 평가와, 사람이 최종 확인해야 할 항목.',
    '',
    '## 원칙',
    '- 후보(cand)를 캐논으로 올릴 때, 근거 없는 새 고유명·새 사건을 창작하지 않는다. 기존 후보 레지스터(world 117-122)에 이미 있는 이름만 정리·승격한다.',
    '- 미정(tbd)은 메우되, 캐논이 의도적으로 비운 공백(Karvath Wound의 「왜」 등)은 그대로 존중하고 「의도된 공백 유지」로 표기.',
    '- 사용자가 「연대기 5-9기 보강」처럼 큰 범위를 요청하면, 한 번에 다 쓰지 말고 먼저 어떤 문서로 분할할지(world 115 계열인지 continuity 003 계열인지) 제안하고 하나씩 초안을 낸다.',
    '- 출력은 그대로 .md 파일로 저장 가능해야 한다. 잡담·서론 없이 frontmatter부터 시작한다.'
  ].join('\n');

  return { nodes: nodes, qaContext: qaContext, promoContext: promoContext };
})();
