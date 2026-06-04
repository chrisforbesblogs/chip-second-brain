# Proposal: Scalable Statistical Model For Predicting League Sports Results

Date: 2026-05-24

## Goal

Build a practical model that predicts league match outcomes, starting with football but designed so it can extend to other league-based sports and regions:

- Home win / draw / away win probabilities
- Expected home and away goals
- Optional derived probabilities such as over/under 2.5 goals, both teams to score, and fair odds

The first version should prioritize reliability, explainability, and repeatable backtesting over complex machine learning. Soccer has low scoring, high draw frequency, and lots of randomness, so calibrated probabilities matter more than simply picking winners.

## Scalability Principle

The system should not be hard-coded as a football-only predictor. It should have a generic league-sport core, with sport-specific modules plugged in around it.

Generic core:

- Countries and regions
- Competitions/leagues
- Seasons
- Teams
- Fixtures/matches
- Results
- Venues/home advantage
- Ratings
- Features
- Predictions
- Backtests

Sport-specific modules:

- Scoring model
- Draw/no-draw rules
- Overtime/extra-time handling
- League table rules
- Promotion/relegation rules
- Market types
- Sport-specific features such as xG, shots, possessions, runs, wickets, sets, maps, penalties, or cards

For football, the first scoring module should be Poisson/Dixon-Coles. For other sports, the same platform can swap in a different outcome model:

- Basketball: possessions/points model, no draw, margin distribution
- Rugby: points model with home advantage and weather/context features
- Cricket: format-specific model for T20/ODI/Test, using innings and venue features
- Baseball: run distribution and starting pitcher features
- Hockey: low-scoring goal model similar to football, but with overtime/shootout handling
- Esports league matches: map-level model with team ratings, side advantage, patch/version, and best-of format

This means the data pipeline and backtesting engine stay reusable while each sport gets its own modelling assumptions.

## Recommended Modelling Approach

The research update changes the recommendation from "pick a model" to "build a layered probability engine". The strongest practical design combines:

- Dynamic team-strength ratings for broad quality.
- A football-specific score model for expected goals and draws.
- Bayesian/hierarchical priors for cross-league and early-season uncertainty.
- xG, player and context features where data is reliable.
- A calibrated ML layer only after the statistical foundation is stable.
- Betting-market comparison as a benchmark and optional feature, with bookmaker margin removed.

David Sumpter's *Soccermatics* perspective is useful here: football has substantial randomness, so the model should estimate honest probabilities rather than pretend to know the winner. The workflow should be team strength -> expected goals -> scoreline probabilities -> outcome probabilities -> calibration testing.

### 1. Baseline: Elo Plus Home Advantage

Start with an Elo-style team strength model:

- Each team has a rating.
- Ratings update after every match.
- The expected result is adjusted for home advantage.
- Goal difference can scale rating movement, but should be capped to avoid overreacting to one-off thrashings.

This gives a strong, simple benchmark and works well with only historical results.

Useful features:

- Team Elo before match
- Elo difference
- Home advantage
- Recent form, calculated from pre-match data only
- Rest days
- Promotion/relegation flag, if available
- Market implied probability from betting odds, if used

Output:

- 1X2 outcome probabilities via logistic or multinomial logistic regression on Elo difference and context features

Why use it:

- Easy to backtest
- Hard to overfit
- Good benchmark for more advanced models

### 2. Core Statistical Model: Poisson Goals Model

The main model should estimate goals directly:

```text
Home goals ~ Poisson(home_attack_strength, away_defence_strength, home_advantage)
Away goals ~ Poisson(away_attack_strength, home_defence_strength)
```

From the predicted home and away goal distributions, we can calculate:

- Home/draw/away probabilities
- Correct score probabilities
- Over/under totals
- Both teams to score

Important refinements:

- Use attack and defence ratings per team.
- Apply time decay so recent matches matter more than old matches.
- Include promoted teams with priors from their previous division instead of treating them as unknown.
- Add league-level scoring rates, because a 1.4 xG/team league and a 1.1 xG/team league behave differently.

### 3. Improved Statistical Model: Dixon-Coles

The Dixon-Coles model is a better version of the Poisson model for football because it corrects for low-score dependence, especially:

- 0-0
- 1-0
- 0-1
- 1-1

This matters because independent Poisson models often misprice draws.

Recommendation:

