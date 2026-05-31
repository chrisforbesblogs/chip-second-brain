---
type: project
status: active
updated: 2026-05-31
tags:
  - project
  - openclaw
canonical_docs:
  - ../../chip-projecthub/PROJECTS.md
  - ../../chip-projecthub/DECISIONS.md
---

# OpenClaw

OpenClaw is the local personal-agent runtime for ChipBoss.

Current memory architecture:
- `second-brain/` is the Obsidian-facing vault for lightweight memory, active context, people, decisions, daily notes, and capture.
- `../chip-projecthub` remains the place for formal project documents such as briefs, specs, implementation plans, research reports, and decision records.
- OpenClaw native memory search indexes both locations so relevant snippets can be retrieved without loading entire folders.

Related docs:
- [Project Hub projects](../../chip-projecthub/PROJECTS.md)
- [Project Hub decisions](../../chip-projecthub/DECISIONS.md)
- [[../00-agent/retrieval-rules|Retrieval rules]]

