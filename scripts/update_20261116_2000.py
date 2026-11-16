# -*- coding: utf-8 -*-
"""
2026-11-16 20:00 PM 이브닝 에디션 (2026-11-16_2000) 40대 심층 안건 업데이트 스크립트
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def update_part1():
    p1_path = os.path.join(SCRIPTS_DIR, "agendas_part1.py")
    with open(p1_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/16 모닝", "[11/16 이브닝")

    # Agenda 01: Monday KOSPI 5,100.50 (-3.59%) close amidst US 10Y 5.1%+ & USD/KRW 1,335.7 won stability ahead of tonight's Kevin Warsh speech
    text = text.replace(
        '"🔴 시사점 점검 (월요일 아시아 장 개막 & 오늘 밤 케빈 워시 연준 의장 AI·생산성 연설! 화요일 미 10월 소매판매·수요일 FOMC 의사록 앞두고 미 10년물 5.15% 공방)"',
        '"🔴 시사점 점검 (미 10년물 5.1%대 경계감에 코스피 5,100.50(-3.59%) 숨고르기 마감! 반면 원/달러 환율은 1,335.7원으로 철벽 안정… 오늘 밤 워시 연준 의장 연설 주목)"'
    )
    text = text.replace(
        '"[11/16 이브닝·월요일 개장 전략] 오늘 밤 케빈 워시 연준 의장 연설을 시작으로 열리는 빅이벤트 주간: 미 10년물 \'5.15%\' 고금리 돌파구 찾기"',
        '"[11/16 이브닝·월요일 마감 총평] 코스피 5,100.50(-3.59%) 조정 속 빛난 \'환율 1,335.7원\'의 방어력: 오늘 밤 워시 의장 연설과 투매 역발상 전략"'
    )

    # Agenda 06: Nvidia notifies cloud customers of 15%+ system price hikes on Grace Blackwell & Vera Rubin due to HBM4 & TSMC CoWoS costs
    text = text.replace(
        '"🟢 시사점 강화 (엔비디아 실적 발표 주간 개막! \'TSMC 3nm 커스텀 NVHBM 베이스다이\' 도입과 베라 루빈(Rubin) HBM4 물량 가이던스에 전 세계 이목 집중)"',
        '"🟢 시사점 대폭발! (엔비디아, 빅테크 고객사에 \'블랙웰·베라 루빈 AI 서버 시스템 가격 15% 이상 인상\' 통보! HBM4·CoWoS 원가 상승분 100% 가격 전가력 입증)"'
    )
    text = text.replace(
        '"[11/16 이브닝·엔비디아 실적 주간 개막] 엔비디아 실적콜 핵심 화두 \'베라 루빈(Rubin) & TSMC 3nm 커스텀 NVHBM\': K-메모리 공급망 대응 전략"',
        '"[11/16 이브닝·엔비디아 가격인상] 엔비디아 \'블랙웰·베라 루빈 서버 가격 15%+ 전격 인상\' 통보! 삼성(-4.47%)·SK(-7.89%) 과매도를 줍는 확실한 근거"'
    )

    # Agenda 11: Vera Rubin VR200 NVL72 (190~230kW) & Rubin Ultra (600kW) making direct-to-chip liquid cooling mandatory baseline
    text = text.replace(
        '"🟡 시사점 유지 (2029년까지 완판된 HBM4를 가동할 물리적 전제조건: \'랙당 200~230kW 루빈 전력망 · 800V DC 배전 · 직결 액체냉각\')"',
        '"🟢 시사점 강화 (블랙웰 NVL72(120~140kW) 발열 설계 개량 완료 & 베라 루빈(190~230kW)·루빈 울트라(600kW) 시대 \'직결 수랭식(Liquid Cooling)\' 100% 의무화!)"'
    )
    text = text.replace(
        '"[11/16 이브닝] 2029년까지 완판된 HBM4와 루빈(230kW 랙)을 돌릴 전기와 냉각수: 금리 5.10%와 무관한 \'초고압 변압기 · 액체냉각\' 독주"',
        '"[11/16 이브닝·AI 열관리 혁명] 공랭식의 종말과 \'직결 액체냉각(Liquid Cooling)\' 의무화: 블랙웰(140kW) 넘어 루빈(230kW)·울트라(600kW)가 부른 수랭식 슈퍼사이클"'
    )

    # Agenda 12: SpaceX & xAI 'Starmind' orbital AI data centers powered by Starship heavy lift
    text = text.replace(
        '"🟢 시사점 역사적 정점! (인류 우주사 새 페이지! 스타십 Flight 15 상단 우주선 \'쉽 42\' 22.5시간 궤도 비행 및 대기권 재진입 후 \'메카질라 로봇팔 포획(Tower Catch)\' 사상 최초 성공!!)"',
        '"🟢 시사점 대확장! (스타십 \'쉽 42\' 포획 성공에 이은 스페이스X·xAI 결합 프로젝트 \'스타마인드(Starmind · 궤도형 우주 AI 데이터센터)\' 가동! 지상 전력망 한계 돌파)"'
    )
    text = text.replace(
        '"[11/16 이브닝·인류 최초 쾌거] 스페이스X 스타십 상단 우주선 \'쉽 42\', 22.5시간 궤도 비행 후 발사대 \'메카질라 로봇팔 포획(Ship Catch)\' 사상 최초 성공!"',
        '"[11/16 이브닝·우주 AI 데이터센터] 스타십 완전 재사용 완성이 여는 \'스타마인드(Starmind · 궤도형 AI 데이터센터)\': 우주 극저온 냉각과 태양광의 결합"'
    )

    # Agenda 14: Tesla Cybercab Private Sales Open ($29,990 base + $299/mo mandatory Autonomy Subscription)
    text = text.replace(
        '"🟢 시사점 대강화! (테슬라 \'텍사스·플로리다 24시간 연중무휴(24/7) 무인 로보택시 가동\' & 수천 대 휴머노이드 자가학습 \'옵티머스 아카데미\' 구축!)"',
        '"🟢 시사점 대폭발! (테슬라 운전대·페달 없는 \'사이버캡(Cybercab) 개인 판매($29,990 + 월 $299 자율주행 의무구독)\' 전격 개시! 하드웨어+SaaS 고마진 모델 완성)"'
    )
    text = text.replace(
        '"[11/16 이브닝·테슬라 피지컬 AI] 텍사스·플로리다 \'24/7 무인 로보택시\' 상시 가동 & 수천 대 로봇 자가학습 \'옵티머스 아카데미(Optimus Academy)\' 공개!"',
        '"[11/16 이브닝·사이버캡 개인 판매 개시] 운전대 없는 테슬라 \'사이버캡 $29,990 + 월 $299 의무 구독\' 전격 오픈: 2027 Q2 개인 로보택시 네트워크 연결!"'
    )

    # Agenda 15: Eli Lilly ObesityWeek EloraTZP Phase 2 (>23% weight loss at 48w) + Foundayo sleep apnea data
    text = text.replace(
        '"🟢 시사점 강화 (일라이 릴리 경구용 비만약 \'파운다요(Foundayo · 오포글리프론)\' 중국 국가약품감독관리국(NMPA) 최초 승인 완료!)"',
        '"🟢 시사점 대강화! (일라이 릴리 ObesityWeek 학회서 차세대 복합제 \'EloraTZP 임상 2상 48주 -23%+ 감량\' 발표 & 중국 경구용 \'파운다요\' 승인 쌍끌이!)"'
    )
    text = text.replace(
        '"[11/16 이브닝·바이오 제국 완성] 중국 NMPA가 최초로 허가한 먹는 GLP-1 비만약: 일라이 릴리 \'파운다요(Foundayo · 오포글리프론)\'의 독식"',
        '"[11/16 이브닝·비만약 초격차] 일라이 릴리 차세대 \'EloraTZP(48주 -23% 감량)\' 임상 2상 대성공 & 경구용 \'파운다요\' 중국 승인: 비만·당뇨·수면무호흡 평정"'
    )

    with open(p1_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part2():
    p2_path = os.path.join(SCRIPTS_DIR, "agendas_part2.py")
    with open(p2_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/16 모닝", "[11/16 이브닝")

    # Agenda 17: ATACMS strikes on Russian ammo depots (Bryansk) & NATO 3~5% GDP defense budget discussion
    text = text.replace(
        '"🟢 시사점 강화 (미 우크라 에이태큼스(ATACMS) 장거리 타격 허용 여파 속 서방 정밀유도탄·방공망 재고 고갈 경보! NATO 동부전선 다층 방공망·탄약 비축 예산 폭증)"',
        '"🟢 시사점 강화 (우크라 에이태큼스(ATACMS)·스톰섀도 러 본토 무기고 타격 & NATO 국방비 \'GDP 대비 3~5% 상향\' 논의 급물살! 한화에어로 등 K-방산 수주 잔고 재평가)"'
    )
    text = text.replace(
        '"[11/16 이브닝·전쟁/지정학] 에이태큼스(ATACMS) 장거리 타격과 서방 정밀유도탄·패트리어트 재고 고갈: NATO 동부전선 요새화가 부른 K-방산 수주 랠리"',
        '"[11/16 이브닝·NATO 국방비 3~5% 시대] 에이태큼스(ATACMS) 러 무기고 정밀타격과 서방 탄약고 고갈: NATO 국방비 GDP 3~5% 증액이 부른 K-방산 독주"'
    )

    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part3():
    p3_path = os.path.join(SCRIPTS_DIR, "agendas_part3.py")
    with open(p3_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/16 모닝", "[11/16 이브닝")

    # Agenda 29: Gold technical rebound past $4,100/oz & Goldman Sachs updated targets ($4,150 year-end, $4,800 in 2027) backed by 60t/mo central bank buying
    text = text.replace(
        '"🟢 시사점 대강화! (금 선물 $3,881.70 조정 덕분에 골드만삭스 12M 목표($4,750)까지 \'+22.4%(+$868/oz)\' · JP모건($6,300)까지 \'+62.3%\' 업사이드 폭발!)"',
        '"🟢 시사점 강화 (국제 금 시세 기술적 반등 가속 & 골드만삭스 \'연말 $4,150 · 2027년 $4,800/oz\' 목표가 제시! 신흥국 중앙은행 월 60톤 매집이 만든 중장기 +16%+ 업사이드)"'
    )
    text = text.replace(
        '"[11/16 이브닝] 금값 \'$3,881.70\' 조정이 열어젖힌 기대수익률: 골드만삭스 12개월 목표($4,750)까지 \'+22.4%\' · JP모건($6,300)까지 \'+62.3%\'!"',
        '"[11/16 이브닝·골드만삭스 금 전망] 골드만삭스 \'연말 $4,150 · 2027년 $4,800/oz\' 리포트 분석: 중앙은행 월 60톤 매집이 보장하는 금현물 분할매수"'
    )

    # Agenda 37: Stress DSR Stage 3 shifting middle-market demand toward 59m2 compact units vs ultra-prime 'One Smart Property'
    text = text.replace(
        '"🟢 시사점 강화 (스트레스 DSR 3단계 여파로 \'강남3구·성동·강동 단기 숨고르기 전환\' vs \'비강남 역세권 대단지 및 전·월세(비중 50% 돌파) 강세\' 디커플링!)"',
        '"🟢 시사점 강화 (스트레스 DSR 3단계 한도 축소에 실수요 \'전용 59㎡ 소형 평형·15억 이하 역세권\' 집중 vs 자산가 \'용산·강남 똘똘한 한 채\' 양극화 심화!)"'
    )
    text = text.replace(
        '"[11/16 이브닝·서울 지역별 양극화] 강남3구·성동·강동 \'매매 숨고르기 전환\' vs 비강남 역세권·전월세(월세 비중 50%+) 강세: 급매 협상 타이밍"',
        '"[11/16 이브닝·서울 평형별 양극화] 스트레스 DSR 3단계가 바꾼 풍경: 대출 맞춘 \'전용 59㎡ 소형·역세권\' 실수요 이동과 \'똘똘한 한 채\' 전략"'
    )

    with open(p3_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_generator_and_index():
    gen_path = os.path.join(SCRIPTS_DIR, "generate_briefing.py")
    with open(gen_path, "r", encoding="utf-8") as f:
        gtext = f.read()

    old_hl_prefix = '"executiveHeadline": "[11/16 모닝 · 40대 심층안건]'
    for line in gtext.splitlines():
        if old_hl_prefix in line:
            new_line = '        "executiveHeadline": "[11/16 이브닝 · 40대 심층안건] ①거시: 미 10년물 5.1%대 경계감에 코스피 5,100.50(-3.59%) 조정 마감에도 원/달러 환율 1,335.7원 철벽 방어 & 오늘 밤 케빈 워시 연준 의장 연설 주목 · ②반도체: 엔비디아 빅테크 고객사에 \'블랙웰·베라 루빈 AI 서버 가격 15%+ 인상\' 통보(HBM4·CoWoS 원가 상승 100% 전가력 입증, 삼성 -4.47%·SK -7.89% 과매도 저가매수 기회) & 직결 액체냉각 의무화 · ③미래기술: 스페이스X·xAI 궤도형 우주 AI 데이터센터 \'스타마인드(Starmind)\' 추진·테슬라 운전대 없는 \'사이버캡 개인 판매($29,990 + 월 $299 의무구독)\' 개시·일라이 릴리 차세대 비만약 EloraTZP 임상 2상 -23% 감량 성공 · ④전쟁/지정학: 에이태큼스 러 본토 타격 및 NATO 국방비 GDP 3~5% 상향 논의 속 한화에어로 등 K-방산 수주 호황·구리 $14,000/t 품귀 전망 · ⑤증시/세테크: 코스피 급락장 속 버핏식 바벨 전략·미 국채 5.1%+환율 1,335.7원 환노출 채권 및 연말 양도세 22% 손익통산 · ⑥금: 유가 안정 속 기술적 반등 및 골드만삭스 \'연말 $4,150 · 2027년 $4,800/oz\' 전망(중앙은행 월 60톤 매집) · ⑦비트코인: 스트래티지(MSTR) 850,364 BTC(발행량의 4%+) 기관 매집 하방 지지 및 업비트 원화 시세 실시간 연동 · ⑧부동산: 스트레스 DSR 3단계 여파 실수요 \'전용 59㎡ 소형·역세권\' 이동 vs \'용산·강남 똘똘한 한 채\' 양극화·1기 신도시 자율정비촉진법", '
            gtext = gtext.replace(line, new_line)
            break

    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gtext)

    idx_path = os.path.join(BASE_DIR, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        itext = f.read()
    itext = itext.replace(
        "2026년 11월 16일 · 08:00 AM 모닝 에디션",
        "2026년 11월 16일 · 20:00 PM 이브닝 에디션"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(itext)


if __name__ == "__main__":
    update_part1()
    update_part2()
    update_part3()
    update_generator_and_index()
    print("Successfully updated all 40 agendas for 2026-11-16_2000!")
