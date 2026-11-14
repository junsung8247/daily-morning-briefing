# -*- coding: utf-8 -*-
"""
2026-11-14 20:00 PM 이브닝 에디션 (2026-11-14_2000) 40대 심층 안건 업데이트 스크립트
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def update_part1():
    p1_path = os.path.join(SCRIPTS_DIR, "agendas_part1.py")
    with open(p1_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/14 모닝", "[11/14 이브닝")

    # Agenda 01: Fed Governor Waller hawkish commentary & US 10Y 5.14~5.15% / 2Y 4.85%
    text = text.replace(
        '"🔴 시사점 점검 (미 10월 PPI 전년비 +6.5% 4년래 최고치 쇼크로 미 10년물 금리 5.15% 돌파! 단 다우 +0.10%·S&P500 -0.40%(주간 상승 마감) 선방)"',
        '"🔴 시사점 점검 (월러 연준 이사 \'인플레 지속 시 12월 FOMC 강경 대응\' 매파 발언! 미 10년물 5.14~5.15% · 2년물 4.85% 고금리 장기화 대비)"'
    )
    text = text.replace(
        '"[11/14 이브닝] 미 10월 생산자물가(PPI) \'+6.5% YoY(4년래 최고)\' 쇼크와 10년물 금리 \'5.15%\' 돌파: 금요일 뉴욕 증시(S&P 7,561 · 주간 상승 마감) 총평"',
        '"[11/14 이브닝] 크리스토퍼 월러 연준 이사의 매파 경고와 미 국채 10년물 \'5.14~5.15%\' · 2년물 \'4.85%\': 금리 인하 기대 후퇴 속 생존 포트폴리오"'
    )

    # Agenda 03: BofA Institute Consumer "Trading Down" + WTI $88.56~$88.92 (2nd weekly decline)
    text = text.replace(
        '"🔴 시사점 점검 (미 10월 PPI 도매물가 전년비 +6.5% · 전월비 +0.3% 서프라이즈! 관세·공급망 전가 압력 속 WTI 유가는 $88.41로 안정 유지)"',
        '"🟢 시사점 강화 (BofA 리포트 \'미 가계 가성비 유통 채널로 하향 소비(Trading Down) 뚜렷\' & WTI 유가 $88.56~$88.92로 2주 연속 주간 하락 안정)"'
    )
    text = text.replace(
        '"[11/14 이브닝] 미 10월 생산자물가지수(PPI) \'+6.5% YoY(전월비 +0.3%)\' 4년 만의 최고치: 관세·공급망 비용 전가와 가격결정력(Pricing Power) 기업 선별"',
        '"[11/14 이브닝] 고물가에 지친 미국 소비자의 \'트레이딩 다운(가성비 이동)\'과 2주 연속 하락한 WTI 유가($88.56): 필수소비재·할인점 대장주 부각"'
    )

    # Agenda 05: DXY 103.41 (+0.23%) vs USD/KRW 1,335.00원
    text = text.replace(
        '"🟢 시사점 강화 (미 PPI 쇼크·10년물 5.15% 급등에도 뉴욕 마감 원/달러 환율 1,336.49원(주간 종가 1,336.7원) 철벽 방어! 달러 매수 적기)"',
        '"🟢 시사점 강화 (달러 인덱스 103.41(+0.23%) 강세에도 역외 원/달러 환율 \'1,335.0원\' 하향 안정! 1,335원 구간 달러 분할 매수 찬스)"'
    )
    text = text.replace(
        '"[11/14 이브닝] 미 금리 5.15% 발 강달러에도 원/달러 환율 \'1,336.49원\' 선방: 1,330원대 중반에서 확보하는 달러 현금·단기채 전략"',
        '"[11/14 이브닝] 달러 인덱스(DXY) \'103.41\' 돌파에도 역외 원/달러 환율은 \'1,335.00원\' 안착: 주말 환테크·달러RP 확보 골든타임"'
    )

    # Agenda 06: NVIDIA $162.85 (-2.01%) & Colette Kress / TSMC 3nm custom NVHBM base die
    text = text.replace(
        '"🟢 시사점 강화 (엔비디아 콜레트 크레스 직무대행 이사회 \'차세대 로드맵 무차질\' 공식 확인 & TSMC \'3nm NVHBM 베이스다이 + 3D DRAM\' 투트랙 가속)"',
        '"🟢 시사점 강화 (엔비디아 $162.85(-2.01%) 눌림목 & 콜레트 크레스 체제 \'루빈/HBM4 로드맵 정상 가동 + TSMC 3nm NVHBM 베이스다이 표준화\' 추진)"'
    )
    text = text.replace(
        '"[11/14 이브닝] 엔비디아 콜레트 크레스 체제의 \'투트랙 메모리 승부수\': TSMC 3nm NVHBM 베이스다이 표준화 압박과 차세대 3D DRAM 탐색"',
        '"[11/14 이브닝] 엔비디아($162.85) 콜레트 크레스 체제와 \'TSMC 3nm NVHBM 베이스다이\' 표준화: 메모리 하청화 우려를 돌파할 K-반도체의 해법"'
    )

    # Agenda 07: Samsung & SK Hynix diversifying beyond NVIDIA via Google TPU 8i Max & 8tx (Broadcom partnership)!
    text = text.replace(
        '"🟢 시사점 강화 (삼성전자 206,000원 주간 마감 안착! 2027년 HBM LTA 100% 완판 속 온양 5라인 증설 및 \'자체 4nm vs TSMC 3nm\' 베이스다이 대응)"',
        '"🟢 시사점 대폭발! (삼성전자·SK하이닉스 \'탈(脫)엔비디아 편중 해법\' 가동: 구글 상업용 AI 칩 \'TPU 8i Max · 8tx\' 및 브로드컴 향 HBM 공급 대확장!)"'
    )
    text = text.replace(
        '"[11/14 이브닝] 삼성전자 206,000원(-0.96%) 주간 마감으로 \'20만 원 지지선\' 안착: 2027년 HBM 100% 완판과 온양 5라인·4nm 베이스다이"',
        '"[11/14 이브닝] 엔비디아 의존도 낮추는 삼성전자(206,000원)·SK하이닉스의 비장의 카드: \'구글 TPU 8i Max · 8tx(브로드컴 동맹)\' 향 HBM 공급 확대!"'
    )

    # Agenda 12: SpaceX Starship Flight 15 live outcome: Ship 42 ("Don't Panic") reaches 275km LEO & deploys 26 Starlink V3 satellites (Booster 22 Gulf splashdown)!
    text = text.replace(
        '"🟢 시사점 강화 (스타십 Flight 15 \'블록3 부스터22 + 쉽42\' 고도 275km·스타링크 V3 26기 궤도 실증 & 사우스텍사스 수십억 달러 AI 데이터센터 추진)"',
        '"🟢 시사점 대폭발! (스타십 Flight 15 발사 성공! 상단 \'쉽 42\' 고도 275km 궤도 진입 및 \'스타링크 V3 위성 26기 실전 사출\' 쾌거 · 22시간 궤도 비행 돌입!)"'
    )
    text = text.replace(
        '"[11/14 이브닝·우주+AI 융합] 스타십 Flight 15(부스터22+쉽42 · 스타링크 V3 26기) 궤도 미션과 스페이스X \'사우스텍사스 초대형 AI 데이터센터\' 구축"',
        '"[11/14 이브닝·스타십 Flight 15 속보] 상단 \'쉽 42(Don\'t Panic)\' 275km 저궤도 진입 & \'스타링크 V3 26기 사출\' 성공! (부스터22 멕시코만 안전 착수)"'
    )

    with open(p1_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part2():
    p2_path = os.path.join(SCRIPTS_DIR, "agendas_part2.py")
    with open(p2_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/14 모닝", "[11/14 이브닝")

    # Agenda 21: Uranium $91.85/lb & LME Copper $13,610/t ($6.06/lb) vs WTI $88.56~$88.92/bbl (2nd consecutive weekly drop)
    text = text.replace(
        '"🟢 시사점 강화 (우라늄 파운드당 \'$90.55~$91\' 고공행진 & 구리 톤당 \'$13,200~$13,800\' 강세 vs WTI 유가 \'$88.41(-0.37%)\' 반락)"',
        '"🟢 시사점 강화 (우라늄 현물 \'$91.85/lb\' 연중 최고권 돌파 & LME 구리 \'$13,610/t(전년비 +20%)\' 강세 vs WTI 유가 \'$88.56\' 2주 연속 주간 하락!)"'
    )
    text = text.replace(
        '"[11/14 이브닝·원자재 가격 실증] 우라늄 \'$90.55~$91/lb\' 고공행진 & 구리 \'$13,200~$13,800/t\' vs WTI 유가 \'$88.41(-0.37%)\': 완벽히 갈린 성적표"',
        '"[11/14 이브닝·전략 원자재] 우라늄 \'$91.85/lb\' 추가 상승 & LME 구리 \'$13,610/t(+20% YoY)\' vs WTI 유가 \'$88.56(2주 연속 하락)\' 완벽 디커플링"'
    )

    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part3():
    p3_path = os.path.join(SCRIPTS_DIR, "agendas_part3.py")
    with open(p3_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/14 모닝", "[11/14 이브닝")

    # Agenda 27: Gold $3,887.60~$3,896/oz testing $3,900 recovery threshold despite DXY 103.41 & US10Y 5.14%
    text = text.replace(
        '"🟢 시사점 강화 (미 PPI +6.5% 쇼크·10년물 금리 5.15% 급등에도 국제 금 시세 $3,885~$3,895/oz 견조한 방어! 인플레 헤지 실물 매수세 유입 확인)"',
        '"🟢 시사점 강화 (달러 인덱스 103.41·미 금리 5.14% 압박 속에서도 국제 금 선물 \'$3,887.60~$3,896/oz\' 상승 반전하며 $3,900 재돌파 시도!)"'
    )
    text = text.replace(
        '"[11/14 이브닝] 미 PPI(+6.5%)·금리 5.15% 파고에도 \'$3,885~$3,895/oz\' 지켜낸 국제 금 시세: 스태그플레이션 경계감이 깨운 실물 금 수요"',
        '"[11/14 이브닝] 강달러(DXY 103.41) 이겨내고 \'$3,887.60~$3,896/oz\'로 고개 든 국제 금 시세: $3,900선 탈환 눈앞에 둔 KRX 금현물 전략"'
    )

    # Agenda 37: Olympic Park Foreon (올림픽파크포레온, 12,032가구) 3-year residence obligation deferral expiration & lease maturity fueling jeonse tension
    text = text.replace(
        '"🟢 시사점 강화 (서울 아파트 매매 매물 \'8만 건 돌파\'로 매수자 협상력 우위(+0.07% 둔화) vs 전세는 매물 품귀로 +0.10% 독주 및 2027 전세난 예고!)"',
        '"🟢 시사점 강화 (강동 \'올림픽파크포레온(1.2만 가구)\' 실거주 의무 유예 종료·만기 도래 발 전월세 연쇄 이동 경보! 매매 관망세 속 전세만 독주)"'
    )
    text = text.replace(
        '"[11/14 이브닝·11월 서울 입주절벽과 전세난] 11월 서울 아파트 \'입주 물량 극소화\'가 부른 전세 강세(+0.10%) vs 매매 매물 8만 건 속 역세권 대단지 선별법"',
        '"[11/14 이브닝·전세 시장 뇌관] 강동 \'올림픽파크포레온\' 실거주 의무 유예 종료·임대차 만기가 부르는 동남권 전월세 도미노와 실수요 내집마련 전략"'
    )

    # Agenda 40: "부동산 실용주의" — 1-homeowner basic deduction 14억 + abolishing non-resident 1-homeowner penalty
    text = text.replace(
        '"[11/14 이브닝·종부세 비강남 국평 확산 vs 14억 공제] 비강남권 국민평형까지 번진 종부세 경계선과 \'1주택 기본공제 14억 상향\' 법안 · GTX-A/C/D 역세권 전략"',
        '"[11/14 이브닝·부동산 실용주의 세제개편] \'1주택 종부세 기본공제 14억 상향 + 비거주 1주택 불이익 폐지\' 급물살 & GTX-A/C/D 핵심 역세권 공략"'
    )

    with open(p3_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_generator_and_index():
    gen_path = os.path.join(SCRIPTS_DIR, "generate_briefing.py")
    with open(gen_path, "r", encoding="utf-8") as f:
        gtext = f.read()

    old_hl_prefix = '"executiveHeadline": "[11/14 모닝 · 40대 심층안건]'
    for line in gtext.splitlines():
        if old_hl_prefix in line:
            new_line = '        "executiveHeadline": "[11/14 이브닝 · 40대 심층안건] ①거시: 월러 연준 이사 \'12월 FOMC 매파 경계\' 발언·미 10년물 5.14%·DXY 103.41 속 역외 원/달러 1,335.0원 하향 안정 & 미 소비자 \'가성비 하향소비(Trading Down)\' 뚜렷 · ②반도체: 삼성전자(206,000원)·SK하이닉스(1,216,000원) \'구글 상업용 TPU 8i Max·8tx(브로드컴 동맹)\' 향 HBM 공급 대확장으로 엔비디아 편중 탈피 & HBM4 수율 70% 돌파 · ③미래기술: 스페이스X 스타십 Flight 15 상단 \'쉽42\' 고도 275km 궤도 진입 및 \'스타링크 V3 26기 사출 성공\'(22시간 비행 돌입)·테슬라 무인 로보택시 & 옵티머스 · ④전쟁/지정학: 한화에어로(641,000원) \'1,773억 독자 항공엔진 수주+미 한화시마론 인수\'·우라늄($91.85/lb)·구리($13,610/t) 강세 vs WTI 유가($88.56) 2주 연속 하락 · ⑤증시/세테크: 미 국채 5.14%+환율 1,335원 채권 전략·연말 해외주식 양도세 22% 절세 · ⑥금(강달러 뚫고 $3,887.6~$3,896/oz 반등하며 $3,900 재돌파 시도)·⑦비트코인(실시간 업비트 원화 시세 연동 및 기관 ETF 수급 점검)·⑧부동산(강동 올림픽파크포레온 실거주 유예 종료발 전월세 이동 경보·1주택 종부세 14억 공제 상향 및 비거주 차별 철폐 추진·GTX-A/C/D)",'
            gtext = gtext.replace(line, new_line)
            break

    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gtext)

    idx_path = os.path.join(BASE_DIR, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        itext = f.read()
    itext = itext.replace(
        "2026년 11월 14일 · 08:00 AM 모닝 에디션",
        "2026년 11월 14일 · 20:00 PM 이브닝 에디션"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(itext)


if __name__ == "__main__":
    update_part1()
    update_part2()
    update_part3()
    update_generator_and_index()
    print("Successfully updated all 40 agendas for 2026-11-14_2000!")
