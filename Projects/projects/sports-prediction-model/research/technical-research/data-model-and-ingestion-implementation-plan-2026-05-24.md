# Data Model And Ingestion Implementation Plan

Date: 2026-05-24

Project: scalable league-sports prediction platform, football-first.

## Objective

Create a data platform that can regularly ingest, normalize and serve model-ready data for match prediction:

- Base match data: fixtures, results, standings, odds and team ratings.
- Advanced features: xG/chance quality, player availability/lineups and match context.
- Multi-league/multi-country support across Europe, Asia and later other league sports.
- Time-aware feature snapshots so backtests use only data that would have been known at prediction time.

The platform should support sparse leagues gracefully. It should not require every league to have xG, injuries or lineups before we can make a prediction.

## Architecture Overview

```text
Provider APIs / files / weather / odds
  -> provider adapters
  -> raw payload store
  -> canonical entity store
  -> entity resolution and provider mappings
  -> feature snapshot builder
  -> offline feature store
  -> model training / backtesting
  -> online prediction feature views
```

Core principles:

- Store raw provider payloads unchanged.
- Normalize into canonical sports, countries, competitions, seasons, teams, players, fixtures and venues.
- Keep provider IDs out of modelling tables.
- Build time-aware snapshots at known prediction times.
- Track source, timestamp, confidence and missing reason for every important feature.
- Use explicit feature coverage tiers so sparse leagues produce lower-confidence predictions rather than false precision.

## Recommended Tool Stack

### MVP Local/Small-Scale Stack

- Python 3.12
- `httpx` for API clients
- `pydantic` for provider payload validation
- `tenacity` for retries/backoff
- `pandas` or `polars` for transformations
- DuckDB for local analytical storage
- Parquet for raw/normalized table files
- SQLite or Postgres for metadata, provider mappings and job state
- `pytest` for adapter and transform tests
- `ruff` for linting
- `mypy` or pyright later if the codebase grows

### Production-Ready Stack

- Postgres for canonical relational data
- Object storage for raw payloads: S3, Cloudflare R2, GCS or local MinIO
- DuckDB/Parquet for offline training datasets
- Redis or Postgres materialized views for online fixture features
- Dagster or Prefect for orchestration
- dbt for SQL transformations once schemas stabilize
- Great Expectations or Soda for data quality checks
- OpenTelemetry/logging for ingestion observability
- GitHub Actions for tests and scheduled smoke checks

### Provider Access Tools

Provider adapters should be small Python clients:

- `providers/football_data_co_uk.py`
- `providers/football_data_org.py`
- `providers/sportmonks.py`
- `providers/api_football.py`
- `providers/thestatsapi.py`
- `providers/open_meteo.py`
- `providers/odds.py`

Each adapter should expose the same shape:

```python
class ProviderAdapter:
    provider_name: str

    def fetch_fixtures(self, competition_id: str, season: str): ...
    def fetch_results(self, competition_id: str, season: str): ...
    def fetch_standings(self, competition_id: str, season: str): ...
    def fetch_odds(self, fixture_id: str): ...
    def fetch_lineups(self, fixture_id: str): ...
    def fetch_injuries(self, team_id: str, fixture_id: str | None = None): ...
    def fetch_xg(self, fixture_id: str | None = None, team_id: str | None = None): ...
    def fetch_weather(self, venue_id: str, valid_at: str): ...
```

Not every provider supports every method. Unsupported methods should return a typed `UnsupportedCapability` result, not fail unpredictably.

## Provider Strategy

### Phase 1: Free / Prototype Sources

Use these to build the first ingestion and modelling pipeline:

- Football-Data.co.uk: historical results, odds and CSVs.
- football-data.org: fixtures, standings and supported competitions.
- StatsBomb Open Data: event/xG-style prototype data, limited coverage.
- Open-Meteo: global weather forecast and historical weather.
- ClubElo: external team-strength benchmark.

### Phase 2: Coverage Trial Sources

Trial these across 8-12 target leagues before committing:

- Sportmonks
- API-Football
- TheStatsAPI
- SportsDataIO
- One odds provider
- Open-Meteo

