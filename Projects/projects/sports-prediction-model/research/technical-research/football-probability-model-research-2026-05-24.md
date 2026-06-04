# Research Note: Best Modelling Approaches For Accurate Football Probabilities

Date: 2026-05-24

## Context

The user mentioned *Soccermatics* by David Sumpter. I am treating "David sumptuous" as David Sumpter, author of *Soccermatics*. This note does not reproduce the book. It summarizes the modelling ideas relevant to our project and compares them with current statistical and machine-learning approaches for predicting accurate football probabilities.

## Key Takeaway

There is no single "absolute best" football prediction model. The best practical system is an ensemble probability engine:

```text
dynamic team strength ratings
  + football score model
  + Bayesian uncertainty
  + xG / player / context features where reliable
  + market calibration
  + strict time-based backtesting
```

The goal should be accurate, calibrated probabilities, not winner-picking accuracy. A model that says 60% should win about 60% of the time across a large sample.

## What Sumpter / Soccermatics Contributes

Sumpter's publicly available Soccermatics course material emphasizes:

- Football outcomes contain substantial randomness.
- Goals can be modelled using Poisson-style assumptions.
- Re-simulating a league many times can show how much of the final table is driven by chance.
- Goal-based Poisson models are useful but imperfect.
- xG-based models can be better than raw goal models during a season because they capture underlying chance quality sooner.

This is directly useful for us because it supports a simulation-first view:

1. Estimate team attacking and defensive strength.
2. Convert strengths into expected goals.
3. Simulate scorelines or compute a score probability matrix.
4. Aggregate scorelines into outcome probabilities.
5. Evaluate calibration, not just hit rate.

Source: https://soccermatics.readthedocs.io/en/latest/lesson5/Prediction.html

## Candidate Model Families

### 1. Elo / Dynamic Ratings

Use case:

- Broad team strength
- New leagues with limited data
- Cross-country or cross-division modelling
- Baseline model

Strengths:

- Simple and robust
- Works with only match results
- Easy to update after every game
- Good for scalable multi-league architecture

Weaknesses:

- Does not naturally produce correct-score probabilities
- Can mishandle draws unless adapted
- Needs calibration to convert rating gaps into probabilities

Recommendation:

- Use Elo as the universal baseline across all league sports.
- For football, feed Elo difference into the expected goals model and/or an outcome calibration layer.

### 2. Maher / Independent Poisson Attack-Defence Model

Use case:

- First serious football score model
- Expected goals and scoreline probabilities

Core idea:

```text
home_goals ~ Poisson(home_attack_strength * away_defence_weakness * home_advantage)
away_goals ~ Poisson(away_attack_strength * home_defence_weakness)
```

Strengths:

- Explainable
- Produces full scoreline matrix
- Converts naturally into 1X2, totals, BTTS, correct score

Weaknesses:

- Assumes home and away goals are independent
- Often misprices low scores and draws
- Can be slow to adapt if not time-weighted

Recommendation:

- Use as a stepping stone, not final production model.

### 3. Dixon-Coles Model

Use case:

- Football score probabilities
- Draw calibration
- Low-scoring games

Why it matters:

- Dixon-Coles extends the independent Poisson model.
- It corrects low-score probabilities such as 0-0, 1-0, 0-1 and 1-1.
- It also uses time decay so recent matches influence team strengths more than old matches.

Strengths:

- Still explainable
- Better low-score handling than independent Poisson
- Strong benchmark in football betting/modeling literature

Weaknesses:

- Still mostly team-level unless enriched with features
- Needs league-specific calibration
- The rho/low-score correction may differ across leagues, eras and competitions

Recommendation:

- This should be our first production-grade football score model.
- Fit parameters by league where data volume allows.
- Use a global prior for smaller leagues, then league-specific adjustment once enough matches exist.

Sources:

- https://www.research.lancs.ac.uk/portal/en/publications/modelling-association-football-scores-and-inefficiencies-in-the-football-betting-market%28d16276a2-d6e0-483b-a708-1d29663f1992%29.html
- https://arxiv.org/abs/2307.02139

### 4. Bivariate Poisson / Diagonal-Inflated Models

Use case:

- Modelling correlation between team scores
- Better draw modelling
- Alternative to Dixon-Coles

Strengths:

- More directly models score dependence
- Can improve draw probabilities

