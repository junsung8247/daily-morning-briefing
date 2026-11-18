# -*- coding: utf-8 -*-
"""
2026-11-18 20:00 PM 이브닝 에디션 (2026-11-18_2000) 40대 심층 안건 업데이트 스크립트
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def update_part1():
    p1_path = os.path.join(SCRIPTS_DIR, "agendas_part1.py")
    with open(p1_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/18 모닝", "[11/18 이브닝")

    # Agenda 01: Morning Briefing 100% Hit! KOSPI +1.99% (5,067.44) reclaims 5,000, USD/KRW drops 5.2 won to 1,333.0 won, US 10Y eases to 5.10% ahead of tonight's FOMC Minutes
    text = text.replace(
        '"🟢 시사점 반전 포착! (미 10월 핵심 소매판매 +0.6% 호조 속 정규장 S&P500 7,340.53(-1.03%) 마감 직후, 엔비디아 역대급 실적 서프라이즈로 시간외 선물 급반등! 오늘 밤 FOMC 의사록)"',
        '"🟢 모닝 시사점 100% 적중!! (엔비디아 축포에 코스피 +1.99%(5,067.44) 단숨에 5,000선 탈환! 원/달러 환율 1,333.0원(-5.2원) 급락 안정 & 미 10년물 5.10% 속 오늘 밤 FOMC 의사록)"'
    )
    text = text.replace(
        '"[11/18 이브닝·수요일 반등장 개막] 미 10월 소매판매(+0.2%·핵심 +0.6%) 통과와 엔비디아 시간외 축포: 코스피 5,000선 탈환 및 오늘 밤 FOMC 의사록 전략"',
        '"[11/18 이브닝·코스피 5,067 탈환!] 모닝 브리핑 예고대로 단 하루 만에 \'5,067.44(+1.99%)\' 회복 & 환율 \'1,333.0원\' 안착: 오늘 밤 FOMC 의사록 관전법"'
    )

    # Agenda 06: Vera Rubin NVL72 packs 20.7TB of HBM4 per 72-GPU rack -> SK Hynix (+4.19%) & Samsung Electronics (+2.31%) rally
    text = text.replace(
        '"🟢 시사점 역사적 폭발!! (엔비디아 3분기 매출 \'$115.8B(+103% YoY)\' 어닝 서프라이즈 & 4분기 가이던스 \'$130B\' + 자사주 매입 \'$150B 추가(총 $227B)\' + 베라 루빈 NVL72 출하 공식화!)"',
        '"🟢 시사점 대폭발! (베라 루빈 NVL72 랙당 \'HBM4 무려 20.7TB 탑재\' 괴물 스펙 확인! 오늘 SK하이닉스 +4.19%·삼성전자 +2.31% 동반 급등 이끈 진짜 동력)"'
    )
    text = text.replace(
        '"[11/18 이브닝·엔비디아 실적 대폭발] 매출 $115.8B(+103%)·차기 가이던스 $130B·자사주 $150B 폭격! \'베라 루빈 NVL72 대량 출하\'가 증명한 K-반도체 반격"',
        '"[11/18 이브닝·루빈 랙당 HBM4 20.7TB] 엔비디아 베라 루빈 NVL72 \'랙당 HBM4 20.7TB 흡수\'와 K-반도체 급반등(SK +4.19%·삼성 +2.31%)"'
    )

    # Agenda 10: Samsung Electro-Mechanics (삼성전기) AI server MLCC & ABF substrate double boom alongside Amkor/TSMC CoWoS
    text = text.replace(
        '"🟢 시사점 대폭발! (엔비디아, \'삼성전기(ABF 기판 2028년까지 증설) · 앰코(인터포저 4배 확장) · TSMC\' 차세대 패키징 동맹 공식 발표! 후공정·기판 슈퍼사이클)"',
        '"🟢 시사점 대강화! (엔비디아 2028 ABF 기판 동맹 \'삼성전기\', 수랭식 베라 루빈 서버용 \'초고용량 AI MLCC + FC-BGA 기판\' 쌍끌이 수혜 폭발!)"'
    )
    text = text.replace(
        '"[11/18 이브닝·엔비디아 패키징 동맹] 엔비디아가 지목한 병목 해결사: \'삼성전기(2028 ABF 기판 증설) · 앰코(인터포저 4배)\'와 HBM4 후공정 장비 대호황"',
        '"[11/18 이브닝·삼성전기 기판·MLCC 독식] 엔비디아 베라 루빈이 쏘아 올린 \'삼성전기(ABF 기판 2028 증설 + AI 서버용 고온 MLCC)\'와 후공정 슈퍼사이클"'
    )

    # Agenda 15: Eli Lilly raises full-year 2026 revenue guidance to $91B~$92B (Mounjaro, Zepbound, Foundayo) + Calytrix Bio oncology M&A
    text = text.replace(
        '"🟢 시사점 강화 (일라이 릴리 엔비디아 기반 AI 슈퍼컴 \'릴리팟(LillyPod)\' 가동 & 크레용바이오 \'양자화학 기반 RNA 신약\' 동맹! + EloraTZP -23% 감량)"',
        '"🟢 시사점 대폭발! (일라이 릴리 2026 연간 매출 가이던스 \'$91B~$92B(약 122조 원)\' 전격 상향! 마운자로·젭바운드·경구용 파운다요 삼각편대와 정밀항암 M&A)"'
    )
    text = text.replace(
        '"[11/18 이브닝·AI·양자 신약 제국] 일라이 릴리의 초격차 비결: 엔비디아 AI 슈퍼컴 \'릴리팟(LillyPod)\'과 양자화학 RNA 신약 + EloraTZP -23% 감량"',
        '"[11/18 이브닝·연매출 122조 바이오 제국] 일라이 릴리 2026 가이던스 \'$91B~$92B\' 상향! 마운자로·젭바운드·파운다요 독주와 항암 바이오텍 M&A"'
    )

    with open(p1_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part2():
    p2_path = os.path.join(SCRIPTS_DIR, "agendas_part2.py")
    with open(p2_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/18 모닝", "[11/18 이브닝")

    # Agenda 17: NATO shifts from Cold-War border containment to 'Active Denial & Deep Counter-Strike Doctrine' -> surging demand for Hanwha Aerospace K9/Chunmoo
    text = text.replace(
        '"🟢 시사점 강화 (러시아 \'신(新) 핵 교리(핵사용 문턱 하향)\' 공식 승인 맞불! 유럽 안보 위기감 고조 속 한화에어로스페이스 \'유럽 현지 합작법인(JV)·기술협력\' 가속)"',
        '"🟢 시사점 강화 (NATO 군사독트린 \'수동적 국경방어 ➔ 적 종심 정밀타격·적극적 거부(Active Denial)\' 대전환! 한화에어로 다연장 천무·장사정포 유럽 필수재 등극)"'
    )
    text = text.replace(
        '"[11/18 이브닝·러 핵교리 개정 파장] 에이태큼스 본토 타격에 맞선 러시아 \'핵사용 문턱 하향\' 공식화: 유럽 현지 생산(JV) 장악한 K-방산 수혜"',
        '"[11/18 이브닝·NATO 종심타격 독트린 전환] 냉전식 수동 방어 버린 NATO \'적 종심 타격(Active Denial)\' 채택: 한화에어로 천무·K9이 유럽 표준인 이유"'
    )

    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part3():
    p3_path = os.path.join(SCRIPTS_DIR, "agendas_part3.py")
    with open(p3_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/18 모닝", "[11/18 이브닝")

    with open(p3_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_generator_and_index():
    gen_path = os.path.join(SCRIPTS_DIR, "generate_briefing.py")
    with open(gen_path, "r", encoding="utf-8") as f:
        gtext = f.read()

    old_hl_prefix = '"executiveHeadline": "[11/18 모닝 · 40대 심층안건]'
    for line in gtext.splitlines():
        if old_hl_prefix in line:
            new_line = '        "executiveHeadline": "[11/18 이브닝 · 40대 심층안건] ①거시: 엔비디아 어닝 서프라이즈에 힘입어 수요일 코스피 5,067.44(+1.99%) 단숨에 5,000선 탈환! 원/달러 환율 1,333.0원(-5.2원) 하향 안정 & 미 10년물 5.10% 속 오늘 밤 10월 FOMC 의사록 대기 · ②반도체: 엔비디아 베라 루빈 NVL72 \'랙당 HBM4 20.7TB 탑재\' 확인에 SK하이닉스(+4.19%·청주 M15X)·삼성전자(+2.31%·루빈 HBM4 슬롯 확보) 동반 급등 및 삼성전기(2028 ABF 기판+AI 서버 MLCC) 수혜 · ③미래기술: 일라이 릴리 2026 연간 매출 가이던스 $91B~$92B(약 122조 원) 상향·두산에너빌리티 SMR 상업 본생산 및 미국향 대형 가스터빈 수출·스페이스X 스타십 V4 우주 AI 데이터센터 · ④전쟁/지정학: NATO 군사독트린 \'적 종심 타격(Active Denial)\' 대전환 속 한화에어로(천무·K9) 유럽 재무장 핵심 수혜 · ⑤증시/세테크: 어제 공포장(4,968pt) 매수가 증명한 버핏식 역발상 승리 및 환율 1,333원 구간 달러·미국채 분할 확보 · ⑥금: 중앙은행 월 60~85톤 실물 매집 속 $3,765~$3,865/oz 하방 지지 및 골드만·JP모건 장기 강세 뷰 · ⑦비트코인: 블랙록 IBIT 옵션 기관 헤징 및 스트래티지 850,849 BTC 보유 · ⑧부동산: 스트레스 DSR 한도 축소 속 용산서울코어 8,000호 절충안 및 1기 신도시 선도지구 분담금·사업성 옥석 가리기",'
            gtext = gtext.replace(line, new_line)
            break

    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gtext)

    idx_path = os.path.join(BASE_DIR, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        itext = f.read()
    itext = itext.replace(
        "2026년 11월 18일 · 08:00 AM 모닝 에디션",
        "2026년 11월 18일 · 20:00 PM 이브닝 에디션"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(itext)


if __name__ == "__main__":
    update_part1()
    update_part2()
    update_part3()
    update_generator_and_index()
    print("Successfully updated all 40 agendas for 2026-11-18_2000!")
