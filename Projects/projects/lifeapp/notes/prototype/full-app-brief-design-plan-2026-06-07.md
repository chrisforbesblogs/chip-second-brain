# Life App Full App Brief And Design Plan
Date: 2026-06-07
Status: Prototype design plan for ChipCode handoff

Source inputs:
- `Projects/projects/lifeapp/MVP_SPEC.md`
- `Projects/projects/lifeapp/notes/prototype/prototype-architecture-2026-06-07.md`
- `Projects/projects/lifeapp/assets/prototype/README.md`
- `Projects/projects/lifeapp/notes/product-discovery/final-product-discovery-summary-and-plan-2026-06-07.md`

## Product Direction
Life App is a daily health command centre for motivated fitness users who already use several tools for training, food, recovery, sleep, and habits.
The MVP should not replace Garmin, WHOOP, Strava, MyFitnessPal, Runna, or habit apps. It should prove the daily decision layer: what is my body telling me, what should I train/eat/drink/recover from/repeat, and what changed this week?
The first user is a Garmin or wearable user who trains several times per week and wants one practical daily action plan.

## Visual Direction
Blend the original clean dashboard/prototype structure with the current prototype's circular recovery, strain/training, and sleep displays.
- Keep the original structure: calm hierarchy, clear cards, visible next actions, mobile-first bottom navigation.
- Keep the circular metrics users liked: recovery/readiness, sleep, and training load/strain should be instantly scannable.
- Dark mode should feel like a performance/recovery cockpit without copying WHOOP's brand, palette, wording, or interaction patterns.
- Light mode should be the same system in a cleaner daytime expression, not a separate product.
- Use Life App's own language: daily plan, signals, actions, consistency, review.

## Product Principles
- One useful daily plan comes first.
- Signals should become actions, not just scores.
- Garmin is first, but other wearable/app and manual entry paths must feel valid.
- Manual entry is a supported mode, not an error state.
- Recommendations should be explainable and deterministic in the prototype.
- Weekly Review should show what improved, what slipped, and what to adjust.
- Paywall framing should be present but must not block prototype testing.

## Navigation
Bottom nav:
- Today
- Calendar
- Training
- Nutrition
- Habits

Top-right:
- Profile/settings

Secondary surfaces:
- Weekly Review
- Paywall

Training tabs:
- Today
- Workouts

## Screen Plan
### Onboarding
Purpose: set up goals, mode, and data source quickly.
Content:
- Welcome promise: one daily health plan.
- Goal setup: training, body/nutrition, sleep/recovery, first habit.
- Mode choice: Simple or Performance.
- Data source choice: Garmin, other wearable/app, or no connection/manual entry.
- Manual baseline confirmation for users without a connected source.
- Setup complete state leading to Today.
Design notes:
- Garmin is the primary recommended path.
- Other wearable/app is fully valid and normalized into the same Life App signals.
- Manual entry is fast setup with editable baseline values.
- Source badges should appear immediately.

### Today
Purpose: answer "what should I do today?"
Content:
- Date and source/sync badge.
- Primary readiness/recovery ring.
- Mini rings for sleep and training load/strain.
- State label: Ready to train, Train easy, Recover, or Refuel.
- Today's actions: training, protein/nutrition, water, habit, sleep/recovery.
- Key signals: sleep, HRV/recovery, training load, nutrition, hydration or steps.
Design notes:
- Preserve the clean dashboard skeleton: signal summary, action cards, deeper signal rows.
- Use circular metrics for the most important signals only.
- Each recommendation should include a short reason tied to visible data.

### Calendar
Purpose: show the user's health/training week without becoming a full calendar app.
Content:
- Week strip.
- Today plan.
- Upcoming training.
- Habit markers.
- Nutrition focus days.
- Rest/recovery days.
Design notes:
- Use mini rings or compact status dots for the week strip.
- Keep the screen scannable and avoid dense scheduling controls.

### Training
Purpose: make training decisions recovery-aware.
Content:
- Tabs: Today and Workouts.
- Today's recommended workout, duration, intensity, and reason.
- Garmin/normalized signals: last workout, training load, HRV/recovery, sleep context.
- Workout history summary.
Design notes:
- Do not build Runna-style plans in v1.
- Training should connect visibly to recovery and nutrition.
- Use a training ring or load meter for push, maintain, easy, or rest guidance.

