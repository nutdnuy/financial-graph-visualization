# Chapter 18: Creating Interactive Graph Visualizations

## Core Idea

Use interaction to navigate complexity, preserve context, and reveal details progressively. Interaction is not decoration: every control should help users locate, understand, compare, or verify relationships.

## Frameworks Introduced

- **Navigate -> Select -> Inspect -> Expand**
  - When to use: Graphs beyond trivial size.
  - How: Provide pan/zoom; make selection state obvious; show node/link details; allow expansion into adjacent data while retaining the current context.
- **Declutter by Progressive Disclosure**
  - When to use: Labels and attributes obscure structure.
  - How: Keep essential visual properties visible; use tooltips or detail panels for secondary attributes; reveal labels according to zoom/selection.
- **Progressive Expansion**
  - When to use: The complete network is too large to load or comprehend.
  - How: Start from a relevant seed or query result; let users expand neighbors; record expansion history and provide reset/backtracking.
- **Animation with Mental-Map Protection**
  - When to use: Showing a meaningful transition or state change.
  - How: Keep duration short, preserve identity and spatial continuity, and allow interruption; remove animation when it adds no explanatory value.
- **Touch-First Interaction Review**
  - When to use: Mobile or touch delivery.
  - How: Replace hover-only detail, enlarge targets, reduce simultaneous nodes, and test gestures and occlusion.

## Key Concepts

- **Navigation**: Pan, zoom, search, and focus movement.
- **Tooltip/detail panel**: Secondary information revealed after selection.
- **Progressive expansion**: Loading or revealing adjacent nodes on demand.
- **Mental map**: User's remembered spatial arrangement and identity mapping.
- **Selection state**: Persistent indication of the current node, link, group, or path.
- **Touch target**: Interactive area large enough for reliable touch input.

## Mental Models

- The initial graph is an entry point, not the entire database.
- Surface encodings help users decide where to interact.
- Every expansion increases cognitive and rendering load; make it reversible.
- Stable identity and position are more valuable than gratuitous motion.

## Anti-patterns

- Hover-only information on touch devices.
- Expanding the graph without a visible history or reset.
- Moving every node after each small interaction.
- Putting all metadata into labels to avoid building details-on-demand.
- Adding animation because the library supports it.
- Allowing selection to disappear after filter/layout changes.

## Worked Example

An investigation starts from one suspicious account. The initial view shows the account and first-degree counterparties. Selecting a node opens a detail panel with amount, type, and timestamps. An "expand" action adds the next relevant neighbors while preserving prior positions as much as possible. Filters restrict the period and transaction type. A path view highlights how value moved between selected accounts. The user can collapse additions or return to the seed state.

## Reference Table

| User need | Interaction |
|---|---|
| Find an entity | Search and focus |
| Inspect precise attributes | Selection + tooltip/detail panel |
| Follow a relationship | Highlight path/neighbors |
| Work with bounded data | Progressive expansion |
| Reduce surface clutter | Zoom-dependent labels and details on demand |
| Compare states | Stable selection and coordinated views |

## Key Takeaways

1. Give every interaction an analytical purpose.
2. Preserve selection, identity, and navigation history.
3. Reveal data progressively instead of loading the universe.
4. Design separately for mouse and touch behavior.

## Connects To

- **ch10**: Uses overview, zoom, filter, details, and compare.
- **ch20**: Adds explicit filtering/grouping for scale.
- **ch21**: Applies interaction to time-varying graphs.
