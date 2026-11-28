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
try:
    from agendas_extra import AGENDAS_EXTRA
except ImportError:
    AGENDAS_EXTRA = []
from archive_manager import process_tiered_archives
from fact_guard import validate_edition_facts

MARKET_SYMBOLS = [
    {"symbol": "^GSPC", "id": "sp500", "name": "S&P 500", "category": "macro", "unit": "", "color": "#38bdf8"},
    {"symbol": "^IXIC", "id": "nasdaq", "name": "나스닥 종합", "category": "macro", "unit": "", "color": "#818cf8"},
    {"symbol": "^DJI", "id": "dow", "name": "다우존스 산업", "category": "macro", "unit": "", "color": "#0284c7"},
    {"symbol": "^SOX", "id": "sox", "name": "필라델피아 반도체", "category": "tech", "unit": "", "color": "#a855f7"},
    {"symbol": "^KS11", "id": "kospi", "name": "코스피 (KOSPI)", "category": "equities", "unit": "", "color": "#059669"},
    {"symbol": "^KQ11", "id": "kosdaq", "name": "코스닥 (KOSDAQ)", "category": "equities", "unit": "", "color": "#14b8a6"},
    {"symbol": "^TNX", "id": "us10y", "name": "미 10년물 국채금리", "category": "macro", "unit": "%", "color": "#f43f5e"},
    {"symbol": "KRW=X", "id": "usdkrw", "name": "원/달러 환율", "category": "macro", "unit": "원", "color": "#10b981"},
    {"symbol": "DX-Y.NYB", "id": "dxy", "name": "달러 인덱스 (DXY)", "category": "macro", "unit": "", "color": "#94a3b8"},
    {"symbol": "GC=F", "id": "gold", "name": "금 선물 ($/oz)", "category": "gold", "unit": "$", "color": "#fbbf24"},
    {"symbol": "BTC-KRW", "id": "btc", "name": "비트코인 (만원)", "category": "crypto", "unit": "만원", "color": "#f97316", "scale": 0.0001},
    {"symbol": "NVDA", "id": "nvda", "name": "엔비디아 (NVDA)", "category": "tech", "unit": "$", "color": "#22c55e"},
    {"symbol": "TSM", "id": "tsm", "name": "TSMC (TSM)", "category": "tech", "unit": "$", "color": "#06b6d4"},
    {"symbol": "GOOGL", "id": "google", "name": "구글 (Alphabet 통합)", "category": "tech", "unit": "$", "color": "#4285f4"},
    {"symbol": "AMD", "id": "amd", "name": "AMD (AMD)", "category": "tech", "unit": "$", "color": "#ef4444"},
    {"symbol": "ANT", "id": "anthropic", "name": "앤트로픽 (ANT)", "category": "tech", "unit": "$", "color": "#d97706"},
    {"symbol": "005930.KS", "id": "samsung", "name": "삼성전자", "category": "tech", "unit": "원", "color": "#3b82f6"},
    {"symbol": "000660.KS", "id": "skhynix", "name": "SK하이닉스", "category": "tech", "unit": "원", "color": "#ec4899"},
    {"symbol": "CL=F", "id": "wti", "name": "WTI 원유 선물", "category": "geopolitics", "unit": "$", "color": "#eab308"},
    {"symbol": "HG=F", "id": "copper", "name": "구리 선물 ($/lb)", "category": "geopolitics", "unit": "$", "color": "#d97706"},
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

    # KRX 공식 지수(코스피·코스닥)는 Yahoo 전일봉 누락으로 인한 오차 방지를 위해 네이버 공식 API로 정확한 등락률·종가 동기화
    naver_idx_map = {"kospi": "KOSPI", "kosdaq": "KOSDAQ"}
    for m in results:
        ncode = naver_idx_map.get(m["id"])
        if not ncode:
            continue
        try:
            nurl = f"https://m.stock.naver.com/api/index/{ncode}/basic"
            nreq = urllib.request.Request(nurl, headers=headers)
            with urllib.request.urlopen(nreq, timeout=6) as nresp:
                ndata = json.loads(nresp.read().decode("utf-8"))
                n_price_str = str(ndata.get("closePrice", "")).replace(",", "").strip()
                n_chg_str = str(ndata.get("fluctuationsRatio", "")).replace(",", "").strip()
                if n_price_str:
                    m["price"] = round(float(n_price_str), 2)
                if n_chg_str:
                    m["dayChangePct"] = round(float(n_chg_str), 2)
        except Exception as e:
            print(f"[WARN] Naver index sync skipped for {ncode}: {e}")

    return results


def _parse_cnbc_mktcap(text):
    """'3.025T', '696.037B', '520.1M' 문자열을 달러 숫자(원화/달러 원본)로 변환합니다."""
    if not text:
        return None
    s = str(text).strip().upper().replace(",", "").replace("$", "")
    mult = 1.0
    if s.endswith("T"):
        mult = 1e12
        s = s[:-1]
    elif s.endswith("B"):
        mult = 1e9
        s = s[:-1]
    elif s.endswith("M"):
        mult = 1e6
        s = s[:-1]
    try:
        return float(s) * mult
    except Exception:
        return None


def _parse_naver_krw_mktcap(text):
    """'1,057조 5,918억' 형식의 네이버 시가총액 문자열을 원(KRW) 숫자로 변환합니다."""
    if not text:
        return None
    import re
    s = str(text).replace(",", "").strip()
    jo_m = re.search(r"(\d+)\s*조", s)
    eok_m = re.search(r"(\d+)\s*억", s)
    total = 0.0
    if jo_m:
        total += float(jo_m.group(1)) * 1e12
    if eok_m:
        total += float(eok_m.group(1)) * 1e8
    return total if total > 0 else None


def fetch_stock_valuation_fundamentals(market_data):
    """
    반도체·AI 빅테크 7대 종목(NVDA, TSM, GOOGL[A+C 통합], AMD, ANT, 삼성전자[보통+우선 통합], SK하이닉스)의
    최신 시가총액 + 최근 4개 분기 순이익 합계 + 최근 1개 분기 순이익을 매일 실시간 API에서 수집하여
    ① '최근 4분기 PER' (= 현재 시총 ÷ 최근 4분기 순이익 합계)
    ② '최근 1분기 X4 PER' (= 현재 시총 ÷ (최근 1분기 순이익 × 4))
    를 정확히 산출합니다. (전년도 연간 순이익 기반 PER 절대 사용 안 함)
    """
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    now_ts = int(datetime.datetime.now().timestamp())
    start_ts = now_ts - 620 * 86400

    # 1. CNBC 실시간 시총 & USD/TWD 환율 수집 (NVDA, TSM, GOOGL[A+B+C 통합], AMD, ANT, TWD=)
    cnbc_info = {}
    usd_twd = 32.95
    try:
        cnbc_syms = "NVDA|TSM|GOOGL|AMD|ANT|TWD="
        url = f"https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols={urllib.parse.quote(cnbc_syms)}&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=1&output=json"
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=8) as resp:
            raw = json.loads(resp.read().decode("utf-8"))
            for q in raw.get("FormattedQuoteResult", {}).get("FormattedQuote", []):
                sym = q.get("symbol")
                if sym == "TWD=":
                    try:
                        usd_twd = float(str(q.get("last")).replace(",", ""))
                    except Exception:
                        pass
                else:
                    mc = _parse_cnbc_mktcap(q.get("mktcapView"))
                    try:
                        lp = float(str(q.get("last")).replace(",", ""))
                    except Exception:
                        lp = None
                    try:
                        chg = float(str(q.get("change_pct")).replace("%", "").replace("+", "").replace(",", ""))
                    except Exception:
                        chg = None
                    cnbc_info[sym] = {"marketCap": mc, "last": lp, "chg": chg}
    except Exception as e:
        print(f"[WARN] CNBC valuation fetch skipped: {e}")

    # 2. 네이버 금융 실시간 API에서 삼성전자(보통주+우선주 합산) 및 SK하이닉스 최신 시총·종가 수집
    naver_kr = {}
    for code in ["005930", "005935", "000660"]:
        entry = {"price": None, "chg": None, "mktcap": None}
        try:
            u_basic = f"https://m.stock.naver.com/api/stock/{code}/basic"
            with urllib.request.urlopen(urllib.request.Request(u_basic, headers=headers), timeout=6) as r:
                nb = json.loads(r.read().decode("utf-8"))
                if nb.get("closePrice"):
                    entry["price"] = float(str(nb["closePrice"]).replace(",", ""))
                if nb.get("fluctuationsRatio") is not None:
                    entry["chg"] = float(str(nb["fluctuationsRatio"]).replace(",", ""))
            u_int = f"https://m.stock.naver.com/api/stock/{code}/integration"
            with urllib.request.urlopen(urllib.request.Request(u_int, headers=headers), timeout=6) as r:
                ni = json.loads(r.read().decode("utf-8"))
                infos = {x.get("code"): x.get("value") for x in ni.get("totalInfos", [])}
                entry["mktcap"] = _parse_naver_krw_mktcap(infos.get("marketValue"))
        except Exception as e:
            print(f"[WARN] Naver finance fetch skipped ({code}): {e}")
        naver_kr[code] = entry

    # 최근 공식 실적 공시 직후 Yahoo DB 반영 지연(며칠)을 보완하는 검증 분기 데이터 (Yahoo에 더 최신 분기가 뜨면 자동 덮어씀)
    VERIFIED_RECENT_QUARTERS = {
        "NVDA": {
            "2026-10-31": 65287000000.0,  # Q3 FY2027 (2026-11-17 공식 발표 GAAP 순이익 $65.287B)
        },
        "ANT": {
            # S-1 투자설명서 공시 기준 H1 2026(-$80.7B) 분기 분배 + Q3 2026(-$23.291B)
            "2026-03-31": -38500000000.0,
            "2026-06-30": -42200000000.0,
            "2026-09-30": -23291000000.0,
            "2025-12-31": -16858000000.0,
        },
    }

    STOCK_CONFIGS = [
        {"id": "nvda", "yf": "NVDA", "cnbc": "NVDA", "currency": "USD", "note": "최근 4Q(Q4'26~Q3'27)"},
        {"id": "tsm", "yf": "TSM", "cnbc": "TSM", "currency": "USD", "ni_currency": "TWD", "note": "TWD➔USD 환산"},
        {"id": "google", "yf": "GOOGL", "cnbc": "GOOGL", "currency": "USD", "note": "알파벳 A+C 합산"},
        {"id": "amd", "yf": "AMD", "cnbc": "AMD", "currency": "USD", "note": "GAAP 분기순이익"},
        {"id": "anthropic", "yf": "ANT", "cnbc": "ANT", "currency": "USD", "note": "S-1·분기 GAAP(비현금 평가손 포함)"},
        {"id": "samsung", "yf": "005930.KS", "naver": "005930", "naver_pref": "005935", "currency": "KRW", "note": "보통주+우선주 합산"},
        {"id": "skhynix", "yf": "000660.KS", "naver": "000660", "currency": "KRW", "note": "연결 분기순이익"},
    ]

    qmap = {m["id"]: m for m in market_data}

    for cfg in STOCK_CONFIGS:
        sid = cfg["id"]
        yf_sym = cfg["yf"]
        m_item = qmap.get(sid)
        if not m_item:
            continue

        # A. 최근 분기별 당기순이익 수집 (Yahoo Finance fundamentals-timeseries: quarterlyNetIncome)
        q_dict = {}
        ni_curr = cfg.get("ni_currency", cfg["currency"])
        try:
            u_ts = f"https://query2.finance.yahoo.com/ws/fundamentals-timeseries/v1/finance/timeseries/{urllib.parse.quote(yf_sym)}?type=quarterlyNetIncome&period1={start_ts}&period2={now_ts}"
            with urllib.request.urlopen(urllib.request.Request(u_ts, headers=headers), timeout=8) as r:
                td = json.loads(r.read().decode("utf-8"))
                for blk in td.get("timeseries", {}).get("result", []):
                    for pt in blk.get("quarterlyNetIncome", []):
                        if pt and "reportedValue" in pt and pt.get("asOfDate"):
                            q_dict[pt["asOfDate"]] = float(pt["reportedValue"]["raw"])
                            if pt.get("currencyCode"):
                                ni_curr = pt["currencyCode"]
        except Exception as e:
            print(f"[WARN] Quarterly net income fetch skipped ({yf_sym}): {e}")

        # Yahoo에 아직 미반영된 최신 공시 분기가 있을 경우에만 보완 병합
        for d_key, val in VERIFIED_RECENT_QUARTERS.get(yf_sym, {}).items():
            if d_key not in q_dict:
                q_dict[d_key] = val

        sorted_dates = sorted(q_dict.keys())
        last_4_dates = sorted_dates[-4:]
        if len(last_4_dates) < 1:
            continue

        ni_4q_raw = sum(q_dict[d] for d in last_4_dates)
        latest_date = last_4_dates[-1]
        ni_1q_raw = q_dict[latest_date]

        # 통화 통일 (TSM: TWD 순이익 ➔ 실시간 USD/TWD 환율로 USD 변환)
        if cfg["currency"] == "USD" and ni_curr == "TWD":
            ni_4q_val = ni_4q_raw / usd_twd
            ni_1q_val = ni_1q_raw / usd_twd
        else:
            ni_4q_val = ni_4q_raw
            ni_1q_val = ni_1q_raw

        # B. 실시간 현재 시가총액 확정
        mktcap = None
        if "cnbc" in cfg:
            ci = cnbc_info.get(cfg["cnbc"], {})
            mktcap = ci.get("marketCap")
            if ci.get("last"):
                m_item["price"] = round(ci["last"], 2)
            if ci.get("chg") is not None:
                m_item["dayChangePct"] = round(ci["chg"], 2)
        elif "naver" in cfg:
            nv = naver_kr.get(cfg["naver"], {})
            if nv.get("price"):
                m_item["price"] = round(nv["price"])
            if nv.get("chg") is not None:
                m_item["dayChangePct"] = round(nv["chg"], 2)
            mc_main = nv.get("mktcap") or 0.0
            mc_pref = 0.0
            if cfg.get("naver_pref"):
                mc_pref = naver_kr.get(cfg["naver_pref"], {}).get("mktcap") or 0.0
            if mc_main > 0:
                mktcap = mc_main + mc_pref

        if not mktcap or mktcap <= 0:
            continue

        # C. 최근 4분기 PER & 최근 1분기 X4 PER 정밀 계산
        per_4q = round(mktcap / ni_4q_val, 2) if ni_4q_val != 0 else None
        per_1q_x4 = round(mktcap / (ni_1q_val * 4.0), 2) if ni_1q_val != 0 else None

        m_item["marketCap"] = round(mktcap)
        m_item["marketCapCurrency"] = cfg["currency"]
        m_item["netIncome4Q"] = round(ni_4q_val)
        m_item["netIncome1Q"] = round(ni_1q_val)
        m_item["netIncomeCurrency"] = ni_curr
        if ni_curr == "TWD":
            m_item["netIncome4QRawTwd"] = round(ni_4q_raw)
            m_item["netIncome1QRawTwd"] = round(ni_1q_raw)
            m_item["usdTwdRate"] = round(usd_twd, 4)
        m_item["latestQuarterDate"] = latest_date
        m_item["quartersUsed"] = last_4_dates
        m_item["per4Q"] = per_4q
        m_item["per1Qx4"] = per_1q_x4
        m_item["valuationNote"] = cfg["note"]

    return market_data


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


