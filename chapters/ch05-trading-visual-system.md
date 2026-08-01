# Chapter 5: Trading Visual System

## Core Idea

Redesign ticker, quote, and watchlist views as one coherent monitoring system. Use a shared visual element to connect current value, recent path, range, and direction without forcing users to re-learn each surface.

## Frameworks Introduced

- **Contrail**
  - When to use: Showing a current market value in the context of its recent path and range.
  - How: Place the current value as a prominent marker; attach a colored trail for prior values; set trail length to a declared time window; encode direction consistently.
- **Ticker-Quote-Watchlist System**
  - When to use: Designing related monitoring views at different densities.
  - How: Reuse the Contrail grammar from minimal ticker through detailed quote to comparative watchlist; increase detail without changing semantic mappings.
- **Iterative Information Reduction**
  - When to use: Modernizing text-heavy trading displays.
  - How: Ask which fields change decisions; separate status, change, technical indicators, and liquidity; test compact versions before adding fields.

## Key Concepts

- **Current marker**: The latest observed value.
- **Trail**: Ordered prior values connected to the current marker.
- **Range**: Declared bounds for interpreting current position.
- **Direction**: Consistent encoding of increasing/decreasing movement.
- **Monitoring**: Repeated rapid assessment rather than one-time explanation.

## Mental Models

- A monitoring mark is a sentence: current state, direction, recent path, and range.
- Repetition across surfaces builds fluency.
- Compactness is valuable only when the user can decode it at monitoring speed.
- Different time windows tell different stories; label the horizon.

## Anti-patterns

- Using the same color for direction, category, and alert severity.
- Showing a trail without a time horizon or scale.
- Filling a watchlist with indicators that do not change actions.
- Redesigning ticker, quote, and watchlist with unrelated visual grammars.
- Using animation that makes scanning or comparison unstable.

## Worked Example

A trader monitors 40 securities. Each watchlist row shows the current price marker on a daily range and a short trail of recent values. The selected security expands into a quote view that preserves the same marker/trail but adds day, month, 52-week, technical, volume, and spread context. A minimal ticker retains only symbol, percent change, and the compact state mark. Because the visual semantics remain stable, the trader can move between densities without relearning direction or alert meaning.

## Visual Reference

Inspect [reference 03](../references/visual-index.md) for the integrated ticker, quote, and watchlist anatomy.

## Key Takeaways

1. Reuse one grammar across monitoring surfaces.
2. Declare time window, scale, and direction semantics.
3. Prioritize scan speed and actionable exceptions.
4. Add detail progressively rather than compressing all fields into every row.

## Connects To

- **ch01**: Connects monitoring information to role-specific needs.
- **ch09**: Reuses stable components across fund communication channels.
- **ch21**: Extends time-aware thinking to dynamic networks.
