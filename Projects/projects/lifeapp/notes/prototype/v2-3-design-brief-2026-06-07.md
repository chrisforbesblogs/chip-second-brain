# Life App V2.3 Prototype Design Brief

Date: 2026-06-07
Status: Prototype design brief for ChipCode
Owner: ChipBoss

Source inputs:
- Current prototype README: `Projects/projects/lifeapp/assets/prototype/README.md`.
- V2 redesign brief: `Projects/projects/lifeapp/notes/prototype/v2-prototype-redesign-brief-2026-06-07.md`.
- Onboarding pattern research: `Projects/projects/lifeapp/notes/research/onboarding-patterns-health-fitness-mobbin-2026-06-07.md`.
- Pricing strategy: `Projects/projects/lifeapp/notes/monetisation/pricing-strategy-2026-06-07.md`.
- Chris/Charley prototype feedback captured on 2026-06-07.

## Purpose

V2.3 should make the prototype feel like a coherent premium health product, not just a correct sequence of screens.

The current v2.1 prototype already has the right strategic structure:
- 18-screen onboarding built from the 9-part v2 formula.
- Beginner / Intermediate / Advanced density.
- Today, Training, Nutrition, Calendar, and Log navigation.
- Account setup near the end.
- Dismissible premium preview with simulated pricing.
- Dark-first visual system.

V2.3 should focus on quality, polish, and product believability:
- sharper onboarding copy;
- clearer plan generation and account-save moment;
- richer Today screen hierarchy;
- better Nutrition and Calendar product surfaces;
- a more useful Log;
- consistent premium/performance styling;
- clearer labels for synced, simulated, manual, and missing data.

## Product Promise

Use this promise across the prototype:

> Life App turns health, training, nutrition, and wearable data into clear daily guidance.

Avoid over-narrow lines such as "one clear health plan for today" because they make the product sound too temporary and too shallow.

Good supporting copy:
- "See what your body is telling you, what changed, and what to do next."
- "Connect Garmin or continue manually. Life App keeps the guidance useful either way."
- "Choose a simple summary or a deeper performance view without changing products."

Avoid:
- medical diagnosis language;
- "AI knows your body" claims;
- generic wellness copy;
- copy that makes the free app sound useless.

## V2.3 Priorities

### 1. Make onboarding feel designed, not like a questionnaire

Keep the current 18 micro-screens, but make each screen visually distinct enough that the flow does not feel repetitive.

Required improvements:
- Add stronger progress context: short step labels such as Goal, Training, Nutrition, Data, Preview, Save, Premium.
- Make each screen's primary decision obvious above the fold.
- Use option cards with clear selected states.
- Keep one decision per screen.
- Keep secondary explanations short.
- Make "Preview with demo data" feel legitimate, not like a fallback for failure.

Do not add:
- theme choice in onboarding;
- habits setup;
- medical forms;
- long free-text inputs;
- sign-up before the plan preview.

### 2. Tighten the onboarding sequence copy

Recommended screen intent:

1. Welcome
   - Headline: "Your health data, turned into daily guidance."
   - CTA: "Start setup"
   - Secondary: "Preview with demo data"

2. Primary goal
   - "What should Life App help with first?"
   - Options: Train smarter, Improve body composition, Recover better, Build consistency.

3. Secondary goal
   - "What else should it keep an eye on?"
   - Allow one extra choice, or let the user skip.

4. Training days
   - "How often do you train right now?"
   - Options: 0-2, 3-5, 6+ days per week.

5. Training type
   - "What kind of training matters most?"
   - Options: Strength, Running/cardio, Hybrid, General fitness.

6. Training confidence
   - "How confident are you choosing when to push or recover?"
   - Options should map to coaching depth, not judgement.

7. Experience level
   - "How much detail do you want?"
   - Beginner: clear actions.
   - Intermediate: balanced signals.
   - Advanced: dense metrics and analysis.

8. Nutrition tracking style
   - "How closely do you want to track food?"
   - Options: Quick targets, Macro aware, Detailed logging.

9. Nutrition focus
   - "What should Life App keep visible?"
   - Options: Protein, Calories/body weight, Fuel training, Hydration.

10. Hydration/fuel confidence
   - "How dialled-in does your fuelling feel?"
   - Use this to shape Nutrition and Today copy.

