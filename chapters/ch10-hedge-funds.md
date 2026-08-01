# Chapter 10: Hedge Funds

## Core Idea

Use multivariate glyphs and interactive overview-to-detail workflows to compare hedge-fund exposures, characteristics, ranks, and strategy paths. Dense encodings are justified only when the audience can learn and repeatedly use them.

## Frameworks Introduced

- **Exposure Glyph System**
  - When to use: Comparing many long/short exposures or fund characteristics in a compact space.
  - How: Give each glyph part one stable property; provide a schematic; order and scale features consistently; test whether users can decode patterns faster than a table.
- **Visual Information-Seeking Mantra + Compare**
  - When to use: Interactive analysis of many strategies and funds.
  - How: Overview -> zoom -> filter -> details on demand -> compare. Keep selections, years, and strategy identity stable across steps.
- **Rank as a Temporal Property**
  - When to use: Evaluating whether top performance persists.
  - How: Show rank path, range, and underlying returns; distinguish one-year peak from consistency.
- **Familiar Metaphor with Capacity Limit**
  - When to use: An encoded object can make multivariate profiles memorable.
  - How: Use a familiar form only if its visual features map clearly to variables; stop adding features when recognition and comparison deteriorate.

## Key Concepts

- **Butterfly Bar**: Opposing quantities from a common origin, suited to long/short exposure.
- **Glyph**: Compact mark whose parts encode several properties.
- **Encoded glyph**: Familiar object with semantically assigned features.
- **Strategy rank**: Relative order that may vary materially over time.
- **Temporal path**: Connected positions showing how an entity moves across periods.
- **Bubble Plot**: Position, size, color, outline, and annotation layered on circles.

## Mental Models

- A compact glyph trades precision for pattern recognition.
- Ranking is a path, not a permanent label.
- Overview identifies where to look; details provide evidence.
- Comparison should stay available after every zoom or filter.

## Anti-patterns

- Encoding more characteristics than infrequent users can remember.
- Using a whimsical metaphor without measurable decoding benefit.
- Ranking funds without return magnitude, dispersion, or history.
- Showing only the best year or current rank.
- Letting zoom/filter remove all strategic context.

## Worked Example

An investment consultant reviews 100 funds across strategies and six years. The overview shows strategy averages and ranges. Selecting a strategy zooms to its funds, while a time filter moves among years and a temporal path shows persistence. Details-on-demand reveal fund AUM, firm AUM, and return. A comparison tray keeps selected funds visible across filters. For a smaller set of long/short funds, a glyph can encode exposure groups and magnitude, but the user must have access to a schematic and exact values.

## Reference Table

| Need | Pattern |
|---|---|
| Compare long vs short | Butterfly/diverging bar |
| Scan many multivariate profiles | Glyph with stable schematic |
| Assess rank consistency | Temporal rank path + range |
| Explore hundreds of funds | Overview, zoom, filter, details, compare |
| Show exact values | Table/detail panel alongside compact marks |

## Visual Reference

Inspect [reference 06](../references/visual-index.md) for a dense encoded fund glyph and its decoding burden.

## Key Takeaways

1. Use glyphs for repeated expert comparison, not universal communication.
2. Show rank history and magnitude, not only current order.
3. Preserve comparison through the information-seeking sequence.
4. Pair compact marks with exact details and definitions.

## Connects To

- **ch04**: Shares long/short and multivariate portfolio comparisons.
- **ch17**: Generalizes visual-property binding and audience calibration.
- **ch20**: Manages scale through filtering and grouping.
