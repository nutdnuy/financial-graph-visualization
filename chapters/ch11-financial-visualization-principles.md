# Chapter 11: Financial Data Visualization Principles

## Core Idea

Judge every financial visualization by three principles: cater to the audience, provide clarity, and be efficient. Accuracy is necessary but insufficient if the audience cannot decode, compare, or verify the result.

## Frameworks Introduced

- **Cater to the Audience**
  - When to use: Every design decision.
  - How: Define relevance, context, focus, likely follow-ups, delivery channel, and user sophistication. Offer multiple perspectives only when they answer real audience questions.
- **Provide Clarity**
  - When to use: Evaluating truthfulness and interpretability.
  - How: Use accurate data and scales; disclose calculations and source detail; minimize decoding; select chart forms that make comparison direct.
- **Be Efficient**
  - When to use: Reducing user effort.
  - How: Consolidate related views, prioritize visual hierarchy, label directly where practical, and remove elements that do not help the decision.
- **Focus Tilt**
  - When to use: The same data must answer short-term, long-term, rank, cumulative, average, or variance questions.
  - How: Preserve the data and context but change ordering, emphasis, or selected horizon; make the current tilt explicit.

## Key Concepts

- **Relevance**: Connection between displayed data and the user's decision.
- **Context**: Benchmark, time, peer, target, or category reference.
- **Transparency**: Visibility of definitions, calculations, and component data.
- **Accountability**: Ability to trace a statement to responsible source data.
- **Focus**: Deliberate guidance of attention to the primary signal.
- **Efficiency**: Analytical value delivered with minimal decoding and navigation effort.

## Mental Models

- Accurate but hard-to-compare is not clear.
- Context belongs behind the focal data, not in a competing foreground.
- Every visual element must explain, orient, distinguish, or enable action.
- The visualization should perform the comparison so the audience does not have to.

## Anti-patterns

- Pie charts with more than about five slices.
- Legends far from marks when direct labeling is possible.
- Decorative color, gradients, or shapes without data meaning.
- Truncated or inconsistent scales that exaggerate change.
- Aggregates without calculation or source disclosure.
- A single perspective presented to audiences with different responsibilities.

## Worked Example

A mutual-fund performance view is accurate but uses three overlapping lines, a remote legend, and no peer distribution. Improve audience relevance by showing the fund and category comparison appropriate to the user's question. Improve clarity by using a direct label and a muted quartile backdrop. Improve efficiency by removing redundant grid lines and exposing exact values only on selection. Offer a focus tilt between absolute growth and peer-relative position while keeping period and benchmark stable.

## Reference Table

| Principle | Test |
|---|---|
| Audience | Does the view answer this role's decision and follow-ups? |
| Clarity | Are data, scale, comparison, calculation, and provenance unambiguous? |
| Efficiency | Can the user identify the signal and act without unnecessary decoding? |

## Key Takeaways

1. Evaluate audience, clarity, and efficiency together.
2. Accuracy alone does not guarantee correct understanding.
3. Use context and focus to guide interpretation without hiding evidence.
4. Remove visual elements that do not earn attention.

## Connects To

- **ch01**: Grounds audience-specific information delivery.
- **ch09**: Demonstrates context backdrops and focus tilts.
- **ch17**: Applies the same principles to graph encodings.
