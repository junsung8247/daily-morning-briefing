// ==========================================================================
// 데일리 브리핑 메인 목록 페이지 스크립트 (app.js)
// - 최근 7일 브리핑 원본(최대 14회차) 보존 및 회차 전환
// - 7일 / 30일 / 120일(1분기) 단위 최중요 브리핑 계층형 합산 뷰 지원
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
        pinnedMap: loadJson("briefing_pinned_map_v1", {}) // 사용자가 직접 지정한 장기 보존 안건
    };

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
        if (!q || q.price === undefined) return "-";
        const num = Number(q.price);
        if (q.unit === "만원") return Math.round(num) + "만원";
        if (q.unit === "원") return num.toLocaleString("ko-KR", { maximumFractionDigits: 0 }) + "원";
        if (q.unit === "$") return "$" + num.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
        if (q.unit === "%") return num.toFixed(2) + "%";
        return num.toLocaleString("en-US", { minimumFractionDigits: 2, maximumFractionDigits: 2 });
    }

    function getActiveEditionObj() {
        const found = recent7dEditions.find(e => e.editionId === state.selectedEditionId);
        return found || recent7dEditions[0] || currentEdition;
    }

    function getActiveAgendasList() {
        // 사용자가 직접 '★ 중요 보존' 지정한 안건들도 롤업 뷰에 누락 없이 병합
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

    function init() {
        renderHeader();
        renderTierControls();
        syncCategoryTabs();
        renderAgendaList();
        bindEvents();
        fetchLiveQuotesOnOpen();
        setInterval(fetchLiveQuotesOnOpen, 60000); // 페이지가 열려 있는 동안 1분마다 실시간 갱신
    }

    async function fetchLiveQuotesOnOpen() {
        const statusEl = document.getElementById("live-quote-status");
        if (statusEl) {
            statusEl.textContent = "🔄 실시간 시세 동기화 중...";
        }

        const ed = getActiveEditionObj();
        const quotes = ed.marketQuotes || currentEdition.marketQuotes || [];
        const qMap = {};
        quotes.forEach(q => { qMap[q.id] = q; });

        const parseNum = (str) => {
            if (str === undefined || str === null) return NaN;
            return parseFloat(String(str).replace(/[,%+\s]/g, ""));
        };

        try {
            // 1. CNBC 실시간 글로벌 지표 API (미 10년물 금리, S&P500, 필라델피아 반도체, 금 선물 $/oz, 원/달러 환율)
            const cnbcUrl = "https://quote.cnbc.com/quote-html-webservice/restQuote/symbolType/symbol?symbols=US10Y%7C.SPX%7C.SOX%7C%40GC.1%7CKRW%3D&requestMethod=itv&noform=1&partnerId=2&fund=1&exthrs=1&output=json";
            const cnbcPromise = fetch(cnbcUrl, { cache: "no-store" })
                .then(r => r.json())
                .then(data => {
                    const list = (data && data.FormattedQuoteResult && data.FormattedQuoteResult.FormattedQuote) || [];
                    const symToId = {
                        "US10Y": "us10y",
                        ".SPX": "sp500",
                        ".SOX": "sox",
                        "@GC.1": "gold",
                        "KRW=": "usdkrw"
                    };
                    list.forEach(item => {
                        const targetId = symToId[item.symbol];
                        if (targetId && qMap[targetId]) {
                            const priceVal = parseNum(item.last);
                            const chgVal = parseNum(item.change_pct);
                            if (!isNaN(priceVal)) qMap[targetId].price = priceVal;
                            if (!isNaN(chgVal)) qMap[targetId].dayChangePct = chgVal;
                        }
                    });
                })
                .catch(() => {});

            // 2. 업비트(Upbit) 실시간 원화 비트코인 API (만원 단위 변환)
            const upbitUrl = "https://api.upbit.com/v1/ticker?markets=KRW-BTC";
            const btcPromise = fetch(upbitUrl, { cache: "no-store" })
                .then(r => r.json())
                .then(arr => {
                    if (Array.isArray(arr) && arr[0] && qMap["btc"]) {
                        const tradePrice = Number(arr[0].trade_price);
                        const chgRate = Number(arr[0].signed_change_rate) * 100.0;
                        if (tradePrice > 0) {
                            qMap["btc"].price = Math.round(tradePrice / 10000);
                            qMap["btc"].unit = "만원";
                        }
                        if (!isNaN(chgRate)) {
                            qMap["btc"].dayChangePct = chgRate;
                        }
                    }
                })
                .catch(() => {});

            await Promise.all([cnbcPromise, btcPromise]);
            renderHeader();

            const nowStr = new Date().toLocaleTimeString("ko-KR", { hour12: false });
            if (statusEl) {
                statusEl.textContent = `🟢 실시간 시세 연동됨 (페이지 열 때마다 자동 갱신 · ${nowStr} 기준)`;
            }
        } catch (err) {
            if (statusEl) {
                statusEl.textContent = "🟢 시세 표시 중 (브리핑 기준 시세)";
            }
        }
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
            execEl.innerHTML = `<span style="color:#0284c7;margin-right:8px;">[핵심 시사점 총평]</span>${ed.executiveHeadline || currentEdition.executiveHeadline || ""}`;
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

        const marketQuotes = ed.marketQuotes || currentEdition.marketQuotes || [];
        const coreIds = ["us10y", "sp500", "sox", "gold", "btc", "usdkrw"];
        const coreBar = document.getElementById("core-metrics-bar");
        if (coreBar && marketQuotes.length > 0) {
            const coreItems = coreIds.map(id => marketQuotes.find(m => m.id === id)).filter(Boolean);
            coreBar.innerHTML = coreItems.map(q => {
                const isUp = q.dayChangePct >= 0;
                const sign = isUp ? "+" : "";
                return `
                    <div class="core-metric-item">
                        <div class="core-metric-name">${q.name}</div>
                        <div class="core-metric-val">${formatPrice(q)}</div>
                        <div class="core-metric-chg ${isUp ? "up" : "down"}">${sign}${q.dayChangePct.toFixed(2)}%</div>
                    </div>
                `;
            }).join("");
        }
    }

    function renderTierControls() {
        // 각 탭 부제에 건수 표시
        const subDaily = document.getElementById("sub-daily7d");
        const subWeekly = document.getElementById("sub-weekly7d");
        const subMonthly = document.getElementById("sub-monthly30d");
        const subQuarterly = document.getElementById("sub-quarterly120d");

        if (subDaily) subDaily.textContent = `보관 에디션 ${recent7dEditions.length}회차 (회차당 25건 전체 보존)`;
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
                        🗓️ ${label} (열람 ${edReadCount}/${edAgendas.length}건)
                    </button>
                `;
            }).join("");

            subCtrl.innerHTML = `
                <div class="edition-history-bar">
                    <span style="font-size:14.5px;font-weight:800;color:var(--text-muted);margin-right:6px;">최근 7일 회차 선택 (최대 14회차 자동 누적):</span>
                    ${buttonsHtml}
                </div>
            `;
        } else if (state.tier === "weekly7d") {
            subCtrl.innerHTML = `
                <div class="rollup-info-banner">
                    📌 <strong>[7일 단위 최중요 브리핑 합산]</strong> 7일이 지나 일별 보관함에서 걸러지는 브리핑 중 중요도가 높은 핵심 안건(CRITICAL 및 시사점 전환·신규·강화)만 자동 추출하여 합산한 목록입니다.
                </div>
            `;
        } else if (state.tier === "monthly30d") {
            subCtrl.innerHTML = `
                <div class="rollup-info-banner">
                    🏆 <strong>[30일 단위 최중요 브리핑 합산]</strong> 7일 단위 중요 브리핑에 모인 안건들 중에서도 거시경제·반도체·금·비트코인·부동산의 구조적 추세를 바꾼 최상위 안건만 뽑아 남긴 월간 통합본입니다.
                </div>
            `;
        } else {
            subCtrl.innerHTML = `
                <div class="rollup-info-banner">
                    🏛️ <strong>[120일(1분기) 단위 최중요 브리핑 합산]</strong> 30일 단위 최중요 브리핑들을 하나로 모아 최근 1분기(120일) 동안의 핵심 시사점 변화를 한눈에 복기할 수 있는 분기 빅픽처 보관함입니다.
                </div>
            `;
        }
    }

    function syncCategoryTabs() {
        const activeAgendas = getActiveAgendasList();
        const counts = { all: activeAgendas.length, macro: 0, tech: 0, gold: 0, crypto: 0, realestate: 0 };
        activeAgendas.forEach(a => {
            counts[a.category] = (counts[a.category] || 0) + 1;
        });

        const labels = {
            all: `전체 안건 (${counts.all})`,
            macro: `🏛️ 거시경제 · 금리 (${counts.macro})`,
            tech: `🔬 반도체 · 빅테크 · 2나노 (${counts.tech})`,
            gold: `🥇 금($/oz) · 전망 (${counts.gold})`,
            crypto: `₿ 비트코인 95%+ (${counts.crypto})`,
            realestate: `🏢 한국 부동산 · 정책 (${counts.realestate})`
        };

        document.querySelectorAll(".tab-btn").forEach(btn => {
            const cat = btn.getAttribute("data-cat");
            if (labels[cat]) btn.textContent = labels[cat];
            btn.classList.toggle("active", cat === state.category);
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
        const refreshBtn = document.getElementById("btn-refresh-quotes");
        if (refreshBtn) {
            refreshBtn.addEventListener("click", () => {
                fetchLiveQuotesOnOpen();
            });
        }

        // 아카이브 티어 탭 전환
        document.querySelectorAll(".tier-tab-btn").forEach(btn => {
            btn.addEventListener("click", () => {
                state.tier = btn.getAttribute("data-tier") || "daily7d";
                renderHeader();
                renderTierControls();
                syncCategoryTabs();
                renderAgendaList();
            });
        });

        // 최근 7일 회차 선택 및 안건 클릭 시 즉시 열람 기록 위임 이벤트
        document.body.addEventListener("click", e => {
            const edBtn = e.target.closest("[data-select-edition]");
            if (edBtn) {
                state.selectedEditionId = edBtn.getAttribute("data-select-edition");
                renderHeader();
                renderTierControls();
                syncCategoryTabs();
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
                renderAgendaList();
            });
        });

        // 시사점 필터
        document.querySelectorAll(".delta-chip").forEach(chip => {
            chip.addEventListener("click", () => {
                document.querySelectorAll(".delta-chip").forEach(c => c.classList.remove("active"));
                chip.classList.add("active");
                state.deltaFilter = chip.getAttribute("data-delta") || "ALL";
                renderAgendaList();
            });
        });
    }

    document.addEventListener("DOMContentLoaded", init);
})();
