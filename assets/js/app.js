// ==========================================================================
// 데일리 브리핑 메인 목록 페이지 스크립트 (app.js)
// - PC 3단 레이아웃 지원: 좌측(날짜·회차 / 브리핑 종류 / 시사점 변화별) · 중앙(브리핑 본문) · 우측(실시간 시세 보드)
// - 외부 API(CNBC · Upbit · Open ER · Binance) 연동 실시간 시세 표시 (접속 시 및 수동 클릭 시에만 갱신)
// - 안건 클릭 시 독립된 상세 페이지(detail.html)로 이동
// ==========================================================================

(function () {
    const portalData = window.BRIEFING_PORTAL_DATA || {};
    const currentEdition = portalData.currentEdition || {};
    const recent7dEditions = portalData.recent7dEditions && portalData.recent7dEditions.length > 0
        ? portalData.recent7dEditions
        : [currentEdition];
    const weeklyRollup = portalData.weeklyRollup || { agendas: [] };
    const monthlyRollup = portalData.monthlyRollup || { agendas: [] };
    const quarterlyRollup = portalData.quarterlyRollup || { agendas: [] };

    const params = new URLSearchParams(window.location.search);

    const READ_STORAGE_KEY = "briefing_read_map_v2";

    const state = {
        tier: params.get("tier") || "daily7d", // daily7d | weekly7d | monthly30d | quarterly120d
        selectedEditionId: params.get("edition") || currentEdition.editionId || "",
        category: params.get("cat") || "all",
        deltaFilter: "ALL",
        readMap: loadReadMap(),
        pinnedMap: loadJson("briefing_pinned_map_v1", {}),
        liveQuotesMap: {}
    };

    // 우측 실시간 시세 보드 기본 항목 및 그룹 정의
    const DEFAULT_MARKET_ITEMS = [
        { id: "us10y", name: "미 10년물 국채금리", unit: "%", price: 5.14, dayChangePct: 0.71, src: "CNBC", group: "rates_fx" },
        { id: "us2y", name: "미 2년물 국채금리", unit: "%", price: 4.85, dayChangePct: 0.03, src: "CNBC", group: "rates_fx" },
        { id: "usdkrw", name: "원/달러 환율", unit: "원", price: 1336.5, dayChangePct: 0.02, src: "CNBC·FX", group: "rates_fx" },
        { id: "dxy", name: "달러 인덱스 (DXY)", unit: "", price: 103.41, dayChangePct: 0.23, src: "CNBC", group: "rates_fx" },

        { id: "sp500", name: "S&P 500", unit: "", price: 7561.67, dayChangePct: -0.40, src: "CNBC", group: "indices" },
        { id: "nasdaq", name: "나스닥 종합", unit: "", price: 25136.27, dayChangePct: -0.91, src: "CNBC", group: "indices" },
        { id: "dow", name: "다우존스 산업", unit: "", price: 52347.55, dayChangePct: 0.10, src: "CNBC", group: "indices" },
        { id: "sox", name: "필라델피아 반도체", unit: "", price: 10146.32, dayChangePct: -3.43, src: "CNBC", group: "indices" },
        { id: "kospi", name: "코스피 (KOSPI)", unit: "", price: 5290.53, dayChangePct: -0.98, src: "CNBC·KRX", group: "indices" },
        { id: "kosdaq", name: "코스닥 (KOSDAQ)", unit: "", price: 699.66, dayChangePct: 0.45, src: "CNBC·KRX", group: "indices" },

        { id: "nvda", name: "엔비디아 (NVDA)", unit: "$", price: 162.85, dayChangePct: -2.01, src: "CNBC", group: "tech" },
        { id: "tsm", name: "TSMC (TSM)", unit: "$", price: 398.73, dayChangePct: -1.67, src: "CNBC", group: "tech" },
        { id: "samsung", name: "삼성전자", unit: "원", price: 206000, dayChangePct: -0.96, src: "KRX·YF", group: "tech" },
        { id: "skhynix", name: "SK하이닉스", unit: "원", price: 1216000, dayChangePct: -3.03, src: "KRX·YF", group: "tech" },

        { id: "btc", name: "비트코인 (만원)", unit: "만원", price: 9810, dayChangePct: 5.87, src: "Upbit", group: "assets" },
        { id: "gold", name: "금 선물 ($/oz)", unit: "$", price: 3887.60, dayChangePct: 0.06, src: "CNBC·COMEX", group: "assets" },
        { id: "wti", name: "WTI 원유 선물", unit: "$", price: 88.92, dayChangePct: 0.20, src: "CNBC·NYMEX", group: "assets" },
        { id: "copper", name: "구리 선물 ($/lb)", unit: "$", price: 6.06, dayChangePct: -2.14, src: "CNBC·COMEX", group: "assets" }
    ];

    const MARKET_GROUPS = [
        { key: "rates_fx", title: "🏛️ 금리 · 환율" },
        { key: "indices", title: "📈 한 · 미 주요 지수" },
        { key: "tech", title: "🔬 반도체 · AI 빅테크" },
        { key: "assets", title: "🥇 비트코인 · 금 · 원자재" }
    ];

    function loadJson(key, fallback) {
        try {
            const raw = localStorage.getItem(key);
            return raw ? JSON.parse(raw) : fallback;
        } catch (e) {
            return fallback;
        }
    }

    function loadReadMap() {
        const merged = {};
        try {
            const rawLocal = localStorage.getItem(READ_STORAGE_KEY);
            if (rawLocal) {
                Object.assign(merged, JSON.parse(rawLocal));
            }
        } catch (e) {}
        try {
            if (window.name && window.name.startsWith("BRIEFING_STATE:")) {
                const parsed = JSON.parse(window.name.slice("BRIEFING_STATE:".length));
                if (parsed && parsed.readMap) {
                    Object.assign(merged, parsed.readMap);
                }
            }
        } catch (e) {}
        return merged;
    }

    function saveReadMap(map) {
        state.readMap = map;
        try {
            localStorage.setItem(READ_STORAGE_KEY, JSON.stringify(map));
        } catch (e) {}
        try {
            window.name = "BRIEFING_STATE:" + JSON.stringify({ readMap: map });
        } catch (e) {}
    }

    function getCurrentScopeId() {
        if (state.tier === "daily7d") {
            const ed = getActiveEditionObj();
            return ed.editionId || currentEdition.editionId || "default";
        }
        return state.tier;
    }

    function makeReadKey(scopeId, agendaId) {
        return `${scopeId}::${agendaId}`;
    }

    function isAgendaRead(agendaId, scopeId) {
        const sid = scopeId || getCurrentScopeId();
        return !!state.readMap[makeReadKey(sid, agendaId)];
    }

    function markAgendaRead(agendaId, scopeId) {
        const sid = scopeId || getCurrentScopeId();
        const map = loadReadMap();
        map[makeReadKey(sid, agendaId)] = true;
        saveReadMap(map);
    }

    function formatPrice(q) {
        if (!q || q.price === undefined || q.price === null) return "-";
        const num = Number(q.price);
        if (isNaN(num)) return "-";
        if (q.unit === "만원") return Math.round(num).toLocaleString("ko-KR") + "만원";
        if (q.unit === "원") {
            if (num >= 10000) return Math.round(num).toLocaleString("ko-KR") + "원";
            return num.toLocaleString("ko-KR", { minimumFractionDigits: 1, maximumFractionDigits: 1 }) + "원";
        }
        if (q.unit === "$") return "$" + num.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        if (q.unit === "%") return num.toFixed(2) + "%";
        return num.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }

    function getActiveEditionObj() {
        const found = recent7dEditions.find(e => e.editionId === state.selectedEditionId);
        return found || recent7dEditions[0] || currentEdition;
    }

    function getMergedMarketQuotes() {
        const ed = getActiveEditionObj();
        const baseQuotes = ed.marketQuotes || currentEdition.marketQuotes || [];
        const baseMap = {};
        baseQuotes.forEach(q => {
            if (q && q.id) baseMap[q.id] = q;
        });

        return DEFAULT_MARKET_ITEMS.map(defItem => {
            const fromEd = baseMap[defItem.id] || {};
            const fromLive = state.liveQuotesMap[defItem.id] || {};
            return Object.assign({}, defItem, fromEd, fromLive, {
                name: defItem.name,
                unit: defItem.unit,
                src: fromLive.src || defItem.src,
                group: defItem.group
            });
        });
    }

    function getActiveAgendasList() {
        const pinnedIds = Object.keys(state.pinnedMap).filter(k => state.pinnedMap[k]);
        const allKnownAgendas = (currentEdition.agendas || []);

        function withUserPinned(baseList, tierLabel) {
            const map = {};
            baseList.forEach(a => { map[a.id] = a; });
            pinnedIds.forEach(pid => {
                if (!map[pid]) {
                    const found = allKnownAgendas.find(x => x.id === pid);
                    if (found) {
                        map[pid] = Object.assign({}, found, { archiveTier: tierLabel + " (사용자 지정 보존)" });
                    }
                }
            });
            return Object.values(map);
        }

        if (state.tier === "weekly7d") {
            return withUserPinned(weeklyRollup.agendas || [], "7일 주간 핵심");
        }
        if (state.tier === "monthly30d") {
            return withUserPinned(monthlyRollup.agendas || [], "30일 월간 최중요");
        }
        if (state.tier === "quarterly120d") {
            return withUserPinned(quarterlyRollup.agendas || [], "120일(1분기) 빅픽처");
        }
        const ed = getActiveEditionObj();
        return ed.agendas || [];
    }

    function setQuoteStatusText(msg) {
        document.querySelectorAll(".js-quote-status").forEach(el => {
            el.textContent = msg;
        });
    }

    function init() {
        renderHeader();
        renderRightMarketSidebar();
        renderTierControls();
        syncCategoryTabs();
        syncDeltaChips();
        renderAgendaList();
        bindEvents();
        // 새로고침 빈도: 웹페이지 접속 시 1회 자동 호출 + 사용자 수동 클릭 시에만 호출 (주기적 타이머 없음)
        fetchLiveQuotesOnOpen();
    }

    async function fetchLiveQuotesOnOpen() {
        setQuoteStatusText("🔄 외부 API에서 실시간 시세 수신 중...");

        const parseNum = (str) => {
            if (str === undefined || str === null) return NaN;
            return parseFloat(String(str).replace(/[,%+\s]/g, ""));
        };

        let updatedCount = 0;

        try {
            // 1. CNBC 글로벌 실시간 시세 웹서비스 API (금리, 한·미 지수, 환율, 반도체, 원자재)
            const cnbcSymbols = [
                "US10Y", "US2Y", ".SPX", ".IXIC", ".DJI", ".SOX",
                ".KS11", ".KQ11", "@GC.1", "@CL.1", "@HG.1", ".DXY", "KRW=", "NVDA", "TSM"
            ].join("|");
            const cnbcUrl = `https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=${encodeURIComponent(cnbcSymbols)}&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=1&output=json`;

            const cnbcPromise = fetch(cnbcUrl, { cache: "no-store" })
                .then(r => r.json())
                .then(data => {
                    const list = (data && data.FormattedQuoteResult && data.FormattedQuoteResult.FormattedQuote) || [];
                    const symToId = {
                        "US10Y": "us10y",
                        "US2Y": "us2y",
                        ".SPX": "sp500",
                        ".IXIC": "nasdaq",
                        ".DJI": "dow",
                        ".SOX": "sox",
                        ".KS11": "kospi",
                        ".KQ11": "kosdaq",
                        "@GC.1": "gold",
                        "@CL.1": "wti",
                        "@HG.1": "copper",
                        ".DXY": "dxy",
                        "KRW=": "usdkrw",
                        "NVDA": "nvda",
                        "TSM": "tsm"
                    };
                    list.forEach(item => {
                        const targetId = symToId[item.symbol];
                        if (targetId) {
                            const priceVal = parseNum(item.last);
                            const chgVal = parseNum(item.change_pct);
                            if (!isNaN(priceVal) && priceVal > 0) {
                                state.liveQuotesMap[targetId] = {
                                    price: priceVal,
                                    dayChangePct: !isNaN(chgVal) ? chgVal : 0.0,
                                    src: "CNBC LIVE"
                                };
                                updatedCount++;
                            }
                        }
                    });
                })
                .catch(() => {});

            // 2. 업비트(Upbit) 실시간 원화 비트코인 외부 API (만원 단위 표기)
            const upbitUrl = "https://api.upbit.com/v1/ticker?markets=KRW-BTC";
            const btcPromise = fetch(upbitUrl, { cache: "no-store" })
                .then(r => r.json())
                .then(arr => {
                    if (Array.isArray(arr) && arr[0]) {
                        const tradePrice = Number(arr[0].trade_price);
                        const chgRate = Number(arr[0].signed_change_rate) * 100.0;
                        if (tradePrice > 0) {
                            state.liveQuotesMap["btc"] = {
                                price: Math.round(tradePrice / 10000),
                                unit: "만원",
                                dayChangePct: !isNaN(chgRate) ? chgRate : 0.0,
                                src: "Upbit LIVE"
                            };
                            updatedCount++;
                        }
                    }
                })
                .catch(() => {});

            // 3. Open Exchange Rates API (원/달러 환율 보조 외부 API)
            const fxUrl = "https://open.er-api.com/v6/latest/USD";
            const fxPromise = fetch(fxUrl, { cache: "no-store" })
                .then(r => r.json())
                .then(data => {
                    if (data && data.rates && data.rates.KRW && !state.liveQuotesMap["usdkrw"]) {
                        state.liveQuotesMap["usdkrw"] = {
                            price: Number(data.rates.KRW),
                            dayChangePct: 0.0,
                            src: "ER-API LIVE"
                        };
                        updatedCount++;
                    }
                })
                .catch(() => {});

            await Promise.all([cnbcPromise, btcPromise, fxPromise]);

            renderHeader();
            renderRightMarketSidebar();

            const nowStr = new Date().toLocaleTimeString("ko-KR", { hour12: false });
            if (updatedCount > 0) {
                setQuoteStatusText(`🟢 외부 API 실시간 연동됨 (${nowStr} 기준)`);
            } else {
                setQuoteStatusText(`🟢 브리핑 기준 시세 표시 중 (${nowStr})`);
            }
        } catch (err) {
            setQuoteStatusText("🟢 시세 표시 중 (브리핑 기준 시세)");
        }
    }

    function renderRightMarketSidebar() {
        const rightListEl = document.getElementById("right-market-list");
        if (!rightListEl) return;

        const allQuotes = getMergedMarketQuotes();

        rightListEl.innerHTML = MARKET_GROUPS.map(grp => {
            const items = allQuotes.filter(q => q.group === grp.key);
            const rowsHtml = items.map(q => {
                const chg = Number(q.dayChangePct) || 0;
                const isUp = chg >= 0;
                const sign = isUp ? "+" : "";
                return `
                    <div class="right-quote-row">
                        <div class="right-quote-left">
                            <div class="right-quote-name">${q.name}</div>
                            <div class="right-quote-src">${q.src || "LIVE"}</div>
                        </div>
                        <div class="right-quote-right">
                            <div class="right-quote-val">${formatPrice(q)}</div>
                            <div class="right-quote-chg ${isUp ? "up" : "down"}">${sign}${chg.toFixed(2)}%</div>
                        </div>
                    </div>
                `;
            }).join("");

            return `
                <div class="market-group-block">
                    <div class="market-group-title">${grp.title}</div>
                    ${rowsHtml}
                </div>
            `;
        }).join("");
    }

    function formatExecutiveHeadlineHtml(rawText) {
        if (!rawText) return `<div class="exec-head-line">🧭 [핵심 시사점 총평]</div>`;
        const parts = String(rawText)
            .split(/(?=[①②③④⑤⑥⑦⑧⑨⑩])/)
            .map(s => s.replace(/\s*·\s*$/, "").trim())
            .filter(Boolean);

        let headPrefix = "";
        const bulletItems = [];

        parts.forEach(part => {
            if (/^[①②③④⑤⑥⑦⑧⑨⑩]/.test(part)) {
                // "①거시: 내용" 또는 "⑥금(내용)" 형태에서 앞부분 카테고리명을 굵게 강조
                const formatted = part
                    .replace(/^([①②③④⑤⑥⑦⑧⑨⑩][^:：(（]{1,14}[:：])/, '<strong style="color:#0369a1;">$1</strong> ')
                    .replace(/^([①②③④⑤⑥⑦⑧⑨⑩][^(（:：]{1,10})\((.+)\)$/, '<strong style="color:#0369a1;">$1:</strong> $2');
                bulletItems.push(`<div class="exec-item-line">${formatted}</div>`);
            } else {
                headPrefix = part;
            }
        });

        if (bulletItems.length === 0) {
            return `<div class="exec-head-line">🧭 [핵심 시사점 총평]</div><div class="exec-item-line">${rawText}</div>`;
        }

        return `
            <div class="exec-head-line">🧭 [핵심 시사점 총평] ${headPrefix}</div>
            <div class="exec-bullet-list">
                ${bulletItems.join("")}
            </div>
        `;
    }

    function renderHeader() {
        const ed = getActiveEditionObj();
        const badgeEl = document.getElementById("edition-badge");
        if (badgeEl) {
            if (state.tier === "daily7d") {
                badgeEl.textContent = `${ed.displayDate || "오늘"} · ${ed.slotLabel || "08:00 AM 에디션"}`;
            } else if (state.tier === "weekly7d") {
                badgeEl.textContent = "📌 7일 단위 최중요 브리핑 합산본";
            } else if (state.tier === "monthly30d") {
                badgeEl.textContent = "🏆 30일 단위 최중요 브리핑 합산본";
            } else {
                badgeEl.textContent = "🏛️ 120일(1분기) 최중요 브리핑 합산본";
            }
        }

        const execEl = document.getElementById("exec-summary-box");
        if (execEl) {
            const rawHeadline = ed.executiveHeadline || currentEdition.executiveHeadline || "";
            execEl.innerHTML = formatExecutiveHeadlineHtml(rawHeadline);
        }

        state.readMap = loadReadMap();
        const scopeId = getCurrentScopeId();
        const activeAgendas = getActiveAgendasList();
        const readCount = activeAgendas.filter(a => isAgendaRead(a.id, scopeId)).length;
        const readEl = document.getElementById("read-status-label");
        if (readEl) {
            const scopeLabel = state.tier === "daily7d" ? (ed.shortDate || ed.editionId || "") : "합산본";
            readEl.textContent = `열람 완료 (${scopeLabel}): ${readCount} / ${activeAgendas.length}건`;
        }

        // 모바일 상단 6대 핵심 지표 바 렌더링
        const allQuotes = getMergedMarketQuotes();
        const coreIds = ["us10y", "sp500", "sox", "gold", "btc", "usdkrw"];
        const coreBar = document.getElementById("core-metrics-bar");
        if (coreBar && allQuotes.length > 0) {
            const coreItems = coreIds.map(id => allQuotes.find(m => m.id === id)).filter(Boolean);
            coreBar.innerHTML = coreItems.map(q => {
                const chg = Number(q.dayChangePct) || 0;
                const isUp = chg >= 0;
                const sign = isUp ? "+" : "";
                return `
                    <div class="core-metric-item">
                        <div class="core-metric-name">${q.name}</div>
                        <div class="core-metric-val">${formatPrice(q)}</div>
                        <div class="core-metric-chg ${isUp ? "up" : "down"}">${sign}${chg.toFixed(2)}%</div>
                    </div>
                `;
            }).join("");
        }
    }

    function renderTierControls() {
        const subDaily = document.getElementById("sub-daily7d");
        const subWeekly = document.getElementById("sub-weekly7d");
        const subMonthly = document.getElementById("sub-monthly30d");
        const subQuarterly = document.getElementById("sub-quarterly120d");

        const curCount = (currentEdition.agendas || []).length || 40;
        if (subDaily) subDaily.textContent = `보관 에디션 ${recent7dEditions.length}회차 (회차당 ${curCount}건 보존)`;
        if (subWeekly) subWeekly.textContent = `중요 선별 ${(weeklyRollup.agendas || []).length}건 합산 보관 중`;
        if (subMonthly) subMonthly.textContent = `최중요 선별 ${(monthlyRollup.agendas || []).length}건 합산 보관 중`;
        if (subQuarterly) subQuarterly.textContent = `분기 핵심 ${(quarterlyRollup.agendas || []).length}건 영구 합산 중`;

        document.querySelectorAll(".tier-tab-btn").forEach(btn => {
            btn.classList.toggle("active", btn.getAttribute("data-tier") === state.tier);
        });

        const subCtrl = document.getElementById("tier-sub-control");
        if (!subCtrl) return;

        if (state.tier === "daily7d") {
            const buttonsHtml = recent7dEditions.map(ed => {
                const isAct = ed.editionId === (getActiveEditionObj().editionId);
                const label = ed.shortDate || `${ed.displayDate} ${ed.slotLabel}`;
                const edAgendas = ed.agendas || [];
                const edReadCount = edAgendas.filter(a => isAgendaRead(a.id, ed.editionId)).length;
                return `
                    <button class="edition-slot-btn ${isAct ? "active" : ""}" data-select-edition="${ed.editionId}">
                        <span>🗓️ ${label}</span>
                        <span style="font-size:12px;opacity:0.85;">열람 ${edReadCount}/${edAgendas.length}</span>
                    </button>
                `;
            }).join("");

            subCtrl.innerHTML = `
                <div class="edition-history-bar">
                    <span style="font-size:13.5px;font-weight:800;color:var(--text-muted);">최근 7일 날짜·회차 선택 (최대 14회차):</span>
                    ${buttonsHtml}
                </div>
            `;
        } else if (state.tier === "weekly7d") {
            subCtrl.innerHTML = `
                <div class="rollup-info-banner">
                    📌 <strong>[7일 최중요 합산]</strong> 최근 7일 브리핑 중 시사점 전환·신규·강화 핵심 안건만 자동 추출한 목록입니다.
                </div>
            `;
        } else if (state.tier === "monthly30d") {
            subCtrl.innerHTML = `
                <div class="rollup-info-banner">
                    🏆 <strong>[30일 최중요 합산]</strong> 7일 중요 브리핑 중 구조적 추세를 바꾼 최상위 안건만 남긴 월간 통합본입니다.
                </div>
            `;
        } else {
            subCtrl.innerHTML = `
                <div class="rollup-info-banner">
                    🏛️ <strong>[120일(1분기) 합산]</strong> 최근 1분기 동안의 핵심 시사점 변화를 복기하는 분기 빅픽처 보관함입니다.
                </div>
            `;
        }
    }

    function syncCategoryTabs() {
        const activeAgendas = getActiveAgendasList();
        const counts = {
            all: activeAgendas.length,
            macro: 0,
            tech: 0,
            frontier: 0,
            geopolitics: 0,
            equities: 0,
            gold: 0,
            crypto: 0,
            realestate: 0
        };
        activeAgendas.forEach(a => {
            counts[a.category] = (counts[a.category] || 0) + 1;
        });

        const labels = {
            all: `전체 안건 (${counts.all})`,
            macro: `🏛️ 거시경제 · 금리 (${counts.macro})`,
            tech: `🔬 반도체 · AI 빅테크 (${counts.tech})`,
            frontier: `🚀 미래기술 · 우주 · 로봇 · 바이오 (${counts.frontier})`,
            geopolitics: `🌍 전쟁 · 지정학 · 방산 · 원자재 (${counts.geopolitics})`,
            equities: `📈 한·미 증시 · 산업 · 세테크 (${counts.equities})`,
            gold: `🥇 금($/oz) · 안전자산 (${counts.gold})`,
            crypto: `₿ 비트코인 95%+ (${counts.crypto})`,
            realestate: `🏢 한국 부동산 · 정책 (${counts.realestate})`
        };

        document.querySelectorAll(".tab-btn").forEach(btn => {
            const cat = btn.getAttribute("data-cat");
            if (labels[cat]) btn.textContent = labels[cat];
            btn.classList.toggle("active", cat === state.category);
        });
    }

    function syncDeltaChips() {
        const activeAgendas = getActiveAgendasList();
        const catFiltered = activeAgendas.filter(ag => state.category === "all" || ag.category === state.category);
        const dCounts = {
            ALL: catFiltered.length,
            REINFORCED: 0,
            CHALLENGED: 0,
            NEW: 0,
            MAINTAINED: 0
        };
        catFiltered.forEach(ag => {
            dCounts[ag.deltaStatus] = (dCounts[ag.deltaStatus] || 0) + 1;
        });

        const dLabels = {
            ALL: `전체 보기 (${dCounts.ALL})`,
            REINFORCED: `🟢 시사점 강화 (${dCounts.REINFORCED})`,
            CHALLENGED: `🔴 시사점 약화 · 전환 (${dCounts.CHALLENGED})`,
            NEW: `🆕 신규 시사점 (${dCounts.NEW})`,
            MAINTAINED: `🟡 기조 유지 · 혼조 (${dCounts.MAINTAINED})`
        };

        document.querySelectorAll(".delta-chip").forEach(chip => {
            const dKey = chip.getAttribute("data-delta");
            if (dLabels[dKey]) chip.textContent = dLabels[dKey];
            chip.classList.toggle("active", dKey === state.deltaFilter);
        });
    }

    function renderAgendaList() {
        const listEl = document.getElementById("agenda-list");
        if (!listEl) return;

        const activeAgendas = getActiveAgendasList();
        const filtered = activeAgendas.filter(ag => {
            if (state.category !== "all" && ag.category !== state.category) return false;
            if (state.deltaFilter !== "ALL" && ag.deltaStatus !== state.deltaFilter) return false;
            return true;
        });

        if (filtered.length === 0) {
            listEl.innerHTML = `
                <div style="background:#ffffff;border:1px solid var(--border-light);border-radius:16px;padding:48px;text-align:center;font-size:20px;font-weight:700;color:var(--text-muted);">
                    선택하신 조건에 해당하는 안건이 없습니다.
                </div>
            `;
            return;
        }

        const scopeId = getCurrentScopeId();
        const activeEditionId = (getActiveEditionObj().editionId) || state.selectedEditionId;

        listEl.innerHTML = filtered.map((ag, idx) => {
            const isRead = isAgendaRead(ag.id, scopeId);
            const detailUrl = `detail.html?id=${encodeURIComponent(ag.id)}&tier=${encodeURIComponent(state.tier)}&edition=${encodeURIComponent(activeEditionId)}&cat=${encodeURIComponent(state.category)}`;
            const tierBadge = ag.archiveTier ? `<span class="badge-tier">🗂️ ${ag.archiveTier}</span>` : "";

            return `
                <a class="agenda-list-card ${isRead ? "is-read" : ""}" href="${detailUrl}" data-agenda-id="${ag.id}" data-scope-id="${scopeId}">
                    <div class="card-top-badges">
                        <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;">
                            <span class="badge-cat ${ag.category}">안건 #${idx + 1} · ${ag.categoryLabel}</span>
                            ${tierBadge}
                        </div>
                        <div style="display:flex;align-items:center;gap:10px;">
                            ${isRead ? `<span style="font-size:14px;font-weight:800;color:#059669;">✓ 읽음</span>` : ""}
                            <span class="badge-delta ${ag.deltaStatus}">${ag.deltaLabel}</span>
                        </div>
                    </div>

                    <h2 class="card-main-title">${ag.title}</h2>
                    <p class="card-subtitle">${ag.subtitle}</p>

                    <div class="card-split-body">
                        <div class="card-implication-box">
                            <div>
                                <div class="imp-item-label highlight">🧭 핵심 시사점 및 투자 판단 변화</div>
                                <div class="imp-updated-text">${ag.updatedImplication}</div>
                            </div>
                            <div>
                                <div class="imp-item-label">⏮️ 기존 시사점 대비 변화 배경</div>
                                <div class="imp-prev-text">
                                    <strong>[기존]</strong> ${ag.previousImplication}<br/>
                                    <strong style="color:#0284c7;">[신규 팩트]</strong> ${ag.newCatalyst}
                                </div>
                            </div>
                        </div>

                        <div class="card-chart-preview">
                            <img src="${ag.chartImage}" alt="${ag.title}" loading="lazy" />
                        </div>
                    </div>

                    <div class="card-footer-row">
                        <span style="font-size:15px;color:var(--text-muted);font-weight:600;">출처: ${(ag.sources || []).join(" · ")}</span>
                        <span class="go-detail-link">상세 브리핑 · 대형 차트 페이지로 이동 →</span>
                    </div>
                </a>
            `;
        }).join("");
    }

    function bindEvents() {
        // 수동 클릭 시에만 실시간 시세 새로고침 호출
        document.querySelectorAll(".js-refresh-quotes").forEach(btn => {
            btn.addEventListener("click", () => {
                fetchLiveQuotesOnOpen();
            });
        });

        // 아카이브 티어 탭 전환
        document.querySelectorAll(".tier-tab-btn").forEach(btn => {
            btn.addEventListener("click", () => {
                state.tier = btn.getAttribute("data-tier") || "daily7d";
                renderHeader();
                renderRightMarketSidebar();
                renderTierControls();
                syncCategoryTabs();
                syncDeltaChips();
                renderAgendaList();
            });
        });

        // 최근 7일 회차 선택 및 안건 클릭 시 즉시 열람 기록 위임 이벤트
        document.body.addEventListener("click", e => {
            const edBtn = e.target.closest("[data-select-edition]");
            if (edBtn) {
                state.selectedEditionId = edBtn.getAttribute("data-select-edition");
                renderHeader();
                renderRightMarketSidebar();
                renderTierControls();
                syncCategoryTabs();
                syncDeltaChips();
                renderAgendaList();
                return;
            }

            const cardEl = e.target.closest(".agenda-list-card[data-agenda-id]");
            if (cardEl) {
                const aid = cardEl.getAttribute("data-agenda-id");
                const sid = cardEl.getAttribute("data-scope-id") || getCurrentScopeId();
                if (aid) {
                    markAgendaRead(aid, sid);
                    cardEl.classList.add("is-read");
                    renderHeader();
                    renderTierControls();
                }
            }
        });

        // 브라우저 뒤로가기(BFCache 복원) 및 탭 포커스 복귀 시 열람 카운트 즉시 동기화
        const syncReadStateFromStorage = () => {
            state.readMap = loadReadMap();
            renderHeader();
            renderTierControls();
            renderAgendaList();
        };
        window.addEventListener("pageshow", syncReadStateFromStorage);
        window.addEventListener("focus", syncReadStateFromStorage);
        window.addEventListener("storage", syncReadStateFromStorage);
        document.addEventListener("visibilitychange", () => {
            if (!document.hidden) syncReadStateFromStorage();
        });

        // 카테고리 탭
        document.querySelectorAll(".tab-btn").forEach(btn => {
            btn.addEventListener("click", () => {
                state.category = btn.getAttribute("data-cat") || "all";
                syncCategoryTabs();
                syncDeltaChips();
                renderAgendaList();
            });
        });

        // 시사점 필터
        document.querySelectorAll(".delta-chip").forEach(chip => {
            chip.addEventListener("click", () => {
                state.deltaFilter = chip.getAttribute("data-delta") || "ALL";
                syncDeltaChips();
                renderAgendaList();
            });
        });
    }

    document.addEventListener("DOMContentLoaded", init);
})();
