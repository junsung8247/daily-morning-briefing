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
        "asOfDate": "2026-11-28",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 블랙프라이데이 뉴욕 대폭발 마감! (S&P {{LIVE:sp500}}({{LIVE:sp500_chg}}) 주간 +5.6% 19개월 최대 · 나스닥 {{LIVE:nasdaq}}({{LIVE:nasdaq_chg}}) · 다우 {{LIVE:dow}}({{LIVE:dow_chg}}) 4년 만의 최대 주간 랠리 · SOX {{LIVE:sox}}({{LIVE:sox_chg}}) 9,100 돌파!)",
        "title": "[11/28 모닝] 뉴욕 블프 단축장 대폭발 마감(나스닥 {{LIVE:nasdaq_chg}} · SOX {{LIVE:sox_chg}} · S&P 주간 +5.6%): 2025년 4월 이후 최고 주간 랠리 완성",
        "subtitle": "다우 50,774(2022년 10월 이후 최대 주간 상승) · 나스닥100 +2.61% · 앤트로픽 +11% · 마이크론 +7.6% · 아마존 ~+4% 전면 숏커버링!",
        "chartImage": "assets/charts/agenda_01.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "sp500",
            "title": "S&P 500 지수 최근 10거래일 실시간 추이 ({{LIVE:sp500}})",
            "subtitle": "실시간 API 연동 차트 · 11/27 블프 단축장 {{LIVE:sp500_chg}} 급등 마감({{LIVE:sp500}})으로 주간 +5.6% 대반전 완성",
            "labels": ["11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/24", "11/25", "11/26", "11/27"],
            "values": [7592.4, 7510.0, 7418.0, 7340.5, 7323.6, 7175.8, 7201.1, 7182.8, 7182.8, 7297.5],
            "unit": "pt",
            "color": "#0284c7",
            "benchmark_val": 7250.0,
            "benchmark_label": "주간 반등 돌파선 7,250pt",
            "badge_text": "LIVE {{LIVE:sp500}}"
        },
        "keyMetrics": [
            {"label": "뉴욕 3대 지수 (11/27 블프 마감)", "value": "S&P {{LIVE:sp500}} / 나스닥 {{LIVE:nasdaq}}", "change": "S&P {{LIVE:sp500_chg}}(주간 +5.6%, 2025.4 이후 최고) · 나스닥 {{LIVE:nasdaq_chg}}(나스닥100 +2.61%) · 다우 {{LIVE:dow}}({{LIVE:dow_chg}})"},
            {"label": "반도체·AI 지수 폭발", "value": "SOX {{LIVE:sox}} ({{LIVE:sox_chg}})", "change": "단숨에 9,100선 탈환! 앤트로픽 +10.98% · 마이크론 +7.60% · AMD +4.56% · 브로드컴 +3.82%"},
            {"label": "유일한 경계 변수", "value": "미 10년물 {{LIVE:us10y}} / DXY {{LIVE:dxy}}", "change": "블프 온라인 $129억(+9.2%) 호조와 리스크온에 국채금리가 4.94%로 재반등하며 12/8~9 FOMC 경계"}
        ],
        "facts": [
            "11월 27일(현지시간) 오후 1시(ET) 조기 폐장한 미국 블랙프라이데이 뉴욕 증시는 극적인 주간 대반전을 완성했습니다. **S&P 500은 +114.71pt({{LIVE:sp500_chg}}) 급등한 {{LIVE:sp500}}**으로 주간 **+5.6%(2025년 4월 이후 최고 주간 수익률)**를 기록했고, **나스닥 종합은 +543.70pt({{LIVE:nasdaq_chg}}) 폭등한 {{LIVE:nasdaq}}**(나스닥 100 +2.61%)으로 마감했습니다(LA Times·BigGo).",
            "**다우존스 산업평균지수 역시 +591.99pt({{LIVE:dow_chg}}) 상승한 {{LIVE:dow}}**로 50,700선을 돌파하며 **2022년 10월 이후 4년 만의 최대 주간 상승률**을 달성했습니다. 특히 **필라델피아 반도체(SOX) 지수가 {{LIVE:sox_chg}} 폭등한 {{LIVE:sox}}**로 단숨에 9,100선을 재탈환했습니다.",
            "종목별로는 공모가($83) 아래로 추락했던 **앤트로픽(ANT)이 {{LIVE:anthropic_chg}} 폭등({{LIVE:anthropic}})**하며 상장 후 최고 반등을 냈고, **마이크론(+7.60%)·AMD({{LIVE:amd_chg}})·브로드컴(+3.82%)·TSMC({{LIVE:tsm_chg}})·아마존(약 +4%)**이 랠리를 주도했습니다. 다만 **엔비디아({{LIVE:nvda}}, {{LIVE:nvda_chg}})**는 동남아 AI 서버 출하 중단 보도 여파로 상대적 약보합에 머물렀습니다."
        ],
        "previousImplication": "근원 PCE 3.3%·301조 관세 악재를 11/25 장중 -4%에서 V자 소화하며 공포 정점을 통과했다고 판단함 (11/26).",
        "newCatalyst": "11/27 블랙프라이데이 단축장서 S&P +1.60%(주간 +5.6%)·나스닥 +2.31%·다우 +1.18%·SOX +4.69% 전면 폭등 마감.",
        "updatedImplication": "이번 주 초반 극단 투매(코스피 -6.16%·삼성 17만·SK 103만·SOX 급락) 구간에서 공포 매도를 차단하고 코어 종목을 지킨 전략이 **주간 +5.6% 대반등**으로 완벽히 승리함! 특히 **마이크론 +7.60%·SOX +4.69% 폭등**은 다음 주 월요일(11/30) 한국 메모리 대형주(삼성·SK)의 18만·115만 원대 추가 회복 훈풍이 될 전망이나, **미 10년물 {{LIVE:us10y}} 재상승**을 감안해 급등 추격은 자제해야 함.",
        "implicationHistory": [
            {"time": "11/26 08:00", "text": "🟢 PCE 3.3%·301조 관세 악재 딛고 나스닥 장중 -4%➔-0.62% 극적 방어! 다우 50,182"},
            {"time": "11/28 08:00", "text": "🟢 블프 단축장 S&P {{LIVE:sp500}}({{LIVE:sp500_chg}}, 주간 +5.6%)·나스닥 {{LIVE:nasdaq_chg}}·SOX {{LIVE:sox_chg}} 전면 폭등 마감!"}
        ],
        "actionPoints": [
            "SOX +4.69%·마이크론 +7.60% 폭등 수혜로 월요일(11/30) 국내 K-메모리(삼성·SK) 갭상승 시 추격 매수 금지, 기존 보유 물량 수익 향유",
            "12월 초 사이버먼데이·고용지표 및 FOMC(12/8~9) 앞두고 현금·미국채 20% 바벨 비중 규율 유지"
        ],
        "sources": ["Yahoo Finance 실시간 ^DJI ({{LIVE:dow}}) / ^GSPC ({{LIVE:sp500}}) / ^IXIC ({{LIVE:nasdaq}}) / ^SOX ({{LIVE:sox}})", "LA Times / Forbes / BigGo / TradingKey (Nov 27 Black Friday close: S&P +1.60% weekly +5.6%, Nasdaq +2.31%, Dow +1.18%, Micron +7.60%, ANT +11%)"]
    },
    {
        "id": "agenda_02",
        "asOfDate": "2026-11-28",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "CRITICAL",
        "deltaStatus": "CHALLENGED",
        "deltaLabel": "🟡 미 10년물 국채금리 '{{LIVE:us10y}}({{LIVE:us10y_chg}})' 재반등 & 달러인덱스 {{LIVE:dxy}}({{LIVE:dxy_chg}}) '104' 돌파! (블프 온라인 $129억 역대 최대 소비 + 12월 FOMC 인상 경계 재점화!)",
        "title": "[11/28 모닝] 미 10년물 금리 '{{LIVE:us10y}}({{LIVE:us10y_chg}})' 반등 · DXY '{{LIVE:dxy}}' 104 회복: 블프 역대급 소비가 다시 깨운 12월 FOMC 긴축 경계",
        "subtitle": "이틀 전 4.85%까지 내려왔던 10년물 금리가 4.94%로 반등하며 5%선 재근접… 12/8~9 FOMC(+25bp) 앞두고 1배수 미국채 바벨 가치 재부각",
        "chartImage": "assets/charts/agenda_02.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "us10y",
            "title": "미국 10년물 국채금리(^TNX) 최근 10거래일 실시간 추이 ({{LIVE:us10y}})",
            "subtitle": "실시간 API 연동 차트 · 11/27 블프 리스크온·강한 소비 지표에 {{LIVE:us10y_chg}} 반등하며 {{LIVE:us10y}} 기록",
            "labels": ["11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/24", "11/25", "11/26", "11/27"],
            "values": [5.10, 5.08, 5.06, 5.04, 5.05, 5.02, 4.90, 4.85, 4.85, 4.94],
            "unit": "%",
            "color": "#f43f5e",
            "benchmark_val": 5.00,
            "benchmark_label": "핵심 경계선 5.00%",
            "badge_text": "LIVE {{LIVE:us10y}}"
        },
        "keyMetrics": [
            {"label": "미 10년물 금리 (11/27 마감)", "value": "{{LIVE:us10y}} ({{LIVE:us10y_chg}})", "change": "11/25 4.85%에서 +9bp 반등하며 5.00% 경계선 재접근(1개월 {{LIVE:us10y_1m}})"},
            {"label": "달러인덱스 & 원/달러", "value": "DXY {{LIVE:dxy}} / 원달러 {{LIVE:usdkrw}}", "change": "DXY 104선 재돌파({{LIVE:dxy_chg}})에도 원/달러는 {{LIVE:usdkrw}} 강세 안정 — 달러 분할 환전 메리트 극대화"},
            {"label": "금리 반등 배경", "value": "블프 소비 $129억(+9.2%) & FOMC", "change": "추수감사절·블프 소비 탄력 + 위험자산 랠리에 안전자산 채권 차익매물 출회"}
        ],
        "facts": [
            "11월 27일(현지시간) 블랙프라이데이 뉴욕 채권시장(오후 2시 ET 조기 폐장)에서 **미 10년물 국채금리는 {{LIVE:us10y_chg}} 반등한 {{LIVE:us10y}}**로 마감했습니다. 직전 거래일(4.85%) 대비 +9bp 오르며 다시 5.00% 경계선 턱밑으로 올라섰습니다.",
            "채권금리 반등과 함께 **달러 인덱스(DXY)도 {{LIVE:dxy_chg}} 상승한 {{LIVE:dxy}}**로 104선을 회복했습니다. 어도비 애널리틱스 집계상 미국 추수감사절 온라인 소비가 $71억(+10.4% YoY), 블랙프라이데이 소비가 사상 최대 $129억(+9.2% YoY)에 육박하는 강한 명목 소비가 확인되면서, **12월 8~9일 FOMC 25bp 인상 및 '고금리 장기화'** 경계가 다시 살아난 영향입니다.",
            "눈여겨볼 대목은 **글로벌 달러(DXY 104.01)가 강해지고 미 10년물 금리가 {{LIVE:us10y}}로 뛰었는데도 원/달러 환율은 {{LIVE:usdkrw}}({{LIVE:usdkrw_chg}})에 머물러 있다**는 점입니다. 한국 투자자 입장에서는 1,333원대 싼 환율로 연 4.94% 고금리 1배수 미국채·단기채를 확보할 수 있는 최적의 창구입니다."
        ],
        "previousImplication": "11/25 실질 PCE(-0.1%) 둔화로 미 10년물 금리가 4.85%까지 내려오며 증시·금의 구원투수 역할을 수행함 (11/26).",
        "newCatalyst": "11/27 블프 리스크온과 역대급 소비($129억)에 미 10년물 금리 {{LIVE:us10y}}({{LIVE:us10y_chg}}) 반등 · DXY {{LIVE:dxy}}(104 회복).",
        "updatedImplication": "12월 FOMC(12/8~9) 전까지는 **미 10년물 금리가 4.85%~5.05% 박스권에서 등락하며 증시 상단을 수시로 시험**할 것임. 따라서 **레버리지 장기채(TMF)는 여전히 배제**하되, **1,330원대 원/달러({{LIVE:usdkrw}})에서 연 {{LIVE:us10y}} 이자를 주는 1배수 미국채·단기채(SGOV/BIL) 바벨 20~30%**를 탄탄히 유지하는 전략이 최강임.",
        "implicationHistory": [
            {"time": "11/26 08:00", "text": "🟢 근원 PCE 3.3%에도 실질소비(-0.1%) 둔화에 미 10년물 4.85% 추가 하락! 증시·금 구원"},
            {"time": "11/28 08:00", "text": "🟡 블프 역대급 소비·리스크온에 미 10년물 {{LIVE:us10y}}({{LIVE:us10y_chg}}) 재반등 · DXY {{LIVE:dxy}} 104 회복!"}
        ],
        "actionPoints": [
            "원/달러 {{LIVE:usdkrw}} 강세 구간을 활용해 연 {{LIVE:us10y}} 고금리 1배수 미국채·초단기채(SGOV) 바벨 20~30% 분할 유지",
            "12/8~9 FOMC(+25bp) 및 12/17~18 일본 BOJ 연쇄 회의 전까지 3배 레버리지 채권·기술주 진입 금지"
        ],
        "sources": ["Yahoo Finance 실시간 ^TNX ({{LIVE:us10y}}) & DX-Y.NYB ({{LIVE:dxy}})", "Adobe Analytics / TradingEconomics (Nov 27 Black Friday $12.9B online sales +9.2%, 10Y yield rebounds to 4.94%)"]
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
        "asOfDate": "2026-11-27",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 대반전 원화 강세! 30조 삼성 배당일에도 서울 원/달러 '1,337.9원(-4.8원)' 급락 · 역외 실시간 {{LIVE:usdkrw}}({{LIVE:usdkrw_chg}}) 1,330원대 초중반 진입! 달러 분할 환전 창구 개방!",
        "title": "[11/27 마감] '삼성 외인 배당 $118억' 역송금 공포 완전 격파! 서울 원/달러 1,337.9원(-4.8원) · 실시간 {{LIVE:usdkrw}} 급락",
        "subtitle": "외국인 코스피 +1조 1,298억 대규모 순매수 유입이 배당 역송금 압력 압도… 기다리던 1,330원대 달러 RP·미국채 분할 환전 찬스 도래!",
        "chartImage": "assets/charts/agenda_05.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "usdkrw",
            "title": "원/달러 환율(USD/KRW) 최근 10거래일 실시간 추이 ({{LIVE:usdkrw}})",
            "subtitle": "실시간 API 연동 차트 · 11/27 외인 +1.13조 유입에 서울 종가 1,337.9원(-4.8원) · 역외 {{LIVE:usdkrw}}({{LIVE:usdkrw_chg}}) 급락!",
            "labels": ["11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/24", "11/25", "11/26", "11/27"],
            "values": [1335.0, 1333.5, 1333.0, 1334.8, 1332.5, 1330.0, 1342.4, 1343.2, 1342.7, 1337.9],
            "unit": "원",
            "color": "#10b981",
            "benchmark_val": 1340.0,
            "benchmark_label": "하향 돌파선 1,340원",
            "badge_text": "LIVE {{LIVE:usdkrw}}"
        },
        "keyMetrics": [
            {"label": "11/27 서울 종가 / 실시간", "value": "종가 1,337.9원(-4.8원) / {{LIVE:usdkrw}}", "change": "삼성전자 외국인 배당 $118억 지급일에도 오히려 환율 급락! 1,330원대 초중반 안착"},
            {"label": "원화 강세 핵심 동력", "value": "외인 코스피 +1.13조 + 한은 3.25%", "change": "외국인 9월 초 이후 최대 순매수(전기전자 +1.03조) + 한은 매파 점도표 + 수출 $1조 돌파"},
            {"label": "글로벌 FX 환경", "value": "DXY {{LIVE:dxy}} · 도쿄 CPI 2.9%", "change": "일본 도쿄 근원 CPI 2.9%(기조 2.5% 둔화)로 엔화·아시아 통화 불안 진정"}
        ],
        "facts": [
            "오늘 아침 외환시장이 바짝 긴장했던 **삼성전자 외국인 배당 $118억(15.3조 원) 역송금 폭탄** 우려가 하루 만에 보기 좋게 빗나갔습니다. 11월 27일(금) 서울 외환시장에서 **원/달러 환율은 전일 대비 4.8원 급락한 1,337.9원**에 마감했고, 저녁 역외 시장에서는 **실시간 {{LIVE:usdkrw}}({{LIVE:usdkrw_chg}})**까지 추가 하락하며 1,330원대 초반을 터치했습니다.",
            "배당금 역송금 수요를 압도한 것은 **외국인의 코스피 +1조 1,298억 원(9월 초 이후 최대!) 대규모 순매수 유입**과 한국은행 3.25% 매파 인상, 그리고 **사상 첫 한국 연간 수출 1조 달러 돌파**라는 압도적 경상수지 체력이었습니다.",
            "오늘 아침 브리핑에서 강조한 **'1,340원대 배당 역송금 공포에 달러 추격 매수 절대 금지 · 1,330원대 되돌림 대기'** 전략이 단 12시간 만에 100% 적중하며 환테크 매수 구간이 열렸습니다."
        ],
        "previousImplication": "오늘(11/27) 삼성 배당 역송금 공포에 달러 추격 매수를 금지하고 1,330원대 되돌림 분할 환전을 권고함 (11/27 모닝).",
        "newCatalyst": "외인 +1.13조 유입에 배당일 원/달러가 서울 종가 1,337.9원(-4.8원) · 역외 {{LIVE:usdkrw}}({{LIVE:usdkrw_chg}})로 급락.",
        "updatedImplication": "드디어 기다리던 **1,330원대 초중반({{LIVE:usdkrw}}) 달러 분할 환전 창구**가 열렸음! 미국채 10년물({{LIVE:us10y}})·엔비디아/TSMC 현물 매수용 달러 현금이나 달러 RP를 지금 1,330원대 초반에서 차분히 분할 환전해 두기 최적의 타이밍임.",
        "implicationHistory": [
            {"time": "11/27 08:00", "text": "🚨 삼성 배당 $118억 역송금 경계 — 추격 달러 환전 금지 · 1,330원대 대기 제시"},
            {"time": "11/27 20:00", "text": "🟢 대반전! 외인 +1.13조 유입에 서울 1,337.9원(-4.8원) · 역외 {{LIVE:usdkrw}} 1,330원대 진입! 환전 찬스"}
        ],
        "actionPoints": [
            "기다리던 1,330원대 초중반({{LIVE:usdkrw}}) 도달 ➔ 미국 우량주·연 {{LIVE:us10y}} 미국채·달러 RP용 달러 1차 분할 환전 개시",
            "원화 강세와 외국인 귀환(+1.13조)이 동시 진행 중이므로 국내 K-반도체 코어 비중도 병행 유지"
        ],
        "sources": ["Yahoo Finance 실시간 KRW=X ({{LIVE:usdkrw}}) & DX-Y.NYB ({{LIVE:dxy}})", "중소기업신문 / 주달 / 연합뉴스 (11/27 서울 원/달러 종가 1,337.9원 -4.8원)"]
    },

    # ==========================================
    # 섹션 2: 반도체 & AI 빅테크 (06~11)
    # ==========================================
    {
        "id": "agenda_06",
        "asOfDate": "2026-11-28",
        "category": "tech",
        "categoryLabel": "반도체 · AI 빅테크",
        "importance": "CRITICAL",
        "deltaStatus": "MAINTAINED",
        "deltaLabel": "🟡 엔비디아 '$150 탈환'({{LIVE:nvda}}, {{LIVE:nvda_chg}}) vs SOX +4.69% 대비 상대 부진! (미 BIS 동남아 4국 AI 서버 출하 중단 명령·국가안보위 신설 여파 · 여전히 1Q×4 PER {{LIVE:nvda_per1qx4}} 초저평가!)",
        "title": "[11/28 모닝] 엔비디아 $150 회복({{LIVE:nvda}}, {{LIVE:nvda_chg}})에도 SOX(+4.69%) 대비 소외된 이유: 동남아 4국 AI 서버 출하 중단 & BIS 우회 차단",
        "subtitle": "델·슈퍼마이크로에 말레이·싱가포르·태국·인니 AI 서버 배송 일시 중단 지시… Q3 매출 $115.8B(+103%) · 1Q×4 PER {{LIVE:nvda_per1qx4}}(13배대) 저평가 재점검",
        "chartImage": "assets/charts/agenda_06.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "nvda",
            "title": "엔비디아(NVDA) 최근 10거래일 실시간 주가 추이 ({{LIVE:nvda}})",
            "subtitle": "실시간 API 연동 차트 · 11/27 동남아 서버 출하 중단 여파로 {{LIVE:nvda_chg}} 소폭 반등하며 {{LIVE:nvda}} 마감(1Q×4 {{LIVE:nvda_per1qx4}})",
            "labels": ["11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/24", "11/25", "11/26", "11/27"],
            "values": [166.2, 162.0, 158.0, 155.0, 151.0, 146.0, 155.38, 149.30, 149.30, 150.49],
            "unit": "$",
            "color": "#22c55e",
            "benchmark_val": 150.0,
            "benchmark_label": "재탈환 지지선 $150",
            "badge_text": "LIVE {{LIVE:nvda}}"
        },
        "keyMetrics": [
            {"label": "엔비디아 주가 (11/27 마감)", "value": "{{LIVE:nvda}} ({{LIVE:nvda_chg}})", "change": "프리마켓 +4% 상승폭 반납 후 $150선 사수 — SOX +4.69%·AMD +4.56%·MU +7.60% 대비 소외"},
            {"label": "상대 부진 직접 원인", "value": "동남아 4국 AI 서버 출하 중단", "change": "미 상무부 BIS 원격접속·90일 라이선스 강화(메가스피드 조사) ➔ 말레이·싱가포르·태국·인니 배송 정지"},
            {"label": "실시간 분기 PER (시세보드)", "value": "4Q {{LIVE:nvda_per4q}} / 1Q×4 {{LIVE:nvda_per1qx4}}", "change": "Q3 매출 $115.8B(+103%)·베라 루빈 NVL72 폭증에도 1Q×4 PER 13배대 극단 저평가 지속"}
        ],
        "facts": [
            "11월 27일(현지시간) 블랙프라이데이 뉴욕 장에서 필라델피아 반도체(SOX {{LIVE:sox_chg}})와 마이크론(+7.60%)·AMD({{LIVE:amd_chg}})가 폭등한 반면, **엔비디아(NVDA)는 장 초반 +4%대 강세를 반납하고 {{LIVE:nvda_chg}} 오른 {{LIVE:nvda}}**로 $150 선을 가까스로 회복하는 데 그쳤습니다.",
            "엔비디아 주가의 발목을 잡은 핵심 악재는 **동남아시아 4개국(말레이시아·싱가포르·태국·인도네시아)행 AI 서버 출하 중단 지시**였습니다. 미 상무부 산업안보국(BIS)이 싱가포르 클라우드 기업 '메가스피드(Megaspeed)' 등의 대중국 원격 연산 우회(Transshipment) 경로를 원천 차단하며 **90일 내 최종사용자(End-user) 라이선스 증빙을 의무화**하자, 엔비디아가 델·슈퍼마이크로 등 파트너사에 일시 배송 중단을 통보한 것입니다(TrendForce·TechRepublic).",
            "아울러 젠슨 황 CEO 복귀 직후 이사회가 **'국가안보 및 수출통제 감독위원회'**를 신설하며 내부 컴플라이언스 고삐를 죄고 있습니다. 다만 동남아 물량은 글로벌 하이퍼스케일러(미국·유럽·우주 스타마인드)의 베라 루빈 NVL72 대기 수요로 즉각 흡수될 구조이며, 현재 **최근 1분기×4 PER {{LIVE:nvda_per1qx4}}(13배대)**는 이미 수출통제 노이즈를 과도하게 반영한 수준입니다."
        ],
        "previousImplication": "11/25 $150 이탈 구간을 1Q×4 PER 13배대 초저평가 분할 매집 구간으로 평가함 (11/26).",
        "newCatalyst": "미 BIS 원격접속·동남아 4국(말레이·싱가포르·태국·인니) AI 서버 출하 중단 명령으로 NVDA {{LIVE:nvda}}({{LIVE:nvda_chg}}) 상대 소외.",
        "updatedImplication": "동남아 우회 물량 차단은 단기 매출 이연 노이즈일 뿐, 미국·유럽·중동 국부펀드·스타마인드의 베라 루빈 대기 수요가 넘쳐남. **SOX +4.69% 급등장에서 홀로 $150(1Q×4 PER {{LIVE:nvda_per1qx4}})에 묶인 엔비디아**는 단기 추격 부담이 가장 적은 역발상 분할 매집 기회임(TSMC·K-메모리 동반 보유 병행).",
        "implicationHistory": [
            {"time": "11/26 08:00", "text": "🔴 NVDA $149.30(-3.91%) $150 하회 · 1Q×4 PER 13.78배 초저평가 구간 진입"},
            {"time": "11/28 08:00", "text": "🟡 NVDA {{LIVE:nvda}}({{LIVE:nvda_chg}}) $150 회복했으나 BIS 동남아 4국 서버 출하 중단으로 SOX(+4.69%) 대비 소외"}
        ],
        "actionPoints": [
            "동남아 90일 라이선스 심사로 눌린 엔비디아 $150 부근(1Q×4 PER {{LIVE:nvda_per1qx4}}) 현물 분할 매집 지속",
            "단일 기업 수출통제 노이즈 분산 차원에서 TSMC({{LIVE:tsm}})·구글({{LIVE:google}})·K-메모리(삼성·SK) 4분산 코어 유지"
        ],
        "sources": ["Yahoo Finance / CNBC 실시간 NVDA ({{LIVE:nvda}})", "TrendForce / TechRepublic / The Guardian / NVIDIA Official (Nov 27 Southeast Asia AI server halt to MY/SG/TH/ID under BIS 90-day license rule, National Security & Export Control Oversight Committee)"]
    },
    {
        "id": "agenda_07",
        "asOfDate": "2026-11-27",
        "category": "tech",
        "categoryLabel": "반도체 · AI 빅테크",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 외국인 순매수 1위 복귀! 삼성전자 정규장 179,100원(+4.55% · NXT {{LIVE:samsung}} {{LIVE:samsung_chg}}) — 30조 배당 재투자 기대 & 미 프리마켓 급등 겹호재 · 1Q×4 PER {{LIVE:samsung_per1qx4}}!",
        "title": "[11/27 마감] 삼성전자 179,100원(+4.55% · 실시간 {{LIVE:samsung}}) 급반등: 외국인 순매수 1위 귀환 & 18만 원선 재탈환 초읽기",
        "subtitle": "장 초반 약세 딛고 18만 원 턱밑까지 급등… 미 프리마켓 마이크론 +6.4%·NVDA +4.2% 급등에도 여전히 1Q×4 PER {{LIVE:samsung_per1qx4}}(3.8배) 초저평가",
        "chartImage": "assets/charts/agenda_07.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "samsung",
            "title": "삼성전자(005930) 최근 10거래일 실시간 주가 추이 ({{LIVE:samsung}})",
            "subtitle": "실시간 API 연동 차트 · 11/27 외인 순매수 1위 복귀로 정규 179,100원(+4.55% · NXT {{LIVE:samsung}}), 1Q×4 {{LIVE:samsung_per1qx4}}",
            "labels": ["11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/24", "11/25", "11/26", "11/27"],
            "values": [208000, 205000, 202000, 199000, 197000, 195000, 189400, 170700, 171300, 179100],
            "unit": "원",
            "color": "#3b82f6",
            "benchmark_val": 180000.0,
            "benchmark_label": "재돌파 기준선 180,000원",
            "badge_text": "LIVE {{LIVE:samsung}}"
        },
        "keyMetrics": [
            {"label": "11/27 KRX 정규 / 실시간 NXT", "value": "정규 179,100원(+4.55%) / NXT {{LIVE:samsung}}", "change": "+7,800원 급등하며 18만 원선 턱밑 회복! 외국인 전기전자 +1조 316억 중 순매수 1위"},
            {"label": "실시간 분기 PER (보통+우선)", "value": "4Q {{LIVE:samsung_per4q}} / 1Q×4 {{LIVE:samsung_per1qx4}}", "change": "+4.5% 급등하고도 최근 1분기×4 PER 3.8배대 · 4Q PER 5.4배대 압도적 저평가"},
            {"label": "미 블프 프리마켓 후속 훈풍", "value": "마이크론 +6.4% · 샌디스크 +10.8%", "change": "오늘 밤 미 메모리·스토리지주 폭등 + 삼성 30조 배당금 재투자 유입으로 월요일 추가 랠리 기대"}
        ],
        "facts": [
            "11월 27일(금) 삼성전자는 장 초반 약세를 완벽히 뒤집고 **KRX 정규장에서 +4.55%(+7,800원) 급등한 179,100원**에 마감하며 18만 원 선을 코앞에 두었습니다(실시간 NXT **{{LIVE:samsung}}, {{LIVE:samsung_chg}}**).",
            "어제 SK하이닉스로 먼저 복귀했던 외국인 자금이 오늘은 **삼성전자를 순매수 1위 종목으로 쓸어 담으며 전기·전자 업종 전체에 1조 316억 원을 집중 투입**했습니다. 오늘 지급된 30조 원 규모의 역대 최대 배당금 중 일부가 증시로 재유입될 것이라는 기대감도 투심을 뜨겁게 달궜습니다.",
            "게다가 저녁 20:00 KST 기준 미국 블랙프라이데이 프리마켓에서 **마이크론(+6.4%)·샌디스크(+10.8%)·엔비디아(+4.2%)**가 동반 급등 중이어서, **1Q×4 PER {{LIVE:samsung_per1qx4}}**에 불과한 삼성전자의 18만~19만 원대 회복 탄력이 한층 강해지고 있습니다."
        ],
        "previousImplication": "어제 기관 +3,220억 방어와 외인 매도 1/10 급감을 확인하며 17만 원대 보유·외인 전환 체크를 권고함 (11/26).",
        "newCatalyst": "11/27 외국인 순매수 1위 복귀로 정규장 179,100원(+4.55%)·NXT {{LIVE:samsung}} 급등 & 미 프리마켓 마이크론 +6.4% 동반 랠리.",
        "updatedImplication": "17만 원대 투매 공포 구간을 버티고 분할 매수한 전략이 단 이틀 만에 외국인 순매수 1위 복귀와 +4.55% 급등으로 보답받음! **4Q PER {{LIVE:samsung_per4q}} · 1Q×4 PER {{LIVE:samsung_per1qx4}}**는 여전히 극저평가 구간이므로 핵심 보유 유지가 정답임.",
        "implicationHistory": [
            {"time": "11/26 20:00", "text": "🟡 11/26 정규 171,300원(+0.35%) · 기관 +3,220억 방어 & 외인 매도 1/10 급감"},
            {"time": "11/27 20:00", "text": "🟢 11/27 정규 179,100원(+4.55% · NXT {{LIVE:samsung}})! 외국인 순매수 1위 전격 귀환!"}
        ],
        "actionPoints": [
            "외국인 순매수 1위 복귀 확인 ➔ 삼성전자(1Q×4 PER {{LIVE:samsung_per1qx4}}) 핵심 코어 보유 유지",
            "오늘 수령한 주당 4,601원 배당금은 중개형 ISA·연금계좌를 통해 저평가 구간 재투자 검토"
        ],
        "sources": ["Naver Finance 실시간 005930 ({{LIVE:samsung}})", "연합뉴스 / 중소기업신문 / 코리아리포트 (11/27 삼성전자 179,100원 +4.55%, 외국인 순매수 1위)"]
    },
    {
        "id": "agenda_08",
        "asOfDate": "2026-11-28",
        "category": "tech",
        "categoryLabel": "반도체 · AI 빅테크",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 TSMC '$353' 탈환({{LIVE:tsm}}, {{LIVE:tsm_chg}}) & 'AI 디자인 키트(ADK · 설계효율 5배)' · 'A14(1.4나노) 고객 설계 개방' 동시 출격! (1Q×4 PER {{LIVE:tsm_per1qx4}} · 앤트로픽/오픈AI 지분동맹 시너지!)",
        "title": "[11/28 모닝] TSMC {{LIVE:tsm}}({{LIVE:tsm_chg}}) $350 돌파! 'AI 디자인 키트(ADK · 칩개발 12개월 단축)' & 1.4나노(A14) 설계 개방으로 파운드리 초격차 굳히기",
        "subtitle": "전날 앤트로픽·오픈AI 각 $5억 지분 동맹에 이어 파운드리 독점 데이터를 AI EDA에 직결… 미 BIS 제3국 OSAT 우회 규제 강화도 TSMC 독점력 강화",
        "chartImage": "assets/charts/agenda_08.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "tsm",
            "title": "TSMC(TSM) 최근 10거래일 실시간 주가 추이 ({{LIVE:tsm}})",
            "subtitle": "실시간 API 연동 차트 · 11/27 {{LIVE:tsm_chg}} 급등하며 $350 돌파({{LIVE:tsm}}, 1Q×4 {{LIVE:tsm_per1qx4}})",
            "labels": ["11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/24", "11/25", "11/26", "11/27"],
            "values": [375.0, 368.0, 362.0, 358.0, 355.0, 352.0, 349.20, 342.34, 342.34, 353.34],
            "unit": "$",
            "color": "#06b6d4",
            "benchmark_val": 350.0,
            "benchmark_label": "재돌파 기준선 $350",
            "badge_text": "LIVE {{LIVE:tsm}}"
        },
        "keyMetrics": [
            {"label": "TSMC 주가 & 분기 PER", "value": "{{LIVE:tsm}} ({{LIVE:tsm_chg}})", "change": "4Q PER {{LIVE:tsm_per4q}} · 1Q×4 PER {{LIVE:tsm_per1qx4}} — 단숨에 $350 돌파하며 19배대 견조한 저평가"},
            {"label": "AI 디자인 키트(ADK) & A14", "value": "설계효율 5배↑ · 개발기간 12개월", "change": "TSMC 공정 지식을 AI EDA에 직결(ADK) + 차세대 A14(1.4나노급) 초기 고객 칩 설계 공식 개방!"},
            {"label": "지분동맹 · BIS 규제 수혜", "value": "앤트로픽/오픈AI 각 $5억 + OSAT 통제", "change": "미 상무부 BIS의 제3국 패스트트랙 OSAT 규제 강화 속 선단 패키징·공정 통행세 지위 절대화"}
        ],
        "facts": [
            "11월 27일(현지시간) 블랙프라이데이 뉴욕 장에서 **TSMC(TSM)가 {{LIVE:tsm_chg}} 급등한 {{LIVE:tsm}}**로 마감하며 $350 저항선을 단숨에 뚫고 올라섰습니다. 최근 1분기×4 PER은 **{{LIVE:tsm_per1qx4}}**(4Q **{{LIVE:tsm_per4q}}**)로 글로벌 선단 파운드리 독점 프리미엄 대비 여전히 합리적입니다.",
            "주가 급반등에 불을 붙인 기술 호재는 TSMC가 공식 출격시킨 **'AI 디자인 키트(ADK)'와 'A14(1.4나노급) 초기 설계 개방'**입니다. ADK는 TSMC 고유의 선단 공정 데이터를 AI 기반 전자설계자동화(EDA)에 직접 연결하는 '기술 지식 계층'으로, **디지털 칩 설계 효율을 최대 5배 끌어올리고 차세대 AI 칩 개발 주기를 12개월 수준으로 단축**시킵니다(CryptoBriefing·DigiTimes).",
            "여기에 어제 확인된 **앤트로픽·오픈AI 각 $5억 지분 동맹**과 미 상무부 BIS의 **제3국 우회 OSAT(후공정) 규제 강화**까지 맞물리며, 커스텀 AI 칩(구글·오픈AI·앤트로픽)과 GPU(엔비디아·AMD) 어느 진영이 이기든 최종 제조·패키징 이익은 TSMC로 수렴하는 독점 해자가 완벽히 굳어졌습니다."
        ],
        "previousImplication": "TSMC가 앤트로픽·오픈AI 각 $5억 지분 동맹으로 AI 자체 칩설계 시대의 최종 승자로 부각됨 (11/27).",
        "newCatalyst": "TSMC AI 디자인 키트(ADK · 설계효율 5배↑) 공식 출시 · A14(1.4나노) 고객 설계 개방 및 11/27 {{LIVE:tsm}}({{LIVE:tsm_chg}}) $350 돌파.",
        "updatedImplication": "엔비디아가 동남아 서버 출하 중단 노이즈로 +0.80%에 그친 날, **TSMC는 ADK·A14 기술 초격차로 +3.21%($353.34) 돌파**하며 '중립 파운드리 최상위 코어' 위상을 증명함! **1Q×4 PER {{LIVE:tsm_per1qx4}}**는 중장기 AI 인프라의 가장 안전한 핵심 축이므로 흔들림 없이 보유해야 함.",
        "implicationHistory": [
            {"time": "11/27 08:00", "text": "🆕 TSMC 사상 첫 중립 관행 깨고 앤트로픽·오픈AI 각 $5억 지분 동맹! AI 자체 칩설계 확산 최종 승자"},
            {"time": "11/28 08:00", "text": "🟢 TSMC {{LIVE:tsm}}({{LIVE:tsm_chg}}) $350 돌파! AI 디자인 키트(ADK · 5배 효율) & A14(1.4나노) 설계 개방!"}
        ],
        "actionPoints": [
            "글로벌 AI 반도체 포트폴리오 최상위 중립 코어로 TSMC({{LIVE:tsm}}, 1Q×4 {{LIVE:tsm_per1qx4}}) 핵심 보유 유지",
            "TSMC ADK 수혜 EDA 소프트웨어(시놉시스·케이던스) 및 선단 패키징 장비주 중장기 연동 관찰"
        ],
        "sources": ["Yahoo Finance / CNBC 실시간 TSM ({{LIVE:tsm}})", "CryptoBriefing / DigiTimes / ETNews (TSMC AI Design Kit ADK up to 5x efficiency, A14 early design readiness, BIS third-country OSAT tightening)"]
    },
    {
        "id": "agenda_09",
        "asOfDate": "2026-11-27",
        "category": "tech",
        "categoryLabel": "반도체 · AI 빅테크",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 '배당락일'에도 +5.41% 폭등(1,110,000원)! (실시간 NXT {{LIVE:skhynix}} {{LIVE:skhynix_chg}} · 이틀 연속 외국인 집중 순매수 2위 + 대규모 주주환원 공시 · 4Q PER {{LIVE:skhynix_per4q}}!)",
        "title": "[11/27 마감] SK하이닉스 '배당락 뚫고 +5.41% 폭등(1,110,000원 · NXT {{LIVE:skhynix}})': 110만 원선 2일 만에 탈환 & 4Q PER {{LIVE:skhynix_per4q}}",
        "subtitle": "3분기 배당락 악재마저 저가 매수·외인 2연속 순매수로 완벽 압도… 대규모 주주환원 계획 공시 & 미 마이크론 +6.4% 급등 동반 호재",
        "chartImage": "assets/charts/agenda_09.svg",
        "chartConfig": {
            "type": "line",
            "liveChartSymbol": "skhynix",
            "title": "SK하이닉스(000660) 최근 10거래일 실시간 주가 추이 ({{LIVE:skhynix}})",
            "subtitle": "실시간 API 연동 차트 · 11/27 배당락일에도 +5.41%(1,110,000원 · NXT {{LIVE:skhynix}}) 폭등하며 110만 원 탈환!",
            "labels": ["11/12", "11/13", "11/16", "11/17", "11/18", "11/19", "11/24", "11/25", "11/26", "11/27"],
            "values": [1240000, 1220000, 1205000, 1190000, 1185000, 1175000, 1158000, 1030000, 1053000, 1110000],
            "unit": "원",
            "color": "#ec4899",
            "benchmark_val": 1100000.0,
            "benchmark_label": "재탈환 기준선 110만원",
            "badge_text": "LIVE {{LIVE:skhynix}}"
        },
        "keyMetrics": [
            {"label": "11/27 KRX 정규 / 실시간 NXT", "value": "정규 1,110,000원(+5.41%) / NXT {{LIVE:skhynix}}", "change": "3분기 배당락일임에도 +57,000원 급등하며 단 이틀 만에 110만 원 황제주 안착!"},
            {"label": "외국인 수급 & 주주환원", "value": "외인 2연속 집중 순매수(2위)", "change": "어제 11일 만의 +3,141억 복귀에 이어 오늘도 대거 매수 + 대규모 주주환원 계획 공시"},
            {"label": "실시간 분기 PER (연결)", "value": "4Q {{LIVE:skhynix_per4q}} / 1Q×4 {{LIVE:skhynix_per1qx4}}", "change": "이틀 연속 +7.7% 급반등하고도 4Q PER 4.1배로 글로벌 7대 AI 빅테크 압도적 최저!"}
        ],
        "facts": [
            "11월 27일(금) SK하이닉스는 통상 매물이 출회되는 **3분기 배당락일**이었음에도 불구하고, 외국인 저가 매수세가 폭발하며 **KRX 정규장에서 +5.41%(+57,000원) 폭등한 1,110,000원**에 마감했습니다(실시간 NXT **{{LIVE:skhynix}}, {{LIVE:skhynix_chg}}**).",
            "어제 11거래일 만에 +3,141억 원 순매수로 돌아선 외국인이 오늘도 삼성전자와 함께 SK하이닉스를 집중 매수(외인 순매수 2위)했고, **대규모 주주환원 계획 공시**까지 더해져 밸류업 모멘텀을 키웠습니다.",
            "이틀 만에 103만 원에서 111만 원으로 8만 원 가까이 뛰어오르고도 여전히 **최근 4분기 PER은 {{LIVE:skhynix_per4q}}**(글로벌 7대 종목 중 압도적 최저치!)에 불과하며, 오늘 밤 미 프리마켓 마이크론(+6.4%)·NVDA(+4.2%) 급등까지 더해져 12월 120만 원대 재도전 기반을 다졌습니다."
        ],
        "previousImplication": "어제 외인 11일 만의 +3,141억 복귀를 바닥 확인 신호로 보고 핵심 보유 및 110만 원 재탈환 점검을 권고함 (11/26).",
        "newCatalyst": "3분기 배당락일에도 +5.41%(1,110,000원) 폭등 · 외인 2연속 순매수 & 대규모 주주환원 계획 공시.",
        "updatedImplication": "11/25 103만 원(4Q PER 3.79배) 극단 저평가 분할 매수 타점이 **불과 이틀 만에 111만 원(+7.8%)**으로 완벽 적중함! 여전히 **4Q PER {{LIVE:skhynix_per4q}}**는 역사적 저평가이므로 흔들리지 않는 장기 코어 보유를 이어가야 함.",
        "implicationHistory": [
            {"time": "11/26 20:00", "text": "🟢 외국인 11거래일 만에 +3,141억 귀환! SK하이닉스 1,053,000원(+2.23%) 반등"},
            {"time": "11/27 20:00", "text": "🟢 배당락일 뚫고 +5.41%(1,110,000원 · NXT {{LIVE:skhynix}}) 폭등! 110만 원 즉각 탈환 & 4Q PER {{LIVE:skhynix_per4q}}"}
        ],
        "actionPoints": [
            "4Q PER {{LIVE:skhynix_per4q}} · 외인 2연속 순매수 확인 ➔ SK하이닉스 핵심 코어 비중 끝까지 보유",
            "단기 이틀 +7.8% 급등 직후 추격 몰빵은 자제, 12월 FOMC·BOJ 변동성 구간에서만 분할 추가"
        ],
        "sources": ["Naver Finance 실시간 000660 ({{LIVE:skhynix}})", "연합뉴스 / 파이낸셜타임스 / 코리아리포트 (11/27 SK하이닉스 배당락 돌파 1,110,000원 +5.41%, 대규모 주주환원 공시)"]
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