Evaluate:

- league coverage
- fixture freshness
- team/player ID stability
- lineup completeness
- injury reliability
- xG availability
- odds coverage
- API cost and rate limits
- redistribution/commercial rights

### Phase 3: Enterprise Sources

Consider only once the modelling spike proves value:

- Stats Perform / Opta
- StatsBomb paid API
- Wyscout
- Sportradar / IMG Arena
- TXODDS or equivalent premium odds feed
- RotoWire or specialist injury/news syndication

### Avoid As Core Dependencies Without Legal Review

- Scraping Transfermarkt
- Scraping Sofascore
- Scraping FotMob
- Scraping Flashscore
- Scraping Understat
- Scraping FBref
- Unofficial club/social scraping

These may be useful for manual research, but they are brittle and terms-sensitive.

## Canonical Data Model

### Entity Tables

#### `sports`

- `sport_id`
- `sport_name`
- `scoring_type`
- `allows_draw`
- `default_model_family`
- `created_at`
- `updated_at`

#### `countries`

- `country_id`
- `country_name`
- `country_code`
- `region`
- `timezone`

#### `competitions`

- `competition_id`
- `sport_id`
- `country_id`
- `competition_name`
- `competition_type`
- `tier`
- `governing_body`
- `active`

#### `seasons`

- `season_id`
- `competition_id`
- `season_name`
- `start_date`
- `end_date`
- `rules_version`
- `active`

#### `teams`

- `team_id`
- `sport_id`
- `country_id`
- `team_name`
- `short_name`
- `home_venue_id`
- `active`

#### `players`

- `player_id`
- `sport_id`
- `canonical_name`
- `date_of_birth`
- `nationality_country_id`
- `primary_position`
- `active`

#### `venues`

- `venue_id`
- `venue_name`
- `country_id`
- `city`
- `latitude`
- `longitude`
- `altitude_m`
- `surface`
- `capacity`
- `timezone`

### Provider Mapping Tables

#### `provider_entities`

- `provider_entity_id`
- `provider_name`
- `entity_type`: competition, season, team, player, fixture, venue
- `provider_native_id`
- `provider_name_text`
- `canonical_entity_id`
- `match_confidence`
- `first_seen_at`
- `last_seen_at`
- `active`

#### `entity_resolution_queue`

- `resolution_id`
- `provider_name`
- `entity_type`
- `provider_native_id`
- `provider_name_text`
- `candidate_canonical_id`
- `candidate_score`
- `status`: pending, approved, rejected, merged
- `reviewed_by`
- `reviewed_at`

Use deterministic provider IDs where possible. Use fuzzy matching only into the review queue for teams/players, not direct automatic merges.

## Fixture And Result Model

#### `fixtures`

- `fixture_id`
- `sport_id`
- `country_id`
- `competition_id`
- `season_id`
- `home_team_id`
- `away_team_id`
- `venue_id`
- `kickoff_at`
- `kickoff_timezone`
- `status`: scheduled, postponed, live, complete, abandoned, cancelled
- `neutral_venue`
- `round_name`
- `source_provider`
- `created_at`
- `updated_at`

#### `fixture_versions`

- `fixture_version_id`
- `fixture_id`
- `observed_at`
- `source_provider`
- `kickoff_at`
- `venue_id`
- `status`
- `raw_payload_ref`
- `change_reason`

Fixture times change often. Versioning avoids silent leakage and allows backtests to use the schedule known at the time.

#### `results`

- `fixture_id`
- `home_score`
- `away_score`
- `home_score_periods_json`
- `away_score_periods_json`
- `result_status`
- `settled_at`
- `source_provider`
- `raw_payload_ref`

#### `standings_snapshots`

- `snapshot_id`
- `competition_id`
- `season_id`
- `snapshot_at`
- `team_id`
- `position`
- `played`
- `wins`
- `draws`
- `losses`
- `goals_for`
- `goals_against`
- `goal_difference`
- `points`
- `source_provider`

## Odds And Market Data

#### `odds_snapshots`