- Use Dixon-Coles as the first serious production model.
- Keep Elo as the benchmark.
- Compare both against bookmaker closing odds where available.

### 4. Bayesian Hierarchical Model

Once the basic pipeline works, move to a Bayesian version:

- Team attack/defence strengths are parameters with priors.
- League strength and season effects can be modelled hierarchically.
- Newly promoted teams can inherit a reasonable prior rather than starting from scratch.
- Uncertainty intervals become available, which is useful early in a season.

This is stronger but more complex. It should be phase two, not the first build.

### 5. Machine Learning Layer

After the statistical models are stable, add ML as a second layer:

- Gradient boosting, such as LightGBM or XGBoost
- Regularized multinomial logistic regression
- Random forest only as a comparison, not the main model

Inputs should include:

- Elo features
- Poisson/Dixon-Coles expected goals
- Recent rolling team metrics
- Schedule congestion
- Odds-implied probabilities
- Injury/suspension indicators if a reliable source is found
- xG trend features where available

The ML layer should not replace the statistical model initially. It should learn residual patterns on top of strong model outputs.

### 6. Challenger Models And Research Path

Once the baseline is working, test challenger models:

- Bivariate Poisson for correlated team scores.
- Diagonal-inflated or Sarmanov-family extensions for better draw/low-score calibration.
- Negative binomial or overdispersed goal models where simple Poisson underfits variance.
- Multinomial-Dirichlet outcome models for direct 1X2 probability prediction.
- Dolores-style dynamic ratings plus Bayesian network features for multi-country scaling.
- Player-rating models where reliable lineup/player data exists.

These should be evaluated with proper scoring rules, not just accuracy. A challenger only replaces the production model if it improves log loss, Brier score and calibration on time-based backtests.

### Recommended Model Ranking

For football probability accuracy, the research points to this ordering:

1. Market-calibrated hierarchical Dixon-Coles / bivariate Poisson ensemble.
2. Bayesian hierarchical Dixon-Coles with dynamic attack/defence ratings.
3. Dixon-Coles with time decay and league-specific calibration.
4. Independent Poisson attack/defence model.
5. Elo plus multinomial logistic calibration.
6. Simple rolling-form or league-table models.

For scalable league sports generally:

1. Sport-specific scoring model plus dynamic ratings plus calibration.
2. Bayesian hierarchical ratings shared across countries/leagues.
3. ML ensemble on top of statistical model outputs.
4. Pure Elo baseline.
5. Generic classifier without sport-specific scoring assumptions.

## Data Sources

### Primary Free Sources

1. Football-Data.co.uk

Best for:

- Historical match results
- Betting odds
- Basic match stats for many leagues
- CSV downloads suitable for modelling

Use this as the MVP data backbone. It is especially useful because odds allow us to benchmark against the market.

Source notes:

- Football-Data describes itself as a free football betting portal with historical results and odds.
- It provides computer-ready Excel/CSV files for quantitative analysis.

Source: https://www.football-data.co.uk/

2. football-data.org

Best for:

- Fixtures
- Schedules
- Results
- Standings
- API access

Use this for a live-ish application layer, fixture updates, and current season structure.

Source notes:

- The free tier includes major competitions such as Premier League, Championship, Bundesliga, Ligue 1, Serie A, La Liga, Eredivisie, Primeira Liga, Champions League, Brazil Serie A, World Cup, and European Championships.

Source: https://www.football-data.org/coverage

3. StatsBomb Open Data

Best for:

- Event-level data
- Lineups
- Some 360 freeze-frame data
- Research-grade feature engineering

Use this to prototype advanced ideas like shot quality, possession value, pressing, and xG-style features. Do not use it as the main league-prediction backbone because open coverage is selective rather than complete across all current league seasons.

Source notes:

- StatsBomb provides free open data for public research and football analytics.
- The repository includes competitions, matches, events, lineups, and selected 360 data.

Source: https://github.com/statsbomb/open-data

4. openfootball / football.json

Best for:

- Public domain fixtures and results
- No API key
- JSON format

Use this as a fallback/secondary source for fixtures and historical results, or for lightweight demos.

Source notes:

- The project provides public domain football data in JSON, with leagues including Premier League, Championship, Bundesliga, La Liga, Serie A, Ligue 1, and others.

Source: https://github.com/openfootball/football.json

5. ClubElo

Best for:

- Pre-existing club strength ratings
- Feature seeding
- Benchmarking our own Elo ratings

