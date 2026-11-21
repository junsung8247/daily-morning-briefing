# -*- coding: utf-8 -*-
"""
2026-11-21 20:00 PM 이브닝 에디션 (2026-11-21_2000) 56대 확장 심층 안건 업데이트 스크립트
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def update_all_parts():
    for fname in ["agendas_part1.py", "agendas_part2.py", "agendas_part3.py", "agendas_extra.py"]:
        fpath = os.path.join(SCRIPTS_DIR, fname)
        with open(fpath, "r", encoding="utf-8") as f:
            text = f.read()

        text = text.replace("[11/21 모닝", "[11/21 이브닝")

        if fname == "agendas_part1.py":
            # Agenda 04: Bank of Korea Nov 26 final 2026 meeting -> 3.00% vs 3.25% hike consensus (DBS etc.)
            text = text.replace(
                '"🟢 시사점 강화 (미 10년물 5.10% 도달에도 원/달러 환율 1,334.53원(-0.55%) 철벽 방어! 한국 외환보유고 미 국채 운용 수익 극대화)"',
                '"🔴 시사점 긴급 전환! (11/26(목) 올해 마지막 한은 금통위: 현행 3.00% ➔ 3.25% 추가 인상(25bp) 유력 부상! 물가 2%대 후반·수출 주도 성장률 3%대 후반)"'
            )
            text = text.replace(
                '"[11/21 이브닝] 미 금리가 5.10%로 뛰었는데 한국 환율은 1,334원(-0.55%)으로 안정된 기적: 한은(2.50%)과 외환보유고($443B+)의 미소"',
                '"[11/21 이브닝·11/26 한은 금통위 프리뷰] 한은 기준금리 \'연 3.00% ➔ 3.25% 추가 인상\' 기로! 2% 후반 물가·반도체 고성장 vs 증시 변동성 충돌"'
            )

            # Agenda 07: Samsung Electronics & SK Hynix near 100% fab utilization despite Nov 19 new US 16nm China export rules
            text = text.replace(
                '"🔴 주가 급락 vs 펀더멘털 괴리 (삼성전자 -7.31% 급락 \'182,500원\' 마감! 그러나 1c D램·4nm 베이스다이 HBM4 및 루빈 울트라용 8단 HBM4 수주 파이프라인 건재)"',
                '"🔴 주가 vs 공장 가동률 괴리! (11/19 미 16nm 이하 대중 규제 발효에 삼성 180,900원(-8.13%) 급락… 그러나 실제 삼성·SK 메모리 팹 가동률은 \'100% 육박 풀가동\'!)"'
            )

        if fname == "agendas_part3.py":
            # Agenda 31: Weekend Bitcoin slide to $57,500~$58,800 (Upbit ~8,300~8,390만원, -50%+ from ATH)
            text = text.replace(
                '"🔴 시사점 긴급 점검 (글로벌 증시 폭락·현물 ETF 10억 달러+ 순유출 여파에 비트코인 \'8,250만원~8,350만원($61,500~$63,000)\' 급락! 현금 비중 유지 및 하방 테스트)"',
                '"🔴 주말 변동성 확대 (주말 글로벌 BTC \'$57,500~$58,800\'(-5~6% 추가 조정 · 고점 대비 -50%+) & 업비트 8,300만 원대! 8,000만 원 핵심 지지선 테스트)"'
            )
            text = text.replace(
                '"[11/21 이브닝·BTC 8,250만원대 급락 점검] 글로벌 투매·ETF 환매 속 8,250만원~8,350만원($61.5K~$63K) 밀린 비트코인: 레버리지 금지·분할 저가매수 구간"',
                '"[11/21 이브닝·주말 BTC $57.5K 테스트] 고점 대비 -50% 넘게 빠진 글로벌 BTC($57.5K~$58.8K · 업비트 8,300만원대): 레버리지 청산 끝자락과 8천만원 지지선"'
            )

            # Agenda 37: Seoul Gangnam 3-gu & Yongsan/Dongjak turning slightly negative while Gyeonggi (Suwon/Anyang/Yongin) & Pyeongchon A-17 contractor selection stay firm
            text = text.replace(
                '"🟢 시사점 강화 (스트레스 DSR 3단계 한도 축소에 실수요 \'전용 59㎡ 소형 평형·15억 이하 역세권\' 집중 vs 자산가 \'용산·강남 똘똘한 한 채\' 양극화 심화!)"',
                '"🔴 서울·경기 국지적 반전 포착 (한국부동산원 주간: 스트레스 DSR 3단계 직격탄에 강남3구 일부·용산·동작 하락 전환 vs 경기 수원·안양·용인 대단지·평촌 A-17 시공사 선정 강세!)"'
            )
            text = text.replace(
                '"[11/21 이브닝·서울 평형별 양극화] 스트레스 DSR 3단계가 바꾼 풍경: 대출 맞춘 \'전용 59㎡ 소형·역세권\' 실수요 이동과 \'똘똘한 한 채\' 전략"',
                '"[11/21 이브닝·서울 숨고르기 vs 경기 강세] 용산·동작·강남 일부 하락 전환 vs 수원·안양·용인 대단지 및 평촌 A-17 시공사 선정: 한은 3.25% 인상 변수 점검"'
            )

        with open(fpath, "w", encoding="utf-8") as f:
            f.write(text)


def update_generator_and_index():
    gen_path = os.path.join(SCRIPTS_DIR, "generate_briefing.py")
    with open(gen_path, "r", encoding="utf-8") as f:
        gtext = f.read()

    old_hl_prefix = '"executiveHeadline": "[11/21 모닝 · 52대 확장 심층안건'
    for line in gtext.splitlines():
        if old_hl_prefix in line:
            new_line = '        "executiveHeadline": "[11/21 이브닝 · 56대 주말 확장 심층안건] ①거시: 차주 추수감사절 초압축 주간 개막 — 11/25(수) \'슈퍼 수요일\' 미 10월 PCE(+0.3% 예상)·Q3 GDP·베이지북 동시 발표 & 11/26(목) 한국은행 기준금리 연 3.00%➔3.25% 추가 인상 기로 · ②반도체: 앤트로픽(ANT, $88.91·총 $93.5B IPO + $26B 테크동맹 사모투자) 상장 2일차 급락과 11/19 미 16nm 이하 대중 수출규제 발효로 삼성(180,900원)·SK(1,100,000원)·NVDA($125.53) 투매 속 삼성·SK 메모리 팹 가동률 100% 육박 풀가동(실시간 시세보드 7종목 최근 4Q·1Q×4 PER 자동 반영) · ③미래기술: 테슬라 베를린 €30억 투자 \'연산 100만 대 사이버캡 전용 공장\' 발표 & 기가 텍사스 \'옵티머스 전용 기가프레스\' 기초 공사 포착 · 일라이 릴리 캐나다 경구용 비만약 \'파운다요\' 승인 및 $74억(Stipple $5.9B·Calytrix $1.5B) 연속 빅딜 · ④전쟁/지정학: [긴급] 러시아 미사일 80발·드론 400기 대공습 도중 러 순항미사일 2발·제트드론 1기 NATO 회원국 폴란드 영토 추락(뤼터 사무총장·투스크 총리 강력 규탄) ➔ 월요일 K-방산 핵심 촉매 · 구리 -20% 약세장 vs 중국 실물 프리미엄 사상 최고 · ⑤증시/세테크: 코스피·코스닥 동시 매도 사이드카 이후 월요일 반대매매 소화 전략 · 고배당 배당소득 분리과세 특례 & 생산적금융 ISA · 만기전환 +300만 원 세액공제 · ⑥금: 12월 연준 인상 90% 선반영에 $3,550/oz 눌림목 & 골드만삭스 연말 $4,900/oz 장기 강세 뷰 · ⑦비트코인: 주말 글로벌 BTC $57,500~$58,800(고점 대비 -50%+ · 업비트 8,300만원대) 추가 조정 속 8,000만원 핵심 지지선 테스트 · ⑧부동산: 스트레스 DSR 3단계 속 서울 용산·동작·강남 일부 하락 전환 vs 경기 수원·안양·용인 및 평촌 A-17 시공사 선정 강세 · 11/26 한은 3.25% 인상 변수 점검",'
            gtext = gtext.replace(line, new_line)
            break

    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gtext)

    idx_path = os.path.join(BASE_DIR, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        itext = f.read()
    itext = itext.replace(
        "2026년 11월 21일 · 08:00 AM 모닝 에디션",
        "2026년 11월 21일 · 20:00 PM 이브닝 에디션"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(itext)


if __name__ == "__main__":
    update_all_parts()
    update_generator_and_index()
    print("Successfully updated all 56 agendas for 2026-11-21_2000!")