- `odds_snapshot_id`
- `fixture_id`
- `snapshot_at`
- `bookmaker`
- `market_type`: 1x2, over_under, btts, handicap
- `selection`
- `decimal_odds`
- `is_opening`
- `is_closing`
- `source_provider`
- `raw_payload_ref`

#### `market_probabilities`

- `fixture_id`
- `snapshot_at`
- `market_type`
- `home_implied_prob`
- `draw_implied_prob`
- `away_implied_prob`
- `bookmaker_margin`
- `margin_removed_method`
- `source_provider`

Odds are both a benchmark and optional feature. Closing odds should be kept separate from prediction-time odds to avoid leakage.

## Feature Snapshot Tables

### Context

#### `fixture_context_snapshots`

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
- `home_matches_last_21d`
- `away_matches_last_21d`
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
- `feature_coverage_tier`
- `context_confidence`
- `missing_feature_summary`

#### `fixture_weather_snapshots`

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

For pre-match modelling, prefer forecast snapshots from the time of prediction. Actual weather is useful for analysis but can leak future information in backtests.

### xG / Chance Quality

#### `team_chance_quality_snapshots`

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
- `chance_quality_tier`: none, basic_stats, xg, event
- `provider_xg_definition_version`
- `confidence`
- `is_missing_reason`

#### `match_chance_quality_events`

Optional for event providers:

- `event_id`
- `fixture_id`
- `team_id`
- `player_id`
- `event_time`
- `event_type`
- `x`
- `y`
- `xg`
- `post_shot_xg`
- `body_part`
- `situation`
- `source_provider`
- `raw_payload_ref`

### Player / Lineup / Availability

#### `fixture_lineup_snapshots`

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

#### `player_availability_snapshots`

- `fixture_id`
- `team_id`
- `player_id`
- `snapshot_at`
- `status`: available, confirmed_starting, confirmed_bench, confirmed_not_in_squad, injured_out, injury_doubtful, suspended, international_duty, personal_other, unknown
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

### Staff / Transfers

#### `team_staff_transfer_snapshots`

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

## Ratings And Model Tables

#### `team_ratings`

- `rating_id`
- `sport_id`
- `competition_id`
- `team_id`
- `rating_date`
- `rating_model`
- `elo`
- `attack_rating`
- `defence_rating`
- `home_advantage_component`
- `rating_uncertainty`
- `model_version`

#### `model_feature_vectors`

- `feature_vector_id`
- `fixture_id`
- `snapshot_at`
- `model_version`
- `feature_schema_version`
- `feature_coverage_tier`
- `features_json`
- `created_at`

#### `predictions`

- `prediction_id`
- `fixture_id`
- `snapshot_at`
- `model_version`
- `model_family`
- `predicted_home_score_mean`
- `predicted_away_score_mean`
- `home_win_prob`
- `draw_prob`
- `away_win_prob`
- `over_2_5_prob`
- `btts_prob`
- `probability_confidence`
- `feature_coverage_tier`
- `created_at`

#### `backtest_runs`

- `backtest_run_id`
- `model_version`
- `feature_schema_version`
- `competition_scope`
- `date_start`
- `date_end`
- `split_policy`
- `created_at`
- `notes`

#### `backtest_metrics`

- `backtest_run_id`
- `competition_id`
- `season_id`
- `log_loss`
- `brier_score`
- `ranked_probability_score`
- `calibration_error`
- `mean_absolute_goal_error`
- `closing_line_log_loss`
- `sample_size`

## Raw Payload Store

Store raw data outside canonical tables:

```text
data/raw/
  provider=football-data-co-uk/entity=matches/date=2026-05-24/...
  provider=sportmonks/entity=lineups/date=2026-05-24/...
  provider=open-meteo/entity=forecast/date=2026-05-24/...

data/normalized/
  fixtures/
  teams/
  players/
  standings/

data/features/
  fixture_context_snapshots/
  fixture_weather_snapshots/
  team_chance_quality_snapshots/
```

Each raw payload metadata record should include:

- `raw_payload_ref`
- `provider_name`
- `endpoint`
- `request_params`
- `fetched_at`
- `http_status`
- `response_hash`
- `licence_tier`
- `parser_version`

