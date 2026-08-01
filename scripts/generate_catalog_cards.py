#!/usr/bin/env python3
"""Generate deterministic SVG cards for the visual chapter catalog."""

from __future__ import annotations

import argparse
from html import escape
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "docs" / "assets" / "catalog"

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


def visual(item_index: int, category: str) -> str:
    if category in {"GRAPH", "APPENDIX"}:
        points = [(90, 68), (190, 118), (300, 62), (430, 132), (530, 78)]
        edges = []
        for i, (x, y) in enumerate(points[:-1]):
            nx, ny = points[i + 1]
            edges.append(f'<line x1="{x}" y1="{y}" x2="{nx}" y2="{ny}" stroke="#03DAC6" stroke-width="4" opacity=".75"/>')
        edges.append('<line x1="190" y1="118" x2="430" y2="132" stroke="#BB86FC" stroke-width="3" stroke-dasharray="8 7" opacity=".8"/>')
        nodes = []
        for i, (x, y) in enumerate(points):
            color = "#BB86FC" if i % 2 == 0 else "#03DAC6"
            nodes.append(f'<circle cx="{x}" cy="{y}" r="{16 + (i % 3) * 4}" fill="{color}" stroke="#121212" stroke-width="6"/>')
        return "".join(edges + nodes)
    if category == "EXAMPLE":
        if item_index % 3 == 0:
            bars = []
            for i in range(5):
                color = "#BB86FC" if i % 2 == 0 else "#03DAC6"
                bars.append(f'<rect x="{90 + i * 100}" y="{145 - (i % 3) * 24}" width="54" height="{105 + (i % 3) * 24}" rx="6" fill="{color}"/>')
            return "".join(bars)
        if item_index % 3 == 1:
            return '<rect x="75" y="150" width="72" height="120" rx="5" fill="#BB86FC"/><rect x="190" y="118" width="72" height="152" rx="5" fill="#03DAC6"/><rect x="305" y="92" width="72" height="178" rx="5" fill="#CF6679"/><rect x="420" y="64" width="72" height="206" rx="5" fill="#BB86FC"/>'
        return '<path d="M70 180 L180 94 L300 168 L418 78 L544 146" fill="none" stroke="#03DAC6" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/><path d="M180 94 L300 168 L418 78" fill="none" stroke="#BB86FC" stroke-width="4" stroke-dasharray="8 8"/><circle cx="70" cy="180" r="18" fill="#BB86FC"/><circle cx="180" cy="94" r="23" fill="#03DAC6"/><circle cx="300" cy="168" r="16" fill="#BB86FC"/><circle cx="418" cy="78" r="20" fill="#CF6679"/><circle cx="544" cy="146" r="17" fill="#03DAC6"/>'
    bars = []
    for i in range(6):
        height = 54 + ((item_index * 13 + i * 19) % 112)
        color = "#BB86FC" if i % 2 == 0 else "#03DAC6"
        bars.append(f'<rect x="{74 + i * 82}" y="{226 - height}" width="48" height="{height}" rx="5" fill="{color}"/>')
    bars.append('<path d="M72 82 L170 116 L250 78 L350 124 L454 88 L552 106" fill="none" stroke="#FFFFFF" stroke-opacity=".7" stroke-width="4" stroke-linecap="round"/>')
    return "".join(bars)


def card_svg(index: int, slug: str, title: str, subtitle: str, category: str) -> str:
    accent = "#03DAC6" if category in {"GRAPH", "EXAMPLE"} else "#BB86FC"
    lines = wrap(title, 23)
    title_svg = "".join(f'<text x="52" y="{250 + line_index * 30}" fill="#FFFFFF" fill-opacity=".90" font-family="Arial, Helvetica, sans-serif" font-size="28" font-weight="600">{escape(line)}</text>' for line_index, line in enumerate(lines))
    number = f"{index:02d}" if slug.startswith("ch") else "EX"
    visual_transform = "translate(0 -45)" if category == "EXAMPLE" else "translate(0 0)"
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="360" viewBox="0 0 640 360" role="img" aria-labelledby="title desc">
  <title id="title">{escape(title)} card</title>
  <desc id="desc">{escape(subtitle)}</desc>
  <rect width="640" height="360" fill="#121212"/>
  <rect x="24" y="24" width="592" height="312" rx="14" fill="#1E1E1E" stroke="#FFFFFF" stroke-opacity=".15"/>
  <rect x="52" y="52" width="82" height="8" rx="4" fill="{accent}"/>
  <text x="52" y="94" fill="{accent}" font-family="Arial, Helvetica, sans-serif" font-size="14" font-weight="700" letter-spacing="2">{number} · {category}</text>
  <g transform="{visual_transform}">{visual(index, category)}</g>
  {title_svg}
  <text x="52" y="322" fill="#FFFFFF" fill-opacity=".60" font-family="Arial, Helvetica, sans-serif" font-size="15">{escape(subtitle)}</text>
</svg>
'''


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="check generated files without writing")
    args = parser.parse_args()
    if not args.check:
        OUTPUT.mkdir(parents=True, exist_ok=True)
    failures: list[str] = []
    expected = {f"{slug}.svg" for slug, *_ in ITEMS}
    if args.check:
        stale = sorted(path.name for path in OUTPUT.glob("*.svg") if path.name not in expected)
        failures.extend(f"{OUTPUT.relative_to(ROOT)}/{name} (stale)" for name in stale)
    for index, (slug, title, subtitle, category) in enumerate(ITEMS, start=1):
        path = OUTPUT / f"{slug}.svg"
        content = card_svg(index, slug, title, subtitle, category)
        if args.check:
            if not path.exists() or path.read_text(encoding="utf-8") != content:
                failures.append(str(path.relative_to(ROOT)))
        else:
            path.write_text(content, encoding="utf-8")
    if failures:
        print("Catalog cards out of date:")
        print("\n".join(f"- {item}" for item in failures))
        return 1
    print(f"{'Checked' if args.check else 'Generated'} {len(ITEMS)} catalog cards.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
