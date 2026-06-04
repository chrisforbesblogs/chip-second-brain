# Parcel Post Implementation Plan

Date: 2026-05-24  
Product: cozy pixel courier game  
Working title: **Parcel Post**

## 1. Product Direction

**Parcel Post** is a cozy pixel-art delivery game where the player controls a small red postman delivering nice parcels around a friendly village.

The feel should be closer to:

- Animal Crossing
- Stardew Valley
- cozy lofi pixel art
- gentle arcade score chasing
- simple mobile controls

It should not feel like neon cyberpunk, combat, or a harsh reflex game.

## 2. One-Line Pitch

Deliver parcels around a cozy pixel village before sunset, build perfect delivery streaks, avoid cute obstacles, and earn stamps to unlock village charm.

## 3. First Prototype Goal

The first test should answer:

> Is it fun to move around a small village, pick up parcels, deliver them, and chase a better end-of-day grade?

Do not build the full game yet. The first version only needs to prove the core loop.

## 4. Target Platform

First test:

- Expo React Native
- Android via Expo Go
- Possible iOS later

Reason:

- We already have Expo set up.
- The game can be grid-based and simple.
- No heavy physics or 3D is required.
- It is a good test for our mobile app workflow.

## 5. MVP Scope

### Must Have

- Start screen
- 10x10 or 12x12 village grid
- Red postman character
- Swipe controls
- Post office pickup tile
- 5 delivery houses
- Parcel pickup and delivery loop
- 60 or 90 second route timer
- Score
- Delivery streak/combo
- One cute hazard type
- End-of-day results screen
- Restart button
- Local high score/stamp count

### Should Have

- Cozy pixel-style UI
- Soft background color palette
- Simple parcel icons
- Delivery feedback animation
- Happy villager reaction text
- Grade system: C, B, A, S

### Later

- Daily route
- More maps
- Unlockable postman outfits
- Unlockable parcel designs
- Lofi music
- Sound effects
- Online leaderboard
- Village decoration rewards
- More hazards
- Weather variants

## 6. Core Gameplay Loop

1. Player starts at the post office.
2. A parcel is assigned.
3. A destination house lights up.
4. Player moves through the village.
5. Player avoids cute hazards.
6. Player reaches the correct house.
7. Delivery completes.
8. Score and streak increase.
9. New parcel appears.
10. Timer runs down.
11. End screen grades the route.
12. Player restarts to improve.

## 7. Controls

Recommended first version:

- Swipe up, down, left, right.
- Postman moves one tile per tick in the current direction.
- Player can change direction at grid intersections.

Alternative:

- Tap adjacent tile to move one step.

Recommendation:

Use swipe controls first. It is more game-like and closer to Snake/Pac-Man, while still being simple enough for Expo.

## 8. Game Board

First board size:

- 10x10 grid for quickest test
- 12x12 grid if the screen feels too small

Tile types:

- Path
- Grass
- House
- Post office
- Pond
- Fence
- Puddle
- Cat/hazard

Only path tiles should be walkable.

## 9. Character

Player character:

- Small red postman
- Red cap
- Red coat or satchel
- Simple 2-frame walking animation later

First prototype can use a styled square/circle placeholder:

- Red body
- Cream face
- Tiny parcel/satchel marker

## 10. Parcels

First prototype parcel types:

1. **Standard parcel**
   - Normal delivery
   - Basic points

2. **Fragile parcel**
   - Bonus if delivered without hitting a hazard
   - First version can just show a fragile icon

3. **Express parcel**
   - Bonus if delivered quickly
   - Adds time pressure

Later parcel types:

- Bakery box
- Birthday gift
- Flower parcel
- Heavy parcel
- Mystery parcel

## 11. Hazards

Use one hazard for the first version.

Best first hazard:

- **Puddle**
  - Slows the postman for 1 second
  - Easy to implement
  - Fits cozy village tone

Later hazards:

- Cat sleeping on the road
- Goose chase
- Bicycle crossing
- Dog steals parcel
- Muddy shortcut
- Garden gate opening/closing

## 12. Scoring

Suggested scoring:

- Pickup parcel: +10
- Successful delivery: +100
- Fast delivery bonus: +50
- Streak bonus: +25 per streak level
- Fragile delivered safely: +100
- Perfect day bonus: +500

Streak:

- Each correct delivery increases streak by 1.
- Hitting a hazard resets streak or reduces bonus.

Grades:

- C: 0-499
- B: 500-999
- A: 1000-1499
- S: 1500+

