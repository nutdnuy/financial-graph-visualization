# Chapter 2: Benefits of Using Visual Methods

## Core Idea

Use charts to externalize comparisons, expose relationships, and support conclusions that would require substantial mental computation from tables. A visualization should answer its stated question while making productive follow-up questions easier to pursue.

## Frameworks Introduced

- **Compare -> Connect -> Conclude**
  - When to use: Evaluating whether a proposed chart provides analytical value.
  - How: Confirm that users can compare relevant values, trace relationships or drivers, and reach an action or defensible conclusion.
- **Comparison Families**
  - When to use: Selecting an encoding for rank, attributes, or time.
  - How: Use ordered position/length for rank, aligned encodings for attributes, and stable x-time for historical change.
- **Connection Families**
  - When to use: Showing composition, influence, or association.
  - How: Use drill-down for aggregate-to-detail, networks for explicit relationships, and correlation views for statistical association. Do not treat correlation as causality.
- **Discovery Beyond Initial Intent**
  - When to use: Building exploratory analytics.
  - How: Anticipate common follow-ups, provide adjacent context, and preserve a path from observed pattern to underlying data.

## Key Concepts

- **Rank**: Ordered relationship among items.
- **Attributes**: Characteristics of an entity that may be encoded through multiple marks.
- **Time series**: Values arranged across discrete or continuous time.
- **Drill-down**: Navigation from an aggregate to its contributing records.
- **Network**: Explicit connections among entities.
- **Correlation**: Degree of association between variables, not proof of a causal mechanism.

## Mental Models

- A chart precomputes comparisons for the eye.
- The same dataset may need different views to answer what, when, how, and where.
- A useful visualization creates questions as well as answers; an effective interface makes those questions cheap to investigate.

## Anti-patterns

- Showing a chart that offers no analytical advantage over a small table.
- Encoding many attributes without a clear comparison task.
- Presenting an aggregate without access to its components.
- Using a network to imply influence when the data records only association.
- Treating visual memorability as evidence of analytical accuracy.

## Worked Example

An exception report begins as an unordered list of threshold breaches. First, rank exceptions by severity. Next, place counts and severity over time to determine whether the problem is worsening. Then compare exceptions with volume, season, or market conditions to test possible associations. Finally, enable inspection of the underlying events. One visualization does not need to contain every step; coordinated views can implement the sequence while preserving the selected exception and period.

## Reference Table

| User question | Useful visual operation |
|---|---|
| Which items lead or lag? | Sort and rank on an aligned scale |
| What changed and when? | Time series or small multiples |
| What composes this total? | Drill-down, waterfall, or linked detail |
| Which entities connect? | Node-link or matrix view |
| Do variables move together? | Scatter/correlation view with caveats |

## Key Takeaways

1. Require a comparison, connection, or conclusion from every analytical view.
2. Match the view to the question family.
3. Provide follow-up paths rather than overloading the first chart.
4. Keep statistical association separate from causal interpretation.

## Connects To

- **ch04**: Applies multiple view types to portfolio questions.
- **ch13**: Distinguishes graph exploration from communication.
- **ch18**: Adds interactive follow-up paths.
