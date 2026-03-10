---
name: academic-literature-review-pipeline
description: Run a full academic literature-review workflow by chaining research-paper-scout, related-work-writer, academic-draft-polish, and optionally paper-figure-builder. Use when the user wants one-shot execution of paper scouting, related-work drafting, bilingual academic polishing, and optional figure-note preparation without manually invoking each skill.
---

# Academic Literature Review Pipeline

Use this as the single entrypoint for the full academic writing flow.

## Workflow

1. Start with `research-paper-scout` to collect and structure papers.
2. Create a fresh run folder according to `references/run-folder-convention.md`.
3. Save the scouting result into that run folder when persistent output is useful.
4. Pass the paper cards or note file into `related-work-writer`.
5. Produce a related-work draft, usually with Chinese academic prose plus English technical anchors.
6. Pass the draft into `academic-draft-polish` for polished English + academic Chinese rendering.
7. If the user asks for a figure, call `paper-figure-builder` and produce a bilingual figure note.
8. Return the final outputs with clear file paths inside the run folder.

## Rules

- Prefer this pipeline when the user wants the whole chain, not a single step.
- Do not force all stages if the user only needs scouting or polishing.
- Keep bilingual output consistent with the default bilingual templates of the downstream skills.
- Prefer file-based handoff for long literature notes and drafts.

## Read More

- Read `references/pipeline-contract.md` before running the full flow.
- Read `references/run-folder-convention.md` before creating artifacts for a run.
- Read `references/call-template.md` for the recommended user-facing invocation format.
