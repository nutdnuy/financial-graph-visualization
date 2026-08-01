---
name: financial-graph-visualization
description: "Knowledge base from Visualizing Financial Data and Visualizing Graph Data. Use when designing or implementing deterministic, code-native financial charts, portfolio or fund dashboards, graph/network visualizations, node-link diagrams, visual encodings, layouts, filtering, temporal or geographic graphs, or choosing visualization implementation methods."
---

<!-- argument-hint: [decision, topic, framework, visual pattern, or chapter number] -->

# Financial and Graph Visualization

**Sources**: *Visualizing Financial Data* by Julie Rodriguez and Piotr Kaczmarek; *Visualizing Graph Data* by Corey L. Lanum<br>
**Coverage**: 787 source pages | 22 chapters + D3.js appendix | Generated 2026-08-01

## How to Use This Skill

- With no topic, apply the Core Decision System below.
- With a financial task, route to ch01-ch12.
- With a graph/network task, route to ch13-ch23.
- With a named topic, consult the Topic Index and read the relevant chapter before answering.
- With a visual-design decision, read [cheatsheet.md](cheatsheet.md) and [patterns.md](patterns.md).
- When appearance, layout, or chart anatomy matters, read [references/visual-index.md](references/visual-index.md) and inspect only the relevant local reference image.

Do not claim that an extracted page image is a reusable template. It is copyrighted source evidence for personal study and design reasoning.

## Mandatory Execution Boundary: No Image Generator

Never call Image Generator, `image_gen`, or another generative-image model while this skill is active. This prohibition applies to analytical charts, dashboard mockups, node-link diagrams, infographics, backgrounds, and decorative layers.

- Build visuals from data and explicit geometry using code-native or visualization-native methods such as SVG, HTML/CSS/Canvas, D3.js, Vega-Lite, Plotly, Matplotlib, NetworkX, Graphviz, or Cytoscape.js.
- A raster deliverable is allowed only when exported or captured deterministically from the code/data-native source. Keep the editable source with the export.
- When real data is unavailable, create a labeled wireframe or use declared synthetic data. Do not ask a generative model to invent chart values, labels, topology, or visual relationships.
- Never submit the local book-page visual references to a generative-image model. Use them only for personal study and source verification.
- For layouts with stochastic behavior, set and record the random seed and layout parameters when the implementation permits it.
- If a user asks for Image Generator while invoking this skill, explain that this skill is code-native only and offer SVG, HTML, React, or a charting-library implementation instead. Do not silently switch tools.

Before delivery, confirm that no generative-image tool was used and that every displayed value, mark, position, size, color, and relationship is traceable to data, a declared rule, or an explicitly labeled illustrative assumption.

## Core Decision System

1. **Define the decision.** State the audience, task, decision, primary question, likely follow-up questions, and delivery channel.
2. **Model the data.** Separate entities, measures, time, hierarchy, geography, and relationships. For networks, define nodes, links, direction, weight, time, and properties.
3. **Choose the comparison.** Add a benchmark, peer group, prior period, target, distribution, or category context when a value is not meaningful alone.
4. **Choose the visual grammar.** Map position first, then length/size, color, shape, and texture. Encode only properties that help the user decide.
5. **Choose structure and interaction.** Select chart family or graph layout from the data shape. Use overview, zoom, filter, details-on-demand, and comparison for complex data.
6. **Control scale.** Filter, group, aggregate, sample, or query before rendering. Do not show every record simply because the tool can.
7. **Verify truth and usability.** Check calculations, baselines, scales, labels, color meaning, accessibility, and whether the intended audience can decode the view without hidden assumptions.
8. **Choose implementation effort.** Balance business value, complexity, audience reach, frequency, data volume, interactivity, and maintenance before choosing a prebuilt or code-native programmable delivery. Do not use generative-image delivery.

## Core Frameworks and Mental Models

### Audience -> Question -> Storyline

Use audience needs to determine which data matters and how it should unfold. Design the first view to answer the primary question, then anticipate the next questions with context and drill-down paths. A portfolio manager, relationship manager, executive, regulator, and retail investor should not receive the same emphasis even when they share a data source.

### Compare -> Connect -> Conclude

