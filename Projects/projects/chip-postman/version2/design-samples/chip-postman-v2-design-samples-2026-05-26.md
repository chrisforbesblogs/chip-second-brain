# Chip Postman Version 2 - Design Samples for Approval

Date: 2026-05-26  
Project: Chip Postman / Parcel Post  
Audience: Vance approval, then ChipCode implementation  
Related concept: `../chip-postman-version-2-concept-2026-05-26.md`  
Visual sample board: `chip-postman-v2-design-samples.html`

## Reference Notes

Chris provided this inspiration link: `https://share.google/1Yvv7OlM9tvVqE03g`.

I attempted to resolve it during this revision, but the browser tool could not safely open the redirected Google share URL. The design pack therefore applies the requested direction directly rather than citing specific details from the referenced app.

Chris's latest Telegram screenshot reference is treated as the active visual brief: a Cartoon City / farm-to-village style with a bright isometric/top-down 2.5D cartoon map, clear dark roads in a grid/curved network, green village/farm blocks, buildings beside roads, compact water features, coin/marker-style points of interest, and a larger scrolling world.

## Approval Goal

Approve the visual and implementation direction for Version 2 before ChipCode builds the next playable slice.

This design pack covers:

- Two mobile-suitable map layout/style options.
- Sprite concepts for Chip, parcels, houses/shops, obstacles, markers, route elements, and vehicles.
- React Native implementation notes.
- Asset pipeline, naming, dimensions, sprite states, and animation states.

## Direction Summary

Version 2 should be designed from the start as a **fluid animated top-down/isometric cartoon tile game** with a larger scrolling world. The revised target visual direction is closer to Cartoon City / farm-to-village maps: bright, more 3D-looking, premium, and readable, with dark road lanes, green village/farm blocks, raised buildings, dimensional trees, compact bridges, coin-style points of interest, and narrow water features running through the village.

- Chip in a blue postman outfit on a small yellow scooter.
- Sunny village roads with cottages, post boxes, parcel stops, small bridges, gardens, farm/village blocks, and small shops.
- Route clarity through yellow route lines, numbered delivery pins, and readable road/path contrast.
- Obstacles that are charming but legible: narrow water features, puddles, and little black-and-white cats first.
- Smooth movement, route pulses, water shimmer, cat animation, parcel pickup/dropoff effects, and delivery success feedback should be present in the first approval-quality slice.
- The map is larger than the phone viewport and scrolls/pans as Chip approaches screen edges.
- Houses and shops sit beside roads on clear land plots; roads remain open and readable for route planning.
- Points of interest can use coin/medallion-style markers, but markers must not hide roads or obstacles.

The map should never read like houses sitting in water. Water is a supporting village feature: slim streams, canals, ponds, puddles, and bridge crossings. The dominant read must be village blocks, paths, roads, lawns, hedges, shops, and homes.

## Primary Map Direction - Animated Cartoon Tile Village

**Primary recommendation for the next build.**

Use a tile-based top-down/isometric map with cartoon rendering and smooth animation from day one. The grid remains the gameplay foundation for predictable mobile controls, collisions, level authoring, and route logic, but the player sees a fluid modern 2.5D village: dark readable road lanes, raised road edges, clear road-adjacent building plots, farm-green blocks, small canals/streams, animated water accents, pulsing route lines, scooter lean, cat movement, delivery effects, and lively but restrained environmental details.

### Why approve this

- Best balance of rich visuals and realistic React Native implementation.
- Works with the existing board/tile logic in `App.tsx`.
- Easy to author levels as arrays or JSON.
- Predictable collisions for water, roads, cats, houses, and puddles.
- Strong readability on small phones.
- Supports smooth visual upgrades without abandoning tile-based level data.
- Avoids the visual problem of oversized water fields by constraining water to narrow tile features and marked crossings.
- Enables multi-screen route design without shrinking the map to fit the phone.

### Visual Style

- Top-down cartoon map with a stronger 2.5D/isometric flavour.
- Clean bright grass, farm-green blocks, dark charcoal roads, pale paving, small blue streams/canals, navy UI, yellow route.
- Cottages and shops placed beside roads on clear grass/pavement plots, never on roads and never directly in water.
- Raised building bases, soft cast shadows, subtle roof highlights, dimensional bridges, full tree canopies, coin/medallion markers, and scooter/character depth.
- Rounded or curved road corners, dark lane surfaces, clipped grass verges, tidy hedges, tree clusters, and controlled soft shadows.
- Route preview appears as a thick yellow Skia path over road/path tiles.
- Animated layer details: route glow pulse, water shimmer, scooter dust, cat crossing, parcel pop, delivery sparkle.

