# Life App Onboarding And Paywall Brief

Date: 2026-06-07
Status: Prototype handoff brief
Owner: ChipThink

## Recommendation
Use 7 onboarding screens before the first Today view.

Why:
- Life App spans recovery, training, nutrition, hydration, habits, and data sources.
- Fewer than 6 screens would create dense forms and generic recommendations.
- More than 8 screens risks delaying the first value moment.
- Seven screens matches strong fitness patterns: promise, goals, context, data, preferences, value preview, dashboard.
- Keep one main decision per screen, with progress visible and optional details skippable.

## Exact MVP Onboarding Sequence
1. Welcome
   - Promise: "One clear health plan for today."
   - CTA: "Start setup"; secondary: "Preview with demo data."
2. Goals
   - Primary: build fitness, lose fat, gain muscle, improve endurance, improve consistency, recover better.
   - Body/nutrition: maintain, lose, gain, fuel performance, improve protein.
   - Sleep/recovery: sleep more, improve routine, reduce fatigue, train smarter.
3. Training Context
   - Frequency, main activity, current plan source.
   - Sources: self-led, Garmin, Strava, Runna/coach, other app, no plan.
4. Nutrition And Hydration
   - Preference: quick add, saved meals/recents, barcode/database, photo estimate later.
   - Focus: calories, protein, macros, water, meal timing.
   - Posture: "I track often", "I track sometimes", "I want low effort."
5. Habits
   - Pick 1 to 3 starter habits.
   - Capture cue/time/place, smallest version, reminder preference.
   - Support done, partial, skipped, and skip reason from day one.
6. Data Source
   - Branch into Garmin, other wearable/app, or manual/demo.
   - Garmin is the primary MVP path.
   - If live connection is unavailable, show simulated Garmin-style data clearly.
7. Mode, Theme, Plan Preview
   - Mode: Simple or Performance.
   - Theme: Light, Dark, or System.
   - Preview: readiness label, today's action, nutrition focus, water target, first habit.
   - CTA: "See Today."

## Data Source Branches
Garmin:
- Copy: "Connect Garmin to turn sleep, HRV, training load, steps, and workouts into today's plan."
- States: connect, syncing, connected, not enough data yet, unavailable/demo.
- Signals: sleep duration/quality, HRV or recovery proxy, resting HR, steps, workouts, training load/activity intensity, activity energy.
- If prototype data is simulated, say so plainly.
- Avoid medical-grade claims.

Other wearable/app:
- Options: Apple Health, Strava, WHOOP, Wahoo, Google Fit, other.
- Prototype state: "Coming next. Use manual or demo data today."
- Capture demand without blocking onboarding.
- Let users continue with manual check-ins and imported-style demo signals.

Manual entry:
- Ask for sleep hours, energy, soreness, last workout, and activity estimate.
- Use a 3-touch daily check-in: sleep, body, training.
- Show "not enough data yet" honestly where needed.
- Keep the full core loop available: Today plan, food/water, habits, weekly review.

## Setup Questions
Goals:
- "What do you want Life App to help with first?"
- "Which body or nutrition target matters most right now?"
- "What would make this week feel like progress?"
Training:
- "How many days per week do you train?"
- "What kind of training do you do most?"
- "Are you following a plan already?"
- "How hard was your last workout?"
Nutrition:
- "How closely do you want to track food?"
- "Which target should Life App keep visible?"
- "What is your easiest repeat meal?"
- "Do you want fast estimates or tighter accuracy?"
Recovery:
- "How has your sleep felt lately?"
- "Do you want Life App to tell you when to push, maintain, or recover?"
- "What recovery habit would help most?"
Habits:
- "Choose up to 3 habits for this week."
- "When and where will the first habit happen?"
- "What is the smallest version that still counts?"
- "Do you want reminders?"
Data source:
- "Where should Life App read your health signals from?"
- "Connect Garmin, choose another app for later, or continue manually."
Mode/theme:
- "How should Life App speak to you?"
- Simple: fewer metrics, direct actions.
- Performance: more signals, compact athlete-style dashboard.
- Theme: Light, Dark, System.

