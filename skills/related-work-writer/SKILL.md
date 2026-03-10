---
name: related-work-writer
description: Organize paper cards or literature notes into a coherent related-work section. Use when the user wants a related work draft, comparison of prior methods, clustering by method/timeline/task, or a literature review section instead of isolated summaries.
---

# Related Work Writer

Turn multiple paper cards into a structured related-work draft.

## Workflow

1. Validate the available source material using `references/input-contract.md`.
2. Read the provided paper cards or research notes.
3. Group papers by method, task, timeline, or benchmark depending on the topic.
4. Use `references/comparison-axes.md` to choose the most meaningful comparison dimensions.
5. Build a section outline before writing prose.
6. When the user wants Chinese output, use `references/bilingual-output.md` to keep useful English technical anchors while producing academic Chinese prose.
7. Write comparative paragraphs rather than one-paper-at-a-time summaries.
8. Highlight differences, limitations, and the opening for the user's work.

## Rules

- Avoid bibliography-shaped writing.
- Prefer synthesis over repetition.
- Preserve factual claims from source notes; do not add unsupported comparisons.
- If the notes are too thin, ask for more material or produce only an outline.

## Output Pattern

Default output:
1. Section outline
2. Related-work draft
3. Optional bullet list of missing citation gaps

## Read More

- Read `references/input-contract.md` before drafting.
- Read `references/handoff-from-scout.md` when the source material came from `research-paper-scout`.
- Read `references/organization-modes.md` to choose structure.
- Read `references/comparison-axes.md` before writing comparisons.
- Read `references/output-format.md` for the default section template.
- Read `references/bilingual-output.md` when the user wants Chinese-facing output with English technical anchors retained.
- Read `references/default-bilingual-template.md` to keep bilingual related-work output consistent.
- Use `references/save-convention.md` when saving a related-work draft into the workspace.
- Use `references/run-folder-convention.md` to keep the draft inside the current run folder.
