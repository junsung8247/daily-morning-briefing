# -*- coding: utf-8 -*-
"""
2026-11-19 08:00 AM 모닝 에디션 (2026-11-19_0800) 40대 심층 안건 업데이트 스크립트
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def update_part1():
    p1_path = os.path.join(SCRIPTS_DIR, "agendas_part1.py")
    with open(p1_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/18 이브닝", "[11/19 모닝")

    # Agenda 01: Oct FOMC Minutes digested! Nasdaq bucks trend to close UP +0.42% (24,429.89), US 10Y eases to 5.07~5.10%, USD/KRW drops to 1,332.46 won
    text = text.replace(
        '"🟢 모닝 시사점 100% 적중!! (엔비디아 축포에 코스피 +1.99%(5,067.44) 단숨에 5,000선 탈환! 원/달러 환율 1,333.0원(-5.2원) 급락 안정 & 미 10년물 5.10% 속 오늘 밤 FOMC 의사록)"',
        '"🟢 시사점 강화 (10월 FOMC 의사록 매파 경계감 이겨내고 나스닥 +0.42%(24,429.89) 반등 마감! 유가 안정에 미 10년물 5.07~5.10% 진정 & 역외 원/달러 환율 1,332.46원 강세)"'
    )
    text = text.replace(
        '"[11/19 모닝·코스피 5,067 탈환!] 모닝 브리핑 예고대로 단 하루 만에 \'5,067.44(+1.99%)\' 회복 & 환율 \'1,333.0원\' 안착: 오늘 밤 FOMC 의사록 관전법"',
        '"[11/19 모닝·목요일 개장 전략] 10월 FOMC 의사록 소화하며 반등한 나스닥(+0.42%)과 미 금리 \'5.07~5.10%\' 안정: 역외 환율 \'1,332.46원\'이 여는 외국인 수급"'
    )

    # Agenda 06: Nvidia's Long-Term Supply Purchase & Capacity Reservation Commitments jump +$111B in a single quarter to $390 Billion!
    text = text.replace(
        '"🟢 시사점 대폭발! (베라 루빈 NVL72 랙당 \'HBM4 무려 20.7TB 탑재\' 괴물 스펙 확인! 오늘 SK하이닉스 +4.19%·삼성전자 +2.31% 동반 급등 이끈 진짜 동력)"',
        '"🟢 시사점 역사적 대폭발!! (엔비디아 \'장기 공급계약·캐파 예약 약정액 1개 분기 만에 +$111B 폭증한 $390B(약 520조 원)\' 달성! HBM4·CoWoS·기판 싹쓸이 입증)"'
    )
    text = text.replace(
        '"[11/19 모닝·루빈 랙당 HBM4 20.7TB] 엔비디아 베라 루빈 NVL72 \'랙당 HBM4 20.7TB 흡수\'와 K-반도체 급반등(SK +4.19%·삼성 +2.31%)"',
        '"[11/19 모닝·엔비디아 520조 입도선매] 엔비디아 장기 공급약정액 \'$390B(분기 +$111B 폭증)\'의 충격: 삼성·SK HBM4와 TSMC 패키징을 통째로 예약했다!"'
    )

    # Agenda 12: SpaceX Starship orbital propellant transfer & uncrewed Mars cargo mission carrying Tesla Optimus humanoid robots as autonomous crew
    text = text.replace(
        '"🟢 시사점 대폭발! (일론 머스크 차세대 \'스타십 V4(상단 70m·길이 40% 확장·9엔진)\' 전격 공개! 배스트럽 기가샛 공장과 우주 AI 데이터센터 \'스타마인드\' 수송력 극대화)"',
        '"🟢 시사점 강화 (스페이스X \'스타십 궤도 연료 이송\' 및 \'테슬라 옵티머스 휴머노이드 탑승 화성 무인 선발대\' 로드맵 가동! 우주-로봇-AI 삼각 생태계 결합)"'
    )
    text = text.replace(
        '"[11/19 모닝·스타십 V4 전격 공개] 상단 우주선 길이 40% 키운 \'스타십 V4(70m·9엔진)\' 로드맵과 우주 AI 데이터센터 \'스타마인드\' 대량 발사 시대"',
        '"[11/19 모닝·우주·로봇 대통합] 스타십 V4 \'궤도 연료 이송\'과 \'옵티머스 로봇 화성 선발대\' 프로젝트: 스페이스X·테슬라·xAI 밸류체인 재평가"'
    )

    # Agenda 13: NuScale adopts Everstar Gordian AI platform for NRC licensing + NY Power Authority (NYPA) SMR pipeline + Gyeongnam/Doosan Enerbility global SMR hub
    text = text.replace(
        '"🟢 시사점 강화 (두산에너빌리티, 뉴스케일 SMR 상업 본생산 + \'미국향 대형 가스터빈 수출 및 AI 디지털트윈 원전 용접 자동화\' 완성! AI 전력망 올라운더)"',
        '"🟢 시사점 강화 (뉴스케일 \'Gordian AI 인허가 가속 플랫폼\' 도입 & 미 뉴욕전력청(NYPA) SMR 파이프라인 가동! 경남·두산에너빌리티 글로벌 SMR 제조 허브 도약)"'
    )
    text = text.replace(
        '"[11/19 모닝·두산에너빌리티 양날개] 뉴스케일 SMR 상업 본생산 + \'미국향 가스터빈 수출 & AI 디지털트윈 원전 제조\': AI 데이터센터 전력 독점"',
        '"[11/19 모닝·미국 SMR 인허가 가속] 뉴스케일 \'AI 인허가 가속\' & 뉴욕전력청(NYPA) SMR 추진: 글로벌 SMR 파운드리 두산에너빌리티 수주 확대"'
    )

    with open(p1_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part2():
    p2_path = os.path.join(SCRIPTS_DIR, "agendas_part2.py")
    with open(p2_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/18 이브닝", "[11/19 모닝")

    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part3():
    p3_path = os.path.join(SCRIPTS_DIR, "agendas_part3.py")
    with open(p3_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/18 이브닝", "[11/19 모닝")

    # Agenda 35: Korean corporate/institutional crypto account access & tax timeline discussions + Bitcoin 95%+ discipline
    text = text.replace(
        '"🟢 시사점 강화 (미 금리 5.10% 점프에 알트코인 유동성 급감 vs 200일선($73.7K · 9524만원) 지켜낸 \'비트코인 95%+ 집중 / 알트 5% 미만\' 철칙)"',
        '"🟢 시사점 강화 (국내 법인·기관 가상자산 실명계좌 단계적 허용 및 과세 유예 논의 급물살! 기관 장세일수록 \'비트코인 95%+ 집중 / 알트 5% 미만\' 철칙 유효)"'
    )
    text = text.replace(
        '"[11/19 모닝·크립토 생존 철칙] 미 금리 \'5.10%\'의 밤이 증명한 진리: 왜 가상화폐는 \'비트코인(9524만원) 95% 이상 · 알트코인 5% 미만\'이어야 하는가?"',
        '"[11/19 모닝·국내 법인계좌 허용과 BTC 집중] 한국도 \'법인·기관 가상자산 계좌\' 열린다: 알트 변동성 피하고 \'비트코인 95% 이상\'에 집중해야 할 이유"'
    )

    with open(p3_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_generator_and_index():
    gen_path = os.path.join(SCRIPTS_DIR, "generate_briefing.py")
    with open(gen_path, "r", encoding="utf-8") as f:
        gtext = f.read()

    old_hl_prefix = '"executiveHeadline": "[11/18 이브닝 · 40대 심층안건]'
    for line in gtext.splitlines():
        if old_hl_prefix in line:
            new_line = '        "executiveHeadline": "[11/19 모닝 · 40대 심층안건] ①거시: 간밤 10월 FOMC 의사록 매파 경계감을 이겨내고 나스닥 +0.42%(24,429.89) 반등 마감! 유가 하락에 미 10년물 국채금리 5.07~5.10% 진정 & 역외 원/달러 환율 1,332.46원 강세 · ②반도체: 엔비디아 \'장기 공급구매·캐파 예약 약정액이 단 1개 분기 만에 +$111B 폭증한 총 $390B(약 520조 원)\' 달성! SK하이닉스·삼성전자 HBM4와 TSMC CoWoS·삼성전기 ABF 기판 다년 입도선매 확인 · ③미래기술: 스페이스X 스타십 궤도 연료 이송 및 옵티머스 로봇 화성 선발대 로드맵·뉴스케일 AI 인허가 가속 및 뉴욕전력청(NYPA) SMR 추진(두산에너빌리티 수혜)·일라이 릴리-엔비디아 AI 신약 연구소 · ④전쟁/지정학: 우크라 에이태큼스·스톰섀도 타격과 NATO 적 종심 타격 독트린 전환 속 한화에어로 유럽 수주 확대 · ⑤증시/세테크: 원/달러 환율 1,332원 진입을 활용한 달러·환노출 미국채 분할 매수 및 연말 해외주식 양도세 22% 손익통산 · ⑥금: 미 실질금리 부담 속 $3,735~$3,850/oz 분할 매수 구간 및 신흥국 중앙은행 실물 매집 · ⑦비트코인: 블랙록 IBIT 옵션 기관 거래 확대·스트래티지 850,849 BTC 보유 및 국내 법인 가상자산 계좌 허용 논의 · ⑧부동산: 스트레스 DSR 한도 축소 속 매매 관망·전월세 강세 디커플링 및 용산국제업무지구·1기 신도시·GTX-A 핵심지 차별화",'
            gtext = gtext.replace(line, new_line)
            break

    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gtext)

    idx_path = os.path.join(BASE_DIR, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        itext = f.read()
    itext = itext.replace(
        "2026년 11월 18일 · 20:00 PM 이브닝 에디션",
        "2026년 11월 19일 · 08:00 AM 모닝 에디션"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(itext)


if __name__ == "__main__":
    update_part1()
    update_part2()
    update_part3()
    update_generator_and_index()
    print("Successfully updated all 40 agendas for 2026-11-19_0800!")
