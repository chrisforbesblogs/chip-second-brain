---
type: operating-note
status: active
updated: 2026-05-31
tags:
  - agent
  - retrieval
---

# Retrieval Rules

- Use OpenClaw native `memory_search` before reading large files.
- Prefer targeted retrieval over loading whole folders.
- Use `rg` for exact terms, IDs, filenames, environment variables, and command output fragments.
- Treat Markdown files as canonical memory; treat indexes as disposable generated search layers.
- Keep `MEMORY.md` compact. Store detailed second-brain context in this vault.
- Use `../chip-projecthub` for formal project documents; link to those docs rather than duplicating them here.
- Write quick captures to `Inbox/` or `Daily/`.
- Distill durable facts into `Projects/`, `People/`, and `Decisions/`.
- Update memory on meaningful boundaries: decisions, corrections, project-state changes, task completion, and compaction flushes.

