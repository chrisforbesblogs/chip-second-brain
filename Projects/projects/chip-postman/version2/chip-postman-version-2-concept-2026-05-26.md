# Chip Postman / Parcel Post - Version 2 Concept

Date: 2026-05-26  
Prepared for: ChipCode implementation handoff  
Project hub: `/home/cef-admin/.openclaw/workspace/second-brain/Projects/projects/chip-postman/version2/`

## Executive Summary

Version 2 should move **Chip Postman / Parcel Post** from a simple cozy grid prototype into a warmer, richer, more character-led mobile route game.

The player controls Chip, a cheerful young postman on a small yellow scooter, riding through a stylised village map to deliver parcels across multiple levels. Each level gives the player a fixed route objective: reach delivery points in order, keep moving, avoid water, dodge little black-and-white cats, and finish before the timer or parcel condition runs out.

The strongest direction is **polished 2D top-down/isometric-lite arcade routing**, inspired by the existing generated artwork: sunny village, chunky readable shapes, warm lighting, blue uniform, yellow scooter, expressive character art, and clear route-map UI.

## Game Concept

**One-line pitch:**  
Ride Chip's scooter through a charming village, follow delivery routes, avoid cats and water, and complete increasingly tricky parcel runs across handcrafted levels.

**Core loop:**

1. Player selects a level.
2. Level opens with a short route preview.
3. Chip starts at the post office or route start marker.
4. Player drives along village paths toward marked stops.
5. Obstacles force timing, detours, or steering precision.
6. Successful deliveries award stars, stamps, and unlock the next route.
7. Player replays to improve time, route accuracy, and parcel safety.

## Target Feel

The game should feel:

- Warm, upbeat, and characterful.
- Slightly chaotic, but never harsh.
- Easy to understand in the first 10 seconds.
- Skill-based through steering, route reading, and obstacle timing.
- More polished than a pixel prototype, with mobile-game presentation quality.

Reference feel:

- **Arcade route driving:** simple steering, quick retries, readable hazards.
- **Cozy village charm:** friendly houses, gardens, post boxes, small landmarks.
- **Character-led marketing:** Chip and the scooter should be the emotional hook.

Avoid:

- Abstract grid-only visuals.
- Overly realistic vehicle physics.
- Punishing crash/fail language.
- Dark, cyberpunk, or gritty city styling.

## Art Direction

Use the generated promotional artwork as inspiration, but translate it into practical game assets.

### Visual Pillars

- **Warm sunlight:** golden highlights, soft blue shadows, creamy skies.
- **Chunky charm:** rounded buildings, thick silhouettes, readable props.
- **Polished 2D:** painterly or high-quality cartoon sprites rather than tiny pixel art.
- **Village detail:** red post box, blue parcel box, flower beds, hedges, fences, little cottages.
- **Route clarity:** yellow route lines, bright stop markers, clear danger signals.

### Palette

- Uniform blue: `#1F68C5` / deep outline `#0B2B5C`
- Scooter yellow: `#F5B62E` / highlight `#FFD85A`
- Road warm grey: `#9D8D7D`
- Path tan: `#D6B27A`
- Grass green: `#7CB55C`
- Water blue: `#58AEEB`
- Cat black/white: high contrast with soft outline
- UI navy: `#10294A`
- Reward gold: `#FFC83D`

## Character and Scooter

### Chip

Chip should be a friendly, expressive postman:

- Blue cap with small gold parcel/post badge.
- Blue short-sleeve postal shirt or jacket.
- Brown satchel crossing the body.
- Dark gloves for scooter grip.
- Warm face, large readable eyes, confident smile.
- Slightly oversized head and hands for readability on mobile.

In gameplay, Chip does not need full body detail. The sprite should preserve:

- Blue cap.
- Brown hair/face shape.
- Yellow scooter body.
- Parcel crate or mail bag on the rear.

### Scooter

The scooter is central to Version 2.

- Small yellow delivery scooter.
- Rounded front headlamp.
- Front basket for envelopes or parcels.
- Rear crate stacked with parcels.
- Subtle exhaust puff or wheel dust when accelerating.
- Lean animation on turns.

Minimum gameplay animation set:

- Idle.
- Moving north/east/south/west or 8-direction equivalent.
- Turn/lean frames.
- Delivery celebration pop.
- Bump/skid reaction.
- Water splash reaction.

## Village and Map Style

The game map should read like a toy village from above.

### Camera

