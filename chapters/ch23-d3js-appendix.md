# Chapter 23: D3.js Appendix

## Core Idea

D3.js provides low-level, data-driven control over DOM/SVG marks, interactions, and force simulation. Use it when custom behavior and visual grammar justify engineering effort; verify modern D3 APIs because the source examples reflect an earlier version.

## Frameworks Introduced

- **Select -> Bind -> Enter/Update/Exit -> Render**
  - When to use: Creating marks from data.
  - How: Select a container/mark set; bind data with stable keys; create entering marks; update existing marks; remove exiting marks; set accessible attributes and styles.
- **Data/Visual Separation**
  - When to use: Supporting several views from one data model.
  - How: Keep graph objects and transformations separate from SVG/Canvas rendering; compute derived values before binding; centralize scales and semantic tokens.
- **SVG Primitive Graph**
  - When to use: Small/medium networks requiring DOM-level control.
  - How: Use lines/paths for links and shapes/images for nodes; create groups/layers; bind visual properties through scales; add labels selectively.
- **Force Simulation Loop**
  - When to use: Automatically positioning a generic network.
  - How: Supply nodes and links; configure link, charge, centering, and collision forces; update positions on ticks; stop/reheat deliberately after interactions.
- **Interaction Binding**
  - When to use: Selection, hover/focus, drag, or transition.
  - How: Attach pointer and keyboard-accessible handlers; update state first, then render; avoid interaction that exists only on hover.

## Key Concepts

- **Selector**: Rule that finds DOM elements.
- **Data binding**: Association of data objects with visual elements.
- **SVG**: Vector drawing model using DOM elements.
- **Scale**: Function translating data values into visual ranges.
- **Force simulation**: Iterative physics-style positioning engine.
- **Tick**: Simulation step that updates positions.
- **Canvas/WebGL**: Alternatives for larger rendering workloads with different interaction/accessibility trade-offs.

## Mental Models

- D3 is a visualization construction toolkit, not a prebuilt chart catalog.
- Low-level flexibility transfers responsibility for layout, interaction, accessibility, and maintenance to the developer.
- Keep data semantics independent from render technology.
- Use SVG when direct DOM interaction and accessibility outweigh node-count limits.

## Anti-patterns

- Using D3 for a standard chart already supported by a governed component.
- Mixing data transformation, state, and DOM mutation in one function.
- Recreating the entire SVG on every interaction.
- Running force simulation indefinitely.
- Copying source-era syntax without checking the installed D3 version.
- Supporting mouse hover while omitting keyboard/focus and touch behavior.

## Illustrative Code Pattern

```javascript
const nodes = data.nodes;
const links = data.links;

const simulation = d3.forceSimulation(nodes)
  .force("link", d3.forceLink(links).id(d => d.id))
  .force("charge", d3.forceManyBody().strength(-40))
  .force("center", d3.forceCenter(width / 2, height / 2));
```

Use the installed D3 documentation to confirm exact module and event APIs. Bind links and nodes with stable keys, update their positions on simulation ticks, and stop or reheat the simulation only in response to meaningful data/layout changes.

## Worked Example

Build a small fund-holdings bipartite graph. Transform holdings into fund nodes, security nodes, and weighted ownership links. Bind links to SVG paths and nodes to grouped circle/text marks. Use node type for shape/color and position with force/link/collision forces. Add click selection and a side panel for exact position size. For a much larger graph, keep the same semantic model but consider Canvas or a specialized graph renderer rather than forcing thousands of DOM nodes.

## Reference Table

| Need | D3 mechanism | Responsibility |
|---|---|---|
| Create marks from data | Selection + data join | Stable keys and lifecycle |
| Map values to visuals | Scales | Domain, range, accessibility |
| Position generic network | Force simulation | Parameters, stability, stopping |
| Enable interaction | Event handlers + state | Mouse, touch, keyboard, focus |
| Render larger graphs | Canvas/WebGL or specialized renderer | Hit testing and accessibility |

## Key Takeaways

1. Use D3 when custom behavior earns low-level complexity.
2. Separate data semantics, state, and rendering.
3. Treat force layout as a configurable process, not a default truth.
4. Verify modern APIs and accessibility requirements.

## Connects To

- **ch12**: Determines whether custom implementation is justified.
- **ch17**: Defines visual property mappings.
- **ch18**: Defines interaction and mental-map requirements.
