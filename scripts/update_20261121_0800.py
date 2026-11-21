# -*- coding: utf-8 -*-
"""
2026-11-21 08:00 AM 모닝 에디션 (2026-11-21_0800) 40대 심층 안건 업데이트 스크립트
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def update_part1():
    p1_path = os.path.join(SCRIPTS_DIR, "agendas_part1.py")
    with open(p1_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/19 이브닝", "[11/21 모닝")

    # Agenda 01: Black Friday-level global tech rout! S&P500 -3.70% (6,910.39, correction), Nasdaq -5.28% (22,617.73, YTD wiped), KOSPI -5.21% (4,869.96) vs US 10Y plunging below 5% to 4.95% & USD/KRW 1,336.20 resilience
    text = text.replace(
        '"🟢 시사점 대적중! (목요일 코스피 +1.39%(5,137.89) 2거래일 연속 랠리! SK하이닉스 118.3만(+3.41%)·삼성 19.69만(+1.13%) 급등 & 원/달러 환율 1,330.0원 진입·미 10년물 5.08%)"',
        '"🔴 시사점 긴급 전환! (금요일 글로벌 AI 투매 쇼크: 나스닥 -5.28%(22,617)·S&P500 -3.70%(6,910·조정장 진입)·코스피 -5.21%(4,869)! 반면 미 10년물 4.95% 급락 & 환율 1,336.2원 방어)"'
    )
    text = text.replace(
        '"[11/21 모닝·코스피 5,137 안착!] 기관·외인 쌍끌이에 코스피 \'5,137.89(+1.39%)\' 돌파 & 환율 \'1,330.0원\' 강세: 화요일 공포장(4,968pt) 매수의 완벽한 승리"',
        '"[11/21 모닝·주말 긴급 시황] 나스닥 -5.28%·코스피 4,869(-5.21%) 폭락과 \'12월 금리인상 90% 반영\': 미 10년물 4.95% 하회 속 생존·저가매수 전략"'
    )

    # Agenda 02: US 10Y Treasury Yield drops below 5% to 4.95% on safe-haven flight despite December Fed hike pricing
    text = text.replace(
        '"🔴 시사점 점검 (미 현물 국채 재개장 후 10년물 금리 5.10%(+2.10%) 급등… 단 1개월 고점 대비 -2.61% 낮은 구간으로 \'연 5.1% 확정금리\' 매수 호기)"',
        '"🟢 채권 시사점 대적중! (증시 폭락 속 안전자산 쏠림으로 미 10년물 국채금리 \'5% 하회 ➔ 4.95%\' 급락! 5.1%대 분할매수했던 미국채 완벽한 방패 역할)"'
    )
    text = text.replace(
        '"[11/21 모닝] 미 10년물 국채금리 5.10%(+2.10%) 점프의 진실: 휴장분 일시 반영과 \'연 5.10% 무위험 이자\'를 잠글 절호의 타점"',
        '"[11/21 모닝·국채의 귀환] 증시 -5% 폭락장에 빛난 안전자산 헤지: 미 10년물 금리 \'4.95%\' 하회(채권 가격 급등)와 바벨 포트폴리오의 위력"'
    )

    # Agenda 07: Samsung Electronics plunges -7.31% to 182,500 KRW vs 1c DRAM/4nm base-die HBM4 & 8-layer Q2 2027 Rubin Ultra roadmap
    text = text.replace(
        '"🟢 시사점 대호재! (엔비디아, 베라 루빈 GPU당 \'HBM4 288GB 탑재\' 확정 및 초기 양산 수율 극대화 위해 \'대역폭 22➔19.2TB/s 실용 최적화\'! 삼성전자 196,900원(+1.13%) 수혜)"',
        '"🔴 주가 급락 vs 펀더멘털 괴리 (삼성전자 -7.31% 급락 \'182,500원\' 마감! 그러나 1c D램·4nm 베이스다이 HBM4 및 루빈 울트라용 8단 HBM4 수주 파이프라인 건재)"'
    )
    text = text.replace(
        '"[11/21 모닝·루빈 HBM4 스펙 최적화] 엔비디아 루빈 \'GPU당 HBM4 288GB 탑재 & 수율 중심 대역폭 최적화(19.2TB/s)\': 삼성전자(196,900원) 공급 확대 청신호!"',
        '"[11/21 모닝·삼성전자 18.2만원 급락 점검] 글로벌 AI 투매에 -7.31%(182,500원) 밀린 삼성전자: 1c D램 HBM4·삼성전기 세종/부산 기판 증설 펀더멘털 점검"'
    )

    # Agenda 09: SK Hynix drops -6.59% to 1,105,000 KRW despite locked-in 12-layer HBM4 orders & Nvidia $390B supply commitments
    text = text.replace(
        '"🟢 시사점 대적중! (화요일 109.8만 원 바겐세일 외쳤던 SK하이닉스, 이틀 만에 \'1,183,000원(+3.41%)\' 급반등! 엔비디아 $390B 장기약정 최대 수혜주 입증)"',
        '"🔴 시사점 점검 (글로벌 AI 투매 여파에 SK하이닉스 -6.59% 급락 \'1,105,000원\'! 12단 HBM4 완판·엔비디아 $390B 약정 대비 극단적 매크로 디커플링 구간)"'
    )
    text = text.replace(
        '"[11/21 모닝·SK하이닉스 118.3만 탈환] 이틀 만에 +8.5만 원 치솟은 SK하이닉스(1,183,000원, +3.41%): 엔비디아 520조($390B) 장기 공급약정의 주인공"',
        '"[11/21 모닝·SK하이닉스 110.5만 재조정] 펀더멘털(12단 HBM4·$390B 약정)은 그대로인데 주가만 -6.59%(1,105,000원): 변동성 장세 분할매수 기준선"'
    )

    # Agenda 14: Tesla registers record 200 Cybercabs in a single day in Texas (fleet >1,500 units!), personal Cybercab ($29,990) Dec delivery, Optimus demo in 1-2 months
    text = text.replace(
        '"🟢 시사점 대폭발! (테슬라 운전대·페달 없는 \'사이버캡(Cybercab) 개인 판매($29,990 + 월 $299 자율주행 의무구독)\' 전격 개시! 하드웨어+SaaS 고마진 모델 완성)"',
        '"🟢 시사점 대폭발! (테슬라 텍사스 하루 최다 \'사이버캡 200대 신규 등록 ➔ 누적 1,500대 돌파\'! 개인용 12월 인도 개시 + 1~2개월 내 옵티머스 실전 데모 예고)"'
    )
    text = text.replace(
        '"[11/21 모닝·사이버캡 개인 판매 개시] 운전대 없는 테슬라 \'사이버캡 $29,990 + 월 $299 의무 구독\' 전격 오픈: 2027 Q2 개인 로보택시 네트워크 연결!"',
        '"[11/21 모닝·테슬라 로보택시 1,500대 돌파] 텍사스 하루 200대 등록·총 1,500대 넘어선 사이버캡과 12월 개인 인도 개시: 폭락장 속 피지컬 AI 성장 지표"'
    )

    with open(p1_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part2():
    p2_path = os.path.join(SCRIPTS_DIR, "agendas_part2.py")
    with open(p2_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/19 이브닝", "[11/21 모닝")

    # Agenda 17: UK £240M ($316M) winter air-defense package (1,000+ missiles) & Russia deploying low-cost jet-powered Banderol quasi-cruise missiles
    text = text.replace(
        '"🟢 시사점 강화 (러시아 신형 극초음속 중거리 탄도미사일 \'오레시니크(Oreshnik)\' 실전 배치 위협 속 NATO 동부전선 다층 방공망·장거리 화력 증강! K-방산 수주 가속)"',
        '"🟢 시사점 강화 (영국 \'£2.4억($3.16억) 동계 방공 패키지(미사일 1,000발+)\' 긴급 지원 & 러 저가 제트 미사일 \'반데롤\' 소모전 격화! 요격탄·다층방공 수주 폭발)"'
    )
    text = text.replace(
        '"[11/21 모닝·오레시니크 미사일 파장] 러시아 극초음속 \'오레시니크\' 위협과 NATO 적극적 거부(Active Denial) 독트린: 한화에어로·LIG넥스원 방공·화력 독주"',
        '"[11/21 모닝·유럽 동계 방공전 격화] 영국 $3.16억(미사일 1,000발+) 긴급 지원과 러 \'반데롤\' 소모전: 가성비 요격체계·K-방산 수혜 심화"'
    )

    # Agenda 21: Copper plunges into bear market (-20%+ from Sep peak, COMEX $5.44~$5.50/lb, LME $12,235/t) & WTI 3rd weekly drop ($83.98) vs Uranium rock-solid at $90.10/lb
    text = text.replace(
        '"🟢 시사점 강화 (골드만삭스·도이치뱅크 \'2027년 구리 톤당 $13,000~$14,000+ 구조적 공급부족\' 경고 & CME 실물 우라늄($90.25~$91.85/lb) 선물 추진!)"',
        '"🔴 원자재 극단적 차별화! (구리 2026 최악의 주간 폭락 \'약세장 진입(LME $12,235/t · 고점 대비 -20%+)\' & WTI 3주 연속 하락 $83.98 vs 우라늄 $90.10/lb 철벽 방어!)"'
    )
    text = text.replace(
        '"[11/21 모닝·전략 광물 슈퍼사이클] 골드만·도이치뱅크 \'2027 구리 $14,000/t 구조적 품귀\' 전망과 CME 실물 우라늄($90.25~$91.85/lb) 선물 도입"',
        '"[11/21 모닝·구리 약세장 vs 우라늄 독주] 펀드 청산에 고점 대비 -20% 급락한 구리(중국 실물 프리미엄은 사상 최고!) vs $90.10/lb 사수한 우라늄"'
    )

    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part3():
    p3_path = os.path.join(SCRIPTS_DIR, "agendas_part3.py")
    with open(p3_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/19 이브닝", "[11/21 모닝")

    # Agenda 27: Gold breaks below $3,600 to $3,540~$3,575/oz on ~90% December Fed hike pricing & strong dollar
    text = text.replace(
        '"🟢 시사점 점검 (미 10년물 물가채(TIPS) 실질금리 3% 근접에 금 현물 \'$3,740~$3,755/oz\' 다중 지지선 테스트! 중앙은행 실물 매집 기반 KRX 금현물 분할매수 구간)"',
        '"🔴 시사점 점검 (12월 미 연준 금리인상 확률 90% 급등·강달러 직격탄에 금 현물 \'$3,600 하회 ➔ $3,540~$3,575/oz\' 급락! 단기 패닉 셀링 속 분할매수 타점 재조정)"'
    )
    text = text.replace(
        '"[11/21 모닝·금 실질금리 눌림목] 미 TIPS 실질금리 상승이 만든 금 현물 \'$3,740~$3,755/oz\' 눌림목: 중앙은행 바닥권 지지 활용 KRX 금현물 분할매수"',
        '"[11/21 모닝·금 $3,600 하회 급락] 12월 연준 인상 우려(90%)가 부른 금 현물 \'$3,540~$3,575/oz\' 투매: 패닉 구간의 KRX 금현물 분할 대응 전략"'
    )

    # Agenda 31: Bitcoin slides to 8,250~8,350만원 ($61,500~$63,000) amid >$1B multi-week ETF outflows & global risk-off rout
    text = text.replace(
        '"🟢 이브닝 시사점 정확히 적중! ($70,800 · 9266만원 선물 레버리지 대청소 직후 글로벌 BTC $73,400 · 원화 \'9810만원(+5.87%)\' V자 급반등 성공!)"',
        '"🔴 시사점 긴급 점검 (글로벌 증시 폭락·현물 ETF 10억 달러+ 순유출 여파에 비트코인 \'8,250만원~8,350만원($61,500~$63,000)\' 급락! 현금 비중 유지 및 하방 테스트)"'
    )
    text = text.replace(
        '"[11/21 모닝·BTC V자 반등] 어제 저녁 \'9266만원($70.8K)\' 바닥 찍고 하룻밤 새 \'9810만원($73,400, +5.87%)\' 탈환한 비트코인: 레버리지 청산 후 숏스퀴즈!"',
        '"[11/21 모닝·BTC 8,250만원대 급락 점검] 글로벌 투매·ETF 환매 속 8,250만원~8,350만원($61.5K~$63K) 밀린 비트코인: 레버리지 금지·분할 저가매수 구간"'
    )

    # Agenda 36: Prices hold firm while transaction volume freezes (거래절벽) under Stress DSR, pushing waiting buyers into Jeonse/Wolse
    text = text.replace(
        '"🔵 신규 대출 정책 포착 (스트레스 DSR \'수도권 vs 지방 2원화 체제\' 확정: 지방 주담대는 2026 상반기까지 2단계(1.5%·50%) 유예 vs 수도권은 3단계(3.0%+·100%) 직격탄!)"',
        '"🟢 시사점 강화 (2026년 11월 서울 아파트 \'가격은 버티고 거래는 묶인 거래절벽\' 고착화! 스트레스 DSR 현금 장벽에 대기 수요 전·월세 쏠림 가속)"'
    )
    text = text.replace(
        '"[11/21 모닝·스트레스 DSR 이원화] \'지방은 풀어주고 수도권은 조인다\': 지방 주담대 DSR 3단계 \'2026 상반기까지 추가 유예(2단계 유지)\' vs 수도권 100% 적용!"',
        '"[11/21 모닝·서울 아파트 거래절벽과 전세난] 스트레스 DSR이 만든 \'가격 방어 + 거래량 바닥\' 장세: 현금 부자 중심 재편과 임대차 상승 압력"'
    )

    with open(p3_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_generator_and_index():
    gen_path = os.path.join(SCRIPTS_DIR, "generate_briefing.py")
    with open(gen_path, "r", encoding="utf-8") as f:
        gtext = f.read()

    old_hl_prefix = '"executiveHeadline": "[11/19 이브닝 · 40대 심층안건]'
    for line in gtext.splitlines():
        if old_hl_prefix in line:
            new_line = '        "executiveHeadline": "[11/21 모닝 · 40대 심층안건] ①거시: 금요일 글로벌 기술주·AI 동반 투매 쇼크로 나스닥 -5.28%(22,617·연초대비 상승분 전액 반납)·S&P500 -3.70%(6,910·조정장 진입)·코스피 -5.21%(4,869.96) 급락! 반면 안전자산 쏠림에 미 10년물 금리는 4.95%로 5% 하회 & 원/달러 환율은 1,336.20원 선방 · ②반도체: 글로벌 투매에 삼성전자 182,500원(-7.31%)·SK하이닉스 1,105,000원(-6.59%) 동반 급락했으나, 엔비디아 $390B 장기약정·베라 루빈 HBM4(12단+27년 8단)·삼성전기 세종/부산 기판 증설 등 펀더멘털 이상 무 · ③미래기술: 테슬라 텍사스 하루 최다 사이버캡 200대 신규 등록(누적 1,500대 돌파·개인용 12월 인도)·스페이스X 스타십 V4(70m·9엔진)·두산에너빌리티 뉴스케일 SMR 상업 본생산 · ④전쟁/지정학: 영국 $3.16억 동계 방공 패키지(미사일 1,000발+) 긴급 지원·구리 고점 대비 -20% 약세장 추락(LME $12,235/t) & WTI 3주 연속 하락 $83.98 vs 우라늄 $90.10/lb 철벽 방어 · ⑤증시/세테크: 증시 -5% 폭락장에서 미 10년물 국채(4.95%)가 입증한 버핏식 바벨 전략의 방어력 및 연말 해외주식 양도세 22% 손익통산 · ⑥금: 12월 연준 금리인상 확률 90% 반영·강달러에 금 현물 $3,600 하회($3,540~$3,575/oz) 급락 · ⑦비트코인: ETF 10억 달러+ 환매 및 위험회피에 원화 8,250만원~8,350만원($61,500~$63,000) 급락 및 스트래티지(MSTR) 지수 리밸런싱 압박 · ⑧부동산: 스트레스 DSR 현금 장벽에 서울 아파트 \'가격 방어+거래절벽\' 고착화 및 전·월세 상승 압력 심화",'
            gtext = gtext.replace(line, new_line)
            break

    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gtext)

    idx_path = os.path.join(BASE_DIR, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        itext = f.read()
    itext = itext.replace(
        "2026년 11월 19일 · 20:00 PM 이브닝 에디션",
        "2026년 11월 21일 · 08:00 AM 모닝 에디션"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(itext)


if __name__ == "__main__":
    update_part1()
    update_part2()
    update_part3()
    update_generator_and_index()
    print("Successfully updated all 40 agendas for 2026-11-21_0800!")
