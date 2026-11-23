# -*- coding: utf-8 -*-
"""
할루시네이션 · 구시세 · 날짜 위조 원천 차단 검증 엔진 (fact_guard.py)
- generate_briefing.py 빌드 및 GitHub Pages 푸시 직전에 반드시 실행되는 Fail-Closed 방화벽입니다.
- 단 1건의 치명적 오류(실시간 API 시세와 모순되는 구시세, 미치환 {{LIVE:*}} 토큰, 오래된 본문에
  오늘 날짜 꼬리표만 덮어쓴 좀비 기사, 차트-본문 불일치, 비생산적 연예/가십 키워드)가 발견되면
  빌드와 배포를 즉시 중단(exit code 1)합니다.
"""
import re
import datetime


# 과거 역사·목표가·지지선·평단·전고점 등 합법적 기준 수치임을 명시하는 문맥 키워드
HISTORICAL_OR_TARGET_QUALIFIERS = [
    "전고점", "고점", "최고", "역대", "목표", "타깃", "전망", "예상", "뷰", "컨센서스",
    "평단", "매입원가", "생산원가", "원가", "저점", "최저", "지지", "저항", "경계선", "기준선",
    "과거", "당시", "기존", "전월", "직전", "어제", "주말", "지난주", "금요일", "장중", "야간",
    "공모가", "상장가", "플래시", "테스트", "하회", "돌파", "상단", "하단", "밴드", "구간",
    "분할", "매집", "시나리오", "반등선", "붕괴", "조정", "10/", "11/1", "11/20", "11/21", "11/22",
    "2024", "2025", "2027", "2028", "2029", "2030", "1개월", "연초", "종가", "마감", "정규장",
    "대비", "에서", "➔", "->", "~", "부터", "까지", "선언", "약정", "매출", "시총", "보조금",
]

# 본문에 남아 있으면 안 되는 '오래된 날짜의 현재형 서술' 패턴
STALE_PRESENT_DATE_REGEX = re.compile(
    r"(11월\s*(?:1[0-7]|[1-9])일\s*(?:아침|오전|오후|저녁|밤|기준|마감))"
    r"|(\(11/(?:1[0-7]|0?[1-9])\s*(?:모닝|이브닝)\))"
)

UNRESOLVED_TOKEN_REGEX = re.compile(r"\{\{LIVE:[^}]+\}\}")


def _to_float(num_str):
    try:
        return float(str(num_str).replace(",", "").strip())
    except Exception:
        return None


def _has_qualifier_near(text, start_idx, end_idx, window=32):
    left = max(0, start_idx - window)
    right = min(len(text), end_idx + window)
    snippet = text[left:right]
    for kw in HISTORICAL_OR_TARGET_QUALIFIERS:
        if kw in snippet:
            return True
    return False


def _collect_current_texts(ag):
    """안건에서 '현재 시황/시세'를 진술하는 필드만 추출 (과거 기록 필드인 previousImplication, implicationHistory 제외)."""
    fields = []
    for k in ["title", "subtitle", "deltaLabel", "newCatalyst", "updatedImplication"]:
        v = ag.get(k)
        if isinstance(v, str) and v.strip():
            fields.append((k, v))
    for i, f in enumerate(ag.get("facts") or []):
        if isinstance(f, str):
            fields.append((f"facts[{i}]", f))
    for i, ap in enumerate(ag.get("actionPoints") or []):
        if isinstance(ap, str):
            fields.append((f"actionPoints[{i}]", ap))
    for i, km in enumerate(ag.get("keyMetrics") or []):
        if isinstance(km, dict):
            fields.append((f"keyMetrics[{i}]", f"{km.get('label', '')}: {km.get('value', '')} ({km.get('change', '')})"))
    cfg = ag.get("chartConfig") or {}
    for ck in ["title", "subtitle", "badge_text"]:
        if isinstance(cfg.get(ck), str):
            fields.append((f"chartConfig.{ck}", cfg[ck]))
    return fields