## Ingestion Jobs

### Daily Jobs

1. `sync_competitions`
   - Pull competitions/leagues/seasons from provider.
   - Update canonical competition and season records.

2. `sync_fixtures`
   - Pull fixtures for target leagues.
   - Record fixture versions when kickoff/status/venue changes.

3. `sync_results`
   - Pull completed results.
   - Settle final scores.
   - Trigger ratings update.

4. `sync_standings`
   - Pull or derive standings.
   - Store timestamped standings snapshots.

5. `sync_injuries_suspensions`
   - Pull player availability feeds where supported.
   - Normalize statuses.
   - Update availability snapshots.

6. `sync_weather_forecasts`
   - Pull weather for upcoming fixtures at T-7d/T-48h/T-24h/T-6h/T-1h.

7. `build_feature_snapshots`
   - Generate model-ready snapshots for upcoming fixtures.

### Matchday Jobs

1. `poll_fixture_status`
   - Every 5-15 minutes for fixtures in the next 24h.

2. `poll_lineups`
   - Every 30-60 seconds in the final 90 minutes before kickoff if provider terms permit.
   - Otherwise every 2-5 minutes.

3. `poll_odds`
   - Frequency depends on provider cost and product need.
   - Store opening, periodic and closing snapshots separately.

4. `lineup_confirmed_prediction_refresh`
   - Rebuild feature vector when confirmed lineups arrive.
   - Generate updated probabilities.

### Post-Match Jobs

1. `finalize_match_stats`
   - Pull stats/xG/events when provider marks fixture final.

2. `update_team_ratings`
   - Update Elo, attack and defence ratings.

3. `rebuild_rolling_features`
   - xG, shots, form, rest and lineup continuity.

4. `settle_predictions`
   - Compare predictions to result.
   - Update backtest/evaluation tables.

## Data Quality Checks

### Entity Checks

- No duplicate canonical teams in same competition/season.
- Provider team mappings must resolve to one canonical team.
- Player mappings require high confidence or manual review.
- Fixture home and away teams cannot be the same.

### Fixture Checks

- Kickoff time must have timezone.
- Fixture status transitions must be valid.
- Venue coordinates required for priority leagues.
- Fixture date changes must create a version record.

### xG Checks

- xG must be non-negative.
- Team match xG normally between 0 and 6; investigate above 7.
- Non-penalty xG must not exceed total xG.
- xG finalization timestamp must be after match end.
- Provider xG definition/version changes must be flagged.

### Player Checks

- Confirmed starting XI should equal 11 except special cases.
- Suspended players appearing in confirmed lineup must create conflict flag.
- Injury records must have observed timestamp and source.
- Predicted lineup accuracy should be tracked by provider and league.

### Context Checks

- Rest days cannot be negative.
- Travel distance must be plausible.
- Weather valid time must be near kickoff.
- Table-pressure features must be generated from standings known at snapshot time.
- Manager changes/transfers must be known before snapshot time.

## Feature Coverage And Graceful Degradation

Every fixture should be assigned a tier:

- Tier A: xG/event data, lineups, injuries, player stats and odds.
- Tier B: match stats, lineups, odds and limited injuries.
- Tier C: fixtures, results, standings and odds.
- Tier D: fixtures/results only.

Model behavior:

- Tier A: full model.
- Tier B: stats proxy plus lineup/context model.
- Tier C: team-strength plus context and market baseline.
- Tier D: conservative team-strength model with strong shrinkage and wider uncertainty.

Every prediction should include:

- `feature_coverage_tier`
- `probability_confidence`
- `missing_feature_summary`

## Implementation Phases

### Phase 0: Project Setup

Deliverables:

- Repository structure.
- Python environment.
- Config system for provider credentials.
- Basic logging.
- Raw data directory conventions.
- DuckDB/Postgres schema migrations.

Suggested folders:

```text
sports-prediction-model/
  docs/
  src/
    sports_prediction/
      providers/
      ingest/
      normalize/
      features/
      quality/
      models/
      backtests/
  data/
    raw/
    normalized/
    features/
  tests/
```

