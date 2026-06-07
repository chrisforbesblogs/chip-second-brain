# Life App MVP Spec

Date: 2026-06-07
Status: MVP blueprint v1
Working title: Life App

## Product Position

Life App is a daily health command centre for people who already use fitness, food, recovery, and habit tools but want one clear plan for the day.

Core promise:

> Life App turns fragmented health, fitness, recovery, nutrition, and habit data into clear daily action.

V1 should not try to replace Garmin, WHOOP, Strava, MyFitnessPal, or a full training coach. V1 should prove the daily decision layer:

1. What is my body telling me today?
2. What should I train, eat, drink, recover from, and repeat?
3. What changed this week?

## First User

Primary early user:

**Garmin/fitness wearable user who trains several times per week and wants one daily action plan.**

Traits:

- Uses Garmin or another wearable/activity tracker.
- Cares about training, sleep, recovery, calories, protein, hydration, and habits.
- Currently jumps between several apps.
- Wants clear recommendations, not more charts.
- Is motivated enough to log food/habits if the product feels useful.

## MVP Goal

Prove that users return daily because Life App makes health decisions easier.

The MVP succeeds if a user can:

1. Onboard with goals.
2. Connect or simulate Garmin data.
3. See one useful Today dashboard.
4. Log basic nutrition, hydration, and habits.
5. Get a simple training/recovery recommendation.
6. Complete a weekly review.

## Core User Flow

1. **Welcome**
   - Show the promise: one daily health plan.
   - Ask user to start setup.

2. **Goal Setup**
   - Training goal.
   - Body/nutrition goal.
   - Sleep/recovery goal.
   - First habit.
   - Experience mode: Simple or Performance.

3. **Connect Data**
   - Garmin compatible from MVP.
   - If live Garmin connection is not available in the prototype, use a simulated Garmin data state.
   - Optional later: Apple Health, Strava, WHOOP, Wahoo.

4. **Today Dashboard**
   - Show recovery/readiness state.
   - Show key signals.
   - Show today's recommended actions.
   - Show Garmin sync state.

5. **Daily Actions**
   - Training recommendation.
   - Nutrition/protein target.
   - Hydration target.
   - Habit check-in.
   - Sleep/recovery action.

6. **Weekly Review**
   - What improved.
   - What slipped.
   - What to adjust next week.

## App Structure

Bottom navigation:

- Today
- Calendar
- Training
- Nutrition
- Habits

Top-right:

- Profile/settings, similar placement to Garmin Connect.

Training section:

- Today
- Workouts

## Screen Requirements

### Today

Purpose:
The home screen. It should answer "what should I do today?"

Required content:

- Date and Garmin sync status.
- Recovery/readiness score.
- Key signals:
  - Sleep.
  - Recovery/HRV.
  - Training load.
  - Nutrition status.
  - Hydration or steps.
- Today's actions:
  - Training recommendation.
  - Protein/nutrition target.
  - Water target.
  - Habit target.
  - Sleep/recovery action.
- Clear state label:
  - Ready to train.
  - Train easy.
  - Recover.
  - Refuel.

### Calendar

Purpose:
Show the user's health/training week without becoming a full calendar app.

Required content:

- Week strip.
- Today plan.
- Upcoming training.
- Habit markers.
- Nutrition focus days.
- Rest/recovery days.

### Training

Purpose:
Make training decisions recovery-aware.

Required content:

- Tabs: Today and Workouts.
- Today's recommended workout.
- Duration and intensity.
- Reason for recommendation.
- Garmin signals:
  - Last workout.
  - Training load.
  - HRV/recovery.
  - Sleep context.
- Workout history summary.

V1 should not generate full Runna-style training plans.

### Nutrition

Purpose:
Help the user hit simple food targets tied to training and recovery.

Required content:

- Calories.
- Protein.
- Carbs.
- Fat.
- Water.
- Simple insight:
  - Protein low.
  - Fuel before training.
  - Hydration behind.
  - Recovery day target.
- Quick add:
  - Meal.
  - Snack.
  - Water.
  - Saved meal.

V1 logging modes:

- Manual quick add.
- Saved meals.
- Recent meals.

Nice-to-have if practical:

- Barcode/database food lookup.

Later:

- AI photo food logging with confidence/correction flow.

### Habits

Purpose:
Build consistency without making streaks punishing.

Required content:

- One to three daily habits.
- Habit setup:
  - Cue.
  - Time/place.
  - Smallest version.
  - Reminder.
- Check-in states:
  - Done.
  - Partial.
  - Skipped.
- Skip reason.
- Streak/consistency view.

Example MVP habits:

- Protein target.
- 8k steps.
- Mobility.
- Hydration.
- Sleep before 11.

### Profile

Purpose:
Account, goals, connections, and preferences.

Required content:

