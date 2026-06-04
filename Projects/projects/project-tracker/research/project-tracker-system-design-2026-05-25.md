# Project Tracker System Design

Date: 2026-05-25  
Project: `project-tracker`  
Workspace: `/home/cef-admin/.openclaw/workspace/second-brain/Projects`

## Executive Summary

Build the project tracker as a small internal app backed by plain files in the second-brain project structure. The MVP should prioritise durability, easy agent access, Git-friendly history, and simple human inspection over complex workflow automation.

Recommended approach:

- Use **YAML or JSON files as the source of truth** for projects, tasks, board stages, and activity log.
- Provide a **small CLI first** so agents like ChipThink and ChipCode can read and update tasks reliably.
- Add a **lightweight local web UI** after the data model and CLI are stable.
- Track the tracker itself as `projects/project-tracker`, with its own tasks on the same board.

This avoids dependency on an external SaaS tool while keeping a clear upgrade path to SQLite or a small API if task volume grows.

## Goals

- Maintain a register of all active and inactive OpenClaw projects.
- Track multiple tasks per project with status, owner agent, priority, dates, links, and notes.
- Support Kanban stages: `Backlog`, `Ready`, `In Progress`, `Blocked`, `Requires Review`, `Done`.
- Let agents read the current project/task state before working.
- Let agents safely update task status, append progress notes, and hand off work.
- Keep records easy for humans to inspect and edit in Markdown/YAML.
- Treat `project-tracker` itself as a normal tracked project.

## Non-Goals For MVP

- Full Jira/Linear replacement.
- Multi-user permissions.
- Cloud sync.
- Complex sprint planning.
- Automation that changes task status without an explicit agent action.
- Heavy database or hosted dependency before the workflow is proven.

## Recommended Data Model

Use one project register and one task file per project. This keeps global discovery fast while preventing one large task file becoming noisy.

### Project

```yaml
id: chip-postman
name: Chip Postman
status: active
stage: playable-prototype
priority: high
owner_agent: ChipCode
strategy_agent: ChipThink
project_path: /home/cef-admin/.openclaw/workspace/second-brain/Projects/projects/chip-postman
source_path: /home/cef-admin/projects/source-code/chip-postman
github_repo: https://github.com/chrisforbesblogs/chip-postman
current_focus: Improve core arcade loop and delivery features
next_milestone: Streak and parcel-type prototype
updated_at: 2026-05-25T16:04:00+01:00
tags:
  - game
  - mobile
```

Recommended project statuses:

- `idea`
- `active`
- `paused`
- `blocked`
- `shipped`
- `archived`

Recommended project stages:

- `idea`
- `research`
- `planning`
- `design`
- `prototype`
- `build`
- `testing`
- `release-prep`
- `launched`
- `maintenance`

### Task

```yaml
id: task-20260525-001
project_id: project-tracker
title: Define MVP tracker data schema
status: In Progress
priority: high
type: research
owner_agent: ChipThink
created_by: Vance
created_at: 2026-05-25T16:04:00+01:00
updated_at: 2026-05-25T16:04:00+01:00
due_at:
blocked_by: []
depends_on: []
links:
  - /home/cef-admin/.openclaw/workspace/second-brain/Projects/projects/project-tracker/research/project-tracker-system-design-2026-05-25.md
acceptance_criteria:
  - Data model covers projects and tasks
  - Board stages are explicit and reusable
  - Agent workflow is documented
notes:
  - 2026-05-25T16:04:00+01:00 ChipThink started research/design report.
```

Recommended task statuses:

- `Backlog` - captured but not ready to start.
- `Ready` - defined enough for an agent to pick up.
- `In Progress` - actively being worked.
- `Blocked` - cannot progress until a blocker is resolved.
- `Requires Review` - completed by an agent and waiting for human or peer review.
- `Done` - accepted or no further action required.

Recommended task priorities:

- `critical`
- `high`
- `medium`
- `low`

Recommended task types:

- `research`
- `product`
- `design`
- `engineering`
- `testing`
- `release`
- `ops`
- `admin`

## Recommended Folder And File Structure

Keep operational tracker data in `projects/project-tracker/data/`, while research, plans, and decisions follow the existing second-brain/Projects structure.

```text
/home/cef-admin/.openclaw/workspace/second-brain/Projects/projects/project-tracker/
  README.md
  research/
    project-tracker-system-design-2026-05-25.md
  product/
    tracker-mvp-prd.md
  implementation/
    plans/
      tracker-mvp-build-plan.md
  decisions/
    2026-05-25-file-backed-tracker.md
  data/
    board.yaml
    projects.yaml
    activity-log.ndjson
    tasks/
      project-tracker.yaml
      chip-postman.yaml
      football-betting-app.yaml
      compliance-tracker.yaml
      sports-prediction-model.yaml
      app-ideas.yaml
  tools/
    tracker-cli/
      README.md
      package.json
      src/
```

