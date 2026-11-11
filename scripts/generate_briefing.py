# -*- coding: utf-8 -*-
"""
데일리 모닝 & 이브닝 인텔리전스 브리핑 생성 엔진 (08:00 / 20:00 정각 + 늦게 켰을 때 자동 보충 실행)
- 08:00 ~ 19:59 구간: 당일 '08:00 AM 모닝 에디션 (YYYY-MM-DD_0800)' 생성
- 20:00 ~ 익일 07:59 구간: '20:00 PM 이브닝 에디션 (YYYY-MM-DD_2000)' 생성
- 실시간 시장 지표를 안건 수치(keyMetrics)와 차트에 동적으로 주입하여 클라우드 단독 실행 시에도 최신 수치 보장
"""
import os
import sys
import json
import datetime
import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(BASE_DIR, "scripts"))

from chart_generator import (
    ensure_dir,
    create_line_chart_svg,
    create_bar_comparison_svg,
    create_infographic_matrix_svg,
)
from agendas_part1 import AGENDAS_PART1
from agendas_part2 import AGENDAS_PART2
from agendas_part3 import AGENDAS_PART3
from archive_manager import process_tiered_archives

MARKET_SYMBOLS = [
    {"symbol": "^GSPC", "id": "sp500", "name": "S&P 500", "category": "macro", "unit": "", "color": "#38bdf8"},
    {"symbol": "^IXIC", "id": "nasdaq", "name": "나스닥 종합", "category": "macro", "unit": "", "color": "#818cf8"},
    {"symbol": "^SOX", "id": "sox", "name": "필라델피아 반도체", "category": "tech", "unit": "", "color": "#a855f7"},
    {"symbol": "^TNX", "id": "us10y", "name": "미 10년물 국채금리", "category": "macro", "unit": "%", "color": "#f43f5e"},
    {"symbol": "KRW=X", "id": "usdkrw", "name": "원/달러 환율", "category": "macro", "unit": "원", "color": "#10b981"},
    {"symbol": "GC=F", "id": "gold", "name": "금 선물 ($/oz)", "category": "gold", "unit": "$", "color": "#fbbf24"},
    {"symbol": "BTC-KRW", "id": "btc", "name": "비트코인 (만원)", "category": "crypto", "unit": "만원", "color": "#f97316", "scale": 0.0001},
    {"symbol": "NVDA", "id": "nvda", "name": "엔비디아 (NVDA)", "category": "tech", "unit": "$", "color": "#22c55e"},
    {"symbol": "TSM", "id": "tsm", "name": "TSMC (TSM)", "category": "tech", "unit": "$", "color": "#06b6d4"},
    {"symbol": "005930.KS", "id": "samsung", "name": "삼성전자", "category": "tech", "unit": "원", "color": "#3b82f6"},
    {"symbol": "000660.KS", "id": "skhynix", "name": "SK하이닉스", "category": "tech", "unit": "원", "color": "#ec4899"},
    {"symbol": "CL=F", "id": "wti", "name": "WTI 원유 선물", "category": "geopolitics", "unit": "$", "color": "#eab308"},
    {"symbol": "DX-Y.NYB", "id": "dxy", "name": "달러 인덱스 (DXY)", "category": "macro", "unit": "", "color": "#94a3b8"},
]

