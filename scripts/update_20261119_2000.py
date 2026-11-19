# -*- coding: utf-8 -*-
"""
2026-11-19 20:00 PM 이브닝 에디션 (2026-11-19_2000) 40대 심층 안건 업데이트 스크립트
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def update_part1():
    p1_path = os.path.join(SCRIPTS_DIR, "agendas_part1.py")
    with open(p1_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/19 모닝", "[11/19 이브닝")

    # Agenda 01: Thursday KOSPI +1.39% (5,137.89) 2-day rally! SK Hynix 1,183,000 (+3.41%), Samsung 196,900 (+1.13%), USD/KRW 1,330.0~1,331.0 won, US 10Y 5.08~5.09%
    text = text.replace(
        '"🟢 시사점 강화 (10월 FOMC 의사록 매파 경계감 이겨내고 나스닥 +0.42%(24,429.89) 반등 마감! 유가 안정에 미 10년물 5.07~5.10% 진정 & 역외 원/달러 환율 1,332.46원 강세)"',
        '"🟢 시사점 대적중! (목요일 코스피 +1.39%(5,137.89) 2거래일 연속 랠리! SK하이닉스 118.3만(+3.41%)·삼성 19.69만(+1.13%) 급등 & 원/달러 환율 1,330.0원 진입·미 10년물 5.08%)"'
    )
    text = text.replace(
        '"[11/19 이브닝·목요일 개장 전략] 10월 FOMC 의사록 소화하며 반등한 나스닥(+0.42%)과 미 금리 \'5.07~5.10%\' 안정: 역외 환율 \'1,332.46원\'이 여는 외국인 수급"',
        '"[11/19 이브닝·코스피 5,137 안착!] 기관·외인 쌍끌이에 코스피 \'5,137.89(+1.39%)\' 돌파 & 환율 \'1,330.0원\' 강세: 화요일 공포장(4,968pt) 매수의 완벽한 승리"'
    )

    # Agenda 07: Nvidia optimizes Vera Rubin HBM4 bandwidth (22 TB/s -> 19.2 TB/s) to guarantee initial mass-production yields & packs 288GB HBM4 per GPU -> huge win for Samsung (196,900 KRW, +1.13%) & SK Hynix (1,183,000 KRW, +3.41%)
    text = text.replace(
        '"🟢 시사점 강화 (삼성전자 190,300원(-3.30%) 과매도 진입! 구글·AWS·AMD 다변화된 하이퍼스케일러 HBM 수주 버퍼 + \'1c D램 HBM4\' 퀄테스트 모멘텀)"',
        '"🟢 시사점 대호재! (엔비디아, 베라 루빈 GPU당 \'HBM4 288GB 탑재\' 확정 및 초기 양산 수율 극대화 위해 \'대역폭 22➔19.2TB/s 실용 최적화\'! 삼성전자 196,900원(+1.13%) 수혜)"'
    )
    text = text.replace(
        '"[11/19 이브닝·삼성전자 19만원선 점검] 삼성전자(190,300원, -3.30%) 과매도 구간 진입: 구글·AWS·AMD 멀티 고객망과 \'1c D램 HBM4\' 반격 카드"',
        '"[11/19 이브닝·루빈 HBM4 스펙 최적화] 엔비디아 루빈 \'GPU당 HBM4 288GB 탑재 & 수율 중심 대역폭 최적화(19.2TB/s)\': 삼성전자(196,900원) 공급 확대 청신호!"'
    )

    # Agenda 09: SK Hynix surges +3.41% to 1,183,000 KRW backed by Nvidia's $390B supply commitments & 288GB/GPU HBM4 demand
    text = text.replace(
        '"🟢 시사점 대폭발! (SK하이닉스 \'엔비디아 베라 루빈 초기 HBM4 물량 70% 독점 확보\' 및 장기선급금(LTA) 락인! 오늘 1,098,000원(-1.96%)은 바겐세일)"',
        '"🟢 시사점 대적중! (화요일 109.8만 원 바겐세일 외쳤던 SK하이닉스, 이틀 만에 \'1,183,000원(+3.41%)\' 급반등! 엔비디아 $390B 장기약정 최대 수혜주 입증)"'
    )
    text = text.replace(
        '"[11/19 이브닝·SK하이닉스 109.8만원] 엔비디아 베라 루빈 \'초기 HBM4 물량 70% 독식\'과 선수금(LTA) 락인: 110만 원 하회는 펀더멘털 괴리 저가매수 찬스"',
        '"[11/19 이브닝·SK하이닉스 118.3만 탈환] 이틀 만에 +8.5만 원 치솟은 SK하이닉스(1,183,000원, +3.41%): 엔비디아 520조($390B) 장기 공급약정의 주인공"'
    )

    with open(p1_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part2():
    p2_path = os.path.join(SCRIPTS_DIR, "agendas_part2.py")
    with open(p2_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/19 모닝", "[11/19 이브닝")

    # Agenda 17: Russia's Oreshnik IRBM/ICBM-derivative missile deployment & NATO eastern flank air-defense/artillery reinforcement boosting Hanwha Aerospace
    text = text.replace(
        '"🟢 시사점 강화 (NATO 군사독트린 \'수동적 국경방어 ➔ 적 종심 정밀타격·적극적 거부(Active Denial)\' 대전환! 한화에어로 다연장 천무·장사정포 유럽 필수재 등극)"',
        '"🟢 시사점 강화 (러시아 신형 극초음속 중거리 탄도미사일 \'오레시니크(Oreshnik)\' 실전 배치 위협 속 NATO 동부전선 다층 방공망·장거리 화력 증강! K-방산 수주 가속)"'
    )
    text = text.replace(
        '"[11/19 이브닝·NATO 종심타격 독트린 전환] 냉전식 수동 방어 버린 NATO \'적 종심 타격(Active Denial)\' 채택: 한화에어로 천무·K9이 유럽 표준인 이유"',
        '"[11/19 이브닝·오레시니크 미사일 파장] 러시아 극초음속 \'오레시니크\' 위협과 NATO 적극적 거부(Active Denial) 독트린: 한화에어로·LIG넥스원 방공·화력 독주"'
    )

    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part3():
    p3_path = os.path.join(SCRIPTS_DIR, "agendas_part3.py")
    with open(p3_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/19 모닝", "[11/19 이브닝")

    # Agenda 27: US 10Y TIPS real yield nearing ~3% pushing spot gold to $3,740~$3,755/oz multi-month support zone while central banks provide floor
    text = text.replace(
        '"🟢 시사점 강화 (달러 인덱스 103.41·미 금리 5.14% 압박 속에서도 국제 금 선물 \'$3,887.60~$3,896/oz\' 상승 반전하며 $3,900 재돌파 시도!)"',
        '"🟢 시사점 점검 (미 10년물 물가채(TIPS) 실질금리 3% 근접에 금 현물 \'$3,740~$3,755/oz\' 다중 지지선 테스트! 중앙은행 실물 매집 기반 KRX 금현물 분할매수 구간)"'
    )
    text = text.replace(
        '"[11/19 이브닝] 강달러(DXY 103.41) 이겨내고 \'$3,887.60~$3,896/oz\'로 고개 든 국제 금 시세: $3,900선 탈환 눈앞에 둔 KRX 금현물 전략"',
        '"[11/19 이브닝·금 실질금리 눌림목] 미 TIPS 실질금리 상승이 만든 금 현물 \'$3,740~$3,755/oz\' 눌림목: 중앙은행 바닥권 지지 활용 KRX 금현물 분할매수"'
    )

    with open(p3_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_generator_and_index():
    gen_path = os.path.join(SCRIPTS_DIR, "generate_briefing.py")
    with open(gen_path, "r", encoding="utf-8") as f:
        gtext = f.read()

    old_hl_prefix = '"executiveHeadline": "[11/19 모닝 · 40대 심층안건]'
    for line in gtext.splitlines():
        if old_hl_prefix in line:
            new_line = '        "executiveHeadline": "[11/19 이브닝 · 40대 심층안건] ①거시: 목요일 코스피 +1.39%(5,137.89) 2거래일 연속 랠리로 5,130선 안착! 원/달러 환율 1,330.01~1,331.07원 강세 및 미 10년물 금리 5.08~5.09% 안정 · ②반도체: 엔비디아 $390B(약 520조 원) 장기 공급약정 발표 및 베라 루빈 \'GPU당 HBM4 288GB 탑재·양산 수율 극대화 위한 대역폭 최적화(19.2TB/s)\' 호재에 SK하이닉스 1,183,000원(+3.41%)·삼성전자 196,900원(+1.13%) 동반 급등 · ③미래기술: 두산에너빌리티 뉴스케일 SMR 상부 원자로 압력용기(URPV) 상업 본생산 및 미국 가스터빈 수주·스페이스X 스타십 V4 궤도 연료 이송 및 옵티머스 화성 선발대 · ④전쟁/지정학: 러시아 신형 중거리 탄도미사일 \'오레시니크\' 위협과 NATO 적 종심 타격 독트린 전환 속 한화에어로·LIG넥스원 수주 확대 · ⑤증시/세테크: 원/달러 1,330원 초입 환노출 미국채(연 5.08%) 분할 확보 및 연말 해외주식 양도세 22% 손익통산 · ⑥금: 미 TIPS 실질금리 상승에 따른 $3,740~$3,755/oz 지지선 테스트 및 신흥국 중앙은행 실물 매집 바닥 방어 · ⑦비트코인: 블랙록 IBIT 옵션 기관 헤징 거래 활성화·스트래티지 850,849 BTC 보유 및 업비트 원화 시세 연동 · ⑧부동산: 스트레스 DSR 한도 축소 속 용산국제업무지구·1기 신도시 선도지구(추가 분담금 옥석 가리기)·GTX-A 역세권 차별화",'
            gtext = gtext.replace(line, new_line)
            break

    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gtext)

    idx_path = os.path.join(BASE_DIR, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        itext = f.read()
    itext = itext.replace(
        "2026년 11월 19일 · 08:00 AM 모닝 에디션",
        "2026년 11월 19일 · 20:00 PM 이브닝 에디션"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(itext)


if __name__ == "__main__":
    update_part1()
    update_part2()
    update_part3()
    update_generator_and_index()
    print("Successfully updated all 40 agendas for 2026-11-19_2000!")
