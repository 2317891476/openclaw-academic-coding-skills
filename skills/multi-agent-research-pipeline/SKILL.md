---
name: multi-agent-research-pipeline
description: Orchestrate complex research or coding tasks across multiple specialist subagents such as researcher, writer, reviewer, coder, and tester. Use when a single session would be overloaded and the task benefits from explicit delegation, file-based handoff, and staged synthesis across multiple skills.
---

# Multi-Agent Research Pipeline

Delegate large tasks to specialist roles and merge the outputs.

## Workflow

1. Break the task into clear subproblems.
2. Choose the smallest viable workflow from `references/pipeline-patterns.md`.
3. Follow a concrete recipe from `references/workflow-recipes.md` when one fits.
4. Use explicit handoff objects from `references/handoff-contracts.md`.
5. Assign each subproblem to a specialist role.
6. Keep deliverables structured and narrow.
7. Merge outputs into a unified result.
8. Run a final reviewer pass for consistency.

## Rules

- Use only when the task is genuinely decomposable.
- Avoid spawning agents for trivial work.
- Give each subagent a bounded output contract.
- Prefer file-based handoff for long artifacts.
- End with a human-readable synthesis, not raw subagent dumps.

## Read More

- Read `references/role-patterns.md` before planning delegation.
- Read `references/pipeline-patterns.md` to choose a small, appropriate workflow.
- Read `references/workflow-recipes.md` when mapping a concrete task to a workflow.
- Read `references/handoff-contracts.md` before passing outputs between skills.
