# Life App Clickable Prototype

Standalone, dependency-free HTML prototype for the Life App MVP.

## Open

- Open `index.html` directly in a browser.
- Or serve this folder with any static server if preferred.

## Included screens

- 7-step onboarding flow
  - Welcome
  - Goals
  - Training context
  - Nutrition and hydration
  - Habits
  - Data source
  - Mode / theme / plan preview
- Today
- Calendar
- Training
- Nutrition
- Habits
- Profile
- Dismissible paywall preview

## How to use the onboarding

- Start on **Welcome** and step through the linear flow.
- Choose a data source:
  - **Garmin**: primary path, shows connected-style copy.
  - **Other wearable/app**: normalized as a valid path, with “coming next” copy.
  - **No connection / manual entry**: supported path with manual check-in copy.
- Pick **Simple** or **Performance** mode and a **Light** or **Dark** theme in the final step.
- Finish setup to land on **Today**.
- The setup state updates Today, Training, Nutrition, Habits, Calendar, and Profile copy where practical.

## Paywall preview

- A dismissible premium preview appears without blocking onboarding completion.
- Use **Continue free** to proceed into the prototype.
- The preview explains the MVP boundary between **Free**, **Premium**, and **Coach later**.

## Notes

- Mobile-first layout
- Light and dark theme toggle
- Dark mode aims for a WHOOP-inspired performance vibe without copying branding
- Light mode keeps the same information architecture in a cleaner daytime style
- The prototype stays static and dependency-free
- Cool animations are intentionally not included in this MVP prototype
