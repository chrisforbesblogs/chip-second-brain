# Life App V2 Prototype Redesign Brief

Date: 2026-06-07
Status: Prototype redesign brief for ChipCode
Owner: ChipBoss acting as architect after subagent write failure

## Purpose

V2 should stop being a broad demo and become a sharper product prototype.

The product promise:

> Life App turns health, training, nutrition, and wearable data into a clear summary, deeper analysis when wanted, and practical guidance for what to do next.

Life App must support two appetites inside one product:
- Clean summary and guidance for users who want clarity without data overload.
- A data nerd's dream for users who want detailed signals, trends, and context.

The bridge between both is guidance: the app should not just show data, it should explain how the data changes training, recovery, nutrition, and logging decisions.

## V2 Principles

- Keep the app dark-first for the prototype.
- Move theme controls into Profile/Settings.
- Remove Habits from prototype v2.
- Replace Habits with Log.
- Keep Profile/Settings in the top-right, not bottom nav.
- Make Beginner / Intermediate / Advanced the key experience choice.
- Make Today the strongest screen.
- Make Calendar and Nutrition feel like serious product surfaces, not placeholders.
- Keep the paywall dismissible and separate from account creation.
- Account creation is about saving/syncing the plan; Premium is about deeper insight and less friction.

## Revised Onboarding

Recommended onboarding sequence:

1. Welcome
   - Replace "one clear health plan for today."
   - Suggested headline: "Your health data, turned into useful guidance."
   - Supporting copy: "Connect your training, recovery, nutrition, and logs so Life App can show what matters and what to do next."

2. Goals
   - Keep this screen.
   - Focus on outcomes:
     - Train smarter.
     - Improve body composition.
     - Recover better.
     - Build consistency.

3. Training Baseline
   - Split current training context into clearer pieces.
   - Ask current rhythm:
     - 0-2 days/week.
     - 3-5 days/week.
     - 6+ days/week.
   - Ask primary training:
     - Strength.
     - Running/cardio.
     - Hybrid.
     - General fitness.

4. Experience Level
   - Beginner / Intermediate / Advanced.
   - This controls dashboard density and language.
   - Beginner: clean, action-led, fewer metrics.
   - Intermediate: balanced signal summary and guidance.
   - Advanced: dense metrics, trends, and deeper analysis.

5. Nutrition Baseline
   - Cleaner than current version.
   - Ask tracking preference:
     - Quick targets.
     - Macro aware.
     - Detailed logging.
   - Ask main nutrition focus:
     - Protein.
     - Calories/body weight.
     - Fuel training.
     - Hydration.

6. Connect Data
   - Combine data source with trust copy.
   - Options:
     - Garmin.
     - Other wearable/app.
     - Manual/demo.
   - Explain source state clearly: synced, simulated, manual, or missing.

7. Plan Preview
   - Show a mini Today preview based on the user's choices.
   - Include clean summary and, for Advanced, a denser signal preview.
   - Do not ask for theme here.

8. Account Setup / Save Plan
   - Near the end of onboarding.
   - Purpose: save plan, sync devices, and keep progress.
   - Options:
     - Continue with Apple.
     - Continue with Google.
     - Continue with email.
     - Continue with demo data.
   - Include trust copy:
     - "You control connections and can disconnect anytime."
     - "Life App uses health and training data for recommendations, not medical advice."

9. Premium Preview
   - Keep similar location to current paywall: after plan preview/account save moment, before or on first Today.
   - Dismissible with "Continue free."
   - Add simulated pricing from pricing strategy:
     - Free: GBP0 / $0.
     - Premium Monthly: GBP9.99 / $12.99.
     - Premium Annual: GBP69.99 / $89.99, Best value.
     - Coach Later: from GBP29.99 / $39.99, Coming later.

## Experience Levels

Beginner:
- Cleanest language.
- Show readiness, one training recommendation, core nutrition target, hydration, and one recovery prompt.
- Use fewer metrics and more explanation.
- Example: "Train easy today. Sleep was okay, but recovery is not fully back."

Intermediate:
- Balanced dashboard.
- Show readiness, sleep, HRV/recovery, load, protein, hydration, steps, and weekly trend.
- Explain why actions changed.

Advanced:
- Dense and nerdy by design.
- Show readiness drivers, HRV trend, resting HR, sleep debt, training load, acute/chronic load proxy, recovery status, calories, protein, carbs, hydration, body weight trend, recent lifting progress, and manual notes.
- Use compact cards, rings, sparklines, and signal labels.
- Still translate signals into training guidance.

## Navigation

Bottom nav:
- Today
- Training
- Nutrition
- Calendar
- Log

Top-right:
- Profile / Settings

Remove:
- Habits tab from prototype v2.

