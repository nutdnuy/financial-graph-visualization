#!/usr/bin/env python3
"""Generate deterministic SVG cards for the visual chapter catalog."""

from __future__ import annotations

import argparse
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "assets" / "catalog"
THEMES = {
    "dark": {
        "background": "#121212",
        "surface": "#1E1E1E",
        "outline": "#FFFFFF",
        "primary": "#BB86FC",
        "secondary": "#03DAC6",
        "error": "#CF6679",
        "text": "#FFFFFF",
        "border_opacity": ".15",
    },
    "light": {
        "background": "#FFFFFF",
        "surface": "#FFFFFF",
        "outline": "#000000",
        "primary": "#6200EE",
        "secondary": "#03DAC6",
        "error": "#B00020",
        "text": "#000000",
        "border_opacity": ".15",
    },
}

ITEMS = [
    ("ch01", "Financial Visual Communications", "audience, narrative, perspectives", "FINANCIAL"),
    ("ch02", "Benefits of Visual Methods", "compare, connect, conclude", "FINANCIAL"),
    ("ch03", "Security Assessment", "Tile Framework, normalized comparison", "FINANCIAL"),
    ("ch04", "Portfolio Construction", "singular, multifaceted, varied views", "FINANCIAL"),
    ("ch05", "Trading Visual System", "Contrail, ticker, quote, watchlist", "FINANCIAL"),
    ("ch06", "Performance Measurement", "attribution, grids, linked views", "FINANCIAL"),
    ("ch07", "Financial Statements", "waterfall, cascade, transparency", "FINANCIAL"),
    ("ch08", "Pension Funds", "demographic and funding context", "FINANCIAL"),
    ("ch09", "Mutual Funds", "components and benchmark context", "FINANCIAL"),
    ("ch10", "Hedge Funds", "glyphs, ranking, information seeking", "FINANCIAL"),
    ("ch11", "Visualization Principles", "audience, clarity, efficiency", "FINANCIAL"),
    ("ch12", "Implementing Financial Visuals", "business value, complexity, score", "FINANCIAL"),
    ("ch13", "Graph Visualization Basics", "model, explore, communicate", "GRAPH"),
    ("ch14", "Graph Case Studies", "fraud, intelligence, cyber, marketing", "GRAPH"),
    ("ch15", "Gephi and KeyLines", "tool-selection trade-offs", "GRAPH"),
    ("ch16", "Graph Data Modeling", "nodes, links, properties, databases", "GRAPH"),
    ("ch17", "Building Graph Visualizations", "encoding and audience calibration", "GRAPH"),
    ("ch18", "Interactive Graph Visualizations", "navigation and details on demand", "GRAPH"),
    ("ch19", "Graph Layouts", "force, hierarchy, radial, circular", "GRAPH"),
    ("ch20", "Big Graph Data", "filtering, grouping, scalability", "GRAPH"),
    ("ch21", "Dynamic Graphs", "small multiples and time bars", "GRAPH"),
    ("ch22", "Graphs on Maps", "geography, filtering, overlays", "GRAPH"),
    ("ch23", "D3.js Appendix", "selectors, SVG, data binding", "APPENDIX"),
    ("example-portfolio-tile", "Portfolio Comparison Tiles", "normalized bands and benchmarks", "EXAMPLE"),
    ("example-performance-waterfall", "Performance Waterfall", "ordered cumulative decomposition", "EXAMPLE"),
    ("example-transaction-network", "Transaction Network", "fixed geometry and typed links", "EXAMPLE"),
]


