# Handoff From Repo Coding Assistant

Expected upstream inputs:
- task
- repo path
- likely files
- validation plan
- constraints

When receiving a plan:
1. Start from the smallest high-confidence file set.
2. Use the validation plan if available; otherwise ask for one or infer a standard command cautiously.
3. Preserve stated constraints during the repair loop.
4. Mention if the implementation loop needs to expand beyond the original plan.
