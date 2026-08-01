# Chapter 13: Getting to Know Graph Visualization

## Core Idea

Use graph visualization when relationships are central to the question. A graph is a model of entities and connections, not a chart type tied to a graph database; the same source data can support several graph models with different analytical consequences.

## Frameworks Introduced

- **Node-Link-Property Model**
  - When to use: Modeling explicit relationships among entities.
  - How: Define node identity and type; define link meaning, direction, weight, and multiplicity; attach properties needed for filtering and encoding.
- **Explore vs Communicate**
  - When to use: Establishing the purpose of a graph visualization.
  - How: For exploration, preserve flexible filtering, multiple layouts, and metadata. For communication, fix the question, highlight the relevant subgraph, and explain the encodings.
- **Graph Suitability Test**
  - When to use: Before choosing a node-link diagram.
  - How: Ask whether the conclusion depends on paths, hubs, communities, reach, dependencies, or relationship structure. If not, use a table or conventional chart.
- **Alternative Graph Views**
  - When to use: Node-link diagrams become dense or the task is global structure rather than individual paths.
  - How: Consider matrices, chord-like views, flow diagrams, or aggregated summaries according to the comparison required.

## Key Concepts

- **Node**: Entity such as person, account, security, device, company, or location.
- **Link**: Relationship or event connecting nodes.
- **Property**: Attribute on a node or link.
- **Path**: Sequence of links joining nodes.
- **Degree**: Count of incident links, adjusted for direction when applicable.
- **Component**: Connected subset of a graph.

## Mental Models

- A graph is one interpretation of data, not the data itself.
- Relationship semantics matter more than visual layout.
- A node-link view is good at paths and local structure but can fail at dense global comparison.
- Exploration can reveal a finding; communication should show only the structure needed to support it.

## Anti-patterns

- Using a graph merely because the source is a graph database.
- Creating links from weak shared attributes without analytical meaning.
- Mixing event links and durable relationships without distinction.
- Treating visual proximity as a measured relationship.
- Communicating a dense exploratory hairball without filtering or annotation.

## Worked Example

A portfolio holdings table contains funds and securities. One graph model uses funds and securities as two node types, with ownership links weighted by position size. It supports overlap and concentration questions. A second model creates fund-to-fund links weighted by shared holdings; it supports fund comparison but hides individual security paths. Both are valid, but the correct model depends on whether the user asks "which security creates this overlap?" or "which fund pair is most similar?"

## Reference Table

| Task | Node-link suitability |
|---|---|
| Trace a path or dependency | High |
| Find hubs or bridges | High |
| Compare exact values across hundreds of entities | Low without a companion chart/table |
| Inspect community structure | Medium/high with suitable layout and filtering |
| Show dense all-to-all relationships | Low; consider matrix/aggregation |

## Key Takeaways

1. Model relationships before drawing.
2. Choose exploration or communication intent.
3. Use node-link views for relational questions, not every dataset.
4. Change the model when the analytical unit changes.

## Connects To

- **ch14**: Shows relational questions across real domains.
- **ch16**: Details how to translate source data into graph models.
- **ch20**: Provides alternatives when scale defeats a node-link view.
