# -*- coding: utf-8 -*-
"""
데일리 모닝 & 이브닝 브리핑 심층 안건 카탈로그 (Part 1: 거시경제/금리 & 빅테크/반도체/2나노)
"""

AGENDAS_PART1 = [
    # ==========================================
    # 섹션 1: 거시경제 & 금리/환율 (Macro & Rates)
    # ==========================================
    {
        "id": "agenda_01",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "CRITICAL",
        "deltaStatus": "CHALLENGED",
        "deltaLabel": "🔴 시사점 전환 (인하 기대 ➔ 재인상 경계)",
        "title": "FOMC 3.75~4.00% 금리 동결 속 '인상 소수의견' 등장과 12월 추가 인상 리스크",
        "subtitle": "연준 내부 매파 목소리 확대… JP모건·BofA '12월 25bp 인상 및 2027년 초 추가 긴축' 경고",
        "chartImage": "assets/charts/agenda_01.svg",
        "chartConfig": {
            "type": "line",
            "title": "미 연준 기준금리 경로 및 시장 예상 추이 (%)",
            "subtitle": "9월 25bp 인상에 이은 동결… 끈적한 물가로 12월 4.25% 상단 돌파 가능성 부각",
            "labels": ["25.Q3", "25.Q4", "26.Q1", "26.Q2", "26.09", "26.10", "26.12(E)", "27.Q1(E)"],
            "values": [3.50, 3.50, 3.62, 3.75, 4.00, 4.00, 4.25, 4.38],
            "unit": "%",
            "color": "#f43f5e",
            "benchmark_val": 4.00,
            "benchmark_label": "현재 상단 금리 4.00%",
            "badge_text": "Fed Policy Watch",
            "annotations": [{"index": 5, "text": "소수의견 2명 즉시 인상 주장"}]
        },
        "keyMetrics": [
            {"label": "미 기준금리", "value": "3.75 ~ 4.00%", "change": "동결 (매파적 기조)"},
            {"label": "FOMC 소수의견", "value": "2명 (Cook, Hammack)", "change": "+25bp 즉시 인상 주장"},
            {"label": "12월 인상 컨센서스", "value": "+25bp 유력", "change": "BofA · JPM 전망 상향"}
        ],
        "facts": [
            "미국 연방공개시장위원회(FOMC)가 기준금리를 현행 3.75%~4.00% 구간에서 동결했으나, 회의록과 성명서 세부 내용은 시장의 기대보다 훨씬 매파적(Hawkish)이었던 것으로 확인되었습니다. 지난 9월 2023년 이후 처음으로 단행된 25bp 금리 인상에 이어, 이번 회의에서도 리사 쿡(Lisa Cook) 이사와 베스 해맥(Beth Hammack) 총재 등 2명의 위원이 물가 고착화를 이유로 즉각적인 25bp 추가 인상을 주장하며 반대표(Dissent)를 던졌습니다.",
            "배경에는 예상보다 훨씬 끈적한(Sticky) 소비자물가 상승률과 에너지 가격 압력, 그리고 견조한 미국 내수 소비가 자리 잡고 있습니다. 실업률이 4.1%로 낮아지고 비농업 고용(NFP)이 시장 예상치를 크게 상회하면서, 연준 입장에서는 경기 침체 우려 없이 인플레이션 타깃(2.0%) 달성을 위해 추가 긴축 카드를 꺼내 들 수 있는 명분이 강화되었습니다.",
            "이에 따라 뱅크오브아메리카(BofA)와 JP모건 등 월가 주요 투자은행(IB)들은 연준이 오는 12월 FOMC에서 25bp 추가 금리 인상을 재개할 것으로 전망을 수정했으며, 인플레이션 둔화 속도가 더딜 경우 2027년 상반기까지 긴축 사이클이 연장될 수 있다고 경고했습니다. 또한 연준은 2027년부터 금리 결정 회의 횟수를 조정하고 통화정책 전략 점검 회의를 별도로 운영하는 구조 개편도 예고했습니다."
        ],
        "previousImplication": "인플레이션이 완만하게 둔화되면서 연준이 금리 동결 후 점진적인 금리 인하(완화) 사이클로 복귀할 것이라는 기대감이 기술주 밸류에이션을 지지함.",
        "newCatalyst": "FOMC 내 2명의 금리 인상 소수의견 발생 + 견조한 고용(실업률 4.1%) 및 월가 IB들의 12월 추가 금리 인상(Re-hiking) 전망 공식화.",
        "updatedImplication": "금리 인하 기대감은 사실상 소멸되고 '재인상(Re-hiking) 리스크'가 시장의 핵심 변수로 전환됨. 할인율 상승에 취약한 적자 성장주·고멀티플 주식의 비중 축소 및 압도적 현금흐름을 보유한 기업으로의 압축 대응 필요.",
        "implicationHistory": [
            {"time": "1개월 전", "text": "🟢 완만한 디스인플레이션 지속으로 연준 금리 동결 장기화 전망"},
            {"time": "12시간 전", "text": "🟡 물가 지표 반등 조짐으로 금리 인하 기대 후퇴"},
            {"time": "현재 브리핑", "text": "🔴 FOMC 인상 소수의견 확인 및 12월 25bp 추가 인상 경계감 본격화"}
        ],
        "actionPoints": [
            "주식: PER 멀티플이 높은 중소형 기술주보다 순현금 보유량이 많아 고금리 이자수익을 누리는 빅테크 대형주 방어적 우위",
            "채권: 단기 통화정책 불확실성 확대로 장기채 추격 매수 자제, 단기채(T-Bill) 중심의 높은 일드 확보 전략 유효"
        ],
        "sources": ["Federal Reserve (FOMC Statement)", "J.P. Morgan Global Research", "Bank of America Macro Watch"]
    },
    {
        "id": "agenda_02",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 시사점 강화 (고금리 장기화 고착)",
        "title": "미 10년물 국채금리 4.85~4.88% 돌파: GDP 6% 재정적자와 기간 프리미엄의 역습",
        "subtitle": "단기 통화정책을 넘어선 구조적 국채 공급 부담… 증시 밸류에이션 할인율 압박 가중",
        "chartImage": "assets/charts/agenda_02.svg",
        "chartConfig": {
            "type": "line",
            "title": "미국 10년물 국채금리(^TNX) 최근 30일 추이 (%)",
            "subtitle": "중간선거 직후 일시 숨고르기 후 재차 4.88% 근접… 5.0% 심리적 저항선 테스트 우려",
            "labels": ["10/10", "10/15", "10/20", "10/25", "10/30", "11/04", "11/07", "11/10"],
            "values": [4.58, 4.64, 4.71, 4.76, 4.82, 4.79, 4.85, 4.88],
            "unit": "%",
            "color": "#f59e0b",
            "benchmark_val": 4.50,
            "benchmark_label": "주식시장 부담 임계선 4.50%",
            "badge_text": "US 10Y Yield 4.88%",
            "annotations": [{"index": 6, "text": "재정적자 GDP 6% 우려 반영"}]
        },
        "keyMetrics": [
            {"label": "미 10년물 금리", "value": "4.88%", "change": "고점 부근 등락"},
            {"label": "미 연방 재정적자", "value": "GDP 대비 ~6%", "change": "구조적 적자 지속"},
            {"label": "S&P 500 지수", "value": "7,528.61", "change": "금리 부담으로 조정"}
        ],
        "facts": [
            "글로벌 금융시장의 중력 역할을 하는 미국 10년 만기 국채 수익률이 4.85%~4.88% 선에서 고공행진을 이어가고 있습니다. 중간선거 직후 일시적인 되돌림이 나타났으나, 강력한 고용 지표와 연준의 추가 긴축 가능성이 맞물리며 장기 금리는 다시 연고점 부근을 위협하고 있습니다.",
            "시장 전문가들이 더욱 주목하는 부분은 연준의 기준금리뿐만 아니라 미 연방정부의 구조적인 재정적자(GDP 대비 약 6% 수준)와 막대한 이자 상환 비용입니다. 국채 발행 물량이 지속적으로 쏟아지는 가운데 투자자들이 장기 국채 보유에 따른 위험 보상인 '기간 프리미엄(Term Premium)'을 더 높게 요구하면서 10년물 금리의 하방 경직성이 매우 강해졌습니다.",
            "10년물 금리가 4.8%를 넘어 5.0%에 육박하면서 주식시장의 무위험 할인율이 급등했고, 이에 따라 최근 한 달간 S&P 500(-3.6%)과 나스닥(-7.9%), 필라델피아 반도체 지수(-20.5%) 등 그동안 가파르게 올랐던 기술주 중심의 밸류에이션 조정(Multiple De-rating)이 촉발되었습니다."
        ],
        "previousImplication": "장기 국채금리가 4.5% 이하에서 안정화되며 기술주 멀티플 확장을 허용할 것이라는 시사점.",
        "newCatalyst": "미 10년물 금리 4.88% 도달 및 GDP 대비 6% 수준의 구조적 재정적자·국채 이자비용 부담 부각.",
        "updatedImplication": "'고금리 뉴노멀(Higher for Longer)' 시사점이 한층 더 강화됨. 금리 4.8% 이상 구간에서는 실적이 아무리 좋아도 주가수익비율(PER)이 높은 종목은 차익실현 표적이 되므로 밸류에이션 정당화 여부가 최우선 기준이 됨.",
        "implicationHistory": [
            {"time": "1개월 전", "text": "🟡 10년물 금리 4.5% 돌파로 장기채 변동성 경계 시작"},
            {"time": "12시간 전", "text": "🟢 재정적자 및 고용 호조로 장기 금리 상승 압력 지속"},
            {"time": "현재 브리핑", "text": "🟢 4.88% 안착으로 기술주 할인율 부담 시사점 강력 유지"}
        ],
        "actionPoints": [
            "성장주: 실적 발표 직후 가이던스가 시장 기대치를 압도하지 못하면 금리 부담으로 주가가 급락하는 패턴에 주의",
            "자산배분: 미 10년물 4.8~5.0% 구간은 장기 투자자 입장에서 분할 매수 매력이 발생하는 금리대이나 CPI 발표 전까지는 변동성 대비"
        ],
        "sources": ["U.S. Treasury Department", "RSM US Economic Outlook", "TradingEconomics"]
    },
    {
        "id": "agenda_03",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "HIGH",
        "deltaStatus": "MAINTAINED",
        "deltaLabel": "🟡 시사점 혼조 (실물 경기 호조 vs 긴축 부담)",
        "title": "미 비농업 고용 서프라이즈 및 실업률 4.1%: '노 랜딩(No Landing)'의 양날의 검",
        "subtitle": "경기 침체 우려는 불식시켰으나 'Good News is Bad News' 장세 재현",
        "chartImage": "assets/charts/agenda_03.svg",
        "chartConfig": {
            "type": "bar",
            "title": "미국 실업률 추이 및 주요 거시경제 지표 비교 (%)",
            "subtitle": "실업률 4.1% 하락 및 소비 견조… 침체 없는 고물가(No Landing) 국면 진입",
            "categories": ["실업률", "근원 물가(YoY)", "기준금리 상단", "10년물 금리", "GDP 성장률(E)"],
            "series_name_1": "이전 분기",
            "values_1": [4.3, 3.1, 3.75, 4.45, 2.6],
            "color_1": "#64748b",
            "series_name_2": "현재 수치",
            "values_2": [4.1, 3.4, 4.00, 4.88, 2.9],
            "color_2": "#38bdf8",
            "unit": "%"
        },
        "keyMetrics": [
            {"label": "미 실업률", "value": "4.1%", "change": "-0.2%p 하락 (고용 탄탄)"},
            {"label": "소비자 지출", "value": "견조한 확장세", "change": "서비스·에너지 물가 자극"},
            {"label": "경기 국면", "value": "No Landing", "change": "침체 없는 고금리 지속"}
        ],
        "facts": [
            "미국 노동시장이 시장의 둔화 예상을 깨고 또다시 강력한 회복력을 증명했습니다. 최근 발표된 비농업 부문 신규 고용(NFP)이 컨센서스를 큰 폭으로 상회한 데 이어, 실업률 역시 4.1%로 낮아지며 완전고용에 가까운 탄탄한 흐름을 유지하고 있습니다.",
            "탄탄한 고용은 곧 가계의 임금 소득과 소비 여력으로 직결됩니다. 실제로 미국 내수 소비 지출은 고금리 환경에서도 꺾이지 않고 있으며, 이는 기업들의 매출 펀더멘털을 뒷받침하는 가장 강력한 버팀목이 되고 있습니다. 즉, 실물 경제가 꺾이는 '경착륙(Hard Landing)' 가능성은 현시점에서 극히 낮아졌습니다.",
            "그러나 주식시장 입장에서는 전형적인 '호재가 곧 악재(Good News is Bad News)'인 딜레마가 발생하고 있습니다. 고용과 소비가 너무 강하다 보니 서비스 물가와 에너지 수요가 줄어들지 않고, 결과적으로 연준이 금리를 내리기는커녕 추가 인상을 고민하게 만들어 금융시장의 유동성 프리미엄을 갉아먹고 있기 때문입니다."
        ],
        "previousImplication": "고용 시장이 점진적으로 냉각되면서 임금 인플레이션이 잡히고 연착륙(Soft Landing)에 도달할 것이라는 시사점.",
        "newCatalyst": "비농업 고용 서프라이즈 및 실업률 4.1% 하락으로 미국 경제가 '노 랜딩(No Landing·무착륙 과열)' 양상을 보임.",
        "updatedImplication": "실물 경기 침체로 인한 기업 이익 급감 우려는 낮으나, 금융 여건 긴축으로 인한 밸류에이션 조정이 진행되는 혼조 국면. 향후 발표될 CPI/PPI 물가 지표가 시장 방향성을 결정할 최대 분수령.",
        "implicationHistory": [
            {"time": "1개월 전", "text": "🟢 고용 둔화 조짐으로 연착륙 기대감 우세"},
            {"time": "12시간 전", "text": "🟡 고용 재반등 확인으로 과열 논란 재점화"},
            {"time": "현재 브리핑", "text": "🟡 기업 실적 지지(호재)와 금리 상승(악재)이 맞서는 혼조세"}
        ],
        "actionPoints": [
            "섹터 전략: 내수 소비와 B2B 투자가 견조하므로 금융주·산업재·전력 인프라 등 실물 경기 민감 섹터의 이익 방어력 주목",
            "이벤트 체크: 곧 발표될 미국 CPI(소비자물가지수) 및 PPI(생산자물가지수) 결과에 따라 나스닥 반등 여부 결정"
        ],
        "sources": ["U.S. Bureau of Labor Statistics (BLS)", "UBS Macro Strategy", "TradingEconomics"]
    },
    {
        "id": "agenda_04",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "CORE",
        "deltaStatus": "NEW",
        "deltaLabel": "🆕 신규 시사점 (분점 의회 ➔ 재정팽창 제동)",
        "title": "미 중간선거 결과 의회 권력 분점(Divided Government)과 2027 재정적자 축소 기대",
        "subtitle": "민주당 양원 장악으로 행정부-의회 견제 구도 형성… 무분별한 재정부양책 제동 전망",
        "chartImage": "assets/charts/agenda_04.svg",
        "chartConfig": {
            "type": "infographic",
            "title": "2027 워싱턴 분점 정부(Divided Government)의 거시경제 파급 구조",
            "subtitle": "행정부와 의회의 권력 분점이 국채 발행·금리·규제에 미치는 핵심 시사점",
            "center_label": ["워싱턴 권력 분점", "재정팽창 제동"],
            "badge_text": "US Fiscal Policy",
            "nodes": [
                {"title": "신규 재정부양책 차단", "metric": "대규모 지출 법안 제동", "desc": "인플레이션 추가 자극 요인 완화", "color": "#38bdf8"},
                {"title": "국채 발행 속도 조절", "metric": "장기채 공급 우려 완화", "desc": "10년물 금리 상단 제약 요인", "color": "#10b981"},
                {"title": "부채한도 협상 진통", "metric": "2027 정치적 불확실성", "desc": "단기 변동성 이벤트 상존", "color": "#f59e0b"},
                {"title": "빅테크·AI 정책 기조", "metric": "초당적 안보/기술 패권", "desc": "반도체·전력망 지원은 지속", "color": "#8b5cf6"}
            ]
        },
        "keyMetrics": [
            {"label": "미 의회 구도", "value": "Divided Gov", "change": "민주당 양원 다수당 확보"},
            {"label": "추가 재정부양 확률", "value": "대폭 하락", "change": "대규모 감세·지출 법안 견제"},
            {"label": "장기 국채 수급", "value": "공급 부담 완화 기대", "change": "중장기 적자 축소 요인"}
        ],
        "facts": [
            "최근 치러진 미국 중간선거 결과 민주당이 상·하원 양원의 주도권을 확보하면서, 2027년 미국 정국은 행정부와 의회가 서로를 견제하는 '분점 정부(Divided Government)' 구도로 재편되었습니다.",
            "월가 채권 전략가들은 이러한 정치적 교착 상태가 금융시장, 특히 국채 시장에는 오히려 긍정적인 안정판 역할을 할 수 있다고 분석합니다. 한 정당이 행정부와 의회를 모두 장악할 경우 대규모 재정 지출이나 공격적인 감세 패키지가 통과되며 재정적자가 눈덩이처럼 불어날 위험이 크지만, 분점 의회 하에서는 대규모 신규 재정부양책(Fiscal Stimulus)이 통과될 가능성이 급격히 낮아지기 때문입니다.",
            "결과적으로 향후 연방 재정적자 확대 속도에 브레이크가 걸리면서, 그동안 장기 국채 금리를 밀어 올렸던 '국채 공급 과잉' 우려가 중장기적으로 진정될 수 있다는 새로운 시사점이 도출되고 있습니다."
        ],
        "previousImplication": "워싱턴의 멈추지 않는 재정 지출과 적자 국채 발행이 10년물 금리를 끝없이 밀어 올릴 것이라는 우려.",
        "newCatalyst": "미 중간선거 결과 양원 분점 구도 확정으로 2027년 신규 대규모 재정부양책 통과 가능성 급감.",
        "updatedImplication": "정치적 입법 교착이 역설적으로 '재정 규율(Fiscal Discipline)' 효과를 내며 중장기 국채 발행 물량 부담을 덜어줄 수 있음. 단기 통화정책 발 금리 발작이 지나가면 장기채 금리는 점차 고점을 확인할 가능성.",
        "implicationHistory": [
            {"time": "1개월 전", "text": "🔴 선거 결과에 따른 재정적자 폭증 리스크 경계"},
            {"time": "12시간 전", "text": "🆕 중간선거 결과 분점 정부 구도 확정"},
            {"time": "현재 브리핑", "text": "🆕 추가 재정팽창 제동으로 장기 국채 수급 우려 완화 시사점 부상"}
        ],
        "actionPoints": [
            "정책 수혜주: 정당 간 이견이 큰 보조금 사업보다 초당적 합의가 확고한 AI 안보·전력망·방산 섹터의 정책 연속성 우위",
            "채권 시장: 미 10년물 금리가 4.9~5.0% 부근까지 오버슈팅할 경우 분점 정부의 재정 억제 효과를 감안한 장기채 분할 접근 유효"
        ],
        "sources": ["Cushman & Wakefield Macro Watch", "Business Insider Markets", "Wall Street Fiscal Tracker"]
    },
    {
        "id": "agenda_05",
        "category": "macro",
        "categoryLabel": "거시경제 · 금리",
        "importance": "CORE",
        "deltaStatus": "MAINTAINED",
        "deltaLabel": "🟡 시사점 유지 (환율 1,345원대 박스권 공방)",
        "title": "원/달러 환율 1,345원대 및 달러 인덱스(DXY) 101.9선: 한·미 금리차와 외국인 수급",
        "subtitle": "미 고금리에도 분점 의회 영향으로 달러 폭등은 제한… 국내 증시 외국인 반도체 차익실현은 부담",
        "chartImage": "assets/charts/agenda_05.svg",
        "chartConfig": {
            "type": "line",
            "title": "원/달러 환율(USD/KRW) 최근 추이 (원)",
            "subtitle": "1,345원 중심 등락… 미 국채금리 상승 압력과 수출 네고 물량이 맞서는 균형 구간",
            "labels": ["10/10", "10/15", "10/20", "10/25", "10/30", "11/04", "11/07", "11/10"],
            "values": [1338.5, 1341.2, 1346.8, 1351.0, 1348.4, 1342.1, 1343.0, 1345.3],
            "unit": "원",
            "color": "#10b981",
            "benchmark_val": 1350.0,
            "benchmark_label": "1차 저항선 1,350원",
            "badge_text": "USD/KRW 1,345.3"
        },
        "keyMetrics": [
            {"label": "원/달러 환율", "value": "1,345.28원", "change": "+0.17% (보합권 등락)"},
            {"label": "달러 인덱스(DXY)", "value": "101.90", "change": "-0.30% (102선 하회)"},
            {"label": "WTI 국제유가", "value": "$88.22 / 배럴", "change": "-3.95% (단기 조정)"}
        ],
        "facts": [
            "외환시장에서 원/달러 환율은 1,345.28원(+0.17%)을 기록하며 비교적 안정적인 박스권 흐름을 이어가고 있습니다. 미 연준의 매파적 기조와 10년물 국채금리 상승에도 불구하고, 달러 인덱스(DXY)가 101.90선에서 상단이 제한되면서 원화 가치의 급격한 약세는 방어되고 있는 모습입니다.",
            "다만 WTI 국제유가가 배럴당 88.22달러 수준으로 여전히 높은 레벨에 머물러 있어 에너지 수입 의존도가 높은 한국 경제의 무역수지와 물가에 잠재적인 부담 요인으로 작용하고 있습니다.",
            "특히 최근 글로벌 기술주 및 반도체 지수(SOX)의 밸류에이션 조정 과정에서 외국인 투자자들이 삼성전자와 SK하이닉스 등 국내 대형주에서 차익실현 매물을 출회하면서, 원/달러 환율이 1,330원대 이하로 빠르게 내려가는 것 또한 제한되고 있습니다."
        ],
        "previousImplication": "달러 강세 진정과 함께 원/달러 환율이 1,300원 초반으로 안착하며 외국인 자금이 유입될 것이라는 시사점.",
        "newCatalyst": "미 금리 재인상 경계감에 따른 한·미 금리차 유지 및 외국인 반도체 차익실현 수급.",
        "updatedImplication": "환율 자체가 외환위기급 리스크를 유발할 수준(1,400원대)은 아니나, 미 금리 인하가 지연됨에 따라 1,330~1,360원 박스권이 장기화될 전망. 달러 자산과 원화 자산의 균형 잡힌 통화 분산 유지.",
        "implicationHistory": [
            {"time": "1개월 전", "text": "🟢 달러 약세 전환 기대감으로 원화 강세 전망"},
            {"time": "12시간 전", "text": "🟡 미 국채금리 상승에도 DXY 102선 저항으로 박스권 유지"},
            {"time": "현재 브리핑", "text": "🟡 1,345원대 균형, 외국인 주식 수급이 단기 환율 방향성 좌우"}
        ],
        "actionPoints": [
            "환테크: 달러 매수는 1,330원대 초반 접근 시 분할 대응, 1,350원 이상에서는 추격 매수 자제",
            "국내 증시: 환율 급등이 없는데도 외국인이 매도하는 것은 환차손 우려가 아니라 글로벌 반도체 멀티플 조정 때문임을 구분할 필요"
        ],
        "sources": ["Yahoo Finance FX", "한국은행 외환시장 동향", "연합인포맥스"]
    },

    # ==========================================
    # 섹션 2: 빅테크 & 반도체/핵심 기술 (Big Tech & Semi/Tech)
    # ==========================================
    {
        "id": "agenda_06",
        "category": "tech",
        "categoryLabel": "반도체 · 빅테크 · 2나노",
        "importance": "CRITICAL",
        "deltaStatus": "NEW",
        "deltaLabel": "🆕 신규 시사점 (커스텀 HBM '로직 파운드리화')",
        "title": "엔비디아, 삼성·SK하이닉스·마이크론에 차세대 커스텀 HBM 베이스 다이 'TSMC 3나노' 채택 요구",
        "subtitle": "메모리 반도체의 패러다임 전환… HBM 두뇌 역할을 하는 Base Die에 파운드리 초미세 공정 결합",
        "chartImage": "assets/charts/agenda_06.svg",
        "chartConfig": {
            "type": "infographic",
            "title": "엔비디아 차세대 커스텀 HBM & TSMC 3나노 베이스 다이(Base Die) 결합 구조",
            "subtitle": "표준형 메모리에서 '고객 맞춤형 로직+메모리 융합 칩'으로 진화하는 HBM 밸류체인",
            "center_label": ["NVIDIA 커스텀 HBM", "TSMC 3nm Base Die"],
            "badge_text": "Custom HBM Architecture",
            "nodes": [
                {"title": "SK하이닉스", "metric": "TSMC 3nm 원팀 동맹", "desc": "HBM4 베이스 다이 파운드리 협력 선점", "color": "#38bdf8"},
                {"title": "삼성전자", "metric": "자체 파운드리 vs TSMC", "desc": "엔비디아 요구 충족 위한 전략적 선택 기로", "color": "#f59e0b"},
                {"title": "마이크론 (Micron)", "metric": "TSMC 3nm 공정 직결", "desc": "자체 파운드리 부재를 TSMC 협력으로 돌파", "color": "#10b981"},
                {"title": "TSMC", "metric": "3D DRAM 진출설 부인", "desc": "'메모리 직접 제조 안 해, 로직 파운드리 집중'", "color": "#8b5cf6"}
            ]
        },
        "keyMetrics": [
            {"label": "요구 공정", "value": "TSMC 3nm", "change": "차세대 커스텀 HBM Base Die"},
            {"label": "대상 기업", "value": "SK하이닉스·삼성·마이크론", "change": "메모리 3사 전원 해당"},
            {"label": "TSMC 공식 입장", "value": "로직 파운드리 전념", "change": "3D DRAM 직접 진출설 일축"}
        ],
        "facts": [
            "글로벌 AI 반도체 생태계에 중대한 기술적 변곡점이 포착되었습니다. 엔비디아(NVIDIA)가 차세대 AI 가속기 성능을 극대화하기 위해 삼성전자, SK하이닉스, 마이크론 등 메모리 3사에 차세대 맞춤형(Custom) HBM의 맨 아래층 두뇌 역할을 하는 '베이스 다이(Base Die, 로직 다이)'를 TSMC의 선단 3나노(3nm) 공정으로 제조할 것을 공식 요청했다는 소식이 전해졌습니다.",
            "기존 HBM까지는 메모리 제조사들이 자체 성숙 공정으로 베이스 다이를 만들었으나, 차세대 HBM4 이후부터는 데이터 전송 대역폭과 전력 효율 한계를 돌파하기 위해 베이스 다이에 고도의 연산·제어 회로가 들어가야 합니다. 즉, 메모리가 단순 범용 부품(Commodity)에서 파운드리 초미세 공정이 필수적인 '주문형 로직 융합 반도체'로 진화하고 있는 것입니다.",
            "한편 시장 일각에서 제기된 'TSMC가 엔비디아를 위해 직접 3D DRAM 메모리 제조에 뛰어든다'는 루머에 대해, TSMC는 '메모리 제조사로 변신할 계획이 없으며 순수 로직 파운드리 역할에 집중할 것'이라고 명확히 선을 그었습니다. 대신 베이스 다이 파운드리와 CoWoS 패키징을 통해 메모리 생태계에 대한 지배력을 더욱 공고히 하는 전략을 택했습니다."
        ],
        "previousImplication": "HBM 시장은 메모리 3사(SK하이닉스·삼성전자·마이크론)의 D램 적층 기술력만으로 승부가 갈릴 것이라는 시사점.",
        "newCatalyst": "엔비디아가 메모리 3사 모두에 커스텀 HBM 베이스 다이용으로 'TSMC 3나노 공정' 활용을 요구.",
        "updatedImplication": "차세대 HBM 패권은 'D램 코어 다이 기술력 + TSMC 선단 공정 및 CoWoS 패키징 생태계와의 매끄러운 결합 능력'이 좌우함. TSMC는 GPU뿐만 아니라 HBM 베이스 다이 물량까지 흡수하며 AI 밸류체인 내 독점적 지위가 한층 더 강화됨.",
        "implicationHistory": [
            {"time": "1개월 전", "text": "🟢 HBM4 표준화 논의 및 베이스 다이 파운드리 위탁 가능성 대두"},
            {"time": "12시간 전", "text": "🆕 엔비디아, 메모리 3사에 TSMC 3나노 베이스 다이 적용 구체적 요구"},
            {"time": "현재 브리핑", "text": "🆕 커스텀 HBM 시대 개막으로 TSMC-메모리 합종연횡 시사점 부각"}
        ],
        "actionPoints": [
            "TSMC: GPU 파운드리에 이어 HBM 로직 다이까지 3나노 수주 영역이 확장되므로 구조적 성장성 최우선 픽 유지",
            "SK하이닉스 & 삼성전자: TSMC와의 얼라이언스를 이미 구축한 SK하이닉스의 연속성 우위 속, 삼성전자의 파운드리·메모리 유연한 대응 여부가 관건"
        ],
        "sources": ["MLQ.ai Semiconductor Report", "Economic Times Tech", "TrendForce Memory Research"]
    },
    {
        "id": "agenda_07",
        "category": "tech",
        "categoryLabel": "반도체 · 빅테크 · 2나노",
        "importance": "CRITICAL",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 시사점 강화 (2나노 GAA 양산 & CapEx 폭발)",
        "title": "TSMC 연간 설비투자(CapEx) 600~640억 달러 상향과 2나노(N2)·차세대 A16 공정 질주",
        "subtitle": "나노시트(GAA) 구조 2나노 월간 웨이퍼 생산량 급증… 삼성 파운드리도 2나노 GAA 대형 수주 총력전",
        "chartImage": "assets/charts/agenda_07.svg",
        "chartConfig": {
            "type": "bar",
            "title": "TSMC 연간 설비투자(CapEx) 확대 및 공정별 배분 (십억 달러)",
            "subtitle": "2026년 CapEx 가이던스 600~640억 달러 역대 최대… 70~80%를 2나노·3나노 선단 공정에 집중",
            "categories": ["2023", "2024", "2025", "2026 가이던스(하단)", "2026 가이던스(상단)"],
            "series_name_1": "연간 CapEx ($B)",
            "values_1": [30.4, 29.8, 42.5, 60.0, 64.0],
            "color_1": "#38bdf8",
            "unit": "$B"
        },
        "keyMetrics": [
            {"label": "TSMC 연간 CapEx", "value": "$60B ~ $64B", "change": "역대 최대 규모 상향"},
            {"label": "선단 공정 비중", "value": "70% ~ 80%", "change": "2나노(N2) · 3나노(N3) 집중"},
            {"label": "삼성·SK 설비투자", "value": "+35% YoY 증가", "change": "전 라인 풀가동(Full Cap)"}
        ],
        "facts": [
            "빅테크 기업들의 폭발적인 차세대 AI 칩 수요에 대응하기 위해 TSMC가 올해 연간 설비투자(CapEx) 목표치를 600억~640억 달러(약 80조~86조 원)라는 사상 초유의 규모로 상향 조정했습니다. 이 중 무려 70%~80%가 2나노(N2)와 3나노(N3) 등 초미세 선단 공정 증설에 투입되며, 10%~20%는 첨단 패키징에 배정됩니다.",
            "기술적으로 가장 주목받는 대목은 TSMC의 '2나노(N2) 공정' 상업 양산 램프업입니다. 나노시트(Nanosheet, GAA) 트랜지스터 아키텍처와 후면전력공급(Backside Power Rail) 기술을 결합한 N2 패밀리는 2027년 중반을 향해 월간 웨이퍼 생산 능력을 가파르게 늘리고 있으며, 슈퍼 파워 레일(Super Power Rail)이 적용되는 차세대 'A16(1.6나노급)' 노드 역시 연내 양산 준비에 돌입합니다.",
            "한편 삼성전자 역시 독자적인 2나노 게이트올어라운드(GAA) 공정 기술력을 앞세워 글로벌 티어1 빅테크의 커스텀 AI 칩 수주를 따내기 위해 사활을 걸고 있습니다. 마이크로소프트(Maia), 구글(TPU), 메타, 아마존 등 빅테크들이 자체 ASIC 칩 개발을 확대하면서 파운드리 물량 자체가 커지고 있어, TSMC의 독주 속에 삼성 파운드리가 2나노에서 얼마나 의미 있는 파이를 확보할지가 핵심 관전 포인트입니다."
        ],
        "previousImplication": "2나노 공정 전환 비용이 너무 높아 빅테크 고객사들의 초기 채택 속도가 3나노 때보다 느릴 수 있다는 우려.",
        "newCatalyst": "TSMC CapEx 600~640억 달러 전격 상향 및 2나노(N2)·A16 노드의 가파른 웨이퍼 생산 능력 확장 확인.",
        "updatedImplication": "AI 데이터센터의 전력 효율 문제 해결을 위해 빅테크들이 비용을 불문하고 2나노 GAA 및 후면전력공급 공정으로 직행하고 있음이 증명됨. ASML(EUV)·어플라이드머티어리얼즈 등 2나노 전공정 장비 및 소재 밸류체인 수혜 시사점 대폭 강화.",
        "implicationHistory": [
            {"time": "1개월 전", "text": "🟢 2나노 시험 생산 수율 안정화 소식"},
            {"time": "12시간 전", "text": "🟢 TSMC CapEx 600~640억 달러 상향 및 N2/A16 로드맵 가속"},
            {"time": "현재 브리핑", "text": "🟢 2나노 GAA 전환이 AI 하드웨어의 필수 관문으로 확정"}
        ],
        "actionPoints": [
            "반도체 장비/소재: TSMC(640억 달러)와 삼성·SK하이닉스(+35% YoY)의 동시다발적 CapEx 증액은 선단 공정 장비주의 확정된 매출을 의미",
            "파운드리: TSMC 주가가 최근 매크로 조정으로 $392선(-13%)까지 눌린 구간은 펀더멘털 대비 매력적인 중장기 진입 기회로 평가"
        ],
        "sources": ["Bits&Chips Semiconductor", "SemiWiki 2nm Analysis", "BusinessKorea"]
    },
    {
        "id": "agenda_08",
        "category": "tech",
        "categoryLabel": "반도체 · 빅테크 · 2나노",
        "importance": "HIGH",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 시사점 강화 (CoWoS 단가 10~20% 인상)",
        "title": "AI 칩 최대 병목 'CoWoS 패키징' 수요 3배 폭증과 TSMC 패키징 단가 10~20% 인상",
        "subtitle": "월 13만 장 돌파 후 2028년까지 2배 추가 증설… 글로벌파운드리와 미 현지 실리콘 인터포저 20억 달러 협력",
        "chartImage": "assets/charts/agenda_08.svg",
        "chartConfig": {
            "type": "line",
            "title": "TSMC CoWoS 첨단 패키징 월간 생산능력(웨이퍼/월) 확장 추이",
            "subtitle": "2년 만에 수요 3배 폭증… 월 13만 장 돌파 및 단가 10~20% 인상으로 이익률 극대화",
            "labels": ["24.H1", "24.H2", "25.H1", "25.H2", "26.H1", "26.H2(현)", "27.E", "28.E"],
            "values": [32, 45, 65, 85, 110, 135, 190, 260],
            "unit": "K장",
            "color": "#a855f7",
            "badge_text": "CoWoS +10~20% ASP",
            "annotations": [{"index": 5, "text": "단가 10~20% 인상 단행"}]
        },
        "keyMetrics": [
            {"label": "CoWoS 단가 인상", "value": "+10% ~ +20%", "change": "극심한 공급 부족 반영"},
            {"label": "월간 생산능력", "value": "130,000장+ / 월", "change": "2028년까지 2배 추가 확장"},
            {"label": "공급망 파트너십", "value": "GF와 $2B 계약", "change": "미국 내 실리콘 인터포저 생산"}
        ],
        "facts": [
            "고성능 AI 가속기(GPU/ASIC)와 HBM 메모리를 하나로 묶어주는 핵심 후공정 기술인 'CoWoS(Chip-on-Wafer-on-Substrate)' 첨단 패키징이 여전히 글로벌 AI 공급망의 가장 치명적인 병목(Bottleneck) 구간으로 작용하고 있습니다. 최근 2년 사이 CoWoS 수요는 약 3배 가까이 폭증했습니다.",
            "공급이 수요를 따라가지 못하는 극심한 쇼티지(Shortage) 속에서 TSMC는 강력한 가격 결정력(Pricing Power)을 행사하며 첨단 패키징 서비스 견적 단가를 10%~20% 인상했습니다. 동시에 내부 CoWoS 생산 능력을 월 13만 장(웨이퍼 기준) 이상으로 끌어올렸으며, 2028년까지 이를 다시 두 배로 확대할 계획입니다.",
            "더 나아가 병목을 해소하기 위해 TSMC는 글로벌파운드리(GlobalFoundries)와 20억 달러 규모의 전략적 파트너십을 체결하고, 전력 안정성을 높이는 딥 트렌치 커패시터(Deep Trench Capacitor)가 내장된 실리콘 인터포저를 2028년까지 미국 현지에서 생산하기로 합의하는 등 후공정 생태계 확장에 박차를 가하고 있습니다."
        ],
        "previousImplication": "후공정(패키징)은 전공정 파운드리에 비해 부가가치와 마진율이 낮은 보조 공정이라는 전통적 시각.",
        "newCatalyst": "CoWoS 수요 3배 폭증에 따른 패키징 단가 10~20% 인상 및 월 13만 장 이상 대규모 증설·외주 생태계 확장.",
        "updatedImplication": "첨단 패키징(CoWoS)이 AI 칩 출하량을 결정짓는 핵심 전략 자산이자 고마진 캐시카우로 완전히 격상됨. 패키징 기판·인터포저·TC본더 장비 기업들의 수주 모멘텀 지속.",
        "implicationHistory": [
            {"time": "1개월 전", "text": "🟢 CoWoS 증설에도 빅테크 할당량 부족 지속"},
            {"time": "12시간 전", "text": "🟢 패키징 서비스 단가 10~20% 인상 및 글로벌파운드리 $2B 협력"},
            {"time": "현재 브리핑", "text": "🟢 후공정 패키징의 구조적 마진 확대 시사점 강화"}
        ],
        "actionPoints": [
            "밸류체인: CoWoS 및 HBM 적층에 필수적인 TC본더(한미반도체 등), 실리콘 인터포저, 유리기판 등 차세대 패키징 기술 보유 기업 주목",
            "가격 전가력: 인플레이션과 금리 상승기에는 TSMC처럼 단가를 10~20% 올려도 고객이 줄을 서는 독점 기업이 최고의 투자처"
        ],
        "sources": ["Investing.com Semi Watch", "TradingView Tech Insights", "Keming-IC Supply Chain"]
    },
    {
        "id": "agenda_09",
        "category": "tech",
        "categoryLabel": "반도체 · 빅테크 · 2나노",
        "importance": "CRITICAL",
        "deltaStatus": "CHALLENGED",
        "deltaLabel": "🔴 시사점 조정 (역대급 마진 vs 고금리 발 주가 조정)",
        "title": "SK하이닉스·마이크론 HBM 영업이익률 80% 기염 속 반도체 지수(SOX) -20% 급락의 역설",
        "subtitle": "펀더멘털은 사상 최고치이나 미 10년물 금리 4.88% 발 멀티플 디레이팅… 실적과 주가의 괴리 분석",
        "chartImage": "assets/charts/agenda_09.svg",
        "chartConfig": {
            "type": "bar",
            "title": "HBM 메모리 영업이익률(%) vs 최근 1개월 주요 반도체 주가 등락률(%)",
            "subtitle": "HBM 영업이익률은 최대 80%에 달하나, 매크로 고금리 여파로 주가는 큰 폭의 기간 조정 진행 중",
            "categories": ["HBM 영업이익률", "SOX 지수(1M)", "엔비디아(1M)", "TSMC(1M)", "SK하이닉스(1M)", "삼성전자(1M)"],
            "series_name_1": "수치 / 등락률 (%)",
            "values_1": [78.0, -20.5, -22.9, -13.4, -32.4, -27.5],
            "color_1": "#38bdf8",
            "unit": "%"
        },
        "keyMetrics": [
            {"label": "HBM 최고 영업이익률", "value": "최대 ~80%", "change": "SK하이닉스·마이크론 역대급 수익성"},
            {"label": "필라델피아 반도체(SOX)", "value": "9,993.65", "change": "-20.51% (1개월 조정)"},
            {"label": "엔비디아(NVDA)", "value": "$176.77", "change": "-22.90% (밸류에이션 숨고르기)"}
        ],
        "facts": [
            "현재 반도체 시장은 '사상 최고의 실적 펀더멘털'과 '매크로 금리 발 주가 급락'이라는 극단적인 괴리를 겪고 있습니다. 산업 데이터에 따르면 SK하이닉스와 마이크론 등 선두 메모리 기업들은 엔비디아 향 HBM 공급 부족에 힘입어 HBM 부문에서 최대 80%에 육박하는 경이적인 영업이익률을 기록하고 있으며, HBM의 구조적 공급 부족은 향후 수년간 지속될 것으로 전망됩니다.",
            "그럼에도 불구하고 최근 1개월간 필라델피아 반도체 지수(SOX)는 9,993.65로 -20.51% 하락했고, 엔비디아($176.77, -22.9%), TSMC($392.48, -13.4%), SK하이닉스(1,136,000원, -32.4%), 삼성전자(189,900원, -27.5%) 등 한미 대장주들이 일제히 큰 폭의 가격 조정을 받았습니다.",
            "이러한 주가 하락의 원인은 AI 수요가 꺾여서가 아니라, 앞선 매크로 안건에서 확인했듯 연준의 금리 재인상 우려와 미 10년물 국채금리의 4.88% 치솟음으로 인해 기관 투자자들이 고수익률을 기록 중이던 반도체 섹터에서 대규모 차익실현(De-risking)에 나섰기 때문입니다."
        ],
        "previousImplication": "HBM과 AI 칩 실적이 워낙 강력하므로 거시경제 금리와 무관하게 반도체 주가가 일방적인 우상향을 이어갈 것이라는 시사점.",
        "newCatalyst": "HBM 영업이익률 80% 달성에도 불구하고 미 금리 급등 여파로 SOX 지수 -20.5%, 엔비디아 -22.9% 등 급격한 멀티플 조정 발생.",
        "updatedImplication": "실적(EPS)은 여전히 상향 중이나 금리 상승이 밸류에이션(PER)을 누르는 구간. 무리한 레버리지나 단기 추격 매수는 금물이며, 과매도 구간에서 분할 매수로 접근하되 금리 진정 시그널(CPI 둔화 등)을 확인하며 비중을 늘려야 함.",
        "implicationHistory": [
            {"time": "1개월 전", "text": "🟢 AI 반도체 슈퍼사이클 고점 경신 랠리"},
            {"time": "12시간 전", "text": "🔴 매크로 고금리 발작으로 반도체 섹터 차익실현 매물 집중"},
            {"time": "현재 브리핑", "text": "🔴 펀더멘털(이익률 80%)은 견고하나 매크로 할인율 조정 국면 인식 필요"}
        ],
        "actionPoints": [
            "투자 심리 관리: 업황 피크아웃(수요 감소)에 의한 하락이 아닌 '매크로 금리 발 밸류에이션 조정'이므로 패닉셀(투매) 자제",
            "분할 매수 기준: 엔비디아 $170~$175 지지선 및 미 10년물 금리 4.85% 피크아웃 여부를 연동하여 체크"
        ],
        "sources": ["Benzinga Semiconductor", "Yahoo Finance Market Data", "MLQ.ai Earnings Tracker"]
    },
    {
        "id": "agenda_10",
        "category": "tech",
        "categoryLabel": "반도체 · 빅테크 · 2나노",
        "importance": "HIGH",
        "deltaStatus": "REINFORCED",
        "deltaLabel": "🟢 시사점 강화 (빅테크 자체 AI 칩 ASIC 확대)",
        "title": "MS·구글·메타·아마존의 AI 인프라 CapEx 질주와 자체 맞춤형 칩(ASIC) 내재화 가속",
        "subtitle": "잉여현금흐름(FCF) 수익화 검증 요구 속 엔비디아 의존도 낮추기 위한 Maia·TPU 등 자체 실리콘 확대",
        "chartImage": "assets/charts/agenda_10.svg",
        "chartConfig": {
            "type": "bar",
            "title": "4대 하이퍼스케일러(MS·구글·메타·아마존) 합산 연간 AI CapEx 추이 ($B)",
            "subtitle": "다년간의 인프라 구축 사이클 지속… 비용 효율화를 위해 자체 주문형 반도체(ASIC) 비중 급증",
            "categories": ["2023", "2024", "2025", "2026(E)", "2027(E)"],
            "series_name_1": "빅테크 합산 CapEx ($B)",
            "values_1": [148, 215, 285, 345, 390],
            "color_1": "#10b981",
            "unit": "$B"
        },
        "keyMetrics": [
            {"label": "빅테크 AI 투자 시계", "value": "Multi-Decade", "change": "수십 년 단위의 기간 인프라 구축"},
            {"label": "핵심 전략 변화", "value": "Custom ASIC 확대", "change": "MS Maia · Google TPU · AWS Trainium"},
            {"label": "월가 핵심 요구", "value": "FCF 수익화 증명", "change": "투자 대비 현금흐름 회수 타임라인 점검"}
        ],
        "facts": [
            "마이크로소프트(Microsoft), 구글(Alphabet), 메타(Meta), 아마존(AWS) 등 4대 하이퍼스케일러의 연간 설비투자(CapEx) 예산이 역대 최고치를 경신하며 전 세계 AI 데이터센터 확장을 주도하고 있습니다. 빅테크 경영진은 이번 AI 인프라 투자를 단순한 1~2년짜리 IT 사이클이 아닌 향후 수십 년간 지속될 기반 시설 구축으로 규정하고 있습니다.",
            "다만 월가 투자자들은 막대한 CapEx 지출이 실제 잉여현금흐름(FCF)과 소프트웨어 매출로 얼마나 빠르게 회수되는지(Monetization Timeline)를 엄격하게 따지기 시작했습니다.",
            "이러한 수익성 압박을 타개하기 위해 빅테크들이 선택한 핵심 돌파구는 '자체 AI 칩(Custom Silicon / ASIC) 내재화'입니다. 범용 GPU를 전량 구매하는 대신 자사 워크로드에 최적화된 자체 가속기(구글 TPU, MS Maia, AWS Trainium 등) 비중을 높여 총소유비용(TCO)을 낮추고 있으며, 이는 TSMC와 삼성 파운드리, 그리고 브로드컴(Broadcom)·마벨 등 ASIC 설계 파트너들에게 새로운 대형 수주 기회를 열어주고 있습니다."
        ],
        "previousImplication": "빅테크의 AI CapEx가 엔비디아의 범용 GPU 구매에만 90% 이상 독점적으로 집중될 것이라는 시사점.",
        "newCatalyst": "빅테크 FCF 수익성 검증 압박 심화 및 MS·구글·메타·아마존의 자체 커스텀 AI 가속기(ASIC) 양산 물량 급증.",
        "updatedImplication": "AI 투자의 총량(CapEx)은 계속 커지되, 그 내부 구성이 '범용 GPU(학습 및 고성능 추론) + 자체 커스텀 ASIC(대규모 서비스 추론 비용 절감)'의 투트랙으로 빠르게 분화됨.",
        "implicationHistory": [
            {"time": "1개월 전", "text": "🟡 빅테크 과잉투자 논란 대두"},
            {"time": "12시간 전", "text": "🟢 빅테크 CapEx 확대 기조 재확인 및 커스텀 칩 투자 가속"},
            {"time": "현재 브리핑", "text": "🟢 ASIC 생태계 및 선단 파운드리 수혜 시사점 강화"}
        ],
        "actionPoints": [
            "수혜 다변화: 엔비디아 일변도에서 브로드컴(AVGO) 등 커스텀 ASIC 설계 기업 및 파운드리(TSMC)로 AI 포트폴리오 다각화",
            "빅테크 선별: 자체 클라우드와 광고/B2B 소프트웨어에서 즉각적인 AI 매출 전환이 확인되는 메타·MS·구글 선호"
        ],
        "sources": ["FutureX Capital Research", "BusinessKorea Tech", "Hyperscaler Earnings Transcripts"]
    },
    {
        "id": "agenda_11",
        "category": "tech",
        "categoryLabel": "반도체 · 빅테크 · 2나노",
        "importance": "CORE",
        "deltaStatus": "NEW",
        "deltaLabel": "🆕 신규 시사점 (전력 장벽 & 피지컬 AI 확산)",
        "title": "AI 데이터센터 '전력 장벽(Power Wall)'과 엔비디아 '피지컬 AI·디지털 트윈' 한국 제조업 결합",
        "subtitle": "칩 확보보다 더 어려운 전력망·액침냉각 확보전… 삼성·SK·현대차·LG와 엔비디아 옴니버스 동맹",
        "chartImage": "assets/charts/agenda_11.svg",
        "chartConfig": {
            "type": "infographic",
            "title": "차세대 AI 인프라의 2대 확장 축: 전력/열관리 인프라 & 피지컬 AI(Physical AI)",
            "subtitle": "데이터센터의 물리적 한계(Power Wall) 돌파와 제조 현장(로보틱스·디지털 트윈)으로의 AI 확산",
            "center_label": ["Next AI Wave", "전력망 & 피지컬 AI"],
            "badge_text": "Power & Physical AI",
            "nodes": [
                {"title": "전력 장벽 (Power Wall)", "metric": "원전·지열·전력망 직결", "desc": "데이터센터 배포 속도의 최대 결정 변수", "color": "#f59e0b"},
                {"title": "차세대 액침/수랭 냉각", "metric": "2nm·고밀도 랙 열관리", "desc": "공랭식 한계 초과로 액체 냉각 필수화", "color": "#38bdf8"},
                {"title": "반도체 팹 디지털 트윈", "metric": "삼성·SK하이닉스 도입", "desc": "NVIDIA Omniverse로 실시간 공정 최적화", "color": "#10b981"},
                {"title": "피지컬 AI & 로보틱스", "metric": "현대차·LG전자 협력", "desc": "자율주행·휴머노이드·스마트팩토리 확장", "color": "#a855f7"}
            ]
        },
        "keyMetrics": [
            {"label": "최대 물리적 병목", "value": "전력 가용성 (Power)", "change": "원자력·전력망·액체냉각 필수"},
            {"label": "NVIDIA AI Day 서울", "value": "Physical AI 선언", "change": "Omniverse 디지털 트윈 확산"},
            {"label": "국내 핵심 파트너", "value": "삼성·SK·현대차·LG", "change": "제조 공정 및 로보틱스 결합"}
        ],
        "facts": [
            "글로벌 AI 데이터센터 구축 경쟁에서 가장 결정적인 제약 요인이 '반도체 칩 확보'에서 '전력 가용성(Power Availability)'으로 이동했습니다. 차세대 2나노 및 고성능 AI 가속기가 집적된 메가 클러스터는 막대한 전력을 소모하며, 전력망 연결 지연과 초고밀도 서버 랙의 발열 문제가 데이터센터 가동 일정을 좌우하는 물리적 천장(Power Wall)이 되고 있습니다. 이에 빅테크들은 원자력(SMR)·지열 발전 직접 구매 계약 및 첨단 액체 냉각(Liquid Cooling) 기술 도입에 사활을 걸고 있습니다.",
            "동시에 AI의 활용 영역이 챗봇 등 디지털 공간을 넘어 현실 세계의 공장과 로봇을 제어하는 '피지컬 AI(Physical AI)'로 급격히 확장되고 있습니다.",
            "최근 열린 '엔비디아 AI 데이 서울(NVIDIA AI Day Seoul)'에서 엔비디아는 삼성전자 및 SK하이닉스와 손잡고 반도체 제조 라인의 실시간 모니터링과 수율 최적화를 위해 '엔비디아 옴니버스(Omniverse)' 기반 디지털 트윈을 구축한다고 발표했습니다. 또한 현대자동차그룹, LG전자 등 국내 대표 제조 대기업들과 피지컬 AI 및 로보틱스 인프라 협력을 전방위로 확대하고 있습니다."
        ],
        "previousImplication": "AI 테마는 오직 반도체 칩과 클라우드 소프트웨어 기업만의 영역이라는 시사점.",
        "newCatalyst": "데이터센터 전력 장벽(Power Wall) 본격화 및 엔비디아-한국 대기업(삼성·SK·현대차·LG) 간 피지컬 AI·옴니버스 동맹 발표.",
        "updatedImplication": "AI 인프라 투자의 수혜가 변압기·전력망·원전·냉각 시스템 등 에너지 인프라와, 디지털 트윈·로보틱스를 도입해 공정 수율을 높이는 피지컬 AI 제조업으로 폭넓게 확산됨.",
        "implicationHistory": [
            {"time": "1개월 전", "text": "🟢 데이터센터 전력 부족 이슈 부각"},
            {"time": "12시간 전", "text": "🆕 엔비디아 AI 데이 서울 개최 및 삼성·SK·현대차 피지컬 AI 협력 공식화"},
            {"time": "현재 브리핑", "text": "🆕 전력 인프라 + 피지컬 AI(제조·로봇) 양대 확장 시사점 정립"}
        ],
        "actionPoints": [
            "전력 인프라: 북미 데이터센터 전력망 확충에 필수적인 초고압 변압기·전력기기·원전 밸류체인은 반도체 주가 조정 시에도 독자적 모멘텀 보유",
            "피지컬 AI: 현대차·LG전자 등 로보틱스 및 자율주행 팩토리를 엔비디아 생태계와 결합하는 국내 대형 제조주의 중장기 리레이팅 주목"
        ],
        "sources": ["NVIDIA AI Day Seoul Official", "KuCoin Tech Report", "Global Data Center Grid Watch"]
    }
]