Use ClubElo as an external rating feature or sanity check. It can be accessed via the soccerdata Python package, which documents a CSV API at `http://api.clubelo.com`.

Source: https://soccerdata.readthedocs.io/

### Secondary / Cautious Sources

- Understat: useful for xG on major European leagues, but scraping/terms should be checked before relying on it operationally.
- FBref: historically useful, but advanced free data availability has changed. Treat as non-core unless terms and current availability are confirmed.
- Kaggle datasets: good for historical experiments, but often stale, inconsistently licensed, or not suitable for automated production updates.
- API-Football / SportMonks / FootyStats / similar: usually useful, but free tiers may be limited. Consider later if the project needs injuries, lineups, player stats, or broader competition coverage.

## Advanced Feature Data Strategy

The base model should work from fixtures, results, standings, odds and team ratings. The next layer should add xG, player and context features through a tiered data strategy, because coverage will vary heavily across Europe, Asia and lower-tier leagues.

### Feature Tiers

Tier 1: broad context, available for nearly every league

- Fixtures
- Results
- Standings
- Home/away/neutral venue
- Rest days
- Fixture congestion
- Travel-distance proxy
- Venue and weather
- Table pressure
- Season phase

Tier 2: player and lineup layer, available where provider coverage exists

- Confirmed starting XI
- Substitutes
- Formation
- Player minutes
- Injuries
- Suspensions
- Doubtful status
- Missing-starter count
- Missing-minutes share
- Lineup continuity

Tier 3: xG and event/chance-quality layer, available only in rich leagues

- Team xG for and against
- Non-penalty xG
- Shot count
- Shots on target
- xG per shot
- Big chances
- Player xG/xA
- Post-shot xG
- Set-piece xG
- Game-state xG

Every feature should carry:

- `source_provider`
- `observed_at`
- `snapshot_at`
- `effective_for_fixture_id`
- `confidence`
- `is_missing_reason`

This lets the model degrade gracefully instead of pretending sparse leagues have the same data quality as the Premier League.

### Regular Data Sources To Test

MVP provider candidates:

- Sportmonks: broad football API with fixtures, lineups, injuries/sidelined players, expected lineups, xG endpoints and odds add-ons. Needs league-by-league validation.
- API-Football: broad and affordable football API with fixtures, lineups, injuries, odds and coverage flags. Needs ID-quality and completeness testing.
- TheStatsAPI: developer-friendly provider claiming xG/npxG/xA, player stats, match stats, odds and historical data. Needs validation because it is newer/smaller.
- SportsDataIO: mature multi-sport provider, useful if the platform expands beyond football. Soccer depth and cost need verification.
- Open-Meteo: strong default for global weather forecast and historical weather enrichment.

Enterprise/later candidates:

- Stats Perform / Opta
- StatsBomb paid API
- Wyscout
- Sportradar / IMG Arena
- TXODDS or another premium odds feed
- RotoWire or specialist injury/news syndication

Prototype/research-only sources:

- StatsBomb Open Data
- football-data.co.uk
- football-data.org
- soccerdata / socceraction loaders
- manually curated derby, venue and manager datasets

Avoid as production dependencies without legal review:

- Scraping Transfermarkt, Sofascore, FotMob, Flashscore, Understat, FBref, club pages or social feeds.

### Ingestion Architecture

The ingestion pipeline should separate raw data, normalized entities, feature snapshots and model-ready vectors:

```text
provider APIs/news/weather
  -> provider adapters
  -> raw payload store
  -> canonical normalization
  -> entity resolution
  -> feature snapshots
  -> offline/online feature store
  -> model feature vectors
```

Key rules:

- Store raw provider payloads unchanged for auditability.
- Maintain provider ID mapping tables for teams, players, venues, competitions and fixtures.
- Build feature snapshots at prediction times such as T-7d, T-48h, T-24h, T-6h, T-1h and lineup-confirmed.
- Never use actual post-match data in a pre-match backtest unless that data would really have been available at prediction time.
- Encode missingness explicitly instead of filling unknown injuries/xG with fake defaults.
- Track provider freshness, coverage, missing-field rates, outliers and cross-provider conflicts.

### Recommended MVP Feature Tables

- `fixture_context_snapshot`
- `fixture_weather_snapshot`
- `team_chance_quality_snapshot`
- `fixture_lineup_snapshot`
- `player_availability_snapshot`
- `team_staff_transfer_snapshot`

