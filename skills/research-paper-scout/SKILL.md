---
name: research-paper-scout
description: Search, triage, and summarize academic papers into reusable research cards. Use when the user asks for paper search, literature scouting, reading lists, arXiv/topic overviews, benchmark discovery, or structured research notes for later writing.
---

# Research Paper Scout

Search for papers and turn results into structured paper cards, not loose search notes.

## Workflow

1. Clarify the topic, keywords, time window, and desired output language if missing.
2. Use web tools to gather candidate papers; prefer primary sources such as arXiv, project pages, publisher pages, and benchmark repositories.
3. Select a manageable set with a bias toward recent relevant papers plus a few foundational works when useful.
4. Produce paper cards in a stable structure:
   - Title
   - URL
   - Year
   - Problem
   - Method
   - Dataset/Benchmark
   - Strengths
   - Limitations
   - Relevance
   - Read priority
5. Screen and rank papers using the rubric in `references/screening-rubric.md`.
6. When the user wants Chinese output, use `references/bilingual-output.md` to keep English records and add academic Chinese rendering.
7. End with a short synthesis: trends, gaps, and what to read first.

## Rules

- Prefer quality over count; avoid dumping long unranked lists.
- Distinguish primary papers from blog posts or secondary summaries.
- Do not invent citations, metrics, or claims that were not verified.
- When evidence is thin, say so explicitly.
- When the user is clearly building toward a survey or related-work section, keep terminology consistent across cards.
- When the user wants persistent notes, save them using `references/save-convention.md`.
- Prefer a fresh per-run folder using `references/run-folder-convention.md`.

## Output Pattern

Use the card format in `references/output-format.md`.

## Read More

- Read `references/query-design.md` before constructing search queries.
- Read `references/source-priority.md` when source quality is ambiguous.
- Read `references/output-format.md` before generating cards.
- Read `references/bilingual-output.md` when the user wants both English and Chinese output.
- Read `references/default-bilingual-template.md` to keep bilingual scouting notes consistent.
- Read `references/screening-rubric.md` when deciding what to keep.
- Read `references/synthesis-pattern.md` before writing the concluding synthesis.
- Use `references/research-note-template.md` when saving the result as a reusable note.
- Use `references/save-convention.md` when writing notes to the workspace.
- Use `references/run-folder-convention.md` when this run should create a new artifact folder.
