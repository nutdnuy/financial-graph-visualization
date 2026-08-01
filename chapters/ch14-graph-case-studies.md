# Chapter 14: Graph Visualization Case Studies

## Core Idea

Graph patterns become useful only when tied to a domain hypothesis. Hubs, bridges, clusters, repeated shared devices, and unusual link patterns can direct investigation in intelligence, fraud, cyber security, and marketing, but they are leads rather than automatic proof.

## Frameworks Introduced

- **Zoomed-Out Pattern -> Local Investigation**
  - When to use: Large networks where the first task is locating suspicious or influential regions.
  - How: View broad structure; identify hubs, bridges, clusters, isolates, or unusual motifs; filter and zoom; inspect underlying records.
- **Fraud Starburst Heuristic**
  - When to use: Transaction or review networks.
  - How: Look for many accounts tied to one device, IP, merchant, or destination; compare with normal behavioral patterns; verify timestamps and records.
- **Bridge/Hold-Together Node**
  - When to use: Intelligence, social, or organizational networks.
  - How: Use path/centrality measures and visual inspection to find nodes connecting communities; verify whether the connection is operationally meaningful.
- **Property-Enriched Graph**
  - When to use: Topology alone cannot distinguish entity types, severity, or behavior.
  - How: Bind type to shape/icon, group to color, importance to size, and relationship strength to width; expose exact attributes on demand.

## Key Concepts

- **Hub**: Node with many connections.
- **Bridge**: Node or link connecting otherwise separated regions.
- **Betweenness**: Structural measure associated with shortest-path bridging.
- **Starburst**: Hub-and-spoke motif that may indicate consolidation, coordination, or fraud.
- **Device fingerprint**: Technical identity signal that can connect apparently separate accounts.
- **Social graph**: Network of social interactions or connections.

## Mental Models

- A suspicious pattern is a query generator, not a verdict.
- Compare suspected motifs with a baseline of normal structure.
- Topology becomes more useful when joined with time, type, and value.
- Zooming changes detail, not evidence quality; always inspect source records.

## Anti-patterns

- Labeling a high-degree node fraudulent solely because it is central.
- Using color or size without domain-calibrated meaning.
- Ignoring missing data or link-generation rules.
- Showing all relationships when only a task-specific subgraph matters.
- Treating algorithmic community assignments as ground-truth categories.

## Worked Example

To investigate review fraud, model reviewer accounts, businesses, devices, IP addresses, and reviews. A cluster of many reviewers sharing one device/IP and targeting the same business within a short period is a stronger lead than any one attribute. Use icons for node type, link color for rating, width/count for repeated actions, and a time filter for submission velocity. Investigators then inspect the actual reviews and account metadata before making a determination.

## Reference Table

| Domain | Useful graph pattern | Required verification |
|---|---|---|
| Intelligence | Hubs, bridges, communities | Relationship meaning and source reliability |
| Payment/review fraud | Shared devices, accounts, merchants, starbursts | Transactions, timestamps, identity evidence |
| Cyber security | Unusual traffic, propagation paths, botnet clusters | Network logs and system state |
| Sales/marketing | Influencers, communities, engagement paths | Campaign, audience, and conversion data |

## Key Takeaways

1. Connect every pattern to a domain question and baseline.
2. Use topology, attributes, and time together.
3. Treat centrality and community detection as investigative aids.
4. Preserve access to underlying evidence.

## Connects To

- **ch15**: Implements centrality and communities in graph tools.
- **ch17**: Encodes types, importance, and relationship strength.
- **ch21**: Adds temporal evidence to event networks.