These should feed into the model as time-aware snapshots, not mutable latest-state records.

### Sparse-League Strategy

For Asia and smaller European leagues, classify each competition by feature coverage:

- Tier A: xG/event data, lineups, injuries, player stats and odds. Use full model.
- Tier B: match stats, lineups, odds and limited injuries. Use stats proxies, lineup continuity and context.
- Tier C: fixtures, results, standings and odds. Use team-strength, market baseline, rest, travel and table pressure.
- Tier D: fixtures/results only. Use conservative team-strength model with strong shrinkage and wider uncertainty.

Every prediction should output:

- `feature_coverage_tier`
- `probability_confidence`
- `missing_feature_summary`

This is important because a 56% home-win probability from rich Premier League data is not the same as a 56% home-win probability from fixtures/results-only coverage in a lower-data league.

## Proposed Scalable Data Schema

Core tables:

- `sports`
  - sport_id
  - sport_name
  - scoring_type
  - allows_draw
  - default_model_family

- `countries`
  - country_id
  - country_name
  - region
  - timezone

- `competitions`
  - competition_id
  - sport_id
  - country_id
  - competition_name
  - tier
  - governing_body

- `matches`
  - match_id
  - sport_id
  - country_id
  - competition_id
  - date
  - season
  - league
  - home_team
  - away_team
  - home_goals
  - away_goals
  - status
  - neutral_venue
  - source_provider

- `odds`
  - match_id
  - market_type
  - bookmaker
  - home_odds
  - draw_odds
  - away_odds
  - closing_flag

- `team_ratings`
  - sport_id
  - team
  - league
  - date
  - elo
  - attack_rating
  - defence_rating

- `features`
  - match_id
  - model_family
  - elo_diff
  - home_form_points
  - away_form_points
  - home_goals_for_rolling
  - away_goals_for_rolling
  - home_goals_against_rolling
  - away_goals_against_rolling
  - rest_days_home
  - rest_days_away
  - market_home_prob
  - market_draw_prob
  - market_away_prob

- `predictions`
  - match_id
  - model_version
  - sport_id
  - model_family
  - predicted_home_goals
  - predicted_away_goals
  - home_win_prob
  - draw_prob
  - away_win_prob
  - created_at

- `provider_mappings`
  - provider
  - provider_entity_id
  - internal_entity_type
  - internal_entity_id
  - provider_name
  - normalized_name

For football, columns like `home_goals` and `away_goals` are natural. In the implementation, these should be generalized internally as home/away scores, with sport-specific aliases used at the presentation layer.

## Evaluation

Use time-based backtesting only. Never randomly split matches, because that leaks future team strength into the past.

Metrics:

- Log loss for 1X2 probabilities
- Brier score
- Calibration curves
- Ranked probability score
- Mean absolute error for expected goals
- Return-on-investment simulation only as a secondary measure

Benchmarks:

- Home-team naive baseline
- League-average home/draw/away probabilities
- Elo-only model
- Bookmaker implied probabilities, where odds are available

The model is only useful if it is calibrated. A model that says a team has a 60% chance should win about 60% of those games over a large sample. This applies across sports, even when the scoring model changes.

## Implementation Plan

### Phase 1: Data And Baselines

Build:

- Importer for Football-Data.co.uk CSVs
- Normalized sport/country/competition/team/match tables
- Provider mapping layer for team and competition names
- Elo rating engine
- Baseline 1X2 probability model
- Backtest runner
- Simple report of performance versus bookmaker odds

Expected output:

- Reliable baseline model
- Historical evaluation by league and season

### Phase 2: Goals Model

Build:

- Independent Poisson model
- Dixon-Coles adjustment
- Time decay weighting
- Home advantage per league
- Correct-score and totals probabilities
- Sport model interface so football-specific scoring logic is isolated

Expected output:

- Better draw calibration
- Expected goals per team
- More useful derived betting/forecast markets

### Phase 3: Feature Expansion

Add:

- ClubElo ratings
- Rest days and congestion
- Rolling xG where trustworthy data exists
- Squad/injury features only if source quality is good
- Promoted/relegated team adjustment

Expected output:

- Stronger pre-match forecasts
- Better early-season handling

### Phase 4: ML Ensemble

Build:

- Feature store
- LightGBM/XGBoost model
- Calibration layer
- Model comparison dashboard