### Composition Rules

- At least 70% of the visible map should read as village land: roads, paths, grass, homes, shops, gardens, and plaza space.
- Water should usually occupy narrow channels of 1 tile width, or small ponds no larger than 2x2 tiles.
- Every water crossing should have an explicit bridge, stepping path, or blocked-edge treatment.
- Buildings must sit on land plots with a 1-tile visual buffer from water unless intentionally placed beside a canal.
- Houses and shops must be adjacent to roads, not placed on road tiles. Use a doorstep/driveway tile to connect the road to the building.
- Roads must remain visually clear enough for route planning: do not cover lanes with building bases, tree crowns, oversized markers, or decorative props.
- Dark roads should be the primary navigation read. Use lighter edge strips or kerbs only as accents, not as the road body.
- Coin/marker points of interest should sit on verges, building plots, or destination nodes beside roads. They should never sit in the middle of a driving lane unless deliberately used as a route checkpoint.
- Use controlled shadows under buildings, trees, Chip, cats, markers, and bridge rails; avoid heavy drop shadows that muddy the map.
- Keep route color separate from water color: route = warm yellow/gold, water = clean blue/cyan.

## Scrolling World and Camera

The playable world should be larger than the phone viewport. The player should feel like Chip is riding through a real village rather than around a single board.

### World Size

Recommended first scrolling level:

- World grid: `24 x 32` tiles.
- Tile visual size: `96px` source art, rendered around `48-72dp` depending on device.
- Viewport: phone-sized crop of the world, usually showing around `8-11` tiles across and `11-15` tiles tall after HUD/controls.
- Chunk size: `8 x 8` tiles for culling, authoring, and future streaming.

Later levels can grow to `32 x 48` tiles if performance remains stable.

### Camera Behaviour

Use a soft edge-following camera:

- Keep Chip near the centre while riding through the middle of the map.
- Define a camera dead zone around the centre, about 35-45% of viewport width and height.
- When Chip moves outside that dead zone, pan the camera smoothly toward Chip.
- Clamp camera position at world boundaries so the viewport never shows outside the map.
- Use easing/lerp for camera motion, not instant snapping.
- During route preview, pan along the route or zoom out slightly if technically practical; return to Chip before the countdown starts.

Suggested logic:

```ts
type CameraState = {
  x: number;
  y: number;
  viewportWidth: number;
  viewportHeight: number;
  worldWidth: number;
  worldHeight: number;
};

const CAMERA_DEAD_ZONE = { x: 0.38, y: 0.38 };
const CAMERA_LERP = 0.16;
```

### Tile Chunks and Culling

Use chunks to keep rendering practical:

- Store the level as tile layers and entity lists.
- Split static tiles into `8 x 8` chunks.
- Each frame, compute visible chunk bounds from camera position plus one chunk of padding.
- Draw only visible chunks, visible sprites, visible route segments, and visible effects.
- Keep collision checks independent from rendering culling so gameplay remains deterministic.

### Edge-Following Movement

Movement remains tile/waypoint based, but the camera follows smoothly:

- Chip moves continuously between tile centres or route waypoints.
- Direction input can buffer before intersections.
- Camera pans when Chip approaches the viewport edge/dead-zone boundary.
- Route arrows and destination markers should be positioned in world space and transformed by camera offset.
- Optional off-screen destination indicator can sit on the viewport edge if the next stop is outside view.

### Implementation Fit

Use Expo + TypeScript + React Native Skia as the main graphics layer:

- Skia `Canvas` for map tiles, route lines, water overlays, shadows, particles, and animated effects.
- TypeScript level definitions for tile types, route paths, obstacle paths, delivery stops, and animation triggers.
- React Native `Image` or Skia image drawing for sprite sheets.
- Standard React Native views for HUD, menus, settings, and level select.
- Keep gameplay hitboxes in TypeScript, separate from visual bounds.

Use Rive/Lottie selectively:

- Rive only if Chip/cat animation needs rigged vector state machines.
- Lottie only for UI-grade reward effects such as stamp bursts or level-complete confetti.
- Do not make Rive/Lottie mandatory for core movement; sprite sheets plus Skia timing are enough for the first version.

### Main Tradeoff

Skia introduces one real dependency up front, but it aligns the implementation with the approved Version 2 visual direction immediately.

## Secondary Layout Sample - Clean Canal Village Variant

