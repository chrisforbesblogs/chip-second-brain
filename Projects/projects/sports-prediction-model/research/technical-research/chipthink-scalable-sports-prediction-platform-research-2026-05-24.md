# Scalable Sports Prediction Platform Research

Date: 2026-05-24  
Prepared by: ChipThink  
Scope: league-based sports prediction platform, starting with football/soccer and designed to scale across Asia, Europe, and later other league sports.

## Executive Summary

The strongest product direction is a calibrated probability engine, not a "tips" app. Start with football pre-match probabilities for 1X2, exact score distribution, totals, BTTS, Asian handicap-derived lines, and season simulations. Build around transparent team-strength models inspired by David Sumpter/Soccermatics and Dixon-Coles, then add xG, market priors, and calibration layers only where they demonstrably improve proper scoring-rule performance.

Recommended MVP:

1. Cover 8-12 leagues with mixed profiles: England/Spain/Germany/Italy/France top leagues, Championship, Japan J1/J2, Korea K League 1, Saudi Pro League, and one lower-data Asian league.
2. Ship a model benchmark dashboard before shipping public predictions: log loss, Brier score, ranked probability score, calibration plots, closing-line comparison, coverage health, and league-level confidence.
3. Use an interpretable baseline as the product's foundation: dynamic attack/defence strengths, home advantage, league effects, time decay, promotion/relegation priors, and optional xG enhancement.
4. Treat bookmaker odds as a calibration benchmark and optional prior, not the whole product. If the model cannot beat a de-vigged closing market on calibration or log loss in major leagues, the product should focus on transparency, niche-league coverage, simulations, and developer API use cases rather than claiming sharper-than-market forecasts.

The key commercial wedge is "calibrated, explainable probabilities for underserved leagues and sports", especially Asian and second-tier competitions where mainstream public models are weaker and data coverage is fragmented.

## Assumptions

- The platform aims to provide probabilities and analytics, not regulated betting execution.
- First product is pre-match football. In-play is explicitly out of MVP unless a reliable low-latency event and odds feed is already licensed.
- Accuracy means calibrated probabilities under proper scoring rules, not headline hit rate.
- The business may later offer B2B API/data feeds, B2C dashboards, or white-label widgets.

## Target Users

### Primary MVP Users

- Sports analytics builders needing reliable football probabilities through an API.
- Media/content operators needing explainable match probabilities and simulations.
- Serious football analysts who care about model calibration, not only "picks".
- Sportsbook-adjacent tools that need fair prices, market comparison, and transparent methodology.

### Secondary Users

- Clubs, agents, and scouts, if the product later includes team/player performance layers.
- Fantasy and prediction-game operators.
- Fans who want probabilities and league simulations without betting framing.

## Market And Competitor Notes

### Data And Prediction API Landscape

