# -*- coding: utf-8 -*-
"""
2026-11-17 20:00 PM 이브닝 에디션 (2026-11-17_2000) 40대 심층 안건 업데이트 스크립트
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def update_part1():
    p1_path = os.path.join(SCRIPTS_DIR, "agendas_part1.py")
    with open(p1_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/17 모닝", "[11/17 이브닝")

    # Agenda 01: Tuesday KOSPI 4,968.48 (-2.59%, sub-5,000 first time in 9 months) vs USD/KRW 1,338.2 won rock-solid stability & US 10Y 5.12~5.13% ahead of tonight's US Oct Retail Sales
    text = text.replace(
        '"🔴 시사점 점검 (간밤 미 증시 3거래일 연속 숨고르기 & 미 10년물 금리 5.13~5.15% 고점 진정세! 역외 원/달러 환율 1,335.55원 철벽 방어 속 오늘 밤 \'미 10월 소매판매\' 발표)"',
        '"🔴 시사점 점검 (화요일 코스피 4,968.48(-2.59%) 9개월 만의 5,000선 하회! 그러나 원/달러 환율 1,338.2원·미 10년물 5.12% 안정으로 \'외환위기 없는 과매도\' 입증)"'
    )
    text = text.replace(
        '"[11/17 이브닝·화요일 개장 전략] 미 10년물 \'5.13~5.15%\' 진정세와 역외 환율 \'1,335.55원\' 철벽 수성: 오늘 밤 \'미 10월 소매판매\'가 여는 변곡점"',
        '"[11/17 이브닝·화요일 마감 긴급점검] 코스피 \'4,968.48(-2.59%)\' 언더슈팅에도 환율은 \'1,338.2원\' 요지부동: 오늘 밤 미 소매판매와 공포 매수 타점"'
    )

    # Agenda 07: Samsung Electronics 190,300 KRW (-3.30%) multi-hyperscaler HBM buffer (Google, AWS, AMD) + HBM4 validation
    text = text.replace(
        '"🟢 시사점 대폭발! (삼성전자 \'1c D램 기반 HBM4\' 엔비디아 퀄테스트 임박 및 \'할인 없는 가격 협상력(Price Parity) 역전\'! + 3D Cube-H·구글 TPU 확장)"',
        '"🟢 시사점 강화 (삼성전자 190,300원(-3.30%) 과매도 진입! 구글·AWS·AMD 다변화된 하이퍼스케일러 HBM 수주 버퍼 + \'1c D램 HBM4\' 퀄테스트 모멘텀)"'
    )
    text = text.replace(
        '"[11/17 이브닝] 삼성전자(206,000원) \'1c D램 HBM4\' 퀄테스트 결과 임박: HBM3E 때와 달리 \'할인 없는 제값(Price Parity)\' 받는 공급자 우위 시장!"',
        '"[11/17 이브닝·삼성전자 19만원선 점검] 삼성전자(190,300원, -3.30%) 과매도 구간 진입: 구글·AWS·AMD 멀티 고객망과 \'1c D램 HBM4\' 반격 카드"'
    )

    # Agenda 09: SK Hynix 1,098,000 KRW (-1.96%) locking in ~70% of Nvidia's initial Vera Rubin HBM4 orders + multi-year LTA prepayments
    text = text.replace(
        '"🟢 시사점 강화 (SK하이닉스 \'청주 P&T6 공장 HBM4 후공정(본딩·다이싱·검사) 장비 발주 확정\' & 수율 70% 돌파! 121.6만 원 눌림목 매수 적기)"',
        '"🟢 시사점 대폭발! (SK하이닉스 \'엔비디아 베라 루빈 초기 HBM4 물량 70% 독점 확보\' 및 장기선급금(LTA) 락인! 오늘 1,098,000원(-1.96%)은 바겐세일)"'
    )
    text = text.replace(
        '"[11/17 이브닝] SK하이닉스(1,216,000원) \'청주 P&T6 HBM4 후공정 장비 발주 확정\'과 수율 70% 돌파: 엔비디아 루빈 독점력 굳히기"',
        '"[11/17 이브닝·SK하이닉스 109.8만원] 엔비디아 베라 루빈 \'초기 HBM4 물량 70% 독식\'과 선수금(LTA) 락인: 110만 원 하회는 펀더멘털 괴리 저가매수 찬스"'
    )

    # Agenda 12: Elon Musk unveils 'Starship V4' (~70m upper stage, +40% length, 9 engines) following Ship 42 catch to power 'Starmind' orbital AI data centers
    text = text.replace(
        '"🟢 시사점 강화 (스페이스X 텍사스 배스트럽 \'기가샛 팩토리(Gigasat Factory)\' 풀가동! 태양동기궤도 우주 AI 데이터센터 \'스타마인드\'와 광학 레이저 통신망 구축)"',
        '"🟢 시사점 대폭발! (일론 머스크 차세대 \'스타십 V4(상단 70m·길이 40% 확장·9엔진)\' 전격 공개! 배스트럽 기가샛 공장과 우주 AI 데이터센터 \'스타마인드\' 수송력 극대화)"'
    )
    text = text.replace(
        '"[11/17 이브닝·스타마인드 양산 기지] 스페이스X 텍사스 \'기가샛 팩토리(Gigasat)\'와 태양동기궤도 우주 AI 데이터센터: 24시간 태양광·진공 냉각 혁명"',
        '"[11/17 이브닝·스타십 V4 전격 공개] 상단 우주선 길이 40% 키운 \'스타십 V4(70m·9엔진)\' 로드맵과 우주 AI 데이터센터 \'스타마인드\' 대량 발사 시대"'
    )

    # Agenda 13: Doosan Enerbility signs commercial contract with NuScale Power for SMR Upper Reactor Pressure Vessel Module at Changwon plant
    text = text.replace(
        '"🟢 시사점 강화 (미 원자력규제위원회(NRC), 다우·엑스에너지 텍사스 \'롱 모트(Long Mott) 첨단 SMR 건설 허가\' 승인! 뉴스케일·엑스에너지 핵심 주기기 맡은 두산에너빌리티 수혜)"',
        '"🟢 시사점 대강화! (두산에너빌리티, 미 뉴스케일파워와 \'SMR 상부 원자로 압력용기 모듈 상업 본생산 계약\' 체결! 창원 공장 풀가동 + 미 NRC 엑스에너지 허가 겹호재)"'
    )
    text = text.replace(
        '"[11/17 이브닝·SMR 건설 허가 돌파] 미 NRC, 다우·엑스에너지 텍사스 \'롱 모트 SMR 건설 허가\' 전격 승인! 뉴스케일·엑스에너지 주기기 독점 두산에너빌리티 재평가"',
        '"[11/17 이브닝·두산에너빌리티 본생산 계약] 두산에너빌리티-뉴스케일 \'SMR 상부 원자로 모듈 상업 본생산 계약\' 체결! 창원 SMR 파운드리 가동 돌입"'
    )

    # Agenda 15: Eli Lilly launches Nvidia-powered 'LillyPod' AI supercomputer & Creyon Bio quantum-chemistry RNA partnership
    text = text.replace(
        '"🟢 시사점 대강화! (일라이 릴리 ObesityWeek 학회서 차세대 복합제 \'EloraTZP 임상 2상 48주 -23%+ 감량\' 발표 & 중국 경구용 \'파운다요\' 승인 쌍끌이!)"',
        '"🟢 시사점 강화 (일라이 릴리 엔비디아 기반 AI 슈퍼컴 \'릴리팟(LillyPod)\' 가동 & 크레용바이오 \'양자화학 기반 RNA 신약\' 동맹! + EloraTZP -23% 감량)"'
    )
    text = text.replace(
        '"[11/17 이브닝·비만약 초격차] 일라이 릴리 차세대 \'EloraTZP(48주 -23% 감량)\' 임상 2상 대성공 & 경구용 \'파운다요\' 중국 승인: 비만·당뇨·수면무호흡 평정"',
        '"[11/17 이브닝·AI·양자 신약 제국] 일라이 릴리의 초격차 비결: 엔비디아 AI 슈퍼컴 \'릴리팟(LillyPod)\'과 양자화학 RNA 신약 + EloraTZP -23% 감량"'
    )

    with open(p1_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part2():
    p2_path = os.path.join(SCRIPTS_DIR, "agendas_part2.py")
    with open(p2_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/17 모닝", "[11/17 이브닝")

    # Agenda 17: Russia formally lowers nuclear doctrine threshold in response to ATACMS strikes -> NATO accelerates localized defense JVs with Hanwha Aerospace
    text = text.replace(
        '"🟢 시사점 강화 (우크라 에이태큼스(ATACMS)·스톰섀도 러 본토 무기고 타격 & NATO 국방비 \'GDP 대비 3~5% 상향\' 논의 급물살! 한화에어로 등 K-방산 수주 잔고 재평가)"',
        '"🟢 시사점 강화 (러시아 \'신(新) 핵 교리(핵사용 문턱 하향)\' 공식 승인 맞불! 유럽 안보 위기감 고조 속 한화에어로스페이스 \'유럽 현지 합작법인(JV)·기술협력\' 가속)"'
    )
    text = text.replace(
        '"[11/17 이브닝·NATO 국방비 3~5% 시대] 에이태큼스(ATACMS) 러 무기고 정밀타격과 서방 탄약고 고갈: NATO 국방비 GDP 3~5% 증액이 부른 K-방산 독주"',
        '"[11/17 이브닝·러 핵교리 개정 파장] 에이태큼스 본토 타격에 맞선 러시아 \'핵사용 문턱 하향\' 공식화: 유럽 현지 생산(JV) 장악한 K-방산 수혜"'
    )

    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part3():
    p3_path = os.path.join(SCRIPTS_DIR, "agendas_part3.py")
    with open(p3_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/17 모닝", "[11/17 이브닝")

    # Agenda 33: MicroStrategy expands BTC holdings to 850,849 BTC ($64.20B cost, avg $75,452) via ATM/STRC while navigating MSCI index rebalancing & Gold $3,850~$3,875 floor
    text = text.replace(
        '"🟢 시사점 강화 (스트래티지(MSTR) \'총 850,364 BTC(전체 발행량의 4% 돌파 · 평단가 $75,456) 보유\' 기관 매집 하방 경직성 & 금($3,887~$3,896/oz) 동시 지지!)"',
        '"🟢 시사점 강화 (스트래티지(MSTR) 추가 매수로 \'총 850,849 BTC(매입원가 $64.2B · 평단 $75,452)\' 돌파! MSCI 지수 리밸런싱 노이즈 이겨내는 기관 실물 락업)"'
    )
    text = text.replace(
        '"[11/17 이브닝·기관 매집과 진바닥] 스트래티지(MSTR) \'850,364 BTC(평단 $75,456) 총량의 4% 독식\'과 금($3,887/oz): 양대 대체자산의 강력한 하방 지지선"',
        '"[11/17 이브닝·MSTR 85만849 BTC 돌파] 조정장에도 멈추지 않는 스트래티지 \'850,849 BTC(평단 $75,452)\' 매집과 금($3,850~$3,875/oz) 중앙은행 바닥권 지지"'
    )

    # Agenda 39: Yongsan Seoul Core (용산서울코어 · 용산국제업무지구) 8,000-unit compromise & Asia-Pacific business/MICE hub acceleration
    text = text.replace(
        '"🟢 시사점 구체화! (용산국제업무지구 주택 공급 갈등 해법: 서울시 원안(6,000호)과 정부 목표(10,000호) 사이 \'\'8,000호 절충안\' + 100층 랜드마크\' 부상!)"',
        '"🟢 시사점 강화 (단군 이래 최대 개발 \'용산서울코어(용산국제업무지구)\' 8,000호 절충안 & 100층 글로벌 오피스·MICE 허브 구체화! 강북·한강벨트 대장주 견인)"'
    )
    text = text.replace(
        '"[11/17 이브닝·용산 마스터플랜 급진전] 용산국제업무지구 주택 공급 \'8,000호 절충안\' 부상: 6천 호(서울시)와 1만 호(국토부) 이견 좁히고 100층 랜드마크 속도!"',
        '"[11/17 이브닝·용산서울코어 가속화] 아태 비즈니스·MICE 허브 \'용산서울코어(용산국제업무지구)\' 8,000호 절충안과 한강벨트 핵심지 가치 재평가"'
    )

    with open(p3_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_generator_and_index():
    gen_path = os.path.join(SCRIPTS_DIR, "generate_briefing.py")
    with open(gen_path, "r", encoding="utf-8") as f:
        gtext = f.read()

    old_hl_prefix = '"executiveHeadline": "[11/17 모닝 · 40대 심층안건]'
    for line in gtext.splitlines():
        if old_hl_prefix in line:
            new_line = '        "executiveHeadline": "[11/17 이브닝 · 40대 심층안건] ①거시: 화요일 코스피 4,968.48(-2.59%) 9개월 만의 5,000선 하회 언더슈팅에도 원/달러 환율 1,338.2원·미 10년물 5.12% 안정으로 외환 건전성 입증(오늘 밤 미 10월 소매판매 대기) · ②반도체: SK하이닉스(1,098,000원, -1.96%) \'엔비디아 베라 루빈 초기 HBM4 물량 70% 독점 및 장기선급금(LTA) 확보\'·삼성전자(190,300원, -3.30%) 구글/AWS/AMD 멀티 고객망 버퍼 및 1c HBM4 퀄테스트 임박 · ③미래기술: 일론 머스크 \'스타십 V4(상단 70m·길이 40% 확장·9엔진)\' 공개 및 스타마인드 우주 AI 데이터센터·두산에너빌리티-뉴스케일 \'SMR 상부 원자로 모듈 상업 본생산 계약\' 체결·일라이 릴리 AI 슈퍼컴 \'릴리팟\' 및 양자화학 신약 · ④전쟁/지정학: 러시아 \'핵사용 문턱 하향\' 신(新) 핵교리 공식 승인 속 NATO 재무장 및 한화에어로 유럽 현지 합작법인(JV) 가속 · ⑤증시/세테크: 코스피 5,000선 하회 공포장을 활용한 버핏식 분할매수 및 연말 해외주식 양도세 22% 손익통산 · ⑥금: 강달러 속 $3,850~$3,875/oz 중앙은행 실물 매집 지지 및 골드만삭스 연말 $4,150·2027년 $4,800 전망 · ⑦비트코인: 스트래티지(MSTR) 추가 매집으로 \'총 850,849 BTC(평단 $75,452)\' 돌파 및 IBIT 옵션 헤징 거래 급증 · ⑧부동산: 스트레스 DSR 한도 축소 속 \'용산서울코어(용산국제업무지구)\' 8,000호 절충안 및 1기 신도시 분당·평촌 옥석 가리기",'
            gtext = gtext.replace(line, new_line)
            break

    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gtext)

    idx_path = os.path.join(BASE_DIR, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        itext = f.read()
    itext = itext.replace(
        "2026년 11월 17일 · 08:00 AM 모닝 에디션",
        "2026년 11월 17일 · 20:00 PM 이브닝 에디션"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(itext)


if __name__ == "__main__":
    update_part1()
    update_part2()
    update_part3()
    update_generator_and_index()
    print("Successfully updated all 40 agendas for 2026-11-17_2000!")
