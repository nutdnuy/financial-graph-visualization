# Chapter 12: Implementing Financial Visuals

## Core Idea

Choose implementation method and project priority by assessing business value separately from solution complexity, then combining them in a transparent Solution Score. Tool choice follows the value and constraints; it should not lead them.

## Frameworks Introduced

- **Business Value Assessment (BVA)**
  - When to use: Prioritizing visualization initiatives.
  - How: Score business criticality, external reach, internal reach, frequency of use, number of users, and any organization-specific factors. Apply disclosed weights that sum to one.
- **Complexity Assessment**
  - When to use: Estimating effort and delivery method.
  - How: Score uniqueness, channels, entitlements, localization, integration, interactivity, releases, refresh, and volume. Treat time and budget as planning outputs, not substitutes for value.
- **Solution Score**
  - When to use: Comparing projects across value and complexity.
  - How: Plot or rank the BVA and complexity results on a consideration grid; disclose weighting and strategic bias; use position to guide prebuilt, programmable, flexible, or custom delivery.
- **Delivery Method Spectrum**
  - When to use: Selecting tools and team.
  - How: Move from no-code/prebuilt to programmable/prebuilt to custom according to required uniqueness, control, integration, and interaction.

## Key Concepts

- **Business criticality**: Degree to which the solution changes decisions, efficiency, risk, revenue, or competitiveness.
- **Delivery channel**: Print, presentation screen, desktop, mobile, wearable, or installation.
- **Uniqueness**: Distance from supported conventional patterns.
- **Integration**: Number and difficulty of required data and application connections.
- **Strategic bias**: Deliberate weighting toward long-term business value or near-term ease/speed.

## Mental Models

- Build the mini-business case before selecting the stack.
- Value and complexity are independent axes; high complexity is not high value.
- Available budget is a constraint after priority, not evidence of priority.
- Scores support discussion; assumptions and weights remain visible.

## Anti-patterns

- Choosing a trendy library before defining the solution.
- Mixing value and effort into one opaque score.
- Treating high effort as proof of strategic importance.
- Ignoring maintenance, refresh, entitlements, localization, or integration.
- Using arbitrary weights without owner agreement.

## Worked Example

Compare three initiatives: a lobby ticker, a cash-flow statement redesign, and a performance-attribution application. Score each for criticality, reach, frequency, reuse, and users. Separately score uniqueness, channels, integration, interactivity, and data volume. Plot the scores. A high-value, moderate-complexity statement redesign may rank above a visually impressive ticker or a high-complexity attribution build. Use the result to select a prebuilt, programmable, or custom approach and to frame time and budget requirements.

## Reference Table

| Dimension | Example criteria |
|---|---|
| Business value | Criticality, external/internal reach, frequency, users, reuse |
| Complexity | Uniqueness, channels, entitlements, localization, integration, interaction, releases, refresh, volume |
| Delivery method | Prebuilt no-code, programmable component, open library, custom application |
| Governance | Weights, assumptions, maintenance, review, data ownership |

## Visual Reference

Inspect [reference 08](../references/visual-index.md) for the Solution Score value-complexity grid.

## Key Takeaways

1. Score value and complexity separately.
2. Disclose criteria, weights, and strategic bias.
3. Select the implementation method after understanding the project position.
4. Include maintenance and operating constraints in the decision.

## Connects To

- **ch15**: Applies implementation trade-offs to graph tools.
- **ch20**: Makes data scale an explicit complexity factor.
- **ch23**: Positions D3.js as a flexible but code-intensive option.