### Core Files

`data/board.yaml`

```yaml
stages:
  - Backlog
  - Ready
  - In Progress
  - Blocked
  - Requires Review
  - Done
rules:
  only_one_in_progress_per_agent: false
  require_note_on_blocked: true
  require_review_before_done: false
```

`data/projects.yaml`

```yaml
projects:
  - id: project-tracker
    name: Project Tracker
    status: active
    stage: research
    priority: high
    owner_agent: ChipThink
    project_path: /home/cef-admin/.openclaw/workspace/second-brain/Projects/projects/project-tracker
    source_path:
    current_focus: Define and build internal tracking MVP
```

`data/tasks/project-tracker.yaml`

```yaml
project_id: project-tracker
tasks:
  - id: task-20260525-001
    title: Produce tracker system design report
    status: Requires Review
    priority: high
    type: research
    owner_agent: ChipThink
```

`data/activity-log.ndjson`

```json
{"ts":"2026-05-25T16:04:00+01:00","agent":"ChipThink","action":"task.update","project_id":"project-tracker","task_id":"task-20260525-001","from":"In Progress","to":"Requires Review","note":"Research report completed."}
```

## MVP App Concept

The MVP is a local-first project board for humans and agents.

### Core User Story

As Vance, I want one place to see all OpenClaw projects, their current status, and the next tasks each agent is working on, so that multi-agent work does not become scattered across chats, reports, and source folders.

### MVP Capabilities

- Project register view across all hub projects.
- Per-project task list.
- Kanban board grouped by stage.
- Task detail view with owner, links, notes, blockers, and acceptance criteria.
- Agent-safe update command for changing status and appending notes.
- Activity log for recent changes.
- Basic filters by project, agent, priority, and status.

### Suggested MVP Commands

```bash
tracker projects list
tracker project show chip-postman
tracker tasks list --project chip-postman
tracker board --project chip-postman
tracker task show task-20260525-001
tracker task move task-20260525-001 "Requires Review" --agent ChipThink --note "Report completed"
tracker task add --project chip-postman --title "Prototype delivery streaks" --status Ready --priority high
```

## UI Views

### 1. Dashboard

Purpose: quick status across the whole workspace.

Content:

- Active project count.
- Blocked task count.
- Tasks requiring review.
- Recently updated projects.
- Agent workload by status.
- Top next actions.

### 2. Project Register

Purpose: single list of all projects.

Columns:

- Project
- Status
- Stage
- Priority
- Current focus
- Owner agent
- Last updated
- Open tasks
- Blocked tasks

### 3. Kanban Board

Purpose: operational task movement.

Columns:

- Backlog
- Ready
- In Progress
- Blocked
- Requires Review
- Done

Task card fields:

- Title
- Project
- Owner agent
- Priority
- Type
- Blocker indicator
- Updated date

### 4. Project Detail

Purpose: context before an agent starts work.

Sections:

- Project summary and paths.
- Current focus and next milestone.
- Open tasks.
- Recent activity.
- Key links.
- Decisions and reports.

### 5. Task Detail

Purpose: make task state explicit and handoffs clean.

Sections:

- Title, status, owner, priority, type.
- Description.
- Acceptance criteria.
- Links to files, reports, PRs, screenshots, or source repos.
- Blockers and dependencies.
- Notes/activity timeline.
- Status transition controls.

### 6. Agent Inbox

Purpose: each agent sees what it can work on.

Filters:

- Assigned to me.
- Ready tasks.
- In-progress tasks.
- Blocked tasks I own.
- Requires Review tasks I completed.

## Agent Workflow

Agents should treat the tracker as the working ledger for project state.

### Starting Work

1. Read `data/projects.yaml` to understand active projects.
2. Read the relevant `data/tasks/<project_id>.yaml`.
3. Select a task in `Ready` or continue a task assigned to the agent in `In Progress`.
4. Move the task to `In Progress` with an activity note.
5. Work in the appropriate project folder or source repo.

### During Work

Agents should update the task when:

- The task moves status.
- A blocker appears.
- A meaningful artifact is produced.
- A handoff is needed.
- Scope changes.

Agents should not silently overwrite another agent's active status update. The CLI should check file modification time or use a lock file during writes.

### Completing Work

Recommended default:

- Move to `Requires Review` when the agent believes the task is complete.
- Include links to produced files, changed source paths, screenshots, reports, or test output.
- Human or designated reviewer moves the task to `Done`.

For low-risk admin tasks, agents may move directly to `Done` if the task definition allows it.

### Blocked Work

When moving to `Blocked`, require:

- A blocker note.
- `blocked_by` entry if another task is responsible.
- Clear next action for unblocking.

Example:

```yaml
status: Blocked
blocked_by:
  - task-20260525-004
notes:
  - 2026-05-25T16:20:00+01:00 ChipCode blocked: waiting for API key decision.
```

## Implementation Options

### Option A: File-Backed CLI First

Build a Node or Python CLI that reads/writes YAML files and appends NDJSON activity events.

Pros:

- Fastest path.
- Git-friendly.
- Easy for agents to use.
- Human-readable data.
- No server required.

Cons:

- Needs write-lock discipline.
- Cross-file queries are limited.
- UI comes later.

Best for: first MVP.

### Option B: SQLite With CLI And Web UI

Use SQLite as the source of truth, with import/export to Markdown/YAML.

Pros:

- Better querying.
- Safer concurrent writes.
- Easier reporting.
- Strong base for a web UI.

Cons:

- Less human-editable.
- Needs migrations and backup conventions.
- Slightly heavier first build.

Best for: second phase if task volume or querying grows.

### Option C: Local Web App First

Build a small web app immediately, backed by JSON/YAML or SQLite.

Pros:

- Better human visibility.
- Drag-and-drop board is intuitive.
- Useful screenshots and reviews.

Cons:

- Slower first build.
- Agents still need CLI/API access.
- UI can distract from data correctness.

Best for: after CLI/data workflow works.

### Option D: External Tool Integration

Use Linear, GitHub Projects, Notion, or Trello and let agents update via APIs.

Pros:

- Mature UI.
- Mobile access.
- Notifications and collaboration built in.

Cons:

- External dependency.
- More auth and API handling.
- Project-hub source of truth becomes less clear.
- May be overkill for a local multi-agent workspace.

Best for: later sync/export, not MVP.

## Recommended First Build Plan

### Phase 1: Data Foundation

Deliverables:

- `data/board.yaml`
- `data/projects.yaml`
- `data/tasks/project-tracker.yaml`
- seed task files for current active projects
- `activity-log.ndjson`

Acceptance criteria:

- Every current project in `PROJECTS.md` exists in `projects.yaml`.
- Every task has `id`, `project_id`, `title`, `status`, `priority`, `type`, and `updated_at`.
- Board stages are defined once and validated.

### Phase 2: CLI MVP

Deliverables:

- `tracker projects list`
- `tracker tasks list`
- `tracker task show`
- `tracker task add`
- `tracker task move`
- validation for allowed statuses
- append-only activity log
- basic file lock during writes

Acceptance criteria:

- Agents can update a task without manually editing YAML.
- Invalid statuses are rejected.
- Every status change records agent, timestamp, old status, new status, and note.

### Phase 3: Human Board View

Deliverables:

- local web page or static generated HTML board
- dashboard counters
- project filters
- task cards grouped by stage
- link back to hub files

Acceptance criteria:

- Vance can see all active project tasks by status in under 10 seconds.
- Blocked and review-needed tasks are visually obvious.
- Board can be refreshed from current tracker data.

### Phase 4: Agent Workflow Integration

Deliverables:

- add tracker workflow notes to relevant agent instructions
- standard task handoff template
- optional `tracker next --agent ChipThink` command

Acceptance criteria:

- ChipThink and ChipCode can independently discover ready work.
- Completed work is consistently moved to `Requires Review`.
- Reports, source changes, and review requests are linked from task notes.

## First Tasks For Project Tracker

```yaml
project_id: project-tracker
tasks:
  - id: task-20260525-001
    title: Produce tracker system design report
    status: Requires Review
    priority: high
    type: research
    owner_agent: ChipThink
  - id: task-20260525-002
    title: Create initial tracker data files
    status: Ready
    priority: high
    type: engineering
    owner_agent: ChipCode
  - id: task-20260525-003
    title: Build tracker CLI commands for list, show, add, and move
    status: Backlog
    priority: high
    type: engineering
    owner_agent: ChipCode
  - id: task-20260525-004
    title: Generate first HTML Kanban board from tracker data
    status: Backlog
    priority: medium
    type: engineering
    owner_agent: ChipCode
  - id: task-20260525-005
    title: Add agent workflow notes for using tracker before and after tasks
    status: Backlog
    priority: medium
    type: ops
    owner_agent: ChipThink
```

## Recommendation

Start with **Option A: file-backed CLI first**.

The first build should create the tracker data files and a small CLI before any richer app UI. That gives agents a stable contract for reading and updating project state, keeps the system transparent in Git, and reduces the risk of building a polished board on top of an unproven workflow.

Once the CLI is reliable, generate a simple HTML Kanban board from the same data. Move to SQLite only if concurrent updates, reporting, or task volume make the file-backed model painful.
