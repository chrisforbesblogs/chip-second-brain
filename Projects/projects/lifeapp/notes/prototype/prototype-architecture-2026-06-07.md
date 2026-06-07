# Life App Prototype Architecture

Date: 2026-06-07
Status: Static clickable prototype guidance
Audience: ChipCode / future app build

## Purpose

Build a static clickable prototype that proves the daily decision layer before committing to live integrations or a full app stack.

The prototype should make these promises feel real:

- A user can onboard with Garmin, another wearable/app, or no connection/manual entry.
- The Today screen turns health signals into clear actions.
- Training, nutrition, hydration, recovery, and habits feel connected.
- Light and dark modes share one product system.
- Dark mode has a high-performance recovery feel, without copying WHOOP branding or interaction patterns.

Rich animation is a later-phase product differentiator, not an MVP dependency.

## Recommended Prototype File Structure

Keep the prototype build simple enough for static hosting and easy handoff:

```text
Projects/projects/lifeapp/prototype/
  index.html
  assets/
    images/
    icons/
  src/
    app.js
    data/
      demo-state.js
      recommendations.js
    styles/
      base.css
      themes.css
      components.css
      screens.css
    screens/
      onboarding.js
      today.js
      calendar.js
      training.js
      nutrition.js
      habits.js
      profile.js
```

For a first pass, `index.html`, `src/app.js`, and the CSS files are enough. Split screens into separate files once the prototype has more than one or two interaction branches.

Do not put real source code in the project root until the prototype direction is validated. Keep static prototype assets separate from notes and wireframes.

## Navigation Flow

The clickable flow should be shallow, direct, and complete:

1. Welcome
2. Goal setup
3. Data connection choice
4. Today dashboard
5. Bottom-nav sections: Calendar, Training, Nutrition, Habits
6. Profile/settings from the top-right

### Onboarding Branches

The data connection step needs three selectable paths:

- `garmin_connected`: Garmin is connected and synced.
- `other_connected`: Another wearable/app is selected, but data is normalized into the same demo signal model.
- `manual`: No connection; the user enters or confirms baseline values manually.

The prototype should show all three branches as valid, not treat manual entry as an error state. Garmin remains the primary first-user path, but manual entry is the resilience path for demos, early testing, and unsupported users.

### Main App Navigation

Use the MVP navigation already decided:

- Today
- Calendar
- Training
- Nutrition
- Habits

Keep Profile/settings in the top-right. It should include connection state, goals, theme mode, and Simple/Performance mode.

Training should have two sub-tabs:

- Today
- Workouts

## State Model

Use a small client-side state object so the static prototype can demonstrate product logic without backend work:

```js
{
  user: {
    name: "Alex",
    trainingGoal: "Build endurance",
    nutritionGoal: "Hit protein target",
    recoveryGoal: "Improve sleep consistency",
    mode: "performance"
  },
  integrations: {
    selectedSource: "garmin", // garmin | other | manual
    status: "synced", // synced | simulated | manual | disconnected
    lastSyncLabel: "Today 07:42"
  },
  theme: "dark", // light | dark
  today: {
    readinessLabel: "Ready to train",
    readinessScore: 82,
    sleepScore: 78,
    hrvStatus: "balanced",
    trainingLoad: "productive",
    nutritionStatus: "protein behind",
    hydrationStatus: "600ml behind"
  },
  actions: {
    training: "45 min zone 2 run",
    protein: "45g remaining",
    water: "2.4L target",
    habit: "10 min mobility",
    recovery: "Wind down by 22:30"
  }
}
```

For MVP prototyping, avoid complex persistence. Store state in memory, with optional `localStorage` only for theme and selected onboarding branch.

Recommendation copy can be deterministic. Example: if readiness is high, show a training action; if readiness is low, show recovery and refuel actions. The point is to make the product judgment visible, not to build a coaching engine.

## Theme System

Build light and dark modes from shared semantic tokens:

- `--color-bg`
- `--color-surface`
- `--color-text`
- `--color-muted`
- `--color-border`
- `--color-accent`
- `--color-positive`
- `--color-warning`
- `--color-danger`
- `--color-recovery`
- `--color-training`
- `--color-nutrition`
- `--color-habit`

Dark mode should feel like a performance cockpit: high contrast, compact hierarchy, strong signal colors, and quiet surfaces. Avoid copying WHOOP's exact palette, copy, brand framing, or distinctive interaction patterns.

Light mode should be a cleaner expression of the same system, not a separate product. Screen density, component layout, and signal color meanings should remain consistent between themes.

## Future App Architecture Considerations

When moving beyond the static prototype, the app should separate four concerns:

- Presentation: screens, components, navigation, theming.
- Health data ingestion: Garmin and future integrations.
- Normalized daily signals: sleep, recovery, load, nutrition, hydration, habits.
- Recommendation logic: rules or AI-assisted coaching that turns signals into actions.

Recommended future shape:

- Mobile-first web app or React Native app for the first real build.
- Backend service for integration tokens, sync jobs, user goals, and normalized health data.
- Integration adapter layer per source: Garmin first, then Apple Health, Strava, WHOOP, Wahoo, food logging sources.
- Recommendation service with explainable rules before opaque AI.
- Event model for logs: meal, water, habit check-in, workout, sleep/recovery note.

Avoid letting Garmin-specific fields leak into every screen. Normalize source data before it reaches UI components so other wearable/app paths can reuse the same product experience.

## Key Risks

### Garmin Integration

Garmin should be treated as a high-risk dependency until API access, data permissions, sync cadence, and commercial terms are confirmed. The prototype should support simulated Garmin states so product testing does not block on live integration.

Mitigation:

- Label prototype data as synced, simulated, or manual.
- Design a normalized health signal model before implementing Garmin-specific UI.
- Keep integration status visible on Today and Profile.

### Manual-Entry Fallback

Manual entry can become tedious if it asks for too much. If manual users cannot reach Today quickly, the product will feel broken without integrations.

Mitigation:

- Ask only for baseline values during onboarding.
- Use quick daily check-ins instead of full data entry.
- Make manual values visibly editable from Today and Profile.
- Keep recommendations useful with partial data.

### Theme System

Dark and light modes can diverge if styles are hard-coded per screen. A dark performance aesthetic also risks feeling too close to WHOOP if visual references are copied too literally.

Mitigation:

- Use semantic CSS tokens from the first prototype.
- Test each screen in both themes before handoff.
- Preserve the same information architecture across themes.
- Use original Life App language, icons, and color assignments.

### Future Animation

Rich animation can make the product feel premium, but early motion work can slow the MVP and hide weak product logic.

Mitigation:

- MVP motion should be limited to theme transitions, tab changes, progress rings, and simple pressed/hover states.
- Reserve advanced motion for later: readiness transitions, weekly review storytelling, workout state changes, and data sync moments.
- Keep components structured so animation can be layered on later without rewriting screens.

## Build Notes For ChipCode

- Start with a static single-page prototype.
- Use real buttons and state changes, not separate screenshots.
- Implement onboarding branch selection early because it affects Today copy, sync state, and Profile.
- Use existing wireframe assets as visual reference, but build reusable HTML/CSS components.
- Make Today the most polished screen first; it is the core product proof.
- Keep Calendar, Training, Nutrition, and Habits complete enough to navigate and understand, even if their data is demo-only.
- Include a clear theme toggle in Profile and optionally a small top-level control during prototype review.
