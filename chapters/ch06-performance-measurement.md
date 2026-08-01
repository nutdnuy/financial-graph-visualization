# Chapter 6: Performance Measurement

## Core Idea

Performance visualization must connect market, firm, and portfolio levels while making comparison, composition, and attribution legible. Reorganize data around the decision instead of preserving the reporting table's original layout.

## Frameworks Introduced

- **Reorganize, Group, Deliver, Remap**
  - When to use: Converting market maps, composites, gain/loss reports, and attribution tables into analytical views.
  - How: Reorder items for comparison; group related measures; reveal detail on demand; map values to a grid or coordinate system that exposes structure.
- **Familiar Base + Informative Extension**
  - When to use: Introducing new financial chart forms.
  - How: Begin with bars, stacked bars, treemaps, or quadrants; add one meaningful extension such as linked highlighting, a delta marker, or a second dimension.
- **Foreground/Background Context**
  - When to use: Showing positive/negative performance, ranges, or benchmarks.
  - How: Use muted context and clear focal marks; keep zero and sign semantics explicit.

## Key Concepts

- **Marimekko**: Rectangles using both height and width to encode quantity across categories.
- **Interlocking Blocks**: Connected blocks representing components and net result.
- **Linked Segmented Bar**: Coordinated stacked bars that highlight corresponding segments.
- **Hyperbolic Quadrants/Plane**: Coordinate system based on reciprocal relationships for ranking paired measures.
- **Bar Delta**: Bar plus triangle comparing two quantities or indicating rate of change.
- **Attribution**: Decomposition of portfolio return or risk into contributing decisions and exposures.

## Mental Models

- Attribution is a decomposition problem: always preserve the connection from total to components.
- Familiarity can carry one additional encoding; do not introduce many at once.
- Market, firm, and portfolio views should share definitions even when their granularity differs.
- Comparison improves when category order and baseline are deliberately chosen.

## Anti-patterns

- Leaving performance data in accounting/reporting order when the task is comparison.
- Encoding area without explaining both dimensions.
- Using linked highlighting with inconsistent category definitions.
- Mapping positive and negative performance to an unclear midpoint.
- Showing attribution components without reconciling them to the reported total.

## Worked Example

A return-attribution report contains sectors, allocation effect, selection effect, interaction, benchmark weight, and portfolio weight. Reorder sectors by total contribution rather than alphabetically. Use aligned bars around zero for contribution, and linked detail for weights and sub-effects. Keep the portfolio total and reconciliation visible. If a quadrant or hyperbolic view is added to rank return and risk jointly, provide an aligned table or labels so users can verify the precise values.

## Reference Table

| Form | Best use | Main risk |
|---|---|---|
| Marimekko | Composition across two dimensions | Area is harder to compare precisely |
| Linked segmented bars | Locate corresponding categories across views | Interaction must preserve identity |
| Hyperbolic plane | Rank paired measures with reciprocal structure | Unfamiliar geometry requires explanation |
| Bar Delta | Compare two quantities compactly | Triangle semantics may be misread |
| Interlocking Blocks | Explain components and net result | Dense blocks can overwhelm labels |

## Key Takeaways

1. Reorganize performance data for the analytical task.
2. Reconcile totals and components.
3. Extend familiar chart types one meaningful encoding at a time.
4. Keep context, zero, and sign explicit.

## Connects To

- **ch07**: Applies decomposition rigor to financial statements.
- **ch09**: Adds peer and quartile context to fund performance.
- **ch17**: Generalizes careful mapping from data properties to visual properties.
