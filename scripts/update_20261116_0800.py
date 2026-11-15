# -*- coding: utf-8 -*-
"""
2026-11-16 08:00 AM 모닝 에디션 (2026-11-16_0800) 40대 심층 안건 업데이트 스크립트
"""
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SCRIPTS_DIR = os.path.join(BASE_DIR, "scripts")


def update_part1():
    p1_path = os.path.join(SCRIPTS_DIR, "agendas_part1.py")
    with open(p1_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/15 이브닝", "[11/16 모닝")

    # Agenda 01: Monday Morning Market Kickoff - Kevin Warsh speech tonight, Tue Oct Retail Sales, Wed FOMC Minutes & US 10Y 5.15%
    text = text.replace(
        '"🔴 시사점 점검 (이번 주 빅이벤트 주간 개막: 월요일 케빈 워시 연준 의장 연설 ➔ 화요일 미 10월 소매판매(예상 +0.3%) ➔ 수요일 FOMC 의사록! 미 10년물 5.15~5.16%)"',
        '"🔴 시사점 점검 (월요일 아시아 장 개막 & 오늘 밤 케빈 워시 연준 의장 AI·생산성 연설! 화요일 미 10월 소매판매·수요일 FOMC 의사록 앞두고 미 10년물 5.15% 공방)"'
    )
    text = text.replace(
        '"[11/16 모닝·주간 매크로 프리뷰] 미 10년물 \'5.15~5.16%\' 속 운명의 3일: 워시 의장 연설(월) · 10월 소매판매(화) · FOMC 의사록(수) 완전 해부"',
        '"[11/16 모닝·월요일 개장 전략] 오늘 밤 케빈 워시 연준 의장 연설을 시작으로 열리는 빅이벤트 주간: 미 10년물 \'5.15%\' 고금리 돌파구 찾기"'
    )

    # Agenda 06: Nvidia Earnings Week D-Day Kickoff & TSMC 3nm Custom NVHBM Base Die
    text = text.replace(
        '"🟢 시사점 강화 (엔비디아 실적 발표 주간 카운트다운! 콜레트 크레스 체제 첫 실적콜 3대 관전포인트: \'베라 루빈 일정 · HBM4 물량 · TSMC 3nm NVHBM\')"',
        '"🟢 시사점 강화 (엔비디아 실적 발표 주간 개막! \'TSMC 3nm 커스텀 NVHBM 베이스다이\' 도입과 베라 루빈(Rubin) HBM4 물량 가이던스에 전 세계 이목 집중)"'
    )
    text = text.replace(
        '"[11/16 모닝·엔비디아 실적 프리뷰] 전 세계가 주목하는 콜레트 크레스 체제 첫 실적 발표: \'베라 루빈(Rubin) 로드맵\'과 HBM4 공급망 가이던스"',
        '"[11/16 모닝·엔비디아 실적 주간 개막] 엔비디아 실적콜 핵심 화두 \'베라 루빈(Rubin) & TSMC 3nm 커스텀 NVHBM\': K-메모리 공급망 대응 전략"'
    )

    # Agenda 13: US NRC Construction Permit for Dow & X-energy Long Mott SMR in Texas + Doosan Enerbility
    text = text.replace(
        '"🟡 시사점 유지 (뉴스케일파워 \'상업용 SMR 모듈 실물 제조\' & 미 에너지부 HALEU 핵연료 지원 vs 캐나다 OPG 지연… 두산에너빌리티 독점 수혜)"',
        '"🟢 시사점 강화 (미 원자력규제위원회(NRC), 다우·엑스에너지 텍사스 \'롱 모트(Long Mott) 첨단 SMR 건설 허가\' 승인! 뉴스케일·엑스에너지 핵심 주기기 맡은 두산에너빌리티 수혜)"'
    )
    text = text.replace(
        '"[11/16 모닝·SMR 실물 제조] 미 금리 5.10%에도 흔들림 없는 \'두산에너빌리티\'의 해자: 뉴스케일 SMR 모듈 실물 제작과 서방 원전 시공 병목"',
        '"[11/16 모닝·SMR 건설 허가 돌파] 미 NRC, 다우·엑스에너지 텍사스 \'롱 모트 SMR 건설 허가\' 전격 승인! 뉴스케일·엑스에너지 주기기 독점 두산에너빌리티 재평가"'
    )

    with open(p1_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part2():
    p2_path = os.path.join(SCRIPTS_DIR, "agendas_part2.py")
    with open(p2_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/15 이브닝", "[11/16 모닝")

    # Agenda 17: US ATACMS long-range strike authorization & NATO Eastern Flank precision munitions / air-defense inventory replenishment
    text = text.replace(
        '"🟢 시사점 강화 (푸틴 DMZ 거부·우크라 대공습 여파로 폴란드·핀란드 등 NATO 동부전선 \'다층 방공망·대드론·대전차 요새화\' 예산 폭증!)"',
        '"🟢 시사점 강화 (미 우크라 에이태큼스(ATACMS) 장거리 타격 허용 여파 속 서방 정밀유도탄·방공망 재고 고갈 경보! NATO 동부전선 다층 방공망·탄약 비축 예산 폭증)"'
    )
    text = text.replace(
        '"[11/16 모닝·전쟁/지정학] 푸틴 DMZ 거부 후 가속화된 NATO 동부전선(폴란드·핀란드) \'다층 방공망·대드론 요새화\': 유럽 재무장 최대 수혜국 한국"',
        '"[11/16 모닝·전쟁/지정학] 에이태큼스(ATACMS) 장거리 타격과 서방 정밀유도탄·패트리어트 재고 고갈: NATO 동부전선 요새화가 부른 K-방산 수주 랠리"'
    )

    with open(p2_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_part3():
    p3_path = os.path.join(SCRIPTS_DIR, "agendas_part3.py")
    with open(p3_path, "r", encoding="utf-8") as f:
        text = f.read()

    text = text.replace("[11/15 이브닝", "[11/16 모닝")

    # Agenda 33: Institutional BTC Treasury (MicroStrategy 850,364 BTC, >4% of total supply, avg cost $75,456) & Gold ($3,880~$3,896/oz) floor
    text = text.replace(
        '"🟢 시사점 강화 (미 금리 5.10%에 금 선물(-2.97%)과 비트코인(-3.65%) 동반 눌림목! \'BTC-to-Gold 18.5~19.0배\' & 양대 대체자산 동시 쌍바닥)"',
        '"🟢 시사점 강화 (스트래티지(MSTR) \'총 850,364 BTC(전체 발행량의 4% 돌파 · 평단가 $75,456) 보유\' 기관 매집 하방 경직성 & 금($3,887~$3,896/oz) 동시 지지!)"'
    )
    text = text.replace(
        '"[11/16 모닝·금 vs 비트코인 동시 바닥] 미 금리 5.10%가 만든 기막힌 우연: \'금($3,881.7 · 10/30 쌍바닥)\'과 \'비트코인(9524만원 · 200일선)\'이 동시에 바닥에 왔다!"',
        '"[11/16 모닝·기관 매집과 진바닥] 스트래티지(MSTR) \'850,364 BTC(평단 $75,456) 총량의 4% 독식\'과 금($3,887/oz): 양대 대체자산의 강력한 하방 지지선"'
    )

    with open(p3_path, "w", encoding="utf-8") as f:
        f.write(text)


def update_generator_and_index():
    gen_path = os.path.join(SCRIPTS_DIR, "generate_briefing.py")
    with open(gen_path, "r", encoding="utf-8") as f:
        gtext = f.read()

    old_hl_prefix = '"executiveHeadline": "[11/15 이브닝 · 40대 심층안건]'
    for line in gtext.splitlines():
        if old_hl_prefix in line:
            new_line = '        "executiveHeadline": "[11/16 모닝 · 40대 심층안건] ①거시: 월요일 아시아 장 개막 & 오늘 밤 케빈 워시 연준 의장 AI·생산성 연설 ➔ 화 미 10월 소매판매 ➔ 수 FOMC 의사록 빅이벤트 주간 돌입(미 10년물 5.15%) · ②반도체: 엔비디아 실적 발표 주간 개막(베라 루빈 로드맵 & TSMC 3nm 커스텀 NVHBM 베이스다이 도입 파장)·삼성전자 \'1c D램 HBM4\' 퀄테스트 임박·SK하이닉스 청주 P&T6 후공정 발주 · ③미래기술: 미 원자력규제위원회(NRC) 다우·엑스에너지 텍사스 \'롱 모트 SMR 건설 허가\' 전격 승인(두산에너빌리티 수혜)·스타십 쉽42 메카질라 포획 성공·테슬라 프리몬트 옵티머스 양산 라인 가동 · ④전쟁/지정학: 에이태큼스(ATACMS) 장거리 타격 및 서방 유도탄 재고 고갈 속 K-방산 수주 호황·구리 $14,000/t 품귀 전망 & CME 실물 우라늄($91.85/lb) 선물 추진 · ⑤증시/세테크: 미 국채 5.15%+환율 1,335원 환노출 채권 전략·연말 해외주식 양도세 22% 손익통산 · ⑥금: 강달러 속 $3,887~$3,896/oz 지지선 안착 및 신흥국 중앙은행 월 60~85톤 실물 매집 · ⑦비트코인: 스트래티지(MSTR) 총 850,364 BTC(발행량의 4%+ · 평단 $75,456) 보유 하방 지지 및 업비트 실시간 원화 시세 연동 · ⑧부동산: 스트레스 DSR 3단계 수도권 집중 여파 강남3구 단기 숨고르기 vs 비강남 역세권·전월세(월세 비중 50%+) 강세·1주택 종부세 14억 공제 상향 추진",'
            gtext = gtext.replace(line, new_line)
            break

    with open(gen_path, "w", encoding="utf-8") as f:
        f.write(gtext)

    idx_path = os.path.join(BASE_DIR, "index.html")
    with open(idx_path, "r", encoding="utf-8") as f:
        itext = f.read()
    itext = itext.replace(
        "2026년 11월 15일 · 20:00 PM 이브닝 에디션",
        "2026년 11월 16일 · 08:00 AM 모닝 에디션"
    )
    with open(idx_path, "w", encoding="utf-8") as f:
        f.write(itext)


if __name__ == "__main__":
    update_part1()
    update_part2()
    update_part3()
    update_generator_and_index()
    print("Successfully updated all 40 agendas for 2026-11-16_0800!")
