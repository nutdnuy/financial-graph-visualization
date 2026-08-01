# Chapter 9: Mutual Funds

## Core Idea

Build mutual-fund communication from reusable components for allocation, fees, performance, and risk. Add benchmark, category, quartile, and historical context so investors can judge a value rather than merely read it.

## Frameworks Introduced

- **Core Component System**
  - When to use: Fact sheets, websites, plan-sponsor tools, and comparison interfaces.
  - How: Design allocation, fees, performance, and risk components once; keep definitions and visual grammar stable across channels; combine only the components needed for the audience.
- **Context Backdrop**
  - When to use: A fund value is meaningful only relative to peers or a benchmark.
  - How: Put category average, quartiles, or benchmark in muted background bands; foreground the fund; preserve the same context across related views.
- **Absolute + Relative Pairing**
  - When to use: Users need both the actual value and its peer-relative position.
  - How: Align an absolute chart with a relative or percentile view; use shared period and contextual bands.
- **Progressive Fund Comparison**
  - When to use: Comparing many funds.
  - How: Start with ranked compact components; highlight outliers; allow selection for a full fact sheet and detailed history.

## Key Concepts

- **Allocation profile**: Distribution across asset, sector, geography, or style.
- **Expense ratio**: Annual operating expense relative to fund assets.
- **Growth of investment**: Historical value of a hypothetical investment.
- **Quartile band**: Peer-distribution context divided into four groups.
- **Capture ratio**: Performance in up or down markets relative to a benchmark.
- **Risk metrics**: Measures such as alpha, beta, Sharpe, Sortino, and R-squared that require definition and context.

## Mental Models

- A fund fact sheet is a component system, not a page template.
- Context turns a statistic into a judgment.
- Relative and absolute views answer different questions; align rather than collapse them.
- Reuse builds user fluency across channels.

## Anti-patterns

- Pie charts with many allocation slices and difficult cross-fund comparison.
- Showing one fund's return without benchmark, peer, or horizon.
- Mixing trailing periods and calendar years without explicit labeling.
- Treating a risk metric as self-explanatory.
- Using different quartile colors or direction across components.

## Worked Example

A plan participant compares five funds. A compact comparison view shows allocation, fee, trailing return, and risk components in consistent columns. Selecting a fund opens a fact sheet where growth of $10,000 is paired with category average and quartile bands. A second aligned view shows the fund's relative position. The participant can distinguish a strong absolute return from a merely average peer-relative result and can see whether fees or downside capture alter the decision.

## Reference Table

| Component | Essential context |
|---|---|
| Allocation | Benchmark/category and time period |
| Fee | Category distribution and included/excluded charges |
| Performance | Benchmark, category, horizon, load/no-load convention |
| Capture | Up/down market definition and benchmark |
| Alpha/Beta/Sharpe/Sortino | Period, benchmark, risk-free rate, calculation method |
| R-squared | Benchmark and interpretation of closeness |

## Visual Reference

Inspect [reference 05](../references/visual-index.md) for a trailing-return view using aligned quartile context.

## Key Takeaways

1. Build reusable components around stable definitions.
2. Add peer, benchmark, and historical context before inviting judgment.
3. Pair absolute and relative views when both matter.
4. Keep time horizon and calculation conventions visible.

## Connects To

- **ch03**: Shares normalized component comparison.
- **ch06**: Extends performance and risk encodings.
- **ch11**: Applies audience, clarity, and efficiency.