11. Data source
   - "Where should Life App read your health signals from?"
   - Garmin recommended, Other wearable/app, Manual/demo.

12. Garmin/data trust
   - "Connect data when you are ready."
   - Include manual and demo reassurance.

13. Consent/data state
   - Use plain trust copy:
     - "You control connections and can disconnect anytime."
     - "We show when data is synced, simulated, manual, or missing."
     - "Life App gives fitness and recovery guidance, not medical advice."

14. Plan generation
   - Make this feel like synthesis, not fake loading.
   - Show the chosen goal, data source, experience level, and nutrition posture as inputs.

15. Plan preview
   - Show a mini Today result before account or payment.
   - Include readiness, training action, nutrition focus, hydration target, and log prompt.

16. Save your plan
   - Position account creation as saving and syncing, not as a gate.

17. Account options
   - Apple, Google, email, continue with demo data.
   - Add privacy reassurance near the options.

18. Premium preview
   - Dismissible.
   - Annual selected by default.
   - Continue free visible.

### 3. Strengthen Today

Today should feel like the reason the product exists.

Beginner Today:
- Large readiness/recovery ring.
- One direct recommendation.
- Four readable signal cards: Sleep, Recovery, Training Load, Fuel/Hydration.
- Today's action list:
  - Training adjustment.
  - Protein or fuel target.
  - Hydration target.
  - Recovery prompt.
- Use plain explanation copy:
  - "Sleep was shorter and training load is high, so keep today's session easy."

Intermediate Today:
- Readiness ring plus 6-8 signal cards.
- Show trend hints, not just current values.
- Explain why the recommendation changed.
- Keep actions visually dominant over raw metrics.

Advanced Today:
- Dense signal grid with compact cards.
- Include HRV trend, resting HR, sleep debt, training load, acute/chronic load proxy, calories, protein, carbs, hydration, body weight trend, and recent lift/run marker.
- Include a guidance block with:
  - recommended training adjustment;
  - why;
  - what to watch tomorrow.

Advanced should still end in guidance. Do not let it become charts without a decision.

### 4. Make Nutrition look like a real product surface

Nutrition should not read as a basic calorie table.

Required sections:
- Training-day target summary.
- Calories, protein, carbs, fat, and water.
- Quick add buttons for meal, snack, water, saved meal.
- Recent meals / saved meals.
- Insight block:
  - protein behind;
  - fuel before training;
  - hydration catch-up;
  - recovery day target.

Advanced additions:
- macro split;
- meal timing;
- refuel target;
- weekly average;
- adherence trend.

Use amber/gold for nutrition/fuel states and cyan for hydration. Do not make every nutrition state green.

### 5. Make Calendar feel performance-led

Calendar should be a health and training week view, not a dull admin grid.

Required sections:
- Week strip with readiness/load markers.
- Planned sessions.
- Recovery days.
- Nutrition focus days.
- Weight/check-in markers.
- Weekly summary card.

Advanced additions:
- mini trend row for load, sleep, weight, and nutrition adherence.

Design direction:
- Use compact markers, mini rings, and chips.
- Show why certain days are push, maintain, easy, or recover.
- Make today visually obvious.

### 6. Make Log useful enough to justify replacing Habits

Log is the user's history and manual input surface.

Required sections:
- Today's quick log:
  - weight;
  - energy;
  - soreness;
  - notes.
- Body weight progression.
- Lifting progress.
- Garmin health stats history.
- Manual daily check-ins.
- Nutrition history.
- Data source status.

Good Log copy:
- "Add the signals Garmin cannot see."
- "Manual notes help explain tomorrow's guidance."
- "Simulated data is labelled until you connect a real source."

### 7. Make Profile / Settings the home for controls

Profile / Settings should be available from the top-right.

Include:
- account state;
- data connection and disconnect controls;
- theme: dark, light, system;
- experience level: Beginner, Intermediate, Advanced;
- privacy/data controls;
- subscription status;
- demo/manual data reset.

Theme must stay out of onboarding and the main dashboard.

### 8. Polish the paywall without making it pushy

Placement:
- after plan preview and account/demo choice;
- before the first full Today, or as a first-Today overlay/card.

