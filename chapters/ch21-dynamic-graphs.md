# Chapter 21: Dynamic Graphs - Showing Change Over Time

## Core Idea

Model time explicitly and choose a view that preserves comparison and the user's mental map. Use small multiples for stable state comparison, time filters for exploration, and dynamic properties for values that change independently of graph structure.

## Frameworks Introduced

- **Time-Semantics Check**
  - When to use: Adding time to a graph model.
  - How: Determine whether time describes a node's existence, a relationship event, a changing property, or a viewing window. In many event networks, timestamp links because the event is the connection.
- **Small Multiples**
  - When to use: Comparing discrete periods or scenarios.
  - How: Reuse layout rules, scales, encodings, and ordering; highlight additions/removals; keep snapshots aligned enough for visual comparison.
- **Time-Window Filtering**
  - When to use: Exploring events during a selectable interval.
  - How: Bind a time bar to node/link visibility; show the active interval; preserve selection where possible; update summaries with the filtered network.
- **Dynamic Property Model**
  - When to use: Node/link attributes change through time.
  - How: Store time-indexed values; separate structural appearance/disappearance from value changes; provide exact history in detail view.
- **Mental-Map Preservation**
  - When to use: Animating or stepping across periods.
  - How: Anchor stable nodes, minimize unnecessary movement, interpolate only meaningful changes, and let users pause or compare frames.

## Key Concepts

- **Event time**: Timestamp of a relationship occurrence.
- **Validity interval**: Period during which a node, link, or value is active.
- **Dynamic property**: Attribute with different values at different times.
- **Time bar/window**: Interactive control selecting the active interval.
- **Small multiple**: Aligned snapshot for one period.
- **Transition**: Visual change between states.

## Mental Models

- Time is part of data semantics before it is an animation.
- Animation is good for continuity; small multiples are better for direct comparison.
- A stable layout makes change visible; a fully recomputed layout can make motion dominate.
- Distinguish "relationship did not exist" from "relationship existed with zero value."

## Anti-patterns

- Putting timestamps on nodes when they describe link events.
- Recomputing positions so aggressively that users cannot track identity.
- Animating without a visible time indicator or controls.
- Comparing snapshots with different scales or filtering rules.
- Treating missing events as measured zero values.

## Worked Example

A communication network contains messages with sender, recipient, and timestamp. Model people as persistent nodes and communications as time-stamped links or aggregated links with event history. Use a time bar to select a week and update link weights and visible relationships. Provide small multiples for four selected weeks when direct comparison matters. Keep node identity and approximate position stable; use a detail panel for the exact message counts and period boundaries.

## Reference Table

| Need | Technique |
|---|---|
| Compare several fixed periods | Small multiples |
| Explore arbitrary windows | Time bar/filter |
| Show gradual property change | Dynamic property + controlled transition |
| Trace one entity through time | Stable selection + temporal path/history |
| Explain additions/removals | Highlight entering/exiting nodes and links |

## Visual Reference

Inspect [reference 13](../references/visual-index.md) for a time-filtered graph example.

## Key Takeaways

1. Define whether time belongs to nodes, links, properties, or windows.
2. Prefer small multiples for exact cross-period comparison.
3. Preserve identity and mental maps across transitions.
4. Expose the active period and missing-data semantics.

## Connects To

- **ch05**: Shares current-state plus historical-path reasoning.
- **ch18**: Supplies stable interaction and selection.
- **ch22**: Combines temporal and geographic filtering for movement networks.