Treat a visualization as a reasoning surface. First make meaningful comparisons possible; then show relationships, drivers, and decomposition; finally support a defensible conclusion or action. A chart that merely decorates a value has not completed this chain.

### Summary + Detail on Demand

Show a stable summary before exposing detail. Preserve the relationship between totals and components so users can inspect causes without losing context. This principle unifies financial waterfalls, Tile drill-downs, graph navigation, tooltips, grouping, and progressive expansion.

### Tile Framework

Use normalized Profile and Results Tiles when comparing heterogeneous securities. Keep band order, definitions, scale, and drill-down behavior consistent. Adapt the measures to the security type, but do not change the visual grammar so much that cross-security comparison breaks. See ch03 and visual reference 01.

### Singular, Multifaceted, or Varied View

- Use a **singular** view when one chart answers the decision cleanly.
- Use a **multifaceted** view when the same visual grammar can be pivoted, reordered, filtered, or tilted to answer follow-ups.
- Use **varied** coordinated views when distinct questions require different encodings.

Prefer the smallest set that answers the task; multiple views must contribute different reasoning, not repetition.

### Context Before Judgment

Pair absolute values with benchmarks, quartiles, targets, history, or peer distributions. Use muted context in the background and the focal entity in the foreground. When relative and absolute views answer different questions, show both with aligned scales and shared reference bands.

### Graph Model Before Graph Drawing

Define what nodes and links mean before choosing a layout. A shared property can create a graph even when the source is relational or tabular, but different valid models reveal different phenomena. Document direction, weight, multiplicity, and time semantics; otherwise visual proximity or link density can be misread.

### Visual Properties Carry Specific Jobs

Use node size for a meaningful numeric count or importance measure, link width for relationship strength, and categorical color for group membership. Minimize link labels, provide human-readable node labels, and add legends when mappings are not self-evident. Avoid continuous color gradients for categories.

### Layout Follows Topology and Task

- Use **force-directed** for unfamiliar or generic networks and exploratory clustering.
- Use **hierarchy** for a directed acyclic or near-hierarchical structure.
- Use **radial** to make one or more focal nodes explicit.
- Use **circular** when equal placement and low center bias matter, accepting weaker structural insight.
- Avoid 3D unless occlusion, navigation, and lost size encoding are explicitly solved.

Layout changes positions, not underlying relationships. See ch19 and visual reference 11.

### Filter for Focus; Group for Abstraction

Filter at the database/query side for scale and performance; filter in the visualization for responsive user control. Group nodes when the analytical unit is a cluster rather than an individual, and allow expansion when details matter. If a network remains unreadable after filtering and grouping, a graph may be the wrong view.

### Time Belongs in the Relationship Model

Use small multiples for stable side-by-side comparison, time windows for exploration, and dynamic properties only when animation or state transitions clarify change. In many event networks, timestamp links rather than nodes because the event is the relationship. Keep the user's mental map stable across time.

### Business Value, Complexity, and Solution Score

Score visualization initiatives on business criticality, audience reach, frequency, reuse, and number of users. Separately assess complexity through uniqueness, channels, permissions, localization, integration, interactivity, releases, refresh rate, and volume. Use both scores to choose effort and delivery method; do not treat available budget as a substitute for value. See ch12 and visual reference 08.

## Chapter Index

