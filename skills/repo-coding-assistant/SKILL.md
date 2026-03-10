---
name: repo-coding-assistant
description: Analyze a repository, locate implementation points, and plan safe code changes. Use when the user wants help understanding a codebase, finding where to modify behavior, producing a patch plan, or making a minimal-change implementation strategy before editing.
---

# Repo Coding Assistant

Understand the repository before changing it.

## Workflow

1. Read the task carefully and identify constraints.
2. Inspect repository structure, entrypoints, and relevant modules.
3. Trace the flow of data or control related to the requested change.
4. Build the plan using the guardrails in `references/plan-rules.md`.
5. Produce a small implementation plan with likely files and risk points.
6. Apply minimal edits only after the plan is clear.
7. Summarize what changed and what still needs verification.

## Rules

- Prefer minimal, compatible changes.
- Do not patch blindly when the entrypoint is unclear.
- Preserve existing public behavior unless the user asked to change it.
- When uncertainty is high, present the plan first.

## Output Pattern

Default output:
1. Repo understanding
2. Change plan
3. Applied changes
4. Risk notes
5. Next steps

## Read More

- Read `references/repo-analysis-checklist.md` before complex edits.
- Read `references/plan-rules.md` before proposing a patch plan.
- Read `references/output-template.md` when returning a structured repo analysis.
- Read `references/run-folder-convention.md` when saving plan artifacts for a coding run.
