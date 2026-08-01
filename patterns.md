# Reusable Visualization Patterns

## Question-Led Visual Narrative

**When to use**: Any analytical dashboard, report, or presentation.<br>
**How**: Define audience and primary decision; list follow-up questions; make the first view answer the primary question; sequence context and detail views to answer follow-ups.<br>
**Trade-offs**: Different audiences may require different emphasis even with one data model.

## Normalized Entity Tiles

**When to use**: Comparing securities or entities with partly different characteristics.<br>
**How**: Separate Profile and Results; normalize band order and scales; provide a schematic; keep drill-down locations stable.<br>
**Trade-offs**: Over-normalization can hide asset-specific measures; uncontrolled customization destroys comparison.

## Context Backdrop

**When to use**: A focal value must be judged against peers, targets, or history.<br>
**How**: Render benchmark/quartiles/ranges in muted background layers; foreground the focal entity; use the same reference bands across related views.<br>
**Trade-offs**: Too much context can dominate the signal.

## Summary-to-Detail Decomposition

**When to use**: Users need both the result and its drivers.<br>
**How**: Present total/summary first; link to components through waterfall, drill-down, selection, or detail panels; preserve the total as context.<br>
**Trade-offs**: Detail-on-demand requires interaction or more screen space.

## Diverging Exposure View

**When to use**: Long/short, positive/negative, inflow/outflow, or above/below benchmark.<br>
**How**: Use a shared origin and opposing bars; keep scales symmetric when magnitude comparison matters; label sign clearly.<br>
**Trade-offs**: Symmetry may waste space for highly one-sided data.

## Coordinated Multiple Views

**When to use**: One dataset supports materially different questions.<br>
**How**: Assign one question to each view; align filters, scales, and highlighting; link selections across views.<br>
**Trade-offs**: More views increase attention and maintenance costs.

## Overview-Zoom-Filter-Details-Compare

**When to use**: Large fund collections, strategy rankings, or complex networks.<br>
**How**: Start with aggregate overview; allow zoom; expose filters; show metadata on demand; enable side-by-side or selected-item comparison.<br>
**Trade-offs**: The interaction model must remain visible and reversible.

## Property-to-Visual Binding

**When to use**: Node-link diagrams or multivariate glyphs.<br>
**How**: Bind size to count/importance, link width to strength, categorical color to group, shape/icon to type, and concise labels to identity. Document every mapping.<br>
**Trade-offs**: Each added encoding increases decoding effort.

## Topology-Aware Layout

**When to use**: Choosing a network arrangement.<br>
**How**: Inspect direction, hierarchy, focal nodes, density, and component structure; choose force-directed, hierarchy, radial, or circular accordingly; compare results before fixing a layout.<br>
**Trade-offs**: Automated layouts can imply meaning through proximity that the data does not contain.

## Filter vs Group

**When to use**: The network or chart is too dense.<br>
**How**: Filter when excluded items are irrelevant to the current question; group when clusters are the relevant analytical unit; let users restore or expand.<br>
**Trade-offs**: Filtering removes context; grouping hides within-cluster variation.

## Database-Side vs Visual-Side Filtering

**When to use**: Large interactive datasets.<br>
**How**: Query server-side when volume exceeds client capacity; filter client-side when fast reversible exploration matters; combine both for bounded working sets.<br>
**Trade-offs**: Server queries add latency; client filtering consumes memory and CPU.

## Temporal Small Multiples

**When to use**: Users must compare network or portfolio states across discrete periods.<br>
**How**: Freeze layout rules and scales; show ordered snapshots; highlight additions, removals, or changed properties.<br>
**Trade-offs**: Many periods consume space; inconsistent positioning breaks the mental map.

## Geographic Graph Overlay

**When to use**: Physical proximity or routes are central to the question.<br>
**How**: Model location explicitly; filter to a relevant subset; group colocated nodes; distinguish geographic placement from network topology.<br>
**Trade-offs**: A map fixes node position, causes crossing links, and limits layout optimization.

## Value-Complexity Implementation Gate

**When to use**: Selecting among visualization projects or delivery methods.<br>
**How**: Score business impact separately from implementation complexity; plot/rank projects; choose prebuilt, programmable, or custom solutions according to the combined position and strategic bias.<br>
**Trade-offs**: Scores are decision aids, not objective truth; weights must be disclosed.