**Alternative layout style using the same tile-based foundation.**

This is not a separate road-graph build. It is a more premium tile-map presentation where tiles contain curved road art, clean canal/stream pieces, bridge tiles, clipped hedges, and decorative masks. Chip still moves through tile/waypoint centres, but Skia draws the route as a smooth path over the tile grid.

### Why approve this

- Looks closer to the generated promo artwork.
- Roads and paths feel more natural and less blocky.
- Route planning is visually obvious.
- Still uses practical tile data, collision zones, and predictable mobile controls.
- Water supports level design without dominating the map.

### Visual Style

- Curved road/path art inside a tile map.
- Yellow route line follows a Skia path through tile centres.
- Delivery stops use large numbered pins.
- Cats cross short tile paths.
- Water appears as narrow streams, small canals, puddles, and compact ponds with bridges.

### Implementation Fit

Use tile data with optional route control points:

```ts
type TilePoint = { row: number; col: number };
type RouteSegment = {
  from: TilePoint;
  to: TilePoint;
  curve?: { x: number; y: number };
};
```

Skia responsibilities:

- Draw roads as atlas tiles plus curved route overlays.
- Draw route previews as animated yellow paths.
- Draw small water shimmer loops, bridge masks, and canal-edge highlights.
- Draw entity shadows and transient effects.

### Main Tradeoff

This needs more tile art than the stricter grid sample, but it keeps engineering scope under control because movement and collisions stay tile-based.

## Recommendation

Approve the **animated top-down cartoon tile map** as the primary direction.

Build path:

1. Add React Native Skia to the Expo app.
2. Render the map with a Skia canvas from tile data.
3. Use transparent sprite sheets for Chip, cats, parcels, vehicles, and markers.
4. Animate scooter riding, route pulse, water/puddles, parcel pickup/dropoff, and delivery success in the first slice.
5. Keep Rive/Lottie optional and focused on specific high-value animation assets.

## Sprite Concept Set

The sample board uses simple SVG forms to show shape language, tile readability, and animation targets. Production assets should keep the same clean silhouettes, modern rounded forms, soft shadows, and land-first composition. Export gameplay art as Skia-friendly PNG/WebP sprite sheets, with Rive/Lottie only for selected effects where they clearly reduce implementation effort.

### Chip / Postman Scooter

Core identity:

- Blue cap and shirt.
- Warm face and brown hair visible from gameplay scale.
- Yellow scooter body.
- Front headlamp.
- Rear parcel crate.
- Slight lean on turns.

Gameplay silhouette:

- Width: roughly 1 road lane.
- Height: 1 road lane plus small parcel crate.
- Strong blue/yellow color split so Chip remains readable on grass and roads.

Required states:

- `idle_south`
- `idle_east`
- `idle_north`
- `idle_west`
- `drive_north`
- `drive_east`
- `drive_south`
- `drive_west`
- `ride_loop_north`
- `ride_loop_east`
- `ride_loop_south`
- `ride_loop_west`
- `turn_left`
- `turn_right`
- `bump`
- `splash`
- `parcel_pickup`
- `parcel_dropoff`
- `deliver`

### Parcels

Types:

- Standard brown parcel.
- Express parcel with blue label.
- Fragile parcel with red tape/label.
- Stack of parcels for scooter crate and pickup point.

Required states:

- `idle`
- `pickup_pop`
- `dropoff_pop`
- `delivered_pop`
- `fragile_wobble`
- `crate_stack_idle`
- `crate_stack_bounce`

### Houses and Shops

Core buildings:

- Cottage with warm orange roof.
- Blue-roof house.
- Bakery/shop with awning.
- Post office with mail sign.

Implementation note:

- Treat houses as non-collidable decorative sprites unless they are also delivery stops.
- Place buildings on explicit land-plot tiles such as `plot_grass`, `plot_paving`, or `plaza`.
- Place buildings beside roads, not on road tiles. Doorstep, driveway, or path connector tiles should bridge the building to the road.
- Delivery hitboxes should be attached to a marker or doorstep zone, not the full building image.
- Use a consistent soft oval/base shadow under buildings so they feel anchored to land.
- Use raised walls, roof faces, subtle side shading, and cast shadows for a 2.5D feel while keeping collision top-down.
- Do not place building sprites over water, canal, stream, or pond tiles.

### Obstacles

First obstacles:

- Deep water: blocks route.
- Puddle: slows scooter.
- Sleeping black-and-white cat: static blocker.
- Crossing black-and-white cat: moving hazard on short loop.