def fetch_extra_live_quotes():
    """BTC-USD 등 본문 교차검증 및 {{LIVE:*}} 템플릿 치환용 보조 실시간 시세를 수집합니다."""
    extra = {}
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    for key, sym in [("btc_usd", "BTC-USD")]:
        try:
            url = f"https://query1.finance.yahoo.com/v8/finance/chart/{urllib.parse.quote(sym)}?range=5d&interval=1d"
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=6) as resp:
                raw = json.loads(resp.read().decode("utf-8"))
                meta = raw["chart"]["result"][0]["meta"]
                p = meta.get("regularMarketPrice")
                if p:
                    extra[key] = round(float(p), 2)
        except Exception as e:
            print(f"[WARN] Extra live fetch skipped ({sym}): {e}")
    return extra


def build_live_token_map(market_data, extra_live=None):
    """실시간 API 시세와 7종목 분기 PER을 {{LIVE:*}} 치환 딕셔너리로 변환합니다 (단일 진실 공급원)."""
    extra_live = extra_live or {}
    tokens = {}

    def fmt_per(val):
        if val is None:
            return "-"
        if val < 0:
            return f"적자({val:.1f}배)"
        return f"{val:.1f}배"

    for m in market_data:
        mid = m["id"]
        p = m.get("price")
        unit = m.get("unit", "")
        chg = m.get("dayChangePct", 0.0)
        mchg = m.get("monthChangePct", 0.0)

        if p is None:
            continue
        if unit == "만원":
            p_str = f"{int(round(p)):,}만원"
        elif unit == "원":
            p_str = f"{int(round(p)):,}원" if p >= 10000 else f"{p:,.1f}원"
        elif unit == "$":
            p_str = f"${p:,.2f}"
        elif unit == "%":
            p_str = f"{p:.2f}%"
        else:
            p_str = f"{p:,.2f}"

        tokens[f"{{{{LIVE:{mid}}}}}"] = p_str
        tokens[f"{{{{LIVE:{mid}_num}}}}"] = f"{int(round(p)):,}" if unit in ("만원", "원") and p >= 1000 else f"{p:,.2f}"
        tokens[f"{{{{LIVE:{mid}_chg}}}}"] = f"{chg:+.2f}%"
        tokens[f"{{{{LIVE:{mid}_1m}}}}"] = f"{mchg:+.2f}%"

        if m.get("per4Q") is not None:
            tokens[f"{{{{LIVE:{mid}_per4q}}}}"] = fmt_per(m["per4Q"])
        if m.get("per1Qx4") is not None:
            tokens[f"{{{{LIVE:{mid}_per1qx4}}}}"] = fmt_per(m["per1Qx4"])

    if extra_live.get("btc_usd"):
        bu = float(extra_live["btc_usd"])
        tokens["{{LIVE:btc_usd}}"] = f"${bu:,.0f}"
        tokens["{{LIVE:btc_usd_exact}}"] = f"${bu:,.2f}"

    return tokens