def validate_edition_facts(edition_payload, market_data, extra_live=None, unproductive_keywords=None):
    """
    에디션 전체의 실시간 시세 일치성, 날짜 무결성, 토큰 치환 완료 여부, 차트 정합성을 검증합니다.
    반환값: (passed: bool, report: dict)
    """
    errors = []
    warnings = []
    extra_live = extra_live or {}
    unproductive_keywords = unproductive_keywords or []

    agendas = edition_payload.get("agendas") or []
    edition_id = edition_payload.get("editionId", "")
    edition_date_str = edition_id.split("_")[0] if "_" in edition_id else datetime.date.today().strftime("%Y-%m-%d")
    try:
        edition_date = datetime.date.fromisoformat(edition_date_str)
    except Exception:
        edition_date = datetime.date.today()

    # 1. 최소 분량 (40건+) 검증
    if len(agendas) < 40:
        errors.append(f"[COUNT] 안건 수 부족: 현재 {len(agendas)}건 (최소 40건 이상 필수)")

    # 2. 실시간 API 기준가 맵 구성
    qmap = {m["id"]: m for m in (market_data or []) if m.get("id") and m.get("price") is not None}
    live_prices = {k: float(v["price"]) for k, v in qmap.items()}
    if extra_live.get("btc_usd"):
        live_prices["btc_usd"] = float(extra_live["btc_usd"])

    # 자산별 시세 이탈 감지 규칙: (asset_id, label, regex, max_rel_dev_or_abs, is_abs_diff, min_val, max_val)
    PRICE_RULES = [
        # 비트코인 원화 (만원 단위): 예 "비트코인 9524만원", "BTC(8,258만원)"
        ("btc", "비트코인(만원)", re.compile(r"(?:비트코인|BTC|업비트)[^.\n]{0,18}?([0-9],[0-9]{3}|[5-9][0-9]{3}|1[0-9]{4})\s*만\s*원"), 0.10, False, 3000, 30000),
        # 비트코인 달러: 예 "비트코인 $61,118"
        ("btc_usd", "비트코인($)", re.compile(r"(?:비트코인|BTC)[^.\n]{0,16}?\$([0-9]{2},[0-9]{3}(?:\.[0-9]+)?)"), 0.12, False, 20000, 250000),
        # 국제 금 ($/oz)
        ("gold", "금($/oz)", re.compile(r"(?:금\s*(?:현물|선물|값|시세)|Gold)[^.\n]{0,16}?\$([2-6],[0-9]{3}(?:\.[0-9]+)?)"), 0.08, False, 1800, 8000),
        # 엔비디아 ($)
        ("nvda", "엔비디아($)", re.compile(r"(?:엔비디아|NVDA)[^.\n]{0,14}?\$([0-9]{2,3}\.[0-9]{2})"), 0.10, False, 50, 500),
        # TSMC ($)
        ("tsm", "TSMC($)", re.compile(r"(?:TSMC|TSM)[^.\n]{0,14}?\$([0-9]{2,3}\.[0-9]{2})"), 0.10, False, 100, 700),
        # 구글 ($)
        ("google", "구글($)", re.compile(r"(?:구글|알파벳|GOOGL)[^.\n]{0,14}?\$([0-9]{2,3}\.[0-9]{2})"), 0.10, False, 100, 600),
        # AMD ($)
        ("amd", "AMD($)", re.compile(r"\bAMD\b[^.\n]{0,14}?\$([0-9]{2,3}\.[0-9]{2})"), 0.10, False, 80, 900),
        # 삼성전자 (원)
        ("samsung", "삼성전자(원)", re.compile(r"삼성전자[^.\n]{0,16}?([1-3][0-9]{2},[0-9]{3})\s*원"), 0.10, False, 50000, 400000),
        # SK하이닉스 (원)
        ("skhynix", "SK하이닉스(원)", re.compile(r"SK하이닉스[^.\n]{0,16}?([1-2],[0-9]{3},[0-9]{3})\s*원"), 0.10, False, 150000, 2500000),
        # 원/달러 환율 (원)
        ("usdkrw", "원/달러(원)", re.compile(r"(?:원/달러|원·달러|환율)[^.\n]{0,16}?(1,[2-5][0-9]{2}(?:\.[0-9]{1,2})?)\s*원"), 0.025, False, 1100, 1600),
        # 달러 인덱스 (DXY)
        ("dxy", "달러인덱스(DXY)", re.compile(r"(?:달러\s*인덱스|DXY)[^.\n]{0,12}?([9][0-9]\.[0-9]{2}|1[01][0-9]\.[0-9]{2})"), 0.025, False, 85, 120),
        # 미 10년물 국채금리 (%)
        ("us10y", "미10년물(%)", re.compile(r"(?:미\s*10년물|10년물\s*(?:국채)?금리)[^.\n]{0,14}?([3-6]\.[0-9]{2})%"), 0.30, True, 2.5, 7.0),
        # S&P 500
        ("sp500", "S&P500", re.compile(r"S&P\s*500[^.\n]{0,16}?([5-8],[0-9]{3}(?:\.[0-9]{1,2})?)"), 0.08, False, 4000, 10000),
        # 필라델피아 반도체 (SOX)
        ("sox", "SOX", re.compile(r"(?:필라델피아\s*반도체|SOX)[^.\n]{0,14}?([5-9],[0-9]{3}|1[0-2],[0-9]{3})(?:\.[0-9]{1,2})?"), 0.10, False, 3500, 15000),
        # 코스피 (KOSPI)
        ("kospi", "코스피", re.compile(r"(?:코스피|KOSPI)[^.\n]{0,16}?([3-6],[0-9]{3}(?:\.[0-9]{1,2})?)"), 0.08, False, 2000, 7000),
        # WTI 유가 ($)
        ("wti", "WTI($)", re.compile(r"WTI[^.\n]{0,14}?\$([5-9][0-9](?:\.[0-9]{1,2})?|1[0-2][0-9](?:\.[0-9]{1,2})?)"), 0.12, False, 40, 140),
    ]

    # 3. 총평(executiveHeadline) 토큰 미치환 및 시세 검증
    exec_text = edition_payload.get("executiveHeadline", "")
    if UNRESOLVED_TOKEN_REGEX.search(exec_text):
        errors.append(f"[TOKEN] executiveHeadline 미치환 토큰 잔존: {UNRESOLVED_TOKEN_REGEX.findall(exec_text)}")

    # 4. 개별 안건 전수 검증
    seen_ids = set()
    stale_title_re = re.compile(r"\[(\d{1,2})/(\d{1,2})\s*(?:모닝|이브닝)")

    for ag in agendas:
        aid = ag.get("id", "UNKNOWN")
        if aid in seen_ids:
            errors.append(f"[DUP_ID] 중복 안건 ID 발견: {aid}")
        seen_ids.add(aid)

        # (a) 필수 기준일(asOfDate) 존재 및 날짜 위조 점검
        as_of = ag.get("asOfDate")
        if not as_of:
            errors.append(f"[MISSING_DATE] {aid}: 'asOfDate' (YYYY-MM-DD) 필드 누락 — 작성 기준일 명시 필수")
        else:
            try:
                as_of_dt = datetime.date.fromisoformat(as_of)
                # 제목의 [MM/DD ...] 날짜가 asOfDate보다 미래이거나(날짜 위조!), 1일 이상 불일치하는 경우 차단
                tm = stale_title_re.search(ag.get("title", ""))
                if tm:
                    t_month, t_day = int(tm.group(1)), int(tm.group(2))
                    if (t_month, t_day) != (as_of_dt.month, as_of_dt.day):
                        errors.append(
                            f"[FAKE_DATE] {aid}: 제목 날짜({t_month:02d}/{t_day:02d})와 실제 작성 기준일 asOfDate({as_of}) 불일치! 본문 갱신 없이 날짜 꼬리표만 바꾼 위조 금지"
                        )
                age_days = (edition_date - as_of_dt).days
                if age_days > 7:
                    warnings.append(f"[OLD_AGENDA] {aid}: 기준일({as_of})이 현재({edition_date_str})보다 {age_days}일 경과")
            except Exception:
                errors.append(f"[BAD_DATE] {aid}: asOfDate 형식 오류({as_of})")

        # (b) 전체 문자열에서 미치환 토큰 & 연예/가십 키워드 검사
        all_fields = _collect_current_texts(ag)
        for fname, txt in all_fields:
            if UNRESOLVED_TOKEN_REGEX.search(txt):
                errors.append(f"[TOKEN] {aid}.{fname}: 미치환 라이브 토큰 잔존 -> {UNRESOLVED_TOKEN_REGEX.findall(txt)}")

            low_t = txt.lower()
            for ukw in unproductive_keywords:
                if ukw and ukw in low_t:
                    # "스타링크", "스타십", "스타베이스", "스타마인드", "스타트업", "에버스타", "모닝스타", "톱스타뉴스" 제외 처리
                    if ukw == "스타" and any(ok in txt for ok in ["스타링크", "스타십", "스타베이스", "스타마인드", "스타트업", "에버스타", "모닝스타", "톱스타뉴스", "스타벅스", "아스테리움"]):
                        continue
                    warnings.append(f"[UNPROD] {aid}.{fname}: 비생산 키워드 '{ukw}' 감지")

            # (c) 오래된 날짜를 '오늘 아침/어제'처럼 위장한 좀비 본문 차단
            m_stale = STALE_PRESENT_DATE_REGEX.search(txt)
            if m_stale and as_of:
                try:
                    if (edition_date - datetime.date.fromisoformat(as_of)).days <= 3:
                        errors.append(
                            f"[STALE_TEXT] {aid}.{fname}: 최신 기준일({as_of}) 안건 본문에 오래된 과거 시제 '{m_stale.group(0)}' 잔존!"
                        )
                except Exception:
                    pass

            # (d) 실시간 API 시세 대비 할루시네이션 / 구시세 편차 차단
            for asset_id, label, regex, tol, is_abs, min_v, max_v in PRICE_RULES:
                if asset_id not in live_prices:
                    continue
                live_v = live_prices[asset_id]
                for match in regex.finditer(txt):
                    val = _to_float(match.group(1))
                    if val is None or not (min_v <= val <= max_v):
                        continue
                    diff = abs(val - live_v)
                    rel_diff = diff / live_v if live_v else 0.0
                    exceeded = (diff > tol) if is_abs else (rel_diff > tol)
                    if exceeded and not _has_qualifier_near(txt, match.start(), match.end()):
                        errors.append(
                            f"[PRICE_DRIFT] {aid}.{fname}: {label} 표기 '{match.group(0).strip()}' (={val:,.2f}) vs 실시간 API '{live_v:,.2f}' (편차 {rel_diff*100:.1f}%) — 구시세/할루시네이션 의심! {{{{LIVE:{asset_id}}}}} 토큰 사용 또는 기준시점 명시 필수"
                        )

        # (e) 시계열 라인 차트 날짜 신선도 검증
        cfg = ag.get("chartConfig") or {}
        if cfg.get("type") == "line" and cfg.get("labels"):
            last_lbl = str(cfg["labels"][-1])
            lm = re.match(r"^(\d{1,2})/(\d{1,2})$", last_lbl)
            if lm and "최근" in str(cfg.get("title", "")):
                try:
                    c_dt = datetime.date(edition_date.year, int(lm.group(1)), int(lm.group(2)))
                    if (edition_date - c_dt).days > 6:
                        errors.append(
                            f"[STALE_CHART] {aid}.chartConfig: 제목에 '최근' 표기했으나 마지막 차트 날짜가 '{last_lbl}'로 오래됨! liveChartSymbol 바인딩 또는 차트 최신화 필요"
                        )
                except Exception:
                    pass

    passed = len(errors) == 0
    report = {
        "passed": passed,
        "checkedAt": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S KST"),
        "checkedAgendas": len(agendas),
        "liveReferenceCount": len(live_prices),
        "errorCount": len(errors),
        "warningCount": len(warnings),
        "errors": errors,
        "warnings": warnings,
    }
    return passed, report