| # | Source chapter | Key frameworks |
|---|---|---|
| [ch01](chapters/ch01-financial-visual-communications.md) | Financial 1 - Paving a Path Toward Visual Communications | audience, narrative, multiple perspectives |
| [ch02](chapters/ch02-benefits-of-visual-methods.md) | Financial 2 - Benefits of Using Visual Methods | compare, connect, conclude |
| [ch03](chapters/ch03-security-assessment-tile-framework.md) | Financial 3 - Security Assessment | Tile Framework, normalized comparison |
| [ch04](chapters/ch04-portfolio-construction.md) | Financial 4 - Portfolio Construction | singular/multifaceted/varied views |
| [ch05](chapters/ch05-trading-visual-system.md) | Financial 5 - Trading | Contrail, ticker/quote/watchlist system |
| [ch06](chapters/ch06-performance-measurement.md) | Financial 6 - Performance Measurement | attribution, grids, linked views |
| [ch07](chapters/ch07-financial-statements.md) | Financial 7 - Financial Statements | waterfall, cascade, transparency |
| [ch08](chapters/ch08-pension-funds.md) | Financial 8 - Pension Funds | demographic/time views, funding context |
| [ch09](chapters/ch09-mutual-funds.md) | Financial 9 - Mutual Funds | reusable components, benchmark context |
| [ch10](chapters/ch10-hedge-funds.md) | Financial 10 - Hedge Funds | glyphs, ranking, information-seeking mantra |
| [ch11](chapters/ch11-financial-visualization-principles.md) | Financial 11 - Data Visualization Principles | audience, clarity, efficiency |
| [ch12](chapters/ch12-implementing-financial-visuals.md) | Financial 12 - Implementing the Visuals | BVA, complexity, Solution Score |
| [ch13](chapters/ch13-graph-visualization-basics.md) | Graph 1 - Getting to Know Graph Visualization | graph model, explore vs communicate |
| [ch14](chapters/ch14-graph-case-studies.md) | Graph 2 - Case Studies | fraud, intelligence, cyber, marketing |
| [ch15](chapters/ch15-gephi-and-keylines.md) | Graph 3 - Gephi and KeyLines | tool-selection trade-offs |
| [ch16](chapters/ch16-graph-data-modeling.md) | Graph 4 - Data Modeling | nodes, links, properties, graph databases |
| [ch17](chapters/ch17-building-graph-visualizations.md) | Graph 5 - Building Graph Visualizations | visual encoding, audience calibration |
| [ch18](chapters/ch18-interactive-graph-visualizations.md) | Graph 6 - Interactive Visualizations | navigation, decluttering, progressive expansion |
| [ch19](chapters/ch19-graph-layouts.md) | Graph 7 - Organizing a Chart | force, hierarchy, radial, circular |
| [ch20](chapters/ch20-big-graph-data.md) | Graph 8 - Big Data | filtering, grouping, scalability |
| [ch21](chapters/ch21-dynamic-graphs.md) | Graph 9 - Dynamic Graphs | small multiples, time bars, dynamic properties |
| [ch22](chapters/ch22-graphs-on-maps.md) | Graph 10 - Graphs on Maps | geographic modeling, filtering, overlays |
| [ch23](chapters/ch23-d3js-appendix.md) | Graph Appendix - D3.js | selectors, SVG, data binding, force simulation |

## Topic Index

- **Attribution** -> ch06
- **Audience and questions** -> ch01, ch11, ch17
- **Benchmarks and quartiles** -> ch04, ch09
- **Big graphs** -> ch18, ch20
- **Business Value Assessment** -> ch12
- **Centrality and communities** -> ch14, ch15
- **Color, size, labels, link width** -> ch11, ch17
- **D3.js** -> ch23
- **Dynamic/time graphs** -> ch21
- **Filtering and grouping** -> ch18, ch20
- **Financial statements** -> ch07
- **Gephi / KeyLines** -> ch15
- **Geographic graphs** -> ch22
- **Glyphs** -> ch10, ch17
- **Graph data models / databases** -> ch16
- **Graph layouts** -> ch19
- **Hedge funds** -> ch10
- **Implementation selection** -> ch12, ch15, ch23
- **Interactivity / details on demand** -> ch10, ch18
- **Mutual funds** -> ch09
- **Pension funds** -> ch08
- **Portfolio construction and risk** -> ch04
- **Security comparison / Tiles** -> ch03
- **Solution Score** -> ch12
- **Trading displays / Contrail** -> ch05
- **Waterfalls and cascades** -> ch07, ch08

## Supporting Files

- [cheatsheet.md](cheatsheet.md) - decision rules and trade-off matrices
- [patterns.md](patterns.md) - reusable visualization patterns
- [glossary.md](glossary.md) - key terms with chapter references
- [references/visual-index.md](references/visual-index.md) - curated source-page visual references
- [references/source-notes.md](references/source-notes.md) - provenance, extraction notes, and limitations

## Scope and Limits

This skill synthesizes the two named books. Tool versions and product capabilities described in the 2016-2017 sources may be outdated; verify current APIs and software behavior before implementation. The visual-reference images are local study excerpts, not licensed templates, generative-model inputs, or distributable assets. All created visuals must remain deterministic and code/data-native. For any claim requiring exact wording, a full figure, or page-level verification, return to the user-supplied source PDFs.