RSS_FEEDS = [
    {"category": "macro", "source": "CNBC Economy", "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=20910258"},
    {"category": "tech", "source": "CNBC Tech", "url": "https://search.cnbc.com/rs/search/combinedcms/view.xml?partnerId=wrss01&id=19854910"},
    {"category": "frontier", "source": "Google 뉴스 (우주/로봇/SMR/바이오)", "url": "https://news.google.com/rss/search?q=SpaceX+SMR+%EC%9B%90%EC%A0%84+%ED%9C%B4%EB%A8%B8%EB%85%B8%EC%9D%B4%EB%93%9C+%EB%B9%84%EB%A7%8C%EC%B9%98%EB%A3%8C%EC%A0%9C+%EC%96%91%EC%9E%90%EC%BB%B4%ED%93%A8%ED%8C%85&hl=ko&gl=KR&ceid=KR:ko"},
    {"category": "geopolitics", "source": "Google 뉴스 (전쟁/지정학/방산/원자재)", "url": "https://news.google.com/rss/search?q=%EB%B0%A9%EC%82%B0+%EC%9A%B0%ED%81%AC%EB%9D%BC%EC%9D%B4%EB%82%98+%EC%A4%91%EB%8F%99+%EA%B4%80%EC%84%B8+%EC%9A%B0%EB%9D%BC%EB%8A%AC+%EA%B5%AC%EB%A6%AC&hl=ko&gl=KR&ceid=KR:ko"},
    {"category": "equities", "source": "Google 뉴스 (증시/밸류업/절세/ISA)", "url": "https://news.google.com/rss/search?q=%EB%B0%B8%EB%A5%98%EC%97%85+ISA+%EC%96%91%EB%8F%84%EC%86%8C%EB%93%9D%EC%84%B8+%EB%B0%B0%EB%8B%B9+%EC%A1%B0%EC%84%A0&hl=ko&gl=KR&ceid=KR:ko"},
    {"category": "realestate", "source": "Google 뉴스 (한국 부동산/정책)", "url": "https://news.google.com/rss/search?q=%EB%B6%80%EB%8F%99%EC%82%B0+%EC%A0%95%EC%B1%85+%EC%9E%AC%EA%B1%B4%EC%B6%95+DSR+GTX&hl=ko&gl=KR&ceid=KR:ko"},
    {"category": "gold", "source": "Google 뉴스 (금 시세/전망)", "url": "https://news.google.com/rss/search?q=%EA%B8%88+%EC%8B%9C%EC%84%B8+%EC%98%A8%EC%8A%A4+%EC%A4%91%EC%95%99%EC%9D%80%ED%96%89+%EA%B8%88%EA%B0%92&hl=ko&gl=KR&ceid=KR:ko"},
    {"category": "crypto", "source": "Google 뉴스 (비트코인 ETF)", "url": "https://news.google.com/rss/search?q=%EB%B9%84%ED%8A%B8%EC%BD%94%EC%9D%B8+%ED%98%84%EB%AC%BC+ETF+%EA%B8%B0%EA%B4%80&hl=ko&gl=KR&ceid=KR:ko"},
]

UNPRODUCTIVE_KEYWORDS = [
    "연예", "아이돌", "걸그룹", "보이그룹", "예능", "드라마", "열애", "결혼", "이혼", "가수", "배우",
    "스타", "화보", "팬미팅", "콘서트", "음원", "가십", "celebrity", "gossip", "hollywood", "k-pop"
]


def get_target_edition_slot(now=None):
    """
    현재 시각을 기준으로 이미 도래한 가장 최근 정규 에디션(08:00 또는 20:00)을 반환합니다.
    (아직 도래하지 않은 미래 시각의 에디션은 절대 미리 생성하지 않습니다.)
    - 00:00 ~ 07:59 -> 전일 20:00 PM 이브닝 에디션 (어제 20시)
    - 08:00 ~ 19:59 -> 당일 08:00 AM 모닝 에디션 (오늘 08시)
    - 20:00 ~ 23:59 -> 당일 20:00 PM 이브닝 에디션 (오늘 20시)
    """
    if now is None:
        now = datetime.datetime.now()

    if now.hour < 8:
        target_date = (now - datetime.timedelta(days=1)).date()
        slot_code = "2000"
        slot_label = "20:00 PM 이브닝 에디션"
    elif 8 <= now.hour < 20:
        target_date = now.date()
        slot_code = "0800"
        slot_label = "08:00 AM 모닝 에디션"
    else:
        target_date = now.date()
        slot_code = "2000"
        slot_label = "20:00 PM 이브닝 에디션"

    edition_id = f"{target_date.strftime('%Y-%m-%d')}_{slot_code}"
    display_date = target_date.strftime("%Y년 %m월 %d일")
    short_date = f"{target_date.strftime('%m/%d')} {'08:00' if slot_code == '0800' else '20:00'}"
    return {
        "editionId": edition_id,
        "displayDate": display_date,
        "shortDate": short_date,
        "slotCode": slot_code,
        "slotLabel": slot_label,
    }


