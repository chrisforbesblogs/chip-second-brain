# Life App Pricing Strategy
Date: 2026-06-07
Status: Focused monetisation recommendation for onboarding/paywall prototype
Owner: ChipThink

Source inputs:
- `Projects/projects/lifeapp/MVP_SPEC.md`
- `Projects/projects/lifeapp/notes/prototype/onboarding-paywall-brief-2026-06-07.md`
- `Projects/projects/lifeapp/notes/prototype/account-setup-onboarding-audit-2026-06-07.md`
- `Projects/projects/lifeapp/notes/prototype/full-app-brief-design-plan-2026-06-07.md`
- Prior monetisation note: `Projects/projects/lifeapp/notes/product-discovery/step-04-monetization-ai-food-questions-2026-06-07.md`

## Recommendation

Use freemium subscription pricing with one clear paid tier in the MVP prototype and a visible-but-disabled Coach Later tier.

The product should feel useful before payment: basic onboarding, account creation, Garmin/demo/manual path, Today plan, manual food/water logging, habits, and basic weekly review stay free. Premium should justify payment by removing logging friction and making wearable/nutrition data more useful through richer insights, limits lifted, and adaptive targets.

## Simulated Pricing

Use these prices in the prototype as simulated test pricing, not final launch pricing:

| Tier | GBP | USD | Prototype role |
| --- | ---: | ---: | --- |
| Free | GBP0 | $0 | Useful daily plan and habit loop |
| Premium Monthly | GBP9.99/month | $12.99/month | Main conversion offer |
| Premium Annual | GBP69.99/year | $89.99/year | Best value offer, about 42 percent off monthly |
| Coach Later | From GBP29.99/month | From $39.99/month | Disabled/future tier for coaching/programmes |

Default the paywall selection to annual with a "Best value" label, while keeping monthly visible and easy to compare.

## Tier Boundaries

### Free

Purpose: build trust and a daily habit.

Includes:
- Goal onboarding, account setup, mode/theme, and basic profile.
- Garmin MVP path, simulated Garmin/demo state, and manual entry path.
- Today dashboard with readiness label and basic daily actions.
- Simple Mode as the default cleaner experience for average users.
- Manual meal, snack, water, and habit logging.
- Calories, protein, macros, water basics.
- One to three habits, partial/skip states, and basic consistency view.
- Basic recovery/manual check-in and transparent synced/simulated/manual/missing-data states.
- Basic weekly review with one next-week focus.
- Privacy controls, data-source controls, and manual fallback routes.

Free limits to test:
- Saved meals: 3.
- AI/photo scans if present: 3 trial scans total or 1 per week.
- Weekly review: summary only, no deeper trend explanations.
- Wearable insights: basic reason text only.

### Premium

Purpose: sell deeper clarity and less logging friction.

Includes:
- Unlimited saved meals, recent meal shortcuts, and custom foods.
- Higher AI/photo food allowance if included in the prototype.
- Barcode/label scanning if that capability is present.
- Richer wearable summaries: sleep, HRV/recovery, training load, refuel, and readiness drivers.
- Advanced weekly review with trends, explanations, and suggested target changes.
- Adaptive protein, hydration, recovery, and training-day nutrition targets.
- Performance Mode detail layer: nerdier metrics, signal history, load/readiness context, and compact athlete-style dashboard.
- Private accountability/share summaries later if validated.
- Data export later if requested by early users.
- Ad-free experience only if ads are ever tested.

Premium should not be required to create an account, connect the basic Garmin path, use Today, log manually, check habits, edit AI estimates, or access privacy controls.

### Coach Later

Purpose: future higher-price layer after the core daily loop proves retention.

Potential includes:
- AI trainer personas.
- Eight-week programmes.
- Adaptive running/strength/nutrition plans.
- Advanced meal planning and grocery lists.
- Human coach or expert add-ons.
- Group accountability or specialist programmes.

In the prototype, Coach Later should be shown as "Coming later" or visually muted. Do not let it compete with Premium as the main purchase decision.

## Best First Paywall Moment

Best first moment: after Step 7 "Plan Preview And Save" and account/demo choice, either immediately before the first Today view or as a soft card on the first Today visit.

