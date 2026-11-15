# -*- coding: utf-8 -*-
"""
2026-11-15 20:00 PM 이브닝 에디션 (2026-11-15_2000) 40대 심층 안건 업데이트 스크립트
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def update_part1():
    p1_path = os.path.join(SCRIPTS_DIR, "agendas_part1.py")
    with open(p1_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/15 모닝", "[11/15 이브닝")

    # Agenda 01: Week-Ahead Macro Calendar (Mon Kevin Warsh AI/Productivity speech, Tue Oct Retail Sales +0.3% consensus, Wed Oct FOMC Minutes) & US 10Y 5.15~5.16%
    text = text.replace(
        '"🔴 시사점 점검 (월러·로건·보우먼 연준 매파 3인방 \'인플레 2% 안착까지 긴축 고삐\' 합창! 실업률 4.1% 견조 속 미 10년물 금리 5.14~5.15% 고착화)"',
        '"🔴 시사점 점검 (이번 주 빅이벤트 주간 개막: 월요일 케빈 워시 연준 의장 연설 ➔ 화요일 미 10월 소매판매(예상 +0.3%) ➔ 수요일 FOMC 의사록! 미 10년물 5.15~5.16%)"'
    )
    text = text.replace(
        '"[11/15 이브닝] 월러·로건·보우먼 연준 매파 3인방의 동시 경고와 미 10년물 \'5.14~5.15%\': 실업률 4.1% 탄탄한 고용이 부른 고금리 장기화 대응법"',
        '"[11/15 이브닝·주간 매크로 프리뷰] 미 10년물 \'5.15~5.16%\' 속 운명의 3일: 워시 의장 연설(월) · 10월 소매판매(화) · FOMC 의사록(수) 완전 해부"'
    )

    # Agenda 06: NVIDIA Earnings Preview (Colette Kress interim CEO, Vera Rubin & HBM4 timeline, TSMC 3nm custom NVHBM base die)
    text = text.replace(
        '"🟢 시사점 강화 (엔비디아 $162.85(-2.01%) 눌림목 & 콜레트 크레스 체제 \'루빈/HBM4 로드맵 정상 가동 + TSMC 3nm NVHBM 베이스다이 표준화\' 추진)"',
        '"🟢 시사점 강화 (엔비디아 실적 발표 주간 카운트다운! 콜레트 크레스 체제 첫 실적콜 3대 관전포인트: \'베라 루빈 일정 · HBM4 물량 · TSMC 3nm NVHBM\')"'
    )
    text = text.replace(
        '"[11/15 이브닝] 엔비디아($162.85) 콜레트 크레스 체제와 \'TSMC 3nm NVHBM 베이스다이\' 표준화: 메모리 하청화 우려를 돌파할 K-반도체의 해법"',
        '"[11/15 이브닝·엔비디아 실적 프리뷰] 전 세계가 주목하는 콜레트 크레스 체제 첫 실적 발표: \'베라 루빈(Rubin) 로드맵\'과 HBM4 공급망 가이던스"'
    )

    # Agenda 07: Samsung 1c DRAM HBM4 qualification imminent & price parity leverage flip + 3D Cube-H / Google TPU
    text = text.replace(
        '"🟢 시사점 강화 (삼성전자 차세대 \'3D Cube-H\' 첨단 패키징 승부수 & 구글 상업용 TPU(8i Max·8tx)·브로드컴 향 HBM 공급 확대로 파운드리·메모리 동시 반격!)"',
        '"🟢 시사점 대폭발! (삼성전자 \'1c D램 기반 HBM4\' 엔비디아 퀄테스트 임박 및 \'할인 없는 가격 협상력(Price Parity) 역전\'! + 3D Cube-H·구글 TPU 확장)"'
    )
    text = text.replace(
        '"[11/15 이브닝] 삼성전자(206,000원) 차세대 \'3D Cube-H\' 패키징과 구글 TPU(브로드컴 동맹) HBM 확장: TSMC 독주를 깨는 양날개 전략"',
        '"[11/15 이브닝] 삼성전자(206,000원) \'1c D램 HBM4\' 퀄테스트 결과 임박: HBM3E 때와 달리 \'할인 없는 제값(Price Parity)\' 받는 공급자 우위 시장!"'
    )

    # Agenda 09: SK Hynix Cheongju P&T6 back-end equipment orders locked in + 70%+ HBM4 yield
    text = text.replace(
        '"🟢 시사점 대폭발! (SK하이닉스 6세대 \'HBM4 양산 수율 70% 돌파\' 쾌거! 금요일 1,216,000원(-3.03%) 눌림목을 압도하는 2029년 완판 펀더멘털)"',
        '"🟢 시사점 강화 (SK하이닉스 \'청주 P&T6 공장 HBM4 후공정(본딩·다이싱·검사) 장비 발주 확정\' & 수율 70% 돌파! 121.6만 원 눌림목 매수 적기)"'
    )
    text = text.replace(
        '"[11/15 이브닝] SK하이닉스(1,216,000원) \'HBM4 양산 수율 70% 전격 돌파\'! HBM3E 매출 추월 카운트다운과 120만 원대 분할 매수 기회"',
        '"[11/15 이브닝] SK하이닉스(1,216,000원) \'청주 P&T6 HBM4 후공정 장비 발주 확정\'과 수율 70% 돌파: 엔비디아 루빈 독점력 굳히기"'
    )

    # Agenda 14: Tesla Optimus Fremont high-volume pilot line (targeting 1M/yr capacity, commercial external sales late 2027)
    text = text.replace(
        '"[11/15 이브닝·피지컬 AI 혁명] 테슬라 \'텍사스·플로리다 24/7 무인 로보택시 & 유료 사이버캡\' 가동과 \'옵티머스 아카데미(자가학습)·기업 렌탈 모델\'!"',
        '"[11/15 이브닝·피지컬 AI 혁명] 테슬라 프리몬트 공장 \'연산 100만 대 목표 옵티머스 양산 라인\' 초기 가동 돌입 & 24/7 무인 로보택시 상용화 가속"'
    )

    with open(p1_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part2():
    p2_path = os.path.join(SCRIPTS_DIR, "agendas_part2.py")
    with open(p2_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/15 모닝", "[11/15 이브닝")

    # Agenda 21: Goldman Sachs & Deutsche Bank projecting structural Copper deficit ($13,000~$14,000+/t into 2027) + CME physical Uranium ($90.25~$91.85/lb)
    text = text.replace(
        '"🟢 시사점 강화 (미 시카고상업거래소(CME) \'실물 우라늄(옐로케이크) 선물·보관 인프라\' 도입 추진! 현물 $91.85/lb 강세 속 금융화 수급 폭발 예고)"',
        '"🟢 시사점 강화 (골드만삭스·도이치뱅크 \'2027년 구리 톤당 $13,000~$14,000+ 구조적 공급부족\' 경고 & CME 실물 우라늄($90.25~$91.85/lb) 선물 추진!)"'
    )
    text = text.replace(
        '"[11/15 이브닝·우라늄 금융화 빅뱅] 시카고상업거래소(CME) \'실물 우라늄(옐로케이크) 선물·보관\' 추진과 파운드당 $91.85 돌파: AI 원전 연료 슈퍼사이클"',
        '"[11/15 이브닝·전략 광물 슈퍼사이클] 골드만·도이치뱅크 \'2027 구리 $14,000/t 구조적 품귀\' 전망과 CME 실물 우라늄($90.25~$91.85/lb) 선물 도입"'
    )

    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part3():
    p3_path = os.path.join(SCRIPTS_DIR, "agendas_part3.py")
    with open(p3_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/15 모닝", "[11/15 이브닝")

    # Agenda 37: Gangnam 3-gu & Seongdong/Gangdong short-term pause under Stress DSR Stage 3 vs non-Gangnam transit complexes & Jeonse/Wolse rise
    text = text.replace(
        '"🟢 시사점 강화 (서울 자치구 과반 \'임대차 월세 비중 50% 돌파\' 구조적 월세화 가속 & 강동 올림픽파크포레온 만기 맞물린 전월세 상승 압력!)"',
        '"🟢 시사점 강화 (스트레스 DSR 3단계 여파로 \'강남3구·성동·강동 단기 숨고르기 전환\' vs \'비강남 역세권 대단지 및 전·월세(비중 50% 돌파) 강세\' 디커플링!)"'
    )
    text = text.replace(
        '"[11/15 이브닝·임대차 패러다임 변화] 서울 자치구 과반 \'월세 비중 50% 돌파\'와 전세 매물 잠김(+0.10%): 월세 수익형 현금흐름 vs 실수요 매수 손익계산"',
        '"[11/15 이브닝·서울 지역별 양극화] 강남3구·성동·강동 \'매매 숨고르기 전환\' vs 비강남 역세권·전월세(월세 비중 50%+) 강세: 급매 협상 타이밍"'
    )

    with open(p3_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_generator_and_index():
    gen_path = os.path.join(SCRIPTS_DIR, "generate_briefing.py")
    with open(gen_path, "r", encoding="utf-8") as f:
        gtext = f.read()

    old_hl_prefix = '"executiveHeadline": "[11/15 모닝 · 40대 심층안건]'
    for line in gtext.splitlines():
        if old_hl_prefix in line:
            new_line = '        "executiveHeadline": "[11/15 이브닝 · 40대 심층안건] ①거시: 이번 주 3대 빅이벤트(월 케빈 워시 연준 의장 AI·생산성 연설 ➔ 화 미 10월 소매판매 예상 +0.3% ➔ 수 10월 FOMC 의사록) 개막 & 미 10년물 금리 5.15~5.16% · ②반도체: 엔비디아 실적 발표 주간 카운트다운(베라 루빈·HBM4 가이던스 주목)·삼성전자(206,000원) \'1c D램 HBM4\' 퀄테스트 임박 및 가격결정력 회복·SK하이닉스(1,216,000원) 청주 P&T6 후공정 장비 발주 확정 · ③미래기술: 스페이스X 스타십 상단 \'쉽42\' 메카질라 로봇팔 포획 사상 최초 성공·테슬라 프리몬트 공장 \'연산 100만 대 목표 옵티머스 라인\' 초기 가동 · ④전쟁/지정학: 한화에어로(641,000원) 1,773억 독자 항공엔진 수주·골드만/도이치뱅크 \'2027 구리 $14,000/t 품귀\' 경고 & CME 실물 우라늄($90.25~$91.85/lb) 선물 추진 · ⑤증시/세테크: 미 국채 5.15%+환율 1,335원 채권 전략·연말 해외주식 양도세 22% 손익통산 · ⑥금: 강달러 속 $3,883~$3,894/oz 지지선 확인 및 중앙은행 실물 매집 · ⑦비트코인: 실시간 업비트 원화 시세 연동 및 미 현물 ETF 7거래일 연속 환매 소화 점검 · ⑧부동산: 스트레스 DSR 3단계 여파 강남3구·성동·강동 단기 숨고르기 vs 비강남 역세권·전월세(월세 비중 50%+) 강세·1주택 종부세 14억 공제 상향 추진",'
            gtext = gtext.replace(line, new_line)
            break

    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gtext)

    idx_path = os.path.join(BASE_DIR, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        itext = f.read()
    itext = itext.replace(
        "2026년 11월 15일 · 08:00 AM 모닝 에디션",
        "2026년 11월 15일 · 20:00 PM 이브닝 에디션"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(itext)


if __name__ == "__main__":
    update_part1()
    update_part2()
    update_part3()
    update_generator_and_index()
    print("Successfully updated all 40 agendas for 2026-11-15_2000!")
