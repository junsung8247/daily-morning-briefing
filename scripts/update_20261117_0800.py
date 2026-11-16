# -*- coding: utf-8 -*-
"""
2026-11-17 08:00 AM 모닝 에디션 (2026-11-17_0800) 40대 심층 안건 업데이트 스크립트
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def update_part1():
    p1_path = os.path.join(SCRIPTS_DIR, "agendas_part1.py")
    with open(p1_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/16 이브닝", "[11/17 모닝")

    # Agenda 01: Overnight US equities 3-day pullback ahead of tonight's US Oct Retail Sales (+0.3% consensus), US 10Y 5.13~5.15% stabilization & USD/KRW 1,335.55 defense
    text = text.replace(
        '"🔴 시사점 점검 (미 10년물 5.1%대 경계감에 코스피 5,100.50(-3.59%) 숨고르기 마감! 반면 원/달러 환율은 1,335.7원으로 철벽 안정… 오늘 밤 워시 연준 의장 연설 주목)"',
        '"🔴 시사점 점검 (간밤 미 증시 3거래일 연속 숨고르기 & 미 10년물 금리 5.13~5.15% 고점 진정세! 역외 원/달러 환율 1,335.55원 철벽 방어 속 오늘 밤 \'미 10월 소매판매\' 발표)"'
    )
    text = text.replace(
        '"[11/17 모닝·월요일 마감 총평] 코스피 5,100.50(-3.59%) 조정 속 빛난 \'환율 1,335.7원\'의 방어력: 오늘 밤 워시 의장 연설과 투매 역발상 전략"',
        '"[11/17 모닝·화요일 개장 전략] 미 10년물 \'5.13~5.15%\' 진정세와 역외 환율 \'1,335.55원\' 철벽 수성: 오늘 밤 \'미 10월 소매판매\'가 여는 변곡점"'
    )

    # Agenda 08: TSMC weighing up to 20% price hike for CoWoS packaging & 5~10% for 2nm nodes alongside Nvidia's 15%+ server price hike
    text = text.replace(
        '"🟢 시사점 강화 (미 금리 5.10%·엔비디아 -4.34% 속에서도 TSMC $405.49(-1.90%)로 \'$400 핵심 지지선\' 철벽 방어! 파운드리-메모리 통합의 심장)"',
        '"🟢 시사점 대폭발! (TSMC \'CoWoS 패키징 최대 20% · 2나노 선단공정 5~10% 가격 인상\' 검토! 엔비디아 서버 15%+ 인상에 이은 독점 공급망의 완벽한 가격 전가)"'
    )
    text = text.replace(
        '"[11/17 모닝] 미 금리 5.10% 폭풍 속 \'$405.49(-1.90%)\'로 $400 지지선 지켜낸 TSMC: 모든 AI 칩과 HBM4 베이스다이가 지나는 관문"',
        '"[11/17 모닝·TSMC 가격인상] TSMC \'CoWoS 패키징 20% · 2나노 공정 5~10% 단가 인상\' 추진: 반도체 조정장을 압도할 슈퍼을(乙)의 가격결정력"'
    )

    # Agenda 12: SpaceX Bastrop Gigasat Factory scaling for 'Starmind' sun-synchronous orbital AI data centers + Starship optical laser links
    text = text.replace(
        '"🟢 시사점 대확장! (스타십 \'쉽 42\' 포획 성공에 이은 스페이스X·xAI 결합 프로젝트 \'스타마인드(Starmind · 궤도형 우주 AI 데이터센터)\' 가동! 지상 전력망 한계 돌파)"',
        '"🟢 시사점 강화 (스페이스X 텍사스 배스트럽 \'기가샛 팩토리(Gigasat Factory)\' 풀가동! 태양동기궤도 우주 AI 데이터센터 \'스타마인드\'와 광학 레이저 통신망 구축)"'
    )
    text = text.replace(
        '"[11/17 모닝·우주 AI 데이터센터] 스타십 완전 재사용 완성이 여는 \'스타마인드(Starmind · 궤도형 AI 데이터센터)\': 우주 극저온 냉각과 태양광의 결합"',
        '"[11/17 모닝·스타마인드 양산 기지] 스페이스X 텍사스 \'기가샛 팩토리(Gigasat)\'와 태양동기궤도 우주 AI 데이터센터: 24시간 태양광·진공 냉각 혁명"'
    )

    with open(p1_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part2():
    p2_path = os.path.join(SCRIPTS_DIR, "agendas_part2.py")
    with open(p2_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/16 이브닝", "[11/17 모닝")

    # Agenda 18: US ATACMS stockpile depletion & shift toward cost-effective mass precision artillery/drones boosting Hanwha Aerospace
    text = text.replace(
        '"🟢 시사점 강화 (한화에어로 \'1,773억 독자 무인기 엔진 우선협상자 + 미 한화시마론 인수\'에 이은 한화그룹-KAI 항공우주 수직계열화 시너지 부각!)"',
        '"🟢 시사점 강화 (미 에이태큼스(ATACMS) 등 고가 정밀유도탄 재고 고갈 직면! 가성비·대량양산 갖춘 한화에어로(천무·K9·독자 무인기 엔진 1,773억) 대체 불가 위상)"'
    )
    text = text.replace(
        '"[11/17 모닝·K-방산 대표주 점검] 한화에어로스페이스(641,000원) \'1,773억 독자 무인기 항공엔진 수주 + 미 한화시마론 인수\': 조정장이 준 매수 찬스"',
        '"[11/17 모닝·K-방산 대체불가 해자] 미국조차 바닥난 ATACMS 재고와 \'가성비 대량양산\' 전쟁 패러다임: 한화에어로스페이스(천무·무인기 엔진)의 독식"'
    )

    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part3():
    p3_path = os.path.join(SCRIPTS_DIR, "agendas_part3.py")
    with open(p3_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/16 이브닝", "[11/17 모닝")

    # Agenda 34: Spot Bitcoin ETF Options (IBIT Options) institutional covered call, protective put & delta-hedging expansion
    text = text.replace(
        '"🟢 시사점 강화 (미 국채금리 5.10% 돌파로 블록체인 기반 \'토큰화 미 국채(RWA)\' 수익률도 연 5.10% 시대로! ETF 옵션·WM·401k 인프라 요지부동)"',
        '"🟢 시사점 강화 (블랙록 IBIT 등 \'비트코인 현물 ETF 옵션\' 활용한 월가 기관 커버드콜·프로텍티브 풋·델타헤징 급증! + 토큰화 미 국채(RWA) 연 5.1%+ 수익)"'
    )
    text = text.replace(
        '"[11/17 모닝·크립토 금융 인프라] 미 국채금리 5.10%가 부른 \'토큰화 국채(RWA) 연 5.1% 수익\' 열풍과 9524만원 비트코인을 받치는 월가 배관"',
        '"[11/17 모닝·월가 IBIT 옵션 전략] 블랙록 비트코인 ETF(IBIT) 옵션 활용한 기관 \'커버드콜·하방 헤징\' 폭발과 연 5.1% 토큰화 국채(RWA) 인프라"'
    )

    # Agenda 38: 1st-gen New Town polarization between Bundang/Pyeongchon (high consent & viability) vs reconstruction burden areas + Fast-track Act
    text = text.replace(
        '"🟢 시사점 대강화! (국회 1기 신도시 \'자율정비촉진법(사전승인 ➔ 사후보고 전환)\' 발의! 분당 가격·시공사 선정 독주 + 비규제 \'산본·중동\' 거래량 급증!)"',
        '"🟢 시사점 강화 (1기 신도시 선도지구 내 \'분당·평촌(높은 동의율·사업성)\' 매수세 집중 vs 분담금 우려 지역 양극화 뚜렷! + 국회 \'자율정비촉진법\' 속도전)"'
    )
    text = text.replace(
        '"[11/17 모닝·1기 신도시 입법 & 풍선효과] 국회 \'자율정비촉진법(사전승인➔사후보고)\' 발의로 속도 2배! \'분당\' 독주 속 비규제 \'산본·중동\' 거래 폭발"',
        '"[11/17 모닝·1기 신도시 옥석 가리기] 선도지구 사업성 입증된 \'분당·평촌\' 대장주 집중과 국회 \'자율정비촉진법(사후보고 전환)\'이 가를 수익률 격차"'
    )

    with open(p3_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_generator_and_index():
    gen_path = os.path.join(SCRIPTS_DIR, "generate_briefing.py")
    with open(gen_path, "r", encoding="utf-8") as f:
        gtext = f.read()

    old_hl_prefix = '"executiveHeadline": "[11/16 이브닝 · 40대 심층안건]'
    for line in gtext.splitlines():
        if old_hl_prefix in line:
            new_line = '        "executiveHeadline": "[11/17 모닝 · 40대 심층안건] ①거시: 간밤 미 증시 3거래일 숨고르기 속 미 10년물 금리 5.13~5.15% 진정세 & 역외 원/달러 환율 1,335.55원 철벽 방어(오늘 밤 미 10월 소매판매 발표 주목) · ②반도체: TSMC \'CoWoS 패키징 최대 20% · 2나노 공정 5~10% 단가 인상\' 추진 및 엔비디아 서버 15%+ 가격 인상(독점 공급망 가격전가력 입증, K-메모리 저가매수 기회) · ③미래기술: 스페이스X 텍사스 \'기가샛 팩토리\' 기반 태양동기궤도 우주 AI 데이터센터 \'스타마인드\' 본격화·테슬라 사이버캡 개인 판매($29,990+월 $299 구독)·일라이 릴리 EloraTZP -23% 감량 · ④전쟁/지정학: 미 에이태큼스(ATACMS) 재고 고갈 직면 속 가성비·대량양산 갖춘 한화에어로(천무·K9·무인기 엔진) 수주 해자 재부각 · ⑤증시/세테크: 미 국채 5.13%+환율 1,335원 환노출 채권 바벨 전략 및 연말 해외주식 양도세 22% 손익통산 · ⑥금: $3,885~$4,020/oz 지지선 방어 및 골드만삭스 연말 $4,150·2027년 $4,800 전망(중앙은행 월 60~85톤 매집) · ⑦비트코인: 블랙록 IBIT 옵션 활용한 월가 기관 커버드콜·델타헤징 확산 및 스트래티지 850,364 BTC 보유 · ⑧부동산: 스트레스 DSR 한도 축소 속 1기 신도시 \'분당·평촌\' 사업성 양극화 및 서울 전용 59㎡ 역세권 vs 용산·강남 똘똘한 한 채 재편",'
            gtext = gtext.replace(line, new_line)
            break

    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gtext)

    idx_path = os.path.join(BASE_DIR, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        itext = f.read()
    itext = itext.replace(
        "2026년 11월 16일 · 20:00 PM 이브닝 에디션",
        "2026년 11월 17일 · 08:00 AM 모닝 에디션"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(itext)


if __name__ == "__main__":
    update_part1()
    update_part2()
    update_part3()
    update_generator_and_index()
    print("Successfully updated all 40 agendas for 2026-11-17_0800!")
