# -*- coding: utf-8 -*-
"""
2026-11-14 08:00 AM 모닝 에디션 (2026-11-14_0800) 40대 심층 안건 업데이트 스크립트
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def update_part1():
    p1_path = os.path.join(SCRIPTS_DIR, "agendas_part1.py")
    with open(p1_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/13 이브닝", "[11/14 모닝")
    text = text.replace("[11/13 모닝", "[11/14 모닝")

    # Agenda 01: US 10Y 5.15% & Oct PPI +6.5% YoY (4-year high) vs S&P 500 7,561.67 (-0.40%) / Nasdaq 25,136.27 (-0.91%) / Dow 52,347.55 (+0.10%)
    text = text.replace(
        '"🟢 시사점 강화 (미 10년물 금리 5.10~5.13% 고공행진 및 12월 연준 경계감 속 오늘 밤 뉴욕 증시·PPI 검증 대기)"',
        '"🔴 시사점 점검 (미 10월 PPI 전년비 +6.5% 4년래 최고치 쇼크로 미 10년물 금리 5.15% 돌파! 단 다우 +0.10%·S&P500 -0.40%(주간 상승 마감) 선방)"'
    )
    text = text.replace(
        '"[11/14 모닝] 미 10년물 국채금리 \'5.10~5.13%\' 압박과 12월 연준 매파 경계감: 오늘 밤 금요일 뉴욕 증시 주간 마감 분수령"',
        '"[11/14 모닝] 미 10월 생산자물가(PPI) \'+6.5% YoY(4년래 최고)\' 쇼크와 10년물 금리 \'5.15%\' 돌파: 금요일 뉴욕 증시(S&P 7,561 · 주간 상승 마감) 총평"'
    )

    # Agenda 02: US 10Y 5.15% bond auction & strategic duration split
    text = text.replace(
        '"[11/14 모닝] 10년물 국채 금리 \'5.10%(+2.10%)\' 재돌파의 역설: 채권 자경단이 선물한 \'5%대 초반 이자 고정(Lock-in)\' 골든타임"',
        '"[11/14 모닝] PPI 물가 충격이 밀어 올린 미 10년물 국채 금리 \'5.15%(주간 +30bp)\': 5.15% 확정이자 구간에서의 단계별 채권 매수 공식"'
    )

    # Agenda 03: US Oct PPI +6.5% YoY (+0.3% MoM) vs WTI $88.41
    text = text.replace(
        '"🟢 시사점 강화 (WTI 유가 저녁 장 $88.41(-0.37% · 1개월 -6.09%)로 재차 반락! $90 저항선 막히며 에너지 물가 안정 재확인)"',
        '"🔴 시사점 점검 (미 10월 PPI 도매물가 전년비 +6.5% · 전월비 +0.3% 서프라이즈! 관세·공급망 전가 압력 속 WTI 유가는 $88.41로 안정 유지)"'
    )
    text = text.replace(
        '"[11/14 모닝] WTI 원유 선물 $88.41(-0.37% · 월간 -6.09%)로 반등 하루 만에 재차 하락: $90 저항선에서 꺾인 유가"',
        '"[11/14 모닝] 미 10월 생산자물가지수(PPI) \'+6.5% YoY(전월비 +0.3%)\' 4년 만의 최고치: 관세·공급망 비용 전가와 가격결정력(Pricing Power) 기업 선별"'
    )

    # Agenda 05: USD/KRW 1,336.49~1,336.70원 vs DXY 103.22
    text = text.replace(
        '"🟢 시사점 강화 (달러 인덱스 103.22(+0.05%) 추가 상승에도 원/달러 환율 1,336.25원 보합 방어! 1,330원대 중반 달러 매수 찬스 지속)"',
        '"🟢 시사점 강화 (미 PPI 쇼크·10년물 5.15% 급등에도 뉴욕 마감 원/달러 환율 1,336.49원(주간 종가 1,336.7원) 철벽 방어! 달러 매수 적기)"'
    )
    text = text.replace(
        '"[11/14 모닝] 달러 인덱스(DXY) \'103.22\' 고공행진 속 원/달러 환율 \'1,336.25원\' 철벽 방어: 주말 앞둔 달러 자산 바겐세일"',
        '"[11/14 모닝] 미 금리 5.15% 발 강달러에도 원/달러 환율 \'1,336.49원\' 선방: 1,330원대 중반에서 확보하는 달러 현금·단기채 전략"'
    )

    # Agenda 06: NVIDIA $166.19 & Colette Kress interim CEO + Two-Track Memory (TSMC 3D DRAM + 3nm NVHBM base die)
    text = text.replace(
        '"🔵 신규 이슈 점검 (엔비디아 $166.19 · 콜레트 크레스(Colette Kress) 리더십 체제 전환 및 TSMC 3nm 커스텀 NVHBM 베이스다이 로드맵 지속)"',
        '"🟢 시사점 강화 (엔비디아 콜레트 크레스 직무대행 이사회 \'차세대 로드맵 무차질\' 공식 확인 & TSMC \'3nm NVHBM 베이스다이 + 3D DRAM\' 투트랙 가속)"'
    )
    text = text.replace(
        '"[11/14 모닝] 엔비디아($166.19) 리더십 전환(콜레트 크레스 직무대행)과 불변의 HBM4 로드맵: TSMC 3nm 커스텀 베이스다이 & 공급망 영향"',
        '"[11/14 모닝] 엔비디아 콜레트 크레스 체제의 \'투트랙 메모리 승부수\': TSMC 3nm NVHBM 베이스다이 표준화 압박과 차세대 3D DRAM 탐색"'
    )

    # Agenda 07: Samsung 206,000원 & Onyang Line 5 / 4nm base die vs NVIDIA standardization pressure
    text = text.replace(
        '"🟢 시사점 강화 (삼성전자 금요일 종가 206,000원(-0.96%)으로 20.6만 선 단단히 지지! 2027년 HBM LTA 100% 완판 및 자체 4nm 베이스다이 무기)"',
        '"🟢 시사점 강화 (삼성전자 206,000원 주간 마감 안착! 2027년 HBM LTA 100% 완판 속 온양 5라인 증설 및 \'자체 4nm vs TSMC 3nm\' 베이스다이 대응)"'
    )

    # Agenda 09: SK Hynix 1,216,000원 & HBM4 yield surpasses 70%!
    text = text.replace(
        '"🟡 시사점 유지 (SK하이닉스 1,216,000원(-3.03%) 금요일 차익 소화로 120만 원 지지선 확인… 2029년 완판 & TSMC 3nm 베이스다이 동맹 건재)"',
        '"🟢 시사점 대폭발! (SK하이닉스 6세대 \'HBM4 양산 수율 70% 돌파\' 쾌거! 금요일 1,216,000원(-3.03%) 눌림목을 압도하는 2029년 완판 펀더멘털)"'
    )
    text = text.replace(
        '"[11/14 모닝] SK하이닉스 1,216,000원(-3.03%) 주간 마감 눌림목과 \'2029년 D램/HBM 완판\' 펀더멘털: TSMC 3nm 베이스다이 동맹의 힘"',
        '"[11/14 모닝] SK하이닉스(1,216,000원) \'HBM4 양산 수율 70% 전격 돌파\'! HBM3E 매출 추월 카운트다운과 120만 원대 분할 매수 기회"'
    )

    # Agenda 12: SpaceX Starship Flight 15 + South Texas multi-billion-dollar AI compute center initiative
    text = text.replace(
        '"🟢 시사점 강화 (오늘 11/13 스타십 Flight 15 \'블록3 부스터22 + 쉽42(Don\'t Panic)\' 출격! 고도 275km·지구 14바퀴(22시간+) 비행 및 더블 캐치)"',
        '"🟢 시사점 강화 (스타십 Flight 15 \'블록3 부스터22 + 쉽42\' 고도 275km·스타링크 V3 26기 궤도 실증 & 사우스텍사스 수십억 달러 AI 데이터센터 추진)"'
    )
    text = text.replace(
        '"[11/14 모닝·스타십 Flight 15 상세 제원] 블록3 \'부스터 22 + 쉽 42(Don\'t Panic)\' 출격: 고도 275km · 지구 14바퀴(22시간+) 체공 후 더블 캐치!"',
        '"[11/14 모닝·우주+AI 융합] 스타십 Flight 15(부스터22+쉽42 · 스타링크 V3 26기) 궤도 미션과 스페이스X \'사우스텍사스 초대형 AI 데이터센터\' 구축"'
    )

    with open(p1_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part2():
    p2_path = os.path.join(SCRIPTS_DIR, "agendas_part2.py")
    with open(p2_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/13 이브닝", "[11/14 모닝")
    text = text.replace("[11/13 모닝", "[11/14 모닝")

    # Agenda 17: Russia-Ukraine war entering 5th year & NATO frontline (Poland/Finland) multi-layered air defense & counter-drone fortifications
    text = text.replace(
        '"🟢 시사점 강화 (푸틴 모스크바 회동서 \'비무장지대(DMZ) 거부·4개주 영토 고수\' 강경 입장 & 키이우·오데사·자포리자 대공습! 방공망 수요 폭발)"',
        '"🟢 시사점 강화 (푸틴 DMZ 거부·우크라 대공습 여파로 폴란드·핀란드 등 NATO 동부전선 \'다층 방공망·대드론·대전차 요새화\' 예산 폭증!)"'
    )
    text = text.replace(
        '"[11/14 모닝·전쟁/지정학] 아부다비 회담 직후 찬물 끼얹은 푸틴 \'비무장지대 거부·4개주 영토 강경 고수\'와 키이우·오데사 대공습"',
        '"[11/14 모닝·전쟁/지정학] 푸틴 DMZ 거부 후 가속화된 NATO 동부전선(폴란드·핀란드) \'다층 방공망·대드론 요새화\': 유럽 재무장 최대 수혜국 한국"'
    )

    # Agenda 18: Hanwha Aerospace 641,000원 (-1.99%) close despite 1,773억 ADD 10,000-lbf engine preferred bidder + KAI/defense consolidation
    text = text.replace(
        '"🟢 시사점 초대형 호재 연타! (한화에어로 \'1,773억 국산 1만파운드급 첨단 항공엔진 우선협상대상자 선정\' + \'미 한화시마론(590억) 인수\'로 북미·항공우주 수직계열화!)"',
        '"🟢 시사점 강화 (한화에어로 641,000원(-1.99%) 숨고르기 속 \'1,773억 독자 항공엔진 우선협상자 선정 + 미 한화시마론 인수 + 폴란드 유도탄 착공\' 3대 모멘텀)"'
    )
    text = text.replace(
        '"[11/14 모닝·한화에어로 겹경사] \'1,773억 독자 항공엔진(1만파운드급 터보팬) 우선협상자 선정\' & \'미국 한화시마론(590억) 인수\'로 방산·우주 제국 완성!"',
        '"[11/14 모닝·K-방산 대표주 점검] 한화에어로스페이스(641,000원) \'1,773억 독자 무인기 항공엔진 수주 + 미 한화시마론 인수\': 조정장이 준 매수 찬스"'
    )

    # Agenda 22: S&P 500 7,561.67 (-0.40%) / Dow 52,347.55 (+0.10%) / KOSPI 5,290.53 (-0.98%, intraday 5,504.44) & Warren Buffett FCF discipline at 5.15% 10Y
    text = text.replace(
        '"[11/14 모닝·거장의 투자원칙] 미 국채 10년물 금리 \'5.10%\' 시대에 빛나는 워런 버핏의 철칙: \'무차입 잉여현금흐름(FCF)과 확실한 가격결정력\'"',
        '"[11/14 모닝·한미 증시 & 버핏 원칙] 미 10년물 \'5.15%\' 속 다우(+0.10%)·S&P500(7,561) 주간 상승 마감 vs 코스피 장중 5,504 터치 후 5,290 마감 해부"'
    )

    # Agenda 26: US 10Y 5.15% & USD/KRW 1,336.49~1,336.70원
    text = text.replace(
        '"미 국채 5.10~5.13% + 환율 1,336.25원"',
        '"미 국채 5.15% + 환율 1,336.5원"'
    )

    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part3():
    p3_path = os.path.join(SCRIPTS_DIR, "agendas_part3.py")
    with open(p3_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/13 이브닝", "[11/14 모닝")
    text = text.replace("[11/13 모닝", "[11/14 모닝")

    # Agenda 27: Gold holds $3,885~$3,895/oz ($3,891.50/oz) despite US PPI +6.5% YoY & 10Y yield 5.15%
    text = text.replace(
        '"🟢 모닝 시사점 즉시 적중! (아침 $3,881.70 바닥 찍고 저녁 $3,893.80/oz(+0.22%) 즉각 반등 성공! $3,880~$3,890 쌍바닥 저가 매수세 유입 입증)"',
        '"🟢 시사점 강화 (미 PPI +6.5% 쇼크·10년물 금리 5.15% 급등에도 국제 금 시세 $3,885~$3,895/oz 견조한 방어! 인플레 헤지 실물 매수세 유입 확인)"'
    )
    text = text.replace(
        '"[11/14 모닝] 아침 바닥($3,881.7) 찍고 \'$3,893.80/oz(+0.22%)\'로 반등 시동 건 국제 금 시세: $3,880 쌍바닥 지지선 완벽 작동!"',
        '"[11/14 모닝] 미 PPI(+6.5%)·금리 5.15% 파고에도 \'$3,885~$3,895/oz\' 지켜낸 국제 금 시세: 스태그플레이션 경계감이 깨운 실물 금 수요"'
    )

    # Agenda 31: Bitcoin rebounds to $73,400 (~9810만원) from $70,800 (9266만원) after $1.3B leverage flush!
    text = text.replace(
        '"deltaStatus": "CHALLENGED",\n        "deltaLabel": "🔴 시사점 점검 (미 PPI 경계감 및 선물 레버리지 $1.3B 강제청산으로 글로벌 BTC $70,800~$70,900 · 원화 \'9266만원(-2.65%)\' 진입! 악성 빚투 청산 후 현물 분할 매수 구간)"',
        '"deltaStatus": "REINFORCED",\n        "deltaLabel": "🟢 이브닝 시사점 정확히 적중! ($70,800 · 9266만원 선물 레버리지 대청소 직후 글로벌 BTC $73,400 · 원화 \'9810만원(+5.87%)\' V자 급반등 성공!)"'
    )
    text = text.replace(
        '"[11/14 모닝·BTC 핵심] 비트코인 \'9266만원(-2.65% · 월간 -16.78%)\' 및 글로벌 $70,800 테스트: \'$1.3B 선물 레버리지 대청소\'가 만든 현물 바겐세일"',
        '"[11/14 모닝·BTC V자 반등] 어제 저녁 \'9266만원($70.8K)\' 바닥 찍고 하룻밤 새 \'9810만원($73,400, +5.87%)\' 탈환한 비트코인: 레버리지 청산 후 숏스퀴즈!"'
    )
    text = text.replace(
        '"value": "9266만원"',
        '"value": "9810만원"'
    )
    text = text.replace(
        '전일 대비 -2.65% 조정받은 9266만원(1개월 변동 -16.78%)**을 기록하며, 글로벌 달러 시세 기준 **$70,800~$70,900 구간(지난 8월 이후 최저치)**에서 파생상품 레버리지 물량 약 13억 달러($1.3B)를 일거에 청산하는 바닥 다지기를 진행하고 있습니다.',
        '어제 저녁 $1.3B 규모의 선물 레버리지 강제청산으로 찍었던 9266만원($70,800) 진바닥에서 하룻밤 사이 +5.87% 급반등한 약 9810만원(글로벌 달러 시세 $73,400~74,000 구간)**을 회복하며 극적인 V자 반등(Short Squeeze)에 성공했습니다.'
    )

    # Agenda 32: Spot BTC ETF outflows (-$284M Nov 12, -$300M Nov 11, YTD -$1.1B in the red led by IBIT, while Morgan Stanley MSBT sees selective inflows)
    text = text.replace(
        '"[11/14 모닝·BTC ETF 수급 분석] 미 PPI 물가 발표 앞둔 현물 ETF 누적 -$1.4B 환매 스트레스와 블랙록 IBIT: 단기 매크로 헤지 물량 정점 통과 중"',
        '"[11/14 모닝·BTC ETF 수급 역설] 미 현물 ETF \'연초 이후 누적 -$1.1B 순유출 전환(11/12 -$284M)\'에도 $73,400(9810만원) 반등한 이유: 모건스탠리 MSBT 유입과 매도 소진"'
    )

    # Agenda 37: Seoul November apartment move-in cliff (입주 물량 급감) vs >80,000 sale listings
    text = text.replace(
        '"[11/14 모닝·서울 매물 8만 건 vs 전세난] 서울 매매 매물 \'8만 건 돌파(상승폭 +0.07% 둔화)\' vs 전세 \'+0.10% 급등\': 쌓인 매물 속 급매 골라잡을 타이밍"',
        '"[11/14 모닝·11월 서울 입주절벽과 전세난] 11월 서울 아파트 \'입주 물량 극소화\'가 부른 전세 강세(+0.10%) vs 매매 매물 8만 건 속 역세권 대단지 선별법"'
    )

    # Agenda 40: Comprehensive Real Estate Tax (종부세) expanding to non-Gangnam 84㎡ (국민평형) vs 14억원 basic deduction push & GTX-A/C/D
    text = text.replace(
        '"[11/14 모닝·부동산 세제 & GTX 빅뉴스] \'1주택자 종부세 기본공제 14억 원 상향(실거주 무관)\' 입법 추진 & GTX-A·C(상록수 착공)·D 핵심 역세권 전략"',
        '"[11/14 모닝·종부세 비강남 국평 확산 vs 14억 공제] 비강남권 국민평형까지 번진 종부세 경계선과 \'1주택 기본공제 14억 상향\' 법안 · GTX-A/C/D 역세권 전략"'
    )

    with open(p3_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_generator_and_index():
    gen_path = os.path.join(SCRIPTS_DIR, "generate_briefing.py")
    with open(gen_path, "r", encoding="utf-8") as f:
        gtext = f.read()

    old_hl_prefix = '"executiveHeadline": "[11/13 이브닝 · 40대 심층안건]'
    for line in gtext.splitlines():
        if old_hl_prefix in line:
            new_line = '        "executiveHeadline": "[11/14 모닝 · 40대 심층안건] ①거시: 미 10월 PPI +6.5% YoY(4년래 최고) 쇼크·10년물 금리 5.15% 돌파 속 뉴욕 증시(다우 +0.10%·S&P500 7,561 주간 상승 마감) 선방 & 원/달러 1,336.5원 방어 · ②반도체: SK하이닉스(1,216,000원) \'HBM4 양산 수율 70% 전격 돌파\'·삼성전자(206,000원) 2027 HBM 100% 완판·엔비디아 콜레트 크레스 체제 \'TSMC 3nm NVHBM+3D DRAM\' 투트랙 · ③미래기술: 스페이스X 스타십 Flight 15(부스터22+쉽42) 궤도 미션 & 사우스텍사스 AI 데이터센터·테슬라 로보택시 & 옵티머스·일라이릴리 경구 비만약 파운다요 · ④전쟁/지정학: 한화에어로(641,000원) \'1,773억 독자 무인기 항공엔진 수주+미 한화시마론 인수\'·NATO 동부전선 다층방공망 요새화·우라늄($91)/구리($13,500) 강세 · ⑤증시/세테크: 코스피 장중 5,504 터치 후 5,290 마감·미 국채 5.15%+환율 1,336.5원 채권 전략·해외주식 양도세 22% 절세 · ⑥금(PPI 쇼크에도 $3,885~$3,895/oz 인플레 헤지 방어!)·⑦비트코인(어제 9266만원 바닥 찍고 하룻밤 새 9810만원·$73,400 V자 급반등 성공!)·⑧부동산(11월 서울 입주절벽 발 전세 +0.10% 강세·비강남 국평 종부세 확산 vs 1주택 공제 14억 상향 추진·GTX-A/C/D)",'
            gtext = gtext.replace(line, new_line)
            break

    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gtext)

    idx_path = os.path.join(BASE_DIR, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        itext = f.read()
    itext = itext.replace(
        "2026년 11월 13일 · 20:00 PM 이브닝 에디션",
        "2026년 11월 14일 · 08:00 AM 모닝 에디션"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(itext)


if __name__ == "__main__":
    update_part1()
    update_part2()
    update_part3()
    update_generator_and_index()
    print("Successfully updated all 40 agendas for 2026-11-14_0800!")
