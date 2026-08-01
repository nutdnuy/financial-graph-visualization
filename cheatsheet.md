# Financial and Graph Visualization Decision Cheatsheet

## Start Here

| Question | If yes | If no |
|---|---|---|
| Is the decision and audience explicit? | Identify the comparison and action. | Stop and define audience, task, question, follow-ups, and channel. |
| Are relationships the analytical object? | Build a graph model and use ch13-ch22. | Choose a conventional financial/statistical chart first. |
| Does one value require judgment? | Add benchmark, target, peer, quartile, distribution, or history. | Keep the view minimal. |
| Does the user need causes beneath a total? | Use summary/detail, waterfall, drill-down, or linked views. | Avoid unnecessary interaction. |
| Is the graph unreadable at full scale? | Filter, group, aggregate, query, or change the analytical unit. | Preserve direct access to individual nodes. |

## Output Method Gate

| Need | Required method |
|---|---|
| Editable static chart | SVG or chart-library source with explicit data bindings |
| Interactive dashboard | HTML/Canvas, React, D3.js, Vega-Lite, Plotly, or another code-native visualization stack |
| Network visualization | D3.js, NetworkX, Graphviz, Cytoscape.js, Gephi, or another graph-native tool with recorded layout settings |
| PNG/PDF deliverable | Deterministically export or capture the code/data-native source; retain the editable source |
| Concept without real data | Labeled wireframe or explicitly declared synthetic dataset |

**Hard prohibition:** Never use Image Generator, `image_gen`, or any generative-image model while this skill is active. Do not use generative imagery for charts, dashboard mockups, network diagrams, decorative layers, or backgrounds. Never upload the local book-page references to a generative model.

## Financial View Selection

| Need | Prefer | Avoid |
|---|---|---|
| Compare heterogeneous securities | Consistent Profile/Results Tiles | Changing measures, band order, or scale per item |
| Explain a derived balance | Waterfall or cascade with visible subtotals | A single end value without drivers |
| Compare allocation or performance | Aligned bars/lines with benchmark context | Unsorted tables or uncontextualized values |
| Show positive and negative exposure | Butterfly/diverging bar | Two unrelated charts with incompatible scales |
| Show many fund attributes compactly | Glyph only for frequent/expert users | Dense glyphs for infrequent audiences |
| Show relative and absolute performance | Paired views with shared quartile bands | Mixing the two scales in one ambiguous axis |

## Graph Layout Selection

| Data/task | Layout | Reason |
|---|---|---|
| Unknown general network | Force-directed | Surfaces clusters, central nodes, and isolates without assuming hierarchy |
| Directed acyclic or near-hierarchical | Hierarchy | Makes direction and levels legible |
| One focal entity and its reach | Radial | Makes the selected node's centrality explicit |
| Equal placement / minimize center bias | Circular | Gives every node equal radial status, with weaker structural insight |
| Geographic coordinates are essential | Map overlay | Preserves location, but sacrifices algorithmic layout freedom |
| Dense or very large graph | Filter/group before layout | Layout cannot rescue excessive data volume |

## Encoding Defaults

- Use position and aligned length before area or angle.
- Use node size for a numeric count or importance measure.
- Use link width for relationship strength or volume.
- Use categorical color for membership; use ordered lightness only for ordered magnitude.
- Keep labels human-readable and minimize labels on links.
- Put context in muted background layers and focal data in foreground.
- Keep zero, scale, benchmark, and sign conventions visible.

## Scale and Interaction

| Constraint | Decision rule |
|---|---|
| Server can query a huge corpus | Filter/aggregate in the database for performance. |
| Data fits in memory and users need exploration | Filter in the visualization for responsive control. |
| Users reason about clusters | Group nodes; allow expansion to members. |
| Users need a stable comparison through time | Use small multiples. |
| Users need to explore event windows | Use a time bar/filter. |
| Animation changes position without adding meaning | Remove it; preserve the mental map. |

## Failure Smells

- More than about five pie slices.
- Every record rendered at once.
- Color doing several jobs without a legend.
- Thick link labels obscuring the links.
- 3D depth hiding nodes or corrupting size comparisons.
- A graph used only because the data came from a graph database.
- A custom build selected before value, complexity, and maintenance are assessed.
- A visually novel glyph that requires users to memorize dozens of encodings.
