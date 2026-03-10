# Run Folder Convention

For every coding-fix-pipeline execution, create a fresh run folder.

Recommended path:

- `reports/code-loop/runs/<YYYYMMDD-HHMMSS>-<repo-slug>-<task-slug>/`

Expected artifacts:
- `repo-plan.md`
- `validation-log.json`
- `final-report.md`

Rules:
- This pipeline should be the owner of the run folder.
- Upstream and downstream stages should write into the same run folder.
