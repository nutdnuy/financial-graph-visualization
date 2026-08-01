# Chapter 16: Graph Data Modeling

## Core Idea

Translate source data into a graph model that matches the analytical question. Nodes, links, and properties can be derived from relational tables, key-value data, or graph databases; native graph storage reduces translation but does not eliminate semantic modeling.

## Frameworks Introduced

- **Question-to-Graph Translation**
  - When to use: Creating a graph from non-graph data.
  - How: Define the entities that matter; define meaningful relationship events; decide direction, weight, multiplicity, and time; attach only properties needed for reasoning or interaction.
- **Model Variants**
  - When to use: One source supports several analytical units.
  - How: Create alternative models; state what each preserves and hides; test representative queries before committing.
- **Source-to-Visualization Pipeline**
  - When to use: Designing an application architecture.
  - How: Source database -> query/transform -> graph object or interchange format -> visual encoding/layout -> interaction -> evidence lookup.
- **Native vs Translated Graph**
  - When to use: Selecting data storage and query strategy.
  - How: Use native graph storage when relationship traversal is operationally central; retain relational or document storage when the graph is one analytical projection and translation cost is acceptable.

## Key Concepts

- **Relational model**: Tables joined through keys.
- **Key-value/document model**: Flexible records with named attributes.
- **Graph model**: Nodes, links, and properties.
- **Graph database**: Stores relationships as first-class structures.
- **Direction**: Ordered source-to-target meaning.
- **Weight**: Numeric relationship strength, count, value, or probability.
- **Multiplicity**: Whether repeated events are separate links or aggregated.

## Mental Models

- The visual graph is an analytical projection of the source.
- Shared keys can create relationships, but only domain meaning makes them useful.
- Aggregate repeated events when the question is durable relationship strength; retain events when sequence and time matter.
- Storage choice and visualization choice are separate architecture decisions.

## Anti-patterns

- Making every row a node and every join a link without a question.
- Aggregating event links and then claiming temporal behavior.
- Dropping direction or weight during interchange.
- Conflating database schema with the best user-facing model.
- Assuming native graph storage removes the need to define semantics.

## Worked Example

A trade database contains accounts, instruments, counterparties, timestamps, and amounts. For counterparty exposure, model accounts and counterparties as nodes and aggregate trades into weighted directed links by period. For suspicious-trading sequences, keep individual trade events or model transactions as nodes so time and path order remain available. The first model is compact and efficient for exposure; the second is larger but supports event-chain investigation.

## Reference Table

| Modeling choice | Preserve | Hide/cost |
|---|---|---|
| Aggregate events into weighted link | Relationship strength, compactness | Individual sequence and event detail |
| Keep each event as link | Time and transaction detail | Parallel-edge complexity |
| Transaction as node | Rich event attributes and multi-party links | More nodes and paths |
| Fund-to-security bipartite graph | Exact shared holdings | Harder direct fund comparison |
| Projected fund-to-fund graph | Similarity/overlap | Which security created the link |

## Key Takeaways

1. Let the question determine entity and relationship semantics.
2. Document direction, weight, multiplicity, and time.
3. Compare model variants before optimizing storage.
4. Preserve a route from visual marks to source records.

## Connects To

- **ch13**: Establishes the graph suitability test.
- **ch20**: Uses aggregation and query boundaries to manage scale.
- **ch21**: Requires explicit temporal semantics.
