---
type: agent-context
status: active
updated: 2026-05-31
tags:
  - agent
  - working-context
---

# Working Context

This vault is the Obsidian-facing second brain for ChipBoss/OpenClaw.

Current focus:
- Use Obsidian as the human-readable interface for second-brain notes.
- Use OpenClaw native memory search to retrieve from this vault and `../Projects`.
- Treat `Projects/projects/<project-slug>/` as the durable home for all formal project outputs, handoffs, and project learnings produced by agents.
- Require future agents to use RAG/memory search against this second-brain before starting project work.
- Keep Markdown files as the source of truth; the vector/SQLite index is generated and rebuildable.
- When ChipBoss changes this vault, commit and push meaningful updates to GitHub so Chris can pull them locally when needed.

Load this file first when second-brain context is needed. Search before reading broad sections of the vault.