Expected output:

- Ensemble that combines statistical model outputs, ratings, market information, and context features

## Recommended First Build

I would start with:

1. Football-Data.co.uk as the historical data source.
2. Premier League plus Championship as the first competitions.
3. A generic data model that includes sport, country, competition, season, team, match, provider, and prediction entities.
4. Elo baseline.
5. Dixon-Coles model as the first football-specific scoring module.
6. Time-decay weighting so recent results matter more.
7. League-specific home advantage and low-score/draw calibration.
8. Backtest from at least 2015-16 onwards.
9. Compare against closing odds where available.
10. Keep a challenger-model framework ready for Bayesian, bivariate Poisson and ML ensemble experiments.

This gives a serious model quickly without depending on fragile scraping or paid data. Once the model can beat simple baselines and produce calibrated probabilities, we can decide whether richer data is worth the extra complexity.

The first implementation should be football, but the repo/package layout should make the extension path explicit:

```text
core/
  data model
  provider ingestion
  team normalization
  ratings
  backtesting
  calibration

sports/
  football/
    poisson.py
    dixon_coles.py
    football_features.py
  basketball/
    placeholder for points/margin model
  rugby/
    placeholder for points model
```

That keeps the football MVP focused while avoiding a rewrite when adding Asian leagues, European leagues, or another league-based sport.

## Practical Notes

- Treat betting odds as both a benchmark and a feature. The market is extremely strong, so beating it directly is hard, but odds are excellent for model calibration checks.
- Avoid using post-match data accidentally. Rolling features must be computed only from matches before the fixture being predicted.
- Keep team-name mapping explicit. Football datasets often use inconsistent names.
- Store raw source files unchanged, then transform into normalized tables.
- Version every model run so predictions can be audited later.
- Position the product as calibrated probability infrastructure, not a betting tips product. The strongest wedge is explainable, audited probabilities for underserved leagues across Asia and second-tier Europe.
- Run a 2-4 week modelling spike across 8-12 leagues before choosing any paid data provider.
- Run a provider coverage test across at least 10 target Europe/Asia leagues before committing to xG, lineup or injury feeds.

## Suggested Stack

- Python
- pandas / polars for data processing
- DuckDB or SQLite for local storage
- scipy / statsmodels for Poisson and Dixon-Coles
- scikit-learn for calibration and baselines
- LightGBM or XGBoost later
- matplotlib / plotly for evaluation charts

## Final Recommendation

The best starting point is not a black-box ML model. It is a transparent statistical forecasting system that can later become a calibrated ensemble:

```text
Football-Data CSVs
  -> normalized sport/country/competition/match database
  -> dynamic Elo/team-strength ratings
  -> football Dixon-Coles goal model with time decay
  -> league-specific calibration
  -> backtest against closing odds
  -> challenger models: Bayesian, bivariate Poisson, ML ensemble
```

That gives us a solid football foundation while keeping the platform general enough for Asia, Europe, and other league-based sports. After that, add ClubElo, rest days, rolling xG, lineups, injuries, Bayesian hierarchy and an ML ensemble only where the data quality justifies it. For each new sport, reuse the core data/backtesting/calibration pipeline and add only the sport-specific scoring model and features.

## Research Sources Added

- ChipThink second-opinion report: `chipthink-scalable-sports-prediction-platform-research-2026-05-24.md`
- ChipThink feature-data report: `chipthink-sports-prediction-feature-data-layers-2026-05-24.md`
- Soccermatics prediction lesson: https://soccermatics.readthedocs.io/en/latest/lesson5/Prediction.html
- Dixon & Coles paper page: https://www.research.lancs.ac.uk/portal/en/publications/modelling-association-football-scores-and-inefficiencies-in-the-football-betting-market%28d16276a2-d6e0-483b-a708-1d29663f1992%29.html
- Dolores multi-country model: https://link.springer.com/article/10.1007/s10994-018-5703-7
- Player-rating forecasting model: https://www.sciencedirect.com/science/article/pii/S016920702300033X
- Comparing probabilistic predictive models: https://arxiv.org/abs/1705.04356
- Extending Dixon-Coles: https://arxiv.org/abs/2307.02139
- Dixon-Coles time weighting discussion: https://opisthokonta.net/?cat=48
- Market-calibrated in-play forecasting: https://arxiv.org/abs/2605.16066
