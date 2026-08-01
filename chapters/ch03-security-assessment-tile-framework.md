# Chapter 3: Security Assessment and the Tile Framework

## Core Idea

Use a consistent Tile Framework to summarize heterogeneous securities while preserving asset-specific measures and drill-down. Comparison depends on normalized structure, not identical raw data.

## Frameworks Introduced

- **Profile and Results Tiles**
  - When to use: Comparing stocks, bonds, mutual funds, ETFs, or other entities with different defining metrics.
  - How: Put descriptive characteristics in a Profile Tile and investment outcomes in a Results Tile. Keep band order and visual syntax consistent; change measures only when the asset requires it.
- **Tile Schematic**
  - When to use: When a compact encoding is unfamiliar.
  - How: Label every band, scale, color, and drill-down location in a separate explanatory view. Do not force users to memorize undocumented encodings.
- **Tile Collection**
  - When to use: Scanning or comparing a list of securities.
  - How: Arrange equal-size Tiles in a stable grid; use the same order, range, and semantic color rules; make outliers visually detectable.
- **Summary Entry Point**
  - When to use: When users need fast triage before detailed analysis.
  - How: Surface distinguishing traits and results, then link each region to its source detail.

## Key Concepts

- **Profile Tile**: Compact description of characteristics such as category, style, capitalization, maturity, or credit.
- **Results Tile**: Compact outcome view such as performance, value/growth, risk, or ratings.
- **Normalization**: Aligning structure and scales so items can be compared.
- **Band**: Stable visual region assigned to one metric family.
- **Custom weighting**: Adjusting outcome emphasis to reflect a user's evaluation criteria while preserving definitions.

## Mental Models

- Think of a Tile as an index card with a fixed grammar, not a miniature dashboard.
- Adapt measures within a stable syntax; do not adapt the syntax for every measure.
- Use overview for selection and drill-down for conviction.
- Consistency is an analytical feature: it makes deviations visible.

## Anti-patterns

- Changing color direction or scale between securities.
- Putting all available metrics into the Tile.
- Mixing profile and outcome data without visual separation.
- Hiding definitions or data provenance behind a compact mark.
- Allowing user weights to change the underlying observations rather than only the evaluation.

## Worked Example

To compare a stock and an equity ETF, use the same Tile footprint and band order. The stock Profile Tile may encode sector, style, market capitalization, and regional exposure; the ETF Tile may encode mandate, style mix, diversification, and region. The Results Tiles can use aligned performance, risk, and rating bands. A yellow overlay may flag emerging-market exposure, but its meaning must remain identical across the collection. Selecting the risk band opens the appropriate underlying volatility, drawdown, or credit detail for that security type.

## Reference Table

| Component | Stable across entities | May vary by entity type |
|---|---|---|
| Tile size and band order | Yes | No |
| Color semantics and scale direction | Yes | Only with explicit warning |
| Metric definition | Within a band family | Yes, when required by asset type |
| Drill-down location | Yes | Detail content may vary |
| User evaluation weights | Interaction pattern | Weight values may vary |

## Visual Reference

Inspect [reference 01](../references/visual-index.md) when the exact Tile anatomy matters.

## Key Takeaways

1. Normalize grammar, not necessarily every metric.
2. Provide a schematic for unfamiliar compact encodings.
3. Keep overview linked to evidence.
4. Validate that customization preserves cross-entity comparison.

## Connects To

- **ch09**: Reuses component visualizations for mutual-fund communication.
- **ch10**: Contrasts disciplined Tiles with higher-density glyphs.
- **ch17**: Generalizes property-to-visual binding.
