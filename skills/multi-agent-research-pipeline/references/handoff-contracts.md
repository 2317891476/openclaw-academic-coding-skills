# Handoff Contracts

Use these handoff objects between skills.

## research-paper-scout -> related-work-writer
- topic
- language
- organization_mode
- paper_cards_path or inline paper cards

## related-work-writer -> academic-draft-polish
- section_type=related_work
- source_text
- style_goal
- language

## repo-coding-assistant -> code-implement-test-loop
- task
- repo_path
- likely_files
- validation_command
- constraints

Rules:
- Prefer file-path handoff for long outputs.
- Prefer inline handoff only for short summaries.
- Keep the receiver inputs explicit; do not require the next skill to infer hidden state.