Weaknesses:

- More complex to fit
- May not outperform Dixon-Coles enough to justify starting there

Recommendation:

- Add as a challenger model after Dixon-Coles.

### 5. Bayesian Hierarchical Dynamic Models

Use case:

- Many leagues/countries
- Small leagues with sparse data
- New seasons
- Promoted teams
- Cross-country generalization

Strengths:

- Shares information across leagues, teams and seasons
- Handles uncertainty explicitly
- Better early-season predictions
- Suitable for Asia/Europe/multi-country scaling

Weaknesses:

- More implementation complexity
- Requires careful priors and diagnostics
- Slower to train

Recommendation:

- Phase two/foundation upgrade.
- Use Bayesian priors for team attack, defence, home advantage and league scoring environment.
- Let smaller leagues borrow strength from similar leagues instead of fitting unstable local-only models.

### 6. Dolores-Style Dynamic Ratings + Bayesian Network

Use case:

- Multi-country, multi-league prediction
- Missing or uneven data
- Generalization across countries

Why it matters:

The Dolores model was built for predicting football outcomes across many countries and leagues. It combines dynamic ratings with Hybrid Bayesian Networks and showed that a model can learn useful information from leagues that the target teams did not participate in.

This is highly relevant to our scalability requirement because we want Asia, Europe and other regions to use the same architecture.

Recommendation:

- Borrow the idea, not necessarily the exact model.
- Use dynamic ratings globally, league/country priors and Bayesian/contextual features.

Source: https://link.springer.com/article/10.1007/s10994-018-5703-7

### 7. Player-Rating Models

Use case:

- Stronger team strength estimates
- Lineup-aware forecasting
- Injury/suspension handling

Strengths:

- Captures that teams are not fixed objects; lineups change.
- Useful for clubs with major squad rotation.
- Can improve pre-match predictions when lineups or probable lineups are available.

Weaknesses:

- Needs reliable player data.
- Free player data is harder to source consistently across leagues.
- Lineups often arrive late.

Recommendation:

- Do not block MVP on this.
- Add later for high-data leagues.

Source: https://www.sciencedirect.com/science/article/pii/S016920702300033X

### 8. xG-Based Models

Use case:

- Faster signal than raw goals
- Better measure of underlying chance creation and prevention
- Mid-season form analysis

Strengths:

- Reduces noise from finishing luck.
- Better than raw goals for assessing team performance in small samples.
- Sumpter's public course material notes that xG-based models may be preferable during a season.

Weaknesses:

- Free xG coverage is inconsistent.
- Different providers calculate xG differently.
- Historical xG for many Asian and lower-tier European leagues may be unavailable.

Recommendation:

- Use xG where reliable, but design the core model to work without it.
- Add xG as a feature, not a hard dependency.

### 9. Gradient Boosted Trees / ML Ensemble

Use case:

- Combining many features
- Capturing nonlinear effects
- Model stacking

Good features:

- Elo difference
- Expected goals from Dixon-Coles
- Home advantage
- Team attack/defence ratings
- Rest days
- Travel distance
- Recent schedule congestion
- League strength
- Market-implied probabilities
- xG rolling averages
- Player availability

Strengths:

- Often strong predictive performance
- Handles interactions between features

Weaknesses:

- Less interpretable
- Easy to leak future data
- Needs calibration
- Can overfit small leagues

Recommendation:

- Use ML as a second-layer model after the statistical model is stable.
- Always calibrate outputs using isotonic regression, Platt scaling, temperature scaling or Bayesian calibration.

Source: https://pmc.ncbi.nlm.nih.gov/articles/PMC10101499/

### 10. Market-Calibrated Models

Use case:

- Benchmarking
- Probability calibration
- Identifying where our model disagrees with the market

Strengths:

- Betting markets are very strong aggregate predictors.
- Closing odds are usually the hardest benchmark.
- Market probabilities help detect model overconfidence.

Weaknesses:

- If the model relies too heavily on market odds, it becomes less independent.
- Opening odds and closing odds have different meanings.
- Odds include bookmaker margin.

Recommendation:

- Use closing odds as a benchmark.
- Use opening odds or market-implied probabilities as optional features only if the product allows it.
- Always strip bookmaker margin before comparison.

