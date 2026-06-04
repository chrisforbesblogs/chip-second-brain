---
type: decision
status: accepted
date: 2026-05-31
tags:
  - decision
  - second-brain
  - openclaw
---

# Use Obsidian Vault Plus OpenClaw Native Memory Search

Decision:
- Use `second-brain/` as a normal Obsidian Markdown vault.
- Use OpenClaw native memory search to index `second-brain` and `second-brain/Projects`.
- Keep Markdown files as the canonical source of memory.
- Keep the vector/SQLite index disposable and rebuildable.
- Keep `second-brain/Projects` as the canonical location for formal project documents.

Rationale:
- Obsidian gives Chris a human-friendly interface: links, graph view, tags, daily notes, and review.
- OpenClaw native memory search gives ChipBoss hybrid retrieval without custom RAG infrastructure.
- Cross-linking avoids duplicating formal project documents into the second brain.

