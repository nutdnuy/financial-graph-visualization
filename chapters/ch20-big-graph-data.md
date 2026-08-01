# Chapter 20: Big Data - When the Graph Is Too Large

## Core Idea

Do not attempt to display the entire dataset when the analytical question concerns a subset, group, or pattern. Use database-side filtering for scale, visual-side filtering for responsive control, and grouping for abstraction; acknowledge when a graph is no longer the right representation.

## Frameworks Introduced

- **Database-Side vs Visual-Side Filtering**
  - When to use: Choosing where to reduce data.
  - How: Query/aggregate server-side when the full graph exceeds client capacity; filter client-side when a bounded working set fits in memory and users need reversible exploration.
- **Hybrid Bounded Working Set**
  - When to use: Large systems with interactive analysis.
  - How: Query a relevant subgraph from the database; retain a limited cache in the client; allow fast visual filters inside that boundary; requery when scope changes.
- **Grouping/Combination**
  - When to use: Users care about departments, communities, sectors, or categories more than individuals.
  - How: Replace members with a group node; aggregate intergroup links; expose count/range; allow expansion for internal detail.
- **Graph Suitability Exit Rule**
  - When to use: Filtering and grouping still produce an unreadable view.
  - How: Switch to matrix, distribution, ranked table, flow summary, or query results; retain graph drill-down only where relational structure adds value.

## Key Concepts

- **Working set**: Data currently loaded for interaction.
- **Query filter**: Reduction performed before transfer/rendering.
- **Visual filter**: Reduction performed inside the client/tool.
- **Group node/combo**: Aggregate representation of several nodes.
- **Edge aggregation**: Combining many links into a summarized intergroup relationship.
- **Rendering limit**: Practical boundary imposed by memory, CPU/GPU, interaction latency, and human perception.

## Mental Models

- Human readability is usually a stricter limit than rendering capacity.
- Filter removes irrelevant items; group changes the analytical unit.
- A link can summarize thousands of events; document the aggregation.
- A graph is a query result, not a picture of the database.

## Anti-patterns

- Loading every record because the library benchmark allows it.
- Hiding nodes without indicating that data was filtered.
- Grouping without exposing member count or aggregation logic.
- Filtering only in the client when data exceeds memory or transfer budgets.
- Applying many filters whose interactions are invisible or irreversible.

## Worked Example

An email corpus contains millions of messages. Model people as nodes and aggregate repeated communications into weighted links for a selected period. Query only the relevant departments or investigation seeds from the database. In the client, let users adjust department and weight thresholds. Group remaining nodes by department to inspect interdepartment communication, then expand one department for detail. If the question becomes exact volume by department pair, switch to a matrix or table rather than forcing a dense network.

## Reference Table

| Method | Benefits | Costs |
|---|---|---|
| Database filtering | Handles large corpus; lowers transfer/render cost | Query latency; scope changes may require new query |
| Visual filtering | Fast reversible interaction; full working-set context retained | Limited by client memory/CPU and loaded data |
| Grouping | Reduces clutter while preserving aggregate relationships | Hides internal variation and can change interpretation |
| Sampling | Fast preview of structure | May miss rare paths, bridges, or communities |
| Alternative view | Better exact comparison or global structure | Loses local path intuition |

## Visual Reference

Inspect [reference 12](../references/visual-index.md) for the filtering trade-off table.

## Key Takeaways

1. Bound the graph before rendering.
2. Filter for relevance and group for abstraction.
3. Make reduction and aggregation visible.
4. Exit the node-link view when another form answers the question better.

## Connects To

- **ch16**: Defines aggregation and model boundaries.
- **ch18**: Uses progressive expansion and reversible controls.
- **ch22**: Requires aggressive filtering for geographic overlays.
