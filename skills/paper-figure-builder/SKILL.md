---
name: paper-figure-builder
description: Build controllable academic figures such as pipeline diagrams, architecture figures, experiment flowcharts, and caption drafts. Use when the user needs paper-ready Mermaid, Graphviz, SVG, or simple generated visuals that are editable and reproducible.
---

# Paper Figure Builder

Generate controllable paper figures before reaching for free-form image generation.

## Workflow

1. Determine the figure type: pipeline, architecture, comparison, experiment flow, or overview.
2. Extract nodes, relations, and grouping from the user's description.
3. Prefer Mermaid or Graphviz source for reproducibility.
4. Render to SVG or PNG when needed.
5. Draft a caption suitable for a paper figure.
6. When the user wants Chinese output, use `references/bilingual-output.md` and `references/default-bilingual-template.md` to keep figure notes bilingual while preserving concise in-figure labels.

## Rules

- Prefer editable vector-style outputs over opaque image generation.
- Optimize first for clarity, then for visual polish.
- Keep labels short and publication-friendly.
- If the structure is underspecified, ask for missing nodes or relations.

## Read More

- Read `references/figure-types.md` to choose an output style.
- Read `references/bilingual-output.md` when the user wants bilingual figure notes.
- Read `references/default-bilingual-template.md` to keep bilingual figure output consistent.
- Use bundled scripts when rendering is needed.
