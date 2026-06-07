# Life App V2 Onboarding Patterns: Health And Fitness

Date: 2026-06-07
Owner: ChipThink
Status: concise research formula for Architect/ChipCode

## Source Note

Mobbin was only partially accessible in this environment. The public Mobbin site loaded and exposed its general library/search shell, login links, and some public page data, including health/fitness app references such as Ladder and Tonal, but the health/fitness onboarding screenshot collection was not cleanly browseable without login/pro access. OpenClaw web search was also quota-limited during this run.

This note is therefore based on:
- Partial Mobbin access and the platform's public positioning as a real app screenshot and flow library.
- Known onboarding patterns from strong health, fitness, wearable, nutrition, and training apps such as WHOOP, Garmin, Bevel, Runna, Strava, MyFitnessPal, Cronometer, MacroFactor, Cal AI-style food apps, Ladder, and Tonal.
- Existing Life App project notes on v2 onboarding, account placement, paywall timing, pricing, and colour direction.

## Strong Health/Fitness Onboarding Patterns

1. Promise first, setup second
   - Strong apps start with a concrete outcome, not a form.
   - For Life App: "Your health data, turned into useful guidance" is stronger than a generic wellness welcome because it explains the data-to-action promise.

2. One decision per screen
   - Health onboarding becomes heavy when goals, training, nutrition, device access, reminders, and account creation are mixed together.
   - Keep each step focused: goal, training baseline, experience level, nutrition baseline, data source, preview, save.

3. Goal-led personalization
   - Runna-style and coaching apps ask what the user is trying to achieve before asking for detail.
   - Life App should capture the user's first outcome: train smarter, improve body composition, recover better, or build consistency.

4. Baseline without interrogation
   - Better fitness flows use fast ranges and familiar labels instead of long health questionnaires.
   - Life App should ask rhythm and primary training type, not detailed medical history, exact biometrics, or exhaustive preference trees in onboarding.

5. Data-source choice with fallback
   - Wearable-led products make the best path obvious but do not block the user if the device is missing.
   - Life App should make Garmin the recommended path, then offer other wearable interest capture and manual/demo continuation.

6. Value preview before account or paywall
   - Strong flows show a generated plan, score, recommendation, or sample dashboard before asking for identity or money.
   - Life App should show a mini Today preview before account setup and premium framing.

7. Trust copy close to data permission
   - Health data consent works best when it is plain, specific, and near the connection step.
   - Use copy such as: "You control connections and can disconnect anytime" and "Life App uses health and training data for recommendations, not medical advice."

8. Mode controls as density, not separate products
   - Advanced users want metrics; beginners want confidence and guidance. The product should not fork into different brands.
   - Beginner, Intermediate, and Advanced should change density, labels, and explanation depth while keeping the same visual system.

## Bad Patterns To Avoid For Life App

- Sign-up-first onboarding. It asks for trust before the user sees the plan.
- Medical-style questionnaires. Life App is guidance for training, recovery, nutrition, and logging, not clinical triage.
- Theme selection inside onboarding. Theme belongs in Profile/Settings for v2.
- Habits setup in v2 onboarding. Habits were removed from v2; Log is now the fifth main nav item.
- Device dead ends. If Garmin is unavailable, users still need manual and demo paths.
- Hidden simulation. Prototype/demo data must be visibly labelled as simulated, manual, synced, or missing.
- Paywall as account setup. Account saves and syncs the plan; Premium adds deeper insight and less friction.
- One giant "preferences" screen. It will feel like homework and produce lower-quality choices.
- Dull calendar styling. Calendar should feel like a training/recovery week view, not a plain admin schedule.
- Overclaiming AI or wearable accuracy. Avoid "we know your body" and any medical diagnosis language.

## Reusable Life App V2 Onboarding Formula

Use 9 screens if visual clarity matters. If the prototype must stay shorter, combine screens 7 and 8, but keep account setup near the end.