def fetch_market_data():
    results = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    for item in MARKET_SYMBOLS:
        sym = item["symbol"]
        try:
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}?range=1mo&interval=1d"
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=6) as resp:
                raw = json.loads(resp.read().decode("utf-8"))
                res = raw["chart"]["result"][0]
                meta = res["meta"]
                timestamps = res.get("timestamp", [])
                closes = res["indicators"]["quote"][0].get("close", [])

                valid_pts = [(ts, c) for ts, c in zip(timestamps, closes) if c is not None]
                price = meta.get("regularMarketPrice")
                if price is None and valid_pts:
                    price = valid_pts[-1][1]

                prev_day = valid_pts[-2][1] if len(valid_pts) >= 2 else meta.get("chartPreviousClose", price)
                month_start = valid_pts[0][1] if valid_pts else prev_day

                day_chg_pct = ((price - prev_day) / prev_day * 100.0) if prev_day else 0.0
                month_chg_pct = ((price - month_start) / month_start * 100.0) if month_start else 0.0

                scale = item.get("scale", 1.0)
                scaled_price = round(price * scale) if scale != 1.0 else (round(price, 2) if price else 0)
                labels = [datetime.datetime.fromtimestamp(ts).strftime("%m/%d") for ts, _ in valid_pts[-10:]]
                vals = [round(c * scale) if scale != 1.0 else round(c, 2) for _, c in valid_pts[-10:]]

                results.append({
                    **item,
                    "price": scaled_price,
                    "dayChangePct": round(day_chg_pct, 2),
                    "monthChangePct": round(month_chg_pct, 2),
                    "historyLabels": labels,
                    "historyValues": vals,
                })
        except Exception as e:
            print(f"[WARN] Failed to fetch {sym}: {e}")
    return results


def fetch_live_rss_headlines():
    headlines = []
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    for feed in RSS_FEEDS:
        try:
            req = urllib.request.Request(feed["url"], headers=headers)
            with urllib.request.urlopen(req, timeout=6) as resp:
                xml_bytes = resp.read()
                root = ET.fromstring(xml_bytes)
                for item in root.findall(".//item")[:6]:
                    title = item.findtext("title") or ""
                    link = item.findtext("link") or ""
                    pub_date = item.findtext("pubDate") or ""
                    if title:
                        low_t = title.lower()
                        if any(kw in low_t for kw in UNPRODUCTIVE_KEYWORDS):
                            continue
                        headlines.append({
                            "category": feed["category"],
                            "source": feed["source"],
                            "title": title.strip(),
                            "link": link.strip(),
                            "pubDate": pub_date.strip()[:25]
                        })
        except Exception as e:
            print(f"[WARN] RSS fetch skipped for {feed['source']}: {e}")
    return headlines


def inject_live_market_into_agendas(agendas, market_data):
    """실시간 시장 시세를 관련 안건의 keyMetrics 및 시계열 차트에 동적으로 반영합니다."""
    qmap = {m["id"]: m for m in market_data}
    agenda_live_binding = {
        "agenda_02": "us10y",
        "agenda_05": "usdkrw",
        "agenda_27": "gold",
        "agenda_31": "btc",
    }
    for ag in agendas:
        aid = ag["id"]
        if aid in agenda_live_binding and agenda_live_binding[aid] in qmap:
            m = qmap[agenda_live_binding[aid]]
            if m.get("historyLabels") and len(m["historyLabels"]) >= 5:
                ag["chartConfig"]["labels"] = m["historyLabels"]
                ag["chartConfig"]["values"] = m["historyValues"]
                if m["unit"] == "만원":
                    p_str = f"{int(round(m['price']))}만원"
                else:
                    p_str = f"{m['price']:,.2f}{m['unit']}"
                ag["chartConfig"]["badge_text"] = f"LIVE {p_str}"
                if aid == "agenda_31" and ag.get("keyMetrics"):
                    ag["keyMetrics"][0]["value"] = p_str
    return agendas


def generate_all_charts(agendas, market_data):
    charts_dir = os.path.join(BASE_DIR, "assets", "charts")
    ensure_dir(charts_dir)

    for ag in agendas:
        cfg = ag.get("chartConfig", {})
        ctype = cfg.get("type", "line")
        out_path = os.path.join(BASE_DIR, ag["chartImage"].replace("/", os.sep))
        if ctype == "line":
            create_line_chart_svg(
                filepath=out_path,
                title=cfg["title"],
                subtitle=cfg["subtitle"],
                labels=cfg["labels"],
                values=cfg["values"],
                unit=cfg.get("unit", ""),
                color=cfg.get("color", "#0284c7"),
                benchmark_val=cfg.get("benchmark_val"),
                benchmark_label=cfg.get("benchmark_label", ""),
                annotations=cfg.get("annotations"),
                badge_text=cfg.get("badge_text", "")
            )
        elif ctype == "bar":
            create_bar_comparison_svg(
                filepath=out_path,
                title=cfg["title"],
                subtitle=cfg["subtitle"],
                categories=cfg["categories"],
                series_name_1=cfg["series_name_1"],
                values_1=cfg["values_1"],
                color_1=cfg.get("color_1", "#0284c7"),
                series_name_2=cfg.get("series_name_2"),
                values_2=cfg.get("values_2"),
                color_2=cfg.get("color_2", "#d97706"),
                unit=cfg.get("unit", "")
            )
        elif ctype == "infographic":
            create_infographic_matrix_svg(
                filepath=out_path,
                title=cfg["title"],
                subtitle=cfg["subtitle"],
                nodes=cfg["nodes"],
                center_label=cfg["center_label"],
                badge_text=cfg.get("badge_text", "DEEP-DIVE")
            )

    for m in market_data:
        if m.get("historyLabels") and m.get("historyValues"):
            live_svg_path = os.path.join(charts_dir, f"live_{m['id']}.svg")
            p_str = f"{int(round(m['price']))}만원" if m["unit"] == "만원" else f"{m['price']:,.2f}{m['unit']}"
            create_line_chart_svg(
                filepath=live_svg_path,
                title=f"{m['name']} 최근 시세 추이",
                subtitle=f"현재가: {p_str} (일간 {m['dayChangePct']:+.2f}% / 1개월 {m['monthChangePct']:+.2f}%)",
                labels=m["historyLabels"],
                values=m["historyValues"],
                unit=m["unit"],
                color=m["color"],
                badge_text=f"LIVE: {p_str}"
            )


