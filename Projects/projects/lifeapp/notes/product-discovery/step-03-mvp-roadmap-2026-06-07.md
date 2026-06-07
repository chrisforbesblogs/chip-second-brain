# Step 03 - MVP And Roadmap

Date: 2026-06-07  
Project: LifeApp  
Scope: MVP wedge, phased roadmap, deferrals, validation tests, and success metrics only.

## Recommendation

LifeApp should not launch as a full health super app first. The v1 wedge should be:

> A daily health operating system for motivated fitness users who already track training, food, sleep, recovery, and habits across too many apps.

The first version should prove one tight daily loop:

1. See today's health state.
2. Log the few actions that matter.
3. Get a simple recommendation for training, nutrition, hydration, recovery, and one habit.
4. Review progress weekly and adjust.

The v1 should feel useful even before every integration, AI trainer, social feature, and advanced nutrition feature exists.

## Product Thesis For MVP

Motivated fitness users will return to LifeApp daily if it reduces app switching and turns fragmented health data into clear daily actions.

The strongest v1 wedge is not "best wearable app", "best calorie tracker", or "best habit tracker" in isolation. It is the connection between:

- recovery and sleep context;
- simple food, macro, protein, and water tracking;
- one to three health-linked habits;
- a plain-English daily plan.

## First Target User

Primary early user hypothesis:

**Hybrid fitness self-improver**

- Trains several times per week.
- Uses or wants to use a wearable, activity app, or fitness tracker.
- Cares about calories, protein, water, sleep, recovery, and consistency.
- Has tried multiple apps but finds the overall workflow fragmented.
- Wants practical daily guidance, not a wall of charts.

Secondary users can be explored later: serious macro trackers, endurance athletes, beginners, habit-only users, and people seeking AI coaching.

## V1 Scope

V1 should validate the daily operating loop with a small but coherent product.

### Must Have

- Goal-led onboarding: training goal, body goal, sleep/recovery goal, nutrition focus, and first habit.
- Daily dashboard: today's priority actions across recovery, food, water, training/activity, and habit.
- Simple recovery/sleep state: enough to guide the day without trying to replace Garmin, WHOOP, or Bevel.
- Basic nutrition tracking: calories, protein, macros, water, saved meals, quick add, and simple correction.
- Habit builder: one to three health-linked habits with cue, time/place, smallest version, reminder, check-in, partial completion, and skip reason.
- Weekly review: what improved, what slipped, and what to adjust next week.
- Progress view: simple trends for consistency, nutrition adherence, water, sleep/recovery, and habit completion.

### Should Have

- Barcode or database-assisted food lookup if available without derailing the wedge.
- Weight/progress logging for users with body composition goals.
- Private share card or accountability check-in, not a full public social network.
- Lightweight reminders for food, water, sleep wind-down, and habits.
- Clear free vs premium boundaries from the start, even if monetization is tested later.

### Could Have

- Limited AI food photo logging beta with clear confidence and correction prompts.
- More detailed micronutrient summaries for users who want them.
- Basic workout logging or import summary.
- Small challenges such as hydration week, sleep wind-down week, or protein consistency week.

### Do Not Build First

- Full Strava-style public feed, leaderboards, clubs, and segments.
- AI personal trainer personas or eight-week programme generation.
- Full multi-device compatibility across Garmin, WHOOP, Wahoo, Apple, Google, Strava, and others.
- Advanced meal planning, grocery lists, recipes, or full diet coaching.
- Heavy micronutrient dashboards for all users.
- Medical-grade recommendations or diagnostic claims.
- Ads-heavy free experience that damages trust.
- Large content library, courses, or generic wellness articles.

## V1.5 Scope

V1.5 should improve retention and logging convenience once the daily loop is showing promise.

- Better food logging convenience: barcode, saved meals, recent meals, copied meals, label/photo assist if validated.
- More useful weekly insights: "what helped recovery", "what hurt consistency", "what habit should shrink or progress".
- Expanded wearable/activity inputs based on the v1 audience's most-used devices.
- Private accountability: friend check-ins, small groups, or coach-style share summaries.
- More habit templates for sleep, hydration, protein, walking, gym attendance, journaling, caffeine cutoff, and recovery routines.
- Pricing tests for premium insights, advanced logging convenience, and deeper personalization.