- Garmin connection status.
- Optional future connections:
  - Apple Health.
  - Strava.
  - WHOOP.
  - Wahoo.
- Goals:
  - Training.
  - Nutrition/body.
  - Sleep/recovery.
  - Habit.
- Mode:
  - Simple.
  - Performance.
- Theme:
  - Light.
  - Dark.
  - System.
- Notifications.
- Subscription placeholder.

## Garmin Data Requirements

MVP should be Garmin compatible.

Priority data:

- Sleep duration.
- Sleep quality/score if available.
- HRV or recovery proxy.
- Resting heart rate.
- Steps.
- Activities/workouts.
- Training load or activity intensity if available.
- Calories/activity energy if available.

Fallback if data is unavailable:

- Ask the user for a simple manual check-in.
- Use simulated demo data in prototypes.
- Show "not enough data yet" states clearly.

## MVP Scoring Logic

V1 scoring should be simple, explainable, and not medical.

### Readiness / Recovery

Inputs:

- Sleep duration.
- Sleep quality.
- HRV/recovery proxy.
- Resting heart rate trend.
- Recent training load.

Output:

- 0-100 score.
- Label:
  - Green: ready.
  - Yellow: moderate.
  - Red: recover.

Recommendation examples:

- Green: train as planned.
- Yellow: keep intensity moderate.
- Red: recovery or easy movement.

### Training Recommendation

Inputs:

- Readiness/recovery.
- Last workout.
- Training load.
- User goal.
- Calendar plan if available.

Outputs:

- Train.
- Train easy.
- Rest/recover.
- Move/walk/mobility.

### Nutrition Gap

Inputs:

- Calories logged.
- Protein logged.
- User body goal.
- Training recommendation.

Outputs:

- Protein target status.
- Calories/fuel status.
- Simple next action.

### Habit Completion

Inputs:

- Done/partial/skipped check-ins.
- Habit frequency.
- Skip reasons.

Outputs:

- Daily completion state.
- Weekly consistency.
- Suggested adjustment.

## Design Direction

### Dark Mode

Primary direction:

- WHOOP-style performance vibe.
- Dark background.
- High-contrast cards.
- Neon/lime recovery accent.
- Compact body-signal metrics.
- Circular recovery/load/sleep rings.
- Serious, athlete-led, data-first feel.

Reference assets:

- `assets/wireframes/mock-today-dashboard-whoop-vibe.png`
- `assets/wireframes/mock-training-workouts-whoop-vibe.png`
- `assets/wireframes/color-schemes/05-whoop-inspired-performance.png`

### Light Mode

Required for final product:

- Same information architecture as dark mode.
- Cleaner daytime version of the performance system.
- Light surfaces, strong contrast, same accent language.
- Should not feel like a separate app.

### Animation Direction

Later phase, not MVP:

- Animated score rings.
- Progress fills.
- Smooth light/dark theme transitions.
- Dashboard card transitions.
- Sync/loading motion.
- Weekly review reveal animations.
- Subtle haptics/microinteractions.

Do not let animation delay MVP clarity.

## MVP Must Have

- Goal-led onboarding.
- Garmin-compatible data path or prototype simulation.
- Today dashboard.
- Training recommendation.
- Nutrition/protein/water tracking.
- One to three habits.
- Weekly review.
- Light and dark theme requirement captured.
- Clear empty/error/loading states.

## MVP Should Have

- Saved meals.
- Recent meals.
- Basic weight/progress logging.
- Reminders.
- Private share card.
- Simple free/premium boundary.

## Out Of Scope For V1

- Full social feed.
- AI personal trainer personas.
- Full running plan generation.
- Full meal planning/grocery lists.
- Unlimited AI food scanning.
- Medical claims or diagnosis.
- Broad integration coverage beyond Garmin-first.
- Heavy animation system.
- Ads-heavy monetization.

## Key Empty States

- Garmin not connected.
- Garmin syncing.
- Not enough sleep/recovery data.
- No workouts yet.
- No meals logged yet.
- No habits created.
- Weekly review not ready.

## Success Metrics

Early MVP success should be based on behaviour and perceived usefulness.

- User completes onboarding.
- User connects Garmin or uses demo data.
- User opens Today on 4+ days in week one.
- User logs nutrition/water on 3+ days in week one.
- User checks a habit 5+ times in week one.
- User completes first weekly review.
- 60%+ of beta users say Life App helps them know what to do today.
- 40%+ of active beta users say they would be very disappointed if Life App went away.

## Next Build Step

Create a clickable prototype using the approved structure:

1. Onboarding.
2. Connect Garmin.
3. Today.
4. Training.
5. Nutrition.
6. Habits.
7. Calendar.
8. Profile/settings.

The prototype should include both light and dark theme direction, but animation can remain noted for later phases.
