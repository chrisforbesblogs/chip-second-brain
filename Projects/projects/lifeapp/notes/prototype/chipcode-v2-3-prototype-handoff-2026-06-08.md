# Life App V2.3 Prototype Handoff For ChipCode

Date: 2026-06-08
Status: Approved handoff prep for ChipCode
Owner: ChipBoss

## Task

Update the existing static clickable Life App prototype from v2.1 toward v2.3.

Use this design brief as the source of truth:

`Projects/projects/lifeapp/notes/prototype/v2-3-design-brief-2026-06-07.md`

Do not set up or depend on ChipArchitect today. Chris will handle a real ChipArchitect agent later. For now, treat the v2.3 brief as the temporary architecture/design handoff.

## Scope

Update only:

- `Projects/projects/lifeapp/assets/prototype/index.html`
- `Projects/projects/lifeapp/assets/prototype/README.md`

Do not create a new source-code repo.
Do not move the prototype to `/home/cef-admin/projects-source-code/`.
Do not change unrelated Life App notes unless a blocker requires it.

## Required Prototype Changes

- Update prototype README version/changelog to v2.3.
- Sharpen onboarding copy using the 18-screen flow in the v2.3 brief.
- Add or improve onboarding progress labels: Goal, Training, Nutrition, Data, Preview, Save, Premium.
- Make plan generation show selected inputs rather than feeling like fake loading.
- Keep account setup near the end and frame it as save/sync.
- Keep premium preview dismissible with visible Continue free.
- Use simulated pricing:
  - Free: GBP0 / $0.
  - Premium Monthly: GBP9.99 / $12.99.
  - Premium Annual: GBP69.99 / $89.99, Best value.
  - Coach Later: from GBP29.99 / $39.99, Coming later.
- Strengthen Today for Beginner, Intermediate, and Advanced density.
- Improve Nutrition so it includes quick actions, recent/saved meals, hydration, and insight copy.
- Improve Calendar into a performance week view with readiness/load/recovery/nutrition markers.
- Improve Log with body weight, lifting progress, health stats history, manual check-ins, and nutrition history.
- Add Profile / Settings top-right if feasible in this pass.
- Keep theme controls in Profile / Settings only, not onboarding.
- Preserve bottom nav: Today, Training, Nutrition, Calendar, Log.
- Label data state wherever trust matters: synced, syncing, simulated, manual, missing.
- Apply the dark-first visual direction and accent rules from the v2.3 brief.

## Verification

Before handing back:

- Confirm the prototype opens locally.
- Confirm onboarding can progress all the way to Today.
- Confirm Continue free closes/dismisses the paywall path.
- Confirm nav tabs switch correctly.
- Confirm Beginner / Intermediate / Advanced changes Today density or copy.
- Confirm embedded JavaScript has no syntax errors.
- Report changed files, verification steps, and any remaining blockers.
