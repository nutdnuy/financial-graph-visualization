# Chapter 22: Graphs on Maps

## Core Idea

Overlay a graph on a map only when physical location or movement is central to the question. Geographic coordinates fix node position and remove much of the layout freedom that normally reduces crossings and clutter, so filtering and aggregation become essential.

## Frameworks Introduced

- **Geography-First Suitability Test**
  - When to use: Deciding whether to combine map and network views.
  - How: Confirm that proximity, route, region, or movement affects the decision. If geography is merely an attribute, use a separate map or filter instead of constraining the entire network.
- **Location Modeling Choice**
  - When to use: Representing places in a graph.
  - How: Choose between coordinates as node properties, explicit location nodes, or region membership links; state how moving entities and multiple locations are represented.
- **Map Overlay Reduction**
  - When to use: The overlay creates crossings and dense clusters.
  - How: Filter routes/nodes, group colocated entities, aggregate flows, cluster by zoom level, or separate overview and detail maps.
- **Geographic vs Topological Dual View**
  - When to use: Users need both physical and relationship structure.
  - How: Coordinate a map with a topology-optimized network; link selection and filters rather than forcing one view to answer both.

## Key Concepts

- **Coordinate property**: Latitude/longitude or projected position stored on a node.
- **Location node**: Explicit place connected to entities or events.
- **Route**: Link whose physical path matters.
- **Colocation**: Several entities sharing or nearly sharing coordinates.
- **Map mode**: View where geographic projection controls position.
- **Topological view**: Layout optimized for relationship structure rather than geography.

## Mental Models

- A map is a fixed layout with strong real-world semantics.
- Geographic closeness and network closeness are different relationships.
- Crossing routes scale poorly; aggregate or filter before drawing.
- Use coordinated views when one layout cannot serve both questions.

## Anti-patterns

- Putting a dense global network on a map without filtering.
- Assuming a node has one permanent location when the entity moves.
- Drawing straight links that imply a physical route the data does not contain.
- Letting overlapping nodes hide multiplicity.
- Using map position and then interpreting absence of clustering as absence of network communities.

## Worked Example

An airline network needs to compare route coverage and hub structure. The map view places airports geographically and aggregates flights into weighted route links, with filters for airline, period, and minimum frequency. A linked topological view uses force/radial layout to reveal hubs and communities without geographic constraints. Selecting an airport highlights it in both views. At national zoom, nearby airports may group; expansion restores individual airports.

## Reference Table

| Question | Representation |
|---|---|
| Which nodes are physically close? | Geographic map |
| Which paths or hubs are structurally central? | Topological graph |
| How much flows between regions? | Aggregated route/flow map |
| Where did an entity move over time? | Time-filtered trajectory with clear event semantics |
| What happens inside one dense city/region? | Zoom-dependent clustering and detail view |

## Visual Reference

Inspect [reference 14](../references/visual-index.md) for an example of a graph overlaid on a map.

## Key Takeaways

1. Require a geographic decision before using a map.
2. Model location explicitly and handle moving/multiple locations.
3. Filter and aggregate more aggressively than in free-layout networks.
4. Coordinate map and topological views when users need both meanings.

## Connects To

- **ch19**: Explains the layout freedom lost in map mode.
- **ch20**: Supplies filtering and grouping strategies.
- **ch21**: Adds time semantics to movement and route data.
