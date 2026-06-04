# Chip Postman UX Wireframes

Date: 2026-05-25  
Context: Mobile postman/parcel arcade game. UX rethink requested because the board needs more screen real estate and the current in-game menu/options are too large.

## Recommendation

Move the game toward a **board-first arcade layout**:

- Landing page stays simple and playful, but does not carry in-game UI weight.
- Options live on their own screen, not inside the active game board.
- In-game view uses a slim top score/status bar.
- The board takes almost the full screen.
- Controls are reduced to arrow/D-pad clusters only.
- Bottom-left and bottom-right thumb zones are reserved for controls.
- Add an accessibility/control preference to move controls to the top if the player prefers.

Wireframe artifact:

- `wireframes/chip-postman-ux-wireframes-2026-05-25.html`

## 1. Landing Page With Options

Purpose: quick start without crowding the player.

Layout:

- Title/logo at top.
- Large primary `Play` action.
- Smaller secondary actions: `Options`, `How To Play`, `Scores`.
- No gameplay controls visible.
- Optional small character/parcel visual, but keep it compact.

## 2. Options / Settings Screen

Purpose: move configuration out of the game board.

Settings to include:

- Sound on/off.
- Music on/off.
- Control placement: `Bottom` or `Top`.
- Control style: `Split arrows` or `D-pad`.
- Haptics on/off.
- Difficulty/speed if already supported.
- Back button returns to landing page or pause menu.

UX note: keep settings as rows with compact toggles. Avoid large decorative buttons.

## 3. In-Game Mode

Purpose: maximise game board visibility.

Layout:

- Top status bar height target: 32-44px.
- Status bar contains only essentials: score, parcels, timer, pause icon.
- Board fills the central area.
- Avoid large side panels or bulky option menus.
- Use pause overlay only when paused.

## 4. Bottom Thumb-Zone Controls

Purpose: keep controls reachable while preserving the board.

Layout:

- Bottom-left thumb zone: left/right/up/down or small D-pad.
- Bottom-right thumb zone: alternative arrows/action if needed.
- Center bottom stays visually light so the board still feels dominant.
- Controls should be translucent or compact if they overlap the board.

Recommendation: if the game only needs movement, use a single D-pad on the bottom-left and reserve bottom-right for future action/power-up. If two-handed play feels better, split horizontal/vertical controls across left/right zones.

## 5. Top Controls Option

Purpose: accessibility and player comfort.

Layout:

- Options screen includes `Controls position: Bottom / Top`.
- In top mode, controls sit below the slim status bar.
- Board starts below the control strip.
- This sacrifices some board height, but helps players who prefer thumbs/hands lower on the phone or who play with one hand differently.

## Proposed Navigation

```text
Landing
  -> Play
      -> Game
          -> Pause
              -> Resume
              -> Options
              -> Quit
  -> Options
      -> Landing
  -> Scores
  -> How To Play
```

## Key UX Decisions

- **Separate settings from play:** options should not occupy permanent in-game space.
- **Slim status bar:** score/status is important, but should not compete with the board.
- **Controls as zones, not panels:** reserve thumb areas without building large UI blocks.
- **Board first:** every in-game choice should be tested against whether it reduces playable space.
- **Top controls as preference:** useful, but not the default because it costs vertical board space.

## Implementation Notes

- Add a `controlPlacement` setting with values `bottom` and `top`.
- Add a `controlStyle` setting with values `dpad` and `splitArrows`.
- Store settings locally.
- Keep game HUD separate from pause/options UI.
- Use safe-area padding for notches/home indicators.
- Test on small phone screens first; if it works there, it will scale up.

## Next Step

Implement the slim in-game HUD and bottom thumb-zone controls first. That directly addresses the screen-real-estate issue and will show whether the board feels large enough before adding more settings polish.