Recommendation: **top-down with slight isometric/3/4 asset styling**.

This keeps collision and route logic simple while allowing richer art than a strict grid. ChipCode can implement the first version on a tile map while using polished sprites and decals to soften the grid.

### Map Ingredients

- Curving roads and paved paths.
- Small cottages with coloured roofs.
- Post office start point.
- Red post boxes and blue parcel boxes.
- Village green.
- Bridges over water.
- Ponds, streams, canals, and puddles.
- Garden fences and hedges.
- Market stalls or bakery as later landmarks.
- Route arrows painted or glowing subtly on roads.

### Layout Rules

- Roads must remain readable above decoration.
- Hazards must contrast strongly against roads.
- Water should be obvious as non-driveable.
- Cats should be animated and outlined enough to stay visible.
- Each level should fit within a single mobile screen or support smooth camera follow without disorientation.

## Obstacle Design

Obstacles should create route pressure without feeling mean.

### Water

Water is a hard obstacle.

- Forms: pond edges, streams, puddles, canals, flooded road tiles.
- Main rule: scooter cannot drive through deep water.
- Puddles can be a soft hazard that slows Chip briefly.
- Bridges and stepping-stone road crossings create planned route choices.

Feedback:

- Deep water collision: bounce back, splash, lose a parcel health point or time.
- Puddle: small splash, speed reduction for 0.8-1.2 seconds.

### Little Black-and-White Cats

Cats are the signature moving hazard.

- Small black-and-white village cats.
- They wander, nap, cross roads, or chase parcels briefly.
- They should be cute, not threatening.
- Colliding with a cat should trigger a skid/stop, never harm the cat visually.

Cat behaviours:

- **Sleeping cat:** static blocker on route.
- **Crossing cat:** moves along a short path at intervals.
- **Curious cat:** wanders near parcel stops.
- **Parcel cat:** briefly follows Chip if he drives too close, increasing pressure.

Collision rule:

- Chip brakes and loses time or streak.
- Cat hops away safely.
- Optional parcel wobble animation if carrying fragile parcel.

### Additional Later Obstacles

- Roadworks cones.
- Garden gates opening/closing.
- Delivery van parked across a lane.
- Rolling football.
- Market crowd.
- Wind gusts affecting envelopes.

## Level Structure

Version 2 should launch with handcrafted levels, not procedural generation.

### Level Format

Each level is a route challenge:

- Start point.
- Ordered delivery stops.
- Optional pickup point.
- Timer target.
- Star thresholds.
- Obstacles and moving obstacle paths.
- Route preview line or hint.

### Suggested MVP Levels

1. **Post Office Lane**
   - Tutorial route.
   - One delivery stop.
   - No cats, one visible pond as boundary.

2. **Cat Crossing**
   - Two delivery stops.
   - Introduces black-and-white crossing cat.

3. **Bridge Run**
   - Stream splits the map.
   - Player must use bridge and avoid puddles.

4. **Village Green Loop**
   - Circular route around green.
   - Multiple cats and optional shortcut.

5. **Parcel Rush**
   - Three stops under tighter time.
   - Mix of water, cats, and route decisions.

6. **Market Morning**
   - Denser obstacles.
   - Introduces parked carts or roadwork as a blocker.

### Progression

- Complete level to unlock next.
- Earn 1-3 stars based on time, collisions, and delivery accuracy.
- Optional stamp collection for replay motivation.
- Later worlds can introduce new village zones: canal side, hill cottages, rainy day, seaside pier.

## Mechanics

### Movement

Target Version 2 movement:

- The scooter should feel like it is driving through a village, not stepping from square to square.
- Movement should be continuous along roads, lanes, and curved route segments.
- The player can still use simple mobile inputs, but the on-screen result should be smooth acceleration, eased turns, and natural scooter lean.
- Collision boundaries prevent leaving roads, entering deep water, or clipping through buildings and props.
- If a grid is used internally, it should be invisible implementation data for collision, path validation, and level authoring only.

Recommended first build:

- Road graph with waypoints and lane segments.
- Scooter follows segment-to-segment movement with interpolation.
- Player direction input is buffered before junctions so controls stay responsive.
- Turns happen through short eased arcs instead of instant 90-degree snaps.
- Roads can be authored on a coarse grid for speed, but rendered as curved/rounded paths with no visible square stepping.

Fallback prototype only:

- A tile map may be used briefly to prove route logic.
- Even in the prototype, visual movement should interpolate between points rather than jump tile-by-tile.
- Direction changes should happen at junction trigger zones, not hard tile centres.
- This fallback should not define the final feel or art direction.

