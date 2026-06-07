# Life App Account Setup Onboarding Audit
Date: 2026-06-07
Status: Focused product-discovery audit
Owner: ChipThink

Source inputs:
- `Projects/projects/lifeapp/MVP_SPEC.md`
- `Projects/projects/lifeapp/notes/prototype/onboarding-paywall-brief-2026-06-07.md`
- `Projects/projects/lifeapp/notes/prototype/full-app-brief-design-plan-2026-06-07.md`
- `Projects/projects/lifeapp/assets/prototype/README.md`

## Recommendation
Account setup should happen after goals and value preview, at the save/sync moment.

Do not ask users to create an account before goals. Life App needs the user to feel the promise first: one daily plan from goals, habits, nutrition, and wearable or manual signals. Early account creation would add friction before trust exists.

Do not leave account creation until much later in the app. Garmin sync, saved goals, reminders, profile settings, and subscription state all imply identity. The right moment is: "Save this plan and keep it synced."

## Placement In Flow
Best placement:
- After current step 7 plan preview.
- Before the first real saved/synced Today state.
- Allow a demo/preview path without an account, but make save/sync require one.

Product logic:
- Goals first: earns relevance.
- Data source before account: clarifies why identity matters.
- Plan preview before account: shows value before asking for credentials.
- Account at save/sync: the request is understandable and purposeful.

## MVP Account Setup Fields
Required:
- Email address or Apple/Google identity.
- Display name or first name.
- Consent acknowledgement for health/wearable data use.
- Terms and privacy acknowledgement.

Optional during onboarding:
- Password, only if using email signup without magic link.
- Marketing emails, default off or clearly optional.
- Time zone, inferred when possible and editable later.

Defer to Profile:
- Date of birth, sex, height, weight, detailed medical context, full notification schedule, emergency or clinical information.
- These are sensitive and not needed to prove the MVP daily-plan loop.

## Auth Options
MVP should present:
- Continue with Apple.
- Continue with Google.
- Continue with email.

Fallback:
- Continue with demo data, clearly labelled as not saved across devices.
- If email auth is included, prefer magic link or one-time code to reduce password friction.

Why:
- Apple is expected for iOS health/fitness apps and signals privacy.
- Google is expected cross-platform and for Android/Google Fit-adjacent users.
- Email is required as an accessible fallback.
- Demo/manual continuation preserves prototype testing and avoids blocking users who are not ready to connect Garmin.

## Garmin And Health Data Trust Copy
Use plain, non-medical trust copy near account and Garmin connection:
- "Life App uses your health and training data to create your daily plan."
- "You control connections and can disconnect Garmin anytime."
- "We show when data is synced, simulated, manual, or missing."
- "Your data is used for recommendations in Life App, not sold."
- "Life App gives fitness and recovery guidance, not medical advice."

Avoid:
- Medical claims.
- Overpromising accuracy.
- Vague "AI knows your body" language.
- Hiding simulated data in the prototype.

## Change To The 7-Step Onboarding
Account setup should not become an eighth heavy setup screen if the product can avoid it. The existing 7-step flow is already near the upper limit for first-run friction.

Recommended adjustment:
- Keep seven core onboarding steps.
- Rename step 7 from "Mode, Theme, Plan Preview" to "Plan Preview And Save".
- Include a compact account panel after the plan preview inside step 7.
- If visual clarity requires a separate screen in the prototype, label it as a save gate rather than a new discovery step.

Account panel content:
- Preview summary: readiness label, training action, nutrition focus, water target, first habit.
- Prompt: "Create an account to save this plan and keep Garmin synced."
- Buttons: Apple, Google, Email.
- Secondary: "Continue with demo data."

## Recommended Final Onboarding Sequence
1. Welcome
   - Promise and demo preview option.
2. Goals
   - Training, body/nutrition, sleep/recovery.
3. Training Context
   - Frequency, activity, plan source.
4. Nutrition And Hydration
   - Tracking posture and visible targets.
5. Habits
   - One to three starter habits, cue, smallest version, reminder preference.
6. Data Source
   - Garmin recommended, other app interest capture, manual/demo fallback.
7. Plan Preview And Save
   - Mode and theme.
   - Today preview.
   - Account setup to save/sync, with demo continuation.

After step 7:
- If account created: land on Today with saved/synced or syncing state.
- If demo continued: land on Today with simulated/manual badge and a persistent but quiet "Save plan" option in Profile or top-right.

## Free Vs Premium At Account Creation
Free at account creation:
- Account, saved goals, basic profile, theme/mode, Garmin/demo/manual path.
- Basic Today dashboard and basic recommendations.
- Manual food/water logging.
- One to three habits.
- Basic recovery/manual check-in.
- Basic weekly review.
- Privacy controls, data-source status, disconnect controls.

Premium should not be required to create an account or connect the basic Garmin MVP path.

Premium framing after account creation:
- Richer wearable insights.
- Advanced weekly review.
- Adaptive targets.
- More AI/photo logging allowance if included.
- Unlimited saved meals/custom foods if that boundary is tested.
- Data export or advanced accountability later if validated.

Account setup copy should not feel like a paywall. Keep premium separate and dismissible after the user has seen the plan or first Today view.

## Handoff Notes For ChipCode
- Do not edit the prototype flow as a generic "sign up first" pattern.
- Add account setup at the plan-preview save/sync moment.
- Keep "Continue with demo data" available in the prototype.
- Add account state to Profile copy: signed out demo, signed in, synced, simulated, manual.
- Make Garmin connection copy explain why account identity is needed.
- Keep privacy/data controls visible from Profile.
- Keep paywall dismissible and separate from account setup.
- Do not block basic onboarding, manual logging, Today, or privacy controls behind Premium.
- If the UI keeps seven steps, fold account setup into step 7. If it uses eight screens for clarity, present the extra screen as "Save your plan", not another setup questionnaire.

## Product Risks To Test
- Whether users trust Garmin/health data access after seeing the plan preview.
- Whether account setup after preview improves completion compared with signup before goals.
- Whether users understand demo data is not fully saved/synced.
- Whether free vs premium boundaries are clear without making account setup feel paid.
- Whether Apple/Google/email coverage is enough for the first prototype audience.
