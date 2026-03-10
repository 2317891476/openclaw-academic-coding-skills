---
name: coding-fix-pipeline
description: Run a full coding-fix workflow by chaining repo-coding-assistant and code-implement-test-loop. Use when the user wants one-shot repository analysis, patch planning, validation-loop execution, and a final markdown repair report without manually invoking each skill.
---

# Coding Fix Pipeline

Use this as the single entrypoint for repository diagnosis + implement-test-fix flow.

## Workflow

1. Create or select a topic folder according to `references/run-folder-convention.md`.
2. Inside that topic folder, create a fresh coding run folder.
3. Start with `repo-coding-assistant` to understand the repository and locate likely patch points.
4. Produce a concise change plan and validation strategy.
5. Pass the plan into `code-implement-test-loop`.
6. Run the implement-test-feedback loop with explicit stop conditions.
7. Save the loop report inside that coding run folder when persistent output is useful.
8. Return the final status, patch summary, and report path.

## Rules

- Prefer this pipeline when the user wants the whole coding loop, not just repo analysis.
- Require or infer a validation command before running the loop.
- Stop cleanly when the loop hits its stop conditions; do not hide failures.
- Prefer markdown reports for persistent artifacts.

## Read More

- Read `references/pipeline-contract.md` before running the full flow.
- Read `references/run-folder-convention.md` before creating artifacts for a run.
- Read `references/call-template.md` for the recommended user-facing invocation format.
