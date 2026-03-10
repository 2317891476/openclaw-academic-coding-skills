---
name: code-implement-test-loop
description: Implement a code change, run tests or validation commands, analyze failures, and iterate toward a working patch. Use when the user wants an automated fix-test-feedback loop for bug fixing, feature implementation, regression repair, or repeated test-driven refinement.
---

# Code Implement Test Loop

Run an engineering loop, not a one-shot edit.

## Workflow

1. Confirm the task, repository path, test command, and iteration limit.
2. Validate the required inputs using `references/input-contract.md`.
3. Make the smallest sensible implementation step.
4. Run tests, lint, or build validation.
5. Analyze failures and classify them.
6. Iterate until success, stop condition, or manual handoff.
7. Apply `references/stop-conditions.md` explicitly when deciding whether to continue.
8. Summarize each round and the final state.

## Rules

- Require an explicit validation command whenever possible.
- Stop after the agreed iteration limit.
- Escalate for manual review when failures point to missing requirements, flaky tests, or large refactors.
- Do not silently keep looping.
- When the user wants a persistent artifact, save a loop report using `references/report-save-convention.md`.

## Output Pattern

Default output:
1. Iteration log
2. Final status
3. Patch summary
4. Remaining issues
5. Manual follow-up

## Read More

- Read `references/input-contract.md` before starting.
- Read `references/handoff-from-repo-assistant.md` when the plan came from `repo-coding-assistant`.
- Read `references/iteration-policy.md` before running multi-round repair.
- Read `references/stop-conditions.md` before deciding to continue or stop.
- Read `references/failure-classification.md` when summarizing failures.
- Read `references/output-template.md` before returning the final engineering summary.
- Read `references/report-save-convention.md` when saving loop reports to disk.
- Read `references/run-folder-convention.md` when creating a fresh run folder for this execution.
- Use `scripts/run_loop.py` as a deterministic helper when a simple repeated validation loop is enough.
- Use `scripts/render_report.py` to convert loop JSON into a markdown report.