| Order | Screen | Purpose | Copy Direction | Selected/Entered |
| --- | --- | --- | --- | --- |
| 1 | Welcome | State the promise and offer a low-friction start. | "Your health data, turned into useful guidance." Supporting copy: connect training, recovery, nutrition, and logs so Life App can show what matters today. | CTA: Start setup. Secondary: Preview with demo data. |
| 2 | Goals | Anchor personalization in outcomes. | "What should Life App help with first?" Keep choices plain and outcome-led. | Select 1-2: Train smarter, improve body composition, recover better, build consistency. |
| 3 | Training Baseline | Capture enough context to shape guidance. | "What does your training look like right now?" | Select rhythm: 0-2, 3-5, 6+ days/week. Select type: strength, running/cardio, hybrid, general fitness. |
| 4 | Experience Level | Set dashboard density and coaching language. | "How much detail do you want?" | Select Beginner, Intermediate, or Advanced. Persist to profile and allow change later. |
| 5 | Nutrition Baseline | Establish food/hydration posture without forcing full tracking. | "How should Life App help with food and hydration?" | Select tracking style: quick targets, macro aware, detailed logging. Select focus: protein, calories/body weight, fuel training, hydration. |
| 6 | Connect Data | Explain the source of recommendations and give a fallback. | "Where should Life App read your health signals from?" | Choose Garmin recommended, other wearable/app interest, or manual/demo. Consent copy appears here. |
| 7 | Plan Preview | Show value before identity or payment. | "Here is how Life App would guide today." | Show mini Today: readiness/recovery label, training action, nutrition focus, hydration target, log prompt. Advanced also sees driver preview. |
| 8 | Account Setup / Save Plan | Save, sync, and make device connection durable. | "Create an account to save this plan and keep your data synced." | Options: Continue with Apple, Google, email, or demo data. Include health data consent and terms/privacy acknowledgement. |
| 9 | Premium Preview | Present pricing after value is visible, not as a blocker. | "Go deeper when you are ready." Premium is deeper insight and less logging friction. | Show Free, Premium Monthly, Premium Annual best value, Coach Later coming later. CTA: Start Premium. Secondary: Continue free. |

## Account, Consent, And Data Path Placement

Place account setup near the end, after Plan Preview and before first saved/synced Today. Do not put account setup before goals.

Account options:
- Continue with Apple.
- Continue with Google.
- Continue with email, ideally magic link or one-time code.
- Continue with demo data, clearly labelled as not fully saved/synced.

Health data consent copy:
- "Life App uses your health and training data to create your daily plan."
- "You control connections and can disconnect anytime."
- "We show when data is synced, simulated, manual, or missing."
- "Your data is used for recommendations in Life App, not sold."
- "Life App gives fitness and recovery guidance, not medical advice."

Garmin/manual path trust copy:
- Garmin: "Connect Garmin to turn sleep, HRV/recovery, training load, steps, and workouts into today's guidance."
- Manual: "No Garmin? Use a quick daily check-in and Life App will still guide training, recovery, nutrition, and hydration."
- Demo: "Preview with simulated data. You can save and connect real data later."

## Paywall Timing And Pricing Strategy

Paywall should appear near the end, tied to the plan preview and the pricing strategy already defined for v2.

Recommended timing:
- Best: after account setup/save plan, before first full Today.
- Acceptable: as a dismissible first-Today overlay after the plan preview.
- Do not block basic onboarding, account creation, Garmin/manual/demo path, Today, manual logging, or privacy controls.

Pricing framing:
- Free: core Today, basic recommendations, manual logging, basic Garmin/manual/demo path, basic weekly review.
- Premium Monthly: GBP9.99 / $12.99.
- Premium Annual: GBP69.99 / $89.99, marked Best value.
- Coach Later: from GBP29.99 / $39.99, Coming later.

Premium message:
- "Premium adds deeper wearable explanations, adaptive targets, advanced weekly reviews, and less logging friction."
- Keep "Continue free" visible.

## Beginner / Intermediate / Advanced Handling

Use the same product, brand, navigation, and colour system for all three. The difference is density and guidance.

Beginner:
- Fewer metrics, larger summary, warmer explanatory copy.
- Shows readiness/recovery label, one training recommendation, one nutrition focus, hydration, and one quick log prompt.
- Copy explains why: "Recovery is not fully back, so keep training easy today."

Intermediate:
- Balanced signal cards and action guidance.
- Shows readiness, sleep, recovery/HRV proxy, training load, protein, hydration, steps, and weekly trend.
- Copy connects cause and action: "Higher load plus shorter sleep means maintain, not push."

Advanced:
- Dense metrics and compact analysis.
- Shows readiness drivers, HRV trend, resting HR, sleep debt, training load, acute/chronic load proxy, calories, protein, carbs, hydration, weight trend, lifting progress, and notes.
- Still ends with guidance, not just charts.

## Colour And Theme Direction

### Dark-First Vs Light-First Patterns