Recent research on in-play forecasting found market calibration to be a dominant driver of predictive accuracy in continuous-time scoring models.

Source: https://arxiv.org/abs/2605.16066

## Recommended "Best" Model Architecture

For our project, the best architecture is:

```text
1. Global data layer
   - sport
   - country
   - competition
   - season
   - team
   - fixture
   - result
   - provider mappings

2. Team strength layer
   - global Elo
   - league-adjusted Elo
   - attack rating
   - defence rating
   - home advantage
   - league strength

3. Football scoring layer
   - Dixon-Coles as production baseline
   - bivariate/diagonal-inflated model as challenger
   - Bayesian hierarchical version for multi-league scaling

4. Feature layer
   - form
   - rest days
   - travel
   - promoted/relegated status
   - xG where reliable
   - player availability where reliable
   - odds-implied probabilities where allowed

5. Calibration layer
   - log loss optimization
   - Brier score
   - calibration curves
   - league-specific probability shrinkage

6. Ensemble layer
   - statistical model probability
   - Elo probability
   - ML residual model
   - market benchmark
```

## Model Ranking For Accurate Probabilities

For football specifically:

1. Market-calibrated hierarchical Dixon-Coles / bivariate Poisson ensemble
2. Bayesian hierarchical Dixon-Coles with dynamic attack/defence ratings
3. Dixon-Coles with time decay and league-specific calibration
4. Independent Poisson attack/defence model
5. Elo + multinomial logistic calibration
6. Simple rolling-form or league-table models

For scalable league sports generally:

1. Sport-specific scoring model + dynamic ratings + calibration
2. Bayesian hierarchical ratings shared across countries/leagues
3. ML ensemble on top of statistical model outputs
4. Pure Elo baseline
5. Generic classifier without sport-specific scoring assumptions

## What I Would Build Next

### MVP

Build:

- Elo baseline
- Football Dixon-Coles score model
- Time-decay weighting
- League-specific home advantage
- League-specific draw/low-score calibration
- Backtest against Football-Data.co.uk closing odds

### Upgrade

Add:

- Bayesian hierarchical priors across countries and leagues
- ClubElo as external benchmark
- xG features for leagues where data is reliable
- ML ensemble layer
- Market-calibrated probability correction

### Research Experiments

Run challenger models:

- Bivariate Poisson
- Diagonal-inflated bivariate Poisson
- Negative binomial / overdispersed goals
- Multinomial-Dirichlet outcome model
- Player-rating model
- Gradient boosted trees using statistical-model outputs as features

## Evaluation Rules

Use these rules or the project will fool itself:

- Use time-based splits only.
- Never calculate rolling features using future matches.
- Evaluate by league, season and probability bucket.
- Prefer log loss and Brier score over accuracy.
- Check calibration curves.
- Compare against bookmaker implied probabilities after removing margin.
- Track closing-line performance separately from opening-line performance.
- Require a minimum sample size before trusting league-level conclusions.

## Practical Conclusion

The best model for this project should be:

```text
Elo and dynamic ratings for broad strength
+ Dixon-Coles for football score probabilities
+ Bayesian hierarchical priors for multi-league scaling
+ xG/player/context features where available
+ calibration against historical results and market odds
+ ML ensemble only after the statistical foundation is working
```

This fits Sumpter's core lesson: football is deeply probabilistic. We should not try to predict certainty. We should build the most honest probability engine we can, then measure whether those probabilities are calibrated.

## Sources

- Soccermatics prediction lesson: https://soccermatics.readthedocs.io/en/latest/lesson5/Prediction.html
- Dixon & Coles paper page: https://www.research.lancs.ac.uk/portal/en/publications/modelling-association-football-scores-and-inefficiencies-in-the-football-betting-market%28d16276a2-d6e0-483b-a708-1d29663f1992%29.html
- Dolores multi-country model: https://link.springer.com/article/10.1007/s10994-018-5703-7
- Player-rating forecasting model: https://www.sciencedirect.com/science/article/pii/S016920702300033X
- Comparing probabilistic predictive models: https://arxiv.org/abs/1705.04356
- Extending Dixon-Coles: https://arxiv.org/abs/2307.02139
- Dixon-Coles time weighting discussion: https://opisthokonta.net/?cat=48
- Market-calibrated in-play forecasting: https://arxiv.org/abs/2605.16066
