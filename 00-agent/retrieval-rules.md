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
- Use `../Projects` for formal project documents; link to those docs rather than duplicating them here.
- For all agents, use `Projects/projects/<project-slug>/` as the durable home for project outputs and project learnings when a project exists.
- Store formal outputs in the relevant project folder: research reports, product briefs, architecture briefs, implementation plans, decision records, test plans, project READMEs, handoff packages, and durable lessons learned.
- Use RAG/memory search before starting project work so existing second-brain context, prior research, decisions, and lessons are reused.
- Future isolated agents must have memory search access to `/home/cef-admin/.openclaw/workspace/second-brain`; do not rely only on relative `second-brain` paths from each agent workspace.
- Put marketing requests, audience research, campaign ideas, channel research, and marketing drafts in `Research/` unless Chris explicitly asks for a formal second-brain/Projects document.
- Do not copy `.git` directories, remotes, account URLs, or repository credentials into second-brain research notes when moving or summarizing second-brain/Projects material.
- Write quick captures to `Inbox/` or `Daily/`.
- Distill durable facts into `Projects/`, `People/`, and `Decisions/`.
- Update memory on meaningful boundaries: decisions, corrections, project-state changes, task completion, and compaction flushes.