Strong performance and wearable products often use dark-first onboarding because it feels premium, focused, and signal-led. It supports readiness rings, recovery status, load charts, and high-contrast data cards. The risk is muddy contrast or a product that feels intimidating to normal users.

Strong mainstream fitness and nutrition apps often use light-first onboarding because it feels approachable, familiar, and easy to scan. The risk is looking generic, clinical, or like a plain calendar/productivity tool.

For Life App v2, use dark-first for the prototype and main premium/performance identity, with a clean light theme available in Profile/Settings later. Do not ask for theme in onboarding.

### Palette Direction

Life App should feel credible, premium, and performance-aware without copying WHOOP, Garmin, or Apple. Avoid a pure black plus lime WHOOP clone, a Garmin teal/white clone, or Apple Health-style medical white with system rings.

Recommended direction:
- Base dark: near-black charcoal with subtle green-grey undertone.
- Surface: layered dark graphite, not flat black.
- Text: warm off-white for primary, cool muted grey-green for secondary.
- Primary accent: clean performance green, less acidic than WHOOP.
- Secondary accent: controlled blue for training/load and data.
- Warm accent: amber for fuel, hydration nudges, and attention states.
- Error/warning: coral/red used sparingly.
- Light theme: crisp off-white background, graphite text, same accent logic.

Suggested tokens:
- Dark background: `#080C0D`
- Dark surface: `#121819`
- Elevated surface: `#1A2224`
- Primary text: `#F4F7F2`
- Secondary text: `#9AA7A2`
- Performance green: `#4DDF87`
- Training blue: `#5E9CFF`
- Nutrition amber: `#F2B84B`
- Hydration cyan: `#43C7D9`
- Warning coral: `#FF6B5F`
- Progress mint: `#78E3B0`
- Light background: `#F5F7F3`
- Light surface: `#FFFFFF`
- Light text: `#17201A`

### Accent System

- Readiness/recovery: green for ready, amber for moderate, coral for low/recover. Use labels as well as colour.
- Training load: blue scale for load and intensity; avoid making all training states green.
- Nutrition: amber/gold for calories, fuel, meal timing, and protein prompts.
- Hydration: cyan/teal-blue for water targets and hydration status.
- Warnings: coral/red only for clear risk or missing critical action; do not overuse it for normal recovery dips.
- Positive progress: mint/green with check states, trend arrows, and small celebrations.

### What To Avoid

- Dull calendar styling: no plain grey grid as the main Calendar identity.
- Cheap neon: do not rely on glowing green/purple outlines.
- Overly medical blue/white: Life App is performance guidance, not a clinic portal.
- Muddy dark UI: dark surfaces need clear elevation and contrast.
- One-note palette: do not make every metric green, blue, or purple.
- Copying WHOOP/Garmin/Apple: borrow the principle of clear signal hierarchy, not the exact palette or ring language.

### Visual Differences By Experience Level

Beginner:
- Larger cards, fewer accents, more whitespace, more labels.
- Use colour as reassurance and state, not decoration.

Intermediate:
- Medium-density cards, more secondary metrics, subtle trend accents.
- Keep explanations visible but shorter.

Advanced:
- Compact cards, sparklines, segmented status chips, denser grids.
- Same colours and typography; smaller components and deeper drill-downs create the advanced feel.

## Final Handoff Checklist For Architect/ChipCode

- Build onboarding around the 9-screen formula or combine Plan Preview and Save Plan only if needed.
- Keep v2 navigation: Today, Training, Nutrition, Calendar, Log; Profile/Settings top-right.
- Remove Habits from v2 onboarding and nav.
- Move theme controls to Profile/Settings, not onboarding.
- Persist Beginner/Intermediate/Advanced as the primary density setting.
- Make Garmin the recommended data path while preserving other-app interest, manual, and demo.
- Label data state everywhere it matters: synced, syncing, simulated, manual, missing.
- Place account setup near the end with Apple, Google, email, and demo options.
- Keep health data consent plain, non-medical, and close to data connection/account save.
- Place paywall near the end after plan value is visible; keep it dismissible with Continue free.
- Do not paywall basic Today, manual logging, basic Garmin/manual/demo path, account creation, or privacy controls.
- Use the dark-first premium palette direction, with accessible contrast and non-colour labels.
- Make Beginner/Intermediate/Advanced visually distinct through density and guidance, not separate brands.
- Ensure first Today reflects onboarding choices immediately.
