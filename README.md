# Financial and Graph Visualization

Design explainable, reproducible financial and network visuals — without
generative images.

`financial-graph-visualization` is a source-grounded skill for turning a
financial or graph question into a defensible visual grammar, layout,
interaction model, and editable code-native implementation.

[![Latest release](https://img.shields.io/github/v/release/nutdnuy/financial-graph-visualization?display_name=tag)](https://github.com/nutdnuy/financial-graph-visualization/releases/latest)
[![Examples](https://img.shields.io/badge/examples-code--native-03DAC6)](examples/)

The editable [social preview source](assets/social-preview.svg) is included
for repository sharing. Export it to PNG when uploading a custom GitHub Social
Preview under repository Settings.

## Quick links

| Need | Start here |
|---|---|
| See working output | [Examples](examples/) |
| Install the skill | [Install as an agent skill](#install-as-an-agent-skill) |
| Copy a prompt | [Copy-ready prompts](#copy-ready-prompts) |
| Follow one input to one output | [Complete walkthrough](#complete-walkthrough) |
| Choose a chapter | [Coverage catalog](docs/CATALOG.md) |
| Check the package | `python3 scripts/validate_examples.py` |

## See it in 30 seconds

The examples are dependency-free HTML/SVG files using labeled synthetic data.
Open any `index.html` directly in a browser, or serve the repository locally:

```bash
python3 -m http.server 8000
```

Then open:

- [Portfolio comparison tiles](examples/portfolio-tile/) — normalized security profiles and benchmark context
- [Performance waterfall](examples/performance-waterfall/) — deterministic contribution and return decomposition
- [Transaction network](examples/transaction-network/) — fixed-position graph layout with typed, weighted links

Validate the three example documents without installing dependencies:

```bash
python3 scripts/validate_examples.py
```

### Portfolio comparison

![Portfolio comparison tile preview](examples/portfolio-tile/preview.svg)

### Performance waterfall

![Performance waterfall preview](examples/performance-waterfall/preview.svg)

### Transaction network

![Transaction network preview](examples/transaction-network/preview.svg)

Every preview has an editable HTML/SVG source beside it. The examples are
illustrative and do not provide investment advice.

## Why this exists

- **Decision first:** start with the audience, question, comparator, and next action.
- **Traceable visuals:** every mark, value, position, size, and relationship maps to data or a declared rule.
- **Reproducible output:** deterministic code, explicit geometry, fixed seeds, and documented layout parameters.
- **Editable delivery:** SVG, HTML/CSS, Canvas, D3.js, Vega-Lite, Plotly, Matplotlib, NetworkX, Graphviz, or Cytoscape.js remain available for revision.
- **Evidence-aware:** source, method, cutoff, limitations, accessibility, and data status stay visible.
- **No image generation:** Image Generator, `image_gen`, and other generative-image models are prohibited by design.

## Install as an agent skill

Clone the standalone repository and symlink its root into the agent runtime:

```bash
git clone https://github.com/nutdnuy/financial-graph-visualization.git
cd financial-graph-visualization

mkdir -p ~/.claude/skills ~/.codex/skills
ln -sfn "$PWD" ~/.claude/skills/financial-graph-visualization
ln -sfn "$PWD" ~/.codex/skills/financial-graph-visualization
```

If your runtime uses another skills directory, copy or symlink this repository
folder there instead.

Supported local skill locations:

| Runtime | Skill directory |
|---|---|
| Claude Code | `~/.claude/skills/financial-graph-visualization` |
| Codex | `~/.codex/skills/financial-graph-visualization` |
| Other Agent Skills host | Its configured skills directory |

## Use it

Invoke the skill by name and provide the decision, data, audience, and delivery
format when known:

```text
Use financial-graph-visualization to choose a layout for this unfamiliar
transaction network. Explain the topology assumptions, filtering strategy,
and accessibility checks before writing deterministic SVG.
```

```text
Use financial-graph-visualization to design a normalized comparison tile for
these ETFs. Include benchmark context, units, a cutoff date, and an editable
code-native implementation.
```

```text
Use financial-graph-visualization to turn this return series into a waterfall
and attribution view. Keep the source data, calculation rules, and export
source together.
```

The skill routes requests to:

- Financial visualization: chapters `ch01` through `ch12`
- Graph and network visualization: chapters `ch13` through `ch23`
- Visual design decisions: `cheatsheet.md` and `patterns.md`
- Provenance and limits: `references/source-notes.md`
- Visual-reference routing: `references/visual-index.md`

## Copy-ready prompts

| Goal | Prompt starter |
|---|---|
| Compare securities | `Use financial-graph-visualization to normalize these securities into profile and results tiles. Preserve units, benchmark context, and the cutoff date.` |
| Explain drivers | `Use financial-graph-visualization to turn this total return into a waterfall. Show the ordered drivers, calculation rule, and editable SVG source.` |
| Choose a network layout | `Use financial-graph-visualization to compare force-directed, hierarchy, radial, and circular layouts for this topology and task.` |
| Reduce graph density | `Use financial-graph-visualization to design a server-side and client-side filtering strategy for this graph. State what is hidden and how users restore it.` |
| Audit a chart | `Use financial-graph-visualization to audit this chart for misleading scales, missing comparators, inaccessible color, unclear units, and unsupported claims.` |

## Complete walkthrough

### Input

Suppose a return attribution table contains an opening value, ordered positive
and negative drivers, a period, a unit, and a cutoff date.

### Route

The skill routes the task to performance measurement and financial-statement
patterns, then applies **Summary + Detail on Demand** and an ordered waterfall.

### Output

Start with the [performance waterfall example](examples/performance-waterfall/)
and replace the `components` array in `index.html`. The editable source keeps
the calculation, geometry, labels, and method note together.

### Verification

The example checks that `100 + 12 + 8 - 3 - 5 = 112`, labels the value index,
states that the data is synthetic, keeps positive and negative values distinct,
and renders without a random layout or external dependency.

## Package map

```text
SKILL.md                         # routing, decision system, and guardrails
cheatsheet.md                    # compact decision rules
patterns.md                      # reusable visualization patterns
glossary.md                      # terms with chapter references
chapters/                        # progressive-disclosure source synthesis
references/source-notes.md       # provenance and limitations
references/visual-index.md       # local-only visual routing index
examples/                        # runnable HTML/SVG demonstrations
scripts/validate_examples.py     # dependency-free smoke check
docs/CATALOG.md                  # chapter and example catalog
```

## Coverage map

| Area | Chapters | Best starting point |
|---|---:|---|
| Financial communication and audience | `ch01`–`ch02`, `ch11` | [Core Decision System](SKILL.md#core-decision-system) |
| Security comparison and tiles | `ch03`, `ch09` | [Portfolio comparison example](examples/portfolio-tile/) |
| Portfolio, trading, and performance | `ch04`–`ch06` | [Patterns](patterns.md) |
| Statements, waterfalls, and funds | `ch07`–`ch10` | [Performance waterfall example](examples/performance-waterfall/) |
| Implementation and prioritization | `ch12` | `Solution Score` in [cheatsheet](cheatsheet.md) |
| Graph modeling and case studies | `ch13`–`ch17` | [Graph Model Before Graph Drawing](SKILL.md#graph-model-before-graph-drawing) |
| Interaction and scale | `ch18`, `ch20` | [Transaction network example](examples/transaction-network/) |
| Layouts and dynamic graphs | `ch19`, `ch21` | [Layout Follows Topology and Task](SKILL.md#layout-follows-topology-and-task) |
| Maps and D3.js | `ch22`–`ch23` | [Chapter catalog](docs/CATALOG.md) |

## Verification contract

Before delivery, confirm that:

1. The audience, decision, comparator, period, units, and cutoff are explicit.
2. Values and visual relationships are calculated from data or labeled assumptions.
3. A stochastic layout records its seed and parameters, or uses fixed geometry.
4. Color is paired with labels, icons, or text for semantic states.
5. Scales, baselines, labels, accessibility, and responsive behavior are checked.
6. The editable source remains with any raster export.
7. No generative-image tool was used.

## Sources and distribution boundary

The skill synthesizes *Visualizing Financial Data* by Julie Rodriguez and Piotr
Kaczmarek and *Visualizing Graph Data* by Corey L. Lanum. The source PDFs and
full-page rendered book references are intentionally excluded. Those renders
are local personal-study excerpts, not licensed templates or distributable
assets.

This repository contains a concise synthesis and original deterministic
examples, not a replacement for the source books. Tool behavior described by
the 2016-2017 sources may be outdated; verify current APIs before implementation.
See [NOTICE.md](NOTICE.md) for the source and usage boundary.

## Contributing and support

Open an issue with a minimal dataset, the intended decision, the expected
visual relationship, and the current output. Keep examples synthetic or
properly licensed. Proposed visual changes should include the editable source,
validation notes, and an explanation of why the encoding improves the decision.