### Animation and Motion Feel

The animation plan should be designed around fluid scooter motion from the start.

Scooter animation:

- Idle bounce while stationary.
- Wheel spin or subtle motion blur while moving.
- Lean left/right on turns.
- Gentle squash or suspension bob on acceleration and braking.
- Small dust puff or exhaust puff on start.
- Skid/bump animation when hitting water edge, cones, fences, or cat avoidance zones.
- Delivery celebration: Chip raises an arm, parcel pops, stamp effect appears.

Movement smoothing:

- Use delta-time movement, not frame-count movement.
- Use easing for acceleration, braking, and turns.
- Use route segment headings to rotate the scooter gradually toward its travel direction.
- Allow a small steering assist so the scooter magnetises to the road centreline.
- Use forgiving collision radii rather than exact sprite bounds.

Road and route animation:

- Roads should be drawn as continuous shapes or rounded tile blends.
- Route preview line should animate as a painted/glowing path rather than highlighting squares.
- Direction arrows can curve along the road.
- Destination pins should pulse softly.
- Cat path previews can use tiny paw-print hints on tutorial levels.

Implementation guidance:

- Represent roads as nodes and segments even if authored from a grid.
- Each segment should have start/end points, optional curve control points, width, speed modifier, and tags.
- The scooter stores world coordinates and velocity, not just row/column.
- Obstacles use world-space hit zones or paths.
- Level data can still include coarse tile metadata for editor simplicity, but gameplay should read from road segments and collision shapes.

### Deliveries

- Active stop is marked with a bright pin, glowing house, or parcel icon.
- Player must reach stops in order.
- Delivery happens automatically within a small radius.
- Delivery triggers parcel pop, stamp sound, score/time bonus.

### Route Guidance

Use route clarity as a major UX feature:

- Before the level starts, show the full route line for 2 seconds.
- During play, show only the next segment or destination marker.
- Optional difficulty setting can reduce route hints later.

### Scoring

Suggested MVP scoring:

- Delivery completed: +100.
- Time remaining bonus: +5 per second.
- No collision bonus: +150.
- Perfect route bonus: +100.
- Cat near-miss bonus: +25, only if it does not encourage risky unreadable play.

Star rating:

- 1 star: route completed.
- 2 stars: route completed under target time.
- 3 stars: route completed under target time with no crashes.

## Controls

Primary mobile controls:

- Bottom-left D-pad by default.
- Optional swipe steering.
- Pause icon in slim top HUD.

Control requirements:

- Controls must stay outside the main playfield where possible.
- Buttons must be large enough for thumbs.
- Movement input must buffer slightly before intersections.
- Accessibility setting should allow bottom or top control placement, matching the existing UX recommendation.

Recommended first implementation:

- D-pad first for reliable testing.
- Add swipe after movement tuning.

## Audio and SFX Direction

Audio should be light and tactile.

Music:

- Bright village theme.
- Acoustic guitar, brushed drums, ukulele, soft piano, or marimba.
- Tempo should support movement without creating stressful urgency.

SFX:

- Scooter start chirp.
- Gentle engine loop while moving.
- Turn tick or soft tyre squeak.
- Parcel delivery pop.
- Stamp reward sound.
- Cat meow when crossing or startled.
- Water splash.
- Timer warning chime.
- Level complete fanfare.

Haptics:

- Light tap on delivery.
- Soft bump on collision.
- Short success pulse on three-star result.

## UI and UX Flow

### Main Flow

```text
Title Screen
  -> Play
      -> Level Select
          -> Route Preview
              -> Game
                  -> Results
                      -> Next Level / Retry / Level Select
  -> Options
  -> How To Play
```

### Title Screen

- Large Chip + scooter key art or animated idle.
- Primary Play button.
- Secondary Options and Scores buttons.
- Keep it compact; do not make this a marketing landing page.

### Level Select

- Village map with route nodes.
- Locked/unlocked levels.
- Star count per level.
- Visual route path between nodes.

### In-Game HUD

Slim top bar:

- Timer.
- Current delivery count.
- Stars/progress indicator.
- Pause icon.

Game area:

- Board/map dominates screen.
- Destination pin.
- Optional next-turn arrow.

Bottom controls:

- Compact D-pad or split arrows.
- Use translucent backing only if controls overlap map.

### Results

Show:

- Stars earned.
- Time.
- Collisions.
- Parcels delivered.
- Best time.
- Buttons: Next, Retry, Map.

Keep results celebratory but fast. The player should be able to retry within one tap.

## Data Structures

The following structures are implementation guidance for Expo/React Native or a similar TypeScript codebase.

### Level Definition

```ts
type Vector2 = {
  x: number;
  y: number;
};

type LevelDefinition = {
  id: string;
  name: string;
  world: string;
  mapId: string;
  start: Vector2;
  startHeadingDegrees: number;
  timeLimitSeconds: number;
  playerSpeed: number;
  deliveries: DeliveryStop[];
  obstacles: ObstacleDefinition[];
  waterZones: CollisionZone[];
  roads: RoadSegment[];
  starTargets: StarTargets;
  tutorialSteps?: TutorialStep[];
};
```

### Road Segment

Road segments are the main movement model. They allow the game to look and feel fluid while still being easy to author.

```ts
type RoadSegment = {
  id: string;
  from: string;
  to: string;
  points: Vector2[];
  width: number;
  speedModifier?: number;
  tags?: Array<"road" | "bridge" | "path" | "junction" | "tutorial">;
};

type RoadNode = {
  id: string;
  position: Vector2;
  connectedSegmentIds: string[];
};
```

For a simple implementation, `points` can be `[start, end]`. For a more polished implementation, it can include curve control points or sampled points along a curved road.

### Delivery Stop

```ts
type DeliveryStop = {
  id: string;
  label: string;
  location: Vector2;
  triggerRadius: number;
  order: number;
  parcelType: "standard" | "fragile" | "express";
  bonusSeconds?: number;
};
```

### Obstacle

```ts
type ObstacleDefinition =
  | {
      id: string;
      type: "cat_sleeping";
      position: Vector2;
      radius: number;
      penalty: ObstaclePenalty;
    }
  | {
      id: string;
      type: "cat_crossing";
      path: Vector2[];
      radius: number;
      cycleSeconds: number;
      offsetSeconds?: number;
      penalty: ObstaclePenalty;
    }
  | {
      id: string;
      type: "puddle";
      position: Vector2;
      radius: number;
      slowSeconds: number;
    };
```

### Player State

```ts
type PlayerState = {
  position: Vector2;
  headingDegrees: number;
  velocity: Vector2;
  speed: number;
  currentSegmentId?: string;
  targetNodeId?: string;
  activeDeliveryIndex: number;
  deliveredStopIds: string[];
  collisions: number;
  isSlowedUntil?: number;
};
```

### Save Data

```ts
type SaveData = {
  unlockedLevelIds: string[];
  levelResults: Record<
    string,
    {
      bestTimeSeconds: number;
      bestStars: 0 | 1 | 2 | 3;
      bestCollisions: number;
    }
  >;
  settings: {
    soundEnabled: boolean;
    musicEnabled: boolean;
    hapticsEnabled: boolean;
    controlStyle: "dpad" | "swipe";
    controlPlacement: "bottom" | "top";
  };
};
```

## Implementation Phases

### Phase 1 - Playable Route Prototype

Goal: prove scooter routing and route completion.

Build:

- One static village map.
- Chip/scooter placeholder sprite.
- D-pad movement driving a world-position scooter.
- Road segment or waypoint-following movement with interpolated travel.
- Eased 90-degree junction turns instead of visible square stepping.
- Collision with roads/water.
- One delivery route.
- Timer and result screen.

Acceptance:

- Player can complete a route from start to destination.
- Water blocks movement or penalises clearly.
- Scooter movement is visually continuous, even if the underlying prototype map is coarse.
- Turns show heading rotation and light lean instead of instant direction flips.
- Retry loop takes under 3 seconds from results.

### Phase 2 - Obstacles and Level System

Goal: prove multi-level challenge.

Build:

- Level definition loader.
- 5-6 handcrafted levels.
- Sleeping cat and crossing cat behaviours.
- Puddle slow effect.
- Star scoring.
- Level select with unlocks.
- Local save data.

Acceptance:

- Each level can be completed and replayed.
- Cats are visible, readable, and never feel like random unavoidable failure.
- Star ratings save locally.

### Phase 3 - Visual Upgrade

Goal: make the game match the Version 2 art direction.

Build:

- Final Chip/scooter sprite set.
- Scooter animation set: idle, moving, turn/lean, skid, delivery celebration.
- Warm village tile/prop set.
- Rounded/curved road rendering or blended road tiles that hide square map construction.
- Route markers and delivery effects.
- Title screen key art or animated idle.
- Results screen polish.
- Basic animation pass.