## Pattern Synthesis
- WHOOP: strong recovery identity, morning readiness, subscription value framing.
- Garmin: deep signals, but Life App should translate data into clear action.
- Bevel: clean wearable interpretation and calm readiness summaries.
- Runna: goal-led setup and confidence, but full training plans stay out of v1.
- Strava: progress identity and later accountability, not first-loop social.
- MyFitnessPal/Cronometer: familiar targets, barcode/database expectations, fast edit/correction.
- MacroFactor: adaptive coaching is a later premium loop; MVP uses simple targets and weekly adjustment.
- Cal AI/photo apps: photo logging is convenience with confidence and correction, not source of truth.
- Mobbin-style patterns: short steps, one decision per screen, progress indicator, value preview before paywall, free continuation.

## Paywall Plan
Where it appears:
- Do not block onboarding completion.
- First soft paywall after plan preview or first Today visit; allow "Continue free."
- Later prompts after value moments: weekly review insight, AI scan limit, advanced wearable insight, saved meal limit, trend view.
- Test timing after onboarding, after first weekly review, and at AI/logging limit.
Free includes:
- Goal onboarding, Garmin/demo/manual data path, Today dashboard, basic recommendations.
- Manual food/water logging, calories, protein, macros, water basics.
- One to three habits, basic recovery/sleep state, weekly review.
- Limited saved meals and limited AI/photo trial only if economics allow.
Premium includes:
- Higher AI photo allowance, unlimited saved meals/custom foods, barcode/label scanning if not free.
- Deeper weekly insights, richer wearable summaries, adaptive targets, selected micronutrients.
- Private accountability/share summaries, ad-free experience if ads are tested, data export if requested.
Never paywall:
- Basic onboarding, basic Today plan, manual food/water logging, basic habit check-in.
- Basic recovery/manual check-in, clear missing-data states, privacy/data controls.
- Editing AI food estimates and manual fallback routes.
Later, not MVP:
- AI trainer personas, eight-week programmes, Runna-style adaptive running plans.
- Advanced meal planning/grocery lists, human coach add-ons, broad integrations, social feed.

## Example Screen Copy
Welcome:
- "Your health apps collect the data. Life App turns it into today's plan."
- "Know whether to train, fuel, hydrate, recover, and repeat."
Goals:
- "Pick the outcomes you want Life App to keep you honest about."
- "You can change these anytime."
Data:
- "Garmin is the fastest way to personalize your plan."
- "No Garmin? Continue manually and Life App will still guide today."
Plan preview:
- "Today looks like a moderate day."
- "Keep training easy, hit 140g protein, drink 2.5L water, and finish your mobility habit."
Paywall:
- "Upgrade when you want deeper insight and less logging friction."
- "Premium adds more AI scans, unlimited saved meals, richer wearable insights, adaptive targets, and advanced weekly reviews."
- CTA: "Start Premium"; secondary: "Continue free."

## Handoff Notes For ChipCode
- Build a linear onboarding flow with branch-specific cards.
- Persist setup answers into profile/settings.
- Use Garmin as the primary connection card; show other integrations as future/manual fallback.
- Support Simple and Performance modes in onboarding and Today.
- Include Light, Dark, and System theme choices.
- Paywall should be dismissible in the MVP prototype.
- Add free/premium labels only where they clarify boundaries.
- Empty states are required: syncing, not enough data, no meals, no habits, weekly review not ready.
- Keep language non-medical: readiness, training, recovery, fuel, hydration, consistency.

## Risks And Tests
Risks:
- Too much onboarding delays Today; too little makes recommendations generic.
- Garmin-first may alienate non-Garmin users without a strong manual/demo path.
- Early paywall may reduce trust; late paywall may hide the business model.
- AI food logging may overpromise without confidence, edits, and fallback.
- Premium boundaries may feel punitive if the daily loop is restricted.
Tests:
- Onboarding completion by step and branch.
- Time from welcome to Today.
- Garmin vs other-app vs manual continuation.
- Simple vs Performance retention.
- Theme selection and readability.
- First-day food, water, habit, and training-decision completion.
- Paywall comprehension and dismissal after plan preview.
- Conversion intent after first weekly review.
- AI scan limit acceptance if included.
- Interview prompt: "Could you explain what is free and what Premium adds?"
