# WORKFLOWS.md

## Academic Literature Review Flow

1. Run `academic-literature-review-pipeline` or start with `research-paper-scout`
2. Create a topic folder under `research/<topic-slug>/`
3. Inside it, create a fresh run folder under `research/<topic-slug>/academic/<run-id>/`
4. Save scouting, draft, and polished outputs into that same academic run folder
5. Optionally run `paper-figure-builder`

## Coding Fix Flow

1. Run `coding-fix-pipeline` or start with `repo-coding-assistant`
2. Reuse or create the topic folder under `research/<topic-slug>/`
3. Inside it, create a fresh coding run folder under `research/<topic-slug>/coding/<run-id>/`
4. Save repo plan, raw validation log, and final report into that same coding run folder

## Multi-Agent Usage

Use `multi-agent-research-pipeline` only when the task is clearly decomposable and benefits from explicit role separation.