### Phase 1: Base Data Backbone

Implement:

- Football-Data.co.uk CSV importer.
- football-data.org fixture/standings adapter.
- Canonical sports/countries/competitions/seasons/teams/fixtures/results schema.
- Provider mapping tables.
- Fixture versioning.
- Standings snapshots.

Output:

- Clean historical match database.
- Repeatable import command.
- Basic coverage report.

### Phase 2: Weather And Context

Implement:

- Venue coordinates.
- Open-Meteo adapter.
- Rest days.
- Fixture congestion.
- Travel proxy.
- Table pressure.
- Context snapshot table.

Output:

- `fixture_context_snapshots`
- `fixture_weather_snapshots`
- Feature vectors for base + context model.

### Phase 3: Provider Coverage Trial

Trial:

- Sportmonks
- API-Football
- TheStatsAPI
- SportsDataIO

Across:

- 8-12 target leagues.
- Mix of major Europe, second-tier Europe and Asian leagues.

Measure:

- fixtures
- results
- standings
- odds
- lineups
- injuries
- suspensions
- xG
- match stats
- player IDs
- freshness
- cost

Output:

- Provider coverage matrix.
- Recommendation on paid provider selection.

### Phase 4: Player And Lineup Layer

Implement:

- Lineup adapter for chosen provider.
- Injury/suspension adapter.
- Player entity resolution.
- Player availability snapshots.
- Lineup snapshots.
- Missing-minutes and missing-starter features.

Output:

- Late pre-match model feature set.
- Lineup-confirmed prediction refresh.

### Phase 5: xG And Chance Quality Layer

Implement:

- xG/match stats adapter.
- Rolling xG and shot features.
- Provider xG definition tracking.
- Chance-quality tiering.

Output:

- xG-enhanced attack/defence model features.
- Ablation tests: base vs base + xG.

### Phase 6: Modelling And Backtesting

Implement:

- Elo baseline.
- Dixon-Coles football score model.
- Feature vector exporter.
- Time-based backtest runner.
- Metrics: log loss, Brier score, ranked probability score, calibration, closing-line comparison.
- Ablations:
  - base only
  - base + context
  - base + player/lineup
  - base + xG
  - all features

Output:

- Model performance report by league and feature tier.
- Decision on which features are worth production cost.

## Commands To Build

The implementation should expose simple CLI commands:

```bash
spm ingest football-data-co-uk --competition EPL --season 2024-2025
spm ingest football-data-org --competition PL --season 2025
spm ingest provider-trial --provider sportmonks --league-list config/target_leagues.yml
spm enrich weather --from 2026-05-24 --to 2026-06-01
spm build features --snapshot T-24h
spm build features --snapshot lineup-confirmed
spm quality report --league EPL --season 2025-2026
spm backtest --model dixon-coles --from 2018-08-01 --to 2026-05-24
spm predict upcoming --competition EPL --snapshot T-24h
```

## Required Secrets And Config

Use `.env` or a secret manager for:

- `FOOTBALL_DATA_ORG_API_KEY`
- `SPORTMONKS_API_KEY`
- `API_FOOTBALL_API_KEY`
- `THESTATSAPI_API_KEY`
- `SPORTSDATAIO_API_KEY`
- `ODDS_PROVIDER_API_KEY`

Config files:

- `config/providers.yml`
- `config/target_leagues.yml`
- `config/feature_snapshots.yml`
- `config/model_versions.yml`
- `config/manual_derbies.yml`
- `config/manual_venues.yml`

## Immediate Next Step

Build the Phase 1 and Phase 2 backbone before buying data:

1. Create the repository/package structure.
2. Implement raw payload storage.
3. Implement Football-Data.co.uk historical import.
4. Implement football-data.org fixture/standings import.
5. Implement canonical schema in DuckDB or Postgres.
6. Add Open-Meteo weather enrichment.
7. Generate fixture context snapshots.
8. Run a first backtest with base model plus context.

Then run a provider coverage trial across 8-12 leagues before selecting paid xG/lineup/injury feeds.