Acceptance:

- The first screen immediately communicates Chip, scooter, parcels, and village.
- Gameplay remains readable on small phone screens.
- Art does not obscure roads, cats, water, or destination markers.

### Phase 4 - Juice, Audio, and Tuning

Goal: make the game feel polished enough for external testing.

Build:

- Music loop.
- SFX pass.
- Haptics.
- Scooter acceleration/turn tuning.
- Timer and star threshold tuning.
- Tutorial prompts.
- Device testing on small and large phones.

Acceptance:

- First-time player can understand Level 1 without external explanation.
- 3-star completion feels achievable but skillful.
- No UI overlap on small mobile screens.

## Technical Risks

- **Readability risk:** rich art may obscure gameplay. Mitigation: enforce contrast rules and test on small screens early.
- **Movement feel risk:** scooter physics can become slippery or too grid-like. Mitigation: use road segments/waypoints, input buffering, centreline assist, eased turns, and forgiving collision radii.
- **Authoring complexity:** curved roads and world-space obstacles are harder to author than simple tiles. Mitigation: allow coarse grid authoring, then convert to road nodes, collision zones, and rendered curved paths.
- **Collision frustration:** cats and water could feel unfair. Mitigation: forgiving hitboxes, warning animation, predictable cat paths.
- **Scope creep:** polished character animation can consume time. Mitigation: MVP requires only directional movement, delivery, bump, and idle.
- **Performance:** large bitmap maps may cause memory pressure on low-end phones. Mitigation: tile atlases, compressed assets, capped animation frames.
- **Aspect ratios:** map and controls may collide on short screens. Mitigation: board-first layout, safe-area testing, scalable camera.

## Asset List

### Required for MVP

- Chip scooter sprite placeholder, 4 directions.
- Placeholder turn/lean frame or rotation-friendly scooter sprite.
- Road/path tiles.
- Road node/segment metadata for smooth movement.
- Grass tile.
- Water tile/zone.
- House/delivery stop marker.
- Post office/start marker.
- Sleeping cat sprite.
- Crossing cat sprite/animation.
- Puddle sprite.
- Route line and destination pin.
- Parcel icon.
- HUD icons: timer, pause, parcel, star.
- Level select node icons.
- Delivery pop effect.

### Required for Polished Version 2

- Chip scooter final sprite, 4 or 8 directions.
- Turn/lean frames.
- Idle and celebration frames.
- Cat animations: sleep, walk, hop-away.
- Village house variants.
- Red post box.
- Blue parcel box.
- Bridges.
- Fences, hedges, flowers, trees.
- Water edge tiles.
- Road signs and cones.
- Title key art or hero composition.
- Results stars and stamp badge.
- UI button set in navy/gold/cream palette.

### Audio Assets

- Main music loop.
- Scooter engine loop.
- Scooter start.
- Delivery pop.
- Stamp reward.
- Cat meow.
- Water splash.
- Collision/skid.
- Timer warning.
- Level complete.

## Acceptance Criteria

Version 2 concept is build-ready when:

- A player can start the app, select a level, preview the route, play, finish, and see results.
- At least 5 handcrafted levels exist with different route layouts.
- Water and black-and-white cats are implemented as clear, readable obstacles.
- The scooter character is visually recognisable as Chip from gameplay distance.
- Scooter motion feels fluid and road-driven rather than grid-square driven.
- Turns, braking, collisions, and deliveries have visible animation feedback.
- The visual direction matches the warm, polished, character-led promo-art style.
- UI uses a slim HUD and keeps the map as the primary screen content.
- Controls work on mobile without blocking critical gameplay.
- Level results and star ratings persist locally.
- Audio and haptics can be toggled in settings.
- The first level teaches movement, delivery, and hazards without a written manual.

## Recommended Next Step for ChipCode

Build Phase 1 as a vertical slice in the source repo:

1. Create a single `LevelDefinition` for Post Office Lane.
2. Implement D-pad scooter movement on road segments/waypoints with world-space interpolation.
3. Add water collision and one delivery stop.
4. Add route preview, timer, and results screen.
5. Add minimum scooter animation feedback: idle, moving, turn/lean, bump, and delivery pop.
6. Use placeholder art sized to match the future final sprites.

Once movement and readability feel good, expand to cats and level progression before commissioning or generating the final asset set.
