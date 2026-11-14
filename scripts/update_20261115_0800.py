# -*- coding: utf-8 -*-
"""
2026-11-15 08:00 AM 모닝 에디션 (2026-11-15_0800) 40대 심층 안건 업데이트 스크립트
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def update_part1():
    p1_path = os.path.join(SCRIPTS_DIR, "agendas_part1.py")
    with open(p1_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/14 이브닝", "[11/15 모닝")
    text = text.replace("[11/14 모닝", "[11/15 모닝")

    # Agenda 01: Hawkish Fed trio (Waller, Logan, Bowman) & 4.1% unemployment + US 10Y 5.14~5.15%
    text = text.replace(
        '"🔴 시사점 점검 (월러 연준 이사 \'인플레 지속 시 12월 FOMC 강경 대응\' 매파 발언! 미 10년물 5.14~5.15% · 2년물 4.85% 고금리 장기화 대비)"',
        '"🔴 시사점 점검 (월러·로건·보우먼 연준 매파 3인방 \'인플레 2% 안착까지 긴축 고삐\' 합창! 실업률 4.1% 견조 속 미 10년물 금리 5.14~5.15% 고착화)"'
    )
    text = text.replace(
        '"[11/15 모닝] 크리스토퍼 월러 연준 이사의 매파 경고와 미 국채 10년물 \'5.14~5.15%\' · 2년물 \'4.85%\': 금리 인하 기대 후퇴 속 생존 포트폴리오"',
        '"[11/15 모닝] 월러·로건·보우먼 연준 매파 3인방의 동시 경고와 미 10년물 \'5.14~5.15%\': 실업률 4.1% 탄탄한 고용이 부른 고금리 장기화 대응법"'
    )

    # Agenda 07: Samsung 3D Cube-H advanced packaging + Google TPU diversification
    text = text.replace(
        '"🟢 시사점 대폭발! (삼성전자·SK하이닉스 \'탈(脫)엔비디아 편중 해법\' 가동: 구글 상업용 AI 칩 \'TPU 8i Max · 8tx\' 및 브로드컴 향 HBM 공급 대확장!)"',
        '"🟢 시사점 강화 (삼성전자 차세대 \'3D Cube-H\' 첨단 패키징 승부수 & 구글 상업용 TPU(8i Max·8tx)·브로드컴 향 HBM 공급 확대로 파운드리·메모리 동시 반격!)"'
    )
    text = text.replace(
        '"[11/15 모닝] 엔비디아 의존도 낮추는 삼성전자(206,000원)·SK하이닉스의 비장의 카드: \'구글 TPU 8i Max · 8tx(브로드컴 동맹)\' 향 HBM 공급 확대!"',
        '"[11/15 모닝] 삼성전자(206,000원) 차세대 \'3D Cube-H\' 패키징과 구글 TPU(브로드컴 동맹) HBM 확장: TSMC 독주를 깨는 양날개 전략"'
    )

    # Agenda 12: HISTORIC BREAKING NEWS — SpaceX Starship Flight 15 Upper Stage Ship 42 ("Don't Panic") CAUGHT by Mechazilla launch tower arms for the first time in history after 22.5-hour orbital flight!
    text = text.replace(
        '"🟢 시사점 대폭발! (스타십 Flight 15 발사 성공! 상단 \'쉽 42\' 고도 275km 궤도 진입 및 \'스타링크 V3 위성 26기 실전 사출\' 쾌거 · 22시간 궤도 비행 돌입!)"',
        '"🟢 시사점 역사적 정점! (인류 우주사 새 페이지! 스타십 Flight 15 상단 우주선 \'쉽 42\' 22.5시간 궤도 비행 및 대기권 재진입 후 \'메카질라 로봇팔 포획(Tower Catch)\' 사상 최초 성공!!)"'
    )
    text = text.replace(
        '"[11/15 모닝·스타십 Flight 15 속보] 상단 \'쉽 42(Don\'t Panic)\' 275km 저궤도 진입 & \'스타링크 V3 26기 사출\' 성공! (부스터22 멕시코만 안전 착수)"',
        '"[11/15 모닝·인류 최초 쾌거] 스페이스X 스타십 상단 우주선 \'쉽 42\', 22.5시간 궤도 비행 후 발사대 \'메카질라 로봇팔 포획(Ship Catch)\' 사상 최초 성공!"'
    )

    with open(p1_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part2():
    p2_path = os.path.join(SCRIPTS_DIR, "agendas_part2.py")
    with open(p2_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/14 이브닝", "[11/15 모닝")
    text = text.replace("[11/14 모닝", "[11/15 모닝")

    # Agenda 18: Hanwha Group (Hanwha Aerospace / Systems / Ocean) strategic KAI consolidation + Poland/Romania local production
    text = text.replace(
        '"🟢 시사점 강화 (한화에어로 641,000원(-1.99%) 숨고르기 속 \'1,773억 독자 항공엔진 우선협상자 선정 + 미 한화시마론 인수 + 폴란드 유도탄 착공\' 3대 모멘텀)"',
        '"🟢 시사점 강화 (한화에어로 \'1,773억 독자 무인기 엔진 우선협상자 + 미 한화시마론 인수\'에 이은 한화그룹-KAI 항공우주 수직계열화 시너지 부각!)"'
    )

    # Agenda 21: CME Group moving toward physical yellowcake uranium futures & storage solutions + spot $90.25~$91.85/lb
    text = text.replace(
        '"🟢 시사점 강화 (우라늄 현물 \'$91.85/lb\' 연중 최고권 돌파 & LME 구리 \'$13,610/t(전년비 +20%)\' 강세 vs WTI 유가 \'$88.56\' 2주 연속 주간 하락!)"',
        '"🟢 시사점 강화 (미 시카고상업거래소(CME) \'실물 우라늄(옐로케이크) 선물·보관 인프라\' 도입 추진! 현물 $91.85/lb 강세 속 금융화 수급 폭발 예고)"'
    )
    text = text.replace(
        '"[11/15 모닝·전략 원자재] 우라늄 \'$91.85/lb\' 추가 상승 & LME 구리 \'$13,610/t(+20% YoY)\' vs WTI 유가 \'$88.56(2주 연속 하락)\' 완벽 디커플링"',
        '"[11/15 모닝·우라늄 금융화 빅뱅] 시카고상업거래소(CME) \'실물 우라늄(옐로케이크) 선물·보관\' 추진과 파운드당 $91.85 돌파: AI 원전 연료 슈퍼사이클"'
    )

    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part3():
    p3_path = os.path.join(SCRIPTS_DIR, "agendas_part3.py")
    with open(p3_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/14 이브닝", "[11/15 모닝")
    text = text.replace("[11/14 모닝", "[11/15 모닝")

    # Agenda 37: Seoul apartment monthly rent (월세) surpassing 50% share across majority of districts + Olympic Park Foreon maturity
    text = text.replace(
        '"🟢 시사점 강화 (강동 \'올림픽파크포레온(1.2만 가구)\' 실거주 의무 유예 종료·만기 도래 발 전월세 연쇄 이동 경보! 매매 관망세 속 전세만 독주)"',
        '"🟢 시사점 강화 (서울 자치구 과반 \'임대차 월세 비중 50% 돌파\' 구조적 월세화 가속 & 강동 올림픽파크포레온 만기 맞물린 전월세 상승 압력!)"'
    )
    text = text.replace(
        '"[11/15 모닝·전세 시장 뇌관] 강동 \'올림픽파크포레온\' 실거주 의무 유예 종료·임대차 만기가 부르는 동남권 전월세 도미노와 실수요 내집마련 전략"',
        '"[11/15 모닝·임대차 패러다임 변화] 서울 자치구 과반 \'월세 비중 50% 돌파\'와 전세 매물 잠김(+0.10%): 월세 수익형 현금흐름 vs 실수요 매수 손익계산"'
    )

    with open(p3_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_generator_and_index():
    gen_path = os.path.join(SCRIPTS_DIR, "generate_briefing.py")
    with open(gen_path, "r", encoding="utf-8") as f:
        gtext = f.read()

    old_hl_prefix = '"executiveHeadline": "[11/14 이브닝 · 40대 심층안건]'
    for line in gtext.splitlines():
        if old_hl_prefix in line:
            new_line = '        "executiveHeadline": "[11/15 모닝 · 40대 심층안건] ①거시: 월러·로건·보우먼 연준 매파 3인방 \'인플레 2% 안착까지 긴축 유지\' 경고·실업률 4.1% 견조 속 미 10년물 5.14~5.15% & 원/달러 1,335.0원 방어 · ②반도체: 삼성전자(206,000원) 차세대 \'3D Cube-H\' 첨단 패키징 및 구글 TPU(브로드컴 동맹) HBM 확장·SK하이닉스(1,216,000원) HBM4 양산 수율 70% 돌파 · ③미래기술: 인류 우주사 쾌거! 스페이스X 스타십 Flight 15 상단 우주선 \'쉽42\' 22.5시간 궤도 비행 및 대기권 재진입 후 발사대 \'메카질라 로봇팔 포획(Ship Catch)\' 사상 최초 성공! · ④전쟁/지정학: 한화에어로(641,000원) \'1,773억 독자 항공엔진 수주+미 한화시마론 인수\'·CME 거래소 \'실물 우라늄(옐로케이크) 선물\' 추진 및 현물 $91.85/lb 강세 · ⑤증시/세테크: 미 국채 5.14%+환율 1,335원 채권 전략·연말 해외주식 양도세 22% 절세 · ⑥금: 강달러 속 $3,887.6~$3,896/oz 지지력 확보 및 중앙은행 실물 매집 · ⑦비트코인: 실시간 업비트 원화 시세 연동 및 기관 ETF 수급 점검 · ⑧부동산: 서울 자치구 과반 \'임대차 월세 비중 50% 돌파\'·1주택 종부세 14억 공제 상향 및 비거주 차별 철폐 추진·GTX-A/C/D", '
            gtext = gtext.replace(line, new_line.rstrip(", ") + ",")
            break

    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gtext)

    idx_path = os.path.join(BASE_DIR, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        itext = f.read()
    itext = itext.replace(
        "2026년 11월 14일 · 20:00 PM 이브닝 에디션",
        "2026년 11월 15일 · 08:00 AM 모닝 에디션"
    )
    itext = itext.replace(
        "2026년 11월 14일 · 08:00 AM 모닝 에디션",
        "2026년 11월 15일 · 08:00 AM 모닝 에디션"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(itext)


if __name__ == "__main__":
    update_part1()
    update_part2()
    update_part3()
    update_generator_and_index()
    print("Successfully updated all 40 agendas for 2026-11-15_0800!")