Rules:
- Dismissible.
- "Continue free" always visible.
- Account creation is not payment.
- Free still includes core Today, basic logging, basic Garmin/manual/demo path, and privacy controls.
- Premium sells deeper insight, adaptive targets, advanced weekly reviews, and less logging friction.

Use simulated pricing:
- Free: GBP0 / $0.
- Premium Monthly: GBP9.99 / $12.99.
- Premium Annual: GBP69.99 / $89.99, Best value.
- Coach Later: from GBP29.99 / $39.99, Coming later.

Recommended headline:
- "Go deeper when you are ready."

Recommended support copy:
- "Free keeps the daily plan and basic logging. Premium adds richer wearable explanations, adaptive targets, advanced weekly reviews, and less logging friction."

## Visual System

V2.3 should keep the dark-first performance direction but improve contrast, spacing, and state clarity.

Use:
- dark background: `#080C0D`;
- dark surface: `#121819`;
- elevated surface: `#1A2224`;
- primary text: `#F4F7F2`;
- secondary text: `#9AA7A2`;
- performance green: `#4DDF87`;
- training blue: `#5E9CFF`;
- nutrition amber: `#F2B84B`;
- hydration cyan: `#43C7D9`;
- warning coral: `#FF6B5F`;
- progress mint: `#78E3B0`.

Accent rules:
- Readiness/recovery: green, amber, coral, always with text labels.
- Training/load: blue.
- Nutrition/fuel: amber.
- Hydration: cyan.
- Warnings: coral only for meaningful attention states.
- Progress: mint/green, used sparingly.

Avoid:
- copying WHOOP black/lime styling;
- Garmin teal/white cloning;
- Apple Health medical-white styling;
- cheap neon glows;
- dull grey calendar grids;
- one-note green dashboards;
- purple-heavy gradients;
- low-contrast dark cards.

## Interaction And State Requirements

Prototype state should visibly affect:
- Today recommendation;
- Today density;
- Training recommendation;
- Nutrition targets;
- Calendar weekly markers;
- Log data status and manual prompts;
- Profile experience level and data-source state.

Data state labels:
- synced;
- syncing;
- simulated;
- manual;
- missing.

Use labels as well as colour so the state is accessible and clear.

## Implementation Scope

Update only prototype files unless asked otherwise:
- `Projects/projects/lifeapp/assets/prototype/index.html`
- `Projects/projects/lifeapp/assets/prototype/README.md`

Expected v2.3 prototype changes:
- Update README version and changelog to v2.3.
- Sharpen onboarding copy using the screen intent above.
- Add or improve progress labels across onboarding.
- Make plan generation show selected inputs.
- Make account setup feel like save/sync, not signup-first.
- Keep premium preview dismissible and priced.
- Improve Today hierarchy for Beginner, Intermediate, and Advanced.
- Improve Nutrition from target table into a decision surface.
- Improve Calendar into a performance week view.
- Improve Log with meaningful history/manual sections.
- Add Profile / Settings top-right if feasible in this pass.
- Keep theme controls in Profile / Settings only.
- Use the v2.3 colour and accent rules consistently.
- Verify embedded JavaScript compiles.
- Step through onboarding to Today in a browser.

## Acceptance Checklist

- Onboarding reaches Today without dead ends.
- Every onboarding screen has one clear decision.
- Demo/manual path feels intentional.
- Account setup appears near the end.
- Paywall is dismissible with Continue free.
- Free vs Premium boundaries are understandable.
- Today shows different density for Beginner, Intermediate, and Advanced.
- Today explains what to do next, not just what happened.
- Nutrition includes quick actions and insights.
- Calendar shows training/recovery/nutrition context for the week.
- Log includes body weight, lifting progress, health stats, manual check-ins, and nutrition history.
- Profile / Settings contains theme and experience-level controls.
- Data state is labelled wherever it affects trust.
- Dark UI has clear contrast and visible surface hierarchy.

## Open Questions For Later

- Which exact lifts should appear by default in Log?
- Whether Advanced density is fully free or partly Premium.
- Whether the real app should use email magic link instead of password.
- Whether Coach Later is AI-only, human-led, or hybrid.
- Whether weekly review belongs in Calendar, Today, or a separate surface after v2.3.
