// ==========================================================================
// 데일리 브리핑 안건 상세 페이지 스크립트 (detail.js)
// - 최근 7일 회차 및 7일 / 30일 / 120일 합산 보관함과 완벽 연동
// - 그림자 없는 깔끔한 플랫 디자인 + 큰 글씨 시사점 및 대형 차트 제공
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
    const tierParam = params.get("tier") || "daily7d";
    const editionParam = params.get("edition") || currentEdition.editionId || "";
    const catParam = params.get("cat") || "all";
    const agendaId = params.get("id") || "";

    const READ_STORAGE_KEY = "briefing_read_map_v2";

    function loadJson(key, fallback) {
        try {
            const raw = localStorage.getItem(key);
            return raw ? JSON.parse(raw) : fallback;
        } catch (e) {
            return fallback;
        }
    }

    function saveJson(key, val) {
        try {
            localStorage.setItem(key, JSON.stringify(val));
        } catch (e) {}
    }

    function getCurrentScopeId() {
        if (tierParam === "daily7d") {
            const foundEd = recent7dEditions.find(e => e.editionId === editionParam) || recent7dEditions[0] || currentEdition;
            return foundEd.editionId || editionParam || currentEdition.editionId || "default";
        }
        return tierParam;
    }

    function markAsRead(id) {
        const merged = {};
        try {
            const rawLocal = localStorage.getItem(READ_STORAGE_KEY);
            if (rawLocal) Object.assign(merged, JSON.parse(rawLocal));
        } catch (e) {}
        try {
            if (window.name && window.name.startsWith("BRIEFING_STATE:")) {
                const parsed = JSON.parse(window.name.slice("BRIEFING_STATE:".length));
                if (parsed && parsed.readMap) Object.assign(merged, parsed.readMap);
            }
        } catch (e) {}

        const scopeId = getCurrentScopeId();
        merged[`${scopeId}::${id}`] = true;

        try {
            localStorage.setItem(READ_STORAGE_KEY, JSON.stringify(merged));
        } catch (e) {}
        try {
            window.name = "BRIEFING_STATE:" + JSON.stringify({ readMap: merged });
        } catch (e) {}
    }

    function getActiveAgendasList() {
        if (tierParam === "weekly7d") return weeklyRollup.agendas || currentEdition.agendas || [];
        if (tierParam === "monthly30d") return monthlyRollup.agendas || currentEdition.agendas || [];
        if (tierParam === "quarterly120d") return quarterlyRollup.agendas || currentEdition.agendas || [];
        const foundEd = recent7dEditions.find(e => e.editionId === editionParam) || recent7dEditions[0] || currentEdition;
        return foundEd.agendas || [];
    }

    function buildBackUrl() {
        const q = new URLSearchParams();
        if (tierParam) q.set("tier", tierParam);
        if (editionParam) q.set("edition", editionParam);
        if (catParam && catParam !== "all") q.set("cat", catParam);
        const qs = q.toString();
        return qs ? `index.html?${qs}` : "index.html";
    }

    function buildDetailUrl(targetId) {
        const q = new URLSearchParams();
        q.set("id", targetId);
        if (tierParam) q.set("tier", tierParam);
        if (editionParam) q.set("edition", editionParam);
        if (catParam) q.set("cat", catParam);
        return `detail.html?${q.toString()}`;
    }

    function init() {
        const backUrl = buildBackUrl();
        const backTop = document.getElementById("btn-back-list");
        const backBottom = document.getElementById("btn-back-list-bottom");
        if (backTop) backTop.href = backUrl;
        if (backBottom) backBottom.href = backUrl;

        const agendas = getActiveAgendasList();
        let currentIndex = agendas.findIndex(a => a.id === agendaId);
        let ag = currentIndex >= 0 ? agendas[currentIndex] : null;

        if (!ag && (currentEdition.agendas || []).length > 0) {
            ag = currentEdition.agendas.find(a => a.id === agendaId) || currentEdition.agendas[0];
            currentIndex = 0;
        }

        if (!ag) {
            const container = document.getElementById("detail-article-container");
            if (container) container.innerHTML = `<p>안건 정보를 찾을 수 없습니다.</p>`;
            return;
        }

        document.title = `${ag.title} — 데일리 브리핑`;
        markAsRead(ag.id);

        renderArticle(ag, currentIndex, agendas);
        renderPrevNext(currentIndex, agendas);
        window.scrollTo(0, 0);
    }

    function renderArticle(ag, idx, agendas) {
        const container = document.getElementById("detail-article-container");
        if (!container) return;

        const pinnedMap = loadJson("briefing_pinned_map_v1", {});
        const isPinned = !!pinnedMap[ag.id];

        const metricsHtml = (ag.keyMetrics || []).map(m => `
            <div class="detail-metric-box">
                <div class="detail-metric-label">${m.label}</div>
                <div class="detail-metric-val">${m.value}</div>
                <div class="detail-metric-chg">${m.change}</div>
            </div>
        `).join("");

        const paragraphsHtml = (ag.facts || []).map(p => `<p>${p}</p>`).join("");

        const timelineHtml = (ag.implicationHistory || []).map(t => `
            <div class="detail-timeline-card">
                <div style="font-size:15px;font-weight:900;color:#0284c7;margin-bottom:6px;">${t.time}</div>
                <div style="font-size:18px;font-weight:700;color:#0f172a;line-height:1.55;">${t.text}</div>
            </div>
        `).join("");

        const tierBadge = ag.archiveTier ? `<span class="badge-tier">🗂️ ${ag.archiveTier}</span>` : "";

        container.innerHTML = `
            <div class="card-top-badges">
                <div style="display:flex;align-items:center;gap:8px;flex-wrap:wrap;">
                    <span class="badge-cat ${ag.category}">안건 #${idx + 1} / ${agendas.length} · ${ag.categoryLabel}</span>
                    ${tierBadge}
                </div>
                <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;">
                    <button id="btn-pin-archive" class="back-btn" style="padding:6px 14px;font-size:14.5px;${isPinned ? 'background:#fef3c7;border-color:#f59e0b;color:#92400e;' : ''}">
                        ${isPinned ? "★ 7·30·120일 합산 영구보존 지정됨" : "☆ 7·30·120일 중요 브리핑에 보존하기"}
                    </button>
                    <span class="badge-delta ${ag.deltaStatus}">${ag.deltaLabel}</span>
                </div>
            </div>

            <h1 class="detail-title">${ag.title}</h1>
            <p class="detail-subtitle">${ag.subtitle}</p>

            <!-- 1. 가장 중요한 시사점 변화 특대형 섹션 -->
            <section class="detail-implication-hero">
                <div class="detail-imp-heading">🧭 핵심 시사점 및 투자 판단 변화 (Implication Delta)</div>

                <div class="detail-imp-step updated">
                    <div class="detail-imp-label" style="color:#b45309;">🔥 변화된 시사점 & 현재 투자 결론</div>
                    <div class="detail-imp-text">${ag.updatedImplication}</div>
                </div>

                <div class="detail-imp-step">
                    <div class="detail-imp-label" style="color:#0284c7;">⚡ 최근 12시간 신규 발생 모멘텀 (Catalyst)</div>
                    <div class="detail-imp-text" style="font-weight:700;">${ag.newCatalyst}</div>
                </div>

                <div class="detail-imp-step" style="margin-bottom:0;">
                    <div class="detail-imp-label" style="color:#64748b;">⏮️ 기존 시사점 (이전 시장 내러티브)</div>
                    <div class="detail-imp-text" style="color:#475569;">${ag.previousImplication}</div>
                </div>
            </section>

            <!-- 2. 대형 차트 & 인포그래픽 이미지 -->
            <div class="detail-chart-frame">
                <img src="${ag.chartImage}" alt="${ag.title}" />
            </div>

            <!-- 3. 핵심 지표 3단 -->
            <div class="detail-metrics-grid">
                ${metricsHtml}
            </div>

            <!-- 4. 상세 배경 및 신규 팩트 리포트 -->
            <h2 class="detail-section-title">📰 상세 배경 및 신규 팩트 브리핑</h2>
            <div class="detail-body-paragraphs">
                ${paragraphsHtml}
            </div>

            <!-- 5. 시사점 변화 타임라인 -->
            <h2 class="detail-section-title">⏱️ 시사점 변화 흐름 (Timeline)</h2>
            <div class="detail-timeline-grid">
                ${timelineHtml}
            </div>

            <!-- 6. 투자 액션 포인트 -->
            <div class="detail-action-box">
                <div style="font-size:20px;font-weight:900;color:#047857;margin-bottom:12px;">💡 포트폴리오 대응 및 투자 액션 포인트</div>
                <ul class="detail-action-list">
                    ${(ag.actionPoints || []).map(pt => `<li>${pt}</li>`).join("")}
                </ul>
            </div>

            <div style="margin-top:28px;padding-top:18px;border-top:1px solid var(--border-light);font-size:16px;color:var(--text-muted);font-weight:700;">
                📌 신뢰 출처 및 데이터 레퍼런스: ${(ag.sources || []).join(" · ")}
            </div>
        `;

        const pinBtn = document.getElementById("btn-pin-archive");
        if (pinBtn) {
            pinBtn.addEventListener("click", () => {
                const map = loadJson("briefing_pinned_map_v1", {});
                map[ag.id] = !map[ag.id];
                saveJson("briefing_pinned_map_v1", map);
                renderArticle(ag, idx, agendas);
            });
        }
    }

    function renderPrevNext(idx, agendas) {
        const prevAg = idx > 0 ? agendas[idx - 1] : null;
        const nextAg = idx < agendas.length - 1 ? agendas[idx + 1] : null;

        const topNav = document.getElementById("top-prev-next");
        if (topNav) {
            topNav.innerHTML = `
                ${prevAg ? `<a class="back-btn" href="${buildDetailUrl(prevAg.id)}">◀ 이전 안건 (#${idx})</a>` : ""}
                ${nextAg ? `<a class="back-btn" href="${buildDetailUrl(nextAg.id)}">다음 안건 (#${idx + 2}) ▶</a>` : ""}
            `;
        }

        const bottomNav = document.getElementById("bottom-prev-next");
        if (bottomNav) {
            bottomNav.innerHTML = `
                ${prevAg ? `
                    <a class="prev-next-card" href="${buildDetailUrl(prevAg.id)}">
                        <div style="font-size:14px;font-weight:800;color:var(--text-muted);margin-bottom:6px;">◀ 이전 안건 (#${idx})</div>
                        <div style="font-size:19px;font-weight:800;color:#0f172a;line-height:1.4;">${prevAg.title}</div>
                    </a>
                ` : `<div></div>`}
                ${nextAg ? `
                    <a class="prev-next-card" href="${buildDetailUrl(nextAg.id)}" style="text-align:right;">
                        <div style="font-size:14px;font-weight:800;color:var(--text-muted);margin-bottom:6px;">다음 안건 (#${idx + 2}) ▶</div>
                        <div style="font-size:19px;font-weight:800;color:#0f172a;line-height:1.4;">${nextAg.title}</div>
                    </a>
                ` : `<div></div>`}
            `;
        }
    }

    document.addEventListener("DOMContentLoaded", init);
})();