def wrap(text: str, width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    line = ""
    for word in words:
        candidate = f"{line} {word}".strip()
        if line and len(candidate) > width:
            lines.append(line)
            line = word
        else:
            line = candidate
    if line:
        lines.append(line)
    return lines[:3]


def visual(slug: str, colors: dict[str, str]) -> str:
    """Return one content-specific, deterministic visual motif per card."""
    p = colors["primary"]
    s = colors["secondary"]
    e = colors["error"]
    t = colors["text"]
    bg = colors["background"]

    if slug == "ch01":
        return f'''<g fill="none" stroke-linecap="round" stroke-linejoin="round">
  <rect x="72" y="112" width="118" height="82" rx="8" stroke="{p}" stroke-width="3" opacity=".75"/>
  <rect x="94" y="155" width="18" height="24" rx="3" fill="{p}" stroke="none"/><rect x="122" y="140" width="18" height="39" rx="3" fill="{s}" stroke="none"/><rect x="150" y="126" width="18" height="53" rx="3" fill="{p}" stroke="none"/>
  <path d="M190 153 H244 M232 143 L244 153 L232 163" stroke="{t}" stroke-opacity=".45" stroke-width="3"/>
  <rect x="252" y="112" width="136" height="82" rx="8" stroke="{s}" stroke-width="3" opacity=".75"/><path d="M270 170 L296 146 L326 158 L354 126 L374 138" stroke="{s}" stroke-width="5"/>
  <path d="M388 153 H442 M430 143 L442 153 L430 163" stroke="{t}" stroke-opacity=".45" stroke-width="3"/>
  <rect x="450" y="112" width="118" height="82" rx="8" stroke="{p}" stroke-width="3" opacity=".75"/><line x1="478" y1="168" x2="516" y2="132" stroke="{s}" stroke-width="4"/><line x1="516" y1="132" x2="544" y2="166" stroke="{p}" stroke-width="4"/><circle cx="478" cy="168" r="9" fill="{s}" stroke="{bg}" stroke-width="3"/><circle cx="516" cy="132" r="12" fill="{p}" stroke="{bg}" stroke-width="3"/><circle cx="544" cy="166" r="8" fill="{s}" stroke="{bg}" stroke-width="3"/>
</g>'''
    if slug == "ch02":
        return f'''<g stroke-linecap="round" stroke-linejoin="round">
  <line x1="92" y1="190" x2="92" y2="118" stroke="{t}" stroke-opacity=".25" stroke-width="3"/><rect x="106" y="154" width="24" height="36" rx="3" fill="{p}"/><rect x="142" y="132" width="24" height="58" rx="3" fill="{s}"/>
  <path d="M188 154 H238 M226 144 L238 154 L226 164" fill="none" stroke="{t}" stroke-opacity=".4" stroke-width="3"/>
  <line x1="268" y1="130" x2="318" y2="174" stroke="{s}" stroke-width="4"/><line x1="318" y1="174" x2="366" y2="126" stroke="{p}" stroke-width="4"/><circle cx="268" cy="130" r="12" fill="{s}"/><circle cx="318" cy="174" r="10" fill="{p}"/><circle cx="366" cy="126" r="14" fill="{s}"/>
  <path d="M392 154 H440 M428 144 L440 154 L428 164" fill="none" stroke="{t}" stroke-opacity=".4" stroke-width="3"/>
  <circle cx="502" cy="152" r="42" fill="none" stroke="{p}" stroke-width="6"/><path d="M480 153 L496 169 L526 132" fill="none" stroke="{s}" stroke-width="8"/>
</g>'''
    if slug == "ch03":
        tiles = []
        widths = (74, 46, 92, 58, 82, 66)
        for i, width in enumerate(widths):
            x = 76 + (i % 3) * 172
            y = 112 + (i // 3) * 52
            color = p if i % 2 == 0 else s
            tiles.append(f'<rect x="{x}" y="{y}" width="144" height="38" rx="7" fill="{t}" fill-opacity=".06" stroke="{t}" stroke-opacity=".18"/><rect x="{x + 10}" y="{y + 12}" width="{width}" height="14" rx="7" fill="{color}"/><circle cx="{x + 125}" cy="{y + 19}" r="7" fill="{color}"/>')
        return "".join(tiles)
    if slug == "ch04":
        return f'''<g fill="none" stroke-linecap="round" stroke-linejoin="round">
  <line x1="86" y1="200" x2="552" y2="200" stroke="{t}" stroke-opacity=".28" stroke-width="3"/><line x1="86" y1="200" x2="86" y2="112" stroke="{t}" stroke-opacity=".28" stroke-width="3"/>
  <path d="M112 186 C210 186 280 170 344 146 C412 121 478 111 544 112" stroke="{s}" stroke-width="5"/>
  <circle cx="148" cy="182" r="9" fill="{p}"/><circle cx="236" cy="169" r="13" fill="{s}"/><circle cx="328" cy="151" r="10" fill="{p}"/><circle cx="424" cy="124" r="15" fill="{s}"/><circle cx="518" cy="113" r="11" fill="{p}"/>
  <path d="M296 200 L344 146 L392 200 Z" fill="{p}" fill-opacity=".12" stroke="{p}" stroke-dasharray="6 6" stroke-width="3"/>
</g>'''
    if slug == "ch05":
        candles = []
        data = [(112, 132, 178, 148, p), (174, 118, 168, 130, s), (236, 142, 198, 162, e), (298, 108, 166, 124, s), (360, 126, 184, 144, p), (422, 116, 154, 130, s), (484, 136, 194, 158, e)]
        for x, high, low, body, color in data:
            candles.append(f'<line x1="{x}" y1="{high}" x2="{x}" y2="{low}" stroke="{color}" stroke-width="4"/><rect x="{x - 12}" y="{body}" width="24" height="24" rx="3" fill="{color}"/>')
        candles.append(f'<path d="M84 178 L150 160 L212 170 L278 134 L344 146 L410 126 L516 142" fill="none" stroke="{t}" stroke-opacity=".5" stroke-width="3"/>')
        return "".join(candles)
    if slug == "ch06":
        return f'''<g stroke-linejoin="round">
  <rect x="78" y="132" width="58" height="70" rx="5" fill="{p}"/><line x1="136" y1="132" x2="170" y2="132" stroke="{t}" stroke-opacity=".35" stroke-dasharray="5 5" stroke-width="3"/>
  <rect x="170" y="112" width="58" height="20" rx="4" fill="{s}"/><line x1="228" y1="112" x2="262" y2="112" stroke="{t}" stroke-opacity=".35" stroke-dasharray="5 5" stroke-width="3"/>
  <rect x="262" y="112" width="58" height="34" rx="4" fill="{e}"/><line x1="320" y1="146" x2="354" y2="146" stroke="{t}" stroke-opacity=".35" stroke-dasharray="5 5" stroke-width="3"/>
  <rect x="354" y="122" width="58" height="24" rx="4" fill="{s}"/><line x1="412" y1="122" x2="446" y2="122" stroke="{t}" stroke-opacity=".35" stroke-dasharray="5 5" stroke-width="3"/>
  <rect x="446" y="122" width="72" height="80" rx="5" fill="{p}"/>
</g>'''
    if slug == "ch07":
        return f'''<g stroke-linecap="round" stroke-linejoin="round">
  <rect x="78" y="112" width="84" height="36" rx="5" fill="{p}"/><rect x="78" y="152" width="84" height="26" rx="5" fill="{s}"/><rect x="78" y="182" width="84" height="24" rx="5" fill="{t}" fill-opacity=".18"/>
  <rect x="232" y="120" width="84" height="50" rx="5" fill="{s}"/><rect x="232" y="174" width="84" height="32" rx="5" fill="{e}"/>
  <path d="M162 130 C220 130 190 138 232 138 M162 165 C206 165 202 186 232 190 M316 145 C382 145 382 132 446 132 M316 190 C380 190 390 182 446 182" fill="none" stroke="{t}" stroke-opacity=".35" stroke-width="4"/>
  <rect x="446" y="112" width="92" height="94" rx="6" fill="none" stroke="{p}" stroke-width="5"/><line x1="458" y1="154" x2="526" y2="154" stroke="{t}" stroke-opacity=".3" stroke-width="3"/>
</g>'''
    if slug == "ch08":
        parts = [f'<line x1="320" y1="108" x2="320" y2="208" stroke="{t}" stroke-opacity=".3" stroke-width="3"/>']
        for i, (left, right) in enumerate(((74, 98), (112, 82), (142, 62), (94, 48))):
            y = 116 + i * 24
            parts.append(f'<rect x="{320-left}" y="{y}" width="{left}" height="14" rx="7" fill="{p}"/><rect x="320" y="{y}" width="{right}" height="14" rx="7" fill="{s}"/>')
        parts.append(f'<path d="M474 198 A44 44 0 0 1 562 198" fill="none" stroke="{t}" stroke-opacity=".2" stroke-width="12"/><path d="M474 198 A44 44 0 0 1 544 162" fill="none" stroke="{s}" stroke-width="12"/><line x1="518" y1="198" x2="542" y2="170" stroke="{p}" stroke-width="5" stroke-linecap="round"/>')
        return "".join(parts)
    if slug == "ch09":
        return f'''<g stroke-linecap="round" stroke-linejoin="round">
  <rect x="82" y="112" width="470" height="24" rx="4" fill="{p}" fill-opacity=".10"/><rect x="82" y="136" width="470" height="24" rx="4" fill="{s}" fill-opacity=".12"/><rect x="82" y="160" width="470" height="24" rx="4" fill="{p}" fill-opacity=".10"/><rect x="82" y="184" width="470" height="24" rx="4" fill="{s}" fill-opacity=".12"/>
  <line x1="82" y1="158" x2="552" y2="158" stroke="{t}" stroke-opacity=".38" stroke-width="3" stroke-dasharray="8 7"/>
  <path d="M92 188 L154 174 L218 180 L282 147 L346 156 L410 126 L474 138 L542 116" fill="none" stroke="{p}" stroke-width="6"/><circle cx="282" cy="147" r="8" fill="{s}"/><circle cx="410" cy="126" r="8" fill="{s}"/>
</g>'''
    if slug == "ch10":
        return f'''<g fill="none" stroke-linejoin="round">
  <circle cx="148" cy="158" r="48" stroke="{t}" stroke-opacity=".2"/><polygon points="148,116 178,148 166,190 124,184 112,142" fill="{p}" fill-opacity=".22" stroke="{p}" stroke-width="4"/>
  <circle cx="320" cy="158" r="48" stroke="{t}" stroke-opacity=".2"/><polygon points="320,110 356,142 342,184 304,198 280,148" fill="{s}" fill-opacity=".22" stroke="{s}" stroke-width="4"/>
  <circle cx="492" cy="158" r="48" stroke="{t}" stroke-opacity=".2"/><polygon points="492,124 528,132 536,174 504,202 460,180 454,142" fill="{e}" fill-opacity=".18" stroke="{e}" stroke-width="4"/>
</g>'''
    if slug == "ch11":
        return f'''<g stroke-linecap="round" stroke-linejoin="round">
  <rect x="72" y="110" width="206" height="100" rx="8" fill="{t}" fill-opacity=".04" stroke="{t}" stroke-opacity=".18"/><path d="M86 126 H264 M86 146 H264 M86 166 H264 M86 186 H264" stroke="{t}" stroke-opacity=".18" stroke-width="2"/><rect x="96" y="142" width="22" height="56" fill="{e}"/><rect x="128" y="122" width="22" height="76" fill="{s}"/><rect x="160" y="154" width="22" height="44" fill="{p}"/><path d="M90 172 L136 134 L184 162 L254 124" fill="none" stroke="{p}" stroke-width="3"/>
  <path d="M290 160 H340 M328 150 L340 160 L328 170" fill="none" stroke="{t}" stroke-opacity=".4" stroke-width="3"/>
  <rect x="356" y="110" width="206" height="100" rx="8" fill="{t}" fill-opacity=".04" stroke="{t}" stroke-opacity=".18"/><line x1="378" y1="190" x2="540" y2="190" stroke="{t}" stroke-opacity=".25" stroke-width="3"/><rect x="404" y="154" width="42" height="36" rx="4" fill="{t}" fill-opacity=".18"/><rect x="472" y="126" width="42" height="64" rx="4" fill="{p}"/><circle cx="493" cy="126" r="9" fill="{s}"/>
</g>'''
    if slug == "ch12":
        return f'''<g stroke-linecap="round" stroke-linejoin="round">
  <rect x="88" y="108" width="464" height="104" rx="8" fill="{t}" fill-opacity=".04" stroke="{t}" stroke-opacity=".18"/><line x1="320" y1="108" x2="320" y2="212" stroke="{t}" stroke-opacity=".25" stroke-width="3"/><line x1="88" y1="160" x2="552" y2="160" stroke="{t}" stroke-opacity=".25" stroke-width="3"/>
  <circle cx="162" cy="182" r="9" fill="{t}" fill-opacity=".35"/><circle cx="252" cy="132" r="12" fill="{s}"/><circle cx="382" cy="184" r="11" fill="{e}"/><circle cx="454" cy="128" r="17" fill="{p}"/><circle cx="454" cy="128" r="26" fill="none" stroke="{s}" stroke-width="4" stroke-dasharray="6 5"/><circle cx="510" cy="146" r="8" fill="{p}"/>
</g>'''
    if slug == "ch13":
        return f'''<g stroke-linecap="round">
  <line x1="112" y1="166" x2="214" y2="126" stroke="{s}" stroke-width="5"/><line x1="214" y1="126" x2="322" y2="180" stroke="{p}" stroke-width="4"/><line x1="214" y1="126" x2="392" y2="118" stroke="{s}" stroke-width="3"/><line x1="322" y1="180" x2="500" y2="150" stroke="{p}" stroke-width="6"/><line x1="392" y1="118" x2="500" y2="150" stroke="{s}" stroke-width="4"/>
  <circle cx="112" cy="166" r="18" fill="{p}" stroke="{bg}" stroke-width="5"/><circle cx="214" cy="126" r="25" fill="{s}" stroke="{bg}" stroke-width="5"/><circle cx="322" cy="180" r="16" fill="{p}" stroke="{bg}" stroke-width="5"/><circle cx="392" cy="118" r="20" fill="{p}" stroke="{bg}" stroke-width="5"/><circle cx="500" cy="150" r="14" fill="{s}" stroke="{bg}" stroke-width="5"/>
</g>'''
    if slug == "ch14":
        return f'''<g stroke-linecap="round">
  <path d="M108 136 L152 116 L184 150 L138 180 Z M292 126 L336 112 L370 148 L316 176 Z M454 146 L496 116 L538 154 L494 190 Z" fill="none" stroke="{t}" stroke-opacity=".25" stroke-width="3"/>
  <line x1="184" y1="150" x2="292" y2="126" stroke="{p}" stroke-width="3" stroke-dasharray="7 6"/><line x1="370" y1="148" x2="454" y2="146" stroke="{s}" stroke-width="4"/>
  <circle cx="108" cy="136" r="13" fill="{p}"/><circle cx="152" cy="116" r="17" fill="{p}"/><circle cx="184" cy="150" r="11" fill="{p}"/><circle cx="138" cy="180" r="14" fill="{p}"/>
  <circle cx="292" cy="126" r="12" fill="{s}"/><circle cx="336" cy="112" r="18" fill="{s}"/><circle cx="370" cy="148" r="13" fill="{s}"/><circle cx="316" cy="176" r="15" fill="{s}"/>
  <circle cx="454" cy="146" r="12" fill="{e}"/><circle cx="496" cy="116" r="17" fill="{e}"/><circle cx="538" cy="154" r="11" fill="{e}"/><circle cx="494" cy="190" r="14" fill="{e}"/>
</g>'''
    if slug == "ch15":
        return f'''<g stroke-linecap="round" stroke-linejoin="round">
  <rect x="70" y="108" width="222" height="104" rx="8" fill="{t}" fill-opacity=".04" stroke="{t}" stroke-opacity=".18"/><line x1="112" y1="170" x2="164" y2="126" stroke="{s}" stroke-width="3"/><line x1="164" y1="126" x2="232" y2="166" stroke="{p}" stroke-width="4"/><line x1="112" y1="170" x2="232" y2="166" stroke="{t}" stroke-opacity=".3" stroke-width="3"/><circle cx="112" cy="170" r="13" fill="{p}"/><circle cx="164" cy="126" r="18" fill="{s}"/><circle cx="232" cy="166" r="14" fill="{p}"/>
  <rect x="348" y="108" width="222" height="104" rx="8" fill="{t}" fill-opacity=".04" stroke="{t}" stroke-opacity=".18"/><line x1="458" y1="124" x2="404" y2="158" stroke="{s}" stroke-width="4"/><line x1="458" y1="124" x2="512" y2="158" stroke="{s}" stroke-width="4"/><line x1="404" y1="158" x2="382" y2="192" stroke="{p}" stroke-width="3"/><line x1="404" y1="158" x2="430" y2="192" stroke="{p}" stroke-width="3"/><line x1="512" y1="158" x2="538" y2="192" stroke="{p}" stroke-width="3"/><circle cx="458" cy="124" r="15" fill="{s}"/><circle cx="404" cy="158" r="12" fill="{p}"/><circle cx="512" cy="158" r="12" fill="{p}"/><circle cx="382" cy="192" r="9" fill="{s}"/><circle cx="430" cy="192" r="9" fill="{s}"/><circle cx="538" cy="192" r="9" fill="{s}"/>
</g>'''
    if slug == "ch16":
        return f'''<g stroke-linecap="round" stroke-linejoin="round">
  <rect x="74" y="126" width="112" height="58" rx="10" fill="{p}" fill-opacity=".16" stroke="{p}" stroke-width="4"/><circle cx="100" cy="155" r="10" fill="{p}"/><line x1="120" y1="146" x2="166" y2="146" stroke="{t}" stroke-opacity=".35" stroke-width="3"/><line x1="120" y1="163" x2="154" y2="163" stroke="{t}" stroke-opacity=".25" stroke-width="3"/>
  <rect x="264" y="112" width="112" height="86" rx="10" fill="{s}" fill-opacity=".14" stroke="{s}" stroke-width="4"/><circle cx="290" cy="150" r="13" fill="{s}"/><line x1="314" y1="138" x2="356" y2="138" stroke="{t}" stroke-opacity=".35" stroke-width="3"/><line x1="314" y1="156" x2="346" y2="156" stroke="{t}" stroke-opacity=".25" stroke-width="3"/><line x1="286" y1="178" x2="352" y2="178" stroke="{t}" stroke-opacity=".25" stroke-width="3"/>
  <rect x="454" y="126" width="112" height="58" rx="10" fill="{p}" fill-opacity=".16" stroke="{p}" stroke-width="4"/><circle cx="480" cy="155" r="10" fill="{p}"/><line x1="500" y1="146" x2="546" y2="146" stroke="{t}" stroke-opacity=".35" stroke-width="3"/><line x1="500" y1="163" x2="534" y2="163" stroke="{t}" stroke-opacity=".25" stroke-width="3"/>
  <line x1="186" y1="155" x2="264" y2="155" stroke="{t}" stroke-opacity=".42" stroke-width="4"/><line x1="376" y1="155" x2="454" y2="155" stroke="{t}" stroke-opacity=".42" stroke-width="4"/>
</g>'''
    if slug == "ch17":
        return f'''<g stroke-linecap="round">
  <circle cx="112" cy="174" r="10" fill="{p}"/><circle cx="158" cy="158" r="18" fill="{p}"/><circle cx="214" cy="138" r="28" fill="{p}"/>
  <rect x="284" y="128" width="34" height="34" rx="6" fill="{p}"/><rect x="328" y="128" width="34" height="34" rx="6" fill="{s}"/><rect x="372" y="128" width="34" height="34" rx="6" fill="{e}"/>
  <line x1="456" y1="124" x2="552" y2="124" stroke="{s}" stroke-width="2"/><line x1="456" y1="154" x2="552" y2="154" stroke="{s}" stroke-width="6"/><line x1="456" y1="190" x2="552" y2="190" stroke="{s}" stroke-width="12"/>
  <path d="M80 208 H230 M276 208 H416 M448 208 H562" stroke="{t}" stroke-opacity=".2" stroke-width="3"/>
</g>'''
    if slug == "ch18":
        return f'''<g stroke-linecap="round" stroke-linejoin="round">
  <rect x="68" y="108" width="298" height="104" rx="8" fill="{t}" fill-opacity=".04" stroke="{t}" stroke-opacity=".18"/><line x1="112" y1="168" x2="188" y2="128" stroke="{s}" stroke-width="3"/><line x1="188" y1="128" x2="268" y2="174" stroke="{p}" stroke-width="4"/><line x1="188" y1="128" x2="318" y2="136" stroke="{s}" stroke-width="3"/><circle cx="112" cy="168" r="12" fill="{p}"/><circle cx="188" cy="128" r="18" fill="{s}"/><circle cx="268" cy="174" r="13" fill="{p}"/><circle cx="318" cy="136" r="11" fill="{s}"/><circle cx="188" cy="128" r="27" fill="none" stroke="{p}" stroke-width="4" stroke-dasharray="6 5"/>
  <rect x="390" y="108" width="180" height="104" rx="8" fill="{p}" fill-opacity=".08" stroke="{p}" stroke-width="3"/><circle cx="420" cy="140" r="14" fill="{s}"/><line x1="446" y1="132" x2="546" y2="132" stroke="{t}" stroke-opacity=".5" stroke-width="4"/><line x1="410" y1="170" x2="548" y2="170" stroke="{t}" stroke-opacity=".24" stroke-width="3"/><line x1="410" y1="190" x2="520" y2="190" stroke="{t}" stroke-opacity=".24" stroke-width="3"/>
</g>'''
    if slug == "ch19":
        return f'''<g stroke-linecap="round" stroke-linejoin="round">
  <rect x="68" y="108" width="116" height="100" rx="7" fill="{t}" fill-opacity=".04" stroke="{t}" stroke-opacity=".18"/><line x1="92" y1="176" x2="126" y2="126" stroke="{s}" stroke-width="3"/><line x1="126" y1="126" x2="158" y2="172" stroke="{p}" stroke-width="3"/><circle cx="92" cy="176" r="8" fill="{p}"/><circle cx="126" cy="126" r="11" fill="{s}"/><circle cx="158" cy="172" r="8" fill="{p}"/>
  <rect x="198" y="108" width="116" height="100" rx="7" fill="{t}" fill-opacity=".04" stroke="{t}" stroke-opacity=".18"/><line x1="256" y1="124" x2="226" y2="160" stroke="{s}" stroke-width="3"/><line x1="256" y1="124" x2="286" y2="160" stroke="{s}" stroke-width="3"/><circle cx="256" cy="124" r="10" fill="{s}"/><circle cx="226" cy="160" r="8" fill="{p}"/><circle cx="286" cy="160" r="8" fill="{p}"/>
  <rect x="328" y="108" width="116" height="100" rx="7" fill="{t}" fill-opacity=".04" stroke="{t}" stroke-opacity=".18"/><line x1="386" y1="158" x2="350" y2="126" stroke="{p}" stroke-width="3"/><line x1="386" y1="158" x2="422" y2="126" stroke="{p}" stroke-width="3"/><line x1="386" y1="158" x2="386" y2="194" stroke="{s}" stroke-width="3"/><circle cx="386" cy="158" r="12" fill="{s}"/><circle cx="350" cy="126" r="8" fill="{p}"/><circle cx="422" cy="126" r="8" fill="{p}"/><circle cx="386" cy="194" r="8" fill="{p}"/>
  <rect x="458" y="108" width="116" height="100" rx="7" fill="{t}" fill-opacity=".04" stroke="{t}" stroke-opacity=".18"/><circle cx="516" cy="158" r="34" fill="none" stroke="{t}" stroke-opacity=".25" stroke-width="3"/><circle cx="516" cy="124" r="8" fill="{p}"/><circle cx="550" cy="158" r="8" fill="{s}"/><circle cx="516" cy="192" r="8" fill="{p}"/><circle cx="482" cy="158" r="8" fill="{s}"/>
</g>'''
    if slug == "ch20":
        nodes = []
        for i in range(34):
            x = 82 + (i * 37) % 244
            y = 112 + (i * 29) % 94
            color = p if i % 3 == 0 else s
            nodes.append(f'<circle cx="{x}" cy="{y}" r="{3 + i % 4}" fill="{color}" fill-opacity=".72"/>')
        nodes.append(f'<path d="M340 116 H402 L426 148 L402 180 H340 L370 148 Z" fill="{t}" fill-opacity=".08" stroke="{t}" stroke-opacity=".28" stroke-width="3"/>')
        nodes.append(f'<line x1="426" y1="148" x2="464" y2="148" stroke="{t}" stroke-opacity=".35" stroke-width="4"/><circle cx="506" cy="132" r="27" fill="{p}" fill-opacity=".85"/><circle cx="530" cy="180" r="20" fill="{s}" fill-opacity=".9"/><circle cx="474" cy="184" r="14" fill="{e}" fill-opacity=".8"/>')
        return "".join(nodes)
    if slug == "ch21":
        panels = []
        for i, x in enumerate((70, 252, 434)):
            panels.append(f'<rect x="{x}" y="112" width="142" height="92" rx="7" fill="{t}" fill-opacity=".04" stroke="{t}" stroke-opacity=".18"/>')
            panels.append(f'<line x1="{x+30}" y1="{176-i*5}" x2="{x+70}" y2="{130+i*4}" stroke="{s}" stroke-width="{3+i}"/><line x1="{x+70}" y1="{130+i*4}" x2="{x+112}" y2="{172-i*3}" stroke="{p}" stroke-width="4"/>')
            panels.append(f'<circle cx="{x+30}" cy="{176-i*5}" r="9" fill="{p}"/><circle cx="{x+70}" cy="{130+i*4}" r="{11+i}" fill="{s}"/><circle cx="{x+112}" cy="{172-i*3}" r="9" fill="{p}"/>')
        panels.append(f'<path d="M218 158 H244 M400 158 H426" stroke="{t}" stroke-opacity=".35" stroke-width="3" stroke-dasharray="5 5"/>')
        return "".join(panels)
    if slug == "ch22":
        return f'''<g stroke-linecap="round" stroke-linejoin="round">
  <path d="M78 170 C118 120 174 118 216 144 C256 168 286 120 338 132 C388 144 410 190 460 178 C500 168 532 132 562 148 L548 204 H94 Z" fill="{t}" fill-opacity=".08" stroke="{t}" stroke-opacity=".22" stroke-width="3"/>
  <path d="M126 170 C212 112 306 198 394 142 C444 110 494 150 536 128" fill="none" stroke="{s}" stroke-width="5" stroke-dasharray="10 7"/>
  <circle cx="126" cy="170" r="11" fill="{p}" stroke="{bg}" stroke-width="4"/><circle cx="286" cy="174" r="14" fill="{s}" stroke="{bg}" stroke-width="4"/><circle cx="394" cy="142" r="10" fill="{p}" stroke="{bg}" stroke-width="4"/><circle cx="536" cy="128" r="13" fill="{e}" stroke="{bg}" stroke-width="4"/>
  <path d="M286 174 L278 194 L294 194 Z M536 128 L528 148 L544 148 Z" fill="{s}"/>
</g>'''
    if slug == "ch23":
        return f'''<g stroke-linecap="round" stroke-linejoin="round">
  <line x1="86" y1="202" x2="494" y2="202" stroke="{t}" stroke-opacity=".3" stroke-width="3"/><line x1="86" y1="202" x2="86" y2="112" stroke="{t}" stroke-opacity=".3" stroke-width="3"/>
  <path d="M104 184 C164 180 190 142 248 154 C306 166 340 114 408 128 C442 136 466 122 490 116" fill="none" stroke="{s}" stroke-width="5"/>
  <circle cx="132" cy="176" r="7" fill="{p}"/><circle cx="206" cy="148" r="10" fill="{p}"/><circle cx="286" cy="158" r="8" fill="{p}"/><circle cx="364" cy="126" r="12" fill="{p}"/><circle cx="458" cy="124" r="8" fill="{p}"/>
  <text x="516" y="148" fill="{p}" font-family="monospace" font-size="34" font-weight="700">&#123;&#125;</text><text x="506" y="184" fill="{t}" fill-opacity=".45" font-family="monospace" font-size="15">data()</text>
</g>'''
    if slug == "example-portfolio-tile":
        return f'''<g stroke-linecap="round" stroke-linejoin="round">
  <rect x="70" y="108" width="232" height="104" rx="9" fill="{p}" fill-opacity=".07" stroke="{p}" stroke-width="3"/><rect x="86" y="124" width="200" height="18" rx="9" fill="{t}" fill-opacity=".10"/><rect x="86" y="124" width="126" height="18" rx="9" fill="{p}"/><circle cx="212" cy="133" r="8" fill="{s}"/><rect x="86" y="154" width="200" height="18" rx="9" fill="{t}" fill-opacity=".10"/><rect x="86" y="154" width="82" height="18" rx="9" fill="{s}"/><rect x="86" y="184" width="90" height="10" rx="5" fill="{t}" fill-opacity=".26"/>
  <rect x="338" y="108" width="232" height="104" rx="9" fill="{s}" fill-opacity=".06" stroke="{s}" stroke-width="3"/><rect x="354" y="124" width="200" height="18" rx="9" fill="{t}" fill-opacity=".10"/><rect x="354" y="124" width="154" height="18" rx="9" fill="{s}"/><circle cx="508" cy="133" r="8" fill="{p}"/><rect x="354" y="154" width="200" height="18" rx="9" fill="{t}" fill-opacity=".10"/><rect x="354" y="154" width="112" height="18" rx="9" fill="{p}"/><rect x="354" y="184" width="106" height="10" rx="5" fill="{t}" fill-opacity=".26"/>
</g>'''
    if slug == "example-performance-waterfall":
        return f'''<g stroke-linejoin="round">
  <rect x="74" y="126" width="58" height="78" rx="5" fill="{p}"/><line x1="132" y1="126" x2="164" y2="126" stroke="{t}" stroke-opacity=".35" stroke-width="3" stroke-dasharray="5 5"/><rect x="164" y="106" width="58" height="20" rx="4" fill="{s}"/><line x1="222" y1="106" x2="254" y2="106" stroke="{t}" stroke-opacity=".35" stroke-width="3" stroke-dasharray="5 5"/><rect x="254" y="106" width="58" height="28" rx="4" fill="{e}"/><line x1="312" y1="134" x2="344" y2="134" stroke="{t}" stroke-opacity=".35" stroke-width="3" stroke-dasharray="5 5"/><rect x="344" y="118" width="58" height="16" rx="4" fill="{s}"/><line x1="402" y1="118" x2="434" y2="118" stroke="{t}" stroke-opacity=".35" stroke-width="3" stroke-dasharray="5 5"/><rect x="434" y="118" width="82" height="86" rx="5" fill="{p}"/>
  <line x1="70" y1="204" x2="524" y2="204" stroke="{t}" stroke-opacity=".22" stroke-width="3"/>
</g>'''
    if slug == "example-transaction-network":
        return f'''<g stroke-linecap="round">
  <line x1="92" y1="164" x2="198" y2="122" stroke="{s}" stroke-width="8"/><line x1="198" y1="122" x2="302" y2="176" stroke="{p}" stroke-width="4"/><line x1="198" y1="122" x2="410" y2="116" stroke="{s}" stroke-width="6"/><line x1="302" y1="176" x2="508" y2="154" stroke="{e}" stroke-width="3"/><line x1="410" y1="116" x2="508" y2="154" stroke="{p}" stroke-width="9"/><path d="M178 126 L192 122 L184 136 Z M390 112 L404 116 L392 126 Z M486 146 L502 154 L488 160 Z" fill="{t}" fill-opacity=".7"/>
  <circle cx="92" cy="164" r="18" fill="{p}" stroke="{bg}" stroke-width="5"/><circle cx="198" cy="122" r="26" fill="{s}" stroke="{bg}" stroke-width="5"/><circle cx="302" cy="176" r="15" fill="{p}" stroke="{bg}" stroke-width="5"/><circle cx="410" cy="116" r="20" fill="{p}" stroke="{bg}" stroke-width="5"/><circle cx="508" cy="154" r="17" fill="{s}" stroke="{bg}" stroke-width="5"/>
</g>'''
    raise ValueError(f"No visual motif registered for {slug}")


def card_svg(index: int, slug: str, title: str, subtitle: str, category: str, colors: dict[str, str]) -> str:
    accent = colors["secondary"] if category in {"GRAPH", "EXAMPLE"} else colors["primary"]
    lines = wrap(title, 23)
    title_svg = "".join(f'<text x="52" y="{250 + line_index * 30}" fill="{colors["text"]}" fill-opacity=".90" font-family="Arial, Helvetica, sans-serif" font-size="28" font-weight="600">{escape(line)}</text>' for line_index, line in enumerate(lines))
    number = f"{index:02d}" if slug.startswith("ch") else "EX"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="360" viewBox="0 0 640 360" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)} card</title>
  <desc id="desc">{escape(subtitle)}</desc>
  <rect width="640" height="360" fill="{colors["background"]}"/>
  <rect x="24" y="24" width="592" height="312" rx="14" fill="{colors["surface"]}" stroke="{colors["outline"]}" stroke-opacity="{colors["border_opacity"]}"/>
  <rect x="52" y="52" width="82" height="8" rx="4" fill="{accent}"/>
  <text x="52" y="94" fill="{accent}" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="700" letter-spacing="2">{number} · {category}</text>
  <g>{visual(slug, colors)}</g>
  {title_svg}
  <text x="52" y="322" fill="{colors["text"]}" fill-opacity=".60" font-family="Arial, Helvetica, sans-serif" font-size="15">{escape(subtitle)}</text>
