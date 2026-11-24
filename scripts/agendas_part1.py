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
        "asOfDate": "2026-11-24",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "CRITICAL",
        "deltaStatus": "CHALLENGED",
        "deltaLabel": "🟢 대반전 랠리! (S&P 500 {{LIVE:sp500}}({{LIVE:sp500_chg}}) 7일 연속 하락 끊고 조정장 즉시 탈출! 나스닥 {{LIVE:nasdaq}}({{LIVE:nasdaq_chg}}) · VIX -25.8% 급락!)",
        "title": "[11/24] S&P 500 {{LIVE:sp500}}({{LIVE:sp500_chg}}) · 나스닥 {{LIVE:nasdaq}}({{LIVE:nasdaq_chg}}) 폭발적 반등: 젠슨 황 복귀가 만든 7연패 종결과 내일 PCE 분수령",
        "subtitle": "다우 +1,447pt(49,595)·러셀2000 +3.40%·VIX 26.62(-25.83%)… 미 11월 PMI 54.6 확장 유지 속 12월 연준 인상 확률 98% 경계 병존",
        "chartImage": "assets/charts/agenda_01.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "sp500",
            "title": "S&P 500 지수 최근 10거래일 실시간 추이 ({{LIVE:sp500}})",
            "subtitle": "실시간 API 연동 차트 · 11/23 밤 {{LIVE:sp500_chg}} 급등하며 7,000선 단숨에 재탈환 및 조정장 탈출",
            "labels": ["11/10", "11/11", "11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/20", "11/23"],
            "values": [7520.9, 7619.4, 7592.4, 7510.0, 7418.0, 7340.5, 7323.6, 7175.8, 6910.4, 7237.2],
            "unit": "pt",
            "color": "#059669",
            "benchmark_val": 7000.0,
            "benchmark_label": "핵심 분기선 7,000pt",
            "badge_text": "LIVE {{LIVE:sp500}}"
        },
        "keyMetrics": [
            {"label": "S&P 500 (11/23 마감)", "value": "{{LIVE:sp500}} ({{LIVE:sp500_chg}})", "change": "+326.78pt 폭등 · 7거래일 연속 하락 종결 및 공식 조정장(-10%) 탈출"},
            {"label": "나스닥 · 다우 · VIX", "value": "나스닥 {{LIVE:nasdaq}} / 다우 {{LIVE:dow}}", "change": "나스닥 {{LIVE:nasdaq_chg}}(+1,471pt) · 다우 {{LIVE:dow_chg}}(+1,448pt) · VIX 26.62(-25.83%)"},
            {"label": "미 11월 플래시 PMI", "value": "종합 54.6 (전월 55.9) · 서비스 54.7", "change": "4개월 최저로 소폭 둔화됐으나 확장(50+) 지속 — 12/8~9 FOMC 25bp 인상 확률 ~98%"}
        ],
        "facts": [
            "11월 23일(현지시간) 뉴욕 증시는 젠슨 황 엔비디아 CEO의 전격 복귀 발표에 힘입어 7거래일 연속 하락을 끊고 **S&P 500 {{LIVE:sp500}}({{LIVE:sp500_chg}}), 나스닥 종합 {{LIVE:nasdaq}}({{LIVE:nasdaq_chg}}), 다우 {{LIVE:dow}}({{LIVE:dow_chg}})**로 역사적 대반등을 기록하며 단숨에 조정장에서 탈출했습니다.",
            "월가 공포지수(**VIX**)도 하루 만에 **-25.83% 급락한 26.62**로 내려앉았고, 테슬라(+11.46%)·오라클(+12.34%)·팔란티어(+11.06%)·메타(+6.55%)·알파벳(+6.34%) 등 기술주 전반에 대규모 숏커버링과 저가 매수가 쏟아졌습니다.",
            "한편 같은 날 발표된 **미국 11월 S&P 글로벌 플래시 종합 PMI는 54.6(전월 55.9, 서비스업 54.7)**으로 4개월 최저 수준으로 소폭 식었으나 여전히 50을 크게 웃도는 확장세를 유지했습니다. 이에 따라 12월 8~9일 FOMC 25bp 인상 확률이 약 98%로 반영돼 있어 **내일 밤(11/25) 미 10월 PCE 물가**가 추세 안착의 최종 시험대입니다."
        ],
        "previousImplication": "S&P 500이 6,910pt까지 밀리며 공식 조정장에 진입해 추수감사절 단축주간 변동성이 우려됨 (11/23).",
        "newCatalyst": "젠슨 황 엔비디아 CEO 전격 복귀로 S&P 500 {{LIVE:sp500}}({{LIVE:sp500_chg}})·나스닥 {{LIVE:nasdaq}}({{LIVE:nasdaq_chg}}) 폭등, VIX -25.8% 급락 및 11월 미 PMI 54.6 확장 확인.",
        "updatedImplication": "공포의 정점(사이드카·7연패)에서 패닉 투매하지 않고 버틴 바벨 투자자가 완벽히 승리한 장세임. 다만 하루 +5~6% 폭등 직후 추격 몰빵은 단기 차익실현 매물에 물릴 수 있으므로, **내일(11/25) 밤 미 10월 PCE 확인 전까지는 기존 보유분 수익을 누리면서 눌림목 분할 매수**만 허용해야 함.",
        "implicationHistory": [
            {"time": "11/23 18:00", "text": "🔴 S&P 500 6,910 조정장 진입 · 추수감사절 유동성 경계"},
            {"time": "11/24 08:00", "text": "🟢 젠슨 황 복귀로 S&P 500 {{LIVE:sp500}}({{LIVE:sp500_chg}})·나스닥 {{LIVE:nasdaq}}({{LIVE:nasdaq_chg}}) 폭등! 조정장 즉시 탈출"}
        ],
        "actionPoints": [
            "오늘(11/24) 한국 증시 개장 급등 시 흥분한 추격 매수·레버리지 추격 절대 금지(단기 차익매물 출회 경계)",
            "잔여 현금 탄약은 내일 밤(11/25 22:30 KST) 미 10월 PCE 물가 확인 후 눌림목 분할 투입"
        ],
        "sources": ["Yahoo Finance 실시간 ^GSPC ({{LIVE:sp500}}) / ^IXIC ({{LIVE:nasdaq}}) / ^DJI ({{LIVE:dow}})", "Washington Post / Morningstar / Around Prague (Nov 23 rally, VIX 26.62, US Flash PMI 54.6)"]
    },
    {
        "id": "agenda_02",
        "asOfDate": "2026-11-23",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 국채 안전판 작동! (증시 폭락 속 미 10년물 국채금리 {{LIVE:us10y}}({{LIVE:us10y_chg}})로 5% 하회 안착! 채권가격 반등으로 바벨 헤지 위력 입증)",
        "title": "[11/23] 미 10년물 국채금리 {{LIVE:us10y}} (5% 하회 안착): 증시 폭락장에서 증명된 미국채 바벨 헤지의 위력",
        "subtitle": "주식·가상화폐 투매가 쏟아질 때 5%대에서 모아둔 미국채가 즉각 가격 반등(금리 하락)하며 계좌 방패 역할 수행",
        "chartImage": "assets/charts/agenda_02.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "us10y",
            "title": "미국 10년물 국채금리(^TNX) 최근 10거래일 실시간 추이 ({{LIVE:us10y}})",
            "subtitle": "실시간 API 연동 차트 · 최근 1개월 변동 {{LIVE:us10y_1m}}, 5.00% 기준선 아래로 내려오며 안전자산 매수세 유입",
            "labels": ["11/10", "11/11", "11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/20"],
            "values": [4.98, 5.00, 5.10, 5.08, 5.06, 5.04, 5.05, 5.02, 4.91],
            "unit": "%",
            "color": "#0284c7",
            "benchmark_val": 5.00,
            "benchmark_label": "핵심 기준선 5.00%",
            "badge_text": "LIVE {{LIVE:us10y}}"
        },
        "keyMetrics": [
            {"label": "미 10년물 금리 (실시간)", "value": "{{LIVE:us10y}} ({{LIVE:us10y_chg}})", "change": "1개월 변동 {{LIVE:us10y_1m}} · 5.00% 하회하며 채권 가격 반등"},
            {"label": "연준 12월 경계 변수", "value": "11/25 미 10월 PCE · 베이지북", "change": "근원 PCE 예상(3.2~3.3% YoY) 하회 시 채권 랠리·증시 안도 동시 촉발"},
            {"label": "포트폴리오 역할", "value": "연 ~4.9% 무위험 이자 + 폭락 방패", "change": "주식 급락 시 유동성 공급(리밸런싱 탄약) 역할을 완벽히 수행"}
        ],
        "facts": [
            "글로벌 주식·반도체·가상화폐가 동반 급락하는 국면에서 **미국 10년물 국채금리(^TNX)는 실시간 {{LIVE:us10y}}({{LIVE:us10y_chg}})**까지 내려오며 5.00% 선 아래로 안착했습니다.",
            "금리 하락은 곧 **채권 가격 상승**을 의미합니다. 연 5% 부근에서 1배수 미국 중장기 국채와 단기채(달러 현금)를 바벨로 편입해 둔 투자자들은 주식 낙폭을 방어함과 동시에 저가 매수용 탄약을 지켜냈습니다.",
            "다만 12월 FOMC를 앞두고 11월 25일(수) 발표될 10월 PCE 물가가 예상치를 크게 웃돌 경우 금리가 다시 5%를 시험할 수 있으므로, 3배 레버리지 채권 ETF(TMF) 대신 **1배수 현물 국채·단기채 중심 바벨**이 여전히 우월합니다."
        ],
        "previousImplication": "5%대 고금리 구간에서 1배수 미국채 분할 매수가 유효한 안전판 역할을 할 것으로 분석됨.",
        "newCatalyst": "증시 급락과 동시 발생한 안전자산 쏠림으로 미 10년물 금리가 {{LIVE:us10y}}까지 하락하며 5% 하회 안착.",
        "updatedImplication": "미국채 금리가 {{LIVE:us10y}}로 내려오며 '채권-주식 음(-)의 상관관계(방패 효과)'가 정상 복원되었음이 확인됨. 포트폴리오의 20~30%를 단기채·1배수 미국채 현금 탄약으로 유지하는 바벨 원칙을 흔들림 없이 고수해야 함.",
        "implicationHistory": [
            {"time": "11/21 08:00", "text": "🟢 미 10년물 5% 하회 돌파 — 증시 폭락장 속 국채 헤지 완벽 작동"},
            {"time": "11/23 18:00", "text": "🟢 미 10년물 {{LIVE:us10y}} 안착 확인 · 11/25 PCE 앞둔 1배수 국채·현금 바벨 유지"}
        ],
        "actionPoints": [
            "채권 비중은 3배 레버리지(TMF) 배제, 이자수익과 방어력이 확실한 1배수 미국채·초단기 국채(SGOV/BIL)로 20~30% 유지",
            "11/25(수) 미 10월 PCE 결과 확인 후 국채 수익 일부를 급락한 실적 1등주로 기계적 리밸런싱"
        ],
        "sources": ["Yahoo Finance 실시간 ^TNX ({{LIVE:us10y}})", "CME FedWatch / Bloomberg Treasury Desk"]
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
        "asOfDate": "2026-11-23",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "CRITICAL",
        "deltaStatus": "NEW",
        "deltaLabel": "🆕 이번 주 2대 빅이벤트 (11/25(수) 슈퍼 수요일 '미 10월 PCE(+3.2~3.3% 예상)·Q3 GDP·베이지북' ➔ 11/26(목) 한은 금통위 '3.00%➔3.25% 인상' 유력!)",
        "title": "[11/23] 이번 주 2대 분수령: 11/25(수) '미 슈퍼 수요일(10월 PCE·GDP)' & 11/26(목) '한은 금통위 3.25% 인상 기로'",
        "subtitle": "추수감사절 휴장으로 미국 핵심 지표가 수요일 단 하루에 집중! 다음 날 한국은행 올해 마지막 금통위의 25bp 인상 여부 결판",
        "chartImage": "assets/charts/agenda_04.svg",
        "chartConfig": {
            "type": "infographic",
            "title": "11/23~11/27 추수감사절 초압축 주간 핵심 매크로 타임테이블",
            "subtitle": "수요일 밤 미 10월 PCE·GDP·베이지북 5연타 직후 목요일 오전 한국은행 금통위 3.25% 인상 여부 결정",
            "center_label": "11/25 PCE &\n11/26 한은 금통위",
            "badge_text": "THIS WEEK CRITICAL",
            "nodes": [
                {"title": "11/25(수) 미 10월 PCE", "metric": "근원 +3.2~3.3% YoY 예상", "desc": "12월 FOMC 전 마지막 핵심 물가 · 예상치 하회 시 기술주·금·BTC 강력 안도 랠리", "color": "#e11d48"},
                {"title": "11/25(수) GDP·베이지북", "metric": "Q3 GDP · 내구재 · 실업", "desc": "추수감사절 휴장 전 미국 핵심 지표 5종과 존 윌리엄스 뉴욕 연은 총재 발언 집중", "color": "#0284c7"},
                {"title": "11/26(목) 한은 금통위", "metric": "현행 3.00% ➔ 3.25% 유력", "desc": "반도체 수출 호조(3분기 GDP +3.4% YoY)·물가·가계부채 경계로 25bp 인상 컨센서스", "color": "#d97706"},
                {"title": "11/26~27 미 유동성 공백", "metric": "목 휴장 · 금 조기 폐장", "desc": "한국 증시는 목·금 정상 개장하므로 얇은 미국 선물 유동성 속 급등락 경계 필수", "color": "#7c3aed"}
            ]
        },
        "keyMetrics": [
            {"label": "11/25(수) 22:30 KST", "value": "미 10월 근원 PCE (3.2~3.3% 예상)", "change": "헤드라인 ~3.8% 예상 · 연준 12월 긴축 우려가 이미 선반영돼 하회 시 급반등 촉매"},
            {"label": "11/26(목) 한은 금통위", "value": "기준금리 3.00% ➔ 3.25% 전망", "change": "채권 전문가·글로벌 IB 압도적 인상 전망 · 3분기 한국 GDP ~3.4% YoY 성장 상향 기대"},
            {"label": "국내 시장 영향", "value": "은행주 수혜 vs 부동산·채권 압박", "change": "한은 인상 시 시중 주담대 금리 상단(6.5%+) 추가 압박 및 고배당 금융지주 NIM 방어"}
        ],
        "facts": [
            "이번 주 글로벌 금융시장의 모든 시선은 **11월 25일(수) 밤 10시 30분(KST) '슈퍼 수요일'**에 집중됩니다. 미국 추수감사절(26일) 휴장을 앞두고 **10월 개인소비지출(PCE) 물가지수(근원 3.2~3.3%, 헤드라인 ~3.8% YoY 컨센서스), 3분기 GDP 수정치, 내구재 수주, 신규 실업수당, 연준 베이지북**이 하루에 쏟아집니다.",
            "국내에서는 다음 날인 **11월 26일(목) 한국은행 금융통화위원회(올해 마지막 정례회의)**가 열립니다. 10월 한 차례 숨을 고른 한국은행이 반도체 수출 호조에 따른 **탄탄한 3분기 성장률(약 3.4% YoY)과 물가·가계부채 경계감**을 이유로 **기준금리를 3.00%에서 3.25%로 25bp 추가 인상**할 것이라는 전망이 국내외 채권시장의 압도적 컨센서스입니다.",
            "다만 11/20·11/23 2거래일 연속 코스피 매도 사이드카가 발동된 증시 충격(코스피 {{LIVE:kospi}})을 감안해, 신현송 한은 총재가 **인상하더라도 '매파적 소수의견 자제·금융안정 강조'로 시장을 달랠지** 여부가 목요일 국내 채권·환율·부동산의 결정적 변수입니다."
        ],
        "previousImplication": "연준 12월 긴축 우려와 한은 3.25% 인상 관측이 주식·채권 시장에 동시 부담으로 작용 중이었음.",
        "newCatalyst": "11/25 미 10월 PCE·베이지북과 11/26 한은 금통위(3.25% 인상 여부)가 사흘 앞으로 임박하며 시장 긴장 최고조.",
        "updatedImplication": "이번 주 월~수요일 낮에는 큰 베팅을 자제하고 **수요일 밤 미 PCE 결과와 목요일 오전 한은 총재 기자회견**을 확인한 뒤 비중을 집행하는 것이 압도적으로 안전함. 한은 3.25% 인상 현실화 시 **고배당 은행·금융지주(분리과세 특례)는 수혜**, 고가 아파트 매매는 관망세 장기화가 불가피함.",
        "implicationHistory": [
            {"time": "11/22 20:00", "text": "🆕 11/25 슈퍼 수요일(미 PCE) & 11/26 한은 3.25% 인상 전망 분수령 확정"},
            {"time": "11/23 18:00", "text": "🆕 2거래일 연속 코스피 사이드카 속 한은 3.25% 인상 시 신현송 총재의 금융안정 톤이 핵심 변수로 부상"}
        ],
        "actionPoints": [
            "현금 탄약 70%는 11/25(수) 22:30 미 10월 PCE 결과 확인 후 분할 투입",
            "11/26(목) 한은 3.25% 인상 시 고배당 은행·보험주 비중 유지 및 국내 주담대 변동금리 차주의 고정금리·대환 여부 재점검"
        ],
        "sources": ["TradingEconomics / 머니투데이 / 조선일보 / Korea Herald (Nov 25 US Oct PCE & Nov 26 BOK 3.25% rate preview)"]
    },
    {
        "id": "agenda_05",
        "asOfDate": "2026-11-24",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "HIGH",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 환율 하향 안정 전환! (외국인 8거래일 만에 코스피 +7,400억 순매수 복귀에 서울 원/달러 종가 1,342.40원(-3.5원) 하락! 실시간 {{LIVE:usdkrw}} · DXY {{LIVE:dxy}})",
        "title": "[11/24] 원/달러 환율 {{LIVE:usdkrw}} (서울 종가 1,342.40원 · -3.5원): 외국인 8일 만의 순매수 복귀 vs 삼성전자 배당 역송금 공방",
        "subtitle": "코스피 5,000 탈환(+6.32%)과 위험선호 회복에 환율 하락… DXY {{LIVE:dxy}} 강달러 속 1,340원대 초반 안착 점검",
        "chartImage": "assets/charts/agenda_05.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "usdkrw",
            "title": "원/달러 환율(USD/KRW) 최근 10거래일 실시간 추이 ({{LIVE:usdkrw}})",
            "subtitle": "실시간 API 연동 차트 · 11/24 외국인 코스피 순매수 전환에 서울 주간종가 1,342.40원(-3.5원) 안정",
            "labels": ["11/10", "11/11", "11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/20", "11/24"],
            "values": [1341.0, 1339.5, 1335.0, 1333.5, 1333.0, 1334.8, 1332.5, 1330.0, 1345.9, 1342.4],
            "unit": "원",
            "color": "#10b981",
            "benchmark_val": 1340.0,
            "benchmark_label": "단기 기준선 1,340원",
            "badge_text": "LIVE {{LIVE:usdkrw}}"
        },
        "keyMetrics": [
            {"label": "원/달러 환율 (실시간)", "value": "{{LIVE:usdkrw}} ({{LIVE:usdkrw_chg}})", "change": "11/24 서울 외환시장 주간종가 1,342.40원(-3.50원) · 1개월 {{LIVE:usdkrw_1m}}"},
            {"label": "달러 인덱스 (실시간)", "value": "DXY {{LIVE:dxy}} ({{LIVE:dxy_chg}})", "change": "12월 미 연준 인상 경계로 104선 강달러 유지 중이나 원화 방어력 견조"},
            {"label": "수급 충돌 변수", "value": "외인 +7,400억 vs 삼성 배당송금", "change": "외인 주식 순매수 유입이 환율을 눌렀으나 삼성전자 배당 지급일 경계가 하단 지지"}
        ],
        "facts": [
            "11월 24일(화) 서울 외환시장에서 원/달러 환율은 전일 대비 3.50원 내린 **1,342.40원**에 주간거래를 마쳤으며, 실시간 역외 환율은 **{{LIVE:usdkrw}}({{LIVE:usdkrw_chg}})**에서 안정적 흐름을 보이고 있습니다.",
            "간밤 미국 증시 대반등에 힘입어 **외국인이 8거래일 만에 코스피 순매수(+7,390~7,400억 원대)로 돌아선 것**이 장 초반 환율 하락을 견인했습니다. 다만 삼성전자 대규모 분기 배당 지급일 역송금 경계감과 저가 달러 매수세로 하락폭은 제한됐습니다.",
            "글로벌 달러 인덱스(**DXY {{LIVE:dxy}}**)가 104선 위에 머무는 강달러 환경에서도 원화가 1,340원대 초반을 지키고 있으며, 모레 **11/26 한국은행 금통위(3.25% 인상 가능성)**가 통과되면 1,330원대 재진입 여부가 결정됩니다."
        ],
        "previousImplication": "외국인 7거래일 연속 매도로 원/달러 주간종가가 1,345.9원까지 상승 압력을 받음 (11/23).",
        "newCatalyst": "외국인 8일 만의 코스피 +7,400억 순매수 복귀로 서울 원/달러 주간종가 1,342.40원(-3.5원) 하락 안정.",
        "updatedImplication": "코스피 5,000선 회복과 함께 외환시장 불안도 즉각 진정됨. 삼성전자 배당 역송금 물량이 소화되는 이번 주 후반과 11/26 한은 금통위를 전후해 **1,330원대 되돌림 구간에서 달러 RP·미국채 분할 환전**이 여전히 유효함.",
        "implicationHistory": [
            {"time": "11/23 18:00", "text": "🔴 외인 7일 연속 매도에 서울 원/달러 종가 1,345.9원 상승"},
            {"time": "11/24 20:00", "text": "🟢 외국인 +7,400억 복귀로 서울 원/달러 1,342.40원(-3.5원) 하향 안정 전환!"}
        ],
        "actionPoints": [
            "1,340원대 중반 추격 환전 자제 — 삼성 배당 역송금 소화 및 11/26 한은 금통위 전후 1,330원대 분할 환전 대기",
            "보유 달러 현금은 연 {{LIVE:us10y}} 미국채·달러 RP로 운용해 이자수익과 환율 변동 동시 헤지"
        ],
        "sources": ["Yahoo Finance 실시간 KRW=X ({{LIVE:usdkrw}}) & DX-Y.NYB ({{LIVE:dxy}})", "연합인포맥스 (11/24 서울 외환시장 주간종가 1,342.40원)"]
    },

    # ==========================================
    # 섹션 2: 반도체 & AI 빅테크 (06~11)
    # ==========================================
    {
        "id": "agenda_06",
        "asOfDate": "2026-11-24",
        "category": "tech",
        "categoryLabel": "반도체 · AI 빅테크",
        "importance": "CRITICAL",
        "deltaStatus": "CHALLENGED",
        "deltaLabel": "🟢 세기의 대반전! (젠슨 황, 사임 11일 만에 엔비디아 CEO·이사회 만장일치 전격 복귀! 백악관 지지 속 NVDA {{LIVE:nvda}}({{LIVE:nvda_chg}}) 하루 시총 $9,520억 폭증!)",
        "title": "[11/24] 젠슨 황 전격 CEO 복귀! 엔비디아 {{LIVE:nvda}}({{LIVE:nvda_chg}}) 23년 만에 최대 폭등(하루 시총 +$9,520억) & 4Q PER {{LIVE:nvda_per4q}}",
        "subtitle": "트럼프 행정부·미 고위당국 협의 거쳐 국가안보 우려 해소 후 이사회 만장일치 복귀… SOX +14.03% · 마이크론 +19% · 코어위브 +22% 동반 폭발",
        "chartImage": "assets/charts/agenda_06.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "nvda",
            "title": "엔비디아(NVDA) 최근 10거래일 실시간 주가 추이 ({{LIVE:nvda}})",
            "subtitle": "실시간 API 연동 차트 · 11/23 젠슨 황 CEO 복귀 발표로 하루 {{LIVE:nvda_chg}} 폭등하며 4Q PER {{LIVE:nvda_per4q}} 회복",
            "labels": ["11/10", "11/11", "11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/20", "11/23"],
            "values": [172.0, 170.5, 166.2, 162.0, 158.0, 155.0, 151.0, 146.0, 125.53, 165.05],
            "unit": "$",
            "color": "#22c55e",
            "benchmark_val": 160.0,
            "benchmark_label": "복귀 안착선 $160",
            "badge_text": "LIVE {{LIVE:nvda}}"
        },
        "keyMetrics": [
            {"label": "엔비디아 주가 (11/23 마감)", "value": "{{LIVE:nvda}} ({{LIVE:nvda_chg}})", "change": "2003년 5월 이후 23년 만에 최대 일간 상승률 · 단일 세션 시총 +$9,520억 폭증"},
            {"label": "실시간 분기 PER (시세보드)", "value": "4Q {{LIVE:nvda_per4q}} / 1Q×4 {{LIVE:nvda_per1qx4}}", "change": "+31.5% 폭등하고도 Q3 순이익 $65.3B(4Q $226.3B) 덕에 1Q×4 PER 15배대 합리적"},
            {"label": "공급망 동반 폭발", "value": "SOX {{LIVE:sox}}({{LIVE:sox_chg}})", "change": "TSMC {{LIVE:tsm}}({{LIVE:tsm_chg}}) · 마이크론 +19% · 코어위브 +22% · AMD {{LIVE:amd_chg}}"}
        ],
        "facts": [
            "월가 역사를 새로 쓰는 초대형 반전이 터졌습니다. 엔비디아 이사회가 **트럼프 대통령 및 미국 고위 당국자들과의 협의를 거쳐 국가안보 우려가 없음을 확인한 뒤, 사임 11일 만에 창업자 젠슨 황(Jensen Huang)을 CEO·사장·이사로 만장일치 전격 복귀**시켰습니다.",
            "발표 직후 11월 23일 뉴욕 정규장에서 **엔비디아(NVDA) 주가는 하루 만에 {{LIVE:nvda_chg}} 폭등한 {{LIVE:nvda}}**로 마감하며 2003년 5월 이후 최대 일간 상승률을 기록했고, **하루에만 약 9,520억 달러(약 1,280조 원)의 시가총액**을 되찾았습니다.",
            "놀라운 점은 +31% 넘게 폭등한 뒤에도 엔비디아의 실시간 밸류에이션이 **최근 4분기 PER {{LIVE:nvda_per4q}}, 최근 1분기×4 PER {{LIVE:nvda_per1qx4}}**에 불과해 Q3 매출 $115.8B(+103% YoY)·Q4 $130B 가이던스 대비 여전히 합리적이라는 사실입니다. 단, 백악관과의 밀착 복귀로 향후 대중국 수출 통제 준수 압박은 한층 커질 전망입니다."
        ],
        "previousImplication": "젠슨 황 퇴진과 SEC 공시·회계 조사 보도로 엔비디아 거버넌스 불확실성이 극대화됐음 (11/23).",
        "newCatalyst": "백악관 지지 속 젠슨 황 11일 만의 만장일치 CEO 전격 복귀 ➔ NVDA {{LIVE:nvda}}({{LIVE:nvda_chg}}) 하루 시총 $9,520억 폭증 · SOX {{LIVE:sox_chg}} 폭발.",
        "updatedImplication": "지난주 글로벌 증시 폭락의 최대 원인이었던 **'엔비디아 리더십 공백'이 완전히 해소**되며 AI 슈퍼사이클의 구심점이 복원됨. 오늘 09:00 개장하는 삼성전자({{LIVE:samsung}})·SK하이닉스({{LIVE:skhynix}}) 역시 마이크론 +19%·SOX +14%에 힘입어 강력한 동반 반등이 유력함. 단, 단기 +31% 폭등 직후 추격 매수보다 눌림목 분할 접근이 정석임.",
        "implicationHistory": [
            {"time": "11/23 18:00", "text": "🔴 엔비디아 SEC 조사·리더십 공백 충격으로 $125.53 급락"},
            {"time": "11/24 08:00", "text": "🟢 백악관 지지 속 젠슨 황 11일 만에 전격 CEO 복귀! NVDA {{LIVE:nvda}}({{LIVE:nvda_chg}}) 23년 만에 최대 폭등"}
        ],
        "actionPoints": [
            "엔비디아 하루 +31.5% 급등 직후 흥분한 추격 매수 자제(SEC 민사 조사 경과 및 차익매물 소화 확인 후 분할 진입)",
            "마이크론 +19%·TSMC +14% 급등의 직접 수혜를 입으면서 아직 PER 4~5배대인 삼성전자·SK하이닉스 수급 개선 최우선 추적"
        ],
        "sources": ["Yahoo Finance / CNBC 실시간 NVDA ({{LIVE:nvda}})", "조선일보 / Motley Fool / Asia Times (Jensen Huang unanimously reinstated, +31.48%, +$952B mcap)"]
    },
    {
        "id": "agenda_07",
        "asOfDate": "2026-11-24",
        "category": "tech",
        "categoryLabel": "반도체 · AI 빅테크",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 KRX 정규장 +6.70% 폭등(189,400원)! (실시간 애프터 {{LIVE:samsung}} · 4Q PER {{LIVE:samsung_per4q}} / 1Q×4 {{LIVE:samsung_per1qx4}}! 젠슨 황 복귀 + 자사주 한도 100% 완화 겹호재!)",
        "title": "[11/24 마감] 삼성전자 정규장 189,400원(+6.70%) 급반등(실시간 {{LIVE:samsung}}): HBM4 로드맵 정상화 & 자사주 100% 완화 수혜",
        "subtitle": "젠슨 황 복귀로 HBM4·HBM5 협력 불안 단숨에 해소… +6.7% 뛰고도 보통주+우선주 합산 4Q PER {{LIVE:samsung_per4q}} · 1Q×4 {{LIVE:samsung_per1qx4}} 극단 저평가",
        "chartImage": "assets/charts/agenda_07.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "samsung",
            "title": "삼성전자(005930) 최근 10거래일 실시간 주가 추이 ({{LIVE:samsung}})",
            "subtitle": "실시간 API 연동 차트 · 11/24 KRX 정규장 189,400원(+6.70%) 급등 마감, 4Q PER {{LIVE:samsung_per4q}} · 1Q×4 {{LIVE:samsung_per1qx4}}",
            "labels": ["11/10", "11/11", "11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/20", "11/24"],
            "values": [212000, 210000, 208000, 205000, 202000, 199000, 197000, 195000, 177500, 189400],
            "unit": "원",
            "color": "#3b82f6",
            "benchmark_val": 185000.0,
            "benchmark_label": "안착 기준선 185,000원",
            "badge_text": "LIVE {{LIVE:samsung}}"
        },
        "keyMetrics": [
            {"label": "11/24 KRX 정규종가 / 실시간", "value": "정규 189,400원(+6.70%) / 실시간 {{LIVE:samsung}}", "change": "젠슨 황 복귀·마이크론 +19% 훈풍에 18만 원선 단숨에 돌파(야간·대체거래소 변동 반영)"},
            {"label": "실시간 분기 PER (보통+우선)", "value": "4Q {{LIVE:samsung_per4q}} / 1Q×4 {{LIVE:samsung_per1qx4}}", "change": "급반등 직후에도 최근 1분기×4 PER 3~4배대 역사적 저평가 구간 유지"},
            {"label": "2대 핵심 수급 촉매", "value": "외인 순매수 복귀 + 자사주 100% 완화", "change": "11/24 시행 자사주 1일 100% 주문 허용 + 올해 메모리 매출 +402%·HBM4 협력 안정"}
        ],
        "facts": [
            "11월 24일(화) 삼성전자는 간밤 젠슨 황 엔비디아 CEO 전격 복귀(NVDA +31.48%)와 마이크론 +19% 폭등에 힘입어 **KRX 정규장에서 +6.70% 급등한 189,400원**에 마감했습니다(실시간 네이버·대체거래소 포함 기준 **{{LIVE:samsung}}, {{LIVE:samsung_chg}}**).",
            "젠슨 황 복귀로 그동안 시장을 짓눌렀던 **엔비디아향 HBM4·HBM5 공급 일정 지연 우려가 단숨에 해소**됐고, 오늘(11/24)부터 3개월간 시행된 **상장사 1일 자사주 매수 한도 100% 완화**와 외국인의 8거래일 만의 순매수 복귀가 주가를 강력히 끌어올렸습니다.",
            "그럼에도 보통주+우선주 합산 시총 기준 실시간 **최근 4분기 PER은 {{LIVE:samsung_per4q}}, 최근 1분기×4 PER은 {{LIVE:samsung_per1qx4}}**에 머물러 있어, 오늘 밤 델(Dell) 실적과 내일 밤(11/25) 미 10월 PCE를 무난히 통과하면 추가 리레이팅 여력이 큽니다."
        ],
        "previousImplication": "11/23 177,500원 급락으로 1Q×4 PER 3배대 극단 저평가 구간에 진입해 분할 매수 타점으로 평가됨 (11/23).",
        "newCatalyst": "젠슨 황 복귀 및 자사주 100% 완화 첫날인 11/24 KRX 정규장 189,400원(+6.70%) 급반등 및 외국인 8일 만의 순매수 복귀.",
        "updatedImplication": "어제 17만 원대 패닉에 투매하지 않고 버틴 전략이 하루 만에 +6.7% 반등으로 완벽히 보상받음. 4Q PER **{{LIVE:samsung_per4q}}**는 여전히 극저평가이므로 보유 유지하되, **오늘 밤 델(Dell) AI 서버 실적과 내일 밤 미 PCE** 확인 후 눌림목 추가 분할 대응이 정석임.",
        "implicationHistory": [
            {"time": "11/23 18:00", "text": "🔴 11/23 정규장 177,500원 급락 · 1Q×4 PER 3.8배 극단 저평가 분할 매수 구간"},
            {"time": "11/24 20:00", "text": "🟢 11/24 정규장 189,400원(+6.70%) 급반등 · 젠슨 황 복귀 & 자사주 100% 완화 시너지 확인!"}
        ],
        "actionPoints": [
            "보유 물량 유지(4Q PER {{LIVE:samsung_per4q}} · 1Q×4 {{LIVE:samsung_per1qx4}} 여전히 초저평가)",
            "오늘 밤 델(Dell) AI 서버 마진·메모리 원가 발언 및 내일 밤(11/25) 미 10월 PCE 확인 후 추가 비중 결정"
        ],
        "sources": ["Naver Finance 실시간 005930 ({{LIVE:samsung}})", "영남경제 / 연합인포맥스 / 코리아헤럴드 (11/24 삼성전자 정규장 189,400원 +6.70%)"]
    },
    {
        "id": "agenda_08",
        "asOfDate": "2026-11-24",
        "category": "tech",
        "categoryLabel": "반도체 · AI 빅테크",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 TSMC 'AI 거품론' 정면 일축 & 주가 폭발! (TSMC {{LIVE:tsm}}({{LIVE:tsm_chg}}) · 1Q×4 PER {{LIVE:tsm_per1qx4}}! '첨단 AI 칩·CoWoS 수요가 생산능력 크게 초과' 재확인!)",
        "title": "[11/24] TSMC {{LIVE:tsm}}({{LIVE:tsm_chg}}) 폭발적 반등 & AI 거품론 정면 반박: '첨단 칩·CoWoS 수요가 생산 캐파 압도'",
        "subtitle": "TSMC 'AI 조정 우려 근거 없다' 공식 일축 + $51억 보조금 · 3나노 HBM 베이스다이 독점 지위 재확인",
        "chartImage": "assets/charts/agenda_08.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "tsm",
            "title": "TSMC(TSM) 최근 10거래일 실시간 주가 추이 ({{LIVE:tsm}})",
            "subtitle": "실시간 API 연동 차트 · 11/23 밤 {{LIVE:tsm_chg}} 급등하며 4Q PER {{LIVE:tsm_per4q}}, 1Q×4 PER {{LIVE:tsm_per1qx4}} 기록",
            "labels": ["11/10", "11/11", "11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/20", "11/23"],
            "values": [380.0, 378.0, 375.0, 368.0, 362.0, 358.0, 355.0, 352.0, 318.71, 363.60],
            "unit": "$",
            "color": "#06b6d4",
            "benchmark_val": 350.0,
            "benchmark_label": "핵심 돌파선 $350",
            "badge_text": "LIVE {{LIVE:tsm}}"
        },
        "keyMetrics": [
            {"label": "TSMC 주가 (11/23 마감)", "value": "{{LIVE:tsm}} ({{LIVE:tsm_chg}})", "change": "젠슨 황 복귀 + AI 수요 일축 발언으로 하루 +14%대 폭등하며 $360선 단숨에 회복"},
            {"label": "실시간 분기 PER (TWD환산)", "value": "4Q {{LIVE:tsm_per4q}} / 1Q×4 {{LIVE:tsm_per1qx4}}", "change": "1Q×4 PER이 4Q PER보다 낮아 가파른 분기 이익 성장 모멘텀 입증"},
            {"label": "TSMC 공식 입장", "value": "AI 수요가 첨단 캐파 초과", "change": "CoWoS 패키징·2/3나노 풀가동 + $51억 보조금 + 3나노 HBM 베이스다이 장악"}
        ],
        "facts": [
            "11월 23일 뉴욕 정규장에서 **TSMC(TSM)는 하루 만에 {{LIVE:tsm_chg}} 폭등한 {{LIVE:tsm}}**로 마감하며 지난주 낙폭을 대거 만회했습니다.",
            "타이베이타임스 보도에 따르면 TSMC 경영진은 월가의 AI 시장 깊은 조정 우려를 정면 반박하며 **'글로벌 첨단 AI 칩과 CoWoS 첨단 패키징에 대한 구조적 수요가 여전히 TSMC의 선단 제조 능력을 크게 초과하고 있다'**고 단언했습니다.",
            "아울러 TSMC는 순수 파운드리 원칙(3D DRAM 직접 양산설 부인)을 지키면서도 차세대 커스텀 HBM 3나노 베이스다이 공정과 $51억 보조금을 확보해, 실시간 **1Q×4 PER {{LIVE:tsm_per1qx4}}**로 AI 칩 전쟁의 무풍지대 승자임을 재입증했습니다."
        ],
        "previousImplication": "TSMC $51억 보조금·3나노 베이스다이 독점력이 AI 칩 경쟁 중립 승자임을 입증함 (11/23).",
        "newCatalyst": "TSMC 'AI 조정 우려 일축·첨단 수요 캐파 초과' 재확인 및 젠슨 황 복귀 랠리로 TSM {{LIVE:tsm}}({{LIVE:tsm_chg}}) 폭등.",
        "updatedImplication": "엔비디아·구글·AMD 어느 진영이 승리하든 **결국 TSMC({{LIVE:tsm}})가 모든 AI 칩의 통행세를 징수**한다는 핵심 논리가 하루 +14% 반등으로 완벽 입증됨. 글로벌 반도체 코어 비중 1순위로 지속 보유해야 함.",
        "implicationHistory": [
            {"time": "11/23 18:00", "text": "🟢 TSMC $51억 보조금 확보 & 3나노 베이스다이 핵심 지위 확인"},
            {"time": "11/24 08:00", "text": "🟢 TSMC AI 거품론 정면 일축 & 주가 {{LIVE:tsm}}({{LIVE:tsm_chg}}) 폭등! 1Q×4 PER {{LIVE:tsm_per1qx4}}"}
        ],
        "actionPoints": [
            "AI 반도체 포트폴리오 내 '엔비디아-구글-AMD 경쟁 중립 절대 승자'로 TSMC 핵심 코어 비중 유지",
            "단기 +14% 급등 직후 추격보다 11/25 미 PCE 전후 숨 고르기 구간 분할 대응"
        ],
        "sources": ["Yahoo Finance / CNBC 실시간 TSM ({{LIVE:tsm}})", "Taipei Times (TSMC dismisses AI correction fears, CoWoS demand > capacity)"]
    },
    {
        "id": "agenda_09",
        "asOfDate": "2026-11-24",
        "category": "tech",
        "categoryLabel": "반도체 · AI 빅테크",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 KRX 정규장 +6.73% 폭등(1,158,000원)! (실시간 {{LIVE:skhynix}} · 4Q PER {{LIVE:skhynix_per4q}} / 1Q×4 {{LIVE:skhynix_per1qx4}}! 젠슨 황 복귀로 HBM4/HBM5 타임라인 완전 안심!)",
        "title": "[11/24 마감] SK하이닉스 정규장 1,158,000원(+6.73%) 급반등(실시간 {{LIVE:skhynix}}): 젠슨 황 복귀로 HBM4/5 불안 소멸 & 4Q PER {{LIVE:skhynix_per4q}}",
        "subtitle": "장중 10%대 급등하며 코스피 매수 사이드카 견인… 급반등에도 글로벌 7대 AI주 최저 PER(4배대) · 대미 매출 60%+ 초격차 유지",
        "chartImage": "assets/charts/agenda_09.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "skhynix",
            "title": "SK하이닉스(000660) 최근 10거래일 실시간 주가 추이 ({{LIVE:skhynix}})",
            "subtitle": "실시간 API 연동 차트 · 11/24 KRX 정규장 1,158,000원(+6.73%) 급반등, 4Q PER {{LIVE:skhynix_per4q}} · 1Q×4 {{LIVE:skhynix_per1qx4}}",
            "labels": ["11/10", "11/11", "11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/20", "11/24"],
            "values": [1260000, 1255000, 1240000, 1220000, 1205000, 1190000, 1185000, 1175000, 1085000, 1158000],
            "unit": "원",
            "color": "#ec4899",
            "benchmark_val": 1100000.0,
            "benchmark_label": "핵심 돌파선 110만원",
            "badge_text": "LIVE {{LIVE:skhynix}}"
        },
        "keyMetrics": [
            {"label": "11/24 KRX 정규종가 / 실시간", "value": "정규 1,158,000원(+6.73%) / 실시간 {{LIVE:skhynix}}", "change": "장중 10% 이상 폭등하며 115만 원선 탈환(야간·대체거래소 변동 반영)"},
            {"label": "실시간 분기 PER (연결)", "value": "4Q {{LIVE:skhynix_per4q}} / 1Q×4 {{LIVE:skhynix_per1qx4}}", "change": "+6.7% 반등 후에도 글로벌 7대 반도체·AI 빅테크 중 최저 수준 PER(4배대)"},
            {"label": "HBM4/5 · 대미 방어력", "value": "대미 매출 60%+ · YTD +268%", "change": "젠슨 황 복귀로 HBM4/HBM5 타임라인 안정 + 구글·AWS 등 비엔비디아 다변화 병행"}
        ],
        "facts": [
            "11월 24일(화) SK하이닉스는 젠슨 황 엔비디아 CEO 복귀와 마이크론 +19% 폭등에 힘입어 장중 10% 안팎까지 치솟으며 코스피 매수 사이드카를 이끌었고, **KRX 정규장 +6.73% 급등한 1,158,000원**에 마감했습니다(실시간 네이버·대체거래소 기준 **{{LIVE:skhynix}}, {{LIVE:skhynix_chg}}**).",
            "그동안 SK하이닉스 주가를 눌렀던 최대 악재는 엔비디아 리더십 공백에 따른 차세대 HBM4/HBM5 공급 차질 우려였으나, 젠슨 황 복귀로 로드맵 연속성이 완전히 확보됐습니다.",
            "대미 매출 비중 60%+ · 올해 메모리 매출 +268% · 구글 HBM 직거래 협력과 포스트-HBM(HBF/zHBM/PIM) 초격차에도 **최근 4분기 PER은 여전히 {{LIVE:skhynix_per4q}}**에 불과해 중장기 리레이팅 여력이 압도적입니다."
        ],
        "previousImplication": "11/23 108.5만 마감으로 4Q PER 4.1배 극단 저평가 진입, 분할 매수 최상위 후보로 평가됨 (11/23).",
        "newCatalyst": "젠슨 황 복귀로 HBM4/HBM5 협력 불안 해소, 11/24 KRX 정규장 1,158,000원(+6.73%) 급반등 및 외국인 순매수 복귀.",
        "updatedImplication": "급반등 후에도 **4Q PER {{LIVE:skhynix_per4q}}**는 여전히 역사적 저평가 영역임. 오늘 밤 델(Dell) 실적에서 AI 서버용 HBM 원가·수요 강도가 재확인되면 120만 원대 재도전이 유력하므로 핵심 보유 유지가 정답임.",
        "implicationHistory": [
            {"time": "11/23 18:00", "text": "🟢 11/23 108.5만 마감(4Q PER 4.1배) · 대미 매출 60%+ 탈중국 방어력 확인"},
            {"time": "11/24 20:00", "text": "🟢 11/24 정규장 1,158,000원(+6.73%) 급반등! 젠슨 황 복귀로 HBM4/5 로드맵 완전 안심"}
        ],
        "actionPoints": [
            "4Q PER {{LIVE:skhynix_per4q}} 초저평가 핵심 코어 보유 유지(오늘 밤 델 실적·내일 밤 미 PCE 확인 후 눌림목 추가 분할)",
            "엔비디아 HBM4/5 안정화 + 구글(TPU v8t)·AWS향 커스텀 HBM 다변화 수주 지속 추적"
        ],
        "sources": ["Naver Finance 실시간 000660 ({{LIVE:skhynix}})", "영남경제 / Seeking Alpha / 코리아헤럴드 (11/24 SK하이닉스 정규장 1,158,000원 +6.73%)"]
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
        "subtitle": "11/20 폭락장 방어(-2.7%) 이어 11/23 {{LIVE:google_chg}} 반등한 빅테크… 턴키 중개 마진 15~20% 제거로 수백억 달러 CapEx 절감 추진",
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
                {"title": "알파벳 압도적 방어력", "metric": "4Q PER {{LIVE:google_per4q}} 저평가", "desc": "알파벳 A+C 합산 시총 대비 합리적 PER과 자체 TPU 효율로 하락장 방어·반등장 {{LIVE:google_chg}} 선도", "color": "#059669"}
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