## V2 Scope

V2 should widen LifeApp only after v1 proves daily use and v1.5 improves retention.

- AI food photo logging as a paid convenience layer, with limits, confidence, and manual correction.
- Smarter coaching insights that connect recovery, nutrition, training, sleep, weight trend, and habit consistency.
- Broader wearable and activity coverage.
- Richer workout tracking and progress summaries.
- More social/accountability loops, still biased toward private progress and health consistency rather than public comparison.
- Premium packages around advanced insights, unlimited AI convenience, deeper goal tracking, and personalized plans.

## Later Ideas

These are aligned with Charley's bigger vision but should wait until the core loop is proven:

- AI personal trainer personas for running, lifting, cycling, and hybrid fitness.
- Eight-week training programmes.
- Coach marketplace or human expert add-ons.
- Full Strava-like social network.
- Advanced meal plans, grocery lists, recipe import, and nutrition coaching.
- Free-with-ads model at scale.
- Corporate wellness, gyms, team plans, or creator-led communities.

## Validation Tests

1. **Problem interview test**
   - Interview 15-25 target users who train regularly and use at least two health/fitness apps.
   - Validate app-switching pain, current tools, daily routines, and willingness to adopt one combined dashboard.

2. **Concierge daily-plan test**
   - For 10-15 users, manually create a daily health summary from their current training, food, water, sleep, and habit inputs.
   - Test whether users find the "what should I do today?" layer more useful than their existing apps.

3. **Clickable prototype test**
   - Show onboarding, daily dashboard, food/water logging, habit setup, and weekly review.
   - Measure whether users understand the value within two minutes.

4. **Seven-day diary beta**
   - Ask users to use the v1 loop for one week.
   - Track daily dashboard opens, food/water logs, habit check-ins, and qualitative feedback on app switching.

5. **Habit design test**
   - Test whether users can create a useful health habit with cue, time/place, smallest version, and reminder.
   - Measure whether partial completion and skip reasons feel motivating rather than punishing.

6. **Pricing and packaging test**
   - Test willingness to pay only after users experience the dashboard and weekly review.
   - Compare premium appetite for advanced insights, AI food convenience, and deeper personalization.

## Success Metrics

Early metrics should prove behaviour and value, not vanity downloads.

- **Activation:** user completes onboarding, creates one habit, logs first food or water action, and checks the daily dashboard.
- **Daily engagement:** user opens the daily dashboard on four or more days in week one.
- **Nutrition engagement:** user logs food, protein, macros, or water on three or more days in week one.
- **Habit engagement:** user checks in on a habit five or more times in week one, including partial or skipped entries.
- **Weekly review:** user completes the first weekly review.
- **Retention:** early target of 35-45% day-7 retention and 15-25% day-30 retention as working consumer-app hypotheses.
- **Perceived value:** 60%+ of beta users say LifeApp helps them know what to do today.
- **Fragmentation relief:** users report using fewer separate apps or feeling less need to jump between apps.
- **Product-market fit signal:** 40%+ of active beta users say they would be very disappointed if LifeApp went away.

## Key Risks And Assumptions

- The vision is broad enough to become unfocused unless v1 is deliberately narrow.
- Users may say they want one app but still prefer specialist apps for serious tracking.
- Food logging friction could undermine daily retention.
- Recovery insights must be trusted and clear, or they become another score users ignore.
- Habit tracking can become demotivating if it overuses streak pressure.
- Free-with-ads may conflict with trust in a health product.
- AI food logging may be expensive, inaccurate, or overpromised if introduced too early.
- Device compatibility expectations must be managed carefully; v1 should communicate supported sources plainly.

## Step 3 Conclusion

The recommended first product is a narrow daily health command centre, not the full super app. V1 should prove that users want one place to decide what to do today across recovery, nutrition, hydration, and habits. Social, AI trainers, broad integrations, advanced AI food logging, and deep coaching should be phased in only after that daily loop is validated.
