# Local Folder Setup

Date: 2026-05-25

Implemented local project organisation with project collateral under the OpenClaw second-brain and buildable source repositories under `/home/cef-admin/projects-source-code`.

## Root Structure

```text
/home/cef-admin/.openclaw/workspace/second-brain/Projects/

/home/cef-admin/projects-source-code/
  chip-hello/
  chip-postman/
  compliance-tracker/
  football-betting-app/
  sports-prediction-model/

/home/cef-admin/projects/
  archive/
  sandbox/
```

## Source Code

Each child folder under `/home/cef-admin/projects-source-code` is its own Git repository or ready to connect to one:

```text
/home/cef-admin/projects-source-code/
  chip-hello/
  chip-postman/
  compliance-tracker/
  football-betting-app/
  sports-prediction-model/
```

## Second-Brain Projects

`second-brain/Projects` contains planning and collateral:

```text
second-brain/Projects/
  docs/
  templates/
  projects/
  archive/
```

## Migration Notes

- Moved `chip-postman` source to `/home/cef-admin/projects-source-code/chip-postman`.
- Moved `compliance-tracker-mockup` source to `/home/cef-admin/projects-source-code/compliance-tracker`.
- Moved `chip-hello` source to `/home/cef-admin/projects-source-code/chip-hello`.
- Moved `parcel-post` and `expo-hello-world` to `/home/cef-admin/projects/archive`.
- Moved reports and mockups into the matching `second-brain/Projects/projects/<project>` folders.
- Trashed generated `node_modules` and `.expo` folders from migrated source/archive projects.
- Left OpenClaw memory/config files in `/home/cef-admin/.openclaw/workspace`.

## Follow-Up

- Add GitHub remotes when the repositories exist.
- Commit `second-brain/Projects` once reviewed.
- Commit or review uncommitted `chip-postman` changes on branch `feature/audio-pass`.
