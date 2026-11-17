# -*- coding: utf-8 -*-
"""
2026-11-18 08:00 AM 모닝 에디션 (2026-11-18_0800) 40대 심층 안건 업데이트 스크립트
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def update_part1():
    p1_path = os.path.join(SCRIPTS_DIR, "agendas_part1.py")
    with open(p1_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/17 이브닝", "[11/18 모닝")

    # Agenda 01: US Oct Retail Sales (+0.2% MoM, Core +0.6% beat), S&P 500 regular close 7,340.53 (-1.03%) followed by Nvidia after-hours blowout (+2~4%) & tonight's FOMC Minutes
    text = text.replace(
        '"🔴 시사점 점검 (화요일 코스피 4,968.48(-2.59%) 9개월 만의 5,000선 하회! 그러나 원/달러 환율 1,338.2원·미 10년물 5.12% 안정으로 \'외환위기 없는 과매도\' 입증)"',
        '"🟢 시사점 반전 포착! (미 10월 핵심 소매판매 +0.6% 호조 속 정규장 S&P500 7,340.53(-1.03%) 마감 직후, 엔비디아 역대급 실적 서프라이즈로 시간외 선물 급반등! 오늘 밤 FOMC 의사록)"'
    )
    text = text.replace(
        '"[11/18 모닝·화요일 마감 긴급점검] 코스피 \'4,968.48(-2.59%)\' 언더슈팅에도 환율은 \'1,338.2원\' 요지부동: 오늘 밤 미 소매판매와 공포 매수 타점"',
        '"[11/18 모닝·수요일 반등장 개막] 미 10월 소매판매(+0.2%·핵심 +0.6%) 통과와 엔비디아 시간외 축포: 코스피 5,000선 탈환 및 오늘 밤 FOMC 의사록 전략"'
    )

    # Agenda 06: Nvidia Q3 FY2027 Earnings Blowout ($115.8B rev +103% YoY, Q4 guidance $130B, +$150B buyback -> $227B pool, Vera Rubin NVL72 volume shipments underway)
    text = text.replace(
        '"🟢 시사점 대폭발! (엔비디아, 빅테크 고객사에 \'블랙웰·베라 루빈 AI 서버 시스템 가격 15% 이상 인상\' 통보! HBM4·CoWoS 원가 상승분 100% 가격 전가력 입증)"',
        '"🟢 시사점 역사적 폭발!! (엔비디아 3분기 매출 \'$115.8B(+103% YoY)\' 어닝 서프라이즈 & 4분기 가이던스 \'$130B\' + 자사주 매입 \'$150B 추가(총 $227B)\' + 베라 루빈 NVL72 출하 공식화!)"'
    )
    text = text.replace(
        '"[11/18 모닝·엔비디아 가격인상] 엔비디아 \'블랙웰·베라 루빈 서버 가격 15%+ 전격 인상\' 통보! 삼성(-4.47%)·SK(-7.89%) 과매도를 줍는 확실한 근거"',
        '"[11/18 모닝·엔비디아 실적 대폭발] 매출 $115.8B(+103%)·차기 가이던스 $130B·자사주 $150B 폭격! \'베라 루빈 NVL72 대량 출하\'가 증명한 K-반도체 반격"'
    )

    # Agenda 10: Nvidia locks in 2028 ABF substrate & packaging expansion with Samsung Electro-Mechanics (삼성전기), Amkor (4x interposer), SPIL & TSMC
    text = text.replace(
        '"🟢 시사점 강화 (미 금리 5.10% 속 필라델피아 반도체 지수(SOX) 10,506.67(-0.54%)로 10,500pt 사수! 삼성 온양 5라인·SK MR-MUF 후공정 장비 발주 탄력)"',
        '"🟢 시사점 대폭발! (엔비디아, \'삼성전기(ABF 기판 2028년까지 증설) · 앰코(인터포저 4배 확장) · TSMC\' 차세대 패키징 동맹 공식 발표! 후공정·기판 슈퍼사이클)"'
    )
    text = text.replace(
        '"[11/18 모닝] 미 금리 5.10%에도 \'10,506pt(-0.54%)\' 지켜낸 필라델피아 반도체(SOX): 2029년까지 완판된 HBM4가 부른 후공정 장비 대호황"',
        '"[11/18 모닝·엔비디아 패키징 동맹] 엔비디아가 지목한 병목 해결사: \'삼성전기(2028 ABF 기판 증설) · 앰코(인터포저 4배)\'와 HBM4 후공정 장비 대호황"'
    )

    # Agenda 13: Doosan Enerbility US gas turbine deals + AI digital-twin nuclear welding automation alongside NuScale SMR commercial production
    text = text.replace(
        '"🟢 시사점 대강화! (두산에너빌리티, 미 뉴스케일파워와 \'SMR 상부 원자로 압력용기 모듈 상업 본생산 계약\' 체결! 창원 공장 풀가동 + 미 NRC 엑스에너지 허가 겹호재)"',
        '"🟢 시사점 강화 (두산에너빌리티, 뉴스케일 SMR 상업 본생산 + \'미국향 대형 가스터빈 수출 및 AI 디지털트윈 원전 용접 자동화\' 완성! AI 전력망 올라운더)"'
    )
    text = text.replace(
        '"[11/18 모닝·두산에너빌리티 본생산 계약] 두산에너빌리티-뉴스케일 \'SMR 상부 원자로 모듈 상업 본생산 계약\' 체결! 창원 SMR 파운드리 가동 돌입"',
        '"[11/18 모닝·두산에너빌리티 양날개] 뉴스케일 SMR 상업 본생산 + \'미국향 가스터빈 수출 & AI 디지털트윈 원전 제조\': AI 데이터센터 전력 독점"'
    )

    with open(p1_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part2():
    p2_path = os.path.join(SCRIPTS_DIR, "agendas_part2.py")
    with open(p2_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/17 이브닝", "[11/18 모닝")

    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part3():
    p3_path = os.path.join(SCRIPTS_DIR, "agendas_part3.py")
    with open(p3_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/17 이브닝", "[11/18 모닝")

    # Agenda 28: World Gold Council (WGC) Q3/Q4 official sector accumulation led by China, Poland, and Uzbekistan supporting $3,850~$3,865/oz floor
    text = text.replace(
        '"🟢 시사점 강화 (금 선물 $3,881.70 투매를 두 팔 벌려 받아내는 \'중국·신흥국 중앙은행 월 60~85톤 실물 매집\'… $3,880~$3,900 진바닥 형성)"',
        '"🟢 시사점 강화 (세계금협회(WGC) 확인 \'중국·폴란드·우즈베키스탄 중앙은행 공격적 금 매집\' 지속! 미 금리 5.14% 속에서도 $3,850~$3,865/oz 철벽 지지)"'
    )
    text = text.replace(
        '"[11/18 모닝] 헤지펀드가 던진 \'$3,881 금 선물\'을 중국·신흥국 중앙은행이 웃으며 줍는 이유: 월 60~85톤 실물 금괴 흡수 메커니즘"',
        '"[11/18 모닝·세계금협회 중앙은행 수급] 중국·폴란드·우즈베키스탄 중앙은행이 쓸어담는 실물 금괴: $3,850~$3,865/oz 진바닥과 JP모건 $6,000+ 장기 뷰"'
    )

    with open(p3_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_generator_and_index():
    gen_path = os.path.join(SCRIPTS_DIR, "generate_briefing.py")
    with open(gen_path, "r", encoding="utf-8") as f:
        gtext = f.read()

    old_hl_prefix = '"executiveHeadline": "[11/17 이브닝 · 40대 심층안건]'
    for line in gtext.splitlines():
        if old_hl_prefix in line:
            new_line = '        "executiveHeadline": "[11/18 모닝 · 40대 심층안건] ①거시: 미 10월 소매판매(+0.2%·핵심 +0.6% 호조) 및 미 10년물 5.14% 속 정규장 S&P500 7,340.53(-1.03%) 마감 직후 엔비디아 어닝 서프라이즈로 시간외 선물 반등(오늘 밤 10월 FOMC 의사록 공개) · ②반도체: 엔비디아 FY27 3분기 매출 $115.8B(+103% YoY)·4분기 가이던스 $130B·자사주 매입 $150B 추가(총 $227B) 역대급 실적 폭격! \'베라 루빈 NVL72 대량 출하 공식화\' 및 삼성전기(2028 ABF 기판 증설)·앰코(인터포저 4배)·SK하이닉스·삼성전자 공급망 대호황 · ③미래기술: 두산에너빌리티 뉴스케일 SMR 상업 본생산 + 미 가스터빈 수출 및 AI 디지털트윈 제조·스페이스X 스타십 V4(70m·9엔진)·테슬라 사이버캡 개인 판매 · ④전쟁/지정학: 우크라 에이태큼스 브랸스크 타격 및 러시아 신(新) 핵교리 서명 속 NATO 재무장·한화에어로 유럽 현지 JV 수혜 · ⑤증시/세테크: 엔비디아 시간외 축포에 따른 코스피 5,000선 탈환 기대 및 연말 해외주식 양도세 22% 손익통산 · ⑥금: 세계금협회(WGC) 중국·폴란드·우즈베키스탄 중앙은행 매집 속 $3,850~$3,865/oz 지지선 방어 · ⑦비트코인: 스트래티지 850,849 BTC 보유 및 블랙록 IBIT 옵션 헤징 인프라 · ⑧부동산: 스트레스 DSR 한도 축소 속 용산서울코어 8,000호 절충안·1기 신도시 분당·평촌 및 GTX-A 역세권 양극화",'
            gtext = gtext.replace(line, new_line)
            break

    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gtext)

    idx_path = os.path.join(BASE_DIR, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        itext = f.read()
    itext = itext.replace(
        "2026년 11월 17일 · 20:00 PM 이브닝 에디션",
        "2026년 11월 18일 · 08:00 AM 모닝 에디션"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(itext)


if __name__ == "__main__":
    update_part1()
    update_part2()
    update_part3()
    update_generator_and_index()
    print("Successfully updated all 40 agendas for 2026-11-18_0800!")
