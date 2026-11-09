# -*- coding: utf-8 -*-
"""
고해상도 금융 차트 및 인포그래픽 SVG 이미지 생성기 (Large Typography & Clean Light Theme)
차트 내부의 모든 글자 크기를 크게 키우고 불필요한 복잡함을 줄여 한눈에 읽히도록 생성합니다.
"""
import os

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

COLOR_MAP_LIGHT = {
    "#38bdf8": "#0284c7",
    "#fbbf24": "#d97706",
    "#f59e0b": "#d97706",
    "#10b981": "#059669",
    "#f43f5e": "#e11d48",
    "#a855f7": "#7c3aed",
    "#8b5cf6": "#6d28d9",
    "#f97316": "#ea580c",
    "#22c55e": "#16a34a",
    "#06b6d4": "#0891b2",
    "#818cf8": "#4f46e5",
    "#64748b": "#475569",
}

def to_light_accent(c):
    return COLOR_MAP_LIGHT.get(c.lower(), c) if isinstance(c, str) else "#0284c7"

def create_line_chart_svg(filepath, title, subtitle, labels, values, unit="", color="#0284c7", fill_color="", benchmark_val=None, benchmark_label="", annotations=None, badge_text=""):
    """큰 글씨와 시원한 여백의 시계열 라인 차트 SVG 생성"""
    color = to_light_accent(color)
    w, h = 900, 480
    pad_l, pad_r, pad_t, pad_b = 95, 50, 105, 70
    plot_w = w - pad_l - pad_r
    plot_h = h - pad_t - pad_b

    min_v = min(values)
    max_v = max(values)
    if benchmark_val is not None:
        min_v = min(min_v, benchmark_val)
        max_v = max(max_v, benchmark_val)
    span = (max_v - min_v) if max_v != min_v else 1.0
    min_v -= span * 0.14
    max_v += span * 0.18
    span = max_v - min_v

    pts = []
    for i, v in enumerate(values):
        x = pad_l + (i / max(1, len(values) - 1)) * plot_w
        y = pad_t + plot_h - ((v - min_v) / span) * plot_h
        pts.append((x, y, v, labels[i] if i < len(labels) else ""))

    poly_points = " ".join(f"{x:.1f},{y:.1f}" for x, y, _, _ in pts)
    area_points = f"{pts[0][0]:.1f},{pad_t + plot_h:.1f} " + poly_points + f" {pts[-1][0]:.1f},{pad_t + plot_h:.1f}"

    grid_lines = []
    for i in range(5):
        gy = pad_t + (i / 4) * plot_h
        gv = max_v - (i / 4) * span
        val_str = f"{gv:,.2f}{unit}" if abs(gv) < 100 else f"{gv:,.0f}{unit}"
        grid_lines.append(f'<line x1="{pad_l}" y1="{gy:.1f}" x2="{w - pad_r}" y2="{gy:.1f}" stroke="#e2e8f0" stroke-width="1.5" stroke-dasharray="5,5"/>')
        grid_lines.append(f'<text x="{pad_l - 14}" y="{gy + 5:.1f}" fill="#334155" font-family="Pretendard, sans-serif" font-size="15" font-weight="700" text-anchor="end">{val_str}</text>')

    x_labels = []
    step = max(1, len(pts) // 6)
    for i in range(0, len(pts), step):
        x, y, v, lbl = pts[i]
        x_labels.append(f'<text x="{x:.1f}" y="{h - 24}" fill="#334155" font-family="Pretendard, sans-serif" font-size="15" font-weight="700" text-anchor="middle">{lbl}</text>')
    if (len(pts) - 1) % step != 0:
        x, y, v, lbl = pts[-1]
        x_labels.append(f'<text x="{x:.1f}" y="{h - 24}" fill="#0f172a" font-family="Pretendard, sans-serif" font-size="15" font-weight="900" text-anchor="middle">{lbl}</text>')

    bench_svg = ""
    if benchmark_val is not None:
        by = pad_t + plot_h - ((benchmark_val - min_v) / span) * plot_h
        bench_svg = f'''
        <line x1="{pad_l}" y1="{by:.1f}" x2="{w - pad_r}" y2="{by:.1f}" stroke="#e11d48" stroke-width="2.2" stroke-dasharray="7,5"/>
        <rect x="{w - pad_r - 220}" y="{by - 30:.1f}" width="215" height="28" rx="6" fill="#ffe4e6" stroke="#fda4af" stroke-width="1.2"/>
        <text x="{w - pad_r - 112}" y="{by - 11:.1f}" fill="#be123c" font-family="Pretendard, sans-serif" font-size="14" font-weight="800" text-anchor="middle">{benchmark_label}</text>
        '''

    dots_svg = []
    for i, (x, y, v, lbl) in enumerate(pts):
        if i == len(pts) - 1 or i == 0 or i == values.index(max(values)) or i == values.index(min(values)):
            r = 7.5 if i == len(pts) - 1 else 5.5
            dots_svg.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{color}" stroke="#ffffff" stroke-width="2.5"/>')
            if i == len(pts) - 1:
                v_str = f"{v:,.2f}{unit}" if abs(v) < 100 else f"{v:,.0f}{unit}"
                dots_svg.append(f'<rect x="{x - 82:.1f}" y="{y - 42:.1f}" width="96" height="30" rx="8" fill="{color}"/>')
                dots_svg.append(f'<text x="{x - 34:.1f}" y="{y - 22:.1f}" fill="#ffffff" font-family="Pretendard, sans-serif" font-size="15" font-weight="800" text-anchor="middle">{v_str}</text>')

    ann_svg = ""
    if annotations:
        for ann in annotations:
            idx = min(len(pts) - 1, max(0, ann.get("index", len(pts) // 2)))
            ax, ay, _, _ = pts[idx]
            text = ann.get("text", "")
            ann_svg += f'''
            <line x1="{ax:.1f}" y1="{ay:.1f}" x2="{ax:.1f}" y2="{ay - 44:.1f}" stroke="#d97706" stroke-width="2"/>
            <rect x="{ax - 115:.1f}" y="{ay - 74:.1f}" width="230" height="30" rx="7" fill="#fef3c7" stroke="#f59e0b" stroke-width="1.5"/>
            <text x="{ax:.1f}" y="{ay - 54:.1f}" fill="#92400e" font-family="Pretendard, sans-serif" font-size="14" font-weight="800" text-anchor="middle">{text}</text>
            '''

    badge_svg = ""
    if badge_text:
        badge_svg = f'''
        <rect x="{w - pad_r - 190}" y="22" width="190" height="34" rx="17" fill="#f0f9ff" stroke="{color}" stroke-width="1.8"/>
        <text x="{w - pad_r - 95}" y="44" fill="{color}" font-family="Pretendard, sans-serif" font-size="14.5" font-weight="800" text-anchor="middle">{badge_text}</text>
        '''

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
    <rect width="{w}" height="{h}" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="32" y="44" fill="#0f172a" font-family="Pretendard, sans-serif" font-size="22" font-weight="900">{title}</text>
    <text x="32" y="72" fill="#475569" font-family="Pretendard, sans-serif" font-size="15.5" font-weight="600">{subtitle}</text>
    {badge_svg}
    {"".join(grid_lines)}
    <polygon points="{area_points}" fill="{color}" fill-opacity="0.12"/>
    <polyline fill="none" stroke="{color}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round" points="{poly_points}"/>
    {bench_svg}
    {"".join(dots_svg)}
    {ann_svg}
    {"".join(x_labels)}
</svg>'''
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg)


def create_bar_comparison_svg(filepath, title, subtitle, categories, series_name_1, values_1, color_1, series_name_2=None, values_2=None, color_2="#d97706", unit="", badge_text=""):
    """큰 글씨의 막대 비교 차트 SVG 생성"""
    color_1 = to_light_accent(color_1)
    color_2 = to_light_accent(color_2)
    w, h = 900, 480
    pad_l, pad_r, pad_t, pad_b = 95, 50, 105, 72
    plot_w = w - pad_l - pad_r
    plot_h = h - pad_t - pad_b

    all_vals = list(values_1) + (list(values_2) if values_2 else [])
    min_v = min(0, min(all_vals))
    max_v = max(0, max(all_vals))
    if min_v < 0:
        min_v *= 1.2
    max_v *= 1.2
    span = (max_v - min_v) if max_v != min_v else 1.0

    zero_y = pad_t + plot_h - ((0 - min_v) / span) * plot_h

    grid_lines = []
    for i in range(5):
        gy = pad_t + (i / 4) * plot_h
        gv = max_v - (i / 4) * span
        val_str = f"{gv:,.1f}{unit}" if abs(gv) < 100 else f"{gv:,.0f}{unit}"
        grid_lines.append(f'<line x1="{pad_l}" y1="{gy:.1f}" x2="{w - pad_r}" y2="{gy:.1f}" stroke="#e2e8f0" stroke-width="1.5" stroke-dasharray="5,5"/>')
        grid_lines.append(f'<text x="{pad_l - 14}" y="{gy + 5:.1f}" fill="#334155" font-family="Pretendard, sans-serif" font-size="15" font-weight="700" text-anchor="end">{val_str}</text>')

    grid_lines.append(f'<line x1="{pad_l}" y1="{zero_y:.1f}" x2="{w - pad_r}" y2="{zero_y:.1f}" stroke="#64748b" stroke-width="2"/>')

    bars_svg = []
    n = len(categories)
    group_w = plot_w / max(1, n)
    bar_w = group_w * (0.34 if values_2 else 0.50)

    for i, cat in enumerate(categories):
        cx = pad_l + (i + 0.5) * group_w
        v1 = values_1[i]
        y1 = pad_t + plot_h - ((v1 - min_v) / span) * plot_h
        bh1 = abs(zero_y - y1)
        by1 = min(zero_y, y1)
        bx1 = cx - bar_w - 4 if values_2 else cx - bar_w / 2
        c1 = "#e11d48" if (v1 < 0 and not values_2) else color_1
        bars_svg.append(f'<rect x="{bx1:.1f}" y="{by1:.1f}" width="{bar_w:.1f}" height="{max(3, bh1):.1f}" rx="6" fill="{c1}"/>')
        v1_str = f"{v1:+.1f}{unit}" if min_v < 0 else (f"{v1:,.1f}{unit}" if abs(v1) < 100 else f"{v1:,.0f}{unit}")
        ty1 = by1 - 10 if v1 >= 0 else by1 + bh1 + 20
        bars_svg.append(f'<text x="{bx1 + bar_w/2:.1f}" y="{ty1:.1f}" fill="#0f172a" font-family="Pretendard, sans-serif" font-size="14.5" font-weight="800" text-anchor="middle">{v1_str}</text>')

        if values_2 and i < len(values_2):
            v2 = values_2[i]
            y2 = pad_t + plot_h - ((v2 - min_v) / span) * plot_h
            bh2 = abs(zero_y - y2)
            by2 = min(zero_y, y2)
            bx2 = cx + 4
            bars_svg.append(f'<rect x="{bx2:.1f}" y="{by2:.1f}" width="{bar_w:.1f}" height="{max(3, bh2):.1f}" rx="6" fill="{color_2}"/>')
            v2_str = f"{v2:,.1f}{unit}" if abs(v2) < 100 else f"{v2:,.0f}{unit}"
            ty2 = by2 - 10 if v2 >= 0 else by2 + bh2 + 20
            bars_svg.append(f'<text x="{bx2 + bar_w/2:.1f}" y="{ty2:.1f}" fill="{color_2}" font-family="Pretendard, sans-serif" font-size="14.5" font-weight="800" text-anchor="middle">{v2_str}</text>')

        bars_svg.append(f'<text x="{cx:.1f}" y="{h - 24}" fill="#0f172a" font-family="Pretendard, sans-serif" font-size="14.5" font-weight="800" text-anchor="middle">{cat}</text>')

    legend_svg = f'''
    <rect x="{w - pad_r - 290}" y="24" width="15" height="15" rx="3" fill="{color_1}"/>
    <text x="{w - pad_r - 268}" y="37" fill="#0f172a" font-family="Pretendard, sans-serif" font-size="14.5" font-weight="800">{series_name_1}</text>
    '''
    if values_2:
        legend_svg += f'''
        <rect x="{w - pad_r - 135}" y="24" width="15" height="15" rx="3" fill="{color_2}"/>
        <text x="{w - pad_r - 113}" y="37" fill="#0f172a" font-family="Pretendard, sans-serif" font-size="14.5" font-weight="800">{series_name_2}</text>
        '''

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
    <rect width="{w}" height="{h}" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="32" y="44" fill="#0f172a" font-family="Pretendard, sans-serif" font-size="22" font-weight="900">{title}</text>
    <text x="32" y="72" fill="#475569" font-family="Pretendard, sans-serif" font-size="15.5" font-weight="600">{subtitle}</text>
    {legend_svg}
    {"".join(grid_lines)}
    {"".join(bars_svg)}
</svg>'''
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg)


def create_infographic_matrix_svg(filepath, title, subtitle, nodes, center_label, badge_text="DEEP-DIVE"):
    """큰 글씨의 4분할 핵심 구조도 인포그래픽 SVG 생성"""
    w, h = 900, 480
    cx, cy = w // 2, h // 2 + 28

    node_elements = []
    lines = []
    positions = [
        (190, 175), (710, 175),
        (190, 365), (710, 365),
    ]
    for i, node in enumerate(nodes[:4]):
        nx, ny = positions[i]
        ncol = to_light_accent(node.get("color", "#0284c7"))
        lines.append(f'<line x1="{cx}" y1="{cy}" x2="{nx}" y2="{ny}" stroke="{ncol}" stroke-width="2.8" stroke-dasharray="6,5" opacity="0.7"/>')
        node_elements.append(f'''
        <g>
            <rect x="{nx - 150}" y="{ny - 50}" width="300" height="100" rx="12" fill="#f8fafc" stroke="{ncol}" stroke-width="2.4"/>
            <text x="{nx}" y="{ny - 18}" fill="{ncol}" font-family="Pretendard, sans-serif" font-size="16.5" font-weight="900" text-anchor="middle">{node.get("title","")}</text>
            <text x="{nx}" y="{ny + 9}" fill="#0f172a" font-family="Pretendard, sans-serif" font-size="15.5" font-weight="800" text-anchor="middle">{node.get("metric","")}</text>
            <text x="{nx}" y="{ny + 33}" fill="#475569" font-family="Pretendard, sans-serif" font-size="13.5" font-weight="600" text-anchor="middle">{node.get("desc","")}</text>
        </g>
        ''')

    center_svg = f'''
    <circle cx="{cx}" cy="{cy}" r="82" fill="#eff6ff" stroke="#0284c7" stroke-width="3.5"/>
    <circle cx="{cx}" cy="{cy}" r="72" fill="#ffffff" stroke="#bae6fd" stroke-width="1.5"/>
    <text x="{cx}" y="{cy - 6}" fill="#0284c7" font-family="Pretendard, sans-serif" font-size="15.5" font-weight="900" text-anchor="middle">{center_label[0]}</text>
    <text x="{cx}" y="{cy + 18}" fill="#0f172a" font-family="Pretendard, sans-serif" font-size="14.5" font-weight="800" text-anchor="middle">{center_label[1]}</text>
    '''

    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="100%" height="100%">
    <rect width="{w}" height="{h}" rx="14" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5"/>
    <text x="32" y="44" fill="#0f172a" font-family="Pretendard, sans-serif" font-size="22" font-weight="900">{title}</text>
    <text x="32" y="72" fill="#475569" font-family="Pretendard, sans-serif" font-size="15.5" font-weight="600">{subtitle}</text>
    {"".join(lines)}
    {center_svg}
    {"".join(node_elements)}
</svg>'''
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(svg)
