# -*- coding: utf-8 -*-
"""
2026-11-22 08:00 AM 일요일 모닝 에디션 (2026-11-22_0800) 56대 확장 심층 안건 업데이트 스크립트
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def update_all_parts():
    for fname in ["agendas_part1.py", "agendas_part2.py", "agendas_part3.py", "agendas_extra.py"]:
        fpath = os.path.join(SCRIPTS_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()

        text = text.replace("[11/21 이브닝", "[11/22 모닝")

        if fname == "agendas_part1.py":
            # Agenda 04: BOK Nov 26 unanimous 3.25% hike + 3.50% early-2027 terminal rate dot plot
            text = text.replace(
                '"🔴 시사점 긴급 전환! (11/26(목) 올해 마지막 한은 금통위: 현행 3.00% ➔ 3.25% 추가 인상(25bp) 유력 부상! 물가 2%대 후반·수출 주도 성장률 3%대 후반)"',
                '"🔴 채권시장 만장일치 경고 (11/26 한은 금통위 \'3.00% ➔ 3.25% 인상\' 압도적 컨센서스 + 2027 초 \'최종금리 3.50%\' 점도표 시사 전망! 주담대·부동산 압박)"'
            )
            text = text.replace(
                '"[11/22 모닝·11/26 한은 금통위 프리뷰] 한은 기준금리 \'연 3.00% ➔ 3.25% 추가 인상\' 기로! 2% 후반 물가·반도체 고성장 vs 증시 변동성 충돌"',
                '"[11/22 모닝·한은 최종금리 3.50% 예고] 11/26 한은 3.25% 인상 만장일치 전망 & \'2027 초 3.50% 최종금리\' 점도표 경계: 채권·은행·주담대 대응"'
            )

        if fname == "agendas_part3.py":
            # Agenda 31: Overnight BTC flash crash to $55,130 (₩7,850만원, $2.4B~$2.7B liquidations!) -> Sunday morning V-rebound above $60,200 (₩8,400만원대!)
            text = text.replace(
                '"🔴 주말 변동성 확대 (주말 글로벌 BTC \'$57,500~$58,800\'(-5~6% 추가 조정 · 고점 대비 -50%+) & 업비트 8,300만 원대! 8,000만 원 핵심 지지선 테스트)"',
                '"🟢 레버리지 대청소 후 V자 반등! (간밤 BTC \'$55,130 · 업비트 7,850만원\' 순간 붕괴 및 $27억 강제청산 직후, 일요일 아침 \'$60,200+ · 8,400만원대\' 즉각 탈환!)"'
            )
            text = text.replace(
                '"[11/22 모닝·주말 BTC $57.5K 테스트] 고점 대비 -50% 넘게 빠진 글로벌 BTC($57.5K~$58.8K · 업비트 8,300만원대): 레버리지 청산 끝자락과 8천만원 지지선"',
                '"[11/22 모닝·BTC $27억 청산 후 $60K 탈환] 업비트 \'7,850만원($55.1K)\' 순간 이탈하며 롱 레버리지 전멸 ➔ 일요일 아침 \'$60,200+(8,400만원대)\' 급반등!"'
            )

        if fname == "agendas_extra.py":
            # Agenda 53: Poland identifies Russian Kh-101 cruise missile during KOALICJA 26.2 but declines NATO Article 4 invocation (de-escalating WW3 fear while boosting defense budgets)
            text = text.replace(
                '"🆕 토요일 긴급 속보! (러시아 미사일 80발·드론 400기 대공습 중 \'러 순항미사일 2발·제트드론 1기 폴란드 영토(NATO) 추락\'! 뤼터 사무총장·투스크 총리 강력 규탄)"',
                '"🟢 확전 공포 진정 + 방산 수혜 유지 (폴란드 추락 미사일 \'러 Kh-101\' 확인! 단 폴란드가 \'NATO 제4조 발동 보류\' 결정하며 전면전 공포 완화 · 동부 방공망 강화 가속)"'
            )
            text = text.replace(
                '"[11/22 모닝·확장특집 53] 러시아 순항미사일 2발·드론 폴란드 영토 추락 쇼크: NATO 영공 침범이 촉발할 유럽 방공망 긴급 발주와 K-방산"',
                '"[11/22 모닝·확장특집 53] 폴란드 \'러 Kh-101 순항미사일 추락\' 확인 불구 NATO 제4조 발동 보류: 전면전 공포 진정 속 동부 방공망·K-방산 수혜"'
            )

            # Agenda 54: Super Wednesday Oct PCE (Core +3.2~3.3% YoY, final read before Dec 9 FOMC) + Black Friday NRF $1.013T (+4.2%) test + BOK 3.25%
            text = text.replace(
                '"🆕 차주(11/23~27) 초압축 빅이벤트 프리뷰 (\'슈퍼 수요일(11/25)\' 미 10월 PCE 물가·3분기 GDP·베이지북 동시 폭격 ➔ \'목요일(11/26)\' 한은 금통위 3.00%➔3.25% 인상 기로!)"',
                '"🆕 차주(11/23~27) 최종 관전 포인트 (12/9 FOMC 전 마지막 물가 \'11/25 미 근원 PCE(+3.2~3.3% 예상)\' · 11/26 한은 3.25% 인상 · 블프 소비 \'$1.013조(+4.2%)\' 테스트!)"'
            )

            # Agenda 55: Tesla Musk hints Cybercab Autonomy Subscription ($299 -> ~$115/mo over time) & Dec customer FSD fleet pilot + Berlin €3B plant
            text = text.replace(
                '"🟢 시사점 대강화! (테슬라 \'베를린 기가팩토리에 €30억(약 4.5조 원) 투자 ➔ 연산 100만 대 사이버캡 전용 공장 건설\' 발표 + 기가 텍사스 \'옵티머스 전용 기가프레스\' 기초 공사 포착!)"',
                '"🟢 시사점 대강화! (머스크 \'사이버캡 월 $299 구독료 향후 $115 수준 인하 + 12월 고객 FSD 차량 로보택시 시범 합류\' 시사 & 베를린 €30억 연산 100만 대 공장!)"'
            )

            # Agenda 56: Eli Lilly Zepbound blockbuster adolescent (12-17) weight-loss trial + Health Canada Foundayo approval + $7.4B M&A
            text = text.replace(
                '"🟢 경기방어·바이오 황제주 등극! (일라이 릴리 \'캐나다 보건부 경구용 비만약 파운다요(Foundayo) 공식 승인\' + \'$59억 Stipple Bio 항암·$15억 Calytrix Bio 인수\' 연속 폭격!)"',
                '"🟢 경기방어·바이오 황제주 독주! (일라이 릴리 \'젭바운드 청소년(12~17세) 비만 임상 대성공\'으로 시장 확장 + 캐나다 먹는 비만약 파운다요 승인 & $74억 빅딜!)"'
            )

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(text)


def update_generator_and_index():
    gen_path = os.path.join(SCRIPTS_DIR, "generate_briefing.py")
    with open(gen_path, "r", encoding="utf-8") as f:
        gtext = f.read()

    old_hl_prefix = '"executiveHeadline": "[11/21 이브닝 · 56대 주말 확장 심층안건]'
    for line in gtext.splitlines():
        if old_hl_prefix in line:
            new_line = '        "executiveHeadline": "[11/22 모닝 · 56대 일요일 주간전략 확장안건] ①거시: 12/9 FOMC 전 마지막 물가지표 \'11/25(수) 미 10월 근원 PCE(+3.2~3.3% YoY 예상)\' & 블프 소비($1.013조 +4.2% 전망) + 11/26(목) 한은 금통위 \'3.00%➔3.25% 인상 만장일치 전망 및 2027 초 3.50% 최종금리\' 점도표 경계 · ②반도체: 앤트로픽(ANT) IPO 여파(OpenAI 상장 밸류 압박)·미 16nm 이하 대중 규제·DRAM 소송 노이즈 속 삼성·SK 100% 육박 풀가동(우측 실시간 시세보드 7종목 최근 4분기/1분기×4 PER 매일 자동 갱신) · ③미래기술: 머스크 \'사이버캡 월 $299 구독료 향후 $115 인하·12월 개인 FSD 차량 로보택시 합류\' 시사 & 베를린 €30억 공장 · 일라이 릴리 젭바운드 청소년(12~17세) 임상 대성공·캐나다 파운다요 승인 · 스페이스X 쉽42 은퇴 전시 · ④전쟁/지정학: 폴란드 추락 미사일 \'러 Kh-101\' 확인 불구 바르샤바 \'NATO 제4조 발동 보류\' ➔ 전면전 공포 진정 + 유럽 방공망·K-방산 수혜 유지 · ⑤증시/세테크: 지난주 나스닥 -10%·S&P -8.6% 급락 후 월요일 반대매매 소화 및 고배당 분리과세·생산적금융 ISA·연말정산 전략 · ⑥금: 과매도 RSI 극단 구간($3,550/oz) 속 11~1월 계절적 강세·기술적 반등 및 골드만 연말 $4,900 뷰 · ⑦비트코인: 간밤 $55,130(업비트 7,850만원) 순간 급락 및 $27억 강제청산 직후 일요일 아침 $60,200+(8,400만원대) V자 급반등! · ⑧부동산: 11/26 한은 3.25% 인상 임박·스트레스 DSR 3단계 속 토허제 강남·용산 숨고르기 vs 경기·비규제 1기 신도시 차별화",'
            gtext = gtext.replace(line, new_line)
            break

    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gtext)

    idx_path = os.path.join(BASE_DIR, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        itext = f.read()
    itext = itext.replace(
        "2026년 11월 21일 · 20:00 PM 이브닝 에디션",
        "2026년 11월 22일 · 08:00 AM 모닝 에디션"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(itext)


if __name__ == "__main__":
    update_all_parts()
    update_generator_and_index()
    print("Successfully updated all 56 agendas for 2026-11-22_0800!")