</svg>
'''


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="check generated files without writing")
    args = parser.parse_args()
    if not args.check:
        OUTPUT.mkdir(parents=True, exist_ok=True)
        (OUTPUT / "light").mkdir(parents=True, exist_ok=True)
    failures: list[str] = []
    expected = {f"{slug}.svg" for slug, *_ in ITEMS}
    expected.update(f"light/{slug}.svg" for slug, *_ in ITEMS)
    if args.check:
        actual = {path.relative_to(OUTPUT).as_posix() for path in OUTPUT.rglob("*.svg")}
        failures.extend(f"{OUTPUT.relative_to(ROOT)}/{name} (stale)" for name in sorted(actual - expected))
    for index, (slug, title, subtitle, category) in enumerate(ITEMS, start=1):
        for theme_name, colors in THEMES.items():
            output_dir = OUTPUT if theme_name == "dark" else OUTPUT / "light"
            path = output_dir / f"{slug}.svg"
            content = card_svg(index, slug, title, subtitle, category, colors)
            if args.check:
                if not path.exists() or path.read_text(encoding="utf-8") != content:
                    failures.append(str(path.relative_to(ROOT)))
            else:
                path.write_text(content, encoding="utf-8")
    if failures:
        print("Catalog cards out of date:")
        print("\n".join(f"- {item}" for item in failures))
        return 1
    print(f"{'Checked' if args.check else 'Generated'} {len(ITEMS)} dark and {len(ITEMS)} light catalog cards.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