### Nutrition
Purpose: help the user hit simple targets tied to training and recovery.
Content:
- Calories, protein, carbs, fat, and water.
- Simple insight: protein low, fuel before training, hydration behind, or recovery day target.
- Quick add: meal, snack, water, saved meal.
Design notes:
- Start with manual quick add, saved meals, and recent meals.
- Barcode/database lookup is nice-to-have if practical.
- AI photo logging is later and needs confidence and correction flows.

### Habits
Purpose: build consistency without punishing missed days.
Content:
- One to three daily habits.
- Setup: cue, time/place, smallest version, reminder.
- Check-in states: done, partial, skipped.
- Skip reason.
Design notes:
- Habits should connect to outcomes like sleep consistency, hydration, protein, mobility, or training prep.
- Use forgiving copy and show recovery from misses.

### Profile
Purpose: manage identity, goals, integrations, and preferences.
Content:
- User summary, connection state, goals, theme mode, Simple/Performance mode.
- Data source details and manual baseline editing.
Design notes:
- Keep Profile in the top-right.
- Make data state transparent: synced, simulated, manual, or disconnected.

### Weekly Review
Purpose: turn tracking into adjustment.
Content:
- What improved.
- What slipped.
- What to adjust next week.
- Trends for recovery, sleep, training, nutrition, hydration, and habits.
- One recommended focus for next week.
Design notes:
- Use lightweight trend charts and weekly completion rows.
- Keep the review direct, practical, and action-oriented.

### Paywall
Purpose: test premium framing without blocking the core daily loop.
Content:
- Free: basic dashboard, manual logging, basic habits, limited insights.
- Premium: integrations, richer weekly review, saved meal automation, advanced insights, more AI logging later.
- Coach later: adaptive programmes, AI coach personas, specialist training/nutrition plans.
Design notes:
- Paywall cards should describe outcomes, not just feature lists.
- Always allow users to return to the task they were doing in the prototype.

## Component System
- Metric rings: primary readiness/recovery, sleep, training load/strain, nutrition adherence, hydration.
- Mini rings: week strip, card headers, compact profile summaries.
- Cards: Today actions, signals, workouts, meals, habits, review items.
- Action rows: log water, add meal, check habit, start wind-down, complete workout.
- Bottom nav: five primary sections with clear active state.
- Source badges: Garmin, other wearable/app, manual, simulated, synced, disconnected.
- Paywall cards: Free, Premium, Coach later.
- Trend charts: simple line/bar charts for weekly review and progress context.

## Data Source Strategy
Normalize source data before it reaches UI components. Core signals are recovery/readiness, sleep, HRV or recovery status, training load/strain, activity/workout history, nutrition adherence, hydration, and habit completion.
Source paths:
- Garmin first for the primary early user.
- Other wearable/app normalized into the same signal model.
- Manual entry for baseline values and daily check-ins.
Prototype state should support:
- `selectedSource`: `garmin`, `other`, or `manual`.
- `status`: `synced`, `simulated`, `manual`, or `disconnected`.
- `theme`: `light` or `dark`.
- `mode`: `simple` or `performance`.
- `today`: readiness, sleep, HRV/recovery, training load, nutrition, hydration.
- `actions`: training, protein, water, habit, recovery.

## Future Animation Ideas
Later-phase only:
- Readiness ring transitions after sync.
- Sleep/recovery/training ring count-up.
- Weekly Review storytelling transitions.
- Theme transition polish.
- Workout state changes from planned to completed.
- Data sync moments that make new insights feel earned.
MVP motion should stay limited to pressed states, tab changes, basic progress ring fills, and theme switching.

## ChipThink Dependency
ChipThink onboarding/paywall brief pending; link it later at:
`Projects/projects/lifeapp/notes/prototype/onboarding-paywall-brief-2026-06-07.md`

## Handoff Notes For ChipCode
- Update the prototype after the onboarding/paywall brief exists.
- Preserve the clean dashboard structure while adding circular metric displays in Life App's own visual language.
- Keep dark and light modes on shared semantic tokens.
- Make onboarding support Garmin, other wearable/app, and no connection/manual entry.
- Add source badges consistently across Today and Profile.
- Keep recommendations explainable and tied to visible signals.
- Do not add advanced animations until the core screen logic and paywall/onboarding content are stable.