## Screen Responsibilities

### Today

Purpose:
The strongest screen. It answers: "What is my body telling me, and what should I do?"

Beginner layout:
- Main readiness ring.
- One daily recommendation.
- Four clean metric cards:
  - Sleep.
  - Recovery.
  - Training load.
  - Fuel/hydration.
- Today's actions:
  - Training.
  - Nutrition.
  - Hydration.
  - Recovery.

Advanced layout:
- Readiness ring plus driver breakdown.
- Metrics grid:
  - HRV.
  - Resting HR.
  - Sleep duration and quality.
  - Training load.
  - Acute/chronic load proxy.
  - Steps.
  - Calories.
  - Protein.
  - Carbs.
  - Hydration.
  - Body weight trend.
  - Last lift/run marker.
- Guidance block:
  - "Recommended training adjustment."
  - "Why."
  - "What to watch tomorrow."

### Training

Purpose:
Make training decisions recovery-aware.

Content:
- Today's recommendation.
- Session options: easy, normal, push, recover.
- Reasoning from sleep/recovery/load.
- Recent sessions.
- For Advanced: load trend, volume, intensity, fatigue notes, and progression signal.

### Nutrition

Purpose:
Make nutrition useful, not just a calorie table.

Content:
- Daily targets tied to training day.
- Calories, protein, carbs, fat, water.
- Quick add buttons.
- Saved meals / recent meals.
- Insight block:
  - "Protein is behind."
  - "Fuel before training."
  - "Hydration catch-up."
- Advanced: macro split, meal timing, refuel target, weekly average, adherence trend.

### Calendar

Purpose:
Show the training and health week at a glance.

V2 should be more visual and less dull:
- Week strip with readiness/load markers.
- Planned sessions.
- Recovery days.
- Nutrition focus days.
- Weight/check-in markers.
- Weekly summary card.
- Advanced: mini trend row for load, sleep, weight, and nutrition adherence.

### Log

Purpose:
The history and manual input surface.

Must include:
- Body weight progression.
- Lifting progress.
- Garmin health stats history.
- Manual daily check-ins.
- Nutrition history.

Prototype sections:
- Today's quick log:
  - Weight.
  - Energy.
  - Soreness.
  - Notes.
- Trends:
  - Body weight.
  - Bench/squat/deadlift or chosen lift.
  - Sleep/HRV/resting HR.
  - Calories/protein/water.
- Data source status:
  - Garmin synced, simulated, manual, or missing.

### Profile / Settings

Responsibilities:
- Account state.
- Data source connection and disconnect controls.
- Theme: dark/light/system.
- Experience level: Beginner / Intermediate / Advanced.
- Privacy and data controls.
- Subscription status.
- Demo/manual data reset.

Theme does not belong in onboarding or the main dashboard.

## Paywall

Placement:
- After plan preview and account/demo choice, before first full Today, or as the first Today soft paywall.

Rules:
- Dismissible.
- "Continue free" always visible.
- Account creation is not a paywall.
- Basic Garmin/manual/demo path remains free.
- Premium sells deeper insight and less logging friction.

Paywall content:
- Headline: "Go deeper when you are ready."
- Free: core Today, basic logging, basic review.
- Premium: advanced insights, adaptive targets, richer wearable explanations, unlimited saved meals.
- Coach Later: coming later.
- Show simulated pricing and annual best value.

## ChipCode Implementation Checklist

Update only prototype files unless asked otherwise:
- `Projects/projects/lifeapp/assets/prototype/index.html`
- `Projects/projects/lifeapp/assets/prototype/README.md`

Required prototype v2 changes:
- Rewrite welcome and onboarding copy.
- Replace Simple/Performance with Beginner/Intermediate/Advanced.
- Remove theme selection from onboarding.
- Add account setup near end of onboarding.
- Add Apple/Google/email/demo account options.
- Keep data source and trust copy clear.
- Add simulated pricing to paywall.
- Keep paywall dismissible.
- Remove Habits screen and tab.
- Add Log screen and tab.
- Move theme controls to Profile/Settings.
- Improve Today with clean vs advanced density.
- Improve Calendar beyond simple week cards.
- Improve Nutrition layout and usefulness.
- Ensure nav is Today, Training, Nutrition, Calendar, Log.
- Keep Profile/Settings accessible from top-right.
- Make setup choices visibly affect Today/Profile/Log copy.
- Verify embedded JavaScript compiles before committing.

## Open Questions For Later

- Which exact lifting metrics should be default in Log?
- Whether Advanced should be a free mode with some premium locked cards, or entirely included in Premium.
- Whether account setup should support magic link in the real app.
- Whether Coach Later is AI-only, human-led, or a hybrid.