- Sportmonks advertises football API plans covering 2,300+ leagues, flexible league selection, and prediction/xG add-ons. Its public docs describe prediction endpoints for winner, correct score, over/under and BTTS, plus value-bet detection and league-level model performance endpoints. Sources: [Sportmonks pricing](https://www.sportmonks.com/football-api/plans-pricing/), [Sportmonks prediction docs](https://docs.sportmonks.com/v3/endpoints-and-entities/endpoints/predictions).
- football-data.org is useful for lower-cost fixture, score, table, lineup, and odds add-on coverage. Current public pricing ranges from free to paid tiers with competition limits and request-rate limits, plus odds/statistics add-ons. Source: [football-data.org pricing](https://www.football-data.org/pricing).
- The Odds API provides bookmaker odds, soccer coverage across major competitions, and historical snapshots back to 2020. Source: [The Odds API](https://the-odds-api.com/).
- TheStatsAPI positions itself around developer-friendly football stats, xG, odds, 80 default competitions and up to 1,196 on request, with major-league history going back 10 years and live/pre-match odds from named books where available. Source: [TheStatsAPI coverage](https://www.thestatsapi.com/coverage).
- SportsDataIO lists broad soccer coverage including Asian leagues such as India Super League, Indonesia Liga 1, Japan J1/J2/J3, Korea K League, Malaysia Super League, and Thailand Thai Premier League. Source: [SportsDataIO soccer API](https://sportsdata.io/soccer-api).
- StatsBomb Open Data is high-quality event data for research and model prototyping, but only covers selected competitions and comes with attribution/licence terms. Source: [StatsBomb Open Data](https://github.com/statsbomb/open-data).

### Product Gap

Most competitors sell data breadth, predictions, or betting content. Fewer make calibration, uncertainty, model transparency, and cross-league reliability the core product. That is the opening.

Position the product as:

> A calibrated probability and simulation engine for football and league sports, with transparent model diagnostics and reliable coverage for leagues the mainstream public models treat as afterthoughts.

## Modelling Approaches

### 1. Soccermatics-Style Poisson Team-Strength Model

David Sumpter's Soccermatics teaching material uses the Poisson distribution to predict football scores and model team performance. Source: [Soccermatics prediction lesson](https://soccermatics.readthedocs.io/en/latest/lesson5/Prediction.html).

Use this as the educational/product explanation layer:

- Estimate expected goals for home and away teams.
- Convert those expected goals into a scoreline matrix.
- Sum scoreline cells into 1X2, totals, BTTS, handicap, and exact-score probabilities.
- Explain predictions via attack strength, defence strength, home advantage, recent form, and league scoring environment.

This is not enough on its own for a production platform, but it is the right mental model for users.

### 2. Dixon-Coles Dynamic Score Model

Dixon and Coles' 1997 paper is still a reference point in football score modelling. It improves the basic independent Poisson model by adjusting dependence in low-score outcomes and weighting recent matches more heavily. Source: [Lancaster University publication record](https://research.lancaster-university.uk/?en/publications/modelling-association-football-scores-and-inefficiencies-in-the-football-betting-market(d16276a2-d6e0-483b-a708-1d29663f1992).html).

Use as the MVP baseline:

- Attack parameter per team.
- Defence parameter per team.
- Home advantage.
- Low-score correction for 0-0, 1-0, 0-1, 1-1.
- Exponential time decay.
- League-level scoring intercepts.

Why it fits:

- Transparent and explainable.
- Data-efficient for leagues without detailed event data.
- Naturally produces full score distributions.
- Easy to extend to other low-scoring sports.

### 3. Hierarchical Bayesian Team-Strength Model

Use Bayesian partial pooling when scaling across leagues:

- Team attack/defence strengths shrink toward league averages when data is sparse.
- Promoted teams inherit priors from their previous league, adjusted by historical promotion/relegation transitions.
- New leagues can start with league-level priors rather than unstable team-only estimates.
- Asian leagues with less historical depth benefit from shrinkage instead of overfitting.

Recommended parameter hierarchy:

- Global football scoring prior.
- Region prior: Europe, East Asia, West Asia, Americas, etc.
- League prior: mean goals, home advantage, draw tendency, volatility.
- Team priors: attack, defence, tempo.
- Season effects: manager change, promotion, squad turnover proxy.

Implementation options:

- MVP: penalised maximum likelihood / MAP estimation with time decay.
- Research: PyMC, Stan, NumPyro, or Turing-style Bayesian posterior sampling for uncertainty.
- Production: use approximate inference or scheduled posterior updates; do not rely on slow MCMC in live request paths.

### 4. xG-Enhanced Model

xG is useful because chance quality is more stable than finishing over short windows. However, xG coverage is uneven across global leagues and vendor definitions differ.

Use xG in tiers:

- Tier A leagues: event/xG available; model expected goals using xG for/against, non-penalty xG, shots, shot quality, xG allowed.
- Tier B leagues: match stats available; proxy xG using shots, shots on target, corners, possession, dangerous attacks if vendor quality is acceptable.
- Tier C leagues: results-only; use score-based Dixon-Coles/Bayesian team strength.

Do not make xG mandatory for the platform. The scalable architecture should degrade gracefully to results-only modelling.

### 5. Market-Calibrated Layer

Bookmaker odds are extremely strong aggregated forecasts, especially closing lines in liquid leagues. Use them in three different ways:

- Baseline: compare the model to de-vigged closing odds.
- Feature/prior: blend market-implied probabilities with model probabilities for high-liquidity leagues.
- Product feature: show model-vs-market differences, but avoid making ROI claims without robust evidence.

A recent in-play football paper also supports the practical point that market calibration can dominate predictive accuracy when live markets are available. Source: [market-calibrated in-play football model, arXiv](https://arxiv.org/abs/2605.16066).

Recommendation:

- Pre-match MVP should maintain both "pure model" and "market-informed" probability tracks.
- Public/API consumers should be able to request `model_only`, `market_only`, and `calibrated_blend` outputs.
- Claims of model edge should be league-specific and measured against closing odds, not opening odds.

### 6. Machine Learning Ensemble

Use gradient boosting or neural networks only after the statistical baseline is working and benchmarked.

Candidate features:

- Team Elo/SPI-style rating.
- Attack/defence strengths.
- Recent xG for/against.
- Rest days and travel distance.
- Home/away splits.
- Schedule congestion.
- Missing players or lineup strength if licensed.
- Market movement if odds are licensed.
- Manager change and promoted/relegated status.

Candidate models:

- Multinomial logistic regression as calibrated baseline.
- LightGBM/CatBoost for tabular features.
- Bayesian additive models where interpretability matters.
- Ensemble with isotonic/temperature calibration by league.

Guardrail:

- ML models must beat the transparent baseline out-of-sample by league and season under log loss/Brier/RPS. If they only improve accuracy but worsen calibration, they should not ship as default probabilities.

## Recommended Model Stack

### MVP Model Stack

1. `ScoreModelV1`: Dixon-Coles style model with team attack/defence, home advantage, time decay, low-score correction.
2. `RatingModelV1`: Elo/SPI-style rating used as a prior and sanity check, especially for newly promoted teams and cross-league comparisons.
3. `LeaguePriorV1`: league-specific scoring, draw tendency, home advantage, and volatility priors.
4. `CalibrationV1`: post-hoc calibration by league/market using rolling validation windows.
5. `MarketBaselineV1`: de-vig bookmaker-implied probabilities for evaluation and optional blending.
6. `SimulationV1`: Monte Carlo league-table, promotion/relegation, title, top-four, and tournament-path probabilities.

### Later Model Stack

1. `XGModelV2`: chance-quality model where event data exists.
2. `PlayerAvailabilityV2`: lineup, injury, suspension, and minutes projections.
3. `CrossLeagueTransferV2`: adjusts team priors after promotion/relegation and continental competitions.
4. `InPlayModelV3`: event-clock model driven by score, cards, substitutions, xG/live pressure, and live odds.
5. `MultiSportAdapterV3`: sport-specific scoring distribution and state model for basketball, cricket, rugby, baseball, hockey, etc.

## Data Source Strategy

### Required MVP Data

- Fixtures and results.
- Team identity, league, season, venue/home/away.
- Match date/time and status.
- Closing and opening odds where available.
- League tables and promotion/relegation metadata.
- Basic match stats if available: shots, shots on target, corners, cards, possession.

### Useful But Not Mandatory

- Event data.
- xG and xG allowed.
- Lineups, substitutions, injuries, suspensions.
- Player minutes and squad quality proxies.
- Travel distance and rest days.
- Weather for selected leagues if predictive signal is later proven.

### Suggested Data Provider Path

Phase 1:

- Use football-data.co.uk / football-data.org / StatsBomb Open Data for prototypes and baseline backtests.
- Add one paid API with strong Asian and European coverage for production ingestion tests.
- Add odds feed: The Odds API or provider included in chosen sports-data package.

Phase 2:

- Negotiate vendor rights for storage, redistribution, derived predictions, and historical backfills.
- Add second provider for redundancy and identity-resolution cross-checks.
- Build provider abstraction so leagues can move provider without rewriting models.

Phase 3:

- License advanced event/xG data for high-value leagues only.
- Keep lower-data leagues on results/statistics models.

### Provider Evaluation Criteria

Score vendors on:

- Coverage for target leagues, not headline global count.
- Historical depth per league.
- Fixture ID stability.
- Team/player ID stability across seasons and competitions.
- Odds markets and bookmaker coverage.
- Opening/closing timestamp availability.
- xG availability and definition consistency.
- Update latency.
- Redistribution rights for derived probabilities.
- Cost per covered league and cost per API call.
- SLA and support quality.

## Architecture Recommendation

### Core Services

1. Data ingestion service
   - Pulls fixtures, results, odds, stats, xG, lineups.
   - Supports provider adapters.
   - Stores raw payloads unchanged for audit.

2. Canonical sports data store
   - Normalised entities: sport, region, competition, season, team, player, fixture, market, odds snapshot.
   - Uses internal stable IDs independent of vendors.
   - Maintains mapping tables per provider.

3. Feature store
   - Rolling team features, league priors, xG aggregates, rest/travel, odds-implied probabilities.
   - Time-aware features only; no future leakage.

4. Model training pipeline
   - Scheduled daily or per league.
   - Walk-forward validation.
   - Stores model artefacts, parameters, feature definitions, training window, validation scores.

5. Prediction service
   - Generates pre-match probabilities for fixtures.
   - Returns versioned probability outputs and explanations.
   - Supports cached API responses.

6. Evaluation and monitoring service
   - Tracks calibration, proper scoring rules, provider health, model drift, league-specific degradation.
   - Compares against closing market and naive baselines.

7. Simulation service
   - Runs match, season, tournament, and promotion/relegation simulations.
   - Can power B2C dashboards and B2B APIs.

### Data Storage

Recommended:

- PostgreSQL for canonical relational sports data.
- TimescaleDB or partitioned Postgres tables for odds snapshots and event timelines.
- Object storage for raw vendor payloads and training snapshots.
- DuckDB/Parquet for offline research and backtesting.
- Redis for cached upcoming fixture predictions.

### API Surface

Minimum endpoints:

- `GET /sports`
- `GET /competitions`
- `GET /fixtures?competition=&date=`
- `GET /fixtures/{id}/probabilities`
- `GET /fixtures/{id}/score-distribution`
- `GET /fixtures/{id}/explanation`
- `GET /competitions/{id}/simulation`
- `GET /models/{version}/performance`
- `GET /competitions/{id}/calibration`

Probability response should include:

- Fixture metadata.
- Model version.
- Generated timestamp.
- Market availability.
- 1X2 probabilities.
- Expected goals home/away.
- Scoreline matrix or top N scores.
- Totals probabilities.
- BTTS.
- Handicap probabilities.
- Confidence/coverage tier.
- Key drivers.
- Calibration disclaimer.

## Evaluation Framework

### Metrics

Use proper scoring rules. The scoringrules documentation gives the formal reason: a proper scoring rule is minimised in expectation by the true outcome distribution and discourages hedged or dishonest probabilities. Source: [scoringrules theory](https://scoringrules.readthedocs.io/en/latest/theory.html).

Core metrics:

- Log loss for 1X2 and binary markets.
- Brier score for 1X2, totals, BTTS, handicap.
- Ranked probability score for ordered score-margin or outcome categories.
- Calibration curves by probability bucket.
- Expected calibration error, but do not rely on it alone.
- Sharpness/resolution: whether forecasts move away from base rates for good reasons.
- Coverage: percentage of fixtures with usable predictions.
- League-level scorecards, not only global averages.

Baselines:

- Home/draw/away league base-rate model.
- Elo-only model.
- Independent Poisson.
- Dixon-Coles.
- De-vigged opening odds.
- De-vigged closing odds.

### Validation Design

- Use walk-forward validation by match date.
- Split by season and league; never random-split matches.
- Freeze feature windows at prediction time to avoid leakage.
- Evaluate promoted teams separately.
- Evaluate sparse leagues separately.
- Track model performance before and after adding odds as a feature.

### Calibration Standards

Minimum launch gate:

- Reliability plots do not show systematic overconfidence above 60% probability.
- Log loss and Brier beat naive league base-rate and independent Poisson baselines.
- Dixon-Coles baseline performance is visible to users/admins.
- Major-league market-informed model should be close to closing odds; pure model does not need to beat closing odds to be useful, but the product must be honest.
- For undercovered leagues, compare against opening odds and late odds where closing markets are weak or unavailable.

## Product MVP

### MVP Promise

"Transparent, calibrated football probabilities and simulations across selected European and Asian leagues, with model diagnostics you can audit."

### MVP Features

1. Upcoming-match probability API.
2. Web dashboard for fixtures and model explanations.
3. League simulation dashboard.
4. Model performance dashboard by league and model version.
5. Data coverage dashboard.
6. Admin review tool for provider mismatches and fixture mapping.
7. CSV/API export for analysts.

### MVP Markets

- Match result: home/draw/away.
- Exact score distribution.
- Over/under 1.5, 2.5, 3.5.
- Both teams to score.
- Asian handicap probabilities where score distribution supports them.
- Season table simulations.

### MVP League Mix

Choose leagues to stress-test different conditions:

- High-liquidity, high-data Europe: EPL, La Liga, Bundesliga, Serie A, Ligue 1.
- Second-tier Europe: EFL Championship or Eredivisie/Portugal.
- Strong Asian leagues: Japan J1, Korea K League 1, Saudi Pro League.
- Lower-data Asian league: Thailand, Malaysia, Indonesia, or India depending on provider quality.

Why this mix:

- Major European leagues validate against strong market baselines.
- Asian leagues test the strategic differentiation.
- Lower-data leagues force the architecture to handle sparse data and provider variation.

## Roadmap

### Phase 0: Research Prototype - 2-4 Weeks

- Ingest historical results for 10 leagues.
- Implement independent Poisson, Dixon-Coles, Elo, and baseline market models.
- Build walk-forward evaluation notebook/report.
- Decide first paid data provider.

Exit criteria:

- Reproducible backtest.
- League-level metrics.
- Clear evidence of data quality gaps.
- Chosen provider shortlist.

### Phase 1: MVP API And Dashboard - 6-10 Weeks

- Build canonical data model and ingestion adapters.
- Build `ScoreModelV1`, `RatingModelV1`, calibration, and prediction API.
- Add dashboard for upcoming fixtures, explanations, and performance.
- Add season simulation.

Exit criteria:

- Daily automated predictions.
- Admin-visible calibration and coverage health.
- At least 8 leagues live.
- Public methodology page.

### Phase 2: Differentiation - 8-12 Weeks

- Add xG-enhanced model for data-rich leagues.
- Add market-informed blended model.
- Add more Asian coverage.
- Add API keys, usage limits, billing, and customer docs.

Exit criteria:

- First paying B2B/API pilot.
- League-specific scorecards.
- Provider redundancy plan.

### Phase 3: Multi-Sport Expansion

Adapt the platform by sport:

- Basketball: possession/efficiency rating, score-margin distribution, player availability.
- Cricket: innings/resource-state model, venue, toss, batting/bowling strength.
- Rugby: Poisson/negative-binomial scoring components, home advantage, rest/travel.
- Baseball: pitcher/team run models, lineup, bullpen, park factors.
- Hockey: low-scoring Poisson/xG-style shot-quality model.

The core reusable layer is: entity model, fixtures, odds snapshots, feature store, model registry, scoring rules, calibration, simulation, API.

## Pricing And Business Model Options

### B2B API

Best first commercial path.

- Free/dev tier: limited leagues, delayed predictions, no historical bulk.
- Starter: selected leagues, upcoming probabilities, basic performance metrics.
- Pro: all MVP leagues, simulations, historical predictions, webhooks.
- Enterprise: custom leagues, white-label widgets, SLA, bulk exports, advanced odds integrations.

### B2C Analyst Dashboard

Secondary path.

- Free: limited fixture probabilities and methodology.
- Paid: advanced filters, simulations, exports, model-vs-market, historical model performance.

### Media/Widget Licensing

Useful if the product can provide visually clear probabilities.

- Embeddable match probability widget.
- League table simulation widget.
- API-backed editorial graphics.

## Risks

### Data Licensing Risk

Many sports-data vendors restrict storage, redistribution, or derived commercial outputs. This must be checked before building around a vendor.

Mitigation:

- Review contracts for derived-data rights.
- Store raw data only where permitted.
- Use provider abstraction.
- Keep open/prototype datasets separate from commercial product data.

### Calibration Risk

Models can look accurate by hit rate while being badly calibrated.

Mitigation:

- Make proper scoring rules and reliability plots first-class.
- Publish league-specific performance.
- Avoid "AI pick" framing.

### Market Efficiency Risk

For major football leagues, closing odds are very hard to beat.

Mitigation:

- Differentiate through transparency, simulations, underserved leagues, developer experience, and calibration tooling.
- Treat beating closing odds as an empirical result, not a brand promise.

### Sparse Data Risk

Asian and lower-tier leagues may have short histories, inconsistent IDs, and missing xG.

Mitigation:

- Hierarchical shrinkage.
- Coverage confidence tiers.
- Provider QA dashboard.
- Graceful downgrade to results-only models.

### Overfitting Risk

Football has low scoring and high variance. Complex models can overfit quickly.

Mitigation:

- Keep transparent baseline always available.
- Use walk-forward validation.
- Use league-level holdouts.
- Penalise models that improve in-sample but worsen calibration.

### Regulatory Risk

If positioned around betting, the product may trigger gambling-adjacent compliance questions.

Mitigation:

- Position as probabilities/analytics.
- Avoid bet placement, personalised staking, or guaranteed-profit claims.
- Add jurisdiction review before any consumer betting features.

## Validation Plan

### Technical Validation

- Build a historical backtest over 5+ seasons where available.
- Compare all models against closing odds where odds data exists.
- Produce league-level calibration charts.
- Test sparse-league performance separately.
- Run ablations: no odds, odds prior, xG added, Elo prior, time decay changes.

### Product Validation

Interview:

- 5 sports analytics developers.
- 5 football content/media operators.
- 5 betting-tool builders or serious analysts.
- 3 clubs/scouting analysts if performance layer is being considered.

Test willingness to pay for:

- API access.
- Historical predictions.
- Asian league coverage.
- Model transparency and performance pages.
- Widgets and simulations.

### Kill Criteria

Stop or pivot if:

- Data rights make commercial derived predictions uneconomic.
- The model cannot beat simple baselines outside one or two cherry-picked leagues.
- Target customers only want raw data already supplied by existing APIs.
- Asian league data quality is too inconsistent for credible probabilities at acceptable cost.
- Users value picks over calibrated probabilities and the team does not want betting-content risk.

## Strongest Recommendation

Build the MVP as a probability infrastructure product, not a consumer betting app. The defensible asset is a versioned, audited, calibrated prediction engine with league-level reliability, not a black-box "AI prediction" feed.

Immediate next step:

1. Run a 2-4 week modelling spike on 8-12 leagues using results and odds history.
2. Implement independent Poisson, Dixon-Coles, Elo, and market baselines.
3. Produce a league-by-league calibration report.
4. Choose the first paid data provider only after the spike exposes exactly which data fields and historical depth matter.

## Source Notes

Sources accessed 2026-05-24:

- Soccermatics prediction lesson: https://soccermatics.readthedocs.io/en/latest/lesson5/Prediction.html
- Dixon and Coles publication record: https://research.lancaster-university.uk/?en/publications/modelling-association-football-scores-and-inefficiencies-in-the-football-betting-market(d16276a2-d6e0-483b-a708-1d29663f1992).html
- StatsBomb Open Data: https://github.com/statsbomb/open-data
- Sportmonks football API pricing: https://www.sportmonks.com/football-api/plans-pricing/
- Sportmonks prediction docs: https://docs.sportmonks.com/v3/endpoints-and-entities/endpoints/predictions
- football-data.org pricing: https://www.football-data.org/pricing
- The Odds API: https://the-odds-api.com/
- TheStatsAPI coverage: https://www.thestatsapi.com/coverage
- SportsDataIO soccer API coverage: https://sportsdata.io/soccer-api
- scoringrules theory: https://scoringrules.readthedocs.io/en/latest/theory.html
- Market-calibrated in-play football model: https://arxiv.org/abs/2605.16066
- Comparing probabilistic predictive models applied to football: https://arxiv.org/abs/1705.04356
