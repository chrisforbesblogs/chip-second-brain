# Project Folder Structure Implementation Plan

Date: 2026-05-25

## Goal

Organise all current and future work so that:

- OpenClaw memory/config stays in the OpenClaw workspace.
- Project collateral is captured in one clear second-brain project structure.
- Source code lives in separate Git repositories, one repo per buildable project.
- Research, mockups, decisions, assets, and implementation plans are easy to find.
- We avoid nested Git repositories inside a central repo.

## Recommended Top-Level Layout

Use the OpenClaw second-brain as the canonical project-collateral area, and `/home/cef-admin/projects-source-code` as the canonical buildable-source area.

```text
/home/cef-admin/.openclaw/workspace/second-brain/Projects/
  projects/                          # Project notes: planning, research, collateral, links
  docs/
  templates/

/home/cef-admin/projects-source-code/
  chip-postman/                      # Source repos live here, each with its own .git
  football-betting-app/
  compliance-tracker/
  sports-prediction-model/

/home/cef-admin/projects/
  archive/                           # Old prototypes, superseded experiments, snapshots
  sandbox/                           # Throwaway experiments and temporary spikes
```

Keep `/home/cef-admin/.openclaw/workspace` for OpenClaw's operating context:

```text
/home/cef-admin/.openclaw/workspace/
  AGENTS.md
  SOUL.md
  IDENTITY.md
  USER.md
  TOOLS.md
  MEMORY.md
  memory/
```

## Second-Brain Projects Repo

Create one GitHub repo for non-source collateral, for example:

```text
chrisforbesblogs/second-brain/Projects
```

Local path:

```text
/home/cef-admin/.openclaw/workspace/second-brain/Projects/
```

Suggested structure:

```text
second-brain/Projects/
  README.md
  PROJECTS.md
  DECISIONS.md
  docs/
    openclaw/
    server-setup/
    github/
  templates/
    project-readme.md
    decision-record.md
    implementation-plan.md
    research-report.md
  projects/
    chip-postman/
      README.md
      brief.md
      roadmap.md
      decisions/
      research/
      implementation-plans/
      mockups/
      assets/
      links.md
    football-betting-app/
      README.md
      brief.md
      roadmap.md
      decisions/
      research/
      implementation-plans/
      mockups/
      assets/
      links.md
    app-ideas/
      research/
      shortlist.md
      monetization-notes.md
    compliance-tracker/
      README.md
      research/
      mockups/
      links.md
    sports-prediction-model/
      README.md
      research/
      links.md
  archive/
    superseded-reports/
    old-mockups/
```

This repo should contain Markdown reports, plans, screenshots, mockups, diagrams, product notes, and links to source repos. It should not contain `node_modules`, `.expo`, build outputs, or live app source directories.

## Source Repo Pattern

Each source project should be a separate GitHub repo and local clone:

```text
/home/cef-admin/projects-source-code/chip-postman/              # Git repo
/home/cef-admin/projects-source-code/football-betting-app/      # Git repo
/home/cef-admin/projects-source-code/compliance-tracker/        # Git repo
/home/cef-admin/projects-source-code/sports-prediction-model/   # Git repo
```

Standard source repo structure:

```text
project-name/
  README.md
  .gitignore
  docs/
    architecture.md
    setup.md
    decisions/
  src/
  app/
  assets/
  tests/
  scripts/
  package.json / pyproject.toml / etc
```

For Expo/React Native apps:

```text
project-name/
  README.md
  .gitignore
  app.json
  package.json
  package-lock.json
  App.tsx
  src/
    components/
    screens/
    navigation/
    services/
    state/
    utils/
  assets/
    images/
    audio/
    fonts/
  docs/
    setup.md
    release.md
    decisions/
  tests/
```

`.gitignore` should exclude at least:

```text
node_modules/
.expo/
dist/
build/
.env
.env.*
```

## Current Workspace Mapping

Proposed migration from the current mixed workspace:

```text
/home/cef-admin/.openclaw/workspace/chip-postman
  -> /home/cef-admin/projects-source-code/chip-postman
  -> source repo: chrisforbesblogs/chip-postman

/home/cef-admin/.openclaw/workspace/parcel-post
  -> archive or merge into chip-postman after review
  -> likely old/sibling prototype

/home/cef-admin/.openclaw/workspace/reports/parcel-post-implementation-plan-2026-05-24.md
  -> second-brain/Projects/projects/chip-postman/implementation-plans/

/home/cef-admin/.openclaw/workspace/mockups/parcel-post-*.html
  -> second-brain/Projects/projects/chip-postman/mockups/

/home/cef-admin/.openclaw/workspace/reports/football-*.md
  -> second-brain/Projects/projects/football-betting-app/research/

/home/cef-admin/.openclaw/workspace/reports/football-*.html
  -> second-brain/Projects/projects/football-betting-app/mockups/

/home/cef-admin/.openclaw/workspace/reports/sports-betting-app-*.md
  -> second-brain/Projects/projects/football-betting-app/implementation-plans/

/home/cef-admin/.openclaw/workspace/sports-prediction-model
  -> /home/cef-admin/projects-source-code/sports-prediction-model if it contains useful source
  -> otherwise archive/sandbox

/home/cef-admin/.openclaw/workspace/compliance-tracker-mockup
  -> /home/cef-admin/projects-source-code/compliance-tracker if it is active source
  -> second-brain/Projects/projects/compliance-tracker/mockups/ for collateral snapshots

/home/cef-admin/.openclaw/workspace/expo-hello-world
  -> /home/cef-admin/projects/archive/expo-hello-world unless still needed

/home/cef-admin/.openclaw/workspace/reports/*app-ideas*.md
  -> second-brain/Projects/projects/app-ideas/research/

/home/cef-admin/.openclaw/workspace/agent-profiles
  -> separate private agent-profile backup repo, not second-brain/Projects

/home/cef-admin/.openclaw/workspace/TAILSCALE_REMOTE_ACCESS.md
/home/cef-admin/.openclaw/workspace/TELEGRAM_TOKEN_RESET.md
  -> second-brain/Projects/docs/server-setup/ if safe to share in GitHub
  -> otherwise keep private in OpenClaw workspace
```

