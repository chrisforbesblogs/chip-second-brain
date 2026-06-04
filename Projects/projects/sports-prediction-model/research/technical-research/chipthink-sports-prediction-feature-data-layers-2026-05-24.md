# Feature Data Layers For A Scalable League-Sports Prediction Platform

Date: 2026-05-24  
Prepared by: ChipThink  
Scope: football/soccer-first platform, extensible to other league sports. Focus: the three feature groups above the base team-strength/results model:

1. xG / chance-quality features
2. player, lineup, injury, and suspension features
3. contextual features: rest, travel, weather, venue, fixture congestion, derbies, manager changes, transfers, motivation, relegation/title pressure

## Executive Summary

The feature strategy should be tiered, not all-or-nothing. For global football coverage, especially across Asia and Europe, the platform cannot assume every league has xG, confirmed lineups, reliable injury reports, or clean player IDs. The right approach is to define a canonical feature schema, attach provenance and confidence to every feature, and let models degrade gracefully from rich event/player context down to team-strength and fixture-context features.

Recommended MVP:

- Build three feature tiers:
  - Tier 1: available for nearly every league: fixtures, results, standings, rest days, travel proxy, venue, home/away, fixture congestion, table pressure.
  - Tier 2: available for medium/high coverage leagues: match stats, lineups, suspensions, injuries, player minutes, squad continuity, recent selection patterns.
  - Tier 3: available only for rich leagues: xG, npxG, xG against, shot quality, xA, post-shot xG, player-level xG/xA, expected lineups, tactical/formation data.
- Treat xG and injury feeds as high-value but fragile. Vendor definitions, coverage, and licensing differ materially.
- Use provider abstraction from day one. Do not let Sportmonks/API-Football/StatsBomb/Opta-style IDs leak into the canonical model.
- Store raw payloads, canonical normalized records, feature snapshots, and model-time feature vectors separately.
- Every feature should carry `source_provider`, `observed_at`, `effective_for_fixture_id`, `confidence`, and `is_missing_reason`.

Strongest recommendation: for the MVP, license one broad football API with lineups/injuries/stats/xG where possible, pair it with a dedicated odds feed and Open-Meteo for weather, then supplement sparse leagues with derived context features from fixture/results/table data. Avoid scraping Transfermarkt, Sofascore, FotMob, Flashscore, or club/social pages as core production dependencies unless legal review explicitly approves it.

## Why These Feature Layers Matter

Base team-strength models can perform surprisingly well, especially Dixon-Coles/Poisson/Elo-style models. The extra layers should be added only where they provide measurable out-of-sample improvement under log loss, Brier score, ranked probability score, calibration, and closing-line comparison.

Likely value by feature group:

- xG/chance quality: highest medium-term value for team-strength estimates, especially early-season and finishing-luck correction.
- lineup/player availability: high value close to kickoff and for teams with concentrated player quality.
- context: broadest coverage and most scalable, but individual features are often weak unless carefully encoded and validated.

## Feature Group 1: xG And Chance Quality

### Important Data

MVP fields:

- Fixture-level home xG and away xG
- Non-penalty xG, if available
- xG against by team
- Shot count and shots on target
- Big chances or high-quality chance count, if available
- Set-piece xG and penalty xG, if available
- Rolling xG for and against over last 5, 10, and season-to-date matches
- xG difference and xG ratio
- Shot quality: xG per shot
- Data availability flag and provider definition

Later fields:

- Shot-level xG
- Shot location, body part, situation, assist type
- Post-shot xG / xGOT
- xA and key passes
- Field tilt, possession value, xT, pressure, PPDA
- Player-level xG/xA per 90
- Goalkeeper post-shot xG prevented
- xG by game state: level, leading, trailing
- xG by phase: open play, set piece, transition

### Sources

Primary paid/broad options:

- Sportmonks: offers xG endpoints/add-ons and links lineups to xG in documentation. Useful broad API layer with predictions, fixtures, lineups, injuries, and odds add-ons. Sources: [Sportmonks xG endpoint docs](https://docs.sportmonks.com/football/endpoints-and-entities/endpoints/expected-xg/get-expected-by-team), [Sportmonks lineups/formations docs](https://docs.sportmonks.com/football/tutorials-and-guides/tutorials/lineups-and-formations), [Sportmonks pricing](https://www.sportmonks.com/football-api/plans-pricing/).
- TheStatsAPI: claims xG, npxG, xA, match stats, player stats, odds, and historical data across default and requested competitions. Source: [TheStatsAPI](https://www.thestatsapi.com/).
- Stats Perform / Opta, StatsBomb, Wyscout: enterprise-grade event data. Best for serious xG, but likely expensive and sales-led.
- SportsDataIO: broad sports API with soccer coverage and enterprise positioning; use as a candidate for broader multi-sport infrastructure. Source: [SportsDataIO](https://sportsdata.io/).

Free / prototype options:

- StatsBomb Open Data: excellent for prototyping event/xG pipelines, but limited competition coverage and explicit attribution/licence obligations. Source: [StatsBomb Open Data](https://github.com/statsbomb/open-data).
- socceraction/soccerdata Python ecosystems: useful for research loaders around StatsBomb, Wyscout, Opta-derived formats, FBref/Understat-style sources. Sources: [socceraction docs](https://socceraction.readthedocs.io/_/downloads/en/latest/pdf/), [soccerdata docs](https://soccerdata.readthedocs.io/_/downloads/en/stable/pdf/).

Avoid as core production dependencies without legal review:

- Unofficial scraping of Understat, FBref, Sofascore, FotMob, Flashscore, Transfermarkt, or fan-maintained datasets. These can be useful for private research but are brittle and may breach terms.

### Cadence

- Fixture-level final xG: usually after full time; some providers settle within 1-2 hours.
- Live xG: only available from richer providers and selected leagues.
- Rolling xG aggregates: recompute after each match finalization.
- Shot-level xG: ingest as soon as event data is finalized, then lock once provider marks match verified.

### Reliability And Legal Concerns

- xG is model-based. Providers can assign different xG to the same shot.
- xG definitions can change without obvious historical restatement.
- Event coverage is often strongest in major European competitions and weakest in long-tail Asian/lower-tier leagues.
- Derived metrics may be restricted by vendor terms. Confirm whether predictions based on xG can be redistributed commercially.
- If using open data, obey attribution and non-commercial limitations.

### Graceful Degradation

If no xG:

- Use shots, shots on target, corners, possession, dangerous attacks if available.
- Use score-based team-strength model with stronger shrinkage.
- Encode `chance_quality_tier = none/basic_stats/xg/event`.
- Avoid imputing fake xG as if it were observed. If proxy xG is used, label it `proxy_xg`.

## Feature Group 2: Player, Lineup, Injury, Suspension

### Important Data

MVP fields:

- Confirmed starting XI
- Substitutes
- Formation
- Player position/role
- Player minutes played
- Suspensions
- Injuries / unavailable players
- Doubtful/questionable status
- Expected return date, if available
- Player importance proxy:
  - minutes share this season
  - starts share
  - goals/assists/xG/xA contribution where available
  - team Elo/xG contribution proxy if no player model exists
- Team availability score:
  - total missing minutes share
  - missing attackers/defenders/goalkeeper flags
  - missing top scorer/playmaker/starting GK flags

Later fields:

- Predicted lineups
- Lineup confidence
- Rotation probability
- Player fatigue from recent minutes
- International travel and late return
- Injury severity ontology
- Substitution pattern by manager
- Bench strength
- Transfer-market value or wage proxy, if licensed
- Player embeddings / quality ratings

### Sources

Paid/broad options:

- Sportmonks: lineups, formations, sidelined injured/suspended players, predicted/expected lineups. Source: [Sportmonks lineups/formations docs](https://docs.sportmonks.com/football/tutorials-and-guides/tutorials/lineups-and-formations), [Sportmonks expected lineups](https://www.sportmonks.com/football-api/expected-lineups-api/).
- API-Football: lineups, player stats, injuries, predictions, odds; its beginner guide states injuries can be filtered by fixture/team/player/date and updates every 4 hours. Source: [API-Football beginner guide](https://www.api-football.com/news/post/how-to-get-started-with-api-football-the-complete-beginners-guide).
- SportsDataIO: offers real-time sports data, soccer coverage, and player-feed concepts across sports; useful for a multi-sport provider shortlist. Source: [SportsDataIO getting started](https://support.sportsdata.io/hc/en-us/articles/4406143092887-Getting-Started-with-Sports-Data-APIs).
- Sportradar/IMG Arena documentation: lineups endpoint with 30-second polling recommendation when lineups are expected. Source: [Sportradar soccer lineups docs](https://docs.sportradar.com/soccer/rest-api/lineups).
- RotoWire: soccer injury tables and content syndication, useful for injury coverage in major leagues. Sources: [RotoWire soccer injuries](https://www.rotowire.com/soccer/injury-report.php), [RotoWire content syndication](https://www.rotowire.com/advertise/content-syndication.pdf).
- FootballFeeds / specialist lineup feeds: official-lineup oriented services exist for betting/media use cases. Source: [FootballFeeds official line-ups](https://footballfeeds.com/services/official-line-ups/).

Free / lower-cost / supplementary:

- Official club websites and official league/team social channels for lineup/injury announcements. High authority, but hard to normalize and often not API-friendly.
- Official competition PDFs/feeds in UEFA/FIFA contexts for confirmed lineups, but event-specific and not general enough for platform-wide ingestion.
- News APIs with injury/team filters, e.g. Goalise/Kablenett-style football news/injury APIs for some leagues. Sources: [Goalise football news API](https://goalise.com/football-news-api), [Kablenett injury/news API](https://kablenett.com/).

Avoid as core production dependencies without legal review:

- Scraping Sofascore, FotMob, Flashscore, Transfermarkt or predicted-lineup sites. They are attractive for coverage but brittle and likely terms-sensitive.

### Cadence

- Long-term injuries/suspensions: 1-4 times per day; more often in matchday windows.
- Predicted lineups: daily, then every few hours during 48h before kickoff.
- Confirmed lineups: typically 60-75 minutes before kickoff; poll every 30-60 seconds in final 90 minutes if provider permits.
- Substitutions/minutes: live or post-match depending on provider.
- Player stats aggregates: post-match finalization, then nightly recompute.

### Reliability And Legal Concerns

- Injury data is notoriously noisy: "doubtful", "illness", "knock", and "not in squad" often mean different things across providers.
- Suspensions are more reliable than injuries if sourced from official competition records.
- Predicted lineups are forecasts, not facts. Track provider accuracy.
- Player IDs are often not stable across providers, seasons, and competitions.
- Some APIs have coverage flags by league/season; store these explicitly.
- Personal data concerns are usually manageable for public professional athletes, but contracts and redistribution rights matter.

### Canonical Availability Model

Use a normalized status taxonomy:

- `available`
- `confirmed_starting`
- `confirmed_bench`
- `confirmed_not_in_squad`
- `injured_out`
- `injury_doubtful`
- `suspended`
- `international_duty`
- `personal/other`
- `unknown`

For model use, derive:

- `home_missing_minutes_share`
- `away_missing_minutes_share`
- `home_missing_starters_count`
- `away_missing_starters_count`
- `home_missing_starting_gk`
- `home_missing_top_attacker`
- `home_lineup_continuity_score`
- `home_confirmed_lineup_available`
- same away equivalents

### Graceful Degradation

If no player/injury data:

- Use recent lineup continuity from observed lineups if available.
- Use recent minutes and squad rotation only where lineups exist.
- If no lineups at all, use team-level rest/congestion and team-strength uncertainty.
- Do not infer a player is available because no injury record exists; encode `availability_unknown`.

## Feature Group 3: Context Features

### Important Data

MVP fields:

- Match date/time and timezone
- Venue/stadium ID and coordinates
- Home/away/neutral venue
- Rest days since last match
- Matches in last 7, 14, 21 days
- Travel distance from previous venue/home city
- Domestic vs continental/international fixture
- League table position and points
- Points from relegation/title/playoff/continental spots
- Season phase: early/mid/late
- Derby/rivalry flag, manually curated for major leagues
- Weather at venue near kickoff:
  - temperature
  - precipitation
  - wind speed/gust
  - humidity
  - weather code
- Pitch/venue surface where available
- Manager tenure days
- Recent manager change flag
- Transfer-window squad churn proxy

Later fields:

- Actual travel mode/time zones
- Altitude
- attendance/crowd restrictions
- referee profile
- tactical style matchup
- international-break returnees
- motivation labels:
  - must-win for survival
  - clinched/no-stakes
  - rotation risk before cup/continental match
- local weather forecast snapshots at prediction time, not just actual weather

### Sources

Fixtures, venue, standings:

- Primary sports API provider: Sportmonks, API-Football, SportsDataIO, TheStatsAPI, AnySport, football-data.org depending on coverage. Sources: [Sportmonks pricing](https://www.sportmonks.com/football-api/plans-pricing/), [AnySport docs](https://docs.anysport.io/), [football-data.org pricing](https://www.football-data.org/pricing).
- football-data.org is useful for competitions, fixtures, schedules, tables, and basic historical data in supported competitions. Source: [football-data.org pricing](https://www.football-data.org/pricing).

Weather:

- Open-Meteo: strong default for global historical and forecast weather; historical API supports coordinates and hourly variables. Source: [Open-Meteo historical weather API](https://open-meteo.com/en/docs/historical-weather-api).
- Meteostat: open historical station/weather data via Python library and bulk downloads. Source: [Meteostat developers](https://dev.meteostat.net/).
- Windy / OpenWeatherMap: commercial or higher-end weather options if live/forecast quality becomes important. Source: [Windy API](https://api.windy.com/).

Geocoding / location:

- Provider venue coordinates where available.
- GeoNames / geocoding APIs for fallback city/stadium coordinates. Source: [GeoNames-backed geocoded.me](https://geocoded.me/).
- Manual stadium gazetteer for priority leagues.

Transfers:

- FIFA Transfer Matching System reports are official but aggregated, not fixture-level operational data. Source: [FIFA transfer reports methodology](https://inside.fifa.com/transfer-system/transfer-reports/methodology).
- Paid sports APIs may include transfers; validate coverage per league.
- Transfermarkt is useful for research, but scraping/commercial reuse is legally sensitive and technically brittle.

Manager changes:

- Paid sports data providers may include coaches/managers.
- Official club/league announcements and reputable news feeds are authoritative but require entity extraction and manual QA.
- Wikipedia can be useful for historical backfill in major leagues but should not be a production real-time source.

Derbies/rivalries:

- Best handled as manually curated reference data with source notes.
- Automated derivation from geography alone is not enough.

Motivation/relegation pressure:

- Derive from standings, remaining fixtures, points available, qualification/relegation rules, and simulations.
- Manual competition rules are needed for playoffs, split leagues, deductions, and continental qualification.

### Cadence

- Rest/congestion/travel/table pressure: recompute after every fixture update and nightly.
- Weather forecast: pull at T-7d, T-48h, T-24h, T-6h, T-1h; store snapshots to avoid leakage.
- Historical weather actuals: pull after match completion for analysis/backtests.
- Venue coordinates: static, update monthly or on provider changes.
- Manager changes/transfers: daily outside windows, every 1-4 hours during transfer windows or major news periods.
- Motivation/table pressure: recompute after every relevant match.

### Reliability And Legal Concerns

- Fixture dates/times change often; store version history.
- Weather should be prediction-time forecast for pre-match modelling. Using actual weather in backtests can create leakage unless the product would have had that data at prediction time.
- Travel distance is a proxy unless actual team travel logistics are known.
- Motivation labels are easy to overfit; derive quantitatively where possible.
- Manager/transfer data from news requires source attribution and deduplication.

### Graceful Degradation

If venue coordinates missing:

- Use team home city coordinates.
- If city missing, use league/country centroid only for coarse travel; set low confidence.

If weather missing:

- Encode missing; do not impute league average unless model requires it.

If manager/transfers missing:

- Use squad continuity proxies from lineups/minutes where available.
- Otherwise rely on team-strength uncertainty.

## Provider Shortlist

### MVP Shortlist

1. Sportmonks
   - Why: broad football coverage, lineups, injuries/sidelined, xG, expected lineups, odds/predictions add-ons.
   - Concern: validate league-by-league accuracy, especially injuries and Asian coverage.

2. API-Football
   - Why: affordable, broad coverage, lineups, injuries, odds, predictions, coverage flags.
   - Concern: community reports suggest data quality and ID consistency issues; test before relying on it.

3. TheStatsAPI
   - Why: developer-friendly positioning, xG/npxG/xA, odds, player stats, historical depth, requested coverage expansion.
   - Concern: newer/smaller provider; validate availability for specific Asian leagues and contractual rights.

4. SportsDataIO
   - Why: mature multi-sport provider, relevant if platform expands beyond football.
   - Concern: cost and exact soccer feature depth must be verified.

5. Open-Meteo
   - Why: global weather forecast and historical weather, strong fit for venue-context features.
   - Concern: commercial usage/pricing and model-vs-observation choice need review.

### Enterprise / Later

- Stats Perform / Opta
- StatsBomb paid API
- Wyscout
- Sportradar / IMG Arena
- TXODDS or other premium odds feed
- RotoWire or specialist injury/news syndication provider

### Prototype / Research Only

- StatsBomb Open Data
- football-data.co.uk
- football-data.org
- soccerdata / socceraction loaders
- manually curated derby/venue/manager datasets

## Recommended MVP Canonical Schema

### `fixture_context_snapshot`

- `fixture_id`
- `snapshot_at`
- `kickoff_at`
- `home_team_id`
- `away_team_id`
- `competition_id`
- `season_id`
- `venue_id`
- `neutral_venue`
- `home_rest_days`
- `away_rest_days`
- `home_matches_last_7d`
- `away_matches_last_7d`
- `home_matches_last_14d`
- `away_matches_last_14d`
- `home_travel_km_proxy`
- `away_travel_km_proxy`
- `home_table_position`
- `away_table_position`
- `home_points`
- `away_points`
- `home_points_to_relegation`
- `away_points_to_relegation`
- `home_points_to_title_or_promotion`
- `away_points_to_title_or_promotion`
- `season_phase`
- `derby_flag`
- `context_confidence`

### `fixture_weather_snapshot`

- `fixture_id`
- `snapshot_at`
- `weather_valid_at`
- `source_provider`
- `latitude`
- `longitude`
- `temperature_c`
- `precipitation_mm`
- `wind_speed_kmh`
- `wind_gust_kmh`
- `humidity_pct`
- `weather_code`
- `is_forecast`
- `is_actual`
- `confidence`

### `team_chance_quality_snapshot`

- `fixture_id`
- `team_id`
- `snapshot_at`
- `source_provider`
- `xg_for_last_5`
- `xg_against_last_5`
- `xg_for_last_10`
- `xg_against_last_10`
- `npxg_for_last_10`
- `npxg_against_last_10`
- `shots_for_last_10`
- `shots_against_last_10`
- `shots_on_target_for_last_10`
- `shots_on_target_against_last_10`
- `xg_per_shot_last_10`
- `chance_quality_tier`
- `provider_xg_definition_version`
- `confidence`

### `fixture_lineup_snapshot`

- `fixture_id`
- `team_id`
- `snapshot_at`
- `lineup_type`: predicted, confirmed, actual_final
- `formation`
- `source_provider`
- `provider_confidence`
- `confirmed_at`
- `players_json`
- `lineup_continuity_score`
- `missing_starters_count`
- `missing_minutes_share`
- `availability_confidence`

### `player_availability_snapshot`

- `fixture_id`
- `team_id`
- `player_id`
- `snapshot_at`
- `status`
- `reason`
- `expected_return_at`
- `source_provider`
- `source_url_or_ref`
- `severity`
- `is_suspension`
- `is_injury`
- `is_doubtful`
- `player_minutes_share`
- `player_importance_score`
- `confidence`

### `team_staff_transfer_snapshot`

- `team_id`
- `fixture_id`
- `snapshot_at`
- `manager_id`
- `manager_tenure_days`
- `manager_changed_last_30d`
- `incoming_transfers_last_window`
- `outgoing_transfers_last_window`
- `squad_churn_score`
- `source_provider`
- `confidence`

## Ingestion Architecture

### Principles

- Raw first, normalized second, features third.
- Every row needs provenance.
- Every feature snapshot must be time-aware.
- Missingness is information; encode why a value is absent.
- Model training must use the data that would have been known at prediction time.

### Pipeline

1. Provider adapters
   - One adapter per source: Sportmonks, API-Football, TheStatsAPI, Open-Meteo, etc.
   - Handles auth, pagination, rate limits, retries, and provider-specific schemas.

2. Raw landing zone
   - Store unchanged JSON/XML/PDF/text payloads in object storage.
   - Partition by provider/entity/date.
   - Include request URL, response headers, fetched_at, and licence tier.

3. Canonical normalization
   - Convert provider entities into canonical fixtures, teams, players, venues, competitions, seasons.
   - Maintain provider ID mapping tables.
   - Use compound identity for players: provider_player_id, team, season, competition, date range.

4. Entity resolution
   - Deterministic match on provider IDs where available.
   - Fuzzy matching only with human review for players/teams.
   - Store confidence and never silently merge uncertain players.

5. Snapshot builder
   - Build feature snapshots at defined prediction times:
     - T-7d
     - T-48h
     - T-24h
     - T-6h
     - T-1h
     - lineup-confirmed
   - Lock snapshots for reproducible backtests.

6. Feature store
   - Offline: Parquet/DuckDB/Postgres tables for model training.
   - Online: Redis/Postgres materialized views for upcoming fixture API.
   - Version feature definitions.

7. Quality monitor
   - Provider freshness.
   - Coverage by league.
   - Missing field rates.
   - Outlier detection.
   - Cross-provider conflicts.
   - Lineup prediction accuracy.

8. Model feature vector exporter
   - Outputs `fixture_id`, `model_version`, `snapshot_at`, and feature columns.
   - Guarantees no future leakage.

## Data Quality Checks

### xG / Chance Quality

- xG values non-negative and plausible: team xG normally 0-6, investigate >7.
- Total xG roughly consistent with shot count.
- Penalty xG not double-counted in npxG.
- Match xG finalization timestamp after match end.
- Provider xG version changes flagged.
- Missing xG coverage tracked by competition/season.

### Lineups / Player Availability

- Starting XI count equals 11 except known abandoned/special cases.
- Formation positions compatible with lineup count.
- Suspended player cannot appear in confirmed lineup unless data conflict is flagged.
- Injury status has observed timestamp and source.
- Player ID maps to active squad at fixture date.
- Predicted-lineup accuracy tracked against confirmed lineups by provider/team/league.

### Context

- Rest days cannot be negative unless fixture data changed; flag.
- Travel distance should be plausible; extreme values reviewed.
- Venue coordinates present for priority leagues.
- Weather valid time within match window.
- Table pressure features generated after latest known table at snapshot time.
- Manager change dates not after snapshot time.
- Transfer-window effects use only completed transfers known before snapshot.

## Modelling Use

### xG Features

Use for:

- improving attack/defence strength estimates
- early-season stabilization
- distinguishing finishing luck from chance creation
- total-goals market calibration

Avoid:

- mixing provider xG definitions without source controls
- treating proxy xG as equivalent to event-derived xG

### Player/Lineup Features

Use for:

- late pre-match probability updates
- team-strength adjustment when key players are missing
- lineup-confirmed model variant

Avoid:

- overreacting to unweighted injury counts
- using predicted lineups without provider accuracy history

### Context Features

Use for:

- fixture congestion/rest/travel adjustment
- motivation/table-pressure simulation features
- weather/venue adjustments where signal is proven

Avoid:

- hand-written "must win" labels without validation
- weather effects that look significant only in tiny samples
- derby effects that duplicate home advantage or market priors

## Sparse-League Strategy For Asia And Europe

### League Coverage Tiers

Tier A: rich data

- xG/event data, lineups, injuries, player stats, odds.
- Use full model with xG and player availability.

Tier B: medium data

- match stats, lineups, odds, limited injuries.
- Use stats proxy, lineup continuity, rest/travel/context.

Tier C: basic data

- fixtures, results, standings, odds.
- Use team-strength model, market baseline, rest/travel/table pressure.

Tier D: minimal data

- fixtures/results only.
- Use conservative team-strength model with strong shrinkage and wider uncertainty.

### Degradation Rules

- Always output `feature_coverage_tier`.
- Always output `probability_confidence`.
- Use hierarchical priors for sparse leagues.
- Do not fill missing high-value features with misleading defaults.
- Prefer lower confidence over false precision.
- Compare each league only against relevant baselines.

## MVP Build Plan

### Week 1-2: Provider Test

- Trial Sportmonks, API-Football, TheStatsAPI, and one odds/weather source.
- Select 10 target leagues including Europe and Asia.
- Pull fixtures, results, standings, venues, lineups, injuries, xG/stats where available.
- Build coverage matrix.

### Week 3-4: Canonical Data Model

- Implement provider adapters and raw payload storage.
- Normalize fixtures, teams, players, venues.
- Build ID mapping and source provenance.
- Implement weather enrichment via Open-Meteo.

### Week 5-6: Feature Snapshots

- Build context snapshots.
- Build xG/chance-quality snapshots.
- Build lineup/availability snapshots.
- Create missingness/confidence indicators.

### Week 7-8: Backtest Integration

- Export model-ready feature vectors.
- Run ablations:
  - base model only
  - base + xG
  - base + lineup/availability
  - base + context
  - all features
- Evaluate by league and feature tier.

## Source Notes

Sources accessed 2026-05-24:

- Sportmonks lineups/formations: https://docs.sportmonks.com/football/tutorials-and-guides/tutorials/lineups-and-formations
- Sportmonks expected lineups: https://www.sportmonks.com/football-api/expected-lineups-api/
- Sportmonks xG endpoint: https://docs.sportmonks.com/football/endpoints-and-entities/endpoints/expected-xg/get-expected-by-team
- Sportmonks pricing: https://www.sportmonks.com/football-api/plans-pricing/
- API-Football beginner guide / injuries notes: https://www.api-football.com/news/post/how-to-get-started-with-api-football-the-complete-beginners-guide
- TheStatsAPI: https://www.thestatsapi.com/
- SportsDataIO: https://sportsdata.io/
- SportsDataIO getting started: https://support.sportsdata.io/hc/en-us/articles/4406143092887-Getting-Started-with-Sports-Data-APIs
- Sportradar soccer lineups docs: https://docs.sportradar.com/soccer/rest-api/lineups
- FootballFeeds official line-ups: https://footballfeeds.com/services/official-line-ups/
- RotoWire soccer injuries: https://www.rotowire.com/soccer/injury-report.php
- RotoWire content syndication: https://www.rotowire.com/advertise/content-syndication.pdf
- StatsBomb Open Data: https://github.com/statsbomb/open-data
- socceraction docs: https://socceraction.readthedocs.io/_/downloads/en/latest/pdf/
- soccerdata docs: https://soccerdata.readthedocs.io/_/downloads/en/stable/pdf/
- AnySport docs: https://docs.anysport.io/
- football-data.org pricing: https://www.football-data.org/pricing
- Open-Meteo historical weather API: https://open-meteo.com/en/docs/historical-weather-api
- Meteostat developers: https://dev.meteostat.net/
- Windy API: https://api.windy.com/
- GeoNames-backed geocoded.me: https://geocoded.me/
- FIFA transfer reports methodology: https://inside.fifa.com/transfer-system/transfer-reports/methodology
- Goalise football news API: https://goalise.com/football-news-api
- Kablenett injury/news API: https://kablenett.com/
