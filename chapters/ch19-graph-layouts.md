# Chapter 19: How to Organize a Graph

## Core Idea

Choose a layout from graph topology and user task. A layout changes only visual position; it does not alter or prove relationships. Compare layouts deliberately and reject arrangements that imply structure the data does not support.

## Frameworks Introduced

- **Topology-to-Layout Decision**
  - When to use: Selecting the primary network arrangement.
  - How: Inspect direction, cycles, density, components, focal nodes, and hierarchy; match them to force-directed, hierarchy, radial, or circular layout.
- **Force-Directed Exploration**
  - When to use: Generic or unfamiliar networks where clusters, hubs, and isolates matter.
  - How: Set attraction/repulsion and iteration parameters; filter low-value data; inspect whether proximity is stable and meaningful; label the layout as algorithmic.
- **Hierarchy Layout**
  - When to use: Directed acyclic or nearly hierarchical data.
  - How: Select the root/apex, orient direction, manage cross-level edges, and inspect cycles or rule-breaking links.
- **Radial Focus**
  - When to use: Explaining reach from one or more focal nodes.
  - How: Place the focus centrally and organize others by connection distance; make the intentional bias explicit.
- **Bias-Aware Circular Layout**
  - When to use: Equal radial placement matters more than structural discovery.
  - How: Order nodes by group or another explicit rule; avoid implying that center absence means low importance.

## Key Concepts

- **Attractive force**: Pull between linked nodes in a force model.
- **Repulsive force**: Separation applied to nodes to reduce overlap.
- **Apex/root**: Starting node for a hierarchy.
- **Directed acyclic graph**: Directed structure with no cycles.
- **Layout bias**: Visual emphasis created by position independently of data magnitude.
- **3D layout**: Spatial arrangement with depth, often causing occlusion and size ambiguity.

## Mental Models

- Layout is a lens, not evidence.
- Center position is perceived as importance; use it intentionally.
- A clean hierarchy from cyclic data can be misleading.
- Keep data identity and selection stable when comparing layouts.

## Anti-patterns

- Using force-directed layout for a strict process hierarchy without testing alternatives.
- Using hierarchy when cycles and cross-links dominate.
- Using radial layout while claiming no focal bias.
- Using circular layout to discover structure it intentionally suppresses.
- Moving to 3D to "solve" overlap; occlusion and perspective often make comparison worse.
- Treating the most central-looking node as central without a metric.

## Worked Example

A transaction network has no known hierarchy. Start with force-directed layout to identify clusters and bridges. If the analyst selects one account and asks how counterparties are connected within two steps, switch to a radial focus centered on that account. If a separate ownership model forms a parent-subsidiary DAG, use a hierarchy for that model. Do not force all three tasks into one fixed layout.

## Reference Table

| Layout | Use when | Avoid when |
|---|---|---|
| Force-directed | Generic network, clustering, exploration | Exact path order or strict levels dominate |
| Hierarchy | DAG or near-hierarchical process/ownership | Cycles and cross-level links dominate |
| Radial | One focal node and reach matter | Equal emphasis is required |
| Circular | Equal radial status or group ordering | Structural proximity should reveal topology |
| 3D | Only with a validated spatial task and navigation | Ordinary network decluttering |

## Visual Reference

Inspect [reference 11](../references/visual-index.md) for the source's layout-selection discussion.

## Key Takeaways

1. Match layout to topology and question.
2. State intentional positional bias.
3. Compare candidate layouts on the same filtered data.
4. Do not interpret layout-generated proximity as a measured relationship.

## Connects To

- **ch15**: Implements layout iteration in tools.
- **ch18**: Preserves mental maps during layout changes.
- **ch22**: Shows how geographic position removes layout freedom.