These numbers should be tuned after playtesting.

## 13. Dopamine Hooks

Keep the dopamine cozy, not aggressive.

Hooks:

- Satisfying delivery pop
- Stamp earned after each run
- Happy villager text
- Streak counter
- End-of-day grade
- New best score celebration
- Parcel variety
- Gentle unlock progress

Avoid:

- Loot-box feel
- Overloaded popups
- Harsh failure screens
- Too many currencies

## 14. Visual Direction

Palette:

- Warm cream background
- Soft green grass
- Muted brown paths
- Red postman accent
- Pastel house colors
- Soft blue water

Style:

- Pixel-inspired tiles
- Rounded but blocky shapes
- Cozy village UI
- Lofi, gentle, warm

Screen mood:

- Morning village delivery route
- Kind, cheerful, calm
- Light challenge, not stress

## 15. First Mockup Screens

### Screen 1: Start

Elements:

- Game title: Parcel Post
- Red postman character
- Cozy village background
- Start Route button
- Best score
- Stamp count

### Screen 2: Gameplay

Elements:

- Top HUD: score, timer, streak
- Village grid
- Post office tile
- Red postman
- Parcel/destination indicator
- Delivery houses
- Puddle hazard

### Screen 3: End Of Day

Elements:

- Route complete or day ended
- Grade
- Parcels delivered
- Score
- Stamps earned
- Restart button

## 16. Technical Architecture

Recommended Expo stack:

- Expo React Native
- TypeScript
- React reducer for game state
- `react-native-gesture-handler` for swipes
- `@react-native-async-storage/async-storage` for best score/stamps

Later polish:

- `react-native-reanimated` for smoother movement
- `expo-av` for music/sounds
- React Native Skia if we want better pixel/glow effects

## 17. State Model

Main game state:

- screen: start | playing | results
- board
- player position
- player direction
- current parcel
- current destination
- timer
- score
- streak
- delivered count
- hazard positions
- high score
- stamps

## 18. Simple Data Structures

Example board tile:

```ts
type TileType = 'path' | 'grass' | 'house' | 'postOffice' | 'puddle' | 'water' | 'fence';

type Position = {
  row: number;
  col: number;
};

type ParcelType = 'standard' | 'fragile' | 'express';
```

Example game state:

```ts
type GameState = {
  status: 'start' | 'playing' | 'results';
  player: Position;
  direction: 'up' | 'down' | 'left' | 'right';
  parcelType: ParcelType | null;
  destination: Position | null;
  score: number;
  streak: number;
  timer: number;
  delivered: number;
  highScore: number;
  stamps: number;
};
```

## 19. Build Steps

### Phase 1: Playable Core

1. Create Expo project.
2. Build static village grid.
3. Render player on grid.
4. Add swipe controls.
5. Add movement tick.
6. Add walls/non-walkable tiles.
7. Add parcel pickup at post office.
8. Add random delivery destination.
9. Add delivery scoring.
10. Add timer.
11. Add restart flow.

### Phase 2: Game Feel

1. Add streak scoring.
2. Add one hazard.
3. Add parcel types.
4. Add delivery feedback.
5. Add end-of-day grade.
6. Add high score/stamps with AsyncStorage.

### Phase 3: Cozy Polish

1. Improve pixel-art tile styling.
2. Add postman sprite.
3. Add parcel icons.
4. Add light animations.
5. Add sound effects.
6. Add lofi music toggle.

### Phase 4: Retention Features

1. Daily route seed.
2. Unlockable outfits.
3. Stamp collection.
4. New village themes.
5. Share result card.

## 20. Acceptance Criteria For First Prototype

The prototype is ready when:

- The app opens in Expo.
- User can start a route.
- User can control the postman with swipes.
- User can pick up and deliver parcels.
- Score increases after deliveries.
- Timer ends the route.
- Results screen appears.
- Restart works.
- Game can be played repeatedly without crashing.

## 21. Key Risks

- Grid movement may feel too slow or clunky.
- Swipe controls may need tuning.
- The game may feel too calm without enough urgency.
- Expo View-based grid may become limiting if we add too much animation.
- Cozy visuals need care; bad placeholder art can make it feel cheap.

## 22. Recommendation

Build the first prototype in Expo as a simple grid game. Keep the scope tight:

- one map
- one postman
- one parcel loop
- one hazard
- score/timer/results

If the core loop feels good, then add art, sound, daily routes, and progression.

The strongest identity is:

> A cozy, pixel-style postal route game where every run feels like a tiny delivery shift in a friendly village.

