# Chapter 15: An Introduction to Gephi and KeyLines

## Core Idea

Select graph tools according to user, workflow, deployment, scale, interactivity, licensing, and customization. The source contrasts a desktop exploration tool with a browser-embedded commercial component; the broader decision framework remains useful even though current product details must be reverified.

## Frameworks Introduced

- **Desktop Exploration vs Embedded Application**
  - When to use: Choosing between analyst tooling and a product feature.
  - How: Prefer an exploration environment for data scientists iterating on files, filters, metrics, and layouts. Prefer an embeddable component when end users need a controlled workflow inside a web application.
- **Tool Trade-off Matrix**
  - When to use: Comparing graph stacks.
  - How: Score deployment, data connection, interaction, customization, scale, support, licensing, team skills, accessibility, and maintainability.
- **Graph Refinement Loop**
  - When to use: Turning a raw graph into an interpretable one.
  - How: Import/model -> choose layout -> filter -> compute metrics -> bind size/color -> label -> rerun layout -> inspect errors and source records.
- **Centrality + Community Styling**
  - When to use: Exploring influence and groups.
  - How: Compute a documented metric; scale nodes appropriately; run community detection; assign categorical colors; inspect boundary cases and false interpretations.

## Key Concepts

- **Gephi**: Desktop open-source graph exploration environment described by the source.
- **KeyLines**: Commercial JavaScript graph component described by the source.
- **Eigenvector centrality**: Importance influenced by connections to other important nodes.
- **Modularity/community class**: Group assignment based on link structure.
- **Pajek/GraphML/JSON**: Example interchange or application formats.
- **Layout iteration**: Re-running layout after filtering or styling changes.

## Mental Models

- An analyst tool and a production application optimize for different users.
- Tool capability does not replace graph-model or visual-design decisions.
- Automated metrics and communities need semantic validation.
- A static export can be sufficient for one analyst; a governed interactive app requires product engineering.

## Anti-patterns

- Selecting a stack from a feature list without a deployment/user model.
- Shipping an analyst interface directly to nontechnical users.
- Encoding centrality as size without naming the metric.
- Accepting a community assignment without inspecting cross-group links.
- Relying on source-era versions or APIs without current verification.

## Worked Example

A social-media debate network is imported into an exploration tool. A force-directed layout reveals structure; low-degree isolates are filtered; eigenvector centrality controls node size; community detection controls categorical color. The resulting groups and influential accounts are inspected against posts and user identities. For an internal monitoring product, the same logic is implemented through an embedded web component with curated filters, tooltips, access control, and a stable workflow rather than exposing the full analyst environment.

## Reference Table

| Requirement | Exploration tool | Embedded component/custom app |
|---|---|---|
| Primary user | Analyst/data scientist | Operational/end user |
| Deployment | Desktop/session | Browser/product |
| Data iteration | Fast manual import and tuning | Engineered APIs and data services |
| Interaction | Broad analyst controls | Curated task-specific controls |
| Customization | Plugins/settings | Code and product design |
| Governance/support | Community/process dependent | Vendor + internal engineering |

## Visual Reference

Inspect [reference 09](../references/visual-index.md) for a community-colored network after layout and centrality refinement.

## Key Takeaways

1. Choose tools from workflow and deployment constraints.
2. Keep modeling and design independent from product features.
3. Validate centrality and communities against domain evidence.
4. Verify current capabilities before implementing source-era examples.

## Connects To

- **ch12**: Supplies the value-complexity implementation gate.
- **ch16**: Defines the data models and interchange requirements.
- **ch23**: Provides a lower-level open-library path.
