# Pipeline Contract

Default stage order:
1. `repo-coding-assistant`
2. `code-implement-test-loop`

Expected outputs:
- repo analysis / plan under `plans/` when saved
- validation loop report under `reports/code-loop/`

Minimum required inputs:
- task
- repo path
- validation command (preferred)

Fallback:
- if no validation command is given, infer a standard one cautiously or ask for it