Cat rules:

- Cute, clear, outlined.
- Collision causes Chip to brake/skid and lose time.
- The cat hops away safely; never show harm.

Required cat states:

- `sleep`
- `walk_1`
- `walk_2`
- `hop_away`
- `meow`

### Delivery Markers and Route Elements

Required:

- Numbered destination pin.
- Active route line.
- Next-turn arrow.
- Completed stop check.
- Post office start marker.
- Bridge crossing marker where water is nearby.

Use yellow for active route and red/pink for destination pin so route and target are distinct.

Required states:

- `route_preview`
- `route_pulse_active`
- `route_completed`
- `route_blocked`
- `marker_idle`
- `marker_active_pulse`
- `marker_success_check`
- `next_turn_arrow_pulse`

### Vehicles / Route Props

Core:

- Chip's scooter only.

Additional route entities:

- Parked van as road blocker.
- Bicycle crossing.
- Market cart.
- Roadworks cones.

These should be authored as obstacles with predictable positions or paths, not as background decoration only.

Required states:

- `vehicle_idle`
- `vehicle_crossing_1`
- `vehicle_crossing_2`
- `vehicle_brake`
- `cone_idle`
- `cart_idle`
- `cart_wobble`

### Water and Puddles

Water should feel alive from the first design slice, but it must stay visually secondary to the village.

Tile guidance:

- `stream_straight_horizontal`
- `stream_straight_vertical`
- `stream_corner_ne`
- `stream_corner_nw`
- `canal_edge_north`
- `canal_edge_south`
- `bridge_road_horizontal`
- `bridge_path_vertical`
- `pond_small_1x1`
- `pond_small_2x2_corner`
- `puddle_small`
- `puddle_splash`

Rules:

- Use streams/canals as 1-tile-wide channels.
- Use compact ponds only as obstacles or decoration, not as map backgrounds.
- Add land edging, reeds, stones, or railings to make water boundaries clear.
- Bridges must visually sit on top of water and connect land-to-land paths.

Required states:

- `water_idle_shimmer`
- `water_edge_loop`
- `puddle_idle`
- `puddle_splash_1`
- `puddle_splash_2`
- `puddle_recover`

## React Native Implementation Notes

The current app uses Expo + React Native + TypeScript. Dependencies currently include Expo, React Native, Expo Asset, and Expo Audio. The Version 2 graphics slice should add React Native Skia and treat it as the main gameplay rendering layer.

### Main Rendering Approach

Use Expo + TypeScript + React Native Skia:

- Skia `Canvas` for the map, route lines, water, puddle effects, shadows, particles, and sprite sheet rendering.
- TypeScript map data for tile IDs, walkability, delivery stops, obstacle paths, and route segments.
- Camera transform applied to all world-space Skia draw calls: `screen = world - camera`.
- Chunk culling for static tile layers and decorative props.
- A deterministic animation clock for route pulse, water shimmer, scooter frame selection, cat movement, and delivery effects.
- HUD as standard React Native `View`, `Text`, `Pressable`.
- Local level data in TypeScript files.

This keeps the gameplay realistic to build while matching the approved smooth cartoon visual direction immediately.

### React Native Skia Responsibilities

- Draw tile atlas layers: grass, roads, water, bridges, houses/shops, decorations.
- Draw animated route pulse using stroked paths and alpha/width modulation.
- Draw scooter/cat/parcel sprite frames from image atlases.
- Draw shadows under moving entities.
- Draw small water shimmer loops and puddle splash effects.
- Draw delivery success particles and parcel pop effects.
- Draw 2.5D depth cues: raised building bases, roof highlights, soft ground contact shadows, bridge shadows, and tree canopy overlaps.

Keep React Native UI outside Skia for accessibility and layout reliability.

### Tile Layering Order

Render the map in this order:

1. Base land: grass, plaza, paving.
2. Small water: streams, canals, ponds, puddles.
3. Roads and paths so driving lanes remain visually clear.
4. Bridges and crossing edges above water and roads.
5. Building ground shadows and raised bases.
6. Buildings and shopfronts on land plots beside roads.
7. Static props: hedges, trees, post boxes, signs, garden details.
8. Route overlay and destination markers.
9. Moving entities: Chip, cats, vehicles, parcel effects.
10. Foreground effects: dust, splash, delivery sparkle, tree canopy overlaps where needed.

This order prevents buildings appearing submerged and keeps the map village-first.

### When to Use Rive

Use Rive for:

- Chip scooter animation only if final art needs rigged vector-style lean, bounce, and expressive reactions.
- Cat walk/hop animation only if sprite sheets feel too stiff.
- Title screen animated mascot.

Rive is useful for state machines such as `idle`, `ride`, `turn`, `bump`, `splash`, and `deliver`, but it should not be required to render the map or basic gameplay.

### When to Use Lottie

Use Lottie for:

- Delivery celebration pop.
- Stamp reward.
- Level complete confetti.
- Small UI transitions.

Avoid Lottie for the playable scooter or cats if collision timing depends on exact frame positioning.

## Asset Format Pipeline

### Recommended Pipeline

1. Concept approval from this sample board.
2. Produce final art in layered source files: Figma, PSD, Procreate, or Illustrator.
3. Export gameplay sprites as transparent PNG or WebP sprite sheets.
4. Export UI icons as SVG where static, or PNG when painterly.
5. Export animation primarily as sprite sheets; use Rive for selected character rigs and Lottie for selected UI celebration effects.
6. Place source files in second-brain project structure design assets and runtime exports in the app repo.

### Runtime Asset Formats

- Gameplay sprites: transparent PNG sprite sheets first; WebP sprite sheets if size becomes a problem.
- Tile/background pieces: PNG atlas preferred; individual PNGs acceptable while authoring.
- Static UI icons: SVG if supported by app stack, otherwise PNG.
- Route lines: Skia paths, not baked into map art.
- Rive: `.riv` for selected Chip/cat animation if approved.
- Lottie: `.json` for celebration UI effects only.

## Naming Convention

Use lowercase kebab case for files.

Suggested root:

```text
assets/
  sprites/
    chip/
    cats/
    parcels/
    buildings/
    obstacles/
    markers/
  maps/
    village-01/
  ui/
  audio/
```

Examples:

```text
chip-scooter-drive-east-01.png
chip-scooter-drive-east-02.png
chip-scooter-ride-loop-east.png
chip-scooter-bump-south-01.png
chip-scooter-parcel-pickup-01.png
chip-scooter-parcel-dropoff-01.png
cat-black-white-crossing-walk-01.png
cat-black-white-hop-away-01.png
parcel-standard-idle.png
parcel-fragile-wobble-01.png
building-post-office-village-01.png
marker-delivery-active-01.png
marker-coin-delivery-active-01.png
marker-coin-poi-post-office-01.png
route-arrow-right.png
route-pulse-yellow.png
tile-road-dark-straight-horizontal.png
tile-road-dark-corner-ne.png
tile-road-dark-curve-ne.png
tile-path-rounded-crossing.png
tile-water-edge-north.png
tile-water-shimmer-01.png
tile-stream-straight-horizontal.png
tile-stream-corner-ne.png
tile-canal-edge-south.png
tile-bridge-road-horizontal.png
tile-plot-grass-clean.png
tile-plot-driveway-connector.png
tile-road-adjacent-doorstep.png
tile-hedge-rounded-corner.png
tile-building-shadow-soft.png
tile-tree-canopy-shadow.png
tile-farm-block-green-01.png
tile-field-row-light-01.png
puddle-splash-01.png
vehicle-parked-van-idle.png
```

## Dimensions

Base target assumes a mobile game board with tiles/lanes around 48-72 display pixels depending on screen.

### Recommended Source Dimensions

- Tile source: `128x128`.
- Dark road/path tile: `128x128`, with optional kerb/edge highlights baked into the tile or drawn as a Skia overlay.
- Stream/canal/water tile: `128x128`.
- Bridge tile: `128x128` or `256x128` for longer bridge spans.
- Building source: `256x320` or `384x384` with transparent top/side depth and separate hitbox metadata.
- Tree source: `192x224` with canopy extending above its base tile.
- Chip scooter gameplay frame: `160x160`, with content inside a consistent 128px gameplay area.
- Cat frame: `96x96`.
- Parcel frame: `64x64`.
- Delivery/POI coin marker: `96x128`, with the coin/medallion top fitting inside the upper 72px.
- House/shop: `256x256` or `256x320`.
- Post office: `320x320`.
- UI icon: `64x64` source.
- Title Chip key art: `1024x1024` or larger.

### Runtime Scaling

- Render tile art to the computed tile size.
- Keep hitboxes separate from image bounds.
- Chip hitbox should be smaller than sprite bounds for forgiveness.
- Cat hitbox should be smaller than its visible body.
- Delivery marker touch/completion radius should be generous.
- Buildings may visually overlap above their base tile, but their collision/doorstep zone must stay tied to explicit land tiles beside roads.
- Route planning should use road/path tile centres, not building sprite bounds.