## Implementation Phases

### Phase 1: Create GitHub Repos

Create these first:

```text
chrisforbesblogs/second-brain/Projects
chrisforbesblogs/chip-postman
```

Later, when active:

```text
chrisforbesblogs/football-betting-app
chrisforbesblogs/compliance-tracker
chrisforbesblogs/sports-prediction-model
```

### Phase 2: Create Local Directories

```bash
mkdir -p /home/cef-admin/projects-source-code
mkdir -p /home/cef-admin/projects/archive
mkdir -p /home/cef-admin/projects/sandbox
```

Clone the hub repo:

```bash
git clone git@github.com:chrisforbesblogs/second-brain/Projects.git /home/cef-admin/.openclaw/workspace/second-brain/Projects
```

Clone each source repo under `/home/cef-admin/projects-source-code/`:

```bash
git clone git@github.com:chrisforbesblogs/chip-postman.git /home/cef-admin/projects-source-code/chip-postman
```

### Phase 3: Add Hub Skeleton

Create the second-brain project structure folders:

```bash
mkdir -p /home/cef-admin/.openclaw/workspace/second-brain/Projects/{docs/openclaw,docs/server-setup,docs/github,templates,archive/superseded-reports,archive/old-mockups}
mkdir -p /home/cef-admin/.openclaw/workspace/second-brain/Projects/projects/{chip-postman,football-betting-app,app-ideas,compliance-tracker,sports-prediction-model}
mkdir -p /home/cef-admin/.openclaw/workspace/second-brain/Projects/projects/chip-postman/{decisions,research,implementation-plans,mockups,assets}
mkdir -p /home/cef-admin/.openclaw/workspace/second-brain/Projects/projects/football-betting-app/{decisions,research,implementation-plans,mockups,assets}
mkdir -p /home/cef-admin/.openclaw/workspace/second-brain/Projects/projects/app-ideas/research
mkdir -p /home/cef-admin/.openclaw/workspace/second-brain/Projects/projects/compliance-tracker/{research,mockups}
mkdir -p /home/cef-admin/.openclaw/workspace/second-brain/Projects/projects/sports-prediction-model/research
```

### Phase 4: Move Collateral First

Move reports, plans, and mockups into `second-brain/Projects` before moving source code. Commit this as the first clean organisational commit.

Do not move OpenClaw memory/config files into public GitHub unless explicitly intended.

### Phase 5: Move Source Code Repos

Move or reclone source projects into `/home/cef-admin/projects-source-code`.

For `chip-postman`, be careful: the current repo has uncommitted changes on branch `feature/audio-pass`:

```text
modified: App.tsx
modified: app.json
modified: package-lock.json
modified: package.json
untracked: gameAudio.ts
```

Before moving it, either commit those changes or copy the repo with its `.git` intact and verify status after the move.

### Phase 6: Add Cross-Links

Each hub project should have a `links.md` file:

```markdown
# Links

- Source repo: https://github.com/chrisforbesblogs/chip-postman
- Local source path: `/home/cef-admin/projects-source-code/chip-postman`
- Main planning folder: `/home/cef-admin/.openclaw/workspace/second-brain/Projects/projects/chip-postman`
```

Each source repo `README.md` should link back to the hub project folder/repo.

### Phase 7: Archive Old Experiments

Move obsolete prototypes to:

```text
/home/cef-admin/projects/archive/
```

Do this only after checking whether they contain unique work.

## Rules Going Forward

- New app idea: create a folder under `second-brain/Projects/projects/<slug>/`.
- New source build: create a separate GitHub repo and clone under `/home/cef-admin/projects-source-code/<slug>/`.
- Research reports: save under `second-brain/Projects/projects/<slug>/research/`.
- Implementation plans: save under `second-brain/Projects/projects/<slug>/implementation-plans/`.
- Mockups: save under `second-brain/Projects/projects/<slug>/mockups/`.
- Decisions: save as dated Markdown files under `second-brain/Projects/projects/<slug>/decisions/`.
- OpenClaw identity, memory, and operating notes stay in `/home/cef-admin/.openclaw/workspace`.

## Recommended Next Step

Create the GitHub repo:

```text
chrisforbesblogs/second-brain/Projects
```

Then tell me it exists. I can clone it, create the skeleton structure, move collateral into place, and prepare the first commit.