def update_html_cache_busters(version_tag):
    """브라우저 캐시 때문에 이전 회차가 보이는 현상을 방지하기 위해 HTML 스크립트 태그에 버전 쿼리를 갱신합니다."""
    import re
    for html_name in ["index.html", "detail.html"]:
        hpath = os.path.join(BASE_DIR, html_name)
        if os.path.exists(hpath):
            try:
                with open(hpath, "r", encoding="utf-8") as f:
                    content = f.read()
                content = re.sub(
                    r'src="data/briefing_data\.js(\?v=[^"]*)?"',
                    f'src="data/briefing_data.js?v={version_tag}"',
                    content
                )
                content = re.sub(
                    r'src="assets/js/(app|detail)\.js(\?v=[^"]*)?"',
                    rf'src="assets/js/\1.js?v={version_tag}"',
                    content
                )
                with open(hpath, "w", encoding="utf-8") as f:
                    f.write(content)
            except Exception as e:
                print(f"[WARN] HTML cache buster update skipped ({html_name}): {e}")


def build_briefing_edition():
    now = datetime.datetime.now()
    slot_info = get_target_edition_slot(now)
    edition_id = slot_info["editionId"]

    print(f"[1/5] 실시간 글로벌 시장 지표 수집 중... (목표 에디션: {edition_id})")
    market_data = fetch_market_data()

    print("[2/5] 실시간 국내외 RSS 뉴스 헤드라인 수집 중 (생산성 없는 연예/가십 원천 배제)...")
    rss_headlines = fetch_live_rss_headlines()

    agendas = inject_live_market_into_agendas(AGENDAS_PART1 + AGENDAS_PART2 + AGENDAS_PART3, market_data)
    print(f"[3/5] 총 {len(agendas)}개 심층 안건 전용 고해상도 차트/인포그래픽 SVG 생성 중...")
    generate_all_charts(agendas, market_data)

    delta_counts = {"REINFORCED": 0, "CHALLENGED": 0, "NEW": 0, "MAINTAINED": 0}
    for ag in agendas:
        st = ag.get("deltaStatus", "MAINTAINED")
        delta_counts[st] = delta_counts.get(st, 0) + 1

    edition_payload = {
        "editionId": edition_id,
        "generatedAt": now.strftime("%Y-%m-%d %H:%M:%S KST"),
        "displayDate": slot_info["displayDate"],
        "shortDate": slot_info["shortDate"],
        "slotLabel": slot_info["slotLabel"],
        "scheduleInfo": "매일 08:00 / 20:00 정각 발행 · 8대 영역 40건 돈이 되는 지식 브리핑",
        "totalAgendas": len(agendas),
        "deltaSummary": delta_counts,
        "executiveHeadline": "[11/11 이브닝 · 40대 심층안건] ①거시: 미 10년물 4.98% 속 원/달러 1,336.82원(-0.52%) 역행 강세 · ②반도체: SK하이닉스(+5.36%)·삼성전자(+3.57%) 폭등 및 리벨리온 R200 NVLink·HBM4 TSMC 3나노 베이스다이 · ③미래기술: 스페이스X 스타십 15차 비행(11/13)·미 NRC 60년 만의 SMR 4기 건설 허가·일라이릴리 경구용 비만약 3상·IBM 520큐비트 양자칩 · ④전쟁/지정학: 아부다비 미·러·우 3자 회담·한화에어로 미 탄약공장+LNG 패키지·우라늄/구리 슈퍼사이클 · ⑤증시/세테크: 버핏 현금규율·K조선 밸류업·해외주식 양도세 22% 절세 및 ISA/연금/환노출 채권 공식 · ⑥금($4,059.2 반등)·⑦비트코인(9865만원·IBIT $59.29B)·⑧부동산(서울 전세가율 디커플링·용산 3대 호재)",
        "marketQuotes": market_data,
        "liveHeadlines": rss_headlines,
        "agendas": agendas
    }

    editions_dir = os.path.join(BASE_DIR, "data", "editions")
    ensure_dir(editions_dir)

    edition_file = os.path.join(editions_dir, f"{edition_id}.json")
    with open(edition_file, "w", encoding="utf-8") as f:
        json.dump(edition_payload, f, ensure_ascii=False, indent=2)

    print("[4/5] 7일 원본 보관함 및 7일 / 30일 / 120일(1분기) 최중요 브리핑 계층형 합산(Roll-up) 처리 중...")
    archive_result = process_tiered_archives(BASE_DIR, edition_payload)

    implications_db = {
        "lastUpdated": now.strftime("%Y-%m-%d %H:%M:%S KST"),
        "activeEdition": edition_id,
        "implications": [
            {
                "agendaId": ag["id"],
                "category": ag["category"],
                "title": ag["title"],
                "deltaStatus": ag["deltaStatus"],
                "previousImplication": ag["previousImplication"],
                "newCatalyst": ag["newCatalyst"],
                "updatedImplication": ag["updatedImplication"],
            }
            for ag in agendas
        ]
    }
    db_file = os.path.join(BASE_DIR, "data", "implications_db.json")
    with open(db_file, "w", encoding="utf-8") as f:
        json.dump(implications_db, f, ensure_ascii=False, indent=2)

    portal_bundle = {
        "currentEdition": edition_payload,
        "recent7dEditions": archive_result["recent7dEditions"],
        "weeklyRollup": archive_result["weeklyRollup"],
        "monthlyRollup": archive_result["monthlyRollup"],
        "quarterlyRollup": archive_result["quarterlyRollup"],
    }

    js_bundle_path = os.path.join(BASE_DIR, "data", "briefing_data.js")
    with open(js_bundle_path, "w", encoding="utf-8") as f:
        f.write("// Auto-generated by generate_briefing.py\n")
        f.write("window.BRIEFING_PORTAL_DATA = ")
        json.dump(portal_bundle, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    version_tag = now.strftime("%Y%m%d_%H%M%S")
    update_html_cache_busters(version_tag)

    print(f"[5/5] 브리핑(총 {len(agendas)}건) 및 7/30/120일 아카이브 빌드 완료! ({js_bundle_path})")

    if not os.environ.get("GITHUB_ACTIONS"):
        try:
            import subprocess
            import shutil
            git_dir = os.path.join(BASE_DIR, ".git")
            if os.path.exists(git_dir):
                print("[SYNC] 공유 웹페이지(GitHub Pages)로 최신 브리핑 자동 업로드 중...")
                # 만약 이전 rebase 중단 상태가 남아있다면 안전하게 정리 후 현재 워킹트리를 main 브랜치로 고정
                for rb_folder in ["rebase-merge", "rebase-apply"]:
                    rb_path = os.path.join(git_dir, rb_folder)
                    if os.path.exists(rb_path):
                        shutil.rmtree(rb_path, ignore_errors=True)
                subprocess.run(["git", "checkout", "-B", "main"], cwd=BASE_DIR, check=False, capture_output=True)
                subprocess.run(["git", "add", "-A"], cwd=BASE_DIR, check=False)
                commit_msg = f"update: briefing {edition_id} 40-agendas ({now.strftime('%H:%M KST')})"
                subprocess.run(["git", "commit", "-m", commit_msg], cwd=BASE_DIR, check=False, capture_output=True)
                push_res = subprocess.run(["git", "push", "--force", "origin", "HEAD:main"], cwd=BASE_DIR, check=False, capture_output=True, text=True)
                if push_res.returncode == 0:
                    print("[SYNC] 공유 웹페이지(GitHub Pages) 강제 동기화 완료!")
                else:
                    print(f"[WARN] GitHub push 결과 ({push_res.returncode}): {push_res.stderr}")
        except Exception as e:
            print(f"[WARN] GitHub 자동 동기화 건너뜀: {e}")


if __name__ == "__main__":
    build_briefing_edition()
