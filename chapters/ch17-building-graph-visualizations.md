# Chapter 17: How to Build Graph Visualizations

## Core Idea

Design graph encodings for the user's sophistication and questions. Bind each visual property to one defensible data property, minimize decoding, and reserve secondary information for interaction rather than crowding the surface.

## Frameworks Introduced

- **Audience-Calibrated Encoding**
  - When to use: Choosing how much explanation and density to show.
  - How: Give expert users more direct property bindings and controls; give infrequent users fewer node types, clearer icons, direct labels, and guided interactions.
- **Property-to-Visual Binding**
  - When to use: Styling nodes and links.
  - How: Map numeric importance/count to node size, relationship strength to link width, category/community to color, type to shape/icon, and identity to concise labels.
- **Surface vs Selection Detail**
  - When to use: Many properties compete for attention.
  - How: Keep properties needed for finding/selecting nodes on the surface; move precise metadata and secondary attributes to tooltip/detail panels.
- **Legend Necessity Test**
  - When to use: Reviewing encoding clarity.
  - How: If the mapping is not self-evident, provide a nearby legend; if users must constantly consult it, simplify or use more intuitive marks.

## Key Concepts

- **Visual property**: Position, size, color, shape, icon, label, or link style.
- **Categorical color**: Distinguishes groups without implying order.
- **Ordered color**: Lightness/intensity used for magnitude under accessible contrast.
- **Node icon**: Shape or pictogram representing entity type.
- **Link width**: Encoding of relationship strength, count, or volume.
- **Glyph**: Composite mark encoding several properties.

## Mental Models

- Every visual channel is a scarce variable slot.
- Size suggests importance; use it only when that implication is true.
- Thick links suggest strong relationships; define what strength means.
- Labels identify; they should not become paragraphs on edges.

## Anti-patterns

- Using size for categories or arbitrary emphasis.
- Using a color gradient for unrelated groups.
- Placing long narrative labels on links.
- Encoding the same property differently across views.
- Using icons whose visual weight differs more than the encoded values.
- Providing many visual channels without a readable legend.

## Worked Example

For an influence network, size nodes by a named centrality or observed mention count, not by subjective importance. Use categorical color for community, link width for interaction count, and shape for account type. Keep node names visible only for focal/high-priority nodes and expose full metadata on selection. For nontechnical users, limit types and explain the mapping directly; for analysts, provide controls to switch metrics while updating the legend and title.

## Reference Table

| Visual property | Appropriate data role | Common failure |
|---|---|---|
| Node size | Numeric count/importance | Area differences misread; metric unnamed |
| Link width | Strength/volume | Direction or aggregation unclear |
| Categorical color | Membership/type | Too many categories or low contrast |
| Ordered lightness | Ordered magnitude | Confused with category |
| Shape/icon | Entity type | Decorative or unequal visual weight |
| Label | Identity/essential annotation | Clutter and overlap |

## Visual Reference

Inspect [reference 10](../references/visual-index.md) for the source's visual-property decision table.

## Key Takeaways

1. Map one property to one visual job.
2. Calibrate density and guidance to the audience.
3. Keep selection-critical information on the surface and details on demand.
4. Name metrics and document every encoding.

## Connects To

- **ch03**: Applies stable encoding grammar to security Tiles.
- **ch10**: Demonstrates the benefits and limits of dense glyphs.
- **ch18**: Moves secondary information into interaction.
