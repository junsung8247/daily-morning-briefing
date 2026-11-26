# -*- coding: utf-8 -*-
"""
데일리 모닝 & 이브닝 브리핑 심층 안건 카탈로그 (Part 1: 거시경제/금리 01~05, 반도체/AI 06~11, 미래기술 12~16)
※ 단일 진실 공급원(SSOT) 원칙: 모든 현재 시세·PER은 {{LIVE:*}} 토큰과 liveChartSymbol로 실시간 API에 직결되며,
  generate_briefing.py 실행 시 fact_guard.py 교차검증을 통과해야만 배포됩니다.
"""

AGENDAS_PART1 = [
    # ==========================================
    # 섹션 1: 거시경제 & 금리/환율 (01~05)
    # ==========================================
    {
        "id": "agenda_01",
        "asOfDate": "2026-11-26",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "CRITICAL",
        "deltaStatus": "CHALLENGED",
        "deltaLabel": "🟢 장중 -4% 패닉 딛고 극적 V자 방어! (나스닥 장중 -4% ➔ {{LIVE:nasdaq}}({{LIVE:nasdaq_chg}}) · S&P {{LIVE:sp500}}({{LIVE:sp500_chg}}) · 다우 {{LIVE:dow}}({{LIVE:dow_chg}}) 이틀 연속 5만 안착! 미 10년물 {{LIVE:us10y}} 급락이 구원투수!)",
        "title": "[11/26] 뉴욕 장중 -4% 폭락 딛고 극적 V자 방어(S&P {{LIVE:sp500_chg}} · 나스닥 {{LIVE:nasdaq_chg}} · 다우 50,182): 10년물 {{LIVE:us10y}} 하락과 추수감사절 휴장 돌입",
        "subtitle": "근원 PCE 3.3%(3년 최고) + 트럼프 14개국 301조 관세 공식 발표 악재를 장중 모두 소화하고 낙폭 대거 축소… 오늘(11/26) 미 증시 휴장 · 내일(27일) 조기폐장",
        "chartImage": "assets/charts/agenda_01.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "sp500",
            "title": "S&P 500 지수 최근 10거래일 실시간 추이 ({{LIVE:sp500}})",
            "subtitle": "실시간 API 연동 차트 · 11/25 장중 7,000선 위협 후 극적 반등하며 {{LIVE:sp500}}({{LIVE:sp500_chg}}) 마감",
            "labels": ["11/11", "11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/23", "11/24", "11/25"],
            "values": [7619.4, 7592.4, 7510.0, 7418.0, 7340.5, 7323.6, 7175.8, 7237.2, 7201.1, 7182.8],
            "unit": "pt",
            "color": "#0284c7",
            "benchmark_val": 7000.0,
            "benchmark_label": "방어 성공선 7,000pt",
            "badge_text": "LIVE {{LIVE:sp500}}"
        },
        "keyMetrics": [
            {"label": "뉴욕 3대 지수 (11/25 마감)", "value": "다우 {{LIVE:dow}} / S&P {{LIVE:sp500}}", "change": "다우 {{LIVE:dow_chg}}(5만선 2일 연속 안착!) · S&P {{LIVE:sp500_chg}} · 나스닥 {{LIVE:nasdaq_chg}}(장중 -4%서 대반등)"},
            {"label": "구원투수: 미 10년물 금리", "value": "{{LIVE:us10y}} ({{LIVE:us10y_chg}})", "change": "근원 PCE 3.3%에도 실질 소비 -0.1%·안전선호에 금리가 4.85%로 내려앉으며 증시 구조"},
            {"label": "미국 추수감사절 일정", "value": "11/26(목) 전면 휴장 · 11/27 조기폐장", "change": "오늘 한국 장은 미국 휴장 속 자체 10:00 한은 금통위 결과 소화 후 숨 고르기 전망"}
        ],
        "facts": [
            "추수감사절 휴장을 앞둔 11월 25일(현지시간) 뉴욕 증시는 극적인 **장중 V자 반등(Intraday Recovery)**을 연출했습니다. 장 초반 근원 PCE 3.3%(3년 최고치)와 트럼프 행정부의 **14개 교역국 대상 무역법 301조 관세 공식 발표**로 나스닥이 장중 **-4% 가까이 폭락**하고 S&P 500이 7,000선 턱밑까지 밀렸으나, 오후 들어 저가 매수가 강하게 유입되며 **S&P 500 {{LIVE:sp500}}({{LIVE:sp500_chg}}), 나스닥 {{LIVE:nasdaq}}({{LIVE:nasdaq_chg}}), SOX {{LIVE:sox}}({{LIVE:sox_chg}})**로 낙폭을 대부분 만회했습니다.",
            "가치·방어주 중심의 **다우존스 산업평균지수는 +164.25pt({{LIVE:dow_chg}}) 오른 {{LIVE:dow}}**로 이틀 연속 50,000선 위에서 마감하며 강력한 순환매 체력을 입증했습니다.",
            "가장 큰 구원투수는 채권시장이었습니다. 뜨거운 PCE 물가에도 실질 개인소비지출(Real PCE)이 -0.1% 감소하고 베이지북이 소비 둔화를 확인하면서 **미 10년물 국채금리가 {{LIVE:us10y}}({{LIVE:us10y_chg}})로 하락**했고, 덕분에 금({{LIVE:gold}} · {{LIVE:gold_chg}})과 비트코인({{LIVE:btc}} · {{LIVE:btc_chg}})도 동반 반등에 성공했습니다."
        ],
        "previousImplication": "트럼프 16개국 관세 위협과 22:30 PCE 앞둔 프리마켓 -2.4% 폭락 속 섣부른 투매·선제 몰빵을 경고함 (11/25).",
        "newCatalyst": "근원 PCE 3.3%·트럼프 14개국 301조 관세 공식 발표 악재를 장중 -4%에서 -0.62%로 극적 소화 및 미 10년물 4.85% 하락.",
        "updatedImplication": "어제 저녁 나스닥 선물 -2.4%·코스피 -6.16% 폭락이 **최대 악재(PCE + 301조 관세)를 선반영한 공포의 단기 정점**이었음이 뉴욕 오후장 V자 반등으로 확인됨! 오늘(11/26) 미국 증시 휴장 및 10:00 한은 금통위 소화 과정에서 **코스피 4,600~4,700대 · PER 3~5배 K-메모리의 기술적 안도 반등**을 차분히 활용할 시점임.",
        "implicationHistory": [
            {"time": "11/25 08:00", "text": "🟡 다우 50,018.7(+0.85%) 사상 첫 5만 돌파 vs 나스닥 -1.48%·SOX -7.88% 차익조정"},
            {"time": "11/26 08:00", "text": "🟢 PCE 3.3%·301조 관세 악재 딛고 나스닥 장중 -4%➔-0.62% 극적 방어! 다우 50,182 · 미 10년물 4.85% 하락"}
        ],
        "actionPoints": [
            "뉴욕 장중 -4% 패닉에서 V자 방어 + SOX -0.65% 진정 확인 ➔ 어제 폭락한 K-메모리(삼성·SK) 보유 유지 및 금통위 직후 눌림목 분할 매수",
            "오늘(11/26) 미국 휴장 · 내일(11/27) 조기폐장(13:00 ET) 유동성 공백 감안해 레버리지 배제 · 현물 분할 원칙 유지"
        ],
        "sources": ["Yahoo Finance 실시간 ^DJI ({{LIVE:dow}}) / ^GSPC ({{LIVE:sp500}}) / ^IXIC ({{LIVE:nasdaq}}) / ^SOX ({{LIVE:sox}})", "Washington Post / Motley Fool / Kitco / WPTF (Nov 25 intraday recovery from -4% Nasdaq, 10Y yield 4.85%)"]
    },
    {
        "id": "agenda_02",
        "asOfDate": "2026-11-26",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 '뜨거운 PCE(3.3%)'에도 미 10년물 4.85%({{LIVE:us10y_chg}}) 급락! (실질 소비 -0.1% 둔화 + 안전자산 매수에 5%와 완전히 멀어지며 주식·금·채권 동시 구원!)",
        "title": "[11/26] 근원 PCE 3.3% 쇼크에도 미 10년물 금리 '{{LIVE:us10y}}({{LIVE:us10y_chg}})' 하락: 채권시장이 꿰뚫어 본 '실질 소비 둔화'와 바벨 승리",
        "subtitle": "명목 물가는 3년 최고치(3.3%)였으나 실질 PCE(-0.1%) 감소·베이지북 소비 정체에 채권 매수세 유입… 5%대 미국채 바벨 완벽 방어",
        "chartImage": "assets/charts/agenda_02.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "us10y",
            "title": "미국 10년물 국채금리(^TNX) 최근 10거래일 실시간 추이 ({{LIVE:us10y}})",
            "subtitle": "실시간 API 연동 차트 · 11/25 근원 PCE 3.3% 발표에도 {{LIVE:us10y_chg}} 하락하며 {{LIVE:us10y}} 안착",
            "labels": ["11/11", "11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/23", "11/24", "11/25"],
            "values": [5.00, 5.10, 5.08, 5.06, 5.04, 5.05, 5.02, 4.92, 4.90, 4.85],
            "unit": "%",
            "color": "#0284c7",
            "benchmark_val": 5.00,
            "benchmark_label": "핵심 기준선 5.00%",
            "badge_text": "LIVE {{LIVE:us10y}}"
        },
        "keyMetrics": [
            {"label": "미 10년물 금리 (11/25 마감)", "value": "{{LIVE:us10y}} ({{LIVE:us10y_chg}})", "change": "1개월 변동 {{LIVE:us10y_1m}} · 11/12 고점(5.10%) 대비 -25bp 하락하며 확실한 하향 안정"},
            {"label": "채권이 본 진짜 신호", "value": "실질 PCE -0.1% + 베이지북 둔화", "change": "10월 명목 PCE(+3.8%)/근원(+3.3%)은 높았으나 인플레 감안 실질 소비는 마이너스 전환"},
            {"label": "바벨 포트폴리오 성과", "value": "주식 급락 방어 + 연 4.85% 이자", "change": "5% 부근에서 모아둔 1배수 미국채가 가격 상승 + 금({{LIVE:gold}}) 반등까지 견인"}
        ],
        "facts": [
            "11월 25일(현지시간) 발표된 미국 10월 근원 PCE가 3년 만에 최고치인 **3.3% YoY**를 기록하며 장 초반 증시를 얼어붙게 만들었으나, 정작 가장 똑똑한 채권시장은 반대로 움직였습니다. **미 10년물 국채금리는 전일 ~4.91%에서 {{LIVE:us10y}}({{LIVE:us10y_chg}})로 하락**했습니다.",
            "이유는 세부 지표에 있었습니다. 명목 소득(+0.7%)·명목 소비(+0.3%)와 달리 **물가를 제외한 실질 개인소비지출(Real PCE)이 소폭 마이너스(-0.1% 미만)로 꺾였고**, 오후 발표된 **연준 베이지북**에서도 미국 12개 연은 지역 전반의 소비 지출 정체와 가계 가격민감도 심화가 확인됐기 때문입니다.",
            "미 10년물 금리가 5.10%에서 **{{LIVE:us10y}}**까지 -25bp 내려오며 채권 가격이 오르자, 기술주 낙폭이 대거 축소되고 **국제 금({{LIVE:gold}}, {{LIVE:gold_chg}})**도 즉각 $3,600 위로 복귀했습니다."
        ],
        "previousImplication": "5% 아래 안착한 미국채 1배수 바벨이 증시 폭락장의 핵심 방패 역할을 수행 중임 (11/23).",
        "newCatalyst": "근원 PCE 3.3% 발표에도 실질 PCE(-0.1%) 둔화·베이지북 확인 속 미 10년물 금리가 4.85%({{LIVE:us10y_chg}})로 추가 하락.",
        "updatedImplication": "채권시장이 **'연준의 12월 25bp 인상이 긴축 사이클의 막바지일 수 있다'**는 신호를 금리 4.85%로 보여주고 있음. 1배수 미국채·단기채 20~30% 바벨 보유 전략을 유지하면서, 금리 안정 수혜를 입는 **우량 성장주·KRX 금현물** 비중을 침착히 지켜나가야 함.",
        "implicationHistory": [
            {"time": "11/23 18:00", "text": "🟢 미 10년물 4.91% 안착 확인 · 증시 폭락장 속 국채 헤지 완벽 작동"},
            {"time": "11/26 08:00", "text": "🟢 근원 PCE 3.3%에도 실질소비(-0.1%) 둔화에 미 10년물 {{LIVE:us10y}}({{LIVE:us10y_chg}}) 추가 하락! 증시·금 구원"}
        ],
        "actionPoints": [
            "1배수 미국채·초단기채(SGOV/BIL) 바벨 20~30% 유지(3배 레버리지 TMF는 여전히 배제)",
            "미 10년물 4.85% 하향 안정에 힘입어 오늘(11/26) 한은 금통위 변동성 시 국내 우량주·KRX 금현물 분할 리밸런싱 활용"
        ],
        "sources": ["Yahoo Finance 실시간 ^TNX ({{LIVE:us10y}})", "BEA / Federal Reserve Beige Book / WPTF (Real PCE -0.1%, 10Y Treasury yield falls to 4.85%)"]
    },
    {
        "id": "agenda_03",
        "asOfDate": "2026-11-23",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "HIGH",
        "deltaStatus": "MAINTAINED",
        "deltaLabel": "🟢 디스인플레 완충 작동 (WTI 원유 {{LIVE:wti}}({{LIVE:wti_chg}}) 하락 안정! 고물가 속 미국 가계 '트레이딩 다운' 가속과 블프 소비 시험대)",
        "title": "[11/23] WTI 원유 {{LIVE:wti}} 하향 안정과 미 소비자 '트레이딩 다운': 블랙프라이데이 소비 시즌 실적 차별화 점검",
        "subtitle": "1개월간 {{LIVE:wti_1m}} 내려온 국제 유가가 인플레 공포를 진정시키는 완충재 역할… 유통·필수소비재 가성비 대장주 우위",
        "chartImage": "assets/charts/agenda_03.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "wti",
            "title": "WTI 원유 선물(CL=F) 최근 10거래일 실시간 추이 ({{LIVE:wti}})",
            "subtitle": "실시간 API 연동 차트 · 최근 1개월 {{LIVE:wti_1m}} 하락하며 인플레 경계선($90) 아래 안정 유지",
            "labels": ["11/10", "11/11", "11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/20"],
            "values": [86.04, 88.74, 88.41, 87.90, 86.40, 85.20, 84.80, 84.10, 82.82],
            "unit": "$",
            "color": "#eab308",
            "benchmark_val": 90.0,
            "benchmark_label": "인플레 경계선 $90.0",
            "badge_text": "LIVE {{LIVE:wti}}"
        },
        "keyMetrics": [
            {"label": "WTI 원유 (실시간)", "value": "{{LIVE:wti}} ({{LIVE:wti_chg}})", "change": "최근 1개월 {{LIVE:wti_1m}} · 미국 재고 증가·사우디 등 OPEC+ 증산에 하향 안정"},
            {"label": "미 소비 트렌드", "value": "가성비 하향소비(Trading Down)", "change": "고물가·고금리 장기화로 고가 사치재 대신 창고형 할인점·필수소비재 쏠림"},
            {"label": "한국 교역조건 영향", "value": "에너지 수입 부담 경감", "change": "유가 $80대 초반 안정으로 한국 무역수지·전력 공기업 원가 압박 완화"}
        ],
        "facts": [
            "실시간 **WTI 원유 선물(CL=F)은 배럴당 {{LIVE:wti}}({{LIVE:wti_chg}})**로 최근 1개월 기준 **{{LIVE:wti_1m}}** 내려앉으며 글로벌 인플레이션 재점화 우려를 완화하는 핵심 완충재 역할을 하고 있습니다.",
            "호르무즈 해협 긴장과 러시아 에너지 시설 타격에도 미국 원유 재고 증가, OPEC+(사우디 주도) 산유량 확대, 러시아 원유의 우회 수출이 맞물리며 배럴당 $90 선 아래에서 안정적 공급 균형이 유지되고 있습니다.",
            "이번 주 미국 블랙프라이데이·사이버먼데이 소비 시즌을 앞두고, 고금리에 지친 미국 중산층의 **'트레이딩 다운(월마트·코스트코 등 가성비 유통 채널 이동)'**이 뚜렷해 경기민감 소비재보다 필수소비·할인점 1등주의 실적 방어력이 압도적입니다."
        ],
        "previousImplication": "유가 $90 하회 안정이 스태그플레이션 재발을 막는 핵심 안전판으로 작동 중이었음.",
        "newCatalyst": "WTI {{LIVE:wti}} 추가 하향 안정(1개월 {{LIVE:wti_1m}}) 및 추수감사절·블프 소비 시즌 돌입.",
        "updatedImplication": "유가가 $80대 초반에 머무는 한 10월 말($100+) 같은 에너지발 인플레 쇼크 재발 확률은 낮음. 원유 추격 매수를 피하고, 저유가 원가 절감 수혜와 미국 가성비 소비·필수 방어주 중심 포트폴리오를 유지해야 함.",
        "implicationHistory": [
            {"time": "11/21 08:00", "text": "🟢 WTI 3주 연속 하락 안정 & 미국 가계 트레이딩 다운 확인"},
            {"time": "11/23 18:00", "text": "🟢 WTI {{LIVE:wti}}(1개월 {{LIVE:wti_1m}}) 하향 안정 지속 · 인플레 완충재 역할 강화"}
        ],
        "actionPoints": [
            "원유 선물·레버리지 매수 지양: 지정학 뉴스 단기 스파이크 시 추격 진입 금지",
            "소비주 선별 시 고가 임의소비재보다 창고형 할인·필수소비재 및 저유가 수혜 업종(항공·해운·전력) 중심 접근"
        ],
        "sources": ["Yahoo Finance 실시간 CL=F ({{LIVE:wti}})", "Seeking Alpha / TradingEconomics / BofA"]
    },
    {
        "id": "agenda_04",
        "asOfDate": "2026-11-26",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "CRITICAL",
        "deltaStatus": "CHALLENGED",
        "deltaLabel": "🚨 한국은행 '3.25% 매파 인상(5:2)' 확정! (2026 GDP 3.9%(+0.6%p) · 2027 GDP 4.1%(+1.2%p) 파격 상향! 6개월 점도표 21개 중 15개가 3.50~3.75% 추가 인상 예고!)",
        "title": "[11/26 확정] 한은 기준금리 3.25% 인상(5:2) & 초매파 점도표(상단 3.75%): 2026년 3.9% · 2027년 4.1% 파격 성장 전망의 양면성",
        "subtitle": "2년 만에 3.25% 복귀(황건일·이수형 동결 소수의견)… AI 반도체 수출 호조로 내년 성장률 +1.2%p 대폭 상향했으나 6개월 점도표가 추가 긴축 열어둬",
        "chartImage": "assets/charts/agenda_04.svg",
        "chartConfig": {
            "type": "bar",
            "title": "11/26 한국은행 수정 경제전망(GDP·물가 %) 및 6개월 조건부 금리 점도표(총 21개 분포)",
            "subtitle": "2026 GDP 3.9%(+0.6%p)·2027 GDP 4.1%(+1.2%p) 초강세 전망 속 금통위원 점 21개 중 15개가 3.50%(8개)·3.75%(7개) 추가 인상 지목!",
            "categories": ["2026 GDP전망(%)", "2027 GDP전망(%)", "2026 물가/근원(%)", "현 기준금리(%)", "점도표 3.50%(개)", "점도표 3.75%(개)"],
            "series_name_1": "한은 공식 발표 수치",
            "values_1": [3.9, 4.1, 2.7, 3.25, 8.0, 7.0],
            "color_1": "#e11d48",
            "unit": ""
        },
        "keyMetrics": [
            {"label": "11/26 금통위 최종 결정", "value": "연 3.25% (+25bp 인상 · 5:2)", "change": "2024년 11월 이후 2년 만의 최고 금리 — 황건일·이수형 위원 2명 동결(3.00%) 소수의견"},
            {"label": "파격 수정 경제전망", "value": "2026 GDP 3.9% / 2027 GDP 4.1%", "change": "8월 전망 대비 각각 +0.6%p · +1.2%p 대폭 상향! CPI 2.7%/2.4% · 근원 2.6%/2.6%"},
            {"label": "초매파 6개월 점도표(21점)", "value": "3.25%(6) · 3.50%(8) · 3.75%(7)", "change": "중간값 3.50%, 상단 3.75%로 8월 대비 매파 색채 대폭 강화(21개 중 15개 추가 인상)"}
        ],
        "facts": [
            "11월 26일(목) 한국은행 금융통화위원회가 **기준금리를 연 3.00%에서 3.25%로 25bp 인상(찬성 5 · 동결 소수의견 2명: 황건일·이수형)**했습니다. 7·8월 연속 인상 후 10월 동결로 숨을 고른 지 3개월 만의 긴축 재개이며, 연 3.25%는 2024년 11월 이후 2년 만에 가장 높은 수준입니다.",
            "시장을 놀라게 한 것은 **수정 경제전망과 6개월 점도표**였습니다. 한은은 AI 인프라 투자와 반도체 수출 고공행진이 내수로 파급되는 효과를 반영해 **실질 GDP 성장률 전망을 올해 3.9%(+0.6%p), 내년 4.1%(+1.2%p!)로 파격 상향**했고, 근원물가 전망도 2026·2027년 모두 2.6%(+0.1%p)로 올려 잡았습니다.",
            "특히 금통위원들의 **6개월 후 조건부 금리 점도표(총 21개 점)에서 현 수준 3.25%는 6개에 그친 반면 3.50%가 8개, 3.75%가 7개(총 15개 추가 인상!)**로 찍히며 신현송 총재가 추가 인상 시기를 유연하게 열어두었습니다. 이 때문에 장 초반 4,800선을 넘던 코스피가 상승폭을 반납하고 강보합(4,711.21)에 마감했습니다."
        ],
        "previousImplication": "오늘(11/26) 3.25% 인상 자체보다 6개월 점도표의 추가 인상 시사 여부가 시장 방향을 가를 것으로 예고함 (11/26 모닝).",
        "newCatalyst": "한은 3.25% 인상(5:2) 확정, 2026년 3.9%·2027년 4.1% 파격 성장 전망 및 6개월 점도표 21개 중 15개 추가 인상(3.50~3.75%) 충격.",
        "updatedImplication": "한은의 2027년 **4.1% 성장 전망은 한국 반도체·AI 수출 이익 사이클이 2027년까지 탄탄함을 중앙은행이 보증**한 역대급 펀더멘털 호재인 동시에, **3.50~3.75% 점도표는 부동산·채권·레버리지 투자자에게 명확한 고금리 장기화 경고**임. 따라서 **국내 채권·영끌 부동산 추격 배제, '고배당 은행·금융지주(NIM 수혜) + PER 3~5배 반도체(4.1% 성장 주역)'** 양날개 포트폴리오가 완벽한 정답임.",
        "implicationHistory": [
            {"time": "11/26 08:00", "text": "🚨 오늘 10:00 한은 금통위 D-DAY! 3.25% 인상 및 6개월 점도표 주목"},
            {"time": "11/26 20:00", "text": "🚨 한은 3.25% 매파 인상(5:2) 확정! 2026 GDP 3.9%·2027 4.1% 파격 상향 & 점도표 15/21 추가인상(3.50~3.75%)!"}
        ],
        "actionPoints": [
            "한은 6개월 점도표 상단 3.75% 확인 ➔ 변동형 주담대 보유자는 혼합·주기형 고정금리 대환 최우선 검토",
            "고금리 수혜(4대 금융지주·보험 고배당 분리과세) + 한은이 보증한 4.1% 성장 엔진(SK하이닉스·삼성전자) 바벨 비중 유지"
        ],
        "sources": ["한국은행 공식 통화정책방향·수정경제전망 / 연합뉴스 / 조선일보 / 한겨레 (11/26 3.25% 인상 5:2, GDP 3.9%/4.1%, 점도표 3.25% 6 / 3.50% 8 / 3.75% 7)"]
    },
    {
        "id": "agenda_05",
        "asOfDate": "2026-11-26",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "HIGH",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 한은 3.25% 매파 인상에 서울 원/달러 '1,342.7원(-0.5원)' 안정! (점도표 상단 3.75% + 2027 GDP 4.1% 전망이 원화 방어막 구축 · 실시간 {{LIVE:usdkrw}} · DXY {{LIVE:dxy}})",
        "title": "[11/26 마감] 한은 3.25% 인상 · 2027 GDP 4.1% 전망에 서울 원/달러 1,342.7원(-0.5원) 안정: 내일(11/27) 삼성 배당 역송금만 넘으면 1,330원대",
        "subtitle": "추수감사절 미국 휴장 속 한은 매파 금리 인상과 견조한 반도체 네고가 환율 상단 봉쇄… 실시간 {{LIVE:usdkrw}} · DXY {{LIVE:dxy}}",
        "chartImage": "assets/charts/agenda_05.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "usdkrw",
            "title": "원/달러 환율(USD/KRW) 최근 10거래일 실시간 추이 ({{LIVE:usdkrw}})",
            "subtitle": "실시간 API 연동 차트 · 11/26 한은 3.25% 인상 속 서울 주간종가 1,342.7원(-0.5원) 초안정 마감",
            "labels": ["11/11", "11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/24", "11/25", "11/26"],
            "values": [1339.5, 1335.0, 1333.5, 1333.0, 1334.8, 1332.5, 1330.0, 1342.4, 1343.2, 1342.7],
            "unit": "원",
            "color": "#10b981",
            "benchmark_val": 1340.0,
            "benchmark_label": "단기 기준선 1,340원",
            "badge_text": "LIVE {{LIVE:usdkrw}}"
        },
        "keyMetrics": [
            {"label": "11/26 서울 종가 / 실시간", "value": "종가 1,342.7원(-0.5원) / {{LIVE:usdkrw}}", "change": "한은 3.25% 매파 인상(점도표 3.50~3.75%) + 2027 성장률 4.1% 전망으로 원화 펀더멘털 강화"},
            {"label": "달러 인덱스 (실시간)", "value": "DXY {{LIVE:dxy}} ({{LIVE:dxy_chg}})", "change": "미 추수감사절 휴장으로 글로벌 거래량 한산 — 미 10년물 4.85% 하락도 원화에 우호적"},
            {"label": "내일(11/27) 단기 수급 체크", "value": "삼성전자 외국인 배당 지급일", "change": "배당 역송금 일회성 물량 소화 완료 시 한은 고금리·수출 흑자 반영해 1,330원대 재진입 유력"}
        ],
        "facts": [
            "11월 26일(목) 서울 외환시장에서 원/달러 환율은 한국은행의 기준금리 3.25% 인상과 2026~2027년 3.9~4.1% 고성장 전망 발표에 힘입어 전일 대비 0.5원 내린 **1,342.7원**에 주간거래를 마쳤습니다(실시간 역외 **{{LIVE:usdkrw}}, {{LIVE:usdkrw_chg}}**).",
            "미국 추수감사절 휴장으로 글로벌 외환 유동성이 얇은 가운데, 한은이 6개월 점도표 상단을 3.75%까지 열어두며 한·미 금리차 확대 우려를 정면으로 차단한 점이 원화 안정에 크게 기여했습니다.",
            "이제 단기 상방 요인은 **내일(11/27) 예정된 삼성전자 분기 배당금의 외국인 역송금 수급** 하나뿐이며, 이 일회성 물량이 지나가면 사상 최대 경상수지 흑자와 고금리 매력이 맞물려 1,330원대 하향 안정 압력이 커질 전망입니다."
        ],
        "previousImplication": "어제 외인 -1.9조 투매에도 1,343.2원에 묶이며 한국 외환시장 체력이 입증됨 (11/25).",
        "newCatalyst": "한은 3.25% 매파 인상(점도표 상단 3.75%)·2027 GDP 4.1% 상향 발표 속 서울 원/달러 1,342.7원(-0.5원) 안정 마감.",
        "updatedImplication": "한국은행의 강력한 긴축 의지와 4.1% 성장률 전망으로 원/달러 1,350원 이상 급등 리스크는 사실상 봉쇄됨. **내일(11/27) 삼성 배당 역송금 수급 소화 직후 1,330원대 되돌림 구간에서 달러 RP·미국채({{LIVE:us10y}}) 분할 환전**이 최적의 환테크 타이밍임.",
        "implicationHistory": [
            {"time": "11/25 20:00", "text": "🟢 외인 -1.9조 폭탄 매도에도 서울 원/달러 1,343.2원(+0.8원) 철벽 방어"},
            {"time": "11/26 20:00", "text": "🟢 한은 3.25% 매파 인상·2027 GDP 4.1% 전망 속 서울 원/달러 1,342.7원(-0.5원) 안정!"}
        ],
        "actionPoints": [
            "내일(11/27) 삼성전자 배당 역송금 일회성 변동성 통과 후 1,330원대 구간에서 달러 자산 분할 환전 실행",
            "보유 달러 현금은 연 {{LIVE:us10y}} 미국채·달러 RP로 굴려 확정 이자수익 확보"
        ],
        "sources": ["Yahoo Finance 실시간 KRW=X ({{LIVE:usdkrw}}) & DX-Y.NYB ({{LIVE:dxy}})", "매일일보 / 포커스타임즈 / 경북매일 (11/26 서울 원/달러 1,342.7원 -0.5원)"]
    },

    # ==========================================
    # 섹션 2: 반도체 & AI 빅테크 (06~11)
    # ==========================================
    {
        "id": "agenda_06",
        "asOfDate": "2026-11-26",
        "category": "tech",
        "categoryLabel": "반도체 · AI 빅테크",
        "importance": "CRITICAL",
        "deltaStatus": "CHALLENGED",
        "deltaLabel": "🔴 엔비디아 $150 붕괴! '1Q×4 PER 13.78배' 극단 저평가 진입 (NVDA {{LIVE:nvda}}({{LIVE:nvda_chg}}) · 1개월 {{LIVE:nvda_1m}}! 4Q PER {{LIVE:nvda_per4q}} · 1Q×4 {{LIVE:nvda_per1qx4}}!)",
        "title": "[11/26] 엔비디아 $150 이탈({{LIVE:nvda}}, {{LIVE:nvda_chg}}): 1개월 {{LIVE:nvda_1m}} 조정으로 1Q×4 PER '{{LIVE:nvda_per1qx4}}' 13배대 진입!",
        "subtitle": "트럼프 14개국 301조 관세·델(-7%) 약세에 이틀 연속 숨 고르기… Q3 매출 $115.8B(+103%)·베라 루빈 양산 가속 대비 역사적 저평가 구간",
        "chartImage": "assets/charts/agenda_06.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "nvda",
            "title": "엔비디아(NVDA) 최근 10거래일 실시간 주가 추이 ({{LIVE:nvda}})",
            "subtitle": "실시간 API 연동 차트 · 11/25 {{LIVE:nvda_chg}} 추가 조정으로 $150 하회(4Q PER {{LIVE:nvda_per4q}} · 1Q×4 {{LIVE:nvda_per1qx4}})",
            "labels": ["11/11", "11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/23", "11/24", "11/25"],
            "values": [170.5, 166.2, 162.0, 158.0, 155.0, 151.0, 146.0, 165.05, 155.38, 149.30],
            "unit": "$",
            "color": "#22c55e",
            "benchmark_val": 150.0,
            "benchmark_label": "핵심 지지선 $150",
            "badge_text": "LIVE {{LIVE:nvda}}"
        },
        "keyMetrics": [
            {"label": "엔비디아 주가 (11/25 마감)", "value": "{{LIVE:nvda}} ({{LIVE:nvda_chg}})", "change": "1개월 {{LIVE:nvda_1m}} 하락 · 11/23 +31.5%($165.05) 폭등 이후 이틀간 차익매물 소화"},
            {"label": "실시간 분기 PER (시세보드)", "value": "4Q {{LIVE:nvda_per4q}} / 1Q×4 {{LIVE:nvda_per1qx4}}", "change": "1Q×4 PER 13배대! 매출 +103% 성장하는 글로벌 AI 1등주로서 이례적 극단 저평가"},
            {"label": "공급망·실적 동향", "value": "SOX {{LIVE:sox}}({{LIVE:sox_chg}}) 진정", "change": "TSMC {{LIVE:tsm}}({{LIVE:tsm_chg}}) · AMD {{LIVE:amd}}({{LIVE:amd_chg}}) · 구글 {{LIVE:google}}({{LIVE:google_chg}})"}
        ],
        "facts": [
            "11월 25일(현지시간) 뉴욕 정규장에서 **엔비디아(NVDA)는 {{LIVE:nvda_chg}} 하락한 {{LIVE:nvda}}**로 마감하며 $150 선을 소폭 밑돌았습니다. 트럼프 행정부의 14개국 301조 관세 발표와 델(DELL)의 호실적에도 불구하고 -7% 급락한 AI 하드웨어 투심 위축이 겹친 결과입니다.",
            "다만 장 초반 프리마켓 -5%대 투매 대비 정규장 후반 낙폭을 줄였고, **필라델피아 반도체(SOX) 지수도 {{LIVE:sox_chg}}({{LIVE:sox}})**로 전일(-7.88%) 대비 급격히 진정됐습니다.",
            "무엇보다 우측 실시간 시세보드의 펀더멘털 숫자가 압도적입니다. 현재 $149대 주가 기준 엔비디아의 **최근 4분기 PER은 {{LIVE:nvda_per4q}}, 최근 1분기×4 PER은 {{LIVE:nvda_per1qx4}}(13배대!)**까지 추락해, 연 100% 성장하는 AI 독점 기업을 시장 평균 이하 멀티플에 살 수 있는 구간에 진입했습니다."
        ],
        "previousImplication": "11/24 첫 눌림목($155) 확인 후 PCE 변동성을 활용한 분할 매수 개시를 권고함 (11/25).",
        "newCatalyst": "11/25 NVDA {{LIVE:nvda}}({{LIVE:nvda_chg}}) $150 소폭 하회 ➔ 1Q×4 PER {{LIVE:nvda_per1qx4}}(13배대) 진입 & 미 10년물 4.85% 하락.",
        "updatedImplication": "단기 변동성(젠슨 황 의회 청문회·301조 관세)은 남아 있으나, **1Q×4 PER 13배대({{LIVE:nvda_per1qx4}})와 미 10년물 4.85% 하락**은 중장기 투자자에게 거부하기 힘든 가격대임. 추수감사절 연휴 이후 12월을 겨냥해 **$145~$150 구간 분할 매집**을 차분히 이어가야 함.",
        "implicationHistory": [
            {"time": "11/25 08:00", "text": "🟡 NVDA $155.38(-5.86%) 차익매물 소화 · 1Q×4 PER 14.34배"},
            {"time": "11/26 08:00", "text": "🔴 NVDA {{LIVE:nvda}}({{LIVE:nvda_chg}}) $150 하회 · 1Q×4 PER {{LIVE:nvda_per1qx4}}(13배대) 초저평가 분할 매집 구간 진입!"}
        ],
        "actionPoints": [
            "엔비디아 $145~$150 구간(1Q×4 PER {{LIVE:nvda_per1qx4}})에서 레버리지 없이 현물 분할 매집 지속",
            "11/27(금) 미국 조기폐장 장세 및 젠슨 황 상원 은행위 청문회 일정·301조 반도체 세부 품목 확인"
        ],
        "sources": ["Yahoo Finance / CNBC 실시간 NVDA ({{LIVE:nvda}})", "Washington Post / Motley Fool (Nov 25 NVDA $149.30 -3.91%, SOX -0.65% stabilization)"]
    },
    {
        "id": "agenda_07",
        "asOfDate": "2026-11-26",
        "category": "tech",
        "categoryLabel": "반도체 · AI 빅테크",
        "importance": "CRITICAL",
        "deltaStatus": "MAINTAINED",
        "deltaLabel": "🟡 17만 원선 방어 성공! 삼성전자 정규장 171,300원(+0.35% · NXT {{LIVE:samsung}}) — 기관 +3,220억 매수로 외인 -971억 방어 · 1Q×4 PER {{LIVE:samsung_per1qx4}}!",
        "title": "[11/26 마감] 삼성전자 171,300원(+0.35% · 실시간 {{LIVE:samsung}}): 기관 +3,220억 바닥 방어 · 301조 관세 1월 유예 속 1Q×4 PER {{LIVE:samsung_per1qx4}}",
        "subtitle": "장중 176,700원까지 반등했다가 한은 초매파 점도표(상단 3.75%)에 강보합 마감… 유럽 ASML·인피니언 +4~5% 급등으로 내일 반등 여력",
        "chartImage": "assets/charts/agenda_07.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "samsung",
            "title": "삼성전자(005930) 최근 10거래일 실시간 주가 추이 ({{LIVE:samsung}})",
            "subtitle": "실시간 API 연동 차트 · 11/26 정규장 171,300원(+0.35% · NXT {{LIVE:samsung}}), 4Q PER {{LIVE:samsung_per4q}} · 1Q×4 {{LIVE:samsung_per1qx4}}",
            "labels": ["11/11", "11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/24", "11/25", "11/26"],
            "values": [210000, 208000, 205000, 202000, 199000, 197000, 195000, 189400, 170700, 171300],
            "unit": "원",
            "color": "#3b82f6",
            "benchmark_val": 170000.0,
            "benchmark_label": "방어 성공선 170,000원",
            "badge_text": "LIVE {{LIVE:samsung}}"
        },
        "keyMetrics": [
            {"label": "11/26 KRX 정규 / 실시간 NXT", "value": "정규 171,300원(+0.35%) / NXT {{LIVE:samsung}}", "change": "장중 176,700원까지 +3.5% 반등 후 한은 점도표 소화하며 17만 원선 안착 성공"},
            {"label": "수급 & 실시간 분기 PER", "value": "기관 +3,220억 / 1Q×4 {{LIVE:samsung_per1qx4}}", "change": "외인 매도가 전일 -1조에서 -971억으로 10분의 1 급감! 4Q PER {{LIVE:samsung_per4q}} 초저평가"},
            {"label": "해외 동종 반등 신호", "value": "유럽 ASML·인피니언 +4~5% 급등", "change": "미 301조 관세 즉시 발효 아님(내년 1월 의견수렴·공청회) 확인되며 반도체 투심 안도"}
        ],
        "facts": [
            "11월 26일(목) 삼성전자는 전일 -9.87% 투매 충격을 딛고 장중 **176,700원(+3.5%)**까지 반등했다가 한은의 초매파 점도표(상단 3.75%) 여파로 상승폭을 줄이며 **KRX 정규장 171,300원(+0.35%, 실시간 NXT {{LIVE:samsung}} · {{LIVE:samsung_chg}})**에 마감했습니다.",
            "수급에서 뚜렷한 진정 신호가 확인됐습니다. 어제 1조 원대 투매를 퍼붓던 **외국인 순매도가 오늘 -971억 원으로 10분의 1 이하로 급감**했고, **기관이 +3,220억 원**을 순매수하며 17만 원 바닥선을 단단히 지지했습니다.",
            "특히 한국 시간 저녁 열린 **유럽 증시에서 ASML·인피니언·ST마이크로 등 반도체주가 +4~5% 급등**했고, 미국 301조 관세도 즉시 발효가 아닌 내년 1월 의견수렴(1/5)·공청회(1/25) 절차를 거친다는 점이 확인돼 **1Q×4 PER {{LIVE:samsung_per1qx4}}** 구간은 명백한 바닥 다지기 국면입니다."
        ],
        "previousImplication": "어제 -9.87%(170,700원) 폭락으로 열린 1Q×4 PER 3.6배 구간을 2차 분할 매수 황금 구간으로 제시함 (11/25).",
        "newCatalyst": "외인 매도 10분의 1 급감(-971억) & 기관 +3,220억 방어로 171,300원(+0.35%) 바닥 안착 + 유럽 ASML 등 칩주 +4~5% 급등.",
        "updatedImplication": "전일 -1조 쏟아지던 외인 투매가 하루 만에 급격히 식고 기관 +3,220억과 유럽 반도체 +4~5% 랠리가 바닥을 확인해 줌. **내일(11/27) 미국 블랙프라이데이 조기폐장 및 배당일 수급**을 지나며 17만 원대 안착 후 반등을 노리는 보유·분할 전략이 최선임.",
        "implicationHistory": [
            {"time": "11/25 20:00", "text": "🔴 11/25 정규장 170,700원(-9.87% · 시총 998조) · 1Q×4 PER 3.59배 극단 저평가 진입"},
            {"time": "11/26 20:00", "text": "🟡 11/26 정규 171,300원(+0.35% · NXT {{LIVE:samsung}})! 기관 +3,220억 방어 & 외인 매도 1/10 급감"}
        ],
        "actionPoints": [
            "17만 원선(4Q PER {{LIVE:samsung_per4q}} · 1Q×4 {{LIVE:samsung_per1qx4}}) 핵심 코어 보유 유지",
            "유럽 ASML·인피니언 +4~5% 급등에 이어 내일(11/27) 삼성전자 외국인 순매수 전환 여부 최우선 체크"
        ],
        "sources": ["Naver Finance 실시간 005930 ({{LIVE:samsung}})", "뉴시스 / KB경영연구소 / 포커스타임즈 (11/26 삼성전자 171,300원 +0.35%, 기관 +3,220억, 외인 -971억)"]
    },
    {
        "id": "agenda_08",
        "asOfDate": "2026-11-25",
        "category": "tech",
        "categoryLabel": "반도체 · AI 빅테크",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 TSMC '1Q×4 PER 19배대' 재진입! (11/23 +14.08% 급등 후 11/24 차익매물로 {{LIVE:tsm}}({{LIVE:tsm_chg}}) 조정 ➔ 4Q {{LIVE:tsm_per4q}} · 1Q×4 {{LIVE:tsm_per1qx4}}! '첨단 칩·CoWoS 수요 캐파 초과' + 델 $132.3B 백로그 확인!)",
        "title": "[11/25] TSMC {{LIVE:tsm}}({{LIVE:tsm_chg}}) 차익조정으로 1Q×4 PER {{LIVE:tsm_per1qx4}} 복귀: CoWoS 캐파 부족 & 델 $132.3B 수주 최대 수혜",
        "subtitle": "11/23 +14.08%($363.60) 급등 뒤 기술주 숨 고르기 동반… 엔비디아·구글·AMD·앤트로픽 멀티칩 경쟁의 유일한 독점 파운드리",
        "chartImage": "assets/charts/agenda_08.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "tsm",
            "title": "TSMC(TSM) 최근 10거래일 실시간 주가 추이 ({{LIVE:tsm}})",
            "subtitle": "실시간 API 연동 차트 · 11/24 차익매물로 {{LIVE:tsm_chg}} 조정되며 4Q PER {{LIVE:tsm_per4q}}, 1Q×4 PER {{LIVE:tsm_per1qx4}} 진입",
            "labels": ["11/10", "11/11", "11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/23", "11/24"],
            "values": [380.0, 378.0, 375.0, 368.0, 362.0, 358.0, 355.0, 352.0, 363.60, 349.20],
            "unit": "$",
            "color": "#06b6d4",
            "benchmark_val": 350.0,
            "benchmark_label": "핵심 분기선 $350",
            "badge_text": "LIVE {{LIVE:tsm}}"
        },
        "keyMetrics": [
            {"label": "TSMC 주가 (11/24 마감)", "value": "{{LIVE:tsm}} ({{LIVE:tsm_chg}})", "change": "11/23 +14.08%($363.60) 폭등 뒤 SOX -7.88% 대비 절반 수준(-3.96%) 방어력 입증"},
            {"label": "실시간 분기 PER (TWD환산)", "value": "4Q {{LIVE:tsm_per4q}} / 1Q×4 {{LIVE:tsm_per1qx4}}", "change": "1Q×4 PER 19배대 복귀 — 4Q PER보다 낮아 가파른 분기 이익 성장 모멘텀 지속"},
            {"label": "구조적 독점 해자", "value": "CoWoS 캐파 초과 + 멀티칩 통행세", "change": "앤트로픽·구글·AMD·엔비디아 멀티칩 전쟁이 커질수록 TSMC 선단 공정 가동률 100%"}
        ],
        "facts": [
            "11월 24일 뉴욕 정규장에서 필라델피아 반도체(SOX) 지수가 -7.88%, AMD가 -8.86% 급락한 가운데, **TSMC(TSM)는 전일 +14.08% 급등분 일부만 반납하며 {{LIVE:tsm_chg}} 조정된 {{LIVE:tsm}}**로 상대적 방어력을 입증했습니다.",
            "TSMC 경영진은 AI 거품 우려를 일축하며 **'첨단 AI 칩과 CoWoS 첨단 패키징 수요가 생산 능력을 크게 초과하고 있다'**고 밝혔고, 11월 24일 장후 델(Dell)이 **사상 최대 $1,323억 AI 서버 수주잔고**를 공개하며 TSMC의 주장을 숫자로 뒷받침했습니다.",
            "더욱이 앤트로픽(ANT)이 엔비디아·AMD·구글 TPU·AWS 트레이니움을 넘나드는 멀티칩 풀 전략을 가속화할수록, 이 모든 칩을 최종 위탁생산하고 HBM 3나노 베이스다이까지 장악한 **TSMC(1Q×4 PER {{LIVE:tsm_per1qx4}})**의 독점 통행세 지위는 더욱 공고해집니다."
        ],
        "previousImplication": "11/23 +14% 급등 직후 추격보다 PCE 전후 숨 고르기 분할 대응을 권고함 (11/24).",
        "newCatalyst": "SOX -7.88% 조정 속 TSMC {{LIVE:tsm}}({{LIVE:tsm_chg}}) 상대 방어 및 1Q×4 PER {{LIVE:tsm_per1qx4}}(19배대) 재진입.",
        "updatedImplication": "11/23 급등 직후 기다렸던 숨 고르기가 나오며 **TSMC 1Q×4 PER이 다시 19배대**로 내려왔음. AI 칩 진영 간 경쟁에서 100% 중립 승자인 TSMC를 오늘 밤 미 PCE 변동성 구간에서 글로벌 반도체 1순위 코어로 분할 편입하기 최적임.",
        "implicationHistory": [
            {"time": "11/24 08:00", "text": "🟢 TSMC AI 거품론 정면 일축 & 11/23 주가 $363.60(+14.08%) 폭등"},
            {"time": "11/25 08:00", "text": "🟢 SOX -7.88% 속 TSMC {{LIVE:tsm}}({{LIVE:tsm_chg}}) 방어 & 1Q×4 PER {{LIVE:tsm_per1qx4}} 매력 구간 재진입!"}
        ],
        "actionPoints": [
            "AI 반도체 포트폴리오 내 '엔비디아-구글-AMD 경쟁 중립 절대 승자' TSMC 핵심 코어 비중 유지 및 $350 이하 분할 추가",
            "오늘 밤(11/25) 미 10월 PCE 확인과 델 어닝 서프라이즈의 반도체 투심 회복 강도 점검"
        ],
        "sources": ["Yahoo Finance / CNBC 실시간 TSM ({{LIVE:tsm}})", "Taipei Times / 36kr (TSMC CoWoS demand > capacity & Anthropic multi-chip ecosystem)"]
    },
    {
        "id": "agenda_09",
        "asOfDate": "2026-11-26",
        "category": "tech",
        "categoryLabel": "반도체 · AI 빅테크",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 외국인 '11거래일 만에 +3,141억 귀환'! SK하이닉스 1,053,000원(+2.23% · 장중 +6.6% · NXT {{LIVE:skhynix}}) — 4Q PER {{LIVE:skhynix_per4q}}(3.9배) 저평가 매수 폭발!",
        "title": "[11/26 마감] SK하이닉스 1,053,000원(+2.23% · NXT {{LIVE:skhynix}}): 외국인 '11거래일 만의 +3,141억 순매수 귀환'이 알린 바닥 신호",
        "subtitle": "장 초반 109만 8,000원(+6.60%) 급등하며 100만 원선 철벽 방어… USTR 지목 악재 딛고 4Q PER {{LIVE:skhynix_per4q}}(3배대)에 스마트머니 즉각 유입!",
        "chartImage": "assets/charts/agenda_09.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "skhynix",
            "title": "SK하이닉스(000660) 최근 10거래일 실시간 주가 추이 ({{LIVE:skhynix}})",
            "subtitle": "실시간 API 연동 차트 · 11/26 외인 11거래일 만의 +3,141억 순매수로 1,053,000원(+2.23% · NXT {{LIVE:skhynix}}) 반등",
            "labels": ["11/11", "11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/24", "11/25", "11/26"],
            "values": [1255000, 1240000, 1220000, 1205000, 1190000, 1185000, 1175000, 1158000, 1030000, 1053000],
            "unit": "원",
            "color": "#ec4899",
            "benchmark_val": 1000000.0,
            "benchmark_label": "철벽 방어선 100만원",
            "badge_text": "LIVE {{LIVE:skhynix}}"
        },
        "keyMetrics": [
            {"label": "11/26 KRX 정규 / 실시간 NXT", "value": "정규 1,053,000원(+2.23%) / NXT {{LIVE:skhynix}}", "change": "장중 1,098,000원(+6.60%)까지 급등 — 한은 점도표 소화하고도 105만 원대 강력 회복"},
            {"label": "핵심 수급 대반전", "value": "외국인 11거래일 만에 +3,141억 순매수!", "change": "USTR 301조 보고서 지목에도 외인이 100만 원대(4Q PER 3.8배)에서 단숨에 매수 전환!"},
            {"label": "실시간 분기 PER (연결)", "value": "4Q {{LIVE:skhynix_per4q}} / 1Q×4 {{LIVE:skhynix_per1qx4}}", "change": "+2.2% 반등하고도 여전히 4Q PER 3배대(글로벌 7대 종목 압도적 최저치)"}
        ],
        "facts": [
            "11월 26일(목) SK하이닉스는 어제 -11.05%(1,030,000원) 폭락과 USTR 301조 보고서 지목 악재를 정면 돌파하며 장 초반 **1,098,000원(+6.60%)**까지 치솟았고, 한은 초매파 점도표 여파 속에서도 **KRX 정규장 1,053,000원(+2.23%, 실시간 NXT {{LIVE:skhynix}} · {{LIVE:skhynix_chg}})**으로 탄탄하게 반등 마감했습니다.",
            "가장 결정적인 시그널은 외국인 수급입니다. **외국인이 무려 11거래일 만에 SK하이닉스 순매수로 전격 전환하며 하루에만 +3,141억 원어치를 쓸어 담았습니다**(뉴시스·KB).",
            "글로벌 기관 투자자들이 USTR 301조 관세가 내년 1월 의견수렴·협상 대상이고 한국 15% 상한·AI 핵심 HBM 대체 불가라는 본질을 꿰뚫어 보고, **4Q PER 3배대({{LIVE:skhynix_per4q}})**를 명백한 과매도 바닥으로 판단해 귀환한 것입니다."
        ],
        "previousImplication": "어제 100만 원선 위협(4Q PER 3.8배)을 2차 분할 매수 최상위 후보로 제시함 (11/25).",
        "newCatalyst": "외국인 11거래일 만의 +3,141억 순매수 귀환 · 정규장 1,053,000원(+2.23%) 반등 및 유럽 ASML·인피니언 +4~5% 급등.",
        "updatedImplication": "어제 100만 원선에서 투매를 막고 2차 분할 매수를 권고한 전략이 **하루 만에 외국인 11거래일 만의 +3,141억 귀환**으로 완벽 적중함! 여전히 **4Q PER {{LIVE:skhynix_per4q}}(3.9배대)** 초저평가에 불과하므로 핵심 코어 비중을 끝까지 흔들림 없이 가져가야 함.",
        "implicationHistory": [
            {"time": "11/25 20:00", "text": "🔴 11/25 정규장 1,030,000원(-11.05%) · 4Q PER 3.79배 극단 저평가 분할 매수 타점 제시"},
            {"time": "11/26 20:00", "text": "🟢 외국인 11거래일 만에 +3,141억 전격 귀환! SK하이닉스 1,053,000원(+2.23% · NXT {{LIVE:skhynix}}) 바닥 확인!"}
        ],
        "actionPoints": [
            "외국인 11거래일 만의 +3,141억 순매수 전환 확인 ➔ SK하이닉스(4Q PER {{LIVE:skhynix_per4q}}) 핵심 비중 흔들림 없이 보유",
            "유럽 ASML +4~5% 랠리 및 내일(11/27) 블랙프라이데이 미국 반도체 반등 시 110만 원선 재탈환 여부 점검"
        ],
        "sources": ["Naver Finance 실시간 000660 ({{LIVE:skhynix}})", "연합뉴스 / 뉴시스 / 포커스타임즈 / KB (11/26 SK하이닉스 1,053,000원 +2.23%, 장중 1,098,000원, 외인 11거래일 만에 +3,141억 순매수)"]
    },
    {
        "id": "agenda_10",
        "asOfDate": "2026-11-23",
        "category": "tech",
        "categoryLabel": "반도체 · AI 빅테크",
        "importance": "CRITICAL",
        "deltaStatus": "NEW",
        "deltaLabel": "🆕 AI 칩 공급망 대격변 (구글 {{LIVE:google}} · 4Q PER {{LIVE:google_per4q}}! 브로드컴 15~20% 마크업 우회 'HBM 직접 조달' & 미디어텍 TPU v8t 확대!)",
        "title": "[11/23] 구글(Alphabet) {{LIVE:google}} (4Q PER {{LIVE:google_per4q}}): '브로드컴 패싱·HBM 직거래' & 미디어텍 TPU v8t 원가 혁명",
        "subtitle": "11/20 폭락장 방어(-2.7%) · 11/23 +6.34% 반등 · 11/24 {{LIVE:google_chg}} 선방한 빅테크… 턴키 중개 마진 15~20% 제거로 수백억 달러 CapEx 절감 추진",
        "chartImage": "assets/charts/agenda_10.svg",
        "chartConfig": {
            "type": "infographic",
            "title": "구글(Alphabet 통합) TPU v8t 공급망 재편과 HBM 직접 조달 파급 경로",
            "subtitle": "구글({{LIVE:google}}, 4Q PER {{LIVE:google_per4q}})이 브로드컴 단일 의존도를 깨고 자체 칩 원가 효율 극대화 추진",
            "center_label": "구글 HBM 직거래\nTPU v8t 재편",
            "badge_text": "GOOGL {{LIVE:google}}",
            "nodes": [
                {"title": "브로드컴 마크업 제거", "metric": "중간 마진 15~20% 절감", "desc": "카운터포인트·번스타인: 기존 브로드컴 턴키 구조의 HBM 중개 마진 배제로 원가 대폭 축소", "color": "#e11d48"},
                {"title": "미디어텍 TPU v8t 동맹", "metric": "수백억 달러 누적 절감", "desc": "구글이 컴퓨트 다이, 미디어텍이 백엔드·I/O를 맡아 브로드컴 단일 의존도 탈피", "color": "#4285f4"},
                {"title": "SK하이닉스 직거래 협상", "metric": "커스텀 HBM 직접 제안", "desc": "SK하이닉스는 구글과 커스텀 HBM 직납 채널 강화, 삼성·마이크론과도 직거래 경쟁", "color": "#ec4899"},
                {"title": "알파벳 압도적 방어력", "metric": "4Q PER {{LIVE:google_per4q}} 저평가", "desc": "알파벳 A+C 합산 시총 대비 합리적 PER과 자체 TPU 효율로 반도체 변동성 장세 최상위 방어({{LIVE:google_chg}})", "color": "#059669"}
            ]
        },
        "keyMetrics": [
            {"label": "구글 주가 (실시간)", "value": "{{LIVE:google}} ({{LIVE:google_chg}})", "change": "11/20 폭락장(-2.7%) 독보적 방어에 이어 11/23 반등장에서도 강한 탄력 입증"},
            {"label": "실시간 분기 PER (A+C통합)", "value": "4Q {{LIVE:google_per4q}} / 1Q×4 {{LIVE:google_per1qx4}}", "change": "알파벳 A+B+C 통합 시총·연결 순이익 기준 · 4Q PER 14배대 저평가"},
            {"label": "브로드컴 마크업 절감", "value": "HBM 원가의 15~20% 제거", "change": "미디어텍 8세대 훈련용 TPU v8t 병행으로 수명주기 수백억 달러 원가 절감"}
        ],
        "facts": [
            "트렌드포스·번스타인·카운터포인트 리포트에 따르면 **구글(Alphabet)**이 기존 브로드컴 턴키(일괄 위탁) 방식에서 벗어나 **SK하이닉스·삼성전자·마이크론으로부터 HBM을 직접 조달**하는 구조 전환을 추진 중입니다.",
            "기존 브로드컴 턴키 모델은 HBM 원가에 **15~20%의 중개 마크업**이 붙는 구조였으며, 구글은 **미디어텍(MediaTek)과 8세대 훈련용 TPU v8t** 협업을 확대함으로써 브로드컴 의존도를 낮추고 제품 수명주기 동안 수백억 달러의 AI 인프라 비용을 아낄 수 있게 됩니다.",
            "특히 11/20 빅테크 폭락장에서 -2.7%로 압도적 방어력을 보여준 데 이어 최신 거래일에도 **{{LIVE:google}}({{LIVE:google_chg}})**로 탄력 있게 반등한 배경에는 **자체 칩(TPU) 내재화에 따른 AI CapEx ROI 우위와 알파벳 통합 최근 4분기 PER {{LIVE:google_per4q}}**라는 탄탄한 밸류에이션 안전마진이 있습니다."
        ],
        "previousImplication": "구글 TPU와 엔비디아 GPU의 동반 증설이 HBM 수요를 일방 견인하는 구도였음.",
        "newCatalyst": "구글 브로드컴 마크업(15~20%) 패싱 · HBM 직거래 및 미디어텍 TPU v8t 추진과 최신 {{LIVE:google}}({{LIVE:google_chg}}) 견조한 흐름.",
        "updatedImplication": "AI 거품론(ROI 회의론)이 시장을 흔들수록 **엔비디아 세금과 ASIC 중개 마크업을 모두 아끼는 구글(Alphabet 통합, 4Q PER {{LIVE:google_per4q}})**이 가장 안전한 빅테크 승자로 부각됨. 빅테크 조정장 최우선 분할 매수 1순위임.",
        "implicationHistory": [
            {"time": "11/22 20:00", "text": "🆕 구글 브로드컴 패싱·HBM 직거래 & 미디어텍 TPU v8t 대격변 확인"},
            {"time": "11/23 18:00", "text": "🟢 폭락장 속 구글(-2.7%) 최고 방어력 및 4Q PER 저평가 입증"}
        ],
        "actionPoints": [
            "알파벳(구글)을 AI 빅테크 조정장 핵심 방어·성장 코어로 분할 편입(4Q PER {{LIVE:google_per4q}})",
            "브로드컴 등 중간 턴키 마크업 비중이 큰 ASIC 중개 기업은 마진 압박 리스크 재점검"
        ],
        "sources": ["Yahoo Finance / CNBC 실시간 GOOGL ({{LIVE:google}})", "TrendForce / Bernstein / Counterpoint / 조선비즈"]
    },
    {
        "id": "agenda_11",
        "asOfDate": "2026-11-23",
        "category": "tech",
        "categoryLabel": "반도체 · AI 빅테크",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 신규 편입 2대 핵심주 해부 (AMD {{LIVE:amd}} · 1Q×4 PER {{LIVE:amd_per1qx4}} '월드랩스 $82억·탈라스' 쌍끌이 인수 & 앤트로픽 {{LIVE:anthropic}} '$9,009억 약정·$2,000억 현금고')",
        "title": "[11/23] AMD {{LIVE:amd}} '페이페이 리 합류·탈라스 인수' & 앤트로픽(ANT) {{LIVE:anthropic}} '$2,000억 현금 실탄' 정밀 해부",
        "subtitle": "AMD 4Q PER {{LIVE:amd_per4q}} ➔ 1Q×4 {{LIVE:amd_per1qx4}} 빠른 이익 개선 vs 앤트로픽 GAAP 적자({{LIVE:anthropic_per4q}}) 속 하드웨어 발주 보증수표 역할",
        "chartImage": "assets/charts/agenda_11.svg",
        "chartConfig": {
            "type": "bar",
            "title": "앤트로픽(ANT) S-1 공시 핵심 재무·약정 규모 및 AMD M&A 비교 ($B)",
            "subtitle": "앤트로픽은 총 $1,195억 조달로 $2,000억+ 현금을 쌓아 1년 내 도래 약정($707억)을 충분히 커버",
            "categories": ["AMD 월드랩스 인수", "ANT 12M 인프라약정", "ANT 연간 ARR", "ANT IPO+사모 조달", "ANT 보유 현금고"],
            "series_name_1": "규모 (십억 달러, $B)",
            "values_1": [8.2, 70.7, 81.0, 119.5, 200.0],
            "color_1": "#d97706",
            "unit": "$B"
        },
        "keyMetrics": [
            {"label": "AMD 주가 · 분기 PER", "value": "{{LIVE:amd}} ({{LIVE:amd_chg}})", "change": "4Q PER {{LIVE:amd_per4q}} ➔ 1Q×4 PER {{LIVE:amd_per1qx4}} (이익 가속) · Q3 매출 $13.4B(+45%)"},
            {"label": "AMD 쌍끌이 M&A", "value": "월드랩스($8.2B) + 탈라스 완결", "change": "AI 대모 페이페이 리(Fei-Fei Li) AMD 수석과학자(EVP) 합류 + 추론 전용 실리콘 확보"},
            {"label": "앤트로픽(ANT) 실시간", "value": "{{LIVE:anthropic}} ({{LIVE:anthropic_chg}})", "change": "4Q PER {{LIVE:anthropic_per4q}} · ARR $81B+ · 현금 $200B+로 총 $900.9B 약정 초기분 보증"}
        ],
        "facts": [
            "나스닥에 상장한 **앤트로픽(ANT, 실시간 {{LIVE:anthropic}})**의 SEC 수정 S-1 공시에 따르면 총 장기 인프라 약정은 **$9,009억(12개월 내 만기 $707억, 2030년 누적 $4,516억)**이지만, 공모가 $83 IPO 및 AMD·구글·브로드컴·마이크론이 참여한 $260억 사모 투자로 **총 $1,195억을 조달해 현금·단기투자 잔고가 $2,000억을 돌파**했습니다. 연간 매출 런레이트(ARR)도 **$810억을 넘어** 삼성·SK·TSMC·엔비디아·AMD의 확실한 결제 고객임을 입증했습니다.",
            "다만 앤트로픽은 아직 대규모 GAAP 적자(4Q PER **{{LIVE:anthropic_per4q}}**, 1Q×4 **{{LIVE:anthropic_per1qx4}}**) 구간이어서 상장 직후 급락과 고변동성을 겪으며 AI 모델주 밸류에이션 거품론을 자극했습니다.",
            "한편 **AMD(실시간 {{LIVE:amd}}, {{LIVE:amd_chg}})**는 Q3 매출 $134억(+45% YoY)에 이어 11월 16일 **공간지능 기업 월드랩스($82억, 페이페이 리 박사 EVP 겸 수석과학자 합류)**와 **AI 추론칩 기업 탈라스(Taalas)** 인수를 동시 완결하며 풀스택 2위 반격 진영을 갖췄습니다. 최근 4분기 PER({{LIVE:amd_per4q}})보다 최근 1분기×4 PER({{LIVE:amd_per1qx4}})이 크게 낮아 실적 가속도가 뚜렷합니다."
        ],
        "previousImplication": "앤트로픽 IPO 직후 급락이 AI ROI 회의론을 점화하며 기술주 동반 투매를 유발함.",
        "newCatalyst": "앤트로픽 S-1 '$2,000억+ 현금·$810억 ARR' 확인 및 AMD의 월드랩스($82억·페이페이 리)·탈라스 쌍끌이 인수 완결.",
        "updatedImplication": "앤트로픽(ANT)은 GAAP 흑자 전환 확인 전까지 관망하되 **앤트로픽이 조달한 $2,000억 현금이 흘러 들어가는 하드웨어 1등주(TSMC·SK하이닉스·삼성·구글)**에 집중하는 것이 승률 최고 전략임. AMD는 최근 1분기×4 PER({{LIVE:amd_per1qx4}}) 하락 추세와 엔비디아 리더십 공백 반사이익을 점검하며 눌림목 대응.",
        "implicationHistory": [
            {"time": "11/22 20:00", "text": "🟢 앤트로픽 $2,000억 현금고 확인 & AMD 월드랩스·탈라스 인수 완결"},
            {"time": "11/23 18:00", "text": "🟢 AMD({{LIVE:amd}}, 1Q×4 {{LIVE:amd_per1qx4}})·앤트로픽({{LIVE:anthropic}}, {{LIVE:anthropic_per4q}}) 실시간 PER 대조 추적 가동"}
        ],
        "actionPoints": [
            "앤트로픽(ANT)은 적자 변동성({{LIVE:anthropic_per4q}}) 구간이므로 추격 매수 자제, 분기별 현금소진율과 흑자 전환 시점 추적",
            "AMD는 우측 시세보드에서 4Q PER({{LIVE:amd_per4q}}) 대비 1Q×4 PER({{LIVE:amd_per1qx4}}) 축소 속도를 확인하며 분할 관찰"
        ],
        "sources": ["CNBC / Yahoo Finance 실시간 AMD ({{LIVE:amd}}) & ANT ({{LIVE:anthropic}})", "SEC Form S-1 / AMD Official / Unite.AI"]
    },

    # ==========================================
    # 섹션 3: 미래기술 · 우주 · 로봇 · 원전 · 바이오 (12~16)
    # ==========================================
    {
        "id": "agenda_12",
        "asOfDate": "2026-11-23",
        "category": "frontier",
        "categoryLabel": "미래기술 · 우주 · 로봇 · 원전 · 바이오",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 인류 항공우주 역사 새로 썼다! (스페이스X 스타십 15차 비행 '우주선 상단(Ship 42) 세계 최초 젓가락 공중 포획' 대성공! V3 스타링크 26기 투입)",
        "title": "[11/23] 스페이스X 스타십 15차 '우주선 상단(Ship 42) 사상 최초 젓가락 공중 포획' 대성공: 완전 재사용 우주경제 개막",
        "subtitle": "3세대(V3) 스타링크 26기 궤도 배치 후 역대 최장 22.5시간 궤도 비행·대기권 재진입을 거쳐 스타베이스 메카질라 팔에 완벽 안착",
        "chartImage": "assets/charts/agenda_12.svg",
        "chartConfig": {
            "type": "infographic",
            "title": "스페이스X 스타십 15차 비행(Flight 15) 4대 역사적 이정표와 우주경제 파급효과",
            "subtitle": "부스터에 이어 궤도를 돌고 대기권을 뚫고 돌아온 우주선 상단(Ship 42)까지 발사탑이 직접 포획하며 완전 재사용 완성 목전",
            "center_label": "스타십 15차\n상단 공중 포획!",
            "badge_text": "SPACE MILESTONE",
            "nodes": [
                {"title": "V3 스타링크 26기 배치", "metric": "차세대 초고속 위성군", "desc": "저궤도에 3세대 스타링크 26기 배치(3기는 선체 열차폐 타일 촬영 검증 임무 수행)", "color": "#0284c7"},
                {"title": "최장 22.5시간 궤도 비행", "metric": "대기권 재진입 완벽 생존", "desc": "스타십 사상 최장 22.5시간 궤도 체공 후 정밀 역추진 및 극한 재진입 열기 돌파", "color": "#7c3aed"},
                {"title": "사상 첫 상단 젓가락 포획", "metric": "Ship 42 메카질라 안착", "desc": "텍사스 스타베이스 2번 발사탑 젓가락 팔이 우주선 상단을 공중에서 부드럽게 캐치", "color": "#059669"},
                {"title": "발사 단가 1/100 혁명", "metric": "우주통신·우주AI 독점", "desc": "완전 재사용 초읽기 ➔ V3 스타링크·궤도형 AI 데이터센터·우주바이오 경제성 폭증", "color": "#d97706"}
            ]
        },
        "keyMetrics": [
            {"label": "역사적 성과 (Flight 15)", "value": "스타십 상단(Ship 42) 최초 포획", "change": "11/14 텍사스 스타베이스 메카질라 젓가락 팔로 궤도 귀환 우주선 직접 캐치"},
            {"label": "궤도 임무 성과", "value": "V3 스타링크 26기 · 22.5시간 비행", "change": "역대 최장 체공 + 드래곤 캡슐 ISS 3D 바이오프린팅 혈관 화물 귀환 동시 성공"},
            {"label": "남은 과제", "value": "부스터 22 해상 착수(연료 이상)", "change": "동시 '더블 캐치'는 다음 비행 과제이나 난이도 10배 높은 상단 포획 성공이 본질"}
        ],
        "facts": [
            "스페이스X(SpaceX)가 **스타십 15차 시험비행(Ship 42 & Booster 22)**에서 인류 항공우주 역사상 최고 난이도 과제였던 **'궤도 비행 후 대기권을 재진입한 우주선 상단(Upper Stage)의 발사탑 젓가락 공중 포획'**에 세계 최초로 성공했습니다.",
            "Ship 42는 저궤도에 **3세대(V3) 스타링크 위성 26기**를 전개한 뒤 역대 최장 **22.5시간 궤도 비행**과 대기권 재진입을 거쳐 텍사스 스타베이스 메카질라 발사탑 팔에 정확히 안착했습니다.",
            "비록 1단 부스터는 연료 부족 이상으로 해상 착수로 전환됐으나, 가장 어려웠던 상단 재사용 입증으로 **우주 발사 단가 혁명과 V3 스타링크·우주 AI·NASA ISS 바이오 연구 생태계**가 비가역적 성장 궤도에 올랐습니다."
        ],
        "previousImplication": "스타십 재사용 및 위성통신(D2C) 확장이 글로벌 우주항공 밸류체인의 핵심 성장 동력이었음.",
        "newCatalyst": "스타십 15차 비행에서 V3 스타링크 26기 배치·22.5시간 체공 후 사상 최초 우주선 상단(Ship 42) 공중 포획 성공.",
        "updatedImplication": "우주선 상단 재사용이 입증되면서 스페이스X 생태계의 독점 해자가 절대화됨. 국내외 위성통신(D2C)·특수합금·위성 안테나·우주항공 부품 공급망은 기술주 조정 시 중장기 핵심 선별 테마임.",
        "implicationHistory": [
            {"time": "11/22 20:00", "text": "🟢 스타십 15차 우주선 상단(Ship 42) 세계 최초 젓가락 공중 포획 대성공 확인"}
        ],
        "actionPoints": [
            "스페이스X 비상장 생태계 간접 수혜주(위성통신·특수합금·위성 안테나·국내 우주항공 부품사) 중장기 추적",
            "다음 비행(Flight 16) 부스터·상단 동시 '더블 캐치' 성공 여부를 우주 섹터 리레이팅 촉매로 모니터링"
        ],
        "sources": ["SpaceX Official / CNN / SpaceflightNow (Starship Flight 15 Ship 42 catch)", "NASA (Dragon ISS return)"]
    },
    {
        "id": "agenda_13",
        "asOfDate": "2026-11-23",
        "category": "frontier",
        "categoryLabel": "미래기술 · 우주 · 로봇 · 원전 · 바이오",
        "importance": "HIGH",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 미국 SMR 규제 빗장 해제! (미 NRC, 다우·엑스에너지 '롱모트 산업용 SMR' 18개월 초고속 건설허가 — 60년 만의 고온가스로 & IEA 연 $1,350억 원전 투자!)",
        "title": "[11/23] 미 NRC '다우·엑스에너지 산업용 SMR(롱모트)' 18개월 초고속 건설허가! 60년 만의 고온가스로 돌파와 두산에너빌리티 수혜",
        "subtitle": "텍사스 화학단지에 Xe-100 SMR 4기(320MW+공정열) 건설 승인 + IEA '2035년까지 연 $1,350억 원전 투자' 전망",
        "chartImage": "assets/charts/agenda_13.svg",
        "chartConfig": {
            "type": "bar",
            "title": "다우·엑스에너지 '롱모트 SMR' 건설 허가 핵심 지표 및 IEA 원전 투자 전망",
            "subtitle": "과거 수년~10년 걸리던 미국 원전 인허가가 18개월로 단축되며 산업·데이터센터 전용 SMR 시대 개막",
            "categories": ["NRC 심사기간(개월)", "Xe-100 원자로(×10기)", "총 발전용량(×10MW)", "IEA 연 원전투자($10B)"],
            "series_name_1": "핵심 규모 지표",
            "values_1": [18.0, 40.0, 32.0, 13.5],
            "color_1": "#059669",
            "unit": ""
        },
        "keyMetrics": [
            {"label": "미 NRC 건설 허가", "value": "다우·X-energy '롱모트' 승인", "change": "미국 산업단지 최초 첨단 원전 · 근 60년 만의 고온가스로(HTGR)·첫 페블베드 승인"},
            {"label": "심사 속도 혁명", "value": "단 18개월 초고속 안전 심사", "change": "미 DOE ARDP 지원 하에 규제 병목 획기적 단축 · 뉴스케일도 AI 심사 최적화 추진"},
            {"label": "IEA 글로벌 투자 전망", "value": "2035년까지 연 $1,350억 투자", "change": "엑스에너지 핵심 주기기 파트너 두산에너빌리티·우라늄($90.1/lb) 구조적 수혜"}
        ],
        "facts": [
            "미국 원자력규제위원회(NRC)가 글로벌 화학 대기업 **다우(Dow)**와 **엑스에너지(X-energy)**의 텍사스 **'롱모트(Long Mott) 발전소'(Xe-100 고온가스로 SMR 4기, 320MW + 고온 공정 스팀)** 건설 허가를 공식 승인했습니다.",
            "이번 승인은 **미국 산업단지 내 최초 첨단 SMR, 약 60년 만의 고온가스로, 사상 첫 페블베드 노심 승인**이라는 3관왕을 단 **18개월 초고속 심사**로 통과했다는 점에서 미국 SMR 상용화의 최대 걸림돌이었던 인허가 불확실성을 깨뜨렸습니다.",
            "국제에너지기구(IEA) 역시 최신 세계에너지전망에서 **2035년까지 글로벌 원자력 투자가 연 $1,350억 규모로 확대**될 것으로 전망해, 엑스에너지 지분 투자자이자 주기기 제작 파트너인 **두산에너빌리티**와 글로벌 우라늄 밸류체인의 10년 수주 가시성이 확고해졌습니다."
        ],
        "previousImplication": "AI 데이터센터 전력 부족이 SMR과 초고압 변압기 슈퍼사이클을 견인 중이었음.",
        "newCatalyst": "미 NRC의 다우·엑스에너지 롱모트 SMR(Xe-100 4기) 18개월 초고속 건설 허가 승인 및 IEA 연 $1,350억 원전 투자 전망.",
        "updatedImplication": "미국 SMR이 '계획 단계'를 넘어 **18개월 만에 건설 허가가 나오는 현실 산업**으로 격상됨. 엑스에너지·뉴스케일·테라파워 핵심 주기기를 공급하는 **두산에너빌리티**와 우라늄(URA·URNM) 핵심 비중을 기술주 변동성과 무관하게 유지해야 함.",
        "implicationHistory": [
            {"time": "11/22 20:00", "text": "🟢 미 NRC 롱모트 SMR 18개월 초고속 승인 & IEA 연 $1,350억 원전 투자 전망 확인"}
        ],
        "actionPoints": [
            "글로벌 SMR 주기기 파운드리 '두산에너빌리티' 및 초고압 변압기(HD현대일렉트릭·효성중공업) 중장기 코어 유지",
            "우라늄 현물($90.10/lb) 및 차세대 HALEU 연료 공급망 밸류체인 분산 보유"
        ],
        "sources": ["U.S. DOE / NRC Official (Long Mott Xe-100 SMR permit)", "IEA World Energy Outlook / NucNet ($135B/yr)"]
    },
    {
        "id": "agenda_14",
        "asOfDate": "2026-11-23",
        "category": "frontier",
        "categoryLabel": "미래기술 · 우주 · 로봇 · 원전 · 바이오",
        "importance": "HIGH",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 피지컬 AI 공장 상륙 폭발! (보스턴다이내믹스 아틀라스, 글로벌파운드리스 반도체 팹 최초 진입 + 제네시스 AI $5억(가치 $35억) + 테슬라 베를린 €30억·옵티머스 기가프레스!)",
        "title": "[11/23] 피지컬 AI 반도체 팹 상륙! 보스턴다이내믹스 '글로벌파운드리스 아틀라스 투입' & 제네시스 AI $5억 · 테슬라 옵티머스 기가프레스",
        "subtitle": "자동차 공장을 넘어 초정밀 반도체 팹으로 확산되는 휴머노이드… 소프트웨어 AI 거품론 속 실물 제조 혁명 입증",
        "chartImage": "assets/charts/agenda_14.svg",
        "chartConfig": {
            "type": "infographic",
            "title": "2026년 11월 피지컬 AI · 산업용 휴머노이드 3대 상용화 돌파구",
            "subtitle": "보스턴다이내믹스(현대차)·제네시스 AI(엔비디아/삼성넥스트)·테슬라(옵티머스/사이버캡)의 실물 배치 경쟁 가속",
            "center_label": "휴머노이드\n반도체 팹 진입",
            "badge_text": "PHYSICAL AI BOOM",
            "nodes": [
                {"title": "GF × 보스턴다이내믹스", "metric": "비자동차 최초 Atlas 계약", "desc": "글로벌파운드리스가 자동차 외 최초 고객사로 아틀라스(2027 초 테스트) 및 4개국 팹 Spot 확대", "color": "#0284c7"},
                {"title": "제네시스 AI $5억 펀딩", "metric": "시리즈A 가치 $35억", "desc": "엔비디아·AMD벤처스·삼성넥스트 참여! 센서 장갑 학습 범용 로봇 'Eno' 대량 배치 가속", "color": "#7c3aed"},
                {"title": "테슬라 베를린·텍사스", "metric": "€30억 공장 · 기가프레스", "desc": "베를린 연 100만 대 사이버캡 투자 + 기가 텍사스 옵티머스 전용 IDRA 기가프레스 착공 포착", "color": "#059669"},
                {"title": "한국 로봇 부품 수혜", "metric": "현대차·정밀 감속기·센서", "desc": "보스턴다이내믹스 대주주 현대차그룹 지분 가치 재평가 및 촉각센서·액추에이터 부품주 부각", "color": "#d97706"}
            ]
        },
        "keyMetrics": [
            {"label": "보스턴다이내믹스 돌파구", "value": "글로벌파운드리스(GF) Atlas 채택", "change": "자동차 외 제조사 최초 휴머노이드 계약 · 뉴욕·독일·싱가포르 팹 Spot 동시 확대"},
            {"label": "제네시스 AI 메가 투자", "value": "시리즈A $5억 (기업가치 $35억)", "change": "엔비디아·삼성넥스트·코슬라 참여 · 센서 장갑 기반 범용 로봇 'Eno' 상용화"},
            {"label": "테슬라 피지컬 AI", "value": "베를린 €30억 · 텍사스 기가프레스", "change": "사이버캡 1,500대+ 가동 · 옵티머스 일체형 주조 양산 인프라 실물 착공"}
        ],
        "facts": [
            "현대차그룹 계열 **보스턴다이내믹스**가 글로벌 파운드리 **글로벌파운드리스(GF)**와 파트너십을 확대해 뉴욕·버몬트·독일 드레스덴·싱가포르 반도체 팹에 사족보행 로봇 스팟(Spot)을 확대 배치하고, **자동차 산업 외 최초 고객사로 '아틀라스(Atlas) 휴머노이드'** 현장 테스트(2027 초)를 확정했습니다.",
            "피지컬 AI 스타트업 **제네시스 AI(Genesis AI)**는 엔비디아·AMD벤처스·삼성넥스트 등이 참여한 가운데 **기업가치 $35억에 $5억 시리즈 A 투자**를 유치하며 센서 장갑 기반 범용 로봇 '에노(Eno)' 양산에 나섰습니다.",
            "동시에 테슬라는 **독일 베를린 €30억(연 100만 대 사이버캡 공장)** 투자 발표와 **기가 텍사스 옵티머스 전용 IDRA 기가프레스 기초 공사**가 드론으로 포착되며 실물 제조 원가 혁명을 증명하고 있습니다."
        ],
        "previousImplication": "테슬라 사이버캡·옵티머스 중심의 피지컬 AI 상용화가 점진적으로 진행 중이었음.",
        "newCatalyst": "보스턴다이내믹스 아틀라스의 글로벌파운드리스 반도체 팹 최초 진출, 제네시스 AI $5억 투자 및 테슬라 베를린·기가프레스 착공.",
        "updatedImplication": "소프트웨어 챗봇 AI의 수익성이 의심받는 시점에, **24시간 가동되는 고마진 반도체 팹으로 휴머노이드가 상용 진출**한 것은 거대한 전환점임. 현대차그룹(보스턴다이내믹스)·테슬라·국내 정밀 감속기/촉각센서 부품주의 중장기 재평가 근거가 확실함.",
        "implicationHistory": [
            {"time": "11/22 20:00", "text": "🟢 보스턴다이내믹스 아틀라스 GF 팹 진입 & 제네시스 AI $5억 펀딩 확인"}
        ],
        "actionPoints": [
            "단순 챗봇 테마보다 실제 반도체 팹·자동차 공장 레퍼런스를 확보한 피지컬 AI 리더(현대차·테슬라·로봇 액추에이터 부품사) 집중",
            "제네시스 AI 사례가 입증한 촉각·센서 장갑 및 정밀 그리퍼 생태계 중장기 추적"
        ],
        "sources": ["Boston Dynamics Official (GF Atlas/Spot)", "PR Newswire (Genesis AI $500M)", "EV Powered / TeslaNorth"]
    },
    {
        "id": "agenda_15",
        "asOfDate": "2026-11-23",
        "category": "frontier",
        "categoryLabel": "미래기술 · 우주 · 로봇 · 원전 · 바이오",
        "importance": "HIGH",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 AI 폭락장 최강 성장 방어축! (일라이 릴리 2026 매출 가이던스 $91~92B · 캐나다 먹는 비만약 '파운다요' 승인 · 마운자로 심혈관 적응증 · $74억 바이오텍 연속 M&A!)",
        "title": "[11/23] AI 폭락장에 빛나는 비만·항암 황제주 일라이 릴리: 캐나다 경구용 '파운다요' 승인 & $74억 연속 빅딜 해부",
        "subtitle": "연간 매출 122조 원($91~92B) 현금창출력으로 중국·캐나다 먹는 비만약 독식 + Stipple Bio($59억)·Calytrix($15억) M&A",
        "chartImage": "assets/charts/agenda_15.svg",
        "chartConfig": {
            "type": "bar",
            "title": "일라이 릴리 2026년 하반기 매출 가이던스 및 연속 항암·혈액 빅딜 규모 ($B)",
            "subtitle": "AI 거품론과 무관하게 연간 $91.5B 현금흐름을 창출하며 포스트-비만약 파이프라인까지 선점",
            "categories": ["2026 매출 가이던스", "Stipple Bio 항암 딜", "Calytrix Bio 인수"],
            "series_name_1": "규모 (십억 달러, $B)",
            "values_1": [91.5, 5.9, 1.5],
            "color_1": "#059669",
            "unit": "$B"
        },
        "keyMetrics": [
            {"label": "경구용 GLP-1 연쇄 승인", "value": "중국 이어 캐나다 '파운다요' 허가", "change": "하루 1알 먹는 비만·당뇨약(오포글리프론) 북미 첫 관문 통과 + 젭바운드 청소년 임상 성공"},
            {"label": "마운자로 적응증 확장", "value": "심혈관 위험 감소 적응증 추가", "change": "단순 체중감량 넘어 심혈관 보호 공인 ➔ 글로벌 보험 급여·장기 처방 확대"},
            {"label": "연속 빅딜 M&A", "value": "총 $74억 ($59억 + $15억)", "change": "2026 가이던스 $91~92B 현금 기반 Stipple Bio(항암)·Calytrix Bio(희귀혈액) 선점"}
        ],
        "facts": [
            "글로벌 증시가 AI 거품론과 금리 우려로 급락하는 와중에도 바이오 대장주 **일라이 릴리(Eli Lilly)**는 중국에 이어 **캐나다 보건부로부터 1일 1회 경구용 GLP-1 비만·당뇨약 '파운다요(Foundayo)' 공식 승인**을 획득하고, 주사제 **마운자로에 심혈관 위험 감소 적응증**을 추가했습니다.",
            "또한 2026년 연간 매출 가이던스 **$91B~$92B(약 122조 원)**에서 창출되는 압도적 현금흐름을 바탕으로 **Stipple Bio($59억 다중 표적 항암 제휴)** 및 **Calytrix Bio($15억 희귀혈액질환 인수)** 등 총 $74억 연속 빅딜을 단행했습니다.",
            "엔비디아 Nemotron 기반 아르곤국립연구소 신약 단백질 설계 등 **AI-바이오 융합**도 가속화되며 헬스케어 섹터가 AI 변동성과 무관한 핵심 성장 방어축으로 부각되고 있습니다."
        ],
        "previousImplication": "일라이 릴리가 2026 매출 가이던스 상향과 중국 먹는 비만약 승인으로 독주 중이었음.",
        "newCatalyst": "캐나다 경구용 '파운다요' 공식 승인, 마운자로 심혈관 적응증 추가 및 총 $74억 연속 항암·혈액 M&A 성사.",
        "updatedImplication": "포트폴리오가 반도체·AI 빅테크에만 100% 편중되어 있으면 최근 같은 투매장에서 방어가 불가능함. AI와 상관관계가 낮으면서 확실한 실적 성장을 증명하는 **글로벌 비만·항암 바이오 대장주(일라이 릴리·XLV·국내 ADC/CDMO 우량주)**를 10~15% 분산 축으로 편입할 가치가 극대화됨.",
        "implicationHistory": [
            {"time": "11/22 20:00", "text": "🟢 일라이 릴리 캐나다 파운다요 승인 + 마운자로 심혈관 + $74억 연속 빅딜 확인"}
        ],
        "actionPoints": [
            "반도체·AI 편중 포트폴리오 변동성 완화를 위해 헬스케어·비만약 황제주(일라이 릴리·XLV) 10~15% 분산 축 검토",
            "경구용 GLP-1 북미·중국 확산에 따른 국내 CDMO·제형 플랫폼 수혜 기업 실적 추이 추적"
        ],
        "sources": ["CityNews / Newswire Canada (Health Canada Foundayo & Mounjaro CV)", "BioSpace / Morningstar ($7.4B deals)"]
    },
    {
        "id": "agenda_16",
        "asOfDate": "2026-11-23",
        "category": "frontier",
        "categoryLabel": "미래기술 · 우주 · 로봇 · 원전 · 바이오",
        "importance": "HIGH",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 전력망·양자 2대 돌파구! (스페이스X 텍사스 '100% 독자발전(Off-Grid) 초대형 AI 슈퍼컴' 추진 + 인스브루크 51큐비트 양자 오류검증 · Q-CTRL $2.9억 펀딩!)",
        "title": "[11/23] 스페이스X '독자발전(Off-Grid) 초대형 AI 슈퍼컴퓨터' 착수 & 51큐비트 양자 오류검증·Q-CTRL $2.9억 투자 돌파",
        "subtitle": "공공 전력망 마찰을 원천 차단하는 자가발전 슈퍼컴퓨터 표준 제시 + 고전 컴퓨터 검증 한계를 넘은 양자 신뢰도 기술 돌파",
        "chartImage": "assets/charts/agenda_16.svg",
        "chartConfig": {
            "type": "infographic",
            "title": "차세대 컴퓨팅 2대 프런티어: Off-Grid 자가발전 AI 슈퍼컴 & 결함허용 양자컴퓨팅",
            "subtitle": "스페이스X의 독립 전력 슈퍼컴퓨터와 오스트리아 인스브루크·Q-CTRL의 양자 상용화 돌파구가 동시 가속",
            "center_label": "Off-Grid 슈퍼컴 &\n양자 오류검증 돌파",
            "badge_text": "NEXT COMPUTE",
            "nodes": [
                {"title": "스페이스X Off-Grid 슈퍼컴", "metric": "텍사스 브라운즈빌 추진", "desc": "공공 전력망을 전혀 쓰지 않는 100% 독립 발전 설비로 초대형 AI·바이오 슈퍼컴 구축", "color": "#0284c7"},
                {"title": "Nuclear-NASA 2030", "metric": "달 표면 원자로·우주 원전", "desc": "NASA·DOE가 2030년 달 원자로 및 핵추진 우주선 가속(2026 첫 상업 원자력 위성 발사 연계)", "color": "#059669"},
                {"title": "51큐비트 양자 검증 돌파", "metric": "인스브루크 연구진 성과", "desc": "고전 슈퍼컴으로 검산 불가능한 51큐비트 양자 프로세서의 오차 한계 측정 기술 세계 첫 입증", "color": "#7c3aed"},
                {"title": "Q-CTRL $2.9억 메가펀딩", "metric": "결함허용 양자 + AI 보안", "desc": "양자 제어 소프트웨어 Q-CTRL $2.9억 조달 + 우주·방산 엣지 AI·양자내성암호(PQC) 표준화", "color": "#d97706"}
            ]
        },
        "keyMetrics": [
            {"label": "스페이스X 신규 인프라", "value": "스타베이스 Off-Grid AI 슈퍼컴", "change": "공공 전력망 부담·가정 전기료 인상 반발(안건 44)을 원천 우회하는 자가발전 모델"},
            {"label": "양자컴퓨팅 돌파구", "value": "51큐비트 오류 검증 · Q-CTRL $2.9억", "change": "오스트리아 인스브루크 연구진 양자 불확실성 검증법 입증 + 양자 SW 대규모 VC 유입"},
            {"label": "투자 수혜 연결고리", "value": "자가발전 가스터빈·SMR·ESS·PQC", "change": "공공망 송전 변압기 넘어 데이터센터 직결 자가발전(BTM) 전력기기·양자보안 부각"}
        ],
        "facts": [
            "스페이스X가 텍사스 스타베이스 및 브라운즈빌 항 인근에 **공공 전력망에 의존하지 않고 자체 발전 설비로 전력을 생산하는 '100% 독자발전(Off-Grid) 초대형 AI 슈퍼컴퓨팅 시설'** 구축을 본격 추진 중입니다.",
            "동시에 양자컴퓨팅 분야에서는 오스트리아 **인스브루크 연구진이 51큐비트 양자 시스템에서 고전 컴퓨터의 검증 한계를 넘어서는 오류·불확실성 정량 검증 기법**을 세계 최초로 시연했고, 양자 제어 인프라 기업 **Q-CTRL이 $2.9억 대규모 투자 유치**에 성공하며 결함허용 양자컴퓨팅(FTQC)과 AI 워크플로 통합이 급물살을 타고 있습니다.",
            "또한 NASA-DOE의 **2030년 달 표면 원자로('Nuclear-NASA')**와 우주·방산 업계의 **양자내성보안(Quantum-Ready Security)** 도입이 맞물리며 자가발전 에너지·우주원전·양자보안이 차세대 딥테크 핵심 축을 형성하고 있습니다."
        ],
        "previousImplication": "IBM Nighthawk 등 양자컴퓨팅 스케일링과 AI 전력 인프라 병목이 장기 성장 테마로 부상 중이었음.",
        "newCatalyst": "스페이스X의 100% Off-Grid 자가발전 AI 슈퍼컴 추진, 51큐비트 양자 오류검증 돌파 및 Q-CTRL $2.9억 투자 유치.",
        "updatedImplication": "향후 AI 인프라 수혜는 공공 전력망 송전 변압기뿐만 아니라 **데이터센터 직결 자가발전(가스터빈·SMR·연료전지·ESS)**으로 확장됨. 양자컴퓨팅은 단기 변동성이 큰 소형 하드웨어주보다 **양자내성보안(PQC)·빅테크 클라우드 양자 생태계** 중심으로 선별 접근해야 함.",
        "implicationHistory": [
            {"time": "11/23 08:00", "text": "🟢 스페이스X Off-Grid AI 슈퍼컴 + 51큐비트 양자 오류검증·Q-CTRL $2.9억 돌파 확인"}
        ],
        "actionPoints": [
            "AI 전력 포트폴리오에 공공 변압기(HD현대일렉트릭·효성중공업)와 자가발전(두산에너빌리티 가스터빈/SMR·ESS) 양대 축 동시 편입",
            "양자컴퓨팅은 무리한 소형 테마주 추격보다 빅테크·양자내성암호(PQC) 보안 인프라 중심으로 중장기 관찰"
        ],
        "sources": ["SpaceX Official (Starbase off-grid supercomputer)", "ScienceDaily (Innsbruck 51-qubit verification)", "Q-CTRL ($290M) / World Nuclear News"]
    }
]
