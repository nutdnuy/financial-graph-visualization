# Chapter 4: Portfolio Construction

## Core Idea

Choose a visualization strategy according to the portfolio question: one focused view, one adaptable view, or several coordinated views. Asset allocation, sector analysis, overlap, and stress tests require different comparisons even when they share portfolio data.

## Frameworks Introduced

- **Singular Solution**
  - When to use: One encoding directly answers one stable question.
  - How: Keep the chart focused; examples include a surface view for allocation relationships or grouped heatmaps for factor comparison.
- **Multifaceted Solution**
  - When to use: The same chart grammar can answer follow-ups through ordering, pivoting, or orientation.
  - How: Preserve scales and marks while changing sort, grouping, row/column orientation, or selected period.
- **Varied Solution**
  - When to use: Different questions require materially different encodings.
  - How: Give each view a distinct job and link selections. For overlap, a butterfly view can support pair lookup while a histogram shows the distribution of all pair overlaps.
- **Portfolio Decision Chain**
  - When to use: Designing construction/risk views.
  - How: Move from allocation -> sector/industry -> security -> risk constraints; keep proposed and current states comparable.

## Key Concepts

- **Asset allocation**: Distribution across asset categories.
- **Sector leadership**: Relative performance or rank across sectors and periods.
- **Overlap of holdings**: Shared exposures between portfolios or funds.
- **Stress test**: Outcome under a specified adverse scenario.
- **Heatmap Groups**: Color-encoded quantities arranged into meaningful groups.
- **Tiered Histogram**: Distribution divided into interpretable bands.
- **Weighted Bubble Cluster**: Non-overlapping bubbles encoding size, rank, grouping, and attributes.

## Mental Models

- One dataset does not imply one view.
- Use a lookup view for specific pairs and a distribution view for portfolio-wide concentration.
- Keep current, proposed, and benchmark allocations on aligned definitions and scales.
- Treat risk views as inputs to construction, not isolated post-hoc reports.

## Anti-patterns

- Adding multiple charts that repeat the same comparison.
- Changing scale or category order between current and proposed portfolios.
- Using a heatmap without a documented color midpoint and direction.
- Using bubbles when precise pairwise comparison matters.
- Showing overlap as a list without indicating portfolio-wide concentration.

## Worked Example

A manager asks which fund pairs create concentrated overlap and whether overlap is a firm-wide problem. Use a butterfly or sorted pair view to identify the highest-overlap pairs. Add a tiered histogram to show whether those pairs are isolated or part of a broad concentration. A tiered scatter can relate overlap to another risk dimension, while the same selected pair remains highlighted. Do not combine all three encodings unless each answers a stated question.

## Reference Table

| Question | Useful form | Why |
|---|---|---|
| Which sector led each year? | Sorted Bar Track / aligned time view | Supports rank and period comparison |
| Which factors are positive or negative? | Heatmap Groups | Efficient scanning across groups |
| Which fund pair overlaps most? | Butterfly / sorted pair view | Precise pair lookup |
| Is overlap concentrated across the firm? | Tiered Histogram | Reveals distribution and bands |
| Which items dominate a multivariate set? | Weighted Bubble Cluster | Surfaces relative rank and groups |

## Visual Reference

Inspect [references 02 and 07](../references/visual-index.md) for the Heatmap Groups and overlap Butterfly examples.

## Key Takeaways

1. Assign one decision question to each view.
2. Preserve comparison across current, proposed, and contextual states.
3. Coordinate views when lookup and distribution questions differ.
4. Let risk analysis inform construction choices.

## Connects To

- **ch06**: Extends coordinated views to performance and attribution.
- **ch09**: Applies context and comparison to mutual funds.
- **ch12**: Evaluates whether a custom portfolio view merits the effort.