## Sprite Sheet Guidance

If using sprite sheets instead of separate PNG frames:

```text
chip-scooter.png
frame: 160x160
columns: 6
rows: 6
states:
  row 0: idle south/east/north/west + two blink/bounce frames
  row 1: ride south 6 frames
  row 2: ride east 6 frames
  row 3: ride north 6 frames
  row 4: ride west 6 frames
  row 5: turn-left, turn-right, bump, splash, parcel-pickup, parcel-dropoff
```

Cats:

```text
cat-black-white.png
frame: 96x96
columns: 4
rows: 2
states:
  row 0: sleep, sleep-blink, wake, meow
  row 1: walk-1, walk-2, hop-away-1, hop-away-2
```

Parcels:

```text
parcels.png
frame: 64x64
columns: 4
rows: 2
states:
  row 0: standard, express, fragile, stack
  row 1: pickup-pop-1, pickup-pop-2, dropoff-pop-1, fragile-wobble
```

Water/puddles:

```text
water-effects.png
frame: 128x128
columns: 4
rows: 2
states:
  row 0: water-shimmer-1, water-shimmer-2, water-shimmer-3, water-shimmer-4
  row 1: puddle-idle, splash-1, splash-2, recover
```

Vehicles/route props:

```text
route-obstacles.png
frame: 160x160
columns: 4
rows: 2
states:
  row 0: parked-van-idle, bicycle-crossing-1, bicycle-crossing-2, bicycle-brake
  row 1: market-cart-idle, market-cart-wobble, cone-idle, roadworks-sign
```

## Level and Asset Integration

Each level should reference art by asset key, not file path scattered through game logic.

```ts
type SpriteKey =
  | "chip_scooter"
  | "cat_black_white"
  | "parcel_standard"
  | "building_post_office"
  | "marker_delivery_active";

type LevelArtConfig = {
  tileSet: "village_isometric_01";
  background: "grass_farm_village";
  roadStyle: "dark_cartoon_curved";
  waterStyle: "bright_stream";
  routeStyle: "yellow_coin_route";
  markerStyle: "coin_poi";
  renderer: "skia";
};
```

World and camera data should be explicit:

```ts
type LevelWorld = {
  id: string;
  widthTiles: number;
  heightTiles: number;
  chunkSize: 8;
  tileSize: number;
  layers: {
    base: TileId[][];
    roads: TileId[][];
    water: TileId[][];
    props: PropInstance[];
    buildings: BuildingInstance[];
  };
  routes: RouteDefinition[];
  camera: {
    mode: "edge_follow";
    deadZoneX: number;
    deadZoneY: number;
    lerp: number;
  };
};

type BuildingInstance = {
  id: string;
  spriteKey: string;
  baseTile: TilePoint;
  footprint: { width: number; height: number };
  doorstepTile: TilePoint;
  adjacentRoadTile: TilePoint;
};
```

## Approval Choices

Approve one of these:

1. **Recommended:** Animated top-down cartoon tile map using Skia from day one.
2. **Recommended camera model:** Larger scrolling tile world with edge-following camera and visible chunk culling.
3. **Curvier variant:** Same Skia tile system, but with more organic road-tile art and curved route overlays.
4. **Not recommended:** Static single-screen React Native tile UI with only sprite swaps, because it does not match the approved Version 2 visual ambition.

## Acceptance Criteria for the Next Design Pass

- Approved animated top-down tile map direction.
- Approved larger-than-viewport scrolling world direction.
- Approved edge-following camera behaviour.
- Approved 2.5D top-down cartoon depth style.
- Approved Chip/scooter identity.
- Approved cat style and collision treatment.
- Approved route marker style.
- Approved Skia-first rendering approach.
- Approved rule that houses sit beside roads and roads stay visually clear.
- Confirm which character animations, if any, justify Rive.
- Confirm which reward/UI effects, if any, justify Lottie.

## Recommendation

Approve the **Skia-rendered animated 2.5D top-down cartoon tile map with a larger scrolling world**.

ChipCode should implement the next slice with tile-based movement, a Skia map canvas, a larger-than-viewport world, edge-following camera, visible chunk culling, road-adjacent buildings, animated route overlays, water/puddle animation, scooter riding frames, cat obstacle animation, parcel pickup/dropoff effects, delivery success feedback, and data-driven levels. Rive and Lottie should remain targeted tools for selected character or reward animations, not the core rendering foundation.
