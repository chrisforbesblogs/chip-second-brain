# Life App Clickable Prototype v2.1

Standalone, dependency-free HTML prototype for the Life App MVP.

## Open

- Open `index.html` directly in a browser.
- Or serve this folder with any static server if preferred.

## V2.1 flow

The prototype now uses a longer micro-screen onboarding flow built from the original 9 core sections. The UI expands that formula into 18 onboarding screens before the main app so the experience can feel more like a polished health / finance-style onboarding journey without turning into a boring form.

Core section order preserved:

1. Promise / welcome
2. Goals
3. Training baseline
4. Experience level
5. Nutrition baseline
6. Data source / trust
7. Plan preview
8. Account setup / save plan
9. Premium preview

Micro-screen breakdown in v2.1:

1. Welcome
2. Primary goal
3. Secondary goal
4. Training days per week
5. Training type
6. Training confidence
7. Experience level
8. Nutrition tracking style
9. Nutrition focus
10. Hydration / fuel confidence
11. Data source choice
12. Garmin trust copy
13. Consent / data state explanation
14. Plan generation / loading
15. Plan preview summary
16. Save your plan
17. Account options
18. Premium preview

The prototype keeps account setup near the end and keeps the paywall dismissible with Continue free, which lands in the main app Today screen.

## Main app

After onboarding, the main app uses the v2 bottom navigation:

- Today
- Training
- Nutrition
- Calendar
- Log

Profile / Settings stays top-right and holds theme controls. Theme selection is not shown in onboarding or on the main dashboard.

## What changed in v2.1

- Onboarding expands from 9 sections into a longer 18-screen micro-flow before the main app.
- The old 9 sections are still the backbone of the flow, but each major section now has a smaller, more intentional decision screen.
- Habits remains removed from the prototype.
- Log stays as the fifth bottom-nav tab.
- Beginner / Intermediate / Advanced still changes dashboard density and copy.
- Today remains the strongest screen and now updates from onboarding choices for goals, training rhythm, training type, experience level, nutrition posture, hydration confidence, and data source.
- Nutrition uses training-day targets, quick add, recent meals, and an insight block.
- Calendar uses a week view with readiness/load markers, session types, recovery, nutrition focus, and log markers.
- Log includes body weight progression, lifting progress, Garmin health history, manual check-ins, and nutrition history.
- The paywall is dismissible and appears after the plan/account save moment.

## State and interactions

- Onboarding selections update the prototype state.
- State affects Today, Training, Nutrition, Calendar, Log, and Profile copy.
- Data state labels include synced, simulated, manual, and missing-style wording where relevant.
- The main prototype defaults to the dark-first v2 palette.

## Paywall preview

- A dismissible premium preview appears near the end of onboarding.
- Pricing shown in the prototype is simulated:
  - Free: GBP0 / $0
  - Premium Monthly: GBP9.99 / $12.99
  - Premium Annual: GBP69.99 / $89.99, Best value
  - Coach Later: from GBP29.99 / $39.99, Coming later
- Continue free is always visible.

## Testing notes

- The embedded JavaScript is kept dependency-free and should compile in a plain browser.
- Verify onboarding button flow, option selection, and navigation switching after changes.
- Confirm the onboarding screens can be progressed through all the way to Today.
- Confirm Continue free works and closes the paywall.
- Check that no string-literal or apostrophe syntax issue has been introduced.
- Confirm the chosen experience level changes dashboard density and Today copy.
- Confirm profile/theme controls stay out of onboarding and the main dashboard.
- Open in a browser and step through the flow once before shipping.

## Notes

- Mobile-first layout
- Dark-first colour system from the v2 brief
- Prototype remains static and dependency-free
- No external assets or libraries are required