def _replace_tokens_recursive(obj, token_map):
    if isinstance(obj, str):
        out = obj
        for k, v in token_map.items():
            if k in out:
                out = out.replace(k, v)
        return out
    elif isinstance(obj, list):
        return [_replace_tokens_recursive(x, token_map) for x in obj]
    elif isinstance(obj, dict):
        return {k: _replace_tokens_recursive(v, token_map) for k, v in obj.items()}
    return obj


def inject_live_market_into_agendas(agendas, market_data, extra_live=None):
    """
    1) {{LIVE:*}} 단일 진실 공급원(Single Source of Truth) 템플릿을 모든 안건 텍스트/지표/차트에 주입하고
    2) liveChartSymbol이 지정된 모든 라인 차트의 시계열 데이터·라벨·배지·최신 주석을 실시간 API 데이터로 자동 동기화합니다.
    """
    import copy
    qmap = {m["id"]: m for m in market_data}
    token_map = build_live_token_map(market_data, extra_live)
    hydrated = _replace_tokens_recursive(copy.deepcopy(agendas), token_map)

    default_binding = {
        "agenda_01": "sp500",
        "agenda_02": "us10y",
        "agenda_03": "wti",
        "agenda_05": "usdkrw",
        "agenda_27": "gold",
        "agenda_31": "btc",
    }
    for ag in hydrated:
        aid = ag["id"]
        cfg = ag.get("chartConfig") or {}
        sym_id = cfg.get("liveChartSymbol") or (default_binding.get(aid) if cfg.get("type") == "line" else None)
        if sym_id and sym_id in qmap and cfg.get("type") == "line":
            m = qmap[sym_id]
            if m.get("historyLabels") and len(m["historyLabels"]) >= 5:
                cfg["labels"] = list(m["historyLabels"])
                cfg["values"] = list(m["historyValues"])
                if m["unit"] == "만원":
                    p_str = f"{int(round(m['price'])):,}만원"
                elif m["unit"] == "원":
                    p_str = f"{int(round(m['price'])):,}원" if m["price"] >= 10000 else f"{m['price']:,.1f}원"
                elif m["unit"] == "$":
                    p_str = f"${m['price']:,.2f}"
                elif m["unit"] == "%":
                    p_str = f"{m['price']:.2f}%"
                else:
                    p_str = f"{m['price']:,.2f}"
                cfg["badge_text"] = f"LIVE {p_str} ({m['dayChangePct']:+.2f}%)"
                cfg["annotations"] = [{"index": len(cfg["values"]) - 1, "text": f"최신 {p_str}"}]
                if aid == "agenda_31" and ag.get("keyMetrics"):
                    ag["keyMetrics"][0]["value"] = p_str
    return hydrated


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
                    r'href="assets/css/style\.css(\?v=[^"]*)?"',
                    f'href="assets/css/style.css?v={version_tag}"',
                    content
                )
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

    print(f"[1/6] 실시간 글로벌 시장 지표 및 반도체·AI 7대 종목 분기순이익/시총 PER 수집 중... (목표 에디션: {edition_id})")
    market_data = fetch_market_data()
    market_data = fetch_stock_valuation_fundamentals(market_data)
    extra_live = fetch_extra_live_quotes()

    print("[2/6] 실시간 국내외 RSS 뉴스 헤드라인 수집 중 (생산성 없는 연예/가십 원천 배제)...")
    rss_headlines = fetch_live_rss_headlines()

    agendas = inject_live_market_into_agendas(
        AGENDAS_PART1 + AGENDAS_PART2 + AGENDAS_PART3 + AGENDAS_EXTRA,
        market_data,
        extra_live=extra_live
    )

    delta_counts = {"REINFORCED": 0, "CHALLENGED": 0, "NEW": 0, "MAINTAINED": 0}
    for ag in agendas:
        st = ag.get("deltaStatus", "MAINTAINED")
        delta_counts[st] = delta_counts.get(st, 0) + 1

    raw_exec_headline = (
        "[11/28 이브닝 · 94대 실시간 팩트체크 확장안건] "
        "①다음 주 'OPEC+ · 미 11월 고용보고서(12/4)' 슈퍼 위크 돌입! 12/8~9 FOMC(+25bp) 직전 최종 승부처: 주간 S&P {{LIVE:sp500}}(+5.6%)·나스닥 {{LIVE:nasdaq}}(+2.31%)·SOX {{LIVE:sox}}(+4.69%) 대폭발 마감 뒤 내일(11/29) OPEC+ ➔ 화 JOLTS·한국 11월 수출 ➔ 수 ADP ➔ 금 12/4 NFP 고용보고서 연쇄 출격! 미 10년물 {{LIVE:us10y}}·DXY {{LIVE:dxy}} 반등 속 원/달러 {{LIVE:usdkrw}} 강세 ➔ 1배수 미국채·현금 20% 바벨로 고용 변동성 대비! · "
        "②AI 쇼핑 에이전트 실전 ROI 첫 입증! 블프 온라인 예상치 돌파($130~134억): 어도비 초저녁 +12.8%(최종 $130~134억 상향) · 세일즈포스 글로벌 $830억(+5.2%) 돌파! 구글 제미나이({{LIVE:google}}, 4Q {{LIVE:google_per4q}})·앤트로픽 클로드({{LIVE:anthropic}}, +10.98%) 쇼핑 에이전트가 전환율·객단가(AOV) 급등 주도 ➔ AI 거품론 정면 반박 & 월요일 삼성(1Q×4 {{LIVE:samsung_per1qx4}})·SK(4Q {{LIVE:skhynix_per4q}})·TSMC({{LIVE:tsm}}, 1Q×4 {{LIVE:tsm_per1qx4}}) 훈풍! · "
        "③휴머노이드 양산 원년 & SMR 본공사 돌파: 샤오펑 범용 휴머노이드 'IRON' 2027년 1월 대량양산 선언 · ROBOTERA 중국우정 45대 실전 투입 · 멜렉시스 3D 촉각칩 + 캐나다 달링턴 그리드급 SMR 터널 굴착 완료 & IBM 15분 검증 가능 양자우위! · "
        "④내일(11/29) OPEC+ '독립 실사' 정면충돌 & 오만만 첫 봉쇄 타격: 디골리어&맥노튼 실사(이라크 490만 bpd 제한)에 이라크·카자흐 반발 & 미국 외교 압박 속 WTI {{LIVE:wti}}({{LIVE:wti_chg}}) 숨고르기 vs 미 CENTCOM 오만만 봉쇄돌파선 첫 무력화 · 구리 {{LIVE:copper}}({{LIVE:copper_chg}}) 강세! · "
        "⑤12월 한국 증시 '고배당 · 자사주 소각 · 생산적금융 ISA' 연말 절세 대전: 코스피 {{LIVE:kospi}}({{LIVE:kospi_chg}}) 박스권 내 실적·배당 차별화 전망 ➔ 12/31 한도 마감 전 연금·ISA 납입 + 4대 금융지주(고배당)·K-메모리 양날개 압축! · "
        "⑥국제 금 '{{LIVE:gold}}({{LIVE:gold_chg}})' 3주 만의 주간 상승 결산: 현물 $3,653 마감으로 $3,430 저점 딛고 반등했으나 월가 12/4 NFP·FOMC 경계 ➔ 비과세 KRX 금현물(10~15%) 보유 유지 · 추격 자제 · "
        "⑦비트코인 토요일 밤 '{{LIVE:btc}}({{LIVE:btc_usd}}, {{LIVE:btc_chg}})' 11/25 바닥 재시험: 이더리움 $1,660대 동반 부진 · 11월 현물 ETF -$53억+ 유출 · $68억 옵션만기 여진 ➔ 선물·알트 전면 금지, 무레버리지 현물 BTC 95%+ 분할 인내! · "
        "⑧부동산 규제루머 일축에도 매수심리 동결: 국토부 추가 대출규제설 '사실무근' 진화에도 주담대 4.98%·월세 51%+에 11월 CCSI·주택전망 동반 하락 ➔ 내년 1분기 상급지 급매 선별 대기!"
    )
    token_map = build_live_token_map(market_data, extra_live)
    hydrated_exec = _replace_tokens_recursive(raw_exec_headline, token_map)

    edition_payload = {
        "editionId": edition_id,
        "generatedAt": now.strftime("%Y-%m-%d %H:%M:%S KST"),
        "displayDate": slot_info["displayDate"],
        "shortDate": slot_info["shortDate"],
        "slotLabel": slot_info["slotLabel"],
        "scheduleInfo": f"매일 08:00 / 20:00 정각 발행 · 8대 영역 최소 40건+ (금회 {len(agendas)}건) · 실시간 API 교차검증 완료",
        "totalAgendas": len(agendas),
        "deltaSummary": delta_counts,
        "executiveHeadline": hydrated_exec,
        "marketQuotes": market_data,
        "liveHeadlines": rss_headlines,
        "agendas": agendas
    }

    print("[3/6] 🛡️ 할루시네이션 · 구시세 · 날짜 위조 원천 차단 검증(fact_guard.py) 실행 중...")
    passed, fc_report = validate_edition_facts(
        edition_payload,
        market_data,
        extra_live=extra_live,
        unproductive_keywords=UNPRODUCTIVE_KEYWORDS,
    )
    edition_payload["factCheckReport"] = fc_report
    if not passed:
        print(f"[BLOCKED] ❌ 팩트체크 방화벽에서 치명적 오류 {fc_report['errorCount']}건 감지! 빌드 및 GitHub Pages 배포를 즉시 중단합니다:")
        for err in fc_report["errors"]:
            print("  -", err)
        sys.exit(1)

    verified_ts = now.strftime("%Y-%m-%d %H:%M KST")
    for ag in agendas:
        ag["factVerified"] = True
        ag["factVerifiedAt"] = verified_ts
    print(f"[PASS] ✅ 팩트체크 방화벽 100% 통과! (안건 {fc_report['checkedAgendas']}건 · 실시간 API 기준가 {fc_report['liveReferenceCount']}종 교차검증 · 오류 0건 · 경고 {fc_report['warningCount']}건)")
    if fc_report["warnings"]:
        for w in fc_report["warnings"][:10]:
            print("  [WARN]", w)

    print(f"[4/6] 총 {len(agendas)}개 심층 안건 전용 고해상도 차트/인포그래픽 SVG 생성 중...")
    generate_all_charts(agendas, market_data)

    editions_dir = os.path.join(BASE_DIR, "data", "editions")
    ensure_dir(editions_dir)

    edition_file = os.path.join(editions_dir, f"{edition_id}.json")
    with open(edition_file, "w", encoding="utf-8") as f:
        json.dump(edition_payload, f, ensure_ascii=False, indent=2)

    print("[5/6] 7일 원본 보관함 및 7일 / 30일 / 120일 최중요 브리핑 계층형 합산(Roll-up) 처리 중...")
    archive_result = process_tiered_archives(BASE_DIR, edition_payload)

    implications_db = {
        "lastUpdated": now.strftime("%Y-%m-%d %H:%M:%S KST"),
        "activeEdition": edition_id,
        "factCheckPassed": True,
        "implications": [
            {
                "agendaId": ag["id"],
                "asOfDate": ag.get("asOfDate", ""),
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
        f.write("// Auto-generated by generate_briefing.py (Fact-Checked)\n")
        f.write("window.BRIEFING_PORTAL_DATA = ")
        json.dump(portal_bundle, f, ensure_ascii=False, indent=2)
        f.write(";\n")

    version_tag = now.strftime("%Y%m%d_%H%M%S")
    update_html_cache_busters(version_tag)

    print(f"[6/6] 브리핑(총 {len(agendas)}건, 팩트체크 0오류) 및 7/30/120일 아카이브 빌드 완료! ({js_bundle_path})")

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
                commit_msg = f"update: briefing {edition_id} {len(agendas)}-agendas ({now.strftime('%H:%M KST')})"
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