Recommended prototype flow:
1. User completes goals, data source, mode/theme, and plan preview.
2. User creates account to save/sync or continues with demo data.
3. Show a dismissible Premium paywall framed as "unlock deeper insight and less logging friction."
4. Allow "Continue free" and land on Today.

Do not put the paywall before goals, before data-source choice, or inside account creation. Account setup should feel like saving the plan, not paying for the app.

Later paywall triggers:
- User reaches saved meal limit.
- User reaches AI/photo scan limit.
- User taps an advanced wearable insight in Performance Mode.
- User opens advanced weekly review after the first useful week.
- User taps adaptive target explanation.

## Trial And Annual Discount

Trial recommendation:
- Offer a 7-day free Premium trial.
- Start trial after the plan preview or from the first Today paywall.
- Require no trial for Free; "Continue free" remains available.
- If app-store payment rules require payment details, copy should say so plainly.

Annual recommendation:
- Annual should be the primary value anchor: GBP69.99/year or $89.99/year.
- Label as "Save about 40 percent" or "Best value."
- Keep monthly at GBP9.99/$12.99 for lower commitment.
- Do not use aggressive countdowns or health-anxiety pressure.

## Premium Justification

Features most likely to justify Premium:
- Unlimited saved meals and custom foods because they reduce daily friction.
- AI/photo scan allowance because it is a visible convenience upgrade.
- Richer wearable explanations because Life App's core promise is turning Garmin-style signals into actions.
- Advanced weekly review because it turns tracking into adjustment.
- Adaptive targets because they connect nutrition, recovery, and training days.
- Performance Mode depth because engaged users asked for nerdier metrics and detailed insights.

Simple Mode should remain clean and action-first for average users. Premium can enhance Simple Mode with better explanations and fewer limits, but it should not make Simple Mode busier.

## Paywall Copy Options

Headline options:
- "Go deeper when you are ready."
- "Unlock the full daily plan."
- "Less logging. Clearer insight."

Support copy options:
- "Free keeps your daily plan, logging, habits, and weekly summary. Premium adds deeper wearable insights, adaptive targets, and faster food logging."
- "Use Life App free for the core daily loop. Upgrade when you want richer explanations and fewer limits."
- "Premium helps connect recovery, training, nutrition, and habits into sharper weekly adjustments."

Feature bullets:
- "Unlimited saved meals and faster food logging"
- "Advanced weekly review and trend explanations"
- "Richer Garmin-style recovery, sleep, and training insights"
- "Adaptive protein, hydration, and recovery targets"
- "Performance Mode metrics for deeper analysis"

CTA options:
- Primary: "Start 7-day trial"
- Secondary: "Continue free"
- Annual label: "Best value"
- Coach Later label: "Coming later"

Price display:
- "Premium Annual - GBP69.99/year"
- "Premium Monthly - GBP9.99/month"
- "Prices shown for prototype testing."

## Handoff Notes For ChipCode

- Add simulated pricing to the paywall: Free GBP0/$0, Premium GBP9.99/$12.99 monthly, Premium GBP69.99/$89.99 annual, Coach Later from GBP29.99/$39.99 marked coming later.
- Default selected plan to Premium Annual with "Best value" and show monthly as an alternate.
- Keep the paywall dismissible with "Continue free."
- Place first paywall after plan preview/account save choice or as the first Today soft paywall.
- Do not merge account setup and paywall; account saves/syncs the plan, Premium unlocks deeper insight and lower friction.
- Make Free/Premium/Coach Later boundaries visible, but avoid plastering labels across every screen.
- Simple Mode paywall language should emphasize cleaner guidance and less friction.
- Performance Mode paywall language can mention advanced metrics, trend explanations, and wearable signal depth.
- Coach Later should be disabled or muted so Premium remains the only active paid decision.
- Include a small prototype disclaimer: "Simulated pricing for testing."

## Validation Questions

- Can users explain what remains free after seeing the paywall?
- Does annual feel like a reasonable value anchor or too expensive for a new product?
- Do users see Premium as deeper clarity and less friction, not as the basic app being withheld?
- Are average users comfortable staying in Simple Mode without feeling pushed into nerdier metrics?
- Do Performance users understand which advanced insights are Premium?
