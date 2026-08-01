# Financial and Graph Visualization

`financial-graph-visualization` is a source-grounded skill for designing,
critiquing, and implementing deterministic financial charts, portfolio and
fund dashboards, graph visualizations, and network interfaces.

It synthesizes:

- *Visualizing Financial Data* by Julie Rodriguez and Piotr Kaczmarek
- *Visualizing Graph Data* by Corey L. Lanum

The skill contains a decision system, 23 chapter references, reusable visual
patterns, a glossary, and source-provenance notes.

## Core rule

This skill is code-native only. It must not call Image Generator, `image_gen`,
or another generative-image model. Build visuals from data and explicit
geometry with SVG, HTML/CSS, Canvas, D3.js, Vega-Lite, Plotly, Matplotlib,
NetworkX, Graphviz, Cytoscape.js, or an equivalent deterministic method.

If a raster image is needed, export or capture it from the editable
code/data-native source and keep that source with the deliverable.

## Installation

Clone the repository and make the project folder available to the agent
runtime. The standalone repository root is the skill folder. For local Claude
Code and Codex installations, symlink it into each runtime's skills directory:

```bash
git clone https://github.com/nutdnuy/financial-graph-visualization.git
cd financial-graph-visualization

mkdir -p ~/.claude/skills ~/.codex/skills
ln -sfn "$PWD" \
  ~/.claude/skills/financial-graph-visualization
ln -sfn "$PWD" \
  ~/.codex/skills/financial-graph-visualization
```

If your agent runtime uses a different skill directory, copy or symlink this
repository folder into that directory instead.

## Usage

Invoke the skill by name in a natural-language request. State the decision,
data, audience, and delivery format when they are known.

```text
Use financial-graph-visualization to choose a layout for an unfamiliar
transaction network and explain the trade-offs.
```

```text
Use financial-graph-visualization to design a normalized comparison tile for
these five ETFs, including benchmark context and accessible color rules.
```

```text
Use financial-graph-visualization to implement a deterministic SVG dashboard
from this CSV. Keep the editable source and document the seed and layout
parameters.
```

The skill routes requests as follows:

- Financial visualization: chapters `ch01` through `ch12`
- Graph and network visualization: chapters `ch13` through `ch23`
- Visual design decisions: `cheatsheet.md` and `patterns.md`
- Provenance and limitations: `references/source-notes.md`
- Curated visual routing: `references/visual-index.md`

## Output expectations

Before delivery, verify that every value, mark, position, size, color, and
relationship is traceable to data, a declared rule, or an explicitly labeled
illustrative assumption. Record random seeds and layout parameters when a
layout can be stochastic. Validate calculations, baselines, labels, scales,
color meaning, accessibility, and the intended audience's ability to decode
the result.

## Distribution and source notice

The source PDFs are not included in this repository. The full-page rendered
book references are also intentionally omitted: they are local personal-study
excerpts, not licensed templates or distributable assets. The vault copy may
retain those local references for source verification; do not upload them to a
generative-image model or redistribute them.

This repository contains a concise synthesis, not a replacement for the
source books. Tool and library behavior described by the 2016-2017 sources may
be outdated; verify current APIs before implementation. No separate software
license is asserted for the source-derived documentation.
