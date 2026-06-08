# Life App Clickable Prototype v2.3

Standalone, dependency-free HTML prototype for the Life App MVP.

## Open

- Open `index.html` directly in a browser.
- Or serve this folder with any static server if preferred.

## V2.3 flow

The prototype keeps the longer 18-screen micro-onboarding flow from the earlier v2 prototype family, but sharpens the copy and state handling so the experience feels closer to a coherent premium health product.

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

Micro-screen breakdown in v2.3:

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
12. Connection trust
13. Consent / data state explanation
14. Plan generation
15. Plan preview summary
16. Save your plan
17. Account options
18. Premium preview

The onboarding keeps account setup near the end and frames it as save/sync. The paywall remains dismissible with Continue free, which lands in the main app Today screen.

## Main app

After onboarding, the main app uses the v2 bottom navigation:

- Today
- Training
- Nutrition
- Calendar
- Log

A Profile / Settings button now appears in the top-right once you are inside the main app. Theme controls live there, not in onboarding.

## What changed in v2.3

- README version updated to v2.3.
- Onboarding copy now follows the sharper 18-screen brief more closely.
- Progress labels and trust states are clearer, including synced, syncing, simulated, manual, and missing.
- Plan generation shows the selected inputs instead of looking like a fake loading spinner.
- Account setup is framed as saving and syncing, not payment-first.
- The premium preview is dismissible, priced, and keeps Continue free visible.
- Today now changes density and copy more clearly across Beginner, Intermediate, and Advanced.
- Nutrition is richer, with quick add, recent/saved meals, hydration, and deeper insight copy.
- Calendar is a more performance-led week view with push/recover/fuel/log markers.
- Log includes body weight, lifting progress, wearable history, manual check-ins, and nutrition history.
- Profile / Settings now holds theme, experience level, source, subscription, and privacy/data controls.
- The prototype remains dark-first and dependency-free.

## State and interactions

- Onboarding selections update the prototype state.
- State affects Today, Training, Nutrition, Calendar, Log, and Profile copy.
- Data state labels are used wherever trust matters.
- Beginner / Intermediate / Advanced meaningfully changes Today density and guidance depth.

## Paywall preview

- A dismissible premium preview appears near the end of onboarding.
- Pricing shown in the prototype is simulated:
  - Free: GBP0 / $0
  - Premium Monthly: GBP9.99 / $12.99
  - Premium Annual: GBP69.99 / $89.99, Best value
  - Coach Later: from GBP29.99 / $39.99, Coming later
- Continue free is always visible.

## Testing notes

- The embedded JavaScript is dependency-free and should compile in a plain browser.
- Verify onboarding button flow, option selection, and navigation switching after changes.
- Confirm the onboarding screens can be progressed through all the way to Today.
- Confirm Continue free works and closes the paywall.
- Confirm Beginner / Intermediate / Advanced changes Today density or copy.
- Open in a browser and step through the flow once before shipping.

## Notes

- Mobile-first layout
- Dark-first colour system from the v2.3 brief
- Prototype remains static and dependency-free
- No external assets or libraries are required
